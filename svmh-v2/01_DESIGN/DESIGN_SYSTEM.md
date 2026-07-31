# Design System — SVMH v2

Machine-readable source: `tokens/tokens.json`. Visual source of truth: `pen/svmh-v2.pen`. Reference rationale: `refboards/REFERENCE_DISTILLATION.md`.

**Direction in one line:** heavy-industry editorial — warm concrete and near-black, one molten-copper accent, monumental uppercase type, cut-out cranes breaking the frame, and the grid left visible as ornament.

---

## 1. Palette

| Role | Token | Hex | Where |
|---|---|---|---|
| Light page field | `concrete` | `#EFECE6` | Default background. Warm, not clinical |
| Alt light band | `concrete-2` | `#E4E0D8` | Every other section |
| Card surface | `white` | `#FCFBF8` | Cards on concrete. Never pure `#FFF` |
| Dark band | `ink` | `#0E1418` | Inverted sections, trust strip, footer |
| Dark elevated | `ink-2` | `#1C262C` | Cards inside dark bands |
| Structural dark | `steel` | `#1B3A4B` | Technical/spec panels, carried from v1 |
| **Accent** | `copper` | `#C4531F` | CTAs, active states, whole-card hover, niche flags |
| Accent hover | `copper-hover` | `#A9451A` | |
| Accent wash | `copper-soft` | `rgba(196,83,31,.10)` | Behind featured/niche blocks |
| Certified / in-stock | `safe` | `#2F6F4E` | |
| Lead-time caution | `warn` | `#B8862B` | |
| Safety-critical | `alert` | `#A63D3D` | Never decorative |

Copper is chosen rather than the generic industrial yellow because it reads as **molten metal** — it ties the palette directly to the ladle/foundry niche that is SVMH's actual differentiator. It is also a one-step evolution of the existing v1 `--copper: #C46B3A`, so the two properties stay recognisably related.

**Band sequence** (the only permitted section separator):
`concrete → white → ink → concrete-2 → copper → concrete`

## 2. Typography

| Style | Family | Size | Weight | Tracking | Use |
|---|---|---|---|---|---|
| display-xxl | Archivo Expanded / Anton | `clamp(3.5rem, 9vw, 8.5rem)` | 800 | −0.03em | Home hero, ghost watermarks |
| display-xl | display | `clamp(2.75rem, 6vw, 5.25rem)` | 800 | −0.025em | Page H1 |
| display-l | display | `clamp(2rem, 4vw, 3.25rem)` | 700 | −0.02em | Section H2 |
| display-m | display | `clamp(1.375rem, 2.2vw, 1.875rem)` | 700 | −0.01em | Card titles, H3 |
| stat-numeral | display | `clamp(3rem, 7vw, 6.5rem)` | 800 | −0.04em | Proof lockups |
| index-numeral | IBM Plex Mono | `clamp(1.75rem, 3vw, 3rem)` | 300 | 0 | `01 / 02 / 03` rows |
| lead | Inter | `clamp(1.06rem, 1.4vw, 1.31rem)` | 400 | — | Section intro |
| body | Inter | 15px / 1.62 | 400 | — | Default |
| micro-caps | Inter | 11px | 600 | +0.09em | **All** metadata |
| spec-mono | IBM Plex Mono | 13px | 400 | +0.01em | Capacity / span / duty |

Display is uppercase. Body is sentence case. No serifs. Every heading level skips a full step so hierarchy reads at a glance from across a factory office.

## 3. Grid & spacing

8px base unit. 12 columns, `clamp(16px, 2vw, 32px)` gap, `1240px` content max, `1600px` for full-bleed product stages, `68ch` measure for resource articles. Section band padding `clamp(64px, 9vw, 144px)`.

Breakpoints: 480 / 768 / 1024 / 1280 / 1600. Everything must render 360px → 1920px with no horizontal scroll.

## 4. Components

### Header (nav-as-grid)
Full-width bar divided into cells by 1px hairlines. Logo cell left, nav cells centre, right-most cell solid copper holding `Get a Quote →`. Sticky, collapses to 64px. Mobile: hamburger → full-screen uppercase overlay; persistent bottom bar `Call · WhatsApp · Quote`.

### Hero (headline-split-around-cutout)
Ghost watermark display word at 5–8% contrast; a background-free crane cut-out overlapping the letters; H1 split into two lines staggered around the machine; one dominant CTA plus one ghost secondary; copper circular ↘ scroll button bottom-left; dashed connector line to one callout tag carrying a real spec (`Ladle crane · 40 T · M8 duty`).

### Numbered index row
`index-numeral | display-m label | +/− expander`, 1px hairline between rows. Expands to reveal body copy and a ghost CTA. Requires `aria-expanded` and `aria-controls`.

### Product card
micro-caps index + uppercase 1–2 line title → cut-out render overflowing the card edge → body-s description → hairline → bottom-pinned spec row or ghost button. **Hover fills the entire card copper and inverts text.** Focus state matches hover plus a 2px copper focus ring.

### Stat lockup
Giant numeral + micro-caps caption stacked to its right. Solid on light bands; `outline-stroke` variant over imagery. Counts up on reveal, disabled under `prefers-reduced-motion`.

### Trust strip
Full-width `ink` band: `ISO 9001 (linked PDF) · IS 807 / IS 3177 · GST 29AAKCS6443A1ZB · MSME · Since 2006 · [N] installs`. Sits above the first fold break on every template. Any figure without evidence is marked `[CLIENT TO CONFIRM]` and withheld rather than guessed.

### Spec table
Hairline grid, `spec-mono` values, dotted-leader alignment between label and value (Renault board pattern), `scope` on all headers, a `<caption>`, and horizontal scroll with a shadow affordance on mobile.

### Comparison table ("Pain × Common solution × SVMH solution")
Three columns, expandable rows, SVMH column carrying the `copper-soft` wash. This is the ACME pattern and it is how the TCO argument gets made without a wall of text.

### Process chips
`ENQUIRY ▶▶ DESIGN ▶▶ FABRICATION ▶▶ FAT ▶▶ INSTALL ▶▶ AMC` — pill chips with chevron separators; wraps to two rows on mobile.

### RFQ form
Label-less underline inputs (SwiftCargo pattern) grouped into the IS 3177 sequence, stepped progress `01 — 04`, flat copper submit. Details in `../00_PLAN/04_CONVERSION_SPEC.md`.

### Buttons
| Variant | Look |
|---|---|
| Primary | Solid copper, 2px radius, 14/26 padding, micro-caps label, `↗` glyph |
| Ghost | Transparent, 1px `copper-wire` border |
| Dark pill | Solid ink, fully rounded — reserved for the single hero CTA |

Deliberately small. The headline is the loud element.

## 5. Imagery direction

- Product-in-use, never product-in-void. Every crane is lifting a real load in a real bay.
- Hero and card products are background-free cut-outs overflowing their container.
- The cut-out occludes the ghost watermark — that overlap *is* the depth mechanism.
- Cinematic factory frames: wide, well-lit welding, assembly, load-test.
- Isometric line-art for schematics; 3D renders for products; photography for proof.
- Alt text carries capacity, span and industry. It doubles as SEO.
- Client photos of poor quality get an ink+copper duotone rather than being dropped.
- Dark overlay for text-over-image: `linear-gradient(180deg, rgba(14,20,24,.15), rgba(14,20,24,.72))`.

## 6. Motion

`ease-out cubic-bezier(0.22, 1, 0.36, 1)`; 160ms fast, 280ms base, 560ms slow, 640ms reveal. IntersectionObserver reveal at threshold 0.12 with a 20px rise. Scroll-progress hairline at the top of the viewport. Counters animate once. Right-rail dot pagination on multi-band pages. No parallax on the product cut-out — it must stay crisp. Full `prefers-reduced-motion` honour: reveals off, final states kept.

## 7. Accessibility

4.5:1 body, 3:1 large display. 2px copper focus ring at 2px offset, always visible. Copper body copy is banned (large display only). Ghost watermark type is `aria-hidden`. Accordions, tabs and filters carry `aria-expanded` / `aria-pressed` / `aria-controls`. Data tables carry `scope` and a caption. Target ≥95 Lighthouse a11y — the v1 pages shipped with zero `aria-` attributes on two of three templates and that does not repeat here.

## 8. Design QA checklist

Run before any board or page is called done.

- [ ] Exactly one accent colour on screen
- [ ] Band sequence alternates; no decorative dividers
- [ ] Ghost watermark present in the hero and occluded by the subject
- [ ] At least one cut-out breaks its container edge
- [ ] 3–4× jump between display and body sizes
- [ ] All metadata uses micro-caps, no exceptions
- [ ] Numbered index rows used instead of icon bullets
- [ ] Hairlines only — no shadows between sections
- [ ] Whole-card hover, not button-only
- [ ] CTA is visually smaller than the headline
- [ ] Every stat is a numeral + stacked caption lockup
- [ ] No radii above 8px, no gradients on UI surfaces
- [ ] Every image is product-in-use with spec-bearing alt text
- [ ] One H1, one primary CTA
- [ ] Trust strip above the first fold break
- [ ] Keyboard path complete, focus ring visible
