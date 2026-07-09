# Website Audit — Demag Cranes & Components

**Site audited:** https://www.demagcranes.com (global English `/en`; also reviewed `/en-in`, `/en-us`, product + contact + configurator pages)
**Auditor context:** Competitive research for S.V. Material Handling System Pvt Ltd (SVMH), Bengaluru
**Date accessed:** 2026-07-05
**Method:** Live scrape via firecrawl_scrape / firecrawl_map / firecrawl_search; raw-HTML head inspection for SEO signals
**Overall confidence:** High for on-page structure/SEO/UX (directly observed); Medium for page-speed and mobile (inferred from code signals, not lab-tested)

---

## 0. Company / Site Context (for interpreting the audit)

| Fact | Detail | Source | Confidence | Evidence |
|---|---|---|---|---|
| Brand heritage | "more than 200 years" of material-flow solutions; roots to 1819 | https://www.demagcranes.com/en ; https://www.preqin.com/data/profile/asset/konecranes-and-demag-private-limited/351489 | High | Homepage: "for more than 200 years"; Preqin: "founded in 1819" |
| Ownership | Part of Konecranes group ("Konecranes and Demag") | https://www.konecranes.com/contact-us/locations/konecranes-and-demag-private-limited | High | Konecranes site lists "Konecranes and Demag Private Limited" |
| Legal entity | Demag Cranes & Components GmbH, Ruhrstraße 28, 58300 Wetter, Germany | https://www.demagcranes.com/en (footer) | High | Footer: "Demag Cranes & Components GmbH … 58300 Wetter, Germany" |
| India presence | Demag Distribution India, Godrej Eternia, Shivajinagar, Pune 411005; plus local distributors (Vedant Equip, etc.) | https://www.demagcranes.com/en-in/legal-notice ; international-search?country=IN | High | Legal Notice India address; distributor listing |
| Platform | Drupal 10 CMS | Raw HTML `Generator` meta | High | `"Generator": "Drupal 10"` |

**Key takeaway for SVMH:** This is a global-enterprise, multi-brand, distributor-led site. It is a *benchmark for structure and content depth*, not a like-for-like SME competitor. Demag sells through partners and does NOT show prices or a direct e-commerce checkout on the marketing site (that lives behind the Demag Portal/Shop login).

---

## 1. Navigation

| Aspect | Finding | Source | Confidence | Evidence |
|---|---|---|---|---|
| Primary nav model | Product-led mega-menu: Cranes / Hoist Units / Drives / Components & Parts / Services / Configurators | /en | High | Sticky main nav with 6 top items, each expanding to image-rich subcategory cards |
| Mega-menu quality | Each dropdown shows product thumbnail + name + one-line benefit (e.g. "Rope hoists — High handling rates up to 100 tonnes") | /en | High | Menu items carry descriptive microcopy, not bare links |
| Secondary/global nav | What's new, Company, Careers, References | /en | High | "Global Navigation" block |
| Utility nav | "Get in touch", "Demag Portal", "Your worldwide Demag partners", search | /en | High | Top utility strip present on every page |
| Persistent side icons | Contact / Configurators / References quick-access icons | /en | High | Sidebar icon links in markup |
| Language/country switcher | 14 locales (EN, DE, EN-AU, PT-BR, ZH, CS, FR, EN-IN, IT, PL, ES, EN-US, SEA) | /en | High | Country/language chooser modal |
| Search | Global search present ("press enter to search") | /en | High | Search field in nav + `/search` |

**Strength:** Clear, benefit-annotated, visual mega-menu; strong internationalization. **Weakness:** Depth is high — reaching a specific product can take 3+ clicks; the country modal interrupts first visit.

---

## 2. Sitemap & Information Architecture

| Aspect | Finding | Source | Confidence | Evidence |
|---|---|---|---|---|
| XML/HTML sitemap | Dedicated `/sitemap` linked in footer | /en | High | Footer "Sitemap" link |
| "Products A–Z" index | Alphabetical product index page exists | /en/products/products-z | High | Linked in nav + footer |
| IA hierarchy | Products → category → subcategory → product; Services; Industry Expertise (References/Case Studies); Company; Configurators | /en, map | High | URL patterns e.g. `/products/hoist-units/dvr-rope-hoist` |
| Industry landing pages | Automotive, Railways, Recycling, Shipbuilding, etc. | map results | High | `/en/industries/automotive`, `/en-us/industries/railways` |
| Legacy/localization debt | Many `/node/####` URLs and mismatched language content (Czech/Polish text under `/es/`, `/it/` paths) | map | Medium | Map shows `/es/node/1341` titled in Czech; cross-language leakage |

**Strength:** Multiple discovery paths (mega-menu, A–Z, sitemap, search, configurators, industries). **Weakness:** Localization hygiene is poor — content mismatched to locale folders and exposed `/node/` IDs signal migration debt and hurt SEO.

---

## 3. Homepage Structure

| Section (in order) | Content | Source | Confidence |
|---|---|---|---|
| Hero slider | 3 rotating banners (MPW winch, FSS steel structure, Configurators) each with H2 + "Read more" | /en | High |
| Tools row | Demag Portal (16,000+ products), Demag Designer (CAD models), Docu System (brochures) | /en | High |
| Positioning block | "We deliver best performance" — heavily internally linked paragraph | /en | High |
| Partner recruitment | "Become a Demag Official Country Partner!" → mailto CTA | /en | High |
| Category cards | Configurators, References, Cranes, Hoists, Drives, Components (image tiles) | /en | High |
| Case studies carousel | 12+ named client stories (Omega Flex, Neumüller, MORELO, WILO, Arvato…) | /en | High |
| News | Dated press releases (latest 23.03.2026, LogiMAT 2026) | /en | High |
| Social/footer | Instagram placeholder, LinkedIn/Facebook/YouTube/Instagram, phone/fax, contact form link | /en | High |

**Strength:** Logical funnel — hero → tools → positioning → categories → proof (cases) → news. Rich proof density. **Weakness:** Hero is a carousel (rotating banners dilute focus and hurt LCP); an unrendered "[Instagram placeholder]" is shipped to production (see snippet in markdown: `## [Instagram placeholder]`) — a visible polish defect.

---

## 4. Product Pages (benchmark: DVR Rope Hoist, `/en-us/products/hoist-units/dvr-rope-hoist`)

This is the strongest part of the site and the best template for SVMH to study.

| Element | Finding | Confidence | Evidence |
|---|---|---|---|
| Hero + tagline | Full-width image + "Compact. Versatile. High performance." | High | Page H1 "DVR Rope Hoist" + subhead |
| Benefit-first intro | Plain-language value prop before specs | High | "It offers high levels of efficiency and productivity…" |
| Spec bullets | Concrete figures: "Five sizes with load capacities of up to 80 metric tons"; motor "up to 35 kilowatts"; "IP 55 … optionally IP 66" | High | Bulleted spec lists |
| Model breakdown | 4 model variants (F-DVR, EU-DVR, EK-DVR, EZ-DVR) each with image + capacity | High | Model cards with per-model load capacities |
| Deep tech accordions | Rope Drum, Rope Guide, Motor & Brake, ProHub, Travel Motor, Housing, Bottom Block, Control | High | Expandable "The benefits at a glance", "Rope Drum and Guide", etc. |
| Smart features | Anti-Sway, Slack-Rope Prevention, Area-Specific Load Reduction, Bypass, Tandem, Follow-Me, Hook Centering — each illustrated | High | Feature blocks with images |
| Downloads | Product brochure PDF + **three role-specific RFQ PDFs** (Crane Kit, Solo Hoists, Tandem Hoists) | High | "Downloads → Documents" links to `.pdf` files |
| Cross-sell | "Further products" (DH Rope Hoist, DRC joystick, DST pendants) | High | Related-product cards |
| Images | ~10 product/detail images with descriptive filenames + alt text | High | Model + feature imagery |

**Strength:** Textbook technical product page — benefit → specs → variants → deep engineering detail → downloadable RFQ/brochure → cross-sell. Every claim carries a number. **Weakness:** No visible price/lead-time (by design — distributor model); RFQ is a downloadable PDF form rather than an inline smart form (adds friction vs a web form).

---

## 5. Landing Pages & Configurators (lead-gen engine)

| Aspect | Finding | Source | Confidence | Evidence |
|---|---|---|---|---|
| Configurator hub | Three self-serve configurators: KBK (light crane), Hoists, Drives | /en/demag-configurators | High | "Your offer in just a few clicks" with 3 configurator cards |
| Configurator promise | "type in the data you know… a Demag partner or Demag employee will get in touch" | /en/demag-configurators | High | Explicit lead-routing statement |
| Industry landing pages | Per-vertical pages (Automotive: "reliable partner to the automotive industry for decades") | /en/industries/automotive | High | Industry copy + fields of application |
| Campaign/event pages | LogiMAT 2026 product info, Fairs & exhibitions | map | High | `/en/logimat-product-information` |
| Country-partner LP | "Become a Demag Official Country Partner" recruitment block | /en, /en/contact | High | Repeated distributor-recruitment CTA |

**Strength:** Configurators are a major differentiator — they convert an ambiguous "contact us" into a structured, qualified quote request, and are surfaced in the top nav, homepage hero, and every product context. **Weakness:** Configurator output is still "a partner will get in touch" (not instant pricing), so it's lead-capture, not true self-service commerce.

---

## 6. RFQ / Quote Flow

| Aspect | Finding | Confidence | Evidence |
|---|---|---|---|
| Primary RFQ path | Configurator → structured requirement → routed to partner/employee | High | /en/demag-configurators |
| Secondary RFQ path | Downloadable RFQ PDF forms on product pages | High | DVR page: 3 RFQ PDFs |
| Tertiary path | Generic contact form + "Your worldwide Demag partners" locator | High | /en/contact, /en/international-search |
| Commerce path | Demag Portal/Shop — "order more than 16,000 products online" (login-gated) | High | Homepage tools row |

**Strength:** Multiple, intent-matched RFQ routes (self-serve configurator, PDF for procurement teams, human contact, online shop). **Weakness:** PDF RFQ forms feel dated and break the digital flow; no single obvious "Request a Quote" button persistent across product pages.

---

## 7. Contact Flow

| Aspect | Finding | Source | Confidence | Evidence |
|---|---|---|---|---|
| Contact form fields | First/Last name, Company, Street, Zip, Location, Country (full ISO list), Email, Phone, Industry, Message + privacy consent | /en/contact | High | Full field list rendered |
| Consent/GDPR | Explicit "I have read and understood [privacy] " checkbox; honeypot ("Leave this field blank") | /en/contact | High | Consent line + anti-spam field |
| Partner locator | "Your worldwide Demag contacts" / international search with country filter | /en/international-search | High | Country-parameterized locator |
| Direct contacts | Phone +49 (0)2335 92-0, Fax, mailto links (partner team) | /en footer | High | Footer contact block |
| Localized contact | India contact routes to `/en-in/contact` and Pune entity | /en-in | High | India locale contact link |

**Strength:** Professional, GDPR-compliant form with industry + country routing and a global partner locator; spam-protected. **Weakness:** Form heading shows untranslated German "Kontakt" on the English page — another localization defect. No live chat / callback scheduler / instant confirmation shown.

---

## 8. Trust Elements

| Element | Finding | Source | Confidence | Evidence |
|---|---|---|---|---|
| Heritage | "more than 200 years", "one of the world's leading manufacturers" | /en | High | Positioning paragraph |
| Case studies | 12+ named, industry-tagged client stories with photos | /en | High | Case-study carousel |
| References hub | Dedicated References / Case Studies section | /en/industry-expertise/references | High | Nav + footer |
| Named blue-chip clients | thyssenkrupp Marine Systems, Airbus, WILO, Arvato (news/cases) | /en-in, /en | High | Press releases naming clients |
| ISO certifications | Dedicated ISO Certifications page | /en-us/iso-certifications-1 | Medium | Page title in map (content not fully scraped) |
| Compliance | REACH Notice, Supply-Chain Act (LkSG) policy PDF, Whistleblowing channel | /en, map | High | Footer + LkSG policy PDF |
| Social proof | LinkedIn/Facebook/YouTube/Instagram links | /en | High | Footer social row |

**Strength:** Deep, verifiable trust stack (named marquee clients, quantified case studies, ISO, regulatory compliance). **Weakness:** No customer logos wall or testimonials with quotes on the homepage; trust proof is a click away in References.

---

## 9. Images, Video & Media

| Aspect | Finding | Confidence | Evidence |
|---|---|---|---|
| Image format | Modern WebP delivered site-wide (`.jpg.webp`, `.png.webp`) via Drupal image styles | High | All image URLs end `.webp` with `?itok=` derivative tokens |
| Responsive images | Multiple named styles (hero, medium, slider_banner, subcategory_menu_liftup, max_325x325, thumbnail) | High | Style variants in URLs |
| Alt text | 83/83 `<img>` on homepage carry `alt` attributes | High | Raw-HTML: img count 83, all with alt |
| Lazy loading | `loading="lazy"` used extensively (~90 occurrences) | High | Raw HTML count |
| Video | No embedded homepage video found in scrape; YouTube channel linked (demagcranesTV) | Medium | No `<video>`/iframe in main content; YT footer link |

**Strength:** Best-practice image pipeline — WebP + responsive derivatives + universal alt text + lazy loading. **Weakness:** Little/no on-page video storytelling despite an active YouTube channel; product pages rely on stills.

---

## 10. Downloads / Technical Documentation

| Aspect | Finding | Confidence | Evidence |
|---|---|---|---|
| Product brochures | Per-product PDF brochures | High | DVR page brochure PDF |
| RFQ forms | Downloadable RFQ PDFs (multiple variants) | High | DVR page |
| Docu System | "Docu System" portal for documentation (login) | High | Homepage + footer link (demag-doku.de) |
| Demag Designer | CAD model download / technical-info portal | High | Homepage tools row (demag-designer.com) |
| Compliance docs | LkSG policy PDF, REACH notice | High | Footer/PDF link |

**Strength:** Rich, segmented documentation ecosystem including CAD models — extremely valuable to engineers specifying equipment. **Weakness:** Much of the richest content (Docu System, Portal) is login-gated, invisible to search engines and first-time evaluators.

---

## 11. CTAs

| CTA | Placement | Confidence |
|---|---|---|
| "Read more" | Hero slides, category cards | High |
| "Get in touch" / "Contact form" | Utility nav + footer (every page) | High |
| Configurators | Nav, hero, homepage, product context | High |
| "Learn more" | Every case study | High |
| "Apply now" / "Contact us now" (partner) | Homepage + contact page (mailto) | High |
| RFQ PDF downloads | Product pages | High |

**Strength:** CTAs present at every scroll depth and matched to intent (learn / configure / contact / apply). **Weakness:** Generic verbs ("Read more", "Learn more") dominate; few action-oriented, value-loaded CTAs ("Get my quote", "Download spec sheet"). Two competing homepage priorities (buy vs become-a-partner) can dilute the primary buyer path.

---

## 12. SEO Structure

| Signal | Finding | Source | Confidence | Evidence |
|---|---|---|---|---|
| Title tag | "Cranes, hoists and drives \| Demag" — keyworded + brand | Raw HTML | High | `<title>` |
| Meta description | Present, keyword-rich, ~155+ chars | Raw HTML | High | "Powerful reliable light crane systems…" |
| Meta keywords | Present (legacy, low SEO value): "Demag, cranes, hoists, drives, components…" | Raw HTML | High | `keywords` meta |
| H1 | Exactly one H1 per page | Raw HTML | High | H1 count = 1 ("Demag MPW" hero) |
| Heading hierarchy | H1×1, H2×18, H3×3 on homepage | Raw HTML | High | Tag counts |
| Canonical | Correct self-canonical | Raw HTML | High | `rel="canonical" href="…/en"` |
| Hreflang | 14 hreflang alternates incl. `x-default` | Raw HTML | High | 14 hreflang tags (cs, de, en-AU, en-CN, en-IN, en-US, es, fr, it, pl, pt-br, sea, zh-hans, x-default) |
| Structured data (schema.org / JSON-LD) | **NONE detected** | Raw HTML | High | No `ld+json`, no `schema.org` string in HTML |
| Open Graph / Twitter cards | **NONE detected** | Raw HTML | High | No `og:` or `twitter:` tags found |
| Descriptive URLs | Clean, keyword URLs for main pages (`/products/hoist-units/dvr-rope-hoist`)… | map | High | URL patterns |
| …but | …legacy `/node/####` URLs and cross-language content still indexed | map | Medium | `/es/node/1341` etc. |

**Strength:** Solid fundamentals — unique titles/descriptions, single H1, correct canonical, extensive hreflang for 14 markets. **Weakness (significant):** No structured data (schema.org Organization/Product/BreadcrumbList) and no Open Graph/Twitter tags — the site forfeits rich results and controlled social-share previews. Legacy `/node/` URLs and mislocalized content are indexation liabilities. This is a *clear, copyable opening for SVMH*.

---

## 13. Internal Linking

| Aspect | Finding | Confidence | Evidence |
|---|---|---|---|
| Contextual links | Positioning paragraph links out to 6+ deep pages (light crane, components, hoists, drives, solutions, history) | High | Inline links in homepage prose |
| Cross-sell links | Product pages link related products | High | DVR "Further products" |
| Hub-and-spoke | Category → subcategory → product; case studies interlink to product categories | High | URL + link structure |
| Footer mega-links | Full products/services/company link farm in footer | High | Footer navi |
| A–Z + sitemap | Products A–Z and /sitemap aid crawl + discovery | High | Footer links |

**Strength:** Dense, contextual internal linking (prose links, cross-sell, footer, A–Z, sitemap) — strong for both users and crawlers. **Weakness:** Some links are self-referential `#` anchors in nav (top-level items point to `#` and rely on hover), which can confuse mobile/crawler navigation.

---

## 14. Page-Speed Signals (inferred, not lab-measured)

| Signal | Finding | Confidence | Evidence |
|---|---|---|---|
| Image optimization | WebP + responsive derivatives + lazy loading (~90) | High | Raw HTML |
| CMS | Drupal 10 (mature caching/aggregation available) | High | Generator meta |
| Homepage weight | 83 images + rotating hero carousel — heavy above-the-fold | Medium | Image count; carousel |
| LCP risk | Auto-rotating hero banner (large image) as LCP element | Medium | Hero slider markup |
| Tag load | Google Tag Manager + gtag + OneTrust consent | High | Scripts detected |

**Strength:** Image delivery is genuinely well optimized. **Weakness:** Large hero carousel + 80+ images + GTM/consent stack likely pressure LCP/INP; not verified with Lighthouse here (Confidence: Medium). **Recommend SVMH run its own PageSpeed test before making hard claims.**

---

## 15. Mobile Experience (inferred)

| Signal | Finding | Confidence | Evidence |
|---|---|---|---|
| Viewport | `width=device-width, initial-scale=1.0` set | High | Raw HTML |
| Mobile flags | `HandheldFriendly: true`, `MobileOptimized: width` | High | Meta tags |
| Responsive images | Device-appropriate WebP styles | High | Image styles |
| Risk | Deep multi-level mega-menu can be cumbersome on touch | Medium | Nav depth |

**Strength:** Explicitly responsive, mobile-optimized meta + responsive images. **Weakness:** Not touch-tested here; deep nav + country modal may add mobile friction (Confidence: Medium).

---

## 16. UX Patterns Observed

- Benefit-annotated mega-menu (thumbnail + name + one-liner).
- Configurator-first lead capture surfaced everywhere.
- Consistent proof pattern: every section funnels to case studies.
- Accordion/tabbed deep-dives on product pages (progressive disclosure).
- Persistent quick-access side icons (Contact/Configurator/References).
- Multi-locale with country modal + partner locator.
- Consistent card design language across cases, categories, products.

---

## STRENGTHS & WEAKNESSES — Summary Table

| # | STRENGTHS | WEAKNESSES |
|---|---|---|
| 1 | Best-in-class **technical product pages** (benefit → quantified specs → model variants → deep engineering accordions → downloads → cross-sell) | **No structured data (schema.org/JSON-LD)** and **no Open Graph/Twitter tags** — forfeits rich results & social previews |
| 2 | **Self-serve configurators** (KBK/Hoists/Drives) turn "contact us" into qualified, structured leads | RFQ still relies on **downloadable PDF forms**; no persistent inline "Request a Quote" web form on product pages |
| 3 | **Deep trust stack**: 200-yr heritage, named blue-chip clients (Airbus, thyssenkrupp), 12+ quantified case studies, ISO, REACH/LkSG | **Localization hygiene is poor**: German "Kontakt" heading on EN form, cross-language content under wrong locale folders, exposed `/node/` URLs |
| 4 | **Excellent media pipeline**: universal WebP, responsive derivatives, 100% alt text, lazy loading | **Visible production defects**: shipped `[Instagram placeholder]`; auto-rotating hero carousel likely hurts LCP |
| 5 | **Strong IA & discovery**: mega-menu + Products A–Z + sitemap + search + industry pages + configurators | **High click-depth** to reach a product; **generic CTAs** ("Read more"/"Learn more"); competing buyer-vs-partner priorities on homepage |
| 6 | **Solid SEO fundamentals**: unique titles/descriptions, single H1, correct canonical, **14-market hreflang** | Richest content (**Docu System, Portal, CAD Designer**) is **login-gated** — invisible to SEO and first-time evaluators; no on-page video |
| 7 | **GDPR-compliant contact** (consent + honeypot), global **partner locator** with country routing | No live chat / callback scheduler / instant lead confirmation surfaced |
| 8 | Consistent, professional **card-based design system**; dense contextual internal linking | Top-level nav items are `#` anchors reliant on hover (mobile/crawler friction) |

---

## What SVMH Should COPY

1. **Templated technical product pages.** For every crane type (EOT single/double girder, gantry, jib, EOT hot/ladle) and every component (crab units, forged hooks, DSL busbars, gearboxes, rope drums), build the Demag pattern: one-line benefit tagline → quantified spec bullets (capacity in tonnes, span, class IS 807/FEM 9.511, duty) → variants → downloadable datasheet/brochure PDF → related products. Every claim gets a number.
2. **A configurator / structured RFQ.** Even a lightweight 3-step "Configure your crane" form (type → capacity/span → duty class → contact) beats a bare contact form. This is Demag's biggest conversion asset and directly attacks SVMH's IndiaMART dependence by capturing leads on-site.
3. **Quantified, named case studies by industry.** SVMH serves automotive, steel, power, foundry, cement, construction — build one photo-backed case study per vertical with the load/span/outcome numbers. Tag them by industry.
4. **Trust stack, surfaced early.** ISO 9001, IS-standard compliance, MSME/GST, client logos, and years-in-business (since 2006) — put a proof band on the homepage, not buried.
5. **Media discipline:** WebP + responsive images + alt text on 100% of images + lazy loading. Cheap, high-ROI, and helps SEO/PageSpeed where SVMH can beat an enterprise site.
6. **Downloadable datasheets/brochures + a spec library** as gated-optional lead magnets (email for full catalog).
7. **Industry landing pages** (one per vertical) to capture long-tail search like "EOT crane for foundry" / "ladle crane steel plant India".
8. **hreflang / clean descriptive URLs** — SVMH only needs EN (+ optional Hindi/Kannada) but should adopt the clean `/products/eot-crane/double-girder` URL discipline.

## What SVMH Should AVOID

1. **Do NOT ship without structured data & Open Graph.** Demag's biggest SEO miss. SVMH should add schema.org `Organization`, `Product`, `BreadcrumbList`, and OG/Twitter tags from day one — a cheap way to *out-rank and out-share* a giant.
2. **Do NOT rely on PDF RFQ forms.** Use inline, mobile-friendly web forms with instant confirmation; PDFs add friction and are invisible to analytics.
3. **Avoid auto-rotating hero carousels.** Use a single, fast-loading hero with one clear CTA (better LCP, clearer message) — critical for India's mobile-first, variable-bandwidth users.
4. **Avoid localization/migration debt.** Don't leave placeholder text ("[Instagram placeholder]"), untranslated labels, or orphan `/node/` URLs live. A small clean site with zero defects reads as more trustworthy than a large messy one.
5. **Don't gate your best content.** SVMH's advantage is openness — keep datasheets, spec tables, and capability content indexable and ungated (or soft-gated) so Google and first-time buyers can see them.
6. **Don't split the homepage's primary CTA.** Keep one dominant path (Get a Quote). Demag dilutes with "become a partner" — SVMH should stay laser-focused on buyer conversion.
7. **Don't over-nest navigation.** Keep products reachable in ≤2 clicks; avoid `#`-anchor top-level items that need hover.

---

## Evidence & Source Log (accessed 2026-07-05)

| # | URL | Used for | Confidence |
|---|---|---|---|
| 1 | https://www.demagcranes.com/en | Homepage, nav, footer, SEO meta, trust, CTAs | High |
| 2 | https://www.demagcranes.com/en (rawHtml) | Title/desc/H-tags/canonical/hreflang/schema/OG/img/lazy/analytics | High |
| 3 | https://www.demagcranes.com/en/contact | Contact/RFQ form fields, GDPR, defects | High |
| 4 | https://www.demagcranes.com/en/products/cranes-and-cranes-sets | Product category page structure | High |
| 5 | https://www.demagcranes.com/en/demag-configurators | Configurator lead-gen flow | High |
| 6 | https://www.demagcranes.com/en-us/products/hoist-units/dvr-rope-hoist | Deep product-page benchmark, RFQ PDFs, downloads | High |
| 7 | https://www.demagcranes.com/en-in | India locale homepage | High |
| 8 | firecrawl_map (site link inventory) | Sitemap/IA, localization debt, industry pages | High |
| 9 | https://www.demagcranes.com/en-in/legal-notice | India entity (Pune) | High |
| 10 | https://www.konecranes.com/.../konecranes-and-demag-private-limited | Ownership cross-reference | High |
| 11 | https://www.preqin.com/data/profile/asset/konecranes-and-demag-private-limited/351489 | Founding year cross-reference (1819) | Medium |

**Unverified / Low-confidence items (flagged):** Actual Lighthouse/PageSpeed scores (inferred only); live video presence on inner pages; ISO page contents (title seen, body not fully scraped); true mobile touch behavior. Any hard performance figure should be re-tested with Google PageSpeed Insights before publication.
