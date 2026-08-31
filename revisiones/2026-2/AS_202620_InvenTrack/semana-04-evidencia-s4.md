# semana-04-evidencia-s4 · InvenTrack

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `d7ba824` (2026-08-30T23:39:33-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md indica solo secciones 1,2,3,10 completas | No cumple | Secciones 4,5,6 pendientes |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se encuentra sección 9 en docs/arc42/arc42-template-EN.md | No cumple | Sección 9 no redactada |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42-template-EN.md incluye Quality Requirements con escenarios ESC-01..05 | Cumple | Coherente con aspectos.md |
| Glosario iniciado con términos del dominio | No hay sección 12 en arc42 | No cumple | Glosario ausente |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/context.md y docs/c4/containers.md existen | No cumple | Bandeja del nivel 1 no aparece en nivel 2 |
| Límites del C4 nivel 2 correspondientes a la estructura del código | containers.md tabla: API Backend -> app/, Web y Db sin código | No cumple | Contenedores Web y Db no tienen correspondencia en repo |
| Corte vertical que atraviesa interfaz, lógica y persistencia | app/productos/infrastructure/router.py, app/productos/application/crear_producto.py, app/productos/infrastructure/in_memory_repository.py | Cumple | Recorrido completo con persistencia en memoria |
| Arranque documentado con un solo comando | README y ADR-0001 declaran `python -m uvicorn app.main:app --reload` | Cumple | Comando único documentado |
| Prueba automatizada del recorrido completo, en verde | tests/productos/test_api_corte_vertical.py existe | No verificado | Sin URL de run de CI que muestre verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila ASP-01: Pruebas='Pendiente' | No cumple | Celda Pruebas sin enlace navegable |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_InvenTrack en ISCOUTB, público, 4 integrantes en historial | Cumple | Identidades consolidadas: Josephva24/Jose Vargas = Jose Vargas, Felix Taborda/FlexT21 = Felix Taborda |
| Estructura mínima | docs/adr/0002-usar-monolito-modular-con-hexagonal-por-modulo sin .md | No cumple | Falta extensión .md en ADR-0002 |
| Estado calificado | Commit d7ba824 2026-08-30T23:39:33-05:00 anterior al cierre | Cumple | Sin etiqueta requerida para semanal |
| Convenciones de ADR | ADR-0001 Propuesto, ADR-0002 Aceptado con mismo título sin marcar reemplazo | No cumple | ADR-0001 no marcado como reemplazado; ADR-0002 sin .md |
| Tabla de aspectos | docs/aspectos.md fila ASP-01 con Pruebas Pendiente | No cumple | Celda no navegable |
| Registro de uso de IA | docs/ia.md con entradas y columna rechazado | Cumple | Registro crece en commits |
| README | README.md con descripción, arranque y pruebas | Cumple | Documenta comando único |
| Pipeline y análisis estático | .github/workflows/test.yml presente | No verificado | Sin evidencia de runs ni SonarCloud; haría falta consultar Actions |

## Recuento y nota sugerida

3 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.2 = 1 + 4 × (3/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba automatizada en verde: falta URL de run de CI
- Pipeline y análisis estático: falta evidencia de ejecución y SonarCloud

## Hallazgos para la planilla

- Secciones arc42 4,5,6,9,12 no redactadas
- ADR-0002 sin extensión .md y duplica ADR-0001 sin marcar reemplazo
- C4 nivel 2 omite sistema externo Bandeja del nivel 1
- Contenedores Web y Db dibujados sin código correspondiente
- Fila ASP-01 con Pruebas Pendiente
- Sin evidencia de CI en verde
- Commits posteriores al cierre (no calificados): 9cce393 2026-08-31T00:20:09-05:00 Merge branch 'main' of https://github.com/ISCOUTB/AS_202620_InvenTrack; 4e6957e 2026-08-31T00:20:01-05:00 fix: update aspectos.md to refine data consistency aspect and improve traceability table
