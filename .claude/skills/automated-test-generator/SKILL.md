---
name: automated-test-generator
description: Design, write, or improve unit, integration, and regression tests for existing software. Use when adding test coverage, testing boundaries or error paths, or building regression tests; not for diagnosing and fixing the underlying defect (use debug-and-fix).
---

# Automated Test Generator

## Goal
Create deterministic tests that validate requirements and catch meaningful regressions without depending on unrelated external state.

## Workflow
1. Inspect the implementation, public contract, existing test framework, conventions, and relevant defects or requirements.
2. Define behavior under test and expected outcomes before writing test code. If the contract is ambiguous, expose the ambiguity instead of inventing a requirement.
3. Cover the normal path, boundaries, invalid inputs, error handling, and relevant state transitions. Choose cases based on the domain rather than adding arbitrary null tests to every function.
4. Prefer the smallest meaningful test set. Use parameterization or fixtures when it improves clarity.
5. Isolate tests from network, clock, randomness, filesystem, database, and environment dependencies as appropriate; inject or mock them at stable boundaries.
6. For a reported defect, write a regression test that fails for the original defect and passes for the corrected behavior when feasible.
7. Ensure assertions test observable behavior, not implementation details that may change harmlessly.
8. Avoid flaky timing, shared mutable state, order dependence, production credentials, and destructive side effects.
9. Run the narrow test first, then relevant suites and static checks when available. Record exact commands and results.
10. Review test quality: check whether the test would fail if the behavior were broken, whether setup is meaningful, and whether cleanup is reliable.
11. Report coverage gaps honestly. Do not claim full coverage based only on line coverage or test count.

## Rules
- Follow the project's language and framework; examples are illustrative, not universal.
- Do not delete, skip, or weaken a failing test to force green status.
- Do not claim tests ran unless the execution result was observed.
- Do not over-mock the behavior being tested.
- Include security, privacy, authorization, and data-retention cases when relevant to the feature.

## Completion criteria
Tests are readable, deterministic, contract-based, include meaningful boundary/error cases, and have recorded execution status. Any untested behavior or blocked execution is explicit.

## Examples

### Good example 1
Request: “Add tests for a discount calculator.”
Action: test ordinary discounts, zero and full discounts, negative inputs, over-100 percentages, and rounding according to the documented contract.

### Good example 2
Request: “Prevent a regression where a door connected to a wall is lost.”
Action: add a focused test reproducing the original geometry defect, verify it fails before the fix when possible, and run relevant geometry tests afterward.

### Bad example
Request: “Increase test coverage.”
Bad action: add assertions that only check a function returns something and mock the function under test itself.
Why bad: the test count increases without verifying the required behavior.
