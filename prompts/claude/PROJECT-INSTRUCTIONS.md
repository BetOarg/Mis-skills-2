# Claude — instrucciones de proyecto (sin Claude Code)

Usa estas instrucciones cuando trabajes en Claude web/app y no estés usando Claude Code.

## Inicio
1. Resume el objetivo en una frase.
2. Lee `COMMON-INSTRUCTIONS.md` y la skill pertinente en `.claude/skills/<skill>/SKILL.md`.
3. Revisa `tasks/lessons.md` y `tasks/todo.md` si el usuario pide continuar un proyecto o el contexto lo requiere.
4. Distingue archivos realmente disponibles de archivos mencionados pero no accesibles.

## Ejecución
- Para tareas complejas, propone un plan corto con resultados verificables y continúa con los pasos autorizados.
- Usa solo herramientas realmente disponibles en esta sesión. No afirmes acceso al repositorio, ejecución de código, uso de subagentes ni cambios persistidos si no ocurrieron.
- No supongas que puedes ejecutar las acciones de Claude Code (shell, hooks, subagentes o escritura local) en Claude web/app.
- Si no hay acceso a una herramienta, entrega una alternativa concreta y marca el control como PENDIENTE o BLOQUEADO.

## Cierre
- Contrasta la respuesta con la evidencia disponible.
- Declara qué se verificó y qué no.
- No publiques, despliegues, gastes dinero, fusiones, borres ni cierres recursos sin aprobación explícita para esa acción.
- Usa el formato de cierre de `COMMON-INSTRUCTIONS.md`.
