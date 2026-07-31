# Contract — `.btn`, `.chips`, `.eyebrow`, `.spec`

**Status:** shipped. Small components, heavily reused, easiest to get wrong.

## `.btn`

### Element choice

| Purpose | Element |
|---|---|
| Navigate to a URL | `<a class="btn" href="…">` |
| Trigger behaviour on the page | `<button class="btn" type="button">` |
| Submit a form | `<button class="btn" type="submit">` |

Never `<div class="btn">`, never `<a href="#">` for behaviour, never a `<button>` for navigation.

### Variants

| Class | Appearance | Budget |
|---|---|---|
| `.btn--primary` | Copper fill, on-accent text | **One per band.** Copper appears ≤3× per viewport across the whole page. |
| `.btn--dark` | Ink fill | Secondary action beside a primary |
| `.btn--ghost` | 1px copper hairline (`--color-copper-wire`), transparent | Tertiary / in-band navigation |
| `.btn--link` | Inline underlined text | Inside prose |
| `.btn--block` | Full width | Mobile form actions only |

```html
<a class="btn btn--primary" href="/request-a-quote">Request a quote<span class="btn__glyph" aria-hidden="true">↗</span></a>
<a class="btn btn--dark" href="/downloads">Download catalogue</a>
<a class="btn btn--ghost" href="/eot-cranes">See all crane types</a>
```

### Rules

- Never two `.btn--primary` adjacent or in the same band.
- Label is a verb phrase naming the outcome: "Request a quote", "Download catalogue", "See double-girder specs". Banned: "Click here", "Learn more", "Submit", "Read more".
- `.btn__glyph` (`↗`) is decorative, `aria-hidden="true"`, and used on outbound/forward actions only. Never the sole indicator of anything.
- Downloads state the format in the label or immediately after: `Download catalogue` + a nearby `<span class="spec">PDF · 2.4 MB</span>`.
- Minimum target 44×44px at all widths.
- Hover: fill darkens to `--color-copper-hover` (primary) or border darkens (ghost), `--dur-fast` (160ms). No lift, no scale, no shadow.
- Focus: 2px copper ring at 2px offset, inherited. Never `outline: none`.
- External links get `rel="noopener"` when `target="_blank"`, and the new-window behaviour is stated in the accessible name.

## `.chips`

Two modes. They do not mix in one list.

### Mode A — process display (non-interactive)

```html
<ul class="chips">
  <li class="chips__item"><span class="chips__label"><span class="chips__num">01</span> Enquiry</span></li>
  <li class="chips__item"><span class="chips__label"><span class="chips__num">02</span> Design</span></li>
  <li class="chips__item chips__item--active"><span class="chips__label"><span class="chips__num">03</span> Fabrication</span></li>
</ul>
```

- Plain `<span>`s. No `role`, no `tabindex`, no click handler.
- Numbers mirror the `.index-list` below it exactly.
- `--active` marks the current stage only where a current stage genuinely exists (e.g. an order-status explainer). Otherwise omit.

### Mode B — filter (interactive)

```html
<ul class="chips" role="group" aria-label="Filter by industry">
  <li class="chips__item">
    <button type="button" data-filter="industry" data-industry="all" aria-pressed="true">All</button>
  </li>
  <li class="chips__item">
    <button type="button" data-filter="industry" data-industry="foundry" aria-pressed="false">Foundry</button>
  </li>
</ul>
<p class="form__status" role="status" aria-live="polite">Showing 12 of 12</p>
```

- Real `<button type="button">` per chip.
- `aria-pressed` reflects state; exactly one pressed per group.
- `role="group"` + `aria-label` on the list.
- A `role="status" aria-live="polite"` result count is **mandatory** — otherwise the filter is silent to screen reader users.
- JS toggles `.filter-hide` on the target rows/cards. Nothing is hidden in source HTML.

### Responsive

Chips scroll horizontally below 768px. They do not wrap to a second row and they do not shrink their type. Ensure the scroll container does not clip focus rings.

## `.eyebrow`

```html
<p class="eyebrow eyebrow--rule">Start here</p>
```

- `--text-micro-caps`: 0.6875rem / 600 / +0.09em / uppercase.
- ≤6 words. Longer uppercase strings hurt legibility.
- `--rule` adds a short leading rule; use it on band heads, plain `.eyebrow` elsewhere.
- It is **not** a heading. Never mark it up as `<h2>`. The real heading follows it.
- Colour is `--color-text-muted` on light, `--color-text-on-dark-muted` on ink. Do not use copper eyebrows — it burns accent budget.

## `.spec` / `.mono`

```html
<span class="spec">80 T · 22 m span · M7</span>
<span class="spec spec--boxed">IS 807</span>
<span class="spec">[CLIENT TO CONFIRM]</span>
```

- IBM Plex Mono, 0.8125rem, +0.01em.
- Permitted content only: measurements, capacities, duty classes, standard numbers, part numbers, index numbers, GST/registration numbers, file sizes, and the `[CLIENT TO CONFIRM]` placeholder.
- Mono prose is a defect.
- `--boxed` adds a hairline box; use for standards badges, sparingly (≤3 per band).
- `[CLIENT TO CONFIRM]` is the only permitted placeholder form. Never a plausible-looking invented figure.

## Review gates

- [ ] Correct element for every button (`<a>` vs `<button>`).
- [ ] ≤1 `.btn--primary` per band, copper ≤3× per viewport.
- [ ] No "Learn more" / "Click here" / bare "Submit" labels.
- [ ] `.btn__glyph` `aria-hidden`, never load-bearing.
- [ ] Chips are all-static or all-buttons, never mixed.
- [ ] Filter chips have `aria-pressed` + `role="group"` + a live result count.
- [ ] Chips scroll, not wrap, on mobile.
- [ ] Eyebrows ≤6 words, not headings, not copper.
- [ ] All mono text is technical data.
- [ ] Unknown values render `[CLIENT TO CONFIRM]`.
