#!/usr/bin/env python3
"""
build_indexes_2024.py
Reads the immutable 2024 core baseline and emits lightweight JSON indexes.

Usage (Windows PowerShell):
  python .\scripts\build_indexes_2024.py ^
    --baseline "C:\MyGitHubRepos\Onednd-Rules-and-Builds\rules\2024\baseline\2025-08-11_core" ^
    --out "C:\MyGitHubRepos\Onednd-Rules-and-Builds\indexes\2024"

Design goals:
- Minimal, readable, easy to extend (add a new build_* function and register it).
- Pure reader: baseline is the only data source; no mutation.
- Deterministic output: stable ordering and formatting.
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

def load_all_json_files(baseline_dir: Path) -> List[Tuple[str, Any]]:
    """Load every top-level JSON file from the baseline directory.
    Returns a list of (filename, data). Ensures UTF-8 and stable filename order.
    """
    files = sorted([p for p in baseline_dir.iterdir() if p.suffix.lower() == ".json"])
    results: List[Tuple[str, Any]] = []
    for p in files:
        try:
            with p.open("r", encoding="utf-8") as f:
                data = json.load(f)
            results.append((p.name, data))
        except Exception as e:
            print(f"[WARN] Failed to read {p.name}: {e}", file=sys.stderr)
    return results

def ensure_out(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

def write_json(out_dir: Path, filename: str, payload: Any) -> None:
    """Write compact, deterministic JSON with sorted keys."""
    path = out_dir / filename
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        f.write("\n")  # nice final newline

# ---------- Index builders (add new ones here) ----------

def build_spells_by_class_level(all_files: List[Tuple[str, Any]]) -> Dict[str, Any]:
    """
    Placeholder: returns an empty structure for now.
    Next step we’ll fill in:
      { "<ClassName>": { "<Level:int>": [ {spell...}, ... ] }, ... }
    """
    return {}

def build_feats_by_prereq(all_files: List[Tuple[str, Any]]) -> Dict[str, Any]:
    """
    Placeholder: returns an empty structure for now.
    Next step we’ll fill in:
      { "<PrereqKey>": [ {feat...}, ... ] }
      e.g., "STR>=13", "Race=Elf", "Level>=4", etc.
    """
    return {}

def build_subclass_features_by_level(all_files: List[Tuple[str, Any]]) -> Dict[str, Any]:
    """
    Placeholder: returns an empty structure for now.
    Next step we’ll fill in:
      { "<ClassName>::<SubclassName>": { "<Level:int>": [ {feature...}, ... ] } }
    """
    return {}

# ---------- Orchestration ----------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True, type=Path, help="Path to dated baseline folder")
    ap.add_argument("--out", required=True, type=Path, help="Path to indexes/2024 output folder")
    args = ap.parse_args()

    baseline_dir: Path = args.baseline
    out_dir: Path = args.out

    if not baseline_dir.exists():
        print(f"[ERR] Baseline folder not found: {baseline_dir}", file=sys.stderr)
        return 2

    ensure_out(out_dir)

    all_files = load_all_json_files(baseline_dir)
    print(f"[INFO] Loaded {len(all_files)} JSON files from baseline '{baseline_dir.name}'")

    # Build each index (currently placeholders)
    spells_idx = build_spells_by_class_level(all_files)
    feats_idx = build_feats_by_prereq(all_files)
    subclass_idx = build_subclass_features_by_level(all_files)

    # Write to disk (filenames fixed so other tools can rely on them)
    write_json(out_dir, "spells_by_class_level.json", spells_idx)
    write_json(out_dir, "feats_by_prereq.json", feats_idx)
    write_json(out_dir, "subclass_features_by_level.json", subclass_idx)

    print(f"[OK] Wrote indexes to: {out_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
