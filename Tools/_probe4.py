import re, urllib.request, urllib.error

UA = {"User-Agent": "Mozilla/5.0 (wb-probe)"}

def get(url, timeout=45):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace"), r.read if False else None
    except urllib.error.HTTPError as e:
        return e.code, "", None
    except Exception as e:
        return -1, str(e), None

out = []
def log(s=""):
    out.append(str(s))

BASE = "https://maven.ryanhcode.dev/releases/dev/ryanhcode"

log("=== group dir listing: sable-companion ===")
st, body, _ = get(BASE + "/sable-companion/")
log(f"[{st}]")
if st == 200:
    links = re.findall(r'href="([^"]+)"', body)
    for l in links[:60]:
        log("   " + l)
else:
    log("   (no listing)")

log()
log("=== candidate artifacts ===")
CANDIDATES = [
    "sable-companion/sable-companion-common-1.21.1/maven-metadata.xml",
    "sable-companion/sable-companion-fabric-1.21.1/maven-metadata.xml",
    "sable-companion/sable-companion-common-26.1/maven-metadata.xml",
    "sable-companion/sable-companion-common-26.1.2/maven-metadata.xml",
    "sable-companion/sable-companion-fabric-26.1/maven-metadata.xml",
    "sable-companion/sable-companion-26.1/maven-metadata.xml",
    "sable-companion/maven-metadata.xml",
]
for c in CANDIDATES:
    st, body, _ = get(BASE + "/" + c)
    log(f"[{st}] {c}")
    if st == 200:
        vs = re.findall(r"<version>([^<]+)</version>", body)
        log(f"      versions: {vs}")

log()
log("=== try sources jar for sable-companion-common-1.21.1:1.6.0 ===")
for suffix in ("-sources.jar", ".jar", "-dev.jar"):
    url = f"{BASE}/sable-companion/sable-companion-common-1.21.1/1.6.0/sable-companion-common-1.21.1-1.6.0{suffix}"
    st, body, _ = get(url)
    log(f"[{st}] {url}")

open(r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_probe4.txt", "w", encoding="utf-8").write("\n".join(out))
print("done")
