# semana-04-evidencia-s4 · Drift

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `c4cda62` (2026-08-27T22:44:48-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42_1_introduccion_objetivos.md, arc42_2_restricciones.md, arc42_3_contexto_alcance.md, arc42_4_soluciones_arquitectonica.md, arc42_5_vista_bloques.md, arc42_6_Vista_Ejecucion.md presentes; contenido de 1-5 redactado específico de DRIFT | Cumple | No se detectó texto de plantilla en los archivos mostrados |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/arc42_9_Decisiones_Arquitectonicas.md existe pero no se incluyó su contenido | No verificado | Se requiere verificar que cite docs/adr/0001 y 0002 |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42_10_Requisitos_Calidad.md incluye QS-01 a QS-05 y referencia a docs/Escenarios.md | Cumple | Coherente con escenarios definidos |
| Glosario iniciado con términos del dominio | docs/arc42/arc42_12_Glosario.md contiene términos propios como DRIFT, Adaptador, Tienda digital, Núcleo de dominio | Cumple | Glosario específico del sistema |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.md y docs/c4/contenedores.md existen pero no se incluyó su contenido | No verificado | Se requiere verificar actores y contenedores entre niveles |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin contenido de docs/c4/contenedores.md; estructura de código muestra backend/app/domain, application, infrastructure | No verificado | No se pudo contrastar contenedores con directorios |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Solo backend/app/main.py y backend/tests/test_health.py; directorios domain/application/infrastructure contienen archivos .md, no código de lógica/persistencia | No cumple | Falta implementación real del recorrido |
| Arranque documentado con un solo comando | README.md existe pero el contenido proporcionado no muestra sección de arranque | No verificado | Se requiere verificar comando único y requisitos previos |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_health.py es la única prueba; no hay prueba de corte vertical | No cumple | Sin evidencia de prueba e2e ni run en CI |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md existe pero no se incluyó su contenido | No verificado | Se requiere verificar al menos una fila con todas las celdas navegables |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Drift público en ISCOUTB; autores consolidados: 4 integrantes con commits | Cumple | Todos los integrantes declarados aparecen en historial |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Estructura conforme |
| Estado del repositorio calificado | Commit c4cda62 (2026-08-27T22:44:48-05:00) anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta requerida para evidencia semanal |
| Convenciones de ADR | docs/adr/0001-arquitectura-base.md y 0002-arquitectura-base.md con mismo título; 0001 no marcado como reemplazado; 0002 duplica contenido | No cumple | Violación de convención: ADR aceptado no se edita; reemplazo debe marcar anterior |
| Tabla de aspectos | docs/aspectos.md existe pero sin contenido proporcionado | No verificado | Se requiere verificar filas completas |
| Registro de uso de IA | docs/ia.md existe con commits, pero sin contenido | No verificado | Se requiere verificar columnas de aceptado/rechazado |
| README | README.md existe pero no se muestra sección de arranque con un solo comando | No verificado | Se requiere verificar reproducibilidad |
| Pipeline y análisis estático | .github/workflows/ci.yml existe, pero sin evidencia de ejecución ni SonarCloud | No verificado | Se requiere URL de run en verde y análisis estático |

## Recuento y nota sugerida

3 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.2 = 1 + 4 × (3/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de arc42_9 y enlaces a ADR
- Coherencia C4 nivel 1 y 2
- Correspondencia C4-código
- Arranque con un solo comando en README
- Fila de aspectos completa
- Contenido de docs/ia.md
- Ejecución del pipeline y SonarCloud

## Hallazgos para la planilla

- ADR 0002 duplica 0001 sin marcar reemplazo
- No hay código de lógica/persistencia, solo archivos .md en backend
- Solo existe test_health.py, sin prueba de recorrido completo
- No se evidencia pipeline ejecutado ni análisis SonarCloud
