import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, exceptions as js_exc

def load_json(path):
    with Path(path).open("r", encoding="utf-8-sig") as fh:
        return json.load(fh)

def extract_array(data, array_keys):
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for k in (array_keys or []):
            if k in data and isinstance(data[k], list):
                return data[k]
    print("ERROR: Expected a root array or an object with one of keys: " + ", ".join(array_keys), flush=True, file=sys.stderr)
    return None

def run_standard_validation(category, data_path, schema_path, array_keys):
    try:
        raw = load_json(data_path)
    except FileNotFoundError:
        print(f"ERROR: File not found: {data_path}", flush=True, file=sys.stderr); return 2
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON parse error in {data_path}: {e}", flush=True, file=sys.stderr); return 2

    data = extract_array(raw, array_keys)
    if data is None:
        return 1

    try:
        schema = load_json(schema_path)
        validator = Draft202012Validator(schema)
    except js_exc.SchemaError as e:
        print(f"ERROR: Schema error: {e}", flush=True, file=sys.stderr); return 2
    except Exception as e:
        print(f"ERROR: Schema load error: {e}", flush=True, file=sys.stderr); return 2

    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        print(f"ERROR: Phase 9 ({category}) schema violations: {len(errors)}", flush=True)
        for i, err in enumerate(errors[:25], 1):
            loc = "$" + "".join([f"[{repr(p)}]" if isinstance(p, int) else f".{p}" for p in err.path])
            print(f"  {i:02d}. {loc}: {err.message}", flush=True)
        if len(errors) > 25:
            print(f"  ...and {len(errors)-25} more", flush=True)
        return 1

    print(f"[OK] Phase 9: {category} validated cleanly ({data_path})", flush=True)
    return 0
