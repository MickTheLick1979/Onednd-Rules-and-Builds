import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, exceptions as js_exc

DEF_DATA = Path("rules/2024/condition.json")
DEF_SCHEMA = Path("schema/2024/v1/rules.condition.schema.json")

def load_json(p: Path):
    with p.open("r", encoding="utf-8-sig") as fh:
        return json.load(fh)

def extract_array(data):
    if isinstance(data, list): return data
    if isinstance(data, dict):
        for k in ("condition","conditions"):
            if k in data and isinstance(data[k], list): return data[k]
    print("❌ Expected a root array or an object with 'condition'/'conditions' list.", file=sys.stderr); sys.exit(1)

def main():
    ap = argparse.ArgumentParser(description="Phase 9 strict validator (conditions)")
    ap.add_argument("--file", default=str(DEF_DATA))
    ap.add_argument("--schema", default=str(DEF_SCHEMA))
    args = ap.parse_args()

    data = extract_array(load_json(Path(args.file)))
    schema = load_json(Path(args.schema))
    validator = Draft202012Validator(schema)

    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        print(f"❌ Phase 9 (conditions) schema violations: {len(errors)}")
        for i, err in enumerate(errors[:25], 1):
            loc = "$" + "".join([f"[{repr(p)}]" if isinstance(p, int) else f".{p}" for p in err.path])
            print(f"  {i:02d}. {loc}: {err.message}")
        if len(errors) > 25: print(f"  ...and {len(errors)-25} more")
        sys.exit(1)
    print("[OK] Phase 9: conditions validated cleanly (rules/2024/condition.json)")

if __name__ == "__main__":
    main()

