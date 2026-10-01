import urllib.request, urllib.error

OUT = r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_mavenprobe2.txt"

urls = [
    # ryanhcode maven - try browsable listings / group indexes
    "https://maven.ryanhcode.dev/releases/",
    "https://maven.ryanhcode.dev/releases/foundry/veil/",
    "https://maven.ryanhcode.dev/releases/foundry/",
    "https://maven.ryanhcode.dev/releases/dev/ryanhcode/",
    "https://maven.ryanhcode.dev/releases/dev/ryanhcode/sable-companion/",
    "https://maven.ryanhcode.dev/releases/dev/ryanhcode/sable/",
    # veil alternative coords
    "https://maven.ryanhcode.dev/releases/foundry/veil/veil-fabric-26.1.2/maven-metadata.xml",
    "https://maven.ryanhcode.dev/releases/foundry/veil/veil-fabric-26.1/maven-metadata.xml",
    "https://maven.ryanhcode.dev/releases/foundry/veil/veil-common-26.1/maven-metadata.xml",
    "https://maven.ryanhcode.dev/releases/foundry/veil/veil-fabric/maven-metadata.xml",
    # sable companion alt names
    "https://maven.ryanhcode.dev/releases/dev/ryanhcode/sable-companion/sable-companion-common-26.1.2/maven-metadata.xml",
    "https://maven.ryanhcode.dev/releases/dev/ryanhcode/sable-companion/sable-companion-common/maven-metadata.xml",
    # energy
    "https://maven.terraformersmc.com/releases/teamreborn/energy/maven-metadata.xml",
    "https://maven.terraformersmc.com/releases/teamreborn/energy-fabric/maven-metadata.xml",
    "https://jitpack.io/com/github/team-reborn-energy/Energy/maven-metadata.xml",
    # porting lib 26.1?
    "https://mvn.devos.one/snapshots/io/github/fabricators_of_create/Porting-Lib/3.1.0-beta.39+1.21.1/maven-metadata.xml",
]

def probe(url):
    req = urllib.request.Request(url, headers={"User-Agent": "probe/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, body[:1500]
    except urllib.error.HTTPError as e:
        return e.code, "(HTTPError)"
    except Exception as e:
        return "ERR", str(e)[:120]

lines = []
for u in urls:
    st, body = probe(u)
    lines.append(f"[{st}] {u}")
    if st == 200:
        lines.append("      " + body.replace("\n", " ").replace("  ", " ")[:1400])
    else:
        lines.append(f"      {body}")
    lines.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("done")
