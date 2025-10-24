#!/usr/bin/env python3
# UTF-8, LF. Validates a single target against schema/2024/v1.
import argparse, json, sys, pathlib
from jsonschema import Draft202012Validator, RefResolver  # jsonschema>=4.21

def load_json(p: pathlib.Path):
    return json.loads(p.read_text(encoding="utf-8-sig"))

def first_existing(base: pathlib.Path, candidates: list[str]) -> pathlib.Path | None:
    for name in candidates:
        p = base / name
        if p.exists():
            return p
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--indexes", required=True)
    ap.add_argument("--schema-root", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    base = pathlib.Path(args.baseline)
    idx = pathlib.Path(args.indexes)
    sch = pathlib.Path(args.schema_root)
    outp = pathlib.Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)

    # Work out data + schema filenames
    if args.target.startswith("index:"):
        name = args.target.split(":", 1)[1]
        data_fp = idx / f"{name}.json"
        # Try plain and the "indexes." prefix
        schema_fp = first_existing(sch, [
            f"{name}.schema.json",
            f"indexes.{name}.schema.json",
        ])
    else:
        name = args.target
        data_fp = base / f"{name}.json"
        # Try plain and the "rules." prefix
        schema_fp = first_existing(sch, [
            f"{name}.schema.json",
            f"rules.{name}.schema.json",
        ])

    meta = {"schema_used": None, "data_file": str(data_fp)}
    findings = {args.target: []}
    rc = 0

    if not data_fp.exists():
        findings[args.target].append(f"Missing data file: {data_fp}")
        rc = 2
    if schema_fp is None:
        tried = [f"{name}.schema.json", (f'indexes.{name}.schema.json' if args.target.startswith('index:') else f'rules.{name}.schema.json')]
        findings[args.target].append(f"Missing schema file for '{name}'. Tried: {', '.join(tried)}")
        rc = 2
    else:
        meta["schema_used"] = str(schema_fp)

    if rc == 0:
        data = load_json(data_fp)
schema = load_json(schema_fp)
# If data is wrapped like {"language": [...]}, unwrap it for validation
try:
    if isinstance(data, dict) and name in data:
        data = data[name]
        # note in meta
        if isinstance(meta, dict):
            meta["unwrapped_key"] = name
except Exception:
    pass
        # Use absolute base for resolving $ref
        resolver = RefResolver(base_uri=schema_fp.resolve().parent.as_uri() + "/", referrer=schema)
        validator = Draft202012Validator(schema, resolver=resolver)
        errors = sorted(validator.iter_errors(data), key=lambda e: (list(e.path), e.message))
        if errors:
            rc = 1
            for e in errors:
                loc = "/".join(str(x) for x in e.path) or "(root)"
                findings[args.target].append(f"{e.message} @ {loc}")

    report = {"meta": meta, **findings}
    outp.write_text(json.dumps(report, indent=2), encoding="utf-8")
    if findings[args.target]:
        print(f"[{args.target}] {len(findings[args.target])} issue(s) found.")
    else:
        print(f"[{args.target}] OK")
    sys.exit(rc)

if __name__ == "__main__":
    main()