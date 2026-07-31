# SVMH v2 — Typography & Spacing System

**Owner:** Design Architect (Agent A / T001)
**Status:** Binding for all page builders
**Authority chain:** `01_DESIGN/06_DESIGN_RECALIBRATION.md` → `03_BUILD/assets/css/tokens.css` → this document.
This document **does not introduce new values**. It documents the shipped tokens, tells builders exactly which class to reach for, and fills the two gaps the reference boards exposed (knockout display type, vertical rhythm between unequal bands).

Do not hard-code a `font-size`, `line-height`, `letter-spacing`, `margin` or `padding` in page HTML. Every value below already exists as a token or a utility class.

---

## 1. Families

| Token | Value | Use |
|---|---|---|
| `--font-sans` | `"Inter Tight", "Inter", system-ui, -apple-system, sans-serif` | Everything: display, lead, body, nav, buttons, captions |
| `--font-display` | `var(--font-sans)` | Alias only. There is **no** second display family. |
| `--font-mono` | `"IBM Plex Mono", ui-monospace, SFMono-Regular, monospace` | Specs, capacities, standard numbers, index numerals, table figures, eyebrows-with-codes |

Single-family rule (from `06_DESIGN_RECALIBRATION.md`): Inter Tight carries the voice; IBM Plex Mono is the *technical register only*. A mono word that is not a measurement, code, part number or index number is a defect.

Mono is applied via `.mono`, `.spec`, `.card__index`, `.index-row__num`, `.chips__num`, `.hero__spec-value`, `.eyebrow` and the table figure cells — builders should not add `font-family` anywhere.

## 2. Type scale (exact shipped values)

Every row is a token group in `tokens.css` and a utility class in `base.css`. Sizes are fluid `clamp()`; the min value is the 360px rendering and the max is reached at ≥1600px.

| Utility class | Size token | Min → Max | Weight | Line height | Tracking | Case |
|---|---|---|---|---|---|---|
| `.t-display-xxl` | `--text-display-xxl` | `2.5rem → 4.5rem` (`5.5vw`) | 600 | 1.04 | −0.025em | sentence |
| `.t-display-xl` | `--text-display-xl` | `2rem → 3.25rem` (`4vw`) | 600 | 1.08 | −0.022em | sentence |
| `.t-display-l` | `--text-display-l` | `1.5rem → 2.25rem` (`2.8vw`) | 600 | 1.16 | −0.018em | sentence |
| `.t-display-m` | `--text-display-m` | `1.125rem → 1.375rem` (`1.6vw`) | 600 | 1.28 | −0.01em | sentence |
| `.t-lead` | `--text-lead` | `1.0625rem → 1.3125rem` (`1.4vw`) | 400 | 1.55 | 0 | sentence |
| `.t-body` | `--text-body` | `0.9375rem` fixed | 400 | 1.62 | 0 | sentence |
| `.t-body-s` | `--text-body-s` | `0.875rem` fixed | 400 | 1.58 | 0 | sentence |
| `.eyebrow` | `--text-micro-caps` | `0.6875rem` fixed | 600 | 1.3 | +0.09em | UPPERCASE |
| `.spec` / `.mono` | `--text-spec-mono` | `0.8125rem` fixed | 400 | 1.5 | +0.01em | sentence |
| `.stat__value` | `--text-stat` | `2.25rem → 3.5rem` (`4vw`) | **300** | 1.0 | −0.03em | figures |
| `.index-row__num`, `.card__index` | `--text-index-numeral` | `1.75rem → 3rem` (`3vw`) | **300** | 1.0 | 0 | figures |

### Rules that are non-negotiable

1. **Sentence case for all display type.** No uppercase headlines. Uppercase exists only at `--text-micro-caps` (eyebrows, table headers, nav overlay labels).
2. **Display weight ceiling is 600.** Never 700/800. The premium read comes from tight tracking + generous whitespace, not weight.
3. **Numerals are light (300).** Stat and index numerals are thin against 600 headlines — that contrast *is* the editorial signature (see `IMG_6820`, `IMG_6826`).
4. **One `.t-display-xxl` per page**, and it is the `<h1>` (`.hero__title` already carries it). Section headings are `.t-display-l`; card/row titles are `.t-display-m`.
5. **Measure cap.** Any running paragraph gets `.measure` (`--max-text: 68ch`) or `.measure--tight`. A 1240px-wide paragraph is a defect.
6. **`font-feature-settings: "tnum"` is already on** `.spec-table`, `.compare-table` and `.stat__value` — do not re-declare; do not remove by overriding `font-variant-numeric`.

### Heading hierarchy contract per page

```
h1  .hero__title            → .t-display-xxl   (exactly one)
h2  .band__head heading     → .t-display-l     (one per band, id targeted by aria-labelledby)
h3  card / index-row title  → .t-display-m
h4  spec sub-group label    → .eyebrow (visually) but still a real heading element
```
Never skip a level to get a size. Size comes from the utility class; the element comes from document structure.

## 3. Spacing scale

`--space-0..11` = `0, 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 160` px. There are no intermediate values. If a gap "needs" 20px, it is 16 or 24.

| Range | Tokens | Purpose |
|---|---|---|
| Micro | `--space-1` … `--space-3` (4–12) | Label→value pairs, glyph offsets, chip padding |
| Component internal | `--space-4` … `--space-6` (16–32) | Card padding, stack gaps, form field spacing |
| Component separation | `--space-7`, `--space-8` (48, 64) | `band__head` → content, card grid rows |
| Section | `--space-9` … `--space-11` (96–160) | Reserved; prefer `--band-y` |

### Section rhythm

| Token | Value | Where |
|---|---|---|
| `--band-y` | `clamp(96px, 11vw, 180px)` | Default `.band` `padding-block` |
| `--band-y-tight` | `clamp(40px, 5vw, 72px)` | `.band--tight` — trust strips, chip rows, breadcrumb bands, logo strips |
| `--gutter` | `clamp(20px, 4vw, 40px)` | `.container` inline padding |
| `--grid-gap` | `clamp(16px, 2vw, 32px)` | `.grid` column/row gap |

**Whitespace is the separator.** From the recalibration: a change of subject is signalled by `--band-y`, not by a colour change. Cap colour bands at **two per page** (typically one `.band--ink` and one `.band--white` or `--concrete-2`); everything else rides the default concrete field.

Consecutive bands of the same background must not stack without a hairline or a tight band between them — use `.hairline-top` on the second, or `.band--seam`.

### Vertical rhythm inside a band

```
.band            padding-block: var(--band-y)
 └ .band__head   flex column, gap: var(--space-4)
                 margin-block-end: var(--space-7)  → var(--space-8) @1024
 └ content       .grid (gap --grid-gap) | .stack (gap --space-5)
 └ closing CTA   margin-block-start: var(--space-7)
```
`.stack` gaps: `--space-3` (`.stack--sm`), `--space-5` (default), `--space-7` (`.stack--lg`).

### Spacing decision table for builders

| Situation | Use |
|---|---|
| New topic / section | `<section class="band">` |
| Sub-section of the same topic | `.band--tight` + `.hairline-top`, or a `.grid` row inside the same band |
| Related blocks in a column | `.stack` |
| Peer cards | `.grid grid--cards` |
| Label above a value | `--space-1` / `--space-2` (already in `.hero__spec`, `.trust-strip__item`) |
| Heading block to body | handled by `.band__head` — do not add margins |

## 4. Knockout typography

The reference boards use large display type *as surface*, not as decoration: white sentence-case type sitting on a photo (`IMG_6831`), white type sitting on the light-gray product stage (`IMG_6826`), outline numerals behind a render (`IMG_6820`).

This is **distinct from the revoked ghost watermark.** The revoked pattern was a 5–8% opacity word floating behind unrelated content. Knockout type as specified here is **real, legible, ≥ AA-contrast content**: it is the heading itself, reversed out of a dark image or a solid field.

### The three permitted knockout treatments

**K1 — Reverse-on-image (hero only).** Display type in `--color-text-on-dark` over an image that carries `--overlay-image` (`linear-gradient(180deg, rgba(14,20,24,0.15), rgba(14,20,24,0.72))`). This is the `.hero--ink` + `.hero__media--overlay` combination that already exists.

```html
<section class="hero hero--ink" id="hero" aria-labelledby="hero-h">
  <figure class="hero__media hero__media--overlay">
    <img src="assets/img/hero-double-girder-eot-crane.jpg" width="1600" height="1000"
         alt="Double-girder EOT crane rated 80 T on a 22 m span in a heavy fabrication bay">
  </figure>
  <div class="container hero__body">
    <p class="hero__eyebrow">Manufacturer · Harohalli KIADB · Since 2006</p>
    <h1 class="hero__title" id="hero-h">EOT and gantry cranes built to IS 807</h1>
  </div>
</section>
```
Contract: the gradient is mandatory whenever text sits on an image. Minimum measured contrast 4.5:1 for anything below `--text-display-l`, 3:1 for `.t-display-xxl`/`xl`. If the source photo has a bright sky in the text zone, the builder must either move the text block to the darker third or accept a solid `.hero--ink` panel behind it — **not** lower the type contrast.

**K2 — Reverse-on-ink panel.** Display type on `--color-ink` / `--color-steel` inside `.band--ink`. Text token is `--color-text-on-dark`; secondary is `--color-text-on-dark-muted`; hairlines become `--color-hairline-dark`. Already fully supported — nothing to add.

**K3 — Outline numeral (accent, hard-capped).** Large stat numeral rendered as stroke-only, from `IMG_6820`. Permitted **once per page maximum**, only on a `.stat--accent` inside a `.band--ink`, and only where the numeral is *also* announced in text.

```css
/* Belongs in components.css — Component Specialist to add, builders must not inline it */
.stat--accent .stat__value {
  color: transparent;
  -webkit-text-stroke: 1px var(--color-outline-stroke);
  text-stroke: 1px var(--color-outline-stroke);
}
@supports not (-webkit-text-stroke: 1px currentColor) {
  .stat--accent .stat__value { color: var(--color-text-on-dark); -webkit-text-stroke: 0; }
}
```
The `@supports` fallback is mandatory: without it the numeral disappears in engines lacking text-stroke. `--color-outline-stroke` is `rgba(252,251,248,0.42)`, which is decorative-only contrast, hence the requirement that the value be duplicated in the adjacent `.stat__caption` copy.

### Explicitly still revoked

- `--color-watermark-light` / `--color-watermark-dark`: tokens remain in the file for compatibility but **must not be used**. No 5–8% ghost words behind content.
- Type larger than `--text-display-xxl`.
- Knockout type over an un-overlaid photograph.
- Outline type on a light background (fails at every stroke width that stays elegant).

## 5. Accessibility requirements (typography)

- Body copy meets 4.5:1; `--color-text-secondary` (`#4A555C`) on concrete and white passes; `--color-text-muted` (`#79838A`) is for `--text-micro-caps` metadata only and must never carry sentence-level content.
- `--color-copper` (`#C4531F`) on `--color-concrete`/`--color-white` is used for links and hover states; it is **not** used for body text at `--text-body-s` or below.
- Respect the user's font size: all fixed sizes are in `rem`, and nothing sets `html { font-size: px }`. Do not override.
- No text is conveyed by an icon glyph alone. `.btn__glyph` (`↗`) and `.index-row__icon` are `aria-hidden="true"` and additive.
- Uppercase runs (`.eyebrow`) stay under ~6 words; longer uppercase strings hurt legibility and are a review flag.
- `.sr-only` supplies the accessible heading when a band's heading is visually carried by a strip (see `.trust-strip` in `index.html`).

## 6. QA checklist — typography & spacing

- [ ] Exactly one `.t-display-xxl` / `<h1>` per page.
- [ ] No `font-size`, `letter-spacing`, `margin`, `padding` literals in page HTML.
- [ ] Every paragraph over ~2 lines carries `.measure`.
- [ ] Heading levels sequential; no level skipped for size.
- [ ] At most two colour bands per page.
- [ ] At most one K3 outline numeral per page, inside `.band--ink`, with the value repeated in the caption.
- [ ] All mono text is a measurement, code, part number or index.
- [ ] 360px: no display line breaks mid-word, no horizontal scroll.
- [ ] 1920px: `.container` capped, no line longer than 68ch.
