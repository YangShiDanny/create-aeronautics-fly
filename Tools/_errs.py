"""Parse a javac/Gradle compile log into a triage table.

Usage: python _errs.py [logfile] [--by symbol|file|kind] [--filter SUBSTR]

Pairs each `error:` line with its follow-up `symbol:` / `location:` lines and
prints an aggregated view so the port can be fixed in buckets.
"""
import re
import sys
import collections

LOG = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "Tools/_clog5.txt"

mode = "symbol"
flt = None
for i, a in enumerate(sys.argv):
    if a == "--by" and i + 1 < len(sys.argv):
        mode = sys.argv[i + 1]
    if a == "--filter" and i + 1 < len(sys.argv):
        flt = sys.argv[i + 1]

ERR = re.compile(r"^(?P<path>[^ \t].*?\.java):(?P<line>\d+): error: (?P<msg>.*)$")
SYM = re.compile(r"^  symbol:\s+(?P<kind>\w+)\s+(?P<name>.+?)\s*$")
LOC = re.compile(r"^  location:\s+(?P<loc>.+?)\s*$")

rows = []
with open(LOG, "r", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    m = ERR.match(lines[i])
    if not m:
        i += 1
        continue
    rec = {
        "path": m.group("path").replace("\\", "/"),
        "line": int(m.group("line")),
        "msg": m.group("msg"),
        "sym_kind": "",
        "sym": "",
        "loc": "",
    }
    j = i + 1
    # javac emits up to ~6 indented detail lines for one diagnostic
    while j < len(lines) and lines[j].startswith("  ") and j < i + 10:
        s = SYM.match(lines[j])
        if s:
            rec["sym_kind"] = s.group("kind")
            rec["sym"] = s.group("name")
            # symbol names repeat the kind; keep just the bare name
            rec["sym"] = re.sub(r"^(class|method|variable|constructor)\s+", "", rec["sym"])
        l = LOC.match(lines[j])
        if l:
            rec["loc"] = l.group("loc")
        j += 1
    rows.append(rec)
    i = j

if flt:
    rows = [r for r in rows if flt in r["path"] or flt in r["msg"] or flt in r["sym"]]

print(f"parsed errors: {len(rows)}\n")

def short(p):
    p = re.sub(r"^.*?/src/main/java/", "", p)
    return p

if mode == "symbol":
    agg = collections.Counter()
    for r in rows:
        key = (r["sym_kind"], r["sym"]) if r["sym"] else ("?", r["msg"][:70])
        agg[key] += 1
    for (kind, name), n in agg.most_common():
        print(f"{n:5d}  {kind:11s} {name}")
elif mode == "file":
    agg = collections.Counter(short(r["path"]) for r in rows)
    for name, n in agg.most_common():
        print(f"{n:5d}  {name}")
elif mode == "kind":
    agg = collections.Counter()
    for r in rows:
        m = r["msg"]
        m = re.sub(r"^cannot find symbol.*", "cannot find symbol", m)
        m = re.sub(r"^package .* does not exist$", "package does not exist", m)
        m = re.sub(r"^method .* cannot be applied.*", "method cannot be applied", m)
        m = re.sub(r"^no suitable method.*", "no suitable method", m)
        m = re.sub(r"^incompatible types.*", "incompatible types", m)
        m = re.sub(r"^constructor .* cannot be applied.*", "ctor cannot be applied", m)
        agg[m[:110]] += 1
    for name, n in agg.most_common():
        print(f"{n:5d}  {name}")
elif mode == "detail":
    for r in rows:
        sym = f"{r['sym_kind']} {r['sym']}" if r["sym"] else ""
        print(f"{short(r['path'])}:{r['line']}  |  {r['msg'][:90]}  |  {sym}  |  {r['loc'][:70]}")
