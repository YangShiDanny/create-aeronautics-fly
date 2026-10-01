import re, sys, html, pathlib

SRC = [
    (r"C:\Users\myth\Downloads\移植到 26.1 快照版本 _ Fabric 文档.html", r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_doc_261.txt"),
    (r"C:\Users\myth\Downloads\移植到 1.21.11 _ Fabric 文档.html", r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_doc_12111.txt"),
]

def strip_html(text: str) -> str:
    # drop script/style
    text = re.sub(r"(?is)<script.*?</script>", " ", text)
    text = re.sub(r"(?is)<style.*?</style>", " ", text)
    # keep code blocks somewhat readable
    text = re.sub(r"(?is)<br\s*/?>", "\n", text)
    text = re.sub(r"(?is)</(p|div|li|h[1-6]|tr|pre|table)>", "\n", text)
    text = re.sub(r"(?is)<li[^>]*>", "- ", text)
    text = re.sub(r"(?is)<t[dh][^>]*>", " | ", text)
    text = re.sub(r"(?is)<[^>]+>", "", text)
    text = html.unescape(text)
    # collapse blank lines
    lines = [ln.rstrip() for ln in text.splitlines()]
    out, blank = [], 0
    for ln in lines:
        if ln.strip() == "":
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln)
    return "\n".join(out)

for src, dst in SRC:
    p = pathlib.Path(src)
    if not p.exists():
        print(f"MISSING: {src}")
        continue
    raw = p.read_text(encoding="utf-8", errors="replace")
    txt = strip_html(raw)
    pathlib.Path(dst).write_text(txt, encoding="utf-8")
    print(f"OK {p.name}: {len(txt)} chars -> {dst}")
