# semana-05-corte1 · Tienda virtual UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `3d732d7` en `origin/main` (2026-09-07T14:41:37-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/main 3d732d7 2026-09-07T14:41:37-05:00, anterior al cierre 2026-09-10T17:00:00Z | Cumple | Rama principal declarada y hash dentro del plazo. |
| correcciones.md existe en la raíz del estado calificado | correcciones.md presente en el árbol de 3d732d7 (git ls-tree) | Cumple | Archivo en la raíz y en el hash calificado. |
| Correcciones trazables y contrastadas | correcciones.md objeta la rúbrica preliminar S5; no presenta tabla de seguimiento con hallazgo, acción, evidencia y estado por cada hallazgo S1-S4 | No cumple | No es un índice de verificación trazable; falta contraste con evidencia real por hallazgo. |
| S1 al día: equipo, problema y repositorio | README.md (equipo, problema, enlaces), docs/problema.md, historial con RAZOR7150, pxtroniwnl, Jasen, shalom-A26 | Cumple | Repositorio en ISCOUTB, nombre correcto, público e integrantes visibles. |
| S2 al día: escenarios de calidad y restricciones | docs/arbol-utilidad.md, docs/escenarios-calidad.md (4 escenarios), arc42 §1-3 | Cumple | Restricciones y escenarios documentados y enlazados. |
| S3 al día: estrategia de solución y decisiones | docs/matriz-comparativa-arquitectura.md, docs/adr/0001-monolito-modular.md, arc42 §4 | Cumple | ADR con contexto, alternativas, decisión, consecuencias y trazabilidad. |
| S4 al día: arc42, C4 y corte vertical | arc42 secciones 1-11, docs/c4/context.md, docs/c4/container.md, backend/app/modules/catalog, frontend/app/page.tsx | Cumple | Corte vertical implementado y documentado. |
| Corte vertical reproducible y coherente con la arquitectura | README documenta docker compose up --build y pytest; compose.yaml; run CI 34156890966 success | Cumple | Coherente con C4 (Next.js, FastAPI, PostgreSQL). |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/tests.yml ejecuta pytest en push/PR; runs CI success (34156890966, 34034598673, 33519914553) | Cumple | Runs posteriores al hash calificado y anteriores al cierre. |
| Trazabilidad consolidada navegable | docs/aspectos.md con 8 columnas y enlaces a escenarios, ADR, C4 y evidencia | Cumple | Algunas celdas de código/pruebas son texto sin enlace, pero la cadena principal es navegable. |
| PDF u otro adjunto exigido por el aula | No hay PDF en el repositorio; se entrega en Moodle | No verificado | Requiere acceso al aula para verificar. |
| Sustentación del corte | Sesión de sustentación no disponible en el repositorio | No verificado | La resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | Árbol incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | Rutas conforme a la estructura mínima. |
| Convenciones de ADR | docs/adr/0001-monolito-modular.md con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Nombre en kebab-case y numerado; sin reescrituras detectadas. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas y 4 filas; enlaces a escenarios, ADR, C4 y evidencia | Cumple | Algunas celdas de código/pruebas son texto sin enlace. |
| Registro de uso de IA | docs/ia.md con tabla de usos, herramientas, descartes y motivos; 11 commits de historial | Cumple | Incluye columna de propuestas descartadas con motivo. |
| README | README.md con qué es, arranque con docker compose up --build, pruebas con pytest y requisitos | Cumple | Arranque con un solo comando documentado. |
| Pipeline y análisis estático | .github/workflows/tests.yml ejecuta pytest en push/PR; runs success; sin configuración de SonarCloud | No cumple | Falta el análisis estático en SonarCloud exigido por el contrato. |
| Secretos | git grep sin coincidencias; sin .env versionados | Cumple | Sin credenciales en el repositorio. |
| Autoría y colaboración | shortlog: RAZOR7150 (8), pxtroniwnl (5), Jasen (4+3), shalom-A26 (2) | Cumple | Cuatro integrantes contribuyen; actividad repartida entre agosto y septiembre. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `3d732d740053c8f10ad4c618d3031024c72630bc 2026-09-07T14:41:37-05:00 corte-1`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene avances sólidos en S1-S4 con corte vertical funcional y CI exitoso, pero el correcciones.md no cumple como índice de verificación y falta SonarCloud.

Pendientes que siguen abiertos:
- correcciones.md como índice de verificación trazable
- SonarCloud en pipeline
- PDF no verificado
- sustentación no verificada
- celdas de trazabilidad sin enlace

## Recuento y nota sugerida

9 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.0 = 1 + 4 × (9/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula (se entrega en Moodle; no disponible en el repositorio).
- Sustentación del corte (sesión; la resuelve el docente).

## Hallazgos para la planilla

- correcciones.md no sigue el formato de índice de verificación exigido (hallazgo, acción, evidencia, estado).
- Falta SonarCloud en el pipeline; solo hay pytest en GitHub Actions.
- docs/aspectos.md tiene celdas de código y pruebas como texto sin enlaces navegables.
- PDF y sustentación no verificables desde el repositorio.
- correcciones.md centrado en objetar la rúbrica preliminar, no en contrastar hallazgos S1-S4.
