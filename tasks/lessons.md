# Lecciones aprendidas

## 2026-10-28 — Sincronizar el estado documental tras fusionar un PR
- **Patrón:** los archivos de seguimiento pueden conservar “PR abierto” después de que GitHub confirme la fusión.
- **Regla preventiva:** consultar el estado real del PR y el commit de destino; actualizar `tasks/todo.md` en el mismo cambio que corrige la documentación.
- **Verificación:** contrastar el texto de seguimiento con el estado real del PR.
- **Estado:** regla aplicada en esta rama.

## 2026-10-28 — La existencia de documentación no equivale a CI ejecutada
- **Patrón:** un protocolo manual no genera resultados reproducibles ni garantiza ejecución por cambio.
- **Regla preventiva:** mantener un validador ejecutable y un workflow automático para comprobaciones estáticas.
- **Verificación:** ejecutar el mismo comando localmente y en Actions; comprobar el resultado para el SHA exacto.
- **Límite:** la validación estática no prueba el comportamiento del modelo ni la activación de skills en cada plataforma.

## 2026-10-28 — Separar estados de compatibilidad por evidencia
- **Patrón:** una skill puede ser legible sin activarse automáticamente ni disponer de herramientas.
- **Regla preventiva:** registrar por separado acceso al contenido, aplicación de instrucciones, disponibilidad operativa y ejecución verificada.
- **Verificación:** usar `docs/compatibilidad.md` y registrar plataforma, modo, versión, método de carga, criterios y evidencias.
- **Estado:** las pruebas reales cruzadas siguen pendientes.

## 2026-10-28 — No confundir planes con acciones
- **Patrón:** describir comandos o cambios no demuestra que se hayan ejecutado.
- **Regla preventiva:** afirmar ejecución solo al observar el resultado real; distinguir propuestas, simulaciones y verificaciones.
- **Verificación:** conservar resultados específicos y no declarar VERDE ante checks ausentes, pendientes o ajenos al commit auditado.

## 2026-10-29 — La descripción de una skill es su clave de enrutamiento
- **Patrón:** descripciones que solo resumen la skill, sin indicar cuándo usarla ni qué skill vecina cubre el caso, hacen que skills solapadas compitan o no se activen.
- **Regla preventiva:** toda descripción dice qué hace, `Use when` con frases reales del usuario (ES/EN) y `Not for` con la skill vecina; máximo 1024 caracteres y sin dos puntos seguidos de espacio en YAML sin comillas.
- **Verificación:** `python scripts/validate_repo.py` comprueba formato; la activación real se prueba con prompts que deben y que no deben activar la skill, y queda PENDIENTE hasta tener evidencia.


## 2026-10-29 — Contar recurrencias entre conversaciones, no solo menciones
- **Patrón:** varias repeticiones dentro de un mismo chat pueden confundirse con recurrencia transversal.
- **Regla preventiva:** registrar por separado menciones, conversaciones distintas y días distintos; el umbral de más de tres se aplica a conversaciones distintas.
- **Verificación:** comprobar el identificador/fecha de cada conversación antes de declarar un patrón recurrente.


## 2026-10-29 — Separar interpretación, coordinación, ejecución y verificación
- **Patrón:** una sola skill generalista puede mezclar el significado del pedido, la coordinación de dependencias y la comprobación de resultados.
- **Regla preventiva:** usar smart-task-intake para interpretar, project-orchestrator para coordinar, skills especializadas para ejecutar y evidence-verifier para comprobar.
- **Verificación:** comprobar que cada responsabilidad tenga activadores y exclusiones propios y que el orquestador no duplique el procedimiento especializado.
- **Estado:** arquitectura propuesta en rama; validación CI pendiente.


## 2026-10-29 — Integrar skills de flujo sin convertirlas en una cadena obligatoria
- **Patrón:** agregar coordinadores, optimizadores, gestores de riesgo y verificadores puede aumentar la fricción si se ejecutan todos en cada pedido.
- **Regla preventiva:** definir una ruta mínima (intake → coordinación solo si hace falta → especialista → verificación) y disparadores explícitos para optimización, automatización, registro de decisiones y handoff.
- **Verificación:** incluir un caso multi-skill y un caso trivial adversarial que debe tomar la ruta corta.
- **Estado:** reglas y casos añadidos en rama; CI pendiente.
