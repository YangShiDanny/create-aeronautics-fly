import os, re, collections

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
OUT = os.path.join(ROOT, "Tools", "_imports_detail.txt")
MODULES = ["sable", "simulated", "offroad", "aeronautics"]

PREFIXES = [
    "team.reborn",
    "io.github.fabricators_of_create",
    "foundry.veil",
    "ca.spottedleaf",
    "net.caffeinemc",
    "net.neoforged",
    "dan200.computercraft",
    "mezz.jei",
    "net.irisshaders",
    "com.github.exopandora",
    "toni.sodiumextras",
    "fuzs.forgeconfigapiport",
    "net.fabricmc",
    "com.tterrag.registrate",
    "net.minecraft.gizmos",
    "net.minecraft.BlockUtil",
    "net.minecraft.FileUtil",
    "net.minecraft.Util",
]

imp_re = re.compile(r"^\s*import\s+(static\s+)?([\w.$]+)\s*;", re.M)
buckets = collections.defaultdict(collections.Counter)
where = collections.defaultdict(set)

for mod in MODULES:
    base = os.path.join(ROOT, mod, "src")
    for dirpath, _dirs, files in os.walk(base):
        for fn in files:
            if not fn.endswith(".java"):
                continue
            p = os.path.join(dirpath, fn)
            txt = open(p, encoding="utf-8", errors="replace").read()
            for m in imp_re.finditer(txt):
                fq = m.group(2)
                for pre in PREFIXES:
                    if fq.startswith(pre):
                        buckets[pre][fq] += 1
                        where[(pre, fq)].add(mod + "/" + os.path.relpath(p, os.path.join(ROOT, mod, "src")))
                        break

lines = []
for pre in PREFIXES:
    lines.append(f"##### {pre}  ({sum(buckets[pre].values())} imports)")
    for fq, n in buckets[pre].most_common():
        mods = ",".join(sorted(where[(pre, fq)]))
        lines.append(f"   {n:4d}  {fq}")
    lines.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("done")
