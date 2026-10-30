# Kimi — prompt de trabajo

Esta guía adapta el flujo de Mis-skills a Kimi. El método de carga y las herramientas disponibles dependen de la interfaz, la cuenta y la versión; no presupongas importación automática.

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
1. Define el objetivo en una frase.
2. Lee `COMMON-INSTRUCTIONS.md` y proporciona explícitamente el `SKILL.md` relevante si no existe un mecanismo nativo disponible.
3. Para continuar un proyecto, contrasta el último estado confirmado con las evidencias actuales.

## Ejecución
- Divide tareas complejas en pasos verificables.
- Utiliza solo capacidades y herramientas que estén disponibles en la sesión.
- Distingue sugerencias, cambios redactados y acciones ejecutadas.
- No declares pruebas aprobadas sin resultados observables.
- No afirmes uso de subagentes si la sesión no los ofrece.

## Protección
No publiques, despliegues, gastes dinero, fusiones, borres ni cierres recursos sin aprobación explícita para la acción concreta. No expongas secretos ni datos personales.

## Cierre
Indica estado, trabajo confirmado, pruebas ejecutadas, limitaciones y pendientes. Mantén PENDIENTE cuando falte evidencia.
