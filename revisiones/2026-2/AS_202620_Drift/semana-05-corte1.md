# semana-05-corte1 · Drift

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `d110d6d` en `origin/master` (2026-09-06T23:34:21-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master d110d6d 2026-09-06T23:34:21-05:00; cierre 2026-09-07T05:00:00Z | Cumple | Hash y fecha verificados en la rama principal, anterior al cierre. |
| correcciones.md existe en la raíz del estado calificado | Árbol de d110d6d contiene docs/correciones.md; no hay correcciones.md en la raíz | No cumple | Nombre mal escrito y ubicación distinta a la exigida. |
| Correcciones trazables y contrastadas | docs/correciones.md lista hallazgos pero deja pendientes (etiqueta corte-1, ADR del reto) y el archivo está truncado | No cumple | No todas las correcciones tienen evidencia contrastable; archivo fuera de la raíz. |
| S1 al día: equipo, problema y repositorio | README.md declara equipo y enlaza docs/ficha_problema.md; archivo existe en el árbol | No verificado | No se dispone del contenido de ficha_problema.md ni de la matriz S1 para contrastar. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios.md y docs/arc42/arc42_2_restricciones.md definen E1-E5 con medidas y restricciones | Cumple | Escenarios medibles y restricciones documentadas. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/arc42_4_soluciones_arquitectonica.md y docs/adr/0002-arquitectura-base.md con trazabilidad | Cumple | Estrategia hexagonal y decisiones documentadas con alternativas y consecuencias. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ (secciones 1-6,9,10,12), docs/c4/contexto.md, docs/c4/contenedores.md, backend/frontend con tests | Cumple | Artefactos presentes y coherentes con la arquitectura declarada. |
| Corte vertical reproducible y coherente con la arquitectura | README.md no muestra sección de arranque en la evidencia; scripts/start.py sin contenido visible | No verificado | No se pudo comprobar el comando único de arranque ni la ejecución del corte. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml existe; sin runs_ci verificados en la evidencia | No verificado | Solo referencia en docs/correciones.md; falta URL de run asociado al hash. |
| Trazabilidad consolidada navegable | docs/aspectos.md tiene tabla de 8 columnas pero con celdas 'Pendiente' en E3-E5 (pruebas/evidencia) | No cumple | Huecos en la cadena aspecto-requisito-C4-ADR-código-pruebas-evidencia. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio | No verificado | Depende de la entrega en Moodle. |
| Sustentación del corte | Sin sesión de sustentación en la evidencia | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | Faltan secciones arc42 7, 8 y 11; docs/correciones.md mal escrito | No cumple | La estructura base existe pero incompleta según el contrato. |
| Convenciones de ADR | ADR-0001 tiene 'Commit de la decisión: pendiente'; nombres cumplen patrón | No cumple | Trazabilidad incompleta en ADR-0001. |
| Tabla de aspectos | docs/aspectos.md con celdas 'Pendiente' en E3-E5 sin enlaces | No cumple | Filas con huecos no defendibles. |
| Registro de uso de IA | docs/ia.md existe con historial de commits; contenido no proporcionado | No verificado | No se pudo verificar columnas de aceptado/rechazado. |
| README | README.md describe el proyecto pero la sección de arranque no está visible en la evidencia | No verificado | Falta confirmar el comando único de arranque. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe; sin runs_ci verificados | No verificado | No hay evidencia de ejecución en verde. |
| Secretos | grep sin coincidencias; sin .env versionados | Cumple | Sin credenciales en el repositorio. |
| Autoría y colaboración | 4 identidades consolidadas con contribuciones repartidas (67, 65, 56, 49 commits) | Cumple | Todos los integrantes contribuyen a lo largo del semestre. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `74337a3c9c2a67c807e0018fe865979b29aa330c 2026-09-08T02:53:31Z Update README with vertical slice test instructions`
- **Veredicto**: con pendientes
- Resumen: El primer corte tiene una base arquitectónica sólida pero incumple la forma del compendio: correcciones.md mal ubicado, trazabilidad incompleta y secciones arc42 faltantes; hay correcciones tardías post-cierre.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- dbb98d3 elimina duplicación en tests de búsqueda
- 75881e4 elimina duplicación en test de búsqueda (corte 1)
- e77a240 actualiza README con validación
- c12dda8 documenta proceso de corte vertical en ia.md
- 74337a3 actualiza README con instrucciones de prueba vertical

Pendientes que siguen abiertos:
- correcciones.md en la raíz
- secciones arc42 7/8/11
- trazabilidad E3-E5
- commit en ADR-0001
- etiqueta corte-1
- ADR del reto
- verificación de pipeline
- README con comando único

## Recuento y nota sugerida

4 de 12 criterios Cumple.

## No verificado / pendientes

- Contenido de docs/ficha_problema.md y matriz S1.
- Reproducibilidad del corte vertical (README/scripts/start.py).
- Ejecución de CI (runs_ci).
- PDF entregado en Moodle.
- Sustentación del corte.
- Contenido de docs/ia.md.
- Sección de arranque en README.

## Hallazgos para la planilla

- correcciones.md no está en la raíz; está como docs/correciones.md.
- Faltan secciones arc42 7, 8 y 11.
- ADR-0001 sin commit de la decisión asociado.
- Trazabilidad con pendientes en E3-E5.
- Commits posteriores al cierre corrigen tests y documentación.
- README no muestra comando único de arranque en la evidencia.
- Pipeline sin runs verificados.
- Commits posteriores al cierre (no calificados): 74337a3 2026-09-08T02:53:31Z Update README with vertical slice test instructions; c12dda8 2026-09-07T01:26:25-05:00 Document vertical cut test process in ia.md; e77a240 2026-09-07T01:21:00-05:00 Update README with test file additions and validation info; 75881e4 2026-09-07T01:07:27-05:00 fix: eliminar duplicacion de codigo en test de busqueda (corte 1); dbb98d3 2026-09-07T00:22:27-05:00 fix: eliminar duplicacion de codigo en tests de busqueda de juegos
