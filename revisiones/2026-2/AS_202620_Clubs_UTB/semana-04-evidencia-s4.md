# semana-04-evidencia-s4 · Clubs UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `91323d6` (2026-08-30T23:21:56-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/01_introduccion_y_metas.md, 02_restricciones.md, 03_contexto_y_alcance.md, 04_estrategia_de_solucion.md, 05_vista_de_bloques.md, 06_vista_de_ejecucion.md en commit 91323d6 | Cumple | Secciones redactadas con contenido propio de LinkClub; sin rastros de plantilla ni marcadores TODO. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09_decisiones_de_diseno.md cita docs/adr/0001-hexagonal.md | Cumple | Tabla de decisiones enlaza el ADR 0001 con el escenario U2 y la sección 5; no repite el contenido del ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10_requisitos_de_calidad.md con árbol de utilidades y escenarios U1-U3, C1-C3 | Cumple | Los escenarios mantienen las seis partes (fuente, estímulo, artefacto, entorno, respuesta, medida) y son coherentes con la sección 1. |
| Glosario iniciado con términos del dominio | docs/arc42/12_glosario.md | Cumple | Incluye términos propios del sistema (LinkClub, FastAPI, Flutter, Supabase, Corte vertical) además de los de arquitectura. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.md con diagramas Mermaid de contexto y contenedores | Cumple | Los actores del nivel 1 (estudiante, miembro, administrador) reaparecen en el nivel 2 conectados a la app; el sistema se descompone en app Flutter y API FastAPI. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | API Backend corresponde a backend/src/linkclub/; Supabase como externo | Cumple | El contenedor 'Aplicación móvil' (Flutter) no tiene código aún en el repositorio; se anota como pendiente esperado. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | backend/src/linkclub/adapters/inbound/api/health_router.py → application/use_cases/check_health.py → adapters/outbound/persistence/in_memory_status_adapter.py | Cumple | El recorrido GET /health atraviesa las tres capas; la persistencia es un adaptador en memoria (stub), no una BD real. |
| Arranque documentado con un solo comando | README.md sección '7 Cómo arrancar' | No cumple | El README documenta una secuencia de comandos (crear venv, activarlo, pip install, uvicorn), no un único comando de arranque. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_health.py; run 'Backend tests' success 2026-08-31T04:22:04Z https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/33356832664 | Cumple | El pipeline ejecutó la prueba en verde antes del cierre; el run más reciente es anterior a 2026-08-31T05:00:00Z. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila U2 | Cumple | La fila U2 tiene ID, aspecto, escenario, requisito, C4, ADR, código y pruebas; todas las rutas existen y son navegables. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | AS_202620_Clubs_UTB en ISCOUTB, visible; historial con Zavod Dev, Josh Ortega/Josh4OP, Luis-Salas-Reyes, deortahollman-star | Cumple | Los 4 integrantes declarados aparecen en el historial tras consolidar identidades duplicadas. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md presentes en HEAD | Cumple | La estructura coincide con la mínima del contrato; sin desviaciones de ruta. |
| Estado que se califica (versionado) | Commit 91323d6 (2026-08-30T23:21:56-05:00) anterior al cierre 2026-08-31T05:00:00Z | Cumple | No hay etiquetas de corte, pero para evidencia semanal el commit vigente al cierre es suficiente. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md | Cumple | Nombre válido según convención; incluye contexto, alternativas, decisión, consecuencias y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas | Cumple | La fila U2 está completa y navegable; las demás declaran pendientes explícitos. |
| Registro de uso de IA | docs/ia.md con 7 registros | Cumple | Cada uso indica para qué, herramienta, cómo se usó y motivo; incluye lo rechazado y por qué. |
| README y reproducibilidad | README.md sección '7 Cómo arrancar' | No cumple | El arranque requiere varios comandos manuales; el contrato exige un solo comando. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml; runs CI success | No cumple | Las pruebas corren en CI y están en verde, pero no hay configuración ni evidencia de SonarCloud. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `91323d6b4e4cfccbc66add5802b29f100dc34be6 2026-08-30T23:21:56-05:00 Correción de parrafo en sección 6.1 y corrección del readme`
- **Veredicto**: con pendientes
- Resumen: Proyecto en HEAD 91323d6 con documentación arc42, C4 y corte vertical implementados; quedan pendientes de la semana 4: arranque con un solo comando y SonarCloud.

Pendientes que siguen abiertos:
- Arranque con un solo comando en README
- Análisis estático en SonarCloud
- Código del contenedor Flutter pendiente (esperado para fases siguientes)

## Recuento y nota sugerida

9 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.6 = 1 + 4 × (9/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución local del arranque y de las pruebas no realizada; la verificación se hizo por lectura y por los runs_ci.

## Hallazgos para la planilla

- README no ofrece un único comando de arranque; documenta varios pasos manuales.
- Falta análisis estático en SonarCloud (organización isco-utb).
- Contenedor 'Aplicación móvil' (Flutter) del C4 nivel 2 no tiene código en el repositorio.
- La persistencia del corte vertical es un adaptador en memoria, no una BD real.
- docs/ia.md registra usos de IA con lo aceptado y lo rechazado.
- La fila U2 de aspectos.md es la única completa hasta Pruebas; las demás tienen pendientes declarados.
- Matriz transversal: 6 de 8 criterios cumplidos.
