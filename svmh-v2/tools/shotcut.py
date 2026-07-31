#!/usr/bin/env python3
"""Recover a chrome-devtools screenshot from its saved MCP payload.

take_screenshot responses exceed the inline attachment cap, so the image arrives
truncated and unreadable. The base64 payload in the saved MCP output file is
intact, so decode from there instead.

    python3 tools/shotcut.py                 newest payload -> /tmp/shot_view.jpg
    python3 tools/shotcut.py --tile 1600     also slice into vertical tiles
    python3 tools/shotcut.py --file PATH     decode a specific payload file
"""

from __future__ import annotations

import argparse
import base64
import glob
import os
import sys

SESSIONS = os.path.expanduser("~/.grok/sessions")
OUT_DIR = "/tmp"
VIEW_WIDTH = 1100


def has_image(path: str) -> bool:
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return "base64," in fh.read()
    except OSError:
        return False


def newest_payload() -> str:
    """Newest payload that actually carries an image.

    Every MCP call in every session writes here, so the newest file is usually
    some unrelated tool's JSON. Walk back until an image payload turns up.
    """
    hits = glob.glob(os.path.join(SESSIONS, "*", "*", "mcp", "*.txt"))
    if not hits:
        sys.exit(f"no MCP payload files under {SESSIONS}")
    for path in sorted(hits, key=os.path.getmtime, reverse=True)[:400]:
        if has_image(path):
            return path
    sys.exit("no MCP payload with an image found in the last 400 files")


def decode(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as fh:
        blob = fh.read()
    if "base64," not in blob:
        sys.exit(f"no base64 payload in {path}")
    b64 = blob.split("base64,", 1)[1].split('"')[0].split(")")[0].strip()
    raw = base64.b64decode(b64 + "=" * (-len(b64) % 4))
    dst = os.path.join(OUT_DIR, "shot_raw.jpg")
    with open(dst, "wb") as fh:
        fh.write(raw)
    return dst


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", help="specific MCP payload .txt to decode")
    ap.add_argument("--tile", type=int, metavar="PX",
                    help="slice into vertical tiles of PX source height")
    args = ap.parse_args()

    try:
        from PIL import Image
    except ImportError:
        sys.exit("needs Pillow: python3 -m pip install pillow")

    payload = args.file or newest_payload()
    raw = decode(payload)
    im = Image.open(raw)
    print(f"payload: {payload}")
    print(f"decoded: {raw}  {im.size[0]}x{im.size[1]}")

    view = im.resize(
        (VIEW_WIDTH, round(VIEW_WIDTH * im.height / im.width)), Image.LANCZOS
    )
    view_path = os.path.join(OUT_DIR, "shot_view.jpg")
    view.save(view_path, quality=82)
    print(f"view:    {view_path}  {view.size[0]}x{view.size[1]}")

    if args.tile:
        n = 0
        for top in range(0, im.height, args.tile):
            tile = im.crop((0, top, im.width, min(top + args.tile, im.height)))
            tile = tile.resize(
                (VIEW_WIDTH, round(VIEW_WIDTH * tile.height / tile.width)),
                Image.LANCZOS,
            )
            p = os.path.join(OUT_DIR, f"shot_seg{n:02d}.jpg")
            tile.save(p, quality=82)
            print(f"tile:    {p}  {tile.size[0]}x{tile.size[1]}")
            n += 1


if __name__ == "__main__":
    main()
