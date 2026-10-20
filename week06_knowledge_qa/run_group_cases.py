"""Run and save synthetic Week 6 scenarios against the actual dorm logic."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent
DORM = BASE.parent / "week03_dorm_assistant"
sys.path.insert(0, str(DORM))
import conversation  # noqa: E402
import core  # noqa: E402

SCENARIOS = {
    "grounded": ["可以带电热水壶吗？"],
    "followup": ["可以带电热水壶吗？", "那冰箱呢？"],
    "unavailable": ["奖学金申请日期是什么？"],
    "retrieval_paraphrase": ["烧水的机器能带进宿舍吗？"],
}


def run(client=None, save: bool = False) -> list[dict]:
    data = core.catalog()
    records = []
    for name, questions in SCENARIOS.items():
        history = []
        for question in questions:
            result = conversation.answer({"question": question, "history": history, "language": "zh"}, data, client)
            records.append({"scenario": name, "generated_at": datetime.now(timezone.utc).isoformat(),
                            "input": {"question": question, "history": history.copy()}, "result": result})
            history.append({"question": question, "evidence_ids": [row["item_id"] for row in result["evidence"]]})
            history = history[-3:]
            print(json.dumps({"scenario": name, "question": question, "standalone_question": result["standalone_question"],
                              "keywords_ko": result["keywords_ko"], "retrieved": [
                                  {"item_id": h["item_id"], "document": h["document"], "clause": h["clause"], "url": h["url"]}
                                  for h in result["retrieved"]], "answer": result["answer"],
                              "evidence": [e["item_id"] for e in result["evidence"]],
                              "failure_stage": result["failure_stage"]}, ensure_ascii=False))
    if save:
        evidence = BASE / "evidence"
        evidence.mkdir(exist_ok=True)
        path = evidence / f"{datetime.now().date().isoformat()}_Group_Qwen_cases.json"
        path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved: {path}")
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--save-results", action="store_true")
    args = parser.parse_args()
    try:
        run(save=args.save_results)
        return 0
    except (core.AIError, core.InputError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
