# 第 2 周真实运行记录

2026-09-17 已完成真实文本 API 测试和 7 张图片的 Qwen 分类。北京时间 16:00:13–16:01:02 的分类执行归档为 `runtime/runs/20260917T080013012147Z.json`，实际返回模型为 `qwen3.8-flash`，7 张成功、0 张失败；共 17,979 个提示 token、14 个输出 token，合计 17,993 个 token。结果与预期全部一致，且每张 `sorted/` 副本与输入文件的 SHA-256 相同。该数值对应此归档，后续重跑会有独立用量与归档。

五张课堂样例实际输出依次为 `person`、`document`、`food`、`device`、`other`；新增苹果照片返回 `food`，新增键盘照片返回 `device`。新增两张均为助手选取的公开授权素材，非用户本人拍摄。

本次凭据仅传入一次性进程环境变量，不保存在 `.env` 或源代码中。离开该进程后再次运行，需要重新配置凭据。API 成功与课程平台提交分别核验。

随后已在北京时间 16:08:10–16:08:55 完成第二轮真实请求并录屏，归档为 `runtime/runs/20260917T080810042251Z.json`。第二轮仍为 7 张成功、0 张失败、全部与预期一致，17,993 个 token；输入与 `sorted/` 副本 SHA-256 再次逐一核对一致。两轮都返回 `qwen3.8-flash`，两轮图片请求合计 35,986 token（不包括独立文本连接测试）。

演示文件为 `evidence/Week02_Qwen_Live_Demo.mp4`，59.90 秒、1280 × 720、10 fps。它由助手实际操作并记录 `app.py` 的真实子进程输出，展示全部输入与分类副本。仅裁去 DPI 捕获的右侧/下侧黑边并缩放，没有时间剪辑或加速。原始录像为 `evidence/Week02_Qwen_Raw_Capture.mp4`，补充结果截图为 `evidence/Week02_Classification_Result.png`。可复用窗口源码在 `../tools/live_demo.py`（相对于本周目录）；详细启动方法见项目根目录 `tools/README.md`。

本地环境通过两轮真实执行和文本连接验证；本轮未单独执行 `--check`。录屏、代码和结果材料已上传公开 GitHub 仓库；AI Notion 个人卡截至目前仅可读，尚未提交。剩余待办为恢复 AI 卡编辑权限并完成课程平台提交。

`app.py --test-api` 会向所配置的模型发送一条简短文本请求，并写入 `runtime/api_test.json`。默认运行 `app.py` 会将 `input/` 中 7 张照片逐张发送给模型，成功后把原图副本保存到 `sorted/<实际类别>/`。

每次分类完成后，脚本生成以下文件：

- `runtime/last_run.json`：最近一次执行的逐图结果、输入 SHA-256、耗时、成功/失败数量，以及 API 实际返回的模型名称、响应 ID、请求 ID 和 token 用量。
- `runtime/classification_results.csv`：最近一次执行的平面表格，适合用 Excel 查看。
- `runtime/runs/<UTC时间>.json`：该次结果的归档，避免下次运行覆盖历史。

请求 ID 或用量字段为 `null` 表示服务没有返回该值，不应自行编造。失败记录保留异常类型和 HTTP 状态码，不保存原始错误正文。上述文件不记录 API 密钥、请求头或图片的 Base64 数据。`.env` 仍由 `.gitignore` 排除；也可只在一次性进程的环境变量中传入 `DASHSCOPE_API_KEY`，无需写入文件。

真实课程命令：

```powershell
python app.py --check
python app.py --test-api
python app.py
```

`--check` 只做本地检查，不会生成真实分类结果。离线测试中的假客户端结果不代表真实 API 验证，不能用它提交作业。

`results.csv` 已填写第二轮真实结果，并保留两轮独立 JSON 归档。59.90 秒真实运行视频已完成；剩余步骤是最终推送材料并核验链接，在 AI Notion 编辑权限生效后将 GitHub URL 与视频提交至个人卡。
