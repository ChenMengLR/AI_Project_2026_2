# 实时演示窗口

`live_demo.py` 是本次录屏所用的实时显示器。它展示输入缩略图，并在开始信号出现后实际启动 `app.py`，逐行展示子进程输出，最后读取本次真实结果和 `sorted/` 图片。它不会预填或重放分类答案，不会显示或保存密钥。

在项目根目录，用已配置 `DASHSCOPE_API_KEY` 与 `DASHSCOPE_BASE_URL` 的同一终端启动。凭据只通过进程环境继承；不要把真实密钥写入命令行、此文档或录屏画面。

```powershell
.\.venv\Scripts\python.exe -m pip install -r tools\requirements-demo.txt
Remove-Item -LiteralPath .\week02_photo_classifier\runtime\demo\ai-demo-start.flag -ErrorAction SilentlyContinue
.\.venv\Scripts\python.exe tools\live_demo.py
```

窗口标题固定为 `AI Week02 Live Demo`，客户区 1280 × 720。脚本会自动创建 `week02_photo_classifier/runtime/demo/`，并在窗口准备好时写 `ai-demo-ready.json`。开始录屏后，从另一个位于项目根目录的终端创建开始信号：

```powershell
New-Item -ItemType File -Force -Path .\week02_photo_classifier\runtime\demo\ai-demo-start.flag
```

这会真正发送图片请求并消耗模型额度。执行结束后窗口展示本轮分类结果，保持 10 秒再写入 `ai-demo-complete.json`；之后可停止录屏并关闭窗口。每次重录前删除旧开始信号，避免窗口启动后立即发请求。

只看布局而不发请求，可执行：

```powershell
.\.venv\Scripts\python.exe tools\live_demo.py --preview-only
```

`--preview-only` 不会响应开始信号，也不会运行 `app.py`。已有课程录屏在 `week02_photo_classifier/evidence/`，具体真实性说明见同目录 `README.md`。
