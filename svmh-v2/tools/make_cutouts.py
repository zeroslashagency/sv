#!/usr/bin/env python3
"""
Second-pass cut-outs.

The border flood-fill worked for the studio-black crab frame but not for the
outdoor gantry: keying the sky leaves the ground, trees and the crawler crane
behind. Machine paint is the reliable signal outdoors, so the gantry is masked
on yellow chroma instead, then cleaned morphologically.
"""
import os
from PIL import Image
import numpy as np
from scipy import ndimage

# Paths derive from this file's location so the script runs from anywhere.
HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)
SRC = os.path.normpath(os.path.join(PROJECT, "..", "assets", "company"))
# Cut-outs are their own category in the build: transparent PNGs used by S2.
OUT = os.path.join(PROJECT, "03_BUILD", "assets", "img", "cutouts")
os.makedirs(OUT, exist_ok=True)


def clean(mask, h, w, min_frac=0.01, close=3, keep=1):
    m = ndimage.binary_closing(mask, np.ones((close, close)), iterations=2)
    lab, n = ndimage.label(m)
    if not n:
        return m
    sizes = ndimage.sum(m, lab, range(1, n + 1))
    order = np.argsort(sizes)[::-1]
    idx = [int(order[i]) + 1 for i in range(min(keep, len(order)))
           if sizes[order[i]] > min_frac * h * w]
    return np.isin(lab, idx) if idx else m


def write(im, alpha, dst, max_w=1400, pad=2):
    h, w = alpha.shape
    a = ndimage.uniform_filter(alpha, size=3)
    a = np.where(alpha > 0, np.maximum(a, 200), a).astype(np.uint8)
    out = Image.fromarray(np.dstack([np.asarray(im), a]), "RGBA")
    ys, xs = np.nonzero(a > 8)
    out = out.crop((max(0, xs.min() - pad), max(0, ys.min() - pad),
                    min(w, xs.max() + pad), min(h, ys.max() + pad)))
    if out.width > max_w:
        out = out.resize((max_w, round(out.height * max_w / out.width)), Image.LANCZOS)
    out.save(os.path.join(OUT, dst), "PNG", optimize=True)
    print("%-32s %s  subject %.0f%%" % (dst, out.size, (a > 8).mean() * 100))


# ------------------------------------------------- goliath gantry: yellow chroma
im = Image.open(os.path.join(SRC, "pdf1-img-118.png")).convert("RGB")
a = np.asarray(im).astype(np.int16)
R, G, B = a[..., 0], a[..., 1], a[..., 2]
h, w = R.shape
# Measured on the source: machine paint sits at R-B ~= 210 with B < 50, while
# the dirt/grass foreground that also reads warm tops out around R-B ~= 100.
yellow = (R > 120) & (R - B > 130) & (G - B > 70) & (B < 95)
mask = clean(yellow, h, w, min_frac=0.02, close=3, keep=1)
# close only pinholes in the paint: filling every hole would glue the sky back
# into the portal opening under the girder.
holes = ndimage.binary_fill_holes(mask) & ~mask
lab_h, nh = ndimage.label(holes)
if nh:
    hsz = ndimage.sum(holes, lab_h, range(1, nh + 1))
    small = [i + 1 for i, s in enumerate(hsz) if s < 0.0015 * h * w]
    mask |= np.isin(lab_h, small)
mask = clean(mask, h, w, min_frac=0.02, keep=1)

# Grow back the shaded / sun-bleached paint the strict test dropped, but only
# where it touches the confirmed structure and stays clear of the dirt apron.
loose = (R > 100) & (R - B > 85) & (G - B > 45) & (B < 140)
loose[int(0.86 * h):] = False
grown = mask.copy()
for _ in range(14):
    grown = ndimage.binary_dilation(grown, np.ones((3, 3))) & (loose | mask)
mask = clean(grown | mask, h, w, min_frac=0.02, keep=1)
holes = ndimage.binary_fill_holes(mask) & ~mask
lab_h, nh = ndimage.label(holes)
if nh:
    hsz = ndimage.sum(holes, lab_h, range(1, nh + 1))
    mask |= np.isin(lab_h, [i + 1 for i, s in enumerate(hsz) if s < 0.0015 * h * w])
write(im, (mask * 255).astype(np.uint8), "cutout-goliath-gantry.png")

# ------------------------------------- crab unit: black backdrop, voids kept open
im = Image.open(os.path.join(SRC, "pdf2-img-003.jpg")).convert("RGB")
a = np.asarray(im).astype(np.int16)
h, w = a.shape[:2]
dark = np.sqrt((a ** 2).sum(axis=2)) < 78
lab, n = ndimage.label(dark)
edge = set(lab[0].tolist()) | set(lab[-1].tolist()) | set(lab[:, 0].tolist()) | set(lab[:, -1].tolist())
edge.discard(0)
bg = np.isin(lab, list(edge))          # only backdrop touching the frame edge
fg = ndimage.binary_closing(~bg, np.ones((3, 3)))
fg = clean(fg, h, w, min_frac=0.004, keep=2)   # frame + the loose side panel
write(im, (fg * 255).astype(np.uint8), "cutout-crab-unit.png")

for n_ in ("cutout-goliath-gantry.png", "cutout-crab-unit.png"):
    p = Image.open(os.path.join(OUT, n_)).convert("RGBA")
    p.thumbnail((700, 700))
    bgim = Image.new("RGB", (p.width + 40, p.height + 40), (239, 239, 239))
    bgim.paste(p, (20, 20), p)
    bgim.save("/tmp/chk_" + n_)
