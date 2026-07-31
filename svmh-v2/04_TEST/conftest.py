"""Shared helpers for the 04_TEST suite.

Stdlib only. Import from the static tests; run directly with --refresh to
regenerate the fixtures after an intentional change.
"""

from __future__ import annotations

import json
import os
import re
import struct
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.normpath(os.path.join(TEST_DIR, "..", "03_BUILD"))
FIXTURES = os.path.join(TEST_DIR, "fixtures")

# The built pages, in nav order. Add a page here and every static test picks
# it up automatically.
PAGES = [
    "index.html",
    "request-a-quote.html",
    "eot-cranes/double-girder.html",
    "locations/bangalore.html",
]

# Asset categories under 03_BUILD/assets/img. The category encodes the role the
# asset plays in the DNA grammar, which is what makes a misuse detectable.
IMG_CATEGORIES = ("cutouts", "bands", "cards", "people")


class Result:
    """Collects pass/fail lines so a whole file reports at once."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.rows: list[tuple[bool, str, str]] = []

    def check(self, ok: bool, label: str, detail: str = "") -> bool:
        self.rows.append((bool(ok), label, detail))
        return bool(ok)

    @property
    def failures(self) -> int:
        return sum(1 for ok, _, _ in self.rows if not ok)

    def report(self) -> int:
        print(f"\n=== {self.name}")
        for ok, label, detail in self.rows:
            mark = "PASS" if ok else "FAIL"
            line = f"  {mark}  {label}"
            if detail and not ok:
                line += f"\n          {detail}"
            print(line)
        print(f"  -- {len(self.rows) - self.failures}/{len(self.rows)} passed")
        return self.failures


def read(page: str) -> str:
    with open(os.path.join(BUILD, page), encoding="utf-8") as fh:
        return fh.read()


def main_of(html: str) -> str:
    m = re.search(r"<main\b.*?</main>", html, re.S)
    return m.group(0) if m else ""


def refs(html: str) -> list[str]:
    """Every local src/href that points at a file.

    Includes root-absolute paths like /assets/img/x.jpg. Excluding them used to
    hide a whole class of dead reference: the served site resolves / to the
    build root, so an absolute asset path is just as checkable as a relative
    one, and just as broken when the file is missing.
    """
    found = re.findall(r'(?:src|href)="([^"#?]+)"', html)
    return [
        r
        for r in found
        if not r.startswith(("http", "//", "mailto:", "tel:", "data:"))
        and "." in os.path.basename(r)
    ]


def resolve(page: str, ref: str) -> str:
    """Resolve a reference to a path on disk.

    A leading / is resolved against the build root, matching how the static
    server serves it -- not against the filesystem root.
    """
    if ref.startswith("/"):
        return os.path.normpath(os.path.join(BUILD, ref.lstrip("/")))
    return os.path.normpath(os.path.join(BUILD, os.path.dirname(page), ref))


def image_size(path: str) -> tuple[int, int] | None:
    """Real pixel dimensions for PNG and JPEG, without Pillow."""
    with open(path, "rb") as fh:
        head = fh.read(26)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", head[16:24])
            return int(w), int(h)
        if head[:2] == b"\xff\xd8":
            fh.seek(2)
            while True:
                b = fh.read(1)
                while b and b != b"\xff":
                    b = fh.read(1)
                marker = fh.read(1)
                while marker == b"\xff":
                    marker = fh.read(1)
                if not marker:
                    return None
                if marker[0] in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                                 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    fh.read(3)
                    h, w = struct.unpack(">HH", fh.read(4))
                    return int(w), int(h)
                size = struct.unpack(">H", fh.read(2))[0]
                fh.seek(size - 2, 1)
    return None


def load_fixture(name: str) -> dict:
    with open(os.path.join(FIXTURES, name), encoding="utf-8") as fh:
        return json.load(fh)


def build_asset_manifest() -> dict:
    out: dict[str, dict] = {}
    root = os.path.join(BUILD, "assets", "img")
    for cat in IMG_CATEGORIES:
        d = os.path.join(root, cat)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.startswith("."):
                continue
            size = image_size(os.path.join(d, f))
            out[f"assets/img/{cat}/{f}"] = {
                "category": cat,
                "width": size[0] if size else None,
                "height": size[1] if size else None,
            }
    return out


def build_pages_fixture() -> dict:
    out: dict[str, dict] = {}
    for p in PAGES:
        html = read(p)
        body = main_of(html)
        title = re.search(r"<title>(.*?)</title>", html, re.S)
        counters = re.findall(
            r"<b>(\d+)</b><span class=\"dna-frame__rule\"></span>(\d+)", html
        )
        out[p] = {
            "title": title.group(1).strip() if title else None,
            "h1_count": html.count("<h1"),
            "bands": len(re.findall(r'class="dna-band', body)),
            "frames": body.count("dna-frame__label"),
            "navy_bands": body.count("dna-band--navy"),
            "navy_panels": body.count("dna-panel--navy"),
            "counter_total": counters[0][1] if counters else None,
            "counter_steps": [int(n) for n, _ in counters],
        }
    return out


def refresh() -> None:
    os.makedirs(FIXTURES, exist_ok=True)
    for name, data in (
        ("asset_manifest.json", build_asset_manifest()),
        ("pages.json", build_pages_fixture()),
    ):
        path = os.path.join(FIXTURES, name)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print("wrote", os.path.relpath(path, TEST_DIR), f"({len(data)} entries)")


if __name__ == "__main__":
    if "--refresh" in sys.argv:
        refresh()
    else:
        print(__doc__)
        print(f"build dir: {BUILD}")
        print(f"pages:     {len(PAGES)}")
