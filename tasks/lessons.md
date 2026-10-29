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
\n\n## 2026-10-29 — Contar recurrencias entre conversaciones, no solo menciones\n- **Patrón:** varias repeticiones dentro de un mismo chat pueden confundirse con recurrencia transversal.\n- **Regla preventiva:** registrar por separado menciones, conversaciones distintas y días distintos; el umbral de más de tres se aplica a conversaciones distintas.\n- **Verificación:** comprobar el identificador/fecha de cada conversación antes de declarar un patrón recurrente.\n