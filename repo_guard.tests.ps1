$ErrorActionPreference = 'Stop'

$guard = Join-Path $PSScriptRoot 'repo_guard.ps1'

function Novum-RepositoriumTestis {
    param([string]$Name)

    $root = Join-Path ([System.IO.Path]::GetTempPath()) ('vindex-guard-' + $Name + '-' + [System.Guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $root -Force | Out-Null
    git -C $root init --initial-branch=main | Out-Null
    git -C $root config user.name 'Testis VINDEX'
    git -C $root config user.email 'testis@example.com'
    Set-Content -Path (Join-Path $root 'README.txt') -Value 'basis'
    git -C $root add README.txt
    git -C $root commit -m 'initium' | Out-Null
    return $root
}

function Invoca-Custodem {
    param([string]$TargetRoot)

    $ErrorActionPreference = 'Continue'
    try {
        & $guard -RepoRoot $TargetRoot -Quiet 2>&1 | Out-Null
        return $LASTEXITCODE
    }
    catch {
        return 2
    }
    finally {
        $ErrorActionPreference = 'Stop'
    }
}

$repoMain = Novum-RepositoriumTestis -Name 'main'
try {
    if ((Invoca-Custodem -TargetRoot $repoMain) -eq 0) {
        throw "Custos ramum 'main' recusare debet."
    }
    Write-Host "RECTE: 'main' recusatur."
}
finally {
    Remove-Item -Recurse -Force $repoMain -ErrorAction SilentlyContinue
}

$ramiPermissi = @('chatgpt/testis', 'claude/testis', 'copilot/testis', 'gemini/testis', 'experimentum-humanum')
foreach ($ramus in $ramiPermissi) {
    $repo = Novum-RepositoriumTestis -Name ($ramus -replace '/', '-')
    try {
        git -C $repo checkout -b $ramus | Out-Null
        Set-Content -Path (Join-Path $repo 'mutatio.txt') -Value $ramus
        if ((Invoca-Custodem -TargetRoot $repo) -ne 0) {
            throw "Custos ramum legitimum recusavit: $ramus"
        }
        Write-Host "RECTE: ramus '$ramus' admittitur."
    }
    finally {
        Remove-Item -Recurse -Force $repo -ErrorAction SilentlyContinue
    }
}

$repoDirectorii = Novum-RepositoriumTestis -Name 'directorii'
try {
    git -C $repoDirectorii checkout -b chatgpt/directorii | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $repoDirectorii 'Vindex Chat-GPT') -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $repoDirectorii 'Vindex Claude Ai') -Force | Out-Null
    Set-Content -Path (Join-Path $repoDirectorii 'Vindex Chat-GPT\mutatio.txt') -Value 'chatgpt'
    Set-Content -Path (Join-Path $repoDirectorii 'Vindex Claude Ai\mutatio.txt') -Value 'claude'
    if ((Invoca-Custodem -TargetRoot $repoDirectorii) -ne 0) {
        throw 'Nomina directoriorum agentium sola mutationem impedire non debent.'
    }
    Write-Host 'RECTE: directorii agentium non sunt universaliter vetiti.'
}
finally {
    Remove-Item -Recurse -Force $repoDirectorii -ErrorAction SilentlyContinue
}

$repoTemp = Novum-RepositoriumTestis -Name 'temp'
try {
    git -C $repoTemp checkout -b copilot/temp | Out-Null
    $tempDir = Join-Path $repoTemp '.tmp.driveupload'
    New-Item -ItemType Directory -Path $tempDir -Force | Out-Null
    Set-Content -Path (Join-Path $tempDir 'fragmentum') -Value 'temporarium'
    if ((Invoca-Custodem -TargetRoot $repoTemp) -eq 0) {
        throw 'Custos res temporarias synchronizationis recusare debet.'
    }
    Write-Host 'RECTE: res temporariae synchronizationis recusantur.'
}
finally {
    Remove-Item -Recurse -Force $repoTemp -ErrorAction SilentlyContinue
}

Write-Host 'RECTE: omnes probationes custodis repositorii transierunt.'
