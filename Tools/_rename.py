"""
Mechanical rename pass for the 26.1.2 port.

Two sources:
  1. Fabric API's official IntelliJ migration map
     (Tools/fabric-api-26-1-migration-map.xml) - FQN, simple-class, member renames.
  2. A curated vanilla list for the 1.21.11 "rename shuffle" that 26.1 inherits.

Handles .java, .mixins.json, .accesswidener and fabric.mod.json, and both
dot-separated (source) and slash-separated (internal names) forms.
"""
import os, re, sys
import xml.etree.ElementTree as ET

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
XML = os.path.join(ROOT, "Tools", "fabric-api-26-1-migration-map.xml")
LOG = os.path.join(ROOT, "Tools", "_rename.log")
MODULES = ["sable", "simulated", "offroad", "aeronautics"]

DRY = "--apply" not in sys.argv

# ---------------------------------------------------------------- sources ---
tree = ET.parse(XML)
_raw = [(e.get("oldName"), e.get("newName"), e.get("type"))
        for e in tree.getroot()]
entries = [t for t in _raw if t[0] and t[1]]
skipped = len(_raw) - len(entries)
types = sorted({t[2] for t in _raw if t[2]})

class_map = {}      # oldFQN -> newFQN              (type=class)
member_renames = []  # (oldOwnerFQN, newOwnerFQN, oldMember, newMember)

for old, new, typ in entries:
    if typ == "class":
        class_map[old] = new
    else:
        old_owner, _, old_member = old.rpartition(".")
        new_owner, _, new_member = new.rpartition(".")
        if not old_owner or not new_owner:
            continue
        member_renames.append((old_owner, class_map.get(old_owner, old_owner),
                               old_member, new_member))

# The published XML only carries `type="class"` entries, so the member renames
# from the Fabric API porting guide are listed here explicitly.
# Each rule is (owner class names to gate on, old member, new member).
MEMBER_EXTRA = [
    ({"ItemGroupEvents", "CreativeModeTabEvents"}, "modifyEntriesEvent", "modifyOutputEvent"),
    ({"ItemGroupEvents", "CreativeModeTabEvents"}, "MODIFY_ENTRIES_ALL", "MODIFY_OUTPUT_ALL"),
    ({"FabricItemGroupEntries", "FabricCreativeModeTabOutput"}, "addAfter", "insertAfter"),
    ({"FabricItemGroupEntries", "FabricCreativeModeTabOutput"}, "addBefore", "insertBefore"),
    ({"PayloadTypeRegistry"}, "playC2S", "serverboundPlay"),
    ({"PayloadTypeRegistry"}, "playS2C", "clientboundPlay"),
    ({"PayloadTypeRegistry"}, "configurationC2S", "serverboundConfiguration"),
    ({"PayloadTypeRegistry"}, "configurationS2C", "clientboundConfiguration"),
    ({"KeyBindingHelper", "KeyMappingHelper"}, "registerKeyBinding", "registerKeyMapping"),
    ({"ClientTickEvents"}, "START_WORLD_TICK", "START_LEVEL_TICK"),
    ({"ClientTickEvents"}, "END_WORLD_TICK", "END_LEVEL_TICK"),
    ({"ServerTickEvents"}, "START_WORLD_TICK", "START_LEVEL_TICK"),
    ({"ServerTickEvents"}, "END_WORLD_TICK", "END_LEVEL_TICK"),
    ({"ClientWorldEvents", "ClientLevelEvents"}, "AFTER_CLIENT_WORLD_CHANGE", "AFTER_CLIENT_LEVEL_CHANGE"),
    ({"ServerWorldEvents", "ServerLevelEvents"}, "AFTER_ENTITY_CHANGE_WORLD", "AFTER_ENTITY_CHANGE_LEVEL"),
    ({"ServerChunkEvents"}, "CHUNK_LEVEL_TYPE_CHANGE", "FULL_CHUNK_STATUS_CHANGE"),
    ({"ResourceLoader", "DataResourceLoader"}, "registerReloader", "registerReloadListener"),
    ({"ResourceLoader"}, "addReloaderOrdering", "addListenerOrdering"),
    ({"Screens"}, "getButtons", "getWidgets"),
    ({"Screens"}, "getTextRenderer", "getFont"),
    ({"Screens"}, "getClient", "getMinecraft"),
    ({"BlockApiCache"}, "getWorld", "getLevel"),
    ({"FabricRegistryBuilder"}, "createSimple", "create"),
    ({"DynamicRegistryView"}, "asDynamicRegistryManager", "asRegistryAccess"),
    ({"CustomIngredient"}, "getMatchingItems", "items"),
    ({"CustomIngredient"}, "toDisplay", "display"),
    ({"CustomIngredientSerializer"}, "getPacketCodec", "getStreamCodec"),
    ({"OxidizableBlocksRegistry"}, "registerOxidizableBlockPair", "registerNextStage"),
    ({"OxidizableBlocksRegistry"}, "registerWaxableBlockPair", "registerWaxable"),
    ({"OxidizableBlocksRegistry"}, "registerCopperBlockSet", "registerWeatheringCopperBlocks"),
    ({"VillagerInteractionRegistries"}, "registerCollectable", "registerGatherableItem"),
    ({"StorageUtil"}, "calculateComparatorOutput", "getRedstoneSignal"),
    ({"TransferVariant"}, "getComponentMap", "getComponents"),
    ({"TransferVariant", "FluidVariant", "ItemVariant"}, "withComponentChanges", "withComponents"),
    ({"StorageUtil"}, "calculateComparatorOutput", "getRedstoneSignal"),
    ({"PlayerLookup"}, "getWorld", "getLevel"),
    ({"LivingEntityFeatureRendererRegistrationCallback",
      "LivingEntityRenderLayerRegistrationCallback"}, "registerRenderers", "registerLayers"),
    ({"TooltipComponentCallback", "ClientTooltipComponentCallback"}, "getComponent", "getClientComponent"),
    ({"CompostingChanceRegistry", "CompostableRegistry"}, "add", "add"),
]

VANILLA_FQN = {
    "net.minecraft.resources.ResourceLocationException": "net.minecraft.resources.IdentifierException",
    "net.minecraft.resources.ResourceLocation": "net.minecraft.resources.Identifier",
    "net.minecraft.advancements.critereon": "net.minecraft.advancements.criterion",
    "net.minecraft.BlockUtil": "net.minecraft.util.BlockUtil",
    "net.minecraft.FileUtil": "net.minecraft.util.FileUtil",
    "net.minecraft.Util": "net.minecraft.util.Util",
}
VANILLA_SIMPLE = {
    "ResourceLocationException": "IdentifierException",
    "ResourceLocation": "Identifier",
}
SEPARATOR = re.compile(r"\.|/")

def to_internal(fqn):
    return fqn.replace(".", "/")

# FQN map covering both separators, longest old name first
fqn_pairs = []
for old, new in list(class_map.items()) + list(VANILLA_FQN.items()):
    fqn_pairs.append((old, new))
    fqn_pairs.append((to_internal(old), to_internal(new)))
fqn_pairs.sort(key=lambda kv: len(kv[0]), reverse=True)

def simple_of(fqn):
    return fqn.rsplit(".", 1)[-1].rsplit("$", 1)[-1]

simple_pairs = {}
for old, new in class_map.items():
    if old.endswith("package-info"):
        continue
    so, sn = simple_of(old), simple_of(new)
    if so != sn:
        simple_pairs[so] = sn
simple_pairs.update(VANILLA_SIMPLE)

# owner-simple-name gates for member renames
member_rules = []
for old_owner, new_owner, om, nm in member_renames:
    if om == nm:
        continue
    gates = {simple_of(old_owner), simple_of(new_owner)}
    gates.discard("")
    member_rules.append((gates, om, nm))

for gates, om, nm in MEMBER_EXTRA:
    if om != nm:
        member_rules.append((set(gates), om, nm))

word = lambda s: re.compile(r"(?<![\w$])" + re.escape(s) + r"(?![\w$])")

# ---------------------------------------------------------------- transform -
stats = {"files": 0, "hits": 0}
detail = []

def transform(text, path):
    before = text
    hits = 0

    for old, new in fqn_pairs:
        if old in text:
            n = text.count(old)
            text = text.replace(old, new)
            hits += n

    for old_s, new_s in sorted(simple_pairs.items(), key=lambda kv: len(kv[0]), reverse=True):
        pat = word(old_s)
        text, n = pat.subn(new_s, text)
        hits += n

    # member renames, gated on the owning class being referenced in this file
    for gates, om, nm in member_rules:
        if not any(g in text for g in gates):
            continue
        pat = word(om)
        text, n = pat.subn(nm, text)
        hits += n

    if text != before:
        stats["files"] += 1
        stats["hits"] += hits
        detail.append(f"{hits:5d}  {os.path.relpath(path, ROOT)}")
    return text

targets = []
for mod in MODULES:
    base = os.path.join(ROOT, mod, "src")
    for dirpath, _d, files in os.walk(base):
        for fn in files:
            if fn.endswith(".java") or fn.endswith(".mixins.json") or \
               fn.endswith(".accesswidener") or fn == "fabric.mod.json":
                targets.append(os.path.join(dirpath, fn))

for p in targets:
    txt = open(p, encoding="utf-8").read()
    new = transform(txt, p)
    if new != txt and not DRY:
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)

lines = [
    f"mode       : {'DRY RUN' if DRY else 'APPLIED'}",
    f"xml entries: {len(entries)} usable, {skipped} skipped, types={types}",
    f"fqn pairs  : {len(fqn_pairs)}",
    f"simple map : {len(simple_pairs)}",
    f"member rls : {len(member_rules)}",
    f"files seen : {len(targets)}",
    f"files changed: {stats['files']}",
    f"total hits   : {stats['hits']}",
    "",
]
lines += sorted(detail, reverse=True)
with open(LOG, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("done")
