"""Safety and data-flow checks for the Week 7 AI notice prototype."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "week03_dorm_assistant"))
sys.path.insert(0, str(ROOT))
from week07_notice_interpreter import notice  # noqa: E402

TEXT = ("2026년 11월 입사 예정자는 10월 28일까지 결핵검진 확인서를 제출하세요. "
        "단, 유학생은 제출 서류 종류를 별도 안내에서 확인하세요.")
ACTION = {"action_zh": "提交结核检查证明", "action_ko": "결핵검진 확인서를 제출하세요",
          "source_quote": TEXT,
          "audience_quote": "2026년 11월 입사 예정자", "deadline_quote": "10월 28일까지",
          "exception_quote": "유학생은 제출 서류 종류를 별도 안내에서 확인하세요",
          "catalog_item_id": "DOC_TB"}


class NoticeTests(unittest.TestCase):
    def test_extracts_new_notice_without_sending_personal_status_to_ai(self):
        states = {"DOC_TB": "missing"}
        payload = {"notice_text": TEXT, "source_url": "https://hanlim.donga.ac.kr/example",
                   "profile": "international", "states": states}
        original = deepcopy(payload)
        seen = {}

        def model(prompt, content, **kwargs):
            seen.update(content)
            return {"actions": [ACTION]}

        with patch.object(notice.core, "ask_json", side_effect=model):
            result = notice.interpret_notice(payload)
        self.assertEqual(payload, original)
        self.assertNotIn("profile", seen)
        self.assertNotIn("states", seen)
        self.assertNotIn("source_url", seen)
        self.assertEqual(result["actions"][0]["current_state"], "missing")
        self.assertEqual(result["actions"][0]["catalog_item_id"], "DOC_TB")
        self.assertTrue(result["actions"][0]["catalog_match_unverified"])
        self.assertTrue(result["review_required"])
        self.assertFalse(result["source_url_verified"])

    def test_rejects_model_quote_not_in_pasted_notice(self):
        fabricated = {**ACTION, "deadline_quote": "10월 21일까지"}
        with patch.object(notice.core, "ask_json", return_value={"actions": [fabricated]}):
            with self.assertRaises(notice.core.AIError):
                notice.interpret_notice({"notice_text": TEXT})

    def test_rejects_condition_from_a_different_source_span(self):
        mismatched = {**ACTION, "source_quote": "2026년 11월 입사 예정자는 10월 28일까지 결핵검진 확인서를 제출하세요"}
        with patch.object(notice.core, "ask_json", return_value={"actions": [mismatched]}):
            with self.assertRaises(notice.core.AIError):
                notice.interpret_notice({"notice_text": TEXT})

    def test_rejects_unknown_catalog_item(self):
        fabricated = {**ACTION, "catalog_item_id": "SCHOLARSHIP"}
        with patch.object(notice.core, "ask_json", return_value={"actions": [fabricated]}):
            with self.assertRaises(notice.core.AIError):
                notice.interpret_notice({"notice_text": TEXT})

    def test_new_item_keeps_original_checklist_unchanged(self):
        action = {**ACTION, "catalog_item_id": None}
        states = {"DOC_TB": "ready"}
        with patch.object(notice.core, "ask_json", return_value={"actions": [action]}):
            result = notice.interpret_notice({"notice_text": TEXT, "states": states})
        self.assertIsNone(result["actions"][0]["current_state"])
        self.assertEqual(states, {"DOC_TB": "ready"})

    def test_rejects_non_https_link_and_invalid_status(self):
        with self.assertRaises(notice.core.InputError):
            notice.interpret_notice({"notice_text": TEXT, "source_url": "http://example.com"})
        with self.assertRaises(notice.core.InputError):
            notice.interpret_notice({"notice_text": TEXT, "states": {"DOC_TB": []}})

    def test_warns_when_model_omits_non_repeat_exception(self):
        blind = (ROOT / "week07_notice_interpreter" / "blind_sample.txt").read_text(encoding="utf-8")
        action = {"action_zh": "完成 QR 登记", "action_ko": "QR 출입 등록을 완료하세요",
                  "source_quote": "2026년 11월 동관 입사 예정자 중 아직 모바일 출입 등록을 하지 않은 학생은 10월 30일 18시까지 생활관 포털에서 QR 출입 등록을 완료하세요. 서관 입사 예정자는 이번 등록 대상이 아닙니다.",
                  "audience_quote": "2026년 11월 동관 입사 예정자 중 아직 모바일 출입 등록을 하지 않은 학생",
                  "deadline_quote": "10월 30일 18시까지",
                  "exception_quote": "서관 입사 예정자는 이번 등록 대상이 아닙니다.",
                  "catalog_item_id": None}
        with patch.object(notice.core, "ask_json", return_value={"actions": [action]}):
            result = notice.interpret_notice({"notice_text": blind})
        self.assertEqual(len(result["uncovered_caveats"]), 1)
        self.assertIn("다시 신청할 필요가 없습니다", result["uncovered_caveats"][0])

    def test_labels_no_repeat_statement_as_exception_note(self):
        blind = (ROOT / "week07_notice_interpreter" / "blind_sample.txt").read_text(encoding="utf-8")
        note = {"action_zh": "已完成登记无需再次申请", "action_ko": "등록을 완료한 학생은 다시 신청할 필요가 없습니다",
                "source_quote": "등록을 완료한 학생은 다시 신청할 필요가 없습니다.",
                "audience_quote": "등록을 완료한 학생", "deadline_quote": "", "exception_quote": "",
                "catalog_item_id": None}
        with patch.object(notice.core, "ask_json", return_value={"actions": [note]}):
            result = notice.interpret_notice({"notice_text": blind})
        self.assertEqual(result["actions"][0]["kind"], "exception_note")


if __name__ == "__main__":
    unittest.main()
