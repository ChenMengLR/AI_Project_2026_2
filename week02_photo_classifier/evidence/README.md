# 第 2 周课程演示证据

- [Week02_Qwen_Live_Demo.mp4](Week02_Qwen_Live_Demo.mp4)：59.90 秒，1280 × 720，10 fps，适合课程提交。
- [Week02_Qwen_Raw_Capture.mp4](Week02_Qwen_Raw_Capture.mp4)：保留原始窗口录屏，便于核对。
- [Week02_Classification_Result.png](Week02_Classification_Result.png)：真实分类完成画面；作为补充，非课程新增必交项。

录像由助手实际操作并录制，显示输入 7 张图片、执行命令、`app.py` 子进程真实流式输出，以及 `sorted/` 实际分类副本。录像对应运行 `20260917T080810042251Z`，实际返回模型为 `qwen3.8-flash`，7 张成功、0 张失败。新增 2 张图片为公开授权素材，非 WANG HAOBIN 本人拍摄。

正式演示版仅裁去 Windows DPI 捕获产生的右侧、下侧黑边并缩放到 1280 × 720，没有时间剪辑或加速，没有把缓存答案冒充实时输出。原始视频保留。录屏全程没有显示密钥。

真实性证据见 `../runtime/runs/20260917T080810042251Z.json`；录屏显示工具的可复用源码在 `../../tools/live_demo.py`。
