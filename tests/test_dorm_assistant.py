"""Critical behavior checks: applicability, dates, AI output validation, HTTP boundaries."""
import importlib.util
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "week03_dorm_assistant"
spec = importlib.util.spec_from_file_location("dorm_core", APP / "core.py")
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


def fake_client(response):
    def create(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=json.dumps(response)))])
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))


class PreparationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = core.catalog()

    def payload(self, **extra):
        return {"profile": "standard", "move_in_date": "2026-11-01", "states": {}, "dates": {}, **extra}

    def result_item(self, payload, item_id="DOC_TB"):
        return next(x for x in core.check(payload, self.data, today=core.date(2026, 10, 31))["items"] if x["id"] == item_id)

    def test_sources_are_traceable(self):
        sources = {s["id"]: s for s in self.data["sources"]}
        ids = [x["id"] for x in self.data["items"]]
        self.assertEqual(len(ids), len(set(ids)))
        for item in self.data["items"]:
            self.assertIn(item["source_id"], sources)
            self.assertTrue(item["quote"].strip())
            self.assertEqual(item["source_url"], sources[item["source_id"]]["url"])

    def test_korean_catalog_is_complete(self):
        self.assertTrue(self.data["disclaimer_ko"])
        self.assertTrue(self.data["scope_ko"])
        for source in self.data["sources"]:
            self.assertTrue(source["title_ko"])
            self.assertTrue(source["scope_ko"])
        for item in self.data["items"]:
            self.assertTrue(item["title_ko"])
            self.assertTrue(item["description_ko"])
            self.assertTrue(item["conditions"]["notes_ko"])

    def test_default_is_not_success(self):
        report = core.check({}, self.data)
        self.assertEqual(report["overall"], "scope_unconfirmed")
        self.assertGreater(report["summary"]["unknown"], 0)

    def test_international_ready_still_needs_scope_confirmation(self):
        payload = self.payload(profile="international", states={"DOC_TB": "ready"}, dates={"DOC_TB": "2026-10-01"})
        self.assertEqual(self.result_item(payload)["status"], "confirm")

    def test_unknown_identity_never_clears_documents(self):
        self.assertEqual(self.result_item(self.payload(profile="unknown", states={"DOC_ADDRESS": "ready"}), "DOC_ADDRESS")["status"], "confirm")

    def test_recent_document(self):
        self.assertEqual(self.result_item(self.payload(states={"DOC_TB": "ready"}, dates={"DOC_TB": "2026-10-01"}))["status"], "ready")

    def test_calendar_month_boundary(self):
        self.assertEqual(core.months_before(core.date(2026, 5, 31), 3).isoformat(), "2026-02-28")
        self.assertEqual(core.months_before(core.date(2024, 5, 31), 3).isoformat(), "2024-02-29")
        self.assertEqual(self.result_item(self.payload(states={"DOC_TB": "ready"}, dates={"DOC_TB": "2026-08-01"}))["status"], "ready")

    def test_expired_document(self):
        self.assertEqual(self.result_item(self.payload(states={"DOC_TB": "ready"}, dates={"DOC_TB": "2026-07-31"}))["status"], "invalid_date")

    def test_issue_after_move_in(self):
        self.assertEqual(self.result_item(self.payload(states={"DOC_TB": "ready"}, dates={"DOC_TB": "2026-12-01"}))["status"], "invalid_date")

    def test_future_issue_date_never_counts_as_already_ready(self):
        result = core.check(self.payload(states={"DOC_TB": "ready"}, dates={"DOC_TB": "2026-10-01"}), self.data, today=core.date(2026, 9, 30))
        self.assertEqual(next(x for x in result["items"] if x["id"] == "DOC_TB")["status"], "invalid_date")

    def test_missing_issue_date(self):
        self.assertEqual(self.result_item(self.payload(states={"DOC_TB": "ready"}))["status"], "confirm")

    def test_missing_move_in_date(self):
        self.assertEqual(self.result_item(self.payload(move_in_date="", states={"DOC_TB": "ready"}, dates={"DOC_TB": "2026-10-01"}))["status"], "confirm")

    def test_missing_remains_missing(self):
        self.assertEqual(self.result_item(self.payload(states={"DOC_TB": "missing"}))["status"], "missing")

    def test_supplies_can_be_ready_for_international(self):
        self.assertEqual(self.result_item(self.payload(profile="international", states={"SUPPLY_BEDDING": "ready"}), "SUPPLY_BEDDING")["status"], "ready")

    def test_reference_items_excluded_from_completion(self):
        report = core.check(self.payload(), self.data)
        self.assertEqual(report["summary"]["total"], sum(bool(x.get("checkable", True)) for x in self.data["items"]))
        self.assertEqual(self.result_item(self.payload(), "HEALTH_ITEM_INQUIRY")["status"], "reference")

    def test_standard_recommendations_prioritize_unfinished_before_move_in(self):
        states = {"DOC_TB": "ready", "DOC_ADDRESS": "ready", "NOTICE_REVIEW": "ready",
                  "SUPPLY_HYGIENE": "ready", "SUPPLY_BEDDING": "missing",
                  "SUPPLY_LAUNDRY": "missing", "SUPPLY_NETWORK": "unknown"}
        dates = {"DOC_TB": "2026-09-30", "DOC_ADDRESS": "2026-09-30"}
        result = core.check(self.payload(states=states, dates=dates), self.data, today=core.date(2026, 10, 8))
        self.assertEqual([x["id"] for x in result["recommendations"]],
                         ["SUPPLY_BEDDING", "SUPPLY_LAUNDRY", "SUPPLY_NETWORK"])
        self.assertTrue(all(x["source"]["url"].startswith("https://") for x in result["recommendations"]))

    def test_international_recommendations_preserve_scope_confirmation(self):
        states = {"DOC_TB": "ready", "DOC_ADDRESS": "ready", "NOTICE_REVIEW": "missing",
                  "SUPPLY_HYGIENE": "ready", "SUPPLY_BEDDING": "ready",
                  "SUPPLY_LAUNDRY": "ready", "SUPPLY_NETWORK": "ready"}
        dates = {"DOC_TB": "2026-09-30", "DOC_ADDRESS": "2026-09-30"}
        result = core.check(self.payload(profile="international", states=states, dates=dates,
                                         language="ko"), self.data, today=core.date(2026, 10, 8))
        self.assertEqual([x["id"] for x in result["recommendations"]],
                         ["DOC_TB", "DOC_ADDRESS", "NOTICE_REVIEW"])
        self.assertEqual([x["status"] for x in result["recommendations"]],
                         ["confirm", "confirm", "missing"])
        self.assertTrue(all("생활관" in x["next_action"] or "원문" in x["next_action"]
                            for x in result["recommendations"]))
        self.assertEqual(result["overall"], "scope_unconfirmed")

    def test_korean_check_localizes_all_explanations(self):
        report = core.check(self.payload(language="ko"), self.data, today=core.date(2026, 10, 8))
        self.assertTrue(all(any("가" <= c <= "힣" for c in text)
                            for item in report["items"] for text in (item["message"], item["next_action"])))
        self.assertTrue(all(any("가" <= c <= "힣" for c in text)
                            for row in report["recommendations"] for text in (row["reason"], row["next_action"])))
        self.assertIn("공식", report["notice"])
        self.assertEqual(report["recommendations"][0]["source"]["title"],
                         report["recommendations"][0]["source"]["title_ko"])

    def test_no_candidates_has_explicit_fallback(self):
        states = {x["id"]: "ready" for x in self.data["items"] if x.get("checkable", True)}
        dates = {"DOC_TB": "2026-09-30", "DOC_ADDRESS": "2026-09-30"}
        report = core.check(self.payload(move_in_date="2026-10-01", states=states,
                                         dates=dates, language="ko"), self.data, today=core.date(2026, 10, 8))
        self.assertEqual(report["recommendations"], [])
        self.assertIn("추천할", report["recommendation_notice"])

    def test_invalid_date_is_recommended_for_review(self):
        states = {x["id"]: "ready" for x in self.data["items"] if x.get("checkable", True)}
        dates = {"DOC_TB": "2026-07-31", "DOC_ADDRESS": "2026-09-30"}
        report = core.check(self.payload(states=states, dates=dates), self.data, today=core.date(2026, 10, 8))
        self.assertEqual(report["recommendations"][0]["id"], "DOC_TB")
        self.assertEqual(report["recommendations"][0]["status"], "invalid_date")
        self.assertNotIn("HEALTH_ITEM_INQUIRY", [x["id"] for x in report["recommendations"]])

    def test_invalid_inputs(self):
        for payload in ([], {"profile": []}, {"profile": "all"}, {"states": []},
                        {"states": {"NOT_AN_ITEM": "ready"}}, {"states": {"DOC_TB": "maybe"}},
                        {"dates": {"SUPPLY_BEDDING": "2026-01-01"}}, {"move_in_date": "2026-02-30"},
                        {"move_in_date": "0001-01-01"}, {"dates": {"DOC_TB": "garbage"}}):
            with self.subTest(payload=payload), self.assertRaises(core.InputError):
                core.check(payload, self.data)
        with self.assertRaises(core.InputError):
            core.check(self.payload(language="en"), self.data)


class AIValidationTests(unittest.TestCase):
    def test_korean_interpret_notice_and_reason(self):
        result = core.interpret({"text": "침구류는 아직 준비하지 않았어요", "language": "ko"},
                                client=fake_client({"suggestions": [
                                    {"item_id": "SUPPLY_BEDDING", "state": "missing", "reason": "用户未准备"}]}))
        self.assertIn("확인", result["notices"][0])
        self.assertIn("미준비", result["suggestions"][0]["reason"])

    def test_korean_ask_uses_reviewed_catalog_text_and_caveat(self):
        result = core.ask({"question": "결핵검진 확인서가 필요한가요?", "language": "ko"},
                          client=fake_client({"answered": True, "answer": "中文模型回答", "evidence_ids": ["DOC_TB"]}))
        self.assertIn("3개월", result["answer"])
        self.assertNotIn("中文模型回答", result["answer"])
        self.assertIn("DOC_RECENCY", [x["item_id"] for x in result["evidence"]])
        self.assertEqual(result["evidence"][0]["title"], "결핵검진 확인서")

    def test_korean_refusal(self):
        result = core.ask({"question": "여권으로 대신할 수 있나요?", "language": "ko"},
                          client=fake_client({"answered": False, "answer": "모름", "evidence_ids": []}))
        self.assertFalse(result["answered"])
        self.assertIn("확인할 수 없습니다", result["answer"])
    def test_ambiguous_suggestion_stays_unknown(self):
        result = core.interpret({"text": "床单好像准备了，不确定"}, client=fake_client({"suggestions": [
            {"item_id": "SUPPLY_BEDDING", "state": "unknown", "reason": "用户不确定"}]}))
        self.assertEqual(result["suggestions"][0]["state"], "unknown")

    def test_unknown_suggestion_rejected(self):
        with self.assertRaises(core.AIError):
            core.interpret({"text": "所有项目好了"}, client=fake_client({"suggestions": [{"item_id": "INVENTED", "state": "ready"}]}))

    def test_invalid_state_rejected(self):
        with self.assertRaises(core.AIError):
            core.interpret({"text": "床单好了"}, client=fake_client({"suggestions": [{"item_id": "SUPPLY_BEDDING", "state": "approved"}]}))

    def test_duplicate_suggestion_rejected(self):
        row = {"item_id": "SUPPLY_BEDDING", "state": "ready", "reason": "有床单"}
        with self.assertRaises(core.AIError):
            core.interpret({"text": "床单好了"}, client=fake_client({"suggestions": [row, row]}))

    def test_empty_and_long_input_rejected(self):
        for payload in ({"text": " "}, {"text": "a" * 2001}):
            with self.assertRaises(core.InputError):
                core.interpret(payload, client=fake_client({}))

    def test_answer_quotes_taken_from_catalog_not_model(self):
        result = core.ask({"question": "准备什么床上用品"}, client=fake_client({"answered": True, "answer": "准备床上用品。", "evidence_ids": ["SUPPLY_BEDDING"], "quote": "fake"}))
        self.assertEqual(result["evidence"][0]["quote"], next(x["quote"] for x in core.catalog()["items"] if x["id"] == "SUPPLY_BEDDING"))

    def test_no_evidence_means_no_claim(self):
        result = core.ask({"question": "打印机位置"}, client=fake_client({"answered": True, "answer": "在一楼", "evidence_ids": []}))
        self.assertFalse(result["answered"])
        self.assertNotIn("一楼", result["answer"])

    def test_unknown_reference_rejected(self):
        with self.assertRaises(core.AIError):
            core.ask({"question": "在哪里"}, client=fake_client({"answered": True, "answer": "门口", "evidence_ids": ["FAKE"]}))

    def test_prohibited_items_keep_health_inquiry_condition(self):
        result = core.ask({"question": "电热毯能带吗"}, client=fake_client({"answered": True, "answer": "不能带。", "evidence_ids": ["PROHIBITED_ITEMS"]}))
        self.assertIn("HEALTH_ITEM_INQUIRY", [e["item_id"] for e in result["evidence"]])
        self.assertIn("行政支援室", result["answer"])

    def test_document_answer_keeps_date_condition(self):
        result = core.ask({"question": "要什么材料"}, client=fake_client({"answered": True, "answer": "结核检查证明。", "evidence_ids": ["DOC_TB"]}))
        self.assertIn("DOC_RECENCY", [e["item_id"] for e in result["evidence"]])

    def test_receiving_access_card_keeps_both_sources(self):
        result = core.ask({"question": "怎么领出入证"}, client=fake_client({"answered": True, "answer": "入住时领取。", "evidence_ids": ["ACCESS_CARD"]}))
        self.assertEqual({e["source_id"] for e in result["evidence"]}, {"HANLIM_MOVEIN", "HANLIM_RULES_DMS"})

    def test_out_of_scope_refusal(self):
        result = core.ask({"question": "能用护照替代吗"}, client=fake_client({"answered": False, "answer": "无法确认", "evidence_ids": []}))
        self.assertFalse(result["answered"])

    def test_provider_error_does_not_leak(self):
        def fail(**kwargs):
            raise RuntimeError("SECRET_MUST_NOT_LEAK")
        client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=fail)))
        with self.assertRaises(core.AIError) as caught:
            core.ask({"question": "床上用品"}, client=client)
        self.assertNotIn("SECRET_MUST_NOT_LEAK", str(caught.exception))


class ClassroomRecommendationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("week05_classroom", ROOT / "week05_recommendation" / "app.py")
        cls.app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.app)

    def test_expected_scenarios_are_distinct(self):
        self.assertEqual(self.app.expected_ids(self.app.SCENARIOS["A"]), ["C1", "C3"])
        self.assertEqual(self.app.expected_ids(self.app.SCENARIOS["B"]), ["C4"])
        self.assertEqual(self.app.expected_ids(self.app.SCENARIOS["C"]), [])

    def test_rule_result_covers_every_candidate_once_with_bilingual_reasons(self):
        for name, profile in self.app.SCENARIOS.items():
            with self.subTest(scenario=name):
                result = self.app.rule_result(profile)
                self.assertEqual(self.app.validate_result(profile, result), [])
                self.assertEqual(len(result["recommendations"] + result["excluded"]), 4)

    def test_validator_rejects_wrong_model_recommendation_and_duplicate(self):
        profile = self.app.SCENARIOS["A"]
        wrong = self.app.rule_result(profile)
        wrong["recommendations"].append(wrong["excluded"].pop())
        self.assertTrue(self.app.validate_result(profile, wrong))
        duplicate = self.app.rule_result(profile)
        duplicate["excluded"][0]["id"] = "C1"
        self.assertTrue(self.app.validate_result(profile, duplicate))

    def test_validator_rejects_missing_korean_reason(self):
        profile = self.app.SCENARIOS["B"]
        result = self.app.rule_result(profile)
        result["recommendations"][0]["reason_ko"] = ""
        self.assertTrue(any("reason_ko" in issue for issue in self.app.validate_result(profile, result)))

    def test_all_failed_criteria_and_numbers_appear_in_audited_reasons(self):
        profile = self.app.SCENARIOS["B"]
        result = self.app.rule_result(profile)
        by_id = {row["id"]: row for row in result["recommendations"] + result["excluded"]}
        for item_id in ("C1", "C2", "C3"):
            self.assertEqual(by_id[item_id]["failed_criteria"], ["interest", "level"])
            for field in ("reason_zh", "reason_ko"):
                self.assertIn("Statistics", by_id[item_id][field])
                self.assertIn("intermediate", by_id[item_id][field])
        self.assertIn("60", by_id["C4"]["reason_zh"])
        self.assertIn("90", by_id["C4"]["reason_ko"])

    def test_validator_rejects_incomplete_failure_list(self):
        profile = self.app.SCENARIOS["B"]
        result = self.app.rule_result(profile)
        row = next(row for row in result["excluded"] if row["id"] == "C1")
        row["failed_criteria"] = ["level"]
        self.assertTrue(any("C1" in issue for issue in self.app.validate_result(profile, result)))

    def test_canonicalization_replaces_incomplete_model_reason(self):
        profile = self.app.SCENARIOS["B"]
        raw = self.app.rule_result(profile)
        row = next(row for row in raw["excluded"] if row["id"] == "C1")
        row["reason_zh"], row["reason_ko"] = "级别不匹配", "수준 불일치"
        self.assertTrue(any("C1" in issue for issue in self.app.audit_raw_reasons(profile, raw)))
        audited = self.app.canonicalize_result(profile, raw)
        corrected = next(row for row in audited["excluded"] if row["id"] == "C1")
        self.assertIn("AI", corrected["reason_zh"])
        self.assertIn("Statistics", corrected["reason_ko"])
        self.assertIn("beginner", corrected["reason_zh"])
        self.assertEqual(self.app.validate_result(profile, audited), [])

    def test_raw_decisions_can_be_corrected_when_failure_list_is_incomplete(self):
        profile = self.app.SCENARIOS["C"]
        raw = self.app.rule_result(profile)
        raw["excluded"][0]["failed_criteria"] = ["time"]
        self.assertEqual(self.app.validate_result(profile, raw, require_failed_criteria=False), [])
        self.assertTrue(self.app.validate_result(profile, raw))
        corrected = self.app.canonicalize_result(profile, raw)
        self.assertEqual(corrected["excluded"][0]["failed_criteria"], ["interest", "time"])
        self.assertEqual(self.app.validate_result(profile, corrected), [])

    def test_saved_qwen_result_keeps_raw_omission_and_corrects_final_reason(self):
        profile = self.app.SCENARIOS["B"]
        raw = self.app.rule_result(profile)
        row = next(row for row in raw["excluded"] if row["id"] == "C1")
        row["failed_criteria"] = ["level"]
        row["reason_zh"], row["reason_ko"] = "级别不匹配", "수준 불일치"
        with tempfile.TemporaryDirectory() as folder, patch.object(self.app, "BASE", Path(folder)), \
             patch.object(self.app, "qwen_result", return_value=(raw, "fake-model")):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(self.app.main(["--mode", "qwen", "--scenario", "B", "--save-results"]), 0)
            saved = json.loads((Path(folder) / "evidence" / "result_B.json").read_text(encoding="utf-8"))
        self.assertTrue(saved["validated"])
        self.assertTrue(saved["raw_model_criteria_issues"])
        self.assertTrue(saved["raw_model_reason_issues"])
        original = next(row for row in saved["raw_model_result"]["excluded"] if row["id"] == "C1")
        corrected = next(row for row in saved["result"]["excluded"] if row["id"] == "C1")
        self.assertEqual(original["failed_criteria"], ["level"])
        self.assertEqual(corrected["failed_criteria"], ["interest", "level"])
        self.assertIn("Statistics", corrected["reason_ko"])

    def test_course_output_uses_recommendations_and_saves_profile(self):
        profile = self.app.SCENARIOS["A"]
        legacy = self.app.rule_result(profile)
        legacy["recommended"] = legacy.pop("recommendations")
        self.assertTrue(self.app.validate_result(profile, legacy))
        with tempfile.TemporaryDirectory() as folder, patch.object(self.app, "BASE", Path(folder)):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(self.app.main(["--mode", "rules", "--scenario", "A", "--save-results"]), 0)
            saved = json.loads((Path(folder) / "evidence" / "result_A.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["profile"], profile)
        self.assertIn("recommendations", saved["result"])
        self.assertEqual(saved["result"]["recommendations"][0]["id"], "C1")


class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("dorm_server", APP / "app.py")
        cls.app = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"core": core}):
            spec.loader.exec_module(cls.app)
        cls.server = cls.app.make_server(0)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_catalog_available_without_secret(self):
        with urlopen(self.url + "/api/catalog") as res:
            text = res.read().decode()
            self.assertIn("HANLIM", text)
            self.assertNotIn("DASHSCOPE_API_KEY", text)

    def test_check_http(self):
        request = Request(self.url + "/api/check", data=b'{}', headers={"Content-Type": "application/json"})
        with urlopen(request) as res:
            self.assertEqual(json.load(res)["overall"], "scope_unconfirmed")

    def test_korean_check_http(self):
        body = json.dumps({"language": "ko", "profile": "international"}).encode("utf-8")
        request = Request(self.url + "/api/check", data=body, headers={"Content-Type": "application/json"})
        with urlopen(request) as res:
            report = json.load(res)
        self.assertEqual(report["overall"], "scope_unconfirmed")
        self.assertIn("recommendations", report)
        self.assertIn("확인", report["recommendations"][0]["next_action"])

    def test_cross_origin_rejected(self):
        request = Request(self.url + "/api/check", data=b'{}', headers={"Content-Type": "application/json", "Origin": "https://example.org"})
        with self.assertRaises(HTTPError) as caught:
            urlopen(request)
        self.assertEqual(caught.exception.code, 403)
        caught.exception.close()

    def test_private_files_not_served(self):
        for path in ("/.env", "/../.env", "/core.py", "/data/knowledge.json"):
            with self.subTest(path=path), self.assertRaises(HTTPError) as caught:
                urlopen(self.url + path)
            self.assertEqual(caught.exception.code, 404)
            caught.exception.close()


if __name__ == "__main__":
    unittest.main()
