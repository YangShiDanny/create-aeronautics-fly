"""Check that every `import net.minecraft...` / `import com.mojang...` /
`import net.fabricmc.fabric...` in a module resolves in the local jars.

Catches classes deleted or moved in the 26.1 port without needing a full
Gradle build (which the user has forbidden locally).

Usage:
    python _importcheck.py [sable simulated offroad aeronautics]
"""
import io
import os
import re
import sys
import zipfile

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
MC_JAR = os.path.join(ROOT, "Tools", "_mc", "client-26.1.2.jar")
FRAPI_JAR = os.path.join(ROOT, "Tools", "_jars", "frapi.jar")

IMPORT_RE = re.compile(r"^\s*import\s+(static\s+)?([A-Za-z0-9_.$]+)\s*;", re.M)

# Packages we can validate locally.
CHECKED = ("net.minecraft.", "com.mojang.", "net.fabricmc.fabric.api.client.renderer.")


def entries(jar):
    with zipfile.ZipFile(jar) as z:
        return {n[:-6].replace("/", ".") for n in z.namelist() if n.endswith(".class")}


def candidates(name):
    """Yield possible binary names for a source-level type name.

    A source name like `a.b.Outer.Inner` is stored as `a.b.Outer$Inner`, and the
    split point is not knowable from the text, so try every suffix combination.
    """
    yield name
    parts = name.split(".")
    for i in range(len(parts) - 1, 0, -1):
        yield ".".join(parts[:i]) + "$" + "$".join(parts[i:])


def run(modules):
    mc = entries(MC_JAR)
    fr = entries(FRAPI_JAR)
    known = mc | fr

    bad = 0
    checked = 0
    for mod in modules:
        src = os.path.join(ROOT, mod, "src")
        if not os.path.isdir(src):
            continue
        for dirpath, _dirs, files in os.walk(src):
            for fn in files:
                if not fn.endswith(".java"):
                    continue
                path = os.path.join(dirpath, fn)
                with io.open(path, "r", encoding="utf-8") as fh:
                    text = fh.read()
                for stat, name in IMPORT_RE.findall(text):
                    if not name.startswith(CHECKED):
                        continue
                    # A static import names a member: strip the last segment.
                    owner = name.rsplit(".", 1)[0] if stat else name
                    if not any(c in known for c in candidates(owner)):
                        bad += 1
                        print("%s  ->  %s%s"
                              % (os.path.relpath(path, ROOT),
                                 "static " if stat else "",
                                 name))
                    checked += 1
    print("\nchecked %d checked-package import(s); %d unresolved" % (checked, bad))


if __name__ == "__main__":
    run(sys.argv[1:] or ["sable", "simulated", "offroad", "aeronautics"])
