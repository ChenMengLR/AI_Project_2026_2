$ErrorActionPreference = 'Stop'
$projectRoot = $PSScriptRoot
$pythonPath = Join-Path $projectRoot '.venv\Scripts\python.exe'
$appPath = Join-Path $projectRoot 'week02_photo_classifier\app.py'
$previousKey = $env:DASHSCOPE_API_KEY
$previousUrl = $env:DASHSCOPE_BASE_URL
$previousUtf8 = $env:PYTHONUTF8
$secretValue = Read-Host 'Enter your Singapore Model Studio API key (hidden; not saved)' -AsSecureString
$keyPointer = [IntPtr]::Zero
try {
    $keyPointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secretValue)
    $env:DASHSCOPE_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($keyPointer)
    $env:DASHSCOPE_BASE_URL = 'https://dashscope-intl.aliyuncs.com/compatible-mode/v1'
    $env:PYTHONUTF8 = '1'
    & $pythonPath $appPath
    if ($LASTEXITCODE -ne 0) { throw 'Classification did not finish successfully. Review the safe output above.' }
} finally {
    if ($keyPointer -ne [IntPtr]::Zero) { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($keyPointer) }
    $secretValue.Dispose()
    $env:DASHSCOPE_API_KEY = $previousKey
    $env:DASHSCOPE_BASE_URL = $previousUrl
    $env:PYTHONUTF8 = $previousUtf8
}
