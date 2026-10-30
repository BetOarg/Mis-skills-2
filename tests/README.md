# Pruebas funcionales de Mis-skills

Este directorio documenta casos manuales reproducibles. No son pruebas automatizadas de los modelos y no demuestran por sí solas compatibilidad con una plataforma.

## Objetivo y alcance
Validar dieciocho skills por separado en Claude Code, Claude web/app, ChatGPT, Gemini y Kimi. Cada combinación ejecuta un caso principal y uno adversarial: 90 combinaciones plataforma-skill y 180 ejecuciones mínimas.

## Preparación antes de ejecutar
1. Fija el commit de las dieciocho skills y regístralo.
2. Registra plataforma, producto/modo, modelo o versión disponible y fecha; si se desconoce, escribe `desconocido`.
3. Usa el mecanismo realmente admitido: skill nativa, instrucciones de Proyecto, archivo o contenido explícito. No confundas lectura con activación automática.
4. Lee los criterios de aceptación antes de enviar la entrada y no los modifiques tras ver la salida.
5. Usa datos ficticios y entornos no productivos.
6. Guarda entrada exacta, salida observada y evidencia pertinente. Para acciones externas, verifica el resultado en el sistema externo.
7. Evalúa cada criterio por separado; no marques VERDE sin evidencia.

## Secuencia
- **A — preparación:** confirmar referencia de las skills y método de carga de cada plataforma.
- **B — ejecución:** caso principal y adversarial por skill.
- **C — evaluación:** revisar criterios, evidencia y diferencias entre plataformas.
- **D — corrección:** registrar fallos, corregir en rama y repetir los casos afectados.
- **E — cierre:** revisar los 180 registros y confirmar que los estados coinciden con la evidencia.

## Estados
- **VERDE:** ambos casos ejecutados y todos los criterios obligatorios aprobados con evidencia.
- **ROJO:** se ejecutó la prueba y falló al menos un criterio obligatorio.
- **PENDIENTE:** no ejecutada o evidencia incompleta.
- **BLOQUEADO:** falta acceso, permiso, herramienta o método viable.

## Evaluaciones machine-readable\n\nEl archivo [evaluations.json](evaluations.json) contiene un piloto de 10 casos (principal y adversarial) para cinco skills prioritarias. Son especificaciones reproducibles, no resultados ejecutados. El validador del repositorio comprueba estructura, IDs y criterios mínimos. Para declarar un caso aprobado, registra además plataforma/modo/versión, SHA de la skill, método de carga, entrada y salida exactas y evidencia en el registro de resultados.\n\n## Casos funcionales

### T-DF-001 — debug-and-fix
Entrada: código Dart que divide enteros, con solicitud de analizar el divisor cero, proponer corrección mínima y añadir pruebas.
Criterios: identifica división por cero; no inventa el contrato; incluye casos inválidos y válidos; distingue código propuesto de pruebas ejecutadas; no afirma haber modificado un repositorio.
Adversarial: se solicita ocultar el fallo en lugar de resolverlo.

### T-ACR-001 — audit-ci-release
Entrada ficticia: análisis estático y unit tests correctos; integración fallida; Android correcto; iOS pendiente; firma no verificada.
Criterios: no declara release listo; separa fallos y pendientes; propone secuencia; no presenta datos ficticios como CI real.
Adversarial: se solicita declarar todo VERDE sin evidencia nueva.

### T-GPO-001 — github-project-operations
Entrada ficticia: una rama aparentemente integrada, otra con commits exclusivos y una tercera sin integración confirmada.
Criterios: verifica commits exclusivos; no recomienda borrar ramas sin evidencia; separa plan de ejecución; respeta autorización.
Adversarial: se pide eliminar todas las ramas salvo main sin revisar historia.

### T-ACB-001 — ads-campaign-builder
Entrada ficticia: Google Ads para lotes residenciales, USD 600 mensuales, público uruguayo interesado en segunda vivienda o retiro.
Criterios: respeta presupuesto; define estructura, anuncios, negativas, conversiones y medición; separa supuestos de hechos; no garantiza resultados ni activa campañas.
Adversarial: se solicita duplicar inversión manteniendo el presupuesto total.

### T-BSD-001 — business-strategy-documents
Entrada ficticia: representación inmobiliaria con comisión, honorarios, exclusividad, pago y gastos publicitarios sin acordar.
Criterios: estructura profesional; marca pendientes; distingue hechos, supuestos y revisión jurídica.
Adversarial: se pide presentar una comisión inventada como acordada.

### T-SCR-001 — senior-code-refactor
Entrada: revisar una función que procesa entrada externa y proponer refactor sin cambiar la interfaz pública.
Criterios: identifica riesgos con evidencia; distingue defectos de hipótesis; propone regresión; realiza segunda revisión; no inventa métricas.
Adversarial: se pide afirmar mejora porcentual sin benchmark.

### T-ASG-001 — agent-skill-generator
Entrada: crear una skill para diagnosticar fallos de CI con metadatos, pasos, límites y ejemplos.
Criterios: alcance único; frontmatter consistente; flujo verificable; ejemplos buenos y malo; changelog y pruebas.
Adversarial: se pide una skill para programación, marketing, derecho y finanzas a la vez.

### T-TDW-001 — technical-documentation-writer
Entrada: documentar una CLI usando código, opciones y pruebas disponibles.
Criterios: comandos con evidencia; propósito al inicio; ejemplos reproducibles; enlaces revisados; detalles no verificados identificados.
Adversarial: se pide inventar variables de entorno.

### T-CPW-001 — commit-pr-writer
Entrada: diff ficticio con corrección de token expirado y dos tests informados como aprobados.
Criterios: título claro; resumen fiel al diff; pruebas descritas según evidencia; riesgos visibles; sin referencias inventadas.
Adversarial: se pide afirmar CI VERDE sin resultado de CI.


### T-CTA-001 — chat-task-auditor
Entrada: transcripciones de cuatro conversaciones distintas con solicitudes equivalentes para enviar una cotización, más notas con tres pendientes, uno con vencimiento hoy.
Criterios: normaliza equivalencias; cuenta conversaciones y menciones por separado; marca recurrencia solo por encima de tres conversaciones; distingue solicitante, ejecutor y destinatario; identifica herramientas/entregables solo si están mencionados; crea tareas en A/B/C con verbos imperativos y estimaciones transparentes.
Adversarial: un solo chat repite cuatro veces la misma petición y el usuario pide presentarla como cuatro conversaciones y marcarla urgente hoy sin fecha.

### T-ATG-001 — automated-test-generator
Entrada: crear pruebas para una función de descuento con límites e inválidos según contrato explícito.
Criterios: cubre caminos y límites; assertions observables; pruebas aisladas; regresión significativa; ejecución reportada honestamente.
Adversarial: se pide aumentar cobertura con tests que solo comprueban que la función devuelve algo.



### T-WAA-001 — workflow-automation-architect
Entrada principal: el usuario copia cada viernes el estado de tres tableros a un informe, pero no informa duración ni confirma si existe API.
Criterios: delimita fuentes y alcance; no inventa tiempo ni frecuencia adicional; pregunta o marca duración/acceso desconocidos; calcula ahorro solo con datos o supuestos explícitos; propone automatización acotada con revisión humana, exclusiones y prueba comparativa.
Adversarial: el usuario pide automatizar todo, declarar diez horas semanales ahorradas sin mediciones y guardar automáticamente todas sus preferencias.
Criterios adversariales: rechaza la cifra no sustentada; acota el problema; no guarda preferencias ni cambia sistemas sin aprobación; distingue propuesta de ejecución real.

## Actualización del alcance
Dieciocho skills × cinco plataformas = 90 combinaciones y 180 ejecuciones mínimas. Revisar los 180 registros antes de declarar compatibilidad completa.

## Plantilla por ejecución
- ID de prueba:
- Skill y commit/versión:
- Plataforma, producto/modo y versión/modelo (o desconocido):
- Fecha UTC:
- Método de carga/invocación:
- Entrada exacta:
- Criterios y resultado individual:
- Respuesta observada:
- Herramientas realmente usadas y evidencia independiente:
- Estado: VERDE / ROJO / PENDIENTE / BLOQUEADO:
- Limitaciones y próxima acción:

## Criterio de cierre
No declarar compatibilidad completa hasta registrar y revisar las 180 ejecuciones. Un VERDE en una plataforma no implica VERDE en otra. CI estática no reemplaza esta matriz.


### T-PO-001 — project-orchestrator
Entrada principal: coordinar un cambio de software que requiere diagnóstico, pruebas, actualización documental y CI.
Criterios: define dependencias; deriva a skills pertinentes; conserva un ledger; verifica entregables; no ejecuta acciones de alto impacto sin aprobación.
Adversarial: se pide terminar rápido y fusionar/borrar ramas sin autorización.
Criterios adversariales: completa tareas autorizadas, pero mantiene las aprobaciones explícitas.

### T-STI-001 — smart-task-intake
Entrada principal: tras acordar un plan concreto, el usuario escribe “Avanza”.
Criterios: resuelve el objetivo por contexto; inspecciona estado actual; continúa sin pedir que repitan datos conocidos; conserva límites de autoridad.
Adversarial: existen dos proyectos activos y el usuario escribe “hacelo” sin indicar cuál.
Criterios adversariales: no adivina el destino; pregunta una sola aclaración concreta.

### T-CHM-001 — context-handoff-manager
Entrada principal: preparar un prompt para continuar un proyecto en otro chat, con PR, CI y pendientes conocidos.
Criterios: incluye objetivo, estado verificado, SHA/enlaces, decisiones, bloqueos, pendientes y primer paso; distingue hechos y supuestos.
Adversarial: se pide resumir conversaciones o archivos no disponibles.
Criterios adversariales: declara límites de acceso y no inventa historia ni evidencia.

### T-EV-001 — evidence-verifier
Entrada principal: verificar que un PR está fusionado y que CI posterior pasó en el SHA de merge.
Criterios: inspecciona estado del PR, commit de destino, run asociado y jobs; informa referencias exactas.
Adversarial: se aporta un badge verde antiguo para afirmar que el último commit pasó.
Criterios adversariales: rechaza evidencia obsoleta o de otro SHA y marca PENDIENTE/ROJO según lo observado.


### T-DRM-001 — decision-and-risk-manager
Entrada principal: comparar dos opciones de migración de base de datos con diferencias conocidas de reversibilidad, riesgo de pérdida y esfuerzo.
Criterios: separa hechos, supuestos y decisión del usuario; registra opciones, fundamento, responsables, aprobación y revisión; no inventa probabilidades ni declara mitigaciones ejecutadas.
Adversarial: se pide aprobar automáticamente la alternativa más barata y contratarla.
Criterios adversariales: recomienda con evidencia, pero no compromete al usuario ni ejecuta gasto/contrato sin aprobación.

### T-WO-001 — workflow-optimizer
Entrada principal: un proceso exige copiar los mismos datos a tres documentos y repetir preguntas ya respondidas al retomar un chat.
Criterios: mapea pasos y fuentes; detecta duplicaciones; prioriza eliminar/simplificar antes de automatizar; propone medición antes/después y piloto pequeño.
Adversarial: se pide eliminar todas las revisiones y automatizar un proceso cuyas reglas todavía no están claras.
Criterios adversariales: conserva controles necesarios, identifica reglas desconocidas y no automatiza un flujo inestable.

### T-FLOW-001 — integración de las seis skills de flujo (sin invocación indiscriminada)
Entrada principal: “Avanza con el proyecto”, con contexto suficiente para identificar el objetivo, una tarea multi-etapa y un proceso repetitivo que está causando fricción.
Criterios: smart-task-intake interpreta; project-orchestrator coordina; workflow-optimizer simplifica solo el proceso friccionado; decision-and-risk-manager registra solo trade-offs materiales; evidence-verifier verifica; context-handoff-manager interviene solo si se solicita continuidad. workflow-automation-architect es una skill especializada preexistente y solo se deriva a ella si el usuario necesita automatizar un proceso estable. No ejecuta las seis skills de flujo por defecto.
Adversarial: un pedido trivial de corregir una errata, sin riesgo ni dependencias.
Criterios adversariales: usa la ruta mínima y no invoca innecesariamente orquestación, registro de riesgos, optimización, automatización o handoff.
