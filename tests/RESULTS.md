# Registro de pruebas funcionales

Este archivo registra ejecuciones reales. No marcar un caso VERDE sin evidencia observable.

## Alcance
Doce skills × cinco plataformas = 60 combinaciones y 120 ejecuciones mínimas (caso principal y adversarial). La matriz se mantiene PENDIENTE hasta ejecutar y documentar los casos.

## Reglas
1. Registrar producto/modo, versión y SHA o referencia exacta de la skill.
2. Registrar el método real de carga; no asumir activación automática.
3. Guardar entrada exacta, salida observada y criterios evaluados.
4. Para acciones externas, verificar el resultado en el sistema externo.
5. Usar datos ficticios; no introducir secretos, credenciales ni datos personales.
6. VERDE solo si ambos casos y todos los criterios obligatorios pasan; ROJO si falla uno; PENDIENTE si no se ejecutó; BLOQUEADO si no hay acceso o método viable.

## Matriz de cobertura

| Plataforma | Skill | Principal | Adversarial | Estado combinado |
|---|---|---|---|---|
| Claude Code | debug-and-fix | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | audit-ci-release | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | github-project-operations | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | ads-campaign-builder | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | business-strategy-documents | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | senior-code-refactor | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | agent-skill-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | technical-documentation-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | commit-pr-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | automated-test-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | chat-task-auditor | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude Code | workflow-automation-architect | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | debug-and-fix | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | audit-ci-release | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | github-project-operations | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | ads-campaign-builder | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | business-strategy-documents | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | senior-code-refactor | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | agent-skill-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | technical-documentation-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | commit-pr-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | automated-test-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | chat-task-auditor | PENDIENTE | PENDIENTE | PENDIENTE |
| Claude web/app | workflow-automation-architect | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | debug-and-fix | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | audit-ci-release | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | github-project-operations | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | ads-campaign-builder | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | business-strategy-documents | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | senior-code-refactor | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | agent-skill-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | technical-documentation-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | commit-pr-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | automated-test-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | chat-task-auditor | PENDIENTE | PENDIENTE | PENDIENTE |
| ChatGPT / Proyecto | workflow-automation-architect | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | debug-and-fix | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | audit-ci-release | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | github-project-operations | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | ads-campaign-builder | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | business-strategy-documents | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | senior-code-refactor | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | agent-skill-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | technical-documentation-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | commit-pr-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | automated-test-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | chat-task-auditor | PENDIENTE | PENDIENTE | PENDIENTE |
| Gemini | workflow-automation-architect | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | debug-and-fix | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | audit-ci-release | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | github-project-operations | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | ads-campaign-builder | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | business-strategy-documents | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | senior-code-refactor | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | agent-skill-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | technical-documentation-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | commit-pr-writer | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | automated-test-generator | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | chat-task-auditor | PENDIENTE | PENDIENTE | PENDIENTE |
| Kimi | workflow-automation-architect | PENDIENTE | PENDIENTE | PENDIENTE |

## Ficha por ejecución
- ID de prueba:
- Skill:
- Tipo: principal / adversarial
- Plataforma, producto y modo:
- Versión/modelo:
- Fecha UTC:
- Referencia/SHA de SKILL.md:
- Método de carga/invocación:
- Entrada exacta:
- Criterios y resultado:
- Respuesta observada:
- Herramientas y evidencia independiente:
- Estado: VERDE / ROJO / PENDIENTE / BLOQUEADO
- Fallos y próxima acción:

## Criterio de cierre
No declarar compatibilidad funcional completa hasta registrar y revisar las 120 ejecuciones. Un VERDE en una plataforma no implica VERDE en otra. La CI estática no reemplaza esta matriz.
