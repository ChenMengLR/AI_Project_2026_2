# AI_Project_2026_2 课程环境

项目位置：`C:\Users\31797\Desktop\AI_Project_2026_2`

本地 Python 环境、依赖、启动入口和 GitHub 仓库已部署，5 张课堂示例图片已准备好；仍需填写 Qwen 密钥与接口地址，并自行补充 2–3 张新图片。尚未进行真实 Qwen 调用，也未完成真实分类、录屏或课程作业提交。

## 课程说明与作业模板

- [完整课程操作说明](COURSE_GUIDE.md)：软件安装、课堂流程、API 配置、GitHub 提交上传、作业提交及常见问题。
- [Word 版课程说明](docs/第2周QwenVision课程操作说明.docx)：共 8 页，首页为上课速查。
- [作业与录屏模板](week02_photo_classifier/SUBMISSION.md)：个人提交、团队方案和第 3 周汇报准备。
- [分类结果记录表](week02_photo_classifier/results.csv)：样例预期类别已填写，实际结果等待真实运行。
- [五张课堂样例来源](week02_photo_classifier/SAMPLE_SOURCES.md)。

## 已安装与配置

- Python 3.14.7（64 位）和根目录 `.venv`。
- `openai==3.14.1`、`python-dotenv==1.2.3`；完整依赖版本见 `requirements.txt`。
- Git for Windows 2.55.0.windows.5；本地仓库已初始化为 `main`。
- VS Code 1.138.0；微软 Python 扩展及其配套扩展已安装。
- `.vscode/settings.json` 指定本项目 `.venv` 解释器。
- 根目录 `.gitignore` 忽略 `.env`、`.venv/`、`sorted/` 和 Python 缓存。

## 第一次使用

1. 用 VS Code 的“文件 → 打开文件夹”打开本项目根目录。
2. 编辑 `week02_photo_classifier/.env`，填入自己从同一个 Singapore Model Studio 工作空间复制的两项：

   ```dotenv
   DASHSCOPE_API_KEY=自己的密钥
   DASHSCOPE_BASE_URL=自己的OpenAI兼容端点
   ```

   端点使用 HTTPS 并以 `/compatible-mode/v1` 结尾。不要把密钥发送到聊天、上传 GitHub 或展示在录屏中。
3. `week02_photo_classifier/input/` 已准备好 5 张课堂示例图片；再自行放入 2–3 张新图片，共 7–8 张。
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

第一次使用时，将 `week02_photo_classifier/.env.example` 复制为同目录的 `.env` 并填写自己的密钥和端点；如果已有 `.env`，不要覆盖它。然后准备图片，使用 `Open-Course.cmd` 打开课程环境。`.venv`、真实 `.env` 和 `sorted/` 不在仓库中，需要按上述步骤在新电脑重新准备。

## 与课堂示例的差别

`app.py` 保留五分类和复制原图的课程流程，并增加本地配置检查、文本连接测试、正确的 WebP MIME、按脚本位置定位输入，以及单张失败后继续处理。非法模型标签会明确报告为失败，不会冒充 `other`。这些是运行可靠性补充，不代表已经完成课堂实测或作业。

## 课程来源

- [第 2 周课程](https://app.notion.com/p/3cf7c00fe5ad8140b175c415d1613a7e)
- [第 2 周作业详情](https://app.notion.com/p/3cf7c00fe5ad812a8fbddc3749d02d75)
- [Model Studio 免费额度说明](https://www.alibabacloud.com/help/en/model-studio/new-free-quota)

作业详情要求每人提交自己的 GitHub 链接和 30–60 秒运行视频至个人作业卡；课程正文的截图说明与它存在差异。详情页截止日期写 2026-09-16，实际提交安排请以教师确认为准。
