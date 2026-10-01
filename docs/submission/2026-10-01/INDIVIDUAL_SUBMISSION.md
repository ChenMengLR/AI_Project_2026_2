# 个人作业成果与课程平台状态 · 2026-10-01

姓名：WANGHAOBIN。正式公开仓库：[AI_Project_2026_2](https://github.com/ChenMengLR/AI_Project_2026_2)，[最新提交记录](https://github.com/ChenMengLR/AI_Project_2026_2/commits/main)。本页同时是三个个人周次的链接清单；团队项目另见 [小组提交记录](TEAM_SUBMISSION.md)。

**个人第 2、3、4 周作业已于 2026-10-01 登记到课程 Notion。** [本人个人卡](https://app.notion.com/p/Wang-Haobin-3db7c00fe5ad8143b6aad5a41dbe3cd6)的 `GitHub Repository` 已填写公开仓库；三个周次的 `Submission Date` 均为实际登记日 `2026-10-01`，`Submission Status` 均显示 `제출 · 已提交`。逐卡写入后已重新加载页面，核对字段和正文保留。此前只读、未提交时拍摄的 [PERSONAL_WEEK02_UNSUBMITTED.jpg](PERSONAL_WEEK02_UNSUBMITTED.jpg) 仅作历史记录，不代表当前状态。课程显示已提交不等于教师已批阅或认可展示媒介。

## 第 2 周：图片分类

- [课程个人第 2 周卡](https://app.notion.com/p/2-2-3dd7c00fe5ad81619a5be5287cf82be6)；[代码与输入](../../../week02_photo_classifier/)；[运行结果](../../../week02_photo_classifier/RUNTIME_EVIDENCE.md)。
- [59.90 秒真实运行视频](../../../week02_photo_classifier/evidence/Week02_Qwen_Live_Demo.mp4)，[原始录像](../../../week02_photo_classifier/evidence/Week02_Qwen_Raw_Capture.mp4)。已实际调用 Qwen 分类 5 张课堂样例和 2 张新增公开素材，7/7 处理成功。该视频已在公开 GitHub 上通过匿名访问核验。
- 课程卡已填写：`GitHub Repository` 为上述公开仓库；`Demo Video` 为上述 59.90 秒视频的公开 GitHub 链接；正文写明 7/7 成功。`Submission Date` 为 `2026-10-01`，`Submission Status` 为 `제출 · 已提交`，重新加载后核对保存。

## 第 3 周：规则问答

- [课程个人第 3 周卡](https://app.notion.com/p/3-3-3dd7c00fe5ad81e89614d21a037ca82a)；[程序](../../../week03_rule_chatbot/app.py)；[韩文规则原文](../../../week03_rule_chatbot/rules.txt)；[运行说明](../../../week03_rule_chatbot/README.md)。
- 三题真实 Qwen 运行画面：[电热水壶](../../../week03_rule_chatbot/evidence/2026-10-01/Test1_Kettle_Live.png)、[访客](../../../week03_rule_chatbot/evidence/2026-10-01/Test2_Visitor_Live.png)、[规则外打印机](../../../week03_rule_chatbot/evidence/2026-10-01/Test3_Printer_Live.png)。同目录保留对应 JSON、退出码、执行时间和程序 SHA-256。
- 截图来自**本机浏览器终端展示的实际 Python 子进程输出**，并非原生 PowerShell 窗口。模型初次遗漏第 17 条申请条件；修复后程序依规则原文确定性补全第 11、17 条，原始问题与修复过程见 [首次 QA 记录](../../../week03_rule_chatbot/evidence/2026-10-01/INITIAL_QA_NOTE.md)。最终三题均实际调用 Qwen，退出码为 0；7 项离线测试通过。是否接受这种截图媒介由课程方决定。
- 课程卡已填写：仓库 URL、三题公开截图链接、最新提交链接和运行说明均在正文；`Submission Date` 为 `2026-10-01`，`Submission Status` 为 `제출 · 已提交`，重新加载后核对保存。本周采用截图展示，未另录视频，故 `Demo Video` 字段留空。

## 第 4 周：UCI 退学预测个人练习

- [课程个人第 4 周卡](https://app.notion.com/p/4-4-3ea7c00fe5ad81f1b52cdb6bcd21176a)；[课堂原版程序](../../../week04_dropout_prediction/app.py)；[四输入挑战版](../../../week04_dropout_prediction/challenge_app.py)；[个人结果报告](../../../week04_dropout_prediction/individual_result.md)。
- 课堂原版真实运行：[命令与前十例](../../../week04_dropout_prediction/evidence/Baseline_Command_And_Cases.png)、[指标与退出码](../../../week04_dropout_prediction/evidence/Baseline_Metrics.png)。挑战版：[命令与前十例](../../../week04_dropout_prediction/evidence/Challenge_Command_And_Cases.png)、[指标与退出码](../../../week04_dropout_prediction/evidence/Challenge_Metrics.png)。同目录有原始运行 JSON；[审计数据](../../../week04_dropout_prediction/comparison.json)可复核全部留出集指标。
- 公开 UCI 697 数据共 4,424 行，885 行留出测试。课堂七输入模型准确率 83.1%、实际退学召回率 74.6%；四输入挑战版为 66.2%、61.6%；全部预测未退学的基准为 67.9%、0.0%。十条示例的风险、建议与真实标签、输入重要性及解释限制均写入报告。截图媒介与第 3 周相同，实际程序均退出码 0。
- 课程卡已填写：仓库 URL、个人结果报告、四张公开运行截图、最新提交链接和主要指标；`Submission Date` 为 `2026-10-01`，`Submission Status` 为 `제출 · 已提交`，重新加载后核对保存。本周采用截图展示，未另录视频，故 `Demo Video` 字段留空。团队 Route B 的材料不代替本个人练习。

## 提交复核与后续

课程页面目前可编辑，三个周次均已完成登记与刷新复核。第 3、4 周的截图是在本机浏览器终端中展示真实 Python 子进程输出；是否符合教师对截图媒介的最终要求，仍待课程方判断。提交日期是平台实际填写日期，不是原作业截止日期；教师批阅和成绩仍待确认。
