# Website Audit — GH Cranes & Components (ghcranes.com)

**Auditor context:** Competitive-landscape research for S.V. Material Handling System Pvt Ltd (SVMH), Bengaluru.
**Target:** GH Cranes & Components (Industrias Electromecánicas GH, S.A.), Beasain (Gipuzkoa), Spain.
**Primary URL:** https://www.ghcranes.com/en/
**Date accessed:** 2026-07-05
**Method:** Live scrape via firecrawl (homepage, product, industry, service, contact, RFQ, about, catalogs, India subsite) + raw-HTML inspection for SEO/schema signals + third-party cross-reference (Owler, ZoomInfo, LinkedIn, Hoist Magazine).

---

## 1. Executive Summary

GH Cranes & Components is a global tier-1 European crane manufacturer (family-owned, founded 1958, presence claimed in 70 countries on 5 continents, 1,000+ staff). Its website is a large, mature, multi-language, multi-country platform (15 country subsites, 6 UI languages, ~9,950 URLs mapped) that functions as a genuine global lead-generation and after-sales engine — not a brochure. It is far ahead of SVMH's current IndiaMART-dependent presence in scale, depth, structured RFQ capture, industry-vertical storytelling, downloadable technical documentation, and after-sales digital services (IoT, customer portal, spare-parts e-commerce).

However, the site is technically dated under the hood: it runs on an older template (owl-carousel, inline `<style>` blocks, base64/transparent-GIF image tricks), has **no image optimization** (87 `<img>` on the homepage, zero WebP, zero lazy-loading, zero `srcset`), **thin JSON-LD schema** (Organization with only url + logo), **no canonical tags**, and a **CAPTCHA-heavy, field-heavy RFQ form**. The content is strong; the delivery is heavy.

**Confidence: High** for on-page/structural findings (directly scraped). **Medium** for performance verdicts (inferred from HTML markers, not a live Lighthouse run). **Low/Medium** for third-party firmographics (conflicting sources).

---

## 2. Company & Scale Context (for benchmarking)

| Claim | Value | Source | Confidence | Notes |
|---|---|---|---|---|
| Founded | 1958 | ghcranes.com homepage + /about-us | High | "family owned business, which was founded in 1958" |
| Global presence | 70 countries, 5 continents | Homepage counters | High | Quoted: "Presence in 70 COUNTRIES ON 5 CONTINENTS" |
| Cranes sold | 130,000 (home) vs 125,000 (About) | Homepage / About Us | Medium | **Internal inconsistency** — home counter says "130.000 sold cranes"; About says "more than 125,000 cranes". Flag: sloppy figure hygiene. |
| Employees | "over 1000 people worldwide" | /about-us | Medium | GH self-claim. Third parties conflict: ZoomInfo 501–1,000; Owler lists 38 (likely a single-entity/US record). Cross-ref inconsistent → treat 1,000 as group-wide self-claim. |
| Revenue | ~$30.9M (ZoomInfo, single entity) | zoominfo.com/c/gh-cranes | Low | Third-party estimate, entity scope unclear; not authoritative. |
| Positioning | "one of top 5 crane manufacturer" | /our-products/overhead-crane | Medium | Self-declared marketing claim, unverified externally. |
| Weekly production capacity | 90 standard bridge cranes, 40 hoists/kits, 2 gantry, 1 special, 0.5 automotive gantry | /about-us | High | Concrete, credible operational proof point — strong trust signal. |

---

## 3. Navigation & Information Architecture

**Primary nav (desktop mega-menu):**
- **Our Products** → Catalogs, Overhead crane, Gantry crane, Marine jib cranes, Industrial jib crane, Automotive marine gantry crane, Industrial automotive gantry crane, Dry docks, Motorized boat trailer, Crane kits, Hoist, Built-up hoist, End truck and wheel head, Transfer cart, Technological advantages (15 items)
- **Industries** → 18 verticals (Aerospace, Shipyards, Automotive, Steel constructions, Renewable energies, Railways, Foundry, Container crane, Steel handling, Stone handling, Marinas, Public works, Paper mills, Concrete precast, Waste management, Steelworks, Mining, Other)
- **Service** → Customer Portal, Ten out of ten services, GH Cranes IOT, Digital Plans
- **Information** → Trade Shows, Videos, GH´NEWS, RSS
- **Join Our Team** (careers)
- **About Us** → About Us, Policies and Certification
- **Blog**, **GH StartUp Factory** (external)

**Utility bar (top):** phone `+34 943 805 660`, email `ghcranes@ghcranes.com`, **REQUEST YOUR QUOTE** (persistent), **Parts & Accessories** (external e-commerce `globalservice.ghcranes.com`), **CONTACT**.

**Country/language switcher:** 15 country subsites (Spain, Portugal, France, Poland, Czechia, USA, Colombia, Peru, Brazil, Mexico, Thailand, **India**, Arabia, China) + 6 UI languages (ES/EN/PT/FR/ZH/CS). Also portal links: W.S. (CRM), C.P. (Customer Portal), G.A. (Gure artean / intranet).

**Assessment:** Product-first + Industries dual-taxonomy is best practice for capital equipment — buyers self-identify either by "what I need" (product) or "who I am" (industry). Same content is reachable two ways, which aids both UX and SEO. **Weakness:** 15-item product dropdown + 18-item industries dropdown is cognitively heavy and has no visual grouping; mobile turns this into a very long accordion. Source: https://www.ghcranes.com/en/ (nav scraped in full). Confidence: High.

---

## 4. Sitemap / Scale

- firecrawl_map returned **~9,950 URLs** across the domain and subdomains (`usa.`, `spain.`, `india.` etc.), confirming a very large indexed footprint. Source: firecrawl_map on https://www.ghcranes.com (result truncated at 9,949 lines). Confidence: High.
- URL structure is clean and localized per language: `/en/our-products/overhead-crane/`, `/es/productos/grua-puente/`, `/en/industries/automotive/1350-axima--/` (project reference pages carry numeric IDs + slug).
- **Weakness:** Project-reference slugs are messy (`1426--brazil-/`, `1425---/`, `1424---/`) — empty/placeholder slugs with trailing dashes indicate un-curated auto-generated URLs. Bad for SEO and for human readability. Source: homepage "Latest projects" links. Confidence: High.

---

## 5. Homepage Structure

Scraped section order (https://www.ghcranes.com/en/, accessed 2026-07-05):
1. **Hero rotator** — banner slides: "Solutions for Explosive Atmospheres (ATEX, IECEx, UL & CSA)", "Designed to fit. Built to lead" (YouTube), "New state-of-the-art plant in Texas", "Lifting solution for JENS-S" (Hoist Magazine press), "Inauguration of new GH China facilities" (YouTube). Mixes product, corporate news and PR.
2. **Tagline** — "Intelligent lifting solutions" + "GH — more than 60 years".
3. **Branding hook** — "With GH, innovation is not an extra".
4. **Featured videos** (3, deep-linked to video library).
5. **Trade Shows** — live upcoming events (Expomina Perú 2026 09–11/09/2026 Lima; FIB 28/09–02/10/2026 Bogotá) with dates + location.
6. **Corporate intro** — "Industrias Electromecánicas GH, S.A.… founded in 1958".
7. **Counters** — 70 countries / 130,000 cranes / 1,000 (employees, label truncated in scrape).
8. **Our Products** grid — 13 product tiles with hover image-swap, each linking to product page.
9. **Latest projects** — 4 recent installs (product + industry cross-links).
10. **Thought Leadership** — "Are intelligent cranes right for your application?", "7 questions for a leading crane manufacturer".
11. **Corporate catalog download** CTA (direct PDF).
12. **Representative customers** — large logo wall (ADIF, ABB, Audi, Volkswagen, Renfe, FCC, Alstom, Bombardier, ArcelorMittal, Seat, Airbus, Vestas, Iberdrola, Endesa, Navantia, Embraer, Codelco, Gestamp… ~40+ logos).
13. **Footer** — HQ address, phone/fax/email, social (LinkedIn/Facebook/Twitter/YouTube/RSS), Compliance Channel (whistleblower), Legal Notice & Privacy.

**Assessment:** Rich, multi-layered homepage that balances products, proof (customers, counters, capacity), and freshness (live trade shows, dated news). Strong. **Weakness:** hero mixes 5 unrelated message types with no single dominant CTA; "Intelligent lifting solutions" is the only value prop and it's weak/generic. Confidence: High.

---

## 6. Product Pages

Reference page: **Overhead crane** (https://www.ghcranes.com/en/our-products/overhead-crane/).

**Strengths:**
- Clear definition + benefit lead ("increases productivity, enhances safety, minimize maintenance costs").
- **Hard specs stated:** "Overhead Cranes from 500 kg to 400 ton." Configurations enumerated: box girder / standard profile; top-running single-girder, top-running double-girder, underhung, wall-traveling jib.
- Differentiators with icons: "Standardized Construction" (modular), "Robot Welded" (repeatability, uniform welds) — concrete manufacturing proof, not fluff.
- Cross-link to Industries and a bottom **"Request a quote"** CTA on every product page.

**Weaknesses:**
- **No downloadable spec sheet / datasheet on the product page itself** — technical PDFs live only in the central Catalogs page, not attached per-product. A buyer on the overhead-crane page cannot grab that product's data sheet in one click.
- No capacity/span selector, no comparison table, no interactive configurator on the standard product page (GH has "Digital Plans"/"Crane kits" tooling elsewhere but it's not surfaced here).
- Thin on standards/compliance callouts per product (no FEM/ISO/EN class shown inline) — important for engineering buyers. Confidence: High (page fully scraped).

---

## 7. Industry / Landing Pages

Reference page: **Automotive** (https://www.ghcranes.com/en/industries/automotive/).

**Strengths (this is GH's standout asset):**
- Application-specific narrative: Press Parts Manufacturing, Coil Warehouse Management, Stamping Dies Management, Parts Manufacturing, Automotive Assembly — each with its own image and use-case copy. This is exactly how a capital-equipment buyer thinks.
- **Massive real project/reference wall** with named customers, country, and often capacity/span/lifting-height: e.g. "Renault | España | 40/40 t", "Geely | China | 50/25t", "Integrity Tool & Mold | Querétaro, México | 50t | Span 23.4m | Lifting height 9m", "Gestamp Almussafes | 20/10t | Span 29000mm". Dozens of entries with a "Load more" pattern. Enormous credibility.
- Each industry page ends with the same "Request a quote" CTA — consistent conversion path.

**Weaknesses:**
- **Untranslated content leaks:** an embedded quote block renders raw Spanish placeholder text on the English page ("En seguida están en marcha. Tenemos muchas referencias para que las veas…"), and many reference titles are half-Spanish ("Carro abierto con dos elevaciones…", "grúa puente…"). Poor localization QA.
- Reference thumbnails are almost all `traspa.gif` (1px transparent placeholder) with the real image loaded via JS/hover — so on scrape (and for crawlers/some users) the gallery is effectively imageless. Fragile image delivery. Confidence: High.

---

## 8. RFQ Flow ("Request your quote")

URL: https://www.ghcranes.com/en/request-your-quote/

**Fields captured:** Name, Company, Telephone, E-mail, City, Postal Code; **Technical data:** Product (dropdown, 13 options), Span, Capacity, Lifting height, Industry (dropdown, ~28 options); free-text request; **Country** (full ISO list) → routes to that country's Sales Manager; Region; "How did you find us?" (attribution dropdown); **CAPTCHA image**; privacy-policy consent checkbox; honeypot ("Do not complete the following field").

**Strengths:**
- Product-aware + technically structured (span/capacity/lifting height) — collects genuinely useful engineering data so the quote can be actioned.
- **Geo-routing to a country Sales Manager** ("This request for offer will arrive to the Sales Manager for the selected country") — smart for a global org.
- Lead-source attribution field feeds marketing analytics.
- Honeypot + explicit GDPR consent = compliant and spam-aware.

**Weaknesses:**
- **Long, single-screen form** with no multi-step/progressive disclosure — high friction on mobile.
- **Image CAPTCHA** (`captcha_image_new.php`) is a known conversion-killer and accessibility problem vs. modern invisible/hCaptcha.
- No file-upload (buyer can't attach a drawing/GA layout), no "typical response time" reassurance, no phone/WhatsApp fallback on the form. Confidence: High.

---

## 9. Contact Flow

URL: https://www.ghcranes.com/en/contact/

- Country → Area → **service-type selector** ("Purchase new equipment / Service call / Purchase spare parts / Purchase accessories & maintenance / Others") + interactive world distribution map. Routes to the nearest branch/delegation.
- **Strength:** Intent-based routing separates new-sales from after-sales/spares — mature.
- **Weakness:** The default rendered state is confusing on scrape ("Area: Turkey" appears as a stray default); it's a JS-driven dropdown funnel with no plain fallback list of offices/emails visible without interacting. A user who just wants "the India office phone number" has to work for it. Confidence: Medium (JS-dependent rendering).

---

## 10. Trust Elements

| Element | Present? | Evidence | Confidence |
|---|---|---|---|
| Named blue-chip customers | Yes (strong) | Homepage logo wall + per-industry reference walls (Audi, VW, Renault, Airbus, Vestas, ArcelorMittal, Navantia, Alstom, ADIF…) | High |
| Quantified project references | Yes (strong) | Capacity/span/lifting-height on individual installs | High |
| Company heritage | Yes | "65+ years", founded 1958, 4 founding brothers | High |
| Production-capacity proof | Yes | Weekly output figures on /about-us | High |
| Certifications page | Yes | /about-us/policies-and-certification/ (dedicated) | High (page exists; contents not deep-scraped) |
| Press / third-party validation | Yes | Hoist Magazine article linked from hero | High |
| Compliance/whistleblower channel | Yes | Footer "Compliance Channel" (governance signal) | High |
| Awards / testimonials (quoted voices) | Weak | No customer testimonial quotes found; logos/refs only | Medium |
| Trust badges near forms | No | RFQ/contact forms carry no cert/security badges | High |

---

## 11. Images, Videos, Downloads

**Images:** Homepage carries **87 `<img>` elements**. Raw-HTML inspection: **0 WebP, 0 `loading="lazy"`, 0 `srcset`**. Heavy use of `traspa.gif` (transparent placeholder) + JS hover-swap and base64 inline images. Product/industry photos are real and plentiful but **unoptimized and not responsive**. Source: raw-HTML grep of https://www.ghcranes.com/en/. Confidence: High.

**Videos:** Strong. Dedicated Videos library (/information/videos/) + YouTube channel; homepage features 3 named videos and 2 hero YouTube links (e.g. GH China inauguration, "Designed to fit. Built to lead"). Confidence: High.

**Downloads / technical docs:** Excellent. /our-products/catalogs/ offers a tabbed library — **Catalogs / Options / Brochures** — with the Corporate Catalog and "Corporate Catalog Brief" downloadable as per-language PDFs (ES/EN/FR/DE/MX/PL/RU…), plus an interactive flip-catalog viewer. Example: `GH-Corporate-catalog-2025-en.pdf` (~10.7 MB). Also an interactive "Ex-Solutions" (ATEX) document. Confidence: High. **Weakness:** downloads are centralized, not attached to individual product pages; 10 MB PDFs are heavy.

---

## 12. CTAs & Forms

- **Primary CTA:** "REQUEST YOUR QUOTE" — persistent in top utility bar and repeated as "Request a quote" at the foot of **every** product, industry and service page. Consistent and omnipresent — a real strength.
- **Secondary CTAs:** "Parts & Accessories" (e-commerce), "CONTACT", per-catalog "Download", "Read more" on thought-leadership.
- **Weakness:** CTA copy is generic ("Request a quote"), no urgency/value framing ("Get an engineered quote in 48h"), and the hero lacks one dominant CTA. Forms are the friction point (see §8). Confidence: High.

---

## 13. SEO Structure

| Signal | Finding | Evidence | Confidence |
|---|---|---|---|
| Title tag | `GH crane and hoist manufacturer.` — **trailing whitespace**, brand-led not keyword-led | `<title>` in raw HTML | High |
| Meta description | Present, keyword-stuffed 30+ word list of every crane type | og:description / meta | High |
| H1 | Exactly **1 per page** (good) — home H1 tied to corporate intro | raw HTML `<h1>`=1 | High |
| H2s | 7 on homepage; used for hero slide titles (semantic mismatch — slide names as H2) | raw HTML `<h2>`=7 | High |
| Schema.org | **Thin** — only `Organization` with `url` + `logo`. No `name`, `address`, `ContactPoint`, `Product`, `BreadcrumbList`, or `Organization.sameAs` | JSON-LD block in raw HTML | High |
| Canonical | **None found** (`rel=canonical` absent) — risk of duplicate-content across country subsites/languages | raw HTML grep | High |
| hreflang | **Present** for es/en/pt/fr/zh/cs (6) — good multilingual signal | raw HTML `hreflang=` | High |
| Robots | `index, follow` | meta robots | High |
| OG/Twitter | Full OG + Twitter card set; **og:image is the SVG logo** (not a rich preview image) — weak social sharing | metadata | High |
| Platform | WordPress/Jetpack markers present (`twitter:site=@jetpack`, blog on /blog/) alongside a custom PHP catalog/CAPTCHA — **hybrid stack** | metadata + `captcha_image_new.php` | Medium |
| Content freshness | article:modified_time 2026-06-01/06-11 — actively maintained | metadata | High |

**Net SEO verdict:** Good multilingual + fresh + clean single-H1 fundamentals, undermined by missing canonicals, near-absent structured data, logo-as-OG-image, and trailing-space/brand-led titles. Confidence: High.

---

## 14. Internal Linking

- **Strong:** dual product×industry cross-linking (product pages link to Industries; industry pages surface product-tagged references; "Latest projects" link product+industry together). Deep reference library (thousands of project URLs) creates a large internal link graph.
- **Weak:** placeholder/empty project slugs (`1425---/`) create low-value thin pages; footer is address-only (no HTML sitemap / no columned link hub to aid crawl + users). Confidence: High.

---

## 15. Page-Speed Signals (inferred, not live-Lighthouse)

Evidence-based inference from HTML markers (Confidence: **Medium** — no live Lighthouse run performed):
- **Negative:** 87 homepage images, **no lazy-loading, no WebP, no srcset**; multiple inline `<style>` blocks; owl-carousel + jQuery-era libraries; 10 MB catalog PDFs; base64-inlined images bloat the HTML (homepage raw HTML ~102 KB).
- **Likely outcome:** heavy LCP and large transfer on the homepage and image-dense industry galleries, especially on mobile/slow networks. The `traspa.gif` hover-swap pattern defers real images but is a legacy hack, not modern responsive loading.
- **Positive:** SVG logo, JS-deferred gallery images limit initial paint of the gallery. Recommend a real Lighthouse/CrUX pass before quoting numbers. Confidence: Medium.

---

## 16. Mobile Experience

- Viewport meta present (`width=device-width, initial-scale=1.0`) → responsive template. Confidence: High.
- **Concerns (Confidence: Medium):** the 15-item product + 18-item industry mega-menus collapse into a long accordion; the single-screen RFQ form with image-CAPTCHA is high-friction on a phone; unoptimized images hurt mobile data/LCP; JS-hover image-swaps have no hover on touch (so touch users may see placeholders). Not verified on a device — inferred from markup.

---

## 17. UX Patterns — Notable

- **Persistent global RFQ + intent-routed contact** = mature B2B conversion architecture.
- **After-sales digital ecosystem:** Customer Portal (`portal.ghcranes.com`), spare-parts/accessories e-commerce (`globalservice.ghcranes.com`), **GH Cranes IOT** (real-time crane monitoring, overload/temperature/SWP alarms, TECSER cloud service tech), "Ten out of ten services" (10 named service lines: preventive/corrective maintenance, retrofits, spares, modernization, operator training, commissioning, warranty, IoT, cloud connectivity). This lifecycle/service depth is GH's biggest differentiator over a typical regional maker.
- **Thought-leadership content** ("towards the intelligent crane", "7 key questions for a crane manufacturer") positions GH as advisor, not just vendor.
- **Weaknesses:** legacy carousel-heavy hero; localization leakage (Spanish text on English pages); dated visual/interaction layer.

---

## 18. Strengths & Weaknesses Summary

| # | STRENGTHS | WEAKNESSES |
|---|---|---|
| 1 | Dual **Product × Industry** taxonomy — buyers navigate by need or by sector | Legacy tech stack (owl-carousel, inline styles, PHP CAPTCHA, jQuery-era) |
| 2 | **18 industry landing pages** with application-level copy + huge quantified project/reference walls (named customers, capacity, span, lifting height) | **No image optimization** — 87 homepage imgs, 0 WebP, 0 lazy-load, 0 srcset → heavy pages |
| 3 | **Persistent, geo-routed RFQ** capturing real engineering specs (span/capacity/height) → routed to country Sales Manager | RFQ is a long single-screen form with **image CAPTCHA**, no file upload, no response-time promise |
| 4 | Deep **downloads library** (multi-language corporate + brief catalogs, ATEX doc, interactive flip-catalogs) | Downloads centralized, **not attached per product**; 10 MB PDFs |
| 5 | Strong **trust stack**: blue-chip logo wall, weekly production-capacity figures, 65+ yr heritage, certifications page, compliance channel, Hoist Magazine PR | **Thin schema** (Organization url+logo only), **no canonical tags**, og:image is the logo |
| 6 | **True internationalization**: 15 country subsites + 6 UI languages + hreflang | **Localization QA failures** — raw Spanish placeholder text on English pages, half-translated reference titles |
| 7 | **Full after-sales digital ecosystem**: Customer Portal, spare-parts e-commerce, GH Cranes IOT (real-time monitoring/alarms), TECSER, 10 named services | Messy auto-generated project slugs (`1425---/`), footer with no HTML sitemap/link hub |
| 8 | **Rich media**: dedicated video library + active YouTube, thought-leadership articles, live dated trade-show listings | Hero rotator mixes 5 message types with **no single dominant CTA**; value prop ("Intelligent lifting solutions") is generic |
| 9 | Clean localized URLs, single H1/page, `index,follow`, actively updated (Jun 2026) | Figure inconsistency (130,000 vs 125,000 cranes); brand-led title tags with trailing whitespace |
| 10 | Consistent bottom-of-page "Request a quote" conversion path site-wide | Contact page default state confusing; office details hidden behind JS dropdowns |

---

## 19. What SVMH Should COPY / AVOID

### COPY (adopt for the new SVMH site)
1. **Dual Product × Industry navigation.** Build Industry landing pages (Automotive, Steel, Power, Foundry, Cement, Construction — SVMH's stated verticals) with application-specific copy, not just a product list. This is GH's single most persuasive asset and directly fits SVMH's target industries.
2. **Quantified project/reference wall.** For every install, publish Customer / Location / Capacity / Span / Lifting height (+ standard: IS 807 / IS 3177 / FEM 9.511). SVMH already builds to these codes — turn each delivered crane into a spec-tagged proof card. This beats an IndiaMART listing decisively.
3. **Spec-structured RFQ that routes intelligently.** Capture product + capacity + span + lifting height + industry + "how did you find us". For SVMH (single-country), route by product line or by city/region instead of country. Add lead-source attribution.
4. **Per-product downloadable data sheets + a proper catalogs/downloads hub.** SVMH should attach a PDF datasheet to each product page (crab units, forged hooks, DSL busbars, gearboxes, sheaves, rope drums) — GH proves buyers want downloads, but GH's mistake is centralizing them; SVMH should do both (hub + per-product).
5. **Trust stack + production-capacity proof.** Publish named clients, ISO 9001/GST/MSME certs on a dedicated page, and concrete capability figures (fabrication tonnage/month, AMC fleet under contract). GH's weekly-capacity numbers are highly credible — SVMH's equivalent would differentiate it from anonymous IndiaMART sellers.
6. **After-sales as a first-class section.** SVMH already does AMC + spares. Give it a "Service" hub (preventive/corrective maintenance, spares, retrofits, operator training, commissioning) mirroring GH's "Ten services" clarity — this is where recurring revenue and SEO long-tail live.
7. **Persistent "Request a Quote" CTA site-wide** + phone/WhatsApp in a sticky header (India buyer behavior favors phone/WhatsApp).
8. **hreflang / clean localized URLs & single H1 discipline** — cheap, high-value SEO hygiene GH gets right.

### AVOID (GH's mistakes — do better)
1. **Do NOT ship unoptimized images.** SVMH must use WebP/AVIF, `loading="lazy"`, and `srcset`/responsive images from day one. Never use transparent-GIF + JS-hover-swap hacks (GH's galleries break for crawlers and touch users).
2. **Do NOT use an image CAPTCHA on the RFQ.** Use invisible reCAPTCHA/hCaptcha or a honeypot only; make the RFQ **multi-step/progressive** and add file-upload (buyers want to attach GA drawings) + a stated response time (e.g., "engineered quote within 48 hrs").
3. **Do NOT skimp on structured data.** Implement full JSON-LD: `Organization` (name, address, ContactPoint, sameAs), `Product`, `BreadcrumbList`, `LocalBusiness` (Bengaluru address for local SEO). GH's near-empty schema is a missed opportunity SVMH can exploit to out-rank locally.
4. **Do NOT forget canonical tags** and don't let brand-led/trailing-space titles through. Use keyword-led titles ("EOT Overhead Cranes | Single & Double Girder | IS 807 | SVMH Bengaluru").
5. **Do NOT let localization/placeholder text leak.** GH ships Spanish placeholder copy on English pages — a QA failure that erodes credibility. SVMH's single-language site removes this risk, but the lesson is: no lorem/placeholder in production.
6. **Do NOT overload the hero** with 5 competing messages and no dominant CTA. One clear value proposition + one primary CTA.
7. **Do NOT auto-generate empty URL slugs** (`1425---/`). Curate readable, keyword-rich slugs for every reference/project page.
8. **Do NOT centralize 10 MB PDFs as the only doc access** — compress, and also attach lightweight per-product datasheets.

---

## 20. Sources (all accessed 2026-07-05)

- https://www.ghcranes.com/en/ (homepage — markdown + links + raw HTML) — High
- https://www.ghcranes.com/en/our-products/overhead-crane/ — High
- https://www.ghcranes.com/en/our-products/catalogs/ — High
- https://www.ghcranes.com/en/industries/automotive/ — High
- https://www.ghcranes.com/en/service/ten-out-of-ten-services/ — High
- https://www.ghcranes.com/en/service/gh-cranes-iot/ — High
- https://www.ghcranes.com/en/about-us/about-us/ — High
- https://www.ghcranes.com/en/contact/ — High
- https://www.ghcranes.com/en/request-your-quote/ — High
- https://india.ghcranes.com/ (India subsite) — High
- firecrawl_map of https://www.ghcranes.com (~9,950 URLs) — High
- Raw-HTML grep (schema, hreflang, canonical, img/WebP/lazy/srcset, H1/H2, title) — High
- Cross-reference firmographics: owler.com/company/ghcranes; zoominfo.com/c/gh-cranes; linkedin.com/company/ghcranes — Low/Medium (conflicting third-party data, flagged)

**Caveats:** Page-speed and mobile verdicts are inferred from HTML markers, not a live Lighthouse/CrUX run (Confidence: Medium). Employee/revenue figures from third parties conflict and are marked Low. The 130,000 vs 125,000 cranes-sold discrepancy is GH's own internal inconsistency, documented above.
