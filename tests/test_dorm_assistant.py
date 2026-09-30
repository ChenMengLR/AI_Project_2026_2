"""Critical behavior checks: applicability, dates, AI output validation, HTTP boundaries."""
import importlib.util
import json
from pathlib import Path
import sys
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

    def test_invalid_inputs(self):
        for payload in ([], {"profile": []}, {"profile": "all"}, {"states": []},
                        {"states": {"NOT_AN_ITEM": "ready"}}, {"states": {"DOC_TB": "maybe"}},
                        {"dates": {"SUPPLY_BEDDING": "2026-01-01"}}, {"move_in_date": "2026-02-30"},
                        {"move_in_date": "0001-01-01"}, {"dates": {"DOC_TB": "garbage"}}):
            with self.subTest(payload=payload), self.assertRaises(core.InputError):
                core.check(payload, self.data)


class AIValidationTests(unittest.TestCase):
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
