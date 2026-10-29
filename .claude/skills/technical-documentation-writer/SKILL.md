---
name: technical-documentation-writer
description: Write, restructure, or audit technical documentation, READMEs, API guides, setup instructions, and developer runbooks for accuracy and usability.
---

# Technical Documentation Writer

## Goal
Help a reader understand the purpose, prerequisites, and correct use of a technical system without unsupported claims or unnecessary jargon.

## Workflow
1. Identify the audience, task, repository/product version, and desired document type.
2. Inspect source code, configuration, tests, and existing documentation when available. Treat source behavior as authoritative over stale prose.
3. Put purpose and intended audience first. Organize around the reader's tasks, using concise headings, short lists, and tables only when they improve scanning.
4. Document prerequisites, installation, configuration, examples, expected outputs, failure modes, and troubleshooting where relevant.
5. Verify every command, path, option, API name, environment variable, and example against available evidence. Mark unverified details explicitly.
6. Keep secrets and real credentials out of examples; use safe placeholders and explain required configuration.
7. Check internal links, code fences, terminology, version assumptions, accessibility, and consistency with neighboring docs.
8. Run documentation linting or link validation if available; report exact results and any checks not run.
9. Review the document from a new user's perspective and remove ambiguity or redundant sections.
10. Report files changed, evidence used, assumptions, and remaining documentation gaps.

## Rules
- Never fabricate product behavior, command output, API fields, benchmarks, or compatibility claims.
- Prefer runnable minimal examples over pseudocode; label pseudocode clearly.
- Do not expose secrets or sensitive internal data.
- Keep the first-use path clear while preserving important caveats.
- Use the project's existing terminology and style unless they are demonstrably misleading.

## Completion criteria
The document matches the implementation as far as evidence permits, gives a clear path to the reader's goal, and has links/examples checked or explicitly marked unverified.

## Examples

### Good example 1
Request: “Write a README for this CLI.”
Action: inspect entry points and package metadata, verify install and invocation commands, document flags and exit behavior, then check all local links.

### Good example 2
Request: “Document this API endpoint.”
Action: derive request and response shapes from source/schema/tests, include success and error examples, and mark authentication and rate limits as unknown if not verifiable.

### Bad example
Request: “Document deployment.”
Bad action: invent environment variables and state that deployment was tested.
Why bad: readers may break production systems by following instructions that were never verified.
