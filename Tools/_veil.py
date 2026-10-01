import urllib.request, urllib.error

OUT = r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_veil.txt"
urls = [
    "https://maven.ryanhcode.dev/snapshots/",
    "https://maven.ryanhcode.dev/snapshots/foundry/",
    "https://maven.ryanhcode.dev/snapshots/foundry/veil/",
    "https://maven.ryanhcode.dev/snapshots/dev/ryanhcode/",
    "https://mvn.devos.one/snapshots/foundry/veil/",
    "https://maven.blamejared.com/foundry/veil/",
    "https://maven.createmod.net/foundry/veil/",
    "https://maven.ryanhcode.dev/releases/imguimc/",
]

def probe(url):
    req = urllib.request.Request(url, headers={"User-Agent": "probe/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, "(HTTPError)"
    except Exception as e:
        return "ERR", str(e)[:120]

lines = []
for u in urls:
    st, body = probe(u)
    lines.append(f"[{st}] {u}")
    if st == 200:
        txt = body.replace("\n", " ").replace("  ", " ")
        # extract hrefs
        import re
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', body)
        hrefs = [h for h in hrefs if not h.startswith("http") and "static." not in h and "cloudflare" not in h]
        lines.append("      hrefs: " + ", ".join(hrefs[:40]))
    else:
        lines.append(f"      {body}")
    lines.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("done")
