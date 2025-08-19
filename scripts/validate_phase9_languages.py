import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, exceptions as js_exc

DEF_DATA = Path("rules/2024/language.json")
DEF_SCHEMA = Path("schema/2024/v1/rules.language.schema.json")

def load_json(p: Path):
    try:
        with p.open("r", encoding="utf-8-sig") as fh:
            return json.load(fh)
    except FileNotFoundError:
        print(f"❌ File not found: {p}", file=sys.stderr); sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"❌ JSON parse error in {p}: {e}", file=sys.stderr); sys.exit(2)

def extract_array(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for k in ("language", "languages"):
            if k in data and isinstance(data[k], list):
                return data[k]
    print("❌ Expected a root array or an object with 'language'/'languages' list.", file=sys.stderr)
    sys.exit(1)

def main():
    ap = argparse.ArgumentParser(description="Phase 9 strict validator (languages)")
    ap.add_argument("--file", default=str(DEF_DATA), help="Path to language.json")
    ap.add_argument("--schema", default=str(DEF_SCHEMA), help="Path to language schema")
    args = ap.parse_args()

    data = extract_array(load_json(Path(args.file)))
    schema = load_json(Path(args.schema))
    try:
        validator = Draft202012Validator(schema)
    except js_exc.SchemaError as e:
        print(f"❌ Schema error: {e}", file=sys.stderr); sys.exit(2)

    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        print(f"❌ Phase 9 (languages) schema violations: {len(errors)}")
        for i, err in enumerate(errors[:25], 1):
            loc = "$" + "".join([f"[{repr(p)}]" if isinstance(p, int) else f".{p}" for p in err.path])
            print(f"  {i:02d}. {loc}: {err.message}")
        if len(errors) > 25:
            print(f"  ...and {len(errors)-25} more")
        sys.exit(1)

    print("✅ Phase 9: languages validated cleanly (rules/2024/language.json)")

if __name__ == "__main__":
    main()
