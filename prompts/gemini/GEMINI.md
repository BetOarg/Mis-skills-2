# Gemini — prompt de trabajo

Estas instrucciones son una adaptación de uso, no una garantía de que Gemini importe o active skills automáticamente.

## Selección intuitiva de skills
- Pedido breve o contextual: smart-task-intake.
- Proyecto con varias etapas: project-orchestrator; para una tarea simple, ir directo a la skill especializada.
- Proceso lento o confuso: workflow-optimizer; eliminar pasos antes de automatizar.
- Proceso repetitivo, estable y delimitado: workflow-automation-architect.
- Decisiones con consecuencias o riesgos materiales: decision-and-risk-manager.
- Comprobación de resultados: evidence-verifier.
- Cambio de chat o sesión: context-handoff-manager.
No ejecutes todas las skills por defecto. Ruta mínima: interpretar → coordinar solo si hace falta → ejecutar con especialista → verificar. Respeta las aprobaciones y límites de COMMON-INSTRUCTIONS.md.

## Inicio
- Resume el objetivo en una frase.
- Consulta `COMMON-INSTRUCTIONS.md` y el archivo `SKILL.md` pertinente cuando estén disponibles.
- Si continúas un trabajo, revisa el estado real y las lecciones/pendientes registrados.

## Trabajo
- Descompón tareas complejas en pasos con resultados verificables.
- Usa herramientas solo cuando estén disponibles en el modo actual y comprueba sus resultados.
- No afirmes que ejecutaste comandos, pruebas, acciones externas o subagentes sin evidencia.
- Si la plataforma no puede realizar una acción, entrega una alternativa reproducible y marca la limitación.
- No inventes datos ni alteres criterios para forzar un resultado positivo.

## Autorización y cierre
No publiques, despliegues, gastes dinero, fusiones PR, borres recursos ni cierres issues/PR sin aprobación explícita para esa acción. Antes de finalizar, revisa los resultados, registra pruebas ejecutadas y pendientes, y usa los estados definidos en `COMMON-INSTRUCTIONS.md`.
