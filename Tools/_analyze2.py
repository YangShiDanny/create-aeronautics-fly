"""Summarise a javac compile log: message counts, missing symbols, files, samples."""
import collections
import os
import re
import sys

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
LOG = os.path.join(ROOT, "Tools", sys.argv[1] if len(sys.argv) > 1 else "_rawlog2.txt")
OUT = os.path.join(ROOT, "Tools", "_analysis2.txt")

raw = open(LOG, encoding="utf-8", errors="replace").read().splitlines()

ERR = re.compile(r"^(?P<file>\S+\.java):(?P<line>\d+): (?P<kind>error|warning): (?P<msg>.*)$")
errs = []
for i, ln in enumerate(raw):
    m = ERR.match(ln.strip())
    if not m or m.group("kind") != "error":
        continue
    ctx = [raw[j] for j in range(i + 1, min(i + 4, len(raw)))]
    errs.append({
        "file": m.group("file"), "line": int(m.group("line")),
        "msg": m.group("msg"), "ctx": ctx,
    })

# a Gradle-level failure that never reached javac
gradle_fail = [l for l in raw if "FAILURE:" in l or "What went wrong" in l or
               "Configuration with name" in l or "Could not" in l]

by_msg = collections.Counter(e["msg"].rstrip(";").strip() for e in errs)
by_file = collections.Counter(e["file"].split("create-aeronautics-fly/")[-1] for e in errs)

# missing symbols: `symbol: class Foo` / `symbol: method bar(...)` / `symbol: variable x`
syms = collections.Counter()
for e in errs:
    for c in e["ctx"]:
        c = c.strip()
        if c.startswith("symbol:"):
            syms[c[len("symbol:"):].strip()] += 1

# packages that do not exist
pkgs = collections.Counter()
for e in errs:
    m = re.match(r"package (.+) does not exist", e["msg"])
    if m:
        pkgs[m.group(1)] += 1

out = []
out.append(f"total error records: {len(errs)}")
out.append(f"files with errors  : {len(by_file)}")
out.append("")
out.append("=== by message ===")
for msg, n in by_msg.most_common(30):
    out.append(f"{n:5d}  {msg}")
out.append("")
out.append("=== missing packages ===")
for p, n in pkgs.most_common(30):
    out.append(f"{n:5d}  {p}")
out.append("")
out.append("=== distinct missing symbols ===")
for s, n in syms.most_common(60):
    out.append(f"{n:5d}  {s}")
out.append("")
out.append("=== files (top 40) ===")
for f, n in by_file.most_common(40):
    out.append(f"{n:5d}  {f}")
out.append("")
out.append("=== samples ===")
seen = set()
shown = 0
for e in errs:
    key = (e["msg"][:60], e["file"].split("/")[-1])
    if key in seen:
        continue
    seen.add(key)
    shown += 1
    if shown > 90:
        break
    out.append(f"{e['file'].split('create-aeronautics-fly/')[-1]}:{e['line']}")
    out.append(f"      {e['msg']}")
    for c in e["ctx"][:3]:
        out.append(f"      | {c.strip()}")

if gradle_fail:
    out.append("")
    out.append("=== gradle-level failure lines ===")
    for l in gradle_fail[:40]:
        out.append("   " + l.rstrip())

open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out[:120]))
print("...")
print("see", OUT)
