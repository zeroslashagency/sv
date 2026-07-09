# Website Audit — Konecranes (konecranes.com)

**Subject:** Konecranes Plc — global material handling / overhead crane leader
**Audited for:** S.V. Material Handling Systems Pvt Ltd (SVMH), Bengaluru — competitive landscape research to build a superior website
**Auditor:** Fox (research subagent)
**Date accessed:** 2026-07-05
**Primary URL:** https://www.konecranes.com
**Method:** Live scrape (firecrawl_scrape / firecrawl_map), raw HTML inspection (curl), sitemap + robots.txt parse, network timing. PageSpeed Insights API was quota-blocked on the day of audit (noted where relevant).

> **Context note:** Konecranes is a ~EUR 4bn revenue, NASDAQ-Helsinki-listed global player. It is NOT a like-for-like competitor to a ~Rs 13.6 Cr Bengaluru crane maker. It is audited here as the **gold-standard benchmark** for what a best-in-class crane website looks like. The value for SVMH is in the *patterns and structures* (worth copying at small scale) and the *over-engineering* (worth avoiding). Recommendations are calibrated to that reality throughout.

---

## 1. Executive Summary

Konecranes runs a large, enterprise-grade **Drupal 11** site organized around a clear two-way split: **Industrial Service & Equipment** vs **Port Solutions**. The site is content-rich (hundreds of "Discover" articles, customer stories, downloadable brochures), heavily internationalized (50+ country/language sites with correct hreflang), and structured for both lead generation (a single consultative quote form) and lifecycle service selling. Technical SEO hygiene is strong: clean canonicals, JSON-LD Organization/Breadcrumb/Product schema, descriptive titles/meta, one H1 per page, responsive `srcset` images.

The main weaknesses from a *conversion / usability* standpoint: a heavy homepage (~315 KB HTML, slow-ish TTFB ~1.6s), a generic global quote form that does not carry product context, video content gated behind cookie consent (nothing plays until "Targeting" cookies are accepted), and a product architecture so deep that a first-time buyer can get lost. The India site (`/en-in`) is a thin shell of the global site with little localized content.

**Confidence:** High for structure/SEO/content findings (directly observed in scraped HTML). Medium for performance (field CrUX data unavailable this session; lab timing measured directly). Low only where explicitly flagged.

---

## 2. Navigation & Information Architecture

| Element | Observation | Source | Confidence |
|---|---|---|---|
| Top-level split | Homepage forces one primary choice: **Industrial Service & Equipment** vs **Port Solutions** ("Choose the offering to explore"). Clean mental model for a broad portfolio. | https://www.konecranes.com (2026-07-05) | High |
| Industrial sub-nav | Industrial hub breaks into 4 pillars: **Service, Parts, Equipment, Agilon** (warehouse automation). | https://www.konecranes.com/industrial | High |
| Equipment taxonomy | Equipment → Overhead cranes → (Rope hoist / Chain hoist / Gantry / Portable / Wall-mounted / Open winch / Custom / RENTALL) → individual series (X-series, S-series, CXT, CXT NEO). 3–4 levels deep. | https://www.konecranes.com/equipment/overhead-cranes and /rope-hoist-cranes | High |
| Industry-led entry | Parallel navigation by **industry** (General Mfg, Paper & Forest, Automotive, WTE & Biomass, Metals, Nuclear, Petroleum & Gas, Power, Mining, Ports) — each industry page cross-links to relevant products + services. | https://www.konecranes.com/industrial | High |
| Breadcrumbs | Present and marked up as BreadcrumbList JSON-LD (Home › Equipment › Overhead cranes). | /tmp raw HTML of /equipment/overhead-cranes | High |
| Country selector | Prominent "Select your location" overlay grouping 50+ locales by region (Europe / Americas / MEA / Australia & Asia) + separate lift-trucks brand site. | Homepage scrape | High |

**Read:** Dual-axis navigation (by **product** AND by **industry**) is the standout IA pattern. A buyer who thinks "I run a foundry" and a buyer who thinks "I need a double-girder crane" both find a path. This is the single most copyable structural idea for SVMH.

---

## 3. Sitemap & Scale

| Element | Observation | Source | Confidence |
|---|---|---|---|
| XML sitemap | Drupal "Simple XML Sitemap" module; **sitemap index with 9 paginated sub-sitemaps** (`sitemap.xml?page=1..9`), `lastmod` timestamps present and fresh (2026-07-05). | https://www.konecranes.com/sitemap.xml | High |
| robots.txt | Standard Drupal robots.txt; explicitly Allows CSS/JS/images for crawlers, disallows admin/system paths. Well-formed. | https://www.konecranes.com/robots.txt | High |
| Content depth | Hundreds of `/discover/*` articles (thought leadership, customer stories, history, sustainability), multilingual variants, `/press-releases/*`, `/events/*`. | firecrawl_map (150 links returned, dominated by /discover) | High |

**Read:** Content marketing is industrial-scale. Freshness signals (lastmod) are honest and current. SVMH needs a sitemap (it likely has none or a poor one — to be confirmed in the SVMH audit), but does NOT need hundreds of articles; 10–20 focused pages beat 0.

---

## 4. Homepage Structure

Observed section order on the global homepage (2026-07-05):

1. **Rotating hero carousel** (3 slides): "Meet Hugo" (humanoid robot brand story), "RTG & RMG predictive services", "Q1 2026 interim report" — mixes brand, product, investor messaging.
2. **"Choose the offering to explore"** — the Industrial vs Port Solutions split (primary CTA block).
3. **Featured story cards** (AGM, digital twinning, KBK case study) — editorial.
4. **Brand / About / Careers** liftup blocks.
5. **Press releases** feed (latest 5, dated).
6. **Upcoming events** feed (trade shows with dates + venues).
7. **YouTube featured videos** carousel (15+ thumbnails) — *gated behind cookie consent*.
8. **Customer story** (WD Steelworks, S-series) with video link.
9. Footer + country selector + click-to-call phone list for ~55 countries.

| Signal | Value | Source | Confidence |
|---|---|---|---|
| HTML document weight (mobile UA) | ~314 KB homepage / ~310 KB overhead-cranes / ~250 KB en-in | curl `size_download`, 2026-07-05 | High |
| TTFB (homepage, mobile UA, single sample) | ~1.64 s (total 1.97 s) | curl `time_starttransfer`, 2026-07-05 | Medium (single sample) |
| TTFB (overhead-cranes) | ~0.69 s (total 0.93 s) | curl, 2026-07-05 | Medium |

**Read:** The homepage tries to serve buyers, investors, job-seekers and press simultaneously — classic large-corporate compromise. For SVMH the lesson is *selective copying*: keep the "choose your path" block and the customer-story/press elements; drop the investor/carousel bloat.

---

## 5. Product Pages

**Category page — Overhead cranes** (https://www.konecranes.com/equipment/overhead-cranes):
- H1 "Overhead cranes" + benefit-led intro paragraph.
- **Prominent brochure download CTA** ("Download the product range brochure" → `brochure_industrial_cranes_2026.pdf`) above the fold.
- Card grid of 8 crane types, each with image + name + one-line value prop + deep link.
- "Smart Features" software section, "Get connected" (TRUCONNECT) service cross-sell, and a **customer story with a downloadable reference PDF**.
- Product JSON-LD schema present (`@type: Product`, brand Konecranes).

**Sub-category — Rope hoist cranes** (/rope-hoist-cranes):
- Product range sub-cards (X-series, S-series, CXT, CXT NEO) with substantive descriptions and concrete specs (e.g., "up to 80 ton lifting capacity", "10,000 hoists sold around the world every year").
- **"Want to know more about the crane buying process?"** block → links to a dedicated **Crane Buyer's Guide** (/crane-buyers-guide) — strong mid-funnel content.
- "Learn more" editorial cards (articles + customer stories) at the bottom for internal linking.

| Signal | Value | Source | Confidence |
|---|---|---|---|
| Specs on product pages | Capacity figures, standards, sold-volume proof points present in body copy | /rope-hoist-cranes scrape | High |
| Downloadable brochures | Per-category PDF (`brochure_industrial_cranes_2026.pdf`), Smart Features brochure PDF, per-product reference-story PDFs | product scrapes | High |
| CTA pattern | "Download brochure" + "Watch video" + "Read the story" + deep links; NO price, NO "add to cart" (correct for capital equipment) | product scrapes | High |

**Read:** Product pages sell on **benefit + proof + downloadable detail**, not price. The brochure-download and buyer's-guide patterns are directly copyable and cheap to build.

---

## 6. Landing Pages & Campaign Tracking

- Hero CTAs carry full **UTM tracking** (e.g., predictive-services hero: `utm_source=Konecranes_COM&utm_medium=Organic&utm_campaign=BA_PS_BU_PSERS...&utm_content=Landing_Pages&utm_term=Hero_Banner...`). Indicates a mature campaign/attribution setup. **Source:** homepage links, 2026-07-05. **Confidence:** High.
- Dedicated conversion assets: **Crane Buyer's Guide**, **self-service product-advice tool** (`/konecranes-self-service-tools`), **Mavenoid-powered troubleshooter** chatbot embedded on product pages ("Powered by Mavenoid"). **Confidence:** High.

**Read:** Even organic links are tagged for analytics. SVMH should at minimum tag its RFQ/IndiaMART inbound so it knows what converts.

---

## 7. RFQ / Quote Flow

**Path:** Contact us → "What can we help you find?" → three routes: **Service contacts** (map), **Parts and manuals** (portal), **Product advice** (self-service tool). Below that, a single **"Contact us" quote form**.

Quote form fields observed (https://www.konecranes.com/contact-us, 2026-07-05):
- **"What product do you need a quote or more information on"** — dropdown with 12 options (Service for overhead cranes / Spare parts / Crane training / Chain hoists,jib,workstation / Overhead cranes – standard up to 80 tons / Overhead cranes – heavy/process / Hazardous environment / Port services / Container handling / Mobile harbor cranes / Heavy duty lift trucks / Agilon / Other).
- Briefly describe what you need (free text)
- First name, Last name, Company
- Region + Country (full ISO country dropdown)
- (implied consent/submit)

| Signal | Observation | Source | Confidence |
|---|---|---|---|
| Single global form | One consultative form segments by product type up front — routes lead to right business unit | contact-us scrape | High |
| No product-context carry-through | The quote form is generic; clicking "get a quote" is not obviously wired from each product page with the product pre-filled (product pages push brochure/guide, not an inline RFQ) | product + contact scrapes | Medium |
| Parts quoting | Separate authenticated **customer portal** (portal.konecranes.com) for parts/manuals/quotes | homepage + contact | High |

**Read:** Strength = qualification-by-dropdown so the lead reaches the right team. Weakness = friction; a buyer on the rope-hoist page has to leave, find Contact, and re-specify. **SVMH opportunity:** put a short "Request a quote" form (or WhatsApp CTA) *directly on every product page* with the product pre-selected — beat Konecranes on this exact point.

---

## 8. Contact Flow & Trust

| Element | Observation | Source | Confidence |
|---|---|---|---|
| Click-to-call | Country-by-country phone numbers (~55 countries) as `tel:` links, including India toll-free **1800-209-5333** | homepage scrape | High |
| Location finder | "Find a location near you" + contact map anchor | homepage / contact | High |
| Trust — scale claims | "A global leader in material handling solutions", "largest service network", "century of experience", "10,000 hoists sold... every year" | homepage / product pages | High |
| Trust — proof | Named customer stories (WD Steelworks, A. Reponen, LTC Group, Cummins Germany), downloadable reference PDFs, press releases with real order wins (YILPORT 53 RTGs, Södra forklifts) | homepage / product scrapes | High |
| Trust — certifications | ISO 27001 cybersecurity cert referenced in Discover content; investor/AGM transparency | firecrawl_map /discover | Medium |
| Corporate identity | JSON-LD Organization schema: legalName "Konecranes Plc", foundingDate 1994, areaServed World | raw HTML JSON-LD | High |

**Read:** Trust is built through **named customers + real order news + scale numbers**, not badges alone. SVMH should lead with client logos (automotive/steel/foundry names), project photos, ISO 9001, and specific tonnage/reference projects.

---

## 9. Images, Video & Downloads

| Asset type | Observation | Source | Confidence |
|---|---|---|---|
| Images | Responsive: **144 `srcset` occurrences** and multiple Drupal image styles (banner_md, 5_7_small/large, height_200) per page — proper art direction across breakpoints | raw HTML /equipment/overhead-cranes | High |
| Lazy loading | Partial: only **6 of 28 `<img>`** carry `loading="lazy"` on the overhead-cranes page — hero/above-fold correctly eager, but many below-fold images not lazy-loaded | raw HTML | High |
| Alt text | Descriptive alt attributes present ("Konecranes chain hoist crane", "Overhead crane hooks", etc.) | scrapes | High |
| Video | Heavy YouTube use (product films, "how it's made", customer stories) BUT **all videos gated: "Video cannot be shown. You must accept cookies in the 'Targeting' category"** — zero video plays without consent | homepage + industrial scrapes | High |
| Downloads | Rich PDF library: product-range brochure, Smart Features brochure, per-product reference stories, buyer's guide | product scrapes | High |

**Read:** Image handling is exemplary (srcset/art direction) and cheap-ish to emulate with modern CMS/Next.js. Video-behind-consent is a GDPR-driven UX cost that hurts engagement — SVMH (India, less GDPR-bound) can embed lightweight video/hosted MP4 that plays immediately and win on this.

---

## 10. CTAs & Forms Summary

- **Primary CTAs:** "Select" (offering split), "Explore", "Download the brochure", "Watch the video", "Read the story", "Check out the guide", "Contact us".
- **Tone:** consultative, benefit-led ("Know before it breaks. Plan before it fails."), never pushy/price-led — appropriate for long B2B capital sales cycles.
- **Forms:** one main lead form (segmented), one authenticated parts portal, self-service advisor tool, embedded troubleshooter chatbot.

**Read:** Multiple low-commitment CTAs (download, watch, read) feed a single high-commitment CTA (quote). Good funnel design. SVMH should offer at least one downloadable (product PDF/brochure) as a soft conversion.

---

## 11. SEO Structure

| Signal | Observation | Source | Confidence |
|---|---|---|---|
| Titles | Descriptive, templated: "Overhead cranes \| Konecranes", "Industrial Service & Equipment \| Konecranes" | metadata | High |
| Meta descriptions | Present, unique, benefit-rich (150–300 chars) | metadata | High |
| H1 | Exactly **one H1 per page** matching topic | raw HTML grep (count = 1) | High |
| Canonicals | Self-referencing canonical on each page | raw HTML | High |
| hreflang | **36 hreflang tags** on the overhead-cranes page (all locale variants + x-default) — correct international SEO | raw HTML grep | High |
| Structured data | **3 JSON-LD blocks**: Organization, BreadcrumbList, Product — clean schema.org | raw HTML | High |
| CMS | Drupal 11 (Generator meta) | metadata | High |
| ⚠ robots meta anomaly | Some pages emit BOTH `index, follow` AND `noindex` in the robots meta array; homepage + en-in show `robots: noindex`. Likely a Drupal metatag misconfiguration/duplication — a genuine technical SEO risk worth flagging. | metadata across homepage, en-in, overhead-cranes | Medium |

**Read:** Technical SEO is otherwise textbook. The `noindex`/duplicate-robots quirk is the one concrete SEO defect observed — evidence that even leaders ship metatag bugs. SVMH should get titles/meta/H1/canonical/schema right from day one; it is low-cost and Konecranes proves the template.

---

## 12. Internal Linking

- Dense, contextual internal linking: industry pages → products + services; product pages → sub-products, Smart Features, TRUCONNECT service, buyer's guide, and 3–4 related "Discover" articles/customer stories per page.
- Breadcrumbs reinforce hierarchy and are schema-marked.
- **Source:** all product/industrial scrapes, 2026-07-05. **Confidence:** High.

**Read:** Every page is a hub that funnels toward either a product or a conversion asset. Strong for SEO link equity and for keeping buyers moving. Copyable at small scale.

---

## 13. Page Speed Signals

| Metric | Value | Source | Confidence |
|---|---|---|---|
| Homepage HTML size | ~314 KB (uncompressed document, mobile UA) | curl, 2026-07-05 | High |
| Homepage TTFB | ~1.64 s (single sample, mobile UA) | curl, 2026-07-05 | Medium |
| Product page TTFB | ~0.69 s (overhead-cranes) | curl, 2026-07-05 | Medium |
| Image optimization | Strong srcset/responsive; partial lazy-load (6/28 imgs) | raw HTML | High |
| Field Core Web Vitals (CrUX) | **Not available this session** — Google PageSpeed Insights API returned HTTP 429 (daily quota exceeded). Cannot report LCP/CLS/INP field data. | PSI API, 2026-07-05 | Low (unverified) |

**Read:** The homepage is heavy and TTFB is mediocre (~1.6s) — typical of a media-rich Drupal enterprise site. This is an area a lean, modern SVMH site (static/Next.js, optimized images, CDN) can objectively *beat*. Do not treat Konecranes' speed as the bar to match; treat it as the bar to exceed.

---

## 14. Mobile Experience

- Responsive viewport meta (`width=device-width, initial-scale=1.0`), `MobileOptimized` + `HandheldFriendly` flags, responsive srcset images, `tel:` click-to-call throughout.
- Overlay-style country selector and collapsible mega-menu adapt to mobile.
- Mobile HTML still ~250–315 KB before assets — heavy on 3G/4G typical of Indian field conditions.
- **Source:** metadata + scrapes, 2026-07-05. **Confidence:** High (responsive design); Medium (real-device performance not lab-tested).

**Read:** Mobile is technically responsive but not lightweight. Given SVMH's buyers often browse on mobile in Indian network conditions, a fast mobile-first build is a real competitive wedge.

---

## 15. Strengths & Weaknesses

| # | STRENGTHS | Evidence | Confidence |
|---|---|---|---|
| S1 | **Dual-axis IA** — navigate by product AND by industry; both buyer mindsets served | /industrial cross-links products+services per industry | High |
| S2 | **Clear top-level choice** — "Industrial vs Ports" removes overwhelm for a huge catalog | Homepage offering split | High |
| S3 | **Proof-driven trust** — named customer stories, real order press releases, scale numbers, reference PDFs | Homepage + product scrapes | High |
| S4 | **Textbook technical SEO** — unique titles/meta, single H1, canonicals, 36 hreflang, Org+Breadcrumb+Product JSON-LD | Raw HTML | High |
| S5 | **Excellent responsive imagery** — 144 srcset, art-directed image styles, descriptive alt text | Raw HTML | High |
| S6 | **Mid-funnel content** — Crane Buyer's Guide, self-service advisor, downloadable brochures per product | Product scrapes | High |
| S7 | **Segmented lead qualification** — quote form routes by 12 product categories to the right team | Contact-us scrape | High |
| S8 | **Fresh, honest sitemap** — 9-page sitemap index with current lastmod; content updated 2026 | sitemap.xml | High |
| S9 | **Campaign maturity** — UTM tagging even on organic links; analytics-ready | Homepage links | High |

| # | WEAKNESSES | Evidence | Confidence |
|---|---|---|---|
| W1 | **Heavy pages / mediocre TTFB** — ~315 KB homepage, ~1.6s TTFB; media-heavy Drupal | curl timing | Medium |
| W2 | **Video gated behind cookie consent** — nothing plays until "Targeting" cookies accepted; kills engagement | Homepage/industrial scrapes | High |
| W3 | **RFQ friction** — generic global form; product context not carried from product page into quote | Product + contact scrapes | Medium |
| W4 | **Deep architecture** — 3–4 click levels to a specific crane series; first-timers can get lost | Equipment→OC→rope-hoist→series | High |
| W5 | **Thin localization** — /en-in is a shell of the global site; little India-specific content, pricing, or local proof | en-in scrape | High |
| W6 | **robots meta anomaly** — duplicate/`noindex` robots tags on some pages; SEO risk | metadata | Medium |
| W7 | **Homepage tries to serve everyone** — buyers, investors, press, careers compete for attention above the fold | Homepage structure | High |
| W8 | **Partial lazy-loading** — only 6/28 images lazy on a key product page; wasted bytes below fold | Raw HTML | High |

---

## 16. What SVMH Should COPY

1. **Dual-axis navigation (by product + by industry).** SVMH already serves automotive, steel, power, foundry, cement, construction — build an "Industries" menu that mirrors "Products (EOT/Gantry/Jib/Monorail/Hot-metal)." This is the single highest-value copy. *(from S1)*
2. **"Choose your path" homepage block.** A clean 2–4 tile chooser (e.g., New Cranes / Spares & Components / AMC Service) beats a wall of links. *(S2)*
3. **Proof-driven trust section.** Client logos (real automotive/steel names), tonnage/reference projects with photos, ISO 9001 badge, years-in-business (since 2006). Konecranes proves buyers convert on proof, not adjectives. *(S3)*
4. **Get technical SEO right from day one** — one H1/page, unique title+meta, self canonical, and **Organization + Product + BreadcrumbList JSON-LD**. Cheap, and Konecranes gives you the exact template. *(S4)*
5. **Product pages = benefit + specs + downloadable brochure.** Add a per-product PDF datasheet (capacity, span, IS 807/IS 3177/FEM class, duty). The brochure-download is a proven soft conversion. *(S6)*
6. **A simple "Crane Buyer's Guide" / selection helper.** Even a one-page guide ("how to spec an EOT crane: capacity, span, duty class, HOL") captures mid-funnel search traffic competitors ignore. *(S6)*
7. **Segment the enquiry form** by product/service so leads self-qualify (New crane / Spares / AMC / Modernization). *(S7)*
8. **Responsive images with srcset + descriptive alt + real project photos.** *(S5)*
9. **A real XML sitemap + robots.txt with fresh lastmod.** *(S8)*
10. **UTM-tag inbound links** (including IndiaMART/ExportersIndia and email signatures) to learn what actually converts. *(S9)*

## 17. What SVMH Should AVOID

1. **Don't bloat the homepage.** Skip investor feeds, careers carousels, and 3-slide hero mixes. One clear value prop + path chooser + proof + contact. *(W1, W7)*
2. **Don't gate video behind cookie walls.** Host lightweight MP4/YouTube that plays on click immediately — turn Konecranes' W2 into your win. *(W2)*
3. **Don't make buyers hunt for the quote.** Put a short **"Request a Quote" form + WhatsApp/phone CTA on every product page**, product pre-filled. Directly beat Konecranes' RFQ friction. *(W3)*
4. **Don't build 3–4 level deep taxonomy.** With SVMH's smaller catalog, keep products max 2 clicks from home. *(W4)*
5. **Don't ship a "shell" region site.** Since SVMH IS India-first, lead with India proof, local standards (IS codes), local phone/WhatsApp, and Bengaluru/Karnataka service coverage — the localization Konecranes' /en-in lacks. *(W5)*
6. **Don't skip lazy-loading / performance basics.** Lazy-load below-fold images, compress, use a CDN. A lean site loading fast on Indian mobile networks is a concrete edge over the heavy incumbent. *(W1, W8)*
7. **Don't over-rely on adjectives without proof.** "Leading manufacturer" means nothing without a client list and project photos. *(W7)*

---

## 18. Sources (accessed 2026-07-05)

- Homepage: https://www.konecranes.com
- Industrial hub: https://www.konecranes.com/industrial
- Overhead cranes (category): https://www.konecranes.com/equipment/overhead-cranes
- Rope hoist cranes (sub-category): https://www.konecranes.com/equipment/overhead-cranes/rope-hoist-cranes
- Contact / RFQ: https://www.konecranes.com/contact-us
- India site: https://www.konecranes.com/en-in
- Sitemap index: https://www.konecranes.com/sitemap.xml (9 paginated sitemaps)
- robots.txt: https://www.konecranes.com/robots.txt
- Raw HTML inspection (schema, hreflang, canonical, img/srcset/lazy counts, titles/meta): curl of /equipment/overhead-cranes
- Network timing (TTFB, HTML size): curl, mobile UA, single-sample
- Crane Buyer's Guide referenced: https://www.konecranes.com/crane-buyers-guide
- Self-service tools referenced: https://www.konecranes.com/konecranes-self-service-tools

**Data gaps / low-confidence items:**
- Field Core Web Vitals (CrUX LCP/CLS/INP): **unavailable** — PageSpeed Insights API HTTP 429 (quota) on 2026-07-05. Lab TTFB/size measured directly instead.
- TTFB figures are single-sample; treat as directional, not benchmarked averages.
- robots `noindex` anomaly: observed in scraper metadata; recommend confirming in a live browser view of page source before citing externally.
