# Reference Distillation — `sv/refer/` (16 boards)

Every board in `../../../refer/` was read and reduced to reusable rules. This file is the bridge between "these screenshots look expensive" and "here is what we build".

---

## 1. Board index

| File | Subject | What it contributes |
|---|---|---|
| `IMG_6817.JPG` | Orange framed light card, "SERVICES" + "OUR PRODUCTION" | **Numbered 01–06 accordion index rows** with +/− expanders; horizontal numbered product carousel where the active card is inverted black; dark pill "CONTACT ↗" |
| `IMG_6818.JPG` | ACME® chemicals, industry inner page | **"Pain point × Common solution × Our solution" comparison table** with expandable rows; isometric line-art warehouse hero; 2×2 solution cards with one inverted; resource row (whitepapers / buyer's guide / case studies) with PDF lists + video thumb |
| `IMG_6819.JPG` | Equipment rental catalogue grid | 4-col portrait cards, cut-out machine overflowing the card edge; **whole-card yellow fill as hover state**; hairline above price row; ghost "load more" pill |
| `IMG_6820.JPG` | RM \| Terex, dark | Full-screen uppercase nav overlay; `01/04` slide counters; **giant ghost "3D" numerals behind the machine render**; outline-stroke stat numerals over grey |
| `IMG_6821.JPG` | RM Terex case study, light | **Oversized outline/ghost product name clipped by the product photo** (depth without shadow); 3-up `01/02/03` feature strip with one panel inverted navy; media cards with `date · CATEGORY` micro-caps + `24 ФОТО` footer |
| `IMG_6822.JPG` | «Дело Техники» rental landing | Floating white page container over a darkened site photo; hero headline **split around** the machine cut-out; dashed connector line to a callout tag; `since 2003` inline stat; 3×2 category cards with bottom-pinned secondary button |
| `IMG_6823.JPG` | SKLAD.EXPERT audience bands | **Alternating full-width audience bands** (yellow / black / white), bold uppercase heading + bulleted benefits + deliberately small CTA, machine cut-outs overhanging the colour block |
| `IMG_6824.JPG` | SKLAD.EXPERT presentation | Zig-zag left/right section rhythm ×5; ghost "ПРЕДЛАГАЕМ" watermark; right-rail dot pagination; undersized accent CTA with download glyph |
| `IMG_6825.JPG` | Renault Sport F1 concept | Diagonal black/yellow split; ghost "TEAM" watermark behind "DRIVERS"; **two-column spec/stat lists with dotted leader alignment** |
| `IMG_6826.JPG` | RM Terex case, continued | Asymmetric navy 55% / white 45% intro split holding only a label + 3-line paragraph; full-width grey product stage with white watermark type and `01 — 03` counter; strict 12-col with visible band boundaries, zero radii, zero shadows |
| `IMG_6827.JPG` | SwiftCargo freight | **Nav-as-grid**: bar split by 1px vertical dividers into cells, right-most cell solid red holding `Hire us →`; one saturated object (red container) as the only colour; 3-up numbered service cards with no boxes, hairlines only; **inline calculator with label-less underline inputs** → flat solid CTA; mono logo strip in hairline cells |
| `IMG_6828.JPG` | Ampera, dark editorial | Vertical rotated words; **pill-shaped process chips with ▶▶ separators** (WAREHOUSING → FULFILLMENT → …); massive overlapping "SERVICES" wordmark over photo; hand-drawn circle annotation |
| `IMG_6829.JPG` + `D3EBE31D…GIF` | Extreme/Exciting Sports card system | Two-card diagonal stack with a translucent top card; subject **breaking the frame**; giant date numeral + small stacked caption lockup; `»»»` next-slide button; template-driven carousel slides |
| `IMG_6831.JPG` | Influence Pro Trading, dark | GOAL / RESULT laurel columns; gigantic "ABOUT PROJECT" grey type with the subject overlapping it; crane boom against sky hero with huge condensed white wordmark; **orange circular ↘ scroll button**; underlined nav |
| `IMG_6832.JPG` | gola.io / ARKITECT | Light stacked project panels in tinted gradients; centred pill nav |

## 2. The fourteen rules we adopt

1. **Two-colour discipline.** One neutral base plus exactly one saturated accent. For SVMH: warm concrete `#EFECE6` / near-black `#0E1418` + copper `#C4531F`. Never two accents competing.
2. **Ghost watermark headline.** Oversized display word at 5–8% contrast behind the hero object; the object occludes the letters. Free depth, zero effects. Decorative only — never carries unique information.
3. **Cut-outs break the frame.** Product renders are background-free and overflow their container edge. Nothing is fully boxed in.
4. **3–4× type jump.** Heavy uppercase display with tight-to-negative tracking against 15px light body at 1.6 line-height. No mid-tier heading blurring the two.
5. **micro-caps carries all metadata.** 11px, +0.09em, uppercase, muted — for dates, categories, prices, counters, captions, eyebrows. One style, used everywhere.
6. **Numbered index, not icons.** `01 / 02 / 03` large light mono numerals beside short labels replaces bullet icons and accordion chevrons.
7. **Full-bleed bands are the section separator.** Alternate concrete → white → ink → concrete-2 → copper. No decorative dividers, no drop shadows between sections.
8. **Hairline grid as decoration.** 1px dividers between equal cells — nav bar, 3-up service rows, logo strips, spec tables. The grid itself is the ornament.
9. **Consistent card anatomy.** micro-caps index + uppercase title top → cut-out centre → body-s description → hairline → bottom-pinned ghost button or spec row.
10. **Whole-card hover.** The entire card fills with accent and inverts its text. Never a small button shifting colour.
11. **CTAs are deliberately small.** Flat rectangles, 0–4px radius, tiny uppercase label, arrow or download glyph. Understated next to a 96px headline is the point.
12. **Stat lockup as the proof unit.** Giant numeral + small stacked caption to its right (`20 YRS`, `100 T MAX`, `SINCE 2006`). Solid on light bands, outline-stroke over imagery.
13. **Minimal, edge-anchored motion.** Right-rail dot pagination, `01 — 03` counters, `»»»` next, circular scroll button, dashed connector lines to callout tags. Nothing bounces.
14. **Depth by layering, not effects.** Offset/translucent stacked panels, blurred photo backdrop behind a floating container, soft ground shadow, props outside the frame.

## 3. What we explicitly reject

| Rejected | Why |
|---|---|
| Hero carousel / rotating messages | Kills LCP and dilutes the CTA (flagged in every audit) |
| Product-in-void studio shots as hero | "Product-in-use" is the premium signal; a crane must be lifting something |
| Serif display type | The v1 Cormorant Garamond reads editorial-luxury; this is heavy engineering |
| Radii above 8px, soft gradients, glassmorphism | The Extreme Sports boards are consumer-editorial — we take their *layering logic*, not their surface treatment |
| Mixed icon styles | ElectroMech's mixed grid is the cautionary case. One line-icon system, one stroke weight |
| Decorative floating geometry | The SKLAD diamonds/rings work for a logistics brand; on a safety-critical crane site they undercut credibility |

## 4. Mapping boards → SVMH sections

| Board pattern | Lands on |
|---|---|
| Numbered 01–06 accordion (6817) | Home "How we deliver" · Services pillar · IS 3177 RFQ checklist |
| Pain × Common × Our solution table (6818) | Industry pages · TCO / "why not the cheap quote" block |
| Resource row with PDF lists + video (6818) | `/downloads` · product-page datasheet block |
| Whole-card accent hover grid (6819) | Products index · spares catalogue |
| Ghost numerals + outline stats (6820, 6821) | Home proof band · case-study hero |
| Headline split around cut-out (6822) | Home hero · product money-page hero |
| Alternating audience bands (6823) | Home three-door section (New Cranes / Spares / AMC) |
| Dotted-leader spec lists (6825) | Product spec tables · duty-class readouts |
| Asymmetric dark/light intro split (6826) | Case-study Situation / Task / Solution |
| Nav-as-grid + accent CTA cell (6827) | Global header |
| Inline underline-input calculator (6827) | RFQ step form · Phase 3 calculators |
| Process chips with ▶▶ (6828) | "Enquiry → Design → FAT → Install → AMC" journey |
| Crane-against-sky hero + circular scroll (6831) | Home hero (SVMH's actual product is literally this) |
| Laurel GOAL / RESULT columns (6831) | Case-study outcome block |

`IMG_6831.JPG` is the closest analogue to SVMH's own subject matter — a crane boom against open sky with condensed white type over it. That board is the primary art-direction target for the home hero.
