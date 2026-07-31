# 06 — Design Recalibration: Clean Minimal

**Status:** supersedes the tone of `DESIGN_SYSTEM.md` where the two conflict. Tokens in `tokens/tokens.json` stay valid; what changes is *how loudly* they are used.

**Client direction, verbatim:** "use like clean minimal high qty design".

The v1 recalibration in `DESIGN_SYSTEM.md` aimed at heavy-industry brutalism — monumental type, ghost watermarks, whole-card colour floods. That direction is defensible for the subject matter but it is not what was asked for. This document retunes it to restrained, precise, expensive-feeling minimalism without discarding the industrial credibility.

---

## 1. What changes

| Dimension | Was (brutalist) | Now (clean minimal) |
|---|---|---|
| Display type | `clamp(3.5rem, 9vw, 8.5rem)` weight 800 uppercase | `clamp(2.5rem, 5.5vw, 4.5rem)` weight 500–600, **sentence case** for H1/H2 |
| Type families | Archivo Expanded / Anton heavy | **Inter Tight** or Inter, one family, tight tracking. Mono kept for specs only |
| Ghost watermarks | Present in every hero | **Removed.** Decorative type is the first thing to go |
| Accent usage | CTAs, active states, whole-card floods, niche flags | **Accent appears 2–3 times per viewport, maximum.** One CTA, one active state, one data highlight |
| Card hover | Entire card floods copper | Border darkens to `hairline-2`, title shifts to copper, 1px lift. That is all |
| Section separator | Full-bleed colour bands alternating five ways | **Whitespace is the separator.** Colour bands used ≤2 times per page, for genuine emphasis |
| Band sequence | concrete → white → ink → concrete-2 → copper | `concrete` throughout, with `ink` for exactly one band + the footer |
| Vertical rhythm | `clamp(64px, 9vw, 144px)` | `clamp(96px, 11vw, 180px)` — **more air, not less** |
| Cut-outs breaking frames | Required | Optional, and never more than once per page |
| Stat lockups | Giant numerals, outline-stroke over photos | Numerals at `display-l` scale, thin weight, on a plain hairline grid |
| Imagery | Cinematic, heavily overlaid | Bright, clean, generous margin around the subject. Overlay only where text sits on top |

## 2. What stays

These earned their place from the research, not from the reference boards, so they survive the retune:

- **Warm neutral base.** `concrete #EFECE6` and `white #FCFBF8`. Never pure white — it is the single cheapest tell of a template.
- **Single accent, copper `#C4531F`.** Molten metal, tied to the ladle/foundry niche. Now used sparingly.
- **Hairlines as the only structural device.** No shadows between sections, no gradients on UI surfaces.
- **micro-caps for every piece of metadata.** Consistency here is most of the perceived quality.
- **`spec-mono` for capacity / span / duty.** Engineering data must look like engineering data.
- **Numbered index rows** instead of icon bullets — minimal by nature, keep them.
- **Trust strip above the first fold break.** Now hairline-bordered on `concrete` rather than a solid ink slab.
- **Radii ≤ 4px, flat surfaces.**
- **Every accessibility rule.** Non-negotiable regardless of aesthetic.

## 3. The minimal quality bar

What separates expensive minimal from empty minimal:

1. **Optical alignment over mathematical.** Hairlines and text edges line up to the eye.
2. **One idea per band.** If a section is doing two jobs, split it.
3. **Restraint in weight, generosity in space.** Thin type with a lot of room reads as confident. Heavy type crammed in reads as loud.
4. **Data as decoration.** A capacity table, set precisely, is the ornament. Nothing else is needed.
5. **Asymmetry, deliberately.** 7/5 and 8/4 column splits, not endless centred 6/6. Centred everything is the second cheapest tell.
6. **No more than three type sizes visible in any one viewport.**
7. **Hover states are 160ms and barely there.** If a hover announces itself, it is wrong.

## 4. Revised QA checklist

Replaces §8 of `DESIGN_SYSTEM.md`.

- [ ] Accent appears ≤3 times in any viewport
- [ ] No decorative type anywhere; no ghost watermarks
- [ ] Vertical band padding ≥96px at desktop
- [ ] ≤3 type sizes visible per viewport
- [ ] Whitespace separates sections; ≤2 colour bands per page
- [ ] At least one asymmetric column split per page
- [ ] All metadata in micro-caps, no exceptions
- [ ] All engineering data in spec-mono
- [ ] Hairlines only; zero shadows between sections
- [ ] Hover states ≤160ms and subtle
- [ ] Radii ≤4px, no gradients on UI surfaces
- [ ] Backgrounds warm neutral, never `#FFFFFF`
- [ ] One H1, one primary CTA per page
- [ ] Trust strip above the first fold break
- [ ] Keyboard path complete, 2px copper focus ring visible
- [ ] Every image alt text carries capacity, span, industry
- [ ] Unique title + meta description
- [ ] 360px → 1920px with no horizontal scroll

## 5. Note on the reference image

The client attached a reference image with this direction. It did not transmit — no image data reached the agent and no matching file was found on disk. This recalibration is derived from the written instruction alone. **If the attached reference shows something materially different, this document is the thing to correct first**, before any further page work; the token file and the page specs are unaffected.
