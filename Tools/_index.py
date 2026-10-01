"""Build a complete class index from every jar we can reach locally.

Sources:
  Tools/_mc/client-26.1.2.jar            - Minecraft 26.1.2
  ~/.gradle/caches/modules-2/**/*.jar    - fabric-api, create-fly, puzzleslib, ...

Writes Tools/_all_classes.txt with one internal class name per line, plus
Tools/_all_index.txt mapping simple name -> candidate internal names, which is
what we use to resolve 26.1 renames.
"""
import os
import re
import zipfile
import collections

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
TOOLS = os.path.join(ROOT, "Tools")

jars = []
mc = os.path.join(TOOLS, "_mc", "client-26.1.2.jar")
if os.path.exists(mc):
    jars.append(mc)

cache = os.path.join(os.path.expanduser("~"), ".gradle", "caches", "modules-2", "files-2.1")
for dirpath, _dirs, files in os.walk(cache):
    for fn in files:
        if fn.endswith(".jar") and "-sources" not in fn:
            jars.append(os.path.join(dirpath, fn))

names = set()
for j in jars:
    try:
        with zipfile.ZipFile(j) as z:
            for n in z.namelist():
                if n.endswith(".class") and not n.startswith("META-INF"):
                    names.add(n[:-6])
    except Exception as e:
        print(f"  skip {j}: {e}")

print(f"jars scanned: {len(jars)}, classes: {len(names)}")

with open(os.path.join(TOOLS, "_all_classes.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(names)))

by_simple = collections.defaultdict(list)
for n in names:
    simple = n.rsplit("/", 1)[-1].split("$")[0]
    by_simple[simple].append(n)

with open(os.path.join(TOOLS, "_all_index.txt"), "w", encoding="utf-8") as f:
    for simple in sorted(by_simple):
        cands = sorted(by_simple[simple])
        f.write(f"{simple}\t{','.join(cands)}\n")
print("wrote _all_classes.txt / _all_index.txt")
