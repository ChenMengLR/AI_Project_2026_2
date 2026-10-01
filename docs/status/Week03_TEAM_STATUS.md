# Week 03 团队项目状态

最后更新：2026-10-01。负责人：WANGHAOBIN，一人，无组名。

## 已完成

- `week03_dorm_assistant/`：入住有数，Python 本机服务与中文 Web 界面。
- 15 个知识条目、12 条教学规则、3 个官方来源；Mission A 的 3 可答＋2 不可答真实 Qwen 验证。
- Mission B 规格、流程、4 项同一负责人任务、真实 AI 状态理解、确认、规则检查、保存导出。
- `week04_dorm_validation/week04_feature_test.md`：Route B、五问、功能卡、5 类场景。
- 真实用户测试材料已准备，用户明确暂时找不到试用者。
- 2026-10-01 已提交 [Notion 第 3 周记录](https://app.notion.com/p/03-3-a6a7c00fe5ad8349aab301d526212c47)，包含 Mission A/B、真实证据、规格流程、4 项任务及后续限制。重新打开后正文、链接和“已完成”状态均保留。第 2 周方案也已按实际日期补录，详见 [提交记录](../submission/2026-10-01/TEAM_SUBMISSION.md)。

## 验证与证据

- 36 项离线单元／HTTP 集成检查，输出 `week03_dorm_assistant/evidence/OFFLINE_TESTS.txt`。
- 实际模型 `qwen3.8-flash`。6 个确定性案例＋8 次真实调用的14个自动检查，以及4次Week4真实输入检查。
- 浏览器端验证确认前后状态、保存恢复、实际导出、留学生范围与无AI模式。
- 首次模型条件遗漏、未来日期、双来源三个问题已修复，见 `week03_dorm_assistant/docs/QA_REPORT.md`。

## 尚未发生的事

- 真实用户测试、教师反馈、期中和期末现场汇报。
- 教师对一人项目安排的正式确认及作业批阅；Notion“已完成”只代表材料已登记。
- 国际生特殊材料要求未找到明确来源，产品保持待确认。

## 启动

双击 `week03_dorm_assistant/Start.cmd`，打开 http://127.0.0.1:8765 。沿用根共享 `.venv` 和容器根 `.env`；未修改既有 Week 2、个人 Week 3 程序。

后续按新周创建同级记录并引用本项目，不覆盖个人状态。未经真实执行，不将用户测试、提交或汇报标为完成。
