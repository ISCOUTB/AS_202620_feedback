# semana-04-evidencia-s4 · EnAgenda

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `2bdb540` (2026-08-25T13:45:18-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/02- restricciones.md y 03-contexto y alcance.md redactados; 01,04,05,06 no incluidos en evidencia | No verificado | No se puede confirmar redacción de secciones 1,4,5,6 |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-decisiones-de-arquitectura.md: 'Esta sección se completará durante el desarrollo del proyecto.' | No cumple | Sección 9 sin redactar, sin enlaces a ADR |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-requisitos-de-calidad.md incluye EC-01 a EC-05 | Cumple | Escenarios coherentes con el dominio |
| Glosario iniciado con términos del dominio | docs/arc42/12-glosario.md: 'Esta sección se completará durante el desarrollo del proyecto' | No cumple | Sin términos del dominio |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/nivel-1-contexto.md y nivel-2-contenedores.md con actores y contenedores coherentes | Cumple | Actores reaparecen; contenedores dentro del sistema |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay directorios de código; solo docs/src/modulos/eventos.md vacío | No cumple | Contenedores dibujados sin código correspondiente |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Sin archivos de código; solo docs/src/modulos/eventos.md vacío | No cumple | No hay recorrido implementado |
| Arranque documentado con un solo comando | README.md sin sección de arranque ni comando | No cumple | Falta requisitos previos y comando |
| Prueba automatizada del recorrido completo, en verde | Sin archivos de prueba ni CI | No cumple | No hay prueba del corte vertical |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con celdas 'Pendiente' | No cumple | Celdas C4, ADR, Código, Pruebas sin contenido |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_EnAgenda público; autores: gabimoralesc30, jeimy4637, eliabarnedocondef10 | Cumple | Tres integrantes en historial |
| Estructura mínima | Arbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura presente |
| Estado del repositorio calificado | Commit 2bdb540 fecha 2026-08-25T13:45:18-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin commits tardíos |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md con nombre correcto y contenido | Cumple | Un ADR aceptado |
| La tabla de aspectos | docs/aspectos.md fila A-01 con celdas 'Pendiente' | No cumple | Celdas no navegables |
| Registro de uso de IA | docs/ia.md con entradas que incluyen rechazos y motivos | Cumple | Registro presente |
| README | README.md sin comando de arranque ni pruebas | No cumple | Falta reproducibilidad |
| Pipeline y análisis estático | Sin .github/workflows en arbol; sin runs | No cumple | No hay CI configurada |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 1,4,5,6: contenido no incluido en evidencia

## Hallazgos para la planilla

- Sección 9 y 12 de arc42 sin redactar
- No hay código ni corte vertical
- Fila de aspectos incompleta
- README sin instrucciones de arranque
- Sin pipeline CI
