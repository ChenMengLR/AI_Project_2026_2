# 第 5 周个人作业提交记录

提交人：WANGHAOBIN。主题：推荐与个性化（独立课堂 A/B/C 练习）。实际登记日期：2026-10-08（Asia/Shanghai）。

## 课程平台登记

- 在[本人个人作业卡](https://app.notion.com/p/Wang-Haobin-3db7c00fe5ad8143b6aad5a41dbe3cd6)下的每周提交数据库中创建了[5주차 제출 · 第5周提交](https://app.notion.com/p/5-5-3f37c00fe5ad808894c0c1785666ae0a)。
- `Week · 周次` 为 `5`；`Submission Date · 提交日期` 为 `2026-10-08`；`Submission Status · 提交状态` 为 `제출 · 已提交`。
- `GitHub Repository` 为 [week05_recommendation](https://github.com/ChenMengLR/AI_Project_2026_2/tree/main/week05_recommendation)。正文包含中韩双语说明以及 README、程序源码、A/B/C 三组 JSON 和实际调用 JSONL 共六个材料链接。
- 重新加载该卡后，状态、日期、周次、正文及六个链接均保留。[刷新后的核验截图](INDIVIDUAL_WEEK05_SUBMITTED.jpg)已保存。
- 本次使用个人练习对应的 JSON/JSONL 运行证据，没有另录个人演示视频，`Demo Video` 留空；正文已说明。现有宿舍项目 MP4 属于小组作业，未填入个人视频字段。`Feedback` 保持空白；已提交不代表教师已确认或批阅。

## 提交材料与结果

- [运行说明](../../../week05_recommendation/README.md)、[源码](../../../week05_recommendation/app.py)。
- [A 结果](../../../week05_recommendation/evidence/result_A.json)：C1、C3；[B 结果](../../../week05_recommendation/evidence/result_B.json)：C4；[C 结果](../../../week05_recommendation/evidence/result_C.json)：无推荐。
- [2026-10-08 实际 Qwen 调用记录](../../../week05_recommendation/evidence/2026-10-08_Qwen_ABC.jsonl)。模型推荐集合与规则预期一致，最终三组 `validated=true`。
- A、C 的部分模型原始排除理由存在遗漏；最终中韩理由通过规则核对补全。原始结果与遗漏审计已保留，正文未将补全理由称为模型原始输出，并注明 AI 工具协助和合成课堂资料。

## 仓库核对

提交前通过 `git ls-remote origin refs/heads/main` 核实，线上 `main` 为 `3b3f07fa627a88a1aa1a986540a23058e00b87b9`，与当时本地 HEAD 一致；六份链接所指文件均已跟踪并包含在该版本中。本次仅补充平台登记、核验截图和状态记录，没有修改练习代码或重新调用模型。
