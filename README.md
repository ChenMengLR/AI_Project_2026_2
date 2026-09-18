# AI_Project_2026_2 课程环境

## 当前交接入口

新窗口请先打开本项目根目录并阅读 [HANDOFF.md](HANDOFF.md)。第 3 周规则问答机器人的课程总结在 [docs/Week03_Rule_QA_Summary.md](docs/Week03_Rule_QA_Summary.md)，状态记录在 [docs/status/Week03_STATUS.md](docs/status/Week03_STATUS.md)，总结图在 [docs/Week03_Rule_QA_Summary.png](docs/Week03_Rule_QA_Summary.png)。

第 3 周个人代码位于 `week03_rule_chatbot/`，共用根目录 `.venv`。当前代码和离线测试已经建立；真实 Qwen 调用需要在本机 `.env` 中配置自己的密钥和同地域 Base URL。`.env` 不上传 GitHub。

项目位置：`C:\Users\31797\Desktop\AI_Project_2026_2`

2026-09-17 已真实调用 `qwen3.8-flash`，完成 5 张课堂样例和 2 张新增公开授权图片的分类：7 张成功、0 张失败，全部与预期标签一致。输入原图保留，分类副本已核对 SHA-256。仓库已公开，教师无需登录即可访问；本次使用一次性进程环境变量提供密钥，未将密钥写入项目。

最新运行证据见 [真实调用记录](week02_photo_classifier/RUNTIME_EVIDENCE.md)，课程提交情况见 [个人作业状态](week02_photo_classifier/SUBMISSION.md)。旧课程指南中的待配置/未实测描述属于准备阶段记录，以这两份最新说明为准。

[59.90 秒真实运行视频](week02_photo_classifier/evidence/Week02_Qwen_Live_Demo.mp4) 已录制，包含输入、实际命令、实时输出与分类副本；[原始窗口录像](week02_photo_classifier/evidence/Week02_Qwen_Raw_Capture.mp4) 一并保留。AI 的 Notion 第 2 周页目前只读，视频与链接已备齐，但课程平台尚未提交。

## 课程说明与作业模板

- [完整课程操作说明](COURSE_GUIDE.md)：软件安装、课堂流程、API 配置、GitHub 提交上传、作业提交及常见问题。
- [Word 版课程说明](docs/第2周QwenVision课程操作说明.docx)：共 8 页，首页为上课速查。
- [作业与录屏模板](week02_photo_classifier/SUBMISSION.md)：个人提交、团队方案和第 3 周汇报准备。
- [分类结果记录表](week02_photo_classifier/results.csv)：7 张图片的预期标签、真实返回与核对结果。
- [课堂样例及两张新增图片来源](week02_photo_classifier/SAMPLE_SOURCES.md)。新增图片由助手选取公共领域/CC0素材，不是本人摄影。
- [安全运行脚本](Run-Classifier-Secure.ps1)：在本机隐藏输入 API key，仅供本次进程使用，不保存到文件。

## 已安装与配置

- Python 3.14.7（64 位）和根目录 `.venv`。
- `openai==3.14.1`、`python-dotenv==1.2.3`；完整依赖版本见 `requirements.txt`。
- Git for Windows 2.55.0.windows.5；本地仓库已初始化为 `main`。
- VS Code 1.138.0；微软 Python 扩展及其配套扩展已安装。
- `.vscode/settings.json` 指定本项目 `.venv` 解释器。
- 根目录 `.gitignore` 忽略 `.env`、`.venv/`、新增的 `sorted/` 生成文件和 Python 缓存。本次已验证的 7 张分类副本已定向加入版本库，便于教师查看结果。

## 第一次使用

1. 用 VS Code 的“文件 → 打开文件夹”打开本项目根目录。
2. 编辑 `week02_photo_classifier/.env`，填入自己从同一个 Singapore Model Studio 工作空间复制的两项：

   ```dotenv
   DASHSCOPE_API_KEY=自己的密钥
   DASHSCOPE_BASE_URL=自己的OpenAI兼容端点
   ```

   端点使用 HTTPS 并以 `/compatible-mode/v1` 结尾。不要把密钥发送到聊天、上传 GitHub 或展示在录屏中。
3. `week02_photo_classifier/input/` 已准备好 5 张课堂示例图片和 2 张新增公开素材，共 7 张。也可替换为自己有权使用的测试图片。
4. 双击根目录的 `Open-Course.cmd`，会打开已激活虚拟环境、已进入本周目录的 PowerShell。
5. 在该窗口运行本地检查（不联网）：

   ```powershell
   python app.py --check
   ```
6. 确认 Model Studio 免费额度、有效期及 Free Quota Only / Stop-on-Exhaust 开关后，运行一次文本连接测试：

   ```powershell
   python app.py --test-api
   ```

   这一步会向自己配置的 Qwen 端点发送一个简短文本请求，可能消耗 API 额度。
7. 执行分类：

   ```powershell
   python app.py
   ```

   这一步会将 `input/` 内支持的图片逐张发送给 Qwen。原图保留，分类副本写入 `sorted/`。图片格式支持 JPG、JPEG、PNG、WebP。

## 手动进入环境

在 PowerShell 中执行：

```powershell
cd C:\Users\31797\Desktop\AI_Project_2026_2
.\.venv\Scripts\Activate.ps1
cd .\week02_photo_classifier
python app.py --check
```

也可以不激活，直接指定解释器：

```powershell
& 'C:\Users\31797\Desktop\AI_Project_2026_2\.venv\Scripts\python.exe' 'C:\Users\31797\Desktop\AI_Project_2026_2\week02_photo_classifier\app.py' --check
```

旧的 VS Code / Codex 进程可能仍持有修改前的 PATH；重新打开应用或使用上面的启动入口即可。不要把 `.venv` 移到别处继续使用，迁移后应重新创建并通过 `requirements.txt` 安装依赖。

## Git 与 GitHub

本课程仓库使用 `main` 分支。每次完成一部分实践后，先保存文件、检查修改与暂存清单，再创建提交并上传。`git remote -v` 可查看本机连接的远程仓库。

```powershell
cd C:\Users\31797\Desktop\AI_Project_2026_2
git status
git add .
git diff --cached --name-only
git commit -m "说明本次完成的内容"
git push
```

不要提交 `.env`。`.gitignore` 不会自动停止跟踪已经提交过的密钥文件。`input/` 中后续加入的图片可能出现在暂存清单，上传前要确认图片适合提交。

## 在其他电脑恢复课程环境

安装 Python 3.14、Git 和 VS Code，并克隆本仓库。在克隆得到的课程根目录执行：

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

第一次使用时，可运行 `Run-Classifier-Secure.ps1` 临时输入自己的密钥；也可将 `week02_photo_classifier/.env.example` 复制为同目录的 `.env` 并填写自己的密钥和端点，如果已有 `.env`，不要覆盖它。`.venv` 和真实 `.env` 不在仓库中，需要在新电脑重新准备。仓库保留了本次验证的 7 张分类副本，后续仍应执行程序核对自己的真实结果。

## 与课堂示例的差别

`app.py` 保留五分类和复制原图的课程流程，并增加本地配置检查、文本连接测试、正确的 WebP MIME、按脚本位置定位输入，以及单张失败后继续处理。非法模型标签会明确报告为失败，不会冒充 `other`。真实调用的模型、响应标识、token 用量、耗时和图片哈希保存在 `runtime/`，不记录凭据或请求头。程序和演示由助手协助完成，不能据此声称为独立手动操作。

## 课程来源

- [第 2 周课程](https://app.notion.com/p/3cf7c00fe5ad8140b175c415d1613a7e)
- [第 2 周作业详情](https://app.notion.com/p/3cf7c00fe5ad812a8fbddc3749d02d75)
- [Model Studio 免费额度说明](https://www.alibabacloud.com/help/en/model-studio/new-free-quota)

作业详情要求每人提交自己的 GitHub 链接和 30–60 秒运行视频至个人作业卡；课程正文的截图说明与它存在差异。详情页截止日期写 2026-09-16，实际提交安排请以教师确认为准。
