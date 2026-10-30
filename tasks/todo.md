# Plan de trabajo — Mis-skills

## Estado actual de integración

- [x] Integrar las seis skills de flujo intuitivo.
- [x] Integrar las reglas de enrutamiento en instrucciones comunes y prompts de las cinco plataformas.
- [x] Añadir changelogs individuales.
- [x] Actualizar los casos funcionales y la matriz para 18 skills.
- [x] Actualizar el validador estático para exigir las 18 skills.
- [x] Revisar y fusionar el PR #5 en `main`.
- [x] Actualizar el README y el plan de trabajo después de la fusión.
- [x] Verificar CI posterior a la fusión: ejecución #92, SUCCESS, commit `825a55f28c51562e03a0bd1c85c2be5a3ada677e`.
- [x] Verificar CI del último commit documental en `main`: ejecución #96, SUCCESS, SHA `9adadcfef2ddc2526dff261b3e3f51d4a70a177a`.

## Validación funcional multiplataforma

- [ ] Ejecutar las 180 pruebas: 18 skills × 5 plataformas × 2 casos (principal y adversarial).
- [ ] Registrar para cada ejecución plataforma, producto/modo, versión/modelo, SHA de la skill, método de carga, entrada exacta, salida observada y evidencia.
- [ ] Validar por separado la coordinación integrada y el comportamiento adversarial de ruta mínima.
- [ ] Mantener PENDIENTE todo caso sin ejecución y evidencia real.
- [ ] Corregir fallos y repetir los casos afectados.
- [ ] No declarar compatibilidad funcional completa hasta revisar las 180 ejecuciones.

## Mantenimiento continuo

- [ ] Mantener sincronizados las skills fuente, sus changelogs, las instrucciones comunes, los adaptadores y la documentación.
- [ ] Revisar que el inventario de skills y los totales de la matriz coincidan con el repositorio.
- [ ] Registrar las lecciones de cada fallo o corrección en `tasks/lessons.md`.
- [ ] Antes de futuras fusiones, verificar diff, estado de CI y SHA del PR.

## Estados

- **VERDE:** controles ejecutados y aprobados con evidencia.
- **ROJO:** falló un control obligatorio.
- **PENDIENTE:** no ejecutado o evidencia incompleta.
- **BLOQUEADO:** falta acceso, herramienta, información o autorización.
