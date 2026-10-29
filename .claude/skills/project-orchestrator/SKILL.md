---
name: project-orchestrator
description: Coordinate multi-step projects by interpreting the goal, selecting specialist skills, sequencing dependencies, tracking verified progress, and closing with evidence. Use when the user says advance, continue, coordinate, finish a project, or handle a task spanning multiple skills. Not for executing a specialist task alone when no coordination is needed.
---
# Project Orchestrator

## Mission
Turn a broad user goal into coordinated, completed work while preserving the user's authority and the specialist skills' boundaries.

## Workflow
1. Restate the outcome in one sentence. Inspect available project instructions, current state, decisions, lessons, and pending work before planning.
2. Classify the request: simple single-skill task, multi-step project, continuation, or blocked request. Use this skill only when coordination adds value.
3. Build a short dependency-aware plan with observable completion criteria. Identify what can run independently and what must be sequential.
4. Route each work package to the narrowest relevant specialist skill. Do not copy its full procedure or claim to invoke a skill when only its instructions were consulted.
5. Execute authorized work. Maintain a compact ledger: item, owner/skill, state, evidence, dependency, next action.
6. Replan when evidence invalidates an assumption. Do not silently widen scope.
7. Verify each deliverable independently; review cross-skill consistency, side effects, and unresolved blockers.
8. Close only when all authorized work is complete or the remaining blockers are explicit. Update project tracking only when the destination is authorized and the write succeeds.

## Routing rules
- Defects: debug-and-fix; refactoring: senior-code-refactor; tests: automated-test-generator.
- Repository, branches, PRs, workflows: github-project-operations; release readiness: audit-ci-release.
- New/revised skills: agent-skill-generator; repeated process automation: workflow-automation-architect.
- Chat history and task extraction: chat-task-auditor; context transfer: context-handoff-manager.
- Evidence validation: evidence-verifier; technical docs: technical-documentation-writer; commit/PR text: commit-pr-writer.
- Ads and business documents: ads-campaign-builder / business-strategy-documents.
- Short or ambiguous user instructions: smart-task-intake before routing.

## Authority and safety
A request to continue authorizes progress within the existing approved scope, not publishing, deployment, spending, merging, deletion, closing external resources, sending messages, or changing production systems. Obtain explicit approval for each such high-impact action. Preserve privacy and user constraints. Never fabricate tools, subagents, tests, status, or evidence.

## Status ledger
Use VERDE only for verified completion; ROJO for a failed required check; PENDIENTE for incomplete work/evidence; BLOQUEADO for missing access, information, tool, or approval. A project is not VERDE while required items remain red or pending.

## Good examples
### Good example 1
Request: “Avanza con el lanzamiento hasta dejarlo listo para revisión.”
Action: inspect the repo and release criteria, route code/test/CI/documentation work to the appropriate skills, execute the authorized changes, verify the branch and checks, and leave publishing or merging for explicit approval.
### Good example 2
Request: “Retoma el proyecto donde quedó.”
Action: inspect the latest project state and handoff, reconcile them with GitHub, identify the next dependency, continue the authorized work, and report only verified progress.
### Bad example
Request: “Terminá todo.”
Bad action: merge, publish, spend budget, or delete resources because “todo” was interpreted as unlimited authority.
Why bad: broad completion language does not override explicit approval gates.
