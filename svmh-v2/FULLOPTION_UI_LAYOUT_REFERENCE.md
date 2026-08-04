# Full Option Craft Reno - UI Layout Reference
## Visual ASCII Wireframe Analysis

This document shows the exact UI layout structure of fulloptioncraftreno.ca for reference and adaptation.

---

## 📐 NAVIGATION BAR (Fixed/Sticky)

```
┌─────────────────────────────────────────────────────────────────────┐
│  [LOGO]                                    HOME  ABOUT  SERVICES    │
│  Full Option                               PROJECTS  CONTACT   [≡]  │
│  Craft                                     [SUBMIT INQUIRY Button]  │
└─────────────────────────────────────────────────────────────────────┘
```

**Layout Notes:**
- Logo: Left-aligned, stacked text (company name)
- Navigation: Right-aligned horizontal menu
- CTA Button: Primary button with border/outline style
- Mobile: Hamburger menu (≡)

---

## 🎯 HERO SECTION (Full-Width)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                       │
│                    [LARGE BACKGROUND IMAGE]                          │
│                                                                       │
│     ┌─────────────────────────────────┐                             │
│     │                                  │                             │
│     │  Large Headline Text             │                             │
│     │  "Reliable Service for           │                             │
│     │   Home owners"                   │                             │
│     │                                  │                             │
│     │  [CTA Button]                    │                             │
│     │                                  │                             │
│     └─────────────────────────────────┘                             │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**Layout Notes:**
- Full-viewport height background image
- Text container: Left-aligned, ~40% width
- Large display typography
- Single prominent CTA button

---

## 📊 SERVICES GRID SECTION (3-Column Cards)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                       │
│                    "Excellence in Execution"                         │
│                         Section Heading                              │
│                                                                       │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐ │
│  │                  │  │                  │  │                  │ │
│  │ [Number] 01 /    │  │ [Number] 02 /    │  │ [Number] 03 /    │ │
│  │                  │  │                  │  │                  │ │
│  │ Service Title    │  │ Service Title    │  │ Service Title    │ │
│  │                  │  │                  │  │                  │ │
│  │ Short description│  │ Short description│  │ Short description│ │
│  │ about the service│  │ about the service│  │ about the service│ │
│  │ offering...      │  │ offering...      │  │ offering...      │ │
│  │                  │  │                  │  │                  │ │
│  │ [→ Learn More]   │  │ [→ Learn More]   │  │ [→ Learn More]   │ │
│  │                  │  │                  │  │                  │ │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘ │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**Layout Notes:**
- 3-column equal-width grid
- Numbered prefixes (01 / 02 / 03)
- Minimal card design (no heavy borders)
- Text-based with subtle hover effects
- "Learn More" link at bottom of each card

---

## 🖼️ PROJECT SHOWCASE (Full-Width Image Grid)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                       │
│                         "Recent Projects"                            │
│                                                                       │
│  ┌───────────────────────────┐  ┌───────────────────────────┐      │
│  │                           │  │                           │      │
│  │   [PROJECT IMAGE 1]       │  │   [PROJECT IMAGE 2]       │      │
│  │                           │  │                           │      │
│  │   Project Title           │  │   Project Title           │      │
│  │   Short description       │  │   Short description       │      │
│  │                           │  │                           │      │
│  └───────────────────────────┘  └───────────────────────────┘      │
│                                                                       │
│  ┌───────────────────────────┐  ┌───────────────────────────┐      │
│  │                           │  │                           │      │
│  │   [PROJECT IMAGE 3]       │  │   [PROJECT IMAGE 4]       │      │
│  │                           │  │                           │      │
│  │   Project Title           │  │   Project Title           │      │
│  │   Short description       │  │   Short description       │      │
│  │                           │  │                           │      │
│  └───────────────────────────┘  └───────────────────────────┘      │
│                                                                       │
│                    [View All Projects Button]                        │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**Layout Notes:**
- 2-column grid layout
- Large image thumbnails
- Overlay text on hover
- Project title + description below image
- Centered "View All" CTA button

---

## 📝 CONTENT SECTION (Split Layout - Image + Text)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                       │
│  ┌──────────────────────────┐   ┌───────────────────────────────┐  │
│  │                          │   │                               │  │
│  │                          │   │  Section Heading              │  │
│  │   [LARGE IMAGE]          │   │                               │  │
│  │                          │   │  Paragraph text describing    │  │
│  │                          │   │  the service or feature in    │  │
│  │                          │   │  detail. Multiple lines of    │  │
│  │                          │   │  body copy explaining the     │  │
│  │                          │   │  value proposition.           │  │
│  │                          │   │                               │  │
│  └──────────────────────────┘   │  • Bullet point 1             │  │
│                                  │  • Bullet point 2             │  │
│                                  │  • Bullet point 3             │  │
│                                  │                               │  │
│                                  │  [CTA Button]                 │  │
│                                  │                               │  │
│                                  └───────────────────────────────┘  │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**Layout Notes:**
- 50/50 split (or 40/60) layout
- Image on left, content on right
- Can alternate: content left, image right
- Ample whitespace
- Optional bullet list for features

---

## 💬 TESTIMONIALS / SOCIAL PROOF

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                       │
│                      "What Clients Say"                              │
│                                                                       │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                                                               │  │
│  │  "Quote text from client testimonial. Lorem ipsum dolor      │  │
│  │   sit amet, consectetur adipiscing elit. Excellent work      │  │
│  │   and professional service throughout the project."           │  │
│  │                                                               │  │
│  │                                    — Client Name              │  │
│  │                                      Project Type             │  │
│  │                                                               │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                       │
│                       [← Previous]  [Next →]                         │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**Layout Notes:**
- Centered testimonial card
- Large quote typography
- Client name + title below
- Navigation arrows for carousel

---

## 📧 CONTACT / CTA SECTION (Full-Width)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                       │
│                   [BACKGROUND COLOR OR IMAGE]                        │
│                                                                       │
│               "Ready to Start Your Project?"                         │
│                                                                       │
│          Supporting text encouraging visitors to reach out           │
│                                                                       │
│                      [SUBMIT INQUIRY Button]                         │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**Layout Notes:**
- Full-width section
- Centered content
- Large heading
- Single prominent CTA button
- High contrast background

---

## 🔽 FOOTER (Multi-Column Layout)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌─────────┐│
│  │              │  │              │  │              │  │         ││
│  │ [LOGO]       │  │ Menu         │  │ Inquiries    │  │ Social  ││
│  │              │  │              │  │              │  │         ││
│  │ Full Option  │  │ • Home       │  │ 123-456-7890 │  │ LinkedIn││
│  │ Craft        │  │ • About      │  │              │  │         ││
│  │              │  │ • Services   │  │ info@site.ca │  │ Instagram││
│  │              │  │ • Projects   │  │              │  │         ││
│  │              │  │ • Contact    │  │ 500 Terry St │  │ Facebook││
│  │              │  │              │  │ San Francisco│  │         ││
│  │              │  │              │  │              │  │         ││
│  └──────────────┘  └──────────────┘  └──────────────┘  └─────────┘│
│                                                                       │
│  ─────────────────────────────────────────────────────────────────  │
│                                                                       │
│         © 2023 Full Option Craft  |  Privacy Policy  |  Terms       │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**Layout Notes:**
- 4-column grid layout
- Logo + Company name (Column 1)
- Navigation links (Column 2)
- Contact information (Column 3)
- Social media links (Column 4)
- Bottom copyright bar

---

## 🎨 DESIGN PATTERNS SUMMARY

### Typography Hierarchy
```
H1 (Hero):        ~72px, bold, high contrast
H2 (Section):     ~48px, medium weight
H3 (Card Title):  ~24px, medium weight
Body:             ~16px, regular weight
Small/Meta:       ~14px, light weight
```

### Color Scheme (Approximate)
```
Primary:       Dark charcoal/black (#3F3F3F)
Secondary:     Light gray for backgrounds
Accent:        Minimal accent color
Text:          Dark on light, high contrast
Borders:       Very subtle or none
```

### Spacing System
```
Section padding:  80-120px top/bottom
Card gaps:        24-32px
Element spacing:  16-24px between elements
Container:        Max-width ~1200px, centered
```

### Card Design Pattern
```
- Minimal borders (or borderless)
- Hover effects: subtle background change
- Number prefixes: "01 / " style
- Left-aligned text
- Clean, modern aesthetic
```

### Button Styles
```
Primary:   Solid background, contrasting text
Secondary: Outline/border style, transparent bg
Icon:      Arrow → or ↗ after text
Hover:     Transform/scale or color shift
```

---

## 🔄 KEY LAYOUT PRINCIPLES TO ADOPT

1. **Grid-First Approach**: Consistent 2-column and 3-column grids
2. **Generous Whitespace**: Large padding between sections
3. **Number Prefixes**: "01 / 02 / 03" pattern for ordered items
4. **Minimal Borders**: Clean, borderless card designs
5. **Hover Interactions**: Subtle background changes on cards
6. **Full-Width Sections**: Alternating contained/full-width layouts
7. **Image-Heavy**: Large, high-quality project images
8. **Typography Scale**: Clear hierarchy with size jumps
9. **Centered CTAs**: Important buttons centered in their containers
10. **Responsive Grid**: Auto-fit columns that stack on mobile

---

## 📋 SECTIONS CHECKLIST FOR SVMH SITE

Which sections from Full Option Craft should we adapt for SVMH?

- [ ] Hero section with full-width image background
- [ ] 3-column services grid with number prefixes
- [ ] Project showcase image grid (2-column)
- [ ] Split content sections (image + text)
- [ ] Testimonials carousel
- [ ] Full-width CTA section
- [ ] Multi-column footer layout
- [ ] Numbered card pattern ("01 / Service Name")
- [ ] Hover effects on cards
- [ ] Minimal border design system

---

**Next Steps:**
1. Review this layout analysis
2. Identify which specific sections you want to implement
3. I'll create the HTML/CSS code to match these layouts for your SVMH website

