# semana-04-evidencia-s4 · Drift

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `4254f4a` (2026-08-30T19:13:01-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | Existen docs/arc42/arc42_1..6, pero no se incluyó contenido de arc42_6_Vista_Ejecucion.md | No verificado | Secciones 1-5 redactadas con contenido DRIFT; falta verificar sección 6. |
| arc42 sección 9 al día y enlazada con los ADR existentes | Archivo docs/arc42/arc42_9_Decisiones_Arquitectonicas.md presente, sin contenido en evidencia | No verificado | No se puede comprobar enlaces a ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42_10_Requisitos_Calidad.md tabla 10.2 con QS-01..QS-05 referenciando docs/Escenarios.md | Cumple | Coherente con escenarios definidos. |
| Glosario iniciado con términos del dominio | docs/arc42/arc42_12_Glosario.md incluye términos propios: DRIFT, Tienda digital, Adaptador, etc. | Cumple | Glosario con términos del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Existen docs/c4/contexto.md y docs/c4/contenedores.md, sin contenido | No verificado | Falta verificar coherencia de actores y contenedores. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin contenido de docs/c4/contenedores.md para contrastar con backend/frontend | No verificado | No se puede comparar contenedores con directorios. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | backend/app/main.py (interfaz), backend/app/application/usecases/search_games.py (lógica), backend/app/infrastructure/persistence/in_memory_game_repository.py (persistencia) | Cumple | Tres capas presentes. |
| Arranque documentado con un solo comando | README.md presente, pero no se incluyó sección de arranque en evidencia | No verificado | Falta ver comando de arranque. |
| Prueba automatizada del recorrido completo, en verde | Solo existe backend/tests/test_health.py; no hay prueba para search_games | No cumple | Falta prueba del corte vertical. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md presente, sin contenido | No verificado | No se puede comprobar fila completa. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Drift en ISCOUTB, público, autores 4 integrantes | Cumple | Cumple identidad. |
| Estructura mínima | Arbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura completa. |
| Estado del repositorio calificado | Hash 4254f4a, fecha 2026-08-30T19:13:01-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit vigente correcto. |
| Convenciones de ADR | docs/adr/0001 y 0002: 0002 no marca 0001 como reemplazado; ambos con mismo título | No cumple | ADR aceptado no se edita; falta enlace de reemplazo. |
| Tabla de aspectos | docs/aspectos.md existe, sin contenido | No verificado | Falta verificar columnas y filas. |
| Registro de uso de IA | docs/ia.md con commits, sin contenido | No verificado | Falta verificar columnas de rechazo. |
| README | README.md presente, sin sección de arranque en evidencia | No verificado | Falta ver comando único. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe, sin runs ni SonarCloud | No verificado | Falta evidencia de ejecución. |

## Recuento y nota sugerida

3 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.2 = 1 + 4 × (3/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 6
- arc42 sección 9
- C4 nivel 1 y 2 coherencia
- Correspondencia C4-código
- Arranque con un solo comando
- Fila de aspectos completa
- Tabla de aspectos (transversal)
- Registro de IA (transversal)
- README (transversal)
- Pipeline (transversal)

## Hallazgos para la planilla

- Sección 6 de arc42 no verificable por falta de contenido en evidencia.
- No hay prueba automatizada del corte vertical; solo test_health.py.
- ADR 0002 no marca 0001 como reemplazado, violando convención.
- Falta contenido de docs/c4/ para verificar coherencia.
- README no muestra comando de arranque en evidencia.
- Pipeline sin runs verificados.
