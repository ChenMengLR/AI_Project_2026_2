"""Run the safe synthetic-notice demo without printing credentials."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "week03_dorm_assistant"))
sys.path.insert(0, str(PROJECT))
import core  # noqa: E402
from week07_notice_interpreter.notice import interpret_notice  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=("demo", "blind"), default="demo")
    args = parser.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sample = (Path(__file__).with_name(f"{args.case}_sample.txt")).read_text(encoding="utf-8").strip()
    result = interpret_notice({"notice_text": sample, "profile": "international",
                               "states": {"DOC_TB": "missing", "SUPPLY_BEDDING": "ready"}})
    record = {"recorded_at_utc": datetime.now(timezone.utc).isoformat(),
              "sample_kind": f"synthetic_{args.case}_not_school_policy",
              "model": core.health()["model"], "input": sample, "result": result}
    print(json.dumps(record, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
