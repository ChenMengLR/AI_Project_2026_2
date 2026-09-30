$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $projectRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) {
    throw '请先按项目根 README 安装共享 .venv 与 requirements.txt。'
}
& $python (Join-Path $PSScriptRoot 'app.py') --port 8765
