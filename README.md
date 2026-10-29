# Mis-skills

Biblioteca de skills reutilizables para desarrollo de software, publicidad/negocio y auditoría/gestión de proyectos. Mantiene **una fuente única por skill**, reglas comunes y prompts/adaptadores separados por aplicación.

## Arquitectura

- **Skills fuente:** `.claude/skills/<nombre>/SKILL.md`. Contienen el procedimiento completo y su changelog. La ubicación también permite el uso nativo en Claude Code; en otras plataformas hay que seguir el adaptador correspondiente.
- **Reglas comunes:** [COMMON-INSTRUCTIONS.md](COMMON-INSTRUCTIONS.md), independiente de la interfaz.
- **Prompts por aplicación:** [Claude Code](prompts/claude-code/CLAUDE.md), [Claude web/app](prompts/claude/PROJECT-INSTRUCTIONS.md), [ChatGPT](prompts/chatgpt/PROJECT-INSTRUCTIONS.md), [Gemini](prompts/gemini/GEMINI.md) y [Kimi](prompts/kimi/KIMI.md).
- **Adaptadores:** instrucciones de carga, límites y verificación en [adapters/](adapters/README.md).
- **Pruebas:** casos reproducibles y matriz de resultados en [tests/README.md](tests/README.md) y [tests/RESULTS.md](tests/RESULTS.md).

## Licencia

El repositorio se distribuye bajo la [licencia MIT](LICENSE). Consulta el archivo para conocer los permisos y condiciones.

## Skills disponibles

- [debug-and-fix](.claude/skills/debug-and-fix/SKILL.md): diagnosticar y corregir defectos con pruebas de regresión.
- [audit-ci-release](.claude/skills/audit-ci-release/SKILL.md): auditar CI, repositorios y preparación de releases.
- [github-project-operations](.claude/skills/github-project-operations/SKILL.md): gestionar issues, pull requests, ramas y workflows.
- [ads-campaign-builder](.claude/skills/ads-campaign-builder/SKILL.md): diseñar campañas de Google Ads y Meta Ads.
- [business-strategy-documents](.claude/skills/business-strategy-documents/SKILL.md): preparar estrategias y documentos comerciales basados en hechos.
- [senior-code-refactor](.claude/skills/senior-code-refactor/SKILL.md): refactorizar con control de regresiones.
- [agent-skill-generator](.claude/skills/agent-skill-generator/SKILL.md): diseñar y validar skills reutilizables.
- [technical-documentation-writer](.claude/skills/technical-documentation-writer/SKILL.md): crear y auditar documentación técnica reproducible.
- [commit-pr-writer](.claude/skills/commit-pr-writer/SKILL.md): redactar commits, PR y notas de versión fieles al diff.
- [automated-test-generator](.claude/skills/automated-test-generator/SKILL.md): diseñar pruebas unitarias, de integración y regresión.
- [chat-task-auditor](.claude/skills/chat-task-auditor/SKILL.md): auditar recurrencias en chats y ordenar pendientes en bloques A/B/C.

Cada skill tiene su propio `CHANGELOG.md`.

## Uso por plataforma

| Plataforma | Prompt | Adaptador | Nota |
|---|---|---|---|
| Claude Code | [CLAUDE.md](prompts/claude-code/CLAUDE.md) | [Guía](adapters/claude-code/README.md) | Skills nativas en `.claude/skills/`; verificar invocación real. |
| Claude web/app | [Instrucciones de proyecto](prompts/claude/PROJECT-INSTRUCTIONS.md) | [Guía](adapters/claude/README.md) | No asumir herramientas de Claude Code. |
| ChatGPT | [Instrucciones de Proyecto](prompts/chatgpt/PROJECT-INSTRUCTIONS.md) | [Guía](adapters/chatgpt/README.md) | Adjuntar/indicar una skill no garantiza activación automática. |
| Gemini | [Prompt de trabajo](prompts/gemini/GEMINI.md) | [Guía](adapters/gemini/README.md) | Confirmar mecanismo disponible en el producto y versión. |
| Kimi | [Prompt de trabajo](prompts/kimi/KIMI.md) | [Guía](adapters/kimi/README.md) | Importación y herramientas dependen de la interfaz y versión. |

Las guías previas siguen disponibles: [Claude](docs/uso-claude.md), [ChatGPT](docs/uso-chatgpt.md), [Kimi](docs/uso-kimi.md), [instrucciones universales](docs/instrucciones-universales.md) y [protocolo de compatibilidad](docs/compatibilidad.md).

## Principios de compatibilidad

- Markdown compartido no significa compatibilidad operativa idéntica.
- No se duplican skills por plataforma salvo que un formato de destino lo requiera; las adaptaciones viven en prompts/adapters.
- Registra por separado acceso al contenido, aplicación de instrucciones, herramientas disponibles y ejecución verificada.
- No publiques, despliegues, gastes dinero, fusiones, borres ni cierres recursos sin autorización explícita.
- Consulta [COMMON-INSTRUCTIONS.md](COMMON-INSTRUCTIONS.md) para el flujo de inicio, planificación, validación y cierre.

## Documentación y mantenimiento

- [Instrucciones universales](docs/instrucciones-universales.md): reglas portátiles para otros proyectos y conversaciones.
- [Registro de lecciones](tasks/lessons.md): errores recurrentes y medidas preventivas.
- [Plan de trabajo](tasks/todo.md): tareas completadas y pendientes.
- [Protocolo de compatibilidad](docs/compatibilidad.md): criterios y procedimiento de evaluación.
- [Casos y criterios funcionales](tests/README.md) · [Matriz de resultados](tests/RESULTS.md).

## Pruebas funcionales

La matriz incluye once skills en Claude Code, Claude web/app, ChatGPT, Gemini y Kimi: **55 combinaciones plataforma-skill y 110 ejecuciones mínimas** (caso principal y adversarial). La matriz sigue en PENDIENTE hasta que las ejecuciones reales tengan evidencia registrada. La CI estática comprueba estructura y documentación; no demuestra compatibilidad funcional entre plataformas.

## Estado del proyecto

La reorganización de prompts y adaptadores está integrada en `main`. Esto no significa que las 100 pruebas funcionales estén terminadas ni que todas las plataformas hayan sido validadas. Consulta la matriz para el estado comprobado.

## Estados

- **VERDE:** criterios obligatorios ejecutados y aprobados con evidencia.
- **ROJO:** falló un criterio obligatorio.
- **PENDIENTE:** falta ejecutar una prueba o falta evidencia.
- **BLOQUEADO:** falta acceso, información, herramienta o autorización.
