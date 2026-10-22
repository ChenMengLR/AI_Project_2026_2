# Week 07 状态：让 AI 承担新通知解读任务

最后更新：2026-10-22。负责人：WANGHAOBIN（一人项目）。课程周页与论文截止另见 [`../../week07_creative_award/README.md`](../../week07_creative_award/README.md)。

## 对导师意见的处理

第六周版本的知识问答以预先整理的 15 条索引和固定清单为主；AI 的存在不足以说明项目核心价值。第七周将主要演示流程调整为：**输入尚未收录的韩文宿舍通知 → Qwen 提取中韩双语行动、对象、期限和例外 → 展示原文片段与本地自报状态 → 用户核对适用性**。没有模型时，手动清单仍可使用，但新通知无法自动转成行动候选。导师陈述与 90 秒演示顺序见 [`../../week07_notice_interpreter/MENTOR_BRIEF.md`](../../week07_notice_interpreter/MENTOR_BRIEF.md)。

## 已完成

- `week07_notice_interpreter/notice.py` 和小组网页新增 `/api/notice/interpret`。模型只收到通知文字与非个人化清单标题；身份、状态、来源 URL 不进入模型输入。后端验证返回结构、项目 ID、原文引文及条件片段是否位于同一证据段；不自动修改清单或判定资格。
- 网页首页增加中文／韩语通知输入、模拟样例、来源链接（仅供用户自行核对）、结果卡片、原文、范围／期限／例外、AI 推测的清单关联与自报状态。切换语言会清空旧 AI 结果，准备状态保留。
- 针对模型漏掉限制句的风险，增加保守的韩文关键词提示；若疑似例外句未出现在任何返回证据片段，显示原句供核对。该规则非语义验证，也不能覆盖所有措辞。
- 英文第七周论文初稿已改写成新任务主线，并保留失败案例和评估限制。Word 本机导出三页 PDF 后逐页目视检查，未发现裁切、重叠或缺字。技能自带的 LibreOffice 渲染器因缺少 `soffice.exe` 无法运行，故此次使用 Word 导出核验。
- 新增 `week07_notice_interpreter/WANGHAOBIN_AI_English_Pronunciation_2page.docx`，供现场英文汇报提词：每句按“汉字近似发音／英文／中文意思”排列，标有演示动作和一句听不清时的求助语。用本机 Word 导出并逐页目视核对为两页；文稿如实区分两份模拟通知、模型漏例外以及尚无真实学生试用。
- 按新的汇报长度要求增加 `week07_notice_interpreter/WANGHAOBIN_AI_English_Original_2page.docx` 与 `week07_notice_interpreter/WANGHAOBIN_AI_Bilingual_Pronunciation_Guide.docx`：前者仅英文讲稿及不朗读的操作提示，经 Word 导出核验为两页；后者逐句提供汉字近音、相同的英文原句及中文意思，经导出核验为三页。两份文档的 34 句英文原文逐句一致。旧版两页发音稿仍保留供精简练习。
- 已录制并导出 `week07_notice_interpreter/evidence/Week07_AI_Live_Browser_Demo_20261022.mp4`：89.16 秒英文步骤字幕、无口头旁白的 H.264 演示，附真实浏览器连续录屏 WebM 和调用计数 JSON。视频展示三次实际 Qwen 调用：第一份虚构通知中文结果 2 项，切换韩语后重跑结果 3 项，第二份 QR 通知结果 1 项且页面提示一条模型遗漏的可能例外。MP4 的片头、片尾与 4 秒警示定格属后期说明；不将它们称为连续录屏或真人试用。

## 实际证据与核验

- `live_demo_2026-10-20.json`：真实 Qwen 调用，对教学虚构通知返回三项，首项包含留学生例外及期限。
- `blind_initial_2026-10-20.json`：未用于初始提示词调整的 QR 通知首测；识别东馆对象、期限及西馆例外，但漏掉“已登记无需重复”。
- `blind_guarded_2026-10-20.json`：最终复测仍漏该句，程序在 `uncovered_caveats` 单独提示原文。不能把此结果称为 AI 已可靠识别例外。
- 真实 HTTP POST 到新接口返回三项、例外片段与 `review_required=true`。本机网页实际完成中文输入→结果、韩语切换→重新解读；韩语界面截图见 `week07_notice_interpreter/evidence/Week07_Korean_Notice_UI.png`。
- 2026-10-22 视频已解码全片并抽帧目视核验：1440×900、25 fps、H.264/AAC 静音，时长 89.16 秒；英文字幕、警示和人工核对说明清晰可见。SHA-256：`5B7C31C57BD476661865DE045C5345876F88FED24223647D12E92ED03845EB78`。录制未展示 `.env` 或密钥。
- `python -m unittest discover -s tests -q`：**81 项通过**；`node --check week03_dorm_assistant/static/app.js`、`app.py --check`、`git diff --check` 通过。

## 尚未完成

- 未使用有独立人工标注的当期真实通知评价准确率、错误待办、遗漏例外或与固定索引／关键词基线的差异；两份合成文本只能验证工程链路。
- 未招募真实住校生试用；没有公开部署。通知链接由用户提供，程序未抓取验证。模型释义、清单匹配和条件关联仍需人工核对。
- 2026-10-22 已将英文初稿 DOCX 和 89 秒演示 MP4 上传[第 7 周小组卡](https://app.notion.com/p/07-7-54e7c00fe5ad83e89179017b8a90748f)，刷新后附件和字段保留，视频可播放；同日从本人 Gmail 向课程指定邮箱发送两份附件，已发邮件记录显示 14:09 北京时间。详情见[提交记录](../submission/2026-10-22/TEAM_WEEK07_SUBMISSION.md)。文稿发送晚于课程页所列截止时间，不等于教师接受。
- WANGHAOBIN 的机构与学生 Gmail 已填入 DOCX；Bora Youn 的机构仍待确认，文稿保留占位说明并在邮件中告知。Zoom 现场汇报与教师批阅尚未核实，课程卡状态保留“进行中”。
