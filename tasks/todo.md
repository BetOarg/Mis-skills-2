# Plan de trabajo — arquitectura multiplataforma y pruebas

## Objetivo
Mantener una fuente única por skill y separar los prompts/adaptadores por aplicación, con compatibilidad basada en evidencia.

## Cambios de arquitectura integrados en `main`
- [x] Auditar la estructura actual de main antes de editar.
- [x] Mantener las diez skills existentes y su changelog sin duplicarlas por plataforma.
- [x] Crear prompts separados para Claude web/app, ChatGPT, Gemini y Kimi.
- [x] Mantener la guía específica de Claude Code.
- [x] Añadir adaptadores por plataforma con límites y método de carga.
- [x] Actualizar el README para explicar la arquitectura de fuente única.
- [x] Ampliar el validador para exigir los nuevos prompts y adaptadores.
- [x] Ampliar la matriz a cinco plataformas distintas: Claude Code, Claude web/app, ChatGPT, Gemini y Kimi.

## Estado posterior a la integración
- [x] PR #7 fusionado en `main` mediante squash.
- [x] README actualizado para explicar la arquitectura, enlazar la documentación de mantenimiento y distinguir CI estática de pruebas funcionales.
- [x] CI estática de la rama del PR aprobada antes de integrar.
- [x] Confirmar resultado de CI posterior a la fusión: ejecución 40904380488 completada en VERDE.
- [ ] Eliminar ramas históricas tras la revisión: el conector disponible permite listar y comparar ramas, pero no borrar refs; la limpieza destructiva queda BLOQUEADA hasta disponer de una operación de borrado.

## Limpieza del repositorio
- [ ] Revisar la protección de `main`: la API de ramas informa `protected: false`; no hay una operación disponible en esta conexión para cambiar la protección.

## Nueva skill incorporada en esta rama\n- [x] Crear `chat-task-auditor` con auditoría de recurrencia de chats y limpieza A/B/C de pendientes.\n- [x] Añadir changelog, README, casos principal/adversarial y ampliar matriz a 11 skills.\n- [ ] Validar la nueva skill con CI y revisar el PR antes de integrar.\n\n## Pruebas funcionales pendientes
- [ ] Completar 100 ejecuciones reales: diez skills × cinco plataformas × caso principal y adversarial.
- [ ] Registrar versión/modo, método de carga, entrada exacta, salida observada y evidencia.
- [ ] Marcar una prueba VERDE solo cuando todos sus criterios obligatorios pasen.
- [ ] No afirmar compatibilidad multiplataforma completa antes de revisar las 100 ejecuciones.

## Estados
- VERDE: controles ejecutados y aprobados con evidencia.
- ROJO: falló un control obligatorio.
- PENDIENTE: no ejecutado o evidencia incompleta.
- BLOQUEADO: falta acceso, herramienta, información o autorización.
