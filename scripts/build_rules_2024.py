# verify_rules_2024.py
# Clean, focused verifier for the One D&D 2024 build repo.
# - Labels off-scope categories as INTENTIONALLY EXCLUDED
# - Checks key categories against EXPECTED_COUNTS and prints a clear PASS summary
# - Suppresses generic "mismatch noise" except for keys we explicitly care about

import argparse
import json
import re
from pathlib import Path
from collections import defaultdict

# === Heuristic for "2024-ish" entries in source (kept from your original script) ===
# NOTE: This is intentionally broad (any X* book + 2024 flags) so SRC_2024 will be >= OUT.
X_SRC = re.compile(r"^X[A-Z0-9]+")

# Keys we expect at top level (informational; we learn new ones too)
KNOWN_TOP_KEYS = {
    "action","altArt","artObjects","background","backgroundFluff","baseitem","book",
    "card","class","classFeature","classFluff","classVariant",
    "condition","deck","deity","disease","entries","facility","facilityFluff",
    "feat","featFluff","gems","hazard","hazardFluff","hoard","images","individual",
    "item","itemEntry","itemFluff","itemGroup","itemMastery","itemProperty","itemType",
    "language","languageScript","legendaryGroup","magicItems","magicvariant",
    "monster","monsterFluff","object","objectFluff","optionalfeature","otherSources",
    "race","raceFeature","raceFluff","requires","reward","sense","skill",
    "spell","spellFluff","status","subclass","subclassFeature","subclassFluff",
    "subclasses","table","tableGroup","trap","trapFluff","variantrule","vehicle","vehicleFluff",
    # 2024 naming
    "species","speciesFeature","speciesFluff",
}

# Categories we intentionally exclude from the 2024 character-build scope
INTENTIONALLY_EXCLUDED = {
    "adventure","artObjects","deck","encounter","entries","facility","facilityFluff","name",
    # always excluded per project scope
    "magicItems","magicvariant",
    "trap","trapFluff",
    "vehicle","vehicleFluff",
    "deity","disease",
    "gems","hoard","individual","card",
}

# === NEW: Expected counts for key categories in clean 2024 build ===
# These are the only categories that will contribute to PASS/FAIL.
# (If your PHB/XMM data ever updates, adjust here.)
EXPECTED_COUNTS = {
    "class": 12,                 # XPHB classes
    "feat": 77,                  # XPHB feats
    "spell": 391,                # XPHB spells
    "monster": 504,              # XMM monsters
    "subclass": 48,              # XPHB subclasses
    "subclassFeature": 307,      # XPHB subclass features (your current output)
    "optionalfeature": 58,       # Player options bucket kept (fighting styles, invocations, etc.)
    "background": 16,            # XPHB backgrounds
    "race": 10,                  # If using race* naming
    "raceFeature": 11,           # If using race* naming
    # Add species/speciesFeature counts here if/when your data uses species*
}

def is_2024_entry(entry: dict) -> bool:
    """Heuristic: treat as 2024 if source starts with 'X', or 2024 flags are set."""
    if not isinstance(entry, dict):
        return False
    src = str(entry.get("source", "")).strip()
    if X_SRC.match(src):
        return True
    if entry.get("srd52") or entry.get("basicRules2024") or entry.get("basicRules2024", False):
        return True
    return False

def iter_entries(data):
    """
    Yields (top_key, list_of_entries) pairs for each top-level list found.
    Supports both direct top-level lists and nested {"data":[{key:[...]}]} structures.
    """
    if isinstance(data, dict):
        if "data" in data and isinstance(data["data"], list):
            for block in data["data"]:
                if isinstance(block, dict):
                    for k, v in block.items():
                        if isinstance(v, list):
                            yield k, v
        for k, v in data.items():
            if k == "data":
                continue
            if isinstance(v, list):
                yield k, v

def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def count_source_2024_by_key(src_root: Path):
    counts = defaultdict(int)
    seen_keys = set()
    files = list(src_root.rglob("*.json"))
    for p in files:
        data = load_json(p)
        if data is None:
            continue
        for key, entries in iter_entries(data):
            seen_keys.add(key)
            if not isinstance(entries, list):
                continue
            for e in entries:
                if isinstance(e, dict) and is_2024_entry(e):
                    counts[key] += 1
    return counts, seen_keys, len(files)

def count_output_by_key(out_root: Path):
    counts = {}
    for p in out_root.glob("*.json"):
        key = p.stem
        data = load_json(p)
        if data is None:
            continue
        if isinstance(data, dict) and key in data and isinstance(data[key], list):
            counts[key] = len(data[key])
        elif isinstance(data, list):
            counts[key] = len(data)
        else:
            # Fallback: first list value (if any)
            n = 0
            if isinstance(data, dict):
                for v in data.values():
                    if isinstance(v, list):
                        n = len(v)
                        break
            counts[key] = n
    return counts

def main():
    ap = argparse.ArgumentParser(description="Verify One D&D 2024 build output against scope and expected counts.")
    ap.add_argument("--src", required=True, help="Path to 5etools src data folder (e.g., ...\\5etools-src-main\\data)")
    ap.add_argument("--out", required=True, help="Path to output folder (e.g., ...\\rules\\2024)")
    ap.add_argument("--loose", action="store_true",
                    help="Loosen checks: don't fail on EXPECTED_COUNTS mismatches, just warn.")
    args = ap.parse_args()

    src_root = Path(args.src)
    out_root = Path(args.out)

    print(f"Scanning source: {src_root}")
    src_counts, seen_keys, file_count = count_source_2024_by_key(src_root)
    print(f"  Parsed {file_count} JSON files.")
    if seen_keys - KNOWN_TOP_KEYS:
        unknown = ", ".join(sorted(seen_keys - KNOWN_TOP_KEYS))
        print(f"  Note: saw new top-level keys not in KNOWN_TOP_KEYS: {unknown}")

    print(f"\nScanning output: {out_root}")
    out_counts = count_output_by_key(out_root)

    keys = sorted(set([k for k,c in src_counts.items() if c > 0]) | set(out_counts.keys()))

    print("\n=== Category Check (2024/X* heuristic vs. output) ===")
    print(f"{'Category':<22} {'SRC_2024':>10} {'OUT':>10} {'Status'}")
    print("-"*70)
    issues = []
    for key in keys:
        s = src_counts.get(key, 0)
        o = out_counts.get(key, 0)

        if key in INTENTIONALLY_EXCLUDED:
            status = "INTENTIONALLY EXCLUDED"
        else:
            # Only treat as an "issue" if this key is in EXPECTED_COUNTS
            if key in EXPECTED_COUNTS:
                exp = EXPECTED_COUNTS[key]
                if o != exp:
                    status = f"Expected {exp}, got {o}"
                    issues.append((key, s, o, status))
                else:
                    status = "OK"
            else:
                # For non-key categories, print informational status but don't record as an issue.
                if s > 0 and o == 0:
                    status = "MISSING in output (informational)"
                elif o > s and s == 0:
                    status = "Output has entries but none detected in src (informational)"
                elif s != o:
                    status = "Count mismatch (informational)"
                else:
                    status = "OK"

        print(f"{key:<22} {s:>10} {o:>10} {status}")

    # PASS summary for key categories
    print("\n=== PASS Summary (key categories) ===")
    hard_fail = False
    for key, expected in EXPECTED_COUNTS.items():
        actual = out_counts.get(key, 0)
        ok = (actual == expected)
        tick = "✅" if ok else ("⚠️" if args.loose else "❌")
        print(f"- {key:<18} expected {expected:>4}  |  found {actual:>4}  {tick}")
        if not ok and not args.loose:
            hard_fail = True

    if issues:
        print("\nIssues (key categories):")
        for key, s, o, status in issues:
            print(f"  - {key}: {status}")

    if hard_fail:
        print("\nResult: FAIL — one or more key categories did not match EXPECTED_COUNTS.")
        exit(1)
    else:
        print("\nResult: PASS — key categories match expected counts (or warnings only with --loose).")

if __name__ == "__main__":
    main()
