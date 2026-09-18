# Week 03 状态：规则问答机器人

- 状态：个人代码与课堂规则文档已建立；真实 API 验证待本机配置凭据后执行。
- 代码：`week03_rule_chatbot/app.py`
- 规则：`week03_rule_chatbot/rules.txt`
- 离线测试：`tests/test_week03_chatbot.py`
- 当前测试：4 项离线测试通过。
- API 状态：`.env` 仅为本机忽略文件，当前没有有效密钥和 Base URL；不会把密钥写入仓库。
- 测试题目：电热水壶（规则内）、访客进房（规则内）、打印机位置（规则外）。
- 规则约束：每次提问随请求发送完整 `rules.txt`；回答必须与问题同语言，并输出 `Answer` 与 `Evidence`；找不到依据时输出 `Evidence: Not found`；输入 `exit` 退出。
- 待办：在本机配置同一地域的 `DASHSCOPE_API_KEY` 与 `DASHSCOPE_BASE_URL`，运行 `python week03_rule_chatbot/app.py --check`、`--test-api` 及三个问题，再保存不含密钥的运行结果。

最后更新：2026-09-19
