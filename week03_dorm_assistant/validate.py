"""Reproducible synthetic scenarios; --live explicitly makes real AI requests."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
import core

BASE = Path(__file__).resolve().parent


def run(live=False):
    data = core.catalog()
    records = []
    scenarios = [
        ("CHECK_NORMAL", {"profile": "standard", "move_in_date": "2026-11-01", "states": {"DOC_TB": "ready", "SUPPLY_BEDDING": "ready"}, "dates": {"DOC_TB": "2026-09-30"}}, "DOC_TB", "ready"),
        ("CHECK_MISSING", {"profile": "standard", "states": {"SUPPLY_BEDDING": "missing"}}, "SUPPLY_BEDDING", "missing"),
        ("CHECK_AMBIGUOUS", {"profile": "standard", "states": {"SUPPLY_BEDDING": "unknown"}}, "SUPPLY_BEDDING", "unknown"),
        ("CHECK_INTERNATIONAL", {"profile": "international", "states": {"DOC_ADDRESS": "ready"}}, "DOC_ADDRESS", "confirm"),
        ("CHECK_OLD_DATE", {"profile": "standard", "move_in_date": "2026-11-01", "states": {"DOC_TB": "ready"}, "dates": {"DOC_TB": "2026-07-01"}}, "DOC_TB", "invalid_date"),
        ("CHECK_MISSING_DATE", {"profile": "standard", "states": {"DOC_TB": "ready"}}, "DOC_TB", "confirm"),
    ]
    for case_id, payload, item_id, expected in scenarios:
        actual = core.check(payload, data)
        item = next(x for x in actual["items"] if x["id"] == item_id)
        record = {"id": case_id, "type": "deterministic_synthetic", "input": payload,
                  "expected": {"item_id": item_id, "status": expected}, "actual": actual,
                  "passed": item["status"] == expected}
        records.append(record)
        print(f"{case_id}: {'PASS' if record['passed'] else 'FAIL'}", flush=True)
    if live:
        for fixture in data["qa_fixtures"]:
            started = time.monotonic()
            try:
                result = core.ask({"question": fixture["question"]}, data)
                actual_ids = {e["item_id"] for e in result["evidence"]}
                passed = result["answered"] == fixture["answerable"] and set(fixture["evidence_ids"]).issubset(actual_ids)
                record = {"id": fixture["id"], "type": "real_ai_synthetic_question", "input": fixture["question"],
                          "expected": fixture, "actual": result, "passed": passed,
                          "check_scope": "回答/拒答状态及必要引用ID；完整语义仍需人工核对。"}
            except (core.AIError, core.InputError) as exc:
                record = {"id": fixture["id"], "type": "real_ai_synthetic_question", "input": fixture["question"], "passed": False, "safe_error": str(exc)}
            record["elapsed_seconds"] = round(time.monotonic() - started, 2)
            records.append(record)
            print(f"{record['id']}: {'PASS' if record['passed'] else 'FAIL'} ({record['elapsed_seconds']}s)", flush=True)
        examples = [
            ("AI_PREP_CLEAR", "我的床上用品和洗漱用品已经准备好了，洗衣液还没买。", {"SUPPLY_BEDDING": "ready", "SUPPLY_HYGIENE": "ready", "SUPPLY_LAUNDRY": "missing"}),
            ("AI_PREP_AMBIGUOUS", "我不确定床上用品准备好了没有。", {"SUPPLY_BEDDING": "unknown"}),
            ("AI_PREP_CONTRADICTION", "床上用品我已经准备好了。但刚才说错了，我还没有准备床上用品。", {"SUPPLY_BEDDING": "unknown"}),
        ]
        for case_id, text, expected in examples:
            started = time.monotonic()
            try:
                actual = core.interpret({"text": text}, data)
                actual_states = {s["item_id"]: s["state"] for s in actual["suggestions"]}
                passed = actual_states == expected
                record = {"id": case_id, "type": "real_ai_synthetic_preparation", "input": text, "expected": expected,
                          "actual": actual, "passed": passed, "check_scope": "提取项目及状态精确一致；未经用户确认不应用。"}
            except (core.AIError, core.InputError) as exc:
                record = {"id": case_id, "type": "real_ai_synthetic_preparation", "input": text, "passed": False, "safe_error": str(exc)}
            record["elapsed_seconds"] = round(time.monotonic() - started, 2)
            records.append(record)
            print(f"{case_id}: {'PASS' if record['passed'] else 'FAIL'} ({record['elapsed_seconds']}s)", flush=True)
    report = {"executed_at": datetime.now(timezone.utc).isoformat(), "owner": "WANGHAOBIN",
              "model": core.health()["model"], "live_ai": live,
              "knowledge_sha256": hashlib.sha256((BASE / "data/knowledge.json").read_bytes()).hexdigest(),
              "test_data": "公开资料与合成情境；不含真实参与者或证件。",
              "real_user_testing": "not_conducted", "passed": sum(r["passed"] for r in records),
              "total": len(records), "records": records}
    stem = "LIVE_VALIDATION" if live else "OFFLINE_VALIDATION"
    evidence = BASE / "evidence"
    evidence.mkdir(exist_ok=True)
    (evidence / f"{stem}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [f"# {'真实 API 与合成情境' if live else '离线合成情境'}验证", "", f"执行时间（UTC）：{report['executed_at']}",
             f"模型：{report['model']}；自动检查：{report['passed']}/{report['total']}。", "",
             "这些是工程测试，未开展真实用户测试；不能解释成用户效果或通用准确率。", ""]
    for record in records:
        lines += [f"## {record['id']} — {'通过' if record['passed'] else '需处理'}", "", f"类型：{record['type']}", "",
                  "```json", json.dumps({k: v for k, v in record.items() if k not in ('type', 'id')}, ensure_ascii=False, indent=2), "```", ""]
    (evidence / f"{stem}.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"RESULT {report['passed']}/{report['total']} — evidence/{stem}.json", flush=True)
    return 0 if all(r["passed"] for r in records) else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true", help="make 8 real requests using shared local credentials")
    raise SystemExit(run(parser.parse_args().live))
