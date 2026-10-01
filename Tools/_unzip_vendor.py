import os, zipfile

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
SRC = os.path.join(ROOT, "Tools", "_vendor_src", "common-sources.jar")
DST = os.path.join(ROOT, "Tools", "_vendor_src", "common")
os.makedirs(DST, exist_ok=True)
with zipfile.ZipFile(SRC) as z:
    z.extractall(DST)
for dirpath, _d, files in os.walk(DST):
    for fn in sorted(files):
        print(os.path.relpath(os.path.join(dirpath, fn), DST))
