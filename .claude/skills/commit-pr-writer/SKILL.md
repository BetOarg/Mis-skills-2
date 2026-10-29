---
name: commit-pr-writer
description: Draft or improve Git commit messages, pull request titles, descriptions, and release notes that accurately explain a change and its verification.
---

# Commit and PR Writer

## Goal
Produce concise, reviewable change descriptions that match the actual diff and evidence.

## Workflow
1. Inspect the diff, changed files, issue/request, and test/check results. If unavailable, ask for them or draft with clearly stated assumptions.
2. Identify the user-visible or engineering problem, the cause if established, and the intended impact.
3. Choose a concise title. Use the repository's convention; use Conventional Commits only when suitable or requested.
4. Describe what changed and why, including compatibility or migration notes where relevant.
5. List tests and checks with exact status. Separate PASSED, FAILED, PENDING, and NOT RUN; never infer success from the change itself.
6. Include risks, rollout/rollback notes, and linked issue references only when known.
7. Remove vague claims, duplicated details, speculative root causes, and unrelated files.
8. Cross-check every statement against the diff and observed test evidence.
9. For release notes, write from the user's perspective and distinguish shipped behavior from planned work.
10. Return the draft; do not create commits, open PRs, or merge unless separately requested and authorized.

## Rules
- Never invent issue numbers, links, test results, reviewers, or release status.
- Do not say “all tests pass” unless the complete relevant test result is known.
- Keep titles descriptive and action-oriented.
- Preserve sensitive information: do not include tokens, private URLs, customer data, or secrets.
- A PR description should make review easier, not replace code review.

## Suggested PR format
- Summary
- Motivation / issue
- Changes
- Verification (commands and results)
- Risks / compatibility
- Follow-up work

## Examples

### Good example 1
Observed diff fixes expired-token handling and adds two tests; targeted tests passed.
Title: fix(auth): reject expired access tokens
Body: explain the expiry check, regression coverage, and the exact targeted test result.

### Good example 2
The implementation is drafted but tests have not run.
Title: feat(export): add SVG metadata
Body: describe the implementation and explicitly state Tests: NOT RUN; list the required follow-up verification.

### Bad example
Request: “Write a PR description.”
Bad action: claim “CI green” based only on reading the code.
Why bad: it misleads reviewers and can cause an unsafe merge.
