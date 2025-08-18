import argparse, json, os, re, datetime, collections, math
from typing import Any, Dict, List, Tuple, Set

# -------- helpers --------

def list_json_files(root: str) -> List[str]:
    out = []
    for dp, _, fns in os.walk(root):
        for f in fns:
            if f.lower().endswith(".json"):
                out.append(os.path.join(dp, f))
    return sorted(out)

def load_json(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return None

def type_name(v: Any) -> str:
    if v is None: return "null"
    if isinstance(v, bool): return "bool"
    if isinstance(v, int): return "int"
    if isinstance(v, float): return "float"
    if isinstance(v, str): return "str"
    if isinstance(v, list): return "list"
    if isinstance(v, dict): return "dict"
    return type(v).__name__

def find_entry_array(obj: Any, filename_hint: str) -> Tuple[List[dict], str]:
    """
    Returns (entries, mode) where mode is 'array', 'largest-list', or '' if none.
    Heuristic: prefer top-level list of dicts; otherwise pick the largest list
    of dicts under any top-level key (common in 5etools-style 'spell': [...]).
    """
    if isinstance(obj, list) and obj and all(isinstance(x, dict) for x in obj):
        return obj, "array"
    if isinstance(obj, dict):
        best = None
        bestk = None
        for k, v in obj.items():
            if isinstance(v, list) and v and all(isinstance(x, dict) for x in v):
                if best is None or len(v) > len(best):
                    best, bestk = v, k
        if best is not None:
            return best, f"largest-list:{bestk}"
    return [], ""

def summarise_entries(entries: List[dict]):
    total = len(entries)
    key_freq = collections.Counter()
    key_types: Dict[str, Set[str]] = collections.defaultdict(set)
    scalar_value_samples: Dict[str, Set[Any]] = collections.defaultdict(set)
    for e in entries:
        if not isinstance(e, dict): continue
        for k, v in e.items():
            key_freq[k] += 1
            tn = type_name(v)
            key_types[k].add(tn)
            # collect scalar candidate enums (strings/ints, not too many)
            if tn in ("str", "int", "float", "bool") and len(scalar_value_samples[k]) < 200:
                scalar_value_samples[k].add(v)
    return total, key_freq, key_types, scalar_value_samples

def md_escape(s: str) -> str:
    return s.replace("|", "\\|")

def coverage_str(seen: int, total: int) -> str:
    pct = 0 if total == 0 else (seen * 100.0 / total)
    return f"{seen}/{total} ({pct:.0f}%)"

def detect_latest_upstream_md(reports_root: str) -> str:
    """Find reports/YYYY-MM-DD/upstream-shapes.md with max date dir."""
    if not os.path.isdir(reports_root): return ""
    candidates = []
    for name in os.listdir(reports_root):
        p = os.path.join(reports_root, name)
        if os.path.isdir(p) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", name):
            md = os.path.join(p, "upstream-shapes.md")
            if os.path.isfile(md):
                candidates.append((name, md))
    if not candidates: return ""
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]

def parse_upstream_shapes(md_path: str) -> Dict[str, Dict[str, Set[str]]]:
    """
    Parses upstream-shapes.md into {category: {key: set(types)}}.
    Expects lines like: '- `name` — str (seen in 391/391)'
    """
    if not md_path or not os.path.isfile(md_path):
        return {}
    txt = ""
    with open(md_path, "r", encoding="utf-8") as f:
        txt = f.read()
    out: Dict[str, Dict[str, Set[str]]] = {}
    current_cat = None
    for line in txt.splitlines():
        if line.startswith("## "):
            current_cat = line[3:].strip().split(" ")[0].strip()
            out.setdefault(current_cat, {})
            continue
        m = re.match(r"^\-\s+`([^`]+)`\s+—\s+([^(\n]+)", line.strip())
        if m and current_cat:
            key = m.group(1).strip()
            types_str = m.group(2).strip()
            types = set([t.strip() for t in types_str.split(",") if t.strip()])
            out[current_cat].setdefault(key, set()).update(types)
    return out

def file_stem_category(path: str) -> str:
    """
    Maps a filename stem to a category token used in upstream report (best effort).
    E.g., rules/2024/spell.json -> 'spell'; feat.json -> 'feat'
    """
    stem = os.path.splitext(os.path.basename(path))[0].lower()
    return stem

# -------- main --------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True, help="Path to rules/2024")
    ap.add_argument("--indexes", default="", help="Path to indexes/2024 (optional)")
    ap.add_argument("--reports", default="reports", help="Reports root")
    ap.add_argument("--upstream", default="", help="Path to reports/*/upstream-shapes.md (optional; auto-detect if omitted)")
    args = ap.parse_args()

    date = datetime.date.today().isoformat()
    outdir = os.path.join(args.reports, date)
    os.makedirs(outdir, exist_ok=True)
    md_path = os.path.join(outdir, "observed-contract.md")

    upstream_md = args.upstream or detect_latest_upstream_md(args.reports)
    upstream = parse_upstream_shapes(upstream_md)

    files = list_json_files(args.baseline)
    # Include indexes optionally (gives a section that at least records types)
    if args.indexes and os.path.isdir(args.indexes):
        files += list_json_files(args.indexes)

    sections = []

    sections.append(f"# Observed Contract ({date})\n")
    sections.append(f"_Baseline root_: `{os.path.abspath(args.baseline)}`\n")
    if upstream_md:
        sections.append(f"_Compared against upstream_: `{os.path.abspath(upstream_md)}`\n")
    sections.append("\n---\n")

    for fp in files:
        obj = load_json(fp)
        if obj is None:
            continue
        cat = file_stem_category(fp)
        entries, mode = find_entry_array(obj, cat)

        sections.append(f"## {fp.replace(os.sep, '/')}\n")
        if entries:
            total, key_freq, key_types, scalar_samples = summarise_entries(entries)
            sections.append(f"Detected entries: **{total}** (mode: {mode})\n\n")
            # table header
            sections.append("| key | required | types | coverage | enum candidates | notes |\n")
            sections.append("|---|---|---|---|---|---|\n")
            for k in sorted(key_freq, key=lambda k: (-key_freq[k], k)):
                req = "yes" if key_freq[k] == total else "no"
                tlist = ", ".join(sorted(key_types[k]))
                cov = coverage_str(key_freq[k], total)
                # enum candidates: <= 20 unique scalar values
                enum_cell = ""
                if scalar_samples.get(k) and len(scalar_samples[k]) <= 20:
                    enum_vals = sorted(list(scalar_samples[k]), key=lambda x: str(x))[:20]
                    enum_cell = ", ".join([str(v) for v in enum_vals])
                sections.append(f"| `{md_escape(k)}` | {req} | {md_escape(tlist)} | {cov} | {md_escape(enum_cell)} |  |\n")
            sections.append("\n")

            # Differences vs upstream (if present)
            cat_for_upstream = cat
            if upstream and upstream.get(cat_for_upstream):
                upstream_keys = set(upstream[cat_for_upstream].keys())
                observed_keys = set(key_freq.keys())
                missing_in_observed = sorted(list(upstream_keys - observed_keys))
                added_in_observed = sorted(list(observed_keys - upstream_keys))
                if missing_in_observed or added_in_observed:
                    sections.append("**Differences vs upstream (keys)**\n\n")
                if missing_in_observed:
                    sections.append(f"- Present upstream, missing here: {', '.join('`'+k+'`' for k in missing_in_observed)}\n")
                if added_in_observed:
                    sections.append(f"- Present here, not seen upstream: {', '.join('`'+k+'`' for k in added_in_observed)}\n")
                sections.append("\n")
        else:
            # Non-entry JSON (likely an index/map); record top-level shape briefly
            t = type_name(obj)
            sections.append(f"Top-level type: **{t}**\n\n")
            if isinstance(obj, dict):
                sample_keys = list(obj.keys())[:30]
                sections.append("Top-level keys (sample): " + ", ".join(f"`{k}`" for k in sample_keys) + "\n\n")
            sections.append("*(No per-entry table generated — file does not look like an array of entries.)*\n\n")
        sections.append("---\n")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sections))

    print(md_path)

if __name__ == "__main__":
    main()
