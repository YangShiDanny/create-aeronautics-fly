import json, urllib.request, urllib.parse, sys

OUT = r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_depcheck.txt"

slugs = [
    "jei", "sodium", "cc-tweaked", "natures-compass", "explorers-compass",
    "scalablelux", "veil", "sable", "sable-companion", "entityculling",
    "iris", "create-fly", "forge-config-api-port", "puzzles-lib",
    "architectury-api", "cloth-config", "create",
]

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "dep-check/1.0"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.load(r)

lines = []
for slug in slugs:
    try:
        q = urllib.parse.urlencode({"game_versions": '["26.1.2"]'})
        data = get(f"https://api.modrinth.com/v2/project/{slug}/version?{q}")
        if not data:
            lines.append(f"{slug:26s} -> (no 26.1.2 versions)")
            continue
        for v in data[:3]:
            loaders = ",".join(v.get("loaders", []))
            lines.append(f"{slug:26s} -> {v['version_number']:32s} [{loaders}]")
    except Exception as e:
        lines.append(f"{slug:26s} -> ERROR {e}")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("done")
