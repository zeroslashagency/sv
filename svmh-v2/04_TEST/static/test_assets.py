"""Assets: every reference resolves, dimensions are truthful, nothing upscales.

This is the suite that catches the bug that actually shipped twice during the
build: a page pointing at an asset that was never produced, and a cut-out
declared larger than its own source pixels.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conftest import (  # noqa: E402
    BUILD, IMG_CATEGORIES, PAGES, Result, image_size, load_fixture, read,
    refs, resolve,
)


def run() -> int:
    r = Result("assets")
    manifest = load_fixture("asset_manifest.json")

    # 1. Every asset reference resolves on disk. Asset means something the page
    #    loads (image, stylesheet, script, document) -- not an internal route to
    #    a page that has not been built yet. Those are counted separately in
    #    test_links.py, because an unbuilt page is a roadmap item and a missing
    #    image is a rendering bug.
    for page in PAGES:
        html = read(page)
        for ref in sorted(set(refs(html))):
            if not ref.lower().endswith(
                    (".jpg", ".jpeg", ".png", ".webp", ".svg", ".gif",
                     ".css", ".js", ".pdf", ".ico", ".woff", ".woff2")):
                continue
            path = resolve(page, ref)
            r.check(os.path.isfile(path), f"{page}: {ref} exists",
                    f"resolved to {path}")

    # 2. Declared width/height match the real pixels. A wrong pair either
    #    stretches the photo or causes layout shift.
    for page in PAGES:
        html = read(page)
        for tag in re.findall(r"<img\b[^>]*>", html):
            src = re.search(r'src="([^"]+)"', tag)
            w = re.search(r'width="(\d+)"', tag)
            h = re.search(r'height="(\d+)"', tag)
            if not src:
                continue
            path = resolve(page, src.group(1))
            if not os.path.isfile(path):
                continue
            name = os.path.basename(src.group(1))
            r.check(bool(w and h), f"{page}: {name} declares width and height")
            real = image_size(path)
            if real and w and h:
                r.check((int(w.group(1)), int(h.group(1))) == real,
                        f"{page}: {name} dimensions are truthful",
                        f"declared {w.group(1)}x{h.group(1)}, real {real[0]}x{real[1]}")

    # 3. Alt text on every image; empty alt only for decorative.
    for page in PAGES:
        html = read(page)
        for tag in re.findall(r"<img\b[^>]*>", html):
            name = re.search(r'src="([^"]+)"', tag)
            label = os.path.basename(name.group(1)) if name else "img"
            has_alt = 'alt="' in tag
            meaningful = re.search(r'alt="([^"]{8,})"', tag)
            r.check(has_alt, f"{page}: {label} has an alt attribute")
            r.check(bool(meaningful) or 'alt=""' in tag,
                    f"{page}: {label} alt is descriptive or explicitly empty")

    # 4. Lazy-loading discipline: the first image on a page is eager, the rest
    #    are lazy, or the page pays for offscreen work on first paint.
    for page in PAGES:
        tags = re.findall(r"<img\b[^>]*>", read(page))
        if not tags:
            continue
        r.check("loading=\"lazy\"" not in tags[0],
                f"{page}: first image is not lazy")
        rest = tags[1:]
        eager = [t for t in rest if 'loading="lazy"' not in t]
        r.check(not eager, f"{page}: all later images are lazy",
                f"{len(eager)} eager image(s) below the fold")

    # 5. Every asset on disk sits in a known category folder, and the manifest
    #    matches disk. An asset in the wrong folder is a misuse waiting to happen.
    # Documentation is welcome at the root of assets/img; an image is not,
    # because a loose image has no declared role.
    root = os.path.join(BUILD, "assets", "img")
    stray = [f for f in os.listdir(root)
             if not f.startswith(".")
             and not os.path.isdir(os.path.join(root, f))
             and not f.endswith(".md")]
    r.check(not stray, "no loose images directly in assets/img", f"stray: {stray}")
    r.check(os.path.isfile(os.path.join(root, "README.md")),
            "assets/img documents its categories")

    on_disk = set()
    for cat in IMG_CATEGORIES:
        d = os.path.join(root, cat)
        if os.path.isdir(d):
            on_disk |= {f"assets/img/{cat}/{f}" for f in os.listdir(d)
                        if not f.startswith(".")}
    r.check(on_disk == set(manifest), "asset manifest matches disk",
            f"only on disk: {sorted(on_disk - set(manifest))}; "
            f"only in manifest: {sorted(set(manifest) - on_disk)}")

    # 6. Unplaced assets are reported, not failed: the pipeline makes some
    #    frames ahead of the pages that will use them. Documented in
    #    assets/img/README.md, which must list every one so none is forgotten.
    used: set[str] = set()
    for page in PAGES:
        html = read(page)
        used |= {os.path.basename(x) for x in re.findall(r'src="([^"]+)"', html)}
    unplaced = sorted(os.path.basename(k) for k in manifest
                      if os.path.basename(k) not in used)
    doc = ""
    doc_path = os.path.join(BUILD, "assets", "img", "README.md")
    if os.path.isfile(doc_path):
        with open(doc_path, encoding="utf-8") as fh:
            doc = fh.read()
    # Must be listed in the "Produced but not yet placed" table specifically,
    # not merely mentioned somewhere in the file -- otherwise any filename that
    # appears in prose satisfies the check.
    table = doc.split("## Produced but not yet placed", 1)[-1].split("\n##", 1)[0]
    undocumented = [f for f in unplaced if f not in table]
    r.check(not undocumented,
            f"{len(unplaced)} unplaced asset(s), all documented",
            f"missing from assets/img/README.md: {undocumented}")

    # 7. Cut-outs are the one category that must never be upscaled, so the CSS
    #    has to cap the widest one. Check the cap exists and names a real width.
    css = read("assets/css/dna.css")
    caps = re.findall(r"--stage-sm\s*\{[^}]*?min\(\s*[\d.]+vw\s*,\s*(\d+)px", css, re.S)
    cut = {os.path.basename(k): v for k, v in manifest.items()
           if v["category"] == "cutouts"}
    widths = {v["width"] for v in cut.values()}
    r.check(bool(caps), "dna.css caps the small stage cut-out width")
    if caps:
        r.check(int(caps[0]) in widths,
                "the cap equals a real cut-out width",
                f"cap {caps[0]}px, cut-out widths {sorted(widths)}")

    return r.report()


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
