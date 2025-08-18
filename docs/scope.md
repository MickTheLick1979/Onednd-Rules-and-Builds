# Project Instructions — One D&D 2024 Character Build Repo

## 0) North Star
This repo is a clean, machine-readable dataset and indexes for building characters using 2024 One D&D rules only. Nothing else is included. Focus = things you pick for a character or that directly affect builds. Monsters are included (for optimisation vs. enemies). Magic items and adventure content are excluded.

## 1) Allowed Sources
- XPHB (Player’s Handbook 2024) — main source for builds.
- XMM (Monster Manual 2024) — monsters only.
- Entries flagged `basicRules2024` or `srd52`.
- Everything else (e.g., XDMG) is excluded unless whitelisted later.
Rule of thumb: If it isn’t XPHB (build stuff), XMM (monsters), or explicitly flagged 2024, it stays out.

## 2) Categories
### Keep (build-critical & related)
- Classes & features: class, classFeature, subclass, subclassFeature, subclassFluff
- Feats: feat (plus featFluff)
- Spells: spell (plus spellFluff)
- Backgrounds: background (plus backgroundFluff)
- Species/Races: species, speciesFeature, speciesFluff, race, raceFeature, raceFluff
- Optional player features: optionalfeature (e.g. Fighting Styles, Maneuvers, Invocations, Metamagic, Infusions)
- Equipment: baseitem, item, itemEntry, itemFluff, itemGroup, itemMastery, itemProperty, itemType, itemTypeAdditionalEntries
- Conditions/Rules: condition, action, status, table, tableGroup, variantrule
- Other useful: language, languageScript, sense, skill, reward
- Monsters: monster, monsterFluff, legendaryGroup
- Objects: object, objectFluff
- Books (provenance): book
### Exclude (always)
- magicItems, magicvariant
- trap, trapFluff
- vehicle, vehicleFluff
- deity, disease
- hoard, gems, individual, card
- adventure, artObjects, deck, encounter, entries, facility, facilityFluff, name
- Aggregators/metadata: _versions, manifest, otherSources, requires, images, altArt, etc.

## 3) Filtering Logic
- Build-critical categories (class, classFeature, subclass, subclassFeature, feat, spell, background, species/race, optionalfeature): Keep only entries with source = XPHB OR flagged basicRules2024 / srd52.
- Monsters: Keep only entries with source = XMM OR flagged 2024.
- Equipment & misc rules: Prefer XPHB or flagged 2024. Do not include generic XMM entries.

## 4) Verifier Policy
- Excluded categories must be reported as INTENTIONALLY EXCLUDED (not errors).
- For kept categories: Output count must equal allowed-source 2024 entries. No non-allowed sources should appear.
- Spot checks: class = 12 (XPHB classes). monster = only XMM. feat, spell counts match filtered PHB 2024.

## 5) Indexes We Maintain
Only these three indexes are kept under /indexes/2024/: spells_by_class_level.json, feats_by_prereq.json, subclass_features_by_level.json. All must be built from filtered outputs (not raw sources).

## 6) Directory Layout
/rules/2024/ ← filtered JSON outputs  
/rules/2024/baseline/<date>_core/verify_report.txt ← saved verifier output  
/indexes/2024/ ← generated indexes  
/scripts/ ← builder, verifier, indexers, run_all.ps1  
/docs/ ← scope.md (copy of these rules)

## 7) Daily Workflow
1) Build: `python scripts\build_rules_2024.py --src "C:\5eTools\5etools-src-main\data" --out ".\rules\2024"`  
2) Verify: `python scripts\verify_rules_2024.py --src "C:\5eTools\5etools-src-main\data" --out ".\rules\2024" > .\rules\2024\baseline\<date>_core\verify_report.txt`  
3) Indexes: `python scripts\build_indexes_2024.py --baseline ".\rules\2024" --out ".\indexes\2024"`  
4) Commit: `git add rules/2024 indexes/2024 scripts/*.py rules/2024/baseline/<date>_core/verify_report.txt && git commit -m "build: refresh 2024 outputs, indexes, verify report"`

## 8) Change Control
Single source of truth = Section 3 (Filtering Logic). Builder + verifier must both follow it. If scope changes, update Section 3 → then update builder + verifier → rebuild → verify → reindex → commit.

## 9) Housekeeping
.gitattributes (normalise endings): * text=auto; *.py text eol=lf; *.ps1 text eol=crlf; *.json text eol=lf; *.md text eol=lf  
.gitignore: snapshot_*.txt; _write_check.txt; build/

## 10) Glossary
- XPHB = 2024 Player’s Handbook (build content).  
- XMM = 2024 Monster Manual (monsters only).  
- basicRules2024 / srd52 = explicit 2024 flags.  
- Build-critical = classes, features, subclasses, feats, spells, backgrounds, species/races, optional features.
