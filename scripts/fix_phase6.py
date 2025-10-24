import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
RULES = ROOT / "rules" / "2024"
INDEXES = ROOT / "indexes" / "2024"

# Gentle, non-controversial normalisations only
CLASS_FIX = {
    "Sorceror": "Sorcerer",
    "Wizzard": "Wizard",
    "Warlock ": "Warlock",
}
SOURCE_FIX = {
    "PHB 2024": "XPHB",
    "DMG 2024": "XDMG",
    "MM 2024":  "XMM",
}

STRIP_KEYS  = {"name","source","school"}     # trim whitespace
TITLE_KEYS  = {"school"}                     # Title Case if string

def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(p, data):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def norm_class(name: str) -> str:
    n = CLASS_FIX.get(name.strip(), name.strip())
    return n[:1].upper() + n[1:].lower() if n else n

def fix_spell(sp: dict) -> dict:
    # Trim
    for k in STRIP_KEYS:
        if k in sp and isinstance(sp[k], str):
            sp[k] = sp[k].strip()
    # Title-case school
    for k in TITLE_KEYS:
        if k in sp and isinstance(sp[k], str):
            sp[k] = sp[k].title()
    # Source tokens
    if "source" in sp and isinstance(sp["source"], str):
        sp["source"] = SOURCE_FIX.get(sp["source"].strip(), sp["source"].strip())
    # Classes tidy
    if "classes" in sp and isinstance(sp["classes"], list):
        out = []
        for c in sp["classes"]:
            if isinstance(c, str):
                out.append(norm_class(c))
            else:
                out.append(c)
        sp["classes"] = sorted(set(out))
    return sp

def fix_spell_file(path: pathlib.Path):
    data = load_json(path)
    if isinstance(data, list):
        for i, sp in enumerate(data):
            if isinstance(sp, dict):
                data[i] = fix_spell(sp)
    save_json(path, data)

def fix_spells_index(path: pathlib.Path):
    data = load_json(path)
    fixed = {}
    for cls, lvlmap in data.items():
        cls_norm = norm_class(cls)
        new_lvlmap = {}
        for lvl, spells in lvlmap.items():
            lvl_key = str(int(lvl)) if str(lvl).isdigit() else lvl
            if isinstance(spells, list):
                spells = sorted({s.strip() if isinstance(s, str) else s for s in spells})
            new_lvlmap[lvl_key] = spells
        fixed[cls_norm] = new_lvlmap
    save_json(path, fixed)

def main():
    spells = RULES / "spell.json"
    s_index = INDEXES / "spells_by_class_level.json"

    targets = []
    if spells.exists(): targets.append(spells)
    if s_index.exists(): targets.append(s_index)

    if "--dry-run" in sys.argv:
        print("Would fix:")
        for t in targets: print(" -", t)
        return

    print("Fixing:")
    for t in targets:
        print(" -", t)
        if t.name == "spell.json":
            fix_spell_file(t)
        elif t.name == "spells_by_class_level.json":
            fix_spells_index(t)

if __name__ == "__main__":
    main()
