---
name: context-handoff-manager
description: Prepare accurate continuation briefs when a chat, session, project, or platform is changing or becoming too long. Use when the user asks for a summary to paste into a new chat, transfer context, resume later, or preserve project state. Not for inventing history or claiming access to unavailable conversations.
---
# Context Handoff Manager

## Mission
Transfer the minimum sufficient context so another session can continue without repeating discovery or confusing plans with completed work.

## Workflow
1. Define the target project and handoff purpose. Inspect only accessible conversation, files, project records, and external systems authorized for the task.
2. Identify the latest verified state and its timestamp/reference. Reconcile important claims against current source-of-truth systems when available.
3. Capture:
   - project goal and non-negotiable constraints;
   - repository/workspace, branch, commit, PR/issues and relevant links;
   - completed work with evidence;
   - failed checks, known defects, and unresolved risks;
   - decisions made and alternatives rejected;
   - pending work ordered by dependency/priority;
   - approval gates and exact next action;
   - relevant tool/platform limitations.
4. Label each item VERDE, ROJO, PENDIENTE, or BLOQUEADO. Distinguish verified fact, user decision, hypothesis, and recommendation.
5. Remove unrelated personal details, secrets, credentials, and redundant narrative. Never expose private content unnecessarily.
6. Produce a self-contained, copy-ready prompt that tells the next assistant what to inspect first and what not to repeat.
7. Include source links and SHAs when known. If the source is unavailable or stale, state that explicitly.
8. Do not claim a new session has imported or remembered the brief; handoff is complete when the artifact is delivered or its authorized save is verified.

## Default handoff structure
1. Identity and objective.
2. Current verified state (date, branch, SHA, PR/CI).
3. Completed and verified.
4. Open failures and blockers.
5. Decisions and constraints.
6. Pending steps in execution order.
7. Exact first instruction for the next session.
8. Explicit actions requiring approval.

## Good examples
### Good example 1
Request: “Haceme un prompt para continuar en otro chat.”
Action: produce a self-contained brief with repo, branch, current CI, verified achievements, pending issues, constraints, and first next action.
### Good example 2
Request: “Resumí solo el repo, no la plataforma de ventas.”
Action: filter the handoff to repository evidence and omit unrelated account, marketing, or personal context.
### Bad example
Request: “Resumí lo que hicimos el mes pasado” when only the current chat is available.
Bad action: invent missing conversation history or state that all prior chats were inspected.
Why bad: unavailable history must be identified as a limitation, not reconstructed by guesswork.
