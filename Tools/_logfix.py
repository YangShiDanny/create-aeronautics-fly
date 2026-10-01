"""Compile-log driven precise auto-fixer.

javac reports `file:line: error: <msg>` followed by the offending source line and a
caret (`^`) under the offending token. That gives an exact (file, line, column),
which lets us rewrite only the reported occurrences instead of pattern-matching the
whole tree.
"""
import re, os, sys, collections

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
LOG = os.path.join(ROOT, "Tools", "_rawlog.txt")
REPORT = os.path.join(ROOT, "Tools", "_logfix.txt")
APPLY = "--apply" in sys.argv

ERR = re.compile(r"^(?P<file>[^ ]+\.java):(?P<line>\d+): error: (?P<msg>.*)$")

raw = open(LOG, encoding="utf-8", errors="replace").read().splitlines()

entries = []  # (file, line, msg, col, src)
for i, ln in enumerate(raw):
    m = ERR.match(ln.strip())
    if not m:
        continue
    src = None
    col = None
    for j in range(i + 1, min(i + 4, len(raw))):
        s = raw[j]
        if s.strip().startswith("^"):
            col = s.index("^")
            if src is None and j - 1 > i:
                src = raw[j - 1]
            break
        if s.strip() and src is None:
            src = s
    # the source line is the first non-empty line after the error
    if src is None:
        for j in range(i + 1, min(i + 3, len(raw))):
            if raw[j].strip():
                src = raw[j]
                break
    entries.append({"file": m.group("file"), "line": int(m.group("line")),
                    "msg": m.group("msg"), "col": col, "src": src})

print(f"parsed {len(entries)} error entries")

# ------------------------------------------------ rule: ChunkPos record accessors
# 26.1 turned ChunkPos into a record, so the public x/z fields became x()/z().
plan = collections.defaultdict(list)   # file -> list of (line, col, old, new)
skipped = 0

for e in entries:
    m = re.match(r"^(x|z) has private access in ChunkPos$", e["msg"])
    if not m:
        continue
    field = m.group(1)
    col = e["col"]
    src = e["src"]
    if src is None or col is None:
        skipped += 1
        continue
    # javac puts the caret on the '.' of the field-access expression `.x`, so the
    # token we must match starts exactly at the caret column.
    dot = col
    if not (0 <= dot < len(src) and src.startswith(f".{field}", dot)):
        # fall back to the nearest preceding `.x` inside a small window
        dot = src.rfind(f".{field}", max(0, col - 4), col + 4)
    if dot < 0 or not src.startswith(f".{field}", dot):
        skipped += 1
        continue
    end = dot + 1 + len(field)
    if end < len(src) and (src[end].isalnum() or src[end] == "_"):
        skipped += 1
        continue
    plan[e["file"]].append((e["line"], dot, f".{field}", f".{field}()"))

print(f"ChunkPos accessor fixes: {sum(len(v) for v in plan.values())} occurrences "
      f"in {len(plan)} files (skipped {skipped})")

changed = 0
report = []
for f, fixes in sorted(plan.items()):
    path = f
    if not os.path.isabs(path):
        rel = f.split("create-aeronautics-fly/")[-1]
        path = os.path.join(ROOT, rel.replace("/", os.sep))
    lines = open(path, encoding="utf-8").read().split("\n")
    before = list(lines)
    # group by line, apply right-to-left so columns stay valid
    by_line = collections.defaultdict(list)
    for line, col, old, new in fixes:
        by_line[line].append((col, old, new))
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
        report.append(f"{applied:4d}  {os.path.relpath(path, ROOT)}")
        if APPLY:
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write("\n".join(lines))

header = [
    f"mode       : {'APPLIED' if APPLY else 'DRY RUN'}",
    f"files      : {changed}",
    f"occurrences: {sum(len(v) for v in plan.values())}",
    "",
]
open(REPORT, "w", encoding="utf-8").write("\n".join(header + report))
print(f"files changed: {changed}")
print("see", REPORT)
