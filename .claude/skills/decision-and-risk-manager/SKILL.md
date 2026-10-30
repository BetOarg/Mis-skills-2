---
name: decision-and-risk-manager
description: Maintain a traceable decision and risk register for projects, including options, rationale, owners, impact, reversibility, approval gates, and review triggers. Use when a project has consequential trade-offs, unresolved decisions, recurring risks, or approvals to track. Not for replacing legal, financial, security, or domain-expert review.
---
# Decision and Risk Manager

## Mission
Prevent repeated debates, hidden assumptions, and unowned risks by recording decisions and risks in a compact, reviewable form.

## Workflow
1. Inspect current project instructions, decisions, risk records, and authoritative project state. Reuse an existing register when available.
2. Separate confirmed facts, user decisions, assumptions, recommendations, and unresolved questions.
3. For each material decision, record: ID, date, question, options considered, selected option, rationale, consequences, reversibility, decision owner, approval evidence, and review trigger.
4. For each material risk, record: cause, event, consequence, likelihood and impact (with scale defined), mitigation, contingency, owner, trigger, and residual exposure.
5. Prioritize risks by severity and proximity, not by dramatic wording. Do not invent probabilities or numerical scores; use qualitative labels when evidence is insufficient.
6. Detect dependencies and contradictions between decisions. Flag stale decisions when their assumptions or external state have changed.
7. Route technical, release, automation, and business execution to the relevant specialist skills. This skill records governance; it does not replace implementation.
8. Ask for approval only when a decision belongs to the user or crosses an explicit authority boundary. Do not silently decide high-impact trade-offs.
9. Update the register only in an authorized destination. Verify writes and link each decision to supporting evidence.
10. Close with decisions made, open decisions, top risks, owners, triggers, and the next review point.

## Boundaries
- Do not present legal, medical, financial, or security judgment as professional certification.
- Do not infer consent from silence or broad instructions.
- Do not persist personal preferences or sensitive information unless explicitly requested and supported.
- A risk register is not proof that mitigations have been implemented.

## Good examples
### Good example 1
Request: “Compare the two database migration options and record the decision.”
Action: compare rollback, data integrity, migration effort, and operational constraints; distinguish measured facts from assumptions; record the user's selection and evidence.
### Good example 2
Request: “What can block this release?”
Action: identify concrete risks from current CI, signing, store, and test evidence; assign triggers and next checks; leave unknown likelihoods qualitative.
### Bad example
Request: “Choose the cheapest option and approve it on my behalf.”
Bad action: commit the user to a vendor or spend money without approval.
Why bad: recording a recommendation does not grant purchasing or contracting authority.
