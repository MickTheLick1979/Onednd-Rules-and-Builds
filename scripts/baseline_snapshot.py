import hashlib, json, os, pathlib, datetime

root = pathlib.Path(__file__).resolve().parent.parent
today = datetime.date.today().isoformat()
report_dir = root / "reports" / today
report_dir.mkdir(parents=True, exist_ok=True)

data = {}

for folder in ["rules/2024", "indexes/2024"]:
    for path in (root / folder).rglob("*.json"):
        h = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
        rel = path.relative_to(root).as_posix()
        data[rel] = {"size": path.stat().st_size, "hash": h}

out_path = report_dir / "baseline_snapshot.json"
out_path.write_text(json.dumps(data, indent=2))
print(f"Snapshot saved to {out_path}")
