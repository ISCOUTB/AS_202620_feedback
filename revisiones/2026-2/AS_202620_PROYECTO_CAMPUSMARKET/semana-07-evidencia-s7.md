# Semana 07 · Evidencia S7 · CampusMarket

> Revisión definitiva auditada localmente. Se corrigió el resultado automático porque omitió evidencia legible en el repositorio.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `c53ee32` en `origin/master` (2026-09-18T21:11:48-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato ejecutable versionado | `contracts/openapi-v1.json:2-6` declara OpenAPI 3.1.0 y API 1.0.0. | Cumple | Archivo JSON versionado, no prosa. |
| Rutas y esquemas de datos | `contracts/openapi-v1.json:15-109` contiene `/publicaciones`, `/health` y `components.schemas`. | Cumple | Las respuestas referencian esquemas concretos. |
| Correspondencia contrato–API | `backend/app/publicaciones/router.py:13,32-62` implementa `POST/GET /publicaciones`; `backend/app/main.py:39-48` implementa `/health`, las tres rutas presentes en el contrato. | Cumple | Cotejo bidireccional y prueba automática en `test_contrato_openapi.py:28-59`. |
| Versión e historial | `info.version` es 1.0.0; `git log -- contracts/openapi-v1.json` devuelve `485249a` (2026-09-15). | Cumple | Alta del contrato identificable. |
| Prueba de contrato presente | `backend/tests/test_contrato_openapi.py:19-59`. | Cumple | Compara el OpenAPI versionado con el generado por FastAPI. |
| Pipeline ejecuta la prueba | `.github/workflows/backend-tests.yml:91-92`; run exitoso del hash revisado: https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/35414943658 | Cumple | El mismo workflow separa pruebas funcionales y contractuales. |
| Falla ante cambio incompatible | `docs/evidencias/fallo-contrato-s7-2026-09-15.md:17-57` registra la mutación de `operationId`, el fallo y su restauración. | Cumple | Evidencia aportada por el equipo con salida `1 failed` y código 1. |
| ADR de integración ligado a escenario | `docs/adr/0003-usar-integracion-sincrona-http-json.md` liga la decisión a EC-06, descarta asincronía y explicita acoplamiento. | Cumple | Alternativa y consecuencias documentadas. |
| arc42 sección 6 | `docs/arc42/06-vista-ejecucion.md:3-143` describe creación, consulta y fallo de persistencia con secuencias. | Cumple | Los flujos incluyen HTTP/JSON y respuestas. |
| C4 nivel 2 etiquetado | `docs/c4/02-contenedores.puml:24-30` etiqueta todas las relaciones con HTTPS/Flutter Web, HTTP/JSON o PyMySQL/SQL. | Cumple | Protocolo y formato visibles en cada flecha. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia u observación |
|---|---|---|
| Repositorio público con nombre de convención | Cumple | Clon público `ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET`. |
| Estructura mínima | Cumple | `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`, `README.md`. |
| Estado calificado identificable | Cumple | `origin/master`, `c53ee32`, fecha y cierre consignados. |
| Nombres de ADR | Cumple | ADR 0001–0004 cumplen numeración y kebab-case. |
| ADR aceptados sin reescribir | Cumple | El historial conserva las decisiones y sus reemplazos. |
| `docs/ia.md` al día | Cumple | `docs/ia.md:75-108` registra S7, verificación y rechazos motivados. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | El workflow no invoca el scanner; falta un run que ejecute SonarCloud y su Quality Gate para el estado revisado. |
| Sin credenciales expuestas | Cumple | No se hallaron credenciales reales ni `.env` versionado; las claves de CI son valores efímeros del servicio de pruebas. |
| Contribución de todo el equipo | Cumple | Tres identidades consolidadas para tres integrantes. |

## Estado global del proyecto

La punta actual coincide con el estado calificado. El contrato, la prueba y la documentación S7 están completos; permanece abierta la integración auditable del scanner de SonarCloud en el workflow.

## Recuento y nota sugerida

**10 de 10 criterios Cumple.**

**Nota sugerida (propuesta al docente; la nota final se fija en Moodle): 5.0 = 1 + 4 × (10/10).**
