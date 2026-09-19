# Week 03 规则问答机器人

本周个人练习读取 `rules.txt`，把规则全文和用户问题一起发送给 OpenAI 兼容的 Qwen API。程序要求回答使用与问题相同的语言，并输出依据条款；规则中找不到的内容必须说明无法确认。

## 运行

从项目根目录使用根 `.venv`：

```powershell
cd C:\Users\31797\Documents\ChatGPT\作业 3\AI_Project_2026_2
.\.venv\Scripts\Activate.ps1
python week03_rule_chatbot\app.py --check
python week03_rule_chatbot\app.py --test-api
python week03_rule_chatbot\app.py
```

也可以用单问模式：

```powershell
python week03_rule_chatbot\app.py --question "我可以在房间里使用电热水壶吗？"
```

输入 `exit` 结束交互。`--check` 只检查规则文件和配置是否存在，不发送 API 请求；输出只显示配置是否存在，不显示密钥。

## 本周三类验收问题

1. `我可以在房间里使用电热水壶吗？`：应根据第 11 条及入住/退宿指南回答禁止携带和使用，并显示依据。
2. `朋友可以来我的房间吗？`：应根据第 17 条说明会客时间、地点及不能进入住宿生房间。
3. `宿舍的打印机在哪里？`：规则中没有该信息，应回答无法从提供的规则确认，并输出 `Evidence: Not found`。

真实 API 测试使用“作业 3”容器根目录的共享 `.env`，读取优先级为：进程环境变量 → 容器根 `.env` → AI 项目根 `.env` → 本周目录 `.env`。不要提交 `.env`、密钥、包含密钥的截图或日志；不含密钥的运行证据可以提交。

真实验收结果保存在 [RUNTIME_EVIDENCE.md](RUNTIME_EVIDENCE.md)，原始结构化记录保存在 [RUNTIME_EVIDENCE.json](RUNTIME_EVIDENCE.json)。

离线测试：

```powershell
python -m unittest discover -s tests -p "test_week03_chatbot.py" -v
```
