import json, os, sys
from collections import defaultdict

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(REPO, "rules", "2024", "spell.json")
IX   = os.path.join(REPO, "indexes", "2024", "spells_by_class_level.json")

def load_json(p):
    with open(p, "r", encoding="utf-8-sig") as f: return json.load(f)

def norm_spells(raw):
    return raw["spell"] if isinstance(raw, dict) and "spell" in raw else raw

def derive_index(spells):
    by = defaultdict(lambda: defaultdict(set))
    for sp in spells:
        name = sp.get("name")
        if not name: continue
        lvl  = sp.get("level")
        lvl_key = "unknown" if lvl is None else str(lvl)
        cls_field = sp.get("classes")
        classes = set()

        if isinstance(cls_field, dict):
            for k, v in cls_field.items():
                if isinstance(v, list):
                    for it in v:
                        if isinstance(it, dict) and "name" in it: classes.add(str(it["name"]))
                        elif isinstance(it, str): classes.add(it)
        elif isinstance(cls_field, list):
            for it in cls_field:
                if isinstance(it, dict) and "name" in it: classes.add(str(it["name"]))
                elif isinstance(it, str): classes.add(it)
        elif isinstance(cls_field, str):
            classes.add(cls_field)

        for c in classes:
            by[c][lvl_key].add(name)

    out = {}
    for c in sorted(by.keys()):
        out[c] = {}
        for lvl in sorted(by[c].keys(), key=lambda x: (len(x), x)):
            out[c][lvl] = sorted(by[c][lvl])
    return out

def compare(a, b):
    problems = 0
    a_classes = set(a.keys()); b_classes = set(b.keys())
    missing_classes = a_classes - b_classes
    extra_classes   = b_classes - a_classes

    if missing_classes:
        print("[DIFF] Classes missing in existing index:", sorted(missing_classes)); problems += 1
    if extra_classes:
        print("[DIFF] Extra classes in existing index:", sorted(extra_classes)); problems += 1

    shared = sorted(a_classes & b_classes)
    for c in shared:
        a_lvls = set(a[c].keys()); b_lvls = set(b[c].keys())
        miss_lv = a_lvls - b_lvls
        extra_lv = b_lvls - a_lvls
        if miss_lv:
            print(f"[DIFF] {c}: levels missing in existing index: {sorted(miss_lv)}"); problems += 1
        if extra_lv:
            print(f"[DIFF] {c}: extra levels in existing index: {sorted(extra_lv)}"); problems += 1
        for lv in sorted(a_lvls & b_lvls, key=lambda x:(len(x),x)):
            a_set, b_set = set(a[c][lv]), set(b[c][lv])
            only_in_a = sorted(a_set - b_set)
            only_in_b = sorted(b_set - a_set)
            if only_in_a or only_in_b:
                problems += 1
                print(f"[DIFF] {c} level {lv}:")
                if only_in_a:
                    print("  -> Missing in existing index:", only_in_a[:20], ("...(+%d)" % (len(only_in_a)-20) if len(only_in_a)>20 else ""))
                if only_in_b:
                    print("  -> Extra in existing index:",   only_in_b[:20], ("...(+%d)" % (len(only_in_b)-20) if len(only_in_b)>20 else ""))
    return problems

def main():
    try:
        spells = norm_spells(load_json(DATA))
    except Exception as e:
        print(f"[ERROR] Failed to load DATA: {DATA} -> {e}")
        return 2
    try:
        existing = load_json(IX)
    except Exception as e:
        print(f"[ERROR] Failed to load INDEX: {IX} -> {e}")
        return 2

    derived = derive_index(spells)
    problems = compare(derived, existing)
    if problems:
        print(f"[FAIL] Index mismatches detected: {problems} issue group(s).")
        return 1
    print("[OK] Existing index matches derived view from spell.json.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
