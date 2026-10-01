"""Resolve the class hierarchy (superclass + interfaces) of MC classes.

Usage: python _hier.py <internal/name> [<internal/name> ...]
"""
import struct
import sys

import _dumpapi as D


def parse_hdr(data):
    """Return (pool, access, this, super, interfaces)."""
    count = struct.unpack_from(">H", data, 8)[0]
    off = 10
    i = 1
    pool = {}
    while i < count:
        tag = data[off]
        off += 1
        if tag == 1:
            ln = struct.unpack_from(">H", data, off)[0]
            off += 2
            pool[i] = data[off:off + ln].decode("utf-8", "replace")
            off += ln
        elif tag in (3, 4):
            off += 4
        elif tag in (5, 6):
            off += 8
            i += 1
        elif tag == 7:
            pool[i] = ("class", struct.unpack_from(">H", data, off)[0])
            off += 2
        elif tag == 8:
            pool[i] = ("string", struct.unpack_from(">H", data, off)[0])
            off += 2
        elif tag in (16, 19, 20):
            off += 2
        elif tag in (9, 10, 11, 12, 17, 18):
            off += 4
        elif tag == 15:
            off += 3
        else:
            raise ValueError(f"tag {tag}")
        i += 1

    access, this_i, super_i = struct.unpack_from(">HHH", data, off)
    off += 6
    ifc = struct.unpack_from(">H", data, off)[0]
    off += 2
    ifaces = [struct.unpack_from(">H", data, off + 2 * k)[0] for k in range(ifc)]

    def name(idx):
        e = pool.get(idx)
        if isinstance(e, tuple) and e[0] == "class":
            return pool.get(e[1])
        return e

    return pool, access, name(this_i), name(super_i), [name(x) for x in ifaces]


def describe(z, cls, depth=0, seen=None):
    if seen is None:
        seen = set()
    if cls in seen or depth > 6:
        return
    seen.add(cls)
    try:
        _, acc, this, sup, ifs = parse_hdr(z.read(cls + ".class"))
    except KeyError:
        print("  " * depth + f"{cls}  (not in jar)")
        return
    print("  " * depth + f"{this}")
    for x in ([sup] if sup else []) + list(ifs):
        if x:
            describe(z, x, depth + 1, seen)


if __name__ == "__main__":
    z = D.open_jar("mc")
    for c in sys.argv[1:]:
        print(f"===== {c}")
        describe(z, c.replace(".", "/"))
