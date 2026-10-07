# Week 5：推荐与个性化

## 小组项目：入住有数

负责人 **WANGHAOBIN（一人）**。第 5 周成果已接入原有的 [`week03_dorm_assistant`](../week03_dorm_assistant/)：页面右上角可在中文与韩语间切换；生成行动清单时，程序根据适用身份、预计入住日和九项自填状态，从未完成的可标记事项中给出最多三项下一步，并显示理由、行动和官方来源。报告、来源说明、日期错误、资料不足提示及 AI 辅助区也随语言切换。推荐使用确定性核对和排序，不训练预测模型；两种语言使用同一排序规则。

运行：从 AI 项目根目录双击 `week03_dorm_assistant/Start.cmd`，或执行 `.\.venv\Scripts\python.exe week03_dorm_assistant\app.py`，再打开 <http://127.0.0.1:8765>。手动核对与推荐不需要 API Key；AI 状态理解及规则问答需要容器根目录的本机 `.env` 配置。

- [中韩双语 PPT（已嵌入运行视频）](Week05_Dorm_Recommendation_CN_KR.pptx)
- [独立运行视频 MP4](evidence/Week05_Demo.mp4)：合成情境 A、中文切韩语、合成情境 B、无候选回退。
- [五分钟中韩双语口述稿与实际流程图](TEAM_PRESENTATION_CN_KR.md)
- 实际输入与完整程序输出：[A（一般流程、中文）](evidence/A_standard_zh.json)、[A（一般流程、韩语）](evidence/A_standard_ko.json)、[B（留学生、韩语）](evidence/B_international_ko.json)、[C（无候选、韩语）](evidence/C_all_ready_ko.json)；对应 PNG 截图位于同一 `evidence/` 目录。

A 的前三项是床品、洗护用品、网络用品；B 的前三项是先核实结核证明和居民登记誊本对留学生的适用要求，再阅读最新公告；C 返回空推荐并提示入住前复核所属馆最新公告。A/B/C 均是程序对**合成输入**的实际结果，不是 Qwen 或真实用户反馈。国际生专门文件与替代关系仍缺少可确认的公开依据，程序保留“需确认”，不判断材料真实性或入住资格。真实用户测试与教师批阅尚未发生。

## 课堂独立 A/B/C 练习

这里复现课程的四门候选课程和 A/B/C 三组**课堂合成资料**。它与 `week03_dorm_assistant/` 的宿舍入住准备推荐是两个不同任务，不能把课程推荐的结果当作宿舍项目或真实用户测试结果。

## 硬约束与预期

每门被推荐的课必须同时满足：兴趣标签至少有一个相同、`level` 完全相同、该门课的 `minutes` 不超过用户的 `available_minutes`。最多推荐两门。四门候选课 C1–C4 都必须恰好在课程原页要求的 `recommendations` 或 `excluded` 中出现一次，每项都要有 `reason_zh` 和 `reason_ko`。每项还带 `failed_criteria`；排除项须列全不满足的 `interest`、`level`、`time` 条件，不能只写其中一项。

- C1：AI API 入门 / AI API 입문；10 分钟；beginner；AI。
- C2：高级模型训练 / 고급 모델 학습；90 分钟；advanced；AI。
- C3：VR 交互入门 / VR 인터랙션 입문；25 分钟；beginner；VR。
- C4：统计课程 / 통계 강의；60 分钟；intermediate；Statistics。

按规则计算的课程预期是：A（AI、VR；beginner；30 分钟）推荐 C1、C3；B（Statistics；intermediate；90 分钟）推荐 C4；C（VR；beginner；5 分钟）没有可推荐课程。**这些是规则预期，不是 Qwen 实际返回。**

## 运行

在 AI 项目根目录使用唯一共享 Python 环境：

```powershell
.\.venv\Scripts\python.exe week05_recommendation\app.py --mode rules --scenario all
```

`rules` 模式完全离线，输出可复核的基准以及 `validated` 校验结果。真实模型调用需先在容器根目录的本机 `.env` 配置 `DASHSCOPE_API_KEY`、`DASHSCOPE_BASE_URL` 和可选 `QWEN_MODEL`，然后执行：

```powershell
.\.venv\Scripts\python.exe week05_recommendation\app.py --mode qwen --scenario all --save-results
```

`qwen` 模式按场景分别调用 Qwen，校验课程覆盖、重复、最多两门及推荐集合是否符合硬约束。程序同时审计模型的 `failed_criteria` 和中韩理由；最终 `result` 的理由由已核对的课程与用户资料按规则逐项生成，包含所有失败条件和实际标签、难度、分钟数。未经改写的模型文本另存为 `raw_model_result`，遗漏记录在 `raw_model_criteria_issues` 和 `raw_model_reason_issues`，以免把程序补全的理由说成模型原话。`--save-results` 会在 `evidence/` 中分别保存 `result_A.json`、`result_B.json`、`result_C.json`；每个文件包含该场景的 `profile`、最终 `result`、原始模型结果、模型和校验状态。`validated: true` 表示**最终决策及规则审定的结果**通过程序检查，不表示模型原始理由完备，也不代表人工完成全部语言质量审阅。模型请求可能产生 API 用量。程序不会打印密钥或服务端异常详情；不要把 `.env` 上传 GitHub。

## 2026-10-08 实际运行

- [离线规则输出](evidence/2026-10-08_Rules_ABC.jsonl)：A 为 C1/C3，B 为 C4，C 为空；三组校验通过。
- [初版真实 Qwen 输出](evidence/2026-10-08_Qwen_ABC_initial_incomplete_reasons.jsonl)：保留发现问题的原始记录。B 中 C1、C2 的模型排除理由只提难度，漏掉同样不匹配的兴趣标签；对应独立初版文件为 `initial_result_A/B/C.json`。
- [修订后的真实 Qwen 与规则审定结果](evidence/2026-10-08_Qwen_ABC.jsonl)：按课程原页的 `recommendations` 字段和“列全失败条件”提示重新运行本机 `qwen3.8-flash`，A、B、C 的模型推荐集合分别是 C1/C3、C4、空列表。最终 `result` 在三组均 `validated: true`，排除理由列全不满足的条件。模型原始输出仍见每条记录的 `raw_model_result`；A、C 的模型原始理由或条件列表仍有遗漏，审计字段明确记录，最终理由由规则补全。独立文件见 [A](evidence/result_A.json)、[B](evidence/result_B.json)、[C](evidence/result_C.json)。下次模型输出可能不同。

以上是课堂合成案例的程序检查，不代表真实用户偏好预测能力、教师批阅或全部理由的人工语义审定。宿舍项目的推荐功能和两组模拟情境见 `week03_dorm_assistant/` 及第 5 周项目材料。后续运行仍须注明 `mode`、`model`、日期、实际输出及校验结果；未执行 Qwen 的新案例不能把 `rules` 预期称为模型结果。
