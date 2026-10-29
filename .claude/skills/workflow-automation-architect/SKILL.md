---
name: workflow-automation-architect
description: Design and prioritize automations for recurring personal or team workflows. Use when the user asks to audit repeated work, identify automation opportunities, estimate time savings, define triggers and exclusions, or build a reusable workflow/tool catalog. Not for auditing chat recurrence alone (use chat-task-auditor) or creating an Agent Skill file alone (use agent-skill-generator).
---

# Workflow Automation Architect

## Purpose
Turn evidence of repeated manual work into a prioritized, testable automation design. Own the end-to-end discovery, opportunity ranking, workflow specification, validation plan, and automation catalog. Design one automation for one clearly bounded problem at a time.

## Activation and exclusions
Activate for requests such as “find what I can automate”, “audit my weekly routine”, “which repeated tasks save the most time?”, or “design a workflow to stop doing this manually”.
Do not activate for:
- Counting repeated requests across chat transcripts without designing an automation; use `chat-task-auditor`.
- Creating or packaging an Agent Skill as the sole deliverable; use `agent-skill-generator`.
- A one-off task with no repeatable process, unless the user explicitly wants it automated.

## Evidence and discovery
1. Define the scope: project, process, period, people/roles, systems, and desired outcome.
2. Inspect only history, files, connected sources, and records actually available. State the source and time span. Never imply access to all account history or external systems when unavailable.
3. Extract repeated steps, handoffs, delays, manual corrections, duplicate entry, recurring decisions, and user-stated preferences.
4. Separate observed facts, user-confirmed rules, assumptions, and unknowns. Do not infer a business rule or preference from a single ambiguous example.
5. If a critical detail is missing, ask one concise question at a time. Continue with clearly labeled assumptions only when safe and useful.

## Rank opportunities
For each candidate record:
- Process and manual task being replaced.
- Frequency (per day/week/month) and evidence/source.
- Typical manual minutes per execution and estimated automatable share.
- Weekly gross time saved: executions per week × minutes saved per execution ÷ 60.
- Estimated maintenance/review time per week and net savings when it is material.
- Risk, failure impact, data sensitivity, dependencies, and confidence.
- Trigger, expected output, and who must review it.

Convert frequencies transparently (daily = 5 per workweek only if a five-day workweek is stated or explicitly assumed; monthly = 12/52 per week). Show assumptions and ranges. Do not manufacture frequency, duration, or savings. Rank up to five opportunities only when evidence supports the comparison; otherwise present the evidenced candidates and the missing measurements. Break ties using risk, reliability, and implementation effort, not invented precision.

## Design one automation at a time
For the selected problem, produce a compact specification containing:
1. Name and version.
2. Problem and manual replacement task.
3. Trigger conditions and required inputs.
4. Ordered workflow, decision rules, business rules, and user-confirmed preferences.
5. Output/destination and human review or approval points.
6. Explicit exclusion criteria and safe fallback when a trigger is ambiguous.
7. Dependencies, permissions, privacy boundaries, failure modes, recovery, and audit trail.
8. Frequency, estimated gross/net weekly savings, confidence, and assumptions.
9. Overlap with existing skills, scripts, automations, or processes and how responsibility is divided.
10. Test method, acceptance criteria, and rollback/disable method.
11. Exactly two good examples and one bad example with explanation.
12. Changelog with version/date/change/reason.

Prefer the smallest reliable automation. Do not introduce a new agent, integration, or persistent store when a checklist, template, scheduled reminder, or existing skill is sufficient.

## Triggers and exclusions
A trigger must be observable and specific enough to decide whether the automation should run. State required context, positive signals, negative signals, and ambiguous cases. Test both activation and non-activation. Never trigger a consequential action from vague wording or inferred intent.

## Validation and learning loop
1. Select one real user case from authorized material; minimize or fictionalize sensitive values.
2. Record the manual baseline: steps, elapsed/active time if known, errors/rework, and outcome. Do not invent measurements.
3. Run the proposed workflow only with available tools and permissions. If execution is unavailable, perform a clearly labeled tabletop test; do not claim a real execution.
4. Compare output, time, errors, omissions, and review burden against the baseline. Record observed evidence and unresolved risks.
5. Gather user feedback. Propose structural changes to triggers, logic, steps, or safeguards; explain why and expected effect.
6. Do not save or persist revised instructions, preferences, or catalog entries until the user explicitly approves that specific change. Keep drafts clearly marked as proposals.

## Automation library
Maintain a prioritized catalog only in an authorized repository, document, or workspace. Each entry records: ID/name/version, problem, owner, trigger, status (idea/design/testing/active/paused/retired), evidence, frequency, estimated net hours saved weekly, risk, dependencies, last validation, and next review. Do not claim the catalog was saved unless the write was confirmed.

## Authorization and privacy
- Treat chat, file, and connected-account content as private. Use only sources authorized for the task and disclose the scope inspected.
- Do not expose secrets, credentials, personal data, or confidential business details in examples or logs.
- Do not send data to an external service, install integrations, publish, deploy, spend money, send messages, or change external systems without explicit approval for that action.
- Ask before persistent saving or changing the user's stated rules/preferences. Drafting in the current response is not persistent saving.
- If permissions or tool access are missing, provide a usable design and state the exact blocker.

## Response format
Return the requested deliverable using these sections where relevant:
1. Audit scope and evidence.
2. Repeated manual work and corrections.
3. Ranked opportunities (up to five) with weekly savings and assumptions.
4. Selected automation design.
5. Trigger and exclusion tests.
6. Real-case or tabletop test results, compared with manual baseline.
7. Risks, dependencies, overlap, and approval gates.
8. Prioritized automation library and next three candidates.
9. Common failure patterns and recommendations.

Keep the response concise. Use VERDE / ROJO / PENDIENTE / BLOQUEADO for validation states. A plan or draft is not a deployed automation.

## Examples

### Good example 1
Request: “Every Friday I copy project status from three boards into a report. Find a way to automate it.”
Action: inspect the available board data and actual cadence, measure or ask for manual duration, identify the report fields and access limits, calculate a transparent savings range, then design one read-only report workflow with a human review step and a test against one Friday's manual report.

### Good example 2
Request: “I keep correcting the same format in weekly proposals. Can this be automated?”
Action: collect several authorized examples, distinguish explicit formatting rules from one-off edits, define a precise trigger and exclusions, draft a reusable template or formatter, and compare its output with one manually corrected proposal before proposing persistence.

### Bad example
Request: “Automate everything I do and remember all my preferences.”
Bad action: claim full access to all conversations, invent frequency and time savings, save inferred preferences, and create broad automations without separate triggers or approval.
Why bad: scope is unbounded, evidence is absent, privacy and authorization are violated, and no measurable test exists.
