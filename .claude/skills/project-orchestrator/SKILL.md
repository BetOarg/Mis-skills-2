---
name: project-orchestrator
description: Coordinate multi-step projects by interpreting the goal, selecting specialist skills, sequencing dependencies, tracking verified progress, and closing with evidence. Use when the user says advance, continue, coordinate, finish a project, or handle a task spanning multiple skills. Not for executing a specialist task alone when no coordination is needed.
---
# Project Orchestrator

## Mission
Turn a broad user goal into coordinated, completed work while preserving the user's authority and the specialist skills' boundaries.

## Workflow
1. Restate the outcome in one sentence. Inspect available project instructions, current state, decisions, lessons, risks, and pending work before planning.
2. Classify the request: simple single-skill task, multi-step project, continuation, or blocked request. Use this skill only when coordination adds value.
3. Use smart-task-intake for short/ambiguous instructions. Do not repeat intake questions already answered in accessible context.
4. Build a short dependency-aware plan with observable completion criteria. Identify what can run independently and what must be sequential.
5. Route each work package to the narrowest relevant specialist skill. Do not copy its full procedure or claim to invoke a skill when only its instructions were consulted.
6. Use workflow-optimizer when the process itself is cumbersome; simplify before proposing automation. Use workflow-automation-architect only for a stable, bounded automation candidate.
7. Use decision-and-risk-manager when trade-offs, material risks, approval gates, or durable decisions need tracking. Do not add a register for trivial choices.
8. Execute authorized work. Maintain a compact ledger: item, owner/skill, state, evidence, dependency, next action.
9. Replan when evidence invalidates an assumption. Do not silently widen scope.
10. Use evidence-verifier to independently check material deliverables and cross-skill consistency.
11. Use context-handoff-manager when work is moving to another chat/session or a self-contained continuation brief is requested.
12. Close only when all authorized work is complete or remaining blockers are explicit. Update tracking only when destination is authorized and write succeeds.

## Routing rules
- Short or ambiguous user instructions: smart-task-intake.
- Multi-step work and cross-skill dependencies: project-orchestrator.
- Process friction, duplicate steps, unclear handoffs: workflow-optimizer.
- Stable recurring process needing automation design: workflow-automation-architect.
- Material decisions, trade-offs, risks, approval tracking: decision-and-risk-manager.
- Evidence and completion claims: evidence-verifier.
- Context transfer: context-handoff-manager.
- Defects: debug-and-fix; refactoring: senior-code-refactor; tests: automated-test-generator.
- Repository, branches, PRs, workflows: github-project-operations; release readiness: audit-ci-release.
- New/revised skills: agent-skill-generator.
- Chat history and task extraction: chat-task-auditor.
- Technical docs: technical-documentation-writer; commit/PR text: commit-pr-writer.
- Ads and business documents: ads-campaign-builder / business-strategy-documents.

## Coordination principles
- Default path: intake → orchestration only if needed → specialist execution → evidence verification.
- Add decision/risk, workflow optimization, automation design, and handoff only when their trigger conditions apply.
- Do not run every skill for every request. Avoid duplicate analysis, duplicate questions, and competing sources of truth.
- The orchestrator delegates and tracks; it does not replace specialist procedures.
- The workflow optimizer removes waste before automation. The automation architect designs stable, bounded automations. The decision/risk manager records governance, not implementation. The evidence verifier validates claims, not the underlying work. The handoff manager transfers context, not presumed access.

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
