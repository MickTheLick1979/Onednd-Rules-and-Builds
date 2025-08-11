# verify_sources.py
import argparse, json, sys
from pathlib import Path
from collections import Counter, defaultdict

ALLOWED_SOURCES = {"XPHB", "XMM", "XDMG"}  # 2024 core books

def iter_entries(obj):
    """Yield every dict entry found in arrays at the top level of a 5etools JSON file."""
    if isinstance(obj, dict):
        for v in obj.values():
            if isinstance(v, list):
                for it in v:
                    if isinstance(it, dict):
                        yield it

def is_2024(entry):
    src = entry.get("source")
    if entry.get("basicRules2024") is True:
        return True, src or "basicRules2024"
    return (src in ALLOWED_SOURCES), src

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="Path to 5etools data folder")
    args = ap.parse_args()

    data_dir = Path(args.src)
    if not data_dir.exists():
        print(f"ERROR: {data_dir} not found", file=sys.stderr)
        sys.exit(2)

    kept_sources = Counter()
    kept_by_file = defaultdict(Counter)
    total_checked = 0
    total_kept = 0
    unexpected_sources = Counter()

    for p in sorted(data_dir.rglob("*.json")):
        try:
            with p.open("r", encoding="utf-8") as f:
                obj = json.load(f)
        except Exception:
            continue  # skip weird files

        for e in iter_entries(obj):
            total_checked += 1
            keep, src = is_2024(e)
            if keep:
                total_kept += 1
                kept_sources[src] += 1
                kept_by_file[p.name][src] += 1
                if src not in ALLOWED_SOURCES and src != "basicRules2024":
                    unexpected_sources[src] += 1

    print("\n=== VERIFY 2024 FILTER ===")
    print(f"Total entries scanned : {total_checked}")
    print(f"Total entries kept    : {total_kept}\n")

    print("Unique sources among KEPT entries:")
    for s, c in kept_sources.most_common():
        print(f"  - {s:15} : {c}")

    if unexpected_sources:
        print("\n!!! Unexpected sources found among kept entries !!!")
        for s, c in unexpected_sources.most_common():
            print(f"  - {s:15} : {c}")
        sys.exit(1)
    else:
        print("\nNo unexpected sources. All kept entries are from XPHB/XMM/XDMG or flagged basicRules2024.")

    print("\nTop files contributing to kept entries (first 10):")
    for fname, ctr in sorted(kept_by_file.items(), key=lambda kv: sum(kv[1].values()), reverse=True)[:10]:
        print(f"  - {fname:28} -> {sum(ctr.values())} kept  {dict(ctr)}")

if __name__ == "__main__":
    main()
