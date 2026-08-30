# semana-04-evidencia-s4 · Clubs UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `7d8ae37` (2026-08-29T20:13:48-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/06_* no existe; solo 01-05 y 10 presentes | No cumple | Falta sección 6 (vista de ejecución) |
| arc42 sección 9 al día y enlazada con los ADR existentes | no existe docs/arc42/09_* | No cumple | Sección 9 ausente |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10_requisitos_de_calidad.md contiene escenarios U1-U3, C1-C3 coherentes con el dominio | Cumple | No se pudo contrastar con semana 2 por falta de evidencia previa, pero el contenido es coherente |
| Glosario iniciado con términos del dominio | no existe docs/arc42/12_* | No cumple | Glosario ausente |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | solo docs/C4/contexto.md (nivel 1); no hay nivel 2 | No cumple | Falta diagrama de contenedores (nivel 2) |
| Límites del C4 nivel 2 correspondientes a la estructura del código | no hay C4 nivel 2 para contrastar | No cumple | Sin nivel 2 no se puede verificar correspondencia |
| Corte vertical que atraviesa interfaz, lógica y persistencia | rutas: backend/src/linkclub/adapters/inbound/api/health_router.py, backend/src/linkclub/application/use_cases/check_health.py, backend/src/linkclub/adapters/outbound/persistence/in_memory_status_adapter.py | Cumple | Corte vertical mínimo de health check presente |
| Arranque documentado con un solo comando | README no incluye sección de arranque con comando único | No cumple | Falta documentar requisitos previos y comando de arranque |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_health.py existe, pero no hay evidencia de run de CI en verde | No verificado | Falta URL de run que ejecute la prueba |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md no contiene tabla con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas | No cumple | Falta fila de trazabilidad |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_Clubs_UTB en ISCOUTB, visible true | Cumple | Cumple |
| Estructura mínima | rutas presentes; docs/C4/ en mayúscula (desviación menor) | Cumple | Desviación de estructura: docs/C4/ en lugar de docs/c4/ |
| Estado del repositorio calificado | no se evidencia etiqueta corte-1; commit 7d8ae37 anterior al cierre | No cumple | Falta etiqueta de corte |
| Convenciones de ADR | docs/adr/0001-hexagonal.md sin sección de trazabilidad | No cumple | Falta trazabilidad en ADR |
| Tabla de aspectos | docs/aspectos.md sin tabla de 8 columnas | No cumple | Falta fila de trazabilidad |
| Registro de uso de IA | docs/ia.md sin columna de rechazos | No cumple | Falta qué se rechazó y por qué |
| README | README sin sección de arranque | No cumple | Falta comando único y requisitos previos |
| Pipeline y análisis estático | no hay .github/workflows/ en el árbol | No cumple | Sin pipeline configurado |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba automatizada en verde: falta URL de run de CI

## Hallazgos para la planilla

- Faltan secciones arc42 6, 9 y 12
- Solo existe C4 nivel 1, falta nivel 2
- README no documenta arranque con un solo comando
- docs/aspectos.md no tiene tabla de trazabilidad
- ADR sin trazabilidad
- Registro de IA sin rechazos
- No hay pipeline de CI
- No se evidencia etiqueta de corte
