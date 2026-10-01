import os, re, json

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
LOG = os.path.join(ROOT, "Tools", "_fmj.log")

TARGETS = [
    r"sable\src\main\resources\fabric.mod.json",
    r"simulated\src\main\resources\fabric.mod.json",
    r"offroad\src\main\resources\fabric.mod.json",
    r"aeronautics\src\main\resources\fabric.mod.json",
    r"aeronautics\src\gametest\resources\fabric.mod.json",
]

report = []
ph_re = re.compile(r"\$\{(\w+)\}")

for rel in TARGETS:
    p = os.path.join(ROOT, rel)
    data = json.loads(open(p, encoding="utf-8").read())
    dep = data.setdefault("depends", {})
    changed = []

    if "minecraft" in dep and not str(dep["minecraft"]).startswith("~"):
        dep["minecraft"] = "~" + str(dep["minecraft"])
        changed.append("minecraft -> ~")

    if "team_reborn_energy" in dep:
        dep.pop("team_reborn_energy")
        changed.append("dropped team_reborn_energy")

    if "fabric" in dep:
        dep.pop("fabric")
        changed.append("dropped legacy 'fabric' mod id")

    if "puzzleslib" not in dep:
        dep["puzzleslib"] = "*"
        changed.append("added puzzleslib")

    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    text = open(p, encoding="utf-8").read()
    phs = sorted(set(ph_re.findall(text)))
    report.append(f"{rel}")
    report.append(f"   changes: {', '.join(changed) if changed else 'none'}")
    report.append(f"   placeholders: {', '.join(phs)}")
    report.append(f"   depends: {json.dumps(dep, ensure_ascii=False)}")
    report.append("")

with open(LOG, "w", encoding="utf-8") as f:
    f.write("\n".join(report))
print("done")
