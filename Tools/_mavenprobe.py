import urllib.request, urllib.error

OUT = r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_mavenprobe.txt"

urls = [
    # Fuzs modresources maven - Puzzles Lib
    "https://raw.githubusercontent.com/Fuzss/modresources/main/maven/fuzs/puzzleslib/puzzleslib-fabric/maven-metadata.xml",
    "https://raw.githubusercontent.com/Fuzss/modresources/main/maven/fuzs/puzzleslib/puzzleslib-fabric-26.1/maven-metadata.xml",
    "https://raw.githubusercontent.com/Fuzss/modresources/main/maven/fuzs/puzzleslib/puzzleslib-common/maven-metadata.xml",
    # ryanhcode maven - veil
    "https://maven.ryanhcode.dev/releases/foundry/veil/veil-fabric-26.1/maven-metadata.xml",
    "https://maven.ryanhcode.dev/releases/foundry/veil/veil-fabric-1.21.1/maven-metadata.xml",
    "https://maven.ryanhcode.dev/releases/dev/ryanhcode/veil/veil-fabric-26.1/maven-metadata.xml",
    # ryanhcode maven - sable companion
    "https://maven.ryanhcode.dev/releases/dev/ryanhcode/sable-companion/sable-companion-common-26.1/maven-metadata.xml",
    "https://maven.ryanhcode.dev/releases/dev/ryanhcode/sable-companion/sable-companion-common-1.21.1/maven-metadata.xml",
    # energy
    "https://maven.shedaniel.me/teamreborn/energy/maven-metadata.xml",
    "https://mvn.devos.one/snapshots/teamreborn/energy/maven-metadata.xml",
    # porting lib
    "https://mvn.devos.one/snapshots/io/github/fabricators_of_create/Porting-Lib/maven-metadata.xml",
    # zurrtum
    "https://oss.zurrtum.com/dev/zurrtum/create-fly/maven-metadata.xml",
]

def probe(url):
    req = urllib.request.Request(url, headers={"User-Agent": "probe/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, body[:600]
    except urllib.error.HTTPError as e:
        return e.code, "(HTTPError)"
    except Exception as e:
        return "ERR", str(e)[:200]

lines = []
for u in urls:
    st, body = probe(u)
    lines.append(f"[{st}] {u}")
    if st == 200:
        txt = body.replace("\n", " ")
        lines.append(f"      {txt[:520]}")
    else:
        lines.append(f"      {body}")
    lines.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("done")
