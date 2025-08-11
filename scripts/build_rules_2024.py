# scripts/build_rules_2024.py
# -*- coding: utf-8 -*-

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple, Iterable

# ----------------------------
# Defaults & Helpers
# ----------------------------

DEFAULT_ALLOWED_SOURCES = {"XPHB", "XMM", "XDMG"}  # 2024 core books
# You can extend at runtime with --sources XPHB,XMM,XDMG,XSOM,... etc.

def parse_csv_set(value: str) -> Set[str]:
    if not value:
        return set()
    return {s.strip() for s in value.split(",") if s.strip()}

def path_matches_any_substring(p: Path, needles: Iterable[str]) -> bool:
    pstr = str(p).replace("\\", "/").lower()
    return any(n.lower() in pstr for n in needles)

# ----------------------------
# Filtering Logic
# ----------------------------

def keep_entry(entry: Any, allowed_sources: Set[str]) -> bool:
    """
    Return True if this object (dict) or something immediately inside it
    has an allowed 'source'. Robust against strings, lists, etc.
    """
    if not isinstance(entry, dict):
        return False

    # Direct source on the entry
    source = str(entry.get("source", "")).upper()
    if source in allowed_sources:
        return True

    # If any immediate child dict has an allowed source, keep
    for v in entry.values():
        if isinstance(v, dict):
            child_src = str(v.get("source", "")).upper()
            if child_src in allowed_sources:
                return True

    return False

def process_list(
    lst: List[Any],
    category: str,
    allowed_sources: Set[str],
    accum: Dict[str, List[Dict[str, Any]]],
    dedup: Dict[str, Set[Tuple[str, str]]],
) -> None:
    """
    Look at a list that sits under a category key (e.g. "race", "spell").
    Keep only dict entries with allowed source, and dedupe on (name, source).
    """
    kept: List[Dict[str, Any]] = []

    for item in lst:
        if not isinstance(item, dict):
            # Ignore non-dict items
            continue
        if keep_entry(item, allowed_sources):
            kept.append(item)

    if not kept:
        return

    # Init buckets
    if category not in accum:
        accum[category] = []
    if category not in dedup:
        dedup[category] = set()

    seen = dedup[category]
    out = accum[category]

    for obj in kept:
        name = str(obj.get("name", "")).strip()
        source = str(obj.get("source", "")).upper()
        # Some categories may miss 'name'—fall back to repr to avoid crash
        key = (name or json.dumps(obj, sort_keys=True), source)
        if key in seen:
            continue
        seen.add(key)
        out.append(obj)

def recursive_collect(
    node: Any,
    allowed_sources: Set[str],
    accum: Dict[str, List[Dict[str, Any]]],
    dedup: Dict[str, Set[Tuple[str, str]]],
) -> None:
    """
    Walk any JSON node. Whenever we see a dict with a key -> list,
    treat that key as a category (e.g. 'race', 'species', 'spell', etc.)
    and attempt to filter/collect entries by allowed sources.
    """
    if isinstance(node, dict):
        for k, v in node.items():
            # If this value is a list, see if it looks like a list of objects
            if isinstance(v, list):
                # Only attempt to process lists that *might* contain dict entries.
                if any(isinstance(x, dict) for x in v):
                    # Category is the key name (e.g., "race", "species", "spell", ...)
                    category = str(k)
                    process_list(v, category, allowed_sources, accum, dedup)
                # Also recurse into list contents to catch deeper nests
                for x in v:
                    recursive_collect(x, allowed_sources, accum, dedup)
            else:
                recursive_collect(v, allowed_sources, accum, dedup)

    elif isinstance(node, list):
        for x in node:
            recursive_collect(x, allowed_sources, accum, dedup)
    # Non-dict/list nodes are ignored

# ----------------------------
# File Scanning
# ----------------------------

def scan_file(
    filepath: Path,
    allowed_sources: Set[str],
    accum: Dict[str, List[Dict[str, Any]]],
    dedup: Dict[str, Set[Tuple[str, str]]],
) -> None:
    try:
        text = filepath.read_text(encoding="utf-8")
        data = json.loads(text)
    except Exception as e:
        print(f"  ! Skipped (parse error): {filepath} :: {e}", file=sys.stderr)
        return

    # Walk the JSON to collect matching entries into accum
    recursive_collect(data, allowed_sources, accum, dedup)

# ----------------------------
# Output
# ----------------------------

def write_outputs(out_dir: Path, accum: Dict[str, List[Dict[str, Any]]]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    total_written = 0

    for category, items in sorted(accum.items()):
        # Skip empty buckets (shouldn't happen)
        if not items:
            continue

        # Write each category to its own JSON file for clarity
        # File name: e.g. race.json, species.json, spell.json, etc.
        out_path = out_dir / f"{category}.json"
        payload = {category: items}

        try:
            out_path.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=False),
                encoding="utf-8",
            )
            print(f"  - Wrote {len(items):5d} entries -> {out_path.name}")
            total_written += len(items)
        except Exception as e:
            print(f"  ! Failed to write {out_path}: {e}", file=sys.stderr)

    print(f"\nDone. Total entries written: {total_written}")

# ----------------------------
# Main
# ----------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Build 2024 rules extracts from 5etools JSON by allowed sources."
    )
    parser.add_argument(
        "--src",
        required=True,
        help="Root folder of 5etools JSON (e.g., C:\\5eTools\\5etools-src-main\\data)",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output folder (e.g., C:\\MyRepo\\rules\\2024)",
    )
    parser.add_argument(
        "--include",
        default="",
        help="Comma-separated substrings to include in file paths (optional).",
    )
    parser.add_argument(
        "--exclude",
        default="",
        help="Comma-separated substrings to exclude from file paths (optional).",
    )
    parser.add_argument(
        "--sources",
        default=",".join(sorted(DEFAULT_ALLOWED_SOURCES)),
        help=f"Comma-separated source codes (default: {','.join(sorted(DEFAULT_ALLOWED_SOURCES))}).",
    )

    args = parser.parse_args()

    src_dir = Path(args.src)
    out_dir = Path(args.out)

    if not src_dir.exists():
        print(f"Source folder not found: {src_dir}", file=sys.stderr)
        sys.exit(1)

    include_filters = parse_csv_set(args.include)
    exclude_filters = parse_csv_set(args.exclude)
    allowed_sources = {s.upper() for s in parse_csv_set(args.sources)} or set(DEFAULT_ALLOWED_SOURCES)

    # Accumulators
    accum: Dict[str, List[Dict[str, Any]]] = {}  # category -> list of dicts
    dedup: Dict[str, Set[Tuple[str, str]]] = {}   # category -> {(name, source)}

    files = sorted(src_dir.rglob("*.json"))
    print(f"Scanning {len(files)} JSON files from {src_dir}...")

    scanned = 0
    for jf in files:
        # Include/exclude filtering by substring (case-insensitive):
        if include_filters and not path_matches_any_substring(jf, include_filters):
            continue
        if exclude_filters and path_matches_any_substring(jf, exclude_filters):
            continue

        scan_file(jf, allowed_sources, accum, dedup)
        scanned += 1

    print(f"Scanned {scanned} files. Writing outputs to: {out_dir}")
    write_outputs(out_dir, accum)

if __name__ == "__main__":
    main()
