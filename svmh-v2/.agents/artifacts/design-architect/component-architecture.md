# SVMH v2 — Component Architecture

**Owner:** Design Architect (Agent A / T001)
**Status:** Binding for page builders (B, C) and the Component Specialist (D)
**Extends, does not replace:** `03_BUILD/assets/css/COMPONENT_CONTRACT.md`, `03_BUILD/assets/js/JS_CONTRACT.md`

Every component below already exists in `components.css` unless marked **NEW**. Page builders compose from this list; they do not invent classes. Anything marked NEW is a request to the Component Specialist — builders must not inline the CSS.

---

## 1. Architecture in one page

```
document
├── .skip-link                          a11y, first focusable
├── .progress-bar                       JS: scroll progress
├── header.nav                          global chrome
│   ├── .nav__inner  (in .container)
│   ├── .nav__menu   ≥1024px
│   ├── .nav__cta
│   ├── .nav__toggle <1024px            JS: aria-expanded
│   └── .nav__overlay [hidden]          JS: focus trap, Esc
├── main#main
│   ├── .hero                           ONE per page
│   ├── .trust-strip                    optional, homepage + key landers
│   └── section.band  × N               every content section
│       ├── .band__head                 eyebrow + h2 + lead
│       └── one layout primitive        .grid | .stack | .row
│           └── content components      cards, index rows, stats, tables, chips, form
├── .mobile-bar                         <768px sticky action bar
└── footer.footer
```

### Layering rules

1. **Chrome → Page → Band → Layout → Component → Primitive.** A component never sets its own outer margin; the layout primitive owns spacing.
2. **Bands own background.** Only `.band--*` and `.hero--ink` change surface colour. A card never sets a page-level background.
3. **Components are surface-aware, not surface-setting.** `.band--ink .card` already re-skins cards for dark bands. Builders switch the band; the component follows.
4. **One interactive owner per element.** A card is made clickable by `.card__link` stretching over it — never by wrapping the `<article>` in an `<a>`.
5. **No component nests inside itself.** No card-in-card, no accordion-in-accordion.

---

## 2. Component catalogue

Legend: **Element** = required tag, **Variants** = modifier classes, **Slots** = required/optional children, **JS** = module from `JS_CONTRACT.md`.

### 2.1 `.nav` — global header

| | |
|---|---|
| Element | `<header class="nav">` |
| Variants | none. State classes only: `.is-scrolled` (JS, past 40px → height `--nav-h-scrolled`) |
| Slots | `.nav__brand` (`.nav__wordmark` + `.nav__descriptor`), `.nav__menu` (5 `.nav__link`), `.nav__cta`, `.nav__toggle`, `.nav__overlay` |
| JS | nav shrink; mobile menu (focus trap, Esc, `aria-expanded`, `aria-controls`) |
| Rules | Overlay ships **with `hidden`**. Current page link gets `aria-current="page"`. `.nav__menu` hidden below 1024px; `.nav__toggle` hidden above. |

### 2.2 `.hero` — page opener

| | |
|---|---|
| Element | `<section class="hero" aria-labelledby="hero-h">` |
| Variants | `.hero--ink` (dark, reverse type), `.hero__media--overlay` (gradient scrim for K1 knockout) |
| Slots | `.hero__grid` › `.hero__body` (`.hero__eyebrow`, `.hero__title` = the page `<h1>`, `.hero__lead`, `.hero__specs`, `.hero__actions`) + `.hero__media` (`<figure>` with `<img>` + `.hero__media-caption`) |
| Composition | `.hero__grid` = 7fr/5fr at ≥1024px, single column below, gap `clamp(32px,5vw,96px)` |
| JS | none (hero content must never depend on JS) |
| Rules | Exactly one per page. `<img>` needs `width`/`height` and a spec-bearing `alt`. `.hero__specs` is a `<dl>` of 3–4 pairs, never more. Max two `.hero__actions` buttons: one `.btn--primary`, one `.btn--dark`. |

Variant selection: product/service/location pages → default light hero. Homepage and industry landers with a strong bay photograph → `.hero--ink` + `.hero__media--overlay`.

### 2.3 `.trust-strip` — credential band

| | |
|---|---|
| Element | `<section class="trust-strip" aria-labelledby="…">` with `.sr-only` `<h2>` |
| Slots | `.trust-strip__list` › `.trust-strip__item` (`__label` + `__value`) |
| Variants | `.trust-strip__value--verified` when the value links to a PDF/proof |
| Rules | 4–6 items. Every value is a fact that can be evidenced. Unverified values use `<span class="spec">[CLIENT TO CONFIRM]</span>`. Sits immediately after the hero, flush (no band padding). |

### 2.4 `.band` — section shell (layout component)

| | |
|---|---|
| Element | `<section class="band" id="…" aria-labelledby="…-h">` |
| Variants | `--tight`, `--ink`, `--white`, `--concrete-2`, `--seam`, `--flush-top`, `--flush-bottom` |
| Slots | `.band__head` (optional) + exactly one layout primitive |
| Rules | Every band has `id` + `aria-labelledby` pointing at its own heading `id`. Max two colour-changing variants per page. |

### 2.5 `.btn` — action

| | |
|---|---|
| Element | `<a>` for navigation, `<button type>` for behaviour. Never the wrong one. |
| Variants | `--primary` (copper fill, one per viewport region), `--dark` (ink), `--ghost` (copper hairline), `--link` (inline underline), `--block` (full width) |
| Slots | label text + optional `.btn__glyph` (`↗`, `aria-hidden="true"`) |
| Rules | Copper appears ≤3× per viewport (recalibration §accent). Never two `.btn--primary` side by side. Min target 44px. Label is a verb phrase, never "Click here"/"Learn more". |

### 2.6 `.card` — content unit

| | |
|---|---|
| Element | `<article class="card">` |
| Variants | `.card--product` (adds `.card__media`), `.band--ink .card` (auto dark skin) |
| Slots | `.card__index` (mono numeral, optional), `.card__media` (product only), `.card__title` › `.card__link`, `.card__text`, optional `<ul class="stack stack--sm t-body-s text-secondary">`, `.card__foot` › `.card__spec` |
| JS | none. May carry `.reveal` for entrance. |
| Rules | Hover = border darkens to `--color-hairline-2` + title→copper + `translateY(-1px)`; nothing else, ≤160ms. `.card__link::after` stretches the hit area — so the card contains **exactly one** link. If a card needs a secondary link, it goes in `.card__foot` and the stretched overlay is dropped. `.card__media img` is `aspect-ratio: 3/2`. |

### 2.7 `.index-row` — numbered feature / accordion row

| | |
|---|---|
| Element | `<div class="index-row">` inside `<div class="index-list">` |
| Slots | heading (`<h3>`) wrapping `.index-row__trigger` (`<button>`), containing `.index-row__num`, `.index-row__label`, `.index-row__icon`; sibling `.index-row__panel` |
| Variants | Static mode: no `<button>`, no panel — `.index-row` with `__num` + `__label` + inline copy, used as a non-interactive numbered index (from `IMG_6827`'s `01 Air / 02 Sea` cells) |
| JS | accordion — `aria-expanded` on trigger, `aria-controls` → panel `id`, `hidden` on collapsed panels |
| Rules | Panels ship **visible**; JS adds `hidden` on init (no-JS users read everything). Numbers are zero-padded `01…NN` and sequential. Icon is `aria-hidden`. One accordion group per band. |

### 2.8 `.chips` — process / filter row

| | |
|---|---|
| Element | `<ul class="chips">` › `<li class="chips__item">` |
| Slots | `.chips__label` › optional `.chips__num` + text |
| Variants | `.chips__item--active` |
| JS | When used as filters: `<button data-filter>` with `aria-pressed`; table filter module toggles `.filter-hide` on rows |
| Rules | As process display: non-interactive `<span>`s, mirrors the `.index-list` numbering below it. As filters: real buttons, plus a `role="status" aria-live="polite"` result count. |

### 2.9 `.stat` / `.stat-grid` — figure lockup

| | |
|---|---|
| Element | `<div class="stat">` inside `<div class="stat-grid">` |
| Slots | `.stat__value` (+ optional `.stat__unit`), `.stat__caption` |
| Variants | `.stat--accent` (K3 outline numeral — **max one per page, inside `.band--ink` only**) |
| JS | stat count-up via `data-count-to`; `Intl.NumberFormat('en-IN')`; 1100ms; resolves instantly under `prefers-reduced-motion` |
| Rules | Numerals are weight 300. Caption states the unit and the basis ("Static overload at factory acceptance test"), not a bare noun. Unknown figures render `[CLIENT TO CONFIRM]` and get **no** `data-count-to`. |

### 2.10 `.spec-table` — technical data

| | |
|---|---|
| Element | `<div class="spec-table-wrap">` › `<table class="spec-table">` |
| Variants | `.spec-table--leader` (first column emphasised) |
| Slots | `<caption>`, `<thead>` with `scope="col"`, row headers with `scope="row"`, optional `.spec-table__note` after the wrap |
| JS | optional filter via `data-filter` / `data-region` etc. |
| Rules | `<caption>` is mandatory (may be `.sr-only`). Wrapper scrolls horizontally on mobile — never squeeze columns. Tabular figures already on. Every spec traces to a standard or is marked unconfirmed. |

### 2.11 `.compare-table` — SVMH vs alternative

Same anatomy as `.spec-table` plus `.compare-table__spec` (row label) and `.compare-table__svmh` (highlighted column). Rules: claims must be verifiable and neutral in tone; no competitor is named.

### 2.12 `.form` — RFQ / contact

| | |
|---|---|
| Element | `<form class="form" novalidate>` |
| Slots | `.form__step-track` › `.form__step` + `.form__step-current`; `.form__group` (fieldset) › `.form__legend`, `.form__field` (`.form__label`, `.form__input`/`__select`/`__textarea`, `.form__hint`, `.form__error`), `.form__row`, `.form__check`, `.form__trap` (honeypot), `.form__actions`, `.form__status`, `.form__note` |
| Variants | `.form__field--error`, `.form__status--ok`, `.form__status--error` |
| JS | form steps module — Constraint Validation API, Indian phone `/^(?:\+91\|0)?[6-9]\d{9}$/` |
| Rules | Groups ship **visible**; JS adds `hidden`. Every input has a real `<label for>`. Errors use `aria-describedby` + `aria-invalid`. `.form__status` is `role="status" aria-live="polite"`. `.form__trap` is off-screen and `tabindex="-1"` + `aria-hidden`. **Honeypot is not security** — see risk note in handoff. |

### 2.13 `.mobile-bar` — sticky mobile actions

`<nav class="mobile-bar" aria-label="Quick actions">` › 3–4 `.mobile-bar__item`, one `.mobile-bar__item--accent`. Visible <768px only. Each target ≥44px. Must not cover the last focusable element — pages add bottom padding via the footer, already handled.

### 2.14 `.footer` — global footer

`.footer__grid` › `.footer__brand` (`.footer__blurb`, `.footer__address`) + `.footer__col` × 3–4 (`.footer__heading` + `.footer__list` › `.footer__link`) + `.footer__legal` (`.footer__legal-links`). Address is one canonical NAP block matching the JSON-LD. `<address>` element for the postal block.

### 2.15 Utility / behaviour classes

| Class | Purpose |
|---|---|
| `.container`, `--narrow` (880px), `--wide` (1600px) | Width + gutter |
| `.grid`, `--cards`, `--7-5`, `--5-7`, `--8-4`, `--4-8`, `--6-6`, `.col-N`, `.col-start-N` | Layout |
| `.stack`, `--sm`, `--lg` | Vertical flow |
| `.row` | Horizontal flow with wrap |
| `.measure`, `--tight` | Line-length cap |
| `.hairline-top`, `.hairline-bottom` | 1px separators |
| `.reveal`, `.reveal--stagger`, `.is-visible` | Entrance (IntersectionObserver, threshold 0.12, rootMargin `0px 0px -8% 0px`, stagger 80ms capped 400ms) |
| `.sr-only`, `.skip-link` | a11y |
| `.eyebrow`, `--rule`, `.spec`, `--boxed`, `.mono`, `.text-secondary`, `.text-muted`, `.t-*` | Typography |

---

## 3. NEW components requested from the Component Specialist

Each is derived from a reference board and named to fit the existing BEM system. Builders should **not** use these until D lands them in `components.css`; the reference board and the fallback are given so pages can ship without them.

| Component | Derived from | Purpose | Fallback until shipped |
|---|---|---|---|
| **`.stat--accent` outline treatment** | `IMG_6820` | K3 knockout numeral, ≤1/page, ink band only, `@supports` fallback mandatory | Plain `.stat` |
| **`.stage`** (`.stage__media`, `.stage__label`, `.stage__counter`) | `IMG_6826` | Full-bleed cool-neutral product stage: machine centred, mono capacity label, `01 — 03` counter. Uses `--color-concrete-2`/`-3`, zero radius, zero shadow | `.band--concrete-2` + `.card--product` |
| **`.panel--float`** | `IMG_6822` | Light content panel overlapping a photograph above it; `--elevation-card` only, `--radius-md` max | `.band--white` following an image band |
| **`.split--ink`** | `IMG_6826` | Asymmetric intro: dark 55% column with eyebrow + 3-line paragraph, light 45% column. Implementable today as `.band--ink` + `.grid--7-5` | Use the composition, skip the modifier |
| **`.logo-strip`** | `IMG_6827` | Client/standards marks in hairline cells, mono captions, grayscale | `.trust-strip--tight` semantics |

Nothing on this list is required for a page to be complete. Pages must be buildable from §2 alone.

---

## 4. Composition rules by page type

| Page | Hero | Required bands (in order) |
|---|---|---|
| Homepage | `.hero--ink` + overlay | trust-strip → three-doors (`grid--cards`) → capability split (`grid--7-5`) → stat-grid (`band--ink`) → spec-table → process (`chips` + `index-list`) → industries (`grid--cards`) → proof/locations → RFQ CTA |
| Product listing | light hero | intro split → product card grid (`grid--cards`, `.card--product`) → selection spec-table → accordion FAQ → CTA |
| Product detail | light hero with `.hero__specs` | overview split → spec-table → `compare-table` → application `grid--cards` → process `index-list` → related products → CTA |
| Industry | `.hero--ink` optional | problem split → solution `grid--cards` → spec-table → proof stat-grid → CTA |
| Location | light hero | service area split → coverage spec-table → NAP panel → CTA |
| RFQ | `.hero` compact, no media | `.form` in `.container--narrow` → what-happens-next `index-list` → trust-strip |

Every page ends on a CTA band. Every page carries exactly one `<h1>`, one `.hero`, one `.footer`, one `.mobile-bar`.

## 5. Anti-patterns (auto-fail at review)

1. New class names not in §2 or §3.
2. Inline `style=` attributes.
3. Card inside a card; accordion inside an accordion.
4. Two `.btn--primary` in the same band.
5. More than two colour bands per page.
6. `border-radius` above `--radius-md` (4px).
7. Box shadows other than `--elevation-card` (and `--elevation-float` for the mobile table affordance only).
8. Ghost watermark text (revoked).
9. Content that only exists after JS runs.
10. A band without `aria-labelledby`.
11. `<div>` used where `<section>`/`<article>`/`<button>`/`<a>` is correct.
12. Icon-only controls without an accessible name.
