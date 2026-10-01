import os, re, json, io

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
MODULES = ["sable", "simulated", "offroad", "aeronautics"]
LOG = os.path.join(ROOT, "Tools", "_resources.log")

report = []

def find_files():
    mixins, aw, fmj = [], [], []
    for mod in MODULES:
        base = os.path.join(ROOT, mod, "src")
        for dirpath, _d, files in os.walk(base):
            for fn in files:
                p = os.path.join(dirpath, fn)
                rel = os.path.relpath(p, ROOT)
                if fn.endswith(".mixins.json"):
                    mixins.append(p)
                elif fn.endswith(".accesswidener"):
                    aw.append(p)
                elif fn == "fabric.mod.json":
                    fmj.append(p)
    return mixins, aw, fmj

mixins, aw, fmj = find_files()

# --- 1. mixins.json ------------------------------------------------------
for p in mixins:
    rel = os.path.relpath(p, ROOT)
    raw = open(p, encoding="utf-8").read()
    data = json.loads(raw)
    changed = []
    if "refmap" in data:
        data.pop("refmap")
        changed.append("dropped refmap")
    cl = data.get("compatibilityLevel")
    if cl != "JAVA_25":
        data["compatibilityLevel"] = "JAVA_25"
        changed.append(f"compat {cl} -> JAVA_25")
    ow = data.get("overwrites")
    if not isinstance(ow, dict) or ow.get("requireAnnotations") is not True:
        data["overwrites"] = {"requireAnnotations": True}
        changed.append("added overwrites.requireAnnotations")
    if changed:
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.write("\n")
    report.append(f"[mixins] {rel}: {', '.join(changed) if changed else 'no change'}")

# --- 2. accesswidener ----------------------------------------------------
aw_re = re.compile(r"^(\s*accessWidener\s+v\d+\s+)(\w+)", re.M)
for p in aw:
    rel = os.path.relpath(p, ROOT)
    raw = open(p, encoding="utf-8").read()
    m = aw_re.search(raw)
    if not m:
        report.append(f"[aw] {rel}: no header match")
        continue
    if m.group(2) == "official":
        report.append(f"[aw] {rel}: already official")
        continue
    new = aw_re.sub(lambda mm: mm.group(1) + "official", raw, count=1)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(new)
    report.append(f"[aw] {rel}: {m.group(2)} -> official")

# --- 3. report fabric.mod.json -------------------------------------------
for p in fmj:
    rel = os.path.relpath(p, ROOT)
    try:
        data = json.loads(open(p, encoding="utf-8").read())
    except Exception as e:
        report.append(f"[fmj] {rel}: PARSE ERROR {e}")
        continue
    report.append(f"[fmj] {rel}")
    report.append(f"        depends = {json.dumps(data.get('depends'), ensure_ascii=False)}")
    if "jars" in data:
        report.append(f"        jars = {json.dumps(data.get('jars'), ensure_ascii=False)[:400]}")
    if "accessWidener" in data:
        report.append(f"        accessWidener = {data.get('accessWidener')}")

with open(LOG, "w", encoding="utf-8") as f:
    f.write("\n".join(report))
print("done")
