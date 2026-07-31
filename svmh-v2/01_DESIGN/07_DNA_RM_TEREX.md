# 07 — Design DNA: RM Terex

**Status:** AUTHORITATIVE. Supersedes `06_DESIGN_RECALIBRATION.md` and `DESIGN_SYSTEM.md` on palette, type treatment, and surface rules. Resolves risk **R1** raised in T001.

**Client direction, verbatim:** *"i want that dna style i want"* — attached the two RM | Terex case-study boards (`IMG_6819` / `IMG_6820` / `IMG_6821` / `IMG_6826` family).

The concrete + copper system is retired. Warm neutrals, copper accent, and hairline-only ornament are replaced by the cool-gray / navy / white system below. This is a full palette and treatment swap, not a tint adjustment.

---

## 1. Palette

| Token | Value | Role |
|---|---|---|
| `--color-canvas` | `#EFEFEF` | Primary page field. Cool light gray, no warmth. |
| `--color-canvas-2` | `#E7E7E7` | Adjacent panel field. Distinguishes panels from canvas by a hair. |
| `--color-surface` | `#FFFFFF` | Cards, media bodies, nav. Pure white is correct here — it is the card, not the page. |
| `--color-navy` | `#1E3A6B` | The only accent. Inverted panels, category labels, captions, CTA fills. |
| `--color-navy-deep` | `#162C52` | Navy hover / pressed. |
| `--color-ink` | `#1A1D21` | Body copy and titles on light fields. |
| `--color-ink-muted` | `#8A8F96` | micro-caps metadata, dates, inactive counters. |
| `--color-knockout` | `#FFFFFF` | Giant display numerals and wordmarks on canvas. |

**Accent budget:** navy appears as **one inverted panel per row maximum**, plus labels and counters. Never two navy panels adjacent.

**Deleted tokens:** every `concrete`, `copper`, and `watermark` value. No page may reference them.

## 2. The five signature moves

These are what make the boards read as expensive. Each is mandatory somewhere on the site.

### S1 — Giant white knockout wordmark, occluded by the product
The defining move. An oversized model name or numeral set in white at 180–320px sits on the gray canvas; the product cut-out overlaps and occludes part of it. No shadow, no outline, no opacity trick — solid white on gray, partially hidden.

- Type: heavy geometric sans, tight tracking, `-0.02em`.
- The word is **decorative repetition** of information stated in real text nearby. It is `aria-hidden="true"`.
- The product must cover 25–45% of the glyph run. Less reads as an accident; more loses the word.
- Exactly **one per band**, never two in a viewport.

### S2 — Product cut-out on gray with soft ground shadow
Background-free 3D render or cleanly masked photo, floating on `--color-canvas`, with a soft elliptical contact shadow beneath. Never a boxed photo, never a full-bleed environment shot behind text.

### S3 — Label / counter frame
Every full-bleed band carries a top-left navy micro-caps label (`РЕЗУЛЬТАТ` → `RESULT`, `МЕДИА` → `MEDIA`) and a top-right slide counter `02 — 03` where the active figure is ink and the rest muted. This frame is what turns a section into a "case-study page".

### S4 — Three-up numbered panel row, third panel inverted
Equal-width panels separated by ~4px gray gutters. Each panel: a 6px navy square bullet, then a giant knockout numeral (`01` `02` `03`) at ~64px, then three lines of body copy. The **last panel is filled navy** with white numeral and white copy.

### S5 — Stat lockup: giant knockout numeral + navy caption
Huge white numeral with a small navy lowercase caption baseline-aligned to its right (`22 модели` → `22 models`, `78 рендеров` → `78 renders`), tiny navy square bullet above-left. Product cut-out sits in front of the numeral.

## 3. Surface rules

| Rule | Value |
|---|---|
| Radii | **0px everywhere.** No exceptions. The boards are entirely square. |
| Shadows on UI | None. Only the soft *ground shadow* under product cut-outs. |
| Section separation | 4–8px gray gutters between panels; full-bleed color change between bands. |
| Borders | None on panels. Panels are distinguished by fill, not stroke. |
| Gradients | None. |

The previous system's "hairlines as the only ornament" rule is gone. **Gutters and fill changes are the ornament.**

## 4. Typography

| Class | Size | Weight | Case | Tracking | Use |
|---|---|---|---|---|---|
| `knockout-xl` | `clamp(120px, 22vw, 320px)` | 700 | upper | `-0.02em` | S1 wordmark |
| `knockout-num` | `clamp(56px, 7vw, 96px)` | 700 | — | `-0.01em` | S4 panel numerals, S5 stats |
| `display-l` | `clamp(28px, 3.2vw, 44px)` | 700 | sentence | `-0.01em` | Band headings |
| `title-m` | `17px` | 700 | sentence | `0` | Card titles, 2–3 line wrap |
| `body` | `15px` | 400 | sentence | `0` | 1.55 line-height, max 3 lines in panels |
| `micro-caps` | `11px` | 600 | upper | `+0.09em` | Labels, dates, categories, counters, `24 ФОТО` footers |
| `spec-mono` | `13px` | 400 | — | `+0.02em` | IBM Plex Mono. Capacity, span, duty class only. |

**Families:** Inter Tight for everything except `spec-mono` (IBM Plex Mono). The boards' numerals are a rounded geometric face; Inter Tight at weight 700 with tight tracking is the closest available and is what the Paper file already carries.

**Three sizes per viewport still holds** — the knockout layer does not count toward it, because it is decorative.

## 5. Component translations

| Board pattern | SVMH component |
|---|---|
| `TLB 825` hero (board 1, top) | Product page hero — crane model number as S1 knockout, crane render as S2 cut-out |
| 3-up `01/02/03` row with navy third | Home "How we deliver" · product benefit row |
| Media cards with `date · CATEGORY` + `24 ФОТО` | Projects / case-study index |
| `3D` band with product on knockout glyph | Capability band — "In-house design" or "FEM 9.511 verified" |
| `22 модели` / `78 рендеров` stat pair | Proof band — `20 YRS` / `100 T` / `IS 807` |
| Navy band + phone mockup | Not used — we are not selling a case study of ourselves |
| Hamburger overlay, uppercase menu, `01/04` counter | Mobile nav + hero carousel counter |

## 6. Media card anatomy

Fixed, from the boards. Do not vary it.

```
┌─────────────────────┐
│   image  (4:3)      │  ← photo bleeds to card edges, no inset
├─────────────────────┤
│ 28 ИЮЛ. 2018  ВИДЕО │  ← micro-caps muted date + navy category
│                     │
│ Bold title running  │  ← title-m, 2–3 lines
│ two or three lines  │
│                     │
│ 24 ФОТО         [▷] │  ← micro-caps footer + glyph, baseline aligned
└─────────────────────┘
```

White card on gray canvas. Zero radius. No border. No shadow.

## 7. What we reject from these boards

| Rejected | Why |
|---|---|
| The navy "Мобильная версия" showcase band | That is agency case-study framing. SVMH's site is not a portfolio of itself. |
| Russian-market copy density | Our body copy stays at three lines per panel; the boards occasionally run longer. |
| Studio-void product shots as the *only* imagery | Cut-outs are correct for the knockout bands, but at least one band must show a crane **lifting a load in a real bay** — that is the credibility signal for a manufacturer. |
| Photo-realistic 3D renders we do not own | SVMH's library is brochure scans. Cut-outs must be masked from real plant photography, or commissioned. Flagged as an asset gap. |

## 8. QA checklist — replaces §4 of `06_DESIGN_RECALIBRATION.md`

- [ ] Canvas is `#EFEFEF` / `#E7E7E7`; no warm neutral anywhere
- [ ] Navy is the only accent; one inverted panel per row maximum
- [ ] Every radius is `0`
- [ ] No shadows except product ground shadows
- [ ] Exactly one S1 knockout wordmark per band, occluded 25–45% by the product
- [ ] All knockout decoration is `aria-hidden="true"` and duplicated in real text
- [ ] Every band has the S3 label + counter frame
- [ ] Panels separated by 4–8px gutters, not borders
- [ ] All metadata in `micro-caps`; all engineering data in `spec-mono`
- [ ] ≤3 non-decorative type sizes per viewport
- [ ] Knockout white on `#EFEFEF` is decorative only — never carries unique information (contrast is ~1.1:1 and fails AA by design)
- [ ] Real text contrast: ink on canvas ≥ 4.5:1, white on navy ≥ 4.5:1
- [ ] 360px → 1920px, no horizontal scroll; knockout scales with `vw` and clips rather than reflowing
- [ ] Keyboard path complete, 2px navy focus ring
- [ ] One H1, one primary CTA per page

## 9. Contrast note

White knockout on `#EFEFEF` measures roughly **1.1:1**. This is intentional and permitted **only** because the knockout layer is decorative and `aria-hidden`. Every piece of information it repeats must appear in a compliant text element in the same band. A reviewer finding a knockout that carries unique meaning must fail the page.

Navy `#1E3A6B` on `#EFEFEF` measures **~8.9:1** — safe for labels at 11px.
Ink `#1A1D21` on `#EFEFEF` measures **~15.4:1**.
White on navy `#1E3A6B` measures **~8.6:1**.
