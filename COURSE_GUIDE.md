# 第2周 Qwen Vision 课程操作说明

第2周 Qwen Vision
课程操作说明

软件安装  GitHub操作  课堂实践  作业提交

适用对象 WANG HAOBIN   系统 Windows PowerShell   核验日期 2026年9月17日

本节课要完成一个 AI Photo Classifier：把多张图片交给 Qwen 识别，再按类别复制到文件夹。本说明按你已经部署好的电脑编写，首页用于上课速查，后续页面解释安装、运行和提交步骤。

### 当前进度

- 已完成：Python、Git、VS Code、虚拟环境、课程脚本、五张课堂样例、GitHub 私有仓库及首次推送。

- 本次补齐：样例图片来源记录、结果记录表、个人与团队作业模板、录屏提纲及本说明。

- 尚待完成：阿里云账号内的 API 配置与额度确认、自己准备的 2–3 张新图、真实分类、运行视频及最终作业提交。

### 上课速查顺序

1  打开桌面 AI_Project_2026_2，用 VS Code 打开整个文件夹。

2  在 week02_photo_classifier/.env 填好本人 API Key 和兼容端点；确认免费额度保护。

3  核对 input 已有 sample-01.jpg 至 sample-05.jpg，再加入自己的 2–3 张新图。

4  双击根目录 Open-Course.cmd，按顺序运行下面三条命令。

5  核对每张图片的终端结果与 sorted 文件夹，填写 results.csv，录制 30–60 秒真实运行视频。

6  回到课程根目录，保存文件 → 暂存 → commit → push → 核对 GitHub，再提交个人作业卡。

```powershell
python app.py --check
python app.py --test-api
python app.py
```

第一条只做离线检查；后两条会调用 Qwen。每条确认成功后再执行下一条。

### 提交到哪里

个人：自己的个人作业卡，提交 GitHub 仓库链接和运行视频。团队：本组团队卡的第2周记录，提交一份应用方案和 Week 3 Goal。

[打开你的 GitHub 仓库](https://github.com/ChenMengLR/AI_Project_2026_2)

页码导航：2 软件环境｜3 API与图片｜4 课堂实践｜5 GitHub｜6 作业与录屏｜7 团队与待办｜8 排错与迁移

## 软件安装与本机环境

你的电脑已经装好以下软件，无需重复安装。安装步骤用于以后换电脑或恢复环境。所有命令均输入 PowerShell 或 VS Code 的 Terminal，不写进 app.py。

### 软件各自做什么

- VS Code 1.138.0：编辑代码、查看文件和打开终端；已装微软 Python 扩展及配套组件。

- Python 3.14.7：执行 app.py。课程使用 Python 3.14；本机 .venv 使用这一版本。

- Git 2.55.0.windows.5：在本地保存项目修改历史；Git Bash 随 Git for Windows 安装。

- GitHub：保存和共享 Git 提交。当前账号 ChenMengLR，仓库 AI_Project_2026_2，默认分支 main。

- openai 3.14.1：作为 OpenAI 兼容客户端调用 Qwen；python-dotenv 1.2.3：读取本地 .env。这并不要求购买 OpenAI API。

### 在新电脑安装的顺序

1  安装 VS Code，再在扩展页安装 Microsoft 发布的 Python 扩展。

[VS Code 官方下载](https://code.visualstudio.com/download)

2  安装 Python 3.14。课程给出的新版 Python Install Manager 路线是安装官方管理器后运行 py install 3.14；该命令仅适用于新版管理器。已有 Python 3.14 的电脑直接检查版本即可。

[Python 官方 Windows 下载](https://www.python.org/downloads/windows/)

3  安装 Git for Windows 的 x64 版本，常规选项保持默认。安装后重新打开终端。

[Git for Windows 官方安装入口](https://git-scm.com/install/windows)

```powershell
python --version
python -m pip --version
git --version
code --version
```

### 虚拟环境只需在课程根目录创建一次

本学期持续使用 AI_Project_2026_2，在里面增加 week03、week04 等周次目录，共用根目录 .venv。已有环境不用每节课重建；新电脑先按第8页克隆项目，再执行：

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
```

本机依赖导入与 pip check 已通过。VS Code 请选择根目录 .venv 中的解释器。

## API配置与图片准备

### 先认清文件的位置

```powershell
C:\Users\31797\Desktop\AI_Project_2026_2\
  .venv\                      # 本学期共享环境
  .gitignore                   # 上传排除规则
  README.md                    # 项目使用说明
  Open-Course.cmd              # 双击打开课程终端
  week02_photo_classifier\
    app.py                     # 分类程序
    .env                       # 真实密钥 仅本地
    .env.example               # 无密钥示例 可上传
    input\                    # 原始图片
    sorted\                   # 运行后自动生成
    results.csv                # 预期与实际结果记录
    SUBMISSION.md              # 作业与录屏模板
```

### 账号与密钥由你本人完成

登录 Alibaba Cloud，进入 Model Studio，选择 Singapore。按账号页面实际要求完成注册、服务启用等步骤；若出现服务协议、身份资料或付款信息，请本人核对后操作。

在当前工作空间创建或使用自己的 API Key，同时复制同一工作空间的 OpenAI Compatible Endpoint。将它们粘贴到本周 .env 的等号后，按 Ctrl+S 保存；文件已创建，不要另建 .env.txt。

```powershell
DASHSCOPE_API_KEY=这里替换为自己的真实密钥
DASHSCOPE_BASE_URL=这里替换为自己的兼容端点
```

端点须以 https:// 开头并以 /compatible-mode/v1 结尾。不要填文档网址、API Host 或未经核对的他人端点。密钥只存本地 .env，不粘贴到聊天、GitHub 或录屏。

### 先确认额度 再发送请求

在 Model Studio 查看 qwen3.8-flash 的可用权限、免费余额、到期日，以及 Free Quota Only 或讲义所称 Stop-on-Exhaust 状态。只有看到实际保护状态启用后再测试；开关变化可能延迟生效。额度不能仅凭“已注册”推断。

[官方免费额度与保护开关说明](https://www.alibabacloud.com/help/en/model-studio/new-free-quota)

### 图片已经准备到哪一步

五张教师样例已保存为标准 JPEG：01 人像 → person；02 纸张 → document；03 食物 → food；04 电脑 → device；05 森林 → other。这些是讲义给出的预期类别，尚无真实 API 分类结果。来源见 SAMPLE_SOURCES.md。

还需要你自己选择 2–3 张新图片，建议命名 new-01.jpg 等，先写下预期类别。放到 input 的第一层；当前脚本支持 JPG、JPEG、PNG、WebP，不扫描子文件夹。

## 课堂流程与任务验收

### 课堂按这个顺序推进

1  团队想法分享：说明主题、问题、目标用户、初步服务、AI 的作用及下周目标。本节讲义写每组最多5分钟；第3周汇报要求另为最多3分钟。

2  理解今天的主题：识别是把图像变成可用信息，分类是按规则分到类别；服务再根据类别执行搜索、整理或提示。今天实现“图片 → Qwen → 标签 → 文件夹”。

3  检查软件、虚拟环境和 API 配置，完成文本连接测试。

4  对五张样例和 2–3 张新图做五分类，核对输出，保留真实观察记录。

5  团队讨论这一结构是否适合本组项目，整理最终方案与下一步目标。

6  保存最终代码，提交并推送 GitHub，录制视频，分别完成个人与团队提交。

### 按本机脚本实际运行

双击项目根目录 Open-Course.cmd，会启用虚拟环境并进入 week02_photo_classifier。现有 app.py 已整合连接测试与最终分类，无需按讲义反复覆盖文件。

```powershell
python app.py --check
```

只检查本地准备。当前应识别到五张样例，但因 API Key 与端点为空，仍会提示未就绪。检查通过也不代表 API 已连通。

```powershell
python app.py --test-api
```

发送一个短文本请求；返回连接成功信息后，再运行图片分类。它不能代替图片测试。

```powershell
python app.py
```

逐张发送 input 图片，输出“文件名 → 类别”，并把原图副本放进 sorted/类别/；原图保留。只有本次出现的类别才会创建对应目录。

### 什么算完成

- 全部 7–8 张图片都有结果，失败项已处理；sorted 中可找到对应副本。

- 把新图的预期与真实结果填入 results.csv，写一句观察；不要把预期类别当成实测结果。

- 理解 app.py 的关键流程：加载配置、编码图片、调用模型、检查标签、复制文件。

重复运行会再次调用 API，并可能覆盖同名副本；类别变化后旧目录中的副本不会自动消失。录屏前将旧 sorted 改名为 sorted_archive_日期并放到仓库之外，再做一次可追溯的最终运行。

## GitHub保存与上传

Git 是本地版本记录工具，GitHub 是远程存放这些版本的网站。Ctrl+S 保存文件，git add 选择本次提交内容，git commit 创建本地版本，git push 才把版本上传。上传 GitHub 后，还需按第6页向课程作业卡提交链接。

### 你的仓库信息

账号 ChenMengLR｜仓库 AI_Project_2026_2｜分支 main｜可见性 Private

署名 WANG HAOBIN｜邮箱 chenmenglr@gmail.com；身份仅配置在此课程仓库。

[仓库页面与提交记录](https://github.com/ChenMengLR/AI_Project_2026_2)

```powershell
https://github.com/ChenMengLR/AI_Project_2026_2.git
```

HTTPS 地址可在仓库首页 Code → HTTPS 复制，也可用 git remote -v 查看。本机已经建立 origin 并完成首次 push，不用重复 git init 或 git remote add。

### 每次修改后的标准操作

先按 Ctrl+S 保存文件，再回到课程根目录。以下示例选择代码和作业记录；需要上传其他文件时，按实际文件名补充 git add。

```powershell
cd C:\Users\31797\Desktop\AI_Project_2026_2
git status
git add README.md week02_photo_classifier/app.py
git add week02_photo_classifier/results.csv
git add week02_photo_classifier/SUBMISSION.md
git diff --cached --name-only
git diff --cached
```

核对暂存清单与差异，确认内容正确且不含密钥后，执行：

```powershell
git commit -m "Week 2: record Qwen Vision results"
git push
git status
```

刷新 GitHub，查看最新提交信息及文件内容。工作区干净且分支已同步，才表示本次修改记录和上传均结束。若执行 add 后又改了文件，需要再次 add。

### 上传前要理解的几个细节

- Open-Course 默认进入周次目录，在那里执行 git add . 会漏掉根目录变化；所以先 cd 到课程根目录。

- git add . 会选择当前目录下所有未忽略的变化，也可能包括新照片。可以使用，但必须先核对清单。

- .env、.venv/、sorted/ 已被忽略；.env.example 是可以提交的无密钥示例。忽略规则不会让已跟踪的文件自动退出版本管理。

- 误暂存一个文件：git restore --staged 文件路径。它只撤销暂存，保留你的文件修改。

## 个人作业提交与录屏

按作业详情页，个人实践只需交两项：包含最终 app.py 的个人 GitHub 仓库链接，以及30–60秒真实运行视频。无需另外提交结果截图。

[打开个人作业卡入口](https://app.notion.com/p/c94e0aefc7234bc2b0bc70353cd697e6)

### 先完成 再提交

1  确认五张课堂样例和自己的 2–3 张新图均已运行；终端结果和 sorted 中的图片可对应。

2  把最终代码及实际观察记录提交并推送，打开 GitHub 核对 app.py。

3  录制视频并回放，确认字迹清晰、能看到操作顺序和所有图片结果，没有展示 .env。

4  进入 Individual Assignment Cards，找到自己的个人卡片及第2周提交位置，粘贴仓库链接并上传视频或填写可访问的视频链接。

5  确认页面保存，重新打开卡片检查链接和视频能播放。若找不到本人卡片或无编辑权限，向教师确认，不新建替代提交页。

### 30至60秒录屏提纲

- 0–10秒：展示 VS Code 的 input，能看到 sample-01 至 sample-05 和 2–3 张新图。

- 10–35秒：在已启用环境的 Terminal 输入 python app.py，并展示分类过程。

- 35–50秒：展示每张图片的文件名和分类结果；若网络等待很长，保留原始录像并向教师确认能否加速等待段。

- 50–60秒：展开 sorted 的分类目录，展示图片确实进入对应目录。不要用手工摆放结果代替实际运行。

建议使用 Windows 自带截图工具的录屏功能，或你熟悉的录屏软件；开始前关闭 .env 标签页。SUBMISSION.md 中已准备可直接填写的个人提交模板。

### 私有仓库如何让老师查看

当前仓库为 Private。仅粘贴链接不等于对方有访问权限；需要确认教师使用的 GitHub 账号并按课程要求授予访问，或在教师明确要求公开时调整可见性。本轮尚未邀请教师或改为公开。

### 课程页面中的两处差异

讲义末尾写把截图等交团队卡，作业详情则明确区分个人卡与团队卡，并改为“链接加视频、无需截图”。本说明按更具体的作业详情组织提交，同时保留 results.csv 便于核查。若教师另有通知，以教师确认为准。

详情页 Deadline 写 2026年9月16日，Status 却为 Upcoming；本次检查日期是9月17日。请确认真实截止日期或补交安排，不能由 Upcoming 推断仍未到期。

[第2周作业详细说明](https://app.notion.com/p/3cf7c00fe5ad812a8fbddc3749d02d75)

## 团队任务与尚待完成事项

### 团队只交一份最终方案

小组共同讨论，由一名成员填写本组团队卡的第2周记录。可以把以下结构复制到 SUBMISSION.md 的团队区，达成一致后再提交。

```powershell
Project: 项目名称与一句话说明
Input: 服务接收的数据
AI识别或区分的对象: 待讨论
Categories / States: 尽量列出3至5类
Result → Service Action: 每类结果对应的服务动作
Progress / Result: 实际已完成内容
展示材料: 界面 代码 或运行结果
Blocker: 当前问题或待决事项
Week 3 Goal: 一个下次课可执行且可验收的目标
```

如果识别或分类不适合本组项目，说明原因，并从预测、推荐、生成、对话检索或自动化等功能中选择更合适的一项，不必强行加入。

### 第3周汇报最多3分钟

在本组团队卡“第2周记录”的“3주차 발표 준비”小节填写 Week 3 Goal 与汇报准备。依次说明项目、应用构想、实际成果、阻碍和下一步目标；至少展示一项界面、代码或运行结果，可用幻灯片、Notion 或运行画面。

### 目前还缺什么以及为什么

- 你本人完成阿里云账号步骤，核对服务条款、可能出现的资料或付款要求；当前没有已配置的有效密钥和端点。

- 在本地 .env 填入 API Key 和兼容端点，并确认 Singapore、模型权限、余额及额度保护；完成后可继续代你检查并运行。

- 选择自己的 2–3 张新图，先填预期类别。教师要求“自己准备”，因此没有擅自用随机图片替你完成这一项。

- 真实文本连接和图片分类、实际观察、录屏：依赖以上配置和新图；当前模板的实际结果字段保持空白。

- 个人作业卡最终提交：依赖真实运行视频、可访问仓库，以及确认本人的卡片位置；本轮没有提交未完成作业。

- 团队方案、Week 3 Goal 和汇报：需要你提供团队主题、成员讨论结论与团队卡片；模板已备好，最终决策需小组共同完成。

- 教师仓库访问权限及截止日期：需要教师账号或课程明确的可见性要求，并确认9月16日是否仍为实际截止日。

准备完成、运行成功和作业已提交是三个不同状态。代码与模板齐备不能代替真实运行及课程平台提交。

## 常见问题与换电脑恢复

### 常见问题怎么处理

- python 跳到商店或命令不识别：重新打开终端；本机可直接用 .venv\Scripts\python.exe。

- Activate.ps1 被策略阻止：无需修改全局策略，直接使用虚拟环境中的解释器运行。

```powershell
cd C:\Users\31797\Desktop\AI_Project_2026_2
.\.venv\Scripts\python.exe .\week02_photo_classifier\app.py --check
```

- 找不到 app.py 或 PathNotFound：核对当前位置。已在 week02_photo_classifier 时，不要再 cd 同名子目录。

- 提示缺少 openai 或 dotenv：在课程根目录用 .venv\Scripts\python.exe -m pip install -r requirements.txt。

- API失败：先看本地检查，再核对密钥、同区端点、模型权限、额度和网络。不要把完整密钥贴进报错截图。

- nothing to commit：没有已暂存的新变化；先保存文件和 git status。只修改 .env 不会产生可提交变化，这是正常的。

- push 登录失败：核对当前 GitHub 账号、网络与仓库权限，按凭据管理器引导登录；提交署名不等于登录账号。

- non-fast-forward：远程有本地缺少的提交。先保存本地工作，确认状态后拉取并处理冲突，不使用强推覆盖远程。

### 换电脑恢复同一个仓库

安装第2页的软件并登录有仓库权限的 GitHub 账号，在新电脑希望保存项目的父目录执行；不要在现有课程文件夹内再克隆一份。

```powershell
git clone https://github.com/ChenMengLR/AI_Project_2026_2.git
cd AI_Project_2026_2
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
git config user.name "WANG HAOBIN"
git config user.email "chenmenglr@gmail.com"
```

克隆会自动建立 origin。若本周 .env 不存在，再从 .env.example 复制创建，填写本人配置；不要覆盖已有 .env，也不要跨电脑复制旧 .venv。之后用 Open-Course.cmd 打开环境。

### 资料与检查依据

[第2周课程讲义](https://app.notion.com/p/3cf7c00fe5ad8140b175c415d1613a7e)

[第2周作业详情及个人提交规则](https://app.notion.com/p/3cf7c00fe5ad812a8fbddc3749d02d75)

[GitHub 官方推送说明](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository)

[GitHub 官方克隆与 HTTPS 地址说明](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

[Model Studio API Key 与兼容端点](https://www.alibabacloud.com/help/en/model-studio/get-api-key)

本机核验：虚拟环境版本与依赖导入通过，pip check 无冲突；离线检查确认五张样例可识别，API配置仍为空。课程要求按2026年9月17日可访问页面核对。
