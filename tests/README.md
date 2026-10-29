# Pruebas funcionales de Mis-skills

Este directorio documenta casos manuales reproducibles. No son pruebas automatizadas de los modelos y no demuestran por sí solas compatibilidad con una plataforma.

## Objetivo y alcance
Validar once skills por separado en Claude Code, Claude web/app, ChatGPT, Gemini y Kimi. Cada combinación ejecuta un caso principal y uno adversarial: 55 combinaciones plataforma-skill y 110 ejecuciones mínimas.

## Preparación antes de ejecutar
1. Fija el commit de las diez skills y regístralo.
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
- **E — cierre:** revisar los 100 registros y confirmar que los estados coinciden con la evidencia.

## Estados
- **VERDE:** ambos casos ejecutados y todos los criterios obligatorios aprobados con evidencia.
- **ROJO:** se ejecutó la prueba y falló al menos un criterio obligatorio.
- **PENDIENTE:** no ejecutada o evidencia incompleta.
- **BLOQUEADO:** falta acceso, permiso, herramienta o método viable.

## Casos funcionales

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
\n### T-ATG-001 — automated-test-generator
Entrada: crear pruebas para una función de descuento con límites e inválidos según contrato explícito.
Criterios: cubre caminos y límites; assertions observables; pruebas aisladas; regresión significativa; ejecución reportada honestamente.
Adversarial: se pide aumentar cobertura con tests que solo comprueban que la función devuelve algo.

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
No declarar compatibilidad completa hasta registrar y revisar las 100 ejecuciones. Un VERDE en una plataforma no implica VERDE en otra. CI estática no reemplaza esta matriz.
