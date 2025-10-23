import os, sys, glob
from scripts._validation_common import run_standard_validation

def _resolve_path():
    # Ordered resolution per the Phase 9 plan
    candidates = [
        "rules/2024/language.json",
        "rules/2024/Language.json",
    ]
    # Fallback: any wildcard hit
    wildcard_hits = sorted(glob.glob("rules/2024/*language*.json"))
    candidates.extend([p for p in wildcard_hits if p not in candidates])

    for p in candidates:
        if os.path.exists(p):
            return p
    return None

def main():
    data_path = _resolve_path()
    if not data_path:
        print("ERROR: Could not resolve data path for 'language'. Checked standard and wildcard locations.", flush=True)
        sys.exit(2)

    run_standard_validation(
        category="language",
        data_path=data_path,
        schema_path="schema/2024/v1/rules.language.schema.json",
        array_keys=["language"]  # typical root key for this domain
    )
    print(f"[OK] Phase 9: language validated cleanly ({data_path})")

if __name__ == "__main__":
    main()