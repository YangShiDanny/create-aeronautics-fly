"""Download the 26.1.2 client jar and dump its class/member API (unobfuscated -> official names)."""
import os, io, zipfile, urllib.request, struct, time, re, sys

UA = {"User-Agent": "Mozilla/5.0 (wb)"}
ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
MC_DIR = os.path.join(ROOT, "Tools", "_mc")
os.makedirs(MC_DIR, exist_ok=True)
JAR = os.path.join(MC_DIR, "client-26.1.2.jar")
URL = "https://piston-data.mojang.com/v1/objects/4e618f09a0c649dde3fdf829df443ce0b8831e65/client.jar"
EXPECT = 38113927

def download():
    if os.path.exists(JAR) and os.path.getsize(JAR) == EXPECT:
        return
    for attempt in range(1, 6):
        try:
            req = urllib.request.Request(URL, headers=UA)
            with urllib.request.urlopen(req, timeout=180) as r, open(JAR, "wb") as f:
                got = 0
                while True:
                    chunk = r.read(1 << 20)
                    if not chunk:
                        break
                    f.write(chunk)
                    got += len(chunk)
            print(f"  attempt {attempt}: wrote {got} bytes")
            if os.path.getsize(JAR) == EXPECT:
                return
        except Exception as e:
            print(f"  attempt {attempt} failed: {e}")
        time.sleep(3 * attempt)
    raise SystemExit("download failed")

print("downloading client jar...")
download()
print("size:", os.path.getsize(JAR))

# ---------------------------------------------------------------- class parse
def parse_class(data):
    """Return (this_name, super_name, [field...], [method...]) as (name, descriptor) pairs."""
    off = 8  # magic + minor + major
    (cp_count,) = struct.unpack_from(">H", data, off); off += 2
    cp = {}
    i = 1
    while i < cp_count:
        tag = data[off]; off += 1
        if tag == 1:
            (ln,) = struct.unpack_from(">H", data, off); off += 2
            cp[i] = data[off:off + ln].decode("utf-8", "replace"); off += ln
        elif tag in (3, 4):
            off += 4
        elif tag in (5, 6):
            off += 8; i += 1
        elif tag in (7, 8, 16, 19, 20):
            off += 2
        elif tag in (9, 10, 11, 12, 17, 18):
            off += 4
        elif tag == 15:
            off += 3
        else:
            raise ValueError(f"bad cp tag {tag} at {off}")
        i += 1

    off += 6  # access_flags, this_class, super_class
    (ifc,) = struct.unpack_from(">H", data, off); off += 2 + 2 * ifc

    def read_members(off):
        (cnt,) = struct.unpack_from(">H", data, off); off += 2
        out = []
        for _ in range(cnt):
            acc, name_i, desc_i, attrs = struct.unpack_from(">HHHH", data, off); off += 8
            out.append((cp.get(name_i, "?"), cp.get(desc_i, "?"), acc))
            for _ in range(attrs):
                (_ni, alen) = struct.unpack_from(">HI", data, off); off += 6 + alen
        return out, off

    fields, off = read_members(off)
    methods, off = read_members(off)
    return fields, methods

def u2_at(data, off):
    return struct.unpack_from(">H", data, off)[0]

def class_names(data):
    off = 8
    cp_count = u2_at(data, off); off += 2
    cp = {}
    i = 1
    while i < cp_count:
        tag = data[off]; off += 1
        if tag == 1:
            ln = u2_at(data, off); off += 2
            cp[i] = data[off:off + ln].decode("utf-8", "replace"); off += ln
        elif tag in (3, 4):
            off += 4
        elif tag in (5, 6):
            off += 8; i += 1
        elif tag in (7, 8, 16, 19, 20):
            off += 2
        elif tag in (9, 10, 11, 12, 17, 18):
            off += 4
        elif tag == 15:
            off += 3
        i += 1
    this_i = u2_at(data, off + 2)
    super_i = u2_at(data, off + 4)
    return cp.get(this_i), cp.get(super_i)

INTEREST = [
    "ChunkPos", "AbstractArrow", "ShoulderRidingEntity", "Parrot",
    "AbstractMinecart", "ThrownTrident", "AbstractHurtingProjectile",
    "BlockAndTintGetter", "LightTexture", "RenderType",
    "BlockMultiBufferSource", "BlockRenderDispatcher", "SectionBuffers",
    "LevelRenderState", "BlockOutlineRenderState", "CameraRenderState",
    "BlockBreakingRenderState",
]

classes = []
parsed = {}
with zipfile.ZipFile(JAR) as z:
    for n in z.namelist():
        if not n.endswith(".class"):
            continue
        internal = n[:-6]
        if not internal.startswith("net/minecraft"):
            continue
        classes.append(internal)
        simple = internal.rsplit("/", 1)[-1].split("$")[0]
        if simple in INTEREST:
            try:
                fields, methods = parse_class(z.read(n))
                parsed.setdefault(simple, []).append((internal, fields, methods))
            except Exception as e:
                parsed.setdefault(simple, []).append((internal, f"ERR {e}", []))

classes.sort()
with open(os.path.join(ROOT, "Tools", "_mc_classes.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(classes))
print(f"net.minecraft classes: {len(classes)}")

with open(os.path.join(ROOT, "Tools", "_mc_api.txt"), "w", encoding="utf-8") as f:
    for simple in INTEREST:
        f.write(f"\n===== {simple} =====\n")
        for internal, fields, methods in parsed.get(simple, []):
            f.write(f"CLASS {internal}  ({len(fields)} fields, {len(methods)} methods)\n")
            for nm, d, acc in fields:
                if acc & 0x0001 or acc & 0x0002:  # public or private
                    f.write(f"   F {'pub' if acc & 1 else 'pri'} {nm} {d}\n")
            for nm, d, acc in methods:
                if acc & 0x0001:
                    f.write(f"   M pub {nm}{d}\n")
        if simple not in parsed:
            f.write("  (not present)\n")

# where did the moved ones go? search by simple name
with open(os.path.join(ROOT, "Tools", "_mc_locate.txt"), "w", encoding="utf-8") as f:
    for simple in INTEREST:
        hits = [c for c in classes if c.rsplit("/", 1)[-1].split("$")[0] == simple]
        f.write(f"{simple}: {hits}\n")
print("done")
