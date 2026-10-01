import json, re, urllib.request, urllib.error, sys

UA = {"User-Agent": "Mozilla/5.0 (wb-probe)"}

def get(url, timeout=45):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return -1, str(e)

out = []
def log(s=""):
    out.append(str(s))

def versions_of(url, filt=None):
    st, body = get(url)
    log(f"[{st}] {url}")
    if st != 200:
        log("    (no body)")
        return []
    vs = re.findall(r"<version>([^<]+)</version>", body)
    if filt:
        vs = [v for v in vs if filt in v]
    log(f"    count={len(vs)} -> {vs[-25:]}")
    return vs

log("=== Puzzles Lib (fabric) ===")
versions_of("https://raw.githubusercontent.com/Fuzss/modresources/main/maven/fuzs/puzzleslib/puzzleslib-fabric/maven-metadata.xml", "26.1")

log("\n=== Forge Config API Port (fabric) ===")
versions_of("https://raw.githubusercontent.com/Fuzss/modresources/main/maven/fuzs/forgeconfigapiport/forgeconfigapiport-fabric/maven-metadata.xml", "26.1")

log("\n=== Fabric Loom (plugin marker) ===")
versions_of("https://maven.fabricmc.net/net/fabricmc/fabric-loom/maven-metadata.xml", "1.18")

log("\n=== Fabric API ===")
versions_of("https://maven.fabricmc.net/net/fabricmc/fabric-api/fabric-api/maven-metadata.xml", "26.1")

log("\n=== Mojang minecraft 26.1.2 pom ===")
st, _ = get("https://libraries.minecraft.net/com/mojang/minecraft/26.1.2/minecraft-26.1.2.pom")
log(f"[{st}] libraries.minecraft.net com.mojang:minecraft:26.1.2 pom")
st, _ = get("https://maven.fabricmc.net/com/mojang/minecraft/26.1.2/minecraft-26.1.2.pom")
log(f"[{st}] maven.fabricmc.net com.mojang:minecraft:26.1.2 pom")

log("\n=== Modrinth: create-fly ===")
st, body = get("https://api.modrinth.com/v2/project/create-fly")
if st == 200:
    p = json.loads(body)
    log(f"project: {p.get('slug')} title={p.get('title')}")
    st2, body2 = get("https://api.modrinth.com/v2/project/create-fly/version")
    if st2 == 200:
        for v in json.loads(body2):
            gv = v.get("game_versions", [])
            log(f"    version_number={v.get('version_number')!r} loaders={v.get('loaders')} games={gv}")
else:
    log(f"[{st}] project create-fly not found")

log("\n=== Modrinth: search create fly ===")
st, body = get("https://api.modrinth.com/v2/search?query=create%20fly&limit=5")
if st == 200:
    for h in json.loads(body).get("hits", []):
        log(f"    slug={h.get('slug')} title={h.get('title')}")

log("\n=== Modrinth: create-aeronautics ===")
for slug in ("create-aeronautics", "aeronautics"):
    st, body = get(f"https://api.modrinth.com/v2/project/{slug}")
    log(f"[{st}] {slug}")

open(r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_probe2.txt", "w", encoding="utf-8").write("\n".join(out))
print("done")
