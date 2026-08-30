# semana-04-evidencia-s4 · Drift

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `ff339e9` (2026-08-29T21:53:23-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | Existen docs/arc42/arc42_1_introduccion_objetivos.md, arc42_2_restricciones.md, arc42_3_contexto_alcance.md, arc42_4_soluciones_arquitectonica.md, arc42_5_vista_bloques.md, arc42_6_Vista_Ejecucion.md; contenido de sección 6 no mostrado en evidencia. | No verificado | No se pudo comprobar redacción de sección 6 ni ausencia total de texto de plantilla sin ejecutar grep. |
| arc42 sección 9 al día y enlazada con los ADR existentes | Existe docs/arc42/arc42_9_Decisiones_Arquitectonicas.md, pero su contenido no está en la evidencia. | No verificado | Falta verificar que cite docs/adr/0001-*.md y 0002-*.md. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42_10_Requisitos_Calidad.md incluye tabla QS-01..QS-05 y declara que corresponden a docs/Escenarios.md. | Cumple | Coherencia explícita con escenarios de semana 2. |
| Glosario iniciado con términos del dominio | docs/arc42/arc42_12_Glosario.md define términos propios: DRIFT, Adaptador, Tienda digital, Núcleo de dominio, etc. | Cumple | Glosario con términos del sistema, no genéricos. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Existen docs/c4/contexto.md y docs/c4/contenedores.md, pero no se incluye su contenido. | No verificado | No se puede comprobar coherencia de actores y contenedores sin ver los diagramas. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Estructura de código: backend/app/domain, application, infrastructure; frontend/. No se dispone del contenido de docs/c4/contenedores.md. | No verificado | Falta contrastar contenedores dibujados con directorios reales. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Rutas candidatas: backend/app/main.py (interfaz), backend/app/application/usecases/search_games.py (lógica), backend/app/infrastructure/persistence/in_memory_game_repository.py (persistencia). | No verificado | No se pudo confirmar que estas rutas estén conectadas en un recorrido ejecutable sin ver el código. |
| Arranque documentado con un solo comando | README.md existe y describe estructura, pero el fragmento mostrado no incluye la sección de arranque con comando único. | No verificado | Falta ver el comando declarado y requisitos previos. |
| Prueba automatizada del recorrido completo, en verde | Existe backend/tests/test_health.py y .github/workflows/ci.yml, pero no hay URL de run ni evidencia de ejecución en verde. | No verificado | Sin evidencia de CI no se puede marcar Cumple. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | Existe docs/aspectos.md, pero no se muestra su contenido. | No verificado | No se puede verificar que la fila tenga todas las celdas navegables hasta Pruebas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Drift en organización ISCOUTB, visible true; autores consolidados: 4 integrantes (lmpdiaz12, maufern4ndez, JerryDBM/Sherry, JoshuaR01/JoshXX). | Cumple | Cumple nombre, organización, visibilidad e integrantes. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md. | Cumple | Estructura mínima presente. |
| Estado del repositorio calificado | Commit calificado ff339e9 con fecha 2026-08-29T21:53:23-05:00, anterior al cierre 2026-08-31T05:00:00Z. | Cumple | Commit vigente correcto para evidencia semanal. |
| Convenciones de ADR | docs/adr/0001-arquitectura-base.md no enlaza a 0002; 0002 indica cambio de stack sin marcar 0001 como reemplazado. | No cumple | Se incumple regla de ADR aceptado no editado: falta enlace de reemplazo. |
| Tabla de aspectos | Existe docs/aspectos.md, pero sin contenido en la evidencia. | No verificado | No se puede comprobar completitud de filas. |
| Registro de uso de IA | docs/ia.md existe y tiene historial de commits (12 entradas), pero no se muestra contenido. | No verificado | Falta verificar columna de rechazos con motivo técnico. |
| README | README.md existe con descripción y estructura, pero no se muestra comando de arranque único. | No verificado | No se puede confirmar reproducibilidad. |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml, pero no hay evidencia de runs ni de SonarCloud. | No verificado | Sin URL de run no se puede marcar Cumple. |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 6: falta contenido para confirmar redacción sin plantilla.
- arc42 sección 9: falta contenido para verificar enlaces a ADR.
- C4 niveles 1 y 2: falta contenido de diagramas para comprobar coherencia.
- Correspondencia C4-código: falta diagrama de contenedores.
- Corte vertical: falta código para confirmar conexión entre capas.
- Arranque: falta sección de comando en README.
- Prueba automatizada: falta URL de run de CI.
- Fila de aspectos: falta contenido de docs/aspectos.md.
- Tabla de aspectos (transversal): falta contenido.
- Registro de IA: falta contenido para verificar rechazos.
- README (transversal): falta comando de arranque.
- Pipeline: falta evidencia de runs y SonarCloud.

## Hallazgos para la planilla

- ADR 0001 no está marcado como reemplazado por 0002, incumpliendo convención.
- No hay evidencia de ejecución de CI ni de pruebas en verde.
- Sección 6 de arc42 y C4 no tienen contenido visible en la evidencia.
- Falta verificar comando de arranque único en README.
