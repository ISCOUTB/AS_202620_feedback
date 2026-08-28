# semana-04-evidencia-s4 · AudioShare

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `9e04900` (2026-08-28T14:10:38-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/src/05_building_block_view vacío y falta 06_runtime_view.adoc | No cumple | Secciones 1-4 redactadas; 5 vacía y 6 ausente. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No existe docs/arc42/src/09_architecture_decisions.adoc | No cumple | Falta sección 9. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No existe docs/arc42/src/10_quality_requirements.adoc | No cumple | Falta sección 10. |
| Glosario iniciado con términos del dominio | No existe docs/arc42/src/12_glossary.adoc | No cumple | Falta glosario. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo docs/c4/context.mmd y context.png (nivel 1) | No cumple | No hay nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin C4 nivel 2 | No cumple | No se puede contrastar. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README indica 'aún sin lógica de negocio'; src solo esqueleto | No cumple | No hay lógica ni persistencia. |
| Arranque documentado con un solo comando | README.md declara 'npm run dev' | No verificado | No ejecutado; comando anotado. |
| Prueba automatizada del recorrido completo, en verde | Solo tests/health.test.ts; sin .github/workflows | No cumple | No hay prueba de recorrido completo ni CI. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md solo narrativa, sin columnas C4/ADR/Código/Pruebas | No cumple | Fila incompleta. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_AudioShare público en ISCOUTB; autores incluyen 4 identidades | Cumple | Vincent corresponde a cardonavincent26-design. |
| Estructura mínima | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md presentes | Cumple | Estructura conforme. |
| Estado del repositorio calificado | Hash 9e04900 fecha 2026-08-28 anterior al cierre 2026-08-31 | Cumple | Commit vigente. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md con título 'Selección del estilo arquitectónico' y trazabilidad pendiente | No cumple | Título no enuncia decisión; implementación y pruebas pendientes. |
| Tabla de aspectos | docs/aspectos.md sin tabla de 8 columnas | No cumple | No cumple formato. |
| Registro de uso de IA | docs/ia.md sin sección de rechazos con motivo técnico | No cumple | Falta qué se rechazó y por qué. |
| README | README.md con qué es, arranque, pruebas y requisitos | Cumple | Cumple. |
| Pipeline y análisis estático | Sin .github/workflows ni SonarCloud | No cumple | No hay CI. |

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Arranque no ejecutado (comando declarado: npm run dev).

## Hallazgos para la planilla

- Faltan secciones arc42 5, 6, 9, 10 y 12.
- No existe C4 nivel 2.
- No hay corte vertical con lógica y persistencia.
- No hay prueba de recorrido completo ni pipeline CI.
- ADR con título no decisional y trazabilidad incompleta.
- Tabla de aspectos sin columnas requeridas.
- Registro de IA sin rechazos explícitos.
