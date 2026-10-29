---
name: github-project-operations
description: Plan and carry out GitHub repository operations involving issues, pull requests, branches, commits, workflows, and project cleanup. Use when the user asks to inspect, organize, update, or prepare GitHub work; verify every operation and obtain approval for merge, deletion, closing, or publishing.
---

# GitHub Project Operations

## Goal
Perform repository operations accurately, with minimal risk and clear evidence. Distinguish inspection, preparation, and irreversible or externally visible actions.

## Permission boundaries
- Read and inspect freely when authorized.
- Draft issue/PR text, branch plans, diffs, and workflow changes without publishing them.
- Ask for explicit approval before merging a PR, deleting a branch or file, closing an issue/PR, creating a release/tag, publishing/deploying, changing access/security settings, or spending money.
- User saying “advance” authorizes progress within the agreed scope, not an unstated destructive action.
- Never force-push or rewrite history unless explicitly approved.
- Never assume branch existence, CI status, mergeability, permissions, or file content; fetch current evidence.
- Preserve unique branch commits. A branch that is not merged is not automatically obsolete.
- Do not expose tokens, secrets, or private data in logs or responses.

## Workflow
1. **Confirm target:** exact repository, base branch, target branch, and requested outcome.
2. **Inspect live state:** repository metadata, default branch, branch heads, PR/issue status, latest commits, checks, and permissions relevant to the action.
3. **Classify operations:**
   - Read-only: inspect, compare, audit, fetch logs.
   - Reversible preparation: draft files, propose changes, create an approved working branch.
   - Approval-required: merge, delete, close, release, publish, deploy, spend, alter access/protection.
4. **Build a dependency-aware plan:** order operations so prerequisites exist first. For empty repositories, confirm how an initial commit will be created and get approval before changing the default branch if that is outside the approved plan.
5. **Make minimal changes:** use the named branch; keep unrelated changes untouched; use descriptive commit messages. Do not silently change the user's selected branch strategy.
6. **Verify each mutation:** read back branch/commit/file/issue/PR state from GitHub. A successful API response alone does not prove the full desired state.
7. **Check workflow outcomes:** identify run IDs and commit SHA; distinguish queued, in-progress, cancelled, skipped, failure, and success.
8. **Report exact result:** links, branch names, commit SHAs, files changed, status, and uncompleted items. Do not claim a PR was merged unless GitHub says it is merged.

## Branch cleanup protocol
For every candidate branch, inspect:
- head SHA and last update;
- merge base with the default branch;
- commits unique to the branch;
- whether those commits are already represented elsewhere;
- open PRs, release references, and workflow dependencies.
Classify as KEEP, REVIEW, ARCHIVE, or DELETE CANDIDATE. Execute deletion only after explicit approval.

## Issue and PR protocol
- Read the issue/PR and linked discussion before proposing a close or merge.
- Verify whether acceptance criteria are met and checks are complete.
- Prepare concise title/body/checklist where useful.
- Never close or merge merely because a user asked for “cleanup” unless the scope explicitly authorizes those actions.

## Required reporting
Use **VERDE / ROJO / PENDIENTE / BLOQUEADO** when reporting operation status. Include:
- target repository and branch;
- actual mutations and resulting links/SHAs;
- verification read-back;
- remaining approvals or blockers.

## Examples

### Good example 1
User: “Create a feature branch and add these docs, but don't merge.”
Action: inspect default branch, establish any required initial commit only with approval, create the requested branch, add files there, read each file back from GitHub, and confirm main was not changed beyond the approved bootstrap.

### Good example 2
User: “Close all issues and PRs.”
Action: inventory them, distinguish completed from unresolved work, present the proposed closures, and request explicit approval before closing. If approval is granted, close only the reviewed set and verify each result.

### Bad example
User: “Clean old branches.”
Bad action: delete every branch that is not named main.
Why bad: some branches may contain unique, unmerged work or support an open release.
