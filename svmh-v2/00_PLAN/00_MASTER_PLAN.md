# 00 — Master Plan

**Project:** SVMH v2 — clean-room website build
**Client:** S.V. Material Handling System Pvt. Ltd. · Harohalli KIADB, Kanakapura Taluk, Ramanagara Dist., Bengaluru, Karnataka
**Date:** 2026-07-27
**Status:** Plan approved-pending → design phase not yet started

---

## 1. The problem in one paragraph

SVMH is a ~₹13.6 Cr family-owned EOT/gantry/jib crane manufacturer (founded 2006, group lineage to 1994, MD Shri D. Umapathi, 30+ years) with real heavy-engineering capability — including a genuinely defensible **hot-metal / ladle / foundry crane** niche — and effectively no digital presence. `svind.co.in` is sparse and its **SSL certificate has expired, so the site fails to load entirely** (verified 2026-07-05). Demand is outsourced to IndiaMART and ExportersIndia, which commoditises the company into a price line-item. Meanwhile ElectroMech (~₹684 Cr FY25, ~50× SVMH) publishes 13 industry pages, a technical blog and ~25 case studies, and **K2 Cranes of Chennai is actively ranking for "EOT crane manufacturers in Karnataka / in Bangalore"** — attacking SVMH's home turf. Local Bengaluru rivals (Associated Hoists, ABCO, Gayathri, Ace, Kiran, Pegasus) have no blog, no guides, no case studies, no downloads and no pricing. The opening is wide, and it closes as competitors mature.

## 2. Strategic objective

Reframe the buying conversation from **"price of steel"** to **"20-year total cost of ownership plus safety liability"**, and own the three SERP gaps nobody defends: **local Bengaluru/Karnataka intent**, **INR price transparency**, and **Indian-standards education (IS 807 / IS 3177 / IS 4137)** — with the foundry/ladle niche as the profit wedge.

### Success metrics (12 months)

| Metric | Baseline | Target |
|---|---|---|
| Site loads over valid HTTPS | Fails | 100% uptime, A-grade TLS |
| Indexed money-pages | ~0 | 6 pillars + 14 spokes |
| Bengaluru/Karnataka local pack presence | None | Top-3 for 4 core local queries |
| Inbound RFQs from owned site | ~0 (all aggregator) | 20+/month qualified |
| Downloadable proof assets (datasheets, ISO, CAD) | 0 | 15+ |
| Lighthouse mobile perf / a11y | n/a | ≥90 / ≥95 |

## 3. Quality bar

The reference boards in `../refer/` set the standard. Distilled: this must read as a **premium industrial editorial site**, not an SME brochure. Concretely — oversized display type with the product cut-out occluding a ghost watermark headline; exactly one saturated accent against a disciplined neutral; full-bleed colour bands as section separators instead of borders; numbered `01 / 02 / 03` index rows replacing icon bullets; giant-numeral stat lockups as the reusable proof unit; hairline grids where the grid itself is the decoration; whole-card accent-fill hover states. See `../01_DESIGN/DESIGN_SYSTEM.md` for the enforceable version.

The counter-rule, from the audits: **no hero carousel**, no multi-message hero, no product-in-void photography, no mixed icon styles.

## 4. The nine moves, mapped to build phases

Ranked in `../research/16_Reports/10_Actionable_Recommendations.md`.

| # | Move | Phase |
|---|---|---|
| 1 | Fix SSL, ship a secure fast mobile-first site | **Gate 0** — blocks everything |
| 2 | Own Bengaluru/Karnataka local SERP + GBP + city pages | Phase 1 |
| 3 | Product money-pages with INR price transparency | Phase 1 |
| 4 | Close the credibility gap: catalogue, datasheets, downloadable ISO 9001 | Phase 1 |
| 5 | Win the foundry / ladle / hot-metal niche | Phase 2 |
| 6 | Productise AMC/service + spares | Phase 2 |
| 7 | India-standards + buyer-education snippet content | Phase 2 |
| 8 | Proof: case studies, client logos, factory/FAT video | Phase 2 |
| 9 | Engineering tools: calculators, CAD library, configurator | Phase 3 |

## 5. Phase plan

### Gate 0 — Foundations (Week 0)
Not a design task, but nothing else matters until it clears.
- Renew/reissue TLS on `svind.co.in`; force HTTPS; HSTS.
- Confirm hosting, DNS control, and who holds the registrar login.
- Collect from client: ISO 9001 PDF, GST/MSME certificates, real install photos, capacity/span/duty data for 5 reference projects, factory video footage, client-logo permissions.
- **Exit criteria:** valid cert, asset pack received or gaps explicitly logged as `[CLIENT TO CONFIRM]`.

### Phase 1 — Design system + core commercial spine (Weeks 1–4)
- Tokens → `.pen` design file → high-fidelity boards for Home, Product money-page, Location page, RFQ.
- Greybox wireframes for all 7 templates, reviewed before any pixels.
- Build: Home, 6 pillar pages, Bangalore location page, Contact/RFQ, Trust/Certifications.
- Every product page ships with an inline pre-filled RFQ, a downloadable datasheet, an INR price band, and IS-compliance block.
- **Exit criteria:** Lighthouse ≥90 mobile, RFQ submits end-to-end, all 6 pillars live, zero placeholder copy.

### Phase 2 — Proof, niche and service (Weeks 5–10)
- Foundry/ladle capability page (IS 4137, M8 duty) — the margin wedge.
- Industry landing pages: automotive, steel, power, foundry, cement, construction.
- Case studies with quantified project cards; client logo strip; FAT/factory video.
- AMC & spares hub with response-time commitment and stocking policy.
- Standards explainers targeting featured snippets (IS 807 classification table, single-vs-double girder table, duty class M5/M7 table, "what is an EOT crane" paragraph).
- **Exit criteria:** 5 case studies published, 6 industry pages live, FAQPage/HowTo schema validating.

### Phase 3 — Engineering moat (Weeks 11–16+)
- Crane selector / duty-class configurator feeding a pre-filled RFQ.
- Load / wheel-load / span calculators.
- INR price estimator.
- Searchable spare-parts finder; CAD/DWG library.
- **Exit criteria:** at least two interactive tools live; each one ends in an RFQ handoff.

## 6. Template inventory (7 templates, ~30 pages)

| Template | Instances | Priority |
|---|---|---|
| T1 Home | 1 | P0 |
| T2 Product pillar / money-page | 6 pillars + 14 spokes | P0 |
| T3 Location page | Bangalore, Karnataka, +4 cities | P0 |
| T4 Industry page | 6 | P1 |
| T5 Case study | 5+ | P1 |
| T6 Resource / standards article | 8+ | P1 |
| T7 Utility (Contact/RFQ, Trust, About, Downloads) | 4 | P0 |

Full URL map in `01_SITEMAP_IA.md`. Section-by-section specs in `02_PAGE_WIREFRAME_SPEC.md`.

## 7. Working order (do not reorder)

```
tokens.json ──► .pen variables ──► .pen boards ──► export PNG/HTML
     │                                                    │
     └──► 02_WIREFRAMES/lofi/*.html (greybox, reviewed) ───┴──► 03_BUILD/
```
Rationale: the wireframe locks structure and content before art direction gets a vote, and the `.pen` file stays the single source of visual truth so the build never becomes the design.

## 8. Definition of done (per page)

- [ ] Real copy, no lorem, no unverified claims
- [ ] One dominant H1 message + one primary CTA
- [ ] Inline RFQ with the product/context pre-selected
- [ ] Sticky WhatsApp + click-to-call on mobile
- [ ] Trust strip present above the first fold break
- [ ] Meta title + meta description written (the root site has none — do not repeat that)
- [ ] JSON-LD: Organization, LocalBusiness, Product, FAQPage as applicable
- [ ] All images have descriptive, spec-bearing alt text (capacity/span/industry)
- [ ] Keyboard-navigable; visible focus ring; `aria-*` on all interactive controls; table `scope`
- [ ] Lighthouse mobile ≥90 perf, ≥95 a11y
- [ ] Renders 360px → 1920px without horizontal scroll

## 9. Risks

| Risk | Mitigation |
|---|---|
| Client asset pack never arrives (photos, ISO PDF, project data) | Ship with `[CLIENT TO CONFIRM]` markers and a written asset request list; never fabricate proof |
| Financial opacity ("Issuer Not Cooperating") surfaces in buyer research | Lead with operational proof — installs, duty class, FAT — not financial scale |
| Price transparency invites undercutting | Publish *bands* with cost-factor explanation, not quotes; anchor on TCO |
| K2 Cranes deepens Karnataka SEO first | Ship the Bangalore location page in Phase 1, not Phase 2 |
| Scope creep into Phase 3 tools before the spine converts | Gate Phase 3 on Phase 1 RFQ volume |
