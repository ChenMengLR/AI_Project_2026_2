# Week 03 状态：规则问答机器人

- 状态：个人代码与课程规则文档已建立；规则文件已按 Notion 第 5 项改为韩文原样摘录；真实 API 验证待本机配置凭据后执行。
- 代码：`week03_rule_chatbot/app.py`
- 规则：`week03_rule_chatbot/rules.txt`（UTF-8，包含课程给出的韩文条款、来源 URL 和 2026-09-16 确认日期）
- 离线测试：`python -m unittest discover -s tests -p "test_week03_chatbot.py" -v`，4 项全部通过。
- 本地检查：`python week03_rule_chatbot/app.py --check` 能读取规则（1398 characters），只显示 `API KEY: False`、`BASE URL: False`，不显示密钥。
- API 状态：推荐使用 AI 项目根目录的 `.env` 供第 2、3 周共用，周目录 `.env` 可覆盖；当前这些文件都没有有效的 `DASHSCOPE_API_KEY` / `DASHSCOPE_BASE_URL`；`--test-api` 因配置不完整安全退出，未发起请求。
- 测试题目：电热水壶（规则内）、访客进房（规则内）、打印机位置（规则外）。
- 规则约束：每次提问随请求发送完整 `rules.txt`；回答必须与问题同语言，并输出 `Answer` 与 `Evidence`；找不到依据时输出 `Evidence: Not found`；输入 `exit` 退出。
- 安全：本次没有打印、提交或上传 API key；Git 操作仅在本 AI 子项目内执行。
- 小组范围：Mission A/B 是课程小组任务；既有项目记录按先前用户决定暂不处理，因此没有虚构小组主题、功能负责人或团队验证结果。
- 提交策略：`.githooks` 已启用；提交时自动检查敏感文件、格式和离线测试。

最后更新：2026-09-19
