# 第六周：连续问答与多文档检索

负责人：WANGHAOBIN（一人小组）。课程主题为 Conversation / Knowledge Retrieval。本目录同时保存独立个人练习与小组项目的第六周证据；两者的程序入口不同。

## 小组项目：入住有数

原网站 `../week03_dorm_assistant/` 新增 `/api/conversation` 和 `conversation.py`。网页可连续提问，保留当前页面中的问答；后续提问仅发送最近三轮**问题和已引用条目 ID**作上下文，不把模型的自由回答当成新事实。Qwen 将追问改写为独立问题并给出韩文检索词；本地检索从 15 个已整理条目中选出最多三个主题条目，并连同必要条件条款交给 Qwen 判断是否有足够依据。最终可见事实文字取自已整理条目，来源标题、条款及 URL 由服务器附上；检索未命中与资料不足分开提示。网页仍支持中文／한국어切换，切换后清空当前对话并保留既有准备状态。

打开网站：在仓库根目录运行以下 PowerShell 命令，再打开 `http://127.0.0.1:8765/`。

```powershell
.\.venv\Scripts\python.exe week03_dorm_assistant\app.py
```

小组的结构、输入／检索／回答流和来源清单见 [TEAM_STRUCTURE.md](TEAM_STRUCTURE.md)；三个必需情境的实际输出、修复和复测见 [TEAM_RESULTS.md](TEAM_RESULTS.md)。

## 个人独立练习

`app.py` 单独读取 `docs/rules.txt`、`docs/life_guide.txt`、`docs/notice_printer.txt`，按 `[条款]` 切分。`rules.txt` 是第 3 周课堂整理文本副本；`life_guide.txt` 是官方入住说明的条款摘要；`notice_printer.txt` 是第六周课堂提供的设施摘要，打印机位置尚未独立从网页表格复核。每条引用保留自身对应的原文 URL 和核对日期。Qwen 改写追问并生成 2–5 个韩文检索词；本地检索最多三条；Qwen 基于检索条款回答并返回 `[S1]` 等编号。禁带物品的关键结论通过条款文字再校验，模型原话保留在 JSONL 供审计。

```powershell
.\.venv\Scripts\python.exe week06_knowledge_qa\app.py --check
$env:PYTHONIOENCODING='utf-8'
.\.venv\Scripts\python.exe week06_knowledge_qa\app.py --scenario all --save-results
```

实际结果见 [PERSONAL_RESULTS.md](PERSONAL_RESULTS.md)，原始结构化输出见 [`evidence/2026-10-20_Qwen_cases.jsonl`](evidence/2026-10-20_Qwen_cases.jsonl)。第二条命令真实调用本机配置的 Qwen；共享密钥仅从容器根 `.env` 读取，不进入仓库。

## 展示与边界

- 小组真实 Qwen JSON：[`evidence/2026-10-20_Group_Qwen_cases.json`](evidence/2026-10-20_Group_Qwen_cases.json)。网页四张实际截图：[`Group_UI_grounded.png`](evidence/Group_UI_grounded.png)、[`Group_UI_followup.png`](evidence/Group_UI_followup.png)、[`Group_UI_unavailable.png`](evidence/Group_UI_unavailable.png)、[`Group_UI_Korean.png`](evidence/Group_UI_Korean.png)。
- 演示视频为上述实际页面截图的剪辑，视频内明确标注“非连续录屏”。它展示真实运行结果，但不能代替持续操作录像。
- 输入是人工构造的测试问题，不是已开展的真实住校生试用。检索规则与少量 Qwen 情境不能证明一般准确率；具体学期安排、个人入住资格和留学生材料替代关系须由学校确认。
- 教师第 5 周反馈提出的公开网站 URL 尚未提供。当前地址是本机 `127.0.0.1`，无法作为校外可访问的部署链接。资料适用范围、数据输入、15 条来源索引已在 [TEAM_STRUCTURE.md](TEAM_STRUCTURE.md)补齐。
