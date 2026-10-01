"""Batch 26.1 rename pass: import moves + type renames.

Each entry: (old_fqn, new_fqn, old_simple, new_simple)
  - `import old_fqn;`                      -> `import new_fqn;`
  - bare `old_simple` identifier            -> `new_simple`   (word boundary)
If old_simple == new_simple only the import line changes, but the bare-name
replacement is still applied (it is a no-op there).
"""
import os
import re
import sys

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
MODULES = ["simulated", "offroad", "aeronautics", "sable"]

RENAMES = [
    # 26.1 class moves
    ("net.minecraft.client.renderer.block.model.BakedQuad",
     "net.minecraft.client.resources.model.geometry.BakedQuad",
     "BakedQuad", "BakedQuad"),
    ("net.minecraft.client.renderer.block.model.SimpleModelWrapper",
     "net.minecraft.client.resources.model.SimpleModelWrapper",
     "SimpleModelWrapper", "SimpleModelWrapper"),
    ("net.minecraft.client.renderer.block.model.TextureSlots",
     "net.minecraft.client.resources.model.sprite.TextureSlots",
     "TextureSlots", "TextureSlots"),
    ("net.minecraft.client.renderer.state.QuadParticleRenderState",
     "net.minecraft.client.renderer.state.level.QuadParticleRenderState",
     "QuadParticleRenderState", "QuadParticleRenderState"),
    ("net.minecraft.world.level.GameRules",
     "net.minecraft.world.level.gamerules.GameRules",
     "GameRules", "GameRules"),
    # 26.1 renames
    ("net.minecraft.client.color.block.BlockColor",
     "net.minecraft.client.color.block.BlockTintSource",
     "BlockColor", "BlockTintSource"),
    ("net.minecraft.world.inventory.ClickType",
     "net.minecraft.world.inventory.ContainerInput",
     "ClickType", "ContainerInput"),
    ("net.minecraft.world.level.dimension.end.EndDragonFight",
     "net.minecraft.world.level.dimension.end.EnderDragonFight",
     "EndDragonFight", "EnderDragonFight"),
    ("net.minecraft.client.renderer.entity.state.HitboxesRenderState",
     "net.minecraft.client.renderer.entity.state.HitboxRenderState",
     "HitboxesRenderState", "HitboxRenderState"),
]

dry = "--apply" not in sys.argv
changed_files = 0
counts = {old: 0 for _, _, old, _ in RENAMES}

for mod in MODULES:
    base = os.path.join(ROOT, mod, "src")
    if not os.path.isdir(base):
        continue
    for dirpath, _dirs, files in os.walk(base):
        for fn in files:
            if not fn.endswith(".java"):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, "r", encoding="utf-8", errors="surrogateescape") as f:
                src = f.read()
            orig = src
            for old_fqn, new_fqn, old_simple, new_simple in RENAMES:
                if f"import {old_fqn};" in src:
                    src = src.replace(f"import {old_fqn};", f"import {new_fqn};")
                    counts[old_simple] += 1
                if old_simple != new_simple:
                    new_src, n = re.subn(rf"\b{old_simple}\b", new_simple, src)
                    if n:
                        src = new_src
            if src != orig:
                changed_files += 1
                rel = os.path.relpath(path, ROOT)
                print(f"  {rel}")
                if not dry:
                    with open(path, "w", encoding="utf-8", errors="surrogateescape") as f:
                        f.write(src)

print()
for old_simple, n in counts.items():
    if n:
        print(f"  imports rewritten: {old_simple} ({n})")
print(f"files changed: {changed_files}  {'(dry run)' if dry else '(applied)'}")
