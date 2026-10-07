# Segundo corte S10 · revisión preliminar · XALD

**Preliminar; no es la calificación del corte.** Se revisa la punta actual, con cierre futuro **2026-10-12T05:00:00Z**. S9 queda congelada de forma independiente.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_XALD |
| Rama principal remota | `master` |
| Base S5 publicada | `9bf16cf989667977ff8afe95311a595a66517318` |
| Base S8 | `f90f28d3e3b0fe3da81d71b8cc9d9d10bdf07491` |
| Estado revisado | `9236ff97218b632eeb9a1910f6083968e2c22909` en `origin/master` (2026-10-04T23:53:02-05:00) |
| Punta actual / S10 preliminar | `9236ff97218b632eeb9a1910f6083968e2c22909` · 2026-10-04T23:53:02-05:00 |
| Observado | 2026-10-06T21:29:11.260956Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

## Escenario operativo asignado

**No verificado.** ESC-05 está definido como escenario de calidad y motiva el ADR 0011, pero no aparece una fuente que lo identifique como el escenario operativo oficialmente asignado para S10. Fuente inspeccionada: [docs/arc42/10-Quality Requirements.md:60–69](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/arc42/10-Quality%20Requirements.md#L60-L69). No se equipara un escenario de calidad genérico ni el ejercicio S9 con la asignación oficial. Las filas que dependen de esa correspondencia permanecen abiertas hasta obtener la consigna y contrastarla.

## Matriz de preparación S10

El renglón «PDF de dos páginas» se omite expresamente por exclusión docente: quedan **12 filas**, sin fórmula semanal de calificación.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master anterior al cierre futuro e identificada en el encabezado; revisión preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | [README.md:8–11](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/README.md#L8-L11). GET https://xald-backend.onrender.com/health: primer intento 2026-10-06T21:24:29Z agotó 25,002608 s; segundo intento iniciado 2026-10-06T21:27:21Z devolvió HTTP 200 en 6,211375 s, cuerpo status=ok. Se comprueba salud puntual, no flujo de negocio ni carga. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | [docs/arc42/10-Quality Requirements.md:60–69](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/arc42/10-Quality%20Requirements.md#L60-L69) define escenario de calidad, no confirma asignación operativa S10; falta caracterización del reto oficial. |
| Línea base medida y reproducible | No cumple | [docs/adr/0011-resolucion-conflictos-lww.md:9–23](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L9-L23) ofrece resultado afirmado 30/30 pero no estado inicial medido reproducible. El código LWW ya era de S8; falta comparación antes/después del experimento. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0011-resolucion-conflictos-lww.md:11–32](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L11-L32) tiene alternativas y riesgos, pero falta correspondencia con la consigna S10 y evaluación económica del efecto de la decisión. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [backend/app/main.py:110–132](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L110-L132) implementa comparación de timestamps, aún sin persistencia del cuerpo; no hay vínculo verificable al escenario oficial S10. |
| Resultado contrastado con el umbral | No cumple | [backend/scripts/medir_esc05.py:61–79](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/scripts/medir_esc05.py#L61-L79) no ejecuta concurrencia ni consulta versión ganadora; el contador de conflictos y 202 no prueban la respuesta requerida en [docs/arc42/10-Quality Requirements.md:69](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/arc42/10-Quality%20Requirements.md#L69). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | [CI en success](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/37265397606); salud/logs/métrica presentes en [backend/app/main.py:18–52](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L18-L52) y [backend/app/main.py:93–100](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L93-L100). Salud actual HTTP 200; vínculo de métrica con consigna S10 no verificado. |
| Secretos protegidos | Cumple | Barrido estático del árbol sin credenciales reales detectadas; [backend/app/main.py:59–65](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L59-L65) obtiene llave del entorno; [backend/scripts/medir_esc05.py:8–12](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/scripts/medir_esc05.py#L8-L12) es un marcador. La auditoría diferencia ejemplos/pruebas de secretos reales en [docs/EVIDENCIA-S9.md:71–105](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L71-L105). |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/EVIDENCIA-S9.md:34–40](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L34-L40) identifica discrepancias Room/AES/TLS frente a código; [docs/aspectos.md:3–10](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/aspectos.md#L3-L10) conserva referencias a experimental. ADR 0012 formaliza mock, pero falta reconciliación general de C4/arc42/contratos con MVP. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0011-resolucion-conflictos-lww.md:9–23](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L9-L23) concreta ADR 0001 y afirma confirmación por 30/30, pero el ensayo no reproduce el escenario y no hay línea base del reto asignado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Lo fija el docente en entorno desplegado y con pipeline en vivo. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Evidencia y límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | ESC-05 está definido como escenario de calidad y motiva el ADR 0011, pero no aparece una fuente que lo identifique como el escenario operativo oficialmente asignado para S10. |
| Decisión e implementación | No verificado | Pendiente | ADR y handler existen, pero falta asignación oficial, línea base y prueba de respuesta. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | CI verde, logs JSON y contador ESC-05; health actual HTTP 200 y no se confirmó la observabilidad del reto asignado. |
| Evolución arquitectónica trazable | Básico | 0.60 | Nuevos ADR y auditoría aclaran deudas, pero persisten contradicciones de almacenamiento/cifrado, rama experimental y mock. |
| Sustentación del reto | Lo fija el docente | Pendiente | Sustentación pendiente. |

**No se publica total final.** La escala de cada criterio es 0,00 / 0,60 / 0,80 / 1,00; la sustentación queda a cargo del docente, con entorno desplegado y pipeline en vivo. Las celdas pendientes no equivalen a cero. S6–S9 no se recalifican por existir.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público ISCOUTB/AS_202620_XALD; [README.md:1–9](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/README.md#L1-L9). |
| Estructura mínima presente | Cumple | README y seis rutas mínimas presentes; [docs/aspectos.md:5–11](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/aspectos.md#L5-L11) enlaza arquitectura y ADR. Hay binarios __pycache__ que deben retirarse sin confundirlos con ausencia documental. |
| Estado calificado identificable | Cumple | Rama master y hash/fecha exactos del encabezado, anterior al cierre; no se usaron etiquetas ni experimental para calificar. |
| Nombres de ADR según la convención | Cumple | Doce ADR con nombres NNNN-titulo-en-kebab-case.md; [docs/adr/0011-resolucion-conflictos-lww.md:1–5](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L1-L5). |
| ADR aceptados no reescritos | No cumple | Historial confirma adición de fechas a ADR 0001–0005 ya aprobados el 27-sep; por ejemplo efcc3902311cc8fec393fccf4f1cc7a95badf976 sobre [docs/adr/0001-patron-offline-first.md:1–4](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0001-patron-offline-first.md#L1-L4). Son ediciones de metadatos, no se afirma cambio de decisión; registrar adendas sin reescribir aceptados conforme al contrato. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:39–41](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/ia.md#L39-L41) crece en S9 con aceptados y rechazos motivados. La falta de un apartado de corrección se recoge en la fila específica S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Android CI del hash](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/37265397606) en success; [.github/workflows/ci.yml:29–57](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/.github/workflows/ci.yml#L29-L57) ejecuta Gradle, Redocly y pytest, pero no scanner SonarCloud. No hay configuración ni Quality Gate público de la revisión: el verde de pruebas no lo sustituye. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del árbol y búsqueda histórica de patrones de alta especificidad sin credenciales reales confirmadas; [backend/app/main.py:59–65](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L59-L65). Ejemplos y valores de pruebas revisados, sin publicar valores. |
| Contribución de todos los integrantes | No verificado | 419 commits con cuatro firmas observadas (186, 98, 72 y 63); la cantidad de firmas no verifica por sí sola correspondencia con cuatro integrantes ni distribución sustantiva. |

## Estado global del proyecto (overall)

Punta de la misma rama: `9236ff97218b632eeb9a1910f6083968e2c22909` (2026-10-04T23:53:02-05:00). Hay **17 commits en el delta S8→S9** y **0 commits posteriores al cierre S9**. S9 agrega diecisiete commits de verificación/documentación, sin cambios al handler LWW respecto de S8; se reconoce ese avance sin duplicar la implementación previa. CI actual en verde. Persisten deudas de persistencia, cifrado, cliente Android→backend y evaluación de Gemini futuro.

GET https://xald-backend.onrender.com/health: primer intento 2026-10-06T21:24:29Z agotó 25,002608 s; segundo intento iniciado 2026-10-06T21:27:21Z devolvió HTTP 200 en 6,211375 s, cuerpo status=ok. Se comprueba salud puntual, no flujo de negocio ni carga.

### Hallazgos abiertos

- Repetir ESC-05 con conflictos realmente simultáneos, verificar estado ganador completo y distinguir aceptación HTTP de persistencia sin pérdidas.
- Precisar cuál código fue generado en S9: el handler LWW no cambia desde S8; sí cambian pruebas, medidor y documentación.
- Completar en docs/ia.md qué se corrigió del periodo, o declarar honestamente que no se requirió corrección.
- Cambiar enlaces de aspectos desde experimental al estado revisable y reconciliar Room/AES/TLS con el MVP real.
- Resolver o priorizar H-1…H-5 de la auditoría; no presentar la auditoría como corrección ya implementada.
- Integrar SonarCloud con scanner, run y Quality Gate públicos; retirar __pycache__ versionado.
- Identificar la consigna operativa S10 y medir línea base en el despliegue; documentar estabilidad y recuperación tras el primer timeout.
- Antes de incorporar Gemini, aportar conjunto de evaluación con resultados, costo y latencia; el ADR actual solo aplaza la integración.

### Hallazgos cerrados o sustituidos con evidencia actual

- Hay nueva prueba dirigida al defecto y procedimiento de mutación: [backend/tests/test_lww.py:5–8](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/tests/test_lww.py#L5-L8) y [docs/adr/0011-resolucion-conflictos-lww.md:24](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L24).
- La auditoría y la verificación de dependencias S9 ya están presentes: [docs/EVIDENCIA-S9.md:1–67](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L1-L67).
- La decisión sobre Gemini ya está explicitada para este corte y coincide con el mock: [docs/adr/0012-aplazamiento-integracion-gemini.md:17–31](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0012-aplazamiento-integracion-gemini.md#L17-L31).
- El pipeline sí corre sobre master y el hash actual pasa: [run](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/37265397606); no cierra SonarCloud.
- La planilla antigua decía sin URL, pero el README declara el servicio y health públicos: [README.md:8–11](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/README.md#L8-L11). Salud actual confirmada por HTTP 200 en la segunda consulta; no se probó flujo.

## Para completar antes del cierre

Confirmen la consigna operativa asignada y registren una línea base antes de cambiar el MVP. El experimento debe reproducir la carga real y verificar estado final, pérdida y recuperación, además de respuestas HTTP. Mantengan visible que los datos siguen en memoria y que Gemini es un mock. Falta la evidencia pública de SonarCloud y demostrar el flujo del despliegue, además del health check.

## Tres preguntas para la sustentación

1. ¿Qué pasa con los conflictos aceptados si Render reinicia y se borra ultima_version; qué estado y datos se recuperan?
2. ¿Cuál es el costo y umbral de capacidad al agregar persistencia y eventualmente Gemini, frente al supuesto de 50 usuarios?
3. Si la prueba simultánea o con relojes desfasados cambia el resultado 30/30, ¿qué política de conflicto o diseño modificarían?

## Delta S5→S10 (sin recalificar entregas previas)

Se verificó por Git la base S5 publicada `9bf16cf989667977ff8afe95311a595a66517318` contra la punta `9236ff97218b632eeb9a1910f6083968e2c22909`: 137 commits. [Comparación inmutable](https://github.com/ISCOUTB/AS_202620_XALD/compare/9bf16cf989667977ff8afe95311a595a66517318...9236ff97218b632eeb9a1910f6083968e2c22909). Las filas de decisión, implementación y evolución usan este delta como contexto, sin volver a calificar S5–S9.

Cambios documentales contrastados:

- docs/adr/0001-patron-offline-first.md            |   1 +
- docs/adr/0002-parsing-hibrido.md                 |   1 +
- docs/adr/0003-restriccion-os.md                  |   1 +
- docs/adr/0004-seguridad-y-cifrado.md             |   1 +
- docs/adr/0005-reduccion-de-funcionalidades.md    |   3 +-
- docs/adr/0007-contratos-por-modulo.md            |  74 +++++++++
- docs/adr/0008-plataforma-de-despliegue.md        |  45 ++++++
- docs/adr/0009-distribucion-app.md                |  29 ++++
- docs/adr/0010-observabilidad.md                  |  36 +++++
- docs/adr/0011-resolucion-conflictos-lww.md       |  36 +++++
- docs/adr/0012-aplazamiento-integracion-gemini.md |  35 +++++
- docs/arc42/01-introduction goals.md              |  60 +++++++
- docs/arc42/02-Architecture constraints.md        |  27 ++++
- docs/arc42/03-Context and Scope.md               |  55 +++++++
- docs/arc42/04-Solution Strategy.md               |  11 ++
- docs/arc42/05-Building Block View.md             |  49 ++++++
- docs/arc42/06-Runtime view.md                    | 192 +++++++++++++++++++++++
- docs/arc42/07-Deployment View.md                 |  53 +++++++
- docs/arc42/08-Cross-cutting Concepts.md          |  51 ++++++
- docs/arc42/09-Architecture Decisions.md          |  16 ++
- docs/arc42/10-Quality Requirements.md            | 106 +++++++++++++
- docs/arc42/11-Risks and Technical Debts.md       |  15 ++
- docs/arc42/12-Glossary.md                        |  28 ++++
- docs/arc42/arc42-template-EN.md                  |  89 ++++++++---
- docs/c4/c2.md                                    |  34 ++--
- docs/c4/c3.md                                    | 149 ++++++++++++++++++
- 26 files changed, 1153 insertions(+), 44 deletions(-)
