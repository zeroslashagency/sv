# 05 — MCP Design Workflow (Paper + Pencil)

How the design artifact actually gets made. Two servers, two jobs:

| Server | Job here |
|---|---|
| **Paper** (31 tools, local, offline) | Workspace scaffolding, file/dir creation, token registry, active-file tracking. Workspace root is `/Users/xoxo/Documents/resreah` — all paths are relative to it, so this project is `sv/svmh-v2/…` |
| **Pencil** (9 tools) | The `.pen` design file: create, read, validate, screenshot, export |

**Hard rule:** `.pen` files are encrypted. Never `read_file`, `grep`, `cat` or edit them directly — only `pencil__*` tools. A direct read corrupts nothing but returns garbage and wastes a turn.

---

## 1. Paper — already done

```
paper__create_artboard  sv/svmh-v2/00_PLAN
paper__create_artboard  sv/svmh-v2/01_DESIGN/{tokens,refboards,pen,exports}
paper__create_artboard  sv/svmh-v2/02_WIREFRAMES/{lofi,annotations}
paper__create_artboard  sv/svmh-v2/03_BUILD/assets/{css,js,img}
```

Remaining Paper use:
- `paper__create_tokens` — register the design-token summary in the workspace so any later agent picks up the palette without re-deriving it.
- `paper__open_file` — set the active target when switching focus between wireframe and build.
- `paper__list_files` / `paper__get_children` — verify the tree.

## 2. Pencil — the exact call order

Every session that touches the design file follows this sequence. Skipping step 1 makes every later call fail, because the schema is required to construct valid input.

```
1. pencil__get_editor_state { include_schema: true }
      └─ mandatory first call. Returns the current .pen schema.

2. pencil__get_guidelines { category: "guide" }          → list available guides
   pencil__get_guidelines { category: "guide", name: X }  → load the one we need
   pencil__get_guidelines { category: "guide", name: X, params: {...} }
      └─ 3-step flow: list → load → load with params.
   pencil__get_guidelines { category: "style" }           → same flow for style rules

3. pencil__batch_design { filePath: "sv/svmh-v2/01_DESIGN/pen/svmh-v2.pen", input: {...} }
      └─ creates variables, then frames, then content. One board per call.

4. pencil__get_variables { filePath }                      → confirm tokens landed
   pencil__snapshot_layout { filePath, problemsOnly: true } → catch layout errors
   pencil__get_screenshot { filePath, nodeId }              → visual check (use sparingly, it is expensive)

5. pencil__export_html { filePath, nodeIds, outputPath: "sv/svmh-v2/01_DESIGN/exports", format: "html-css" }
   pencil__export_nodes { filePath, outputDir: "sv/svmh-v2/01_DESIGN/exports", format: "png", scale: 2 }
      └─ exports are reference for the hand-build, not the shipped code.
```

## 3. Variable seeding

Before any frame is drawn, the palette, type scale and spacing from `../01_DESIGN/tokens/tokens.json` get created as `.pen` variables via `batch_design`. Two themes:

- **Light** — `concrete` surface, `ink` text
- **Dark** — `ink` surface, `on-dark` text

Both share the single `copper` accent. Naming inside the `.pen` file mirrors `tokens.json` exactly (`color/base/concrete`, `color/accent/copper`, `type/display-xl`, `space/band-y`) so a token change is a find-and-replace, not a redesign.

## 4. Board sequence

Order matters — the system gets validated on the two hardest templates before the long tail is drawn.

| # | Board | Why this order |
|---|---|---|
| 1 | `00-foundations` | Palette swatches, type specimen, spacing ruler, icon set. Proves the tokens read correctly at size |
| 2 | `01-components` | Header, buttons, product card, index row, stat lockup, spec table, comparison table, process chips, RFQ fields, trust strip, footer |
| 3 | `02-home-desktop` | Hardest composition. If the hero doesn't work, the system is wrong |
| 4 | `03-home-mobile` | 390px. Validates the type scale actually collapses |
| 5 | `04-product-desktop` | Highest-value template (20 instances) |
| 6 | `05-product-mobile` | |
| 7 | `06-ladle-niche` | The differentiator, drawn deliberately not derived |
| 8 | `07-location-bangalore` | Local SERP flagship |
| 9 | `08-industry-foundry` | Comparison-table-driven layout |
| 10 | `09-case-study` | |
| 11 | `10-resource-article` | Reading measure + sticky TOC |
| 12 | `11-rfq-stepped` | The conversion engine, all 4 steps |

## 5. Where designs come from

Reference imagery in `../../refer/` is **art direction only** — patterns get abstracted through `../01_DESIGN/refboards/REFERENCE_DISTILLATION.md`, never traced. Two of those boards are Russian-market equipment sites and one is a Dribbble sports concept; copying their layouts wholesale would produce a site that doesn't fit a Bengaluru crane manufacturer. The rules survive the translation; the compositions don't.

Product imagery: SVMH's own PDF-extracted images in `../../assets/company/` and `../../website/images/` are the starting library. Those are brochure scans, so most will need a duotone treatment or replacement with new photography. The client asset request in `00_MASTER_PLAN.md` §Gate 0 covers this.

## 6. Existing `.pen` files

`../../website/sv.pen` (1.7 MB) and `../../research/designs/SVMH_Protocol_Mockup.pen` hold the earlier direction (Anton headlines, Inter body, warm concrete `#E7E1D8` / `#211D18` / `#7C6F62`). Worth reading via `pencil__batch_get` for continuity — the new palette is a deliberate evolution of it, not a break — but the new work lives in a **fresh file** at `01_DESIGN/pen/svmh-v2.pen`. The old files stay untouched.

## 7. Handoff to build

```
.pen board ──► export_html (html-css) ──► reference only
     │
     └──► hand-authored 03_BUILD/*.html + assets/css/tokens.css
```

Exported HTML is never shipped. Generated markup carries layer-derived class names, absolute positioning and no semantic structure — it fails the accessibility and SEO requirements in `00_MASTER_PLAN.md` §8. It is read as a measurement reference while the real page is written by hand with proper landmarks, headings and schema.

`assets/css/tokens.css` is generated from `tokens.json` so the build and the design file cannot drift.

## 8. Session checklist

- [ ] `pencil__get_editor_state { include_schema: true }` called first
- [ ] Guidelines loaded (3-step flow) before designing
- [ ] Variables verified with `get_variables` after seeding
- [ ] `snapshot_layout { problemsOnly: true }` clean before screenshotting
- [ ] Screenshots used sparingly
- [ ] Design QA checklist from `../01_DESIGN/DESIGN_SYSTEM.md` §8 run on each board
- [ ] Exports written to `01_DESIGN/exports/`, never into `03_BUILD/`
