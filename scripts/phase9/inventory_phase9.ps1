param(
  [switch]$All   # include orphaned schema/validators/workflows not backed by a rules file
)

function New-Row($Category,$HasSchema,$HasValidator,$HasCI,$Notes){
  [pscustomobject]@{
    Category      = $Category
    HasSchema     = [bool]$HasSchema
    HasValidator  = [bool]$HasValidator
    HasCI         = [bool]$HasCI
    Missing       = (@(
      if(-not $HasSchema)    { "schema" }
      if(-not $HasValidator) { "validator" }
      if(-not $HasCI)        { "ci" }
    ) -join ", ")
    Notes         = $Notes
  }
}

$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location (Join-Path $repo "..\..") | Out-Null

$rulesDir  = ".\rules\2024"
$schemaDir = ".\schema\2024\v1"
$scriptDir = ".\scripts\phase9"
$ciDir     = ".\.github\workflows"

$rules = Get-ChildItem $rulesDir -File -Filter *.json | Select-Object -ExpandProperty BaseName

# Optional: find orphans (schema/validators/CI with no matching rules file)
$schemas    = Get-ChildItem $schemaDir -File -Filter *.schema.json -ErrorAction SilentlyContinue | ForEach-Object { $_.BaseName -replace "\.schema$","" }
$validators = Get-ChildItem $scriptDir -File -Filter validate_*.py -ErrorAction SilentlyContinue | ForEach-Object { $_.BaseName -replace "^validate_","" }
$cis        = Get-ChildItem $ciDir -File -Filter phase9-*.yml -ErrorAction SilentlyContinue | ForEach-Object { $_.BaseName -replace "^phase9-","" }

$rows = New-Object System.Collections.Generic.List[object]

foreach($cat in $rules){
  $schemaPath = Join-Path $schemaDir "$cat.schema.json"
  $valPath    = Join-Path $scriptDir "validate_$cat.py"
  $ciPath     = Join-Path $ciDir "phase9-$cat.yml"

  $hasSchema    = Test-Path $schemaPath
  $hasValidator = Test-Path $valPath
  $hasCI        = Test-Path $ciPath

  $notes = @()

  # Lightweight content sanity checks (non-fatal; just notes)
  if($hasValidator){
    $v = Get-Content $valPath -Raw -Encoding UTF8
    if($v -notmatch 'Draft202012Validator'){ $notes += "validator:missing Draft202012" }
    if($v -notmatch 'encoding="utf-8-sig"'){ $notes += "validator:missing utf-8-sig" }
    if($v -notmatch [regex]::Escape("rules,")) { $notes += "validator:check DATA path" }
  }
  if($hasCI){
    $w = Get-Content $ciPath -Raw -Encoding UTF8
    if($w -notmatch [regex]::Escape("scripts/phase9/validate_$cat.py")) { $notes += "ci:validate step mismatch" }
  }

  $rows.Add((New-Row $cat $hasSchema $hasValidator $hasCI ($notes -join "; ")))
}

if($All){
  $ruleSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$rules)
  foreach($s in $schemas){    if(-not $ruleSet.Contains($s)){ $rows.Add((New-Row $s $true  ($validators -contains $s) ($cis -contains $s) "orphan: no rules/2024/$s.json")) } }
  foreach($v in $validators){ if(-not $ruleSet.Contains($v)){ $rows.Add((New-Row $v ($schemas -contains $v) $true  ($cis -contains $v) "orphan: no rules/2024/$v.json")) } }
  foreach($c in $cis){        if(-not $ruleSet.Contains($c)){ $rows.Add((New-Row $c ($schemas -contains $c) ($validators -contains $c) $true  "orphan: no rules/2024/$c.json")) } }
}

# Output
$rows = $rows | Sort-Object Category
$rows | Format-Table -AutoSize

# Write CSV report
$outDir = ".\reports\phase9"
New-Item -ItemType Directory -Path $outDir -Force | Out-Null
$csv = Join-Path $outDir ("inventory_{0:yyyyMMdd_HHmmss}.csv" -f (Get-Date))
$rows | Export-Csv -NoTypeInformation -Encoding UTF8 $csv
Write-Host ("Report: {0}" -f $csv)

# Exit code: 0 if all present, 1 otherwise
$anyMissing = $rows | Where-Object { -not $_.HasSchema -or -not $_.HasValidator -or -not $_.HasCI }
if($anyMissing){ exit 1 } else { exit 0 }
