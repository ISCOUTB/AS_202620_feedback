# semana-04-evidencia-s4 · Tienda virtual UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `0d208a2` (2026-08-29T21:37:39-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md (contenido truncado en evidencia) | No verificado | Se verifican secciones 1-3 redactadas; faltan 4-6 por truncamiento. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/arc42-template-EN.md (no visible sección 9) | No verificado | Contenido truncado; no se puede comprobar enlace a docs/adr/0001. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42-template-EN.md (no visible sección 10) | No verificado | No se puede contrastar con docs/escenarios-calidad.md. |
| Glosario iniciado con términos del dominio | docs/arc42/arc42-template-EN.md (no visible sección 12) | No verificado | Falta ver términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/context.md y docs/c4/container.md | Cumple | Actores y contenedores coinciden; flechas etiquetadas. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/container.md lista web, api, db; árbol muestra frontend/, backend/, compose.yaml | Cumple | Correspondencia directa con servicios de compose. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md sección 'Corte vertical ejecutable'; rutas frontend/app/page.tsx, backend/app/modules/catalog/router.py, repository.py, models.py | Cumple | Recorrido documentado de extremo a extremo. |
| Arranque documentado con un solo comando | README.md sección 'Arranque con un solo comando': docker compose up --build | Cumple | Requisitos previos declarados. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_catalog.py existe; .github/workflows/tests.yml configurado | No verificado | Falta URL de run de GitHub Actions que muestre ejecución en verde; la prueba no cubre frontend. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tabla con 6 columnas, faltan ID y C4 | No cumple | La fila de disponibilidad tiene pruebas pero no cumple las 8 columnas del contrato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible true, repo AS_202620_TIENDA-VIRTUAL-UTB | Cumple | Nombre y visibilidad correctos; organización no explícita en evidencia. |
| Estructura mínima | árbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Todas las rutas requeridas presentes. |
| Estado del repositorio calificado | hash 0d208a2, fecha 2026-08-29T21:37:39-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit vigente correcto. |
| Convenciones de ADR | docs/adr/0001-monolito-modular.md sin sección de trazabilidad | No cumple | Falta enlace a requisito/aspecto, C4, commit y pruebas. |
| Tabla de aspectos | docs/aspectos.md con columnas insuficientes | No cumple | Faltan ID y C4; no cumple las 8 columnas. |
| Registro de uso de IA | docs/ia.md sin columna de rechazos | No cumple | No registra qué se rechazó y por qué. |
| README | README.md con qué es, arranque y pruebas | Cumple | Cumple requisitos. |
| Pipeline y análisis estático | .github/workflows/tests.yml presente, sin SonarCloud ni runs | No cumple | Falta evidencia de ejecución y análisis estático. |

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 5,6,9,10,12: contenido truncado, falta archivo completo
- prueba automatizada en verde: falta URL de run de GitHub Actions
- identidad organización: falta confirmar org ISCOUTB
- pipeline ejecución: falta run de CI

## Hallazgos para la planilla

- arc42 truncado en evidencia, secciones 5,6,9,10,12 no verificables
- aspectos.md no tiene columnas ID y C4
- ADR sin trazabilidad explícita
- ia.md sin columna de rechazos
- sin evidencia de ejecución de CI ni SonarCloud
- prueba de recorrido completo no cubre frontend
