# semana-05-corte1 · CampusMarket

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `8044215` en `origin/master` (2026-09-06T16:05:15-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | Rama origin/master, hash 8044215, fecha 2026-09-06T16:05:15-05:00, anterior al cierre 2026-09-10T17:00:00Z. | Cumple | El estado calificado es identificable y cumple la condición temporal. |
| correcciones.md existe en la raíz del estado calificado | Archivo presente en el árbol del hash 8044215 (git ls-tree). | Cumple | Existe exactamente en la raíz y en el estado calificado. |
| Correcciones trazables y contrastadas | correcciones.md enlaza hallazgos S1-S4 con evidencia real (commits, rutas, runs) y estados declarados. | Cumple | Se contrastaron las correcciones con el historial y archivos; todas verificadas. |
| S1 al día: equipo, problema y repositorio | README.md lista integrantes y problema; repositorio en ISCOUTB con nombre correcto. | Cumple | Equipo y problema documentados; repositorio público y accesible. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10-escenarios-de-calidad.md y 02-restricciones.md con EC-01 a EC-05 y R-01 a R-07. | Cumple | Escenarios y restricciones completos y actualizados. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04-estrategia-de-solucion.md y ADR-0001/0002 con alternativas y decisiones. | Cumple | Estrategia y ADR documentados y trazables. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ARC42.md, docs/c4/01-contexto.puml y 02-contenedores.puml, backend/app/publicaciones/ y frontend/lib/publicaciones/. | Cumple | Documentación y código del corte vertical presentes y coherentes. |
| Corte vertical reproducible y coherente con la arquitectura | README.md con arranque de un comando (scripts/run_s4.sh), prueba test_publicaciones_vertical.py y evidencia de arranque. | Cumple | El recorrido Flutter→FastAPI→SQLite es reproducible y coincide con C4. |
| Pipeline y pruebas respaldan el estado calificado | Workflow .github/workflows/backend-tests.yml y run de CI asociado al hash (conclusión success). | Cumple | Pruebas automatizadas pasan en CI para el estado calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md con 8 columnas y enlaces a requisitos, C4, ADR, código, pruebas y evidencias. | Cumple | La tabla de aspectos es navegable y sin huecos en las filas evaluadas. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; se entrega en Moodle. | No verificado | Requiere acceso al aula para verificar el PDF. |
| Sustentación del corte | Sesión de sustentación no registrada en el repositorio. | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_PROYECTO_CAMPUSMARKET en ISCOUTB, público; integrantes en historial. | Cumple | Nombre y organización correctos. |
| Estructura mínima | Existen docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Estructura cumple con la mínima requerida. |
| Estado del repositorio calificado | Hash 8044215 en origin/master, anterior al cierre; sin commits posteriores al cierre. | Cumple | Se usó la rama principal declarada. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md y 0002-manejo-bloqueo-sqlite.md con nombres válidos y sin ediciones posteriores. | Cumple | Cumplen numeración y formato; no reescritos. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas y enlaces navegables. | Cumple | Cumple el formato y trazabilidad. |
| Registro de uso de IA | docs/ia.md con 14 commits de actualización y contenido de usos y rechazos. | Cumple | Registro creciente y con criterio. |
| README | README.md con descripción, arranque de un comando y pruebas. | Cumple | Cumple con lo requerido. |
| Pipeline y análisis estático | Workflow backend-tests.yml y run de CI exitoso; SonarCloud configurado en .sonarcloud.properties. | Cumple | CI y análisis estático presentes y funcionando. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8044215811e53b111888f75b30fc175fb889dc56 2026-09-06T16:05:15-05:00 Merge pull request #32 from ISCOUTB/S5-alinear-redaccion-r07`
- **Veredicto**: al dia
- Resumen: El proyecto en HEAD (mismo hash 8044215) cumple con los criterios de S1-S5 y el contrato transversal.

## Recuento y nota sugerida

10 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.3 = 1 + 4 × (10/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula
- Sustentación del corte

## Hallazgos para la planilla

- PDF no verificado por falta de acceso a Moodle.
- Sustentación pendiente de sesión docente.
- Sin hallazgos de incumplimiento en el repositorio.
