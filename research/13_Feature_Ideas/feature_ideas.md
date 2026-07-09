# Feature Ideas — SVMH Website (Phase 1)

Website features that beat competitors, each benchmarked against what the audited competitors do (or fail to do). Grounded in the 8 website audits, SEO research, and product/customer intelligence in this repo (accessed 2026-07-05). Prioritized by impact vs effort.

> **Principle:** SVMH doesn't need to out-spend Konecranes on a global platform. It needs a handful of high-utility, India-first tools that no competitor offers *together* — turning the site from a brochure into a lead engine.

## Feature register

| # | Feature | Competitor benchmark | Expected impact | Effort | Implementation note |
|---|---|---|---|---|---|
| 1 | **On-page smart RFQ (product pre-selected)** | Konecranes/Demag/CM route to separate Contact; Kito gates via PDF | High — captures leads at moment of intent | Low | Reuse IS 3177 field set (capacity, span, duty, lift, environment); progressive form; product ID auto-filled |
| 2 | **Crane selector / duty-class configurator** | No competitor offers a usable one | High — interactive lead capture + qualification | Med | Ask lifts/day + avg load % → suggests M-class + single/double girder; ends in RFQ |
| 3 | **Load / capacity / span calculator** | None in India | High — SEO magnet + engineering trust | Med | Simple SWL/span/duty helper; gate the emailed result for lead |
| 4 | **Spare-parts finder / part-number search** | "Rare in Indian SME sector" | High — recurring revenue + differentiation | High | Searchable DB of crab units, hooks, DSL, gearboxes, ropes; "order pendant station" CTA |
| 5 | **CAD / DWG download library** | Kito gates (7-field form+CAPTCHA); most India sites: none | High — wins specifying engineers/EPCs | Med | Light-gated (email only) 2D/3D files per model |
| 6 | **Downloadable per-model spec sheets** | Street/ABUS trap specs in images | High — trust + snippet/SEO | Med | On-page spec table + clean PDF datasheet per model |
| 7 | **Virtual factory tour / process + FAT video** | SVMH weakness; competitors use stock/text | High — tangible proof text can't match | Med | HD walkthrough: welding, assembly bay, 125% load test |
| 8 | **Project gallery / case studies (industry-tagged)** | Thin in Indian SME segment | High — proof + SEO relevance | Med | Filterable by industry + crane type; named clients where permitted |
| 9 | **Dual-axis navigation (products × industries)** | GH/Demag/Kito do it; Indian players mostly don't | High — best-practice IA (audits' "highest-value copy") | Low | "Industries" mega-menu mirroring product menu |
| 10 | **WhatsApp Business RFQ + click-to-call** | Rare among premium; critical in India | High — matches MSME buying behaviour | Low | Sticky WhatsApp + phone; pre-filled enquiry text |
| 11 | **Sticky "Get a Quote" bar / contextual CTAs** | CM/Kito diffuse CTAs; Street form-heavy | Med — lifts conversion site-wide | Low | Persistent header CTA + per-section CTAs |
| 12 | **AMC / service portal & booking** | Cranedge owns service SEO; makers bury it | Med — recurring revenue, "amc bangalore" thin SERP | Med | Service request form, coverage map, response-time promise |
| 13 | **Comparison tool (single vs double, gantry vs goliath)** | Thin everywhere in India | Med — table-snippet wins + shortlist stage | Low | Interactive/table comparison → RFQ |
| 14 | **Standards explainer (IS 807/3177/4137) module** | "Clear India snippet gap" | Med — authority + PAA/snippet capture | Low | Concise definitions + tables + FAQPage schema |
| 15 | **Coverage / service map (Karnataka/India)** | Konecranes /en-in lacks localization | Med — logistical-feasibility trust signal | Low | Google Maps embed of factory + service reach |
| 16 | **Trust-signal strip (ISO 9001, IS, GST, MSME, years, installs)** | Inconsistent in regional tier | Med — clears credibility hurdle | Low | Above-fold badges + downloadable certs |
| 17 | **Live chat / callback scheduler** | Uneven across competitors | Low–Med — captures hesitant buyers | Low | Business-hours chat + "call me back" |
| 18 | **Product / Offer / Breadcrumb schema (JSON-LD)** | Kito 636 pages w/o Product schema | Med — free rich-result SERP real estate | Low | Structured data on every product page |

## Quick-win bundle (ship first)
Features **1, 9, 10, 11, 16, 6** — all Low/Med effort, High/Med impact, and directly attack the conversion + trust + localization whitespace competitors leave open.

## Moat bundle (build over time)
Features **2, 3, 4, 5, 7** — the interactive tools + spares DB + factory video that create a durable differentiation no Indian competitor currently matches.

## Sources
- `02_Website_Audits/*` (RFQ friction, dual-axis nav, CTA dilution, schema gaps) — 2026-07-05 — High
- `03_SEO_Research/seo_research.md` (calculators, comparisons, standards, local SERP gaps) — High
- `04_Product_Research`, `05_Customer_Research` (IS 3177 RFQ fields, WhatsApp/MSME behaviour, spares demand) — High
- `Website Research and Replication Strategy.docx` (factory-tour & spares-DB opportunities) — High
