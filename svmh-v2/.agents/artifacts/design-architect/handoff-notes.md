# T001 Handoff — Design Architect → Page Builders

**Agent:** A (Design Architect)
**Task:** T001 — refine the design system from the reference analysis and produce builder-ready specifications
**Date:** 2026-07-28
**Status:** Complete

---

## 1. Summary

Read the authoritative design documents (`01_DESIGN/06_DESIGN_RECALIBRATION.md`, `01_DESIGN/DESIGN_SYSTEM.md`, `01_DESIGN/refboards/REFERENCE_DISTILLATION.md`), the shipped implementation (`tokens.css`, `base.css`, `components.css`, `COMPONENT_CONTRACT.md`, `JS_CONTRACT.md`), the existing pages (`index.html`, `request-a-quote.html`, `eot-cranes/double-girder.html`, `locations/bangalore.html`), and the reference boards in `refer/`.

Produced four specification documents plus seven component contracts. Everything is anchored to the **already-shipped tokens and classes** — no new token values, no new class names except five explicitly-flagged NEW requests to the Component Specialist, each with a fallback so no page is blocked.

Two gaps in the existing system are now closed:

- **Knockout typography** had no ruling. It now has one: three permitted treatments (reverse-on-image with mandatory gradient, reverse-on-ink, outline numeral capped at one per page with a `@supports` fallback), and an explicit restatement that the revoked 5–8% ghost watermark stays revoked.
- **Reference-board layouts** were catalogued in prose but not translated into markup. There are now eleven named layout patterns (L1–L11), each with a board citation, a copy-pasteable skeleton, and its responsive collapse.

## 2. Artifacts

All under `/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/`:

| File | Contents |
|---|---|
| [component-architecture.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-architecture.md) | Full component tree, 15 shipped components with variants/slots/JS/rules, 5 NEW component requests, per-page-type composition table, 12 auto-fail anti-patterns |
| [layout-patterns.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/layout-patterns.md) | Grid system as shipped, breakpoint ladder 360→1920, patterns L1–L11 with markup, 8 responsive rules, layout QA checklist |
| [typography-spacing-system.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/typography-spacing-system.md) | Exact type scale table (size/weight/lh/tracking/case per class), spacing scale + decision table, vertical rhythm, knockout implementation guide K1–K3, a11y rules |
| [component-contracts/hero.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-contracts/hero.md) | Both hero variants, slot constraints, contrast requirements |
| [component-contracts/card.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-contracts/card.md) | Text + product card, one-link rule, hover contract |
| [component-contracts/index-row-accordion.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-contracts/index-row-accordion.md) | Accordion mode + static numbered mode, progressive enhancement |
| [component-contracts/stat.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-contracts/stat.md) | Count-up contract, `.stat--accent` outline rules |
| [component-contracts/spec-table.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-contracts/spec-table.md) | Spec + compare tables, scope/caption rules, filter wiring |
| [component-contracts/nav.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-contracts/nav.md) | Header, overlay, mobile bar, z-index ladder, 768–1023px window |
| [component-contracts/band-and-layout.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-contracts/band-and-layout.md) | Page shell, band variants + colour budget, container/grid/stack |
| [component-contracts/form-rfq.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-contracts/form-rfq.md) | Full RFQ skeleton, validation contract, security requirements |
| [component-contracts/button-and-chips.md](/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/design-architect/component-contracts/button-and-chips.md) | Button variants + accent budget, chips both modes, eyebrow, spec |

## 3. Key decisions and rationale

**D1 — Palette: kept warm concrete + copper, did not switch to `#E8E8E8` / `#2B4C7E`.**
The task brief and `.agents/team-manifest.md` specify a cool-gray + navy palette with 8–12px radii and soft shadows. The repo's authoritative chain says otherwise: `06_DESIGN_RECALIBRATION.md` (stated as superseding), `tokens.css`, `COMPONENT_CONTRACT.md`, and the Orchestrator's own `.agents/artifacts/design-context-package.md` all specify concrete `#EFECE6` + copper `#C4531F`, radii ≤4px, hairlines with no shadows. All shipped CSS/JS and all four existing pages depend on that. Switching the palette would invalidate 1955 lines of `components.css`, 635 of `base.css`, and every page already built.

Verified where the brief's values came from: the RM Terex boards (`IMG_6826`, `IMG_6820`) genuinely do use a cool gray + navy pairing, so the brief's reading is defensible from the references — it just is not the system this repo implements. Resolution: honour the cool-neutral reading as an *optional treatment* rather than a palette swap — the full-bleed product stage (L10) uses `--color-concrete-2` / `--concrete-3` for exactly the flat photographic field the board shows, and `--color-steel` (`#1B3A4B`) is the site's existing navy-adjacent structural dark. **Flagged to the Orchestrator as R1 below.**

**D2 — Typography brief and repo already agree.** Inter Tight + IBM Plex Mono is what `tokens.css` ships. No conflict, nothing to reconcile.

**D3 — Knockout typography permitted, ghost watermarks stay revoked.** The brief demands a knockout guide; the recalibration revoked watermarks. These are different things and the distinction is now written down: knockout type is real, AA-contrast heading content reversed out of a dark surface; the watermark was low-opacity decoration behind unrelated content. `--color-watermark-*` tokens remain in the file for compatibility but are marked must-not-use.

**D4 — Outline numerals capped hard.** `IMG_6820`'s outline stat numerals are the most copy-able and most abusable pattern in the set. Capped at one per page, ink bands only, `@supports` fallback mandatory (without it the numeral vanishes in engines lacking `text-stroke`), and the figure must be repeated in the caption text because `--color-outline-stroke` is decorative-contrast only.

**D5 — Extend `COMPONENT_CONTRACT.md`, do not fork it.** The shipped contract is complete and internally consistent with the CSS. These artifacts add reference-derived layout patterns, per-component review gates, and the two missing rulings. Where the two documents overlap, `COMPONENT_CONTRACT.md` wins — that is what the CSS actually implements.

**D6 — No 4-up card grid.** Two boards (`IMG_6819`, `IMG_6821`) use 4-up cards, but at ~200px wide they cannot carry our type scale or the `.card__foot` spec line. `.grid--cards` stays 1/2/3.

**D7 — Carousels rejected.** `IMG_6817`'s numbered horizontal product carousel is attractive but hides content behind interaction and is already a stated rejection in `REFERENCE_DISTILLATION.md`. L6 replaces it with the chips + index-list pairing, which shows the whole sequence at a glance.

**D8 — Progressive enhancement direction differs per component, on purpose.** Accordion panels and form groups ship **visible** (JS hides them) because their content is unique and must survive JS-off. The nav overlay ships **hidden** because it is a duplicate index; showing it without JS would dump the sitemap into the page.

## 4. Open questions and risks

**R1 — Palette divergence between the task brief and the repo (needs an Orchestrator ruling).**
Two sources of truth are in circulation. I built to the repo. If the client has actually approved the cool-gray/navy direction, the correct fix is a `tokens.css` revision by the Component Specialist plus a re-review of every shipped page — **not** per-page overrides by builders. Until ruled on, builders must not introduce `#E8E8E8` or `#2B4C7E` literals. Same applies to the manifest's 8–12px radii and soft shadows, which contradict the recalibration's ≤4px / hairlines-only rule.

**R2 — RFQ endpoint is unresolved and is the highest-risk item in the build.**
Static host, no server named. The form needs server-side validation, per-IP and per-number rate limiting, and HTTPS-only POST. The `.form__trap` honeypot is a spam speed bump, not security. Nobody should ship a POST to an unconfirmed endpoint; degrade to phone/`mailto:` with the fields as a checklist until the endpoint exists. No API keys or webhook tokens may appear in client code. Detail in `component-contracts/form-rfq.md`.

**R3 — Unverified client facts.** Installed-crane count, stocking policy, phone/WhatsApp numbers and several spec values are unknown. Contract: `<span class="spec">[CLIENT TO CONFIRM]</span>` in copy, and for phone/WhatsApp specifically, **no placeholder digits in `href`** — link to the quote form instead. An invented plausible figure on a manufacturer's site is a liability, not a placeholder.

**R4 — Five NEW components are unshipped.** `.stat--accent` outline, `.stage`, `.panel--float`, `.split--ink`, `.logo-strip`. Each has a documented fallback and none blocks a page. If the Component Specialist does not land them, pages are still complete — they lose polish, not content.

**R5 — Photography is the real quality risk.** The reference boards' premium read rests on strong, consistent industrial photography. Every knockout hero depends on the source photo having a usable dark zone for text. If the available imagery is mixed quality, prefer the light hero variant over forcing a knockout at unsafe contrast. Do not compensate by lowering type contrast.

**R6 — The 768–1023px window is the most-missed breakpoint.** Nav toggle is showing, mobile bar is not, splits are still stacked, cards are 2-up. It is called out in both `layout-patterns.md` and `nav.md`; QA should test it explicitly.

## 5. Instructions for page builders (B, C)

**Read in this order:** `component-contracts/band-and-layout.md` (page shell) → `layout-patterns.md` (pick your patterns) → `component-architecture.md` §4 (your page's band order) → the individual contracts for the components you are using.

**Non-negotiables:**

1. Compose only from components in `component-architecture.md` §2. No new class names. No inline `style=`.
2. No `font-size`, `letter-spacing`, `margin` or `padding` literals in HTML. Everything is a token or a utility class.
3. Cascade order `tokens.css` → `base.css` → `components.css`, `site.js` deferred at the end of `<body>`.
4. One `<h1>`, one `.hero`, one `<main id="main">`, one `.footer`, one `.mobile-bar` per page.
5. Every `.band` gets `id` + `aria-labelledby` + a real heading (use `.sr-only` if visually absent).
6. Max two colour-changing bands per page. Whitespace (`--band-y`) separates sections, not colour.
7. Copper appears ≤3× per viewport. One `.btn--primary` per band.
8. Accordion panels and form groups ship **visible**; nav overlay ships **hidden**.
9. Every paragraph over two lines gets `.measure`.
10. Every `<img>` gets `width`, `height` and a spec-bearing `alt`. Every table gets a `<caption>` and `scope` attributes.
11. Unknown facts render `[CLIENT TO CONFIRM]`. Never invent a number.
12. Test 360 / 768 / 1024 / 1280 / 1920 and the 768–1023px window before handing off.

**Copy voice reminder:** sentence case throughout, standards cited by number (IS 807, IS 3177, IS 4137, FEM 9.511), claims traceable to a document or a test. The premium read here comes from specificity, not adjectives.

**Escalate rather than improvise if:** you need a component that is not in the catalogue, a layout the eleven patterns do not cover, a third colour band, or a palette value. Route to the Component Specialist (D) for CSS and to the Orchestrator for R1.

## 6. Verification performed

- All twelve artifacts written to `.agents/artifacts/design-architect/` and re-listed to confirm on disk.
- Every token, class and value quoted was read from `tokens.css`, `base.css` or `components.css` — nothing is from memory. Class inventory cross-checked against the full selector list extracted from both stylesheets.
- Markup skeletons were checked against the live patterns in `03_BUILD/index.html` (hero, trust strip, cards, chips, index rows, stats, spec table) so the examples match what already ships.
- Not verified: rendered output. No page was built or opened in a browser during T001, and the five NEW components have no CSS yet. Contrast figures cited for token pairs come from the design system's own AA claims, not from a measurement I ran — the hero knockout contrast check in particular must be measured against the real photograph at build time.
