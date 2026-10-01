"""Dump public/protected members (with static flag) for arbitrary classes.

Usage:
    python _dumpapi.py <jar-or-dir> <internal/name> [<internal/name> ...]
    python _dumpapi.py --search <jar> <substring>

The MC client jar is parsed with a hand-rolled class-file reader so that no
JDK/javap is required (the port is CI-driven and we must stay off local Gradle).
"""
import io
import os
import re
import struct
import sys
import zipfile

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
MC_JAR = os.path.join(ROOT, "Tools", "_mc", "client-26.1.2.jar")
CACHE = os.path.join(ROOT, "Tools", "_jars")
os.makedirs(CACHE, exist_ok=True)


def read_cp(data, off):
    """Parse the constant pool, returning (pool, new_off)."""
    count = struct.unpack_from(">H", data, off)[0]
    off += 2
    cp = {}
    i = 1
    while i < count:
        tag = data[off]
        off += 1
        if tag == 1:  # Utf8
            ln = struct.unpack_from(">H", data, off)[0]
            off += 2
            cp[i] = data[off:off + ln].decode("utf-8", "replace")
            off += ln
        elif tag in (3, 4):  # Integer, Float
            off += 4
        elif tag in (5, 6):  # Long, Double (take two slots)
            off += 8
            i += 1
        elif tag in (7, 8, 16, 19, 20):  # Class, String, MethodType, Module, Package
            off += 2
        elif tag in (9, 10, 11, 12, 17, 18):  # Fieldref..Dynamic
            off += 4
        elif tag == 15:  # MethodHandle
            off += 3
        else:
            raise ValueError(f"bad constant-pool tag {tag}")
        i += 1
    return cp, off


def parse(data):
    cp, off = read_cp(data, 8)
    access, this_i, super_i = struct.unpack_from(">HHH", data, off)
    off += 6
    ifc = struct.unpack_from(">H", data, off)[0]
    off += 2 + 2 * ifc

    def members(off):
        cnt = struct.unpack_from(">H", data, off)[0]
        off += 2
        out = []
        for _ in range(cnt):
            acc, ni, di, attrs = struct.unpack_from(">HHHH", data, off)
            off += 8
            out.append((cp.get(ni, "?"), cp.get(di, "?"), acc))
            for _ in range(attrs):
                _an, alen = struct.unpack_from(">HI", data, off)
                off += 6 + alen
        return out, off

    fields, off = members(off)
    methods, off = members(off)
    return {
        "access": access,
        "name": cp.get(this_i),
        "super": cp.get(super_i),
        "fields": fields,
        "methods": methods,
    }


def flags(acc):
    out = []
    if acc & 0x0001:
        out.append("public")
    elif acc & 0x0004:
        out.append("protected")
    elif acc & 0x0002:
        out.append("private")
    if acc & 0x0008:
        out.append("static")
    if acc & 0x0010:
        out.append("final")
    if acc & 0x0400:
        out.append("abstract")
    return " ".join(out)


def open_jar(spec):
    if os.path.isfile(spec):
        return zipfile.ZipFile(spec)
    if spec == "mc":
        return zipfile.ZipFile(MC_JAR)
    return None


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return
    if sys.argv[1] == "--search":
        z = open_jar(sys.argv[2])
        pat = sys.argv[3].lower()
        for n in z.namelist():
            if n.endswith(".class") and pat in n.lower():
                print(n[:-6].replace("/", "."))
        return

    z = open_jar(sys.argv[1])
    for internal in sys.argv[2:]:
        entry = internal.replace(".", "/") + ".class"
        try:
            info = parse(z.read(entry))
        except KeyError:
            print(f"!! not found: {internal}")
            continue
        print(f"\n=== {info['name']}  extends {info['super']}  [{flags(info['access'])}]")
        for nm, d, acc in info["fields"]:
            if acc & 0x0007 in (1, 4):  # public/protected
                print(f"    F {flags(acc):24s} {nm} : {d}")
        for nm, d, acc in info["methods"]:
            if acc & 0x0007 in (1, 4):
                print(f"    M {flags(acc):24s} {nm}{d}")


if __name__ == "__main__":
    main()
