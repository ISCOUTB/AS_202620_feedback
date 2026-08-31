# semana-04-evidencia-s4 · DinamikUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `8558156` (2026-08-30T23:52:24-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/01-introduction-and-goals.md a 06-runtime-view.md con contenido propio; sin marcadores de plantilla visibles | Cumple | Secciones 1-6 redactadas en archivos separados; 07, 08 y 11 vacías pero no exigidas esta semana. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-architecture-decisions.md cita ADR-0001 pero omite ADR-0002 (docs/adr/0002-seleccion-tecnologia-backend-frontend.md) | No cumple | Falta enlazar ADR-0002 en el índice de decisiones. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-quality-requirements.md con escenarios Q-01 a Q-06 detallados con medida, herramienta y carga | Cumple | Los escenarios Q-01, Q-02 y Q-03 mantienen coherencia con la semana 2. |
| Glosario iniciado con términos del dominio | docs/arc42/12-glossary.md define 'Requisito de grado' y 'Estado de un requisito' | Cumple | Glosario con términos propios del dominio académico, no genéricos. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.puml, contexto.png, contenedores.puml, contenedores.png; secciones 3.3 y 5 describen actores y contenedores | Cumple | Diagramas en código (.puml) e imagen; coherencia documentada en arc42. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | backend/app/{core,usuarios,estudiantes,requisitos,programas,ayuda}/ y frontend/lib/... coinciden con 05-building-block-view.md | Cumple | Cada módulo del nivel 2 tiene directorio correspondiente en backend y frontend. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | frontend/lib/requisitos/requisitos_screen.dart → backend/app/requisitos/service.py → backend/app/core/database.py | Cumple | Recorrido GET /requisitos/{estudiante_id} documentado en 06-runtime-view.md. |
| Arranque documentado con un solo comando | README.md sección 'Inicio Rápido' con comando start.bat y requisitos previos; start.bat en el árbol | Cumple | Un solo comando de arranque declarado. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_requisitos.py y frontend/test/widget_test.dart existen; .github/workflows/ci.yml presente; sin runs_ci | No verificado | No hay URL de run de GitHub Actions que confirme ejecución en verde; comandos: pytest y flutter test. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md existe en el árbol pero su contenido no fue proporcionado | No verificado | No se pudo verificar que las celdas enlacen a destinos existentes. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_DinamikUTB visible; autores consolidados: Juan José Vargas Pérez, Luis Daniel Padilla Leottau, Gillianis Perez, Esteban Ramirez | Cumple | 4 integrantes declarados coinciden con identidades consolidadas del historial. |
| Estructura mínima | docs/arc42/ (12), docs/adr/ (2), docs/c4/ (4), docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Estructura mínima completa. |
| Versionado | Sin etiqueta de corte; hash calificado 8558156 (2026-08-30T23:52:24-05:00); commits post-cierre 4258407, d87a771, 1308052, 3c16fba | No cumple | Etiqueta ausente y commits posteriores al cierre de la semana 4. |
| Convenciones de ADR | docs/adr/0001 y 0002 con nombre y formato correctos, pero sin sección de trazabilidad con commit/PR y pruebas | No cumple | Falta el eslabón de trazabilidad que exige el contrato. |
| Tabla de aspectos | docs/aspectos.md existe; contenido no disponible en la evidencia | No verificado | No se pudo verificar columnas ni navegabilidad. |
| Registro de uso de IA | docs/ia.md con 12 commits de modificación (2026-08-09 a 2026-08-30); contenido no disponible | No verificado | El historial muestra actividad, pero no se verificó la columna de lo rechazado. |
| README y reproducibilidad | README.md con descripción, requisitos previos, comando start.bat y sección de pruebas | Cumple | Arranque con un solo comando y pruebas documentadas. |
| Secretos y autoría | Sin coincidencias de secretos; sin .env versionados; shortlog con 4 autores consolidados | Cumple | Sin incidentes de secretos; autoría repartida aunque con desbalance de commits. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `3c16fbaee7cfa19e23e446166426a64db29a6ad6 2026-08-31T00:13:28-05:00 Update start.bat`
- **Veredicto**: con pendientes
- Resumen: La entrega de la semana 4 tiene la documentación arc42, el C4 y el corte vertical implementados, pero quedan pendientes: sección 9 sin ADR-0002, ADR sin trazabilidad, y sin evidencia de CI en verde.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 4258407 Update start.bat (2026-08-31T00:07:55-05:00)
- d87a771 Merge pull request #8 (2026-08-31T00:11:21-05:00)
- 1308052 Update start.bat (2026-08-31T00:12:04-05:00)
- 3c16fba Update start.bat (2026-08-31T00:13:28-05:00)

Pendientes que siguen abiertos:
- Enlazar ADR-0002 en sección 9
- Añadir trazabilidad commit/PR y pruebas en ADR
- Evidencia de run de CI en verde
- Verificar fila de aspectos.md
- Verificar contenido de docs/ia.md

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba automatizada del recorrido completo en verde: falta URL de run de GitHub Actions.
- Fila de docs/aspectos.md: falta contenido del archivo.
- Registro de IA (docs/ia.md): falta contenido para verificar lo aceptado/rechazado.

## Hallazgos para la planilla

- La sección 9 de arc42 no enlaza el ADR-0002 existente.
- Los ADR carecen de trazabilidad con commit/PR y pruebas.
- No hay evidencia de run de CI en verde para las pruebas del corte vertical.
- docs/aspectos.md no verificable por falta de contenido en la evidencia.
- 4 commits posteriores al cierre de la semana 4 (start.bat y merge).
- Diagramas C4 disponibles como código .puml, favorable para trazabilidad.
- Commits posteriores al cierre (no calificados): 3c16fba 2026-08-31T00:13:28-05:00 Update start.bat; 1308052 2026-08-31T00:12:04-05:00 Update start.bat; d87a771 2026-08-31T00:11:21-05:00 Merge pull request #8 from ISCOUTB/workArea-Luis; 4258407 2026-08-31T00:07:55-05:00 Update start.bat
