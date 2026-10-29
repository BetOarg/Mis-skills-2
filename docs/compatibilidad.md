# Protocolo de compatibilidad multiplataforma

## Objetivo

Evaluar por separado la lectura de las instrucciones, su aplicación, las capacidades operativas y la ejecución real de cada skill de Mis-skills en Claude Code, Claude web/app, ChatGPT, Gemini y Kimi.

La compatibilidad es una conclusión basada en pruebas, no una propiedad que se presupone por compartir Markdown. Las instrucciones por entorno están en `prompts/`; las guías de carga y empaquetado, en `adapters/`.

## Capas de compatibilidad

1. **Documental:** la plataforma puede acceder al contenido correcto de la skill.
2. **Aplicación de instrucciones:** la respuesta cumple los criterios de aceptación.
3. **Operativa:** están disponibles las herramientas y permisos requeridos.
4. **Ejecución verificada:** las acciones o pruebas se ejecutaron y sus resultados fueron observados.
5. **Cruzada:** los criterios aplicables se superaron en varias plataformas.

Una plataforma puede superar un nivel y no superar otro. Registra cada nivel por separado.

## Matriz de prueba

Mantén una fila por combinación de skill y plataforma.

| Campo | Qué registrar |
|---|---|
| Plataforma | Producto, modo y versión conocida |
| Skill | Nombre, ruta y commit o versión |
| Carga | Skill nativa, archivo, instrucciones o copia en el chat |
| Caso | Identificador y entrada usada |
| Esperado | Criterios de aceptación definidos antes de ejecutar |
| Observado | Respuesta y acciones que realmente ocurrieron |
| Herramientas | Herramientas disponibles y utilizadas |
| Evidencia | Resultado de pruebas, enlaces, registros o salida |
| Estado | VERDE, ROJO, PENDIENTE o BLOQUEADO |
| Limitaciones | Lo que no se pudo comprobar |

## Estados

- **VERDE:** se ejecutaron y aprobaron todos los criterios obligatorios aplicables, con evidencia suficiente.
- **ROJO:** la prueba se ejecutó y falló uno o más criterios obligatorios.
- **PENDIENTE:** la prueba no se ejecutó, está incompleta o falta evidencia.
- **BLOQUEADO:** falta acceso, permiso, información o una herramienta indispensable.

No marques VERDE cuando una comprobación obligatoria esté pendiente. Un resultado de una conversación no demuestra activación automática futura.

## Protocolo por skill

1. Fija la versión de la skill y el caso de prueba.
2. Define criterios de aceptación antes de ver la respuesta.
3. Confirma cómo se proporcionó o invocó la skill.
4. Ejecuta el caso principal y uno adversarial.
5. Evalúa cada criterio individualmente.
6. Registra evidencia y limitaciones.
7. Si falla, identifica la causa y repite después de corregir.

Utiliza las mismas entradas y criterios entre plataformas cuando sea posible. Si un criterio depende de una herramienta no disponible en una plataforma, registra esa diferencia; no lo sustituyas silenciosamente por una simulación.

## Reglas de honestidad

- Distingue la respuesta redactada de una acción externa real.
- No aceptes como evidencia una afirmación del asistente sobre una prueba que no se ejecutó.
- Guarda el resultado observado, no solo el resumen.
- No compares resultados de versiones diferentes sin anotarlo.
- No publiques información sensible en los registros.
- No declares que una plataforma soporta skills solo porque pueda leer Markdown.

## Alcance de la validación

La validación funcional es específica de plataforma + modo + versión + skill + caso. Las actualizaciones del proveedor, cambios de instrucciones o nuevas versiones de la skill pueden requerir repetir pruebas.
