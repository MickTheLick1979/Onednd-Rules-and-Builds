import argparse, os, json, datetime, sys
from typing import List, Tuple

# Phase 5 requires warn-only behaviour: print issues but ALWAYS exit 0
# Plan refs:
# - scripts/validate_json.py mapping each output file to its schema
# - print OK/warnings/errors; return exit code 0
# - CI runs with continue-on-error and uploads log
# (See schema_implementation_plan.docx, Phase 5)
# -----------------------------------------------

def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def ensure_parent_dir(path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def today_reports_dir(root: str) -> str:
    d = os.path.join(root, datetime.date.today().isoformat())
    os.makedirs(d, exist_ok=True)
    return d

def make_json_path(err) -> str:
    # Compose a readable JSON path from jsonschema error
    try:
        if hasattr(err, "json_path") and isinstance(err.json_path, str):
            return err.json_path
        parts = []
        for p in list(err.path):
            if isinstance(p, int):
                parts.append(f"[{p}]")
            else:
                parts.append(("." if parts else "") + str(p))
        return "".join(parts) if parts else "$"
    except Exception:
        return "$"

def validate_with_schema(instance, schema) -> List[str]:
    # We depend on jsonschema but keep warn-only behaviour even if missing
    try:
        import jsonschema
        from jsonschema import Draft202012Validator
    except Exception as e:
        return [f"INFO: jsonschema not installed; skipping strict validation ({e})."]

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as e:
        return [f"ERROR: invalid schema: {e}"]

    validator = Draft202012Validator(schema)
    problems = []
    for err in validator.iter_errors(instance):
        path = make_json_path(err)
        problems.append(f"ERROR: {path}: {err.message}")
    if not problems:
        problems.append("OK: no validation errors")
    return problems

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", default="rules/2024", help="Rules dir")
    ap.add_argument("--indexes", default="indexes/2024", help="Indexes dir")
    ap.add_argument("--schemas", default="schema/2024/v0", help="Schema dir (v0)")
    ap.add_argument("--reports", default="reports", help="Reports root for logs")
    args = ap.parse_args()

    # Map produced JSON to schema (extend this list as you add schemas)
    targets: List[Tuple[str, str]] = [
        (os.path.join(args.baseline, "spell.json"), os.path.join(args.schemas, "spell.schema.json")),
        (os.path.join(args.indexes, "spells_by_class_level.json"), os.path.join(args.schemas, "spells_by_class_level.schema.json")),
    ]

    out_dir = today_reports_dir(args.reports)
    log_path = os.path.join(out_dir, "validation.log")
    ensure_parent_dir(log_path)

    lines = []
    lines.append("# JSON Schema Validation (warn-only)\n")
    lines.append(f"_Schemas_: `{os.path.abspath(args.schemas)}`")
    lines.append(f"_Data_: rules=`{os.path.abspath(args.baseline)}`, indexes=`{os.path.abspath(args.indexes)}`\n")

    any_errors = False
    for data_path, schema_path in targets:
        header = f"## {data_path.replace(os.sep,'/')}"
        try:
            instance = load_json(data_path)
            schema = load_json(schema_path)
        except Exception as e:
            lines.append(header)
            lines.append(f"ERROR: could not load files: {e}\n")
            any_errors = True
            continue

        res = validate_with_schema(instance, schema)
        lines.append(header)
        for r in res:
            lines.append(r)
            if r.startswith("ERROR"):
                any_errors = True
        lines.append("")

    summary = ("SUMMARY: VALIDATION COMPLETED — issues found" if any_errors
               else "SUMMARY: VALIDATION COMPLETED — no issues")
    lines.append(summary)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # Print path for CI artifact upload and local convenience
    print(log_path)

    # PHASE 5 REQUIREMENT: exit 0 even if errors are present
    sys.exit(0)

if __name__ == "__main__":
    main()
