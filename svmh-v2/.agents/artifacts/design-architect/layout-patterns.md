# SVMH v2 — Layout Pattern Library

**Owner:** Design Architect (Agent A / T001)
**Status:** Binding for page builders
**Source:** 16 reference boards in `refer/` (indexed in `01_DESIGN/refboards/REFERENCE_DISTILLATION.md`), resolved against the shipped grid in `03_BUILD/assets/css/base.css`.

Every pattern below is implementable **today** with the existing primitives. Each pattern names the reference board it came from, the markup skeleton, and its responsive collapse.

---

## 1. The grid system as shipped

```
.container            max-width: calc(1240px + (var(--gutter) * 2))
.container--narrow    max-width: calc(880px  + (var(--gutter) * 2))
.container--wide      max-width: calc(1600px + (var(--gutter) * 2))
                      inline padding: var(--gutter)  → clamp(20px, 4vw, 40px)

.grid                 1 column below 768px
                      repeat(12, minmax(0,1fr)) at ≥768px
                      gap: var(--grid-gap) → clamp(16px, 2vw, 32px)
.col-1 … .col-12      span N, active ≥768px
.col-start-2/3/6/7/8  explicit column start, ≥768px

.grid--7-5 / --5-7    7fr / 5fr,  resolves at ≥1024px
.grid--8-4 / --4-8    8fr / 4fr,  resolves at ≥1024px
.grid--6-6            equal halves, ≥1024px
.grid--cards          1 col → 2 @640px → 3 @1024px
```

Two ways to place content, and only two:

1. **Named split** (`.grid--7-5` etc.) for two-column editorial compositions. Preferred — it is self-documenting and its collapse is already tuned.
2. **12-column spans** (`.col-N` + `.col-start-N`) for anything asymmetric or offset.

Do not mix both on the same `.grid`.

### Breakpoint ladder

| Token | px | What changes |
|---|---|---|
| — | 360 | Baseline. Single column everywhere. Minimum supported width. |
| `--bp-sm` | 480 | Nothing structural. Type/space clamps grow. |
| `--bp-md` | 768 | 12-col grid activates. `.col-*` spans apply. `.mobile-bar` hides. Card padding steps up to `--space-6`. |
| `--bp-lg` | 1024 | Named splits resolve. `.nav__menu` replaces `.nav__toggle`. `.hero__grid` goes 7/5. `.band__head` bottom margin → `--space-8`. |
| `--bp-xl` | 1280 | `.container` at max. Clamp maxima approached. |
| `--bp-xxl` | 1600 | `--container--wide` at max. All clamps at maximum. No further change to 1920+. |

Between 1600 and 1920 the page **must not grow** — content is capped and the concrete field extends. Verify at 1920 that no band stretches its text past 68ch.

---

## 2. Pattern catalogue

### L1 — Asymmetric hero split
**Board:** `IMG_6831` (crane boom + condensed display type), `IMG_6827` (huge sentence-case display)
**Use:** every page opener.

```html
<section class="hero" id="hero" aria-labelledby="hero-h">
  <div class="container hero__grid">
    <div class="hero__body">
      <p class="hero__eyebrow">Manufacturer · Harohalli KIADB · Since 2006</p>
      <h1 class="hero__title" id="hero-h">EOT and gantry cranes built to IS 807</h1>
      <p class="hero__lead measure">…</p>
      <dl class="hero__specs">…</dl>
      <div class="hero__actions">…</div>
    </div>
    <figure class="hero__media">
      <img src="…" width="1200" height="900" alt="…">
      <figcaption class="hero__media-caption">Double-girder EOT · 80 T · 22 m span · M7 duty</figcaption>
    </figure>
  </div>
</section>
```

Responsive: 7fr/5fr at ≥1024px with `gap: clamp(32px,5vw,96px)`; below that the body stacks above the media. On mobile the image keeps its intrinsic ratio and is never cropped to a letterbox.

### L2 — Ink/light intro split
**Board:** `IMG_6826` (navy 55% / light 45%, label + 3-line paragraph only)
**Use:** the first content band after the hero, on product and industry pages.

```html
<section class="band band--ink" id="intro" aria-labelledby="intro-h">
  <div class="container">
    <div class="grid grid--7-5">
      <div class="stack">
        <p class="eyebrow eyebrow--rule">What we make</p>
        <h2 class="t-display-l" id="intro-h">Cranes specified from your load cycle, not a catalogue page</h2>
      </div>
      <p class="t-lead measure">Three sentences maximum. Restraint is the pattern — the reference boards put a single short paragraph opposite the heading and let the band padding do the work.</p>
    </div>
  </div>
</section>
```

Rule from the board: this composition carries **only** a label, a heading and one short paragraph. Adding cards, stats or lists to it destroys the pattern. Collapses to a single column below 1024px, heading first.

### L3 — Alternating capability rows
**Board:** `IMG_6822`, `IMG_6817`
**Use:** capability, process-detail and application sections with 2–4 entries.

```html
<section class="band" id="capability" aria-labelledby="capability-h">
  <div class="container">
    <div class="band__head">
      <p class="eyebrow eyebrow--rule">Capability</p>
      <h2 class="t-display-l" id="capability-h">Design, fabrication and testing under one roof</h2>
    </div>

    <div class="stack stack--lg">
      <div class="grid grid--7-5 reveal">
        <div class="stack">…text…</div>
        <figure class="card__media">…image…</figure>
      </div>
      <div class="grid grid--5-7 reveal">
        <figure class="card__media">…image…</figure>
        <div class="stack">…text…</div>
      </div>
    </div>
  </div>
</section>
```

Alternate `--7-5` / `--5-7` per row. Below 1024px **every** row stacks text-first — do not let the image lead on mobile, because the reading order would flip between rows.

### L4 — Card grid
**Board:** `IMG_6819`, `IMG_6821` (4-up rental cards), `IMG_6822` (3×2 category cards)
**Use:** product listings, "three doors", industries, resources.

```html
<div class="grid grid--cards">
  <article class="card card--product">
    <p class="card__index">01</p>
    <figure class="card__media"><img src="…" width="900" height="600" alt="…"></figure>
    <h3 class="card__title"><a class="card__link" href="/eot-cranes/double-girder">Double-girder EOT</a></h3>
    <p class="card__text">…</p>
    <div class="card__foot"><span class="card__spec">5 – 100+ T · M5 – M8</span></div>
  </article>
  …
</div>
```

Responsive: 1 → 2 @640px → 3 @1024px. Four-up is **not** supported and must not be forced with `.col-3` — the reference 4-up boards used ~200px cards which fail our type scale. For 4 items, use 3-up and let the fourth wrap; for 6 items, 3×2 lands cleanly.

Board detail adopted: the hairline above the spec row (`.card__foot`), the mono spec line, and the bottom-pinned foot so cards of unequal text length still align. Board detail rejected: the "flooded accent" hover card — our hover is border + title colour + 1px lift only.

### L5 — Floating panel over media
**Board:** `IMG_6822` (white container over blurred site photo)
**Use:** once per page maximum, for a proof or positioning statement.

```html
<section class="band band--flush-bottom" id="proof-media" aria-hidden="false">
  <figure class="hero__media hero__media--overlay">
    <img src="…" width="1600" height="900" alt="…">
  </figure>
</section>
<section class="band band--white band--tight hairline-top" id="proof" aria-labelledby="proof-h">
  <div class="container container--narrow stack">
    <p class="eyebrow eyebrow--rule">Since 2006</p>
    <h2 class="t-display-l" id="proof-h">…</h2>
    <p class="t-lead measure">…</p>
  </div>
</section>
```

Until `.panel--float` ships (see `component-architecture.md` §3) implement it as the flush image band + white band pair above. The overlap effect is optional polish, not a requirement. `--elevation-card` is the only shadow permitted; the dashed connector and callout tag from the board are **not** adopted (mixed decoration).

### L6 — Numbered index list + process chips
**Board:** `IMG_6817` (01–06 accordion with +/− expanders), `IMG_6827` (`01 Air / 02 Sea` hairline cells)
**Use:** process, FAQ, "what happens next".

```html
<section class="band" id="process" aria-labelledby="process-h">
  <div class="container">
    <div class="band__head">
      <p class="eyebrow eyebrow--rule">How a crane gets built</p>
      <h2 class="t-display-l" id="process-h">Six stages, each with something you can check</h2>
    </div>

    <ul class="chips">
      <li class="chips__item"><span class="chips__label"><span class="chips__num">01</span> Enquiry</span></li>
      …
    </ul>

    <div class="index-list">
      <div class="index-row">
        <h3><button class="index-row__trigger" type="button" aria-expanded="false" aria-controls="p-01">
          <span class="index-row__num">01</span>
          <span class="index-row__label">Enquiry and load study</span>
          <span class="index-row__icon" aria-hidden="true"></span>
        </button></h3>
        <div class="index-row__panel" id="p-01">
          <p class="t-body measure">…</p>
        </div>
      </div>
      …
    </div>
  </div>
</section>
```

The chip row and the index list mirror the same numbering — that pairing is the board's device for showing the whole process at a glance before the detail. Chips scroll horizontally below 768px (no wrap-to-two-lines). Panels ship visible.

Board detail rejected: the horizontal numbered product **carousel** with ←/→ arrows. Carousels hide content and are a stated rejection in the distillation.

### L7 — Stat band
**Board:** `IMG_6820` (giant knockout numerals with small stacked captions)
**Use:** once per page, proof of scale.

```html
<section class="band band--ink" id="numbers" aria-labelledby="numbers-h">
  <div class="container">
    <div class="band__head">
      <p class="eyebrow eyebrow--rule">By the numbers</p>
      <h2 class="t-display-l" id="numbers-h">What the works has done since 2006</h2>
    </div>
    <div class="stat-grid reveal reveal--stagger">
      <div class="stat">
        <p class="stat__value" data-count-to="100">100<span class="stat__unit">T +</span></p>
        <p class="stat__caption">Max capacity, double-girder EOT</p>
      </div>
      …
    </div>
  </div>
</section>
```

Grid: 2-up at 360–767px, 4-up at ≥768px. Numerals weight 300, captions `.t-body-s`. At most one `.stat--accent` (outline) per page and only here.

### L8 — Spec table
**Board:** `IMG_6826` (mono technical rows), plus every industrial reference's data block.

```html
<div class="spec-table-wrap">
  <table class="spec-table spec-table--leader">
    <caption class="sr-only">Capacity and duty class by crane type</caption>
    <thead>
      <tr><th scope="col">Type</th><th scope="col">Capacity</th><th scope="col">Span</th><th scope="col">Duty</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">Single-girder EOT</th><td>1 – 15 T</td><td>up to 25 m</td><td>M3 – M6</td></tr>
    </tbody>
  </table>
</div>
<p class="spec-table__note">Deflection limits per IS 807. Duty class per IS 3177.</p>
```

Responsive: the wrapper scrolls horizontally below the table's natural width, with `--elevation-float` as the scroll affordance. Columns are never dropped or stacked into definition lists — engineers compare across rows.

### L9 — Nav-as-grid
**Board:** `IMG_6827` (1px dividers, right-most accent cell)
Already shipped in `.nav`: brand cell, link cells, CTA cell, all separated by hairlines. Builders reproduce the header markup verbatim across pages; the only per-page change is `aria-current="page"`.

### L10 — Full-bleed product stage
**Board:** `IMG_6826` (machine centred on a light field, mono label, `01 — 03` counter)
**Use:** product detail pages, one per page.

```html
<section class="band band--concrete-2 band--tight" id="stage" aria-labelledby="stage-h">
  <div class="container container--wide">
    <h2 class="sr-only" id="stage-h">Double-girder EOT crane, 80 T</h2>
    <figure class="card__media">
      <img src="…" width="1600" height="1000" alt="…">
      <figcaption class="hero__media-caption"><span class="spec">80 T · 22 m span · M7</span></figcaption>
    </figure>
  </div>
</section>
```

This is where the cool-neutral reading of the references is honoured: `--color-concrete-2` / `--concrete-3` give the flat photographic stage the board shows, without swapping the site palette. Zero radius, zero shadow. Until `.stage` ships, the markup above is the pattern.

### L11 — Footer as index
Shipped `.footer__grid`: brand + NAP column, then 3–4 link columns, then a legal row. Collapses to a single column below 768px with the brand block first. NAP text must byte-match the JSON-LD address.

---

## 3. Responsive behaviour rules

1. **360px is the design floor.** Test at 360, 390, 414. No horizontal scroll on `<body>` at any width; the only horizontally scrolling elements are `.spec-table-wrap`, `.compare-table-wrap` and `.chips`.
2. **Text-first stacking.** When a two-column split collapses, the text column comes first, every time, regardless of DOM order at desktop. Use `order` in CSS (already handled in the shipped splits) rather than reordering markup per row.
3. **Reading order = DOM order.** Never use `.col-start-*` to visually move a block ahead of content that precedes it in the DOM.
4. **Images always carry `width` + `height`** so there is no layout shift; `aspect-ratio` handles the rendered box.
5. **Touch targets ≥44px** below 1024px — nav toggle, mobile bar items, accordion triggers, chip filters, buttons.
6. **`.mobile-bar` below 768px only**, `.nav__menu` at ≥1024px only. The 768–1023px band shows the toggle **and** no mobile bar: verify this range explicitly, it is the most-missed window.
7. **No `vw`-based padding on components** — only `--band-y`, `--gutter`, `--grid-gap` and the type clamps use viewport units.
8. **Reduced motion:** `.reveal` resolves to `.is-visible` immediately, count-ups jump to final value, hover transitions drop to 0. Nothing depends on motion to become readable.

## 4. Layout QA checklist

- [ ] 360 / 480 / 768 / 1024 / 1280 / 1600 / 1920 all checked.
- [ ] No horizontal `<body>` scroll at any of those widths.
- [ ] 768–1023px window verified (toggle nav, 2-up cards, splits still stacked).
- [ ] Splits collapse text-first.
- [ ] Card grids are 1/2/3 — never a forced 4-up.
- [ ] Tables scroll in their wrapper, columns intact.
- [ ] Chips scroll horizontally on mobile, no second row.
- [ ] Every band has `id` + `aria-labelledby`.
- [ ] Max two colour bands; alternating rhythm carried by `--band-y` whitespace.
- [ ] Nothing above `--radius-md`; no shadows beyond `--elevation-card` (+ table affordance).
- [ ] 1920px: content capped, no line beyond 68ch, concrete field extends cleanly.
