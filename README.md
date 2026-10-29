# Mis-skills

Biblioteca de skills reutilizables para desarrollo de software, publicidad/negocio y auditoría/gestión de proyectos. Mantiene una fuente única por skill, reglas comunes y prompts/adaptadores por aplicación.

## Arquitectura
- Skills fuente: `.claude/skills/<nombre>/SKILL.md`.
- Reglas comunes: [COMMON-INSTRUCTIONS.md](COMMON-INSTRUCTIONS.md).
- Prompts: [Claude Code](prompts/claude-code/CLAUDE.md), [Claude web/app](prompts/claude/PROJECT-INSTRUCTIONS.md), [ChatGPT](prompts/chatgpt/PROJECT-INSTRUCTIONS.md), [Gemini](prompts/gemini/GEMINI.md) y [Kimi](prompts/kimi/KIMI.md).
- Adaptadores: [adapters/](adapters/README.md).
- Pruebas: [tests/README.md](tests/README.md) y [tests/RESULTS.md](tests/RESULTS.md).

## Licencia
[MIT](LICENSE).

## Skills disponibles
- [debug-and-fix](.claude/skills/debug-and-fix/SKILL.md): diagnosticar y corregir defectos con pruebas de regresión.
- [audit-ci-release](.claude/skills/audit-ci-release/SKILL.md): auditar CI, repositorios y releases.
- [github-project-operations](.claude/skills/github-project-operations/SKILL.md): gestionar issues, PR, ramas y workflows.
- [ads-campaign-builder](.claude/skills/ads-campaign-builder/SKILL.md): diseñar campañas Google Ads y Meta Ads.
- [business-strategy-documents](.claude/skills/business-strategy-documents/SKILL.md): preparar estrategias y documentos comerciales.
- [senior-code-refactor](.claude/skills/senior-code-refactor/SKILL.md): refactorizar con control de regresiones.
- [agent-skill-generator](.claude/skills/agent-skill-generator/SKILL.md): diseñar y validar skills reutilizables.
- [technical-documentation-writer](.claude/skills/technical-documentation-writer/SKILL.md): documentar sistemas con evidencia.
- [commit-pr-writer](.claude/skills/commit-pr-writer/SKILL.md): redactar commits y PR fieles al diff.
- [automated-test-generator](.claude/skills/automated-test-generator/SKILL.md): diseñar pruebas automatizadas.
- [chat-task-auditor](.claude/skills/chat-task-auditor/SKILL.md): auditar recurrencias en chats y ordenar pendientes.
- [workflow-automation-architect](.claude/skills/workflow-automation-architect/SKILL.md): auditar trabajo recurrente, priorizar oportunidades y diseñar automatizaciones medibles.

Cada skill tiene su propio `CHANGELOG.md`.

## Compatibilidad
Markdown compartido no implica compatibilidad operativa idéntica. Registra por separado acceso al contenido, aplicación de instrucciones, herramientas disponibles y ejecución verificada. No publiques, despliegues, gastes dinero, fusiones, borres ni cierres recursos sin autorización explícita.

## Documentación
- [Instrucciones universales](docs/instrucciones-universales.md)
- [Registro de lecciones](tasks/lessons.md)
- [Plan de trabajo](tasks/todo.md)
- [Protocolo de compatibilidad](docs/compatibilidad.md)
- [Casos funcionales](tests/README.md) · [Matriz](tests/RESULTS.md)

## Pruebas funcionales
La matriz contempla doce skills en cinco plataformas: 60 combinaciones y 120 ejecuciones mínimas (caso principal y adversarial). Todo permanece PENDIENTE hasta disponer de evidencia real. CI estática no demuestra compatibilidad funcional.

## Estado del proyecto
La skill workflow-automation-architect está en una rama para revisión; no se considera integrada hasta fusionar su PR. Consulta la matriz para el estado comprobado.

## Estados
- VERDE: criterios ejecutados y aprobados con evidencia.
- ROJO: falló un criterio obligatorio.
- PENDIENTE: falta ejecutar o falta evidencia.
- BLOQUEADO: falta acceso, información, herramienta o autorización.
