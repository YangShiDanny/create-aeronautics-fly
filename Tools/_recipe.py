"""List the constant-pool references made by each method of a class.

Usage:
    python _recipe.py mc net.minecraft.client.renderer.LevelRenderer [methodSubstr]
    python _recipe.py _jars/frapi.jar net.fabricmc...Renderer [methodSubstr]

This is a poor man's decompiler: walking the bytecode instruction stream and
collecting every referenced Field/Method/String/Class constant, in order, is
enough to reconstruct *what* a method does (which helpers it calls, which
constructors it uses) even though we cannot read its source.
"""
import struct
import sys

import _dumpapi as D

# Operand byte-length (after the opcode) for every JVM opcode.
LEN = {}
for op in range(0x00, 0x10):
    LEN[op] = 1
LEN.update({0x10: 2, 0x11: 3, 0x12: 2, 0x13: 3, 0x14: 3})
for op in range(0x15, 0x1A):
    LEN[op] = 2
for op in range(0x1A, 0x36):
    LEN[op] = 1
for op in range(0x36, 0x3B):
    LEN[op] = 2
for op in range(0x3B, 0x84):
    LEN[op] = 1
LEN[0x84] = 3
for op in range(0x85, 0x99):
    LEN[op] = 1
for op in range(0x99, 0xA9):
    LEN[op] = 3
LEN[0xA9] = 2
# tableswitch / lookupswitch handled specially
for op in range(0xAC, 0xB2):
    LEN[op] = 1
for op in range(0xB2, 0xB9):
    LEN[op] = 3
LEN[0xB9] = 5
LEN[0xBA] = 5
LEN[0xBB] = 3
LEN[0xBC] = 2
LEN[0xBD] = 3
LEN[0xBE] = 1
LEN[0xBF] = 1
LEN[0xC0] = 3
LEN[0xC1] = 3
LEN[0xC2] = 1
LEN[0xC3] = 1
LEN[0xC5] = 4
LEN[0xC6] = 3
LEN[0xC7] = 3
LEN[0xC8] = 5
LEN[0xC9] = 5

TWO_BYTE_OPS = {0x12, 0x13, 0x14, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7, 0xB8,
                0xB9, 0xBA, 0xBB, 0xBD, 0xC0, 0xC1}


def resolve(cp, idx):
    """Follow ("class", name_index) -> Utf8."""
    e = cp.get(idx)
    if isinstance(e, tuple) and e[0] == "class":
        return cp.get(e[1], "?")
    return e


def member_ref(cp, idx):
    """Resolve a #idx constant-pool entry to 'Class.name : descriptor'."""
    e = cp.get(idx)
    if not isinstance(e, tuple):
        return repr(e)
    kind = e[0]
    if kind == "nat":
        return repr(e)
    if kind in {"field", "method", "ifacemethod"}:
        cls = resolve(cp, e[1])
        nat = cp.get(e[2])
        if isinstance(nat, tuple) and nat[0] == "nat":
            name, desc = cp.get(nat[1], "?"), cp.get(nat[2], "?")
        else:
            name, desc = "?", "?"
        return f"{cls}.{name}{desc}"
    if kind == "class":
        return resolve(cp, idx)
    if kind == "string":
        return repr(cp.get(e[1], ""))
    if kind == "const":
        return repr(e[1])
    return repr(e)


def parse_full(data):
    """Like D.parse but also keeps the constant pool and raw method bodies."""
    cp, off = D.read_cp(data, 8)
    count = struct.unpack_from(">H", data, 8)[0]
    # re-read cp keeping tags
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
            pool[i] = ("const", struct.unpack_from(">i", data, off)[0] if tag == 3
                       else struct.unpack_from(">f", data, off)[0])
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
            a, b = struct.unpack_from(">HH", data, off)
            kind = {9: "field", 10: "method", 11: "ifacemethod",
                    12: "nat"}.get(tag, f"tag{tag}")
            pool[i] = (kind, a, b)
            off += 4
        elif tag == 15:
            off += 3
        else:
            raise ValueError(f"tag {tag}")
        i += 1

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
            code = None
            for _ in range(attrs):
                an, alen = struct.unpack_from(">HI", data, off)
                body = data[off + 6:off + 6 + alen]
                if pool.get(an) == "Code":
                    code = body
                off += 6 + alen
            out.append((pool.get(ni, "?"), pool.get(di, "?"), acc, code))
        return out, off

    fields, off = members(off)
    methods, off = members(off)
    return pool, methods


def opcodes(code):
    """Yield (opcode, offset) pairs from a Code attribute body.

    Tolerant of truncated/odd trailing bytes: we stop as soon as an operand
    would run past the end of the buffer instead of raising IndexError.
    """
    idx = 8  # skip max_stack/max_locals
    n = len(code)
    while 0 <= idx < n:
        op = code[idx]
        if op == 0xAA:  # tableswitch
            pad = (4 - (idx + 1) % 4) % 4
            base = idx + 1 + pad
            if base + 12 > n:
                return
            lo, hi = struct.unpack_from(">ii", code, base + 4)
            idx = base + 12 + 4 * (hi - lo + 1)
            continue
        if op == 0xAB:  # lookupswitch
            pad = (4 - (idx + 1) % 4) % 4
            base = idx + 1 + pad
            if base + 8 > n:
                return
            cnt = struct.unpack_from(">i", code, base + 4)[0]
            idx = base + 8 + 8 * cnt
            continue
        if op == 0xC4:  # wide
            if idx + 1 >= n:
                return
            # wide iinc = opcode + subop + 2-byte index + 2-byte const (6 bytes)
            # wide <load/store> = opcode + subop + 2-byte index (4 bytes)
            idx += 6 if code[idx + 1] == 0x84 else 4
            continue
        step = LEN.get(op, 1)
        if idx + step > n:
            return
        yield op, idx
        idx += step


def main():
    spec, cls = sys.argv[1], sys.argv[2]
    want = sys.argv[3] if len(sys.argv) > 3 else None
    z = D.open_jar(spec)
    pool, methods = parse_full(z.read(cls.replace(".", "/") + ".class"))
    for name, desc, acc, code in methods:
        if want and want.lower() not in name.lower():
            continue
        print(f"\n### {name}{desc}  [{D.flags(acc)}]")
        if code is None:
            print("    (no code)")
            continue
        seen = set()
        for op, idx in opcodes(code):
            if op in TWO_BYTE_OPS:
                ref = member_ref(pool, struct.unpack_from(">H", code, idx + 1)[0])
                if op in (0x12,):
                    ref = f"LDC {ref}"
                if ref in seen:
                    continue
                seen.add(ref)
                print(f"    {ref}")


if __name__ == "__main__":
    main()
