import json, os, sys
from jsonschema import Draft202012Validator

REPO   = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA   = os.path.join(REPO, "rules", "2024", "object.json")
SCHEMA = os.path.join(REPO, "schema", "2024", "v1", "object.schema.json")

def ascii(s:str)->str:
    try: return s.encode("ascii","ignore").decode("ascii")
    except Exception: return str(s)

def load_json(label:str, path:str):
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    except Exception as e:
        sys.stderr.write(ascii(f"[ERROR] Failed to load {label}: {path}\n  -> {e}\n"))
        sys.exit(2)

def main():
    schema = load_json("SCHEMA", SCHEMA)
    data   = load_json("DATA", DATA)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        sys.stderr.write(ascii(f"[FAIL] object.json has {len(errors)} validation error(s):\n"))
        for i, err in enumerate(errors, 1):
            loc = "$" + "".join(f"[{repr(p)}]" if isinstance(p,int) else f".{p}" for p in err.path)
            sys.stderr.write(ascii(f"  {i}. {loc}: {err.message}\n"))
        sys.exit(1)
    sys.stdout.write(ascii("[OK] object.json passed schema validation.\n"))
    sys.exit(0)

if __name__ == "__main__": main()
