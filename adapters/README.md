# Adaptadores por plataforma

Esta carpeta describe las diferencias de empaquetado e invocación; no duplica las skills fuente.

## Principio de arquitectura
- **Fuente única:** `.claude/skills/<skill>/SKILL.md` contiene el procedimiento completo de cada skill.
- **Reglas comunes:** `COMMON-INSTRUCTIONS.md` define calidad, seguridad, autorización y cierre.
- **Prompts de plataforma:** `prompts/<plataforma>/` adapta el flujo a cada producto.
- **Adaptadores:** documentan cómo proporcionar o empaquetar la fuente sin prometer capacidades inexistentes.
- **Pruebas:** `tests/README.md` y `tests/RESULTS.md` registran compatibilidad observada.

## Reglas
1. No mantengas copias editables de una misma skill en cada plataforma salvo que un formato de destino lo exija.
2. Si generas un paquete derivado, documenta su fuente, versión y método de generación.
3. No declares soporte nativo por poder leer Markdown.
4. Registra por separado lectura, aplicación de instrucciones, herramientas disponibles y ejecución verificada.
5. Comprueba la documentación oficial de la plataforma antes de actualizar instrucciones de instalación.
