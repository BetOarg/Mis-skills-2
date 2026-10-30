---
name: debug-and-fix
description: Diagnose and fix a concrete software defect end to end. Use when code fails, tests regress, CI reports a reproducible defect, or behavior differs from requirements. Requires evidence, a minimal safe fix, regression coverage, and final verification.
---

# Debug and Fix

## Goal
Resolve the actual defect, not merely explain it or silence its symptom. Preserve existing architecture and constraints. Finish with evidence of what was changed and what was verified.

## Operating rules
- Work in the repository and branch explicitly selected by the user. Inspect current state before edits.
- Never claim to have opened, modified, tested, committed, pushed, or merged anything unless the corresponding action and result were observed.
- Do not infer green status from a previous run, local result, or a partial workflow.
- Do not broaden scope into unrelated cleanup.
- Prefer the smallest coherent change. Avoid broad rewrites and unrelated formatting.
- Add or update regression tests that reproduce the failure where practical. Do not weaken, delete, or skip a failing test merely to obtain a green result.
- Preserve public interfaces, persistence contracts, data privacy, platform support, localization, and stated architectural constraints.
- If a key fact is unknown, inspect repository evidence. If still unknowable, mark it as unknown rather than inventing it.
- Do not publish, deploy, spend money, delete resources, close issues/PRs, or merge without explicit approval.
- If blocked by permissions, missing tools, unavailable environment, or unclear requirements, state the exact blocker and the smallest next step.

## Workflow
1. **Restate the defect internally** as expected behavior versus observed behavior. Identify the exact failing test, log, screen, or report.
2. **Establish baseline:** inspect branch/status, relevant files, tests, recent changes, and available CI evidence. Do not overwrite user changes.
3. **Reproduce:** run the narrowest relevant test or diagnostic first. Capture the real error and identify the failure path.
4. **Trace cause:** follow inputs, state transitions, persistence/API boundaries, and caller/callee contracts. Distinguish root cause from downstream symptoms.
5. **Plan minimal fix:** name affected files, intended behavior, compatibility risks, and regression test before changing code.
6. **Implement:** make focused changes, keeping the existing architecture unless evidence proves it is the cause.
7. **Test:** run the new regression test and relevant targeted suite; then format, static analysis, and broader tests available in the environment. Record exact commands and outcomes.
8. **Inspect diff:** review every changed line, accidental files, generated files, secrets, and whether the regression test would fail before the fix.
9. **Verify final state:** inspect repository status and actual CI results. If CI cannot run or is pending, say so. Never label the whole task VERDE if a required check is red or unverified.
10. **Report:** summarize root cause, files changed, test evidence, remaining risks, and status.

## Completion criteria
A fix is complete only when:
- The root cause is supported by evidence.
- The code change is scoped and compatible with the stated constraints.
- A meaningful regression test exists or the reason it cannot be added is explained.
- Relevant checks have actually run and their results are reported.
- The final diff and working-tree state have been inspected.
- Any unresolved red/pending/blocking check is clearly visible.

## Status vocabulary
- **VERDE:** required checks passed and final state verified.
- **ROJO:** a required test/check failed.
- **PENDIENTE:** a check has not completed or could not be run.
- **BLOQUEADO:** progress requires access, input, or approval unavailable to the agent.

## Examples

### Good example 1
User: “The wall-drag test fails when a door is connected.”
Action: reproduce the failing test, trace wall/door constraints, add a regression test for the protected door case, make the smallest geometry change, run targeted geometry tests and the broader relevant suite, inspect the diff, and report the exact result.

### Good example 2
User: “The Drift provider loses projects after reload.”
Action: inspect the repository interface and integration test, reproduce with close/reopen, verify transaction and mapping behavior, fix the persistence path without changing the repository contract, and test both reload and rollback behavior.

### Bad example
User: “CI is red.”
Bad action: change several unrelated files, remove the failing test, and announce “all green” because one local command passed.
Why bad: it hides the failure, lacks root-cause evidence, increases regression risk, and misreports verification.

## Feedback-loop quality and debugging depth
Choose the diagnostic method proportionally to the defect:
- For a small, deterministic defect, start with the narrowest failing test or command; do not build an elaborate harness unnecessarily.
- For intermittent, cross-layer, performance, or hard-to-reproduce defects, first create a red-capable feedback loop that exercises the user's actual symptom. Prefer, in order, a regression test, focused HTTP/CLI/browser replay, captured-trace replay, minimal harness, property/fuzz loop, or differential/bisection run.
- Before accepting a loop, state what exact symptom it detects, how to run it, and what makes the result deterministic. If no viable loop can be built, record what was attempted and identify the missing access or artifact; do not present an untested hypothesis as a diagnosis.
- Minimize a reproducer one change at a time. Rank 3–5 falsifiable hypotheses for complex defects and test one variable per probe. For routine defects, do not force this ceremony if the evidence already isolates the cause.
- When a fix is complete, rerun both the minimized regression and the original end-to-end symptom check.

## Regression-test quality
- Test observable behavior through the narrowest public interface that still reproduces the defect; avoid coupling tests to private implementation details.
- Use an independent expected result from a requirement, known-good example, or fixture. Do not derive the expected value using the same logic as the implementation.
- Work in vertical slices: one meaningful failing test, one minimal fix, then repeat. Avoid writing a large batch of speculative tests before understanding the behavior.
- Record a test seam's coverage and limitations. If no suitable seam exists, state that architectural gap instead of adding a misleading shallow test.
- Redact secrets and personal data from logs, traces, screenshots, and captured requests before displaying or storing them.
