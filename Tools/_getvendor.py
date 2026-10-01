import os, sys, zipfile, urllib.request, urllib.error, time, io

UA = {"User-Agent": "Mozilla/5.0 (wb)"}
ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
OUTDIR = os.path.join(ROOT, "Tools", "_vendor_src")

URLS = {
    "common-sources": "https://maven.ryanhcode.dev/releases/dev/ryanhcode/sable-companion/sable-companion-common-1.21.1/1.6.0/sable-companion-common-1.21.1-1.6.0-sources.jar",
    "fabric-sources": "https://maven.ryanhcode.dev/releases/dev/ryanhcode/sable-companion/sable-companion-fabric-1.21.1/1.6.0/sable-companion-fabric-1.21.1-1.6.0-sources.jar",
}

def fetch(url, tries=4, timeout=90):
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(2 + i * 2)
    raise last

os.makedirs(OUTDIR, exist_ok=True)
report = []
for name, url in URLS.items():
    try:
        data = fetch(url)
        zpath = os.path.join(OUTDIR, name + ".jar")
        with open(zpath, "wb") as f:
            f.write(data)
        report.append(f"=== {name}: {len(data)} bytes ===")
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            java = [n for n in z.namelist() if n.endswith(".java")]
            report.append(f"  .java entries: {len(java)}")
            for n in sorted(java):
                report.append("   " + n)
    except Exception as e:
        report.append(f"=== {name}: FAILED {e} ===")

with open(os.path.join(ROOT, "Tools", "_vendor_list.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(report))
print("done")
