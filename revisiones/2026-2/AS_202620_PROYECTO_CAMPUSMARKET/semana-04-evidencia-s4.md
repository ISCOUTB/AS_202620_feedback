# semana-04-evidencia-s4 · CampusMarket

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `67593c2` (2026-08-25T04:08:32-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | Falta docs/arc42/03-contexto.md en el árbol del commit 67593c2 | No cumple | Secciones 1,2,4,5,6 presentes; sección 3 ausente. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-decisiones.md: tabla con enlace a ADR-0001 | Cumple | Índice trazable sin repetir contenido. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-escenarios-de-calidad.md: EC-01 a EC-04 | Cumple | Escenarios coherentes con ADR y árbol de utilidad. |
| Glosario iniciado con términos del dominio | docs/arc42/12-glosario.md: tabla con términos propios | Cumple | Términos como Publicación, Producto, Modalidad. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/01-contexto.puml y 02-contenedores.puml existen | No verificado | No se pudo verificar coherencia entre niveles sin contenido de los diagramas. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | README.md: fronteras backend usuarios/publicaciones/catalogo/administracion; árbol backend/app/ | Cumple | Correspondencia entre contenedores y directorios. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md: rutas UI, API, router, service, repository; árbol incluye esos archivos | Cumple | Recorrido completo documentado y archivos presentes. |
| Arranque documentado con un solo comando | README.md: sección 'Arranque del corte vertical con un solo comando' con scripts/run_s4.ps1 y .sh | Cumple | Comando único declarado. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_publicaciones_vertical.py y .github/workflows/backend-tests.yml existen | No verificado | No hay evidencia de ejecución en verde (sin URL de run). |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md existe en el árbol | No verificado | No se pudo verificar contenido de la fila ni enlaces de celdas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_PROYECTO_CAMPUSMARKET, visible true, autores incluyen a los tres integrantes | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima | Árbol incluye docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura conforme. |
| Estado del repositorio calificado | hash 67593c2, fecha 2026-08-25T04:08:32-05:00 anterior al cierre 2026-08-31 | Cumple | Commit vigente correcto. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md cumple patrón y contenido | Cumple | ADR aceptado con contexto, decisión, consecuencias. |
| Tabla de aspectos | docs/aspectos.md existe | No verificado | No se pudo verificar columnas ni filas completas. |
| Registro de uso de IA | docs/ia.md con historial de commits (ia_log) | Cumple | Registro presente y creciente. |
| README | README.md con arranque y pruebas | Cumple | Documenta requisitos y comando único. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml existe | No verificado | Sin evidencia de runs ni configuración SonarCloud. |

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- C4 nivel 1 y 2 coherentes: falta contenido de los .puml para comparar actores y contenedores.
- Prueba automatizada en verde: falta URL de run de GitHub Actions.
- Fila de aspectos.md completa: falta contenido del archivo.
- Tabla de aspectos (transversal): falta contenido para verificar columnas.
- Pipeline y SonarCloud: falta evidencia de ejecución y configuración.

## Hallazgos para la planilla

- Falta la sección 3 de arc42 (contexto).
- No hay evidencia de ejecución en verde de la prueba del corte vertical.
- No se pudo verificar la coherencia entre C4 nivel 1 y 2 por falta de contenido de diagramas.
- No se pudo verificar la fila de aspectos.md hasta Pruebas.
- No hay evidencia de pipeline ejecutado ni SonarCloud.
- Los diagramas C4 están como código (.puml), lo cual es positivo.
