# Design Context Package for Page Builders

**For:** Page Builder Alpha & Page Builder Beta
**From:** Orchestrator
**Date:** 2026-07-28

## Quick Reference: Design Direction

### Visual Aesthetic
**Clean Minimal High Quality** — NOT brutalist, NOT loud
- Restrained, precise, expensive-feeling minimalism
- Industrial credibility without heaviness
- Generous whitespace as the primary separator

### Color Palette
- **Base:** Warm concrete `#EFECE6` (primary background)
- **Surface:** Off-white `#FCFBF8` (never pure white)
- **Ink:** Near-black `#0E1418` (text, one emphasis band per page max)
- **Accent:** Copper `#C4531F` (molten metal tie-in, ≤3 times per viewport)

### Typography System
- **Family:** Inter Tight (all weights), IBM Plex Mono (specs only)
- **Display:** `clamp(2.5rem, 5.5vw, 4.5rem)` weight 500-600, sentence case
- **Body:** 15-18px, weight 400, 1.6 line-height
- **micro-caps:** 11px, +0.09em, uppercase, muted (ALL metadata)
- **spec-mono:** IBM Plex Mono for capacity/span/duty data

### Layout Rules
1. **≤3 type sizes visible per viewport**
2. **Accent appears ≤3 times per viewport** (one CTA, one active state, one highlight)
3. **Whitespace separates sections** — ≥96px vertical padding at desktop
4. **≤2 color bands per page** (concrete throughout, ink for one emphasis + footer)
5. **Asymmetric splits preferred** (7/5, 8/4 columns, not endless 6/6 centered)
6. **Hairlines only** — no shadows between sections, no gradients on surfaces
7. **Radii ≤4px, flat surfaces**

### Key Component Patterns (from 15 references)

#### 1. Numbered Index (from IMG_6817)
```
·01  Double Girder EOT Crane
·02  Gantry Crane System
·03  Ladle Handling Crane
```
Large light mono numerals, short labels. No icon bullets.

#### 2. Product Cards (from IMG_6819)
- Portrait aspect ratio
- Cut-out machine overflowing card edge (optional, max 1/page)
- Whole-card subtle hover: border darkens, title → copper, 1px lift
- Hairline above price/spec row

#### 3. Hero Pattern (from IMG_6831 - closest to SVMH subject)
- Crane-against-sky photography
- Large condensed white/light type overlay
- Circular scroll indicator
- NO ghost watermarks (removed in clean minimal)

#### 4. Stat Lockups (from IMG_6820, 6821)
```
20+        100T       IS 807
YEARS    MAX CAPACITY  CERTIFIED
```
Giant numeral + small stacked caption. Clean, no outline-stroke.

#### 5. Spec Tables (from IMG_6825)
- Dotted-leader alignment
- spec-mono for all engineering data
- Hairline grid decoration

#### 6. Process Flow (from IMG_6828)
```
ENQUIRY ▶▶ DESIGN ▶▶ FAT ▶▶ INSTALL ▶▶ AMC
```
Pill-shaped chips with ▶▶ separators

#### 7. Accordion Sections (from IMG_6817)
- Numbered 01-06 rows
- +/− expanders (subtle)
- Clean collapse/expand animation

### Responsive Breakpoints
- **360px** — Mobile base, touch targets ≥44px
- **768px** — Tablet, 2-col grids
- **1024px** — Desktop start
- **1440px** — Optimal desktop
- **1920px** — Wide desktop max

### Hover/Interaction Standards
- **160ms transitions, subtle**
- Border darkens to `hairline-2`
- Title shifts to copper
- 1px lift maximum
- Never whole-card color floods
- 2px copper focus ring for keyboard nav

### Quality Gates (Your Work Must Pass)
✅ Accent used ≤3x per viewport
✅ No decorative type, no ghost watermarks
✅ Vertical padding ≥96px desktop
✅ ≤3 type sizes per viewport
✅ Whitespace-separated sections
✅ At least one asymmetric split per page
✅ All metadata in micro-caps
✅ All engineering data in spec-mono
✅ Hairlines only, zero shadows
✅ Warm neutral backgrounds only
✅ One H1, one primary CTA per page
✅ Responsive 360px-1920px, no horizontal scroll
✅ Valid HTML5, clean CSS

## File References

**Design System:**
- `svmh-v2/01_DESIGN/DESIGN_SYSTEM.md` — base system
- `svmh-v2/01_DESIGN/06_DESIGN_RECALIBRATION.md` — authoritative direction (supersedes)
- `svmh-v2/01_DESIGN/refboards/REFERENCE_DISTILLATION.md` — 15 reference patterns

**Existing Build Foundation:**
- `svmh-v2/03_BUILD/assets/css/tokens.css` — CSS custom properties
- `svmh-v2/03_BUILD/assets/css/base.css` — base styles
- `svmh-v2/03_BUILD/assets/css/components.css` — component library
- `svmh-v2/03_BUILD/assets/js/site.js` — JavaScript behaviors

**Content:**
- `svmh-v2/research/` — company facts, product specs
- `svmh-v2/00_PLAN/03_CONTENT_SEO_MATRIX.md` — page content requirements

## What NOT to Do

❌ Ghost watermarks (removed in clean minimal)
❌ Whole-card color floods on hover
❌ More than 2 color bands per page
❌ Pure white backgrounds (#FFFFFF)
❌ Heavy uppercase display everywhere
❌ Radii >4px
❌ Shadows between sections
❌ Gradients on UI surfaces
❌ Icon bullets (use numbered index)
❌ Multiple accents competing
❌ Centered everything (use asymmetric splits)

## Your Success Criteria

Your pages must:
1. Match the clean minimal aesthetic (not brutalist)
2. Use copper accent ≤3x per viewport
3. Maintain generous whitespace (≥96px sections)
4. Use hairlines as only structural device
5. Present engineering data in spec-mono
6. Work flawlessly 360px-1920px
7. Pass all quality gates above
8. Be production-ready for QA review

---

**Wait for Design Architect's component contracts before building.**
Design Architect (T001) is creating detailed component specifications now.
You'll be notified when specifications are ready for implementation.
