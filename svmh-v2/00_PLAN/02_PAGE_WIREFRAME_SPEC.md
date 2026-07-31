# 02 — Page & Wireframe Spec

Section-by-section specification for all 7 templates. Each section states its **intent** (what job it does), **content source**, **reference pattern** from `../01_DESIGN/refboards/REFERENCE_DISTILLATION.md`, and **acceptance criteria**.

Greybox HTML wireframes go in `../02_WIREFRAMES/lofi/`, one file per template, named to match the T-codes below.

---

## Global furniture (every page)

| Element | Spec |
|---|---|
| Scroll progress | 2px copper hairline, top of viewport, `aria-hidden` |
| Header | Nav-as-grid, hairline cells, right-most cell solid copper `Get a Quote →`. Sticky, collapses to 64px |
| Mobile bottom bar | `Call` · `WhatsApp` · `Get a Quote`, always visible below 768px |
| Trust strip | Ink band, above the first fold break |
| Footer | 4 columns + legal bar with NAP, GST, CIN, ISO PDF link, response-time commitment |
| Meta | Unique title + description on every page. Non-negotiable |
| Schema | Organization + LocalBusiness sitewide; Product / FAQPage / Article per template |

---

## T1 — Home (`/`)

The job: in one screen, prove SVMH is a real manufacturer, and in the second screen, route the visitor to one of three doors. It is not a brand story.

| # | Section | Intent | Content source | Reference | Acceptance |
|---|---|---|---|---|---|
| 1 | **Hero** | One dominant message + one CTA | Brief §products; positioning "20-year TCO, not price of steel" | 6831 crane-against-sky + 6822 headline-split-around-cutout | Ghost watermark `CRANES`; H1 "EOT & GANTRY CRANES BUILT TO IS 807 — BENGALURU, SINCE 2006" split around a cut-out double-girder crane; primary `Request a Quote →`, ghost `Download catalogue`; dashed callout `Ladle crane · 40 T · M8 duty`; copper circular ↘. **No carousel.** |
| 2 | **Trust strip** | Kill the "are they real?" objection before scroll 2 | Brief: ISO 9001, GST 29AAKCS6443A1ZB, MSME, 2006 | Board 6827 hairline logo cells | Ink band, 6 cells, ISO cell links the actual PDF. Unverified counts withheld, not invented |
| 3 | **Three doors** | Route by intent, not by brand | Content plan §1 home "choose your path" | 6823 alternating audience bands | Three full-bleed bands: New Cranes / Spares & Components / AMC Service. Each: display-l heading, 3 bulleted benefits, undersized copper CTA, cut-out overhanging the band edge |
| 4 | **Product index** | Show the range fast | Sitemap product pillars | 6819 whole-card accent hover grid | 6 cards (EOT, Gantry, Jib, Hoists, Spares, Services). Whole card fills copper on hover. Each card carries a capacity range in spec-mono |
| 5 | **Foundry / ladle wedge** | Lead with the differentiator | Brief hot/ladle niche; SEO §9.4 India-vs-China gap | 6821 ghost product name clipped by photo | Copper-soft wash band, IS 4137 reference, one real project or `[CLIENT TO CONFIRM]`, CTA to the niche page |
| 6 | **Proof band** | Operational credibility, not financial | Case studies (Phase 2); brief capability | 6820 outline-stroke stats over imagery | 4 stat lockups: `100 T` max capacity · `SINCE 2006` · `IS 807 / 3177 / 4137` · `[N] INSTALLS`. Outline numerals over a factory frame |
| 7 | **Why not the cheap quote** | Reframe to TCO + safety liability | Recommendations; conversion report §4 | 6818 pain × common × our-solution table | 3-col comparison table, SVMH column with copper-soft wash, expandable rows, `scope` on headers |
| 8 | **How we deliver** | De-risk the process | Content plan; IS 3177 flow | 6817 numbered 01–06 accordion + 6828 process chips | Chips `ENQUIRY ▶▶ DESIGN ▶▶ FABRICATION ▶▶ FAT ▶▶ INSTALL ▶▶ AMC`, then 01–06 accordion rows with detail |
| 9 | **Industries** | Second axis entry | Sitemap tier 3 | 6818 2×2 solution cards, one inverted | 6 tiles: automotive, steel, power, foundry, cement, construction. Foundry tile inverted dark |
| 10 | **Local** | Own Bengaluru intent from the home page | SEO tier 1; move #2 | 6822 floating container over darkened photo | Harohalli KIADB address, service-radius statement, GBP embed, `Cranes in Bangalore →` |
| 11 | **Resources teaser** | Capture research-stage engineers | Content plan resource cluster | 6818 resource row with PDF lists + video | 3 links (IS 807 explainer, single-vs-double, price guide) + factory/FAT video thumb |
| 12 | **RFQ** | Convert on-page, no redirect | Conversion report P0 | 6827 inline underline-input calculator | Compact 4-field entry that hands off to the full stepped RFQ with values carried over |

## T2 — Product money-page (`/eot-cranes`, `/eot-cranes/double-girder`, …)

The highest-value template. Twenty instances. The job: answer a procurement engineer's entire question set without them leaving the page.

| # | Section | Intent | Acceptance |
|---|---|---|---|
| 1 | Breadcrumb + micro-caps eyebrow | Orientation + internal linking | `Products / EOT Cranes / Double Girder`, schema BreadcrumbList |
| 2 | Hero | One product, one claim, one CTA | Ghost watermark = product name; cut-out render occluding it; H1 `DOUBLE GIRDER EOT CRANE — UP TO 100 T`; capacity/span/duty in spec-mono; `Request a Quote` + `Download datasheet (PDF)` |
| 3 | Spec table | Comparability for procurement | Capacity, span, lift height, duty class, travel speeds, power supply, hook approach. Dotted-leader alignment, `scope`, caption, horizontal scroll on mobile |
| 4 | Configuration / variants | Show engineering depth | Numbered 01–0N index rows per variant with expandable detail |
| 5 | Standards & compliance | Win the consulting engineer | IS 807 / IS 3177 / FEM 9.511 (and IS 4137 on the ladle page) with links to the explainer articles and a downloadable compliance declaration |
| 6 | **INR price band** | The gap premium brands refuse to fill | A *band* with cost-factor explanation — span, duty class, hoist type, power supply, site conditions — plus `warn`-coloured "indicative, not a quotation" note. Links to `/resources/eot-crane-price-in-india` |
| 7 | Application / industries | Second-axis lateral links | Industry chips linking to the 6 industry pages |
| 8 | Proof | Reference installs for this exact product | Industry-tagged install cards with capacity/span/duty captions |
| 9 | Spares & service triangle | Convert the maintenance gatekeeper | Links to the spares for this crane, the AMC page, stocking policy, and response-time commitment |
| 10 | FAQ | Featured-snippet harvest | 5–8 question-phrased H3s, FAQPage schema |
| 11 | **Inline RFQ, product pre-selected** | The single highest-ROI element on the site | Product field pre-filled and visible; IS 3177 sequence; WhatsApp fast-track alongside |
| 12 | Related products | Reduce dead ends | 3 cards, whole-card copper hover |

**Ladle/foundry variant** additionally carries: molten-metal handling safety block, M8 duty justification, IS 4137 clause references, thermal-shield/redundant-brake detail, and an explicit India-vs-import cost-and-lead-time argument.

## T3 — Location page (`/locations/bangalore`)

The job: beat K2 Cranes on SVMH's home turf. Must not read as a doorway page.

1. Hero: `EOT CRANE MANUFACTURERS IN BANGALORE` + local photograph, not stock.
2. NAP block: full Harohalli KIADB address, phone, WhatsApp, GST, hours — identical string everywhere on the site.
3. Service-radius statement with named coverage (Peenya, Bommasandra, Harohalli, Hosur road belt) and a stated response window.
4. Local install references with area names and industry tags.
5. Products available locally, linking to money-pages.
6. Local AMC / spares availability + stocking policy.
7. Why local matters: response time, site visits, no freight premium, Kannada/local-language support.
8. GBP embed + directions.
9. Local FAQ (FAQPage schema) + LocalBusiness schema with `areaServed`.
10. RFQ with city pre-filled.

Rule: no city page ships without at least one genuine local project reference.

## T4 — Industry page (`/industries/foundry`)

1. Hero with an isometric line-art plant schematic (6818 pattern).
2. `Pain point × Common solution × SVMH solution` comparison table — the core of the template.
3. Recommended cranes for this industry (product cards).
4. Quantified project cards: capacity, span, duty, industry, outcome.
5. Compliance notes specific to the industry (IS 4137 for foundry, hygiene/washdown for food, etc.).
6. Resource downloads: buyer's guide, datasheets, whitepapers.
7. Industry-contextualised RFQ.

## T5 — Case study (`/case-studies/{slug}`)

1. Hero: ghost project name clipped by the install photo (6821).
2. Asymmetric dark/light split: `SITUATION` / `TASK` (6826).
3. `SOLUTION` band with the spec readout in spec-mono.
4. `GOAL / RESULT` two-column outcome block (6831 laurel pattern).
5. Photo wall: fabrication → FAT → installed.
6. Client quote if permitted; otherwise the MD's engineering note.
7. Related products + `Start a similar project` RFQ.

## T6 — Resource / standards article (`/resources/is-807-classification`)

1. H1 phrased as the query.
2. **40–55 word lead answer** in the first paragraph — the snippet-winning mechanic.
3. Table or ordered list matching the target snippet type (table for comparisons, `<ol>` for processes).
4. Body at `68ch` measure with a sticky table of contents on desktop.
5. Diagram: duty-class chart, girder comparison, or RFQ flow.
6. Related standards cross-links.
7. Money-page handoff — mandatory, no article ends without one.
8. Soft RFQ + downloadable version of the table.
9. Article + FAQPage schema, author = SVMH engineering, dated.

## T7 — Utility pages

**`/request-a-quote`** — full-page stepped RFQ, `01 — 04` counter, IS 3177 sequence, WhatsApp fast-track, response-time promise, trust strip. See `04_CONVERSION_SPEC.md`.

**`/certifications-and-trust`** — ISO 9001 PDF viewer + download, IS declarations, GST/MSME, factory infrastructure list, equipment list, QA process, FAT protocol, factory video.

**`/downloads`** — filterable index (datasheets / certificates / catalogues / CAD) using the 6818 resource-row pattern. Ungated by default; the research shows gating is what competitors get wrong.

**`/about`** — family-owned story since 2006 (group lineage 1994), MD Shri D. Umapathi portrait + quote, board, factory, capability stats. Humanise, as the Street Crane reference does. No financial claims.

**`/contact`** — NAP, map, department routing, WhatsApp, and a callback scheduler (leveraging the flat family structure — a buyer can reach the MD).

---

## Wireframe deliverables

| File | Template |
|---|---|
| `../02_WIREFRAMES/lofi/T1-home.html` | Home |
| `../02_WIREFRAMES/lofi/T2-product.html` | Product money-page (double-girder as the exemplar) |
| `../02_WIREFRAMES/lofi/T2b-ladle.html` | Ladle/foundry variant |
| `../02_WIREFRAMES/lofi/T3-location.html` | Bangalore |
| `../02_WIREFRAMES/lofi/T4-industry.html` | Foundry |
| `../02_WIREFRAMES/lofi/T5-case-study.html` | Case study |
| `../02_WIREFRAMES/lofi/T6-resource.html` | IS 807 article |
| `../02_WIREFRAMES/lofi/T7-rfq.html` | Full RFQ |

Greybox rules: no colour beyond greys plus one copper marker, no imagery beyond labelled placeholder boxes stating what the image must show, real copy stubs from the content plan, and every section labelled with its number from this spec. Annotations live alongside in `../02_WIREFRAMES/annotations/`.
