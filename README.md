# One D&D 2024 — Core Rules & Indexes

![CI — Validate 2024 Data](https://github.com/MickTheLick1979/Onednd-Rules-and-Builds/actions/workflows/ci-validate.yml/badge.svg)

> **Read this first:** For environment, encodings, CI conventions, and day‑to‑day guardrails, see **`OneDND-Assistant-Playbook.md`** (PowerShell **7.5.4**, Python **3.11**, UTF‑8 **no BOM**, **LF** endings, single matrix CI).

---

## Purpose

Ship a **self-contained** One D&D 2024 rules dataset derived from 5etools that downstream tools can consume directly: **cleaned**, **deduped**, and **indexed** JSON—no need to bundle the full 5etools source.

---

## Goals

1. **Self-contained output**: rules, mappings, and indexes live in-repo.  
2. **Minimal & accurate**: include only 2024/X* (e.g., XPHB) sources; dedupe & normalize.  
3. **Maintainable**: updates are “drop new source + rebuild,” not hand patches.  
4. **Fast lookups**: prebuilt indexes (e.g., *spells by class & level*).

---

## Canonical Layout

```
rules/
  2024/
    spell.json
    class.json
    feat.json
    subclass.json
    ... (other allowed 2024 categories)
    mappings/
      spell_to_classes_xphb.json
      spell_levels_xphb.json

indexes/
  2024/
    spells_by_class_level.json
    feats_by_prereq.json
    subclass_features.json

scripts/
  (build, verify, index builders, CI validators)

docs/
  reports/
    2025-10-Phase9-Verification.md  (public snapshot)

reports/   (ignored; local scratch outputs)
```

> **Reports policy**  
> - `docs/reports/**` is **tracked** (public snapshots for PRs/audits).  
> - Top-level `/reports/` remains **ignored** for private scratch output.

---

## Build Pipeline (Phase 9 steady state)

**Orchestrator:** `scripts/run_all.ps1`

1. **Build Rules — `scripts/build_rules_2024.py`**  
   - Read local 5etools `--src`  
   - Filter to 2024/X* (e.g., XPHB/XDMG/XMM)  
   - Dedupe (e.g., ~774 raw spells → **391 unique**)  
   - Write canonical JSON to `rules/2024/`  
   - Emit helper mappings to `rules/2024/mappings/`

2. **Verify — `scripts/verify_rules_2024.py`**  
   - Compare counts vs. source  
   - Flag mismatches/missing categories  
   - Confirm expected exclusions (adventures, traps, psionics, legacy fluff, etc.)

3. **Build Indexes — `scripts/build_indexes_2024.py`**  
   - Consume baseline + mappings  
   - Write compact indexes to `indexes/2024/`

4. **Commit + (optional) Tag**  
   - Stage updated rules/indexes  
   - Commit with a clear, single-purpose message; tag when appropriate

---

## CI & Hygiene (keep it green)

- **Single GitHub Actions workflow**: `.github/workflows/ci-validate.yml`  
  - **Hygiene job first**: enforces **UTF-8 (no BOM)** + **LF** endings across tracked text  
  - **Matrix validation (minimal set)**: `spell`, `index:spells_by_class_level`  
  - Per-target summary artifact uploaded with **sanitized names**

- **Local gate before any commit** (must pass):
```powershell
Set-Location C:\MyGitHubRepos\Onednd-Rules-and-Builds
python scripts\ci\hygiene_check.py
```

- **Pre-commit hook** runs the same hygiene script; commits are blocked on failure.

> Full environment pins and safe patterns are in **`OneDND-Assistant-Playbook.md`**.

---

## Usage — Refresh Against Latest 5etools

### One-shot (recommended)
```powershell
.\scripts\run_all.ps1
```

### Step-by-step
```powershell
# 1) Build rules
python scripts\build_rules_2024.py --src "C:\5eTools\5etools-src-main\data" --out ".\rules\2024"

# 2) Verify
python scripts\verify_rules_2024.py --src "C:\5eTools\5etools-src-main\data" --out ".\rules\2024"

# 3) Build indexes
python scripts\build_indexes_2024.py --baseline ".\rules\2024" --out ".\indexes\2024"

# 4) Commit (after local hygiene passes)
python scripts\ci\hygiene_check.py
git add rules/2024 indexes/2024
git commit -m "Refresh One D&D 2024 rules and indexes"
git push
```

**Key notes**
- Spells: **~391 unique** after dedupe  
- Spell index classes (8): **Bard, Cleric, Druid, Paladin, Ranger, Sorcerer, Warlock, Wizard**  
- Only 2024/X* categories included; exclusions are intentional and verified

---

## Maintenance & Updates

- **New official content**: drop into the 5etools source, re-run the pipeline, commit refreshed outputs.  
- **Third-party content**: integrate into the source folder **before** running builds; whitelist explicitly if needed.  
- **New categories**: update build/verify/index scripts to allowlist/exclude explicitly.  
- **Public verification snapshots**: publish to `docs/reports/` (tracked); keep `/reports/` ignored.

---

## Phase 9 Outcome (baseline)

- CI **green** with a minimal matrix  
- Hygiene enforced locally & in CI (UTF-8 no BOM, LF only)  
- Legacy validators/workflows archived; single consolidated workflow active  
- Public “clean state” snapshot: `docs/reports/2025-10-Phase9-Verification.md`

---

## Transition to Phase 10 (planned next steps)

- Gradually expand CI matrix (e.g., `index:feats_by_prereq`, `index:subclass_features_by_level`)  
- Schema hardening + data-diff artifacts for PRs  
- Optional performance smoke tests (build time, file size thresholds)  
- Optional release packaging (bundled JSON + checksums)

---

## PR Checklist (paste into PR description)

- [ ] Local hygiene passes (`python scripts\ci\hygiene_check.py`)  
- [ ] Only 2024/X* sources included; exclusions unchanged  
- [ ] `rules/2024/` and `indexes/2024/` updated as intended  
- [ ] CI green (hygiene + matrix) with artifacts  
- [ ] Public snapshots (if any) live under `docs/reports/` and are normalized (UTF-8 no BOM, LF)  
- [ ] Commit message is clear and single-purpose

---

## References

- **Environment & guardrails**: `OneDND-Assistant-Playbook.md`  
- **Verification snapshot**: `docs/reports/2025-10-Phase9-Verification.md`
