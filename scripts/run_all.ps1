param(
    [switch]$DryRun,
    [switch]$SkipSnapshot
)

<#
.SYNOPSIS
    One-command refresh for One D&D 2024 repo
.DESCRIPTION
    Runs snapshot → build → verify → indexes → (optional) commit+tag+push
#>

# === CONFIG ===
$SRC  = "C:\5eTools\5etools-src-main\data"
$REPO = "C:\MyGitHubRepos\Onednd-Rules-and-Builds"
$DateTag = (Get-Date -Format 'yyyy-MM-dd') + "_core"
$BaselineDir = Join-Path $REPO "rules\2024\baseline\$DateTag"
$VerifyReport = Join-Path $BaselineDir "verify_report.txt"
$ErrorActionPreference = 'Stop'

Set-Location $REPO

# === 1) SNAPSHOT (optional) ===
if (-not $SkipSnapshot) {
    $SnapFile = "snapshot_{0}.txt" -f (Get-Date -Format 'yyyyMMdd_HHmmss')
    cmd /c "tree /f $REPO > $SnapFile"
    Write-Host "Snapshot saved to $SnapFile"
}

# === 2) BUILD RULES ===
python scripts\build_rules_2024.py --src "$SRC" --out ".\rules\2024"
if ($LASTEXITCODE -ne 0) { throw "Build failed." }
Write-Host "Build complete."

# === 3) VERIFY ===
New-Item -ItemType Directory -Force -Path $BaselineDir | Out-Null
python scripts\verify_rules_2024.py --src "$SRC" --out ".\rules\2024" > "$VerifyReport"
if ($LASTEXITCODE -ne 0) { throw "Verify failed. See $VerifyReport" }
Write-Host "Verify report saved to $VerifyReport"

# === 4) BUILD INDEXES ===
python scripts\build_indexes_2024.py --baseline ".\rules\2024" --out ".\indexes\2024"
if ($LASTEXITCODE -ne 0) { throw "Index build failed." }
Write-Host "Indexes built."

if ($DryRun) {
    Write-Host "DryRun: skipping commit/tag/push."
    return
}

# === 5) COMMIT + TAG ===
git add rules/2024 indexes/2024 ".gitattributes" ".gitignore" "$VerifyReport" docs/scope.md `
        scripts/build_rules_2024.py scripts/verify_rules_2024.py scripts/build_indexes_2024.py `
        scripts/run_all.ps1 scripts/triage_2024_deltas.py 2>$null

# Only commit if there are staged changes
$pending = git diff --cached --name-only
if (-not [string]::IsNullOrWhiteSpace($pending)) {
    git commit -m "build: refresh 2024 outputs, indexes, verify report ($DateTag)"
} else {
    Write-Host "Nothing to commit (working tree clean)."
}

# Tag handling: if tag exists, suffix -2/-3/etc
$TagBase = "baseline/$DateTag"
$Tag = $TagBase
$idx = 2
while ((git tag -l $Tag) -ne "") {
    $Tag = "$TagBase-$idx"
    $idx++
}
if ($Tag -ne $TagBase) {
    Write-Host "Tag '$TagBase' exists; using '$Tag' instead."
}
git tag -a "$Tag" -m "2024 core baseline $Tag"
git push --follow-tags
Write-Host "Commit + tag pushed ($Tag)."
