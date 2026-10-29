---
name: audit-ci-release
description: Audit repository health, CI workflows, branch protections, dependency and version consistency, release artifacts, and release readiness. Use for readiness reviews or diagnosing the overall state of a candidate release; report evidence and gaps without silently changing or publishing anything.
---

# Audit CI and Release

## Goal
Produce an evidence-backed view of repository and release readiness. This skill audits and recommends; it does not automatically fix findings or release software.

## Rules
- Verify the current repository, default branch, candidate version, commit, and workflow runs from live sources before reporting.
- Distinguish current observations from historical conversation context. Historical “green” is not evidence of current green.
- Do not infer a workflow ran merely because it exists. Check run ID, commit SHA, event, status, conclusion, and relevant job results.
- Do not call a release ready when required checks are red, cancelled, missing, stale, or unverified.
- Never claim an artifact exists or has a specific hash unless it was actually retrieved and inspected.
- Keep audit separate from remediation. Propose changes; obtain approval before modifying workflows, deleting branches, closing issues/PRs, merging, tagging, publishing, or deploying.
- Respect app-specific requirements: package/bundle identifiers, supported platforms, database/storage constraints, privacy requirements, signing, and store requirements.
- Do not reveal or copy secrets. Verify only their configured presence when supported, never their values.
- If evidence cannot be accessed, label the finding PENDIENTE/BLOQUEADO rather than guessing.

## Workflow
1. **Scope:** confirm repository, target branch, candidate release/version, platforms, and the required release criteria.
2. **Repository baseline:** inspect working tree if accessible, default branch, recent commits, open PRs/issues, branches, tags, README, release notes, and relevant configuration.
3. **CI inventory:** enumerate applicable workflows and required jobs. Identify triggers, path filters, conditions, concurrency/cancellation, permissions, and platform coverage.
4. **Run verification:** for each required check, record run ID, commit SHA, branch/event, status/conclusion, and job-level red results. Confirm it belongs to the candidate commit.
5. **Code quality:** review test/lint/analyzer coverage, dependency lockfiles, deprecated APIs, dead/orphaned code only where evidence is available, and known regression risks.
6. **Version consistency:** compare app manifest, package metadata, Android/iOS identifiers, tags, changelog/release notes, and build workflow inputs. Flag differences explicitly.
7. **Artifact validation:** if artifact is available, inspect type, package ID, version/build number, architecture/ABI and other required technical properties; calculate hashes only from the actual file.
8. **Platform/store requirements:** check platform-specific build and distribution prerequisites against current repository evidence and current official requirements if web research is available.
9. **Branch and governance review:** inspect protection/rulesets and divergence before recommending branch deletion. Never treat “merged” as proof that a branch is obsolete if it contains unique commits.
10. **Risk-ranked findings:** group as Blocker, High, Medium, Low. Each finding includes evidence, impact, exact next action, and whether approval is needed.
11. **Readiness decision:** VERDE only if all required criteria are evidenced as passed; otherwise ROJO, PENDIENTE, or BLOQUEADO.
12. **Final verification:** link the actual runs, commits, artifacts, and files inspected; state what was not accessible.

## Required output
- **Estado global:** VERDE / ROJO / PENDIENTE / BLOQUEADO.
- **Alcance verificado:** repo, branch, candidate commit/version, time or run identifiers where available.
- **Matriz de checks:** check, evidence/run, commit match, status, conclusion.
- **Blockers and risks:** prioritized, actionable, evidence-based.
- **Version/artifact consistency:** verified values and discrepancies.
- **Approval-required actions:** separate list; do not execute them.
- **Final verdict:** release-ready / not ready / cannot determine, with explicit reasons.

## Examples

### Good example 1
User: “Is version 2.7.2 ready for the store?”
Action: verify the exact candidate commit, Android and iOS workflows, required job conclusions, package identifiers, version/build metadata, and artifact contents. Report each platform independently and flag missing evidence; do not upload.

### Good example 2
User: “Clean up the release branches.”
Action: inventory branch heads, merged status, and unique commits; classify keep/archive/delete candidates with evidence. Ask approval before deleting anything.

### Bad example
User: “Audit the release.”
Bad action: rely on a previous message saying “green,” assume the latest artifact matches the current commit, and declare release-ready without checking run IDs.
Why bad: the audit is not reproducible and may mislead the user into publishing a broken or stale build.
