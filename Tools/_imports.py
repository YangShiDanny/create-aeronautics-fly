import os, re, collections

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
OUT = os.path.join(ROOT, "Tools", "_imports.txt")
MODULES = ["sable", "simulated", "offroad", "aeronautics"]

imp_re = re.compile(r"^\s*import\s+(static\s+)?([\w.$]+)\s*;", re.M)

counter = collections.Counter()
pkg_of = {}

for mod in MODULES:
    base = os.path.join(ROOT, mod, "src")
    for dirpath, _dirs, files in os.walk(base):
        for fn in files:
            if not fn.endswith(".java"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                txt = open(p, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            for m in imp_re.finditer(txt):
                fq = m.group(2)
                if fq.startswith("java.") or fq.startswith("javax."):
                    continue
                parts = fq.split(".")
                # top 3 segments as grouping key
                key = ".".join(parts[:3]) if len(parts) >= 3 else fq
                counter[key] += 1
                pkg_of.setdefault(key, set()).add(mod)

lines = []
for key, n in counter.most_common():
    mods = ",".join(sorted(pkg_of[key]))
    lines.append(f"{n:6d}  {key:60s} [{mods}]")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("done", len(counter))
