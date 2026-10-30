---
name: evidence-verifier
description: Independently verify claims about files, commits, tests, CI, deployments, records, and external actions against authoritative evidence. Use when a user asks whether work is really done, requests an audit, or before reporting completion. Not for performing the underlying repair or treating plans and screenshots as proof of unrelated outcomes.
---
# Evidence Verifier

## Mission
Prevent false completion claims by checking each important statement against evidence appropriate to that claim.

## Verification workflow
1. Convert each completion claim into a falsifiable assertion with target, expected state, and relevant time/commit.
2. Identify the authoritative source: repository tree/file/commit, CI run and jobs, test output, release artifact, or external system record.
3. Query the source directly using available authorized tools. Prefer immutable identifiers (SHA, run ID, artifact ID, record ID) over labels.
4. Verify identity and scope: repository, branch, commit, environment, platform, version, and time window must match the claim.
5. Check the full result, not just a summary badge: inspect failed/skipped/cancelled jobs, test totals, warnings, artifacts, and required gates where available.
6. Distinguish evidence levels:
   - source inspected;
   - static validation passed;
   - automated test executed and passed;
   - behavior manually verified;
   - external action confirmed in its destination.
7. Record source, identifier, observation, limitations, and conclusion for every material claim.
8. If evidence is missing, stale, contradictory, or outside scope, mark PENDIENTE or ROJO as appropriate. Never fill gaps with assumptions.
9. Re-check after a repair or merge using the new target SHA. Do not reuse old green results for a new commit.
10. Report concise findings and the exact next evidence needed.

## Claim-specific rules
- File exists: inspect the exact path on the claimed ref.
- Commit integrated: inspect target branch history or compare refs; PR state alone may be insufficient.
- CI green: verify run conclusion and required jobs for the exact SHA.
- Tests passed: verify command, environment, exit code, and test summary.
- Published/deployed/sent/paid: verify the destination system's resulting record; a successful API request alone may not prove final availability.
- Security/privacy: distinguish configuration inspection from a complete security audit.

## Good examples
### Good example 1
Claim: “CI is green after merge.”
Action: query the run associated with the merge SHA, inspect all jobs, and confirm conclusion success before marking VERDE.
### Good example 2
Claim: “The skill is in main.”
Action: fetch the exact SKILL.md from main and compare the commit/ref with the PR merge commit.
### Bad example
Claim: “All tests passed” based only on a green README badge.
Bad action: repeat the claim without opening the relevant run or test result.
Why bad: a badge may be stale, incomplete, or refer to another commit.
