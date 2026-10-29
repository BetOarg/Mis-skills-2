# Mis-skills

Biblioteca de skills reutilizables para desarrollo, negocio, auditoría y gestión de proyectos. Mantiene una fuente única por skill, instrucciones comunes y adaptadores por plataforma.

## Arquitectura
- Skills fuente: `.claude/skills/<nombre>/SKILL.md`.
- Instrucciones compartidas: [COMMON-INSTRUCTIONS.md](COMMON-INSTRUCTIONS.md).
- Prompts y adaptadores por plataforma: [adapters/](adapters/README.md).
- Casos funcionales y evidencias: [tests/README.md](tests/README.md) · [tests/RESULTS.md](tests/RESULTS.md).

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
- [workflow-automation-architect](.claude/skills/workflow-automation-architect/SKILL.md): auditar trabajo recurrente y diseñar automatizaciones medibles.
- [project-orchestrator](.claude/skills/project-orchestrator/SKILL.md): coordinar proyectos, dependencias y skills especializadas.
- [smart-task-intake](.claude/skills/smart-task-intake/SKILL.md): interpretar instrucciones breves usando el contexto disponible.
- [context-handoff-manager](.claude/skills/context-handoff-manager/SKILL.md): preparar transferencias de contexto para continuar en otra sesión.
- [evidence-verifier](.claude/skills/evidence-verifier/SKILL.md): verificar afirmaciones de finalización contra fuentes autoritativas.

Cada skill tiene su propio `CHANGELOG.md`.

## Flujo de trabajo intuitivo
1. El usuario expresa el resultado que necesita, incluso con una instrucción breve.
2. `smart-task-intake` interpreta la intención y detecta si falta un dato esencial.
3. `project-orchestrator` coordina tareas complejas y deriva cada paquete a la skill especializada.
4. `evidence-verifier` comprueba afirmaciones y resultados antes del cierre.
5. `context-handoff-manager` conserva un resumen trazable cuando se cambia de chat o sesión.

Las skills especializadas siguen siendo responsables de su dominio. El coordinador no reemplaza sus procedimientos ni amplía permisos.

## Compatibilidad y seguridad
Markdown compartido no implica compatibilidad operativa idéntica. Registra por separado acceso al contenido, aplicación de instrucciones, herramientas disponibles y ejecución verificada. No publiques, despliegues, gastes dinero, fusiones, borres ni cierres recursos sin autorización explícita. No afirmes pruebas funcionales sin evidencia de ejecución real.

## Documentación
- [Registro de lecciones](tasks/lessons.md)
- [Plan de trabajo](tasks/todo.md)
- [Protocolo de compatibilidad](docs/compatibilidad.md)
- [Pruebas funcionales](tests/README.md)

## Pruebas funcionales
La matriz contempla 16 skills en cinco plataformas: 80 combinaciones y 160 ejecuciones mínimas (caso principal y adversarial). Todas permanecen PENDIENTES hasta disponer de evidencia real. CI estática no demuestra compatibilidad funcional.

## Estado del proyecto
La rama `feat/intuitive-project-workflow` contiene cuatro skills nuevas y las actualizaciones de documentación/validación. Consulta el PR asociado y la CI antes de considerar los cambios integrados.

## Estados
- VERDE: criterios ejecutados y aprobados con evidencia.
- ROJO: falló un criterio obligatorio.
- PENDIENTE: falta ejecutar o falta evidencia.
- BLOQUEADO: falta acceso, información, herramienta o autorización.
