# 2024 Indexes (generated)

Source: rules/2024/baseline/2025-08-11_core (immutable). Do not edit these JSONs by hand.

## Files
- spells_by_class_level.json
  - Shape: { "<ClassName>": { "<Level:int>": ["Spell A", ...] } }
  - Note: empty for this baseline (spells lack class/list mapping).
- feats_by_prereq.json
  - Shape: { "<PrereqKey>": ["Feat A", ...] }
  - Examples of keys: Level>=4, STR>=13, DEX>=13, Race=Elf.
- subclass_features_by_level.json
  - Shape: { "<Class>::<Subclass>": { "<Level:int>": ["Feature A", ...] } }

## PowerShell query examples
# Feats that require STR 13+
$feats = Get-Content .\indexes\2024\feats_by_prereq.json -Raw | ConvertFrom-Json
$feats.'STR>=13' | Sort-Object

# All levels where a subclass grants features
$sub = Get-Content .\indexes\2024\subclass_features_by_level.json -Raw | ConvertFrom-Json
$key = 'Barbarian::Ancestral Guardian'
$sub.$key.PSObject.Properties.Name | Sort-Object

# Features for a specific level
$sub.$key.'6'
