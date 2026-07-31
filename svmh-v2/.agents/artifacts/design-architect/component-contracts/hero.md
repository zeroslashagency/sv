# Contract — `.hero`

**Status:** shipped in `components.css`. Builders consume; do not modify CSS.
**One per page.** Carries the page `<h1>`.

## Variants

| Class | When |
|---|---|
| `.hero` | Default light hero. Product, service, location, resource, RFQ pages. |
| `.hero .hero--ink` | Dark hero. Homepage and industry landers with a strong bay photograph. |
| `.hero__media--overlay` | Required whenever display text sits over the image (K1 knockout). Applies `--overlay-image`. |

## HTML — default (text + media split)

```html
<section class="hero" id="hero" aria-labelledby="hero-h">
  <div class="container hero__grid">
    <div class="hero__body">
      <p class="hero__eyebrow">Manufacturer · Harohalli KIADB, Bengaluru · Since 2006</p>
      <h1 class="hero__title" id="hero-h">EOT and gantry cranes built to IS 807</h1>
      <p class="hero__lead">Single-girder up to 15 T, double-girder to 100 T and above, hot-metal and ladle cranes to IS 4137.</p>

      <dl class="hero__specs">
        <div class="hero__spec">
          <dt class="hero__spec-label">Capacity</dt>
          <dd class="hero__spec-value">1 – 100+ T</dd>
        </div>
        <div class="hero__spec">
          <dt class="hero__spec-label">Duty class</dt>
          <dd class="hero__spec-value">M3 – M8</dd>
        </div>
        <div class="hero__spec">
          <dt class="hero__spec-label">Standards</dt>
          <dd class="hero__spec-value">IS 807 · IS 3177 · FEM 9.511</dd>
        </div>
      </dl>

      <div class="hero__actions">
        <a class="btn btn--primary" href="/request-a-quote">Request a quote<span class="btn__glyph" aria-hidden="true">↗</span></a>
        <a class="btn btn--dark" href="/downloads">Download catalogue</a>
      </div>
    </div>

    <figure class="hero__media">
      <img src="assets/img/hero-double-girder-eot-crane.jpg" width="1200" height="900"
           alt="Double-girder EOT crane rated 80 T on a 22 m span carrying a fabricated steel assembly across a heavy fabrication bay">
      <figcaption class="hero__media-caption">Double-girder EOT · 80 T · 22 m span · M7 duty</figcaption>
    </figure>
  </div>
</section>
```

## HTML — ink / knockout

```html
<section class="hero hero--ink" id="hero" aria-labelledby="hero-h">
  <figure class="hero__media hero__media--overlay">
    <img src="assets/img/hero-bay-wide.jpg" width="1600" height="1000" alt="…">
  </figure>
  <div class="container hero__body">
    <p class="hero__eyebrow">Harohalli KIADB · Bengaluru · Since 2006</p>
    <h1 class="hero__title" id="hero-h">Cranes that keep the bay moving</h1>
    <p class="hero__lead">…</p>
    <div class="hero__actions">
      <a class="btn btn--primary" href="/request-a-quote">Request a quote<span class="btn__glyph" aria-hidden="true">↗</span></a>
    </div>
  </div>
</section>
```

## Slots

| Slot | Required | Constraint |
|---|---|---|
| `.hero__eyebrow` | yes | `--text-micro-caps`. ≤6 words plus separators. Location + credential, not a slogan. |
| `.hero__title` | yes | `<h1>`, `id` matched by `aria-labelledby`. Sentence case. 4–9 words. Contains the product noun and, where honest, the standard. |
| `.hero__lead` | yes | 1–3 sentences. Capped by `.measure` behaviour built into the component. |
| `.hero__specs` | optional | `<dl>`, **3–4** `.hero__spec` pairs. Values are mono. Omit entirely rather than pad. |
| `.hero__actions` | yes | Max 2 buttons: one `.btn--primary`, one `.btn--dark`. |
| `.hero__media` | default variant: yes | `<figure>` + `<img width height alt>` + `.hero__media-caption` carrying real spec text. |

## CSS contract

- Layout: `.hero__grid` = `7fr 5fr` at ≥1024px, `gap: clamp(32px, 5vw, 96px)`; single column below.
- Type: `.hero__title` inherits `--text-display-xxl` (600 / 1.04 / −0.025em). Do not add a `.t-*` class on top.
- Surface: light hero rides `--color-concrete`; `.hero--ink` uses `--color-ink` with `--color-text-on-dark`.
- Radius 0. No shadow. No decorative shapes.

## JS

None. The hero must render fully with JS disabled. `.reveal` is permitted on `.hero__body` but the hero must be readable if the observer never fires (base `.reveal` state must not be `opacity: 0` without the `.is-visible` fallback already shipped).

## Accessibility

- Exactly one `<h1>` on the page, and it is `.hero__title`.
- `aria-labelledby="hero-h"` on the `<section>`.
- `alt` describes the crane and its duty facts; never "hero image" or empty (the image is content here).
- Text over image: 4.5:1 minimum for anything below `--text-display-l`; 3:1 for the display line. Overlay gradient is mandatory.
- `.btn__glyph` is `aria-hidden="true"`.
- Focus ring: 2px copper at 2px offset — inherited, do not override.

## Review gates

- [ ] One hero, one `<h1>`.
- [ ] `hero__specs` has 3–4 pairs or is absent.
- [ ] ≤2 actions, ≤1 primary.
- [ ] Image has `width`, `height`, spec-bearing `alt`.
- [ ] Overlay present if text sits on the image; contrast measured.
- [ ] 360px: title does not break mid-word; media below text.
- [ ] Renders with JS off.
