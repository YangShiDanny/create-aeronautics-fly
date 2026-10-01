import os, re

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
LOG = os.path.join(ROOT, "Tools", "_phcheck.txt")

FABRIC_MODULE_PROPS = {
    "version", "mod_id", "mod_name", "mod_author", "description", "license",
    "java_version", "minecraft_version", "fabric_loader_version", "fabric_version",
    "create_mod_version", "sable_mod_version_range",
}
SABLE_PROPS = {
    "version", "mod_id", "mod_name", "mod_author", "description", "issues", "license",
    "java_version", "minecraft_version", "fabric_loader_version", "fabric_version",
    "sodium_version",
}
GAMETEST_PROPS = {"fabric_loader_version", "minecraft_version"}

ph_re = re.compile(r"\$\{(\w+)\}")

def props_for(rel):
    rel = rel.replace("\\", "/")
    if rel.startswith("sable/"):
        return SABLE_PROPS
    if rel.startswith("aeronautics/src/gametest/"):
        return GAMETEST_PROPS
    return FABRIC_MODULE_PROPS

lines = []
for dirpath, _d, files in os.walk(ROOT):
    if os.sep + "Tools" + os.sep in dirpath or dirpath.endswith(os.sep + "Tools"):
        continue
    if ".git" in dirpath or ".workbuddy" in dirpath or "build" in dirpath.split(os.sep):
        continue
    for fn in files:
        if not (fn.endswith(".mixins.json") or fn == "fabric.mod.json"):
            continue
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p, ROOT)
        txt = open(p, encoding="utf-8", errors="replace").read()
        phs = sorted(set(ph_re.findall(txt)))
        allowed = props_for(rel)
        missing = [x for x in phs if x not in allowed]
        status = "OK" if not missing else "MISSING: " + ", ".join(missing)
        lines.append(f"{status:40s} {rel}  ({', '.join(phs)})")

with open(LOG, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("done")
