#!/usr/bin/env python3
r"""
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
from json import JSONDecodeError
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

# ----------------- IO helpers -----------------

def load_all_json_files(baseline_dir: Path) -> List[Tuple[str, Any]]:
    """Load every top-level JSON file from the baseline directory.
    Returns a list of (filename, data). Ensures UTF-8 and stable filename order.
    Retries with utf-8-sig if a BOM is present.
    """
    files = sorted([p for p in baseline_dir.iterdir() if p.suffix.lower() == ".json"])
    results: List[Tuple[str, Any]] = []
    for p in files:
        try:
            with p.open("r", encoding="utf-8") as f:
                data = json.load(f)
            results.append((p.name, data))
        except (UnicodeDecodeError, JSONDecodeError):
            try:
                with p.open("r", encoding="utf-8-sig") as f:
                    data = json.load(f)
                results.append((p.name, data))
            except Exception as e:
                print(f"[WARN] Failed to read {p.name}: {e}", file=sys.stderr)
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
        f.write("\n")

# ----------------- Spells index -----------------

def _norm_level(spell: Dict[str, Any]) -> int | None:
    lvl = spell.get("level")
    if isinstance(lvl, int):
        return lvl
    if isinstance(lvl, str):
        s = lvl.strip().lower()
        if s in ("cantrip", "0"):
            return 0
        try:
            return int(s)
        except ValueError:
            return None
    li = spell.get("levelInt")
    return li if isinstance(li, int) else None

def _extract_class_names(spell: Dict[str, Any]) -> List[str]:
    """Support multiple encodings of classes on spells. Returns a sorted list."""
    out: set[str] = set()
    classes = spell.get("classes")

    # Simple list of strings
    if isinstance(classes, list):
        for c in classes:
            if isinstance(c, str) and c.strip():
                out.add(c.strip())

    # Dict forms (5etools-style)
    if isinstance(classes, dict):
        for key in ("fromClassList", "fromClassListVariant"):
            lst = classes.get(key)
            if isinstance(lst, list):
                for entry in lst:
                    name = (entry or {}).get("name")
                    if isinstance(name, str) and name.strip():
                        out.add(name.strip())
        subs = classes.get("fromSubclass")
        if isinstance(subs, list):
            for entry in subs:
                cls = (entry or {}).get("class") or {}
                name = cls.get("name")
                if isinstance(name, str) and name.strip():
                    out.add(name.strip())

    # Flat single-field fallbacks
    for k in ("class", "className"):
        v = spell.get(k)
        if isinstance(v, str) and v.strip():
            out.add(v.strip())

    return sorted(out)

def _build_class_to_lists(all_files: List[Tuple[str, Any]]) -> Dict[str, List[str]]:
    """Map class name -> spell list(s), e.g., {'Cleric':['Divine']} if present."""
    result: Dict[str, List[str]] = {}
    for filename, data in all_files:
        if "class" not in data:
            continue
        classes = data.get("class")
        if not isinstance(classes, list):
            continue
        for cls in classes:
            if not isinstance(cls, dict):
                continue
            name = cls.get("name")
            if not isinstance(name, str) or not name.strip():
                continue

            lists: List[str] = []
            for key in ("spellLists", "spellcastingList"):
                v = cls.get(key)
                if isinstance(v, list):
                    lists.extend([x for x in v if isinstance(x, str) and x.strip()])
                elif isinstance(v, str) and v.strip():
                    lists.append(v.strip())

            sc = cls.get("spellcasting")
            if isinstance(sc, dict):
                for key in ("spellLists", "spellcastingList"):
                    v = sc.get(key)
                    if isinstance(v, list):
                        lists.extend([x for x in v if isinstance(x, str) and x.strip()])
                    elif isinstance(v, str) and v.strip():
                        lists.append(v.strip())

            if lists:
                result[name.strip()] = sorted(set(lists))
    return result

def _extract_spell_lists(spell: Dict[str, Any]) -> List[str]:
    out: List[str] = []
    v = spell.get("spellLists")
    if isinstance(v, list):
        out.extend([x for x in v if isinstance(x, str) and x.strip()])
    elif isinstance(v, str) and v.strip():
        out.append(v.strip())
    return sorted(set(out))

def build_spells_by_class_level(all_files: List[Tuple[str, Any]]) -> Dict[str, Any]:
    """
    Output:
      { "<ClassName>": { "<Level:int>": ["Spell A","Spell B", ...] } }
    Priority:
      1) Use explicit class links if present.
      2) Else, infer via spell list mapping (Arcane/Divine/Primal) if classes expose lists.
    """
    index: Dict[str, Dict[int, List[str]]] = {}
    class_to_lists = _build_class_to_lists(all_files)

    # Reverse map: list -> [classes]
    list_to_classes: Dict[str, List[str]] = {}
    for cls, lists in class_to_lists.items():
        for L in lists:
            list_to_classes.setdefault(L, []).append(cls)
    for L in list_to_classes:
        list_to_classes[L].sort()

    for filename, data in all_files:
        spells = data.get("spell")
        if not isinstance(spells, list):
            continue
        for spell in spells:
            if not isinstance(spell, dict):
                continue
            name = spell.get("name")
            if not isinstance(name, str) or not name.strip():
                continue
            level = _norm_level(spell)
            if level is None:
                continue

            class_names = _extract_class_names(spell)
            if not class_names:
                lists = _extract_spell_lists(spell)
                mapped: set[str] = set()
                for L in lists:
                    mapped.update(list_to_classes.get(L, []))
                class_names = sorted(mapped)

            if not class_names:
                continue

            for cls in class_names:
                index.setdefault(cls, {}).setdefault(level, []).append(name.strip())

    # Deterministic sort + de-dup
    result: Dict[str, Dict[str, List[str]]] = {}
    for cls in sorted(index.keys()):
        lvl_map = index[cls]
        sorted_levels: Dict[str, List[str]] = {}
        for lvl in sorted(lvl_map.keys()):
            sorted_levels[str(lvl)] = sorted(set(lvl_map[lvl]))
        result[cls] = sorted_levels
    return result

# ----------------- Feats index -----------------

_ABIL_MAP = {"str":"STR","dex":"DEX","con":"CON","int":"INT","wis":"WIS","cha":"CHA"}

def _atomic_prereq_keys_from_obj(obj: dict) -> list[str]:
    keys: list[str] = []

    # Level: {"level": 4} or nested
    lvl = obj.get("level")
    if isinstance(lvl, int):
        keys.append(f"Level>={lvl}")
    elif isinstance(lvl, dict):
        lv = lvl.get("level")
        if isinstance(lv, int):
            keys.append(f"Level>={lv}")

    # Ability scores: {"ability":[{"str":13},{"dex":13}]}
    ability = obj.get("ability")
    if isinstance(ability, list):
        for entry in ability:
            if isinstance(entry, dict):
                for k, v in entry.items():
                    k2 = _ABIL_MAP.get(str(k).lower())
                    if k2 and isinstance(v, int):
                        keys.append(f"{k2}>={v}")

    # Other free-form buckets
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

    other = obj.get("other")
    if isinstance(other, str) and other.strip():
        keys.append(f"Other={other.strip()}")

    return keys

def _extract_feat_prereq_keys(feat: dict) -> list[str]:
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

def build_feats_by_prereq(all_files: List[Tuple[str, Any]]) -> Dict[str, List[str]]:
    """
    Output:
      { "<PrereqKey>": ["Feat A","Feat B", ...] }
    """
    index: Dict[str, List[str]] = {}

    for filename, data in all_files:
        feats = data.get("feat")
        if not isinstance(feats, list):
            continue
        for feat in feats:
            if not isinstance(feat, dict):
                continue
            name = feat.get("name")
            if not isinstance(name, str) or not name.strip():
                continue

            keys = _extract_feat_prereq_keys(feat)
            if not keys:
                continue

            nm = name.strip()
            for k in keys:
                index.setdefault(k, []).append(nm)

    out: Dict[str, List[str]] = {}
    for k in sorted(index.keys()):
        out[k] = sorted(set(index[k]))
    return out

# ----------------- Subclass features index (placeholder) -----------------

# -------- Subclass features index --------

def _get_feature_level(obj: dict) -> int | None:
    lvl = obj.get("level")
    if isinstance(lvl, int):
        return lvl
    if isinstance(lvl, dict):
        # tolerate {"level": 6}
        v = lvl.get("level")
        if isinstance(v, int):
            return v
    return None

def _get_feature_class_subclass(obj: dict) -> tuple[str | None, str | None]:
    """
    Try multiple encodings:
      - flat:   className="Monk", subclassShortName="Way of the Four Elements"
      - nested: class={"name":"Monk"}, subclass={"name":"Four Elements"} (or similar)
    """
    cls_name = None
    sub_name = None

    # Flat
    v = obj.get("className")
    if isinstance(v, str) and v.strip():
        cls_name = v.strip()
    v = obj.get("subclassShortName") or obj.get("subclassName")
    if isinstance(v, str) and v.strip():
        sub_name = v.strip()

    # Nested dicts
    if cls_name is None:
        c = obj.get("class")
        if isinstance(c, dict):
            n = c.get("name")
            if isinstance(n, str) and n.strip():
                cls_name = n.strip()
    if sub_name is None:
        s = obj.get("subclass")
        if isinstance(s, dict):
            n = s.get("name")
            if isinstance(n, str) and n.strip():
                sub_name = n.strip()

    return cls_name, sub_name

def build_subclass_features_by_level(all_files: List[Tuple[str, Any]]) -> Dict[str, Any]:
    """
    Output:
      {
        "<ClassName>::<SubclassName>": {
          "<Level:int>": ["Feature A","Feature B", ...]
        }
      }
    """
    idx: Dict[str, Dict[int, List[str]]] = {}

    for filename, data in all_files:
        features = data.get("subclassFeature")
        if not isinstance(features, list):
            continue

        for feat in features:
            if not isinstance(feat, dict):
                continue
            name = feat.get("name")
            if not isinstance(name, str) or not name.strip():
                continue

            level = _get_feature_level(feat)
            if level is None:
                continue

            cls_name, sub_name = _get_feature_class_subclass(feat)
            if not cls_name or not sub_name:
                continue

            key = f"{cls_name}::{sub_name}"
            idx.setdefault(key, {}).setdefault(level, []).append(name.strip())

    # Deterministic output
    out: Dict[str, Dict[str, List[str]]] = {}
    for key in sorted(idx.keys()):
        lvl_map = idx[key]
        sorted_levels: Dict[str, List[str]] = {}
        for lvl in sorted(lvl_map.keys()):
            sorted_levels[str(lvl)] = sorted(set(lvl_map[lvl]))
        out[key] = sorted_levels
    return out


# ----------------- Orchestration -----------------

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

    spells_idx = build_spells_by_class_level(all_files)
    feats_idx = build_feats_by_prereq(all_files)
    subclass_idx = build_subclass_features_by_level(all_files)

    write_json(out_dir, "spells_by_class_level.json", spells_idx)
    write_json(out_dir, "feats_by_prereq.json", feats_idx)
    write_json(out_dir, "subclass_features_by_level.json", subclass_idx)

    print(f"[OK] Wrote indexes to: {out_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
