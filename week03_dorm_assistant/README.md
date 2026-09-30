# 入住有数 · 宿舍入住准备助手

负责人：**WANGHAOBIN**。一人项目，不另设组名。首版完成日期：2026-09-30。

将 Hanlim 公开入住说明转成带来源的准备清单。用户自报准备状态，也可先让 Qwen 理解自然语言，再逐项确认建议。结果辅助准备，不判断入住资格或材料真实性。

## 立即运行

在本机双击本目录的 `Start.cmd`，然后打开 **http://127.0.0.1:8765**。终端保持运行；按 Ctrl+C 停止。

也可以从 AI 项目根目录执行：

```powershell
.\.venv\Scripts\python.exe week03_dorm_assistant\app.py
```

首次在其他电脑使用：Python 3.11+，在 AI 项目根目录创建唯一的 `.venv`，安装根 `requirements.txt`。本机已使用现有共享环境，没有新增依赖或第二个虚拟环境。

手动清单、资料查看、日期核对、浏览器本地保存及 JSON 导出无需 AI。自然语言建议和问答需要共享配置中的 `DASHSCOPE_API_KEY`、`DASHSCOPE_BASE_URL`、`QWEN_MODEL`。主配置固定从“作业 3”容器根 `.env` 读取；项目根及周目录仅兼容回退。不要把密钥写到页面或提交到仓库。

## 如何试用

1. 选择“暂未确认适用身份”或“留学生”；只有向学校确认按一般说明办理后才选一般流程。
2. 阅读条目，填写已准备／待准备／待确认及可选日期。
3. 在 AI 辅助区输入：“我的床上用品和洗漱用品已经准备好了，洗衣液还没买。”
4. 检查建议，确认后应用；也可以取消建议并保持手动状态。
5. 生成行动清单，查看每条下一步及原文；保存进度、导出 JSON 或打印。
6. 用“可以带电热毯和电饭锅吗？”验证有依据问答；用“我可以用护照代替居民登记誊本吗？”验证资料外拒答。

演示日期、状态和问题使用合成数据，不代表学校安排或真实参与者。

## 已实现

- 15 个来源可追溯知识条目、12 条教学规则；9 个可标记事项、6 个参考提醒。
- 国际生／身份未确认的材料要求保留“需确认”，不输出“获准入住”。
- 日期按三个日历月核对，识别缺日期、过旧、未来出具和出具晚于入住等情况。
- AI 建议必须用户确认；未知项目／状态／重复项目会拒绝。
- 问答引用由服务器从已核对的资料取出；关联重要条件会补入回答，双来源项目保留两个出处。
- 浏览器只保存配置、日期、状态和资料版本，不保存自然语言描述或问题。导出只含报告和来源。
- API 不可用时保留手动操作；服务仅监听本机回环地址。

## 课程材料与证据

- [项目计划](docs/PROJECT_PLAN.md)
- [Mission A 规则](rules.txt) 与 [真实问答/技术验证](evidence/LIVE_VALIDATION.md)
- [Mission B 规格、流程及四项任务](docs/MISSION_B_SPEC.md)
- [Week 4 Route B、功能卡与五类测试](../week04_dorm_validation/week04_feature_test.md)
- [QA、实际问题与复测](docs/QA_REPORT.md)
- [五分钟汇报脚本](docs/DEMO_SCRIPT.md)
- [Notion 可复制提交正文](docs/NOTION_SUBMISSION.md)
- [真实用户测试包](docs/USER_TEST_KIT.md)（尚未开展，未伪造用户反馈）
- [官方资料与适用范围](docs/SOURCES.md)

## 复现检查

在 AI 项目根目录运行：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe week03_dorm_assistant\app.py --check
.\.venv\Scripts\python.exe week03_dorm_assistant\validate.py
```

以下命令会真实调用已配置的 Qwen，并消耗 API 用量；前者 8 次、后者 4 次：

```powershell
.\.venv\Scripts\python.exe week03_dorm_assistant\validate.py --live
.\.venv\Scripts\python.exe week03_dorm_assistant\validate_week4.py
```

`validate.py` 的 QA 自动判定检查回答／拒答状态及必要引用，不等于完整语义准确率。发现并修复的语义遗漏见 QA 报告。模型版本或输出改变可能使复测结果不同，应保留真实失败。

## 边界和待办

已收录公开页面没有给出留学生材料替代关系，也未注明具体适用学期。用户需要对照所属馆最新公告。本工具不上传真实证件，不自动提交学校申请，不作健康判断。

本轮是可运行的课程原型与开发者工程验证。真实用户测试、教师反馈、后续学期迭代及最终课程展示尚未发生。后续新增周记录放同级周目录，保留已有个人练习。

开发、代码、文档和验收由 AI 助手协助完成；WANGHAOBIN 为项目负责人，不据此声称全部代码独立手写或已进行真实用户测试。
