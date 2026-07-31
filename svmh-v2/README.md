# SVMH v2 — Clean-Room Site Build

A **brand-new, self-contained** build for S.V. Material Handling System Pvt. Ltd. (SVMH), Harohalli KIADB, Bengaluru.

This folder is deliberately independent of the strategy pages at the repo root (`../index.html`, `../company.html`, `../competitors.html`). Those stay untouched — they were the research deliverable. This is the product.

**The application is `03_BUILD/`.** Everything else plans it, designs it, tests it, or is an explicitly quarantined draft. If you only open one folder, open that one.

## What lives here

```
svmh-v2/
├── README.md                     ← you are here
├── 00_PLAN/                      ← the plan. Read in order.
│   ├── 00_MASTER_PLAN.md         Goals, quality bar, phases, gates, definition of done
│   ├── 01_SITEMAP_IA.md          Full URL map, dual-axis nav, page inventory, templates
│   ├── 02_PAGE_WIREFRAME_SPEC.md Section-by-section wireframe spec for every template
│   ├── 03_CONTENT_SEO_MATRIX.md  Page → keyword → funnel → proof → CTA matrix
│   ├── 04_CONVERSION_SPEC.md     RFQ engine, WhatsApp, trust strip, objection map
│   └── 05_MCP_DESIGN_WORKFLOW.md Paper + Pencil MCP pipeline, exact call order
├── 01_DESIGN/
│   ├── 07_DNA_RM_TEREX.md        ★ AUTHORITATIVE design law. Supersedes the two below
│   │                               on palette, type and surfaces. Signature moves S1–S5
│   ├── 06_DESIGN_RECALIBRATION.md  Superseded — kept for the reasoning trail
│   ├── DESIGN_SYSTEM.md            Superseded on palette/type; still valid on motion + a11y
│   ├── tokens/tokens.json        Machine-readable tokens (feeds .pen variables + CSS)
│   ├── refboards/                Reference distillation from ../refer/
│   ├── pen/                      .pen design files (Pencil MCP only — never Read/Grep)
│   └── exports/                  PNG/HTML exports out of Pencil
├── 02_WIREFRAMES/
│   ├── lofi/                     Greybox HTML wireframes, one per template
│   └── annotations/              Per-section intent, data source, acceptance criteria
├── 03_BUILD/                     ★ THE APPLICATION. Static site, no build step
│   ├── index.html                Homepage
│   ├── request-a-quote.html      RFQ engine — read the form's SECURITY comment
│   ├── eot-cranes/               Product detail pages
│   ├── locations/                Local SEO pages
│   └── assets/
│       ├── css/                  tokens → base → components → dna. Load order matters
│       ├── js/                   site.js — nav, accordions, form stepper
│       ├── docs/                 Client documents for download (certificates)
│       └── img/                  Filed by DNA role: cutouts, bands, cards, people
├── 04_TEST/                      ← verification. `cd 04_TEST && ./run.sh`
│   ├── run.sh                    Runs every static suite + an HTTP check, exits non-zero
│   ├── conftest.py               Shared helpers; `--refresh` regenerates fixtures
│   ├── static/                   No browser needed. The real gate
│   ├── render/                   Browser procedure + viewport matrix (needs a session)
│   ├── fixtures/                 Expected state, so a failure says what changed
│   └── reports/                  Run output (gitignored)
├── 05_DEMO/                      ← NOT the app. Quarantined pre-DNA drafts
├── tools/                        ← build-time scripts: assets, sitemap, screenshot decoder
└── .agents/                      ← orchestration state: task board, manifest, handoffs
```

## The design authority

`01_DESIGN/07_DNA_RM_TEREX.md` is the law. Three documents in that folder
describe design, and they disagree, because the direction changed mid-build. The
DNA document wins on palette, type scale and surfaces. Concrete and copper are
**retired** — the palette is cool grey, white and a single navy accent. The older
documents stay for the reasoning trail, and `04_TEST/static/test_dna_rules.py`
enforces the DNA rules so the disagreement cannot quietly resolve the wrong way.

Five signature moves, each mandatory somewhere on a page: the giant knockout
wordmark (S1), the background-free product cut-out (S2), the label/counter frame
(S3), the three-up numbered panel row (S4), the stat lockup (S5).

## Ground truth inputs

| Input | Path | Used for |
|---|---|---|
| Design reference boards | `../refer/` (16 boards) | Visual quality bar, layout grammar |
| Source photography | `../assets/company/` (24 frames) | Every build image traces to one frame here |
| Client brief | `../research/00_CLIENT_BRIEF.md` | Company facts, products, niche |
| Actionable recommendations | `../research/16_Reports/10_Actionable_Recommendations.md` | The 9 ranked strategic moves |
| Feature gap analysis | `../research/16_Reports/06_Feature_Gap_Analysis.md` | 20 features, 3 tiers |
| SEO report | `../research/16_Reports/04_SEO_Research_Report.md` | Cluster map, keyword tiers |
| Conversion report | `../research/16_Reports/09_Conversion_Opportunity_Report.md` | RFQ flow, trust order |
| Content plan | `../research/12_Content_Ideas/content_plan.md` | Page-level content briefs |

## Rules for this folder

1. **No invented facts.** Every number, cert, or client claim traces to the research corpus or gets marked `[CLIENT TO CONFIRM]`.
2. **No lorem ipsum.** Wireframes carry real copy stubs from the content plan.
3. **Static only.** HTML/CSS/JS, no build step, no framework — matches how the client can host and maintain it.
4. **`.pen` files are encrypted.** Touch them only through `pencil__*` MCP tools.
5. **Design changes flow tokens → .pen → wireframe → build.** Never patch the build first.
6. **No generated imagery.** Every asset is cut from a real photograph in `../assets/company/`.
7. **Nothing in `05_DEMO/` ships.** A promoted draft is rewritten in `03_BUILD`, not moved.

## Working on it

```bash
cd 03_BUILD && python3 -m http.server 8080    # serve
cd 04_TEST  && ./run.sh                        # verify — exits non-zero on failure
python3 tools/make_assets.py                   # regenerate band + card images
python3 tools/make_cutouts.py                  # regenerate the S2 cut-outs
```

Run `04_TEST/run.sh` before calling any change done. It catches the failures that
actually happened during this build: an asset that does not exist, a cut-out
upscaled past its source pixels, a counter sequence with a gap, a retired colour
creeping back, a form losing its security gate, a placeholder hostname reaching
the structured data.

The suite has been mutation-tested — each of those failure modes was deliberately
introduced and confirmed to turn the run red. That is the only evidence worth
having that a green run means something.

## Current state

Four pages built and passing: homepage, RFQ, double-girder EOT, Bangalore. The
sitemap in `00_PLAN/01_SITEMAP_IA.md` is larger than what exists — roughly 39
routes are linked but not yet built. `04_TEST/static/test_links.py` lists them on
every run, so the roadmap stays visible instead of drifting into broken links.
