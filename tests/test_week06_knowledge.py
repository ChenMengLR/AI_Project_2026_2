"""Week 6 checks for real context, clause retrieval, and safe abstention."""
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
DORM = ROOT / "week03_dorm_assistant"
WEEK6 = ROOT / "week06_knowledge_qa"

core_spec = importlib.util.spec_from_file_location("week06_test_core", DORM / "core.py")
core = importlib.util.module_from_spec(core_spec)
core_spec.loader.exec_module(core)
with patch.dict(sys.modules, {"core": core}):
    conv_spec = importlib.util.spec_from_file_location("week06_test_conversation", DORM / "conversation.py")
    conversation = importlib.util.module_from_spec(conv_spec)
    conv_spec.loader.exec_module(conversation)
personal_spec = importlib.util.spec_from_file_location("week06_personal", WEEK6 / "app.py")
personal = importlib.util.module_from_spec(personal_spec)
personal_spec.loader.exec_module(personal)


def fake_client(*results):
    values = iter(results)
    def create(**_):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=json.dumps(next(values))))])
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))


class GroupRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = core.catalog()

    def test_prohibited_item_retrieval_includes_health_condition(self):
        hits = conversation.retrieve("可以带电热水壶吗？", [], self.data)
        self.assertEqual(hits[0]["item_id"], "PROHIBITED_ITEMS")
        self.assertIn("HEALTH_ITEM_INQUIRY", [h["item_id"] for h in hits])
        self.assertTrue(all(h["url"].startswith("https://") for h in hits))

    def test_mixed_question_keeps_both_linked_conditions(self):
        hits = conversation.retrieve("电热水壶 结核 出入证", [], self.data)
        ids = {hit["item_id"] for hit in hits}
        self.assertIn("PROHIBITED_ITEMS", ids)
        self.assertIn("HEALTH_ITEM_INQUIRY", ids)
        self.assertIn("DOC_TB", ids)
        self.assertIn("DOC_RECENCY", ids)

    def test_followup_uses_prior_citation_and_real_source(self):
        history = [{"question": "可以带电热水壶吗？", "evidence_ids": ["PROHIBITED_ITEMS"]}]
        client = fake_client(
            {"standalone_question": "冰箱可以带入宿舍吗？", "keywords_ko": ["냉장고", "반입"]},
            {"answered": True, "answer": "可以带。", "evidence_ids": ["PROHIBITED_ITEMS"]})
        result = conversation.answer({"question": "那冰箱呢？", "history": history}, self.data, client)
        self.assertEqual(result["standalone_question"], "冰箱可以带入宿舍吗？")
        self.assertIn("冰箱", result["answer"])
        self.assertIn("行政支援室", result["answer"])
        self.assertNotIn("可以带。", result["answer"])
        self.assertEqual(result["history_used"], 1)
        self.assertTrue(all(e["url"].startswith("https://") for e in result["evidence"]))

    def test_unrelated_question_abstains_before_model_call(self):
        client = fake_client({"standalone_question": "奖学金申请日期是什么？", "keywords_ko": ["장학금", "신청 기간"]})
        result = conversation.answer({"question": "奖学金申请日期是什么？"}, self.data, client)
        self.assertFalse(result["answered"])
        self.assertEqual(result["failure_stage"], "retrieval")
        self.assertEqual(result["evidence"], [])

    def test_chinese_question_keeps_chinese_standalone_when_model_translates_it(self):
        client = fake_client({"standalone_question": "전기포트를 가져갈 수 있나요?", "keywords_ko": ["전기포트", "반입"]})
        standalone, keywords, mode = conversation.rewrite("可以带电热水壶吗？", [], self.data, "zh", client)
        self.assertEqual(standalone, "可以带电热水壶吗？")
        self.assertEqual(keywords, ["전기포트", "반입"])
        self.assertEqual(mode, "model")

    def test_access_card_answer_keeps_both_sources(self):
        client = fake_client(
            {"standalone_question": "入住时在哪里领取出入证？", "keywords_ko": ["입사", "출입증"]},
            {"answered": True, "answer": "入住时领取出入证。", "evidence_ids": ["ACCESS_CARD"]})
        result = conversation.answer({"question": "入住时在哪里领取出入证？"}, self.data, client)
        self.assertTrue(result["answered"])
        self.assertEqual({entry["source_id"] for entry in result["evidence"]},
                         {"HANLIM_RULES_DMS", "HANLIM_MOVEIN"})

    def test_history_limits_and_unknown_source_rejected(self):
        with self.assertRaises(core.InputError):
            conversation.clean_history([{"question": "a", "evidence_ids": ["invented"]}], self.data)
        with self.assertRaises(core.InputError):
            conversation.clean_history([{"question": "a", "evidence_ids": []}] * 4, self.data)


class PersonalRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs = personal.parse_documents()

    def test_three_documents_have_clause_level_sources(self):
        self.assertEqual({d["file"] for d in self.docs}, {"rules.txt", "life_guide.txt", "notice_printer.txt"})
        self.assertGreaterEqual(len(self.docs), 20)
        self.assertTrue(all(d["urls"] and d["clause"] and d["checked_date"] for d in self.docs))

    def test_rules_clause_urls_are_not_file_wide_union(self):
        simple = next(d for d in self.docs if d["clause"] == "제13조 출입시간")
        mixed = next(d for d in self.docs if "반입금지 물품" in d["clause"])
        self.assertEqual(len(simple["urls"]), 1)
        self.assertEqual(len(mixed["urls"]), 2)

    def test_kettle_and_printer_retrieve_matching_documents(self):
        kettle = personal.search("可以带烧水的机器吗？", ["전기포트", "반입"], self.docs)
        self.assertIn("반입금지", kettle[0]["clause"])
        printer = personal.search("승학1관 프린터는 어디에 있나요?", ["승학1관", "프린터"], self.docs)
        self.assertEqual(printer[0]["file"], "notice_printer.txt")

    def test_scholarship_is_retrieval_failure(self):
        self.assertEqual(personal.search("奖学金何时申请？", ["장학금", "신청 시기", "신청 기간"], self.docs), [])

    def test_answer_guard_preserves_health_exception(self):
        client = fake_client(
            {"standalone_question": "전기포트를 가져갈 수 있나요?", "keywords_ko": ["전기포트", "반입"]},
            {"answered": True, "answer": "전기포트는 반입할 수 없습니다.", "citations": ["S1"]})
        result = personal.answer("전기포트를 가져갈 수 있나요?", [], self.docs, client, "fake")
        self.assertTrue(result["answer_guard_applied"])
        self.assertIn("행정지원실", result["answer"])
        self.assertEqual(result["raw_model_answer"], "전기포트는 반입할 수 없습니다.")

    def test_answer_guard_rejects_model_permission_with_valid_banned_citation(self):
        client = fake_client(
            {"standalone_question": "电饭锅可以带吗？", "keywords_ko": ["전기밥솥", "반입"]},
            {"answered": True, "answer": "可以带。", "citations": ["S1"]})
        result = personal.answer("电饭锅可以带吗？", [], self.docs, client, "fake")
        self.assertEqual(result["raw_model_answer"], "可以带。")
        self.assertTrue(result["answer_guard_applied"])
        self.assertIn("禁带、禁用", result["answer"])
        self.assertIn("行政支援室", result["answer"])


if __name__ == "__main__":
    unittest.main()
