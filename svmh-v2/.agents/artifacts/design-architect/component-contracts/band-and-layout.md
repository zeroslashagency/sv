# Contract — `.band`, `.container`, `.grid`, `.stack` (layout primitives)

**Status:** shipped in `base.css`. These four own **all** spacing on the site. Components never set outer margins.

## Page shell

```html
<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>…</title>
  <meta name="description" content="…">
  <link rel="canonical" href="https://svind.co.in/…">
  <link rel="stylesheet" href="assets/css/tokens.css">
  <link rel="stylesheet" href="assets/css/base.css">
  <link rel="stylesheet" href="assets/css/components.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="progress-bar" aria-hidden="true"><div class="progress-bar__fill"></div></div>
  <header class="nav">…</header>
  <main id="main">
    <section class="hero">…</section>
    <section class="band">…</section>
  </main>
  <nav class="mobile-bar" aria-label="Quick actions">…</nav>
  <footer class="footer">…</footer>
  <script src="assets/js/site.js" defer></script>
</body>
</html>
```

Cascade order `tokens.css` → `base.css` → `components.css` is mandatory and must not be reordered, bundled differently, or inlined.

## `.band`

```html
<section class="band" id="capability" aria-labelledby="capability-h">
  <div class="container">
    <div class="band__head">
      <p class="eyebrow eyebrow--rule">Capability</p>
      <h2 class="t-display-l" id="capability-h">Design, fabrication and testing under one roof</h2>
      <p class="t-lead measure">One or two sentences of orientation.</p>
    </div>
    <!-- exactly one layout primitive follows -->
    <div class="grid grid--cards">…</div>
  </div>
</section>
```

| Variant | Effect | Budget |
|---|---|---|
| `.band` | `padding-block: var(--band-y)` on `--color-concrete` | unlimited |
| `.band--tight` | `--band-y-tight` (40–72px) | unlimited |
| `.band--ink` | `--color-ink` surface, reverse type, dark hairlines, dark card skin | counts toward the 2-colour-band budget |
| `.band--white` | `--color-white` surface | counts toward the budget |
| `.band--concrete-2` | `--color-concrete-2` surface | counts toward the budget |
| `.band--seam` | Hairline seam between same-coloured bands | free |
| `.band--flush-top` / `--flush-bottom` | Removes padding on that edge, for image bands that must butt against the next band | free |

**Two colour-changing bands per page, maximum.** A third is a review failure. Section separation is whitespace (`--band-y`), not colour.

Every band requires `id` and `aria-labelledby` pointing at its own heading's `id`. If the heading is visually absent, supply `<h2 class="sr-only" id="…">`.

`.band__head` handles its own internal `gap: var(--space-4)` and bottom margin (`--space-7`, `--space-8` at ≥1024px). Do not add margins around it.

## `.container`

| Class | Max content width | Use |
|---|---|---|
| `.container` | 1240px + gutters | Default for every band |
| `.container--narrow` | 880px + gutters | Long-form prose, RFQ form, single-column legal pages |
| `.container--wide` | 1600px + gutters | Full-bleed product stage, wide image bands |

Inline padding is `--gutter` (`clamp(20px, 4vw, 40px)`). Never nest containers.

## `.grid`

```html
<!-- named split: preferred -->
<div class="grid grid--7-5">
  <div class="stack">…text…</div>
  <div>…media or specs…</div>
</div>

<!-- explicit spans: for asymmetry the named splits don't cover -->
<div class="grid">
  <div class="col-8 col-start-3">…centred-offset block…</div>
</div>
```

- 1 column below 768px; 12 columns at ≥768px.
- `.grid--7-5 / 5-7 / 8-4 / 4-8 / 6-6` resolve at ≥1024px.
- `.grid--cards` = 1 → 2 @640px → 3 @1024px.
- Gap `--grid-gap` (`clamp(16px, 2vw, 32px)`).
- Do not mix named splits and `.col-*` on the same grid.
- Do not use `.col-start-*` to move a block visually ahead of content that precedes it in the DOM — reading order must equal DOM order.

## `.stack`, `.row`, `.measure`, hairlines

| Class | Effect |
|---|---|
| `.stack` | Vertical flow, gap `--space-5` |
| `.stack--sm` | gap `--space-3` |
| `.stack--lg` | gap `--space-7` |
| `.row` | Horizontal flow with wrap |
| `.measure` | `max-width: 68ch` — every running paragraph |
| `.measure--tight` | Narrower measure for leads beside a heading |
| `.hairline-top` / `.hairline-bottom` | 1px `--color-hairline` separator |

## `.reveal`

```html
<div class="grid grid--cards reveal reveal--stagger">…</div>
```

IntersectionObserver, threshold 0.12, rootMargin `0px 0px -8% 0px`, adds `.is-visible`. Stagger 80ms per child, capped at 400ms. Under `prefers-reduced-motion` elements resolve to their final state immediately. Content must be readable if the observer never fires.

## Anti-patterns

1. Nested `.container`.
2. Inline `style=` for spacing.
3. Margin or padding literals in page HTML.
4. Three or more colour bands.
5. Two consecutive same-coloured bands with no hairline or tight band between them.
6. `.col-*` used on a `.grid--cards`.
7. A band with no `aria-labelledby`.
8. Layout achieved with `<br>` or empty divs.

## Review gates

- [ ] Cascade order intact; `site.js` deferred at the end of `<body>`.
- [ ] One `.hero`, one `<main id="main">`, one `.footer` per page.
- [ ] Every `.band` has `id` + `aria-labelledby` + a real heading.
- [ ] ≤2 colour bands.
- [ ] No nested containers, no spacing literals.
- [ ] Every paragraph capped by `.measure`.
- [ ] Reading order equals DOM order at every breakpoint.
- [ ] 360 → 1920 checked; no horizontal body scroll.
