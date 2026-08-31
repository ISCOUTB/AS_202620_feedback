# semana-04-evidencia-s4 · Clubs UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `91323d6` (2026-08-30T23:21:56-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/01_introduccion_y_metas.md, 02_restricciones.md, 03_contexto_y_alcance.md, 04_estrategia_de_solucion.md, 05_vista_de_bloques.md, 06_vista_de_ejecucion.md con contenido sustantivo | Cumple | No se observan rastros de plantilla sin sustituir. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09_decisiones_de_diseno.md cita docs/adr/0001-hexagonal.md | Cumple | La tabla enlaza la decisión con el ADR y el escenario motivador. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10_requisitos_de_calidad.md incluye escenarios U1-U3 y C1-C3 coherentes con aspectos.md | Cumple | Los escenarios mantienen correspondencia con la tabla de aspectos. |
| Glosario iniciado con términos del dominio | docs/arc42/12_glosario.md contiene solo términos de arquitectura (Adaptador, ADR, C4, etc.) | No cumple | No se definen términos del dominio como club, evento, aviso o noticia. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.md existe pero el contenido proporcionado está truncado antes del nivel 2 | No verificado | No se pudo comprobar la presencia y coherencia del nivel 2 por falta de contenido completo. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | El árbol del repositorio solo contiene backend/; no hay código de app Flutter ni integración con Supabase | No cumple | El diagrama C4 probablemente incluye contenedores sin código correspondiente (frontend, base de datos). |
| Corte vertical que atraviesa interfaz, lógica y persistencia | backend/src/linkclub/adapters/inbound/api/health_router.py (interfaz), application/use_cases/check_health.py (lógica), adapters/outbound/persistence/in_memory_status_adapter.py (persistencia) | Cumple | Las tres rutas del recorrido están citadas y existen. |
| Arranque documentado con un solo comando | README.md sección 7 lista múltiples comandos: cd backend, python -m venv, activate, pip install, uvicorn | No cumple | No se declara un único comando de arranque. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_health.py existe y .github/workflows/backend-tests.yml está presente, pero no se aporta URL de run con conclusión verde | No verificado | Falta evidencia de ejecución exitosa en CI. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila U2 tiene ID, Aspecto, Requisito, C4, ADR, Código y Pruebas con rutas válidas | Cumple | Cada celda apunta a un destino existente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_Clubs_UTB en organización ISCOUTB, visible; autores consolidados incluyen a los 4 integrantes declarados | Cumple | Josh Ortega y Josh4OP son la misma persona por correo institucional. |
| Estructura mínima | Existen docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | La estructura cumple con lo exigido. |
| Qué estado del repositorio se califica | Commit calificado 91323d6 con fecha 2026-08-30T23:21:56-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Evidencia semanal sin etiqueta requerida; commit vigente correcto. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md sigue el patrón de nombre y contiene contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Sin ADR reescritos. |
| La tabla de aspectos | docs/aspectos.md tiene 8 columnas y 6 filas (U1-U3, C1-C3) | Cumple | Cada fila tiene las columnas requeridas. |
| Registro de uso de IA | docs/ia.md existe y el historial muestra múltiples commits (551a0af, 1bc917c, etc.) | Cumple | El registro crece a lo largo del semestre. |
| README | README.md describe el sistema y pruebas, pero el arranque requiere varios comandos, no uno solo | No cumple | No cumple el requisito de un solo comando de arranque. |
| Pipeline y análisis estático | Solo existe .github/workflows/backend-tests.yml; no hay configuración de SonarCloud ni evidencia de runs | No cumple | Falta análisis estático y ejecución verificable. |

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- C4 nivel 2 y coherencia entre niveles (contenido truncado).
- Prueba automatizada en verde (sin URL de run de CI).

## Hallazgos para la planilla

- Glosario sin términos del dominio del sistema.
- Arranque documentado con múltiples comandos, no uno solo.
- Sin evidencia de CI en verde para la prueba del corte vertical.
- Contenido de C4 nivel 2 no verificable por evidencia truncada.
- Falta código de frontend y Supabase para correspondencia con C4 nivel 2.
