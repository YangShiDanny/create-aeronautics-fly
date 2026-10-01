import re, html, urllib.request, urllib.error, pathlib

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}

PAGES = [
    ("https://docs.neoforged.net/primer/docs/26.1",
     r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_primer_261.txt"),
    ("https://docs.neoforged.net/primer/docs/1.21.11",
     r"E:\TUAN2\MCMODS\create-aeronautics-fly\Tools\_primer_12111.txt"),
]

def strip_html(text: str) -> str:
    text = re.sub(r"(?is)<script.*?</script>", " ", text)
    text = re.sub(r"(?is)<style.*?</style>", " ", text)
    text = re.sub(r"(?is)<nav.*?</nav>", " ", text)
    text = re.sub(r"(?is)<br\s*/?>", "\n", text)
    text = re.sub(r"(?is)</(p|div|li|h[1-6]|tr|pre|table)>", "\n", text)
    text = re.sub(r"(?is)<li[^>]*>", "\n- ", text)
    text = re.sub(r"(?is)<t[dh][^>]*>", " | ", text)
    text = re.sub(r"(?is)<code[^>]*>", "`", text)
    text = re.sub(r"(?is)</code>", "`", text)
    text = re.sub(r"(?is)<[^>]+>", "", text)
    text = html.unescape(text)
    lines = [ln.rstrip() for ln in text.splitlines()]
    out, blank = [], 0
    for ln in lines:
        if not ln.strip():
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln)
    return "\n".join(out)

for url, dst in PAGES:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=90) as r:
            raw = r.read().decode("utf-8", "replace")
        txt = strip_html(raw)
        pathlib.Path(dst).write_text(txt, encoding="utf-8")
        print(f"OK {url} -> {len(txt)} chars -> {dst}")
    except Exception as e:
        print(f"FAIL {url}: {e}")
