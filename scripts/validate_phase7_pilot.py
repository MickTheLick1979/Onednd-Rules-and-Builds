import json, sys, pathlib
from jsonschema import validate, Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
TARGET = ROOT / "indexes" / "2024" / "spells_by_class_level.json"
SCHEMA = ROOT / "schema" / "2024" / "v1" / "indexes.spells_by_class_level.schema.json"

def main():
    try:
        data = json.loads(TARGET.read_text(encoding="utf-8-sig"))
        schema = json.loads(SCHEMA.read_text(encoding="utf-8-sig"))
    except Exception as e:
        print(f"ERROR: failed to read files: {e}")
        sys.exit(1)

    v = Draft202012Validator(schema)
    errors = sorted(v.iter_errors(data), key=lambda e: e.path)
    if errors:
        print(f"❌ Phase 7 pilot failed for {TARGET}")
        for err in errors:
            loc = "/".join([str(x) for x in err.path]) or "(root)"
            print(f"- [{loc}] {err.message}")
        sys.exit(1)

    print(f"✅ Phase 7 pilot OK: {TARGET}")
    sys.exit(0)

if __name__ == "__main__":
    main()
