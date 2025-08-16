import argparse, json, re
from pathlib import Path
from collections import defaultdict, Counter

X_SRC = re.compile(r"^X[A-Z0-9]+")
FOCUS = {"class","classFeature","subclass","subclassFeature","feat","spell"}  # build-critical

def load(p: Path):
    try: return json.loads(p.read_text(encoding="utf-8"))
    except Exception: return None

def iter_blocks(data):
    if isinstance(data, dict):
        if "data" in data and isinstance(data["data"], list):
            for block in data["data"]:
                if isinstance(block, dict):
                    for k, v in block.items():
                        if isinstance(v, list): yield k, v
        for k, v in data.items():
            if k == "data": continue
            if isinstance(v, list): yield k, v

def is_2024(e: dict) -> bool:
    if not isinstance(e, dict): return False
    src = str(e.get("source","")).strip()
    return bool(X_SRC.match(src)) or bool(e.get("srd52")) or bool(e.get("basicRules2024"))

def count_src_by_key_and_source(src_root: Path):
    by_key = defaultdict(Counter)
    for p in src_root.rglob("*.json"):
        d = load(p)
        if d is None: continue
        for k, lst in iter_blocks(d):
            if k not in FOCUS or not isinstance(lst, list): continue
            for e in lst:
                if is_2024(e):
                    s = str(e.get("source","")).strip() or "UNKNOWN"
                    by_key[k][s] += 1
    return by_key

def count_out_by_key(out_root: Path):
    out = {}
    for p in out_root.glob("*.json"):
        k = p.stem
        d = load(p)
        if d is None: continue
        if isinstance(d, dict) and k in d and isinstance(d[k], list):
            out[k] = len(d[k])
        elif isinstance(d, list):
            out[k] = len(d)
        else:
            out[k] = next((len(v) for v in d.values() if isinstance(v, list)), 0)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    src = Path(a.src); out = Path(a.out)
    src_by = count_src_by_key_and_source(src)
    out_counts = count_out_by_key(out)

    print("category,source_code,src_count,out_total,delta(out-src)")
    for k in sorted({"class","classFeature","subclass","subclassFeature","feat","spell"}):
        s_total = sum(src_by[k].values())
        o_total = out_counts.get(k, 0)
        delta = o_total - s_total
        if src_by[k]:
            for scode, scount in src_by[k].most_common():
                print(f"{k},{scode},{scount},{o_total},{delta}")
        else:
            print(f"{k},<no 2024 entries found>,0,{o_total},{delta}")

if __name__ == "__main__":
    main()
