# Mis-skills

Biblioteca de skills reutilizables para desarrollo, negocio, auditoría y gestión de proyectos. Mantiene una fuente única por skill, instrucciones comunes y adaptadores por plataforma.

## Arquitectura
- Skills fuente: `.claude/skills/<nombre>/SKILL.md`.
- Instrucciones compartidas: [COMMON-INSTRUCTIONS.md](COMMON-INSTRUCTIONS.md).
- Prompts y adaptadores por plataforma: [adapters/](adapters/README.md).
- Casos funcionales y evidencias: [tests/README.md](tests/README.md) · [tests/RESULTS.md](tests/RESULTS.md).

## Las 18 skills
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
- [decision-and-risk-manager](.claude/skills/decision-and-risk-manager/SKILL.md): registrar decisiones, alternativas, riesgos, responsables y aprobaciones.
- [workflow-optimizer](.claude/skills/workflow-optimizer/SKILL.md): simplificar procesos y eliminar fricción antes de automatizarlos.

Cada skill tiene su propio `CHANGELOG.md`.

## Flujo integrado e intuitivo
1. **Entender:** `smart-task-intake` interpreta instrucciones naturales y resuelve referencias con el contexto disponible. Pregunta solo si falta un dato que cambia materialmente el resultado o la seguridad.
2. **Coordinar:** `project-orchestrator` decide si hace falta coordinación, arma dependencias y deriva a las skills especializadas.
3. **Decidir y proteger:** `decision-and-risk-manager` registra decisiones, riesgos, responsables y aprobaciones cuando hay trade-offs relevantes.
4. **Simplificar:** `workflow-optimizer` elimina pasos, duplicaciones y fricción antes de proponer automatizaciones.
5. **Ejecutar:** las skills especializadas realizan el trabajo de su dominio; `workflow-automation-architect` diseña automatizaciones solo cuando el proceso ya está delimitado.
6. **Comprobar y continuar:** `evidence-verifier` valida los resultados; `context-handoff-manager` prepara la continuidad cuando cambia el chat o la sesión.

### Reglas de integración
- No ejecutar las seis skills en todas las tareas. Se activan solo cuando su función aporta valor.
- El flujo normal es intake → coordinación (si hace falta) → especialista(s) → verificación. Las otras tres se incorporan según la necesidad.
- Una responsabilidad, una fuente de verdad: el orquestador coordina; el optimizador simplifica; el arquitecto diseña automatizaciones; el gestor de riesgos registra decisiones; el verificador comprueba evidencia.
- Evitar repetir preguntas si la respuesta ya está disponible y sigue vigente.
- No confundir leer un archivo de skill con invocarla automáticamente en otra plataforma.
- La coordinación no amplía permisos ni reemplaza aprobaciones explícitas.

## Compatibilidad y seguridad
Markdown compartido no implica compatibilidad operativa idéntica. Registra por separado acceso al contenido, aplicación de instrucciones, herramientas disponibles y ejecución verificada. No publiques, despliegues, gastes dinero, fusiones, borres ni cierres recursos sin autorización explícita. No afirmes pruebas funcionales sin evidencia de ejecución real.

## Documentación
- [Registro de lecciones](tasks/lessons.md)
- [Plan de trabajo](tasks/todo.md)
- [Protocolo de compatibilidad](docs/compatibilidad.md)
- [Pruebas funcionales](tests/README.md)

## Pruebas funcionales
La matriz contempla 18 skills en cinco plataformas: 90 combinaciones y 180 ejecuciones mínimas (caso principal y adversarial). Todas permanecen PENDIENTES hasta disponer de evidencia real. CI estática no demuestra compatibilidad funcional.

## Estado del proyecto
Los cambios están en la rama `feat/intuitive-project-workflow` y el PR #5. Consulta el PR y la CI antes de considerar los cambios integrados.

## Estados
- VERDE: criterios ejecutados y aprobados con evidencia.
- ROJO: falló un criterio obligatorio.
- PENDIENTE: falta ejecutar o falta evidencia.
- BLOQUEADO: falta acceso, información, herramienta o autorización.
