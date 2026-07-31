# Contract — `.spec-table` / `.compare-table`

**Status:** shipped. The credibility component: engineers read these before they read prose.

## HTML — spec table

```html
<div class="spec-table-wrap">
  <table class="spec-table spec-table--leader">
    <caption class="sr-only">Capacity, span and duty class by crane type</caption>
    <thead>
      <tr>
        <th scope="col">Crane type</th>
        <th scope="col">Capacity</th>
        <th scope="col">Span</th>
        <th scope="col">Duty class</th>
        <th scope="col">Standard</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Single-girder EOT</th>
        <td>1 – 15 T</td>
        <td>up to 25 m</td>
        <td>M3 – M6</td>
        <td>IS 807 · IS 3177</td>
      </tr>
      <tr>
        <th scope="row">Double-girder EOT</th>
        <td>5 – 100+ T</td>
        <td>up to 32 m</td>
        <td>M5 – M8</td>
        <td>IS 807 · FEM 9.511</td>
      </tr>
    </tbody>
  </table>
</div>
<p class="spec-table__note">Deflection limited to L/750 per IS 807. Duty class derived from lifts per day and average load per IS 3177. Spans beyond the table are engineered to order.</p>
```

## HTML — compare table

```html
<div class="compare-table-wrap">
  <table class="compare-table">
    <caption>How an SVMH crane is specified against a catalogue-selected crane</caption>
    <thead>
      <tr>
        <th scope="col">What gets fixed</th>
        <th scope="col" class="compare-table__svmh">SVMH</th>
        <th scope="col">Catalogue selection</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row" class="compare-table__spec">Duty class</th>
        <td class="compare-table__svmh">Calculated from your load cycle per IS 3177</td>
        <td>Assumed from capacity alone</td>
      </tr>
    </tbody>
  </table>
</div>
```

## Structure rules

| Rule | Detail |
|---|---|
| `<caption>` mandatory | Every table. `.sr-only` if the band heading already carries it visually. Describes what the rows contain, not "Table 1". |
| Scope everywhere | `scope="col"` on every `<thead>` cell; `scope="row"` on the first cell of every body row, which must be a `<th>`. |
| Wrapper required | `.spec-table-wrap` / `.compare-table-wrap`. It provides the horizontal scroll and the `--elevation-float` affordance on mobile. A bare `<table>` breaks at 360px. |
| No layout tables | Tables carry tabular data only. |
| No nested tables | Ever. |
| Column count | 3–6. Above 6, split into two tables by subject. |
| Note placement | `.spec-table__note` goes **after** the wrapper, not inside the table. Footnote-grade detail, standards references, and "engineered to order" caveats live here. |
| Unconfirmed data | `<span class="spec">[CLIENT TO CONFIRM]</span>` inside the cell. Never invent a number, never leave a cell empty. Use `—` only when the row genuinely does not apply. |

## Responsive

- The table keeps its natural column widths; the wrapper scrolls. Columns are never dropped, wrapped into cards, or converted to definition lists — cross-row comparison is the point.
- On touch, the wrapper is scrollable with momentum and shows the float shadow as the affordance.
- Tabular figures (`font-feature-settings: "tnum"`) are already applied — numbers align across rows. Do not override `font-variant-numeric`.

## Visual contract

- Row separation by hairlines; optional `--color-concrete-3` stripe.
- `.spec-table--leader` emphasises the first column (row headers).
- `.compare-table__svmh` highlights the SVMH column with a subtle wash, not copper fill.
- Zero radius on cells. No shadow except the wrapper scroll affordance.

## JS (optional filtering)

Applies only to long tables (e.g. locations, spares).

```html
<ul class="chips" role="group" aria-label="Filter by region">
  <li class="chips__item"><button type="button" data-filter="region" data-region="all" aria-pressed="true">All</button></li>
  <li class="chips__item"><button type="button" data-filter="region" data-region="karnataka" aria-pressed="false">Karnataka</button></li>
</ul>
<p class="form__status" role="status" aria-live="polite">Showing 12 of 12 rows</p>
```

- Filter module toggles `.filter-hide` on `<tr>` elements matched by `data-region` / `data-tier` / `data-threat`.
- `aria-pressed` reflects active state; exactly one active per filter group.
- The `role="status"` count is mandatory — a silent filter is invisible to screen reader users.
- With JS off, all rows show and the chips render as inert buttons. Acceptable; do not hide rows in source.

## Accessibility

- Never convey a value by colour alone (e.g. a green cell for "certified"); include text.
- Do not use `aria-label` on the table in place of `<caption>`.
- Long tables get a visible caption rather than `.sr-only`, so sighted users get the same orientation.
- If a cell links to a PDF, the link text names the document and the format: `ISO 9001 certificate · PDF`.

## Review gates

- [ ] `<caption>` on every table.
- [ ] `scope` on all header cells; first body cell is a `<th scope="row">`.
- [ ] Wrapper present.
- [ ] 3–6 columns.
- [ ] Notes outside the table.
- [ ] Unknown values marked `[CLIENT TO CONFIRM]`, none invented.
- [ ] Horizontal scroll works at 360px with columns intact.
- [ ] If filtered: `aria-pressed` + `role="status"` count present, all rows visible with JS off.
