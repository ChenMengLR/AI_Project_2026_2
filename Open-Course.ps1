$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
. (Join-Path $PSScriptRoot '.venv\Scripts\Activate.ps1')
Set-Location -LiteralPath (Join-Path $PSScriptRoot 'week02_photo_classifier')
Write-Host 'Course environment is active. Run: python app.py --check'
Write-Host 'Only after local configuration: python app.py --test-api'
Write-Host 'Classification sends input images to Qwen: python app.py'
