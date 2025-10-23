#!/usr/bin/env python3
# Auto-generated Phase 9 validator for: rules.species
import json, sys, pathlib
try:
    from jsonschema import Draft202012Validator as _Validator
except Exception:
    from jsonschema import Draft2020Validator as _Validator

def main() -> int:
    here = pathlib.Path(__file__).resolve()
    repo = here.parents[2]
    schema = repo / "schema/2024/v1/rules.species.schema.json".replace("\\\\", "/")
    target = repo / "rules/2024/species.json".replace("\\\\", "/")

    if not schema.is_file():
        print(f"[ERROR] Schema missing: {schema}", file=sys.stderr); return 2
    if not target.is_file():
        print(f"[ERROR] Target JSON missing: {target}", file=sys.stderr); return 3

    try:
        sch = json.loads(schema.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERROR] Failed to parse schema: {e}", file=sys.stderr); return 4
    try:
        inst = json.loads(target.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERROR] Failed to parse target JSON: {e}", file=sys.stderr); return 5

    v = _Validator(schema=sch)
    errors = sorted(v.iter_errors(inst), key=lambda e: e.path)
    if errors:
        print("[FAIL] Validation errors:")
        for err in errors[:50]:
            loc = "$" + "".join(f"[{repr(p)}]" if isinstance(p, int) else f".{p}" for p in err.path)
            print(f" - {loc}: {err.message}")
        if len(errors) > 50:
            print(f" ... and {len(errors)-50} more")
        return 1

    print(f"[OK] {target.relative_to(repo)} conforms to {schema.relative_to(repo)}.")
    return 0

if __name__ == "__main__":
    sys.exit(main())