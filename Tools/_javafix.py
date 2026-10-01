"""Caret-driven javac auto-fixer for the 26.1 ChunkPos record migration.

javac emits `file:line: error: <msg>`, then the offending source line, then a
caret line. The caret column gives an exact byte offset, so each edit touches
only the reported occurrence instead of pattern-matching the whole tree.

Handled rules (all ChunkPos-specific, decided by the diagnostic text + context):

  1. `x|z has private access in ChunkPos`  ->  `.x` / `.z`   -> `.x()` / `.z()`
  2. `cannot find symbol` + `symbol: method toLong()` +
     `location: variable ... of type ChunkPos`  ->  `toLong` -> `pack`
  3. `cannot find symbol` + `symbol: method asLong(int,int)` +
     `location: class ChunkPos`  ->  `asLong` -> `pack`
  4. `constructor ChunkPos in record ChunkPos cannot be applied` +
     `required: int,int`  ->  `new ChunkPos(` -> `ChunkPos.containing(`

Usage: python _javafix.py <logfile> [--apply]
"""
import collections
import os
import re
import sys

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
LOG = os.path.join(ROOT, "Tools", sys.argv[1] if len(sys.argv) > 1 else "_rawlog2.txt")
REPORT = os.path.join(ROOT, "Tools", "_javafix.txt")
APPLY = "--apply" in sys.argv

ERR = re.compile(r"^(?P<file>\S+\.java):(?P<line>\d+): error: (?P<msg>.*)$")

raw = open(LOG, encoding="utf-8", errors="replace").read().splitlines()

records = []
i = 0
while i < len(raw):
    m = ERR.match(raw[i].strip())
    if not m:
        i += 1
        continue
    src = None
    col = None
    ctx = []
    j = i + 1
    # javac prints: source line, caret line, then symbol:/location:/required:.
    # Keep scanning past the caret so the context lines are captured too.
    while j < len(raw) and j < i + 14:
        s = raw[j]
        if ERR.match(s.strip()):
            break
        st = s.strip()
        if st.startswith("^"):
            col = s.index("^")
        elif st and src is None and not st.startswith(("symbol:", "location:",
                                                       "required:", "found:")):
            src = s
        if st.startswith(("symbol:", "location:", "required:", "found:")):
            ctx.append(st)
        j += 1
    records.append({
        "file": m.group("file"), "line": int(m.group("line")),
        "msg": m.group("msg"), "src": src, "col": col, "ctx": ctx,
    })
    i = j

# file -> line -> list of (col, old, new)
plan = collections.defaultdict(lambda: collections.defaultdict(list))
skipped = collections.Counter()


def rel_path(f):
    rel = f.split("create-aeronautics-fly/")[-1]
    return os.path.join(ROOT, rel.replace("/", os.sep))


def add(rec, col, old, new, end_guard=False):
    src = rec["src"]
    if src is None or col is None or col < 0:
        skipped[old] += 1
        return
    # javac puts the caret on the '.' of a member access (`.x`, `.toLong()`), so
    # accept either the bare token or the dotted form at the caret column.
    if not src.startswith(old, col) and src.startswith("." + old, col):
        col += 1
    if not src.startswith(old, col):
        skipped[old] += 1
        return
    if end_guard:
        e = col + len(old)
        if e < len(src) and (src[e].isalnum() or src[e] == "_"):
            skipped[old] += 1
            return
    plan[rec["file"]][rec["line"]].append((col, old, new))


for rec in records:
    msg = rec["msg"]
    ctx = " ".join(rec["ctx"])

    m = re.match(r"^(x|z) has private access in ChunkPos$", msg)
    if m:
        field = m.group(1)
        add(rec, rec["col"], f".{field}", f".{field}()", end_guard=True)
        continue

    if msg == "cannot find symbol" and "method toLong()" in ctx and "ChunkPos" in ctx:
        add(rec, rec["col"], "toLong", "pack", end_guard=True)
        continue

    if msg == "cannot find symbol" and "method asLong(int,int)" in ctx and "ChunkPos" in ctx:
        add(rec, rec["col"], "asLong", "pack", end_guard=True)
        continue

    if msg == "cannot find symbol" and "method location()" in ctx and "ResourceKey" in ctx:
        add(rec, rec["col"], "location", "identifier", end_guard=True)
        continue

    if msg.startswith("incompatible types: long cannot be converted to BlockPos"):
        # A packed chunk long was fed to `ChunkPos.containing(BlockPos)`; the
        # correct 26.1 entry point for the packed form is `ChunkPos.unpack(long)`.
        # The caret sits on the argument, so walk back to the enclosing call.
        src, col = rec["src"], rec["col"]
        if src is None or col is None:
            skipped["ChunkPos.unpack"] += 1
            continue
        k = src.rfind("ChunkPos.containing(", 0, col)
        if k == -1:
            skipped["ChunkPos.unpack"] += 1
            continue
        off = k + len("ChunkPos.")
        plan[rec["file"]][rec["line"]].append((off, "containing(", "unpack("))
        continue

    if msg.startswith("constructor ChunkPos in record ChunkPos") and "required: int,int" in ctx:
        # The caret may sit on `new`; snap forward to the `new ChunkPos(` token.
        src, col = rec["src"], rec["col"]
        if src is None or col is None:
            skipped["new ChunkPos"] += 1
            continue
        idx = src.find("new ChunkPos(", max(0, col - 2))
        if idx == -1:
            idx = src.find("new ChunkPos(")
        if idx == -1:
            skipped["new ChunkPos"] += 1
            continue
        plan[rec["file"]][rec["line"]].append((idx, "new ChunkPos(", "ChunkPos.containing("))
        continue

total = sum(len(v) for d in plan.values() for v in d.values())
print(f"records: {len(records)}   planned edits: {total}   files: {len(plan)}")
for k, v in skipped.items():
    print(f"   skipped {v:4d}x {k}")

report = []
changed = 0
for f, by_line in sorted(plan.items()):
    path = rel_path(f)
    if not os.path.exists(path):
        report.append(f"MISSING {path}")
        continue
    lines = open(path, encoding="utf-8").read().split("\n")
    before = list(lines)
    applied = 0
    for line, items in by_line.items():
        idx = line - 1
        if not (0 <= idx < len(lines)):
            continue
        for col, old, new in sorted(items, key=lambda t: -t[0]):
            s = lines[idx]
            if s.startswith(old, col) and not s.startswith(new, col):
                lines[idx] = s[:col] + new + s[col + len(old):]
                applied += 1
    if lines != before:
        changed += 1
        report.append(f"{applied:5d}  {os.path.relpath(path, ROOT)}")
        if APPLY:
            open(path, "w", encoding="utf-8", newline="\n").write("\n".join(lines))

header = [
    f"mode       : {'APPLIED' if APPLY else 'DRY RUN'}",
    f"files      : {changed}",
    f"edits      : {total}",
    "",
]
open(REPORT, "w", encoding="utf-8").write("\n".join(header + report))
print("\n".join(header))
print("see", REPORT)
