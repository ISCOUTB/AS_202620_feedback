# semana-04-evidencia-s4 · InvenTrack

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `dd4ea1c` (2026-08-23T23:46:24-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md solo contiene secciones 1, 2, 3 y 10 completas; las secciones 4, 5 y 6 están marcadas como pendientes. | No cumple | Faltan las secciones 4 (Building Block View), 5 (Runtime View) y 6 (Deployment View). |
| arc42 sección 9 al día y enlazada con los ADR existentes | No existe sección 9 en docs/arc42/arc42-template-EN.md. | No cumple | La sección 9 (Decisiones de arquitectura) no está redactada ni enlaza a docs/adr/0001-*.md. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42-template-EN.md incluye la sección 10 con escenarios ESC-01 a ESC-05, coherentes con docs/aspectos.md y docs/utility-tree.md. | Cumple | La sección 10 está completa y alineada con el aspecto de consistencia de datos. |
| Glosario iniciado con términos del dominio | No existe sección 12 en docs/arc42/arc42-template-EN.md. | No cumple | El glosario no está iniciado. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo existe docs/c4/context.md (nivel 1); no hay archivo de nivel 2. | No cumple | Falta el diagrama de contenedores (nivel 2). |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay diagrama C4 nivel 2, por lo que no se puede contrastar con la estructura de directorios. | No cumple | Sin nivel 2 no hay correspondencia que verificar. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Solo existe endpoint /health en app/main.py; los módulos app/inventario/, app/productos/, etc. están vacíos (solo __init__.py). | No cumple | No hay lógica de negocio ni persistencia implementada. |
| Arranque documentado con un solo comando | docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md menciona: 'Comando de arranque documentado en el README: python -m uvicorn app.main:app --reload'. | Cumple | El comando está declarado, aunque no se verificó directamente en el README por falta de contenido completo. |
| Prueba automatizada del recorrido completo, en verde | Solo existe tests/test_health.py que prueba /health; no hay prueba del recorrido completo ni URL de run en verde. | No cumple | No se evidencia prueba de punta a punta ni ejecución en CI. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila ASP-01 tiene en columna Pruebas: 'Pendiente — tests/test_health.py existe pero aún no cubre este aspecto' y en Evidencia: 'Pendiente'. | No cumple | La columna Pruebas no enlaza a una prueba real que cubra el aspecto. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_InvenTrack en organización ISCOUTB, público; autores en historial: Josephva24, Esteban Peluffo, FlexT21, Jose Vargas, jxviercarta-a11y, Felix Taborda. | Cumple | Consolidando identidades: Josephva24 y Jose Vargas son la misma persona (Jose Gabriel Vargas Perez); FlexT21 y Felix Taborda son la misma persona (Felix Andres Taborda Jimenez). Total 4 integrantes reales. |
| Estructura mínima | Existen docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md. | Cumple | arc42 está en un solo archivo arc42-template-EN.md, lo cual es aceptable. |
| Estado del repositorio calificado | Commit calificado dd4ea1c con fecha 2026-08-23T23:46:24-05:00, anterior al cierre 2026-08-31T05:00:00Z. | Cumple | Sin etiqueta, pero se usó el último commit antes del cierre. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md sigue la convención de nombre y estructura. | Cumple | El ADR está en estado 'Propuesto', no 'Aceptado', pero la convención se cumple. |
| Tabla de aspectos | docs/aspectos.md fila ASP-01 tiene celdas Pruebas y Evidencia con texto 'Pendiente' que no enlazan a artefactos reales. | No cumple | Una fila con huecos no se puede defender según el contrato. |
| Registro de uso de IA | docs/ia.md existe con registros de uso, incluyendo columna 'Rechazado / motivo'. | Cumple | Cumple con la estructura requerida. |
| README | README.md existe y documenta descripción, equipo, aspecto, estructura y enlaces; el ADR referencia el comando de arranque. | Cumple | No se verificó el comando exacto en el README por falta de contenido completo, pero el ADR lo cita. |
| Pipeline y análisis estático | Existe .github/workflows/test.yml, pero no se proporciona URL de run ni evidencia de análisis estático en SonarCloud. | No verificado | Haría falta consultar la API de GitHub Actions para ver runs y verificar SonarCloud. |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Pipeline y análisis estático: falta URL de run de GitHub Actions y verificación de SonarCloud.

## Hallazgos para la planilla

- Faltan secciones 4, 5, 6, 9 y 12 de arc42.
- No hay diagrama C4 nivel 2.
- No hay corte vertical: solo endpoint /health y módulos vacíos.
- No hay prueba automatizada del recorrido completo.
- La fila de aspectos tiene Pruebas y Evidencia pendientes.
- El pipeline no tiene evidencia de ejecución en verde.
