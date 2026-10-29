# Adaptador: Claude Code

- Skills nativas: `.claude/skills/<nombre>/SKILL.md`, con un `CHANGELOG.md` por skill.
- Orquestación: `prompts/claude-code/CLAUDE.md`.
- Mantén el frontmatter y la estructura de skills compatibles con la versión de Claude Code utilizada.
- Verifica activación y uso real en una sesión de Claude Code; la presencia del archivo no demuestra que se haya invocado.
- Ejecuta `python scripts/validate_repo.py` y las pruebas pertinentes antes de proponer cambios.
