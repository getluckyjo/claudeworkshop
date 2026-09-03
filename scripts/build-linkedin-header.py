#!/usr/bin/env python3
"""Render the LinkedIn company page header.

    ./scripts/build-linkedin-header.py

LinkedIn wants 4200 x 700 uploaded and renders it at 1128 x 191, so this
draws at 1050 x 175 CSS pixels and screenshots at 4x. Two things constrain
the composition and both are invisible until it's live:

  * On desktop the page logo sits over the bottom-left corner
  * On mobile the banner is cropped to roughly the centre 900 of 1128

So nothing that matters goes in the outer eighth or the bottom-left. The
guides are drawn when run with --guides, to check that by eye.

Two variants, because a banner is a taste call: ink and paper.
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "linkedin"

# Design in 1050 x 175 and scale the whole frame up by transform, rather than
# leaning on --force-device-scale-factor. Chromium's window-size and scale
# factor interact differently across builds and the first attempt rendered a
# clipped 262px viewport; a transform is deterministic.
W, H, SCALE = 1050, 175, 4   # -> 4200 x 700

LINE = "Not a coach. An operator who coaches."
# Stacked single lines rather than a stat grid. Three columns didn't fit the
# width without every label wrapping to three ragged lines, and a banner is
# glanced at rather than studied.
PROOF = [
    ("10m+", "units sold, five countries"),
    ("8", "seats a cohort, never more"),
    ("3hrs", "to your first thing running"),
]
FOOT = "entrepreneurcoach.co.za"


VARIANTS = {
    "ink": {
        "ground": "#0E0E10",
        "type": "#FFFFFF",
        "muted": "rgba(255,255,255,0.52)",
        "accent": "#F25C2A",
        "rule": "rgba(255,255,255,0.14)",
    },
    "paper": {
        "ground": "#FFFFFF",
        "type": "#0E0E10",
        "muted": "#6F6F73",
        "accent": "#F25C2A",
        "rule": "#E0DED7",
    },
}


def page(v, guides):
    proof = "".join(
        f'<p class="stat"><span class="n">{n}</span>'
        f'<span class="l">{l}</span></p>'
        for n, l in PROOF
    )
    guide_markup = """
  <div class="guide mobile"></div>
  <div class="guide logo"></div>""" if guides else ""

    return f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>
@import url("fonts.css");

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

html, body {{
  width: {W * SCALE}px;
  height: {H * SCALE}px;
  overflow: hidden;
  background: {v['ground']};
}}

.frame {{
  width: {W}px;
  height: {H}px;
  transform: scale({SCALE});
  transform-origin: top left;
  background: {v['ground']};
  color: {v['type']};
  font-family: "Geist", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
  position: relative;
  display: flex;
  align-items: center;
  /* The logo plate reaches about 158px in; the mobile crop eats the outer
     eighth. Left padding clears the first, right padding clears the second. */
  padding: 0 150px 0 196px;
  gap: 40px;
}}

/* A single vermilion edge, so the banner reads as ours at thumbnail size
   even when the type is too small to make out. */
.frame::before {{
  content: "";
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 7px;
  background: {v['accent']};
}}

.line {{
  font-size: 31px;
  line-height: 1.14;
  font-weight: 600;
  letter-spacing: -0.028em;
  max-width: 420px;
  text-wrap: balance;
}}
.line .dot {{ color: {v['accent']}; }}

.rule {{
  width: 1px;
  align-self: stretch;
  margin: 38px 0;
  background: {v['rule']};
  flex: none;
}}

.right {{
  display: flex;
  flex-direction: column;
  gap: 14px;
  flex: 1;
}}

.stats {{ display: flex; flex-direction: column; gap: 5px; }}

.stat {{ white-space: nowrap; line-height: 1.2; }}
.stat .n {{
  font-size: 15px;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: {v['accent']};
  display: inline-block;
  min-width: 44px;
}}
.stat .l {{
  font-size: 12.5px;
  color: {v['muted']};
}}

.foot {{
  font-size: 12px;
  letter-spacing: 0.03em;
  color: {v['muted']};
}}

/* Only drawn with --guides, never in the artwork itself. */
.guide {{ position: absolute; pointer-events: none; }}
.guide.mobile {{
  top: 0; bottom: 0;
  left: {round(W * 114 / 1128)}px;
  right: {round(W * 114 / 1128)}px;
  border-left: 1px dashed #00E5FF;
  border-right: 1px dashed #00E5FF;
}}
.guide.logo {{
  left: 0; bottom: 0;
  width: {round(W * 170 / 1128)}px;
  height: {round(H * 96 / 191)}px;
  background: rgba(0,229,255,0.22);
}}
</style></head>
<body>
<div class="frame">
  <p class="line">Not a coach.<br>An operator who coaches<span class="dot">.</span></p>
  <div class="rule"></div>
  <div class="right">
    <div class="stats">{proof}</div>
    <p class="foot">{FOOT}</p>
  </div>{guide_markup}
</div>
</body></html>
"""


def find_chromium():
    for n in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        p = shutil.which(n)
        if p:
            return p
    for pat in ("chromium-*/chrome-linux/chrome",
                "chromium_headless_shell-*/chrome-linux/headless_shell"):
        f = sorted(Path("/opt/pw-browsers").glob(pat))
        if f:
            return str(f[-1])
    sys.exit("Error: no Chromium found.")


def main():
    guides = "--guides" in sys.argv
    OUT.mkdir(exist_ok=True)
    shutil.copy(ROOT / "handouts" / "fonts.css", OUT / "fonts.css")
    chrome = find_chromium()

    for name, v in VARIANTS.items():
        stem = f"linkedin-header-{name}" + ("-guides" if guides else "")
        html_path = OUT / f"{stem}.html"
        png_path = OUT / f"{stem}.png"
        html_path.write_text(page(v, guides))
        subprocess.run(
            [chrome, "--headless", "--disable-gpu", "--no-sandbox",
             "--hide-scrollbars", f"--window-size={W * SCALE},{H * SCALE}",
             "--virtual-time-budget=8000",
             f"--screenshot={png_path}", html_path.as_uri()],
            check=True, capture_output=True,
        )
        kb = png_path.stat().st_size // 1024
        print(f"  {png_path.relative_to(ROOT)}  {W*SCALE}x{H*SCALE}  ({kb} KB)")


if __name__ == "__main__":
    main()
