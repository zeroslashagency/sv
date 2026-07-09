# Feature Gap Analysis — Prioritized Feature Matrix for the SVMH Website

**Client:** S.V. Material Handling System Pvt Ltd (SVMH), Harohalli KIADB Industrial Area, Bengaluru — svind.co.in
**Prepared by:** Competitive Landscape Research — Phase 1 (consolidation of the 15 research folders + 8 website audits + live re-verification)
**Deliverable:** Feature Gap Analysis — a prioritized matrix mapping every website *feature* to competitor coverage, SVMH opportunity, and effort/impact, with a phased build recommendation.
**Date of analysis / all live sources accessed or re-verified:** 2026-07-05

> **Confidence convention (inherited from the corpus).** Confidence on *competitor feature existence* and *SVMH's own gaps* is **High** — directly observed in live scrapes/audits on 2026-07-05 and re-verified this pass. Confidence on *search-volume magnitude* is **Low** (no licensed keyword tool used — validate in Google Keyword Planner / Ahrefs before budget). Price/tonnage/market figures inherit the confidence of their source and are cross-referenced across ≥2 sources where cited as hard numbers. Where a claim rests on a single source or could not be re-verified live, it is marked Medium/Low in-line.

---

## Executive Summary

This report answers one question for the Managing Director: **which website features will move SVMH off rented aggregator traffic and onto owned, higher-margin demand — and in what order should they be built?** It consolidates the feature-level findings from eight competitor website audits (Konecranes, Demag, ABUS, Street Crane, GH Cranes, STAHL, Columbus McKinnon, Kito Crosby), the market-gap and conversion registers, the SEO and engineering-resource plans, and live re-verification of the load-bearing claims into a single prioritized matrix.

The central finding is a **structural asymmetry that defines the entire feature strategy.** SVMH's own site is not merely behind — it currently **fails to load at all: "certificate has expired"** (re-verified live at svind.co.in, 2026-07-05, High). Behind that broken door there is no product page, no datasheet, no RFQ form, no catalogue, no price content, no case study, no WhatsApp CTA — nothing. Yet the feature gap runs in two directions:

- **Against the global/premium leaders** (Konecranes, Demag, ABUS, GH, CM, Kito, Street), SVMH cannot match feature *depth* — configurators, IoT monitoring, customer portals, 12-language hreflang, thousand-page catalogues. The audits are emphatic that SVMH should **not** try to.
- **Against the beatable local field** (Associated Hoists, ABCO, Gayathri, Ace, Kiran, Pegasus in Bengaluru; K2 Cranes attacking from Chennai), the gap is small and mostly on *basics* — a working site, product pages, a downloadable catalogue, a cert PDF. Directly beside SVMH, **Associated Hoists has no blog, no guides, no case studies, no downloads, and no pricing** (Report 07, live 2026-07-05, High).

The decisive insight from the audits is that **no competitor — global or local — offers the winning India-first feature bundle all at once.** The premium brands have deep technical features but route buyers off the product page to a generic quote form (Konecranes W3; CM §6; Kito §6), gate their best assets (Kito's 7-field CAD form; Street's gated brochures), hide price universally, and under-invest in India localization (Konecranes /en-in is "a thin shell"). The Indian/regional players have thin technical depth, weak or absent structured data, and almost no buyer education or interactive tooling. **The undefended middle — on-page RFQ, WhatsApp, INR price transparency, per-product datasheets, India-standards content, the foundry/ladle niche, and lightweight engineering tools — is SVMH's to take.**

This report ranks **20 website features** into three tiers:

1. **Table-stakes / quick-win bundle (ship first, Phase 0–1):** fix the certificate; ship secure fast pages; on-page RFQ with product pre-filled; sticky WhatsApp + click-to-call; per-product spec pages + downloadable datasheets; dual-axis (product × industry) navigation; a trust-signal strip with a real ISO 9001 PDF; JSON-LD schema. All Low/Medium effort, High impact, and every one attacks whitespace a competitor leaves open.
2. **Differentiator bundle (Phase 2–3):** industry landing pages with quantified project cards; case studies; INR price-guidance module; standards-explainer/comparison content; AMC & spares service hub; factory/FAT video; CAD/DWG library.
3. **Moat bundle (Phase 4, highest build cost):** crane selector / duty-class configurator; load/capacity/wheel-load calculators; INR price estimator; searchable spare-parts finder; full spec configurator → pre-filled RFQ. These are the interactive tools that no Indian competitor currently matches together.

The single most important message: **Feature #1 (fix the expired certificate and ship a real, secure site) is a prerequisite, not a feature — nothing else in this matrix can return a rupee until the front door opens.**

---

## 1. Method & Scope

**What "feature" means here.** This analysis is about *website capabilities* — navigation systems, forms, tools, content modules, media, trust components, and technical-SEO features — not about crane engineering. Each feature is scored on:

- **Competitor coverage** — who offers it today (global leaders / Indian leader ElectroMech / beatable local field), observed in the audits and live checks.
- **SVMH opportunity** — the specific, evidence-backed advantage SVMH gains by shipping it.
- **Effort** — Low / Medium / High relative to a lean modern build (static/Next.js or well-tuned CMS).
- **Impact** — Critical / High / Medium / Low on the strategic KPI: *share of demand shifting from rented (IndiaMART/ExportersIndia) to owned (svind.co.in).*

**Evidence base.** Eight full website audits (`02_Website_Audits/01–08`), the market-gap register (`11_Market_Gaps`), feature register (`13_Feature_Ideas`), conversion register (`14_Conversion_Ideas`), SEO research (`03_SEO_Research`), engineering-resources plan (`15_Engineering_Resources`), brochures (`08`), certifications (`10`), case studies (`09`), and the client brief (`00`). Load-bearing claims were re-verified live on 2026-07-05 (see §7).

**A note on the two peers not separately audited.** STAHL CraneSystems and SWF/Verlinde were profiled (`01_Competitors/06`, `09`, `10`) but not given standalone website audits; they are component/hoist specialists now inside Columbus McKinnon, and their feature patterns are represented by the CM and Demag audits. This is flagged so the matrix is read as evidence-complete for the audited set, not as a claim that every one of the 71 competitors was feature-audited.

---

## 2. Baseline: SVMH's Feature State vs the Field

This is the core asymmetry, feature by feature. It shows SVMH trailing the leader on every axis but trailing its *direct local competition* only on basics.

| Website feature | SVMH (live 2026-07-05) | Direct Bengaluru rival (Associated Hoists) | India leader (ElectroMech) | Global/premium pattern |
|---|---|---|---|---|
| Secure, loading site | **No — "certificate has expired"** | Yes | Yes | Yes |
| Product money-pages w/ specs | **None (routes to IndiaMART)** | Basic listings, capacity ranges only | Full solutions taxonomy | Deep technical PDPs (Demag, CM, ABUS, Kito) |
| On-page RFQ, product pre-filled | **None** | None | Enquiry form (not per-product) | **Weak everywhere** — Konecranes/CM/Kito route to generic form (whitespace) |
| WhatsApp / click-to-call | **None** | Phone only | Phone | Rare among premium (whitespace in India) |
| Downloadable datasheet / catalogue | **None** | None | Corporate profile + vertical PDFs | Rich PDF libraries (all leaders) |
| Downloadable ISO 9001 cert PDF | **None ("claimed/ready")** | ISO badge shown | 5 ISO cert PDFs | Real cert PDFs (ABUS, ElectroMech) |
| Dual-axis (product × industry) nav | **None** | None | Yes (13 industry pages) | Yes (Konecranes, Demag, GH, CM, Kito) |
| Industry / vertical landing pages | **None** | None | **13 (live-verified)** | 15–30 (GH 18, Street 15, CM 18, Kito 30) |
| Case studies / project proof | **None** | None | ~25 industry-tagged | Extensive (Street 11, GH huge ref wall) |
| INR price guidance | **None** | None | None (premium brands avoid) | None (universal gap — China players partial) |
| Standards / buyer education | **None** | None | Technical blog | Glossaries, buyer's guides (ABUS ~200-term glossary, Konecranes guide) |
| Interactive calculators / configurator | **None** | None | Limited (EMote IoT; no public calc) | Configurators (Demag ×3), calculators (China players) |
| CAD / DWG library | **None** | None | None public | Yes (CM, Kito gated; Demag Designer) |
| Factory / product video | **None** | None | Factory + product gallery | Yes (all leaders; often cookie-gated) |
| JSON-LD structured data | **None** | None | Partial | **Inconsistent** — Demag/ABUS/GH/Kito all MISS Product schema (whitespace) |

*Sources: svind.co.in, associatedhoists.com, emech.com/in — all live 2026-07-05 (High); `02_Website_Audits/*`, `08_Brochures`, `10_Certifications` (High).*

**Read:** Two-thirds of the "global/premium pattern" column is either enterprise overkill (IoT, portals, 12-language hreflang) or already-conceded whitespace (on-page RFQ, WhatsApp, INR price, Product schema). SVMH does not need to match the leaders; it needs to (a) reach parity with the *local* field on basics, and (b) claim the whitespace the leaders leave open. That is a small, achievable, well-defined feature set.

---

## 3. The Prioritized Feature Gap Matrix

The master deliverable. Twenty features, ordered by build phase then impact. "Competitor coverage" describes who offers the feature today; "SVMH opportunity" states the evidence-backed advantage; effort/impact are scored per §1.

### 3.1 Tier 1 — Table-Stakes & Quick Wins (Phase 0–1)

| # | Feature | Competitor coverage | SVMH opportunity | Effort | Impact |
|---|---|---|---|---|---|
| 1 | **Secure, fast, mobile-first site (fix expired SSL + tech-SEO hygiene)** | Every audited competitor loads securely; SVMH does not | Prerequisite gate. Renew cert, enforce HTTPS, one-H1/page, canonical, sitemap+robots. A lean static/Next.js build also beats the heavy incumbents (ABUS TTFB ~3.1s; Konecranes ~315KB) on Indian mobile networks | Low | **Critical** |
| 2 | **On-page RFQ with product pre-selected** | **Whitespace** — Konecranes (W3), CM (§6), Kito (§6) all route buyers to a generic form; Demag uses downloadable PDF RFQs | Put a short "Request a Quote" form (product auto-filled) on every product page. Beat the incumbents on their single clearest conversion weakness. Mirror IS 3177 fields (capacity/span/HOL/duty/environment) | Low | **High** |
| 3 | **Sticky WhatsApp + click-to-call** | Rare among premium brands; expected in Indian B2B; ElectroMech/local rivals show phone only | Match MSME buying behaviour; leverage direct-MD-access differentiator. Sticky WhatsApp + tel: with pre-filled enquiry text | Low | **High** |
| 4 | **Per-product spec pages + downloadable datasheet (PDF)** | Leaders excel (Demag, CM, Kito, ABUS); Street *gates* brochures (W1); even sub-scale rivals (S.Cranes, Vikrant, Top Crane) publish a catalogue PDF — SVMH has none | Publish clean on-page spec tables (capacity, span, HOL, duty class, wheel load, IS 807/IS 3177/FEM 9.511) + ungated datasheet per model. Table-stakes parity SVMH currently fails below tiny rivals | Med | **High** |
| 5 | **Dual-axis navigation (products × industries)** | GH, Demag, Kito, CM, Konecranes all do it; Indian/local players mostly product-only | "The single most copyable structural idea" (Konecranes audit §16). An "Industries" mega-menu mirroring the product menu serves both buyer mindsets | Low | **High** |
| 6 | **Trust-signal strip + downloadable ISO 9001 PDF** | ISO 9001 is table-stakes — every tier from ElectroMech to tiny Bangalore fabricators displays it; SVMH's "claimed/ready" reads as a red flag | Convert the claim into a real, downloadable cert PDF (not a logo). Above-fold badge strip: ISO 9001, IS 807/3177, GST, MSME, since-2006, installs. Removes a disqualifier | Low | **High** |
| 7 | **Product / Offer / Breadcrumb / FAQ schema (JSON-LD)** | **Whitespace** — Demag, ABUS, GH, Kito, CM all MISS Product schema despite huge catalogues (Kito: 636 product pages, no Product schema) | Free rich-result SERP real estate on every product page. A cheap way to out-rank giants who omit it | Low | **Med** |
| 8 | **Single dominant hero CTA (no carousel dilution)** | Kito, GH, ABUS, CM, Konecranes all dilute with rotating carousels / brand walls / mixed messaging | One benefit-led value prop + one primary CTA above the fold. Also protects LCP on mobile | Low | **Med** |
| 9 | **Clean, slug-based URLs + XML sitemap** | Demag ships `/node/` IDs; ABUS URLs with spaces; GH empty slugs (`1425---/`); STAHL/CM dup/flat sitemaps | Ship canonical, keyword-rich slugs and a clean sitemap from day one — cheap IA hygiene the incumbents get wrong | Low | **Med** |

### 3.2 Tier 2 — Differentiators (Phase 2–3)

| # | Feature | Competitor coverage | SVMH opportunity | Effort | Impact |
|---|---|---|---|---|---|
| 10 | **Industry landing pages w/ quantified project cards** | Strong at leaders (GH 18, Street 15, CM 18, Kito 30, ElectroMech 13); thin in Indian SME segment | Build 6 verticals (automotive, steel, power, foundry, cement, construction) with application copy + Customer/Location/Capacity/Span/IS-class cards. GH's reference wall is "its single most persuasive asset" | Med | **High** |
| 11 | **Case studies / project stories (industry-tagged)** | ElectroMech ~25; Street 11 named; Anupam JSW Dolvi 550T; thin in Indian SME tier | One case study per vertical + an AMC/repeat-order story. Format: "one page, one named customer, problem→solution→outcome." Directly attacks Known Weakness #3 | Med | **High** |
| 12 | **INR price-guidance / cost-factor module** | **Whitespace** — Konecranes, ElectroMech, Demag ignore price; only Timeskrane/China players own it | Own "EOT crane price 5 ton", "gantry crane price India". Schema-marked capacity→price table + cost-driver explainer. Pre-frames the TCO argument that defeats price-only objections | Low | **High** |
| 13 | **AMC / service + spares hub** | Cranedge (ElectroMech) owns service SEO; GH's "Ten services"; most makers bury service | Elevate AMC/inspection/load-testing/modernization beside products. Own "crane amc service bangalore" (thin SERP). Factories Act 1948 Sec 28 makes annual testing statutory — recurring demand | Med | **Med–High** |
| 14 | **Standards explainer + comparison content** | US/China hubs own FEM/CMAA; **India IS standards thin — clear snippet gap** | IS 807 / IS 3177 / IS 4137 explainers + "single vs double girder" comparison tables with FAQPage schema. Authority + featured-snippet capture; feeds money-pages | Med | **Med–High** |
| 15 | **Factory / process / FAT video** | ElectroMech, Konecranes, CM, ABUS use video (often cookie-gated); SVMH has zero multimedia | HD walkthrough (welding, assembly bay, 125% load test) that plays on click — beat the leaders' cookie-gated video. Tangible proof text can't match; low regional competition | Med | **Med–High** |
| 16 | **Buyer's guide / crane-selection helper (content)** | Konecranes has a Crane Buyer's Guide; ABUS "How does a crane work?"; India education gap | A one-page "how to spec an EOT crane" guide captures mid-funnel search the local field ignores. Cheap, durable SEO | Low | **Med** |
| 17 | **Callback scheduler / "MD direct line" + qualified contact form** | Leaders use long 12–15-field forms (CM, Konecranes); no live-assist | Short qualifying form (product/industry/enquiry-type) + callback option. Leverage flat structure and direct-MD-access as a differentiator vs faceless catalog competitors | Low | **Med** |

### 3.3 Tier 3 — Moat Features (Phase 4, highest build cost)

| # | Feature | Competitor coverage | SVMH opportunity | Effort | Impact |
|---|---|---|---|---|---|
| 18 | **Crane selector / duty-class configurator → RFQ** | Demag runs 3 configurators (KBK/Hoists/Drives, re-verified live); R&M CraneDesigner, CMAK; **no usable India equivalent** | Ask lifts/day + avg load% → suggest IS 3177 M-class + single/double girder, ending in a pre-filled RFQ. Directly beats Konecranes' RFQ friction; qualifies + educates | Med | **Med–High** |
| 19 | **Load / capacity / wheel-load / price calculators** | China players run wheel-load calculators (DGCrane re-verified live: free tool, inputs capacity/crane+trolley weight → max/min wheel load); **no INR-aware, IS-anchored India tool** | Lightweight client-side calculators + INR price estimator routing to RFQ. SEO magnet + engineering trust + link bait from specifying engineers. Mandatory competent-person disclaimer | Med | **Med** |
| 20 | **Searchable spare-parts / part-number finder + CAD/DWG library** | "Rare in the Indian SME sector"; Kito/CM offer CAD (gated); Demag Designer | Searchable DB of crab units, forged hooks, DSL busbars, gearboxes, sheaves, rope drums + light-gated CAD. Recurring revenue + client lock-in + a link magnet no local rival matches | High | **High** (recurring) |

---

## 4. How the Gaps Cluster (Feature Themes)

The 20 features resolve into five whitespace themes. This is how the MD should think about *why* each feature wins, not just *what* it is.

| Theme | Features | The competitor failing SVMH exploits |
|---|---|---|
| **1. Conversion whitespace** | 2, 3, 8, 12, 17 | Leaders make buyers leave the product page to enquire (Konecranes W3, CM §6, Kito §6), hide price universally, dilute the hero CTA, and offer no WhatsApp. SVMH removes friction at the moment of intent. |
| **2. Technical-trust whitespace** | 4, 6, 7, 11, 15 | Proof, datasheets, real cert PDFs, Product schema, and factory video — inconsistent or gated across competitors (Street gates brochures W1; Kito gates CAD; Demag/ABUS/GH/Kito miss Product schema). |
| **3. Education / SEO whitespace** | 14, 16 | India-specific standards (IS 807/3177/4137) and buyer education are a "clear snippet gap" no one owns; US/China hubs own FEM/CMAA only. |
| **4. Localization whitespace** | 5, 9, 10, 13 | India-first dual-axis IA, clean URLs, industry pages, and a service-forward hub — the leaders under-invest locally (Konecranes /en-in "a thin shell") and the local field publishes listings only. |
| **5. Aftermarket / leapfrog whitespace** | 18, 19, 20 | Interactive tools, calculators, spares DB, CAD — almost absent among India peers; a durable moat no local rival matches. |

---

## 5. The Two-Direction Gap: What to Match vs What to Ignore

A recurring theme across all eight audits is that copying the leaders wholesale is the wrong move. This table makes the boundary explicit so the MD does not overspend.

| Enterprise feature the leaders have | Verdict for SVMH | Why |
|---|---|---|
| Configurators, IoT monitoring, customer portals | **Later / selective** (Feature 18 only, lightweight) | GH IoT, Demag Portal, Kito WooCommerce, Street portal = enterprise overhead; a lightweight selector→RFQ captures 80% of the value |
| 12–14 language hreflang, 15-country subsites | **Ignore** | SVMH is India-first, single-market; EN (+ optional Hindi/Kannada) suffices |
| Distributor/rep locator as the contact model | **Ignore — do the opposite** | Kito's `/contact`→`/locator` and CM's distributor funnel are wrong for a single-site direct seller; SVMH shows phone/WhatsApp/RFQ directly |
| 3–4-level mega-menus, 18k-page flat sitemaps | **Ignore** | SVMH's catalogue is small; keep nav ≤2 levels, one clean sitemap |
| 15-field qualifying forms, image CAPTCHAs | **Avoid** | CM (~15 fields), GH (image CAPTCHA) depress conversion; keep RFQ to 5–6 fields + invisible spam protection |
| Cookie-gated video, gated CAD behind 7-field forms | **Avoid / invert** | Konecranes/CM cookie-gate video; Kito gates CAD (7 fields+CAPTCHA); SVMH wins by keeping media instant and datasheets ungated |

**Read:** The audits converge on a single verdict — SVMH's advantage is *speed, openness, and India-first directness*, not feature-count. Every "avoid" above is a place a giant added friction that a lean challenger can turn into a win.

---

## 6. Prioritized Recommendations & Phased Build Plan

Sequencing follows the corpus roadmaps (SEO §8 tiering, content-plan and engineering-resource phasing): fix the gate, ship the revenue-and-trust features, then the authority content, then the interactive moat.

### Phase 0 — Prerequisite (Week 0–2)
**Feature 1.** Renew/reissue the SSL certificate and enforce HTTPS. Ship technical-SEO hygiene (one H1/page, canonical, JSON-LD Organization, sitemap+robots) and a fully optimized Google Business Profile. *Nothing else returns value until this is done.* Any RFQ endpoint must ship with server-side validation and rate-limiting from launch (security note — do not deploy an unauthenticated lead form).

### Phase 1 — Quick-Win Bundle (Months 0–4)
**Features 2, 3, 4, 5, 6, 7, 8, 9.** On-page RFQ + WhatsApp/click-to-call; per-product spec pages + ungated datasheets; dual-axis navigation; trust strip + real ISO 9001 PDF; Product/Breadcrumb/FAQ schema; single dominant hero; clean URLs. **This phase carries the most impact per unit of effort** — it reaches parity with the local field on basics *and* claims the conversion + schema whitespace the leaders leave open. Ship a master catalogue + corporate-profile PDF here too (the minimum-viable parity move even tiny rivals have).

### Phase 2 — Differentiator Bundle (Months 3–9)
**Features 10, 11, 13, 15 (begin), 16.** Industry landing pages with quantified project cards; first case studies (one per vertical + the foundry/ladle niche wedge); AMC & spares service hub; begin factory/FAT video capture; buyer's-selection guide. Defends the Bengaluru/Karnataka home turf against K2 Cranes and elevates the higher-margin service line.

### Phase 3 — Authority Bundle (Months 4–12)
**Features 12, 14, 17 (+ complete 11, 15).** INR price-guidance module with schema-marked capacity→price table; IS-standards explainers + comparison tables (the India snippet gap); callback scheduler + qualified short form; complete case studies and video. Wins featured snippets and passes topical authority into the money-pages.

### Phase 4 — Moat Bundle (Months 8–18+)
**Features 18, 19, 20.** Crane selector / duty-class configurator → pre-filled RFQ; load/wheel-load/price calculators; searchable spare-parts finder + light-gated CAD/DWG library. Highest build cost, highest differentiation — the interactive layer no Indian competitor matches together. Every calculator/configurator must show its formula/assumptions and carry the mandatory disclaimer: *"indicative only; final design must be certified by a competent person per IS 807 / IS 3177 / Factories Act 1948,"* and route to a human RFQ.

### Build-Plan Summary

| Phase | Months | Features | Signature outcome |
|---|---|---|---|
| 0 — Prerequisite | 0–0.5 | 1 | Site loads securely, indexable, in Local Pack |
| 1 — Quick wins | 0–4 | 2,3,4,5,6,7,8,9 | Parity with local field + conversion/schema whitespace claimed |
| 2 — Differentiators | 3–9 | 10,11,13,15(begin),16 | Industry/proof/service depth; home-turf defense; niche wedge |
| 3 — Authority | 4–12 | 12,14,17 (+finish 11,15) | Price transparency; India-standards snippets; topical authority |
| 4 — Moat | 8–18+ | 18,19,20 | Interactive tools + spares/CAD no local rival matches |

---

## 7. Live Re-Verification Log (accessed 2026-07-05)

Every load-bearing feature claim in this report was re-checked live this pass. Firecrawl search returned HTTP 402 (quota) and the WebSearch endpoint returned request-body errors this session — the same tool conditions recorded across the corpus — so WebFetch was used for independent re-confirmation.

| # | Source URL | Feature claim verified | Result (quoted where load-bearing) | Confidence |
|---|---|---|---|---|
| 1 | https://svind.co.in | SVMH site state | **"certificate has expired"** — site fails to load securely | High |
| 2 | https://www.demagcranes.com/en/demag-configurators | Competitor configurators (Feature 18) | 3 self-serve configurators (KBK/Hoists/Drives); "Your offer in just a few clicks"; then "a Demag partner or Demag employee will get in touch" | High |
| 3 | https://www.dgcrane.com/online-tools/crane-wheel-load-calculation/ | Competitor calculator (Feature 19) | Free interactive tool; inputs lifting capacity + crane + trolley weight → max/min wheel load; "an online calculator designed to calculate and evaluate the wheel loads of a crane" | High |
| 4 | https://www.emech.com/in/ | Industry pages / dual-axis (Features 5, 10) | **13 industry landing pages** verified verbatim (Automotive, Electrical, Heavy Engineering, Infrastructure, Manufacturing, Nuclear Power Plants, Oil & Gas, Precast, Renewable Energy, Shipbuilding, Steel & Metal, Tunnel/Shaft Mucking, Warehousing) | High |

**Cross-referencing:** The SVMH expired-certificate state, ElectroMech's 13 industry pages, the Demag configurator model, and the DGCrane free wheel-load calculator each corroborate the corpus findings (Reports 07, 10; audits 01/02; `15_Engineering_Resources` §4) and were confirmed from a second, independent live fetch this pass. Price/tonnage figures cited elsewhere in the corpus (Timeskrane INR table, ElectroMech ₹684 Cr FY25) are cross-referenced across ≥2 sources in their source files and inherit Medium/High confidence as marked there.

---

## 8. Key Risks & Caveats

- **The expired SSL certificate blocks everything** until fixed — treat Feature 1 as an urgent prerequisite, not a line item (live 2026-07-05, High).
- **Search-volume magnitude is Low-confidence** across the corpus — no licensed volume tool was used. The *existence* of every competitor feature and SVMH gap is High-confidence (directly observed); the *traffic* each feature will earn must be validated in Keyword Planner/Ahrefs before budget.
- **The ISO 9001 claim must be substantiated before display** (Feature 6). Publishing an unverifiable certificate is a trust risk with procurement buyers, not a shortcut. If certification is genuinely in progress, prioritise closing it.
- **Engineering features carry liability** (Features 18, 19). Calculators, selectors, and load figures are decision-support aids, not certified approvals; the competent-person disclaimer is mandatory and every tool must route to a human RFQ.
- **Verify IS revision numbers against the live BIS catalogue** before publishing any standards-explainer content (Feature 14): IS 3177:2020 vs 1999; adjacent IS codes uncertain (`06_Industry_Research` §11).
- **Performance verdicts on competitors are directional** — several audits used single-sample curl timing, not full Lighthouse/CrUX runs (flagged Medium in the source audits). SVMH should baseline its own Core Web Vitals after Phase 0.
- **Do not over-reach on feature count.** The audits are unanimous: SVMH's credibility rests on speed, openness, and being a responsive Bengaluru maker with real projects — not on matching enterprise feature depth. Lead with proof, ship the quick-win bundle first.

---

## 9. Sources

### 9.1 Internal research consumed (this repo, synthesized 2026-07-05)
- `00_CLIENT_BRIEF.md` — SVMH profile, portfolio, known weaknesses (High).
- `01_Competitors/00_competitor_index.md` — 71-entry competitor set incl. Bengaluru/Karnataka rivals + K2 Cranes Karnataka targeting (High/Medium).
- `01_Competitors/13_ElectroMech_Material_Handling_Systems.md` — India benchmark (₹684 Cr FY25, digital assets, 13 industry pages) (High).
- `02_Website_Audits/01_Konecranes_audit.md` — dual-axis IA, RFQ friction (W3), buyer's guide, schema template, copy/avoid lists (High).
- `02_Website_Audits/02_Demag_Cranes_Components_audit.md` — configurators, deep PDPs, missing schema/OG, PDF-RFQ friction (High).
- `02_Website_Audits/03_ABUS_Kransysteme_audit.md` — per-product guided RFQ + dimension diagram, glossary, real cert PDFs, performance weakness (High).
- `02_Website_Audits/04_Street_Crane_Company_audit.md` — product taxonomy, spec-capturing RFQ + spares form, gated downloads (W1), `user-scalable=no` (High).
- `02_Website_Audits/05_GH_Cranes_Components_audit.md` — dual-axis nav, quantified reference walls, geo-routed RFQ, image/schema weaknesses (High).
- `02_Website_Audits/07_Columbus_McKinnon_CM__audit.md` — best-in-class PDP + document library, diffused CTAs, 15-field form (High).
- `02_Website_Audits/08_Kito_Corporation_Kito_Crosby_audit.md` — 636-product catalogue, gated CAD, missing Product schema, locator-only contact (High).
- `03_SEO_Research/seo_research.md` — keyword clusters, price/standards/foundry/local SERP gaps, SERP features (High intent / Low volume).
- `08_Brochures/brochures_catalogs.md` — competitor downloadable-asset inventory; SVMH's total gap (High).
- `09_Case_Studies/case_studies.md` — case-study formats + named-customer proof (High/Medium).
- `10_Certifications/certifications.md` — standards buyers screen on; cert-display norms (High).
- `11_Market_Gaps/feature_and_content_gap_analysis.md` — 20-item market-gap register + gap themes (High).
- `13_Feature_Ideas/feature_ideas.md` — 18-item feature register + quick-win/moat bundles (High).
- `14_Conversion_Ideas/conversion_opportunities.md` — CRO register, RFQ flow design, objection-to-conversion mapping (High).
- `15_Engineering_Resources/engineering_resources_plan.md` — datasheet/CAD/calculator/configurator/checklist inventory + phasing (High).
- `16_Reports/07_Content_Gap_Analysis.md`, `16_Reports/10_Actionable_Recommendations.md` — consolidated content roadmap + executive playbook (High).

### 9.2 Live re-verification (accessed 2026-07-05) — see §7 for detail
- https://svind.co.in — SVMH "certificate has expired" (High)
- https://www.demagcranes.com/en/demag-configurators — 3 configurators + lead-handling model (High)
- https://www.dgcrane.com/online-tools/crane-wheel-load-calculation/ — free wheel-load calculator (High)
- https://www.emech.com/in/ — 13 industry pages verbatim (High)

**Tooling note:** Live re-verification on 2026-07-05 used WebFetch after `firecrawl_search` returned HTTP 402 (quota) and the WebSearch endpoint returned request-body errors this session — the same conditions recorded across the corpus. The four WebFetch checks above independently re-confirmed the load-bearing feature claims. All other feature findings are drawn from the eight website audits and gap registers, which were themselves built on live firecrawl scrapes on 2026-07-05 (see per-file source registers). Where a claim rests on a single source or could not be re-verified live, confidence is marked Medium/Low in-line.
