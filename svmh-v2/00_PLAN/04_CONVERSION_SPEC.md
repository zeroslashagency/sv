# 04 — Conversion Spec

Source: `../../research/16_Reports/09_Conversion_Opportunity_Report.md`, `13_Feature_Ideas/feature_ideas.md`, `05_Customer_Research/`.

Competitors leak conversions three ways: they make buyers **leave the product page** to enquire, they **hide price and specs**, and their heroes **dilute the CTA**. Every element below exists to not do those three things.

---

## 1. Priority stack

| Priority | Element | Competitor benchmark | Phase |
|---|---|---|---|
| **P0** | On-page smart RFQ with product pre-selected | Konecranes/Demag/CM route away; Kito gates | 1 |
| **P0** | Progressive RFQ mirroring the IS 3177 mental model | Street's static FAQ is the closest anyone gets | 1 |
| **P0** | Sticky WhatsApp + click-to-call | Rare among premium brands; expected in India | 1 |
| **P0** | Proof before the first scroll | Most competitors lead with brand story | 1 |
| **P1** | Transparent INR price guidance + cost factors | Premium brands hide price entirely | 1 |
| **P1** | Single dominant hero CTA, one value prop | Kito/GH/ABUS/CM all dilute | 1 |
| **P1** | Lead magnets: datasheets, CAD, buyer guides | Kito gates heavily; India players thin | 1–2 |
| **P1** | Industry landing pages + case studies | CM/GH do it; Indian SMEs don't | 2 |
| **P2** | Duty-class / crane selector as an interactive CTA | Nobody offers it | 3 |
| **P2** | Trust-signal strip | Inconsistent regionally | 1 |
| **P2** | Spares quick-order + AMC booking | Cranedge owns service SEO | 2 |
| **P3** | Callback scheduler / MD direct line | — | 2 |

## 2. The RFQ engine

The form is not a contact form. It is the **IS 3177 requirement definition sequence**, which means filling it in is genuinely useful to the buyer and simultaneously qualifies the lead.

```
STEP 01  Crane type        [pre-filled from the page the buyer came from]
STEP 02  Capacity (T)  ·  Span (m)  ·  Lift height (m)
STEP 03  Duty / usage class  ·  Indoor / outdoor  ·  Environment (hot metal, dusty, corrosive)
STEP 04  Name · Company · Phone · Email · City
```

Design: label-less underline inputs (SwiftCargo board pattern), `01 — 04` mono step counter top-right, flat copper submit, no modal. Contact details are requested **last**, after the buyer has received value from the spec exercise.

**Fast-track rail** beside the form: `WhatsApp us this spec`, `Call now`, and a stated `Typical response within [X] working hours` — the number comes from the client, not from us.

**Routing:** complete + spec'd → sales immediately. Incomplete → nurture with the buyer's guide and the relevant datasheet. Every submission echoes the spec back to the buyer by email so the form doubles as their own requirement record.

**Pre-fill contract:** every entry point carries context forward. Product page → crane type. Location page → city. Industry page → environment. Calculator (Phase 3) → capacity/span/duty. Nothing is ever re-typed.

**Validation & security:** client-side required-field validation with inline messages tied to inputs via `aria-describedby`, honeypot plus timing check for bots, server-side validation and rate limiting on the endpoint, no PII in query strings or analytics, and HTTPS-only submission. The endpoint needs a real server or a form service — flag to the client which one before build, since a static host alone cannot process submissions securely.

## 3. Sticky conversion furniture

- **Mobile (<768px):** fixed bottom bar, three equal cells — `Call` (`tel:`), `WhatsApp` (`wa.me` with a pre-filled message naming the current page), `Get a Quote`. 56px tall, safe-area inset respected.
- **Desktop:** right-rail floating WhatsApp button, plus the copper CTA cell permanently in the sticky header.
- WhatsApp pre-fill example: `Hi SVMH, I'm looking at the Double Girder EOT Crane page. I need ~20 T / 18 m span.`

## 4. Trust signal order

Ranked by what actually moves Indian crane buyers, per the customer research:

1. Industry-tagged reference installs + FAT / factory video — the biggest single lever.
2. Certifications: ISO 9001, IS 807 / 3177 declaration, GST, MSME — all downloadable.
3. Years and installs stats.
4. Named client logos and case studies.
5. Local service coverage map with a guaranteed response window.
6. **Spares stocking policy** — the maintenance engineer decides on this, and they are the after-sales gatekeeper.

Anything not yet evidenced is marked `[CLIENT TO CONFIRM]` in the build and withheld from the live page. Fabricated proof on a safety-critical product is a liability, not a shortcut.

## 5. Objection → element map

| Objection | On-site answer |
|---|---|
| "Why pay more than the cheap local quote?" | TCO block + duty-class explainer + cost-factor page |
| "Can they actually deliver quality?" | FAT video + reference installs + ISO 9001 PDF |
| "What happens when it breaks?" | Spares stocking policy + response commitment + AMC CTA |
| "Are they a serious, established firm?" | Trust strip + since-2006 + factory proof + MD story |
| "Can they handle hot metal / heavy?" | Foundry-ladle capability page + IS 4137 + M8 duty proof |
| "Will I be locked into their service?" | Standard components, open spares list, training offer |

## 6. Measurement

Track: RFQ starts, per-step drop-off, RFQ completions, WhatsApp clicks, call clicks, datasheet downloads, price-page → RFQ path, calculator → RFQ path (Phase 3), and local-page → RFQ by city. Instrument with a privacy-respecting setup — no PII in event payloads, consent honoured before any analytics loads.

Baseline is effectively zero owned-site conversions today, so the first month of data sets the benchmark rather than testing against one.
