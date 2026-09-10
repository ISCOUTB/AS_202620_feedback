# semana-05-corte1 · TAIA

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `a3f4d82` en `origin/main` (2026-09-06T04:13:11-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/main a3f4d82 2026-09-06T04:13:11-05:00 < cierre 2026-09-07T05:00:00Z | Cumple | Rama principal identificada y hash anterior al cierre. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree a3f4d82 incluye correcciones.md; git show a3f4d82:correcciones.md disponible | Cumple | Archivo presente en la raíz del hash calificado. |
| Correcciones trazables y contrastadas | correcciones.md visible en a3f4d82 es una justificación de la calificación, no un índice con hallazgo, acción, evidencia y estado | No cumple | No se encontró la tabla de seguimiento exigida con enlaces a commits/runs. |
| S1 al día: equipo, problema y repositorio | docs/ficha_problema.md, docs/aspectos.md, docs/ia.md, docs/arc42/arc42.md, docs/adr/ y docs/c4/ presentes en a3f4d82 | Cumple | Equipo, problema, tensiones, aspectos e IA documentados. |
| S2 al día: escenarios de calidad y restricciones | docs/calidad/arbol_utilidad.md y escenarios_calidad.md con 5 escenarios; restricciones en arc42 sección 2 | Cumple | Escenarios y restricciones completos. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-estilo-arquitectonico.md con contexto, alternativas, decisión, consecuencias y trazabilidad; docs/c4/C4-C2.md | Cumple | Estrategia y decisiones documentadas. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42.md, docs/c4/C4-C2.md, backend/app/modules/academic/ con domain/application/adapters y tests | Cumple | Arc42, C4 y corte vertical presentes. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta run.bat y pytest backend/tests; backend/tests/test_academic_register_task.py; run CI 34017421928 success | Cumple | Corte vertical A-01 implementado y verificado por CI. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml; run 34017421928 (2026-09-06T06:47:36Z) success anterior al hash | Cumple | CI en verde para el estado calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md fila A-01 enlaza C4, ADR, código, pruebas y evidencia | Cumple | Cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia navegable. |
| PDF u otro adjunto exigido por el aula | Sin documento adjunto en el repositorio; entrega en Moodle no accesible | No verificado | Requiere revisar Moodle. |
| Sustentación del corte | Sin sesión de sustentación registrada | No verificado | Lo resuelve el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant visible | Cumple | Nombre con convención y visibilidad pública. |
| Estructura mínima presente | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md en a3f4d82 | Cumple | Estructura completa. |
| Estado calificado identificable | origin/main a3f4d82 2026-09-06T04:13:11-05:00 | Cumple | Hash y fecha registrados. |
| Nombres de ADR según la convención | docs/adr/0001-estilo-arquitectonico.md | Cumple | Cumple patrón NNNN-titulo-kebab-case. |
| ADR aceptados no reescritos | Sin git log --follow de docs/adr/0001-*.md en la evidencia | No verificado | Requiere historial de commits del ADR. |
| docs/ia.md al día para la semana | docs/ia.md con entradas 001-006; último commit a3f4d82 2026-09-06 | Cumple | Registro actualizado. |
| Sin credenciales en el repositorio ni en el historial | git grep sin coincidencias; sin .env versionado | Cumple | Sin secretos detectados. |
| Contribución de todos los integrantes | git shortlog: val 19, dei0811 8, mark 3, luis20072002 1 | Cumple | Todos aparecen; distribución desigual. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `915e4996c5f252b0a35e6a0405935e665d2cfa66 2026-09-08T17:42:02-05:00 fix: harden dependency installation for SonarCloud`
- **Veredicto**: con pendientes
- Resumen: Proyecto al día en S1-S4 con corte vertical ejecutable y CI exitoso; correcciones.md no cumple la estructura de índice de verificación.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 3cf6bfc y 915e499 (2026-09-08) corrigen el pipeline de CI después del cierre
- diff_desde_cierre muestra cambios en ci.yml, requirements.txt y correcciones.md posteriores al cierre

Pendientes que siguen abiertos:
- Reestructurar correcciones.md como índice de verificación trazable
- Verificar historial del ADR
- PDF y sustentación pendientes de aula

## Recuento y nota sugerida

9 de 12 criterios Cumple.

## No verificado / pendientes

- Historial de commits de docs/adr/0001-estilo-arquitectonico.md.
- PDF adjunto en Moodle.
- Sustentación oral.

## Hallazgos para la planilla

- correcciones.md no es un índice de verificación trazable; es una justificación de la calificación.
- Commits post_cierre 3cf6bfc y 915e499 modifican CI y correcciones.md.
- Distribución de contribuciones desigual: val 19, dei0811 8, mark 3, luis20072002 1.
- No se pudo verificar reescritura del ADR por falta de historial.
- Commits posteriores al cierre (no calificados): 915e499 2026-09-08T17:42:02-05:00 fix: harden dependency installation for SonarCloud; 3cf6bfc 2026-09-08T17:34:01-05:00 fix: lock dependencies for SonarCloud security gate
