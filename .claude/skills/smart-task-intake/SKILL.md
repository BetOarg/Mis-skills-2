---
name: smart-task-intake
description: Interpret short, natural, or ambiguous task instructions using available conversation and project context, infer the safest useful next step, and ask only essential clarifying questions. Use when the user says continue, advance, fix it, check this, do the rest, or gives an underspecified command. Not for replacing specialist execution or inventing missing facts.
---
# Smart Task Intake

## Mission
Reduce repetitive prompting. Understand the user's intended outcome from accessible context without turning guesses into facts or expanding authority.

## Workflow
1. Read the current request and the immediately relevant conversation, project instructions, prior decisions, and available task state.
2. Resolve references such as “it”, “the red one”, “continue”, or “finish” only when one clear active target exists.
3. Separate known constraints, authorized actions, inferred intent, and unknowns.
4. Choose the smallest useful next action that advances the established goal. For a continuation, inspect current reality before resuming.
5. Ask one concise question only when a missing detail materially changes safety, correctness, cost, recipient, target, or irreversible outcome.
6. If ambiguity is low-risk, proceed with a clearly stated assumption. If ambiguity is high-impact, stop before the consequential action.
7. Translate the request into a concrete task for the relevant specialist skill and pass along constraints and evidence.
8. Report what interpretation was used if it materially affects the outcome.

## Intent and authority
- “Avanza” means continue the already agreed work, not bypass approvals.
- “Hasta el final” means complete all authorized work and identify actions that still need approval.
- “Revisa” means inspect and report; it does not imply edits.
- “Soluciona” authorizes reasonable fixes within the known scope, not production deployment or destructive cleanup.
- “Fusiona”, “publica”, “envía”, “compra”, “borra” or “despliega” require clear target and explicit authorization for that action.
- Never infer consent to spend money, disclose private data, save preferences persistently, or alter external systems.

## Good examples
### Good example 1
Request: after a documented GitHub repair plan, “Avanza”.
Action: re-check the repo and CI, continue the next authorized repair step, and preserve the merge/publish approval gate.
### Good example 2
Request: after a draft email and a request to improve it, “Hacelo más directo”.
Action: revise the existing draft in the same language and preserve its purpose; do not send it.
### Bad example
Request: “Dale para adelante” after discussing two different repos and a paid campaign.
Bad action: guess the repository and activate the campaign.
Why bad: target and financial authorization are unclear; ask one focused question.
