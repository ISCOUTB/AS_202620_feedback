# Semana 07 · Evidencia S7 · ROUTB

> Revisión definitiva auditada localmente. Se corrigió el resultado automático porque omitió evidencia legible en el repositorio.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `fe266aa` en `origin/master` (2026-09-20T21:32:01-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato ejecutable versionado | `docs/contracts/openapi.yaml` declara OpenAPI y una versión de API. | Cumple | El contrato está versionado como YAML. |
| Rutas y esquemas de datos | `docs/contracts/openapi.yaml` contiene rutas y `components.schemas`. | Cumple | Las respuestas se asocian con esquemas concretos. |
| Correspondencia contrato–API | Las rutas del contrato se cotejan con los routers en `backend/app/routers/`. | Cumple | No se hallaron operaciones declaradas sin implementación ni rutas públicas omitidas. |
| Versión e historial | El contrato conserva versión y trazabilidad en Git. | Cumple | El historial permite identificar su incorporación y cambios. |
| Prueba de contrato presente | La suite contiene una prueba que compara el contrato versionado con la API. | Cumple | La comprobación es automática. |
| Pipeline ejecuta la prueba | `.github/workflows/ci.yml` ejecuta la suite; run exitoso del estado revisado: https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/35554490737 | Cumple | Evidencia asociada a la rama principal. |
| Falla ante cambio incompatible | La evidencia S7 documenta una mutación incompatible y el run rojo correspondiente: https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/35531242547 | Cumple | Se observa el ciclo fallo–restauración. |
| ADR de integración ligado a escenario | `docs/adr/` contiene la decisión de integración con alternativa y consecuencias. | Cumple | La decisión se conecta con el escenario correspondiente. |
| arc42 sección 6 | `docs/arc42/06-vista-ejecucion.md` describe los flujos principales y de fallo. | Cumple | Los recorridos identifican componentes y mensajes. |
| C4 nivel 2 etiquetado | `docs/c4/context.md:64-66` etiqueta las relaciones actor–sistema únicamente como «Usa». | No cumple | Faltan protocolo y formato en todas las flechas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia u observación |
|---|---|---|
| Repositorio público con nombre de convención | Cumple | Clon público `ISCOUTB/AS_202620_ROUTB`. |
| Estructura mínima | Cumple | Están presentes las rutas documentales obligatorias. |
| Estado calificado identificable | Cumple | `origin/master`, `fe266aa`, fecha y cierre consignados. |
| Nombres de ADR | Cumple | Los ADR usan numeración y kebab-case. |
| ADR aceptados sin reescribir | Cumple | El historial conserva las decisiones aceptadas. |
| `docs/ia.md` al día | Cumple | El registro incluye la actividad S7. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | El CI es público y está en verde, pero no se acreditó scanner y Quality Gate de SonarCloud. |
| Sin credenciales expuestas | Cumple | No se hallaron credenciales reales versionadas en el estado S7. |
| Contribución de todo el equipo | Cumple | El historial permite identificar aportes de todos los integrantes. |

## Estado global del proyecto

La punta actual contiene cambios posteriores al cierre y no altera el estado calificado. La evidencia S7 es verificable; queda como no conformidad el etiquetado incompleto del C4 nivel 2 y la ausencia de Quality Gate auditable.

## Recuento y nota sugerida

**9 de 10 criterios Cumple.**

**Nota sugerida (propuesta al docente; la nota final se fija en Moodle): 4.6 = 1 + 4 × (9/10).**
