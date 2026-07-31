# SVMH v2 Premium Website Build - Team Manifest

**Project:** High-quality premium website for S.V. Material Handling System Pvt Ltd (EOT/Gantry Crane Manufacturer)
**Build Directory:** `/Users/xoxo/Documents/resreah/sv/svmh-v2/`
**Reference Images:** `/Users/xoxo/Documents/resreah/sv/refer/` (15 high-quality industrial design references analyzed)

## Team Structure

### Orchestrator (Current Session)
**Role:** Route tasks, coordinate between agents, track progress, final quality gates
**Model:** Grok-4.5
**Responsibilities:**
- Task routing and priority decisions
- Cross-agent coordination and handoffs
- Final review and integration
- Quality gate enforcement

### Design Architect (Agent A)
**Role:** High-level design direction, component architecture, layout systems
**Model:** local-claude-opus-5
**Responsibilities:**
- Design system refinement from reference analysis
- Component architecture and hierarchy
- Layout patterns and composition rules
- Typography and spacing systems
**Output:** Design specifications, component contracts, layout blueprints

### Page Builder Alpha (Agent B)
**Role:** Homepage, product listing pages, hero sections
**Model:** local-gpt-5-6-sol
**Responsibilities:**
- Homepage implementation (index.html)
- Product category pages (EOT cranes, gantry systems)
- Hero sections with large knockout typography
- Product card grids matching reference aesthetic
**Output:** Complete HTML pages with inline styles

### Page Builder Beta (Agent C)
**Role:** Detail pages, forms, location pages
**Model:** local-gpt-5-6-sol
**Responsibilities:**
- Product detail pages (double-girder, ladle crane, etc.)
- Request-a-quote form refinement
- Location/facility pages
- Numbered accordion sections
**Output:** Complete HTML pages with inline styles

### Component Specialist (Agent D)
**Role:** Reusable components, JavaScript behaviors, micro-interactions
**Model:** local-claude-opus-5
**Responsibilities:**
- Component library enhancement (components.css)
- JavaScript module refinement (site.js)
- Carousel, accordion, reveal animations
- Mobile navigation and responsive behaviors
**Output:** Enhanced CSS components, refined JS modules

### QA Reviewer (Agent E)
**Role:** Quality assurance, design compliance, accessibility audit
**Model:** local-claude-opus-5
**Responsibilities:**
- Design fidelity check against reference patterns
- Responsive behavior verification (360px-1920px)
- Accessibility audit (WCAG compliance check)
- Performance and asset optimization review
**Output:** Review reports, issue lists, approval/rejection decisions

## Shared Artifacts Directory

`/Users/xoxo/Documents/resreah/sv/svmh-v2/.agents/artifacts/`

### Structure:

> **Historical.** This is the layout as *planned* at kickoff, kept as a record of
> the intended division of labour. It is not the layout on disk today. Two things
> moved during the build and are now owned elsewhere:
>
> - The asset-pipeline scripts left `artifacts/` for `../tools/`, where they
>   derive their own paths and are documented in `tools/README.md`.
> - The `page-builder-alpha` draft pages left `artifacts/` for `../05_DEMO/`,
>   because they use the pre-DNA design system and are not the application.
>
> The empty per-agent directories were removed rather than left as stubs. For the
> current layout, read the tree in the project `README.md`.

```
.agents/
├── team-manifest.md (this file)
├── task-board.json (task state tracking)
├── artifacts/
│   ├── design-architect/
│   │   ├── component-architecture.md
│   │   ├── layout-patterns.md
│   │   └── design-tokens-refined.json
│   ├── page-builder-alpha/
│   │   ├── index.html
│   │   ├── products-overview.html
│   │   └── handoff-notes.md
│   ├── page-builder-beta/
│   │   ├── product-details/
│   │   ├── quote-form.html
│   │   └── handoff-notes.md
│   ├── component-specialist/
│   │   ├── components-enhanced.css
│   │   ├── site-refined.js
│   │   └── module-contracts.md
│   └── qa-reviewer/
│       ├── review-reports/
│       ├── issue-tracker.md
│       └── approval-checklist.md
└── logs/
    └── handoffs.log
```

## Task Lifecycle

```
Inbox → Assigned → In Progress → Review → Done | Needs Revision
```

**State Transitions:**
1. **Inbox:** Task created, awaiting assignment
2. **Assigned:** Routed to specific agent, agent notified
3. **In Progress:** Agent actively working, progress comments required
4. **Review:** Work complete, under QA review
5. **Done:** Approved by reviewer, integrated into main build
6. **Needs Revision:** Reviewer found issues, returned to assigned agent

## Quality Gates

### Gate 1: Design Fidelity
- Matches reference aesthetic (clean minimal industrial editorial)
- Color palette compliance (#E8E8E8, #2B4C7E, white)
- Typography scale and hierarchy correct (Inter Tight + IBM Plex Mono)
- Large knockout typography implemented correctly

### Gate 2: Responsive Behavior
- Mobile-first implementation (360px base)
- Breakpoints at 768px, 1024px, 1440px, 1920px
- Touch targets ≥44px on mobile
- No horizontal scroll at any breakpoint

### Gate 3: Component Quality
- Numbered sections (·01, ·02, ·03) styled correctly
- Product cards with consistent structure
- Accordions expand/collapse smoothly
- Carousels have pagination controls

### Gate 4: Technical Standards
- Valid HTML5 (no unclosed tags, proper nesting)
- CSS follows BEM-like naming conventions
- JavaScript modules isolated and documented
- No console errors in browser

### Gate 5: Accessibility
- Semantic HTML throughout
- ARIA labels on interactive elements
- Keyboard navigation works
- Color contrast ratios meet WCAG AA

## Communication Protocol

### Handoff Format
Every agent handoff includes:
1. **Summary:** What was done (2-3 sentences)
2. **Artifacts:** Exact file paths produced
3. **Verification:** Commands to test/verify
4. **Known Issues:** Incomplete work or technical debt
5. **Next Action:** Clear instruction for next agent

### Progress Comments
Agents must comment at:
- **Start:** "Starting [task], estimated [timeframe]"
- **Blocker:** "Blocked on [issue], need [resolution]"
- **Milestone:** "Completed [component], ready for [next step]"
- **Handoff:** Full handoff format above

### Log File
All handoffs logged to `.agents/logs/handoffs.log` with timestamp and agent ID.

## Design Direction (From Reference Analysis)

### Color Systems
- **Primary:** Cool neutral gray #E8E8E8 (backgrounds)
- **Accent:** Deep navy #2B4C7E (CTAs, headings, highlights)
- **Surface:** White #FFFFFF (cards, overlays)
- **Secondary:** Light gray #F5F5F5 (subtle surfaces)

### Typography Treatments
- **Display:** Inter Tight 600/700, 48-96px, large scale contrast
- **Body:** Inter Tight 400/500, 16-18px, comfortable line height
- **Technical:** IBM Plex Mono 400, 14-16px for specs/data
- **Knockout:** Large white text over industrial photography

### Layout Patterns
- Alternating left-text/right-image compositions
- Floating cards with rounded corners (8-12px) and subtle shadows
- Full-width hero sections with large typography
- Numbered sections with consistent numbering style (·01, ·02, ·03)
- Bento grid product cards
- Generous whitespace and vertical rhythm

### Component Patterns
- Numbered service accordions
- Product carousels with pagination dots
- Structured data tables
- CTA buttons (navy background, white text, rounded)
- Brand logo grids
- Process flow diagrams with arrows

### Photography Style
- Clean product shots on white backgrounds
- Dramatic industrial photography on dark backgrounds
- Technical equipment photography
- 3D rendered products on soft colored backgrounds

## Execution Strategy

### Phase 1: Architecture & Planning (Design Architect)
1. Refine design system based on reference analysis
2. Define component architecture and contracts
3. Create layout pattern library
4. Define responsive behavior rules
**Output:** Design specs ready for builders

### Phase 2: Parallel Build (Builders Alpha + Beta)
1. **Alpha:** Homepage + product overview pages
2. **Beta:** Detail pages + forms + location pages
3. Both use Design Architect's specs
4. Component Specialist supports both with shared components
**Output:** Complete page set

### Phase 3: Integration & Polish (Component Specialist)
1. Refine shared components based on builder needs
2. Enhance JavaScript behaviors
3. Optimize CSS (remove duplicates, consolidate patterns)
4. Implement micro-interactions
**Output:** Polished component library and behaviors

### Phase 4: Quality Assurance (QA Reviewer)
1. Design fidelity audit
2. Responsive behavior testing
3. Accessibility audit
4. Technical standards check
5. Generate issue list
**Output:** Approval or revision requests

### Phase 5: Revision & Finalization (All Agents)
1. Address QA issues
2. Final integration
3. Orchestrator final review
4. Handoff to production
**Output:** Production-ready website

## Success Criteria

✅ All pages match reference aesthetic quality
✅ Responsive 360px-1920px without breaks
✅ All quality gates pass
✅ QA Reviewer approval
✅ Zero console errors
✅ Accessibility audit passes
✅ Ready for client review

---

**Created:** 2026-07-28
**Orchestrator:** Grok Build (current session)
