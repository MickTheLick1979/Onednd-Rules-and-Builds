param(
  [string]$Src = "C:\5eTools\5etools-src-main\data",
  [string]$BuildOut = ".\build\2024",
  [string]$GoldOut = ".\rules\2024",
  [switch]$RefreshGold  # only overwrite snapshot when you pass -RefreshGold
)

# Allow-list of files to populate into the gold snapshot (player builds + core mechanics + monster data)
$allow = @(
  # Player build content
  "background.json",
  "class.json","classFeature.json",
  "subclass.json","subclassFeature.json",
  "race.json","raceFeature.json",
  "feat.json",
  "spell.json",
  "item.json","itemProperty.json","itemType.json","itemMastery.json",
  "optionalfeature.json",
  "language.json",

  # Core mechanics relevant to optimisation
  "action.json","condition.json","status.json",
  "skill.json","sense.json","variantrule.json","table.json",

  # Monster meta
  "monster.json"
) | Sort-Object -Unique

Write-Host "== Build (scratch) ==" -ForegroundColor Cyan
# If you haven't added --prune-outdir yet, remove that flag below.
python .\scripts\build_rules_2024.py --src "$Src" --out "$BuildOut" --sources XPHB,XDMG,XMM --accept-xprefix

Write-Host "`n== Verify build ==" -ForegroundColor Cyan
python .\scripts\verify_rules_2024.py --src "$Src" --out "$BuildOut"

Write-Host "`n== Quick analytics ==" -ForegroundColor Cyan
# These are optional; they just sanity-check data shapes.
python .\scripts\analyse_monsters.py --root "$BuildOut" --summary 2>$null
python .\scripts\analyse_spells.py --root "$BuildOut" summary 2>$null

if ($RefreshGold) {
  Write-Host "`n== Refresh GOLD snapshot (copy allow-list only) ==" -ForegroundColor Yellow
  foreach ($f in $allow) {
    $srcPath = Join-Path $BuildOut $f
    $dstPath = Join-Path $GoldOut  $f
    if (Test-Path $srcPath) {
      Copy-Item $srcPath $dstPath -Force
      Write-Host "  copied $f"
    } else {
      Write-Host "  (skip) $f not produced this build"
    }
  }
  git status
  Write-Host "Snapshot updated. Review diffs, then commit."
} else {
  Write-Host "`n(GOLD snapshot unchanged. Use -RefreshGold to update.)"
}
