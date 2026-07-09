# Engineering Resources Plan — S.V. Material Handling System Pvt Ltd (SVMH)

**Client:** S.V. Material Handling System Pvt Ltd (SVMH), Harohalli KIADB, Bengaluru — svind.co.in
**Purpose:** A concrete plan for the downloadable and interactive engineering assets SVMH's new site should offer — spec-sheet templates, a CAD/DWG library, load/selection calculators, maintenance & inspection checklists, installation guides, and safety/compliance documents. These are the "hard" engineering resources that build technical credibility, earn links, and convert engineers upstream of IndiaMART.
**Date prepared / all live sources accessed:** 2026-07-05
**Method:** Grounded in this repo's prior research (`03_SEO_Research`, `06_Industry_Research`, `08_Brochures`, `10_Certifications`, `09_Case_Studies`, `02_Website_Audits/01_Konecranes_audit.md`) + fresh live competitor verification via firecrawl_search on 2026-07-05.
**Companion file:** `12_Content_Ideas/content_plan.md` (editorial/SEO content; these resources are its downloadable/interactive layer).

---

## 0. Why engineering resources are the sharpest wedge

The research is blunt: **SVMH currently has no downloadable brochure, no catalogue, no company profile PDF, no video, no calculator, no CAD library** — svind.co.in routes to IndiaMART. Yet "even sub-scale regional rivals (Top Crane, Vikrant, S. Cranes, Shubhlaxmi) publish a downloadable PDF catalogue" (`08_Brochures/brochures_catalogs.md` §takeaways, accessed 2026-07-05, High). Meanwhile larger and Chinese competitors publish interactive tools (wheel-load calculators, crane configurators) and CAD-drawing libraries that SVMH's segment in India largely does *not* — an open flank.

Two evidence-backed principles shape this plan:
- **Table-stakes first:** a product datasheet set + corporate profile + one catalogue is the minimum viable parity move (`08_Brochures` §1). Without it SVMH looks less credible than tiny rivals.
- **Then leapfrog:** interactive calculators, a CAD/DWG library, and India-specific (IS 807 / IS 3177 / IS 4137 / Factories Act) checklists and safety docs are where SVMH can out-engineer regional peers and rank for terms premium/China brands own globally but not in India.

**Confidence convention:** Confidence on the *existence of the competitor asset/gap* is High (live-observed). Confidence on *search-volume magnitude* is Low (no licensed volume tool). Any figure cited (dimensions, INR, tonnage) inherits the confidence of its source and must be verified before publishing — engineering resources carry liability, so accuracy is non-negotiable.

> **Liability note (applies to every calculator, checklist, load chart, and safety doc below):** these are decision-support and reference aids, not certified engineering approvals. Every interactive/technical asset must carry a visible disclaimer ("indicative only; final design/load rating/inspection must be certified by a competent person per IS 807 / IS 3177 / the Factories Act 1948") and route to a human RFQ. This both manages risk and creates a conversion handoff.

---

## 1. Resource architecture

All assets live under the Knowledge Hub (`/resources`) defined in `12_Content_Ideas/content_plan.md` §1 and are cross-linked from the relevant product money-pages (product→resource→RFQ handoff).

```
/resources
├── /downloads ............ Spec-sheet/datasheet PDFs, catalogue, corporate profile, vertical one-pagers
├── /cad-library .......... DWG/DXF/PDF/STEP dimensional drawings + general-arrangement blocks
├── /tools ................ Interactive calculators + crane spec configurator (RFQ handoff)
├── /maintenance .......... Inspection & maintenance checklists (daily/monthly/annual), log templates
├── /installation ......... Installation, erection, commissioning & foundation guides
├── /safety ............... Safety & compliance docs (IS/Factories Act), load-test & inspection cert formats
└── /certificates ......... Downloadable ISO 9001 + type-test / load-test certificate samples
```

**Gating strategy:** Konecranes gates high-value assets (buyer's guide) behind consult forms but keeps brochures open (`02_Website_Audits/01_Konecranes_audit.md` §9). Recommended for SVMH: **ungated** datasheets/catalogue/checklists (SEO + trust; they should be indexable and shareable), **light email-gated** high-value assets (CAD files, calculators' PDF export, full engineering handbook) to capture leads without killing reach.

---

## 2. SPEC-SHEET / DATASHEET TEMPLATES (table-stakes parity — build first)

A per-product PDF datasheet is the proven soft conversion Konecranes uses ("add a per-product PDF datasheet: capacity, span, IS 807/IS 3177/FEM class, duty" — `02_Website_Audits/01_Konecranes_audit.md` §16.5). Regional rivals already ship these (S. Cranes, Vikrant, Eddy, Shivpra — `08_Brochures` Tier 3).

| # | Resource | Format | Target keyword / intent | Funnel | Why it wins |
|---|---|---|---|---|---|
| D1 | Single Girder EOT Crane datasheet | 1–2 pg PDF (capacity, span, HOL, duty class, wheel load, power, controls) | `single girder eot crane specification` — Commercial | BOFU | Parity + soft conversion; attaches to money-page P1. |
| D2 | Double Girder EOT Crane datasheet | PDF | `double girder eot crane specification` — Commercial | BOFU | Flagship product; parity with S. Cranes/Vikrant PDFs. |
| D3 | Gantry / Goliath / Semi-Goliath datasheet | PDF | `gantry crane specification` — Commercial | BOFU | Attaches to P5/P6. |
| D4 | Jib crane datasheet (pillar / wall / 360°) | PDF | `jib crane specification` — Commercial | BOFU | Attaches to P7. |
| D5 | Hot Metal / Ladle Crane datasheet (IS 4137) | PDF | `ladle crane specification` — Commercial | BOFU | Niche + margin; ties to Demag's ladle brochure benchmark (`08_Brochures` Demag). |
| D6 | Wire rope hoist / crab unit datasheet | PDF | `wire rope hoist specification` — Commercial | BOFU | Attaches to P8. |
| D7 | Components & spares datasheets (DSL busbar, forged hook, rope drum, sheave, gearbox, pendant) | PDF set | `crane spare parts specification` — Commercial | BOFU | Matches SVMH spares line (`00_CLIENT_BRIEF.md`); component SEO cluster (`seo_research.md` §1.6). |
| D8 | **Blank RFQ / crane spec-request template** (buyer fills capacity/span/HOL/duty/power) | Fillable PDF + web form | `eot crane specification sheet` / `crane data sheet` — Commercial | MOFU→BOFU | IS 3177 defines "information to be provided by the buyer" (Reva buyer's guide) — a branded spec-request sheet both educates and captures a qualified lead. |
| D9 | Master product catalogue + corporate profile PDF | Multi-page PDF | `sv crane catalogue` / brand — Brand | All | The minimum-viable parity move SVMH lacks entirely (`08_Brochures` §1). |
| D10 | Per-vertical solution one-pagers (Automotive / Steel / Power / Foundry / Cement / Construction) | 1-pg PDFs | `crane for <industry>` — Commercial | MOFU | ElectroMech's per-industry PDFs (steel, oil & gas, infra, galvanising) map cleanly to SVMH's verticals (`08_Brochures` §takeaways 3). |

**Evidence (datasheets):** Konecranes per-product datasheet + brochure pattern `02_Website_Audits/01_Konecranes_audit.md` §5, §16.5 (accessed 2026-07-05, High). Regional rivals' downloadable catalogues: S. Cranes `https://scranes.in/wp-content/uploads/2023/11/4.-S.-Cranes-Catalogue.pdf`, Vikrant `https://vikrantcranes.com/wp-content/uploads/2021/08/PRODUCT-CATALOGUE_EOT.pdf`, Shivpra, Top Crane, Eddy (`08_Brochures` Tier 3, all 2026-07-05, High). ElectroMech vertical brochures `https://ecms.emech.com/wp-content/uploads/2019/03/Solutions-for-Steel-Sector.pdf` etc. (High). IS 3177 "information to be provided by the buyer": Reva buyer's guide `https://www.revacranes.com/buyers-guide-for-eot-cranes/` (`10_Certifications` Part B, Medium).

---

## 3. CAD / DWG LIBRARY (leapfrog — few India peers offer this)

American Crane runs a dedicated CAD-drawings resource center; GrabCAD, linecad, CADForum host crane blocks that engineers actively download (firecrawl_search 2026-07-05). Indian EOT peers rarely publish a structured dimensional-drawing library — a genuine differentiator that earns links from specifying engineers and architects doing plant layouts.

| # | Resource | Format | Target keyword / intent | Funnel | Why it wins |
|---|---|---|---|---|---|
| CAD1 | General-arrangement (GA) drawings per crane type & capacity band | DWG + DXF + PDF | `overhead crane cad drawing dwg` / `eot crane general arrangement drawing` — Informational/Commercial | MOFU | American Crane proves the resource-center model; GrabCAD/linecad prove download demand (firecrawl_search 2026-07-05, High). India peers thin. |
| CAD2 | 2D dimensional / clearance drawings (span, HOL, hook approach, wheel base, C-dimension, headroom) | DWG/PDF | `eot crane dimensions drawing` / `crane clearance diagram` — Informational | MOFU | Feeds glossary G2 (span/hook-approach/C-dimension); engineers need these for building/runway design. |
| CAD3 | Runway / gantry rail & end-carriage layout blocks | DWG/DXF | `crane runway beam layout dwg` — Informational | MOFU | Structural engineers & PEB builders (Astal, Mount Roofing — adjacent Bengaluru competitors in `00_competitor_index.md`) need crane-ready layouts; link magnet. |
| CAD4 | AutoCAD blocks for plant-layout planning (top-running & underslung, jib radii) | DWG blocks | `overhead crane cad block` — Informational | TOFU→MOFU | CADForum/linecad-style free blocks pull consistent long-tail + backlinks (firecrawl_search 2026-07-05, High). |
| CAD5 | 3D models (STEP/IGES) for select standard cranes | STEP/IGES | `eot crane 3d model step` — Informational | MOFU | GrabCAD library demand for `bridge crane` models (firecrawl_search 2026-07-05, High); positions SVMH as engineering-led. |
| CAD6 | Component drawings (forged hook, rope drum, sheave, crab unit, DSL busbar section) | DWG/PDF | `crane hook drawing` / `rope drum drawing` — Informational | MOFU | Matches SVMH spares line; component-level link bait. |

**Delivery notes:** host on-site under `/resources/cad-library` (light email gate for DWG/STEP; PDF preview ungated for indexing), and seed a **GrabCAD publisher profile** to capture that channel's traffic back to the site. Each drawing carries the liability/indicative disclaimer (§0).

**Evidence (CAD):** American Crane CAD center `https://americancrane.com/resource-center/drawings/`; GrabCAD `https://grabcad.com/library?query=bridge+crane`; linecad `https://linecad.com/overhead-crane-cad-blocks-dwg-drawing-download/`; CADForum `https://www.cadforum.cz/catalog_en/?q=mobile+crane` (all firecrawl_search 2026-07-05, High for presence/demand). India-peer scarcity inferred from competitor set in `01_Competitors/00_competitor_index.md` (Medium).

---

## 4. INTERACTIVE CALCULATORS & CONFIGURATOR (leapfrog — high engagement + snippet/tool SEO)

Multiple competitors run **online wheel-load calculators** (dgcrane, Kino, KSCrane) and **crane configurators / designers** (R&M CraneDesigner, Demag KBK, CMAK, PWI, Thern) — confirmed live 2026-07-05. No strong India-focused, INR-aware equivalent exists. These tools drive dwell time, earn links, and convert (configurator → RFQ).

| # | Resource | Format | Target keyword / intent | Funnel | Why it wins |
|---|---|---|---|---|---|
| T1 | Crane wheel-load calculator (max/min wheel load, double-girder) | Interactive web tool + PDF export | `crane wheel load calculator` / `crane wheel load calculation` — Informational/Commercial | MOFU | dgcrane, Kino, KSCrane all rank tools for this (firecrawl_search 2026-07-05, High); India/IS-anchored version open. Engineers + structural designers use it → backlinks. |
| T2 | EOT crane cost / price estimator (₹, by capacity/span/duty/features) | Interactive tool + emailed quote PDF | `eot crane price calculator` / `overhead crane cost estimator india` — Transactional | MOFU→BOFU | Price intent "huge and under-served by premium brands" (`seo_research.md` §0); no INR estimator dominates. Directly captures high-intent price searchers and routes to RFQ. |
| T3 | Crane spec configurator ("Build your crane": capacity→span→duty→controls→RFQ) | Interactive configurator → pre-filled RFQ | `build your crane` / `crane configurator` — Commercial | BOFU | R&M CraneDesigner, Demag KBK, CMAK, PWI prove the model (firecrawl_search 2026-07-05, High); solves Konecranes' RFQ-friction weakness (`01_Konecranes_audit.md` §7) — SVMH beats incumbents on this exact point. |
| T4 | Duty-class selector (IS 3177 M1–M8 / FEM 9.511 from usage inputs) | Interactive quiz-style tool | `crane duty class calculator` / `which duty class do i need` — Informational | MOFU | Duty class adds 20–40% to price (`06_Industry_Research` §5); helping buyers self-select is high-value and feeds standards content S1/G3. |
| T5 | Wire rope / hoist selection tool (by load, duty, lift) | Interactive tool | `wire rope hoist selection` / `hoist duty selection` — Commercial | MOFU | Matches SVMH hoist line; complements comparison C4. |
| T6 | Span / HOL / clearance & headroom calculator | Interactive tool + diagram | `crane headroom calculator` / `low headroom crane clearance` — Informational | MOFU | Ties to CAD2 + glossary G2; ABUS's low-headroom positioning shows buyer relevance (`01_Competitors/03_ABUS`). |

**Build note:** T1/T4/T6 are lightweight client-side JS (fast, mobile-first — a wedge per `01_Konecranes_audit.md` §13–14). T2/T3 need a rules engine + RFQ backend and CRM/WhatsApp routing. All must show worked formula + assumptions + the §0 disclaimer, and offer "email me this result / get an engineer to confirm" as the conversion.

**Evidence (calculators/configurators):** Wheel-load calculators — `https://www.dgcrane.com/online-tools/crane-wheel-load-calculation/`, `https://www.kinocranes.com/crane-wheel-load-calculation/`, `https://www.kscranegroup.com/posts/reliable-crane-wheel-load-calculation/` (firecrawl_search 2026-07-05, High). Configurators — `https://cranedesigner.rmhoist.com/`, `https://www.demagcranes.com/en-us/KBK-crane-configurator-landing`, `https://cmak.com/en/cmak-tools/`, `https://pwiworks.com/crane-configurator/`, `https://thern.com/blog/crane-configurator-expansion/` (firecrawl_search 2026-07-05, High). Price-intent gap `seo_research.md` §0, §9.2 (High). Duty-class/VFD cost impact `06_Industry_Research` §5 (Medium). RFQ-friction opportunity `02_Website_Audits/01_Konecranes_audit.md` §7 (High).

---

## 5. MAINTENANCE & INSPECTION CHECKLISTS (India-anchored — the OSHA-vs-IS gap)

The inspection-checklist SERP is dominated by US/OSHA sources (SafetyCulture, OSHA, mhscrane) and Chinese makers (dgcrane) — firecrawl_search 2026-07-05. An **India-specific** checklist tied to IS 807, IS 3177 and the Factories Act 1948 (not OSHA 1910.179) is a clear, uncontested opening — and it directly feeds SVMH's high-margin AMC line.

| # | Resource | Format | Target keyword / intent | Funnel | Why it wins |
|---|---|---|---|---|---|
| M1 | Daily / pre-shift EOT crane inspection checklist (India, IS 807) | Printable PDF + fillable | `overhead crane daily inspection checklist india` — Informational/Commercial | MOFU | SERP is OSHA-dominated (firecrawl_search 2026-07-05, High); India/IS 807 version open. Drives AMC leads. |
| M2 | Monthly & quarterly preventive-maintenance checklist | PDF | `eot crane preventive maintenance checklist` — Commercial | MOFU | Thin competition (CraneCare, MechAllied) per `seo_research.md` §1.5; recurring-revenue funnel. |
| M3 | Annual / periodic thorough-examination checklist (Factories Act, load test) | PDF | `crane annual inspection checklist india` / `crane load test checklist` — Commercial | MOFU | Factories Act 1948 Sec 28 mandates annual load testing (`06_Industry_Research` §8, High) — authoritative India doc nobody owns. |
| M4 | Wire-rope inspection & discard guide (ISO 4309) | PDF + photo guide | `wire rope inspection discard criteria` — Informational | MOFU | ISO 4309 referenced in India export/MNC practice (`10_Certifications` Part A, Medium); visual guide = image-pack + link bait. |
| M5 | Crane maintenance log / record template | Fillable PDF / spreadsheet | `crane maintenance log template` — Informational | MOFU | Practical asset facility engineers keep and cite; low competition. |
| M6 | Component wear-limit reference (hooks, sheaves, wheels, brakes) | PDF reference card | `crane hook wear limit` / `sheave groove wear` — Informational | MOFU | Ties to spares D7/CAD6 → spares + AMC cross-sell. |

**Evidence (maintenance):** Checklist SERP US/OSHA + China dominance — `https://safetyculture.com/checklists/safety/crane-safety`, `https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.179`, `https://mhscrane.com/.../Crane-Daily-Inspection-Checklist-1.pdf`, `https://www.dgcrane.com/posts/overhead-crane-inspection-checklist/` (firecrawl_search 2026-07-05, High). India statutory basis (Factories Act 1948 Sec 28, annual load test) `06_Industry_Research/industry_market_research.md` §8 (High). AMC keyword thinness `seo_research.md` §1.5 (High). ISO 4309 `10_Certifications` Part A (Medium).

---

## 6. INSTALLATION, ERECTION & COMMISSIONING GUIDES (MOFU — practical authority)

IS 807 is specifically the "code of practice for erection, installation, functional testing, operation & maintenance" (`10_Certifications` Part A). Installation/foundation content is scarce in India SERPs and answers real buyer questions about the "hidden costs" (runway, civil) flagged in `06_Industry_Research` §5.

| # | Resource | Format | Target keyword / intent | Funnel | Why it wins |
|---|---|---|---|---|---|
| I1 | EOT crane installation & commissioning guide (IS 807) | Guide + PDF + checklist | `eot crane installation procedure` — Informational | MOFU | IS 807 governs erection/commissioning (`10_Certifications` Part A, High); thin India content. |
| I2 | Crane runway/gantry rail alignment & tolerance guide (ISO 12488) | Guide + diagram + PDF | `crane rail alignment tolerance` — Informational | MOFU | ISO 12488 crane-tolerance reference (`06_Industry_Research` §8, Medium); ties to CAD3. |
| I3 | Foundation & civil requirements for gantry/goliath cranes | Guide + load-data table | `gantry crane foundation design` — Informational | MOFU | Addresses a "frequently excluded" quote item (`06_Industry_Research` §5); pairs with hidden-costs guide (B5). |
| I4 | DSL busbar / conductor-rail installation guide | Guide + PDF | `dsl busbar installation` — Commercial | MOFU | Matches SVMH DSL busbar spares line; component cluster (`seo_research.md` §1.6). |
| I5 | Pre-installation site-readiness checklist (power, headroom, runway, access) | Checklist PDF | `crane site preparation checklist` — Informational | MOFU | Reduces project friction; qualifies leads; complements T6 headroom tool. |

**Evidence (installation):** IS 807 erection/installation/testing scope `10_Certifications/certifications.md` Part A (accessed 2026-07-05, High). ISO 12488 tolerances + excluded civil/runway items `06_Industry_Research/industry_market_research.md` §8, §5 (Medium). Component cluster `seo_research.md` §1.6 (High).

---

## 7. SAFETY & COMPLIANCE DOCUMENTS (BOFU trust — buyers screen on these)

`10_Certifications` is emphatic: in this category "buyers treat certificates as gating criteria," GeM/SAIL tenders demand IS 807/IS 3177 + valid test certificates, and SVMH must convert "ISO 9001 (claimed/ready)" into a verifiable, downloadable document. Safety docs are both trust assets and lead drivers for AMC/inspection.

| # | Resource | Format | Target keyword / intent | Funnel | Why it wins |
|---|---|---|---|---|---|
| SF1 | Downloadable ISO 9001 certificate (+ any IS/CE) | PDF | brand/trust — Trust | BOFU | ISO 9001 is table-stakes; every tier displays it — SVMH's "claimed/ready" reads as a red flag without the actual PDF (`10_Certifications` §takeaways 1–2, High). |
| SF2 | Sample type-test / load-test certificate & report format | PDF | `crane load test certificate format` — Commercial | BOFU | Factories Act makes per-unit test certs mandatory; showing the format signals rigor and answers procurement checklists (`10_Certifications` §takeaways 4, High). |
| SF3 | Crane safety features explainer (overload protection, limit switches, anti-collision, load display) | Guide + PDF | `crane safety features` / `overload protection eot crane` — Informational | MOFU | Safety tech is a rising table-stake (`06_Industry_Research` §7, High); differentiates on the dimension buyers care about most. |
| SF4 | Crane operator safety & do's-and-don'ts guide (India) | PDF poster + guide | `crane operator safety guidelines` / `crane safety training` — Informational/Commercial | MOFU | Operator-training/safety-audit keywords are "thin (opportunity)" (`seo_research.md` §1.5, High); shop-floor poster = shareable + branded. |
| SF5 | India compliance handbook: IS 807 / IS 3177 / IS 4137 / Factories Act 1948 | Downloadable handbook (email-gated) | `eot crane compliance india` / `indian standards for eot crane` — Informational | MOFU | Consolidates the India-standards snippet gap (`seo_research.md` §9.3) into a flagship lead-gen asset; verify all revision numbers vs live BIS catalogue first (`06_Industry_Research` §11). |
| SF6 | Quality & HSE policy (signed) | PDF/JPG | brand/trust — Trust | BOFU | ElectroMech displays signed Quality + HSE policy alongside certs (`10_Certifications` Part B, High) — cheap credibility parity. |

**Evidence (safety/compliance):** Cert-as-gating + GeM/SAIL tender demands + "show the actual certificate PDF" — `10_Certifications/certifications.md` Part A, Part B, §takeaways (accessed 2026-07-05, High). ElectroMech's 5 downloadable ISO certs + signed policies `https://ecms.emech.com/wp-content/uploads/2020/03/3.pdf` etc. (High). Safety-tech trend + Factories Act mandate `06_Industry_Research` §7, §8 (High). Operator-training keyword gap `seo_research.md` §1.5 (High). BIS-verification caveat `06_Industry_Research` §11.

---

## 8. Build sequence — parity first, then leapfrog

Sequenced to close the credibility gap fast, then differentiate. Aligns with `12_Content_Ideas/content_plan.md` §12 phasing.

| Phase | Months | Build (in order) | Rationale |
|---|---|---|---|
| **Phase 1 — Parity (must-have)** | 0–3 | D9 (catalogue + corporate profile); D1–D6 (core datasheets); SF1, SF6 (ISO 9001 + signed policy); M1 (daily inspection checklist) | Closes the "no downloadable anything" gap that puts SVMH below tiny rivals (`08_Brochures` §1; `10_Certifications` §1). |
| **Phase 2 — India-authority assets** | 2–6 | D8, D10 (RFQ template + vertical one-pagers); M2–M6 (maintenance suite); SF2–SF5 (safety/compliance incl. IS handbook); I1, I5 (install + site-readiness) | Owns the IS/Factories-Act India gap (`seo_research.md` §9.3) and feeds the high-margin AMC funnel. |
| **Phase 3 — Interactive leapfrog** | 4–9 | T1 (wheel-load calc); T4, T6 (duty-class + headroom); T2 (price estimator); CAD1–CAD4 (core CAD library) | Tools + CAD are where SVMH out-engineers regional peers and earns links (firecrawl_search 2026-07-05). |
| **Phase 4 — Advanced tooling** | 8–15 | T3 (full configurator → RFQ); T5 (hoist selector); CAD5–CAD6 (3D + component drawings); I2–I4 (advanced install guides) | Highest-build-cost, highest-conversion assets; configurator directly beats incumbent RFQ friction (`01_Konecranes_audit.md` §7). |

---

## 9. Cross-asset principles (so resources convert, not just inform)

Derived from the Konecranes audit and this repo's gap analysis:
1. **Every technical asset → RFQ handoff.** Calculators, configurators, datasheets and CAD pages end with a product-pre-filled "Request a Quote" + WhatsApp/click-to-call — beating Konecranes' generic-form friction (`01_Konecranes_audit.md` §7 Read, §16 AVOID #3).
2. **Ungate for reach, light-gate for leads.** Datasheets/checklists/certs indexable & open (SEO + trust); CAD files, calculator PDF exports, and the IS handbook behind a one-field email gate.
3. **India-first framing everywhere.** IS 807 / IS 3177 / IS 4137 / Factories Act — not OSHA/CMAA-only — is the uncontested wedge (`seo_research.md` §9.3; `06_Industry_Research` §8). Verify all IS revision numbers vs the live BIS catalogue before publishing (`06_Industry_Research` §11).
4. **Fast, mobile-first, lightweight.** Client-side calculators and compressed PDFs load fast on Indian mobile networks — a concrete edge over heavy incumbents (`01_Konecranes_audit.md` §13–14).
5. **Accuracy + disclaimer = trust, not liability.** Every tool/checklist/load figure shows its formula/assumptions and the §0 competent-person disclaimer. In a category where buyers fear undersized/uncertified cranes (`06_Industry_Research` §9 threats), demonstrable rigor is the differentiator.
6. **Schema + freshness.** Mark up HowTo (guides/checklists), Product/Offer (datasheets with price bands), and keep `lastmod` honest (`01_Konecranes_audit.md` §3, §11).

---

## 10. Source register (all live sources accessed 2026-07-05)

**Internal research consumed (this repo):**
- `00_CLIENT_BRIEF.md` — SVMH portfolio, spares line, known weaknesses (no downloadable assets).
- `03_SEO_Research/seo_research.md` — keyword clusters, price-intent gap, India-standards snippet gap, AMC/operator-training thinness, SERP features.
- `06_Industry_Research/industry_market_research.md` — pricing/cost drivers, IS/FEM/ISO standards, Factories Act, safety-tech trend, BIS-verification caveat.
- `08_Brochures/brochures_catalogs.md` — competitor downloadable-asset inventory (ElectroMech hub; regional PDF catalogues; SVMH's total gap).
- `10_Certifications/certifications.md` — standards buyers screen on; competitor cert-display norms; ElectroMech downloadable certs.
- `09_Case_Studies/case_studies.md` — proof-library context (ladle/foundry niche).
- `02_Website_Audits/01_Konecranes_audit.md` — datasheet/brochure/buyer-guide patterns, RFQ friction, performance wedge.

**Live competitor/asset verification (firecrawl_search, 2026-07-05, Confidence High for presence):**
- CAD/DWG libraries — `https://americancrane.com/resource-center/drawings/`; `https://grabcad.com/library?query=bridge+crane`; `https://linecad.com/overhead-crane-cad-blocks-dwg-drawing-download/`; `https://www.cadforum.cz/catalog_en/?q=mobile+crane`.
- Wheel-load calculators — `https://www.dgcrane.com/online-tools/crane-wheel-load-calculation/`; `https://www.kinocranes.com/crane-wheel-load-calculation/`; `https://www.kscranegroup.com/posts/reliable-crane-wheel-load-calculation/`.
- Configurators / crane designers — `https://cranedesigner.rmhoist.com/`; `https://www.demagcranes.com/en-us/KBK-crane-configurator-landing`; `https://cmak.com/en/cmak-tools/`; `https://pwiworks.com/crane-configurator/`; `https://thern.com/blog/crane-configurator-expansion/`.
- Inspection/maintenance checklists (US/OSHA + China dominance = India gap) — `https://safetyculture.com/checklists/safety/crane-safety`; `https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.179`; `https://mhscrane.com/wp-content/uploads/2021/03/Crane-Daily-Inspection-Checklist-1.pdf`; `https://www.dgcrane.com/posts/overhead-crane-inspection-checklist/`.
- Datasheet/catalogue parity (regional rivals) — S. Cranes, Vikrant, Shivpra, Top Crane, Eddy catalogues (URLs in `08_Brochures` Tier 3).

**Confidence notes:** Competitor asset existence & the India-gap = High (live-observed 2026-07-05). Search-volume magnitude = Low (validate in Keyword Planner/Ahrefs). Any dimensional/load/price figure published in these resources must be independently engineering-verified and IS/BIS-checked before release — engineering resources carry real liability; the §0 disclaimer is mandatory, not optional.
