---
name: chat-task-auditor
description: Analyze chat transcripts for repeated requests, action patterns, owners, tools, and deliverables, then organize raw notes into prioritized actionable tasks. Use when the user asks to audit chat history, find recurring requests, count repeated work, extract action items, clean up a backlog, or turn messy notes into a task list. Not for project status audits, repository issue triage, or creating a new agent skill.
---

# Chat Task Auditor — El limpiador de pendientes

## Objetivo
Convertir conversaciones, transcripciones, capturas de texto y notas desordenadas en información accionable, trazable y sin inventar datos. La skill tiene dos modos: **Auditoría de chats** y **Limpieza de pendientes**. Ejecuta uno o ambos según la solicitud.

## Principios obligatorios
- Analiza únicamente el material proporcionado o las fuentes a las que el usuario haya autorizado acceso. No afirmes haber revisado chats que no están disponibles.
- Conserva el contexto suficiente para no cambiar el sentido de una solicitud.
- Separa hechos explícitos, inferencias razonables y datos desconocidos.
- No inventes responsables, fechas, plazos, prioridades, herramientas, enlaces, archivos ni entregables.
- No cuentes varias menciones dentro de un mismo chat como apariciones en conversaciones diferentes.
- Si el corpus no permite contar conversaciones o días de forma fiable, informa el límite y ofrece el recuento verificable.
- Elimina ruido, quejas y repeticiones de la lista de tareas, pero no descartes restricciones, dependencias o riesgos que cambien la ejecución.
- No marques una tarea como completada solo porque alguien dijo que la haría; exige evidencia explícita de finalización.

## Modo 1 — Auditoría de tareas mediante análisis de chats

### Procedimiento
1. **Delimitar el corpus:** identifica qué conversaciones, transcripciones, fechas y fuentes están incluidas. Indica si el historial está completo o es parcial.
2. **Extraer acciones:** busca verbos de solicitud y compromiso (por ejemplo: enviar, revisar, crear, corregir, llamar, aprobar, publicar, pagar, reservar, entregar, verificar, fusionar). Incluye variantes y sinónimos; no conviertas una intención hipotética en una tarea.
3. **Normalizar solicitudes:** agrupa formulaciones equivalentes bajo una tarea canónica, manteniendo diferencias relevantes de proyecto, destinatario, canal o resultado.
4. **Contar recurrencia:** registra número de menciones, número de conversaciones distintas y número de días distintos. Solo clasifica como recurrente destacado si aparece **más de 3 veces en conversaciones distintas**. Si no se puede determinar la conversación, no declares que supera el umbral.
5. **Identificar quién pide qué:** registra solicitante, responsable de ejecución y destinatario por separado. Usa “no identificado” cuando no exista evidencia; no asumas que quien solicita también ejecuta.
6. **Detectar herramientas y entregables:** extrae herramientas, plataformas, enlaces, documentos, hojas de cálculo, correos, mensajes, imágenes, archivos, reuniones y aprobaciones mencionados. Diferencia entregable solicitado de entregable efectivamente producido.
7. **Extraer estado y dependencia:** marca pendiente, en curso, bloqueado o completado solo cuando el texto lo respalde. Registra dependencias y fechas explícitas.
8. **Presentar resultados:** primero los patrones recurrentes (>3 conversaciones); después otras tareas relevantes; finalmente datos faltantes y límites del análisis.

### Formato de salida de auditoría
- **Alcance:** fuentes, rango temporal y limitaciones.
- **Patrones recurrentes:** solicitud normalizada, frecuencia total, conversaciones distintas, días distintos, quién la solicita, quién la ejecuta (si se conoce), herramientas y entregables.
- **Otras acciones detectadas:** tareas relevantes que no superan el umbral.
- **Entregables mencionados:** tipo, destinatario y estado verificable.
- **Pendientes y dependencias:** únicamente los respaldados por el corpus.
- **Datos por confirmar:** responsable, fecha, enlace, archivo u otro dato ausente.

Usa una tabla si mejora la comparación. Incluye citas breves o referencias a conversación/fecha cuando estén disponibles para que el recuento sea auditable.

## Modo 2 — Limpieza de pendientes

### Procedimiento
1. Lee las notas y extrae cada acción concreta. Divide una frase si contiene varias acciones independientes.
2. Reescribe cada tarea comenzando con un verbo en imperativo: **Enviar**, **Revisar**, **Diseñar**, **Confirmar**, **Comprar**, **Llamar**, **Entregar**, etc.
3. Elimina relleno, quejas y comentarios que no afecten a la ejecución. Conserva contexto, destinatario, restricciones, dependencias y resultado esperado.
4. Asigna cada tarea a un único bloque:
   - **Bloque A — Foco prioritario:** tareas críticas que deben realizarse hoy. Incluye aquí solo si el texto indica vencimiento hoy, bloqueo crítico o urgencia explícita. Si no hay evidencia, no inventes “hoy”.
   - **Bloque B — Trabajo administrativo/rápido:** correos, mensajes, aprobaciones y acciones estimadas en menos de 15 minutos.
   - **Bloque C — Próximos pasos/seguimiento:** tareas importantes sin urgencia inmediata, tareas de más de 15 minutos que no sean críticas hoy, y seguimientos con fecha posterior o sin fecha.
5. Estima duración en minutos usando la complejidad descrita. Presenta una cifra aproximada y márcala como estimación; si faltan datos, usa “por estimar” en lugar de falsa precisión.
6. Conserva fecha límite, responsable, destinatario y dependencia cuando estén expresos. Si falta un dato esencial, indícalo como “por confirmar”.
7. Elimina duplicados exactos o equivalentes, pero no fusiones tareas que pertenezcan a proyectos o destinatarios diferentes.
8. Calcula subtotales de tiempo por bloque solo cuando todas las tareas de ese bloque tengan estimación numérica.

### Formato de salida de pendientes
## 🚨 Bloque A — Foco prioritario
- **[Verbo]** tarea y resultado esperado. [XX min] — responsable/fecha si se conocen.

## 📧 Bloque B — Trabajo administrativo/rápido
- **[Verbo]** tarea concreta. [XX min]

## 📌 Bloque C — Próximos pasos/seguimiento
- **[Verbo]** tarea concreta. [XX min]

Cierra con **Datos por confirmar** y **Tiempo estimado total** cuando corresponda. Si un bloque no contiene tareas, escribe “Sin tareas identificadas”.

## Reglas de priorización y estimación
- El orden A/B/C no sustituye una fecha límite explícita: conserva la fecha junto a la tarea.
- “Importante” no equivale automáticamente a “hoy”.
- No asignes prioridad alta por el tono emocional del mensaje.
- Para una tarea compuesta, estima por etapas o divide en subtareas si mejora la ejecución.
- No reduzcas artificialmente una tarea a menos de 15 minutos para colocarla en el Bloque B.
- No sumes tiempos “por estimar” al total.

## Ejemplos

### Good example 1 — Auditoría de recurrencia
Entrada: tres conversaciones diferentes mencionan “enviar el presupuesto” y una cuarta pide “mandar la cotización”; en dos aparece destinatario, y solo una menciona correo.
Salida correcta: normaliza como “Enviar presupuesto/cotización”; cuenta cuatro conversaciones distintas y cuatro apariciones; indica que supera el umbral; registra los destinatarios y el correo solo donde están explícitos; no inventa un responsable.

### Good example 2 — Limpieza de pendientes
Entrada: “Hoy vence el informe; tengo que mandarle a Laura el PDF. También responder el mail de Diego y preparar la presentación para la semana que viene.”
Salida correcta:
- Bloque A: **Enviar** el informe en PDF a Laura hoy. [10 min, estimación]
- Bloque B: **Responder** el correo de Diego. [10 min, estimación]
- Bloque C: **Preparar** la presentación para la semana que viene. [60 min, estimación]
No añade fechas ni responsables que no aparezcan en la entrada.

### Bad example — Falsa recurrencia y urgencia
Entrada: un único chat contiene cuatro veces “revisar el contrato”, sin fecha límite.
Salida incorrecta: “Revisar el contrato” aparece cuatro veces en conversaciones distintas y es prioridad A para hoy.
Por qué está mal: cuatro menciones en un chat no son cuatro conversaciones; no existe evidencia de vencimiento hoy. Debe registrarse como una conversación con cuatro menciones y prioridad por confirmar o C según el contexto.

## Criterios de finalización
- Todas las acciones concretas relevantes están extraídas y normalizadas.
- Los recuentos distinguen menciones, conversaciones y días.
- Las recurrencias destacadas superan estrictamente 3 conversaciones distintas.
- Solicitante, ejecutor, destinatario, herramientas y entregables no se confunden.
- Las tareas están en A/B/C, comienzan con imperativo y tienen estimaciones honestas.
- Las incertidumbres y limitaciones están visibles; no se inventó información.

## Registro de cambios
Consulta [CHANGELOG.md](CHANGELOG.md).
