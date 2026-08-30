# semana-04-evidencia-s4 · CampusMarket

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `0197341` (2026-08-29T01:13:49-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/02-restricciones.md, 03-contexto.md, 04-estrategia-de-solucion.md, 05-bloques-de-construccion.md, 06-vista-ejecucion.md y ARC42.md contienen secciones redactadas; sin rastros de plantilla en los extractos. | Cumple | Secciones 1 a 6 presentes y redactadas. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-decisiones.md incluye tabla con enlace a docs/adr/0001-usar-monolito-modular.md. | Cumple | Sección 9 actúa como índice trazable sin repetir ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-escenarios-de-calidad.md y 10-arbol-de-utilidad.md muestran EC-01 a EC-04 coherentes con ADR-0001 y sección 4. | Cumple | Escenarios de calidad alineados con prioridades del árbol de utilidad. |
| Glosario iniciado con términos del dominio | Existe docs/arc42/12-glosario.md pero no se proporciona su contenido. | No verificado | Falta extracto del glosario para comprobar términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/01-contexto.puml, 01-contexto.md, 02-contenedores.puml, 02-contenedores.md; docs/arc42/03-contexto.md afirma que actores del N1 se mantienen conectados en N2. | Cumple | Diagramas como código y documentación de coherencia. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Contenedores Frontend Web (frontend/campusmarket/lib), Backend API (backend/app), Persistencia local (backend/app/publicaciones/repository.py) corresponden a directorios del árbol. | Cumple | Correspondencia concreta entre diagrama y código. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md lista publicacion_form_page.dart, publicaciones_api.dart, router.py, service.py, repository.py; docs/arc42/06-vista-ejecucion.md describe el flujo. | Cumple | Recorrido completo documentado y con rutas citadas. |
| Arranque documentado con un solo comando | README.md sección 'Arranque con un solo comando' con scripts/run_s4.ps1 y run_s4.sh. | Cumple | Requisitos previos declarados y comando único. |
| Prueba automatizada del recorrido completo, en verde | README.md cita backend/tests/test_publicaciones_vertical.py y enlace a GitHub Actions run #12 con resultado success. | Cumple | Prueba de punta a punta ejecutada en CI. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | README.md afirma que ASP-05 está completa, pero no se proporciona el contenido de docs/aspectos.md. | No verificado | Falta verificar cada celda navegable hasta su destino. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET, visible true; autores consolidados: nilver-garcia/Nnigarp (Nilver), camilixo92 (Camilo), Carulla-sd (Joshua). | Cumple | Los tres integrantes declarados aparecen en el historial. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md. | Cumple | Rutas requeridas presentes. |
| Estado del repositorio calificado | Hash 0197341, fecha 2026-08-29T01:13:49-05:00, anterior al cierre 2026-08-31T05:00:00Z. | Cumple | Commit vigente dentro del plazo. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md sigue numeración y kebab-case; contenido incluye contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | ADR aceptado sin ediciones posteriores. |
| Tabla de aspectos | Existe docs/aspectos.md pero no se proporciona su contenido. | No verificado | No se puede comprobar columnas ni navegabilidad. |
| Registro de uso de IA | Existe docs/ia.md con commits en fechas, pero no se proporciona contenido. | No verificado | Falta verificar columnas de qué se aceptó/rechazó y por qué. |
| README | README.md incluye qué es, arranque con un solo comando, pruebas y requisitos previos. | Cumple | Documento completo para reproducibilidad. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml existe y CI run #12 success, pero no hay configuración de SonarCloud (sin sonar-project.properties ni workflow). | No cumple | Falta análisis estático requerido por contrato. |

## Recuento y nota sugerida

8 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Glosario iniciado con términos del dominio: falta contenido de docs/arc42/12-glosario.md.
- Fila de aspectos completa hasta Pruebas: falta contenido de docs/aspectos.md.
- Tabla de aspectos (transversal): falta contenido de docs/aspectos.md.
- Registro de uso de IA (transversal): falta contenido de docs/ia.md.

## Hallazgos para la planilla

- Sin evidencia de SonarCloud en el repositorio.
- No se pudo verificar contenido de glosario y tabla de aspectos por falta de extractos.
- Autores consolidados: tres integrantes presentes en historial.
- Diagramas C4 como código (PlantUML).
