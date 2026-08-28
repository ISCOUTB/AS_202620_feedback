# semana-04-evidencia-s4 · DinamikUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `3aa2399` (2026-08-28T01:01:01-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | Existen archivos docs/arc42/01 a 06, pero solo se dispone del contenido de 01-04; no se pudo inspeccionar 05 y 06. | No verificado | Se requiere leer docs/arc42/05-building-block-view.md y 06-runtime-view.md para confirmar redacción. |
| arc42 sección 9 al día y enlazada con los ADR existentes | Existe docs/arc42/09-architecture-decisions.md y docs/adr/0001-seleccion-monolito-modular.md, pero no se tiene el contenido de la sección 9. | No verificado | Falta verificar si la sección 9 cita el ADR-0001. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | Existe docs/arc42/10-quality-requirements.md, pero no se tiene su contenido; la sección 4 referencia Q-01, Q-02, Q-03. | No verificado | No se puede comprobar coherencia sin leer la sección 10. |
| Glosario iniciado con términos del dominio | Existe docs/arc42/12-glossary.md, pero no se tiene su contenido. | No verificado | Falta verificar si contiene términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo se encuentra docs/c4/contexto.png y contexto.puml; no hay archivos de nivel 2. | No cumple | Falta el diagrama de nivel 2 (contenedores). |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No existe diagrama de nivel 2, por lo que no hay nada que contrastar con la estructura de directorios. | No cumple | Sin nivel 2, este criterio no se puede satisfacer. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Existen archivos backend/app/main.py y módulos, pero no se inspeccionó el código para confirmar el recorrido. | No verificado | Se requiere leer el código fuente para verificar interfaz, lógica y persistencia. |
| Arranque documentado con un solo comando | README.md tiene sección 'Ejecución del Proyecto', pero el contenido proporcionado está truncado y no muestra el comando. | No verificado | Falta leer la sección completa del README. |
| Prueba automatizada del recorrido completo, en verde | Existe backend/tests/test_main.py y .github/workflows/ci.yml, pero no se tiene evidencia de ejecución en verde. | No verificado | Se requiere consultar los runs de CI para confirmar. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | Existe docs/aspectos.md, pero no se tiene su contenido. | No verificado | Falta verificar si hay al menos una fila completa hasta Pruebas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_DinamikUTB en organización ISCOUTB, visible: true; autores consolidados: Juan José Vargas Pérez, Luis Daniel Padilla Leottau, Gillianis Perez Revolledo, Esteban Ramirez Rios, que coinciden con los 4 integrantes declarados. | Cumple | Sin observaciones. |
| Estructura mínima | Árbol muestra docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md. | Cumple | Sin observaciones. |
| Estado calificado (versionado) | Hash calificado 3aa2399 con fecha 2026-08-28T01:01:01-05:00, anterior al cierre 2026-08-31T05:00:00Z; sin commits nuevos después. | Cumple | Sin observaciones. |
| Convenciones de ADR | Archivo docs/adr/0001-seleccion-monolito-modular.md sigue convención de nombre y contiene contexto, opciones, decisión, consecuencias y trazabilidad. | Cumple | Sin observaciones. |
| Tabla de aspectos | Existe docs/aspectos.md, pero no se tiene su contenido. | No verificado | Falta verificar si tiene filas y columnas completas. |
| Registro de IA | docs/ia.md existe y el log muestra múltiples commits desde 2026-08-09 hasta 2026-08-28. | Cumple | Sin observaciones. |
| README | README.md existe y contiene descripción, pero no se pudo confirmar la presencia de un comando único de arranque. | No verificado | Falta leer la sección de ejecución completa. |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml, pero no se tiene evidencia de runs ni de análisis estático en SonarCloud. | No verificado | Se requiere consultar la API de GitHub Actions y SonarCloud. |

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 5 y 6: falta contenido
- arc42 sección 9: falta contenido
- arc42 sección 10: falta contenido
- Glosario: falta contenido
- Corte vertical: falta inspección de código
- Arranque: falta sección completa del README
- Prueba automatizada: falta evidencia de CI
- Fila de aspectos: falta contenido
- Tabla de aspectos (transversal): falta contenido
- README (transversal): falta sección de ejecución
- Pipeline (transversal): falta evidencia de runs

## Hallazgos para la planilla

- Falta diagrama C4 nivel 2
- No se pudo verificar contenido de secciones arc42 5,6,9,10,12
- No se pudo verificar corte vertical ni prueba automatizada
- No se pudo verificar arranque con un solo comando
- No se pudo verificar fila de aspectos
- No se pudo verificar pipeline en ejecución
