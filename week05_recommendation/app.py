"""Week 5 classroom recommendation exercise, separate from the dorm assistant.

The rule path computes an offline expectation. The Qwen path must be run
separately and its structured response is validated before being accepted.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent
CONTAINER_ROOT = BASE.parent.parent
COURSES = (
    {"id": "C1", "title_zh": "AI API 入门", "title_ko": "AI API 입문", "minutes": 10,
     "level": "beginner", "tags": ["AI"]},
    {"id": "C2", "title_zh": "高级模型训练", "title_ko": "고급 모델 학습", "minutes": 90,
     "level": "advanced", "tags": ["AI"]},
    {"id": "C3", "title_zh": "VR 交互入门", "title_ko": "VR 인터랙션 입문", "minutes": 25,
     "level": "beginner", "tags": ["VR"]},
    {"id": "C4", "title_zh": "统计课程", "title_ko": "통계 강의", "minutes": 60,
     "level": "intermediate", "tags": ["Statistics"]},
)
SCENARIOS = {
    "A": {"interests": ["AI", "VR"], "level": "beginner", "available_minutes": 30},
    "B": {"interests": ["Statistics"], "level": "intermediate", "available_minutes": 90},
    "C": {"interests": ["VR"], "level": "beginner", "available_minutes": 5},
}


def expected_ids(profile: dict) -> list[str]:
    """Apply every hard constraint; the minute limit is per course."""
    matches = [course["id"] for course in COURSES
               if set(course["tags"]) & set(profile["interests"])
               and course["level"] == profile["level"]
               and course["minutes"] <= profile["available_minutes"]]
    return matches[:2]


def failed_criteria(course: dict, profile: dict, selected: bool) -> list[str]:
    if selected:
        return []
    failed = []
    if not set(course["tags"]) & set(profile["interests"]):
        failed.append("interest")
    if course["level"] != profile["level"]:
        failed.append("level")
    if course["minutes"] > profile["available_minutes"]:
        failed.append("time")
    if not failed:
        failed.append("limit")
    return failed


def reasons(course: dict, profile: dict, selected: bool) -> tuple[str, str]:
    """Generate complete bilingual explanations from checked data, not model prose."""
    course_tags = ", ".join(course["tags"])
    interests = ", ".join(profile["interests"])
    minutes, available = course["minutes"], profile["available_minutes"]
    if selected:
        shared = ", ".join(tag for tag in course["tags"] if tag in profile["interests"])
        return (f"兴趣标签 {shared} 匹配；难度同为 {course['level']}；单门 {minutes} 分钟不超过可用的 {available} 分钟。",
                f"관심 분야에 {shared} 태그가 포함되고 난이도 {course['level']}가 일치합니다. 강의 시간 {minutes}분은 이용 가능한 {available}분 이내입니다.")
    parts_zh, parts_ko = [], []
    for criterion in failed_criteria(course, profile, selected):
        if criterion == "interest":
            parts_zh.append(f"兴趣标签 {course_tags} 与用户兴趣 {interests} 不匹配")
            parts_ko.append(f"강의 태그({course_tags})와 사용자 관심 분야({interests})가 일치하지 않습니다")
        elif criterion == "level":
            parts_zh.append(f"难度 {course['level']} 与用户要求 {profile['level']} 不同")
            parts_ko.append(f"강의 난이도({course['level']})와 사용자 요청 난이도({profile['level']})가 다릅니다")
        elif criterion == "time":
            parts_zh.append(f"单门 {minutes} 分钟超过可用的 {available} 分钟")
            parts_ko.append(f"강의 시간은 {minutes}분으로 이용 가능한 {available}분을 초과합니다")
        else:
            parts_zh.append("符合三项条件，但超过最多两门的推荐上限")
            parts_ko.append("세 조건은 충족하지만 최대 2개 추천 제한을 초과합니다")
    return "；".join(parts_zh) + "。", ". ".join(parts_ko) + "."


def rule_result(profile: dict) -> dict:
    selected = set(expected_ids(profile))
    result = {"recommendations": [], "excluded": []}
    for course in COURSES:
        is_selected = course["id"] in selected
        reason_zh, reason_ko = reasons(course, profile, is_selected)
        result["recommendations" if is_selected else "excluded"].append({
            "id": course["id"], "failed_criteria": failed_criteria(course, profile, is_selected),
            "reason_zh": reason_zh, "reason_ko": reason_ko})
    return result


def canonicalize_result(profile: dict, result: dict) -> dict:
    """Retain model decisions; replace prose with complete checked explanations."""
    courses = {course["id"]: course for course in COURSES}
    clean = {"recommendations": [], "excluded": []}
    for section in clean:
        for row in result[section]:
            course = courses[row["id"]]
            selected = section == "recommendations"
            reason_zh, reason_ko = reasons(course, profile, selected)
            clean[section].append({"id": course["id"],
                                   "failed_criteria": failed_criteria(course, profile, selected),
                                   "reason_zh": reason_zh, "reason_ko": reason_ko})
    return clean


def validate_result(profile: dict, result: object, require_failed_criteria: bool = True) -> list[str]:
    """Reject omissions, duplicates, wrong decisions or incomplete failure lists."""
    if not isinstance(result, dict):
        return ["响应不是 JSON 对象。"]
    recommendations, excluded = result.get("recommendations"), result.get("excluded")
    if not isinstance(recommendations, list) or not isinstance(excluded, list):
        return ["recommendations 和 excluded 必须是数组。"]
    errors = []
    if len(recommendations) > 2:
        errors.append("推荐超过两门。")
    rows = recommendations + excluded
    actual_ids = []
    known_ids = {course["id"] for course in COURSES}
    courses = {course["id"]: course for course in COURSES}
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            errors.append("存在无效课程对象。")
            continue
        actual_ids.append(row["id"])
        if row["id"] not in known_ids:
            errors.append(f"出现未知课程 {row['id']}。")
        else:
            selected = index < len(recommendations)
            expected_failures = failed_criteria(courses[row["id"]], profile, selected)
            if require_failed_criteria and row.get("failed_criteria") != expected_failures:
                errors.append(f"{row['id']} 未列全不满足条件：应为 {expected_failures}。")
        for field, pattern in (("reason_zh", r"[\u4e00-\u9fff]"), ("reason_ko", r"[\uac00-\ud7a3]")):
            reason = row.get(field)
            if not isinstance(reason, str) or not reason.strip() or not re.search(pattern, reason):
                errors.append(f"{row['id']} 缺少有效的 {field}。")
    if len(actual_ids) != len(set(actual_ids)):
        errors.append("同一课程在结果中重复。")
    if set(actual_ids) != known_ids or len(actual_ids) != len(known_ids):
        errors.append("四门候选课程未恰好各出现一次。")
    expected = set(expected_ids(profile))
    if {row.get("id") for row in recommendations if isinstance(row, dict) and isinstance(row.get("id"), str)} != expected:
        errors.append("推荐集合不符合兴趣、难度和单门时间硬约束。")
    if {row.get("id") for row in excluded if isinstance(row, dict) and isinstance(row.get("id"), str)} != known_ids - expected:
        errors.append("排除集合与推荐集合不互补。")
    return errors


def audit_raw_reasons(profile: dict, result: dict) -> list[str]:
    """Flag missing course/profile facts in either language of model prose."""
    courses = {course["id"]: course for course in COURSES}
    issues = []
    for section in ("recommendations", "excluded"):
        for row in result[section]:
            course = courses[row["id"]]
            selected = section == "recommendations"
            criteria = failed_criteria(course, profile, selected)
            needed = []
            if selected or "interest" in criteria:
                needed.extend(course["tags"])
                if not selected:
                    needed.extend(profile["interests"])
            if selected or "level" in criteria:
                needed.extend((course["level"], profile["level"]))
            if selected or "time" in criteria:
                needed.extend((str(course["minutes"]), str(profile["available_minutes"])))
            for field in ("reason_zh", "reason_ko"):
                reason = row[field].casefold()
                missing = [token for token in dict.fromkeys(needed) if token.casefold() not in reason]
                if missing:
                    issues.append(f"{row['id']} {field} 未逐项写出或量化：{missing}。")
    return issues


def qwen_result(profile: dict) -> tuple[dict, str]:
    """Only this opt-in path loads the shared local configuration and calls Qwen."""
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv(CONTAINER_ROOT / ".env", override=False)
    key = os.getenv("DASHSCOPE_API_KEY", "").strip()
    endpoint = os.getenv("DASHSCOPE_BASE_URL", "").strip()
    model = os.getenv("QWEN_MODEL", "qwen3.8-flash").strip() or "qwen3.8-flash"
    if not key or not endpoint:
        raise RuntimeError("Qwen 未配置；离线规则模式仍可运行。")
    system = ("你是课程推荐器。只依据给定候选和用户条件输出 JSON 对象。"
              "只有兴趣标签至少一个相同、level 完全相同、单门 minutes 不超过 available_minutes，才可推荐；最多两门。"
              "四门课程必须且只能各出现一次：要么放 recommendations，要么放 excluded。"
              "逐门独立检查兴趣、level、时长，不要因一个条件已失败而省略其他失败条件。"
              "每项包含 id、failed_criteria、简短中文 reason_zh、简短韩文 reason_ko。"
              "failed_criteria 必须按 interest、level、time 的顺序列出所有失败项；都满足但因最多两门上限被排除则为 [\"limit\"]；推荐项为 []。"
              "中韩理由须解释 failed_criteria 中的每一项，并使用输入里的真实标签、级别和分钟数。"
              "输出形如 {\"recommendations\":[{\"id\":\"C1\",\"failed_criteria\":[],\"reason_zh\":\"...\",\"reason_ko\":\"...\"}],\"excluded\":[]}。"
              "不要编造课程、用户条件或例外。")
    try:
        client = OpenAI(api_key=key, base_url=endpoint, timeout=45.0, max_retries=0)
        response = client.chat.completions.create(
            model=model, temperature=0, max_tokens=1600,
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": json.dumps({"profile": profile, "courses": COURSES}, ensure_ascii=False)}],
            response_format={"type": "json_object"}, extra_body={"enable_thinking": False})
        result = json.loads(response.choices[0].message.content or "")
    except Exception:
        # Provider errors can include request headers or other private details.
        raise RuntimeError("Qwen 调用或 JSON 解析失败；未接受模型输出。") from None
    return result, model


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="第5周课堂 A/B/C 推荐练习")
    parser.add_argument("--scenario", choices=["A", "B", "C", "all"], default="all")
    parser.add_argument("--mode", choices=["rules", "qwen"], default="rules")
    parser.add_argument("--save-results", action="store_true", help="将每组结果另存为 evidence/result_A.json 等文件")
    args = parser.parse_args(argv)
    scenarios = SCENARIOS if args.scenario == "all" else {args.scenario: SCENARIOS[args.scenario]}
    had_error = False
    for name, profile in scenarios.items():
        try:
            if args.mode == "qwen":
                raw_result, model = qwen_result(profile)
                decision_errors = validate_result(profile, raw_result, require_failed_criteria=False)
                raw_criteria_issues = [issue for issue in validate_result(profile, raw_result)
                                       if issue not in decision_errors]
                raw_reason_issues = audit_raw_reasons(profile, raw_result) if not decision_errors else []
                result = canonicalize_result(profile, raw_result) if not decision_errors else None
                errors = decision_errors + (validate_result(profile, result) if result is not None else [])
            else:
                result, model = rule_result(profile), None
                raw_result = None
                raw_criteria_issues, raw_reason_issues = [], []
                errors = validate_result(profile, result)
            output = {"scenario": name, "profile": profile, "mode": args.mode, "model": model,
                      "expected_ids": expected_ids(profile), "validated": not errors,
                      "validation_errors": errors, "reason_source": "verified_rules",
                      "result": result}
            if args.mode == "qwen":
                output["raw_model_result"] = raw_result
                output["raw_model_criteria_issues"] = raw_criteria_issues
                output["raw_model_reason_issues"] = raw_reason_issues
            had_error = had_error or bool(errors)
        except RuntimeError as exc:
            output = {"scenario": name, "profile": profile, "mode": args.mode, "validated": False,
                      "validation_errors": [str(exc)]}
            had_error = True
        if args.save_results:
            evidence = BASE / "evidence"
            evidence.mkdir(exist_ok=True)
            (evidence / f"result_{name}.json").write_text(
                json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        # ASCII JSON survives legacy Windows console encodings; JSON readers
        # recover the original Chinese and Korean text without loss.
        print(json.dumps(output, ensure_ascii=True))
    return 1 if had_error else 0


if __name__ == "__main__":
    sys.exit(main())
