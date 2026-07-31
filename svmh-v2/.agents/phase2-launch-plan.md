# Phase 2 Parallel Builder Launch Plan

## Pre-Launch Checklist

**Before spawning builders, verify:**
- [x] Design Architect T001 complete
- [ ] Component architecture document exists at `.agents/artifacts/design-architect/component-architecture.md`
- [ ] Layout patterns documented at `.agents/artifacts/design-architect/layout-patterns.md`
- [ ] Typography system specified at `.agents/artifacts/design-architect/typography-spacing-system.md`
- [ ] Component contracts available at `.agents/artifacts/design-architect/component-contracts/`
- [ ] Design Architect handoff notes at `.agents/artifacts/design-architect/handoff-notes.md`

## Builder Alpha Launch (T002)

**Model:** local-gpt-5-6-sol
**Task:** Homepage & Product Overview Pages
**Input Artifacts:**
- Design context package
- Design Architect specifications
- Existing tokens.css, base.css, components.css
- Research content from svmh-v2/research/

**Pages to Build:**
1. `index.html` — Homepage with hero, features, products sections
2. `eot-cranes/index.html` — EOT cranes overview
3. `gantry-cranes/index.html` — Gantry systems overview

**Key Requirements:**
- Large knockout typography in hero
- Numbered features grid (·01, ·02, ·03)
- Product card layouts matching reference aesthetic
- Copper accent ≤3x per viewport
- Clean minimal style (not brutalist)

## Builder Beta Launch (T003)

**Model:** local-gpt-5-6-sol
**Task:** Product Detail Pages & Forms
**Input Artifacts:**
- Design context package
- Design Architect specifications
- Existing page templates as reference
- Product specs from research/

**Pages to Build:**
1. `eot-cranes/ladle-crane.html` — Ladle handling crane detail page
2. `industries/foundry.html` — Foundry industry page
3. Refine `request-a-quote.html` — Enhanced form UX
4. Additional location pages if time permits

**Key Requirements:**
- Numbered accordion sections for specs
- Structured data tables with dotted leaders
- Form validation and progressive disclosure
- Responsive behavior 360px-1920px
- spec-mono for all engineering data

## Coordination Protocol

### Shared Resources
Both builders access:
- `.agents/artifacts/design-context-package.md`
- `.agents/artifacts/design-architect/*` (all specs)
- `svmh-v2/03_BUILD/assets/css/*`
- `svmh-v2/03_BUILD/assets/js/site.js`

### Output Isolation
- Alpha outputs to: `.agents/artifacts/page-builder-alpha/`
- Beta outputs to: `.agents/artifacts/page-builder-beta/`
- No cross-builder file conflicts

### Handoff Requirements
Each builder must produce:
1. Complete HTML files (valid, production-ready)
2. Handoff notes with:
   - What was built (page list)
   - Where files are (exact paths)
   - How to verify (browser test instructions)
   - Known issues or technical debt
   - Recommendations for Component Specialist

### Progress Monitoring
Orchestrator checks every 10 minutes:
- Are both builders progressing?
- Are artifacts appearing in expected paths?
- Any blockers reported?
- Estimated time to completion?

## Launch Sequence

```bash
# 1. Verify Design Architect completion
check T001 artifacts exist

# 2. Update task board
T002: inbox → assigned
T003: inbox → assigned

# 3. Spawn builders in parallel
spawn Builder Alpha (T002) with design specs
spawn Builder Beta (T003) with design specs

# 4. Log handoffs
echo timestamp | ORCHESTRATOR | Phase 2 launched | Alpha + Beta parallel

# 5. Monitor progress
wait for both builders to complete or report blockers

# 6. Gate check before Phase 3
verify all pages built
verify HTML valid
verify responsive
verify design compliance
```

## Success Criteria for Phase 2

**Builder Alpha Success:**
- Homepage complete and visually matches clean minimal aesthetic
- Product overview pages functional
- Hero sections with proper typography scale
- Numbered features grid implemented
- Product cards with subtle hover states
- Responsive without breaks

**Builder Beta Success:**
- Detail pages complete with accordion specs
- Form UX improved with validation
- Industry page with comparison tables
- All engineering data in spec-mono
- Responsive and accessible
- Clean handoff to Component Specialist

**Gate 2 Pass Conditions:**
- All assigned pages exist and are complete
- HTML validates (no unclosed tags, proper nesting)
- Responsive 360px-1920px verified
- Design aesthetic matches specifications
- Both handoff notes submitted
- No critical blockers remaining

---

**Ready to launch when Design Architect completes T001**
