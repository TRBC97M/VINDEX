param(
    [string]$RepoRoot = (Split-Path -Parent $MyInvocation.MyCommand.Path)
)

$ErrorActionPreference = 'Stop'

$root = (Resolve-Path -Path $RepoRoot).Path
$gitDir = Join-Path $root '.git'
if (-not (Test-Path $gitDir)) {
    throw "Repositorium Git in '$root' non inventum est."
}

$hookDir = Join-Path $gitDir 'hooks'
New-Item -ItemType Directory -Path $hookDir -Force | Out-Null

$guardScript = Join-Path $root 'repo_guard.ps1'
if (-not (Test-Path $guardScript)) {
    throw "Custos repositorii non inventus est: '$guardScript'."
}

$hookPath = Join-Path $hookDir 'pre-commit'
$hookContent = @'
#!/bin/sh
set -eu
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(git -C "$script_dir/../.." rev-parse --show-toplevel)
"$WINDIR/System32/WindowsPowerShell/v1.0/powershell.exe" -NoProfile -ExecutionPolicy Bypass -File "$repo_root/repo_guard.ps1" -Quiet
exit $?
'@

[System.IO.File]::WriteAllText($hookPath, $hookContent, [System.Text.UTF8Encoding]::new($false))
& 'C:\Program Files\Git\bin\bash.exe' -lc "chmod +x '$hookPath'"
if ($LASTEXITCODE -ne 0) {
    throw "Permissio executionis hook constitui non potuit: '$hookPath'."
}

Write-Host "RECTE: hook Git 'pre-commit' institutus est: $hookPath"
Write-Host "Custos 'main' et res temporarias synchronizationis prohibet; ramos collaboratorum non restringit."
