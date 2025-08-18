# scripts/analyse_monsters.py
# -*- coding: utf-8 -*-

import argparse, json, math, statistics
from pathlib import Path
from collections import Counter, defaultdict
from typing import Any, Dict, List, Tuple, Iterable, Optional

# ----- helpers -----

def load_monsters(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    # 5etools format: {"monster":[...]}
    mons = data.get("monster", [])
    # keep only entries that have a name and AC
    return [m for m in mons if isinstance(m, dict) and m.get("name")]

def normalise_resist_list(entry_val: Any) -> Iterable[str]:
    """
    monster.resist is a list of strings and/or dicts with 'resist' arrays.
    We flatten it to a list of lowercased damage type strings (e.g., 'fire','cold').
    """
    out = []
    if not entry_val:
        return out
    if isinstance(entry_val, list):
        for x in entry_val:
            if isinstance(x, str):
                out.append(x.lower())
            elif isinstance(x, dict):
                # standard shape: {"resist": ["fire","bludgeoning"], "note": "..."}
                if "resist" in x and isinstance(x["resist"], list):
                    out.extend([str(t).lower() for t in x["resist"]])
                # sometimes a single type is under "resist" as a string
                elif "resist" in x and isinstance(x["resist"], str):
                    out.append(x["resist"].lower())
                # occasionally nested under "special" notes—skip for now
    elif isinstance(entry_val, str):
        out.append(entry_val.lower())
    return out

def extract_ac(mon: Dict[str, Any]) -> Optional[float]:
    """
    AC can be an int or a list like [{"ac": 15, "from": "natural armour"}].
    Return a simple numeric AC for stats; prefer the first listed.
    """
    ac = mon.get("ac")
    if ac is None:
        return None
    if isinstance(ac, int) or isinstance(ac, float):
        return float(ac)
    if isinstance(ac, list) and ac:
        head = ac[0]
        if isinstance(head, dict) and "ac" in head:
            try:
                return float(head["ac"])
            except Exception:
                return None
        if isinstance(head, (int, float)):
            return float(head)
    return None

def extract_cr(mon: Dict[str, Any]) -> Optional[float]:
    """
    CR can be a number or a string like "1/2".
    """
    cr = mon.get("cr")
    if cr is None:
        return None
    if isinstance(cr, (int, float)):
        return float(cr)
    if isinstance(cr, str):
        s = cr.strip()
        if "/" in s:
            try:
                num, den = s.split("/")
                return float(num) / float(den)
            except Exception:
                return None
        try:
            return float(s)
        except Exception:
            return None
    return None

def extract_saves(mon: Dict[str, Any]) -> Dict[str, int]:
    """
    Returns a dict of save prof bonuses like {"str": 6, "dex": 3, ...}
    Some statblocks store under 'save' mapping, others under 'save' list of dicts—handle common forms.
    """
    sv = mon.get("save")
    out = {}
    if isinstance(sv, dict):
        for k, v in sv.items():
            try:
                out[k.lower()] = int(v)
            except Exception:
                pass
    elif isinstance(sv, list):
        for e in sv:
            if isinstance(e, dict):
                for k, v in e.items():
                    try:
                        out[k.lower()] = int(v)
                    except Exception:
                        pass
    return out

def cr_bucket(value: Optional[float]) -> str:
    if value is None:
        return "unknown"
    if value < 1:
        # keep fractional detail for sub‑1
        return f"{value:g}"
    # bucket integers 1–30 individually
    return f"{int(round(value))}"

# ----- analyses -----

def analyse_resist(monsters: List[Dict[str, Any]], damage_type: Optional[str]) -> None:
    total = len(monsters)
    counter = Counter()
    per_mon = []
    for m in monsters:
        res = set(normalise_resist_list(m.get("resist")))
        per_mon.append((m["name"], sorted(res)))
        counter.update(res)

    if damage_type:
        dt = damage_type.lower()
        have = [name for name, res in per_mon if dt in res]
        print(f"{len(have)}/{total} monsters resist {dt}")
        if len(have) <= 50:
            for n in sorted(have):
                print(f"  - {n}")
    else:
        print("Top resistances (count):")
        for t, c in counter.most_common(20):
            print(f"{t:18} {c}")
        print(f"\nUnique resist types: {len(counter)}   Monsters analysed: {total}")

def analyse_saves(monsters: List[Dict[str, Any]]) -> None:
    """
    Show which save proficiencies (by ability) are most common among monsters,
    plus average save bonus per ability (where present).
    """
    prof_counter = Counter()  # count presence of each save ability
    bonus_accum = defaultdict(list)

    for m in monsters:
        sv = extract_saves(m)
        for ability, bonus in sv.items():
            prof_counter[ability] += 1
            bonus_accum[ability].append(bonus)

    print("Save proficiency prevalence (monsters with a listed save):")
    for ab, c in prof_counter.most_common():
        print(f"{ab.upper():3} : {c}")

    print("\nAverage listed save bonus (mean ± stdev):")
    for ab in sorted(bonus_accum.keys()):
        vals = bonus_accum[ab]
        if vals:
            mu = statistics.mean(vals)
            sd = statistics.pstdev(vals) if len(vals) > 1 else 0.0
            print(f"{ab.upper():3} : {mu:.2f} ± {sd:.2f}  (n={len(vals)})")

def analyse_ac(monsters: List[Dict[str, Any]]) -> None:
    """
    Overall AC stats + AC by CR bucket.
    """
    acs = [a for a in (extract_ac(m) for m in monsters) if a is not None]
    if not acs:
        print("No AC data.")
        return
    mu = statistics.mean(acs); md = statistics.median(acs)
    sd = statistics.pstdev(acs) if len(acs) > 1 else 0.0
    print(f"Overall AC: mean {mu:.2f}, median {md:.1f}, stdev {sd:.2f}, n={len(acs)}")

    buckets = defaultdict(list)
    for m in monsters:
        a = extract_ac(m)
        if a is None: 
            continue
        buckets[cr_bucket(extract_cr(m))].append(a)

    print("\nAverage AC by CR bucket:")
    for b in sorted(buckets, key=lambda x: (x=="unknown", float(x) if x.replace('.','',1).isdigit() else 1e9)):
        vals = buckets[b]
        mu = statistics.mean(vals); md = statistics.median(vals)
        print(f"CR {b:>6}: mean {mu:5.2f}  median {md:5.2f}  n={len(vals)}")

# ----- CLI -----

def main():
    ap = argparse.ArgumentParser(description="Quick analytics over rules/2024/monster.json")
    ap.add_argument("--monsters", default="rules/2024/monster.json", help="Path to monster.json")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_res = sub.add_parser("resist", help="Count/list resistances")
    p_res.add_argument("--type", dest="dtype", default=None, help="Damage type to filter (e.g., fire). If omitted, prints top resistances.")

    sub.add_parser("saves", help="Summarise save proficiencies and bonuses")
    sub.add_parser("ac", help="Average AC overall and by CR")

    args = ap.parse_args()
    monsters = load_monsters(Path(args.monsters))

    if args.cmd == "resist":
        analyse_resist(monsters, args.dtype)
    elif args.cmd == "saves":
        analyse_saves(monsters)
    elif args.cmd == "ac":
        analyse_ac(monsters)

if __name__ == "__main__":
    main()
