import os, sys, glob
from scripts._validation_common import run_standard_validation

def _resolve_path():
    candidates = [
        "rules/2024/legendaryGroup.json",
        "rules/2024/LegendaryGroup.json",
    ]
    wildcard_hits = sorted(glob.glob("rules/2024/*legendarygroup*.json")) + \
                    sorted(glob.glob("rules/2024/*legendaryGroup*.json"))
    for p in wildcard_hits:
        if p not in candidates:
            candidates.append(p)

    for p in candidates:
        if os.path.exists(p):
            return p
    return None

def main():
    data_path = _resolve_path()
    if not data_path:
        print("ERROR: Could not resolve data path for 'legendaryGroup'. Checked standard and wildcard locations.", flush=True)
        sys.exit(2)

    run_standard_validation(
        category="legendaryGroup",
        data_path=data_path,
        schema_path="schema/2024/v1/rules.legendarygroup.schema.json",
        array_keys=["legendaryGroup"]
    )
    print(f"[OK] Phase 9: legendaryGroup validated cleanly ({data_path})")

if __name__ == "__main__":
    main()