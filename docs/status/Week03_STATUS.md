# Week 03 状态：规则问答机器人

- 状态：个人代码与课程规则文档已建立；规则文件已按 Notion 第 5 项改为韩文原样摘录；真实 API 已通过共享根 `.env` 验证，三道 Week 3 验收题均已完成。
- 代码：`week03_rule_chatbot/app.py`
- 规则：`week03_rule_chatbot/rules.txt`（UTF-8，包含课程给出的韩文条款、来源 URL 和 2026-09-16 确认日期）
- 离线测试：`python -m unittest discover -s tests -p "test_week03_chatbot.py" -v`，4 项全部通过。
- 本地检查：`python week03_rule_chatbot/app.py --check` 能读取规则（1398 characters），显示 `API KEY: True`、`BASE URL: True`、`MODEL: qwen3.8-flash`，不显示密钥。
- API 状态：统一使用“作业 3”容器根目录的 `.env` 供第 2、3 周及后续 AI 任务共用，AI 项目根目录和周目录 `.env` 仅作回退；共享根 `.env` 已被读取；`--test-api` 返回 `API connection OK`。真实密钥仍只保留在本机共享配置中。
- 测试题目：电热水壶（规则内）、访客进房（规则内）、打印机位置（规则外）。三题退出码均为 0；实际输出见 `week03_rule_chatbot/RUNTIME_EVIDENCE.md` 和 `.json`。
- 规则约束：每次提问随请求发送完整 `rules.txt`；回答必须与问题同语言，并输出 `Answer` 与 `Evidence`；找不到依据时输出 `Evidence: Not found`；输入 `exit` 退出。
- 安全：本次没有打印、提交或上传 API key；Git 操作仅在本 AI 子项目内执行。
- 小组范围：Mission A/B 是课程小组任务；既有项目记录按先前用户决定暂不处理，因此没有虚构小组主题、功能负责人或团队验证结果。
- 提交策略：`.githooks` 已启用；提交时自动检查敏感文件、格式和离线测试。提交证据中没有 `.env`。

## 2026-10-01 个人作业补充核验

- 已在最终 `app.py` 上重新实际调用 Qwen 完成三题，三次退出码均为 0，程序 SHA-256 同为 `83b4c4481a9f338241dde454925b3f82f627b306b97ef392921be9bd0bdc015f`。三张截图与原始 JSON 见 [2026-10-01 运行证据](../../week03_rule_chatbot/evidence/2026-10-01/)。截图媒介为本机浏览器终端展示的真实 Python 子进程输出，不是原生 PowerShell 窗口。
- 初始复测中，模型回答曾遗漏第 17 条的访客申请条件，第 11 条电热水壶回答也曾遗漏健康例外；没有把这些不完整答案计为通过。最终程序仍先调用 Qwen，再针对匹配的问题从 `rules.txt` 原文确定性补全相应条件；第 3 题规则外问题保持 `Evidence: Not found`。首次遗漏的记录见 [QA 记录](../../week03_rule_chatbot/evidence/2026-10-01/INITIAL_QA_NOTE.md)。
- 个人离线测试现为 7 项，均通过。旧章节的“4 项”是 2026-09-19 历史结果；上文“小组暂不处理”也只是当时决定，小组项目及课程提交已另见 [团队状态](Week03_TEAM_STATUS.md)。
- [个人提交清单](../submission/2026-10-01/INDIVIDUAL_SUBMISSION.md) 已备齐代码与截图链接；课程个人第 3 周卡仍只读并显示未提交。是否接受该截图媒介由课程方决定。

最后更新：2026-10-01
