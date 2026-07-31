# Contract — `.index-list` / `.index-row` (numbered feature + accordion)

**Status:** shipped. Two modes from one component: interactive accordion, and static numbered index.

## Mode A — accordion (process, FAQ, "what happens next")

```html
<div class="index-list">
  <div class="index-row">
    <h3>
      <button class="index-row__trigger" type="button" aria-expanded="false" aria-controls="p-01">
        <span class="index-row__num">01</span>
        <span class="index-row__label">Enquiry and load study</span>
        <span class="index-row__icon" aria-hidden="true"></span>
      </button>
    </h3>
    <div class="index-row__panel" id="p-01">
      <p class="t-body measure">Lifts per day, average and peak load, span, headroom and power supply are recorded before anything is quoted. Duty class follows from that data, per IS 3177.</p>
    </div>
  </div>

  <div class="index-row">
    <h3>
      <button class="index-row__trigger" type="button" aria-expanded="false" aria-controls="p-02">
        <span class="index-row__num">02</span>
        <span class="index-row__label">Design and technical offer</span>
        <span class="index-row__icon" aria-hidden="true"></span>
      </button>
    </h3>
    <div class="index-row__panel" id="p-02">
      <p class="t-body measure">…</p>
    </div>
  </div>
</div>
```

### Progressive enhancement — mandatory

Panels ship **without** `hidden`. The accordion JS module adds `hidden` on init and sets `aria-expanded="false"`. With JS disabled every panel stays open and the page reads as a plain numbered document. Shipping panels pre-hidden is a defect: it deletes content for no-JS users and for crawlers that do not execute scripts.

### Behaviour

| Aspect | Contract |
|---|---|
| Trigger | Real `<button type="button">` inside the heading element. Never a `<div>` or `<a href="#">`. |
| State | `aria-expanded` on the trigger, `hidden` toggled on the panel. |
| Wiring | `aria-controls` on the trigger === panel `id`. IDs unique per page (`p-01`, `faq-01`, …). |
| Multi-open | Independent rows. Opening one does **not** close others. |
| Keyboard | Space/Enter activate (native button). Tab moves between triggers. No custom arrow-key trap. |
| Motion | Icon rotates, panel appears at `--dur-fast`/`--dur-base`. Under `prefers-reduced-motion` the toggle is instant. |
| Deep link | If a panel must open from a URL hash, the JS module handles it; builders only supply matching `id`s. |

## Mode B — static numbered index

For a set of 3–6 facts that need numbering but no disclosure (from `IMG_6827`'s `01 Air / 02 Sea` hairline cells). No button, no panel, no ARIA state.

```html
<div class="index-list">
  <div class="index-row">
    <span class="index-row__num">01</span>
    <div class="stack stack--sm">
      <h3 class="t-display-m">Girder fabrication</h3>
      <p class="t-body-s text-secondary measure">Plate cut, jigged and welded in-house; camber checked before the crab rails are set.</p>
    </div>
  </div>
</div>
```

Do not mix modes inside one `.index-list`.

## Slots

| Slot | Constraint |
|---|---|
| `.index-row__num` | Mono, weight 300, `--text-index-numeral`. Zero-padded, sequential from `01`, no gaps. |
| `.index-row__label` | Sentence case, 2–6 words. It is the accessible name of the trigger. |
| `.index-row__icon` | `aria-hidden="true"`, empty. CSS draws the +/− state. Never the only state indicator — `aria-expanded` carries it for AT. |
| `.index-row__panel` | One or two `.t-body measure` paragraphs, optionally a `.stack stack--sm` list or a `.spec` line. No cards, no tables, no nested accordions. |

## Composition

- One `.index-list` per band.
- Pair with a `.chips` row above it when the whole sequence should be visible at a glance (see `layout-patterns.md` L6); the chip numbers must match the row numbers exactly.
- Rows are separated by hairlines from the component CSS — no manual dividers.

## Accessibility

- Trigger sits **inside** the heading (`<h3><button>…</button></h3>`), so the row appears in the heading outline.
- Heading level matches document position (h3 under a band's h2).
- 44px minimum trigger height on touch.
- Focus ring 2px copper at 2px offset, not clipped.
- Panel content is normal flow content; do not add `role="region"` unless a label is also supplied.

## Review gates

- [ ] Panels ship visible (no `hidden` in source HTML).
- [ ] `aria-expanded="false"` present on every trigger in source.
- [ ] `aria-controls` matches a unique panel `id`.
- [ ] Numbers sequential, zero-padded.
- [ ] `<button type="button">` inside a heading element.
- [ ] Icon `aria-hidden`.
- [ ] No nested accordion, no card or table inside a panel.
- [ ] With JS off, all content readable.
