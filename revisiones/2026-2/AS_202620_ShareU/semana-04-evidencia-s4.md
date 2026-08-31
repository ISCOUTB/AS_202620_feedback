# semana-04-evidencia-s4 · ShareU

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `27e1190` (2026-08-30T15:22:02-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42.md existe en el árbol | No verificado | No se pudo inspeccionar el contenido para verificar redacción y ausencia de plantilla. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/adr/0001-estilo-arquitectonico.md existe | No verificado | No se pudo verificar la sección 9 ni sus enlaces a ADR por falta de contenido de arc42.md. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | Sin evidencia de escenarios ni contenido de sección 10 | No verificado | No se pudo comprobar coherencia con escenarios de semana 2. |
| Glosario iniciado con términos del dominio | docs/arc42/arc42.md existe | No verificado | No se pudo verificar la sección 12 ni términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/nivel1.mmd, nivel2.mmd, nivel-2.md, NIVEL2.png | No verificado | Archivos presentes, pero no se pudo verificar coherencia entre niveles sin contenido. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Estructura de código: app/administracion, app/busqueda, app/calificaciones, app/documentos, app/usuarios | No verificado | No se pudo contrastar con el diagrama C4 nivel 2 por falta de contenido del diagrama. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Rutas: app/*/router.py (interfaz), app/*/service.py (lógica), app/documentos/repository.py (persistencia) | No verificado | Se identifican capas, pero no se pudo verificar el recorrido completo sin inspeccionar el código. |
| Arranque documentado con un solo comando | README.md existe | No verificado | No se pudo leer el README para comprobar requisitos previos y comando único. |
| Prueba automatizada del recorrido completo, en verde | tests/test_busqueda.py existe; .github/workflows/tests.yml existe | No verificado | No se proporcionó URL de run de CI que muestre la prueba en verde. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos/aspectos.md existe | No verificado | No se pudo inspeccionar la tabla para verificar celdas navegables hasta Pruebas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | autores: 1 steven <sc478079@gmail.com>; integrantes declarados: 4 | No cumple | Solo un autor en el historial, se esperaban 4 integrantes. |
| Estructura mínima | Árbol incluye docs/arc42/arc42.md, docs/adr/0001-*.md, docs/c4/, docs/aspectos/aspectos.md, docs/ia.md, README.md | Cumple | Estructura mínima presente. |
| Versionado (estado calificado) | hash_calificado 27e1190, fecha 2026-08-30T15:22:02-05:00, cierre 2026-08-31T05:00:00Z | Cumple | Commit anterior al cierre, sin etiqueta requerida para evidencia semanal. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md cumple patrón de nombre | No verificado | No se pudo verificar contenido requerido (contexto, opciones, decisión, consecuencias, trazabilidad). |
| Tabla de aspectos | docs/aspectos/aspectos.md existe | No verificado | No se pudo inspeccionar la tabla para verificar columnas y enlaces. |
| Registro de uso de IA | docs/ia.md existe; ia_log: sin commits sobre docs/ia.md | No verificado | No se pudo verificar contenido ni crecimiento del registro. |
| README | README.md existe | No verificado | No se pudo leer para comprobar arranque con un solo comando y requisitos previos. |
| Pipeline y análisis estático | .github/workflows/tests.yml existe | No verificado | No se proporcionó evidencia de ejecución (runs) ni de análisis estático. |

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de arc42.md (secciones 1-6, 9, 10, 12)
- Coherencia de diagramas C4 y correspondencia con código
- Recorrido del corte vertical en código
- Comando de arranque en README
- Prueba automatizada en verde (sin URL de run)
- Fila de aspectos.md completa
- Contenido de ADR, aspectos.md, ia.md

## Hallazgos para la planilla

- Solo un autor en el historial, se esperaban 4 integrantes.
- No se pudo inspeccionar contenido de documentación por falta de acceso a archivos.
- No hay evidencia de ejecución de CI ni de análisis estático.
- El registro de IA no muestra commits, posiblemente sin actualizaciones.
