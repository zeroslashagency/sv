#!/usr/bin/env python3
"""
SVMH asset pipeline.

Turns the real plant photography in ../assets/company into the build assets the
DNA grammar needs:
  * S2 cut-outs  -> transparent PNG, background flood-filled away
  * media / hero -> 4:3 (and 3:2) JPEGs, centre-weighted crop, LANCZOS

No generated imagery. Every output traces to one source frame.
"""
import os
from PIL import Image
import numpy as np
from scipy import ndimage

# Paths are derived from this file's location, so the script runs from anywhere
# and survives the project being moved or cloned.
HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)                 # svmh-v2/
SRC = os.path.normpath(os.path.join(PROJECT, "..", "assets", "company"))
OUT = os.path.join(PROJECT, "03_BUILD", "assets", "img")

# Assets are filed by the role they play in the DNA grammar, matching the
# subfolders 04_TEST/static/test_assets.py enforces. A destination is written
# "category/name.ext"; the category folder is created on demand.
CATEGORIES = ("cutouts", "bands", "cards", "people")
for _cat in CATEGORIES:
    os.makedirs(os.path.join(OUT, _cat), exist_ok=True)


def dest(rel):
    """Resolve 'cards/foo.jpg' under OUT, refusing an uncategorised name."""
    cat = rel.split("/")[0] if "/" in rel else None
    if cat not in CATEGORIES:
        raise ValueError(
            f"'{rel}' needs a category prefix, one of {CATEGORIES}. "
            "Flat writes into assets/img are rejected on purpose."
        )
    return os.path.join(OUT, rel)


def crop_to(im, ratio, anchor=0.5):
    """Centre-weighted crop to `ratio` (w/h). anchor = vertical focus 0..1."""
    w, h = im.size
    target = ratio
    cur = w / h
    if cur > target:                      # too wide -> trim sides
        nw = int(round(h * target))
        x = (w - nw) // 2
        box = (x, 0, x + nw, h)
    else:                                 # too tall -> trim top/bottom
        nh = int(round(w / target))
        y = int(round((h - nh) * anchor))
        y = max(0, min(y, h - nh))
        box = (0, y, w, y + nh)
    return im.crop(box)


def photo(src, dst, size, ratio, anchor=0.5, quality=86):
    im = Image.open(os.path.join(SRC, src)).convert("RGB")
    im = crop_to(im, ratio, anchor)
    im = im.resize(size, Image.LANCZOS)
    p = dest(dst)
    im.save(p, "JPEG", quality=quality, optimize=True, progressive=True)
    print("photo  %-42s %s  <- %s" % (dst, im.size, src))


def keyout(src, dst, mode, tol, max_w=1400, feather=1):
    """
    Flood-fill the background from the frame border and write a transparent PNG.
    mode 'light' keys a bright flat sky, 'dark' keys a black studio backdrop.
    """
    im = Image.open(os.path.join(SRC, src)).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    h, w = a.shape[:2]

    if mode == "light":
        # seed colour = median of the top strip (the sky)
        seed = np.median(a[: max(4, h // 20)].reshape(-1, 3), axis=0)
    else:
        seed = np.array([0, 0, 0])

    dist = np.sqrt(((a - seed) ** 2).sum(axis=2))
    cand = dist < tol

    # keep only background connected to the frame edge
    lab, n = ndimage.label(cand)
    edge = set(lab[0].tolist()) | set(lab[-1].tolist())
    edge |= set(lab[:, 0].tolist()) | set(lab[:, -1].tolist())
    edge.discard(0)
    bg = np.isin(lab, list(edge))

    # close pinholes inside the subject, then drop specks
    fg = ~bg
    fg = ndimage.binary_closing(fg, structure=np.ones((3, 3)), iterations=2)
    fg = ndimage.binary_fill_holes(fg)
    lab2, n2 = ndimage.label(fg)
    if n2:
        sizes = ndimage.sum(fg, lab2, range(1, n2 + 1))
        keep = [i + 1 for i, s in enumerate(sizes) if s > 0.004 * h * w]
        fg = np.isin(lab2, keep)

    alpha = (fg * 255).astype(np.uint8)
    if feather:
        alpha = ndimage.uniform_filter(alpha, size=2 * feather + 1)
        alpha = np.where(fg, np.maximum(alpha, 160), alpha).astype(np.uint8)

    rgba = np.dstack([np.asarray(im), alpha])
    out = Image.fromarray(rgba, "RGBA")

    ys, xs = np.nonzero(alpha > 8)
    if len(xs):
        pad = 2
        out = out.crop((max(0, xs.min() - pad), max(0, ys.min() - pad),
                        min(w, xs.max() + pad), min(h, ys.max() + pad)))
    if out.width > max_w:
        out = out.resize((max_w, int(round(out.height * max_w / out.width))),
                         Image.LANCZOS)
    p = dest(dst)
    out.save(p, "PNG", optimize=True)
    cov = (alpha > 8).mean()
    print("cutout %-42s %s  subject %.0f%%  <- %s" % (dst, out.size, cov * 100, src))


# ---------------------------------------------------------------- cut-outs (S2)
# OWNED BY make_cutouts.py. The border-connected flood fill below could not
# isolate an outdoor subject (it kept the dirt apron, grass and a background
# crawler crane), so cut-outs moved to chroma masking in make_cutouts.py.
# Left here disabled so this script never clobbers the tuned PNGs.
#   keyout("pdf1-img-118.png", "cutouts/cutout-goliath-gantry.png", "light", 62)
#   keyout("pdf2-img-003.jpg", "cutouts/cutout-crab-unit.png", "dark", 70)

# ------------------------------------------------------------- hero + wide bands
# goliath lifting a segment mould, workers in hi-vis: the "real load" frame.
# NOTE: 117 is the loaded goliath, 119 is the empty green-floor bay. An earlier
# revision had these two reversed; verified against the source frames.
photo("pdf1-img-117.png", "bands/hero-goliath-lifting-load.jpg", (1440, 960), 3 / 2, 0.45)
photo("pdf1-img-117.png", "bands/band-goliath-lifting-load.jpg", (1600, 800), 2 / 1, 0.42)
# fabrication bay with a yellow EOT overhead
photo("pdf3-img-042.png", "bands/band-fabrication-bay-eot.jpg", (1600, 800), 2 / 1, 0.5)

# ------------------------------------------------------------------- media cards
# single-girder EOT spanning an empty finished bay
photo("pdf1-img-119.png", "cards/eot-single-girder-bay.jpg", (960, 720), 4 / 3, 0.5)
photo("pdf3-img-042.png", "cards/fabrication-bay-eot.jpg", (960, 720), 4 / 3, 0.5)
photo("pdf3-img-102.png", "cards/ladle-carrier-frame.jpg", (960, 720), 4 / 3, 0.45)
photo("pdf3-img-074.png", "cards/structural-steel-bay.jpg", (960, 720), 4 / 3, 0.5)
photo("pdf3-img-058.png", "cards/fabricated-chute-assembly.jpg", (960, 720), 4 / 3, 0.5)
photo("pdf3-img-126.png", "cards/crated-dispatch.jpg", (960, 720), 4 / 3, 0.5)
photo("pdf3-img-128.png", "cards/crated-dispatch-2.jpg", (960, 720), 4 / 3, 0.5)
photo("pdf3-img-120.png", "cards/gearbox-primed.jpg", (960, 720), 4 / 3, 0.5)
photo("pdf3-img-088.png", "cards/shop-enclosure-under-eot.jpg", (960, 720), 4 / 3, 0.5)

# ------------------------------------------------------------------------ company
photo("pdf1-img-016.jpg", "people/md-umapathi-portrait.jpg", (720, 900), 4 / 5, 0.25)

print("\ndone ->", OUT)
