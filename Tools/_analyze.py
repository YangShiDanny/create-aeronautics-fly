"""Summarise javac errors from a Gradle compile log: group by (message, symbol)."""
import re, collections, sys, os

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
LOG = os.path.join(ROOT, "Tools", "_rawlog.txt")

lines = open(LOG, encoding="utf-8", errors="replace").read().splitlines()

err_re = re.compile(r"^(?P<file>[^ ]+\.java):(?P<line>\d+): error: (?P<msg>.*)$")

records = []
for i, ln in enumerate(lines):
    m = err_re.match(ln.strip())
    if not m:
        continue
    # javac puts detail on following indented lines
    symbol = location = None
    for j in range(i + 1, min(i + 8, len(lines))):
        s = lines[j].strip()
        if s.startswith("symbol:"):
            symbol = s[len("symbol:"):].strip()
        elif s.startswith("location:"):
            location = s[len("location:"):].strip()
        elif err_re.match(s):
            break
    records.append((m.group("file"), int(m.group("line")), m.group("msg"), symbol, location))

print(f"total error records parsed: {len(records)}")

by_msg = collections.Counter(r[2] for r in records)
print("\n=== by message ===")
for msg, n in by_msg.most_common(40):
    print(f"{n:5d}  {msg}")

# group cannot-find-symbol by the symbol kind+name
sym = collections.Counter()
for f, l, msg, symbol, loc in records:
    if symbol:
        sym[symbol] += 1
print(f"\n=== distinct missing symbols: {len(sym)} ===")
for s, n in sym.most_common(80):
    print(f"{n:5d}  {s}")

print("\n=== samples (cannot find symbol, with location) ===")
seen = set()
for f, l, msg, symbol, loc in records:
    if symbol and (symbol, loc) not in seen:
        seen.add((symbol, loc))
        print(f"{os.path.relpath(f, '').split('create-aeronautics-fly')[-1].lstrip('/\\\\')}:{l}")
        print(f"      {msg} | symbol={symbol} | location={loc}")
    if len(seen) >= 60:
        break

files = collections.Counter(r[0].split("create-aeronautics-fly")[-1].lstrip("/\\") for r in records)
print(f"\n=== files touched: {len(files)} ===")
for f, n in files.most_common(40):
    print(f"{n:5d}  {f}")
