#!/usr/bin/env python3
# Validate rules/2024/background.json against schema/2024/v1/rules.background.schema.json
import json, sys, pathlib
try:
    from jsonschema import Draft202012Validator as _Validator
except Exception:
    from jsonschema import Draft2020Validator as _Validator

def main() -> int:
    here = pathlib.Path(__file__).resolve()
    repo = here.parents[2]  # .../scripts/phase9 -> scripts -> REPO
    schema = repo / "schema/2024/v1/rules.background.schema.json"
    target = repo / "rules/2024/background.json"

    if not schema.is_file():
        print(f"[ERROR] Schema missing: {schema}", file=sys.stderr); return 2
    if not target.is_file():
        print(f"[ERROR] Target JSON missing: {target}", file=sys.stderr); return 3

    try: sch = json.loads(schema.read_text(encoding="utf-8"))
    except Exception as e: print(f"[ERROR] Failed to parse schema: {e}", file=sys.stderr); return 4

    try: inst = json.loads(target.read_text(encoding="utf-8"))
    except Exception as e: print(f"[ERROR] Failed to parse target JSON: {e}", file=sys.stderr); return 5

    v = _Validator(schema=sch)
    errors = sorted(v.iter_errors(inst), key=lambda e: e.path)
    if errors:
        print("[FAIL] Validation errors:")
        for err in errors[:25]:
            loc = "$" + "".join(f"[{repr(p)}]" if isinstance(p, int) else f".{p}" for p in err.path)
            print(f" - {loc}: {err.message}")
        if len(errors) > 25: print(f" ... and {len(errors)-25} more")
        return 1

    print("[OK] rules/2024/background.json conforms to rules.background schema.")
    return 0

if __name__ == "__main__":
    sys.exit(main())