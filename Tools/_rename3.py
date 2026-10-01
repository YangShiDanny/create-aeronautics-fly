"""mc26.1 rename: LevelRenderer.getLightColor -> getLightCoords, and the
Particle#getLightColor(float) override -> getLightCoords(float).

Only touches exact code-level patterns:
  * "LevelRenderer.getLightColor("            (static helper call)
  * "getLightColor(final float partialTick)"  (Particle override declaration)
  * @Inject(method = "getLightColor"          (mixin target on Particle)
Comments that merely describe the old name are left alone on purpose.
"""
import io
import os
import sys

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
MODULES = ["sable", "simulated", "offroad", "aeronautics"]

RULES = [
    ("LevelRenderer.getLightColor(", "LevelRenderer.getLightCoords("),
    ("getLightColor(final float partialTick)", "getLightCoords(final float partialTick)"),
    ('@Inject(method = "getLightColor"', '@Inject(method = "getLightCoords"'),
]


def main():
    changed = []
    for mod in MODULES:
        base = os.path.join(ROOT, mod, "src")
        if not os.path.isdir(base):
            continue
        for dirpath, _dirs, files in os.walk(base):
            for fn in files:
                if not fn.endswith(".java"):
                    continue
                path = os.path.join(dirpath, fn)
                with io.open(path, "r", encoding="utf-8") as fh:
                    src = fh.read()
                out = src
                hits = []
                for old, new in RULES:
                    if old in out:
                        hits.append("%d x %s" % (out.count(old), old))
                        out = out.replace(old, new)
                if out != src:
                    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
                        fh.write(out)
                    changed.append((os.path.relpath(path, ROOT), hits))

    if not changed:
        print("no changes")
        return
    for path, hits in changed:
        print(path)
        for h in hits:
            print("    " + h)
    print("\n%d file(s) changed" % len(changed))


if __name__ == "__main__":
    main()
