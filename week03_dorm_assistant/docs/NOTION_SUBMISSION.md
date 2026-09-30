# Notion 提交草稿

本文已填入实际完成情况，可复制到项目卡。**Notion 尚未提交**：当前课程库未找到 WANGHAOBIN 卡，也没有新增入口；用户确认暂时没有可编辑项目卡。个人作业仍放个人卡。以下 GitHub 链接指向 main 分支，版本以仓库提交历史为准；仓库上传不等于课程提交。

## 项目概要（可复制）

**项目名称：宿舍入住准备助手**

**成员／负责人：WANGHAOBIN（一人）**

项目面向准备入住东亚大学 Hanlim 生活馆的学生，把公开入住说明转成带来源的准备清单。第一版只覆盖一个公开说明范围，支持 standard、international、unknown 三种配置。用户手动填写准备状态，或用自然语言描述情况，由 AI 提出建议后本人确认，再查看下一步行动并保存／导出。资料不足，特别是国际生文件要求，明确显示需确认。系统不验证材料真实性，也不判断入住资格。

官方资料：

- https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075
- https://dms.donga.ac.kr/hanlim/15139/subview.do

课程仓库：https://github.com/ChenMengLR/AI_Project_2026_2

项目代码：[week03_dorm_assistant](https://github.com/ChenMengLR/AI_Project_2026_2/tree/main/week03_dorm_assistant)。

Week 4 测试材料：[week04_feature_test.md](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week04_dorm_validation/week04_feature_test.md)。

## Week 3／Mission A 与 B 记录（可复制）

**Mission A：** 收录 15 条有来源的入住准备与规则条目，依据原文回答问题，资料不足明确无法确认。已执行 3 道资料内、2 道资料外合成问题的真实 Qwen 调用；相关条件遗漏经过检查与修复，首次结果保留。

**Mission B：** 入住准备状态核对与行动清单。用户输入准备情况 → AI 建议待本人确认／手动填写 → 核对缺项与未知 → 显示来源及行动 → 保存／导出。此功能与单纯规则问答不同。

**规格与流程：** [MISSION_B_SPEC.md](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week03_dorm_assistant/docs/MISSION_B_SPEC.md)。

**真实技术验证：** 36 项离线单元与 HTTP 检查通过；6 个确定性合成案例与 8 次真实 Qwen 调用完成，14/14 既定自动检查通过。8 次包括 5 道问答与 3 条准备状态提取；输入是合成情境，不是真实用户反馈。证据：[OFFLINE_TESTS.txt](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week03_dorm_assistant/evidence/OFFLINE_TESTS.txt)、[LIVE_VALIDATION.md](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week03_dorm_assistant/evidence/LIVE_VALIDATION.md)。

**任务分工：** T1 来源与适用范围；T2 手动核对与保存导出；T3 AI 建议与证据问答；T4 五类测试、修复复测与演示。四项负责人均为 WANGHAOBIN，完成标准见功能规格。

**实际完成情况：** MVP、来源整理、手动核对、AI 建议确认、依据问答、保存与导出、技术及界面验收、复测与演示材料已完成。AI 未配置时手动核对仍可用。

**尚未完成：** 真实用户测试尚未开展；国际生专门材料与实际流程仍需进一步确认；Notion 尚未提交。

## Week 4 记录（可复制）

**选择 Route B：** 当前核对准备状态而不预测未来结果；没有历史真实审批标签，因此延续已有核心 AI 功能并做场景测试。

**本周核心流程：** 自然语言准备情况 → AI 状态建议 → 用户确认 → 有来源的清单和下一步行动。

**Prediction 五问与 AI 功能卡：** [week04_feature_test.md](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week04_dorm_validation/week04_feature_test.md)。

**五类测试：** normal、missing、ambiguous、out-of-scope、privacy-security。输入均由人工合成，保留具体输入、预期、实际结果和证据类型。

**已执行内容：** normal 的日期核对与完整界面流程已验收；M01、A01、O01、P01 的确切输入另行完成 4 次真实 Qwen 调用，保守状态／拒答检查通过。A01 返回 9 个 unknown，无 ready；P01 返回空建议。界面确认前床品保持 missing、确认后变 ready；国际生两项材料保持 confirm；刷新恢复和实际下载通过，导出 total=9、待确认=2、床品 ready，且不含自由文本。证据：[WEEK04_LIVE_CASES.json](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week03_dorm_assistant/evidence/WEEK04_LIVE_CASES.json)、[QA_REPORT.md](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week03_dorm_assistant/docs/QA_REPORT.md)、[UI_EXPORTED_REPORT.json](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week03_dorm_assistant/evidence/UI_EXPORTED_REPORT.json)。

**真实问题、修复与复测：** ① 首次禁带用品回答漏健康用途询问条件，现固定补充相关条件；② 未来出具日期不应表示已准备，现返回 invalid_date；③ 出入证答复需要两处来源，现保留双来源引用。离线、真实输出及界面复测见 QA 报告；首次输出保留在 [INITIAL_VALIDATION.md](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week03_dorm_assistant/evidence/INITIAL_VALIDATION.md)。

**AI 真实调用状态：** 8 次基础调用与 4 次 Week 4 专项调用成功；实际模型与输出保存在上述证据文件。问答自动检查覆盖回答／拒答和必要引用，不能把通过次数解释为通用准确率。

**真实用户测试：** 尚未开展；暂时没有真实参与者，已准备招募说明、任务卡和空白记录模板。合成场景与自动化检查不作为真实用户反馈。

**当前阻碍：** 国际生文件要求在已收录资料中不足；真实用户暂不可用；课程库当前没有找到 WANGHAOBIN 项目卡或新增入口，需要可编辑卡链接。

**下一目标与验收：** 确认国际生实际流程与适用材料，补上可追溯官方依据；仍不明确的项目继续标为未知。明确真实试用范围、准备好任务卡后再招募，独立记录真实操作与反馈。

**5 分钟汇报材料：** [DEMO_SCRIPT.md](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week03_dorm_assistant/docs/DEMO_SCRIPT.md)，按 1 分钟 Mission A、2 分钟 Mission B、2 分钟问题与计划组织。真实试用材料：[USER_TEST_KIT.md](https://github.com/ChenMengLR/AI_Project_2026_2/blob/main/week03_dorm_assistant/docs/USER_TEST_KIT.md)。

## 当前提交状态

- Notion：**未提交**，没有伪造项目卡、保存时间或完成状态。
- 下一提交动作：用户提供可编辑项目卡链接后，将项目概要与对应周记录填入，重新打开验证保存与链接访问。
- GitHub：上述链接指向项目代码、作业正文与运行证据；版本及提交时间以仓库 main 分支的 Git 历史为准。

## 课程来源

- [小组项目卡入口](https://app.notion.com/p/3b780cfda16646888fd0f6016c10069c?v=2fa0947ee73241688fda9eaf20db2675)
- [Week 3：Mission A/B](https://app.notion.com/p/Q-A-3cf7c00fe5ad814c949bfbe5411c447a)
- [Week 4：功能测试与汇报](https://app.notion.com/p/AI-AI-3cf7c00fe5ad819fa18fe0b6fa0a70bd)
