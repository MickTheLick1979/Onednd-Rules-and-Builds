#!/usr/bin/env python3
import json, os, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CANDIDATES = [
    os.path.join(REPO, "schema", "2024", "v1", "indexes.spells_by_class_level.schema.json"),
    os.path.join(REPO, "schema", "2024", "v0", "spells_by_class_level.schema.json"),
]

def main():
    found = [p for p in CANDIDATES if os.path.exists(p)]
    if not found:
        print("No spells_by_class_level schema found in expected locations:", *CANDIDATES, sep="\n  ")
        sys.exit(1)

    ok = True
    for p in found:
        try:
            with open(p, "r", encoding="utf-8") as f:
                json.load(f)
            print(f"OK: JSON parsed — {p}")
        except Exception as e:
            ok = False
            print(f"ERROR: {p}: {e}")

    if not ok:
        sys.exit(2)
    print("spells_by_class_level schema validation: PASS")
if __name__ == "__main__":
    main()