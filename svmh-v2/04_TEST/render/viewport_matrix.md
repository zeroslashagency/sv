# Viewport matrix

The DNA spec requires no horizontal scroll from 360 to 1920px. These are the
widths where something in the system actually changes, so they are the ones
worth checking.

| Width | Why this width | What changes here |
|---:|---|---|
| 360 | Smallest phone still in use | Page gutter drops to 0; stage stops overlapping — knockout goes static above the cut-out; specs go single column; band top padding grows so the S3 frame clears the heading; a wide data table may scroll inside its own wrapper |
| 390 | Modern iPhone | Same as 360; confirms nothing is tuned to one exact width |
| 640 | The `max-width: 640px` breakpoint edge | Last width where the narrow rules apply. Check both 640 and 641 |
| 768 | Tablet portrait, `min-width: 768px` | Panel rows and stat rows become three-up; readout cells stop wrapping |
| 900 | `min-width: 900px` | Split rows become 5fr/7fr two-column; tables must stop clipping at or above this width |
| 1024 | `min-width: 1024px` | Desktop nav replaces the overlay menu |
| 1440 | Design reference width | The layout the bands were composed against; knockout occlusion should read 25–45% |
| 1920 | Large desktop | `--max-content` caps the page; gray bands must not touch the viewport edge |

## Per-page focus

| Page | Watch especially |
|---|---|
| `index.html` | Hero stage occlusion; the single navy band; card grid at 768 |
| `request-a-quote.html` | The four-step form: one fieldset visible with JS, all four without it; field underlines legible; navy required dot |
| `eot-cranes/double-girder.html` | Three data tables — the leader table must fit its column, the wide matrices may scroll only below 900px; accordion toggles |
| `locations/bangalore.html` | The coverage matrix; the map iframe carries no border; two card rows of three |

## Reduced motion and keyboard

Independent of width, check once per page:

- `prefers-reduced-motion: reduce` — card hover transforms and transitions off.
- Tab through the whole page: focus never disappears, the ring is 2px navy
  (white on the navy band), and the skip link reaches `#main` first.
