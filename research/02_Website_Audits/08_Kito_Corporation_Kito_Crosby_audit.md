# Website Audit — Kito Corporation / Kito Crosby (kito.com → kitocrosby.com)

**Prepared for:** S.V. Material Handling System Pvt Ltd (SVMH) competitive-landscape research
**Auditor:** Research pass, live crawl
**Date accessed:** 2026-07-05
**Primary domain audited:** `https://kito.com` (301-redirects to `https://kitocrosby.com/`)
**Platform detected:** WordPress + Elementor 4.1.4 page builder + Slider Revolution 6.7.58 + WooCommerce (catalog/shop), fronted by Cloudflare CDN, hosted on WP Engine (`kitocrosbyprd.wpenginepowered.com`). SEO handled by Yoast-style output + Google Site Kit 1.182.0. (Source: home HTML `generator` meta + asset hostnames, accessed 2026-07-05, Confidence: High)

---

## 0. Context & scope note

`kito.com` is not an independent standalone site — it redirects to **kitocrosby.com**, the consolidated corporate site for Kito Crosby, which is itself **now part of Columbus McKinnon** (acquisition completed, announced on-site banner). Kito Corporation is presented as one **product brand** among several (Kito, Crosby, Harrington, Gunnebo Industries, Peerless, eepos). The Kito-specific hoist catalog largely lives on regional sites (`kito.co.jp`, `kito.co.in`, `kito.net`, etc.); kitocrosby.com hosts the Crosby/Gunnebo rigging-hardware e-commerce catalog directly.

This matters for SVMH: Kito/Kito Crosby is a **global rigging-hardware and hoist giant** (~4,000 employees, 50+ factories, 3,500+ distributors — see Trust section), not a direct like-for-like EOT-crane fabricator. The relevant lessons are about **catalog depth, technical-document delivery, trust architecture, and multi-brand IA**, not about small-shop crane fabrication.

- Source: `https://kito.com` redirect + home banner "Kito Crosby is now part of Columbus McKinnon", accessed 2026-07-05, Confidence: High. Supporting: `og:url` resolves to `https://kitocrosby.com/`.

---

## 1. Navigation

**Structure:** Multi-brand top navigation organized by **product brand** (Kito / Crosby / Harrington / Gunnebo / Peerless / eepos) plus function-based sections (Industries, Resources, Training, Catalogs, Careers, About, Contact/Locator). Home HTML shows **106 `menu-item` classes**, indicating a large multi-level mega-menu. (Source: home HTML class count, accessed 2026-07-05, Confidence: High)

- **Brand-led IA:** Each brand has its own landing hub (`/kito/`, `/crosby/`, `/harrington/`, `/gunnebo/`, `/peerless/`, `/eepos/`) that then fans out to regional sites or product categories.
- **Function-led secondary nav:** Industries, Resources & Tools, Training, Catalogs, Locator (contact), Careers.
- **Utility nav:** Product search bar (part-number / product-ID search), language selector (12 languages via hreflang), cart/account (WooCommerce).

**Strength:** Clear dual-axis navigation (by brand AND by industry AND by product category) lets buyers arrive from any mental model. **Weakness:** With 6 brands + 30 industries + 17 product categories + training + resources, the mega-menu is heavy; first-time visitors may face choice overload. Redirect chain (kito.com → kitocrosby.com) also dilutes the "Kito" identity.

---

## 2. Sitemap

**XML sitemap index present and well-segmented** at `/sitemap_index.xml`, split into typed sub-sitemaps: `page-sitemap.xml`, `product-sitemap.xml`, `category-sitemap.xml`, `product-category` (via category), `resource-sitemap.xml`, `resource-page-sitemap.xml`, `resource-type-sitemap.xml`, `leadership-sitemap.xml`, `event-location-sitemap.xml`. (Source: firecrawl_map of kitocrosby.com, accessed 2026-07-05, Confidence: High)

**Scale (from live map — 916 URLs discovered):**

| Segment | Count | Notes |
|---|---|---|
| `/product/*` | 636 | Individual product detail pages (Crosby/Gunnebo hardware) |
| `/news/*` | 41 | Press/news articles |
| `/resource/*` | 19 | Educational "101" guides, insight articles |
| `/training*` | 17 | Training program pages (in-person, online, regional) |
| `/product-category/*` | 17 | Category listing pages |
| `/leadership/*` | 12 | Executive bios |
| Language variants | ~50 | de/fr/ja/es/zh/sv/ko/it/th/pt-br/id subtrees |
| `/industries*` | 2 hubs + ~30 industry entries | |

- Source: `firecrawl_map` (saved result, 916 URLs), accessed 2026-07-05, Confidence: High. Supporting: top-level segment counts — `636 product`, `41 news`, `19 resource`, `17 training`, `17 product-category`, `12 leadership`.

**Strength:** Deep, typed, machine-readable sitemap architecture — 636 indexable product pages is a massive SEO surface. **Weakness:** Sheer size + WooCommerce filter URLs risk crawl-budget dilution / thin-content pages if not carefully canonicalized.

---

## 3. Homepage structure

Slider Revolution hero carousel with rotating announcement slides (Columbus McKinnon acquisition, Gunnebo hooks "How it's made", Raise Your World podcast, RNER2 hazardous-location hoists, G-2160 shackle launch, eepos acquisition). Below the hero:

1. **Brand-tagline block** — "Together we lift and secure the world today, for a safer, stronger and more productive tomorrow."
2. **6 product-brand cards** (Kito, Crosby, Harrington, Gunnebo, Peerless, eepos) each with logo, one-line value prop, "More" CTA.
3. **Industries block** — "Safe & innovative solutions… broadest portfolio."
4. **Careers** + **Vertical-integration white-paper download** CTAs.

- Source: `firecrawl_scrape` home markdown, accessed 2026-07-05, Confidence: High. Supporting quote: *"With the broadest portfolio of lifting and securement hoists, hardware, and technologies, Kito Crosby meets the specific demands of a wide range of global industries."*

**Homepage heading structure (SEO):** H1 × 2, H2 × 1, H3 × 2, H4 × 7. Two H1s is a minor SEO anti-pattern (one of them is a slider artifact "Raise your world"). (Source: raw HTML heading count, accessed 2026-07-05, Confidence: High)

**Strength:** Communicates scale, brand portfolio, and safety positioning immediately; strong emotional/brand storytelling ("Raise your world"). **Weakness:** Carousel-heavy hero (Slider Revolution) is a known LCP/performance drag and reduces message clarity; no single clear primary CTA for a buyer who wants to "find a product" or "get a quote" above the fold.

---

## 4. Product pages

Product detail pages (e.g., `/product/crosby-g-2130-s-2130-bolt-type-anchor-shackles/`) are **exceptionally rich technical pages**:

- Multiple product photos + identification diagrams + symbol/warning imagery + dimensional line drawings (image gallery with thumbnails).
- SKU + category breadcrumb.
- Detailed bulleted **product specifications** (grade, forging/heat-treat, galvanizing, fatigue rating "20,000 cycles at 1-1/2× WLL", temperature range −40°F to 400°F, standards compliance: ASME B30.26, ABS, DNV 2.7-1, EN13889, ISO 2415, Federal Spec RR-C-271).
- **Full dimensional data tables** in BOTH Imperial and Metric (WLL, stock numbers, weights, all dimensions A–P per size).
- **Videos** section.
- **Downloads** block: Catalog Page (Imperial), Catalog Page (Metric), Applications & Warnings PDF, product Guide PDF, Application Matrix PDF, **User Manual PDF** — all directly downloadable.
- **Gated CAD/PDF download form** ("Download CAD & PDF Files" — First/Last name, Company, Email, Phone, Job Title, Postal Code, CAPTCHA) → lead capture.

- Source: `firecrawl_scrape` of G-2130 product page, accessed 2026-07-05, Confidence: High. Supporting quote: *"Fatigue rated to 20,000 cycles at 1-1/2 times the Working Load Limit… Meets or exceeds all requirements of ASME B30.26."*

**Strength:** Best-in-class technical depth — dual-unit spec tables, standards citations, downloadable CAD + manuals + warnings. This is the gold standard for a rigging/lifting product page. **Weakness:** CAD/full-spec downloads are **gated behind a 7-field form + CAPTCHA**, adding friction. Also: **no Product/Offer/AggregateRating schema** detected in JSON-LD despite being on WooCommerce (only Brand/Organization/WebSite/Breadcrumb schema present) — a missed rich-result opportunity for 636 product pages. (Source: product page HTML schema grep — no `"Product"` type found, accessed 2026-07-05, Confidence: High)

---

## 5. Landing / category pages

- `/product-categories/` — visual grid of 18 categories (Shackles, Load Monitoring, Camera Systems, Hooks & Swivels, Master Links, Chain & Accessories, Clips & Wire Rope Fittings, Subsea & ROV, Synthetic Sling Fittings, Turnbuckles, Lifting Points, Lifting Clamps & Magnets, Load Securement, Sheaves, Blocks, Round Slings, Wire Ropes, Aquaculture) each with icon + "See Products" CTA. Unified Crosby + Gunnebo catalog with a part-number search bar.
- `/product-category/shackles/` — WooCommerce archive: filterable (Brand facets), sortable (popularity/rating/latest/price), paginated ("Showing 1–16 of 40 results"), each item links to spec page ("View Specification").
- **Industry landing pages** — 30 industries listed; ~8 have dedicated deep pages (Construction, Aquaculture, Entertainment, Fishing, Mining, Oil & Gas, Power Sector, Wind Power) with "Learn More"; the rest are icon-only (no link yet).

- Source: `firecrawl_scrape` of `/product-categories/` and `/product-category/shackles/`, accessed 2026-07-05, Confidence: High. Supporting: shackles archive shows *"Showing 1–16 of 40 results"* with sort dropdown.

**Strength:** Strong visual category merchandising + faceted filtering + part-number search. **Weakness:** Many industry pages are dead-end icons (no dedicated content), and the shackles archive markdown leaked raw Salsify image URLs + unlabeled brand facets ("1019533", "G2", "G3") — a data-hygiene/filter-labeling issue.

---

## 6. RFQ / quote flow

**No traditional "Request a Quote" (RFQ) form as the primary path.** Kito Crosby is a **distributor-model** business — the conversion path is:

- **"Locate a local sales manager"** (geolocation-based `/locator/`) — user types an address → returns nearest rep name/email/phone.
- **WooCommerce cart/checkout** exists (`/cart`, `/checkout`, `/my-account`, `/shop`) but the catalog pages emphasize "View Specification" over "Add to Cart" — pricing/purchase is largely channel-mediated.
- **Gated CAD/spec download form** doubles as a lead-gen mechanism.

- Source: `firecrawl_scrape` of `/contact` (redirects to `/locator/`) + product-category footer links, accessed 2026-07-05, Confidence: High. Supporting quote (locator page): *"Find your local sales and customer service contacts… Start typing your address."*

**Strength:** Geolocation rep-locator is smart for a global distributor network (routes leads to the right regional contact). **Weakness:** For a buyer who just wants a fast quote on a specific SKU, there is no one-click "Request Quote on this product" button on product pages — friction vs. a simple RFQ form. SVMH (single-location, direct-sales) should NOT copy the distributor-locator model; a direct RFQ form is more appropriate.

---

## 7. Contact flow

`/contact` **redirects to `/locator/`** — a map/address-search rep finder rather than a classic contact form. There is also brand-specific customer-service routing (e.g., Kito brand page links to `kito.co.jp/en/contact_region/`). No single prominent "phone + email + address + contact form" block in the classic SMB sense.

- Source: `firecrawl_scrape` — `/contact` `sourceURL` resolved to `url: https://kitocrosby.com/locator/`, accessed 2026-07-05, Confidence: High.

**Strength:** Sophisticated global contact routing. **Weakness:** Impersonal for direct buyers; the locator returned "No contacts found" on a blank query (requires exact address input) — a potential dead-end UX. For SVMH, a direct, visible phone/email/WhatsApp + short contact form beats this.

---

## 8. Trust elements

Strong, layered trust architecture:

- **Corporate scale stats (About page):** "**4000+ employees worldwide**", "**50+ factories, offices, & distribution sites**", "**3500+ authorized local distributors**". (Source: `/about` HTML, accessed 2026-07-05, Confidence: High)
- **Heritage/legacy:** brand founding dates baked into schema and copy — Gunnebo "since 1764", Kito "since 1932", Harrington "since 1867". "Set the standard… for centuries."
- **Standards & certifications** cited per product (ASME, ABS, DNV, EN, ISO, Federal Spec).
- **Product authentication tools:** "Authenticate your product" + "Verify authenticity of a certificate" (certpro.thecrosbygroup.com) — anti-counterfeit trust layer. "Look for the Red Pin® — the mark of genuine Crosby quality."
- **Leadership page** (12 executive bios), **Quality page**, **Certified Repair Centers**, **Channel Partners**, **Careers**, **News** (41 articles), **Accessibility Statement** + UserWay accessibility widget.
- **Podcast** ("Raise Your World") + **"How it's made"** video series = brand-authority content.

- Source: `/about`, `/kito/`, product page footer, home HTML, accessed 2026-07-05, Confidence: High. Supporting quote: *"Our products and people have set the standard in the lifting and securement industry for centuries."*

**Strength:** Multi-dimensional trust — scale numbers, heritage dates, third-party standards, product-authentication portal, leadership transparency, accessibility compliance. This is a masterclass. **Weakness:** ISO cert of the corporation itself was not surfaced on `/about` (product-level standards are cited, but a visible corporate ISO 9001 badge was "NOT FOUND" on the about page in this pass — Confidence: Medium, may live on `/quality`).

---

## 9. Images

- Homepage carries **83 `<img>` tags**; product/category pages use high-res product photography served from **Salsify DAM** (`images.salsify.com`, 1000×1000 mfit) and WP media library with responsive `-300x300`/`-253x300` variants. WebP used for some banners (`usa-banner@2x.webp`).
- **Accessibility gap:** **67 of 83 homepage images lack `alt` text** (many are decorative SVG overlays/logos, but the ratio is high). (Source: raw HTML alt-attribute grep, accessed 2026-07-05, Confidence: High)

**Strength:** Professional, consistent product photography via a proper DAM (Salsify); responsive image variants; identification diagrams + dimensional line-art add technical credibility. **Weakness:** High proportion of missing `alt` attributes on the homepage undercuts the site's own accessibility positioning; some decorative images could be CSS backgrounds instead.

---

## 10. Videos

- **"How it's made" video series** (Gunnebo hooks, Crosby shackles, McKissick blocks) — dedicated pages.
- Product pages embed a **Videos** section (YouTube). The shackles category alone references **100+ YouTube video URLs** (product demos, how-tos) pulled into filter data.
- **Podcast** ("Raise Your World" on Spotify) linked from hero.

- Source: `firecrawl_scrape` shackles category (100+ youtu.be/youtube links) + product page Videos section + home hero, accessed 2026-07-05, Confidence: High.

**Strength:** Rich video library (manufacturing transparency, product demos, safety) — excellent for engagement, SEO, and trust. Video + podcast = a genuine content-marketing engine. **Weakness:** Video embeds (YouTube iframes) + Slider Revolution add to page weight.

---

## 11. Downloads / technical documents

Outstanding document delivery:

- Per-product: Catalog Page (Imperial + Metric PDFs), Applications & Warnings, product Guide, Application Matrix, User Manual — all as downloadable PDFs.
- **Full print catalog** (PDF) via `info.kitocrosby.com/catalog`.
- **`/catalogs`**, **`/user-manuals`**, **`/resources`** hubs.
- **CAD files** downloadable from product pages (gated form).
- **White papers** ("Importance of Vertical Integration", "Rigging Industry Insight Series", "Selecting the Right Rigging Hardware Provider").

- Source: G-2130 product page Downloads block + `/product-categories/` catalog CTA, accessed 2026-07-05, Confidence: High. Supporting: 6 distinct PDF download links on a single shackle page.

**Strength:** Best-in-class — dual-unit catalog pages, user manuals, warnings, CAD, application matrices per SKU. This is exactly what specifying engineers need. **Weakness:** CAD/some downloads gated behind lead form + CAPTCHA (friction, and a barrier for quick engineering evaluation).

---

## 12. CTAs

Consistent, varied CTAs: "More", "Learn More", "See Products", "View Specification", "Read More", "Watch Now", "Listen Now", "Download print version of the catalog (PDF)", "Locate a local sales manager", "Authenticate your product". Every product page footer repeats the 4-CTA trust/action block (catalog download, locate sales manager, authenticate product, verify certificate).

- Source: home + product-category + product pages, accessed 2026-07-05, Confidence: High.

**Strength:** CTAs are contextual and repeated at logical decision points; the persistent footer action block is smart. **Weakness:** CTA language is soft ("More"/"Learn More") rather than conversion-driving ("Get a Quote"/"Talk to an Engineer"); no urgent commercial CTA above the fold.

---

## 13. Forms

- **Gated CAD/PDF download form** (First Name, Last Name, Company, Email, Phone, Job Title, Postal Code, all required + reCAPTCHA) — lead capture on product pages.
- **Locator search** (address input).
- **Newsletter/notifications** ("Notifications" element site-wide).
- WooCommerce checkout/account forms.

- Source: G-2130 product page form fields, accessed 2026-07-05, Confidence: High.

**Strength:** Proper lead-gen with CAPTCHA anti-spam and job-title/company qualification fields. **Weakness:** 7 required fields is heavy; likely depresses download conversion. No lightweight "email me this spec" option.

---

## 14. SEO structure (title / meta / H1 / schema)

- **Titles:** Clean, brand-suffixed (`Product Categories`, `Shackles Archives - Kito Crosby`, `Kito | A Kito Crosby Product Brand`, `About Kito Crosby`). Home title is just `Kito Crosby` (could be richer). (Source: page metadata, accessed 2026-07-05, Confidence: High)
- **Meta descriptions:** Present and descriptive on every page audited (e.g., home: *"The world's leading manufacturer of safe lifting and securement solutions…"*).
- **Open Graph / Twitter cards:** Fully populated (og:title/description/image/type, twitter:card=summary_large_image) on all pages.
- **Canonicals:** Present (`<link rel="canonical">`).
- **Robots:** `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1`.
- **hreflang:** 12 languages (en, de, es, fr, id, it, ja, ko, pt-br, sv, th, zh) — proper international SEO.
- **Schema/JSON-LD:** Organization, WebSite (with SearchAction/sitelinks search box), 5× Brand entities, BreadcrumbList, ImageObject, WebPage. **Missing:** Product schema on product pages (no Product/Offer/AggregateRating) despite WooCommerce.
- **Headings:** Home has 2× H1 (one is a slider artifact) — minor issue.

- Source: raw HTML + firecrawl metadata across home, product, category, about pages, accessed 2026-07-05, Confidence: High.

**Strength:** Enterprise-grade international SEO — hreflang across 12 locales, rich OG/Twitter, sitelinks search-box schema, typed sitemaps, per-page meta descriptions. **Weakness:** (1) No Product schema = leaving rich-result eligibility on the table for 636 product pages; (2) duplicate H1 on home; (3) generic home title.

---

## 15. Internal linking

- Strong hub-and-spoke: brand hubs → categories → 636 product pages → related downloads; industries hub → industry pages; resources hub → 19 "101"/insight guides.
- Breadcrumb schema present (Home → Shackles → product).
- Persistent footer cross-links (catalog, locator, authenticate, verify) on every product page.
- Cross-links out to regional brand sites (kito.co.jp, kito.co.in, harringtonhoists.com, etc.).

- Source: product page breadcrumb + footer, sitemap structure, accessed 2026-07-05, Confidence: High.

**Strength:** Deep, logical internal linking with breadcrumbs and contextual cross-links; educational "101" resource pages link to relevant product categories (topic-cluster SEO). **Weakness:** Heavy outbound linking to separate regional domains fragments authority; some industry pages don't link anywhere (dead icons).

---

## 16. Page speed signals

- **TTFB ~1.23s, full HTML download ~1.75s** for the homepage (196 KB HTML) over a single curl. (Source: curl timing, accessed 2026-07-05, Confidence: Medium — single-sample, server-side only, not full Core Web Vitals.)
- **Gzip compression enabled**; served via **Cloudflare** CDN.
- **Cache-control: private, no-store, no-cache, must-revalidate** on the HTML doc — aggressive no-cache on the base document (dynamic WP page).
- **88 `<script>` tags** on the homepage + Slider Revolution + Elementor + multiple tracking/marketing scripts + UserWay widget = heavy JS payload. (Source: raw HTML script count, accessed 2026-07-05, Confidence: High)

**Strength:** Cloudflare CDN + gzip + WP Engine hosting + WebP for some assets. **Weakness:** ~1.2s TTFB is mediocre; 88 scripts + Slider Revolution carousel + 83 images strongly suggest a **poor LCP/heavy main-thread** profile on the homepage. This is a classic WordPress-Elementor performance tax. (Full CWV validation would require Lighthouse/field data — not run in this pass; Confidence: Medium on the performance conclusion.)

---

## 17. Mobile experience

- Correct responsive viewport meta (`width=device-width, initial-scale=1`) on all pages.
- Elementor "additional_custom_breakpoints" enabled + responsive image variants + `font_display:swap`.
- UserWay accessibility widget for mobile a11y.

- Source: page metadata + generator string, accessed 2026-07-05, Confidence: High (responsive intent); Confidence: Low on actual mobile rendering (not device-tested in this pass).

**Strength:** Built responsive-first with custom breakpoints and font-display swap. **Weakness:** The same script/carousel weight that hurts desktop speed hits mobile harder; large dimensional spec tables (Imperial + Metric, ~16 columns) are hard to render on small screens — likely horizontal-scroll pain.

---

## 18. UX patterns (notable)

- Part-number / product-ID **search bar** on catalog pages (engineer-friendly).
- **Faceted filter + sort** on category archives.
- **Dual-unit toggle** (Imperial/Metric) on spec tables.
- **Geolocation rep locator** as contact model.
- **Product authentication + certificate verification** portal (anti-counterfeit).
- **Content engine:** podcast, "How it's made" videos, "101" educational guides, white papers.
- **12-language** international switching.

---

## Strengths / Weaknesses summary table

| # | Area | Strength | Weakness |
|---|---|---|---|
| 1 | Navigation | Dual-axis (brand + industry + category) mega-menu; part-number search | 106-item menu = overload; kito.com→kitocrosby.com redirect dilutes "Kito" |
| 2 | Sitemap | Typed XML sitemap index; 916 URLs, 636 products | Crawl-budget risk; WooCommerce filter-URL bloat |
| 3 | Homepage | Strong brand/scale storytelling; 6-brand portfolio cards | Carousel-heavy hero (LCP drag); no single primary buyer CTA; 2× H1 |
| 4 | Product pages | Dual-unit spec tables, standards citations, CAD + manuals + warnings PDFs | CAD gated behind 7-field form+CAPTCHA; **no Product schema** |
| 5 | Category/landing | Visual grids, faceted filter, sort, part-number search | Many industry pages are dead-end icons; leaked Salsify URLs / unlabeled facets |
| 6 | RFQ flow | Geo rep-locator routes to right distributor | No one-click "Quote this SKU"; friction for direct buyers |
| 7 | Contact | Sophisticated global contact routing | /contact→/locator only; impersonal; blank search = "No contacts found" |
| 8 | Trust | 4000+ employees, 50+ sites, 3500+ distributors; heritage since 1764/1867/1932; standards; product-auth portal; leadership bios; a11y statement | Corporate ISO badge not surfaced on /about (Confidence: Medium) |
| 9 | Images | Salsify DAM, responsive variants, WebP, identification diagrams | 67/83 homepage images missing alt text |
| 10 | Videos | "How it's made" series, 100+ product videos, podcast | Adds page weight |
| 11 | Downloads | Dual-unit catalog pages, user manuals, warnings, CAD, matrices per SKU | Gating friction on CAD |
| 12 | CTAs | Contextual, repeated; persistent footer action block | Soft language ("More"); no urgent commercial CTA |
| 13 | Forms | CAPTCHA + qualification fields (company/job title) | 7 required fields depress conversion |
| 14 | SEO | 12-lang hreflang, rich OG/Twitter, sitelinks search schema, per-page meta | No Product schema; duplicate H1; generic home title |
| 15 | Internal linking | Hub-spoke, breadcrumbs, topic clusters (101 guides→categories) | Outbound to regional domains fragments authority; dead industry icons |
| 16 | Page speed | Cloudflare CDN + gzip + WP Engine + WebP | ~1.2s TTFB; 88 scripts + Slider Rev = heavy JS/LCP (Confidence: Medium) |
| 17 | Mobile | Responsive viewport, custom breakpoints, font-swap | 16-column spec tables hard on mobile; JS weight |
| 18 | Content/UX | Podcast + video + 101 guides + white papers = authority engine | — |

---

## What SVMH should COPY

1. **Rich, dual-unit product/spec pages.** Kito Crosby's product pages are the gold standard: full specification bullets, **standards compliance cited explicitly** (IS 807 / IS 3177 / FEM 9.511 for SVMH), and **dimensional data tables**. SVMH should give each crane type and component (crab units, hooks, DSL busbars, gearboxes, sheaves, rope drums) a real spec page — not just a product photo.
2. **Downloadable technical documents per product.** Offer datasheet PDFs, general-arrangement drawings, load charts, and maintenance/user manuals as direct downloads. This is what specifying engineers and consultants need and it builds enormous credibility vs. an IndiaMART listing.
3. **Trust-by-numbers + heritage block.** SVMH has real assets: founded 2006, ~Rs 13.6 Cr FY24, ISO 9001, GST/MSME, named industries served (automotive, steel, power, foundry, cement, construction). Put "Years in business / cranes delivered / industries served / certifications" as a prominent stats strip like Kito's "4000+ / 50+ / 3500+".
4. **Industry-specific landing pages.** Kito maps products to 30 industries. SVMH should build focused pages for its 6 core industries (automotive, steel, power, foundry, cement, construction) with relevant crane types + a mini case list — strong for both SEO and buyer relevance.
5. **Educational "101" resource content + video.** "How it's made" and "Shackles 101"-style guides drive SEO and authority. SVMH can do "EOT vs. Gantry: which crane do you need?", "Understanding FEM/IS crane duty classes", plus factory/erection videos — cheap, high-trust, and differentiates from competitors who only list products.
6. **Clean technical SEO baseline.** Typed XML sitemap, per-page meta descriptions, canonical tags, Open Graph tags, breadcrumb schema. And **do the thing Kito omitted** — add **Product schema** to product pages for rich results (an easy win SVMH can beat them on).
7. **Product/part search + faceted category grids** if SVMH lists a spares/components catalog.
8. **Certifications/quality page** with visible ISO 9001 and standards badges.

## What SVMH should AVOID

1. **Slider Revolution + heavy carousel hero.** Kito's homepage carries 88 scripts and a rotating hero — an LCP/performance tax. SVMH should ship a **fast, static hero** with one clear CTA (a small manufacturer's speed advantage is real; don't throw it away on a bloated Elementor build).
2. **Gating core technical downloads behind a 7-field form + CAPTCHA.** For a challenger brand trying to win trust, make datasheets and drawings **freely downloadable**; capture leads with a light optional form, not a wall.
3. **Replacing a real contact path with only a geolocation locator.** Kito's `/contact`→`/locator` and "No contacts found" dead-end is wrong for a single-location, direct-sales Indian manufacturer. SVMH should show **phone, WhatsApp, email, address, map, and a short RFQ form prominently**, plus a per-product "Request a Quote" button.
4. **Soft CTA language ("More"/"Learn More").** Use action/commercial CTAs: "Get a Quote", "Download Datasheet", "Talk to an Engineer", "Request AMC Visit".
5. **Missing `alt` text.** 67/83 homepage images without alt is an accessibility and image-SEO miss — SVMH should alt-tag every product image (also helps Google Images discovery for "EOT crane manufacturer Bengaluru").
6. **Multi-brand IA complexity.** Kito's redirect chain and 6-brand mega-menu are enterprise problems SVMH doesn't have. Keep IA **simple and shallow**: Products → (crane types + components) → spec page → quote.
7. **Duplicate H1 / generic home title.** Give the homepage one H1 and a keyword-rich title ("EOT & Gantry Crane Manufacturer in Bengaluru | SVMH") — SVMH can out-optimize Kito on local/long-tail intent where the giant is generic.

---

## Evidence log (URLs accessed 2026-07-05)

| URL | What it evidenced | Confidence |
|---|---|---|
| `https://kito.com` (→ kitocrosby.com) | Redirect; homepage; Columbus McKinnon acquisition; brand portfolio; meta/OG | High |
| `https://kitocrosby.com/` (raw HTML) | 88 scripts, 83 imgs (67 no-alt), 2×H1, schema types, hreflang×12, TTFB 1.23s, gzip, Cloudflare | High |
| `firecrawl_map` (916 URLs) | Sitemap scale: 636 products, 41 news, 19 resource, 17 training, 17 categories, 12 leadership | High |
| `https://kitocrosby.com/product-categories/` | 18-category visual grid, unified Crosby+Gunnebo catalog, part-number search | High |
| `https://kitocrosby.com/product-category/shackles/` | WooCommerce archive, filter/sort/pagination, 100+ video links, Salsify DAM | High |
| `https://kitocrosby.com/product/crosby-g-2130-s-2130-bolt-type-anchor-shackles/` | Dual-unit spec tables, standards, 6 PDF downloads, gated CAD form; no Product schema | High |
| `https://kitocrosby.com/kito/` | Kito brand hub, product lines, "first to" innovation timeline, regional site links | High |
| `https://kitocrosby.com/industries/` | 30 industries, ~8 with deep pages, rest icon-only | High |
| `https://kitocrosby.com/contact` (→ /locator/) | Geolocation rep finder as contact model; "No contacts found" on blank | High |
| `https://kitocrosby.com/about` | 4000+ employees, 50+ sites, 3500+ distributors; formed 2023; brand heritage dates | High |
| `https://kitocrosby.com/resource-sitemap.xml` | 19 "101"/insight educational guides | High |

**Cross-referencing note:** Corporate scale figures (4000+/50+/3500+) and heritage dates (1764/1867/1932) appear consistently across `/about` copy and JSON-LD Brand schema (two independent locations in-source). Performance conclusions (LCP/CWV) are Confidence: Medium — based on server timing + script/asset counts, not a full Lighthouse field test.
