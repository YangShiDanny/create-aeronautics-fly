import os, shutil, pathlib

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
SRC  = os.path.join(ROOT, "Tools", "_vendor_src", "common")
DST  = os.path.join(ROOT, "sable", "src", "main", "java", "dev", "ryanhcode", "sable", "companion")

# DefaultSableCompanion is the library's own fallback implementation; sable ships
# ActiveSableCompanion instead, so only the API + math + codec helper are vendored.
FILES = [
    "dev/ryanhcode/sable/companion/SableCompanion.java",
    "dev/ryanhcode/sable/companion/SubLevelAccess.java",
    "dev/ryanhcode/sable/companion/ClientSubLevelAccess.java",
    "dev/ryanhcode/sable/companion/impl/SableCompanionUtil.java",
    "dev/ryanhcode/sable/companion/math/BoundingBox3d.java",
    "dev/ryanhcode/sable/companion/math/BoundingBox3dc.java",
    "dev/ryanhcode/sable/companion/math/BoundingBox3i.java",
    "dev/ryanhcode/sable/companion/math/BoundingBox3ic.java",
    "dev/ryanhcode/sable/companion/math/JOMLConversion.java",
    "dev/ryanhcode/sable/companion/math/Pose3d.java",
    "dev/ryanhcode/sable/companion/math/Pose3dc.java",
]

BANNER = (
    "/*\n"
    " * Vendored from dev.ryanhcode:sable-companion-common-1.21.1:1.6.0 (sources jar),\n"
    " * Maven: https://maven.ryanhcode.dev/releases\n"
    " *\n"
    " * 26.1.2 has no published sable-companion build, so the library is compiled from\n"
    " * source as part of the sable module. See sable/LICENSE-sable-companion.md.\n"
    " * Local changes are marked with `26.1 PORT:`.\n"
    " */\n"
)

copied = []
for rel in FILES:
    src = os.path.join(SRC, rel.replace("/", os.sep))
    dst = os.path.join(DST, rel.replace("dev/ryanhcode/sable/companion/", "").replace("/", os.sep))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    text = pathlib.Path(src).read_text(encoding="utf-8")
    # banner goes above the package declaration
    if text.startswith("package "):
        text = BANNER + text
    pathlib.Path(dst).write_text(text, encoding="utf-8", newline="\n")
    copied.append(os.path.relpath(dst, ROOT))

# upstream license, with a provenance note
lic_src = pathlib.Path(SRC) / "LICENSE"
lic_dst = pathlib.Path(ROOT) / "sable" / "LICENSE-sable-companion.md"
note = (
    "# sable-companion license\n\n"
    "This file covers `sable/src/main/java/dev/ryanhcode/sable/companion/**`, which was\n"
    "vendored from the `sable-companion-common-1.21.1:1.6.0` sources artifact because\n"
    "no 26.1 build of sable-companion is published.\n\n"
    "Upstream: https://maven.ryanhcode.dev/releases/dev/ryanhcode/sable-companion/\n\n"
    "---\n\n"
)
lic_dst.write_text(note + lic_src.read_text(encoding="utf-8", errors="replace"),
                   encoding="utf-8", newline="\n")
copied.append(os.path.relpath(lic_dst, ROOT))

print("\n".join(copied))
print(f"\ntotal {len(copied)} files")
