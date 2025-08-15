import argparse
import json
import re
from pathlib import Path
from collections import defaultdict

# Treat any source that starts with "X" as 2024+ (XPHB, XMM, XDMG, etc.)
X_SRC = re.compile(r"^X[A-Z0-9]+")

# Keys we expect to appear at the top level in 5etools JSON files
# (this is not exhaustive, but it covers the big hitters; the script also learns new keys it sees)
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
    # possible/likely future keys
    "species","speciesFeature","speciesFluff",
}

# Categories we intentionally exclude from the 2024 character-build scope
INTENTIONALLY_EXCLUDED = {
    "adventure", "artObjects", "deck", "encounter", "entries",
    "facility", "facilityFluff", "name",
}

def is_2024_entry(entry: dict) -> bool:
    """Heuristic: treat as 2024 if source starts with 'X', or 2024 flags are set, or _version says >=2024."""
    if not isinstance(entry, dict):
        return False
    src = str(entry.get("source", "")).strip()
    if X_SRC.match(src):
        return True
    if entry.get("srd52") or entry.get("basicRules2024") or entry.get("basicRules2024", False):
        return True
    # Some entries pack per-source flags under 'otherSources' or nested structures; keep it simple here.
    return False

def iter_entries(data):
    """
    Yields (top_key, entry) pairs for every list of objects found under a top-level key.
    Handles files that use {'data': [...]} wrapping or direct top-level keys.
    """
    if isinstance(data, dict):
        # 5etools sometimes nests real content under "data": [...]
        if "data" in data and isinstance(data["data"], list):
            for block in data["data"]:
                if isinstance(block, dict):
                    for k, v in block.items():
                        if isinstance(v, list):
                            yield k, v
        # also consider direct lists under known keys
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
        key = p.stem  # filename without extension
        data = load_json(p)
        if data is None:
            continue
        # Our build script writes either {"<key>":[...]} or a flat list in some edge cases.
        if isinstance(data, dict) and key in data and isinstance(data[key], list):
            counts[key] = len(data[key])
        elif isinstance(data, list):
            counts[key] = len(data)
        else:
            # try to find the first list value
            n = 0
            for v in data.values() if isinstance(data, dict) else []:
                if isinstance(v, list):
                    n = len(v); break
            counts[key] = n
    return counts

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Verify 2024/X* categories present in output.")
    ap.add_argument("--src", required=True, help="Path to 5etools src data folder (e.g., ...\\5etools-src-main\\data)")
    ap.add_argument("--out", required=True, help="Path to output folder (e.g., ...\\rules\\2024)")
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

    # Build union of keys we saw in source (with any 2024 entries) and keys present in output
    keys = sorted(set([k for k,c in src_counts.items() if c > 0]) | set(out_counts.keys()))

    print("\n=== Category Check (2024/X* only) ===")
    print(f"{'Category':<20} {'SRC_2024':>10} {'OUT':>10} {'Status'}")
    print("-"*60)
    issues = []
    for key in keys:
        s = src_counts.get(key, 0)
        o = out_counts.get(key, 0)

        if key in INTENTIONALLY_EXCLUDED:
            status = "INTENTIONALLY EXCLUDED"
            # Do not record as an issue
        else:
            if s > 0 and o == 0:
                status = "MISSING in output"
                issues.append((key, s, o, status))
            elif o > s and s == 0:
                status = "Output has entries but none detected in src (check filter)"
                issues.append((key, s, o, status))
            elif s != o:
                status = "Count mismatch (could be expected if you filter)"
                issues.append((key, s, o, status))
            else:
                status = "OK"

        print(f"{key:<20} {s:>10} {o:>10} {status}")

    if not issues:
        print("\nNo obvious whole-category gaps detected. Looks consistent. ✅")
    else:
        print("\nPotential issues found:")
        for key, s, o, status in issues:
            print(f"  - {key}: src={s}, out={o} -> {status}")

if __name__ == "__main__":
    main()
