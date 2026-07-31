# 01 — Sitemap & Information Architecture

Derived from the hub-and-spoke cluster map in `../../research/16_Reports/04_SEO_Research_Report.md` §3 and the dual-axis IA the Konecranes audit flags as "the single most copyable structural idea for SVMH".

---

## 1. The organising principle: dual-axis entry

Buyers arrive knowing one of two things — **what machine they need** (product axis) or **what plant they run** (industry axis). A third, smaller group arrives with a **broken crane** (service axis). The IA must serve all three from the header without nesting.

```
                    ┌─────────── PRODUCTS ────────────┐
                    │  what machine do you need?      │
HOME ──► choose ────┼─────────── INDUSTRIES ──────────┤──► PRODUCT PAGE ──► RFQ
         your path  │  what plant do you run?         │
                    ├─────────── SERVICE & SPARES ────┤
                    │  what broke / what's due?       │
                    └─────────────────────────────────┘
```

Home is explicitly a **three-door page**: New Cranes / Spares & Components / AMC Service. That single decision separates SVMH from every competitor whose home page is a brand story.

## 2. Primary navigation

```
[SVMH mark]   Products ▾   Industries ▾   Service & Spares ▾   Resources ▾   Company ▾      🔍   [Get a Quote →]
```

Sticky on scroll, collapses to a 64px bar with the accent-filled CTA cell retained (nav-as-grid pattern from the SwiftCargo board: cells divided by 1px hairlines, right-most cell solid accent).

Mobile: hamburger → full-screen uppercase overlay menu (RM/Terex board pattern), plus a persistent bottom bar: `Call` · `WhatsApp` · `Get a Quote`.

### Products ▾ (mega panel, 2 columns + featured)
```
EOT / Overhead Cranes        Hoists & Components
  Single Girder EOT            Wire Rope Hoist
  Double Girder EOT            Chain Hoist
  Underslung / Monorail        Crab Unit
  Hot Metal / Ladle  ◄ niche   DSL / Shrouded Busbar
Gantry & Goliath               Forged Hooks
  Single Girder Gantry         Rope Drums & Sheaves
  Double Girder Goliath        Gearboxes & Wheels
  Semi-Goliath                 Pendant Cables
  Portable Gantry
Jib & Slewing                [Featured card: Hot Metal / Ladle
  Pillar / Column Jib         Crane — IS 4137, M8 duty.
  Wall-Mounted Jib            View capability →]
  360° Slewing Jib
```

## 3. Full URL map

### Tier 0 — Root & utility
| URL | Template | Priority |
|---|---|---|
| `/` | T1 Home | P0 |
| `/contact` | T7 | P0 |
| `/request-a-quote` | T7 (RFQ full-page) | P0 |
| `/certifications-and-trust` | T7 | P0 |
| `/downloads` | T7 (datasheets, ISO, CAD index) | P0 |
| `/about` | T7 (family story, MD, factory) | P1 |
| `/sitemap.xml`, `/robots.txt` | — | P0 |

### Tier 1 — Product pillars (6) and spokes (14)
| URL | Template | Priority |
|---|---|---|
| `/eot-cranes` | T2 pillar | P0 |
| `/eot-cranes/single-girder` | T2 spoke | P0 |
| `/eot-cranes/double-girder` | T2 spoke | P0 |
| `/eot-cranes/underslung-monorail` | T2 spoke | P1 |
| `/eot-cranes/hot-metal-ladle-foundry` | T2 spoke ★ | P0 |
| `/gantry-cranes` | T2 pillar | P0 |
| `/gantry-cranes/single-girder-gantry` | T2 spoke | P1 |
| `/gantry-cranes/double-girder-goliath` | T2 spoke | P1 |
| `/gantry-cranes/semi-goliath` | T2 spoke | P2 |
| `/jib-cranes` | T2 pillar | P0 |
| `/jib-cranes/pillar-jib` | T2 spoke | P2 |
| `/jib-cranes/wall-mounted-jib` | T2 spoke | P2 |
| `/hoists` | T2 pillar | P0 |
| `/hoists/wire-rope-hoist` | T2 spoke | P1 |
| `/hoists/chain-hoist` | T2 spoke | P2 |
| `/hoists/crab-unit` | T2 spoke | P2 |
| `/crane-spare-parts` | T2 pillar | P0 |
| `/crane-spare-parts/dsl-busbar` | T2 spoke | P1 |
| `/crane-spare-parts/forged-hooks` | T2 spoke | P2 |
| `/services` | T2 pillar (service variant) | P0 |

★ = the foundry/ladle niche wedge. Highest margin, thinnest Indian SERP, matches stated capability.

### Tier 2 — Services detail
| URL | Template |
|---|---|
| `/services/amc-preventive-maintenance` | T2 service |
| `/services/inspection-load-testing` | T2 service |
| `/services/modernization-retrofit` | T2 service |
| `/services/fabrication` | T2 service |
| `/services/operator-training` | T2 service |

### Tier 3 — Industries (6)
`/industries` hub + `/industries/{automotive, steel, power, foundry, cement, construction}` — T4.

### Tier 4 — Locations (local SERP land-grab, Phase 1)
| URL | Notes |
|---|---|
| `/locations` | Coverage hub + service-radius map |
| `/locations/bangalore` | **Flagship.** Directly contests K2 Cranes |
| `/locations/karnataka` | State-level roll-up |
| `/locations/{hosur, mysuru, tumakuru, hubballi}` | Phase 2, only with real service evidence |

Every location page carries NAP-consistent address, GBP embed, local install references, and a named local contact. No thin doorway pages — each needs at least one genuine local project or the page waits.

### Tier 5 — Resources / knowledge hub
| URL | Snippet target |
|---|---|
| `/resources` | Hub |
| `/resources/what-is-an-eot-crane` | Paragraph snippet |
| `/resources/single-girder-vs-double-girder` | **Table snippet** |
| `/resources/crane-duty-class-explained` | Table (M5/M7, FEM 9.511) |
| `/resources/is-807-classification` | **Table — India gap, highest value** |
| `/resources/is-3177-rfq-checklist` | List + doubles as RFQ scaffold |
| `/resources/is-4137-ladle-crane-requirements` | Niche authority |
| `/resources/eot-crane-price-in-india` | **Table — price gap** |
| `/resources/what-does-crane-amc-include` | List snippet |
| `/resources/glossary` | Long-tail catch-all |
| `/resources/calculators` | Phase 3 tools index |
| `/resources/cad-library` | Phase 3 |

### Tier 6 — Proof
`/case-studies` hub + `/case-studies/{slug}` — T5, minimum 5 at Phase 2 exit. Each tagged by industry, capacity, span, duty class.

## 4. Internal linking rules

Three non-negotiable link triangles:

1. **Product → Standards → Comparison → RFQ.** Every money-page links to its governing IS standard explainer, its nearest comparison article, and its own pre-filled RFQ.
2. **Product ↔ Service ↔ Spares.** A crane page links to AMC and to the spares for that crane. A spares page links back to the parent crane. This is what converts the maintenance engineer — the after-sales gatekeeper.
3. **Industry as connector.** Industry pages link laterally to every product used in that industry and to case studies in that industry; product pages link back to the industries they serve.

Blog/guide → money-page handoff is mandatory: no educational article ends without a contextual link to the relevant product page and a soft RFQ CTA.

## 5. Buying-committee mapping

Five roles, from `../../research/16_Reports/09_Conversion_Opportunity_Report.md` and customer intelligence. Each gets an owned surface — nobody has to hunt.

| Role | Cares about | Their surface |
|---|---|---|
| Plant Manager | Uptime, safety liability | TCO block, duty class, safety/compliance section, case studies |
| Procurement Head | Comparable, uniform RFQ | Downloadable datasheets, IS 3177 RFQ form, price bands |
| Maintenance Engineer | Spares lead time (the real gatekeeper) | Spares hub, stocking policy, AMC response commitment |
| MSME Owner | Price, local access, WhatsApp | Price-guidance page, location pages, sticky WhatsApp |
| Consulting Engineer | IS 807/3177 compliance, calcs | Standards explainers, compliance declarations, CAD library |

## 6. Header/footer contract

**Footer** (4 columns + legal bar): product index · industries + locations · service/spares + resources · company + NAP block with GST 29AAKCS6443A1ZB, ISO 9001 badge linking to the actual PDF, MSME mark, phone, WhatsApp, and a one-line map. Legal bar carries CIN, GST, and a "response within [X] working hours" commitment.

**Persistent conversion furniture** on every page: sticky header CTA, mobile bottom bar (Call / WhatsApp / Quote), and a scroll-progress hairline at the very top of the viewport.
