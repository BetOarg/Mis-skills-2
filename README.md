# Mis-skills

Biblioteca de Agent Skills reutilizables para desarrollo de software, publicidad y negocio, auditoría y gestión de proyectos. Mantiene una fuente única por skill, reglas compartidas y adaptadores para distintas plataformas.

## Arquitectura

- **Skills fuente:** `.claude/skills/<nombre>/SKILL.md`. Cada skill incluye su `CHANGELOG.md`.
- **Reglas comunes:** [COMMON-INSTRUCTIONS.md](COMMON-INSTRUCTIONS.md).
- **Prompts por plataforma:**
  - [Claude Code](prompts/claude-code/CLAUDE.md)
  - [Claude web/app](prompts/claude/PROJECT-INSTRUCTIONS.md)
  - [ChatGPT](prompts/chatgpt/PROJECT-INSTRUCTIONS.md)
  - [Gemini](prompts/gemini/GEMINI.md)
  - [Kimi](prompts/kimi/KIMI.md)
- **Adaptadores:** [guía general](adapters/README.md), con instrucciones específicas por plataforma.
- **Pruebas:** [protocolo funcional](tests/README.md), [matriz de resultados](tests/RESULTS.md) y [casos machine-readable](tests/evaluations.json).
- **Investigación:** [auditoría comparativa de Agent Skills](docs/auditoria-comparativa-skills-2026-10.md).

## Skills disponibles

El repositorio contiene **18 skills**:

| Skill | Función |
|---|---|
| [debug-and-fix](.claude/skills/debug-and-fix/SKILL.md) | Diagnosticar y corregir defectos con pruebas de regresión. |
| [audit-ci-release](.claude/skills/audit-ci-release/SKILL.md) | Auditar CI, repositorios y releases. |
| [github-project-operations](.claude/skills/github-project-operations/SKILL.md) | Gestionar issues, pull requests, ramas y workflows. |
| [ads-campaign-builder](.claude/skills/ads-campaign-builder/SKILL.md) | Diseñar campañas Google Ads y Meta Ads. |
| [business-strategy-documents](.claude/skills/business-strategy-documents/SKILL.md) | Preparar estrategias y documentos comerciales. |
| [senior-code-refactor](.claude/skills/senior-code-refactor/SKILL.md) | Refactorizar con control de regresiones. |
| [agent-skill-generator](.claude/skills/agent-skill-generator/SKILL.md) | Diseñar y validar skills reutilizables. |
| [technical-documentation-writer](.claude/skills/technical-documentation-writer/SKILL.md) | Documentar sistemas con evidencia. |
| [commit-pr-writer](.claude/skills/commit-pr-writer/SKILL.md) | Redactar commits y pull requests fieles al diff. |
| [automated-test-generator](.claude/skills/automated-test-generator/SKILL.md) | Diseñar pruebas automatizadas. |
| [chat-task-auditor](.claude/skills/chat-task-auditor/SKILL.md) | Auditar recurrencias en chats y ordenar pendientes. |
| [workflow-automation-architect](.claude/skills/workflow-automation-architect/SKILL.md) | Auditar procesos recurrentes y diseñar automatizaciones medibles. |
| [project-orchestrator](.claude/skills/project-orchestrator/SKILL.md) | Coordinar tareas, dependencias y skills especializadas. |
| [smart-task-intake](.claude/skills/smart-task-intake/SKILL.md) | Interpretar pedidos naturales y referencias usando el contexto disponible. |
| [context-handoff-manager](.claude/skills/context-handoff-manager/SKILL.md) | Preparar traspasos de contexto entre chats y sesiones. |
| [evidence-verifier](.claude/skills/evidence-verifier/SKILL.md) | Verificar resultados y afirmaciones contra fuentes autoritativas. |
| [decision-and-risk-manager](.claude/skills/decision-and-risk-manager/SKILL.md) | Registrar decisiones, alternativas, riesgos y aprobaciones. |
| [workflow-optimizer](.claude/skills/workflow-optimizer/SKILL.md) | Simplificar procesos y eliminar pasos innecesarios antes de automatizar. |

## Flujo integrado de trabajo

Las seis skills de flujo se coordinan con las skills especialistas. **No se ejecutan todas en cada solicitud**: se activa cada una solo cuando aporta valor.

1. **Interpretar — `smart-task-intake`:** entiende el pedido, identifica referencias y aprovecha el contexto disponible. Pregunta únicamente cuando falta un dato material.
2. **Coordinar — `project-orchestrator`:** determina si la tarea necesita varias etapas, dependencias o especialistas. Para tareas simples, mantiene la ruta mínima.
3. **Optimizar — `workflow-optimizer`:** detecta pasos redundantes, fricción y oportunidades de simplificación cuando el proceso lo necesita.
4. **Gestionar decisiones y riesgos — `decision-and-risk-manager`:** registra alternativas, impactos, riesgos y aprobaciones cuando existen decisiones relevantes.
5. **Ejecutar y verificar — skills especialistas + `evidence-verifier`:** la skill de dominio realiza el trabajo y el verificador contrasta los resultados con evidencia. `workflow-automation-architect` interviene solo cuando hay un proceso estable y delimitado que conviene automatizar.
6. **Transferir — `context-handoff-manager`:** prepara un traspaso cuando se cambia de chat/sesión o se solicita continuidad.

### Reglas de coordinación

- Ruta normal: interpretación → coordinación si hace falta → especialista(s) → verificación.
- Optimización, gestión de riesgos y traspaso se incorporan según el contexto; no son pasos obligatorios en todos los pedidos.
- Evitar preguntas repetidas si la respuesta ya está disponible y sigue vigente.
- El orquestador coordina; no duplica el trabajo de las skills especialistas.
- Leer un archivo de skill no demuestra que una plataforma la haya invocado automáticamente.
- La coordinación no amplía permisos ni sustituye la aprobación explícita del usuario.

## Compatibilidad y seguridad

El formato Markdown compartido no garantiza compatibilidad operativa idéntica. Para cada plataforma se deben registrar por separado:

- Acceso al contenido de la skill.
- Aplicación efectiva de sus instrucciones.
- Herramientas y permisos disponibles.
- Ejecución real y evidencia verificable.

No publicar, desplegar, gastar dinero, fusionar, borrar ni cerrar recursos sin autorización explícita. No introducir secretos ni datos personales en casos de prueba. No declarar una prueba funcional VERDE sin evidencia observable.

## Documentación y mantenimiento

- [Instrucciones universales](docs/instrucciones-universales.md)
- [Registro de lecciones](tasks/lessons.md)
- [Plan de trabajo](tasks/todo.md)
- [Protocolo de compatibilidad](docs/compatibilidad.md)
- [Protocolo de pruebas funcionales](tests/README.md)
- [Matriz de cobertura y resultados](tests/RESULTS.md)

## Alcance de las pruebas funcionales

La matriz contempla **18 skills × 5 plataformas = 90 combinaciones** y **180 ejecuciones mínimas**: un caso principal y uno adversarial por combinación.

Plataformas contempladas: Claude Code, Claude web/app, ChatGPT (Proyecto), Gemini y Kimi.

Todas las ejecuciones permanecen **PENDIENTES** hasta que se realicen y documenten con plataforma/producto/modo, versión/modelo, referencia o SHA de la skill, método de carga, entrada exacta, salida observada y evidencia. La CI estática valida estructura y documentación; no demuestra compatibilidad funcional ni coordinación real entre plataformas.

## Auditoría comparativa de Agent Skills — octubre de 2026

Se revisaron las referencias de [Matt Pocock](https://github.com/mattpocock/skills), [Anthropic Skills](https://github.com/anthropics/skills), [Claude Plugins Official](https://github.com/anthropics/claude-plugins-official), [Google Skills](https://github.com/google/skills), [OpenAI Skills](https://github.com/openai/skills) y [NVIDIA Skills](https://github.com/NVIDIA/skills). La auditoría y sus conclusiones están en [el informe comparativo](docs/auditoria-comparativa-skills-2026-10.md).

Principales mejoras incorporadas a cinco skills:
- `debug-and-fix`: reproducción, diagnóstico falsable y pruebas de regresión.
- `audit-ci-release`: evaluación conductual y revisión de supply chain.
- `github-project-operations`: manifests, permisos, procedencia y SHA inmutables.
- `ads-campaign-builder`: experimentación, atribución, guardrails y economía unitaria.
- `business-strategy-documents`: registro de evidencia, escenarios y matriz de negociación.

**Nota de vigencia:** `openai/skills` está marcado como deprecated; para ejemplos actuales de plugins Codex consultar [openai/plugins](https://github.com/openai/plugins).

### Evaluaciones piloto

[`tests/evaluations.json`](tests/evaluations.json) contiene diez casos (uno principal y uno adversarial para cada una de las cinco skills mejoradas). Son definiciones de prueba, no resultados ejecutados. La CI valida su estructura; la evaluación conductual requiere ejecución real y registro de evidencia.

## Estado del repositorio

- Repositorio principal: `main`.
- La integración de las seis skills de flujo se realizó mediante el PR [#5](https://github.com/BetOarg/Mis-skills-2/pull/5).
- La auditoría comparativa y las mejoras de cinco skills se integraron mediante el PR [#6](https://github.com/BetOarg/Mis-skills-2/pull/6), fusionado el 30 de octubre de 2026.
- Commit actual de integración: `0e23dd3accb520fd4bef8b8dbd37fa31812b6a04`.
- CI posterior a la fusión: [Repository validation #126](https://github.com/BetOarg/Mis-skills-2/actions/runs/40994558460), **SUCCESS**, sobre el mismo SHA.
- CI de la PR #6: [ejecución #125](https://github.com/BetOarg/Mis-skills-2/actions/runs/40994531078), **SUCCESS**.
- La validación estructural comprueba archivos requeridos, 18 skills, frontmatter, changelogs, matriz, los diez casos piloto y enlaces Markdown internos. No ejecuta modelos ni demuestra activación o calidad conductual.
- Los diez casos piloto están definidos, pero su ejecución real permanece **PENDIENTE**.
- Las 180 pruebas funcionales (18 skills × 5 plataformas × 2 casos) permanecen **PENDIENTES** hasta registrar evidencia por plataforma.
- La rama `main` no tenía protección habilitada al momento de la comprobación; su configuración requiere una decisión de gobernanza separada.

## Estados

- **VERDE:** criterios ejecutados y aprobados con evidencia.
- **ROJO:** falló un criterio obligatorio.
- **PENDIENTE:** falta ejecutar o falta evidencia.
- **BLOQUEADO:** falta acceso, información, herramienta o autorización.
