# semana-04-evidencia-s4 · EnAgenda

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `91bbaf5` (2026-08-28T20:43:32-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/01,04,05,06 no incluidos en la evidencia; 02 y 03 redactados | No verificado | No se pudo comprobar el contenido de 01,04,05,06; se requiere acceso a esos archivos. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-decisiones-de-arquitectura.md: 'Esta sección se completará durante el desarrollo del proyecto.' | No cumple | Sección 9 es placeholder, no enlaza ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-requisitos-de-calidad.md incluye árbol de utilidad y escenarios EC-01 a EC-05 | Cumple | Coherente con ADR 0001 que cita los mismos escenarios. |
| Glosario iniciado con términos del dominio | docs/arc42/12-glosario.md: 'Esta sección se completará durante el desarrollo del proyecto' | No cumple | Sin términos del dominio. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/nivel-1-contexto.md y docs/c4/nivel-2-contenedores.md con actores y contenedores coherentes | Cumple | Actores Organizador e Invitado reaparecen; contenedores dentro del sistema. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Árbol del repositorio no muestra directorios de código (solo docs y README) | No cumple | No hay código para contrastar con los contenedores. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Sin archivos de código en el árbol | No cumple | No existe corte vertical. |
| Arranque documentado con un solo comando | README.md no incluye sección de arranque ni comando | No cumple | Falta requisitos previos y comando único. |
| Prueba automatizada del recorrido completo, en verde | Sin código ni pruebas en el repositorio | No cumple | No hay prueba automatizada. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con celdas C4, ADR, Código, Pruebas, Evidencia en 'Pendiente' | No cumple | Fila incompleta. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_EnAgenda, visible true | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima | docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Estructura conforme. |
| Estado del repositorio calificado (versionado) | Commit 91bbaf5, fecha 2026-08-28T20:43:32-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit vigente correcto. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md existe y nombre correcto, pero contenido truncado | No verificado | No se pudo verificar trazabilidad (commit, pruebas, C4) por truncamiento. |
| Tabla de aspectos | docs/aspectos.md con fila A-01 incompleta | No cumple | Celdas en Pendiente. |
| Registro de uso de IA | docs/ia.md con entradas que incluyen qué se rechazó y verificación | Cumple | Registro adecuado. |
| README | README.md sin sección de arranque ni comando | No cumple | No cumple requisito de reproducibilidad. |
| Pipeline y análisis estático | No hay .github/workflows en el árbol | No cumple | Sin CI configurada. |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de arc42 secciones 1,4,5,6
- Trazabilidad completa del ADR 0001

## Hallazgos para la planilla

- Sección 9 de arc42 es placeholder
- Glosario sin términos
- No hay código fuente en el repositorio
- README sin comando de arranque
- Fila de aspectos incompleta
- ADR sin trazabilidad verificable
- Sin pipeline de CI
