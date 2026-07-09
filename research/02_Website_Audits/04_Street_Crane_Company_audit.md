# Website Audit — Street Crane Company

**Auditor:** Competitive research (SVMH website project)
**Subject site:** https://www.streetcrane.co.uk → redirects to **https://streetcrane.com/** (primary canonical domain)
**Date accessed:** 2026-07-05
**Method:** Live scrape via firecrawl_scrape + firecrawl_map, raw HTML/`curl` inspection of sitemaps, schema, and headers, plus firecrawl_search cross-reference.
**Company context:** Street Crane Company Limited (Companies House no. 00603923), Chapel-en-le-Frith, High Peak, SK23 0PH, UK. Positions itself as "the UK's largest overhead crane manufacturer," family-owned, ~80 years' heritage (founded 1946), exports to 70+ countries via 100+ distributors. CMS: WordPress 6.8.5 with Yoast SEO. Agency: visionsharp.co.uk.

> **Why this competitor matters to SVMH:** Street is a mature, export-focused, family-owned EOT/overhead crane manufacturer — structurally similar to SVMH but two orders of magnitude ahead on digital maturity. It is a strong "north star" reference for what a credible global crane website looks like. Their exact product taxonomy (single/double girder, portal/goliath, jib, underslung, hoists, spares, AMC-style service) maps almost 1:1 onto SVMH's catalogue, so their IA and page structure are directly transferable.

---

## 1. Executive Summary

Street Crane runs a modern, well-architected WordPress marketing site that is far more sophisticated than SVMH's IndiaMART-dependent presence. Its strengths are a clean product taxonomy, deep engineering-led copy, a strong trust stack (80-year heritage, 30,400+ projects, blue-chip client logos, real case studies), a multi-context tabbed RFQ form that captures technical crane specs (SWL, span, HOL, duty), and solid technical SEO (Yoast, Product/Organization/Service schema, clean URL hierarchy, XML sitemaps). 

Its notable weaknesses: almost **no downloadable technical documentation** (only a Cyber Essentials PDF and a gated brochure request are exposed — no open datasheets/load tables/CAD), **thin video/rich media** despite the industrial subject, a **mobile viewport that disables user zoom** (`user-scalable=no` — an accessibility red flag), **duplicated content blocks** on product pages (the "Built for performance and longevity" section is repeated verbatim), and a **conversion path that funnels everything through a single "we'll be in touch" enquiry model** with no instant pricing, live chat, or self-service configurator. Confidence: **High** for structure/SEO/content (directly observed); **Medium** for performance (limited to header timing + HTML weight, no full Lighthouse run).

---

## 2. Navigation & Information Architecture

| Element | Finding | Confidence |
|---|---|---|
| Primary nav | Products (mega-menu), Spare Parts, Industries (mega-menu, 15 sectors), Our Company, Global Distributors, Contact Us | High |
| Mega-menu depth | 3 levels deep under Products: Cranes → Overhead → Single/Double Girder; Portal → Full/Semi; Jib → Column/Freestanding/Wall Travelling; Underslung → Single/Double; plus Components → Hoists (LX/ZX/VX/Special), End Carriages, Crane Kits | High |
| Utility nav | Sales phone `+44(0)1298 812456`, Contact form link, Servicing phone — all persistent in header | High |
| Extras | Site search (`/?s=`), Customer Portal "Sign In" (`cp.streetcrane.com`) | High |
| Contextual CTA | Mega-menu contains an embedded "Contact Us / Get In Touch" mini-panel | High |

**Evidence (nav structure):** Products menu resolves to `/cranes/`, `/cranes/overhead-cranes/single-girder/`, `/cranes/portal-cranes/`, `/hoists/chain-hoists/`, `/hoists/wire-rope-hoists/ (ZX)`, `/hoists/open-winch-hoists/ (VX)`, `/cranes/hoists-components/crane-kits/` etc. (from homepage link map, 2026-07-05).

**Strength:** Logical, shallow-to-deep taxonomy that mirrors how a buyer actually shops (by crane type, by component, or by industry). Product naming pairs the generic term with the branded hoist family (e.g., "Wire Rope Hoists (ZX)") — good for both SEO and brand recall.

**Weakness:** "Our Company" parent link is a dead `#` anchor (`https://streetcrane.com/#`) rather than a real landing page; the dropdown children carry the links. Minor, but it is a non-functional top-level target.

---

## 3. Sitemap

Yoast-generated XML sitemap index at `/sitemap_index.xml` with segmented child sitemaps (observed 2026-07-05):

| Sitemap | URL count | Last modified |
|---|---|---|
| page-sitemap.xml | **60** | 2026-07-02 |
| post-sitemap.xml (news/blog) | **31** | 2026-04-28 |
| case-studies-sitemap.xml | **11** | 2026-06-29 |
| sector-sitemap.xml (industries) | **9** (custom taxonomy) | 2026-05-20 |
| area-sitemap.xml | present | 2026-05-07 |
| career-sitemap.xml | present | 2025-08-12 |
| category / post_tag / author | present | various |

**Strength:** Clean, recently-updated, segmented sitemaps with `lastmod` — strong crawl hygiene. Custom post types for `case-studies`, `sector`, `area`, `career` show a properly modelled content architecture, not just flat pages.

**Note:** Presence of `area-sitemap.xml` suggests a location/regional landing-page strategy (local SEO). Confidence: Medium (sitemap exists; individual area page content not scraped).

---

## 4. Homepage Structure

Section-by-section (from full scrape, 2026-07-05):

1. **Hero** — "Since 1946, One of the world's leading… **Crane Manufacturers and Suppliers.**" with "Who We Are" + "Scroll Down" cue. Video background present (1 `<video>` tag in HTML).
2. **Positioning paragraph** — "We Specialise in the Design, Manufacture, and Supply of Overhead Cranes and Hoists" + R&D/heritage narrative.
3. **3 product gateways** — Cranes / Components & Hoists / Spares & Servicing (image cards with descriptive copy).
4. **Stats bar** — **80** Years Experience · **30,400+** Projects Completed · **70** Countries.
5. **Client logo wall** — JCB, Bombardier, Honda, Rolls-Royce, Centrica, BMW, FP McCann, BAE (scrolling, duplicated set).
6. **Process narrative** — "Let Us Help You Discover The Right Application" (consultation → 3D modelling → install → post-install via sister co. Street CraneXpress).
7. **Case study carousel** — 8 named studies (AMRC, AV Dawson, Dunlop, Tiger Trailers, Tata Steel, Hitachi Rail, Hayward Tyler, Bombardier).
8. **CEO quote** — Gus Zona, Group CEO (photo + pull-quote on family values).
9. **Industries grid** — 6 featured sectors linking to 15-sector hub.
10. **Company/people** section → About.
11. **News** — 3 latest posts (dated April 2026 — content is current).
12. **Global distributor network** CTA.
13. **FAQ accordion** — 9 buyer-intent questions (why buy, industries, service area, how to get a quote, lead time 8–16 weeks, spares, become a distributor, "I'm new to cranes").
14. **Footer contact form** ("Get Started Today") + full contact block, certifications (Cyber Essentials PDF, BSI), social links (Facebook, LinkedIn, Instagram), navigation, legal.

**Strength:** Textbook B2B industrial homepage — leads with authority, proves it with numbers + logos + named case studies, explains the buying process, answers objections via FAQ, and closes with a form. Every claim is backed by a concrete artefact.

**Weakness:** The homepage is long and form-heavy; the same enquiry form appears in the footer of nearly every page, but there is no lightweight "quick quote" or sticky CTA bar beyond the header phone number.

---

## 5. Product Pages

Analysed: Single Girder (`/cranes/overhead-cranes/single-girder/`), Double Girder, Automotive industry page.

| Attribute | Finding | Confidence |
|---|---|---|
| Structure | H1 + capacity strap ("Capacities typically up to 25 tonnes") → hero image → intro → "Why choose" bullets → "Built for performance" → hoist options → FAQ → distributor CTA → enquiry form | High |
| Copy depth | Very deep, engineering-led. Explains ZX braked gearbox, oil-immersed helical gearing, guide rollers/flangeless wheels, patented safe-load cut-out, VFD control, DWP monitoring | High |
| Internal linking | Dense contextual cross-links to related crane types + relevant hoist families (ZX/LX) | High |
| Capacity specificity | Named limits: single girder ≤25t (ZX) / ≤5t (LX chain); double girder ≤250t; VX open winch ≤200t; portal spans >40m | High |
| Product-level FAQs | 8 technical FAQs on the single-girder page alone (top-running definition, ZX vs LX, cost-effectiveness, mechanical differentiators, VFD, safety features, downtime, spec checklist) | High |

**Strength:** Product copy is genuinely useful to a specifying engineer — it sells on lifetime cost of ownership, maintainability and specific mechanical features, not just capacity. The "what we need from you to spec correctly" FAQ (SWL, span, runway length, headroom, hook approach, duty cycle, power supply, environment) is excellent lead-qualification content.

**Weakness (significant):** **Duplicate content.** On the single-girder page the entire "Built for performance and longevity" block — heading, body, hoist-options list and "Talk to us" CTA — appears **twice, verbatim**. Looks like a page-builder duplication error. Hurts polish and marginally dilutes SEO.

**Weakness:** **No specification tables, load charts, or dimensional/wheel-load data on the page**, and **no downloadable datasheet**. All the hard numbers a buyer eventually needs are gated behind "contact us." For a technical audience this adds friction.

---

## 6. Landing / Industry Pages

15 industry pages (Aerospace, Automotive, Construction, Defence, Glass, Manufacturing, Metals, Paper, Plastics, Power, Precast, Renewables, Rail, Shipbuilding, Warehousing).

**Automotive page structure (evidence):** intro → sector-specific client logo wall (JLR, JCB, Toyota, Mercedes, VW, Ford, BMW, Volvo, Honda, Denso, Gestamp…) → "Crane solutions for automotive production" → 3 product gateways → design-considerations copy (press-shop vibration, BIW, headroom) → 3 tailored product recommendations (ZX single/double, VX heavy-duty ≤200t, portal/semi-portal) → sector case studies → enquiry form.

**Strength:** These are true vertical landing pages, not thin doorway pages. Each speaks the industry's language (BIW, die changes, powertrain, M8 duty), recommends specific product families, shows industry-specific logos, and links relevant case studies. This is a repeatable, scalable template SVMH could emulate directly for its automotive/steel/power/foundry/cement verticals.

**Weakness:** Heavy reliance on client logos raises a permissions/branding question but is a common industry practice; not a functional flaw.

---

## 7. RFQ / Quote Flow

The **`/contact-us/` page uses a tabbed multi-form design** with five contexts (evidence, 2026-07-05):

- **Request A Quote** — captures First/Last name, Company (req), Email (req), Phone, Country (req, full ISO list), County/State (req), **Product (Crane/Hoist/Crane Kit)**, **Height of Lift (m)**, **Capacity (tonnes)**, **Span (m)**, **Crane Type (Single/Double/Underslung/Portal-Goliath/Jib/Other)**, "Please specify crane type," Additional info, **file upload (≤49 MB)**, brochure opt-in, Terms consent.
- **Make An Enquiry** — lighter contact form.
- **Become A Distributor** — partner recruitment.
- **Spares** — includes **Crane/Hoist Serial Number**, Mechanical/Electrical fault selector, issue description, image upload → routes to `spares@streetcrane.com` / `+44(0)1298 816871`.
- Product pages + footer carry a shorter "Get Started Today" enquiry form (name, email, phone, location, message, file upload, brochure selector).

**Strength (strong):** The Request-A-Quote form captures the exact technical parameters an engineer needs to quote a crane (SWL, span, HOL, duty, type) plus drawing/photo upload. This is a genuine RFQ tool, not a generic contact box — it pre-qualifies leads and shortens the sales cycle. The dedicated **Spares form with serial number + fault type** is a smart aftermarket-service capture.

**Weakness:** The country/county/state dropdowns render **all three simultaneously** in the scraped DOM (UK counties, US states, ISO countries all present at once) — suggests conditional show/hide logic that relies on JS; if that logic fails or is slow, the form is confusing. No instant/indicative pricing, no configurator, no scheduling — everything ends in "a sales engineer will be in contact." reCAPTCHA is present (good for spam, adds friction).

---

## 8. Contact Flow & Trust Elements

| Trust element | Present? | Detail |
|---|---|---|
| Phone (sales + servicing) | Yes | `+44(0)1298 812456` (sales), `+44(0)1298 816871` (spares) — click-to-call in header/footer |
| Email | Yes | website@streetcrane.com, spares@streetcrane.com |
| Physical address | Yes | Chapel-en-le-Frith, High Peak, SK23 0PH, UK |
| Company registration | Yes | "Registered In England Company number: 603923" in footer |
| Certifications | Yes | **Cyber Essentials** (linked PDF certificate), **BSI** mark (ISO implied) |
| Heritage/scale proof | Yes | 80 years, 30,400+ projects, 70 countries, 100+ distributors |
| Named clients | Yes | JCB, Bombardier, Rolls-Royce, BMW, BAE, Tata, Honda, Centrica, JLR, Toyota, etc. |
| Case studies | Yes | 11 named, with challenge/solution/benefit + client quotes |
| Leadership visibility | Yes | CEO Gus Zona quoted+photo; "Our Sales Team" page; named Technical Director appointment in news |
| Social proof | Yes | Facebook, LinkedIn, Instagram (2K+ followers) |
| Customer portal | Yes | `cp.streetcrane.com` sign-in (self-service for existing customers) |

**Strength:** One of the most complete B2B trust stacks in this sector — heritage, scale, named blue-chip clients, real engineers, certifications, company-registration transparency, and an actual customer portal. This is the gold standard SVMH should benchmark against.

**Weakness:** No third-party review/testimonial platform (Trustpilot/Google reviews), and case-study client quotes are unattributed to a named individual in some cases.

---

## 9. Images, Video, Rich Media

- **Images:** ~47 `<img>` tags on the homepage; strong real-photography of factory, cranes in situ, staff, and installations. Product pages use genuine product/application photos, not stock renders.
- **Lazy loading:** **0** `loading="lazy"` attributes in the server-rendered HTML — images may be lazy-loaded via JS/plugin, but native lazy-loading is not applied. Confidence: Medium (raw HTML only).
- **Video:** 1 `<video>` (hero background) + 1 `<iframe>` on the homepage. **Rich video is thin** for such a visual, mechanical product — no product demo library, no installation walk-throughs surfaced.
- **Logos:** SVG logos for JCB/Bombardier/etc.; brand logo uses an "80 years" light variant.

**Strength:** Authentic, high-quality first-party imagery builds credibility.

**Weakness:** Under-uses video. A crane is a dynamic, physical product; competitors that show cranes lifting/installing on video convert better. Missing native lazy-loading may hurt LCP with 47 images.

---

## 10. Downloads / Technical Documentation

**This is the weakest content area.** Observed on the ZX wire-rope-hoist product page, the only linked PDF anywhere is the **Cyber Essentials certificate** — there are **no open datasheets, load tables, dimensional drawings, or CAD/BIM files** exposed on product pages.

Technical/brochure content is **gated**: forms offer a "Would you like to receive a brochure?" opt-in with a fixed list (Corporate Brochure, 75 Years & Counting, ZX Hoist, LX Hoist, VX Hoist) — you must submit a form to receive them.

**Weakness:** Specifying engineers strongly prefer self-serve datasheets and dimensional data. Gating everything behind a brochure request adds friction and loses top-of-funnel technical visitors who aren't ready to hand over contact details.

**Opportunity (for SVMH):** Open, ungated datasheets + IS-standard compliance tables + downloadable CAD would be a genuine differentiator against Street.

---

## 11. CTAs & Forms

- **Primary CTAs:** "Get In Touch," "Contact Us," "Talk to us," "Get Started Today," "Request A Quote," phone number, brochure request.
- **CTA placement:** Header (persistent phone + contact), in-menu mini contact panel, end of every product/industry page, sticky footer form on virtually all pages.
- **Forms:** Multi-context tabbed RFQ (5 types), short footer enquiry form, spares/service form. All use Gravity/WP-Forms-style fields with file upload (≤49 MB) and reCAPTCHA.

**Strength:** Consistent, omnipresent conversion paths; the CTA language is varied and buyer-appropriate ("I'm new to cranes — where should I start?").

**Weakness:** No live chat / WhatsApp / callback scheduler; no micro-conversions (e.g., "download load chart") for not-yet-ready buyers; single conversion model (form → sales callback).

---

## 12. SEO Structure

| Signal | Finding | Confidence |
|---|---|---|
| CMS/SEO plugin | WordPress 6.8.5 + **Yoast SEO** | High |
| Title tags | Keyword-rich, benefit + capacity + geo. e.g. "Single Girder Cranes \| Up to 25t \| UK Manufacturer & Supply"; "Double Girder Crane \| Up to 250t \| UK Supply & Manufacturer"; homepage "Crane Manufacturer UK & Global Supplier \| Street Crane Company" | High |
| Meta descriptions | Present, unique, keyword-targeted on every page checked | High |
| H1s | Single, clean H1 per page ("Single Girder Crane", "Double Girder Cranes", "Automotive Plant Cranes", "Contact Us") | High |
| URL structure | Clean, hierarchical, keyword-based (`/cranes/overhead-cranes/single-girder/`) | High |
| Schema (JSON-LD) | **Organization, Product (×4), Offer (×5), Service, ContactPoint, PostalAddress, Person, WebPage, SpeakableSpecification** on homepage | High |
| Robots | `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1` | High |
| Open Graph / Twitter | Full OG + `summary_large_image` Twitter cards, `en_GB` locale | High |
| Sitemaps | Segmented Yoast XML, recent lastmod | High |
| Canonical domain | `.co.uk` 301→ `.com` (single canonical) | High |

**Strength:** Technically excellent SEO. Rich structured data (Product/Offer/Service/Speakable — the latter targets voice search), disciplined title/H1 hygiene, semantic URLs, and fresh sitemaps. This site is built to rank and to earn rich results.

**Weakness:** Minor — the duplicated on-page content block (§5) and heavy reliance on JS-rendered forms are the only SEO drags observed. `Offer` schema without visible prices could risk schema-mismatch flags but is low-risk.

---

## 13. Internal Linking

**Strength:** Dense, contextual, intent-driven. Product pages link laterally to alternative crane types ("for heavier loads, explore double girder"; "where floor space needs to stay clear, single girder underslung") and down to component/hoist pages (ZX/LX). Industry pages link to specific products + case studies. Case studies link back to product and industry hubs. This creates strong topical clusters (crane types ↔ hoists ↔ industries ↔ case studies) that reinforce SEO authority and guide buyers.

**Weakness:** None material. The only broken internal target is the "Our Company" `#` parent (§2).

---

## 14. Page Speed Signals

| Signal | Measurement | Confidence |
|---|---|---|
| Server-rendered HTML weight | ~23 KB gzipped | High (curl) |
| Full page load (header timing) | ~2.4 s `time_total` for HTML doc (incl. DNS/TLS) | Medium |
| Image count (home) | ~47 images | High |
| Native lazy-loading | Not present in server HTML (0 `loading="lazy"`) | Medium |
| Render-blocking | WordPress theme + page-builder + reCAPTCHA + form scripts likely add JS weight | Low (inferred, not profiled) |

**Weakness:** A full Lighthouse/Core-Web-Vitals run was **not** performed, so LCP/CLS/INP are unverified — marked **Low/Medium confidence**. The combination of 47 images without native lazy-loading, a hero video, page-builder markup, and reCAPTCHA suggests real-world mobile LCP could be a concern, but this is **inferred, not measured**. Recommend a live Lighthouse test before treating as fact.

---

## 15. Mobile Experience

**Weakness (accessibility red flag):** The viewport meta is `width=device-width, initial-scale=1.0, **maximum-scale=1.0, user-scalable=no**` on every page checked. Disabling pinch-zoom fails **WCAG 2.1 SC 1.4.4 (Resize Text)** and harms low-vision users. This is a clear, fixable defect. Confidence: High (directly observed in metadata across pages).

**Strength:** Responsive theme with a dedicated mobile logo asset and a collapsing mega-menu (mobile "Products / Industries / Our Company" accordions present in scrape), so layout adapts — the issue is zoom lockout, not layout.

*(Full validation of mobile UX requires manual testing on devices and assistive tech; the `user-scalable=no` finding is definitive from the markup.)*

---

## 16. UX Patterns

- **Progressive disclosure** via mega-menus and FAQ accordions.
- **Repeated trust reinforcement** (stats, logos, case studies recur across page types).
- **Guided selling** — copy explicitly hand-holds ("I'm new to cranes, where should I start?"; "what we need from you to spec correctly").
- **Consistent template system** — product, industry, and case-study pages each follow a repeatable, recognisable layout.
- **Customer portal** for existing-customer self-service — a maturity signal most crane SMEs lack.

**Weakness:** Form-density can feel heavy; conditional dropdown logic (§7) may confuse on slow connections; no live-assist channel.

---

## 17. Strengths / Weaknesses Summary Table

| # | Strengths | # | Weaknesses |
|---|---|---|---|
| S1 | Clean 3-level product taxonomy mirroring buyer intent (type / component / industry) | W1 | **No open technical datasheets/load tables/CAD** — only a Cyber Essentials PDF; brochures are gated behind forms |
| S2 | Deep, engineering-led product copy selling on lifetime cost & maintainability, not just capacity | W2 | **Duplicate content block** ("Built for performance") repeated verbatim on product page |
| S3 | Elite trust stack: 80 yrs, 30,400+ projects, 70 countries, blue-chip logos, 11 named case studies, company reg, certs | W3 | **`user-scalable=no`** viewport — fails WCAG 1.4.4, blocks mobile zoom |
| S4 | Genuine RFQ tool capturing SWL/span/HOL/duty/type + drawing upload; dedicated spares form with serial+fault | W4 | Single conversion model (form → callback); no instant/indicative pricing, configurator, live chat, or callback scheduler |
| S5 | Strong technical SEO: Yoast, Product/Offer/Service/Speakable schema, clean URLs, fresh segmented sitemaps, geo+capacity titles | W5 | Thin video/rich media for a highly visual mechanical product |
| S6 | 15 true vertical industry landing pages with tailored copy, sector logos & case studies | W6 | Native lazy-loading absent on ~47 homepage images; full CWV unverified — possible mobile LCP risk |
| S7 | Dense contextual internal linking → strong topical clusters | W7 | "Our Company" top-level nav is a dead `#` anchor |
| S8 | Authentic first-party photography; customer portal for self-service; current news (Apr 2026) | W8 | Conditional country/county/state dropdowns render all options at once in DOM — JS-dependent, potentially confusing |

---

## 18. What SVMH Should COPY

1. **The product taxonomy & mega-menu** — Street's Cranes→(Overhead→Single/Double; Portal; Jib; Underslung) + Components→(Hoists LX/ZX/VX; End Carriages; Crane Kits) structure maps almost perfectly onto SVMH's catalogue (EOT single/double girder, gantry/portal, jib, monorail, crab units, hooks, DSL busbars, gearboxes). Adopt this shallow-to-deep IA.
2. **Vertical industry landing pages** — Build one tailored page per SVMH industry (automotive, steel, power, foundry, cement, construction) with sector-specific copy, client logos, recommended product families, and matching case studies. This is Street's highest-leverage, most repeatable pattern.
3. **A real RFQ form that captures crane specs** — SWL/capacity (tonnes), span (m), height of lift (m), crane type, duty class (map to IS 807 / IS 3177 / FEM 9.511 for SVMH), plus drawing/photo upload. Pre-qualifies leads and shortens the quote cycle. Add a separate **spares/AMC service form with serial number + fault type**.
4. **The full trust stack** — Heritage (since 2006), projects-completed counter, countries/clients served, named blue-chip customers, real case studies (challenge/solution/benefit + client quote), ISO 9001/GST/MSME certs displayed as badges, company registration transparency, and leadership visibility. SVMH already has the raw material (ISO 9001, MSME, family heritage) — it just needs to present it this well.
5. **Engineering-led, benefit-framed product copy + product-level FAQs** — Sell on reliability, maintainability, lifetime cost, and safety features, and include a "what we need to quote you correctly" checklist. Great for both conversion and long-tail SEO.
6. **Technical SEO discipline** — Yoast (or Rank Math), Product/Organization/Service JSON-LD schema, clean hierarchical URLs, capacity+geo-rich title tags (e.g., "Double Girder EOT Crane | Up to 250t | Bengaluru Manufacturer"), segmented XML sitemaps.
7. **Dense contextual internal linking** between crane types ↔ components ↔ industries ↔ case studies.

## 18b. What SVMH Should AVOID / DO BETTER

1. **Beat them on downloadable technical docs.** Street gates everything. SVMH should publish **open, ungated datasheets, IS-standard load/duty tables, dimensional drawings, and CAD/BIM files** — a real differentiator for specifying engineers, and a magnet for technical SEO traffic.
2. **Don't disable mobile zoom.** Never ship `user-scalable=no`. Keep the site WCAG-compliant from day one.
3. **Don't duplicate content blocks.** QA product pages so page-builder sections aren't repeated verbatim (Street's single-girder page shows this error).
4. **Add rich video** — crane-in-action clips, installation walk-throughs, factory tours. Street under-invests here; it's an easy win for a visual product.
5. **Offer more than "we'll call you."** Add WhatsApp/live chat (high-trust in the Indian B2B context), a callback scheduler, and micro-conversions (download-a-datasheet) so not-yet-ready buyers still convert.
6. **Get Core Web Vitals right from the start** — native lazy-loading, compressed/next-gen images, minimal render-blocking JS. (Street's CWV are unverified but its image/JS profile is a cautionary example.)
7. **Add third-party social proof** (Google reviews/testimonials with named attribution) — Street relies solely on first-party claims.

---

## 19. Evidence Log & Confidence

| Finding area | Primary source URL | Confidence | Notes |
|---|---|---|---|
| Homepage structure, stats, trust | https://streetcrane.com/ (scraped 2026-07-05) | High | Full markdown scrape; stats "80 / 30,400+ / 70" quoted directly |
| Product page structure & duplicate block | https://streetcrane.com/cranes/overhead-cranes/single-girder/ | High | "Built for performance and longevity" block observed twice verbatim |
| Industry landing template | https://streetcrane.com/industry/automotive-plant-cranes/ | High | Tailored copy + sector logos + product recos + case studies |
| Case study format | https://streetcrane.com/industry/case-studies/bombardier/ | High | Challenge/Solution/Benefit + client quote |
| RFQ & spares forms | https://streetcrane.com/contact-us/ ; https://streetcrane.com/crane-parts-service/ | High | 5-context tabbed form; spec fields + serial-number spares form observed |
| Sitemaps & counts | https://streetcrane.com/sitemap_index.xml (+ child sitemaps) | High | 60 pages / 31 posts / 11 case studies / 9 sectors |
| Schema/JSON-LD | Homepage raw HTML `grep` | High | Organization, Product×4, Offer×5, Service, ContactPoint, Speakable, WebPage |
| Title/meta/H1 | Page metadata + raw HTML `<title>`/`<h1>` | High | Yoast; capacity+geo titles confirmed on 2 product pages |
| Company identity / "largest UK manufacturer" | firecrawl_search: streetcrane.com, Instagram bio, Companies House 00603923 | High | Cross-referenced ≥2 sources (own site + Companies House + Instagram) |
| Page weight / images / lazy-load / video | `curl` header timing + HTML grep | Medium | 23 KB HTML, ~2.4s doc load, 47 imgs, 0 native lazy-load, 1 video/1 iframe |
| Mobile `user-scalable=no` | Page metadata (all pages) | High | WCAG 1.4.4 concern, directly observed |
| Full Core Web Vitals (LCP/CLS/INP) | — | Low | **Not measured** — no Lighthouse run; inferred only. Verify before citing as fact |

**Cross-referencing note:** The "largest UK overhead crane manufacturer / 80 years / founded 1946 / 70+ countries" positioning is corroborated across the company's own site, its Instagram bio ("UK's largest overhead crane manufacturer"), and Companies House (co. 00603923). The "30,400+ projects" figure appears only on the company's own homepage (single-source) — **Confidence: Medium** for that specific number.

---
*Audit complete. All live data captured 2026-07-05 via firecrawl_scrape/map, curl, and firecrawl_search. Figures not independently verifiable (e.g., 30,400+ projects) are flagged as single-source. Core Web Vitals were not profiled and should be measured with Lighthouse before being treated as established fact.*
