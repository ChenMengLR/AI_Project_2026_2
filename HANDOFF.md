# AI_Project_2026_2 交接说明

这是本课程项目的唯一共享工作区。新建 Codex 窗口、VS Code 窗口或终端都应打开同一个绝对路径：

```text
C:\Users\31797\Documents\ChatGPT\作业 3\AI_Project_2026_2
```

截图中出现“空 Git 仓库、没有 Week 2 项目”的原因，是新窗口的当前目录不是上面这个路径。不要在 `C:\Users\31797\Documents\Codex` 下面另建一个同名空目录来继续。

## 新窗口的启动步骤

1. 在 Codex 的项目/工作区选择中打开 `C:\Users\31797\Documents\ChatGPT\作业 3\AI_Project_2026_2`。
2. 如果窗口已经打开了错误目录，先关闭该项目，再用上面的绝对路径重新打开。
3. 在新窗口的第一个消息中要求它先执行并读取：

   ```text
   请先打开当前项目根目录下的 HANDOFF.md、README.md 和 docs/status/，再执行 Get-Location、git status --short --branch，并根据文件中的现状继续。不要凭聊天历史猜测项目状态，不要新建第二个 AI_Project_2026_2 目录。
   ```

4. 在 PowerShell 验证路径和文件：

   ```powershell
   Get-Location
   Get-ChildItem
   git status --short --branch
   git log -3 --oneline
   ```

   `Get-Location` 的最后一段应是 `AI_Project_2026_2`，并且能看到 `week02_photo_classifier`、`week03_rule_chatbot`、`README.md` 和本文件。

## 当前目录约定

```text
AI_Project_2026_2/
├─ HANDOFF.md                         # 每个新窗口先读的总交接文件
├─ README.md                          # 环境、运行和 Git 总入口
├─ COURSE_GUIDE.md                    # 课程安装与课堂流程
├─ requirements.txt                   # 根 .venv 的依赖
├─ .venv/                             # 本机虚拟环境；不上传
├─ .gitignore                         # 忽略 .env、.venv、缓存和生成目录
├─ week02_photo_classifier/           # 第 2 周个人练习：图片分类
│  ├─ app.py
│  ├─ input/
│  ├─ sorted/
│  ├─ runtime/
│  └─ evidence/
├─ week03_rule_chatbot/               # 第 3 周个人练习：规则问答
│  ├─ app.py
│  ├─ rules.txt
│  └─ .env                            # 仅本机，当前为空模板，需要本人配置
├─ tests/                             # 跨周离线测试
└─ docs/
   └─ status/                         # 每周状态和交接记录
```

每周课程使用一个同级目录 `weekNN_<topic>`，不要覆盖上一周目录，也不要在周目录中再建 `.venv`。所有周目录共用根目录 `.venv`。现在统一在“作业 3”容器根目录放置一份 `.env`，由第 2、3 周和后续 AI 任务共同读取；AI 项目根目录及周目录中的 `.env` 只作为兼容性回退，但 `.env` 永远不进入 GitHub。

## 多个任务如何互相读取

- **共享读取**：所有任务打开同一根目录，就能读取前几周代码、运行证据、README 和 `docs/status/`。
- **共享写入**：同一时刻只让一个窗口修改同一个工作区。多个窗口同时写同一文件会产生未提交修改互相覆盖或 Git 冲突。
- **任务边界**：新周只新建自己的 `weekNN_<topic>`；需要引用上一周时读取，不直接重写上一周代码。
- **状态同步**：完成一项工作后，在 `docs/status/WeekNN_STATUS.md` 写“已完成、证据、测试、待办”，然后再提交 Git。
- **提交节奏**：每个可检查里程碑一个 commit。新窗口先运行 `git status`，看到上一个窗口有未提交修改时，先读取并验证，不要直接 `git reset` 或删除。
- **并行开发**：如果确实要并行修改，给每个任务建立独立 Git worktree；不要让多个窗口共用同一个可写工作区。仅需要顺序完成课程作业时，使用同一个本地项目根目录更简单。

## 凭据和安全边界

`DASHSCOPE_API_KEY` 只能放在本机“作业 3”容器根 `.env`、兼容性回退 `.env` 或一次性进程环境变量中。不要把 API Key 放入聊天、截图、Notion、GitHub、日志或总结图。提交前必须确认：

```powershell
git status --short
```

输出中不应有任何 `.env`。当前项目的 `.env` 文件是忽略文件，仓库只保存 `.env.example` 或配置说明。

## 新窗口继续第 3 周的建议提示词

```text
请在 C:\Users\31797\Documents\ChatGPT\作业 3\AI_Project_2026_2 继续 Week 3 规则问答机器人。先读 HANDOFF.md、README.md、docs/status/，检查 git status，保留 week02_photo_classifier 不变。检查 week03_rule_chatbot/app.py、rules.txt 和 tests/test_week03_chatbot.py；先运行离线测试和 --check。API 配置若为空，只报告缺少配置，不要让我把密钥发到聊天里。完成后写入 docs/status/Week03_STATUS.md，确认 git diff，再提交和推送。
```
