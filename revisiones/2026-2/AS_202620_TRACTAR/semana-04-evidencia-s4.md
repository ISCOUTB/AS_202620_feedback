# semana-04-evidencia-s4 · TRACTAR

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `2b16439` (2026-08-30T15:02:33-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42.md:1-5 contiene 'About arc42', 'Template Version 9.0-EN' | No cumple | Texto de plantilla sin eliminar; secciones 4-6 no verificables por truncamiento. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se muestra sección 9 en el contenido de arc42.md | No verificado | Falta contenido completo para confirmar enlaces a ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se muestra sección 10 | No verificado | Falta contenido completo. |
| Glosario iniciado con términos del dominio | No se muestra sección 12 | No verificado | Falta contenido completo. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo existe docs/c4/c4_nivel1.md; no hay c4_nivel2.md | No cumple | Falta nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay nivel 2 | No cumple | Sin nivel 2 no se puede contrastar. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | app/main.py y routers sin persistencia; README indica 'no contienen lógica de negocio compleja' | No cumple | Falta tramo de persistencia. |
| Arranque documentado con un solo comando | README.md: sección 'Cómo arrancar' con ./run.sh | Cumple | Comando único documentado. |
| Prueba automatizada del recorrido completo, en verde | app/tests/test_main.py solo prueba /salud/; CI ejecuta pytest | No cumple | No hay prueba de recorrido completo. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md: filas A-03 y A-04 con Código y Pruebas en '—'; A-01 Pruebas 'health check' sin ruta | No cumple | Celdas no navegables. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | git shortlog muestra solo a Sebastian Garcia Devoz (13+4+1 commits) | No cumple | No aparecen los otros 3 integrantes. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura presente. |
| Estado calificado/versionado | Commit 2b16439 fecha 2026-08-30T15:02:33-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta requerida para evidencia semanal. |
| Convenciones de ADR | docs/adr/0002.md no sigue patrón NNNN-titulo.md y está vacío | No cumple | ADR 0002 sin título ni contenido. |
| Tabla de aspectos | docs/aspectos.md con filas incompletas (A-03, A-04 sin código/pruebas) | No cumple | Huecos en trazabilidad. |
| Registro de uso de IA | docs/ia.md no registra rechazos con motivo técnico | No cumple | Falta columna de rechazo explícito. |
| README | README.md documenta arranque con ./run.sh y pruebas con pytest | Cumple | Cumple requisitos. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo ejecuta pytest; no hay SonarCloud | No cumple | Falta análisis estático. |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 9
- arc42 sección 10
- Glosario sección 12
- arc42 secciones 4-6 (contenido no visible)

## Hallazgos para la planilla

- Solo un autor en historial
- ADR 0002 vacío y mal nombrado
- Falta C4 nivel 2
- No hay persistencia en corte vertical
- Prueba solo de salud, no recorrido completo
- Fila de aspectos incompleta
- Falta SonarCloud
- Texto de plantilla en arc42
