"""26.1 GUI migration: GuiGraphics -> GuiGraphicsExtractor.

26.1 deleted `net.minecraft.client.gui.GuiGraphics`. GUI drawing now goes through
`GuiGraphicsExtractor` and the render-state pipeline:
  Renderable#render            -> Renderable#extractRenderState
  AbstractWidget#renderWidget  -> AbstractWidget#extractWidgetRenderState
  Screen#renderBackground      -> Screen#extractBackground
  GuiGraphics#drawString       -> GuiGraphicsExtractor#text
  GuiGraphics#drawCenteredString -> GuiGraphicsExtractor#centeredText
  GuiGraphics#renderItem       -> GuiGraphicsExtractor#item
  GuiGraphics#vLine/hLine      -> GuiGraphicsExtractor#verticalLine/horizontalLine
Unchanged: pose(), fill(), blit(), blitSprite(), fillGradient(), enableScissor(),
disableScissor(), nextStratum(), guiWidth(), guiHeight().

`super.render(...)` and the 4-arg `renderBackground(...)` are NOT rewritten here
(the arity/type is checked by hand) - see the report for the leftovers.
"""
import os
import re
import sys

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
MODULES = ["simulated", "offroad", "aeronautics"]

dry = "--apply" not in sys.argv

SUBSTITUTIONS = [
    # (pattern, replacement, description)
    (r"net\.minecraft\.client\.gui\.GuiGraphics\b",
     "net.minecraft.client.gui.GuiGraphicsExtractor", "import move"),
    (r"\bGuiGraphics\b", "GuiGraphicsExtractor", "type rename"),
    (r"void render\((?=[^)]*GuiGraphicsExtractor)", "void extractRenderState(", "Renderable/Screen override"),
    (r"void renderWidget\((?=[^)]*GuiGraphicsExtractor)", "void extractWidgetRenderState(", "widget override"),
    (r"\.drawString\(", ".text(", "drawString -> text"),
    (r"\.drawCenteredString\(", ".centeredText(", "drawCenteredString -> centeredText"),
    (r"\.vLine\(", ".verticalLine(", "vLine -> verticalLine"),
    (r"\.hLine\(", ".horizontalLine(", "hLine -> horizontalLine"),
]

# renderItem: only on a graphics receiver, never on the static ItemRenderer helper
RENDER_ITEM = re.compile(r"\b(graphics|guiGraphics|gfx|drawContext)\s*\.renderItem\(")

LEFT = [
    (re.compile(r"super\.render\("), "super.render(...)"),
    (re.compile(r"\.renderBackground\([^)]*GuiGraphicsExtractor"), "renderBackground(GuiGraphicsExtractor...)"),
    (re.compile(r"\.textHighlight\([^,]+,[^,]+,[^,]+,[^)]+\)"), "textHighlight(x1,y1,x2,y2) - needs trailing boolean"),
    (re.compile(r"GuiGraphicsMixin"), "file named GuiGraphicsMixin (mixin target string needs manual check)"),
]

changed = 0
leftovers = []
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
            if "GuiGraphics" not in src:
                continue
            orig = src
            for pat, rep, _desc in SUBSTITUTIONS:
                src = re.sub(pat, rep, src)
            src = RENDER_ITEM.sub(lambda m: m.group(1) + ".item(", src)
            if src != orig:
                changed += 1
                print(f"  {os.path.relpath(path, ROOT)}")
                if not dry:
                    with open(path, "w", encoding="utf-8", errors="surrogateescape") as f:
                        f.write(src)
            # report leftovers for manual review
            for rx, desc in LEFT:
                for i, line in enumerate(src.splitlines(), 1):
                    if rx.search(line):
                        leftovers.append(f"  {os.path.relpath(path, ROOT)}:{i}  [{desc}]  {line.strip()[:110]}")

print(f"\nfiles changed: {changed} {'(dry run)' if dry else '(applied)'}")
print("\n--- manual follow-ups ---")
for l in leftovers:
    print(l)
