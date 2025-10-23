import json, os
from collections import defaultdict

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SPELLS = os.path.join(REPO, "rules", "2024", "spell.json")
MAP_LEVELS = os.path.join(REPO, "rules", "2024", "mappings", "spell_levels_xphb.json")
MAP_CLASSES = os.path.join(REPO, "rules", "2024", "mappings", "spell_to_classes_xphb.json")
OUT = os.path.join(REPO, "indexes", "2024", "spells_by_class_level.json")

def load(p):
    with open(p, "r", encoding="utf-8-sig") as f: return json.load(f)

def norm_spells(raw):
    return raw["spell"] if isinstance(raw, dict) and "spell" in raw else raw

def main():
    spells = norm_spells(load(SPELLS))
    by_cls_lvl = defaultdict(lambda: defaultdict(set))

    lvl_map = {}
    if os.path.exists(MAP_LEVELS):
        raw = load(MAP_LEVELS)
        lvl_map = {k: ("unknown" if v is None else str(v)) for k, v in raw.items()}

    cls_map = {}
    if os.path.exists(MAP_CLASSES):
        cls_map = load(MAP_CLASSES)

    def classes_from_spell(sp):
        # fallback only; most 2024 spells will not have classes inline
        cls_field = sp.get("classes")
        out = set()
        if isinstance(cls_field, dict):
            for _, v in cls_field.items():
                if isinstance(v, list):
                    for it in v:
                        if isinstance(it, dict) and "name" in it: out.add(str(it["name"]))
                        elif isinstance(it, str): out.add(it)
        elif isinstance(cls_field, list):
            for it in cls_field:
                if isinstance(it, dict) and "name" in it: out.add(str(it["name"]))
                elif isinstance(it, str): out.add(it)
        elif isinstance(cls_field, str):
            out.add(cls_field)
        return sorted(out)

    for sp in spells:
        name = sp.get("name")
        if not name: continue
        lvl_key = lvl_map.get(name, "unknown" if sp.get("level") is None else str(sp.get("level")))
        classes = cls_map.get(name, None)
        if classes is None:
            classes = classes_from_spell(sp)
        for c in classes:
            by_cls_lvl[c][lvl_key].add(name)

    out = {}
    for c in sorted(by_cls_lvl.keys()):
        out[c] = {}
        for lvl in sorted(by_cls_lvl[c].keys(), key=lambda x: (len(x), x)):
            out[c][lvl] = sorted(by_cls_lvl[c][lvl])

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=True, indent=2)
    print("[OK] Rebuilt indexes/2024/spells_by_class_level.json using mappings (with fallback).")

if __name__ == "__main__":
    main()
