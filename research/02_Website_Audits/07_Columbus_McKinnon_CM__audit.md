# Website Audit — Columbus McKinnon (CM / CMCO)

**Domain:** https://www.cmco.com (US locale: `/en-us`)
**Audited by:** Competitive research for S.V. Material Handling Systems Pvt Ltd (SVMH)
**Date accessed:** 2026-07-05
**Method:** Live scrape via firecrawl_map / firecrawl_scrape + WebSearch/firecrawl_search corroboration
**Note on tier:** Columbus McKinnon (Nasdaq: CMCO) is a ~150-year-old global corporate. This is an enterprise, multi-brand, multi-region site — SVMH is a ~Rs 13.6 Cr single-site SME. The audit flags which patterns are *scalable down* to SVMH and which are enterprise-only overkill.

---

## 0. Company Context (for benchmarking)

| Fact | Value | Source URL | Confidence | Supporting evidence |
|---|---|---|---|---|
| Global HQ | Charlotte, NC (13320 Ballantyne Corporate Place, 28277) | https://www.cmco.com/en-us/ ; LinkedIn | High | Homepage footer "GLOBAL HEADQUARTERS: 13320 Ballantyne Corporate Place Charlotte, NC 28277"; LinkedIn address matches |
| History | "over 150 years" (started as saddlery/hoist craftsman) | https://www.cmco.com/en-us/about-us | High | About summary: "celebrating its 150th anniversary… from a saddlery and hoist craftsman" |
| Footprint | 50+ countries, 3,000+ employees, 19 brands | https://www.cmco.com/en-us/about-us | Medium | About summary: "operates globally in over 50 countries with over 3,000 employees and 19 brands, including CM, STAHL CraneSystems, and Yale" (single source; headcount may shift — Charlotte site closure of 73 jobs reported by businessnc.com) |
| Financials | Nasdaq: CMCO, "Record Orders in Fiscal 2025" | https://investors.cmco.com | High | Investor news headline in sitemap |
| Recent M&A | Completed acquisition of Kito Crosby | https://www.cmco.com/en-us/resources/cmco-articles/columbus-mckinnon-completes-acquisition-of-kito-crosby | High | Article URL present in map; Crosby/Kito/Harrington brands now link out to kitocrosby.com |
| Positioning | "Intelligent Motion Solutions" / "Smart Lifting & Motion Control" | https://www.cmco.com/en-us | High | Homepage H1 "A Global Leader in Intelligent Motion Solutions"; title tag |

**Relevance to SVMH:** CM is the aspirational "big brand" benchmark. Its scale (18,000+ pages) is not copyable, but its *page-level craft* — product page structure, document library, RFQ routing, trust framing — is exactly what SVMH lacks and should emulate at 1/100th the scale.

---

## 1. Navigation

**Primary top nav (mega-menu):** Products · Solutions · Industries · Our Brands · About Us · News · Careers · Contact Us · Investors. Plus a **Customer Login** and a **region/language selector** (flag icon "USA (EN)" → `/region-selection/`).

**Products mega-menu is deeply nested (3 levels), organized by category then sub-category then product:**
- Hoisting and Lifting Equipment → Manual Hoists, Electric/Air Hoists, Wire Rope Hoists…
- Crane Systems → Jib, Enclosed Track/Workstation, Crane Components, Crane Kits, Mobile/Workstation, Material Handling Solutions (Custom Lift Assists, Articulating Arms, Vertical Reaction Lifter, Torque Tubes, Pendant Handles)
- Rigging Equipment → Below-the-Hook Lifting Devices, Shackles/Chain Shackles…
- Power and Motion Technology → Linear Motion Products, AC/DC Motor Control, Radio Transmitters…
- Every level has a **"See All"** link.

**Evidence (High):** homepage nav markup shows `- ProductsSee All … - Hoisting and Lifting EquipmentSee All … - Manual HoistsSee All`, and `Power and Motion TechnologySee All`, `Rigging EquipmentSee All`, `IndustriesSee All`. Source: https://www.cmco.com/en-us (scraped 2026-07-05).

**Assessment:** Strong information scent and consistent "See All" affordance at each tier. The one weakness: parent menu labels link to `#` anchors (`https://www.cmco.com/en-us#`) rather than a real landing page — the top-level "Products"/"About Us"/"News" labels are non-navigable on click, relying on hover/expand. Minor accessibility/UX nit on touch devices.

---

## 2. Sitemap

- `sitemap.xml` exists and is **massive: 18,189 `<loc>` entries** (flat, not a sitemap-index) — Source: https://www.cmco.com/sitemap.xml (scraped 2026-07-05, Confidence: High).
- Per-region sitemaps also exist (e.g. `/en-bb/sitemap.xml`), and the site is fully **multi-locale** (`en-us`, `en-de`, `de-at`, `fr-ca`, etc.).
- **Weakness:** A single flat 18k-URL sitemap is not best practice — Google recommends splitting into a sitemap index of ≤50k-URL/≤50MB child files by section; a flat file this size is harder to crawl-budget and diagnose. (Confidence: Medium — inferred from structure, not a crawl-stats tool.)

**Relevance to SVMH:** SVMH will have dozens, not thousands, of pages — a single clean sitemap.xml is perfect for them. The lesson is simply *have one* (many SME crane sites don't).

---

## 3. Homepage Structure

Section flow (top → bottom), Source: https://www.cmco.com/en-us (High):
1. **Hero** — full-width, H1 "A Global Leader in Intelligent Motion Solutions" + background YouTube video ("Columbus McKinnon: Moving the World Forward"). OG hero image `image-home-hero.png` (1440×575).
2. **"Explore Solutions for Your Industry"** — industry-first entry point.
3. **"Featured Product Categories"** — visual category tiles.
4. **"What's Happening at Columbus McKinnon"** — news/blog feed.
5. **"Brands"** — logo wall of 19 brands (Camlok, CM, Crosby, Dixie, Dorner, Duff-Norton, eepos, Garvey, Gunnebo, Harrington, Kito, Little Mule, Magnetek, montratec, Peerless, Pfaff-silberblau, Shaw-Box, STAHL, Yale…).
6. **Brand mission statement** — "Together we create intelligent motion solutions that move the world forward and improve lives."
7. **Corporate Sustainability** block.
8. **Footer** with GLOBAL HEADQUARTERS, Corporate, Sales, OUR COMPANY, SUPPORT columns.

**Strength:** Dual entry — by **industry** *and* by **product category** — served high on the page. Clean corporate storytelling (mission + sustainability) builds trust.
**Weakness:** Heavy reliance on embedded YouTube/video and a large brand wall makes it corporate-brochure-ish; there is **no single dominant "Request a Quote" CTA in the hero** — conversion is diffused. Homepage summary reads as brand/ESG storytelling more than lead capture.

---

## 4. Product Pages (PDP)

Reviewed exemplar: **Yale YK Wire Rope Hoist** — https://www.cmco.com/en-us/products/hoisting-lifting-equipment/electric-air-hoists/electric-wire-rope-hoists/yale-yk-wire-rope-hoist/ (High).

PDP anatomy (this is the single most copyable asset on the site):
- **Product H1 + brand logo** (Yale) linking to the brand hub.
- **Image gallery + Video tab** ("Images / Videos" toggle) with an embedded how-to video ("Changing Brake Torque Springs…").
- **Concise value paragraph** (modular, configurable, "double beam / low-height monorail").
- **Three primary CTAs inline:** **Request a Quote**, **Buy Now**, and a **Wiring Diagrams** link.
- **Documents block** (front-and-center): Brochure, O&M Manual, "Browse All Documents" anchor.
- **"Need Assistance?"** helper box → Contact form.
- **Features and Benefits** — 10 richly-written spec bullets (capacities to 55 tons, lifts to 131 ft, 5 frame sizes/16 capacity variants, safety features, duty cycles H3/H4/H4+, **CMAA & HMI standards, CSA labeled, NEC explosion-proof**).
- **Control Options** section (2-speed / Standard VFD / Advanced VFD) — application-level education.
- **Full Documents library** grouped into *Brochures & Catalogs*, *Manuals & Supplements*, *Product & Data Sheets* (spec sheets, parts lists, comparison charts) — each a downloadable PDF.
- **Related Products** carousel (cross-sell: drives, transmitters).

**Strength:** This is a best-in-class B2B industrial PDP — standards compliance stated explicitly, deep downloadable technical docs, video, spec depth, and *three* conversion paths (quote / buy / contact). It educates AND converts.
**Weakness:** No live price, no configurator on-page (Buy Now routes to distributor flow); very long single-page (repeated Features blocks in the markup suggest duplicated desktop/mobile render — mild bloat).

---

## 5. Category / Landing Pages

- **Crane Systems hub** (https://www.cmco.com/en-us/products/crane-systems) — icon-tile grid to sub-categories (Jib, Enclosed Track/Workstation, Crane Components, Crane Kits, Mobile Cranes, Material Handling Solutions), a **Featured Brands** strip, a **Workstation Crane Solutions** explainer with video, and **Featured Products** cards (each → PDP with "View Details"). (High)
- **Industries hub** (https://www.cmco.com/en-us/industries) — 18 industry cards (Aerospace, Automotive, Construction, EV, Elevator, Entertainment, Food Processing, Forestry, Heavy Machinery, Manufacturing, Maritime, Metals, Mining, Offshore, Pharma, Rail, Utilities, Warehouse, Water Mgmt), each with a lifestyle photo, plus a **"More About Our Industries"** block feeding in case-study blog posts. (High)

**Strength:** Industry landing pages with real application photography + linked case studies = strong relevance signal and SEO surface. Opening copy is vivid ("lifting a 47-ton airplane wing… securing a lighting grid for a Broadway musical").
**Relevance to SVMH:** SVMH serves automotive/steel/power/foundry/cement/construction — an *Industries* section with one page per vertical + a local case study each is a direct, high-ROI copy target.

---

## 6. RFQ / Quote Flow

- PDPs expose **"Request a Quote"** and **"Buy Now"** inline. (High — seen on Yale YK PDP)
- Primary lead capture is the **Contact form** (see §7), which doubles as the RFQ intake.
- **"Find a Distributor"** (`/how-to-buy/`) and **"Find a Service Center or Technician"** (`/service-repair-centers/`) route buyers to the channel — CM sells largely through distributors, so RFQ often hands off rather than closing on-site.

**Weakness:** There is no dedicated, product-attached RFQ *form* with the SKU pre-filled visible in the scrape; "Request a Quote" appears to funnel into the generic contact form. For a distributor-led model this is fine, but it's a **weaker direct-conversion path** than a per-product quote form.
**Relevance to SVMH:** SVMH sells direct (no distributor layer) — it should do *better* than CM here: a short per-product "Get a Quote for [product]" form that pre-fills the product name.

---

## 7. Contact Flow

Contact form — https://www.cmco.com/en-us/our-locations/contact-form/ (High). Fields observed:
- **Reason for contact** (purchase / more info / order update / careers)
- **Are you an authorized CMCO distributor?** (Yes / No)
- **Is this a request for repair parts?** (Yes / No)
- **Brand of interest** (~19 brands dropdown)
- Email, First/Last name, **Country** (full ISO list), State/Province (US/CA/MX/ZA dropdowns), City, Postal, Company, Phone
- **Industry** (~50-option dropdown)
- Additional details (free text)
- **Privacy Policy consent checkbox** + **double opt-in marketing consent** + **reCAPTCHA** (Salesforce-backed form)

**Strength:** Sophisticated qualification/routing (distributor vs end-user, parts vs product, brand, industry) → clean CRM segmentation. GDPR-style double opt-in + reCAPTCHA = compliant and spam-resistant. Backed by Salesforce.
**Weakness:** The form is **long** (~15 fields incl. huge dropdowns) — friction-heavy for a quick enquiry; no visible phone-first/click-to-call or WhatsApp option surfaced in the form body; parts buyers are pushed off to a separate `columbusmckinnon.com/resources/parts` domain (potential confusion between `cmco.com` and `columbusmckinnon.com`).

---

## 8. Trust Elements

| Element | Present | Source | Confidence |
|---|---|---|---|
| 150-year heritage narrative | Yes | /en-us/about-us | High |
| ISO 9001:2015 certification page | Yes | /en-us/about-us/iso-9001-certification | High |
| Standards compliance on PDPs (CMAA, HMI, CSA, NEC) | Yes | Yale YK PDP | High |
| 19 named heritage brands (Yale, CM, STAHL, Magnetek…) | Yes | Homepage brand wall | High |
| Case studies / application stories | Yes | /resources/*-blogs/* | High |
| Publicly-traded / investor transparency | Yes | investors.cmco.com | High |
| Patents page, Professional Associations | Yes | /resources/patents, /about-us/professional-associations | High |
| Code of Conduct, EthicsPoint, ESG/Sustainability | Yes | footer links | High |
| Warranty Registration | Yes | /en-us/warranty-registration/ | High |

**Strength:** Deep, multi-layered trust stack — certifications, standards, heritage, named brands, ethics, patents, investor disclosure. Very hard for an SME to match, but the *pattern* (badge + standards + case studies) is copyable.

---

## 9. Images

- Uses **Cloudflare Image Resizing** (`/cdn-cgi/image/width=…,height=…,fit=cover/…`) for responsive, right-sized delivery — strong performance practice. (High — every image URL uses this)
- Consistent product-icon system (SVG line icons for categories), real application photography on industry pages, product photography + diagrams on PDPs.
- Most images carry descriptive **alt text** (e.g. "Icon of jib cranes", "Image of Cars on Conveyor Belt", "Utility Worker with CM Lineman's Hoist") — good accessibility/SEO. A few empty `alt=""` on decorative shots.

**Strength:** CDN-optimized, dimension-constrained, alt-tagged, on-brand. **Copyable at any budget** (SVMH can do the same with a Cloudflare/Imgix pipeline + disciplined alt text).

---

## 10. Videos

- Homepage hero background video + brand video (YouTube "Moving the World Forward").
- Product-level how-to videos embedded on PDPs (e.g. brake-torque-spring change on Yale YK).
- Category pages embed explainer videos (Workstation Cranes vs competition).
- Videos are **cookie-consent gated** ("you must accept Performance cookies") — privacy-compliant but adds a click before playback.

**Strength:** Video used at every funnel stage (brand → category → product how-to) — excellent for a technical buyer.
**Relevance to SVMH:** Even 2–3 shop-floor/installation videos would lift SVMH far above IndiaMART-tier competitors.

---

## 11. Downloads / Technical Documents

- PDPs carry a **structured document library**: Brochures & Catalogs, Manuals & Supplements (O&M manuals, storage procedures, VFD control manuals, crane spec sheets), Product & Data Sheets (control comparison charts, parts lists, wire-rope-hoist comparison). All PDFs on `globalassets/inriver/resources/`. (High — Yale YK PDP)
- Documents grouped, collapsible ("Show All / Show Less"), and there's a page-level **#documents** anchor.

**Strength:** This is a **standout**. Buyers/engineers can self-serve full spec sheets, manuals, and parts lists — reduces sales friction, builds credibility, and is a major SEO/long-tail magnet.
**Relevance to SVMH:** Highest-ROI copy target. SVMH already makes IS 807 / IS 3177 / FEM 9.511 cranes — publishing datasheets, load charts, and O&M PDFs per product would instantly differentiate it from IndiaMART listings.

---

## 12. CTAs

- PDP: **Request a Quote**, **Buy Now**, **Contact us** (Need Assistance box), document downloads, **View Details** on cards.
- Global: **Contact Us**, **Customer Login**, **Find a Distributor**, **Find a Service Center**, **Warranty Registration**.

**Weakness:** CTAs are **many but not hierarchically dominant** — no single, high-contrast, persistent "Get a Quote" button that follows the user (no visible sticky CTA in scrape). The multiplicity (Quote vs Buy vs Contact vs Distributor) can dilute action on a distributor-led model.

---

## 13. Forms

- Contact/RFQ form is **Salesforce Web-to-Lead** style with reCAPTCHA + double opt-in (see §7).
- Warranty Registration, Supplier Registration, Investor Information Request, event registration forms exist.

**Strength:** Enterprise-grade CRM integration + consent compliance.
**Weakness:** Length/friction; heavy dropdowns; no progressive disclosure.

---

## 14. SEO Structure

| Signal | Finding | Source | Confidence |
|---|---|---|---|
| Title tags | Descriptive, keyworded, branded — e.g. "Overhead Crane Systems & Components \| Columbus McKinnon", "Yale YK Wire Rope Hoist \| Yale", "Material Handling Industry Applications \| Columbus McKinnon" | multiple PDP/category metadata | High |
| Meta description | Present and benefit-led on every page checked | metadata blocks | High |
| H1 | Single clear H1 per page (Homepage: "A Global Leader in Intelligent Motion Solutions"; PDP: product name; Category: "Crane Systems") | scraped headings | High |
| Open Graph / social | Full OG tags (og:title/description/image/url/locale/site_name, image dims) on every page | metadata | High |
| Canonical/locale | `og:url` canonical + `og:locale` + multi-region hreflang structure (`en-us`, `en-de`, etc.) | metadata + map | High |
| Schema.org / JSON-LD | **Not detected** in scraped markup (`application/ld+json` not found) | homepage raw | Medium (scrape may strip; but no evidence found) |
| URL structure | Clean, hierarchical, keyword-rich: `/en-us/products/crane-systems/…` | all URLs | High |
| Favicon/tiles | Full favicon + MS tile set | metadata | High |

**Strength:** Textbook on titles, meta, single-H1, OG, clean URLs, hreflang.
**Weakness:** **No structured data (JSON-LD Product/Organization/BreadcrumbList) found** in the scrape — a missed rich-result opportunity for a catalog this large (Confidence: Medium — cannot fully rule out client-side injection). Also `keywords: "kmccarthy"` meta tag on several pages looks like a leftover author/owner tag — sloppy.

---

## 15. Internal Linking

- Deep, consistent internal linking: mega-menu → category hubs → PDPs → related products → brand hubs; industry pages → case-study blogs; PDPs → document PDFs and wiring-diagram pages.
- "See All" at every menu tier, "Browse All Documents", "Related Products", "More Details" — strong link equity distribution.
- **Weakness:** Some cross-links leave the domain (Crosby/Kito/Harrington/eepos/Gunnebo/Peerless → `kitocrosby.com`), and parts flow → `columbusmckinnon.com` — a fragmented post-acquisition footprint that dilutes domain authority and can confuse users. (High)

---

## 16. Page-Speed Signals

- **Positive:** Cloudflare image CDN with per-image resize/fit params; SVG icons/logos; favicon/tile optimization. (High)
- **Negative / risk:** Very heavy pages (homepage markup ~88k chars; PDP markup duplicated desktop+mobile blocks), multiple embedded YouTube players, large brand-logo wall, Salesforce + reCAPTCHA third-party scripts. Likely JS-heavy Episerver/Optimizely CMS. No live Lighthouse run performed here.
- **Confidence: Medium** — inferred from payload size and third-party embeds; a real CrUX/Lighthouse run would be needed to confirm Core Web Vitals.

---

## 17. Mobile Experience

- Responsive `viewport` meta present on all pages; CDN serves right-sized images; PDP markup shows separate mobile render path.
- **Weakness (inferred):** Long forms with giant dropdowns, deep 3-level mega-menu, and video-heavy hero are friction points on mobile; parent nav labels linking to `#` are awkward on touch. Confidence: Medium (not tested on a device emulator here).

---

## 18. UX Patterns Worth Noting

- **"You are now leaving Columbus McKinnon" interstitial** on outbound links — trust/safety pattern (good governance, slight friction).
- **Region/language selector** front-and-center — appropriate for a global multi-locale business.
- **Brand-within-brand** architecture: every product tagged "By: Yale / Magnetek / STAHL" — leverages heritage brand equity while unifying under CMCO.
- **Cookie-consent-gated video** — privacy-forward.
- **Customer Login** — B2B portal for existing accounts.

---

## Strengths / Weaknesses Summary Table

| # | Area | Strength | Weakness |
|---|---|---|---|
| 1 | Navigation | 3-level mega-menu, "See All" at every tier, industry+product+brand entry points | Top-level labels link to `#` (non-navigable on tap) |
| 2 | Sitemap | Exists; per-region sitemaps; full hreflang | Flat 18,189-URL file (should be a sitemap index) |
| 3 | Homepage | Dual industry/product entry, strong brand + ESG storytelling, hero video | No dominant hero quote CTA; brochure-heavy, conversion diffused |
| 4 | Product pages | Best-in-class: specs, standards (CMAA/HMI/CSA/NEC), video, 3 CTAs, full doc library | No live price/on-page configurator; duplicated render bloat |
| 5 | Category/Landing | Icon grids, featured products, industry photo cards + case studies | — |
| 6 | RFQ flow | Quote + Buy + Distributor + Service paths | No SKU-prefilled per-product quote form; funnels to generic contact |
| 7 | Contact | Rich qualification/routing, Salesforce, double opt-in, reCAPTCHA | ~15-field friction; no click-to-call/WhatsApp; parts sent off-domain |
| 8 | Trust | ISO 9001, 150-yr heritage, standards, patents, ethics, investor, 19 brands | Enterprise-only depth (not SME-replicable) |
| 9 | Images | Cloudflare resize CDN, alt text, consistent icon system | A few empty alts |
| 10 | Videos | Brand + category + product how-to videos | Cookie-gated (extra click) |
| 11 | Downloads/docs | Structured, grouped, collapsible PDF library per product | — |
| 12 | CTAs | Many action paths | No dominant/sticky primary CTA; choice overload |
| 13 | Forms | Enterprise CRM + consent compliance | Long, dropdown-heavy, no progressive disclosure |
| 14 | SEO | Titles, meta, single H1, OG, clean URLs, hreflang | No JSON-LD schema detected; stray `keywords: kmccarthy` tag |
| 15 | Internal linking | Deep, consistent, related-products, doc links | Authority fragmented across cmco.com / kitocrosby.com / columbusmckinnon.com |
| 16 | Page speed | Image CDN, SVGs | Heavy JS/video/3rd-party; CWV unverified |
| 17 | Mobile | Responsive, CDN images | Long forms + deep menu friction (inferred) |
| 18 | UX | Outbound interstitial, region selector, brand tagging, login portal | — |

---

## What SVMH Should COPY

1. **Product-page template = the crown jewel.** Rebuild every SVMH product (EOT single/double girder, gantry, jib, hoists, crab units, hooks) on a PDP with: H1 + short value paragraph → **specs table with IS 807 / IS 3177 / FEM 9.511 compliance stated explicitly** (mirror CM's CMAA/HMI/CSA callouts) → image gallery → **downloadable datasheet + O&M PDF** → a **"Request a Quote for [this product]" form with the product pre-filled**. This alone would leapfrog SVMH past its IndiaMART-tier competitors.
2. **A real technical Documents library.** Publish brochures, load charts, and O&M manuals as grouped, downloadable PDFs per product. Huge trust + long-tail SEO win at near-zero cost.
3. **Industries section.** One page per served vertical (automotive, steel, power, foundry, cement, construction) with a real photo + one local case study each. Directly copyable and high-ROI.
4. **Dual entry (by industry AND by product)** on the homepage.
5. **Trust stack, scaled down:** ISO 9001, GST/MSME, founding year (2006), IS/FEM standards badges, and 2–3 client case studies — CM's pattern at SME scale.
6. **Image discipline:** CDN-resized responsive images + descriptive alt text on every image.
7. **SEO fundamentals:** unique keyworded title + meta + single H1 + clean hierarchical URLs + OG tags on every page — and go one better than CM by **adding JSON-LD Product/Organization/BreadcrumbList schema** (which CM appears to lack).
8. **A few videos:** shop-floor fabrication, a crane install, an AMC service visit.
9. **Qualifying contact form** (product/industry/enquiry-type) feeding a simple CRM — but keep it *short*.

## What SVMH Should AVOID

1. **Do NOT build an 18,000-page flat sitemap** or a 3-level mega-menu — SVMH's catalog is small; keep nav 2 levels deep and the sitemap a single clean file.
2. **Avoid CM's diffused CTA problem** — SVMH sells direct, so it must have **one dominant, sticky "Get a Quote / Call Now" CTA** (plus a click-to-call and WhatsApp button for the Indian B2B market), not four competing paths.
3. **Avoid the 15-field form.** Keep RFQ to Name, Company, Phone/Email, Product, Message + consent. Long forms kill SME lead volume.
4. **Avoid multi-domain fragmentation** (cmco.com vs columbusmckinnon.com vs kitocrosby.com) — SVMH should keep everything on one domain to concentrate authority.
5. **Avoid brochure-first heroes with no conversion hook** — SVMH's hero must lead with a lifting/crane value prop + quote CTA, not a corporate mission video.
6. **Avoid cookie-gating videos** behind extra clicks for a small site — keep media instantly playable.
7. **Don't copy the enterprise ESG/investor/ethics apparatus** — irrelevant overhead for an SME; a simple About + Quality + Clients set suffices.

---

## Confidence & Verification Notes

- All page-structure, nav, PDP, contact-form, industries and SEO-metadata findings are **High confidence** — captured from live firecrawl scrapes on 2026-07-05 (URLs cited inline).
- Corporate figures (150 yrs / 50+ countries / 3,000+ employees / 19 brands) are **Medium** — stated on CM's own About page and partially corroborated by LinkedIn (HQ address) and businessnc.com; headcount is volatile (Charlotte site closure of 73 jobs reported).
- **JSON-LD schema absence** and **Core Web Vitals / page-speed** are **Medium** — inferred from scraped markup and payload size; a live Lighthouse/CrUX run and a rendered-DOM check would be needed to fully confirm. Flagged as such.
- Sitemap URL count (18,189) is **High** — counted directly from `sitemap.xml`.

**Sources:**
- https://www.cmco.com/en-us
- https://www.cmco.com/en-us/products/crane-systems
- https://www.cmco.com/en-us/products/hoisting-lifting-equipment/electric-air-hoists/electric-wire-rope-hoists/yale-yk-wire-rope-hoist/
- https://www.cmco.com/en-us/industries
- https://www.cmco.com/en-us/about-us
- https://www.cmco.com/en-us/our-locations/contact-form/
- https://www.cmco.com/sitemap.xml
- https://investors.cmco.com
- https://www.linkedin.com/company/columbus-mckinnon
- https://businessnc.com/columbus-mckinnon-to-close-charlotte-manufacturing-site-73-to-lose-jobs/
