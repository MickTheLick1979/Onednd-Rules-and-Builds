# scripts/build_rules_2024.py
# -*- coding: utf-8 -*-

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple, Iterable

# ----------------------------
# Defaults & Configuration
# ----------------------------

# 2024 core books (extend at runtime with --sources)
DEFAULT_ALLOWED_SOURCES = {"XPHB", "XMM", "XDMG"}

# Categories we want for a tight "core rules + items" export.
# Keeping 5etools naming (race*, not species*).
ALLOW_CATEGORIES: Set[str] = {
    # Core rules / mechanics
    "action", "condition", "feat", "featFluff", "language", "languageScript",
    "reward", "sense", "skill", "status", "table", "tableGroup", "variantrule",

    # Character options
    "background", "backgroundFluff",
    "class", "classFeature", "classFluff",
    "subclass", "subclassFeature", "subclassFluff",
    "race", "raceFeature", "raceFluff",

    # Spells
    "spell", "spellFluff",

    # Items & equipment (for optimisation)
    "baseitem", "item", "itemEntry", "itemFluff", "itemGroup",
    "itemMastery", "itemProperty", "itemType", "itemTypeAdditionalEntries",
    "magicItems", "magicvariant",

    # Monsters/objects (rules reference)
    "legendaryGroup", "monster", "monsterFluff", "object", "objectFluff",

    # Hazards/traps/vehicles
    "hazard", "hazardFluff", "trap", "trapFluff", "vehicle", "vehicleFluff",

    # Provenance (optional but useful)
    "book",
}

# Known aggregator/meta categories we never want to write
BLOCKLIST: Set[str] = {
    "_versions", "manifest", "otherSources", "requires", "images", "altArt",
    "backgrounds", "classes", "conditions", "items", "monsters", "spells",
    "subclass-features", "optional-features", "subclasses", "entries",
}

# ----------------------------
# Helpers
# ----------------------------

def parse_csv_set(value: str) -> Set[str]:
    if not value:
        return set()
    return {s.strip() for s in value.split(",") if s.strip()}

def path_matches_any_substring(p: Path, needles: Iterable[str]) -> bool:
    pstr = str(p).replace("\\", "/").lower()
    return any(n.lower() in pstr for n in needles)

def source_string_from(entry: Dict[str, Any]) -> str:
    """Extract a plausible 'source' string from a 5etools entry."""
    for k in ("source", "src", "book", "_source"):
        v = entry.get(k)
        if isinstance(v, str):
            return v.strip()
    return ""

def is_x_source(entry: Dict[str, Any]) -> bool:
    """True if the entry's own source starts with 'X' (XPHB/XDMG/XMM or future X*)."""
    src = source_string_from(entry).upper()
    return bool(src) and src.startswith("X")

def is_allowed_source(entry: Dict[str, Any], allowed_sources: Set[str]) -> bool:
    """True if the entry's source is explicitly in the allowed set (e.g., XPHB/XDMG/XMM)."""
    if not allowed_sources:
        return False
    return source_string_from(entry).upper() in allowed_sources

def keep_entry(entry: Any, allowed_sources: Set[str], accept_xprefix: bool) -> bool:
    """
    Keep only if the entry's OWN source is allowed (or starts with 'X' when enabled).
    Prevents over-pulling via nested child dicts (fixes magicvariant overcount).
    """
    if not isinstance(entry, dict):
        return False

    src = source_string_from(entry).upper()
    if src in allowed_sources:
        return True
    if accept_xprefix and src.startswith("X"):
        return True

    return False

# ----------------------------
# Collection
# ----------------------------

def process_list(
    lst: List[Any],
    category: str,
    allowed_sources: Set[str],
    accept_xprefix: bool,
    accum: Dict[str, List[Dict[str, Any]]],
    dedup: Dict[str, Set[Tuple[str, str]]],
) -> None:
    """
    Inspect a list under a category key (e.g. 'race', 'spell').
    Keep only dict entries with allowed sources; de-dupe on (name, source).
    """
    if category in BLOCKLIST or category not in ALLOW_CATEGORIES:
        return

    kept: List[Dict[str, Any]] = []
    for item in lst:
        if not isinstance(item, dict):
            continue
        if keep_entry(item, allowed_sources, accept_xprefix):
            kept.append(item)

    if not kept:
        return

    if category not in accum:
        accum[category] = []
    if category not in dedup:
        dedup[category] = set()

    seen = dedup[category]
    out = accum[category]

    for obj in kept:
        name = str(obj.get("name", "")).strip()
        source = source_string_from(obj).upper()
        key = (name or json.dumps(obj, sort_keys=True), source or "_NOSRC")
        if key in seen:
            continue
        seen.add(key)
        out.append(obj)

def recursive_collect(
    node: Any,
    allowed_sources: Set[str],
    accept_xprefix: bool,
    accum: Dict[str, List[Dict[str, Any]]],
    dedup: Dict[str, Set[Tuple[str, str]]],
) -> None:
    """
    Walk any JSON node. Whenever we see a dict with a key -> list,
    treat that key as a category (e.g., 'race', 'spell', etc.) and
    filter/collect entries by allowed sources.
    """
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, list):
                if any(isinstance(x, dict) for x in v):
                    process_list(v, str(k), allowed_sources, accept_xprefix, accum, dedup)
                for x in v:
                    recursive_collect(x, allowed_sources, accept_xprefix, accum, dedup)
            else:
                recursive_collect(v, allowed_sources, accept_xprefix, accum, dedup)
    elif isinstance(node, list):
        for x in node:
            recursive_collect(x, allowed_sources, accept_xprefix, accum, dedup)
    # Non-dict/list nodes are ignored

# ----------------------------
# Output
# ----------------------------

def write_outputs(
    out_dir: Path,
    accum: Dict[str, List[Dict[str, Any]]],
    allow_categories: Set[str],
    blocklist: Set[str],
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    total_written = 0

    for category in sorted(accum.keys()):
        if category in blocklist or category not in allow_categories:
            continue

        items = accum.get(category) or []
        if not items:
            continue

        # Stable sort to reduce diffs: by name then source
        def sort_key(o: Dict[str, Any]) -> Tuple[str, str]:
            return (str(o.get("name", "")).lower(), source_string_from(o).upper())
        items_sorted = sorted(items, key=sort_key)

        out_path = out_dir / f"{category}.json"
        payload = {category: items_sorted}

        try:
            out_path.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=False),
                encoding="utf-8",
            )
            print(f"  - Wrote {len(items_sorted):5d} entries -> {out_path.name}")
            total_written += len(items_sorted)
        except Exception as e:
            print(f"  ! Failed to write {out_path}: {e}", file=sys.stderr)

    print(f"\nDone. Total entries written: {total_written}")

# ----------------------------
# Main
# ----------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Build a clean 2024 (X*) rules extract from 5etools JSON."
    )
    parser.add_argument(
        "--src", required=True,
        help="Root folder of 5etools JSON (e.g., C:\\5eTools\\5etools-src-main\\data)",
    )
    parser.add_argument(
        "--out", required=True,
        help="Output folder (e.g., C:\\MyRepo\\rules\\2024)",
    )
    parser.add_argument(
        "--include", default="",
        help="Comma-separated substrings to include in file paths (optional).",
    )
    parser.add_argument(
        "--exclude", default="",
        help="Comma-separated substrings to exclude from file paths (optional).",
    )
    parser.add_argument(
        "--sources", default=",".join(sorted(DEFAULT_ALLOWED_SOURCES)),
        help="Comma-separated explicit source codes, e.g. XPHB,XMM,XDMG. "
             "Leave as default and/or combine with --accept-xprefix for future X* books.",
    )
    parser.add_argument(
        "--accept-xprefix", action="store_true", default=True,
        help="Also accept any entry whose own source starts with 'X' (default: on).",
    )
    parser.add_argument(
        "--no-accept-xprefix", action="store_false", dest="accept_xprefix",
        help="Disable the 'X*' prefix acceptance; use only explicit --sources.",
    )
    parser.add_argument(
        "--allow-extra", default="",
        help="Comma-separated extra categories to allow in addition to the built-in allow-list.",
    )
    parser.add_argument(
        "--block-extra", default="",
        help="Comma-separated extra categories to block in addition to the built-in blocklist.",
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

    # Runtime-adjustable allow/block sets (don’t mutate module constants)
    allow_categories = set(ALLOW_CATEGORIES)
    blocklist = set(BLOCKLIST)
    allow_categories |= parse_csv_set(args.allow_extra)
    blocklist |= parse_csv_set(args.block_extra)

    # Accumulators
    accum: Dict[str, List[Dict[str, Any]]] = {}
    dedup: Dict[str, Set[Tuple[str, str]]] = {}

    files = sorted(src_dir.rglob("*.json"))
    print(f"Scanning {len(files)} JSON files from {src_dir}...")

    scanned = 0
    for jf in files:
        # Include/exclude filtering by substring (case-insensitive):
        if include_filters and not path_matches_any_substring(jf, include_filters):
            continue
        if exclude_filters and path_matches_any_substring(jf, exclude_filters):
            continue

        try:
            text = jf.read_text(encoding="utf-8")
            data = json.loads(text)
        except Exception as e:
            print(f"  ! Skipped (parse error): {jf} :: {e}", file=sys.stderr)
            continue

        recursive_collect(
            data,
            allowed_sources=allowed_sources,
            accept_xprefix=args.accept_xprefix,
            accum=accum,
            dedup=dedup,
        )
        scanned += 1

    print(f"Scanned {scanned} files. Writing outputs to: {out_dir}")
    write_outputs(out_dir, accum, allow_categories, blocklist)

if __name__ == "__main__":
    main()
