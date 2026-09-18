# 第 3 周课程总结：规则问答机器人

来源：Notion「网站与服务规则 Q&A 聊天机器人」课程页（Week 3）。本页只总结文档内容和本地项目执行状态；课程页面中的小组任务说明不等于本人的小组主题或已完成结果。

## 课程目标

使用第 2 周的 Python 环境和 Qwen API，读取一个规则文档，让用户连续提问。机器人必须只依据文档回答，显示依据条款；文档没有答案时要明确说无法确认，不得凭常识猜测。

## 本周要求与本地对应物

| 课程要求 | 本地结果 |
| --- | --- |
| 与 `week02_photo_classifier` 同级创建 `week03_rule_chatbot` | 已创建，未覆盖第 2 周目录 |
| 继续使用根目录 `.venv` | 已保留根 `.venv`，周目录没有重复创建环境 |
| 复制第 2 周 API 配置；不公开密钥 | `.env` 只在本机；仓库只保留 `.env.example`，当前本机配置为空模板 |
| 保存东亚大学翰林生活馆规则摘要 | `week03_rule_chatbot/rules.txt`，包含来源 URL 和确认日期 |
| 连续提问、同语言回答、显示证据、`exit` 退出 | `week03_rule_chatbot/app.py` 已实现 |
| 三类验收题 | 电热水壶、访客进房、打印机位置；测试说明已写入周目录 README |
| GitHub 交付 | 提交前必须确认 `git status` 中没有 `.env`；本次交接文件记录了检查步骤 |

## 课程要求的运行顺序

1. 在项目根目录确认位置，激活根 `.venv`。
2. 进入或直接调用 `week03_rule_chatbot/app.py`。
3. 运行 `--check`，确认 `RULES`、`API KEY`、`BASE URL` 的状态；该命令不联网。
4. 在配置有效时运行 `--test-api`，再运行交互程序。
5. 依次展示两个有答案问题和一个无答案问题的真实输出，然后输入 `exit`。
6. `git status` 确认没有 `.env` 后，提交并推送代码、规则文档、测试和说明。

## 第 3 周个人作业完成情况

- **已完成**：目录、规则文档、问答程序、`.env.example`、离线测试、交接文档和课程总结。
- **已验证**：4 项离线测试通过；代码不会在提示词或诊断中打印 API Key；规则文件可按 UTF-8 读取；请求会同时携带完整规则和问题。
- **待本机执行**：真实 API 的 `--check` 目前显示 `API KEY: False`、`BASE URL: False`，因为当前项目没有有效的本地凭据。配置本人的同地域密钥后，才能完成真实调用、运行截图或运行视频。
- **范围说明**：课程的 Mission A/B 是小组任务。此前已决定暂不处理小组作业，因此没有虚构小组主题、功能负责人或团队验证结果。

## 小组部分的课程要求（以后若恢复）

Mission A 需要从官方来源选 8–15 条与项目相关的规则，设计 3 个有答案问题和 2 个无答案问题，并展示运行结果和修改过程。Mission B 需要选一个可开发核心功能，完成完整功能规格、流程图/线框图/伪代码、至少一项真实技术验证，并拆成 3–5 个有负责人和完成标准的任务。课堂汇报为 3 分钟展示加 2 分钟提问；之后用 10 分钟完成 GitHub 保存与提交确认。

## 参考命令

```powershell
cd C:\Users\31797\Documents\ChatGPT\作业 3\AI_Project_2026_2
.\.venv\Scripts\Activate.ps1
python -m unittest discover -s tests -p "test_week03_chatbot.py" -v
python week03_rule_chatbot\app.py --check
python week03_rule_chatbot\app.py --test-api
python week03_rule_chatbot\app.py
git status --short
git add HANDOFF.md docs week03_rule_chatbot tests
git commit -m "Add Week 3 rules Q&A chatbot"
git push
```

提交前不要把 `.env` 写入命令、截图、Notion 或 GitHub。新窗口应先读取项目根目录的 `HANDOFF.md`，再读取本页和 `docs/status/Week03_STATUS.md`。
