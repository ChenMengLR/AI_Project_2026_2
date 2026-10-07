# Week 05 状态：推荐、个性化与中韩双语

最后更新：2026-10-08。负责人：WANGHAOBIN（一人）。本记录区分小组宿舍项目与课程独立 A/B/C 练习；所有演示资料均为合成输入。

## 已实现的小组项目

- 在原 `week03_dorm_assistant/` 增加中文／韩语界面切换；语言偏好与准备状态分别保存在本地浏览器。切换后重核已有报告，清单、报告、来源、错误和 AI 辅助说明按语言显示；不改变排序规则或原有准备状态。
- 手动核对后从 9 个可标记候选中排除已完成及参考项，按当前阶段、待确认／日期异常、待准备、未知、要求类型及稳定原始顺序取最多 3 项，展示理由、下一步和来源。国际生材料适用性仍需向官方确认；无候选时提示复核所属馆最新公告。未训练预测模型、未采集推荐点击反馈。
- 15 条知识说明、条件注释及 3 个来源补齐韩文。官方韩文原文保持原样。
- [实际流程、两例与五分钟中韩双语讲稿](../../week05_recommendation/TEAM_PRESENTATION_CN_KR.md)；[六页中韩双语 PPT](../../week05_recommendation/Week05_Dorm_Recommendation_CN_KR.pptx)已嵌入[27.56 秒运行视频](../../week05_recommendation/evidence/Week05_Demo.mp4)。PPT 媒体包内 MP4 与独立视频 SHA-256 一致。

## 实际情境与证据

- A（一般流程，入住日 2026-11-01，两份材料自报 ready 且开具日 2026-09-30，床品／洗护 missing、网络用品 unknown）：实际 Top 3 为 `SUPPLY_BEDDING`、`SUPPLY_LAUNDRY`、`SUPPLY_NETWORK`。中文与韩语报告分别存于 `week05_recommendation/evidence/A_standard_zh.json` 和 `A_standard_ko.json`，同目录有界面及推荐区截图。
- B（留学生，同一合成入住日期，两份材料自报 ready、最新公告 missing、其他项 ready）：实际 Top 3 为 `DOC_TB`、`DOC_ADDRESS`、`NOTICE_REVIEW`。前两项为 `confirm`，未将一般说明视作留学生个人结论。证据为 `B_international_ko.json` 及截图。
- C（一般流程，全部可标记事项自报 ready、材料日期有效）：推荐为空，并出现最新公告复核提示。证据为 `C_all_ready_ko.json` 及截图。
- 2026-10-08 通过 Edge 实际页面操作录制两例、切换语言与空候选回退。韩语可见正文中的汉字仅为「中文」切换按钮；移动端 390px 视口横向溢出为 0，页面 JavaScript 错误为 0。

## 独立课堂练习

- `week05_recommendation/app.py` 根据课程原页四候选和 A/B/C 资料运行。离线规则预期 A 为 C1/C3、B 为 C4、C 为空；真实 `qwen3.8-flash` 按课程要求的 `recommendations`/`excluded` 字段重新运行后也是这些结果。
- 初版真实 Qwen 输出的 B 情境漏写部分排除条件，已单独保留。修订提示词后重新调用，模型推荐集合 A/B/C 分别为 C1/C3、C4、空；原始模型 A、C 的部分排除理由仍不完整。最终 `result` 的中韩理由由规则核对实际标签、级别和分钟数后逐项生成，三组 `validated=true`。`raw_model_result` 与遗漏审计字段保留模型原话和问题，不能把最终理由称为模型原始输出。证据为 `evidence/result_A.json`、`result_B.json`、`result_C.json` 与 `2026-10-08_Qwen_ABC.jsonl`。

## 检查与待办

- `python -m unittest discover -s tests -q`：59 项通过。`node --check week03_dorm_assistant/static/app.js`、本机服务 `--check`、`git diff --check` 通过。浏览器实际 A/B/C 的推荐 IDs 与后端确定性输出一致，韩语偏好及状态刷新后保留。
- 用合成韩文输入实际调用本机 Qwen 的状态理解与规则问答：识别床品已准备、洗护用品未准备，并以韩语回答电热毯问题且附韩文官方来源。输入、输出见 `week05_recommendation/evidence/2026-10-08_Korean_AI_Check.json`；这不构成模型质量的广泛评估。
- 真实用户测试、教师对一人项目的确认和课堂现场汇报尚未发生。国际生具体材料及替代关系仍需补充可追溯的官方依据；当前功能保留待确认，不验证证件真实性或入住资格。
- 第 5 周 [Notion 小组卡](https://app.notion.com/p/05-5-bf47c00fe5ad827e881201f714c87e53) 已填写任务、进展、成果并标记 `완료 · 已完成`；中韩双语 PPT、独立 MP4 和不含密钥的第 5 周源码 ZIP 三份附件在新页面中均可见。[提交记录与截图](../submission/2026-10-08/TEAM_WEEK05_SUBMISSION.md)保存了核验证据。
- 本地提交 `e2f0b12` 已创建；向 GitHub `origin/main` 及新分支推送时，远端均返回 `Internal Server Error`。课程卡已写明远端未同步，源码包作为可审阅的备用交付；待恢复后需推送并更新课程卡中的准确提交链接。不能把当前仓库 `main` 链接称为第 5 周线上代码。
