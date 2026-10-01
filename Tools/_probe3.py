import re, urllib.request, urllib.error

UA = {"User-Agent": "Mozilla/5.0 (wb-probe)"}

def get(url, timeout=40):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return -1, str(e)

out = []
def log(s=""):
    out.append(str(s))

PROBES = {
    "foojay marker (plugins.gradle.org)":
        "https://plugins.gradle.org/m2/org/gradle/toolchains/foojay-resolver-convention/org.gradle.toolchains.foojay-resolver-convention.gradle.plugin/maven-metadata.xml",
    "foojay impl (plugins.gradle.org)":
        "https://plugins.gradle.org/m2/org/gradle/toolchains/foojay-resolver-convention/foojay-resolver-convention/maven-metadata.xml",
    "fabric-loom plugin marker (fabricmc)":
        "https://maven.fabricmc.net/net/fabricmc/fabric-loom/net.fabricmc.fabric-loom.gradle.plugin/maven-metadata.xml",
}

for name, url in PROBES.items():
    st, body = get(url)
    log(f"=== {name} ===")
    log(f"[{st}] {url}")
    if st == 200:
        vs = re.findall(r"<version>([^<]+)</version>", body)
        log(f"    versions ({len(vs)}): {vs[-20:]}")
        log(f"    latest={re.findall(r'<latest>([^<]+)</latest>', body)}")
    log()

log("=== foojay plugin portal page ===")
st, body = get("https://plugins.gradle.org/plugin/org.gradle.toolchains.foojay-resolver-convention")
log(f"[{st}] plugin page")
if st == 200:
    m = re.findall(r"(\d+\.\d+\.\d+)", body)
    log(f"    numbers seen: {sorted(set(m))[:40]}")

open(r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_probe3.txt", "w", encoding="utf-8").write("\n".join(out))
print("done")
