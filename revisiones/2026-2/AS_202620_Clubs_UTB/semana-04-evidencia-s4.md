# semana-04-evidencia-s4 · Clubs UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `8d69f62` (2026-08-24T00:21:05-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/ solo contiene 01,02,03,04,10; faltan 05 y 06 (hash 8d69f62, 2026-08-24) | No cumple | No existen las secciones 5 y 6, por lo que no se puede verificar redacción ni ausencia de plantilla en ellas. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No hay archivo docs/arc42/09* en el árbol (hash 8d69f62) | No cumple | Falta la sección 9 de decisiones de arquitectura. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10_requisitos_de_calidad.md incluye escenarios U1-U3 y C1-C3 alineados con metas de sección 1 (hash 8d69f62) | Cumple | La sección 10 mantiene coherencia con los escenarios de calidad definidos. |
| Glosario iniciado con términos del dominio | No existe docs/arc42/12* (hash 8d69f62) | No cumple | Falta la sección 12 con glosario de términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo existe docs/C4/contexto.md (nivel 1); no hay nivel 2 (hash 8d69f62) | No cumple | Falta el diagrama de contenedores (nivel 2) y su coherencia con el contexto. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin C4 nivel 2 no se puede contrastar con el código (hash 8d69f62) | No cumple | No aplica por ausencia del nivel 2. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | backend/src/linkclub/adapters/inbound/api/health_router.py, backend/src/linkclub/application/use_cases/check_health.py, backend/src/linkclub/adapters/outbound/persistence/in_memory_status_adapter.py (hash 8d69f62) | Cumple | Las tres capas del recorrido están presentes con nombres coherentes. |
| Arranque documentado con un solo comando | README.md no incluye sección de arranque ni comando único (hash 8d69f62) | No cumple | El README declara que no hay desarrollo activo y no documenta requisitos previos ni comando. |
| Prueba automatizada del recorrido completo, en verde | Existe backend/tests/test_health.py, pero no hay workflow ni run de CI en la evidencia (hash 8d69f62) | No verificado | Sin pipeline no se puede confirmar ejecución en verde; comando de prueba no documentado. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md no contiene tabla con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia (hash 8d69f62) | No cumple | El archivo solo tiene secciones de problema, tecnologías, estado y autores. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Clubs_UTB en ISCOUTB, visible true; autores incluyen los 4 integrantes (hash 8d69f62) | Cumple | Identidades consolidadas: Josh4OP y Josh Ortega son la misma persona; todos los declarados aparecen. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/, docs/C4/, docs/aspectos.md, docs/ia.md, README.md (hash 8d69f62) | Cumple | C4 en mayúscula es desviación menor, no ausencia. |
| Estado del repositorio calificado | No se registra etiqueta en la evidencia; hash calificado 8d69f62 (2026-08-24) | No cumple | Falta etiqueta de corte o de actividad; se revisa último commit anterior al cierre. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md sin trazabilidad; docs/adr/.temp no sigue convención (hash 8d69f62) | No cumple | ADR sin sección de trazabilidad y archivo .temp sobrante. |
| Tabla de aspectos | docs/aspectos.md no contiene tabla con las 8 columnas requeridas (hash 8d69f62) | No cumple | Falta la cadena de trazabilidad aspecto→evidencia. |
| Registro de uso de IA | docs/ia.md solo describe intenciones generales, sin registros concretos de uso con rechazos (hash 8d69f62) | No cumple | No hay entradas específicas con herramienta, aceptado y rechazado. |
| README | README.md no incluye cómo arrancar con un solo comando ni cómo probar (hash 8d69f62) | No cumple | Faltan requisitos previos y comando de arranque. |
| Pipeline y análisis estático | No existe .github/workflows/ en el árbol (hash 8d69f62) | No cumple | Sin CI ni análisis estático configurado. |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba automatizada del recorrido completo en verde: falta evidencia de ejecución en CI

## Hallazgos para la planilla

- Faltan secciones arc42 5, 6, 9 y 12
- Solo existe C4 nivel 1; falta nivel 2
- docs/aspectos.md no tiene tabla de trazabilidad
- No hay pipeline de CI
- ADR sin trazabilidad y archivo .temp en docs/adr/
- docs/ia.md es genérico, sin usos concretos
- README no documenta arranque ni pruebas
- No se observa etiqueta de versión
