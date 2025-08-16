r"""
build_indexes_2024.py
Reads the immutable 2024 core baseline and emits lightweight JSON indexes.

Usage (Windows PowerShell):
  python .\scripts\build_indexes_2024.py ^
    --baseline "C:\MyGitHubRepos\Onednd-Rules-and-Builds\rules\2024\baseline\2025-08-11_core" ^
    --out "C:\MyGitHubRepos\Onednd-Rules-and-Builds\indexes\2024"
"""
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
    Build a dictionary:
      {
        "<ClassName>": {
          "<Level:int>": [<spell_name>, ...]
        }
      }
    """
    index: Dict[str, Dict[int, List[str]]] = {}

    for filename, data in all_files:
        if "spell" not in data:
            continue
        for spell in data["spell"]:
            name = spell.get("name")
            level = spell.get("level")
            classes = spell.get("classes", [])

            if not isinstance(level, int) or not name or not classes:
                continue

            for cls in classes:
                cls_name = cls.strip()
                if cls_name not in index:
                    index[cls_name] = {}
                if level not in index[cls_name]:
                    index[cls_name][level] = []
                index[cls_name][level].append(name)

    # Sort class names, levels, and spell lists for determinism
    sorted_index: Dict[str, Dict[str, List[str]]] = {}
    for cls in sorted(index.keys()):
        sorted_levels = {}
        for lvl in sorted(index[cls].keys()):
            sorted_levels[str(lvl)] = sorted(index[cls][lvl])
        sorted_index[cls] = sorted_levels

    return sorted_index


# -------- Feat prereq helpers --------

_ABIL_MAP = {"str":"STR","dex":"DEX","con":"CON","int":"INT","wis":"WIS","cha":"CHA"}

def _atomic_prereq_keys_from_obj(obj: dict) -> list[str]:
    """
    Convert structured prerequisite objects to flat keys, e.g.:
      STR>=13, Level>=4, Race=Elf, Class=Monk, Subclass=Monk:Way of Shadow, Proficiency=Athletics
    Extend as needed later.
    """
    keys: list[str] = []

    # level: {"level": 4} or {"level": {"level": 4}}
    lvl = obj.get("level")
    if isinstance(lvl, int):
        keys.append(f"Level>={lvl}")
    elif isinstance(lvl, dict):
        lv = lvl.get("level")
        if isinstance(lv, int):
            keys.append(f"Level>={lv}")

    # ability scores: {"ability":[{"str":13},{"dex":13}]}
    ability = obj.get("ability")
    if isinstance(ability, list):
        for entry in ability:
            if isinstance(entry, dict):
                for k, v in entry.items():
                    k2 = _ABIL_MAP.get(str(k).lower())
                    if k2 and isinstance(v, int):
                        keys.append(f"{k2}>={v}")

    # race/background/class/subclass/proficiency (free-form support)
    def _add_vals(prefix: str, val):
        if isinstance(val, str) and val.strip():
            keys.append(f"{prefix}={val.strip()}")
        elif isinstance(val, list):
            for x in val:
                if isinstance(x, str) and x.strip():
                    keys.append(f"{prefix}={x.strip()}")

    _add_vals("Race", obj.get("race"))
    _add_vals("Background", obj.get("background"))
    _add_vals("Class", obj.get("class"))
    _add_vals("Subclass", obj.get("subclass"))
    _add_vals("Proficiency", obj.get("proficiency"))

    # catch‑all
    other = obj.get("other")
    if isinstance(other, str) and other.strip():
        keys.append(f"Other={other.strip()}")

    return keys

def _extract_feat_prereq_keys(feat: dict) -> list[str]:
    """
    Normalise any prerequisite shapes to atomic keys.
    Accepts:
      "prerequisite": "Strength 13+"
      "prerequisite": [ "Elf", {"level":4}, {"ability":[{"str":13}]} ]
      (also supports "prerequisites" as alias)
    """
    keys: list[str] = []
    raw = feat.get("prerequisite", feat.get("prerequisites"))
    if raw is None:
        return keys

    if isinstance(raw, str):
        s = raw.strip()
        if s:
            keys.append(s)
        return keys

    if isinstance(raw, list):
        for el in raw:
            if isinstance(el, str) and el.strip():
                keys.append(el.strip())
            elif isinstance(el, dict):
                keys.extend(_atomic_prereq_keys_from_obj(el))
        return keys

    if isinstance(raw, dict):
        keys.extend(_atomic_prereq_keys_from_obj(raw))
        return keys

    return keys

def build_feats_by_prereq(all_files: list[tuple[str, dict]]) -> dict[str, list[str]]:
    """
    Output shape:
      { "<PrereqKey>": ["Feat A","Feat B"]()


def build_subclass_features_by_level(all_files: List[Tuple[str, Any]]) -> Dict[str, Any]:
    """
    Placeholder: returns an empty structure for now.
    Next step we'll fill in:
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


