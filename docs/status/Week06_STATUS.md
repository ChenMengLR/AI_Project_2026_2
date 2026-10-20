# Week 06 状态：连续问答与多文档检索

最后更新：2026-10-20。负责人：WANGHAOBIN（一人项目）。本周课程页：[Conversation / Knowledge Retrieval](https://app.notion.com/p/Conversation-Knowledge-Retrieval-3cf7c00fe5ad8106ab03f66f1a6c00fe)。小组与个人成果严格分开。

## 已完成的小组项目

- `week03_dorm_assistant/conversation.py`、`app.py` 和网页加入连续对话、最近三轮问题／引用上下文、Qwen 独立问题改写及韩文检索词、15 条宿舍知识检索、条款与官方 URL 展示。缺少匹配条款时停在 retrieval 阶段；命中但不能回答时停在 answer 阶段。
- 健康用途咨询、材料开具期限等必要条件随主题条款保留；出入证“领取”和“佩戴”展示两条来源。中文与韩语界面均实际运行，切换语言清空对话但不清空准备状态。
- 结构说明、15 条索引、三类必需情境及额外改述情境在 [`../../week06_knowledge_qa/TEAM_STRUCTURE.md`](../../week06_knowledge_qa/TEAM_STRUCTURE.md) 和 [`TEAM_RESULTS.md`](../../week06_knowledge_qa/TEAM_RESULTS.md)。实际 Qwen JSON、四张浏览器截图与注明“截图剪辑”的小组 MP4 位于 [`week06_knowledge_qa/evidence/`](../../week06_knowledge_qa/evidence/)。

## 已完成的个人独立练习

- `week06_knowledge_qa/app.py` 独立解析课堂要求的三个文件、22 个条款；Qwen 处理韩语和中文追问，返回最多三个检索条款、`[S1]` 引用和回答。每条 URL 单独映射，禁带物品的关键结论由已核对条款校验，保留模型原文供审计。
- 七次实际 Qwen 情境输出：韩文水壶→冰箱追问→洗衣用品，中文烧水设备→冰箱追问，奖学金无命中，打印机位置；详见 [`PERSONAL_RESULTS.md`](../../week06_knowledge_qa/PERSONAL_RESULTS.md) 与 `evidence/2026-10-20_Qwen_cases.jsonl`。
- 第六周个人结果展示视频保存在 `week06_knowledge_qa/evidence/Week06_Personal_Qwen_Results.mp4`。它按真实运行记录制作，不冒充连续终端录屏。

## 本次检查

- `python -m unittest discover -s tests -q`：72 项通过。
- `node --check week03_dorm_assistant/static/app.js`、小组 `app.py --check`、个人 `app.py --check`、`git diff --check` 通过。
- 小组真实 Qwen 最终复测：5 个问答调用，电热水壶与冰箱追问命中禁带＋健康用途条款，奖学金问题无命中且不编造，烧水设备改述命中相关条款。个人真实 Qwen：7 条，6 条有来源回答、1 条检索阶段拒答。结果见原始 JSON／JSONL，不能外推为总体准确率。
- 本机网页浏览器实际完成中文三情境和韩语界面测试，截图可查。没有真实用户试用。

## 提交与剩余工作

- 第六周小组 Notion 卡：[06주차 · 第6周](https://app.notion.com/p/06-6-0697c00fe5ad83148635017fc48c39dc)。个人第六周卡及刷新核验结果见本周提交记录（提交后补入）。
- 公开网站 URL 尚未建立；`127.0.0.1` 是本机演示地址。第五周教师对此有反馈，不能声称已解决。
- `notice_printer.txt` 的具体打印机表格来自课程提供的官网摘要，尚未独立从网页表格核实；宿舍知识目录整体核对日为 2026-09-30。留学生材料适用性、个人资格、实时学期安排仍需学校确认。
- 真实住校生试用、教师批阅和第七周现场汇报尚未开展。第七周英文初稿与课堂时间另见交接说明；邮件需由本人发送。
