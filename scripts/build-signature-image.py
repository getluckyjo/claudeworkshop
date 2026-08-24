#!/usr/bin/env python3
"""Render the whole signature to a PNG, for pasting straight into Gmail.

    ./scripts/build-signature-image.py

Prefer signature.html — real text keeps the links clickable, stays readable
when a client blocks images, and is selectable and searchable. This exists for
when an image is what's wanted anyway. It renders at 2× so it stays sharp on a
retina screen, and the width is halved on the <img> so it displays at true size.

Crop and PNG plumbing is shared with build-signature.py, which already had to
solve it without Pillow.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "signature" / "signature.html"
OUT = ROOT / "signature" / "signature-full.png"

SCALE = 2
WINDOW = (720, 260)   # css px, rendered at SCALE
MARGIN = 4            # px of white left around the ink, at render scale

spec = importlib.util.spec_from_file_location("sigmark", ROOT / "scripts" / "build-signature.py")
sigmark = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sigmark)


def main():
    chrome = sigmark.find_chromium()
    subprocess.run(
        [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         f"--window-size={WINDOW[0]},{WINDOW[1]}",
         f"--force-device-scale-factor={SCALE}",
         "--virtual-time-budget=8000",
         f"--screenshot={OUT}", SRC.as_uri()],
        check=True, capture_output=True,
    )
    if OUT.stat().st_size < 3000:
        sys.exit("Error: render came back blank.")

    w, h, channels, color, raw = sigmark.read_png(OUT)
    pixels, stride = sigmark.unfilter(raw, w, h, channels)
    x0, y0, x1, y1 = sigmark.ink_bbox(pixels, w, h, channels, stride)
    box = (max(0, x0 - MARGIN), max(0, y0 - MARGIN),
           min(w - 1, x1 + MARGIN), min(h - 1, y1 + MARGIN))
    cw, ch = sigmark.write_png(OUT, pixels, w, h, channels, stride, color, box)

    print(f"  {OUT.relative_to(ROOT)}  {cw}x{ch}px, {OUT.stat().st_size // 1024} KB")
    print(f'\n  In email, set the img to width="{round(cw / SCALE)}" so it displays at true size.')


if __name__ == "__main__":
    main()
