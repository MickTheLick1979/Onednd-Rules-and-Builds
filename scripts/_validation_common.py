import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, validate

def _print_ascii(msg: str) -> None:
    try:
        sys.stdout.write((msg.encode("ascii", "ignore").decode("ascii") + "\n"))
        sys.stdout.flush()
    except Exception:
        print(msg, flush=True)

def load_json(path: str):
    with Path(path).open("r", encoding="utf-8-sig") as fh:
        return json.load(fh)

def load_schema(path: str):
    with Path(path).open("r", encoding="utf-8-sig") as fh:
        return json.load(fh)

def _extract_array_payload(raw, array_keys):
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        # Prefer explicitly-declared keys
        for k in array_keys:
            if k in raw and isinstance(raw[k], list):
                return raw[k]
        # Fallback: first list value found
        for v in raw.values():
            if isinstance(v, list):
                return v
    return None

def run_standard_validation(category: str, data_path: str, schema_path: str, array_keys):
    try:
        raw = load_json(data_path)
    except Exception as e:
        _print_ascii(f"ERROR: failed to read JSON '{data_path}': {e}")
        sys.exit(2)
    try:
        schema = load_schema(schema_path)
    except Exception as e:
        _print_ascii(f"ERROR: failed to read schema '{schema_path}': {e}")
        sys.exit(2)

    payload = _extract_array_payload(raw, array_keys)
    if payload is None:
        _print_ascii("ERROR: Expected a root array or an object with one of keys: " + ", ".join(array_keys))
        sys.exit(1)

    try:
        Draft202012Validator.check_schema(schema)
        validate(instance=payload, schema=schema)
    except Exception as e:
        _print_ascii(f"ERROR: schema validation failed: {e}")
        sys.exit(1)

    _print_ascii(f"[OK] Phase 9: {category} validated cleanly ({data_path})")
