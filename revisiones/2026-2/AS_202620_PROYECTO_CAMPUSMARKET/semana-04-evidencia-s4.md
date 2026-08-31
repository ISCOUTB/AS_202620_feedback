# semana-04-evidencia-s4 · CampusMarket

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `f3f4367` (2026-08-30T22:55:30-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/02-restricciones.md, 03-contexto.md, 04-estrategia-de-solucion.md, 05-bloques-de-construccion.md, 06-vista-ejecucion.md y ARC42.md (secciones 1-4) con contenido propio | Cumple | No se detectan rastros de plantilla en los archivos listados; secciones 2-6 redactadas con contenido específico del proyecto. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-decisiones.md incluye tabla con enlace a docs/adr/0001-usar-monolito-modular.md | Cumple | La sección funciona como índice trazable y no repite el contenido del ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-escenarios-de-calidad.md y 10-arbol-de-utilidad.md definen EC-01 a EC-04 consistentes con ADR-0001 y sección 4 | Cumple | Los escenarios mantienen atributos, estímulos y medidas alineados con la estrategia de monolito modular. |
| Glosario iniciado con términos del dominio | docs/arc42/12-glosario.md existe en el árbol | No verificado | No se pudo comprobar el contenido del glosario; falta evidencia de que los términos sean propios del dominio y no genéricos. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/01-contexto.puml, 01-contexto.md, 02-contenedores.puml, 02-contenedores.md; actores Estudiante y Administrador reaparecen en nivel 2 | Cumple | Los contenedores Frontend Web, Backend API y Persistencia local corresponden al sistema único del nivel 1. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Contenedores mapean a frontend/campusmarket/lib, backend/app y backend/app/publicaciones/repository.py (SQLite) | Cumple | Cada contenedor del diagrama tiene una carpeta o archivo de código correspondiente en el repositorio. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README cita frontend/campusmarket/lib/publicaciones/publicacion_form_page.dart, backend/app/publicaciones/router.py, service.py y repository.py | Cumple | El recorrido Flutter Web → FastAPI → lógica → SQLite está documentado y las rutas existen en el árbol. |
| Arranque documentado con un solo comando | README.md incluye sección 'Arranque con un solo comando' con scripts/run_s4.ps1 y scripts/run_s4.sh | Cumple | Se declaran requisitos previos y un comando único por sistema operativo. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_publicaciones_vertical.py y README enlaza run #12 exitoso: https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/33219659253 | Cumple | La prueba ejercita HTTP → lógica → persistencia y el pipeline la ejecutó con éxito. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md existe y README menciona fila ASP-05 completa | No verificado | No se pudo comprobar el contenido real de la fila ni que cada celda enlace a un destino existente; falta evidencia del archivo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_PROYECTO_CAMPUSMARKET en organización ISCOUTB, visible públicamente; autores consolidados: Nilver Garcia, Camilo Martinez, Joshua Tenorio | Cumple | El nombre sigue el patrón AS_202620_<PROYECTO> y los tres integrantes aparecen en el historial. |
| Estructura mínima | Árbol contiene docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md | Cumple | Todas las rutas exigidas están presentes. |
| Estado calificado (versionado) | Commit f3f4367 con fecha 2026-08-30T22:55:30-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | No se detectaron commits posteriores al cierre ni etiqueta movida. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md sigue el patrón NNNN-titulo-en-kebab-case.md y contiene contexto, opciones, decisión y consecuencias | Cumple | No se evidencia edición posterior del ADR aceptado. |
| Tabla de aspectos | docs/aspectos.md existe en el árbol | No verificado | No se pudo comprobar que tenga las ocho columnas ni que las celdas sean navegables; falta contenido del archivo. |
| Registro de uso de IA | docs/ia.md existe y el historial muestra commits en fechas 2026-08-08, 08-16, 08-25, 08-29 y 08-30 | Cumple | El registro crece a lo largo del semestre. |
| README | README.md incluye qué es, requisitos previos, arranque con un solo comando y cómo probar | Cumple | Documento completo y enlaza a CI y trazabilidad. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml existe y CI run #12 exitoso, pero no se evidencia integración con SonarCloud | No cumple | Falta evidencia de análisis estático en SonarCloud (organización isco-utb) como exige el contrato. |

## Recuento y nota sugerida

8 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Glosario: falta contenido de docs/arc42/12-glosario.md para confirmar términos de dominio.
- Fila de aspectos: falta contenido de docs/aspectos.md para verificar columnas y enlaces.
- SonarCloud: falta configuración o enlace a análisis estático en el pipeline.

## Hallazgos para la planilla

- Glosario (sección 12) no verificable por falta de contenido.
- Fila de aspectos no verificable por falta de contenido del archivo.
- Análisis estático en SonarCloud no evidenciado.
- El resto de criterios de la ficha y transversales cumplen con la evidencia disponible.
