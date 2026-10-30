# Auditoría comparativa de Agent Skills — octubre de 2026

## Objetivo y alcance

Comparar las prácticas públicas de seis repositorios de referencia con la arquitectura vigente de Mis-skills-2 y aplicar mejoras acotadas a cinco skills prioritarias. Se revisaron README, especificaciones, ejemplos de skills, manifests y material de evaluación disponible en las ramas principales consultadas.

Fecha de revisión: 2026-10-29 (Argentina). Las referencias enlazan a las ramas por defecto; salvo donde se indica un SHA local, el contenido remoto puede cambiar. Esta auditoría no implica certificación de seguridad ni compatibilidad funcional entre modelos.

## Estado del repositorio auditado

- Repositorio: [BetOarg/Mis-skills-2](https://github.com/BetOarg/Mis-skills-2), privado.
- Rama base: `main`; commit observado: `af40dcfc9b2c05960375c3fba34bb0c2683bedd6`.
- Última ejecución observada: [Repository validation #98](https://github.com/BetOarg/Mis-skills-2/actions/runs/40984268882), SUCCESS, asociada al mismo SHA.
- La CI actual ejecuta `python scripts/validate_repo.py`: valida estructura, frontmatter, changelogs y enlaces internos; no ejecuta modelos ni pruebas de comportamiento.
- La matriz documentada conserva 18 skills × 5 plataformas × 2 casos = 180 ejecuciones mínimas, todas PENDIENTES en el registro leído.
- La rama `main` aparece sin protección habilitada en el endpoint consultado. Se registra como riesgo de gobernanza, no se modifica en esta tarea.

## Hallazgos por fuente

### 1. [mattpocock/skills](https://github.com/mattpocock/skills)

**Aportes observados**
- Skills pequeñas, composables y con separación entre invocación explícita por usuario y activación por el modelo.
- TDD basado en ciclos verticales: una prueba de comportamiento, una implementación mínima y repetición.
- En debugging complejo, primero construir una señal de feedback que realmente falle con el síntoma; después minimizar, formular hipótesis falsables, instrumentar y verificar.
- Uso de vocabulario compartido y decisiones de arquitectura para reducir ambigüedad.

**Aplicación:** incorporar loops de diagnóstico proporcionales a la complejidad y criterios de calidad para pruebas de regresión; no imponer el ritual completo a defectos triviales.

### 2. [anthropics/skills](https://github.com/anthropics/skills)

**Aportes observados**
- Una skill es una carpeta autocontenida de instrucciones, scripts y recursos, con `SKILL.md` como punto de entrada.
- El repositorio publica ejemplos, plantilla y especificación; advierte que ejemplos y comportamientos deben probarse en el entorno real.
- La especificación de Agent Skills se mantiene en [agentskills.io/specification](https://agentskills.io/specification).
- La licencia puede variar por directorio; algunos materiales de documentos se declaran source-available y no open source.

**Aplicación:** mantener fuente única por skill, recursos locales versionados, licencia/procedencia revisadas y compatibilidad demostrada por pruebas, no inferida por formato Markdown.

### 3. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**Aportes observados**
- Separación entre manifest del plugin, skills, comandos, agentes y configuración MCP.
- Marketplace con esquema explícito, fuentes de plugins y posibilidad de fijar commit SHA.
- Los identificadores publicados son inmutables; renombres cosméticos se hacen mediante displayName y los cambios inevitables usan un mapa de migración.
- Advertencia expresa: confiar en un plugin requiere revisar el software, MCP, archivos y scripts incluidos; el listado no garantiza seguridad.

**Aplicación:** añadir controles de manifest, slug estable, origen y SHA, permisos, hooks, scripts, MCP y credenciales antes de recomendar instalar o distribuir un bundle.

### 4. [google/skills](https://github.com/google/skills)

**Aportes observados**
- Catálogo amplio, organizado por dominio, con plugins y skills especializadas; incluye ejemplos de manifests para distintas superficies.
- El flujo de evaluación de Agent Platform estructura preparación de datos, simulación/ejecución, evaluación y ciclos de mejora.
- Documenta datasets de un turno y multi-turno, con esquemas tipados y advertencias sobre errores silenciosos de formato.

**Aplicación:** definir casos estructurados y reproducibles, conservar entrada/salida de referencia y contemplar conversaciones multi-turno cuando la skill coordina herramientas o agentes. No trasladar SDKs de Google a Mis-skills si no son necesarios.

### 5. [openai/skills](https://github.com/openai/skills)

**Hallazgo crítico de vigencia:** el README del repositorio declara que está DEPRECATED y remite a [openai/plugins](https://github.com/openai/plugins) para ejemplos actuales de Codex.

**Aportes y corrección de referencia**
- El repositorio antiguo sigue siendo útil para estudiar ejemplos de skills y sus evaluaciones, pero no debe usarse como guía vigente de instalación.
- El repositorio actual [openai/plugins](https://github.com/openai/plugins) documenta plugins bajo `plugins/<name>/`, con manifest requerido `.codex-plugin/plugin.json`, marketplace `.agents/plugins/marketplace.json` y superficies opcionales como `skills/`, MCP, hooks y agentes.

**Aplicación:** conservar compatibilidad documentada para Codex como adaptador específico y actualizar futuras instrucciones contra documentación/repositorio vigente, no copiar pasos de instalación del repositorio deprecated.

### 6. [NVIDIA/skills](https://github.com/NVIDIA/skills)

**Aportes observados**
- Evaluación por capas: validación determinista y seguridad, deduplicación semántica y evaluación real del agente en sandbox.
- La evaluación en vivo compara el mismo conjunto de tareas con la skill ausente y presente.
- El conjunto de evaluación debe incluir casos negativos, en los que la conducta correcta es no activar la skill.
- El benchmark registra agentes, fecha, métricas y veredicto; las dimensiones publicadas incluyen seguridad, corrección, descubribilidad, efectividad y eficiencia.
- Sin un dataset de evaluación, no hay resultado live que pueda presentarse como benchmark.

**Aplicación:** separar linter/CI, revisión de seguridad, solapamiento semántico y evaluación conductual. Añadir casos machine-readable positivos y negativos para cinco skills prioritarias como primer piloto; no presentarlo como prueba funcional multiplataforma completa.

## Comparación con Mis-skills-2

| Área | Estado observado en Mis-skills-2 | Mejora aplicada/preparada |
|---|---|---|
| Fuente única y documentación | Existe `.claude/skills/<name>/SKILL.md`, changelogs y adaptadores | Se conserva; no se duplican skills por plataforma |
| Calidad TDD/debugging | Flujo evidencia-first ya presente | Loop proporcional, minimización, hipótesis falsables y criterios de pruebas independientes |
| Auditoría CI | CI estática estructural | Separación explícita de controles estáticos, seguridad, deduplicación y evaluación live |
| Procedencia de plugins | Límites de permisos ya definidos | Revisión de manifest, SHA inmutable, slugs, MCP, scripts y permisos |
| Medición de campañas | Estrategia y tracking ya incluidos | Hipótesis, control, guardrails, ventanas, reglas de decisión y economía break-even |
| Decisiones comerciales | Clasificación de hechos y pendientes existente | Evidence ledger, comparabilidad, escenarios y matriz de negociación |
| Evaluaciones | Protocolo manual de 180 ejecuciones | Primer set machine-readable de 10 casos para cinco skills; las 180 siguen pendientes |
| Seguridad y licencias | Reglas generales presentes | Revisar origen, licencia, secretos, PII, permisos y componentes ejecutables |

## Cambios preparados en esta rama

Se actualizaron las cinco skills prioritarias y sus changelogs:

1. `debug-and-fix`: feedback loop proporcional, diagnóstico complejo, minimización, hipótesis y pruebas de regresión de calidad.
2. `audit-ci-release`: supply chain de skills/plugins y evaluación baseline-versus-skill.
3. `github-project-operations`: manifests, identificadores estables, SHA inmutable y verificación read-back.
4. `ads-campaign-builder`: diseño de experimentos, medición, reglas de parada/escala y economía unitaria.
5. `business-strategy-documents`: registro de evidencia, comparabilidad, escenarios y términos de negociación.

Se añade `tests/evaluations.json` con 10 casos piloto (positivo y adversarial para cada una de las cinco skills). Estos casos son especificaciones de evaluación; no representan ejecuciones reales ni sustituyen las 180 pruebas multiplataforma.

## Riesgos y pendientes

- La compatibilidad conductual de las 18 skills en cinco plataformas continúa PENDIENTE hasta registrar las 180 ejecuciones con versión, método de carga, prompt exacto, salida y evidencia.
- Los casos piloto machine-readable requieren ejecución en plataformas reales y evaluación de resultados.
- La revisión de seguridad de manifests y código de cada plugin no equivale a una certificación formal; debe repetirse para cada versión fijada.
- `openai/skills` está deprecated; el repositorio actual de referencia para Codex es `openai/plugins`.
- La falta de protección de `main` es un riesgo de gobernanza que queda fuera del cambio autorizado.

## Fuentes consultadas

- [Matt Pocock — Skills](https://github.com/mattpocock/skills)
- [Anthropic — Skills](https://github.com/anthropics/skills)
- [Anthropic — Claude Plugins Official](https://github.com/anthropics/claude-plugins-official)
- [Google — Skills](https://github.com/google/skills)
- [OpenAI — Skills (deprecated)](https://github.com/openai/skills)
- [OpenAI — Plugins (current Codex examples)](https://github.com/openai/plugins)
- [NVIDIA — Skills](https://github.com/NVIDIA/skills)
- [NVIDIA — Evaluating Agent Skills](https://github.com/NVIDIA/skills/blob/main/docs/evaluating-agent-skills.mdx)
- [Agent Skills specification](https://agentskills.io/specification)
