# semana-05-corte1 · AudioShare

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `cb65d13` en `origin/master` (2026-09-06T22:00:48-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master cb65d13 2026-09-06T22:00:48-05:00; cierre 2026-09-10T17:00:00Z | Cumple | Hash anterior al cierre y rama principal identificada. |
| correcciones.md existe en la raíz del estado calificado | Árbol de cb65d13 no incluye correcciones.md (ls-tree del estado calificado) | No cumple | Archivo ausente en la raíz del hash calificado. |
| Correcciones trazables y contrastadas | No existe correcciones.md en cb65d13; sin respuestas a hallazgos S1-S4 | No cumple | No hay índice de verificación de correcciones. |
| S1 al día: equipo, problema y repositorio | docs/ficha-problema.md en cb65d13; shortlog con 4 autores (45+38+36+30 commits); repo ISCOUTB/AS_202620_AudioShare visible | Cumple | Discrepancia de nombre: declarado 'Yeiver Andres Verjel Perez' vs git 'Yeiver Andrés Vergel Pérez'. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios_calidad.md (EC-01 a EC-04), docs/arbol_utilidad.md, docs/Restricciones_justificadas.md (R-01 a R-04) en cb65d13 | Cumple | Escenarios con métricas y restricciones justificadas presentes. |
| S3 al día: estrategia de solución y decisiones | docs/Matriz_Comparativa.md, docs/adr/0001-usar-monolito-modular.md, docs/arc42/src/04_solution_strategy.adoc en cb65d13 | Cumple | Decisión de monolito modular documentada con alternativas y consecuencias. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/src/ (secciones 1,2,3,4,5,6,9,10,12), docs/c4/ (niveles 1 y 2), src/modules/, tests/a01.test.ts en cb65d13 | Cumple | Faltan secciones arc42 7, 8 y 11; no se confirma si la ficha S4 las exigía. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta npm run dev y npm test; tests/a01.test.ts recorre A-01; src/modules/session,audio,sync coherentes con ADR-0001 | Cumple | Corte vertical A-01 implementado y probado a nivel HTTP. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml ejecuta npm run verify; run CI success 2026-09-07T03:21:03Z https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/34079348567 | Cumple | Runs posteriores al hash y anteriores al cierre; los más recientes son success. |
| Trazabilidad consolidada navegable | docs/aspectos.md con matriz A-01 que enlaza escenarios, ADR, C4, implementación y pruebas | Cumple | Enlaces relativos a archivos existentes en cb65d13. |
| PDF u otro adjunto exigido por el aula | Sin acceso a Moodle; no hay PDF en el repositorio | No verificado | Requiere revisar la entrega en el aula. |
| Sustentación del corte | Sesión de sustentación no disponible en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_AudioShare visible; 4 autores en shortlog de cb65d13 | Cumple | Nombre y organización correctos. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md en cb65d13 | Cumple | Estructura requerida presente. |
| Estado del repositorio calificado | origin/master cb65d13 2026-09-06T22:00:48-05:00; sin commits posteriores al cierre | Cumple | Hash anterior al cierre y head sin diferencias. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md en cb65d13; nombre cumple patrón NNNN-titulo-kebab-case | Cumple | Un ADR aceptado; no se observan reescrituras. |
| Registro de uso de IA | docs/ia.md en cb65d13 con tabla de usos, herramientas, aceptado/rechazado; 9 commits de ia.md desde 2026-08-09 | Cumple | Registro creciente y con rechazos justificados. |
| Secretos | git grep sin coincidencias en cb65d13; sin .env versionados | Cumple | Sin credenciales detectadas. |
| Autoría y colaboración | shortlog cb65d13: 45 Elian, 38 Yeiver, 36 cardonavincent26, 30 Santiago; commits desde agosto | Cumple | Discrepancia de nombre Yeiver Verjel/Vergel entre declaración y git. |
| Pipeline y análisis estático | .github/workflows/ci.yml; run CI success 2026-09-07T03:21:03Z https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/34079348567 | Cumple | CI ejecuta npm run verify en cada push; runs recientes success. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `cb65d13134b220c020d0facaa00d0a779d584245 2026-09-06T22:00:48-05:00 Update README.md`
- **Veredicto**: con pendientes
- Resumen: Proyecto con S1-S4 al día y corte vertical funcional; entrega S5 incompleta por ausencia de correcciones.md.

Pendientes que siguen abiertos:
- correcciones.md en la raíz
- PDF en Moodle (no verificado)
- Sustentación (no verificada)

## Recuento y nota sugerida

8 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (8/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u adjunto en Moodle (sin acceso).
- Sustentación del corte (sesión del docente).

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado cb65d13.
- Sin respuestas trazables a hallazgos S1-S4 por ausencia de correcciones.md.
- Discrepancia de nombre del integrante Yeiver (Verjel vs Vergel) entre declaración y git.
- Faltan secciones arc42 7, 8 y 11 en el estado calificado.
- Runs de CI previos al 2026-09-07 fallaron; los recientes son success.
