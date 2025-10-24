import os, sys, glob
from scripts._validation_common import run_standard_validation

def resolve_data_path():
    candidates = [
        os.path.join("rules", "2024", "sense.json"),
        os.path.join("rules", "2024", "Sense.json"),
    ]
    # wildcard fallback (first match wins)
    candidates.extend(sorted(glob.glob(os.path.join("rules", "2024", "*sense*.json"))))
    for p in candidates:
        if os.path.isfile(p):
            return p
    return None

def main():
    data_path = resolve_data_path()
    if not data_path:
        print("ERROR: could not locate sense data file under rules/2024.", flush=True)
        sys.exit(2)

    run_standard_validation(
        category="sense",
        data_path=data_path,
        schema_path=os.path.join("schema", "2024", "v1", "rules.sense.schema.json"),
        array_keys=["sense"]
    )
    print(f"[OK] Phase 9: sense validated cleanly ({data_path})", flush=True)

if __name__ == "__main__":
    main()