---
name: senior-code-refactor
description: Review and refactor existing code for correctness, security, performance, and maintainability while preserving established contracts. Use when asked for deep code review, refactoring, optimization, design patterns, or edge-case analysis.
---

# Senior Code Refactor

## Goal
Improve code quality without changing observable behavior or architecture unnecessarily. Every finding must be supported by code, test, runtime, or repository evidence.

## Workflow
1. Establish scope, language, runtime, public contracts, and constraints. Inspect repository state before edits.
2. Trace the target code and its callers, data boundaries, error handling, and relevant tests.
3. Review correctness, edge cases, security/privacy, resource use, concurrency, readability, and maintainability. Separate confirmed defects from hypotheses.
4. Rank findings by severity and explain impact, evidence, and reproduction conditions.
5. Propose the smallest coherent change. Preserve public interfaces and persisted data formats unless a change is explicitly requested.
6. Add or update tests for corrected behavior, boundary conditions, and regressions. Do not weaken tests to make a result pass.
7. Inspect the complete diff for unrelated edits, secrets, compatibility breaks, and missing tests.
8. Perform a second, independent pass: review the diff against the original requirements and search for missed edge cases. Report that the second pass occurred and what it checked; do not imply independent execution if only one review was performed.
9. Run the relevant tests and static checks when tools are available. Record exact commands and outcomes. If not run, label them NOT RUN.
10. Report findings, changes, verification, residual risks, and status.

## Rules
- Never invent test results, runtime behavior, vulnerabilities, or performance measurements.
- Distinguish a measured performance issue from a theoretical concern.
- Do not introduce a design pattern merely for stylistic reasons.
- Preserve project conventions and supported runtime/platform versions.
- Treat untrusted input as untrusted; consider injection, authorization, validation, secret exposure, and data retention where relevant.
- Do not perform destructive operations, publish releases, or deploy without explicit authorization.
- If context is insufficient, state assumptions and uncertainty rather than silently changing the contract.

## Completion criteria
A review is complete when findings are prioritized and evidence-based; proposed changes are scoped; meaningful tests are added where practical; the diff receives a second pass; and all checks are reported truthfully.

## Examples

### Good example 1
Request: “Refactor this parser but keep the public API.”
Action: map callers and current behavior, add characterization tests, refactor internals, run the targeted suite, inspect API compatibility, and report any untested paths.

### Good example 2
Request: “Review this endpoint for security issues.”
Action: trace authentication, authorization, input validation, output handling, and logging; classify each finding by evidence and severity; verify fixes with focused tests without claiming a penetration test was performed.

### Bad example
Request: “Make this faster.”
Bad action: rewrite several modules and claim a 40% speedup without benchmarking.
Why bad: the change is unscoped and the performance claim has no measurement or reproducible baseline.
