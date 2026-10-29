# Plan de trabajo — Mis-skills

## Estado verificado al iniciar esta rama
- `main` contiene 12 skills, incluida `workflow-automation-architect`.
- PR #4 está fusionado.
- CI post-merge run #41 (SHA `4c3cca1bb14105b479a84e1c178b47bf2ed066aa`) terminó en VERDE.
- No había PR abiertos al iniciar este trabajo.

## Mejora de flujo intuitivo — esta rama

### Las seis skills integradas
- [x] project-orchestrator — coordina y deriva trabajo.
- [x] smart-task-intake — interpreta pedidos naturales y breves.
- [x] context-handoff-manager — conserva continuidad entre sesiones.
- [x] evidence-verifier — comprueba resultados.
- [x] decision-and-risk-manager — registra decisiones y riesgos materiales.
- [x] workflow-optimizer — simplifica procesos antes de automatizar.
- [x] Conectar el routing y las reglas de activación para que no se ejecuten todas en cada pedido.
- [x] Crear `project-orchestrator` para coordinar proyectos y derivar a skills especializadas.
- [x] Crear `smart-task-intake` para interpretar instrucciones breves con contexto y límites de autoridad.
- [x] Crear `context-handoff-manager` para transferir estado verificable entre chats.
- [x] Crear `evidence-verifier` para comprobar afirmaciones contra fuentes autoritativas.
- [x] Añadir changelogs individuales.
- [x] Actualizar instrucciones comunes y routing.
- [x] Actualizar README y eliminar la referencia obsoleta que decía que workflow-automation-architect seguía fuera de main.
- [x] Añadir casos funcionales principales y adversariales para las seis skills.
- [x] Ampliar matriz de 12 a 18 skills: 90 combinaciones / 180 ejecuciones.
- [x] Ampliar validador estático a 18 skills.
- [ ] Ejecutar validación de rama en GitHub Actions.
- [ ] Confirmar que el PR #5 incluye los seis componentes y revisar que la ruta mínima evita invocar skills innecesarias.
- [ ] Revisar diff completo y corregir fallos.
- [ ] Abrir PR para revisión; no fusionar sin autorización explícita.
- [ ] Verificar CI posterior a cualquier futura fusión.

## Pruebas funcionales multiplataforma
- [ ] Ejecutar 180 casos reales: 18 skills × 5 plataformas × 2 casos.
- [ ] Registrar plataforma, producto/modo, modelo, SHA, método de carga, entrada, salida y evidencia.
- [ ] Mantener PENDIENTE todo caso sin ejecución/evidencia.
- [ ] No afirmar compatibilidad completa antes de revisar los 160 registros.

## Estados
- VERDE: controles ejecutados y aprobados con evidencia.
- ROJO: falló un control obligatorio.
- PENDIENTE: no ejecutado o evidencia incompleta.
- BLOQUEADO: falta acceso, herramienta, información o autorización.
