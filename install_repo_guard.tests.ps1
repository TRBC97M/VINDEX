$ErrorActionPreference = 'Stop'

$repoRoot = Join-Path ([System.IO.Path]::GetTempPath()) ('vindex-hook-' + [System.Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $repoRoot -Force | Out-Null

try {
    git -C $repoRoot init --initial-branch=main | Out-Null
    git -C $repoRoot config user.name 'Testis VINDEX'
    git -C $repoRoot config user.email 'testis@example.com'
    Set-Content -Path (Join-Path $repoRoot 'README.txt') -Value 'basis'
    git -C $repoRoot add README.txt
    git -C $repoRoot commit -m 'initium' | Out-Null

    Copy-Item -Path (Join-Path $PSScriptRoot 'repo_guard.ps1') -Destination (Join-Path $repoRoot 'repo_guard.ps1') -Force
    Copy-Item -Path (Join-Path $PSScriptRoot 'install_repo_guard.ps1') -Destination (Join-Path $repoRoot 'install_repo_guard.ps1') -Force

    & (Join-Path $repoRoot 'install_repo_guard.ps1') -RepoRoot $repoRoot | Out-Null

    $hookPath = Join-Path $repoRoot '.git\hooks\pre-commit'
    if (-not (Test-Path $hookPath)) {
        throw 'Hook pre-commit creatus non est.'
    }

    git -C $repoRoot checkout -b gemini/test-hook | Out-Null
    Set-Content -Path (Join-Path $repoRoot 'mutatio.txt') -Value 'probatio hook'
    git -C $repoRoot add mutatio.txt
    git -C $repoRoot commit -m 'probatio hook' 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "Hook ramum validum 'gemini/' impedire non debet."
    }

    Write-Host 'RECTE: hook Git instituitur et ramum collaboratoris validum admittit.'
}
finally {
    Remove-Item -Recurse -Force $repoRoot -ErrorAction SilentlyContinue
}
