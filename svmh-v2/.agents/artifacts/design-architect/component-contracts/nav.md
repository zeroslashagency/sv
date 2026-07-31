# Contract — `.nav` + `.mobile-bar`

**Status:** shipped. Reproduce the markup **verbatim** on every page. The only per-page change is `aria-current="page"`.

## HTML — header

```html
<header class="nav">
  <div class="container nav__inner">
    <a class="nav__brand" href="/">
      <span class="nav__wordmark">SVMH</span>
      <span class="nav__descriptor">EOT &amp; Gantry Cranes · Bengaluru</span>
    </a>
    <nav class="nav__menu" aria-label="Main">
      <a class="nav__link" href="/eot-cranes">Cranes</a>
      <a class="nav__link" href="/industries">Industries</a>
      <a class="nav__link" href="/services">Service &amp; spares</a>
      <a class="nav__link" href="/resources">Resources</a>
      <a class="nav__link" href="/about">Company</a>
    </nav>
    <a class="btn nav__cta" href="/request-a-quote">Get a quote<span class="btn__glyph" aria-hidden="true">↗</span></a>
    <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-overlay" aria-label="Open menu">
      <span class="nav__toggle-bar"></span><span class="nav__toggle-bar"></span><span class="nav__toggle-bar"></span>
    </button>
  </div>

  <div class="nav__overlay" id="nav-overlay" hidden>
    <ul class="nav__overlay-list">
      <li><a class="nav__overlay-link" href="/eot-cranes">EOT cranes</a></li>
      <li><a class="nav__overlay-link" href="/gantry-cranes">Gantry &amp; goliath</a></li>
      <!-- … full product + company index … -->
    </ul>
    <div class="nav__overlay-foot">
      <p class="eyebrow">Harohalli KIADB Industrial Area · Bengaluru</p>
      <a class="btn btn--dark" href="/request-a-quote">Request a quote</a>
    </div>
  </div>
</header>
```

## Current page marking

On the matching top-level link only:

```html
<a class="nav__link" href="/eot-cranes" aria-current="page">Cranes</a>
```

On the homepage, `aria-current="page"` goes on `.nav__brand`. Exactly one `aria-current` per page.

## Behaviour

| Aspect | Contract |
|---|---|
| Shrink | JS adds `.is-scrolled` past 40px scroll → header height `--nav-h` (72px) → `--nav-h-scrolled` (64px). Transition `--dur-fast`. |
| Overlay | Ships **with `hidden`** (opposite of the accordion — the overlay is a duplicate index, so hiding it costs nothing and showing it without JS would dump the whole sitemap into the page). |
| Toggle | `aria-expanded` on the button, `hidden` removed from the overlay, `.is-locked` on `<html>` to stop background scroll. |
| Focus trap | Focus moves into the overlay on open, cycles inside it, returns to the toggle on close. |
| Escape | Closes the overlay and restores focus. |
| Label | `aria-label` on the toggle flips between "Open menu" and "Close menu" via JS. Builders ship "Open menu". |

## Responsive

| Width | Visible |
|---|---|
| <768px | Brand, toggle, `.mobile-bar` at the bottom |
| 768–1023px | Brand, CTA, toggle. **No** `.mobile-bar`, **no** `.nav__menu`. Verify this window explicitly. |
| ≥1024px | Brand, `.nav__menu`, `.nav__cta`. No toggle. |

## Sticky / z-index

- Header uses `--z-nav` (100); overlay `--z-overlay` (200); mobile bar `--z-mobile-bar` (300); scroll progress `--z-progress` (400); skip link `--z-skip` (500). Never introduce a new z-index.
- `.progress-bar` sits above the header and is `aria-hidden="true"`.

## `.mobile-bar`

```html
<nav class="mobile-bar" aria-label="Quick actions">
  <a class="mobile-bar__item" href="tel:+91XXXXXXXXXX">Call</a>
  <a class="mobile-bar__item" href="https://wa.me/91XXXXXXXXXX">WhatsApp</a>
  <a class="mobile-bar__item mobile-bar__item--accent" href="/request-a-quote">Get a quote</a>
</nav>
```

- 3–4 items maximum, one accent.
- Visible below 768px only.
- Each item ≥44px tall.
- Real phone/WhatsApp numbers must match the footer NAP and the JSON-LD. Placeholders stay as `[CLIENT TO CONFIRM]` in copy, not as fake numbers in `href` — an unverified number ships as a link to the quote form instead.

## Skip link

First focusable element in `<body>`:

```html
<a class="skip-link" href="#main">Skip to content</a>
```
`<main id="main">` must exist on every page.

## Accessibility

- `<nav>` elements carry distinct `aria-label`s ("Main", "Quick actions", footer nav).
- Toggle is a real `<button type="button">` with an accessible name; the three bars are decorative spans.
- Overlay links are a real `<ul>`/`<li>` list.
- Focus ring 2px copper at 2px offset, visible against both light header and dark overlay.
- No hover-only dropdowns anywhere in the nav — the overlay is the only disclosure, and it is click/keyboard driven.

## Review gates

- [ ] Header markup identical across all pages.
- [ ] Exactly one `aria-current="page"`.
- [ ] Overlay ships with `hidden`; toggle ships `aria-expanded="false"`.
- [ ] `aria-controls` matches the overlay `id`.
- [ ] `.skip-link` first in `<body>`; `#main` exists.
- [ ] 768–1023px window verified.
- [ ] Esc closes overlay, focus returns to toggle.
- [ ] No new z-index values.
