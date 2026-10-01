"""26.1.2 mechanical port transforms for the aeronautics fly modules.

Ordered regex rules derived from the real 26.1.2 client jar and the 26.1
Fabric API module layout (see Tools/_mc_locate.txt, _mc_api.txt, _dumpapi.py).

Dry run by default; pass --apply to write. Report goes to Tools/_rename2.txt.
"""
import os
import re
import sys

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
REPORT = os.path.join(ROOT, "Tools", "_rename2.txt")
APPLY = "--apply" in sys.argv
MODULES = ["sable", "simulated", "offroad", "aeronautics"]

# ---------------------------------------------------------------- FQN rules
# (pattern, replacement). Every pattern is anchored on a full package path and
# terminated with a word boundary so partial matches inside longer names cannot
# happen (e.g. `animal.Parrot` must not eat `animal.ParrotVariant`).
RULES = [
    # --- Fabric Renderer API v1 became a client-only package in 26.1
    (r"net\.fabricmc\.fabric\.api\.renderer\.v1", "net.fabricmc.fabric.api.client.renderer.v1"),

    # --- client render-state classes gained a `level` sub-package
    (r"net\.minecraft\.client\.renderer\.state\.(LevelRenderState|BlockOutlineRenderState"
     r"|CameraRenderState|BlockBreakingRenderState)\b",
     r"net.minecraft.client.renderer.state.level.\1"),

    # --- projectile/animal/vehicle sub-package splits
    (r"net\.minecraft\.world\.entity\.projectile\.AbstractHurtingProjectile\b",
     "net.minecraft.world.entity.projectile.hurtingprojectile.AbstractHurtingProjectile"),
    (r"net\.minecraft\.world\.entity\.projectile\.windcharge\b",
     "net.minecraft.world.entity.projectile.hurtingprojectile.windcharge"),
    (r"net\.minecraft\.world\.entity\.projectile\.(AbstractArrow|ThrownTrident)\b",
     r"net.minecraft.world.entity.projectile.arrow.\1"),
    (r"net\.minecraft\.world\.entity\.animal\.(Parrot|ShoulderRidingEntity)\b",
     r"net.minecraft.world.entity.animal.parrot.\1"),
    (r"net\.minecraft\.world\.entity\.vehicle\.AbstractMinecart\b",
     "net.minecraft.world.entity.vehicle.minecart.AbstractMinecart"),

    # --- BlockAndTintGetter is now a client block-render type
    (r"net\.minecraft\.world\.level\.BlockAndTintGetter\b",
     "net.minecraft.client.renderer.block.BlockAndTintGetter"),

    # --- RenderType moved into its own rendertype package
    (r"net\.minecraft\.client\.renderer\.RenderType\b",
     "net.minecraft.client.renderer.rendertype.RenderType"),

    # --- light dampening replaced the old "light block" concept
    (r"\bgetLightBlock\(", "getLightDampening("),

    # --- misc 26.1 renames
    (r"\bhasPermissions\(", "hasPermission("),
    (r"\.getBlockPosition\(\)", ".blockPosition()"),
    (r"\.drawsPerLayer\(\)", ".drawGroupsPerLayer()"),
    (r"\.dynamicTransforms\(\)", ".chunkSectionInfos()"),
    (r"\bhasImpulse\b", "needsSync"),
    # EntityType lost `is(TagKey)`; go through its registry holder.
    (r"\.getType\(\)\.is\(", ".getType().builtInRegistryHolder().is("),
]

# RenderType's static factories moved to a sibling `RenderTypes` class in 26.1.
# Membership drives the rename so instance/constant members are left alone.
RENDER_TYPES_FACTORIES = [
    "armorCutoutNoCull", "armorEntityGlint", "armorTranslucent", "bannerPattern",
    "beaconBeam", "blockScreenEffect", "breezeEyes", "breezeWind",
    "createArmorDecalCutoutNoCull", "crumbling", "cutoutMovingBlock",
    "debugFilledBox", "debugPoint", "debugQuads", "debugTriangleFan",
    "dragonRays", "dragonRaysDepth", "endCrystalBeam", "endGateway", "endPortal",
    "energySwirl", "entityCutout", "entityCutoutCull", "entityCutoutDissolve",
    "entityCutoutZOffset", "entityGlint", "entityShadow", "entitySolid",
    "entitySolidZOffsetForward", "entityTranslucent", "entityTranslucentCullItemTarget",
    "entityTranslucentEmissive", "eyes", "fireScreenEffect", "glint",
    "glintTranslucent", "itemCutout", "itemTranslucent", "leash", "lightning",
    "lines", "linesTranslucent", "outline", "secondaryBlockOutline",
    "solidMovingBlock", "text", "textBackground", "textBackgroundSeeThrough",
    "textIntensity", "textIntensityPolygonOffset", "textIntensitySeeThrough",
    "textPolygonOffset", "textSeeThrough", "translucentMovingBlock", "waterMask",
]
RULES.append(
    (r"\bRenderType\.(" + "|".join(RENDER_TYPES_FACTORIES) + r")\b", r"RenderTypes.\1")
)

# --- LightTexture was split: static helpers -> LightCoordsUtil, the rest -> Lightmap
LIGHT_STATIC = [
    (r"LightTexture\.FULL_BRIGHT\b", "LightCoordsUtil.FULL_BRIGHT"),
    # FULL_BLOCK had no sky component (pack(15, 0)) and gained no 26.1 constant.
    (r"LightTexture\.FULL_BLOCK\b", "LightCoordsUtil.pack(15, 0)"),
    (r"LightTexture\.pack\b", "LightCoordsUtil.pack"),
    (r"LightTexture\.block\b", "LightCoordsUtil.block"),
    (r"LightTexture\.sky\b", "LightCoordsUtil.sky"),
    (r"LightTexture\.getBrightness\b", "Lightmap.getBrightness"),
]

LT_IMPORT = "import net.minecraft.client.renderer.LightTexture;"

DISPLAY = "displayClientMessage("


def split_top_level_args(s):
    """Split an argument list on commas that are not nested in (), [] or <>-ish."""
    args, depth, cur, in_str, in_chr = [], 0, [], False, False
    i = 0
    while i < len(s):
        c = s[i]
        if in_str:
            cur.append(c)
            if c == "\\":
                cur.append(s[i + 1] if i + 1 < len(s) else "")
                i += 2
                continue
            if c == '"':
                in_str = False
        elif in_chr:
            cur.append(c)
            if c == "\\":
                cur.append(s[i + 1] if i + 1 < len(s) else "")
                i += 2
                continue
            if c == "'":
                in_chr = False
        elif c == '"':
            in_str = True
            cur.append(c)
        elif c == "'":
            in_chr = True
            cur.append(c)
        elif c in "([{":
            depth += 1
            cur.append(c)
        elif c in ")]}":
            depth -= 1
            cur.append(c)
        elif c == "," and depth == 0:
            args.append("".join(cur))
            cur = []
        else:
            cur.append(c)
        i += 1
    args.append("".join(cur))
    return args


def fix_display_client_message(text):
    """`displayClientMessage(msg, true|false)` -> sendOverlayMessage / sendSystemMessage.

    The 26.1 replacement is two different one-argument methods, so the trailing
    boolean has to be dropped. Arguments can span lines, hence the manual scan.
    """
    n = 0
    out = []
    pos = 0
    while True:
        k = text.find(DISPLAY, pos)
        if k == -1:
            out.append(text[pos:])
            break
        start = k + len(DISPLAY)
        depth = 1
        i = start
        in_str = in_chr = False
        while i < len(text) and depth:
            c = text[i]
            if in_str:
                if c == "\\":
                    i += 2
                    continue
                if c == '"':
                    in_str = False
            elif in_chr:
                if c == "\\":
                    i += 2
                    continue
                if c == "'":
                    in_chr = False
            elif c == '"':
                in_str = True
            elif c == "'":
                in_chr = True
            elif c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        if depth:
            out.append(text[pos:])
            break
        args = split_top_level_args(text[start:i])
        if len(args) < 2:
            out.append(text[pos:k + len(DISPLAY)])
            pos = k + len(DISPLAY)
            continue
        flag = args[-1].strip()
        msg = ",".join(args[:-1])
        if flag == "true":
            out.append(text[pos:k] + "sendOverlayMessage(" + msg + ")")
        elif flag == "false":
            out.append(text[pos:k] + "sendSystemMessage(" + msg + ")")
        else:
            out.append(text[pos:i + 1])
            pos = i + 1
            continue
        n += 1
        pos = i + 1
    return "".join(out), n

# Files that keep a Lightmap / LightCoordsUtil usage and therefore need imports.
LIGHTMAP_FILES = {"SubLevelEntityShadowRenderer.java"}


def java_files():
    for mod in MODULES:
        src = os.path.join(ROOT, mod, "src")
        for dirpath, _dirs, files in os.walk(src):
            for f in files:
                if f.endswith(".java"):
                    yield os.path.join(dirpath, f)


def add_import(text, fqn):
    """Insert an import keeping the existing alphabetical ordering."""
    line = f"import {fqn};"
    if line in text:
        return text
    lines = text.split("\n")
    last_import = -1
    for i, l in enumerate(lines):
        if l.startswith("import "):
            last_import = i
    if last_import < 0:
        return text
    imports = [(i, lines[i]) for i in range(last_import + 1) if lines[i].startswith("import ")]
    pos = last_import + 1
    for i, l in imports:
        if l > line:
            pos = i
            break
    lines.insert(pos, line)
    return "\n".join(lines)


report = []
total_hits = 0
changed_files = 0

for path in java_files():
    orig = open(path, encoding="utf-8").read()
    text = orig
    hits = []

    for pat, rep in RULES:
        new, n = re.subn(pat, rep, text)
        if n:
            hits.append((pat, n))
            text = new

    lt_before = len(re.findall(r"\bLightTexture\b", text))
    for pat, rep in LIGHT_STATIC:
        new, n = re.subn(pat, rep, text)
        if n:
            hits.append((pat, n))
            text = new

    text, n_dcm = fix_display_client_message(text)
    if n_dcm:
        hits.append(("displayClientMessage -> sendOverlayMessage/sendSystemMessage", n_dcm))

    # A leftover bare `LightTexture` outside of the import line means the class is
    # used as a *type* (or via an unmapped member) and needs a manual rewrite.
    body_lines = [l for l in text.split("\n") if l.strip() != LT_IMPORT]
    residual = sum(len(re.findall(r"\bLightTexture\b", l)) for l in body_lines)
    if residual:
        hits.append(("RESIDUAL LightTexture (needs manual rewrite)", residual))
        if text != orig:
            changed_files += 1
            n = sum(c for _, c in hits)
            total_hits += n
            report.append(f"{n:5d}  {os.path.relpath(path, ROOT)}   <-- MANUAL")
            for pat, c in hits:
                report.append(f"          {c:4d}x {pat}")
            if APPLY:
                open(path, "w", encoding="utf-8", newline="\n").write(text)
        continue

    # No LightTexture usage left: drop the dead import and add the replacements.
    text = re.sub(r"^" + re.escape(LT_IMPORT) + r"\n", "", text, flags=re.M)
    if re.search(r"\bRenderTypes\.", text) and "import net.minecraft.client.renderer.rendertype.RenderTypes;" not in text:
        text = add_import(text, "net.minecraft.client.renderer.rendertype.RenderTypes")
    if "LightCoordsUtil." in text and "import net.minecraft.util.LightCoordsUtil;" not in text:
        text = add_import(text, "net.minecraft.util.LightCoordsUtil")
    if "Lightmap." in text and "import net.minecraft.client.renderer.Lightmap;" not in text:
        text = add_import(text, "net.minecraft.client.renderer.Lightmap")

    if text != orig:
        changed_files += 1
        n = sum(c for _, c in hits)
        total_hits += n
        report.append(f"{n:5d}  {os.path.relpath(path, ROOT)}")
        for pat, c in hits:
            report.append(f"          {c:4d}x {pat}")
        if APPLY:
            open(path, "w", encoding="utf-8", newline="\n").write(text)

header = [
    f"mode       : {'APPLIED' if APPLY else 'DRY RUN'}",
    f"files      : {changed_files}",
    f"substitutions: {total_hits}",
    "",
]
open(REPORT, "w", encoding="utf-8").write("\n".join(header + report))
print("\n".join(header))
print("see", REPORT)
