# Contract — `.stat-grid` / `.stat`

**Status:** shipped. `.stat--accent` outline treatment is **NEW** and pending the Component Specialist.

## HTML

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
      <div class="stat">
        <p class="stat__value" data-count-to="2006">2006</p>
        <p class="stat__caption">Manufacturing at Harohalli since</p>
      </div>
      <div class="stat">
        <p class="stat__value" data-count-to="125">125<span class="stat__unit">%</span></p>
        <p class="stat__caption">Static overload at factory acceptance test</p>
      </div>
      <div class="stat">
        <p class="stat__value">[CLIENT TO CONFIRM]</p>
        <p class="stat__caption">Cranes installed to date</p>
      </div>
    </div>
  </div>
</section>
```

## Slots

| Slot | Constraint |
|---|---|
| `.stat__value` | The figure. Weight 300, `--text-stat`, tabular figures. Server-rendered with the final value already in the text — the count-up animates *from* zero *to* the same number. |
| `.stat__unit` | Inline `<span>` inside the value. Smaller. `T +`, `%`, `m`, `t/hr`. Never a full word. |
| `.stat__caption` | `.t-body-s`. States what the number measures *and* the basis. "Static overload at factory acceptance test", not "Overload". |

## JS contract

| Attribute | Behaviour |
|---|---|
| `data-count-to="100"` | Count-up module animates 0 → 100 over 1100ms when the element enters view, formatting with `Intl.NumberFormat('en-IN')`. |
| absent | Value renders as authored. **Required** for non-numeric values like `[CLIENT TO CONFIRM]`. |

- The rendered text must equal the final animated value. If they diverge, no-JS users see a different number than JS users — a factual defect, not a cosmetic one.
- Under `prefers-reduced-motion: reduce` the module resolves immediately to the final value.
- Year values (`2006`) must not be thousands-separated — the module handles this; do not wrap years in extra markup.

## Responsive

2-up from 360px, 4-up at ≥768px. Captions wrap to two lines at the smallest width; that is expected. Never truncate a caption.

## Variant — `.stat--accent` (K3 outline numeral)

Pending CSS from the Component Specialist. Rules once available:

- **Maximum one per page**, and only inside `.band--ink`.
- Uses `-webkit-text-stroke: 1px var(--color-outline-stroke)` with a mandatory `@supports not (...)` fallback to solid `--color-text-on-dark`.
- Stroke colour is decorative-contrast only, so the same figure **must** also appear in the `.stat__caption` text (e.g. caption reads "22 crane models designed to date").
- Do not use on a light band; do not use for the most important number on the page.

## Accessibility

- `.stat-grid` is a plain container, not a list, unless the figures are genuinely a list — then use `<ul>`/`<li>`.
- The band needs its own `<h2>` + `aria-labelledby`; a wall of numerals without a heading is not navigable.
- Value + caption are read in order; do not place the caption before the value in DOM to achieve a visual stack — CSS handles order.
- No `aria-live` on stats. The count-up is decorative; announcing it would spam screen readers.
- Contrast: `--color-text-on-dark` on `--color-ink` passes AA. Outline numerals do not, hence the caption duplication rule.

## Review gates

- [ ] Every numeric `.stat__value` has `data-count-to` matching its rendered text.
- [ ] Non-numeric values have no `data-count-to`.
- [ ] Captions state the basis, not just a noun.
- [ ] Units are inside `.stat__unit`.
- [ ] One stat band per page; ≤1 `.stat--accent`, ink band only, figure duplicated in caption.
- [ ] Reduced-motion path verified.
- [ ] 2-up at 360px without caption truncation.
