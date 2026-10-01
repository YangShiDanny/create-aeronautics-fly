"""Search class files for a UTF-8 constant (field/method name) and report owners.

Usage:
    python _findconst.py <jar> <name> [<name> ...]
"""
import os
import struct
import sys
import zipfile

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
MC_JAR = os.path.join(ROOT, "Tools", "_mc", "client-26.1.2.jar")


def utf8_strings(data):
    """Yield every UTF-8 constant-pool string in a class file."""
    try:
        count = struct.unpack_from(">H", data, 8)[0]
    except struct.error:
        return
    off = 10
    i = 1
    while i < count:
        tag = data[off]
        off += 1
        if tag == 1:
            ln = struct.unpack_from(">H", data, off)[0]
            off += 2
            yield data[off:off + ln].decode("utf-8", "replace")
            off += ln
        elif tag in (3, 4):
            off += 4
        elif tag in (5, 6):
            off += 8
            i += 1
        elif tag in (7, 8, 16, 19, 20):
            off += 2
        elif tag in (9, 10, 11, 12, 17, 18):
            off += 4
        elif tag == 15:
            off += 3
        else:
            return
        i += 1


def main():
    jar = sys.argv[1]
    names = set(sys.argv[2:])
    if jar == "mc":
        jar = MC_JAR
    hits = {n: [] for n in names}
    with zipfile.ZipFile(jar) as z:
        for entry in z.namelist():
            if not entry.endswith(".class") or "$" in entry:
                continue
            try:
                data = z.read(entry)
            except Exception:
                continue
            strs = set(utf8_strings(data))
            for n in names:
                if n in strs:
                    hits[n].append(entry[:-6].replace("/", "."))
    for n in sorted(hits):
        print(f"--- {n}  ({len(hits[n])})")
        for h in hits[n][:40]:
            print("   ", h)


if __name__ == "__main__":
    main()
