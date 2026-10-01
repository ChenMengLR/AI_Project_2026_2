# 个人作业成果与课程平台状态 · 2026-10-01

姓名：WANGHAOBIN。正式公开仓库：[AI_Project_2026_2](https://github.com/ChenMengLR/AI_Project_2026_2)，[最新提交记录](https://github.com/ChenMengLR/AI_Project_2026_2/commits/main)。本页同时是三个个人周次的链接清单；团队项目另见 [小组提交记录](TEAM_SUBMISSION.md)。

**GitHub 成果已准备并推送；课程个人作业库尚未提交。** [本人个人卡](https://app.notion.com/p/Wang-Haobin-3db7c00fe5ad8143b6aad5a41dbe3cd6)及下列三个周次当前对登录账号均为只读，课程字段仍为空，状态显示 `미제출 · 未提交`。用户已确认暂时无法开通编辑权限。因此这里不填写虚构的课程提交日期，也不把团队卡或其他工作区副本当作个人提交。第 2 周页面状态的实际截图见 [PERSONAL_WEEK02_UNSUBMITTED.jpg](PERSONAL_WEEK02_UNSUBMITTED.jpg)。

## 第 2 周：图片分类

- [课程个人第 2 周卡](https://app.notion.com/p/2-2-3dd7c00fe5ad81619a5be5287cf82be6)；[代码与输入](../../../week02_photo_classifier/)；[运行结果](../../../week02_photo_classifier/RUNTIME_EVIDENCE.md)。
- [59.90 秒真实运行视频](../../../week02_photo_classifier/evidence/Week02_Qwen_Live_Demo.mp4)，[原始录像](../../../week02_photo_classifier/evidence/Week02_Qwen_Raw_Capture.mp4)。已实际调用 Qwen 分类 5 张课堂样例和 2 张新增公开素材，7/7 处理成功。该视频已在公开 GitHub 上通过匿名访问核验。
- 课程卡待填：`GitHub Repository` 为上述公开仓库；`Demo Video` 为上述 59.90 秒视频。`Submission Date` 应在课程平台实际保存时填写，不使用开发或 GitHub 上传日期冒充。

## 第 3 周：规则问答

- [课程个人第 3 周卡](https://app.notion.com/p/3-3-3dd7c00fe5ad81e89614d21a037ca82a)；[程序](../../../week03_rule_chatbot/app.py)；[韩文规则原文](../../../week03_rule_chatbot/rules.txt)；[运行说明](../../../week03_rule_chatbot/README.md)。
- 三题真实 Qwen 运行画面：[电热水壶](../../../week03_rule_chatbot/evidence/2026-10-01/Test1_Kettle_Live.png)、[访客](../../../week03_rule_chatbot/evidence/2026-10-01/Test2_Visitor_Live.png)、[规则外打印机](../../../week03_rule_chatbot/evidence/2026-10-01/Test3_Printer_Live.png)。同目录保留对应 JSON、退出码、执行时间和程序 SHA-256。
- 截图来自**本机浏览器终端展示的实际 Python 子进程输出**，并非原生 PowerShell 窗口。模型初次遗漏第 17 条申请条件；修复后程序依规则原文确定性补全第 11、17 条，原始问题与修复过程见 [首次 QA 记录](../../../week03_rule_chatbot/evidence/2026-10-01/INITIAL_QA_NOTE.md)。最终三题均实际调用 Qwen，退出码为 0；7 项离线测试通过。是否接受这种截图媒介由课程方决定。
- 课程卡待填：仓库 URL、三题截图链接和最新提交链接。截图或演示视频是课程要求的展示媒介；本次提供截图，没有声称另录第 3 周视频。

## 第 4 周：UCI 退学预测个人练习

- [课程个人第 4 周卡](https://app.notion.com/p/4-4-3ea7c00fe5ad81f1b52cdb6bcd21176a)；[课堂原版程序](../../../week04_dropout_prediction/app.py)；[四输入挑战版](../../../week04_dropout_prediction/challenge_app.py)；[个人结果报告](../../../week04_dropout_prediction/individual_result.md)。
- 课堂原版真实运行：[命令与前十例](../../../week04_dropout_prediction/evidence/Baseline_Command_And_Cases.png)、[指标与退出码](../../../week04_dropout_prediction/evidence/Baseline_Metrics.png)。挑战版：[命令与前十例](../../../week04_dropout_prediction/evidence/Challenge_Command_And_Cases.png)、[指标与退出码](../../../week04_dropout_prediction/evidence/Challenge_Metrics.png)。同目录有原始运行 JSON；[审计数据](../../../week04_dropout_prediction/comparison.json)可复核全部留出集指标。
- 公开 UCI 697 数据共 4,424 行，885 行留出测试。课堂七输入模型准确率 83.1%、实际退学召回率 74.6%；四输入挑战版为 66.2%、61.6%；全部预测未退学的基准为 67.9%、0.0%。十条示例的风险、建议与真实标签、输入重要性及解释限制均写入报告。截图媒介与第 3 周相同，实际程序均退出码 0。
- 课程卡待填：仓库 URL、结果报告与截图链接、最新提交链接。团队 Route B 的材料不代替本个人练习。

## 完成课程登记所需的唯一外部步骤

课程个人卡的所有者须给当前账号编辑权，或提供课程认可的可编辑提交入口；随后将以上链接分别写入三周的 `GitHub Repository`、`Demo Video`/正文等适用字段，按实际保存日期填写 `Submission Date`，最后重新打开核验。**在课程平台可写并验证保存前，三周状态一律记为未提交。**
