# tools/ — build-time scripts

Scripts that produce or inspect build inputs. They are not part of the site:
`03_BUILD` ships without them, and nothing in the served output depends on them
at runtime.

They used to live in `.agents/artifacts/`, mixed in with agent working notes,
where it was not obvious that they own real files in the build. Rerunning one
from the wrong directory silently overwrote tuned assets once. Both now derive
their paths from their own location and refuse to write an uncategorised asset.

## Requirements

```bash
python3 -m pip install pillow numpy scipy
```

No ImageMagick. `magick` and `convert` are not installed on this machine, and
image generation APIs are not used — every asset traces to a real photograph in
`../../assets/company/`.

## make_assets.py

Crops and resizes the plant photography into the band and card images.

```bash
python3 tools/make_assets.py
```

- Reads `../../assets/company/pdf*-img-*.png|jpg`
- Writes `03_BUILD/assets/img/{bands,cards,people}/`
- Centre-weighted crop with a vertical anchor per photo, LANCZOS resize,
  progressive JPEG at quality 86

Its `keyout()` calls are **deliberately commented out**. The border-connected
flood fill it implements cannot isolate an outdoor subject — it kept the dirt
apron, the grass and a background crawler crane. Cut-outs are owned by
`make_cutouts.py`. Leaving the calls disabled rather than deleted preserves why.

## make_cutouts.py

Produces the two transparent S2 cut-outs.

```bash
python3 tools/make_cutouts.py
```

- Writes `03_BUILD/assets/img/cutouts/`
- **Gantry**: masked on yellow machine paint, not on the sky. Outdoors the paint
  is the only reliable signal. Strict chroma seed, morphological clean, then a
  constrained dilation into a looser band to recover the leg edges. Hole filling
  is size-bounded so the portal opening stays transparent.
- **Crab unit**: studio-black backdrop, so an edge-connected darkness key works.
  No hole filling — it would fill the gaps between the ropes.
- Writes a composite preview to `/tmp/chk_<name>.png` for eyeballing the mask.

The RuntimeWarning about `sqrt` is expected: the darkness test evaluates across
the whole frame including saturated pixels, and the resulting NaNs compare false,
which is the intended outcome.

## make_sitemap.py

Generates `03_BUILD/sitemap.xml` from the pages that exist on disk, taking each
URL from the page's own `<link rel="canonical">` so the two cannot disagree.

```bash
python3 tools/make_sitemap.py
```

Run it after adding or removing a page. `04_TEST/static/test_seo.py` fails if the
sitemap advertises a page that does not exist, omits one that does, or uses an
origin other than the canonical `https://www.svind.co.in`.

## Reproducibility

Both scripts are deterministic. Running them against an unchanged source set
reproduces byte-identical output — verified by checksum after the reorganisation.
If output changes without a source or parameter change, something else touched
the files.

## shotcut.py

Decodes a truncated chrome-devtools screenshot payload into a viewable image.
`take_screenshot` responses exceed the inline attachment cap, so the image
arrives corrupt; the payload is intact in the saved MCP output file.

```bash
python3 tools/shotcut.py                 # newest payload, downscaled to 1100px
python3 tools/shotcut.py --tile 1600     # also slice into vertical tiles
```
