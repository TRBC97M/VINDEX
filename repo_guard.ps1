param(
    [string]$RepoRoot = (Split-Path -Parent $MyInvocation.MyCommand.Path),
    [string[]]$ForbiddenPrefixes = @('.tmp.driveupload', '.tmp.drivedownload'),
    [switch]$Quiet
)

$ErrorActionPreference = 'Stop'

function Normaliza-Viam {
    param([string]$Value)

    $result = [string]$Value
    if ($result.StartsWith('"') -and $result.EndsWith('"')) {
        $result = $result.Substring(1, $result.Length - 2)
        $result = $result -replace '\\"', '"'
    }

    return $result.Trim()
}

function Lege-StatumGit {
    param([string]$Root)

    $status = git -C $Root -c core.quotepath=false status --porcelain --untracked-files=all
    if ($LASTEXITCODE -ne 0) {
        throw "Status Git legi non potest in '$Root'."
    }

    if (-not $status) {
        return @()
    }

    return ($status -split "`r?`n" | Where-Object { $_.Trim() })
}

$root = (Resolve-Path -Path $RepoRoot).Path
$branch = (git -C $root rev-parse --abbrev-ref HEAD).Trim()
if ($LASTEXITCODE -ne 0) {
    Write-Error "ERRATUM: ramus praesens legi non potest in '$root'."
    exit 2
}

if ($branch -eq 'main') {
    Write-Error "ERRATUM: 'main' directe mutari non licet. Ramum separatum crea ante commit."
    exit 2
}

$lines = Lege-StatumGit -Root $root
$tempHits = @()
foreach ($line in $lines) {
    if ($line.Length -lt 4) {
        continue
    }

    $path = Normaliza-Viam -Value $line.Substring(3)
    foreach ($prefix in $ForbiddenPrefixes) {
        if ($path -eq $prefix -or $path.StartsWith($prefix + '/')) {
            $tempHits += $path
        }
    }
}
$tempHits = $tempHits | Select-Object -Unique

if ($tempHits.Count -gt 0) {
    Write-Error "ERRATUM: res temporariae synchronizationis ante commit removendae sunt.`n  - $($tempHits -join "`n  - ")"
    exit 2
}

if (-not $Quiet) {
    if (-not $lines -or $lines.Count -eq 0) {
        Write-Host 'RECTE: nulla mutatio pendet.'
    }
    else {
        Write-Host "RECTE: ramus '$branch' mutationes committere potest."
        foreach ($line in $lines) {
            Write-Host "  $line"
        }
    }
}

exit 0
