# semana-05-corte1 · Tienda virtual UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `20ab43f` en `origin/main` (2026-09-06T07:56:34-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/main 20ab43f 2026-09-06T07:56:34-05:00 anterior al cierre 2026-09-07T05:00:00Z | Cumple | Rama principal main identificada sin etiquetas. |
| correcciones.md existe en la raíz del estado calificado | Árbol de 20ab43f no incluye correcciones.md; aparece solo en 3d732d7 (post-cierre) | No cumple | Archivo añadido después del cierre; no cumple la fila. |
| Correcciones trazables y contrastadas | Sin correcciones.md en 20ab43f no hay índice de verificación | No cumple | No se puede contrastar ningún hallazgo S1-S4. |
| S1 al día: equipo, problema y repositorio | README.md, docs/problema.md, docs/aspectos.md, docs/ia.md, docs/disponibilidad.md en 20ab43f | Cumple | Equipo, problema, alcance y tensiones documentados. |
| S2 al día: escenarios de calidad y restricciones | docs/arbol-utilidad.md, docs/escenarios-calidad.md, arc42 §1-3, docs/c4/context.md | Cumple | Escenarios y restricciones completos. |
| S3 al día: estrategia de solución y decisiones | arc42 §4, docs/matriz-comparativa-arquitectura.md, docs/adr/0001-monolito-modular.md | Cumple | Estrategia y ADR con alternativas evaluadas. |
| S4 al día: arc42, C4 y corte vertical | arc42 secciones 1-12, docs/c4/container.md, docs/aspectos.md, backend/app/modules/catalog/ | Cumple | Corte vertical implementado y documentado. |
| Corte vertical reproducible y coherente con la arquitectura | README con docker compose up --build y pytest; compose.yaml; backend/tests/test_catalog.py | Cumple | Coherente con C4 y ADR 0001. |
| Pipeline y pruebas respaldan el estado calificado | Run 34034598673 success 2026-09-06T12:56:43Z asociado al push de 20ab43f; .github/workflows/tests.yml | Cumple | CI verde para el hash calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md enlaza escenario→ADR→código→pruebas; ADR enlaza a árbol y escenarios | Cumple | Cadena navegable en los 4 escenarios. |
| PDF u otro adjunto exigido por el aula | Sin acceso a Moodle en la evidencia del repositorio | No verificado | Requiere revisar el aula. |
| Sustentación del corte | Sin sesión de sustentación registrada en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB visible; shortlog con RAZOR7150, pxtroniwnl, Jasen/Jasen Yukopila, shalom-A26 | Cumple | 4 integrantes en el historial. |
| Estructura mínima | README.md, docs/arc42/, docs/adr/0001-*.md, docs/c4/, docs/aspectos.md, docs/ia.md en 20ab43f | Cumple | Rutas estándar presentes. |
| Estado del repositorio que se califica | origin/main 20ab43f anterior al cierre | Cumple | Hash y fecha registrados. |
| Convenciones de ADR | docs/adr/0001-monolito-modular.md con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Nombre y contenido conforme. |
| Registro de uso de IA | docs/ia.md con tabla de usos, descartes y validación; log con 10 commits | Cumple | Incluye columna de propuestas descartadas. |
| Secretos | git grep sin coincidencias; sin .env versionados | Cumple | Sin incidentes de credenciales. |
| Autoría y colaboración | shortlog: RAZOR7150 8, pxtroniwnl 5, Jasen 7 (consolidado), shalom-A26 1 | Cumple | Distribución desigual pero todos contribuyen. |
| Pipeline y análisis estático | Runs de CI success en .github/workflows/tests.yml; sin evidencia de SonarCloud | No verificado | Falta config/run de SonarCloud para verificar análisis estático. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `3d732d740053c8f10ad4c618d3031024c72630bc 2026-09-07T14:41:37-05:00 corte-1`
- **Veredicto**: con pendientes
- Resumen: Proyecto S1-S4 completo y con CI verde en 20ab43f; la entrega S5 falla por ausencia de correcciones.md en el estado calificado.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- correcciones.md añadido en 3d732d7 (2026-09-07T14:41:37-05:00), después del cierre
- docs/aspectos.md y docs/ia.md modificados en 3d732d7 post-cierre

Pendientes que siguen abiertos:
- Verificar SonarCloud
- PDF en Moodle
- Sustentación

## Recuento y nota sugerida

8 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula (requiere Moodle).
- Sustentación del corte (sesión docente).
- Análisis estático en SonarCloud (sin evidencia de config/run).

## Hallazgos para la planilla

- correcciones.md ausente en el estado calificado 20ab43f; añadido solo en 3d732d7 post-cierre.
- Commit 3d732d7 posterior al cierre sube correcciones.md, docs/aspectos.md y docs/ia.md.
- Sin evidencia de SonarCloud para análisis estático.
- Distribución de commits desigual: shalom-A26 con 1 commit.
- Tabla de seguimiento de correcciones no construible por ausencia del archivo en el corte.
- Commits posteriores al cierre (no calificados): 3d732d7 2026-09-07T14:41:37-05:00 corte-1
