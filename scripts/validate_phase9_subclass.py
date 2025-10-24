import glob, sys
from scripts._validation_common import run_standard_validation

def _resolve_path():
    candidates = [
        "rules/2024/subclass.json",
        "rules/2024/Subclass.json",
        "rules/2024/*subclass*.json",
    ]
    for pat in candidates:
        matches = sorted(glob.glob(pat))
        if matches:
            return matches[0]
    print("ERROR: no data file resolved for category 'subclass' under rules/2024", flush=True)
    sys.exit(2)

if __name__ == "__main__":
    resolved = _resolve_path()
    run_standard_validation(
        category="subclass",
        data_path=resolved,
        schema_path="schema/2024/v1/rules.subclass.schema.json",
        array_keys=["subclass", "subclasses"]
    )
