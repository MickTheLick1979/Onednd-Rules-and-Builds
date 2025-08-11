# scripts/query_indexes.py
# Minimal CLI to query 2024 indexes from the repo.
# Examples:
#   python scripts/query_indexes.py feats --prereq "STR>=13"
#   python scripts/query_indexes.py subclass --key "Monk::Shadow" --level 6
#   python scripts/query_indexes.py subclass --class Monk --contains Shadow --level 6

from __future__ import annotations
import argparse, json, sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = REPO_ROOT / "indexes" / "2024"

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Missing file: {path}", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {path}: {e}", file=sys.stderr)
        sys.exit(2)

def cmd_feats(args):
    data = load_json(INDEX_DIR / "feats_by_prereq.json")
    if args.prereq:
        feats = data.get(args.prereq, [])
        if not feats:
            print(f"(no feats found for prereq: {args.prereq})")
        else:
            for name in sorted(feats):
                print(name)
        return
    # List available prereq buckets
    for k in sorted(data.keys()):
        print(k)

def _resolve_subclass_key(data: dict, key: str | None, cls: str | None, contains: str | None):
    if key:
        return key if key in data else None
    candidates = list(data.keys())
    if cls:
        candidates = [k for k in candidates if k.startswith(f"{cls}::")]
    if contains:
        needle = contains.lower()
        candidates = [k for k in candidates if needle in k.lower()]
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    print("Multiple matches; specify --key or refine with --class/--contains:")
    for c in sorted(candidates):
        print("  " + c)
    sys.exit(1)

def cmd_subclass(args):
    data = load_json(INDEX_DIR / "subclass_features_by_level.json")
    key = _resolve_subclass_key(data, args.key, args.cls, args.contains)
    if not key:
        print("(no matching subclass key)")
        sys.exit(1)
    levels = data.get(key, {})
    if args.level is None:
        # Print all levels for the subclass (sorted numerically)
        for lvl in sorted(levels.keys(), key=lambda s: int(s)):
            feats = levels[lvl]
            print(f"{lvl}: {', '.join(feats)}")
        return
    feats = levels.get(str(args.level), [])
    if not feats:
        print(f"(no features at level {args.level} for {key})")
    else:
        for f in feats:
            print(f)

def main():
    p = argparse.ArgumentParser(description="Query One D&D 2024 indexes.")
    sub = p.add_subparsers(dest="cmd", required=True)

    pf = sub.add_parser("feats", help="Query feats_by_prereq.json")
    pf.add_argument("--prereq", help='Exact prereq key, e.g. "STR>=13"')
    pf.set_defaults(func=cmd_feats)

    ps = sub.add_parser("subclass", help="Query subclass_features_by_level.json")
    ps.add_argument("--key", help='Exact key, e.g. "Monk::Shadow"')
    ps.add_argument("--class", dest="cls", help='Class prefix, e.g. Monk')
    ps.add_argument("--contains", help='Substring in subclass name, e.g. Shadow')
    ps.add_argument("--level", type=int, help="Level to show; omit to list all")
    ps.set_defaults(func=cmd_subclass)

    args = p.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
