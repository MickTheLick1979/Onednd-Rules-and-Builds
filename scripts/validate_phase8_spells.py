#!/usr/bin/env python3
from __future__ import annotations
import json, sys, pathlib
from typing import Any, List
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPELLS_PATH = ROOT / "rules" / "2024" / "spell.json"
SCHEMA_PATH = ROOT / "schema" / "2024" / "v1" / "rules.spell.schema.json"
INDEX_PATH  = ROOT / "indexes" / "2024" / "spells_by_class_level.json"

def load_json(p: pathlib.Path) -> Any:
    with p.open("r", encoding="utf-8-sig") as f:
        return json.load(f)

def validate_spells_schema() -> List[str]:
    errors: List[str] = []
    try:
        data = load_json(SPELLS_PATH)
        schema = load_json(SCHEMA_PATH)
    except Exception as e:
        return [f"✗ Load error: {e}"]
    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: (list(e.path), e.message)):
        loc = "$" + "".join(f"[{p}]" if isinstance(p,int) else f".{p}" for p in err.path)
        errors.append(f"✗ Spells schema violation at {loc}: {err.message}")
    return errors

def validate_spells_index() -> List[str]:
    errors: List[str] = []
    try:
        idx = load_json(INDEX_PATH)
    except Exception as e:
        return [f"✗ Load error: {e}"]
    if not isinstance(idx, dict):
        return [f"✗ spells_by_class_level.json must be an object."]
    for cls, by_level in idx.items():
        if not isinstance(cls, str) or not cls:
            errors.append(f"✗ Class key must be a non-empty string (got {repr(cls)}).")
            continue
        if not isinstance(by_level, dict):
            errors.append(f"✗ '{cls}' value must be object of levels→arrays.")
            continue
        for lvl, arr in by_level.items():
            s = str(lvl)
            if not s.isdigit():
                errors.append(f"✗ '{cls}' level key must be 0..9 (got {repr(lvl)}).")
                continue
            ilvl = int(s)
            if not (0 <= ilvl <= 9):
                errors.append(f"✗ '{cls}' level {ilvl} out of range.")
            if not isinstance(arr, list):
                errors.append(f"✗ '{cls}' level {ilvl}: value must be array.")
                continue
            for i, name in enumerate(arr):
                if not isinstance(name, str) or not name:
                    errors.append(f"✗ '{cls}' level {ilvl}[{i}] must be non-empty string.")
    return errors

def main() -> int:
    all_errors: List[str] = []

    print("▶ Validating rules/2024/spell.json against schema/2024/v1/rules.spell.schema.json ...")
    e = validate_spells_schema()
    if e: all_errors += e; [print(x) for x in e]
    else: print("✅ Spells schema (v1) OK")

    print("▶ Validating indexes/2024/spells_by_class_level.json shape ...")
    e = validate_spells_index()
    if e: all_errors += e; [print(x) for x in e]
    else: print("✅ Spells index OK")

    if all_errors:
        print(f"\n❌ Phase 8 strict validation failed with {len(all_errors)} error(s).", file=sys.stderr)
        return 1
    print("\n✔ All Phase 8 strict checks passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
