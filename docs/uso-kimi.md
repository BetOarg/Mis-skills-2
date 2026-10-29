# Usar Mis-skills en Kimi

Kimi documenta una función de Skills personalizadas y un flujo para crear skills a partir de documentos o mediante conversación. La interfaz y las opciones pueden variar según el producto o modo de Kimi que estés usando.

## Opción A: crear una skill personalizada en Kimi Agent

1. Abre Kimi Agent y entra en el panel **Skills**.
2. Busca la opción para crear una skill personalizada. La documentación oficial describe dos vías: cargar documentos compatibles desde **Office Document to Skill**, o iniciar el creador escribiendo `/skill-creator` en el chat.
3. Usa como fuente el contenido de la skill que quieres portar desde este repositorio. Si el cargador no admite directamente `SKILL.md`, copia el contenido en el creador conversacional o conviértelo a un formato de documento admitido por la interfaz.
4. Crea primero una skill por tarea; no mezcles todos los procedimientos en una única skill genérica.
5. Revisa la descripción, el flujo, las reglas de aprobación y los ejemplos que genere Kimi. Corrige cualquier omisión antes de guardarla.
6. Prueba la skill con un caso real de bajo riesgo y comprueba si sigue el procedimiento y distingue los resultados verificados de los pendientes.

## Opción B: usar instrucciones en una conversación

1. Abre el `SKILL.md` correspondiente en GitHub.
2. Copia su contenido al chat de Kimi, o adjunta un documento si tu interfaz permite ese formato.
3. Pide: `Sigue este procedimiento para la tarea actual. No afirmes que ejecutaste acciones o pruebas que no realizaste. Respeta las aprobaciones obligatorias.`
4. Si necesitas reutilizarlo, guarda el procedimiento como skill personalizada o prompt rápido cuando la interfaz lo permita.

## Skills de esta biblioteca
- `debug-and-fix`: diagnóstico y corrección de defectos.
- `audit-ci-release`: auditoría de CI y preparación de releases.
- `github-project-operations`: operaciones de GitHub.
- `ads-campaign-builder`: campañas de Google Ads y Meta Ads.
- `business-strategy-documents`: estrategia y documentos comerciales.

## Reglas críticas
Conserva las reglas de `COMMON-INSTRUCTIONS.md`: verificar antes de actuar, no inventar resultados, buscar causa raíz, proteger datos y pedir aprobación antes de publicar, desplegar, gastar, fusionar, borrar o cerrar recursos.

La creación o importación de una skill no demuestra que esté funcionando correctamente. Prueba el resultado en el entorno concreto y registra qué se verificó.

## Fuentes oficiales de Kimi
- Uso de Skills en Agent Mode: https://www.kimi.ai/help/plugins-and-skills/use-skills-in-agent
- Qué son las Skills: https://www.kimi.com/en/help/plugins-and-skills/what-are-skills
