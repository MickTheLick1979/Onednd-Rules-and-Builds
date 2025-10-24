# One D&D 2024 – Core Rules & Player Build Reference

## Overview
This repository contains a **clean, filtered extract** of One D&D 2024 rules and data from the [5etools](https://5etools-mirror-1.github.io/) source files.

It is purpose-built for:
- **Character creation & optimisation**
- **Core game mechanics reference** (e.g., grappling, unarmed strikes, conditions)
- **Monster statistics** for meta-analysis (e.g., resistances, common saves, average ACs)

All data is in JSON format for easy querying and integration with ChatGPT or other tools.

## Scope

### Included
- **Character options**  
  Backgrounds, classes, subclasses, races (One D&D terminology: “species”), feats, optional features, languages.
- **Spells**
- **Equipment & items** (including magic items and item properties)
- **Core mechanics & rules**  
  Actions, conditions, skills, senses, variant rules, rules tables.
- **Monsters & legendary groups** for build-relevant analytics.

### Excluded
- Adventure/module content
- Treasure tables & art objects
- Vehicles, traps, facilities
- Any content not relevant to player builds or core rules mechanics

## How It’s Built
All data is pulled from a local 5etools repo using:
- scripts/build_rules_2024.py – Extracts only 2024 content from allowed sources (XPHB, XDMG, XMM, and any future X* sources), filtered by a strict allow-list of categories.
- scripts/verify_rules_2024.py – Compares your local 5etools data to the export to confirm counts and spot missing or extra categories.

A strict **per-entry** source filter ensures:
- Only 2024/X* sources are included
- No mixed-edition data
- No stale files from older builds

## Updating the Data

### 1. Build the export
\\\powershell
python .\scripts\build_rules_2024.py 
  --src "C:\5eTools\5etools-src-main\data" 
  --out "C:\MyGitHubRepos\Onednd-Rules-and-Builds\rules\2024" 
  --sources XPHB,XDMG,XMM 
  --accept-xprefix
\\\

### 2. Verify the export
\\\powershell
python .\scripts\verify_rules_2024.py 
  --src "C:\5eTools\5etools-src-main\data" 
  --out "C:\MyGitHubRepos\Onednd-Rules-and-Builds\rules\2024"
\\\

### 3. Commit & push
\\\powershell
git add rules/2024
git commit -m "Update core 2024 rules export"
git push
\\\

## Monster Analytics
Use scripts/analyse_monsters.py for quick queries over the monster dataset.

Examples:
\\\powershell
# Top 20 most common resistances
python .\scripts\analyse_monsters.py resist

# Monsters that resist fire
python .\scripts\analyse_monsters.py resist --type fire

# Save proficiencies and average bonuses
python .\scripts\analyse_monsters.py saves

# Average AC overall and by CR
python .\scripts\analyse_monsters.py ac
\\\

---

**Note:**  
This repo deliberately excludes anything that does not directly impact player build decisions or core gameplay mechanics.

### CI Status
![CI � Validate 2024 Data](https://github.com/MickTheLick1979/Onednd-Rules-and-Builds/actions/workflows/ci-validate.yml/badge.svg)

