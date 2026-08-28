# semana-04-evidencia-s4 · Clubs UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `fe29e6e` (2026-08-28T13:41:01-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/ no contiene archivos 05 ni 06 | No cumple | Faltan las secciones 5 y 6 |
| arc42 sección 9 al día y enlazada con los ADR existentes | No existe docs/arc42/09*.md | No cumple | Sección 9 ausente |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10_requisitos_de_calidad.md contiene escenarios U1-U3, C1-C3 | No verificado | No se dispone de la evidencia de semana 2 para contrastar coherencia |
| Glosario iniciado con términos del dominio | No existe docs/arc42/12*.md | No cumple | Sección 12 ausente |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/C4/ solo contiene contexto.md | No cumple | Falta diagrama de nivel 2 |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay C4 nivel 2 | No cumple | Sin nivel 2 no se puede verificar correspondencia |
| Corte vertical que atraviesa interfaz, lógica y persistencia | backend/src/linkclub/adapters/inbound/api/health_router.py, backend/src/linkclub/application/use_cases/check_health.py, backend/src/linkclub/adapters/outbound/persistence/in_memory_status_adapter.py | Cumple | Las tres rutas existen en el árbol |
| Arranque documentado con un solo comando | README.md no incluye comando de arranque; sección 6 indica que no hay código activo | No cumple | Falta sección de arranque |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_health.py existe, pero no hay URL de run de CI | No verificado | Falta evidencia de ejecución en verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md no contiene tabla con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia | No cumple | No hay fila de aspectos |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Clubs_UTB en ISCOUTB, público, autores consolidados 4 | Cumple | Coincide con integrantes declarados |
| Estructura mínima | Árbol incluye README.md, docs/arc42/, docs/adr/, docs/C4/, docs/aspectos.md, docs/ia.md | Cumple | Rutas requeridas presentes |
| Estado calificado/versionado | Hash fe29e6e, fecha 2026-08-28T13:41:01-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit vigente correcto |
| Convenciones de ADR | docs/adr/0001-hexagonal.md no incluye sección de trazabilidad | No cumple | Falta trazabilidad (requisito, C4, commit, pruebas) |
| Tabla de aspectos | docs/aspectos.md no contiene tabla con las ocho columnas | No cumple | Sin filas navegables |
| Registro de IA | docs/ia.md solo registra un uso sin rechazos ni motivos | No cumple | Falta columna de rechazo |
| README | README.md no incluye comando de arranque único | No cumple | No documenta cómo arrancar |
| Pipeline y análisis estático | No existe .github/workflows/ en el árbol | No cumple | Sin CI ni SonarCloud |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Coherencia de arc42 sección 10 con escenarios de semana 2: falta evidencia de semana 2
- Prueba automatizada en verde: falta URL de run de CI

## Hallazgos para la planilla

- Faltan arc42 secciones 5, 6, 9 y 12
- No hay diagrama C4 nivel 2
- docs/aspectos.md no tiene tabla de trazabilidad
- README sin comando de arranque
- Sin pipeline de CI
- ADR 0001 sin trazabilidad
- docs/ia.md sin rechazos
- README desactualizado: dice que no hay código activo pero existe backend
