# Claude Code — Orquestación de tareas

Este archivo complementa `COMMON-INSTRUCTIONS.md` y las skills de `.claude/skills/`. No reemplaza las instrucciones del proyecto ni concede permisos adicionales.

## Selección intuitiva de skills
- Pedido breve o contextual: smart-task-intake.
- Proyecto con varias etapas: project-orchestrator; para una tarea simple, ir directo a la skill especializada.
- Proceso lento o confuso: workflow-optimizer; eliminar pasos antes de automatizar.
- Proceso repetitivo, estable y delimitado: workflow-automation-architect.
- Decisiones con consecuencias o riesgos materiales: decision-and-risk-manager.
- Comprobación de resultados: evidence-verifier.
- Cambio de chat o sesión: context-handoff-manager.
No ejecutes todas las skills por defecto. Ruta mínima: interpretar → coordinar solo si hace falta → ejecutar con especialista → verificar. Respeta las aprobaciones y límites de COMMON-INSTRUCTIONS.md.

## 1. Planificación
- Para tareas no triviales, crea primero un plan verificable en `tasks/todo.md`.
- Define objetivo, pasos numerados, criterios de verificación y revisión final.
- Si la evidencia invalida una hipótesis, detén el enfoque afectado y actualiza el plan.
- No uses planificación extensa para arreglos obvios y de bajo riesgo.

## 2. Subagentes y trabajo paralelo
- Usa subagentes solo si están disponibles en el entorno actual.
- Asigna una tarea acotada y un resultado esperado a cada subagente.
- Prioriza investigación o archivos independientes; evita editar simultáneamente el mismo archivo o rama.
- Revisa evidencia, cambios y supuestos antes de integrar resultados.
- No afirmes que se usaron subagentes cuando no ocurrió.

## 3. Verificación antes de finalizar
- Lee el diff completo y comprueba que los cambios respeten el objetivo y el alcance.
- Ejecuta pruebas relevantes y revisa logs y resultados observables.
- Distingue análisis estático, pruebas unitarias, integración, compilación y pruebas funcionales.
- No marques VERDE si una comprobación obligatoria está pendiente o falló.
- Si una prueba no puede ejecutarse, indica exactamente cuál, por qué y qué evidencia falta.

## 4. Corrección autónoma y segura
- Ante un informe de error, inspecciona primero el estado real, reproduce cuando sea posible y busca la causa raíz.
- Corrige el defecto y añade una prueba de regresión cuando sea viable.
- No desactives pruebas, reduzcas criterios ni ocultes fallos para obtener CI verde.
- No cambies de rama, sobrescribas trabajo existente ni descartes cambios del usuario sin comprobar su estado y respetar las autorizaciones aplicables.

## 5. Seguimiento y lecciones
- Actualiza `tasks/todo.md` a medida que cambie el estado real.
- Tras una corrección significativa, registra en `tasks/lessons.md` el patrón, la regla preventiva y la comprobación temprana.
- Al cierre, registra un resumen de cambios, pruebas ejecutadas, resultados, riesgos y pendientes.

## 6. Reglas de autorización
- No fusionar PR, borrar ramas, cerrar issues/PR, publicar releases, desplegar ni modificar sistemas externos sin autorización explícita para esa acción.
- No incluir secretos en código, logs, capturas ni ejemplos.
- No declarar completada una acción externa basándose solo en haber redactado un comando o un plan.

## Lista de comprobación final
- [ ] El objetivo se cumplió y el diff es mínimo y coherente.
- [ ] Se revisaron los efectos colaterales y requisitos existentes.
- [ ] Se ejecutaron las pruebas disponibles y se registraron sus resultados reales.
- [ ] Las pruebas no ejecutadas están marcadas PENDIENTE o BLOQUEADO.
- [ ] Se actualizó el seguimiento y se registraron lecciones nuevas, si correspondía.
- [ ] No se realizaron acciones de alto impacto sin autorización.
