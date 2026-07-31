# render/ — browser checks

These are not self-running, and the honest reason is that they need a real
layout engine. Collision, paint order, lazy-load behaviour and "does this
actually look like the reference" cannot be asserted from the file on disk. The
static suite covers everything that can be; this covers the rest.

Driven through the chrome-devtools MCP tools from an agent session, or by hand
in a browser.

## Setup

```bash
cd ../../03_BUILD && python3 -m http.server 8080
```

## Procedure

1. `chrome-devtools__list_pages`, then `navigate_page` to
   `http://localhost:8080/index.html`.
2. For each width in `viewport_matrix.md`, `resize_page` and run the probe
   below. Repeat for all four pages.
3. Record anything that fails in `../reports/render-<date>.md`.

## The probe

One `evaluate_script` call returns every measurement at once:

```js
async () => {
  window.scrollTo(0, document.body.scrollHeight);
  await new Promise(r => setTimeout(r, 2500));
  const main = document.querySelector('main');
  return {
    width: innerWidth,
    hscroll: document.documentElement.scrollWidth > innerWidth + 1,
    overflow: [...main.querySelectorAll('*')]
      .filter(e => { const b = e.getBoundingClientRect();
                     return b.width > 0 && b.right > innerWidth + 1; })
      .map(e => (e.className || e.tagName).toString().slice(0, 30)),
    frameOverlap: [...main.querySelectorAll('.dna-band')]
      .map((b, i) => {
        const f = b.querySelector('.dna-frame'), h = b.querySelector('h1,h2');
        if (!f || !h) return null;
        const fr = f.getBoundingClientRect(), hr = h.getBoundingClientRect();
        return (hr.top < fr.bottom + 2 && hr.bottom > fr.top - 2) ? i : null;
      }).filter(x => x !== null),
    brokenImages: [...document.images]
      .filter(i => !i.complete || i.naturalWidth === 0)
      .map(i => i.src.split('/').pop()),
    upscaled: [...document.images]
      .filter(i => i.naturalWidth &&
                   i.getBoundingClientRect().width > i.naturalWidth + 1)
      .map(i => i.src.split('/').pop()),
    radii: [...main.querySelectorAll('*')]
      .filter(e => getComputedStyle(e).borderRadius !== '0px').length,
    borders: [...main.querySelectorAll('*')]
      .filter(e => { const s = getComputedStyle(e);
                     return s.borderTopWidth !== '0px' &&
                            s.borderTopStyle !== 'none' &&
                            s.borderTopColor !== 'rgba(0, 0, 0, 0)'; })
      .map(e => (e.className || e.tagName).toString().slice(0, 30)),
    tableClip: [...main.querySelectorAll('.spec-table-wrap')]
      .filter(w => w.scrollWidth > w.clientWidth + 1).length
  };
}
```

## Pass criteria

| Field | Must be |
|---|---|
| `hscroll` | `false` at every width |
| `overflow` | empty |
| `frameOverlap` | empty — an S3 label must never collide with a heading |
| `brokenImages` | empty after the full-page scroll |
| `upscaled` | empty — a cut-out painted wider than its source is visible mush |
| `radii` | `0` |
| `borders` | form controls only; never a band, panel, card or table cell |
| `tableClip` | `0` above 900px; a wide matrix may scroll below that |

## Known-good baseline

Recorded 2026-07-29 at 360 / 390 / 768 / 900 / 1440 / 1920 across all four
pages: every field above at its pass value, console clean, no failed requests.
Two caveats worth remembering when a run disagrees:

- The browser reports a minimum window width around 500px, so a 390px request
  may come back as `innerWidth: 500`. Use an offscreen iframe sized to the exact
  width when the number matters.
- Lazy images never load in an offscreen iframe, so `brokenImages` will list
  them. Check lazy loading on a real navigated page, not in the iframe harness.

## Screenshot workaround

`take_screenshot` payloads exceed the inline attachment cap and arrive
truncated. Read the saved MCP output file, split on `base64,`, decode, and
downscale before viewing. `../../tools/shotcut.py` does this:

```bash
python3 tools/shotcut.py              # newest image payload
python3 tools/shotcut.py --tile 1600  # also slice into vertical tiles
```
