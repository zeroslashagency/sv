# Contract — `.card` / `.card--product`

**Status:** shipped. The workhorse component: three-doors, product listings, industries, resources, related links.

## Variants

| Class | When |
|---|---|
| `.card` | Text card. Optional `.card__index` numeral. |
| `.card .card--product` | Adds `.card__media` — product, industry and resource cards with imagery. |
| `.band--ink .card` | Automatic dark skin (ink-2 surface, ink-3 hairlines). No extra class needed. |

## HTML — text card

```html
<article class="card">
  <p class="card__index">01</p>
  <h3 class="card__title"><a class="card__link" href="/eot-cranes">New cranes</a></h3>
  <p class="card__text">Specified from your load cycle, not from a catalogue page. Span, hook approach, duty class and power supply are fixed before a drawing is issued.</p>
  <ul class="stack stack--sm t-body-s text-secondary">
    <li>Duty class calculated from lifts per day and average load, per IS 3177</li>
    <li>Girder analysed to IS 807 deflection limits</li>
  </ul>
  <div class="card__foot">
    <span class="card__spec">1 – 100+ T · M3 – M8</span>
  </div>
</article>
```

## HTML — product card

```html
<article class="card card--product">
  <figure class="card__media">
    <img src="assets/img/double-girder-eot.jpg" width="900" height="600"
         alt="Double-girder EOT crane on a 22 m span with the crab centred over the bay">
  </figure>
  <h3 class="card__title"><a class="card__link" href="/eot-cranes/double-girder">Double-girder EOT crane</a></h3>
  <p class="card__text">For spans above 15 m and duty above M6, where hook approach and headroom both matter.</p>
  <div class="card__foot">
    <span class="card__spec">5 – 100+ T · up to 32 m · M5 – M8</span>
  </div>
</article>
```

## Slots

| Slot | Required | Constraint |
|---|---|---|
| `.card__index` | optional | Mono numeral, weight 300, zero-padded, sequential across the grid. Use only when the set is genuinely ordered. |
| `.card__media` | product only | `<figure>` + `<img width height alt>`. Rendered at `aspect-ratio: 3/2`, bleeds to the card edge via negative margins already in CSS. |
| `.card__title` | yes | `<h3>` (or the correct level for its position) wrapping one `.card__link`. `--text-display-m`. |
| `.card__text` | yes | 1–3 sentences. |
| `<ul class="stack stack--sm t-body-s text-secondary">` | optional | Up to 3 evidence bullets. Each cites a standard, a number or a named deliverable. |
| `.card__foot` | recommended | Hairline-topped, bottom-pinned. Holds one `.card__spec` mono line. |

## Interaction contract

- Exactly **one** link per card. `.card__link::after` stretches over the whole card, so a second link would be unreachable.
- If a second action is genuinely needed, drop the stretched pattern: use plain `<a>` in the title and put the secondary link in `.card__foot`, and note it in the PR so review does not flag it.
- Hover / focus-within: border → `--color-hairline-2`, title → `--color-copper`, `translateY(-1px)`. Duration `--dur-fast` (160ms). **Nothing else** — no shadow bloom, no background flood, no scale, no image zoom.
- Cards are not buttons: no `role="button"`, no click handlers.

## CSS contract

- Padding `--space-5`, stepping to `--space-6` at ≥768px.
- Surface `--color-white` on concrete bands; border 1px `--color-hairline`.
- `border-radius` ≤ `--radius-md` (4px). `box-shadow` none or `--elevation-card`.
- `.card__foot` uses `margin-block-start: auto` so feet align across a row of unequal cards — do not add manual spacers.

## JS

None. `.reveal` / `.reveal--stagger` on the parent grid is permitted.

## Accessibility

- `<article>` for standalone content units; `<li>` wrapper if the grid is semantically a list.
- Heading level follows document structure — inside a `<section>` whose heading is `<h2>`, cards use `<h3>`.
- Link text is meaningful on its own ("Double-girder EOT crane", not "Read more").
- Product images need descriptive `alt`; decorative duplicates of adjacent text use `alt=""`.
- Focus ring visible on the card link and not clipped by `overflow` (already handled).
- Touch target: the whole card is the target via the stretched overlay, comfortably ≥44px.

## Review gates

- [ ] One link per card (or documented exception).
- [ ] `card__index` numerals sequential and zero-padded, or absent.
- [ ] Images have `width`, `height`, real `alt`.
- [ ] Hover limited to border + title + 1px lift.
- [ ] Grid is `.grid--cards` (1/2/3), never a forced 4-up.
- [ ] Card feet align across the row.
- [ ] No nested cards.
