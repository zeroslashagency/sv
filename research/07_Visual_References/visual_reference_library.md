# Visual Reference Library — Crane & Industrial Manufacturer Websites

**Client:** S.V. Material Handling Systems Pvt Ltd (SVMH), Bengaluru
**Purpose:** Catalog of best-in-class visual references (with live URLs) to inform a superior SVMH website. Each entry = Source URL + description + "Why it works." Recurring patterns in premium industrial brands summarized at the end.
**Date accessed:** 2026-07-05
**Method:** Live capture via firecrawl_scrape / firecrawl_search / WebSearch. All URLs verified live on 2026-07-05 unless noted.

> **How to read confidence:** *High* = observed directly in scraped page markup/image assets on 2026-07-05. *Medium* = described in a reputable secondary source (design agency roundup) and consistent with the live site. *Low* = inferred or single-source; flagged inline.

---

## Master Reference Table (quick index)

| # | Brand | URL | Primary visual strength | Confidence |
|---|-------|-----|------------------------|-----------|
| 1 | Konecranes | https://www.konecranes.com/en-us | Rotating hero + 3D product renders + "Build & Quote" tool | High |
| 2 | Demag | https://www.demagcranes.com/en | Clean product-tile grid, case-study photo wall, configurator entry points | High |
| 3 | Street Crane | https://streetcrane.com/ | Cinematic factory hero, animated stat counters, client logo wall | High |
| 4 | ABUS Crane Systems | https://www.abuscranes.co.uk/ | Autoplay video hero, "crane-in-action" installation photography | High |
| 5 | ElectroMech (India) | https://www.emech.com/in/ | Industry-icon grid, India-market framing (cautionary example) | High |
| 6 | Liebherr | https://www.liebherr.com/en-int | Umbrella-brand corporate design, proprietary typeface | High |
| 7 | Caterpillar | https://www.caterpillar.com/ | Legacy branding + bold typographic hero, consistent design system | Medium |
| 8 | GE Aerospace | https://www.geaerospace.com/ | Video-anchored hero, editorial typography hierarchy | Medium |
| 9 | Boston Dynamics | https://bostondynamics.com/ | Whitespace, modular blocks, selective animation | Medium |
| 10 | Aerotech | https://www.aerotech.com/ | Timeline + stats "About" storytelling | Medium |
| 11 | Path Robotics | (case study) windmillstrategy.com | "It sees / understands / welds" 3-step explainer | Medium |
| 12 | Auria | (case study) windmillstrategy.com | Interactive "products on a vehicle" hotspot tool | Medium |

---

## 1. HERO SECTIONS

### 1.1 Konecranes — rotating message hero with product render
- **URL:** https://www.konecranes.com/en-us
- **What it is:** Full-bleed hero carousel (2 slides observed): slide 1 a bold safety-led headline ("Detect dangers and prevent accidents…") over an application photo; slide 2 a KBK workstation lifting system on a clean industrial backdrop with "Ergonomic and cost effective workstation lifting." Each slide pairs one big headline + one-line subhead + single CTA.
- **Why it works:** One idea per slide, ruthless message hierarchy (headline → subhead → single CTA). It leads with *customer outcome* (safety, cost) rather than product specs. The paired 3D M-series render lower on the page ("3D image of Konecranes M-series crane on girders") signals engineering capability without a photo shoot.
- **Evidence:** Hero assets `3_hero_adline_mar2026.jpg` and `koncranes-kbk-workstation-lifting-system.jpg`; slide indicators "1 / 2" in scraped markup.
- **Confidence:** High

### 1.2 Street Crane — cinematic factory hero + heritage line
- **URL:** https://streetcrane.com/
- **What it is:** Hero opens with "Since 1946, One of the world's leading… Crane Manufacturers and Suppliers" and a "Scroll Down" affordance, over factory/manufacturing imagery. Immediately followed by a value statement: "We Specialise in the Design, Manufacture, and Supply of Overhead Cranes and Hoists."
- **Why it works:** Heritage year ("Since 1946" / "80 years") is used as the first trust signal — powerful for a legacy manufacturer. The scroll cue invites exploration rather than dumping the menu. Clean type over real factory imagery reads as authentic, not stock.
- **Evidence:** Scraped H1 + "80 Years Experience / 30,400+ Projects Completed / 70 Countries" stat block directly under hero.
- **Confidence:** High

### 1.3 ABUS — autoplay video hero
- **URL:** https://www.abuscranes.co.uk/
- **What it is:** Background `<video>` element (scraped as "Your browser does not support the video tag") behind headline "High-quality industrial cranes" + invitational subhead ("Experience crane technology that inspires…") with dual CTAs "Contact" / "Discover now."
- **Why it works:** Motion of a crane actually lifting in a real hall conveys capability in seconds — more persuasive than a static render. Dual CTA serves both "ready to talk" and "still exploring" visitors. Tagline is aspirational ("technology that inspires") yet grounded.
- **Evidence:** Scraped `<video>` tag fallback text + H1 "High-quality industrial cranes" with Contact/Discover CTAs.
- **Confidence:** High

### 1.4 Caterpillar / GE Aerospace — bold typographic + video heroes (benchmark tier)
- **URLs:** https://www.caterpillar.com/ , https://www.geaerospace.com/
- **What it is:** Per Huemor's 2026 analysis, Caterpillar's homepage "leverages legacy branding and future-focused messaging in equal measure, using modular content and strong visuals"; GE Aerospace "blends storytelling and structure… using video, typography, and layout to anchor trust and innovation."
- **Why it works:** These are the aspirational ceiling — large-scale but still "feel nimble and user-first when content is structured well." Video + typography carry the hero; product specs live deeper.
- **Confidence:** Medium (secondary source: Huemor roundup, 2026-02, consistent with live sites)

---

## 2. PRODUCT PHOTOGRAPHY

### 2.1 Demag — product tiles as photographic hero cards
- **URL:** https://www.demagcranes.com/en
- **What it is:** A grid of product cards (Demag Cranes, Hoist Units, Drives, Components), each a clean studio-style product photo on neutral background with a one-line benefit ("Cost-effective, reliable and safe." / "Technological expertise in lifting technology."). Assets are `1440x810` webp renders.
- **Why it works:** Consistent aspect ratio, consistent lighting, consistent neutral backdrop across the whole range = an ordered, premium catalog feel. Each product is isolated so the hardware is the hero. Benefit-line captions do the selling.
- **Evidence:** Scraped card assets `42240_1_1440x810px_0.jpg.webp`, `43155_Hero.png.webp`, `38944-5-2_Antriebstechnik.jpg.webp`, `Demag_1440x810_42132-3.jpg.webp`.
- **Confidence:** High

### 2.2 Street Crane — product category photography with contextual captions
- **URL:** https://streetcrane.com/cranes/
- **What it is:** Home product tiles ("Cranes" up to 250 tonnes; "Components & Hoists"; "Spares & Servicing") each with a real product/kit photo and a specific capability caption (e.g., kits "include everything needed to build a complete overhead crane except the steelwork").
- **Why it works:** Photography is paired with a concrete spec/claim, not a vague adjective — respects a technical buyer. "Genuine Street parts" framing on the spares tile builds aftermarket trust.
- **Evidence:** Scraped tiles `Home-Page-Cranes-1-scaled.jpg`, `Home-Page-Hoists-2-scaled.jpg`, `Mask-Group-10-1.png`.
- **Confidence:** High

### 2.3 Recurring rule — "product-in-use over product-in-void"
- **Source:** https://huemor.rocks/blog/best-manufacturing-website-designs/ ("Purpose-Driven Visuals Over Decoration")
- **Insight:** Best sites favor "product-in-use photos" that "help users connect function with value," reserving clean isolated renders for the catalog grid. Avoid generic stock that "adds visual noise without purpose."
- **Why it matters for SVMH:** SVMH should shoot its own crabs, hooks, DSL busbars, gearboxes both ways — isolated (catalog grid, à la Demag) *and* installed/in-operation (hero + industry pages).
- **Confidence:** Medium (secondary, well-aligned with observed sites)

---

## 3. FACTORY / MANUFACTURING PHOTOGRAPHY

### 3.1 Street Crane — "our facilities" and "hoists ready to leave" shots
- **URL:** https://streetcrane.com/about/
- **What it is:** Homepage embeds manufacturing/facility imagery ("some of the most up-to-date manufacturing facilities in the world at our headquarters in the High Peak") plus a staged shot of finished hoists on the shop floor ready for dispatch (`Hoists-ready-to-leave-8…jpg`) and a design/engineering shot (`Design-Shot-5-scaled.jpg`).
- **Why it works:** Factory imagery is proof of in-house manufacturing capability — a key differentiator vs. traders/assemblers. "Ready to leave" framing implies volume and reliability.
- **Evidence:** Scraped asset names + copy "most up-to-date manufacturing facilities in the world."
- **Confidence:** High

### 3.2 ABUS — production + KranHaus HQ photography
- **URL:** https://www.abuscranes.co.uk/company-profile/abus-production
- **What it is:** Dedicated "ABUS Production" and "KranHaus" sections with facility photography of the Gummersbach plant; "made in Germany" is used as a visual/verbal seal throughout.
- **Why it works:** Ties place + provenance to quality. A named, photographed HQ ("Visit us in Gummersbach") humanizes a heavy-industrial brand and reinforces the family-business narrative.
- **Evidence:** Scraped nav items "ABUS Production," "KranHaus," title tag: `Indoor cranes "made in Germany"`.
- **Confidence:** High

### 3.3 Best-practice note — cinematic factory shooting
- **Source:** https://caseytempleton.com/blog/types-of-industrial-photography/ ; https://www.studio13online.com/how-high-quality-industrial-photography-can-make-your-brand-accessible-to-all/
- **Insight:** Industrial photography as a genre documents "facilities, people, and processes behind an industrial brand" — the recommended trio is *facility wide shots + process detail + people at work*. High-quality lighting (controlling harsh factory light, sparks/weld glow as drama) makes heavy environments feel premium and "accessible."
- **Why it matters for SVMH:** Commission a dedicated shoot of the Bengaluru fabrication floor — wide establishing shots, close process detail (welding, machining of rope drums/sheaves), and operators in branded PPE.
- **Confidence:** Medium (industry-practitioner sources)

---

## 4. INSTALLATION PHOTOGRAPHY (crane-in-situ / at customer site)

### 4.1 ABUS — "crane in action" application photography with descriptive alt text
- **URL:** https://www.abuscranes.co.uk/
- **What it is:** Large teaser images of cranes doing real work, with unusually descriptive alt text: *"An employee operates a jib crane equipped with an electric chain hoist and performs precise load positioning inside an industrial building."* Reference-project thumbnails (Chiarizia, Hollandia, NARGESA) each show the installed crane in the customer's hall.
- **Why it works:** Shows the product solving a real handling task in a real facility → the buyer pictures it in *their* plant. Descriptive alt text is both accessibility-strong and SEO-strong. Dated "Project of the month" cadence signals an active, living company.
- **Evidence:** Scraped alt strings + reference thumbnails `Auswahl_2…jpg`, `Standbild01…jpg` under "References & News."
- **Confidence:** High

### 4.2 Demag — case-study photo wall (installed solutions)
- **URL:** https://www.demagcranes.com/en/industry-expertise/case-studies
- **What it is:** A large scrollable "Case studies" carousel, each card a real installation photo + customer name + the handling challenge solved (e.g., "Safe handling of construction elements up to 25 meters long and weighing 40 tons – in any weather," Neumüller portal crane; spec caption: "Span 26 m, cantilever ~8 m, two 20 t DH hoists, lift height 10 m").
- **Why it works:** Each image is captioned with *quantified* specs and a named customer — turns a photo into verifiable proof. Breadth of logos/industries (Omega Flex, WILO, Arvato, motorhome maker MORELO) demonstrates versatility.
- **Evidence:** Scraped case-study cards with customer names + spec captions.
- **Confidence:** High

### 4.3 Street Crane — named-brand installation case studies
- **URL:** https://streetcrane.com/industry/
- **What it is:** Case-study grid featuring blue-chip installs (Tata Steel, Bombardier composite aircraft wings, Hitachi Rail 40-t offloading cranes, AMRC Factory 2050), each a photo of the crane installed at that site with capacity/duty specifics.
- **Why it works:** Recognizable customer names + specific application photos = maximum credibility transfer. The pairing of *logo wall* (JCB, BMW, Rolls-Royce, BAE) with *photographed installs* closes the loop between claim and proof.
- **Confidence:** High

---

## 5. TEAM / PEOPLE PHOTOGRAPHY

### 5.1 Street Crane — leadership portrait + staff imagery + founder quote
- **URL:** https://streetcrane.com/about/
- **What it is:** A CEO headshot (`Gus-Head-Shot-6-min.png`) paired with a signed quote from Gus Zona (Group CEO) about family values; plus a "Our Strength Lies in Our People" section with a staff group photo (`Home-Page-Staff-7.jpg`) and copy celebrating "from the factory floor to the boardroom."
- **Why it works:** Real named faces + a personal leadership quote humanize a heavy-industrial brand and directly reinforce the "family-owned" positioning — highly relevant to SVMH (also family-owned since 2006). People imagery differentiates from faceless catalog competitors.
- **Evidence:** Scraped headshot/staff assets + full CEO quote.
- **Confidence:** High

### 5.2 ABUS — careers/team imagery tied to values
- **URL:** https://www.abuscranes.co.uk/ (Careers block) → https://abuscareers.co.uk/
- **What it is:** A full-width "Careers at ABUS" people image plus values copy ("mutual respect, trust and strong teamwork… we put people at the centre"). Employee-in-action shots double as team + installation photography.
- **Why it works:** Frames the workforce as the brand's competence. Values-led people photography supports recruiting *and* buyer trust simultaneously.
- **Confidence:** High

---

## 6. TECHNICAL ILLUSTRATIONS & 3D / CUTAWAY

### 6.1 Konecranes — 3D product renders + "Build & Quote" configurator
- **URLs:** https://www.konecranes.com/en-us ; https://www.konecranes.com/en-us/equipment/overhead-cranes/build-quote
- **What it is:** 3D CGI renders of the M-series crane on girders used as clean "liftup" imagery; and an interactive **Build & Quote** tool that returns "price information… specifications, line drawings and .IFC drawings that can be integrated into your building design."
- **Why it works:** 3D renders show product configurations that would be impractical/expensive to photograph, and read as "engineered." The configurator converts a passive brochure into an *interactive spec-generating* experience — deliverables (IFC/CAD) are exactly what a technical buyer needs, shortening the sales cycle.
- **Evidence:** Scraped `Konecranes M-series 3D … homepage liftup image.jpg`; Build & Quote description in scraped body + search result confirming IFC/line-drawing output.
- **Confidence:** High

### 6.2 Demag Designer / Configurators — CAD + 3D model self-service
- **URLs:** https://www.demagcranes.com/en/demag-configurators ; http://www.demag-designer.com/
- **What it is:** "Demag Configurators — Your offer in just a few clicks" and "Demag Designer — request CAD models, research technical information." 16,000+ orderable products in the Demag Shop.
- **Why it works:** Positions engineering documentation as a self-serve visual product. Reduces friction for specifiers and signals depth of catalog.
- **Confidence:** High

### 6.3 Industry technique reference — cutaway / exploded / X-ray 3D
- **URLs:** https://cranedigital.com/3d-cut-away-illustration-and-animation/ ; https://3deeit.com/ ; https://motiongiraffx.com/blog/3d-animation-for-manufacturing-companies/
- **What it is:** Specialist studios showing cutaway views, transparencies, floating/exploded parts, and X-ray views to "show sealed internals, assembly sequences, and process flows photography can't."
- **Why it works:** For components SVMH sells (crab units, gearboxes, wire-rope hoists, DSL busbars), a cutaway/exploded render reveals internal engineering quality that a closed housing hides — a strong differentiator over photo-only competitors.
- **Confidence:** Medium (specialist vendor sources describing the technique)

### 6.4 CMAK.Tools — crane quoting with 3D models & drawings (competitor tooling)
- **URL:** https://cmak.com/en/cmak-tools/
- **What it is:** Cloud crane configurator generating "crane quotes, 3D models, CAD drawings and technical proposals in minutes" incl. duty classification and PDF proposals.
- **Why it works:** Demonstrates the emerging category standard — even mid-tier crane makers now offer instant 3D + spec generation. A benchmark for what "advanced" looks like in this exact vertical.
- **Confidence:** High (vendor page, live)

---

## 7. ICONS

### 7.1 ElectroMech — industry & solution icon grids (India benchmark, mixed)
- **URL:** https://www.emech.com/in/
- **What it is:** Two icon-led grids: a **Solutions** grid (Hoist, Overhead Cranes, Other Material Handling, Services) and a large **Industries** grid (Oil & Gas, Precast, Renewable Energy, Shipbuilding, Steel, Nuclear, Automotive, etc.) each with a per-industry PNG icon + "know more."
- **Why it works (and where it doesn't):** The *concept* is right — a scannable industry-icon grid lets a visitor self-identify their sector fast (exactly SVMH's need: automotive, steel, power, foundry, cement, construction). **Cautionary note:** ElectroMech's execution is dated — inconsistent icon styles, a heavy multi-slide carousel, and cluttered news walls. SVMH should adopt the *pattern* (industry self-selection grid) with a *cleaner, unified line-icon set*.
- **Evidence:** Scraped industry icon assets under `/04-industries/indus/new/…png` and solution thumbnails.
- **Confidence:** High

### 7.2 Best-practice icon direction — unified line-icon system
- **Sources:** https://huemor.rocks/blog/best-manufacturing-website-designs/ ("Icons and visuals used to simplify complex ideas"; "meaningful iconography" cited for 3M) ; https://www.windmillstrategy.com/best-manufacturing-websites-examples/ (Air-Cure: "colorful and unique iconography… rather than relying on generic-looking stock imagery")
- **Insight:** Premium sites use a *single, custom, consistent* icon family (line or duotone) for capabilities, industries, and spec callouts — never mixed clip-art. Custom iconography is repeatedly called out as a differentiator vs. stock.
- **Why it matters for SVMH:** Commission one bespoke line-icon set covering crane types (EOT single/double girder, gantry, jib, monorail), industries, and spec attributes (capacity, span, duty class, IS standards).
- **Confidence:** Medium

---

## 8. INFOGRAPHICS & STAT / DATA VISUALS

### 8.1 Street Crane — animated stat counters
- **URL:** https://streetcrane.com/
- **What it is:** A three-figure stat band directly below the hero: **80** Years Experience · **30,400+** Projects Completed · **70** Countries (with a `success.png` accent). These typically animate/count up on scroll.
- **Why it works:** Converts credibility into three glanceable numbers. Placing them immediately after the hero front-loads trust before the visitor scrolls into products. Big-number typography = instant scale communication.
- **Evidence:** Scraped stat block values verbatim.
- **Confidence:** High (values confirmed; count-up animation inferred from standard implementation — Confidence Medium for the animation specifically)

### 8.2 Demag — inline spec infographics in captions
- **URL:** https://www.demagcranes.com/en/industry-expertise/case-studies/gantry-crane-storage-yard
- **What it is:** Case-study captions render key specs as compact data lines ("Span 26 m, cantilever ~8 m, two DH hoists 20 t each, lift height 10 m").
- **Why it works:** Micro-infographic embedded in the photo caption gives technical buyers the numbers instantly without a separate spec sheet. Cheap to produce, high information density.
- **Confidence:** High

### 8.3 Aerotech — timeline + stats "About" storytelling
- **URL:** https://www.aerotech.com/ (per Huemor analysis)
- **What it is:** "About page… credibility reinforced through timelines, stats, and product capabilities that feel purposeful, not bloated." Legacy + innovation woven via data viz.
- **Why it works:** A heritage timeline + stat callouts is the standard premium way to tell a manufacturer's "since 19xx" story visually — directly applicable to SVMH's 2006-founding + growth-to-₹13.6 Cr narrative.
- **Confidence:** Medium (secondary)

---

## 9. ANIMATION & INTERACTION

### 9.1 Path Robotics — "It sees / It understands / It welds" scroll explainer
- **URL:** case study https://www.windmillstrategy.com/case-studies/website-redesign-for-a-cutting-edge-ai-robotics-manufacturer/ (live site: bostondynamics-tier)
- **What it is:** Homepage simplifies a complex product into three animated steps ("it sees," "it understands," "it welds") with integrated video and a "how it works" section.
- **Why it works:** Animated step sequences demystify a technical process for non-expert buyers (procurement, execs) while video satisfies engineers — serves the whole buying committee. Windmill flags animated GIF/motion as key to conversions.
- **Confidence:** Medium

### 9.2 Auria — interactive product-hotspot tool
- **URL:** case study https://www.windmillstrategy.com/case-studies/ux-visual-design-web-design-for-automotive-oem-manufacturer/
- **What it is:** An interactive tool "showing website visitors where Auria's products appear throughout a vehicle" — clickable hotspots on a vehicle diagram.
- **Why it works:** Turns a catalog into exploration. SVMH analogue: an interactive factory/plant diagram with hotspots showing where each crane type (EOT, gantry, jib, monorail) fits in a customer's facility.
- **Confidence:** Medium

### 9.3 Boston Dynamics — restrained, selective animation
- **URL:** https://bostondynamics.com/ (per Huemor)
- **What it is:** "Lets whitespace, modular content blocks, and selective animation do the heavy lifting" — motion is used sparingly for emphasis, not everywhere.
- **Why it works:** Selective animation reads as premium/confident; constant motion reads as noisy. The lesson: animate one or two key moments (hero, stat count-up, process step), keep the rest calm.
- **Confidence:** Medium

---

## 10. TYPOGRAPHY

### 10.1 Liebherr — proprietary corporate typeface as brand signature
- **URL:** https://www.liebherr.com/en-int/n/liebherr-website-facelift-shows-elements-of-the-new-corporate-design-for-the-first-time-21986-3935641
- **What it is:** Liebherr's 2021 rebrand centers on "the new company font" — "The use of the new Liebherr typeface in particular creates a characteristic and unique effect," alongside a technically-optimized logo and new color scheme, under an umbrella-brand strategy spanning 13 product segments.
- **Why it works:** A distinctive (even proprietary) typeface is the single cheapest way to make a big industrial brand instantly recognizable and consistent across a huge product range. "Clearly structured layout" + strong type does the premium lift.
- **Evidence:** Scraped press release quotes verbatim.
- **Confidence:** High

### 10.2 Boston Dynamics / GE Aerospace — clean type + strong hierarchy
- **URLs:** https://bostondynamics.com/ , https://www.geaerospace.com/ (per Huemor)
- **What it is:** "Clean typography to communicate bold value propositions with precision" (Boston Dynamics); GE uses "video, typography, and layout to anchor trust."
- **Why it works:** Bold, large, confident headline type + generous whitespace signals a modern, well-resourced company. Type hierarchy (one dominant headline, clear subheads, restrained body) is repeatedly cited as the #1 differentiator ("Message Hierarchy Is Ruthlessly Prioritized").
- **Confidence:** Medium

### 10.3 Typography principle for SVMH
- **Source:** https://huemor.rocks/blog/best-manufacturing-website-designs/ (design details #1, #10)
- **Insight:** "Headlines are bold and focused… design elements like whitespace, contrast, and typography guide the user's eye." Tone should be "confident, not cold." SVMH should pick one strong geometric/grotesque sans for headlines + a highly legible sans for dense spec tables, and enforce a strict type scale.
- **Confidence:** Medium

---

## 11. INDUSTRIAL BRANDING / COLOR & DESIGN SYSTEM

### 11.1 Konecranes — brand-identity refresh + gradient color language
- **URL:** https://www.konecranes.com/press/releases/2024/konecranes-new-brand-identity-reflects-its-ambition-to-become-global-material-handling-solutions-leader
- **What it is:** 2024 new brand identity described internally with a "colourful visualiser with pink, purple and blue" gradient asset — a deliberate move away from utilitarian industrial palettes toward a modern tech gradient, reflecting ambition to be a "global material handling solutions leader."
- **Why it works:** Signals transformation from "crane vendor" to "solutions/technology leader." Shows even the sector leader is modernizing its color language — SVMH can leapfrog dated competitors with a contemporary, confident palette.
- **Evidence:** Scraped `konecranes-new-brand-identity.jpg` teaser + press-release title.
- **Confidence:** High

### 11.2 Liebherr — umbrella-brand system across 13 segments
- **URL:** https://www.liebherr.com/en-int + metadesign case study https://metadesign.com/zh/work/liebherr
- **What it is:** "Holistic design system that enables a consistent brand experience across all touchpoints," unifying 13 diverse product segments under one umbrella brand.
- **Why it works:** A documented design system (color, type, logo, layout rules) guarantees consistency and scales as the company grows — the professional-grade approach SVMH should emulate at its own scale (crane types + components + service + AMC).
- **Confidence:** High (press release) / Medium (metadesign scope detail)

### 11.3 Caterpillar — legacy branding + rigorous UI design system
- **URLs:** https://www.caterpillar.com/ ; component-system reference https://zbdesign.webflow.io/project/caterpillar
- **What it is:** Iconic Cat yellow/black; a comprehensive atomic-design UI component library ("each symbol/component… based on Atomic Design principles"). Digital experience "feels like its products: powerful, reliable, built to perform."
- **Why it works:** A single ownable brand color (Cat yellow) + a systematized component kit = instant recognition and cross-touchpoint consistency. The takeaway for SVMH: choose one ownable accent color and build reusable components.
- **Confidence:** Medium

---

## 12. TRUST / SOCIAL-PROOF VISUALS (cross-cutting)

### 12.1 Client logo walls
- **Street Crane:** dual scrolling logo strips — JCB, Bombardier, Honda, Rolls-Royce, Centrica, BMW, FP McCann, BAE (https://streetcrane.com/).
- **ABUS:** logo slider of reference customers (Brüninghoff, Krone, Samson, Schottel, etc.) linking out to each (https://www.abuscranes.co.uk/).
- **Why it works:** "Logo walls show up before commitment moments" (Huemor, proof-layers principle). Recognizable customers transfer credibility instantly. SVMH should build a logo wall from its automotive/steel/power/cement clients.
- **Confidence:** High

---

## RECURRING VISUAL PATTERNS IN PREMIUM INDUSTRIAL BRANDS

Synthesized from the sites above + two independent design-agency analyses (Windmill Strategy; Huemor, both 2026).

1. **One-idea hero, outcome-led.** A single bold headline about the *customer's* outcome (safety, cost, reliability), one subhead, one CTA — over real footage/photo or a clean 3D render. Never a spec dump. (Konecranes, ABUS, Street Crane)

2. **Heritage/scale numbers front-loaded.** "Since 19xx," years of experience, projects completed, countries served — as animated stat counters right under the hero. (Street Crane 80/30,400+/70; Aerotech timelines)

3. **Real over stock.** Own factory, installation, and people photography beats stock. Product-in-use imagery on marketing pages; clean isolated renders in the catalog grid. (Demag grid vs. ABUS in-action shots; explicit Huemor/Windmill guidance)

4. **Quantified case-study photo walls.** Each installation photo captioned with named customer + hard specs (span, capacity, duty). Turns imagery into verifiable proof. (Demag, Street Crane)

5. **Interactive 3D / configurators are the new baseline.** Build-and-quote tools returning CAD/IFC/line drawings + 3D models are now offered even by mid-tier crane makers. (Konecranes Build & Quote, Demag Designer, CMAK.Tools)

6. **Cutaway / exploded 3D for components.** Reveals internal engineering quality that closed-housing photos hide — a differentiator for component sellers.

7. **Unified custom icon system.** One bespoke line/duotone family for industries, capabilities, and spec attributes; enables fast industry self-selection. Custom > stock clip-art. (Air-Cure, 3M; ElectroMech shows the pattern but with dated execution — a cautionary example.)

8. **Ruthless message hierarchy + generous whitespace.** Bold focused headlines, scannable modular content blocks, whitespace guiding the eye. Modular card/grid components that flex across devices. (Boston Dynamics, all top examples; Huemor detail #1, #3.)

9. **Distinctive, consistent typography.** Often a proprietary or strongly-branded typeface; strict type scale; confident-not-cold tone. (Liebherr proprietary font; GE, Boston Dynamics.)

10. **Documented design system + one ownable color.** Color/type/component rules for consistency at scale; a single ownable accent (Cat yellow; Konecranes' new gradient). Signals a modern "solutions leader," not a commodity vendor.

11. **Selective, purposeful animation.** Motion reserved for hero, stat count-ups, and process-step explainers — calm elsewhere. (Boston Dynamics; Path Robotics 3-step.)

12. **People + family-business humanization.** Named leadership portraits, signed founder quotes, staff photography tied to values — especially powerful for family-owned firms. (Street Crane, ABUS — directly relevant to SVMH.)

13. **Proof woven throughout, not siloed.** Logo walls, certifications/standards badges (ISO, IS 807/3177/FEM), and testimonials placed next to CTAs and before commitment moments. (Huemor proof-layers; all sites.)

14. **Multi-audience pathing.** Overview storytelling for execs/procurement + quick deep links to specs/CAD for engineers, on the same page. (Windmill: "70% of buyer journey online"; Konecranes, Demag.)

---

## GAPS / LOW-CONFIDENCE ITEMS

- **Exact color hex values and font names** for the referenced brands were not extracted from live CSS in this pass (would require rendering/DevTools capture). Brand-color *direction* is High confidence; specific values are unverified — **Confidence: Low** on any specific hex/font-name claim.
- **Animation behaviors** (count-up, scroll-triggered reveals) are inferred from standard implementation patterns and agency descriptions, not from recorded interaction — **Confidence: Medium** on the specific animation, High on the static content.
- **Huemor/Windmill roundup entries** (Caterpillar, GE, Boston Dynamics, Aerotech, Path Robotics, Auria) are **Medium** — described by a reputable secondary source and consistent with the live homepages, but individual visual claims were not each re-verified frame-by-frame on 2026-07-05.
- Cross-referencing: heritage/scale patterns and "real-over-stock" guidance are corroborated by ≥2 independent sources (Windmill + Huemor + observed sites). Interactive-configurator-as-baseline corroborated by 3 (Konecranes + Demag + CMAK).

---
*Compiled 2026-07-05 for SVMH website project — 07_Visual_References.*
