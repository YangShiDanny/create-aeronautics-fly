"""Resolve simple class names to fully qualified names using Tools/_all_index.txt.

Usage: python _resolve.py Name1 Name2 ...        (exact simple-name match)
       python _resolve.py --like Substr ...       (substring match)
"""
import sys
import os

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
IDX = os.path.join(ROOT, "Tools", "_all_index.txt")

exact = {}
allnames = []
with open(IDX, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.rstrip("\n").split("\t")
        if len(parts) != 2:
            continue
        simple, cands = parts
        exact[simple] = cands.split(",")
        allnames.append(simple)

like = "--like" in sys.argv
args = [a for a in sys.argv[1:] if a != "--like"]

for a in args:
    if like:
        hits = sorted({c for n in allnames if a.lower() in n.lower() for c in exact[n]})
        print(f"--- ~{a} ({len(hits)})")
        for h in hits[:25]:
            print(f"      {h}")
        if len(hits) > 25:
            print(f"      ... +{len(hits) - 25} more")
    else:
        cands = exact.get(a)
        if not cands:
            print(f"--- {a}:  NOT FOUND (no class with that simple name)")
        else:
            print(f"--- {a} ({len(cands)})")
            for c in cands[:15]:
                print(f"      {c}")
