# SVMH v2 Premium Build — Loop Workflow

**Loop Type:** Multi-agent orchestrated build with quality gates
**Orchestrator:** Grok Build (main session)
**Execution Mode:** Sequential phases with parallel execution within phases

## Loop Structure

### Phase 1: Architecture (Sequential)
**Agent:** Design Architect (local-claude-opus-5)
**Duration:** ~45-60 min
**Output:** Component specs, layout patterns, contracts

```
START → Design Architect (T001) → Handoff → Phase 2
```

### Phase 2: Parallel Build (Concurrent)
**Agents:** 
- Page Builder Alpha (local-gpt-5-6-sol) — Homepage & product pages
- Page Builder Beta (local-gpt-5-6-sol) — Detail pages & forms
**Duration:** ~90-120 min each
**Output:** Complete HTML pages

```
Design Specs → [Builder Alpha (T002) | Builder Beta (T003)] → Handoff → Phase 3
```

### Phase 3: Integration & Polish (Sequential)
**Agent:** Component Specialist (local-claude-opus-5)
**Duration:** ~60-90 min
**Output:** Refined components, enhanced JS behaviors

```
Built Pages → Component Specialist (T004) → Handoff → Phase 4
```

### Phase 4: Quality Assurance (Sequential)
**Agent:** QA Reviewer (local-claude-opus-5)
**Duration:** ~45-60 min
**Output:** Review report, issue list, approval/rejection

```
Polished Build → QA Reviewer (T005) → Handoff → Phase 5
```

### Phase 5: Revision & Finalization (Conditional Loop)
**Coordinator:** Orchestrator
**Duration:** ~30-45 min
**Output:** Production-ready build

```
IF issues found:
  Route to appropriate agent → Fix → Return to QA
ELSE:
  Final integration → Handoff to client
```

## Quality Gates

Each phase must pass gates before next phase starts:

### Gate 1: Architecture Complete
- [ ] Component architecture document exists
- [ ] Layout pattern library documented
- [ ] Typography system specified
- [ ] Component contracts ready
- [ ] Handoff notes written

### Gate 2: Pages Built
- [ ] All assigned pages complete
- [ ] HTML valid (no unclosed tags)
- [ ] Responsive 360px-1920px
- [ ] Design aesthetic matches specs
- [ ] Handoff notes from both builders

### Gate 3: Components Polished
- [ ] Shared components refined
- [ ] JavaScript behaviors smooth
- [ ] No console errors
- [ ] CSS optimized (duplicates removed)
- [ ] Handoff notes written

### Gate 4: QA Approved
- [ ] Design fidelity audit passed
- [ ] Responsive testing passed
- [ ] Accessibility audit passed
- [ ] Technical standards verified
- [ ] Approval decision documented

### Gate 5: Production Ready
- [ ] All P0/P1 issues resolved
- [ ] Final integration complete
- [ ] Client handoff docs ready
- [ ] Build verified in browser

## Loop Monitoring

### Progress Tracking
Task board JSON updated at each transition:
- `inbox` → `assigned` (when agent spawned)
- `assigned` → `in_progress` (when agent starts work)
- `in_progress` → `review` (when handoff submitted)
- `review` → `done` | `needs_revision` (after QA check)

### Health Checks
Orchestrator checks every 5 minutes:
- Are agents stuck (no progress >30 min)?
- Are handoffs logged properly?
- Are artifacts appearing in expected paths?
- Are quality gates being met?

### Escalation Rules
1. **Agent silent >30 min:** Check output, consider restart
2. **Quality gate failed twice:** Escalate to orchestrator decision
3. **Blocker reported:** Orchestrator intervenes immediately
4. **Task exceeds 2x estimated duration:** Review scope or assist

## Success Metrics

**Loop completes successfully when:**
1. All 6 tasks in task-board.json marked `done`
2. All 5 quality gates passed
3. QA Reviewer approval documented
4. Production build verified in browser
5. Zero P0/P1 issues outstanding

**Estimated Total Duration:** 4-6 hours (with parallel execution)

## Abort Conditions

Loop aborts if:
- Same agent fails same task 3x
- Critical blocker unresolved >2 hours
- Quality gate failure with no path forward
- User manual abort command

---

**Status:** Phase 1 in progress (Design Architect working on T001)
**Next:** Wait for T001 completion → spawn Phase 2 parallel builders
