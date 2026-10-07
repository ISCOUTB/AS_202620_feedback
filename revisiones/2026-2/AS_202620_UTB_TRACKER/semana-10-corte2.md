# Segundo corte S10 · revisión preliminar · UTB Tracker

**Preliminar; no es la calificación del corte.** Se revisa la punta actual, con cierre futuro **2026-10-12T05:00:00Z**. S9 queda congelada de forma independiente.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_UTB_TRACKER |
| Rama principal remota | `main` |
| Base S5 publicada | `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849` |
| Base S8 | `ae526db29b4f2d1f5981536e18438f9a62b1516d` |
| Estado revisado | `d17c9eb241e56755d48b022dc00ddb865e40c391` en `origin/main` (2026-10-06T01:08:05-05:00) |
| Punta actual / S10 preliminar | `d17c9eb241e56755d48b022dc00ddb865e40c391` · 2026-10-06T01:08:05-05:00 |
| Observado | 2026-10-06T21:28:33.555768Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

## Escenario operativo asignado

**No verificado.** README, ADR 0001–0003 y arc42 describen QS-01…QS-06 y el corte vertical, pero no registran la asignación oficial del reto S10. Fuente inspeccionada: [docs/aspectos.md:65–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L65-L82). No se equipara un escenario de calidad genérico ni el ejercicio S9 con la asignación oficial. Las filas que dependen de esa correspondencia permanecen abiertas hasta obtener la consigna y contrastarla.

## Matriz de preparación S10

El renglón «PDF de dos páginas» se omite expresamente por exclusión docente: quedan **12 filas**, sin fórmula semanal de calificación.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Estado preliminar de main registrado en el encabezado y anterior al cierre futuro. |
| Despliegue accesible en el momento de la revisión | No verificado | [README.md:5–11](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/README.md#L5-L11) solo declara localhost; falta URL pública verificable. [app/routers/health.py:6–12](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/routers/health.py#L6-L12) implementa /salud, sin comprobación externa. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | [docs/aspectos.md:65–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L65-L82) contiene escenarios de calidad anteriores; no asignación S10 con hipótesis/montaje/variables. |
| Línea base medida y reproducible | No cumple | [docs/aspectos.md:72–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L72-L82) solo narra la regla de préstamos; no hay medición reproducible de línea base en la punta. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0003-integracion-sincrona.md:21–60](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/adr/0003-integracion-sincrona.md#L21-L60) conserva decisión previa; la nueva autenticación/reorganización no tiene ADR del reto ni costo documentado. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [app/main.py:3–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/main.py#L3-L14) integra autenticación y nuevos módulos después de S9; no hay vínculo a la consigna S10. |
| Resultado contrastado con el umbral | No cumple | [docs/aspectos.md:72–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L72-L82) no aporta resultado numérico frente a línea base y umbral; el árbol carece de experimento S10 reproducible. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | [CI actual en failure](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/37422096531); [.github/workflows/ci.yml:19–23](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L19-L23) cubre solo app/tests/. Salud en código sin logs estructurados ni métrica del escenario identificable. |
| Secretos protegidos | Cumple | [app/core/config.py:7–11](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/config.py#L7-L11) usa entorno y el barrido actual no detecta credenciales reales. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/arc42/arc42.md:249–278](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/arc42/arc42.md#L249-L278) conserva plantilla de despliegue; [README.md:42–67](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/README.md#L42-L67) y [docs/c4/C2.md:3–6](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/c4/C2.md#L3-L6) citan estructura/base de datos anterior a la reorganización. |
| Decisión anterior confirmada o reemplazada con evidencia | No cumple | [docs/adr/0003-integracion-sincrona.md:51–60](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/adr/0003-integracion-sincrona.md#L51-L60) registra consecuencias previas sin confirmación/reemplazo a partir de mediciones del reto actual; no hay ADR nuevo. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Sustentación sobre despliegue y pipeline en vivo pendiente del docente. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Evidencia y límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | README, ADR 0001–0003 y arc42 describen QS-01…QS-06 y el corte vertical, pero no registran la asignación oficial del reto S10. |
| Decisión e implementación | No verificado | Pendiente | Existe cambio tardío de autenticación, pero falta escenario oficial y decisión del reto. |
| Operación, seguridad y observabilidad | Insuficiente | 0.00 | Pipeline de la punta en failure; no se instrumenta métrica del escenario ni logs estructurados, por lo que no se demuestra observabilidad de la respuesta. |
| Evolución arquitectónica trazable | Básico | 0.60 | Hay C4/arc42/ADR previos, pero despliegue conserva plantilla y las rutas no reflejan la reorganización. |
| Sustentación del reto | Lo fija el docente | Pendiente | Sesión pendiente. |

**No se publica total final.** La escala de cada criterio es 0,00 / 0,60 / 0,80 / 1,00; la sustentación queda a cargo del docente, con entorno desplegado y pipeline en vivo. Las celdas pendientes no equivalen a cero. S6–S9 no se recalifican por existir.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público del repositorio vigente; [README.md:1–3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/README.md#L1-L3). |
| Estructura mínima presente | Cumple | Las seis rutas mínimas siguen presentes en la punta. La vigencia de enlaces/diagramas se evalúa por separado. [docs/aspectos.md:63–72](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L63-L72). |
| Estado calificado identificable | Cumple | main d17c9eb241e56755d48b022dc00ddb865e40c391 del 2026-10-06; punta preliminar distinta del estado S9 congelado. |
| Nombres de ADR según la convención | Cumple | Tres nombres conformes: 0001-estilo-arquitectonico.md, 0002-cambio-stack-fastapi-flutter.md y 0003-integracion-sincrona.md; [docs/adr/0003-integracion-sincrona.md:7–25](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L7-L25). |
| ADR aceptados no reescritos | Cumple | Historial de los tres ADR: solo sus commits de creación (5f923cd, e88a3d6, 9cf1ac9); sin ediciones posteriores. [docs/adr/0003-integracion-sincrona.md:3–5](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L3-L5). |
| docs/ia.md al día para la semana | No cumple | [docs/ia.md:11–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/ia.md#L11-L14): no documenta tampoco la nueva autenticación y reorganización de octubre. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Run de la punta](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/37422096531) en failure. [.github/workflows/ci.yml:19–23](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L19-L23) solo invoca app/tests/, omitiendo tests/ de contratos/préstamos/recursos; no incluye scanner SonarCloud. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido de la punta sin credenciales reales; [app/core/config.py:7–11](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/config.py#L7-L11) toma las claves del entorno. No se verificó rotación ni configuración del servidor externo. |
| Contribución de todos los integrantes | No verificado | Firmas del historial agregadas, con variantes de identidad; correspondencia con toda la matrícula no verificada. No se mantienen inferencias individuales de informes anteriores. |

## Estado global del proyecto (overall)

Punta de la misma rama: `d17c9eb241e56755d48b022dc00ddb865e40c391` (2026-10-06T01:08:05-05:00). Hay **0 commits en el delta S8→S9** y **7 commits posteriores al cierre S9**. S9 está congelada sin cambios respecto de S8. Después del cierre hay siete commits, incluida reorganización del backend y autenticación JWT. El CI sigue fallando y la documentación no refleja todavía la nueva estructura.



### Hallazgos abiertos

- S9 no incorpora commits nuevos frente a S8; la autenticación de octubre es tardía y solo se valora en overall/S10.
- Recuperar el CI y ejecutar también tests/ de contratos, préstamos y recursos; actualmente solo se invoca app/tests/.
- Actualizar README, enlaces de aspectos y C4 para la nueva estructura; completar arc42 de despliegue.
- Publicar URL de despliegue, procedimiento reproducible, logs estructurados, métricas y costo.
- Registrar la asignación S10, la línea base, ADR y experimento con resultados.
- Actualizar docs/ia.md, auditar propiedad de datos y decidir sobre componente generativo.
- Corregir configuración de expiración JWT: [app/core/config.py:10](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/config.py#L10) devuelve texto y [app/core/security.py:10](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/security.py#L10) lo pasa a timedelta(minutes=...). Hallazgo estático; no se ejecutó.
- Verificar correspondencia de las identidades del historial con los integrantes.

### Hallazgos cerrados o sustituidos con evidencia actual

- El workflow actual coloca preparación de Python y pruebas antes del despliegue mediante needs: test: [.github/workflows/ci.yml:7–26](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L7-L26). Es una mejora tardía; el run aún falla y no cierra CI.
- Aparecen firmas adicionales en el historial actual; se retira la afirmación categórica antigua de que solo una persona ha contribuido. No se atribuye por nombre una firma a una persona.

## Para completar antes del cierre

Primero recuperen el pipeline y hagan que incluya también las pruebas de contratos, préstamos y recursos. Revisen la conversión de la duración del token a número, actualicen documentación y configuración de arranque y publiquen la URL del entorno. Para el reto, falta identificar la asignación, medir línea base y resultado y añadir observabilidad y costo. La defensa queda pendiente del docente.

## Tres preguntas para la sustentación

1. ¿Cómo evitarían dos préstamos simultáneos del mismo recurso y qué prueba o métrica evidencia que el control funciona?
2. ¿Qué servidor y base de datos sostienen el despliegue y cuál es su costo mensual y límite de capacidad?
3. ¿Qué decisión cambiarían después de comparar la línea base con el experimento del escenario asignado?

## Delta S5→S10 (sin recalificar entregas previas)

Se verificó por Git la base S5 publicada `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849` contra la punta `d17c9eb241e56755d48b022dc00ddb865e40c391`: 11 commits. [Comparación inmutable](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/compare/7cfb8729db79435bf9de7d3975a9a3bd7ac5b849...d17c9eb241e56755d48b022dc00ddb865e40c391). Las filas de decisión, implementación y evolución usan este delta como contexto, sin volver a calificar S5–S9.

Cambios documentales contrastados:

- docs/adr/0003-integracion-sincrona.md | 60 +++++++++++++++++++++++++++++++++++
- docs/c4/C2.md                         | 21 ++++++++----
- 2 files changed, 75 insertions(+), 6 deletions(-)
