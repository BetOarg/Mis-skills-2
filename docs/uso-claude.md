# Usar Mis-skills en Claude

## Elegir el método según el entorno

La forma de usar una skill depende de si trabajas en Claude Code, Claude web u otro producto de Claude. No son entornos equivalentes.

### Claude Code con skills nativas

1. Clona o abre el repositorio en el entorno de trabajo.
2. Comprueba que la skill existe en `.claude/skills/<nombre>/SKILL.md`.
3. Lee la descripción y los requisitos de la skill.
4. Invoca la skill con el mecanismo admitido por la versión de Claude Code instalada, o formula una tarea que coincida con su descripción si la activación automática está documentada y disponible.
5. Para tareas de código, inspecciona la rama y los cambios existentes antes de editar.
6. Ejecuta las pruebas pertinentes y revisa el diff antes de cerrar.

La presencia del archivo no demuestra que se haya invocado. Confirma el procedimiento y el resultado observables en el entorno.

### Claude web o entornos sin acceso al repositorio

1. Abre el archivo `SKILL.md` de la skill elegida en GitHub.
2. Proporciona su contenido mediante las funciones de archivos o instrucciones que estén disponibles.
3. Indica explícitamente: “Aplica este procedimiento a la tarea actual”.
4. Comprueba que la respuesta sigue los criterios de aceptación de la skill.
5. No asumas acceso a terminal, GitHub, subagentes ni archivos locales si no están habilitados.

## Instrucciones específicas de Claude Code

Para reglas de orquestación, inicio de sesión y lista de comprobación final, consulta [prompts/claude-code/CLAUDE.md](../prompts/claude-code/CLAUDE.md). Este archivo complementa las instrucciones comunes y no implica que se hayan ejecutado pruebas.

## Selección de la skill

- Código, defectos y pruebas: [debug-and-fix](../.claude/skills/debug-and-fix/SKILL.md)
- CI y releases: [audit-ci-release](../.claude/skills/audit-ci-release/SKILL.md)
- Ramas, issues y PR: [github-project-operations](../.claude/skills/github-project-operations/SKILL.md)
- Google Ads y Meta Ads: [ads-campaign-builder](../.claude/skills/ads-campaign-builder/SKILL.md)
- Estrategia y documentos comerciales: [business-strategy-documents](../.claude/skills/business-strategy-documents/SKILL.md)
- Refactorización: [senior-code-refactor](../.claude/skills/senior-code-refactor/SKILL.md)
- Creación de skills: [agent-skill-generator](../.claude/skills/agent-skill-generator/SKILL.md)
- Documentación técnica: [technical-documentation-writer](../.claude/skills/technical-documentation-writer/SKILL.md)
- Commits y PR: [commit-pr-writer](../.claude/skills/commit-pr-writer/SKILL.md)
- Pruebas automatizadas: [automated-test-generator](../.claude/skills/automated-test-generator/SKILL.md)

## Reglas operativas

Lee primero [COMMON-INSTRUCTIONS.md](../COMMON-INSTRUCTIONS.md). Mantén la evidencia separada de las hipótesis; no declares pruebas o acciones que no se ejecutaron; solicita autorización para acciones de impacto; y marca como pendiente cualquier verificación que no puedas realizar.

## Prueba mínima de funcionamiento

Pide una tarea concreta, define criterios de aceptación y verifica la respuesta frente a esos criterios. Para una skill de programación, incluye un defecto reproducible y una prueba de regresión. Registra la versión de la skill y el entorno usado.

Una respuesta correcta en una sola prueba no demuestra compatibilidad universal ni garantiza que la skill se active automáticamente en futuras conversaciones.
