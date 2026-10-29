---
name: agent-skill-generator
description: Design, create, or improve reusable agent skills and SKILL.md files with clear activation metadata, safe workflows, examples, and validation. Use when asked to package a repeatable task as an agent skill.
---

# Agent Skill Generator

## Goal
Produce a focused, portable skill that an agent can follow and a maintainer can validate.

## Workflow
1. Identify the single job, intended users, activation signals, exclusions, required tools, and expected output.
2. Inspect the target platform's current skill format and repository conventions when accessible. Do not claim platform compatibility without checking its requirements.
3. Create a directory with SKILL.md; use valid YAML frontmatter containing a stable name and a concise, actionable description.
4. Write an explicit goal, ordered workflow, decision rules, safety/authorization boundaries, completion criteria, and reporting format.
5. Include exactly two good examples and one bad example with an explanation, unless the destination repository has a documented convention that requires another format.
6. Add a CHANGELOG.md when required by the repository's conventions or when version history is useful; for this repository, every skill must have one.
7. Avoid duplicating shared instructions. Link to common guidance where practical, but keep the skill usable when copied according to the target platform's documented mechanism.
8. Add at least one normal and one adversarial test case with observable acceptance criteria.
9. Validate frontmatter, directory/name consistency, internal links, examples, and required files. Run the repository validator if available; report if it was not run.
10. Review the skill as both a user and an adversarial tester. Remove ambiguous commands, impossible requirements, and claims unsupported by tools.

## Quality rules
- One skill should primarily solve one job. Split unrelated workflows.
- Activation descriptions should say when to use the skill, not merely advertise quality.
- Do not assume every platform loads SKILL.md natively or automatically.
- Do not invent tools, APIs, permissions, or platform capabilities.
- State prerequisites and blockers. Never equate a drafted instruction with a completed external action.
- Keep examples short, realistic, and consistent with the workflow.

## Completion criteria
The skill has valid metadata, a focused purpose, executable steps, safety boundaries, success criteria, required examples/changelog, tests, and recorded validation status.

## Examples

### Good example 1
Request: “Create a skill that triages CI failures.”
Action: define triggers and exclusions, specify evidence-first triage, add safe remediation rules, write normal/adversarial tests, and validate metadata and links.

### Good example 2
Request: “Make this skill portable to three assistants.”
Action: compare each platform's documented loading method, separate shared instructions from adapters, and record compatibility as pending until tested in each target environment.

### Bad example
Request: “Create one skill for coding, marketing, legal review, and finance.”
Bad action: produce a single large instruction file with vague activation criteria.
Why bad: its scope is too broad to test, maintain, or activate reliably.
