# Week 4 个人练习：UCI 退学风险预测

课堂来源：[Prediction and Project Data Design](https://app.notion.com/p/Prediction-and-Project-Data-Design-3cf7c00fe5ad8155bde0d5c16d38f441)。本目录是个人第 4 周练习的正式归档位置；团队 Route B 材料独立保存在 `week04_dorm_validation/`。

## 已完成的实际运行

2026-10-01 使用公开 [UCI 697](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success) 数据、本机已有 AI 根目录 `.venv` 执行：

- [app.py](app.py)：课堂第 5 节原版程序，七项输入；[完整输出](baseline_output.txt)。
- [challenge_app.py](challenge_app.py)：仅从模型 `columns` 输入列表移除三个第一学期字段，其他训练和测试设置与原版相同；[完整输出](challenge_output.txt)。
- [make_audit.py](make_audit.py)：从官方 CSV 独立复算数据规模、两版精确指标、十条留出集记录及版本，生成 [comparison.json](comparison.json)，并断言与课堂程序输出一致。若本地没有 `uci697_source.csv`，会从 UCI 官方地址下载。
- [individual_result.md](individual_result.md)：课程要求的指标、十条风险/建议/真实结果、输入重要性、挑战比较和解释边界。
- [evidence/](evidence/)：课堂原版与挑战版的真实命令、前十例、指标和退出码截图，以及实际子进程运行 JSON。截图是本机浏览器终端展示的 Python 输出，不称原生 PowerShell 截图。

本次课堂原版准确率 83.1%、退学召回率 74.6%；四输入挑战版为 66.2%、61.6%；全部预测为“未退学”的基准为 67.9%、0.0%。测试集 885 行，其中实际退学 284 行。原始官方 CSV 共 4,424 行，SHA-256 见结果页。

## 复现

在正式 AI 项目根目录已有的 `.venv` 安装依赖，无需新建虚拟环境：

```powershell
& '.venv\Scripts\python.exe' -m pip install -r requirements.txt
```

进入本目录后执行：

```powershell
$aiPython = (Resolve-Path -LiteralPath '..\.venv\Scripts\python.exe').Path
& $aiPython app.py
& $aiPython challenge_app.py
& $aiPython make_audit.py
```

三个程序均已实际以退出码 0 完成。两个课堂程序各联网读取一次 UCI；审计脚本优先使用本地 CSV。原始公开 CSV 没有纳入仓库；首次运行审计脚本时会从官方地址下载到本目录，`.gitignore` 已排除它。报告保留官方 URL 与本次 SHA-256。所有“新学生”均为公开数据随机留出集中的模拟记录，未进行真实用户招募或前瞻验证。

个人课程卡仍为只读、显示未提交；与第 2、3 周的课程平台状态见[个人提交清单](../docs/submission/2026-10-01/INDIVIDUAL_SUBMISSION.md)。
