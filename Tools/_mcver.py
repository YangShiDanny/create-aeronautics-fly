"""Resolve the 26.1.2 client jar URL from Mojang's version manifest."""
import json, urllib.request, urllib.error, os, time

UA = {"User-Agent": "Mozilla/5.0 (wb)"}
ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
OUT = os.path.join(ROOT, "Tools", "_mcver.txt")

def get(url, timeout=60, tries=3):
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(2 + 2 * i)
    raise last

rep = []
try:
    man = json.loads(get("https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"))
    rep.append(f"manifest latest.release={man['latest']['release']} latest.snapshot={man['latest']['snapshot']}")
    rep.append(f"versions listed: {len(man['versions'])}")
    rep.append("newest 12:")
    for v in man["versions"][:12]:
        rep.append(f"   {v['id']:<24} type={v['type']:<9} released={v.get('releaseTime')}")

    target = None
    for v in man["versions"]:
        if v["id"] == "26.1.2":
            target = v
            break
    if target is None:
        rep.append("!! 26.1.2 NOT FOUND in manifest")
        cands = [v["id"] for v in man["versions"] if v["id"].startswith("26.")]
        rep.append(f"   26.x ids: {cands[:40]}")
    else:
        rep.append(f"\n26.1.2 url: {target['url']}")
        vj = json.loads(get(target["url"]))
        rep.append(f"id={vj['id']} type={vj['type']} javaVersion={vj.get('javaVersion')}")
        for k, d in vj.get("downloads", {}).items():
            rep.append(f"  download[{k}] size={d.get('size')} url={d.get('url')}")
except Exception as e:
    rep.append(f"ERROR: {e}")

open(OUT, "w", encoding="utf-8").write("\n".join(rep))
print("\n".join(rep))
