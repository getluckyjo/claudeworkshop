#!/usr/bin/env python3
"""Turn a markdown note into a branded PDF on the Entrepreneur Coach identity.

    ./scripts/build-note.py <note.md> [--for "Kowie Lotter, Creative Beverages"]
                                      [--title "..."] [--out notes/]

Written for client-facing notes — the things you write once and send to one
person. Styling maps to DESIGN.md, same tokens as the handouts and invoices.

There is no markdown library in this environment, so the converter below covers
exactly what these notes use: headings, bold, italic, inline code, fenced code,
tables, blockquotes, lists, and rules. It is deliberately small rather than
general — if a note needs something it doesn't handle, add it here.
"""

import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------- markdown

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def convert(md):
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        ln = lines[i]

        if ln.startswith("```"):
            block = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(html.escape(lines[i], quote=False))
                i += 1
            out.append("<pre>" + "\n".join(block) + "</pre>")
            i += 1
            continue

        if re.match(r"^\s*(---|===)\s*$", ln):
            out.append("<hr>")
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue

        # table: header row, separator, body
        if ln.strip().startswith("|") and i + 1 < len(lines) and re.match(
                r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            def cells(row):
                return [c.strip() for c in row.strip().strip("|").split("|")]
            head = cells(ln)
            aligns = ["r" if c.strip().endswith(":") and not c.strip().startswith(":")
                      else "" for c in cells(lines[i + 1])]
            i += 2
            body = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(cells(lines[i]))
                i += 1
            th = "".join(f'<th class="{a}">{inline(c)}</th>' for c, a in zip(head, aligns))
            tr = "".join(
                "<tr>" + "".join(f'<td class="{a}">{inline(c)}</td>'
                                 for c, a in zip(r, aligns + [""] * len(r))) + "</tr>"
                for r in body)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>")
            continue

        if ln.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(lines[i].lstrip(">").strip())
                i += 1
            paras = "".join(f"<p>{inline(p)}</p>" for p in
                            " ".join(quote).split("  ") if p.strip())
            out.append(f"<blockquote>{paras or inline(' '.join(quote))}</blockquote>")
            continue

        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", ln)
        if m:
            ordered = bool(re.match(r"\d+\.", m.group(2)))
            items, cur = [], None
            while i < len(lines):
                mm = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", lines[i])
                if mm:
                    if cur:
                        items.append(cur)
                    cur = mm.group(3)
                    i += 1
                elif lines[i].startswith("  ") and lines[i].strip() and cur is not None:
                    cur += " " + lines[i].strip()      # continuation line
                    i += 1
                else:
                    break
            if cur:
                items.append(cur)
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue

        if not ln.strip():
            i += 1
            continue

        para = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#{1,4}\s|```|>|\s*[-*]\s|\s*\d+\.\s|\|)", lines[i]) \
                and not re.match(r"^\s*---\s*$", lines[i]):
            para.append(lines[i].strip())
            i += 1
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


# ------------------------------------------------------------------- page

CSS = """
@import url("../handouts/fonts.css");
:root{--paper:#fff;--bone:#F4F4F1;--soft:#ECEAE3;--ink:#0E0E10;--ink-soft:#2A2A2D;
 --muted:#6F6F73;--rule:#E0DED7;--rule-strong:#C8C5BB;--red:#F25C2A;--red-deep:#C8421A;
 --red-soft:#FCE6DC;--blue:#2D55FF;
 --display:"Geist","Inter Tight",ui-sans-serif,system-ui,sans-serif;
 --script:"Caveat","Brush Script MT",cursive;--tr-eyebrow:.18em;--tr-tight:-.02em;--tr-display:-.035em}
@page{size:A4;margin:18mm 17mm 16mm 17mm}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:var(--display);color:var(--ink);background:#fff;font-size:10pt;
 line-height:1.55;letter-spacing:-.01em;margin:0}
.brandmark{display:flex;align-items:flex-end;gap:2mm;margin:0 0 16mm 0}
.brandmark .name{font-family:var(--script);font-weight:700;font-size:19pt;line-height:.85;
 transform:rotate(-2deg);transform-origin:left bottom}
.brandmark .dot{width:4.2pt;height:4.2pt;border-radius:999px;background:var(--red);margin-bottom:1.4pt}
.brandmark .role{font-size:7.5pt;font-weight:600;letter-spacing:var(--tr-eyebrow);
 text-transform:uppercase;color:var(--muted);margin-left:4mm;padding-bottom:1mm}
.doctitle{font-size:26pt;font-weight:700;letter-spacing:var(--tr-display);line-height:1.02;margin:0 0 5mm 0}
.hero-rule{width:20mm;height:1.5mm;background:var(--red);border-radius:.7mm;margin:0 0 5mm 0}
.forwhom{font-size:9.5pt;color:var(--muted);margin:0 0 14mm 0}
.forwhom b{color:var(--ink);font-weight:600}
h1{font-size:16pt;font-weight:700;letter-spacing:var(--tr-tight);margin:10mm 0 3mm;line-height:1.15}
h2{font-size:13pt;font-weight:700;letter-spacing:var(--tr-tight);margin:9mm 0 3mm;line-height:1.2;
 padding-top:3mm;border-top:1px solid var(--rule)}
h3{font-size:8pt;font-weight:600;letter-spacing:var(--tr-eyebrow);text-transform:uppercase;
 color:var(--red);margin:7mm 0 2.5mm}
p{margin:0 0 3.5mm}
strong{font-weight:600}
a{color:var(--red);text-decoration:none}
code{font-family:var(--display);font-weight:600;background:var(--soft);border-radius:2px;
 padding:.3mm 1.3mm;font-size:9pt}
hr{border:0;border-top:1px solid var(--rule);margin:8mm 0}
ul,ol{margin:0 0 4mm;padding-left:5mm}
li{margin-bottom:2mm}
blockquote{background:var(--bone);border-left:3px solid var(--red);padding:4.5mm 5.5mm;
 margin:0 0 5mm;page-break-inside:avoid}
blockquote p{margin:0 0 2mm;font-size:10pt}
blockquote p:last-child{margin:0}
pre{background:var(--bone);padding:4.5mm 5.5mm;margin:0 0 5mm;font-family:var(--display);
 font-size:9pt;line-height:1.5;white-space:pre-wrap;page-break-inside:avoid;color:var(--ink-soft)}
table{width:100%;border-collapse:collapse;margin:0 0 5mm;font-size:9.5pt;page-break-inside:avoid}
th{text-align:left;font-size:7.5pt;font-weight:600;letter-spacing:var(--tr-eyebrow);
 text-transform:uppercase;color:var(--muted);border-bottom:1.5px solid var(--ink);padding:0 3mm 2mm 0}
td{padding:2.8mm 3mm 2.8mm 0;border-bottom:1px solid var(--rule);vertical-align:top}
th.r,td.r{text-align:right}
.sig{font-family:var(--script);font-weight:700;color:var(--red);font-size:16pt;line-height:1;margin:10mm 0 2mm}
.foot{border-top:1px solid var(--rule);padding-top:3mm;font-size:8.5pt;color:var(--muted);
 display:flex;justify-content:space-between}
"""

BRANDMARK = """<div class="brandmark">
  <span class="name">Johannes le Roux</span><span class="dot"></span>
  <span class="role">Entrepreneur Coach</span>
</div>"""


def find_chromium():
    for n in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        p = shutil.which(n)
        if p:
            return p
    found = sorted(Path("/opt/pw-browsers").glob("chromium-*/chrome-linux/chrome"))
    if found:
        return str(found[-1])
    sys.exit("Error: no Chromium found.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--for", dest="prepared_for", default="")
    ap.add_argument("--title", default="")
    ap.add_argument("--date", default="")
    ap.add_argument("--out", default="notes")
    a = ap.parse_args()

    md = Path(a.source).read_text()
    body = md

    # A leading H1 always becomes the document title — never repeat it in the
    # body, whether or not --title overrides the text.
    title = a.title
    m = re.match(r"^#\s+(.*)$", md.split("\n")[0])
    if m:
        title = title or m.group(1)
        body = "\n".join(md.split("\n")[1:])

    out_dir = ROOT / a.out
    out_dir.mkdir(exist_ok=True)
    (out_dir / "note.css").write_text(CSS)

    meta = []
    if a.prepared_for:
        meta.append(f"Prepared for <b>{html.escape(a.prepared_for)}</b>")
    if a.date:
        meta.append(html.escape(a.date))
    meta.append("Entrepreneur Coach")

    stem = Path(a.source).stem
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{html.escape(title)}</title><link rel="stylesheet" href="note.css"></head><body>
{BRANDMARK}
<p class="doctitle">{html.escape(title)}</p>
<div class="hero-rule"></div>
<p class="forwhom">{' &nbsp;·&nbsp; '.join(meta)}</p>
{convert(body)}
<p class="sig">Johannes</p>
<div class="foot"><span>Johannes le Roux &nbsp;·&nbsp; Entrepreneur Coach</span>
<span>entrepreneurcoach.co.za</span></div>
</body></html>"""

    h = out_dir / f"{stem}.html"
    pdf = out_dir / f"{stem}.pdf"
    h.write_text(page)
    subprocess.run([find_chromium(), "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--virtual-time-budget=5000",
                    f"--print-to-pdf={pdf}", h.as_uri()], check=True, capture_output=True)
    print(f"  {pdf.relative_to(ROOT)}  ({pdf.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
