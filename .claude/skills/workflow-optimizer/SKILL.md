---
name: workflow-optimizer
description: Simplify an existing workflow by finding friction, duplicate steps, handoff delays, unclear ownership, and avoidable tool switching, then propose measurable improvements. Use when a process feels cumbersome, repetitive, slow, or unintuitive. Not for automating a process before its rules, risks, and desired outcome are understood.
---
# Workflow Optimizer

## Mission
Make work easier to understand and complete by removing unnecessary complexity before adding automation.

## Workflow
1. Define the workflow's desired outcome, users, start/end points, constraints, and source of truth.
2. Observe the actual steps from available evidence. Separate current practice from proposed or documented practice.
3. Map each step with trigger, input, action, owner, tool, output, wait time, failure path, and handoff.
4. Identify friction: duplicate entry, repeated explanations, unnecessary approvals, context loss, ambiguous ownership, excess tool switching, avoidable waiting, rework, and unverified completion.
5. Classify each improvement as remove, simplify, standardize, clarify, batch, delegate, or automate. Prefer removing waste before adding tooling.
6. Estimate time/cost impact only from observed or explicitly stated data. Show formulas, assumptions, ranges, and confidence; do not invent baseline metrics.
7. Rank changes by user value, effort, risk, reversibility, and dependencies. Start with the smallest high-value improvement.
8. Coordinate with workflow-automation-architect only when a stable, rule-based step is a real automation candidate. Use project-orchestrator for multi-skill delivery and decision-and-risk-manager for consequential trade-offs.
9. Define before/after measures and a small pilot. Include exceptions, rollback, human review, and acceptance criteria.
10. Implement only within authorization. Do not alter live systems, workflows, permissions, or external processes without approval.
11. Verify the improved flow with a realistic task and record what changed, what did not, and remaining friction.

## Design principles
- Optimize the whole journey, not one isolated step.
- Do not automate unstable, poorly understood, or low-value work.
- Preserve required controls, privacy, auditability, and human judgment.
- Avoid creating a new dashboard, document, or meeting unless it removes more work than it adds.
- Make the default path obvious and exceptions explicit.

## Good examples
### Good example 1
Request: “It takes too many steps to continue work between chats.”
Action: inspect the handoff process, remove repeated context requests, standardize a compact verified brief, and pilot it on one project.
### Good example 2
Request: “Our PR process feels cumbersome.”
Action: map creation, review, CI, approval, and merge; identify duplicate checks and unclear ownership; propose a smaller flow without weakening required gates.
### Bad example
Request: “Make this faster by removing every approval.”
Bad action: remove security, spending, deployment, or merge controls without assessing their purpose and risk.
Why bad: speed is not an acceptable reason to remove necessary safeguards.
