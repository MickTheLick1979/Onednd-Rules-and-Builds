import argparse, os, re, json, datetime

DRAFT_URL = "https://json-schema.org/draft/2020-12/schema"

def detect_latest_observed_md(reports_root: str) -> str:
    if not os.path.isdir(reports_root): return ""
    dated = []
    for name in os.listdir(reports_root):
        p = os.path.join(reports_root, name)
        if os.path.isdir(p) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", name):
            md = os.path.join(p, "observed-contract.md")
            if os.path.isfile(md):
                dated.append((name, md))
    if not dated: return ""
    dated.sort(key=lambda x: x[0], reverse=True)
    return dated[0][1]

def map_type(t: str) -> str:
    t = t.strip().lower()
    return {
        "str": "string",
        "int": "integer",
        "float": "number",
        "number": "number",
        "bool": "boolean",
        "list": "array",
        "dict": "object",
        "null": "null",
    }.get(t, "string")

def to_schema_for_types(types_csv: str):
    # types like: "str, int" from observed-contract
    raw = [s.strip() for s in types_csv.split(",") if s.strip()]
    mapped = []
    for r in raw:
        m = map_type(r)
        mapped.append(m)
    mapped = sorted(set(mapped))
    # collapse integer+number to number
    if "integer" in mapped and "number" in mapped:
        mapped = [t for t in mapped if t != "integer"]
    if not mapped:
        return {}
    if len(mapped) == 1:
        return {"type": mapped[0]}
    return {"anyOf": [{"type": t} for t in mapped]}

def parse_observed(md_path: str):
    """
    Returns dict keyed by file path:
    {
      "<path>": {
        "top_type": "array|object|string|number|boolean|null|",
        "entries_table": [ {key, required(bool), types_csv} ... ]
      }
    }
    """
    data = {}
    if not md_path or not os.path.isfile(md_path):
        return data
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    current = None
    in_table = False
    for i, line in enumerate(lines):
        if line.startswith("## "):
            path = line[3:].strip()
            current = {"top_type": "", "rows": []}
            data[path] = current
            in_table = False
            continue

        if current is None:
            continue

        # Top-level type (for non-array files)
        mtop = re.search(r"Top-level type:\s+\*\*(.+?)\*\*", line)
        if mtop:
            current["top_type"] = mtop.group(1).strip().lower()
            continue

        if line.strip().startswith("| key |"):
            in_table = True
            continue
        if in_table:
            if not line.strip().startswith("|"):
                in_table = False
                continue
            # table row
            cells = [c.strip() for c in line.strip().split("|")]
            if len(cells) < 7 or cells[1] == "key":
                continue
            key_cell = cells[1]
            req_cell = cells[2].lower()
            types_cell = cells[3]
            # `name` -> name
            key = key_cell.strip(" `")
            required = (req_cell == "yes")
            current["rows"].append({"key": key, "required": required, "types": types_cell})

    return data

def build_object_schema(rows):
    props = {}
    required = []
    for r in rows:
        k = r["key"]
        t = r["types"]
        sch = to_schema_for_types(t)
        if not sch:
            sch = {}
        props[k] = sch
        if r["required"]:
            required.append(k)
    obj = {
        "type": "object",
        "properties": props,
        "additionalProperties": True,
    }
    if required:
        obj["required"] = sorted(required)
    return obj

def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    return path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reports", default="reports", help="Reports root containing observed-contract.md")
    ap.add_argument("--observed", default="", help="Path to specific observed-contract.md (optional)")
    ap.add_argument("--out", default="schema/2024/v0", help="Output schema dir")
    ap.add_argument("--include", nargs="*", default=[
        "rules/2024/spell.json",
        "indexes/2024/spells_by_class_level.json",
    ], help="Which files to generate schemas for (path as shown in observed-contract)")
    args = ap.parse_args()

    md_path = args.observed or detect_latest_observed_md(args.reports)
    if not md_path:
        raise SystemExit("Could not locate observed-contract.md — run Phase 3 first.")

    observed = parse_observed(md_path)

    date = datetime.date.today().isoformat()
    # 1) spell.json — usually an array of objects with rows present
    for target in args.include:
        # find exact key match in observed (section header uses forward slashes)
        match_key = None
        for k in observed.keys():
            if k.endswith(target.replace("\\", "/")):
                match_key = k
                break
        # fallback: try to find by filename only
        if not match_key:
            for k in observed.keys():
                if k.endswith(os.path.basename(target)):
                    match_key = k
                    break
        rows = observed.get(match_key, {}).get("rows", [])
        top = observed.get(match_key, {}).get("top_type", "")

        # Build soft v0 schema
        schema = {"$schema": DRAFT_URL, "title": f"v0 schema for {target}", "description": "Auto-generated from observed-contract; soft constraints.",}
        if rows:
            schema.update({
                "type": "array",
                "items": build_object_schema(rows),
            })
        else:
            # Non-array (e.g., index maps). Use very permissive top-level type if we have it; else object.
            top_type = {"array","object","string","number","boolean","null"}
            t = (top if top in top_type else "object")
            schema.update({"type": t})
            if t == "object":
                schema.update({"additionalProperties": True})

        out_path = os.path.join(args.out, os.path.basename(target).replace(".json",".schema.json"))
        write_json(out_path, schema)
        print(out_path)

    # 2) Write a tiny README for v0
    readme_path = os.path.join(args.out, "README.md")
    readme = f"""# v0 Schemas (soft)

Generated {date} from the Phase 3 observed contract.

- Intent: **reporting/warn-only**. These schemas are permissive.
- `additionalProperties: true` everywhere.
- A key is **required** only if it appeared in 100% of entries in `observed-contract.md`.
- No strict enums/patterns yet.

> Tightening happens later in v1 (Phase 7/8)."""
    write_json(readme_path, readme)  # write as plain text using same helper
    print(readme_path)

if __name__ == "__main__":
    main()
