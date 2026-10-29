# Usar Mis-skills en ChatGPT

## Método recomendado: un Proyecto

Los Proyectos de ChatGPT permiten combinar instrucciones específicas y archivos de referencia. La disponibilidad y los límites de archivos dependen del plan y del espacio de trabajo.

1. En ChatGPT, crea un Proyecto llamado **Mis-skills** o uno separado para cada área de trabajo.
2. Abre **Ajustes del proyecto** y pega el contenido de [`COMMON-INSTRUCTIONS.md`](../COMMON-INSTRUCTIONS.md) en las instrucciones del proyecto. Si el campo tiene un límite de caracteres, conserva primero las reglas obligatorias, los estados y las restricciones de aprobación.
3. Adjunta desde este repositorio solo el `SKILL.md` pertinente para la tarea actual. Para trabajos repetidos, puedes dejar adjunta la skill que más uses y reemplazarla cuando cambie el tipo de tarea.
4. Al iniciar una tarea, indica explícitamente qué skill debe aplicar, por ejemplo: `Aplica la skill audit-ci-release del archivo adjunto. Inspecciona el estado actual y verifica cada conclusión.`
5. Si la skill no está adjunta, abre su archivo en GitHub y copia su contenido en el chat o adjúntalo como archivo de texto si la interfaz lo permite.

## Cómo elegir la skill

- Defectos de código o pruebas fallidas: `debug-and-fix/SKILL.md`
- CI, estado de release o artefactos: `audit-ci-release/SKILL.md`
- Ramas, issues, PR o workflows: `github-project-operations/SKILL.md`
- Google Ads o Meta Ads: `ads-campaign-builder/SKILL.md`
- Propuestas o estrategia comercial: `business-strategy-documents/SKILL.md`

## Importante
- Los archivos adjuntos aportan contexto; no garantizan la activación automática de una skill como en un entorno que soporte skills nativas.
- En planes con pocos archivos por Proyecto, no intentes adjuntar los diez archivos de la biblioteca. Usa las instrucciones comunes y la skill concreta que corresponda.
- Si se requiere actuar sobre GitHub, cuentas publicitarias u otros servicios, comprueba que la integración adecuada está conectada y autorizada. No afirmes haber realizado acciones externas si no se ejecutaron.

## Fuente oficial
La ayuda de OpenAI explica cómo agregar archivos e instrucciones a un Proyecto: https://help.openai.com/es-419/articles/10169521-projects-in-chatgpt
