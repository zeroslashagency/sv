# Website Audit — ABUS Kransysteme GmbH

**Site audited:** https://www.abus-kransysteme.de (German flagship domain)
**Auditor context:** Competitive-landscape research for S.V. Material Handling System Pvt Ltd (SVMH), Bengaluru
**Date accessed:** 2026-07-05
**Method:** Live scrape (firecrawl_scrape / firecrawl_map), HTTP header + timing probe (curl), raw-HTML SEO extraction
**Company snapshot:** European hallenkran (indoor/overhead crane) manufacturer, HQ Gummersbach (Sonnenweg 1, 51647), founded 1965, family-owned, "Made in Germany," 80 kg–120 t range, 8 domestic sites + international sales/service network, 9 country/language sub-sites.

---

## 0. Executive Summary

ABUS runs one of the strongest B2B industrial-manufacturer websites in the overhead-crane sector. It is a large, deeply-structured Pimcore-based site (300+ URLs) with a rigorous product taxonomy, product-specific RFQ forms with embedded technical-spec fields, a full downloads/certificate library, a technical glossary of ~200 terms (a large SEO/topical-authority play), video content, reference case studies dated monthly, and a small transactional shop for entry-level products. Its principal weakness is **performance** (measured TTFB ~3.1s, full load ~4.1s, 177 KB of HTML alone) and **structured-data/SEO-markup gaps** (no JSON-LD schema detected, minimal hreflang implementation on the flagship domain). For SVMH the site is a near-ideal blueprint for information architecture, RFQ design, and trust-building; the lessons to *avoid* are the heavy page weight and the reliance on a complex CMS.

**Confidence on structural/UX findings: High** (directly scraped). **Confidence on performance: Medium** (single-run curl probe from one location, not a full Lighthouse lab test). **Confidence on schema absence: Medium-High** (grep of rendered raw HTML found 0 `application/ld+json` blocks; some schema could theoretically be injected client-side).

---

## 1. Navigation

**Source:** https://www.abus-kransysteme.de (homepage header/footer), accessed 2026-07-05 | **Confidence: High**

Top-level primary nav (6 items): **Krane** (Cranes), **Hebezeuge** (Hoists), **Kundenservice** (Customer Service), **Unternehmen** (Company), **Karriere** (Careers), **Kontakt** (Contact). Utility nav: **Shop**, **Telefon** (click-to-call `tel:+492261370`), **Downloads**, region/language selector, and a **"Hoher Kontrast"** (high-contrast) accessibility toggle.

Mega-menu flyout structure (evidence, quoted from scrape):
- Krane → Übersicht, Laufkrane, Hängebahnsysteme, Schwenkkrane, Leichtportalkrane
- Hebezeuge → Übersicht, Elektroseilzüge, Elektrokettenzüge, Komponenten & Zubehör
- Kundenservice → Übersicht, Ersatzteile & Reparaturen, Wiederkehrende Prüfungen, Fachmontagen & Inbetriebnahmen, Nachrüsten & Modernisieren, Seminare & Schulungen, Zeit für neue Herausforderungen
- Each flyout carries a persistent contact card: *"Sie haben Fragen? Kontaktieren Sie uns und wir helfen Ihnen gerne weiter."* with a Kontakt button.

**Strength:** Clean 6-item taxonomy, product-first ordering, "Übersicht" (overview) landing at the top of each category, contact CTA embedded in every flyout. **Weakness:** Deep nesting means the double-girder crane page is 3 levels deep (`/krane/laufkrane/zweitraegerlaufkrane`); no visible breadcrumb trail was found in the rendered HTML (`breadcrumb` string count = 0), which hurts orientation and breadcrumb rich-results eligibility.

---

## 2. Sitemap / Information Architecture

**Source:** firecrawl_map of https://www.abus-kransysteme.de + robots.txt, accessed 2026-07-05 | **Confidence: High**

- `robots.txt` declares **two XML sitemaps**: `sitemap.site_3.xml` and `sitemap.projects_3.xml` (evidence: robots.txt fetched live). Separating editorial/project content from the main site map is good practice.
- The crawl surfaced **300+ unique URLs**, organized in a strict hierarchy: product families → product types → per-product `/anfrage` (inquiry) child pages → configuration/fixing/accessory sub-pages (e.g. `/krane/haengebahnsysteme/befestigung/flanschklemme`).
- A very large **glossary** cluster (~200 single-term pages such as `/tragfaehigkeit`, `/pendeldaempfung`, `/hakenmass`, `/spannweite`) plus a `/glossar` hub — a deliberate topical-authority / long-tail SEO strategy.
- Dedicated **SEO landing pages**: `/kranhersteller-deutschland`, `/hallenkrane-in-nrw`, `/wie-funktioniert-ein-kran`, `/seo-landingpages/blog`, `/kranbahn-stahlbau`.
- Reference/case-study cluster under `/referenzen/*` with named customers (Chiarizia, Hollandia, KraussMaffei, Nargesa, Vekoma, Niehoff).

**Strength:** Exhaustive, logical, machine-readable IA with dual sitemaps and a glossary moat. **Weakness:** Some URLs contain spaces / non-slug characters (e.g. `/Social Menu/Facebook`, `/aktive pendeldaempfung`, `/doppelte hubgeschwindigkeit`) — these are malformed for SEO and indicate CMS-generated cruft that should be noindexed or cleaned.

---

## 3. Homepage Structure

**Source:** https://www.abus-kransysteme.de, accessed 2026-07-05 | **Confidence: High**

Section flow (top → bottom):
1. **Hero with autoplaying background video** (`<video loop playsinline autoplay preload="auto" poster=...>`), H1 *"ABUS Krane jetzt live erleben"* + subcopy inviting a live demo appointment, dual CTA: **"Unverbindlich anfragen"** (non-binding inquiry) + **"Zu unseren Kranen."**
2. **"Finden Sie Ihren passenden Kran"** — a product-picker grid of 8 tiles (Laufkrane, Hängebahnsysteme, Schwenkkrane, Leichtportalkrane, Elektroseilzüge, Elektrokettenzüge, Komponenten & Zubehör, Kundenservice).
3. **Service teaser** — *"Ihr direkter Draht zu uns… Service endet nicht mit dem Kauf"* → link to Kundenservice.
4. **Tabbed company story** (Über Uns / Unsere Werte / Philosophie / Branchen): four value-led narrative blocks ("Unsere Welt steht niemals still," "Auf ABUS ist Verlass," "Gemeinsam mehr bewegen," "Überall dort, wo es schwer wird") establishing 50+ years, family ownership, 80 kg–120 t range, and named industries.
5. **Tagung.Mal.Anders** — event/conference-room offering (brand-experience play).
6. **Referenzen & Neuigkeiten** — 3 dated case-study cards (05.04.2026 Chiarizia, 01.02.2026 Hollandia, 12.10.2025 Nargesa).
7. **Karriere** — split teaser (experienced hires + apprenticeships).
8. **Customer logo slider** — 16 named brand logos (Dörrenberg, Bals, Krone, Samson, Schottel, HSM, Huesker, Horsch, etc.) linking out to each customer.
9. **Newsletter signup** + footer.

**Strength:** Textbook B2B homepage — product finder above the fold, emotional brand story, dated social proof, named logos, service + careers. Balances lead-gen with employer branding. **Weakness:** Heavy media (autoplay video + many high-res PNGs) drives the 177 KB HTML and slow load; the "Tagung.Mal.Anders" conference-room block is off-message for a first-time crane buyer and pushes core proof further down.

---

## 4. Product Pages

**Source:** https://www.abus-kransysteme.de/krane/laufkrane/zweitraegerlaufkrane (double-girder EOT crane), accessed 2026-07-05 | **Confidence: High**

Anatomy of a product page:
- Full-width header image + **H1** (Zweiträgerlaufkrane).
- **"Auf einen Blick"** at-a-glance bullets: *Tragfähigkeit bis 120 t; Spannweite bis 42 m; gute Anbaumöglichkeiten; hohe Fahrgeschwindigkeiten; optional ABUControl.*
- Product illustration + inline **"Preisanfrage"** (price-inquiry) CTA repeated near the top.
- **Image gallery / lightbox carousel** of 6 real installation photos, each captioned with the customer + location (KSB Frankenthal, Lux-Werft Niederkassel, Metalsa Bergneustadt, Neuero Melle, Vecotrade).
- Descriptive prose (computer-optimized box girders, low dead weight, integration variants).
- **"Verwandte Produkte"** — 4 related-product tiles each showing capacity + span (Einträgerlaufkrane 16 t/38.5 m, Deckenlaufkrane 8 t/25 m, Wandlaufkrane 5 t/12 m, Halbportalkrane 10 t/15 m).
- **Specification table** ("experten für schwere fälle"): Type → capacity → max span rows (bis 16 t/42 m; bis 40 t/40 m; bis 50 t/37 m; bis 100 t/30 m; bis 120 t/20 m).
- **"Hauptträger-Einbauvarianten"** — 5 labelled girder-connection diagrams (installation variants).
- **Decision-help CTA block**: *"Sie brauchen Hilfe bei der Entscheidung?"* → Kontaktformular + Ansprechpartner finden.
- **Downloads** — product-relevant PDF brochures (Laufkran-Programm 9.26 MB, Elektro-Seilzug, ABUControl flyer, Wägeunterflasche flyer).
- **"Dieses Produkt in Aktion"** — 3 reference case studies featuring this product.

**Strength:** Best-in-class product page — every buyer question (capacity, span, install variants, accessories, proof, docs, contact) is answered on one page, with real captioned photos and cross-sell. Multiple contextual CTAs (Preisanfrage, Kontakt, Downloads). **Weakness:** No downloadable per-product spec/data sheet as structured data; specs are in an image-heavy layout; no visible price (expected for engineered goods, but the shop shows they *can* price entry products).

---

## 5. Landing Pages

**Source:** firecrawl_map + scrape of `/kranhersteller-deutschland`, `/shop`, accessed 2026-07-05 | **Confidence: Medium** (some LPs returned thin rendered content via scraper, likely JS-gated)

- **Keyword SEO landing pages** exist for high-intent German queries: `kranhersteller-deutschland` (title *"Kranhersteller Deutschland | ABUS Kransysteme GmbH,"* meta *"führende europäische Kranfirma… Made in Germany"*), `hallenkrane-in-nrw` (regional), `wie-funktioniert-ein-kran` (educational/top-of-funnel), `kranbahn-stahlbau`.
- **Blog** hub at `/seo-landingpages/blog` (evidence: sitemap title *"Blog — ABUS Kransysteme GmbH"* with article *"Wie wähle ich den richtigen Hallenkran für mein Unternehmen?"*).
- **Newsletter sustainability landing pages** (`/newsletter/nachhaltigkeit-am-kran`, `.../nachhaltigkeit-im-unternehmen`).

Note: `/kranhersteller-deutschland` and `/shop` returned only *"Zurück"* as rendered markdown to the scraper (content is present per meta tags but likely client-rendered), so LP body depth is **Confidence: Low** on exact content.

**Strength:** Intentional funnel coverage — informational, regional, and commercial-intent landing pages feed the product tree. **Weakness:** LP URL under `/seo-landingpages/blog` literally exposes the SEO intent in the path (minor optimization smell); some LPs appear JS-dependent, a crawl/indexation risk.

---

## 6. RFQ (Request-for-Quote) Flow

**Source:** https://www.abus-kransysteme.de/krane/laufkrane/zweitraegerlaufkrane/anfrage, accessed 2026-07-05 | **Confidence: High**

This is the standout feature. Every product has its **own dedicated `/anfrage` (inquiry) page** — not a generic form. Structure:
- **Contact block:** Anrede (salutation), Vorname, Nachname, Firma, Straße, PLZ, Ort, **Land (full country dropdown)**, E-Mail, Telefon — all marked required (`*`).
- **Product-specific technical fields** ("Technische Daten der gewünschten Krananlage"): Tragfähigkeit (kg), Höchste Hakenstellung HC (mm), Hubgeschwindigkeit (dropdown: Standard 0,8/5 m/min / langsamer / schneller).
- **Site-condition fields** ("Bauseitige Gegebenheiten"): hall status (fertiggestellt / in Planung), lichte Hallenbreite, Oberkante Kranschiene, lichte Hallenhöhe, Spannweite, Kranbahn (vorhanden / mit anbieten), Kranbahnlänge, Anzahl Krane, Hallenkonstruktion (Stahl/Beton), Stützenabstände, free-text Anmerkung.
- An **annotated dimension diagram** (labelled crane schematic) accompanies the fields so buyers know which measurement each field means.
- **Inline downloads** of relevant brochures within the form.
- **Local-contact reassurance:** *"Ihr Kontakt vor Ort — Mit insgesamt über 70 deutschen und internationalen Vertriebspartnern ist ABUS weltweit präsent…"* plus the HQ address and a GDPR consent notice (with explicit third-country data-transfer consent).
- Reset + Absenden (submit). Page is correctly `robots: noindex`.

**Strength:** This converts an intimidating "get a quote" into a guided technical spec sheet — it pre-qualifies the lead and captures exactly the data an application engineer needs, cutting back-and-forth. The dimension diagram is a genuinely superior UX pattern. **Weakness:** The form is long/single-page with no multi-step progress indicator or save/resume; all-required contact fields before the "fun" technical part may raise abandonment; no file-upload for drawings; no honeypot/captcha visible (spam risk unknown).

---

## 7. Contact Flow

**Source:** https://www.abus-kransysteme.de/kontakt + `/kontakt/ansprechpartner`, accessed 2026-07-05 | **Confidence: High**

- Primary contact page offers a **partner-finder**: select Country → Region → enter Postleitzahl (postal code) → "Ansprechpartner finden" — routes the visitor to a local sales rep. Reflects the 70+ distributor model.
- Full HQ block: ABUS Kransysteme GmbH, Sonnenweg 1, 51647 Gummersbach; **click-to-call** `tel:+49 2261 37-0` and a hotline `+49 2261 37-237`; **mailto** `info@abus-kransysteme.de`; Google Maps link; all four social profiles (Facebook, LinkedIn, Instagram, YouTube).
- Secondary paths to KranHaus, Technischer Kundendienst, Ersatzteilverkauf, and a fallback Kontaktformular ("Nicht gefunden, wonach Sie suchen?").

**Strength:** Multi-modal contact (phone, email, form, map, local rep finder, social) — every buyer preference covered; postal-code routing is excellent for a distributor network. **Weakness:** No live chat / WhatsApp / callback-request widget; no stated response-time SLA or business hours on the page.

---

## 8. Trust Elements

**Source:** homepage, downloads, product pages, accessed 2026-07-05 | **Confidence: High**

- **Certifications as downloadable PDFs:** DIN EN ISO 9001 (cert valid 28 Feb 2026 – 27 Feb 2029 per PDF metadata) and **EN 1090** (structural steel/welding) — both on `/downloads`.
- **Heritage:** "seit 1965," "über 50 Jahre," family-owned/investor-independent messaging repeated.
- **Named customer logos** (16) on homepage, all linking to the customer's own site.
- **Dated reference case studies** (monthly "Project of the month") with named international customers and photos.
- **Made in Germany** positioning throughout; 8 production sites detailed under `/unternehmen/produktionsstandorte`.
- **Physical proof:** KranHaus showroom/training center pages with photos.

**Strength:** Deep, verifiable trust stack — real certs (not just logos), named + linked customers, dated projects, heritage, physical facilities. **Weakness:** No customer testimonial *quotes* or review-platform ratings; no on-page display of the ISO/EN badges near CTAs (they're buried in Downloads).

---

## 9. Images

**Source:** raw-HTML extraction of homepage + product page, accessed 2026-07-05 | **Confidence: High**

- **All 27 `<img>` tags on the homepage have `alt` attributes** (imgs 27 / alt 27) — strong accessibility + image-SEO.
- Images are served through a **Pimcore image-thumbnail pipeline** (`image-thumb__ID__variant/`) with purpose-named variants (productImage, galleryCarousel, lightbox, logoSliderImage, FullwidthTeaserImage) — responsive, role-specific sizing.
- Photos are real installations with descriptive, keyword-rich alt text (e.g. *"Zweiträger-Laufkran mit LED-Lichtlinie in der Firma Metalsa in Bergneustadt"*).

**Strength:** Consistent alt-text discipline, real photography, automated responsive variants. **Weakness:** Heavy PNG use for photographic content (illustrations and installation shots as PNG rather than WebP/AVIF) inflates page weight; **no `loading="lazy"` found** (lazy-load count = 0) on the homepage, so all images load eagerly — a measurable speed cost.

---

## 10. Videos

**Source:** homepage `<video>` + `/medien/videos/*` cluster, accessed 2026-07-05 | **Confidence: High**

- Homepage hero is a **self-hosted autoplaying, looping, muted background video** with a poster frame (good: poster prevents blank hero) — `preload="auto"` (bad: forces full early download).
- A dedicated **video library** under `/medien/videos/` covering ABUControl features (Pendeldämpfung/sway damping, Modularität, Gleichlaufregelung/Tandemsteuerung, KranHaus tour).
- Product pages reference "Dieses Produkt in Aktion" video/case content.
- YouTube channel linked in footer.

**Strength:** Video used both for emotional hero impact and technical feature explanation. **Weakness:** `preload="auto"` on the hero video is a page-speed anti-pattern; self-hosting large video (vs. a lazy-loaded facade) likely contributes to the slow TTFB/total load.

---

## 11. Downloads / Technical Documentation

**Source:** https://www.abus-kransysteme.de/downloads, accessed 2026-07-05 | **Confidence: High**

A comprehensive, well-organized library grouped into: **Unternehmen** (image brochure), **Produktprogramm** (12+ product catalogues/flyers — Laufkran 9.26 MB, HB-System, Schwenkkran, Elektro-Seilzug, ABUCompact, Komponenten A/B/C, ABUControl, ABURemote, LED, Tandemsteuerung, Wägeunterflasche), **Service** (service prospectus + phone list), **Zertifikate** (ISO 9001, EN 1090), **Verkaufsbedingungen** (T&Cs, international sales conditions, paint systems C2/C3/C4), **Sonstiges** (directions map). Each item shows a **thumbnail preview + file size**.

**Strength:** Every product family has a downloadable catalogue; certificates and legal terms are public; file sizes and previews set expectations. This is a serious lead-nurture / self-service asset. **Weakness:** PDFs download without any (optional) email gate, so no lead capture from downloads (trade-off: friction vs. leads); no HTML/structured spec sheets (all locked in PDF).

---

## 12. CTAs (Calls to Action)

**Source:** across homepage, product, contact pages, accessed 2026-07-05 | **Confidence: High**

CTA vocabulary is consistent and low-friction: **"Unverbindlich anfragen"** (non-binding inquiry), **"Preisanfrage"** (price request), **"Zu unseren Kranen,"** **"Kontakt,"** **"Ansprechpartner finden,"** **"PDF herunterladen,"** **"Jetzt anmelden"** (newsletter), **"Mehr erfahren."** Product pages repeat the Preisanfrage CTA at top and again mid-page, plus a soft "need help deciding?" contact block.

**Strength:** "Unverbindlich/non-binding" language lowers commitment anxiety; multiple CTA types match different readiness stages (inquire / call / download / subscribe); CTAs are contextual to each product. **Weakness:** Slight CTA overload on long pages; primary vs. secondary CTA hierarchy is not always visually obvious from the markup.

---

## 13. Forms

**Source:** `/anfrage` pages, `/kontakt/kontaktformular`, `/newsletter_anmeldung`, careers forms, accessed 2026-07-05 | **Confidence: High**

Beyond the RFQ forms (§6): a general contact form, a newsletter signup, a **careers application form** with its own data-privacy statement, and a supplier area. Forms use clear required-field marking (`*`), GDPR consent checkboxes with explicit third-country transfer language, and country dropdowns.

**Strength:** Purpose-built forms per journey (buy / contact / subscribe / apply / supply); GDPR-compliant consent handling. **Weakness:** No visible progressive disclosure, inline validation cues, or spam protection in the markup; long forms with no step indicator.

---

## 14. SEO Structure (title / meta / H1 / schema)

**Source:** raw-HTML grep + page metadata, accessed 2026-07-05 | **Confidence: Medium-High**

- **Titles:** unique, keyword-led, benefit-framed — e.g. *"Zweiträgerlaufkran: Traglast bis 120 t | ABUS Kransysteme,"* *"Seilzug bis 16t • Einschienenlaufkatze in kompakter Bauart,"* *"ABUS Kransysteme: Hallenkrane 'Made in Germany'."*
- **Meta descriptions:** present, action-oriented, many with trust glyphs (✓ sicher ✓ kompetent) and CTAs ("Jetzt informieren!").
- **H1:** present and singular per page (homepage H1 = *"ABUS Krane jetzt live erleben"*).
- **Canonical:** present (`rel="canonical" href="https://www.abus-kransysteme.de/"` on homepage).
- **OpenGraph:** full og:title/description/url/type on every page.
- **Correct noindex** on `/anfrage` and `/kontakt` (thin/duplicate pages).
- **JSON-LD structured data: 0 blocks found** in rendered HTML — **no Organization, Product, BreadcrumbList, or FAQ schema detected.** Confidence Medium-High (grep-based).
- **hreflang: only `x-default` found** on the flagship domain despite 9 language sub-sites; proper reciprocal `hreflang` per language is largely absent in the head — an international-SEO gap. The 9 locales are linked via an on-page region selector, not full hreflang annotation.
- **No `twitter:` card tags** found.

**Strength:** Excellent human-facing SEO (titles, metas, H1s, canonicals, glossary, LPs, blog). **Weakness:** Missing machine-facing structured data (no schema.org) forfeits rich results; weak hreflang despite multi-country footprint; no Twitter cards.

---

## 15. Internal Linking

**Source:** homepage + product page link graph, accessed 2026-07-05 | **Confidence: High**

Dense, intentional internal linking: product pages link to related products (with capacity/span), to accessories/components, to ABUControl, to case studies featuring the product, to downloads, and to contact/RFQ. The glossary (~200 terms) and blog interlink to product pages, building topical authority. Footer repeats the full taxonomy.

**Strength:** Strong hub-and-spoke linking — product ↔ accessory ↔ reference ↔ glossary ↔ RFQ; excellent for both users and PageRank flow. **Weakness:** No breadcrumb navigation (orientation + no BreadcrumbList schema); some orphan-ish glossary/CMS URLs with spaces in paths.

---

## 16. Page Speed Signals

**Source:** curl header + timing probe from single location, accessed 2026-07-05 | **Confidence: Medium** (single run, not full Lighthouse)

Measured (one run):
- **DNS:** 0.005 s | **Connect:** 0.456 s | **TTFB: 3.14 s** | **Total: 4.09 s** | **HTML size: 177 KB (177,480 bytes)**.
- Server: **nginx**, CMS: **Pimcore** (`x-powered-by: pimcore`), with aggressive HTML output caching (`cache-control: max-age=2419200, public` ≈ 28 days; `x-pimcore-cache-date` present).
- `content-encoding` not confirmed in the filtered header set; `vary: Accept-Encoding` present.
- No `loading="lazy"`; hero video `preload="auto"`; heavy PNGs.

**Strength:** HTTP/2, sensible long-lived caching, low DNS/connect latency, cached HTML at the edge/app layer. **Weakness:** **TTFB of ~3.1 s is poor** and dominates load time — likely Pimcore render/DB latency on cache-miss plus geographic distance; combined with eager images and a preloaded hero video, real-world LCP is likely well above Google's 2.5 s "good" threshold. This is the site's clearest technical weakness.

---

## 17. Mobile Experience

**Source:** meta viewport + responsive markup, accessed 2026-07-05 | **Confidence: Medium** (inferred from markup, not device-tested)

- `<meta name="viewport" content="width=device-width, initial-scale=1">` present on all pages.
- `color-scheme: dark light` declared (respects OS dark mode).
- Responsive image-thumbnail variants and a mobile flyout nav structure are in the markup.
- Click-to-call `tel:` links aid mobile conversion.

**Strength:** Responsive foundation, dark-mode aware, mobile-friendly contact affordances. **Weakness:** Page weight + slow TTFB hit mobile hardest (mobile networks/CPUs); long single-page forms are harder on mobile; not lab-verified here so treat as Medium confidence.

---

## 18. UX Patterns (notable)

- **Product finder grid** on homepage as the primary entry.
- **Guided technical RFQ with dimension diagram** (the signature pattern).
- **Postal-code rep finder** for the distributor network.
- **Captioned real-installation galleries + lightbox** on product pages.
- **Dated "Project of the month"** social proof.
- **High-contrast accessibility toggle** in the header.
- **Glossary + "Wie funktioniert ein Kran?"** educational layer for top-of-funnel buyers.

---

## Strengths / Weaknesses Summary Table

| # | Area | Strength | Weakness | Confidence |
|---|------|----------|----------|-----------|
| 1 | Navigation | Clean 6-item product-first mega-menu; contact CTA in every flyout; high-contrast toggle | No breadcrumbs; products 3 levels deep | High |
| 2 | Sitemap/IA | Dual XML sitemaps; exhaustive logical hierarchy; ~200-term glossary moat | Malformed URLs with spaces (CMS cruft) | High |
| 3 | Homepage | Product finder above fold; brand story; dated proof; 16 named logos | Heavy media → slow; off-message conference-room block | High |
| 4 | Product pages | At-a-glance specs, spec table, install-variant diagrams, captioned real photos, related products, case studies, downloads — all on one page | Specs locked in images/PDF; no structured spec sheet | High |
| 5 | Landing pages | Intent-based LPs (kranhersteller-deutschland, regional, educational) + blog | SEO intent exposed in URL path; some JS-gated content | Medium |
| 6 | **RFQ flow** | **Per-product guided form with technical + site-condition fields and a dimension diagram — pre-qualifies leads** | Long single-page form; no multi-step/save; no drawing upload | High |
| 7 | Contact | Phone, email, map, social, postal-code rep finder | No live chat/callback; no response-time SLA | High |
| 8 | Trust | Real ISO 9001 + EN 1090 PDFs; named+linked customers; dated projects; 1965 heritage; physical KranHaus | No testimonial quotes/ratings; badges buried in Downloads | High |
| 9 | Images | 100% alt coverage; responsive thumbnail pipeline; real photography | Heavy PNGs; no lazy-loading | High |
| 10 | Videos | Hero video + technical feature video library + YouTube | `preload="auto"` hero; self-hosted heavy video | High |
| 11 | Downloads | Full catalogue/cert/T&C library with previews + sizes | No lead capture; no HTML spec sheets | High |
| 12 | CTAs | Consistent low-friction "unverbindlich/Preisanfrage" language; stage-matched | CTA overload on long pages | High |
| 13 | Forms | Purpose-built per journey; GDPR-compliant consent | No inline validation/spam protection/step indicators | High |
| 14 | SEO markup | Unique keyword titles, metas, single H1s, canonicals, OG | **No JSON-LD schema; weak hreflang; no Twitter cards** | Med-High |
| 15 | Internal linking | Dense hub-and-spoke; glossary/blog → product | No breadcrumbs; orphan CMS URLs | High |
| 16 | Page speed | HTTP/2; 28-day HTML caching; low DNS/connect | **TTFB ~3.1 s, total ~4.1 s, 177 KB HTML** | Medium |
| 17 | Mobile | Responsive viewport; dark-mode aware; click-to-call | Weight/TTFB penalize mobile; long forms | Medium |

---

## What SVMH Should COPY

1. **Per-product guided RFQ forms with a dimension diagram.** This is ABUS's single best idea. For each SVMH crane type (single/double-girder EOT, gantry, jib, monorail), build an inquiry form that captures capacity, span, HOL, hook height, hall dimensions, duty class (IS 807 / FEM 9.511), and runway status — with a labelled schematic so buyers know what to measure. It pre-qualifies leads and signals engineering competence.
2. **One-page product template that answers everything:** "At a glance" bullets → capacity/span spec table → installation-variant diagrams → real captioned installation photos → related products → downloadable catalogue → case studies → contact. SVMH product pages should follow this exact skeleton.
3. **Real trust stack, made downloadable:** publish ISO 9001, IS 807/IS 3177 compliance statements, GST/MSME credentials, and named-customer case studies with photos and dates. Link customer logos to their sites. ABUS proves, it doesn't just claim.
4. **A downloads library** with a per-product PDF catalogue/spec sheet, each shown with a thumbnail + file size.
5. **A glossary + educational layer** ("How does an EOT crane work?", "Choosing the right crane," IS-standard explainers) to win long-tail search and build topical authority — cheap, durable SEO SVMH currently lacks.
6. **Postal-code / region contact routing** if SVMH has regional service engineers or dealers — plus click-to-call `tel:` links everywhere.
7. **Dated case studies / "project of the month"** with named industries (automotive, steel, foundry, cement) — matches SVMH's actual client base and beats IndiaMART listings on credibility.
8. **Consistent low-friction CTA language** ("Request a quote," "Get a non-binding proposal," "Download brochure") repeated contextually on every product page.
9. **100% image alt-text discipline** and keyword-led unique titles/meta/H1 — easy wins ABUS executes perfectly.

## What SVMH Should AVOID

1. **Do NOT copy the performance profile.** ABUS's ~3.1 s TTFB / ~4.1 s load / 177 KB HTML / eager images / `preload="auto"` hero video is the worst part of the site. SVMH should target sub-1 s TTFB and LCP < 2.5 s: use a lightweight stack (static/JAMstack or well-tuned CMS), WebP/AVIF images, `loading="lazy"`, and a lazy-loaded video facade (click-to-play) rather than an autoplaying self-hosted hero.
2. **Do NOT ship without structured data.** ABUS omits JSON-LD schema — SVMH should implement Organization, Product, BreadcrumbList, and FAQ schema from day one to win rich results (a cheap edge over both ABUS and Indian competitors).
3. **Avoid the heavy, cruft-prone CMS pattern.** ABUS's Pimcore generates malformed URLs with spaces and likely drives the slow TTFB. SVMH should keep URLs clean/slugified and the stack lean.
4. **Add what ABUS lacks:** breadcrumbs (nav + BreadcrumbList schema), proper reciprocal hreflang if SVMH runs multi-language, on-page testimonial quotes, a live-chat/WhatsApp/callback widget (especially valuable in the Indian B2B market), and inline form validation + spam protection.
5. **Don't bury credentials.** Surface ISO/IS badges near CTAs and in the footer, not only in a downloads page.
6. **Skip off-message content** (ABUS's conference-room "Tagung.Mal.Anders" block) on the core buyer journey — keep the homepage focused on cranes, proof, and inquiry.

---

## Evidence & Sources (all accessed 2026-07-05)

- Homepage: https://www.abus-kransysteme.de (markdown + raw HTML scrape) — nav, hero video, product finder, brand story, logos, case studies. Confidence High.
- Sitemap/IA: firecrawl_map of domain (300+ URLs) + https://www.abus-kransysteme.de/robots.txt (2 XML sitemaps). Confidence High.
- Product page: https://www.abus-kransysteme.de/krane/laufkrane/zweitraegerlaufkrane — spec table (120 t / 42 m), install variants, galleries. Confidence High.
- RFQ: https://www.abus-kransysteme.de/krane/laufkrane/zweitraegerlaufkrane/anfrage — technical + site-condition fields, dimension diagram, GDPR consent, noindex. Confidence High.
- Contact: https://www.abus-kransysteme.de/kontakt — postal-code rep finder, HQ, tel/mailto/map/social. Confidence High.
- Downloads: https://www.abus-kransysteme.de/downloads — catalogues, ISO 9001 (valid 2026–2029), EN 1090, T&Cs, paint systems. Confidence High.
- SEO markup: raw-HTML grep — 0 JSON-LD blocks, 1 hreflang (x-default), canonical present, 27/27 img alt, 0 lazy-load, 0 breadcrumb. Confidence Medium-High.
- Performance: curl timing probe — TTFB 3.14 s, total 4.09 s, 177,480 bytes; headers nginx/Pimcore, cache-control 28 days. Confidence Medium (single run, one location).
- Cross-references: sitemap page titles/descriptions corroborate product specs and page purposes; company facts (1965, Gummersbach, 120 t, family-owned) confirmed across homepage, `/unternehmen`, `/kranhersteller-deutschland` meta, and `/anfrage` HQ block.

**Low-confidence / unverified:** exact Lighthouse scores and Core Web Vitals field data (not run); body content of JS-gated LPs (`/kranhersteller-deutschland`, `/shop` returned thin rendered text); whether any schema is injected client-side post-load; spam-protection mechanisms on forms.
