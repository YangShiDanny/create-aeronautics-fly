import os, re

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
OUT = os.path.join(ROOT, "Tools", "_modelentity.txt")
MODULES = ["sable", "simulated", "offroad", "aeronautics"]

imp = re.compile(r"^\s*import\s+(?:static\s+)?(net\.minecraft\.client\.model\.[\w.]+|net\.minecraft\.world\.entity\.[\w.]+)\s*;", re.M)

rows = {}
for mod in MODULES:
    for dirpath, _d, files in os.walk(os.path.join(ROOT, mod, "src")):
        for fn in files:
            if not fn.endswith(".java"):
                continue
            p = os.path.join(dirpath, fn)
            txt = open(p, encoding="utf-8", errors="replace").read()
            for m in imp.finditer(txt):
                rows.setdefault(m.group(1), []).append(os.path.relpath(p, ROOT))

lines = []
for fq in sorted(rows):
    lines.append(f"{fq}")
    for f in sorted(set(rows[fq])):
        lines.append(f"      {f}")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("done", len(rows))
