#!/usr/bin/env python3
"""Render the brand mark to a tightly-cropped PNG for use in email signatures.

Email clients won't load Caveat, so the handwritten mark has to be an image if
it's going to appear at all. This renders signature/signature-mark.html with
Chromium and trims the surrounding white.

There's no Pillow or ImageMagick on the cloud runners, so the crop is done here
against the raw PNG — decode, unfilter, find the ink, re-encode.

    ./scripts/build-signature.py
"""

import shutil
import struct
import subprocess
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "signature" / "signature-mark.html"
OUT = ROOT / "signature" / "signature-mark.png"

# Chromium refuses to screenshot very small viewports, so render generously and
# crop after.
WINDOW = (560, 170)
MARGIN = 6  # px of white left around the mark


def find_chromium():
    for name in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        path = shutil.which(name)
        if path:
            return path
    for pattern in ("chromium-*/chrome-linux/chrome",):
        found = sorted(Path("/opt/pw-browsers").glob(pattern))
        if found:
            return str(found[-1])
    sys.exit("Error: no Chromium found.")


def render(chrome, dest):
    subprocess.run(
        [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--hide-scrollbars",
            f"--window-size={WINDOW[0]},{WINDOW[1]}",
            "--virtual-time-budget=8000",
            f"--screenshot={dest}",
            SRC.as_uri(),
        ],
        check=True,
        capture_output=True,
    )
    if dest.stat().st_size < 4000:
        sys.exit("Error: render came back blank — fonts probably hadn't painted.")


# --------------------------------------------------------------------------
# Minimal PNG read / crop / write. 8-bit RGB or RGBA only, which is what
# Chromium emits.
# --------------------------------------------------------------------------

def read_png(path):
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        sys.exit("Error: not a PNG.")
    pos = 8
    idat = bytearray()
    header = None
    while pos < len(data):
        (length,) = struct.unpack(">I", data[pos : pos + 4])
        kind = data[pos + 4 : pos + 8]
        body = data[pos + 8 : pos + 8 + length]
        if kind == b"IHDR":
            w, h, depth, color, _, _, interlace = struct.unpack(">IIBBBBB", body)
            if depth != 8 or color not in (2, 6) or interlace:
                sys.exit(f"Error: unsupported PNG (depth {depth}, colour {color}).")
            header = (w, h, color)
        elif kind == b"IDAT":
            idat += body
        elif kind == b"IEND":
            break
        pos += 12 + length
    w, h, color = header
    channels = 3 if color == 2 else 4
    return w, h, channels, color, zlib.decompress(bytes(idat))


def unfilter(raw, w, h, channels):
    """Undo the per-scanline filters, returning flat pixel rows."""
    stride = w * channels
    out = bytearray(stride * h)
    prev = bytearray(stride)
    pos = 0
    for y in range(h):
        ftype = raw[pos]
        pos += 1
        line = bytearray(raw[pos : pos + stride])
        pos += stride
        if ftype == 1:  # Sub
            for i in range(channels, stride):
                line[i] = (line[i] + line[i - channels]) & 0xFF
        elif ftype == 2:  # Up
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 0xFF
        elif ftype == 3:  # Average
            for i in range(stride):
                left = line[i - channels] if i >= channels else 0
                line[i] = (line[i] + ((left + prev[i]) >> 1)) & 0xFF
        elif ftype == 4:  # Paeth
            for i in range(stride):
                a = line[i - channels] if i >= channels else 0
                b = prev[i]
                c = prev[i - channels] if i >= channels else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pred = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pred) & 0xFF
        elif ftype != 0:
            sys.exit(f"Error: unknown PNG filter {ftype}.")
        out[y * stride : (y + 1) * stride] = line
        prev = line
    return out, stride


def ink_bbox(pixels, w, h, channels, stride, threshold=245):
    """Bounding box of anything that isn't near-white and isn't transparent."""
    min_x, min_y, max_x, max_y = w, h, -1, -1
    for y in range(h):
        row = y * stride
        for x in range(w):
            i = row + x * channels
            if channels == 4 and pixels[i + 3] < 8:
                continue
            if pixels[i] > threshold and pixels[i + 1] > threshold and pixels[i + 2] > threshold:
                continue
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y
    if max_x < 0:
        sys.exit("Error: rendered image is blank.")
    return min_x, min_y, max_x, max_y


def write_png(path, pixels, w, h, channels, stride, color, box):
    x0, y0, x1, y1 = box
    cw, ch = x1 - x0 + 1, y1 - y0 + 1
    raw = bytearray()
    for y in range(y0, y1 + 1):
        raw.append(0)  # filter: none
        start = y * stride + x0 * channels
        raw += pixels[start : start + cw * channels]

    def chunk(kind, body):
        return (
            struct.pack(">I", len(body))
            + kind
            + body
            + struct.pack(">I", zlib.crc32(kind + body) & 0xFFFFFFFF)
        )

    ihdr = struct.pack(">IIBBBBB", cw, ch, 8, color, 0, 0, 0)
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + chunk(b"IEND", b"")
    )
    return cw, ch


def main():
    chrome = find_chromium()
    render(chrome, OUT)

    w, h, channels, color, raw = read_png(OUT)
    pixels, stride = unfilter(raw, w, h, channels)
    x0, y0, x1, y1 = ink_bbox(pixels, w, h, channels, stride)

    box = (
        max(0, x0 - MARGIN),
        max(0, y0 - MARGIN),
        min(w - 1, x1 + MARGIN),
        min(h - 1, y1 + MARGIN),
    )
    cw, ch = write_png(OUT, pixels, w, h, channels, stride, color, box)

    print(f"  {OUT.relative_to(ROOT)}  {cw}x{ch}px, {OUT.stat().st_size // 1024} KB")
    print(f"\n  In email, set the img to width=\"{round(cw / 3)}\" for a 3x-sharp mark.")


if __name__ == "__main__":
    main()
