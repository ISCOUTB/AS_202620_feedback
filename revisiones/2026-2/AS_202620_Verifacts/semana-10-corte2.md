# Segundo corte S10 · revisión preliminar · Verifacts

**Preliminar; no es la calificación del corte.** Se revisa la punta actual, con cierre futuro **2026-10-12T05:00:00Z**. S9 queda congelada de forma independiente.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_Verifacts |
| Rama principal remota | `master` |
| Base S5 publicada | `67f8cea03e6a7b827aced6b60d3af8cf4307b237` |
| Base S8 | `d2d7b5c3d5b64a7008c20d1aa0961d3e0c69053f` |
| Estado revisado | `4f0652291c47f5093da1230b245a980614220e80` en `origin/master` (2026-10-02T00:01:45-05:00) |
| Punta actual / S10 preliminar | `4f0652291c47f5093da1230b245a980614220e80` · 2026-10-02T00:01:45-05:00 |
| Observado | 2026-10-06T21:29:11.297297Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

## Escenario operativo asignado

**No verificado.** ADR-0005 llama «reto de corte» a comparar Render y Lambda para la API, pero no identifica semana/asignación oficial del escenario operativo S10. Es un candidato documental que requiere confirmación; Q-01/Q-05 por sí solos son escenarios de calidad. Fuente inspeccionada: [docs/adr/0005-comparacion-lambda-render.md:7–26](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0005-comparacion-lambda-render.md#L7-L26). No se equipara un escenario de calidad genérico ni el ejercicio S9 con la asignación oficial. Las filas que dependen de esa correspondencia permanecen abiertas hasta obtener la consigna y contrastarla.

## Matriz de preparación S10

El renglón «PDF de dos páginas» se omite expresamente por exclusión docente: quedan **12 filas**, sin fórmula semanal de calificación.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master anterior al cierre futuro e identificada en el encabezado; preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | [docs/despliegue.md:1–2](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/despliegue.md#L1-L2). GET https://verifacts-api.onrender.com/health: primer intento iniciado 2026-10-06T21:26:41Z agotó 25,002888 s; segundo intento iniciado 2026-10-06T21:27:21Z devolvió HTTP 200 en 7,138084 s, cuerpo status=ok. Salud puntual confirmada; no se probó el flujo de análisis. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | [docs/adr/0005-comparacion-lambda-render.md:7–26](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0005-comparacion-lambda-render.md#L7-L26) describe comparación de plataformas; falta verificar que corresponde a la asignación oficial S10 y completar hipótesis/variables del reto. |
| Línea base medida y reproducible | No cumple | [docs/adr/0005-comparacion-lambda-render.md:65–91](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0005-comparacion-lambda-render.md#L65-L91) contrasta duración local SAM de GET /health con una afirmación genérica sobre Render; no es línea base equivalente de POST /analysis con carga reproducible en ambos entornos. La medición S9 local [docs/evidencia/medicion-q01-q05.md:3–12](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/evidencia/medicion-q01-q05.md#L3-L12) no sustituye esa comparación. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0005-comparacion-lambda-render.md:93–125](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0005-comparacion-lambda-render.md#L93-L125) registra costos, alternativas y decisión de mantener Render; falta confirmar su vínculo con el escenario operativo S10. |
| Respuesta implementada o configurada sobre el MVP | No verificado | Prototipo Lambda y configuración Render existen en el delta desde S5. [docs/adr/0005-comparacion-lambda-render.md:28–47](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0005-comparacion-lambda-render.md#L28-L47) declara que Lambda no fue desplegado y [docs/adr/0005-comparacion-lambda-render.md:112–125](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0005-comparacion-lambda-render.md#L112-L125) mantiene Render. Falta demostrar que esa respuesta resuelve el reto oficial. |
| Resultado contrastado con el umbral | No cumple | [docs/adr/0005-comparacion-lambda-render.md:65–91](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0005-comparacion-lambda-render.md#L65-L91) mide health local, mientras Q-01 en [docs/escenarios-de-calidad.md:18–34](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/escenarios-de-calidad.md#L18-L34) mide análisis de texto. Se necesita misma operación/carga, comparación antes/después y límites de validez. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/36967117516) y [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/36967117556) pasan; [app/observability.py:19–34](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/app/observability.py#L19-L34) y [app/observability.py:94–125](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/app/observability.py#L94-L125) muestran logs e histograma. Salud actual HTTP 200; vínculo de la métrica al reto asignado pendiente y gate no confirmado. |
| Secretos protegidos | Cumple | Barrido estático del árbol sin credenciales reales detectadas; referencias al secreto de CI en [.github/workflows/sonarcloud.yml:34–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/.github/workflows/sonarcloud.yml#L34-L38) no son valores. Sin .env real versionado. El historial se informa con alcance de patrones en transversal. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/aspectos.md:25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/aspectos.md#L25) y [README.md:185–190](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/README.md#L185-L190) conservan rutas inexistentes. [docs/adr/0002-contextos-sin-cambios.md:9–12](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0002-contextos-sin-cambios.md#L9-L12) declara MLAnalyzer inexistente; las correcciones que afirma auditoria-s9.md no se reflejan en archivos. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0005-comparacion-lambda-render.md:112–125](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0005-comparacion-lambda-render.md#L112-L125) reafirma Render con una comparación local; no confirma con evidencia equivalente la decisión respecto del escenario operativo asignado. No hay tabla de enmiendas anunciada en la auditoría. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Sustentación, defensa de resultados y pipeline en vivo pendientes del docente. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Evidencia y límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | ADR-0005 llama «reto de corte» a comparar Render y Lambda para la API, pero no identifica semana/asignación oficial del escenario operativo S10. Es un candidato documental que requiere confirmación; Q-01/Q-05 por sí solos son escenarios de calidad. |
| Decisión e implementación | No verificado | Pendiente | ADR-0005 compara alternativas/costo y decide mantener Render, pero asignación oficial y comparación equivalente no verificadas. |
| Operación, seguridad y observabilidad | Básico | 0.60 | CI y scanner ejecutados, logs con correlación e histograma implementados; salud actual HTTP 200, pero Quality Gate no confirmado, sin verificación operativa completa del reto. |
| Evolución arquitectónica trazable | Básico | 0.60 | Nuevas pruebas/medición/ADR, pero enlaces rotos y supuestas correcciones ausentes impiden trazabilidad coherente del MVP. |
| Sustentación del reto | Lo fija el docente | Pendiente | Sustentación pendiente. |

**No se publica total final.** La escala de cada criterio es 0,00 / 0,60 / 0,80 / 1,00; la sustentación queda a cargo del docente, con entorno desplegado y pipeline en vivo. Las celdas pendientes no equivalen a cero. S6–S9 no se recalifican por existir.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público de ISCOUTB/AS_202620_Verifacts; [README.md:1–4](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/README.md#L1-L4). |
| Estructura mínima presente | Cumple | Las seis rutas mínimas están presentes. [docs/aspectos.md:17–25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/aspectos.md#L17-L25) y [docs/arc42/09-decisiones-arquitectonicas.md:8–17](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/arc42/09-decisiones-arquitectonicas.md#L8-L17); enlaces rotos y nombre con espacio se registran aparte. |
| Estado calificado identificable | Cumple | master y hash/fecha exactos del encabezado; último commit ≤ cierre, sin uso de etiquetas. |
| Nombres de ADR según la convención | No cumple | [docs/adr/ADR-0006.md:1–5](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/ADR-0006.md#L1-L5): archivo ADR-0006.md no sigue NNNN-titulo-en-kebab-case.md. [auditoria-s9.md:25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/auditoria-s9.md#L25) afirma renombre que el árbol no contiene. |
| ADR aceptados no reescritos | No cumple | Historial 9430845 añade secciones a ADR 0001–0004 ya aceptados; por ejemplo [docs/adr/0002-contextos-sin-cambios.md:29–34](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0002-contextos-sin-cambios.md#L29-L34). [auditoria-s9.md:26](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/auditoria-s9.md#L26) dice que una tabla de enmiendas lo declara, pero [docs/arc42/09-decisiones-arquitectonicas.md:1–17](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/arc42/09-decisiones-arquitectonicas.md#L1-L17) y el resto del archivo no la contienen. |
| docs/ia.md al día para la semana | No cumple | [docs/ia.md:19–22](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/ia.md#L19-L22): sin cambio desde 50568f1 (23-sep), no documenta S9 y conserva MLAnalyzer como aceptado pese a que el servicio solo instancia RuleAnalyzer. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/36967117516) y [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/36967117556) del hash actual en success; scanner y cobertura presentes en [.github/workflows/sonarcloud.yml:26–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/.github/workflows/sonarcloud.yml#L26-L38) y [sonar-project.properties:1–6](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/sonar-project.properties#L1-L6). Sigue faltando Quality Gate satisfactorio asociado a la revisión: [docs/despliegue.md:37](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/despliegue.md#L37) declara gate general rojo y [auditoria-s9.md:28](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/auditoria-s9.md#L28) confirmación pendiente. La consulta pública al endpoint de gate no fue accesible; no se infiere el estado actual desde el run verde. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido de árbol e historial con patrones de alta especificidad sin credenciales reales confirmadas; ejemplos sin valores productivos. [.github/workflows/sonarcloud.yml:34–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/.github/workflows/sonarcloud.yml#L34-L38). Alcance estático, no prueba sobre servicios externos. |
| Contribución de todos los integrantes | No verificado | 300 commits en tres firmas de autor, incluidas variantes; README/Equipo declaran dos integrantes y EQUIPOS del curso tres. La correspondencia y matrícula deben confirmarse; no se identifica a una persona como ausente por parecido de cuenta. |

## Estado global del proyecto (overall)

Punta de la misma rama: `4f0652291c47f5093da1230b245a980614220e80` (2026-10-02T00:01:45-05:00). Hay **27 commits en el delta S8→S9** y **0 commits posteriores al cierre S9**. Hay veintisiete commits S9 y ningún tardío: constantes/contrato de Scoring, pruebas, mutaciones, medición local y cobertura en SonarCloud. Se verifican los cambios reales y se mantienen abiertas las correcciones declaradas pero ausentes del árbol. Las pruebas/scanner del hash pasan; el Quality Gate no queda confirmado.

GET https://verifacts-api.onrender.com/health: primer intento iniciado 2026-10-06T21:26:41Z agotó 25,002888 s; segundo intento iniciado 2026-10-06T21:27:21Z devolvió HTTP 200 en 7,138084 s, cuerpo status=ok. Salud puntual confirmada; no se probó el flujo de análisis.

### Hallazgos abiertos

- Corregir enlaces y nombre de ADR-0006: la fila A-06 y README apuntan a archivos que no existen.
- Registrar IA de S9 y corregir la afirmación de MLAnalyzer; no basta escribir Corregido en la auditoría.
- Crear realmente el ADR de no incorporar componente generativo si esa es la decisión; ADR-0007 citado no existe.
- Contrastar fila a fila D-1/D-5/D-6/D-7 de auditoria-s9.md: las correcciones anunciadas no están versionadas.
- Confirmar Quality Gate público y revisión asociada; scanner verde con cobertura no garantiza gate aprobado.
- Añadir pytest-cov al inventario de dependencias y fijar su versión o cierre reproducible.
- Confirmar si la comparación Render/Lambda corresponde al escenario operativo asignado S10 y medir operación/carga equivalentes en ambos.
- Aclarar matrícula y correspondencia de autoría; README/Equipo y listado docente discrepan.
- Verificar disponibilidad pública con evidencia fechada y recuperación/persistencia del historial tras reinicios.

### Hallazgos cerrados o sustituidos con evidencia actual

- Scoring ya importa el servicio público de Analysis y la base de pruebas queda aislada: [app/modules/scoring/service.py:1](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/app/modules/scoring/service.py#L1) y [tests/conftest.py:1–13](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/tests/conftest.py#L1-L13).
- Medición formal local de Q-01 y Q-05 publicada: [docs/evidencia/medicion-q01-q05.md:3–12](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/evidencia/medicion-q01-q05.md#L3-L12). Cierra la ausencia de medición para texto local, no la de URL o producción.
- El workflow SonarCloud ahora genera y entrega coverage.xml: [.github/workflows/sonarcloud.yml:21–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/.github/workflows/sonarcloud.yml#L21-L38) y [sonar-project.properties:5–6](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/sonar-project.properties#L5-L6). No se declara cerrado el Quality Gate.
- Los runs del hash actual de Tests y SonarCloud pasan: [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/36967117516), [scanner](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/36967117556).

## Para completar antes del cierre

Confirmen si Render frente a Lambda es la consigna operativa asignada. La comparación debe medir la misma operación y carga: GET /health local en SAM no es equivalente al análisis de texto que exige Q-01. Añadan línea base comparable, resultado y límites, reparen enlaces y confirmen el Quality Gate y la disponibilidad del entorno. El pipeline verde y la cobertura no sustituyen la sustentación.

## Tres preguntas para la sustentación

1. ¿Qué pasa con los análisis guardados cuando Render reinicia su disco efímero, y cómo demostrarían recuperación sin pérdida?
2. ¿Cómo cambia el costo real de Lambda si se mide POST /analysis con la carga de Q-01 en vez de GET /health local?
3. Si el experimento equivalente contradice el P95 local documentado, ¿mantendrían Render o qué cambio de arquitectura justificarían?

## Delta S5→S10 (sin recalificar entregas previas)

Se verificó por Git la base S5 publicada `67f8cea03e6a7b827aced6b60d3af8cf4307b237` contra la punta `4f0652291c47f5093da1230b245a980614220e80`: 66 commits. [Comparación inmutable](https://github.com/ISCOUTB/AS_202620_Verifacts/compare/67f8cea03e6a7b827aced6b60d3af8cf4307b237...4f0652291c47f5093da1230b245a980614220e80). Las filas de decisión, implementación y evolución usan este delta como contexto, sin volver a calificar S5–S9.

Cambios documentales contrastados:

- docs/adr/0001-estilo-arquitectonico.md      |   7 ++
- docs/adr/0002-contextos-sin-cambios.md      |  34 ++++++
- docs/adr/0003-integracion-sincrona.md       | 128 +++++++++++++++++++++
- docs/adr/0004-plataforma-despliegue.md      |  91 +++++++++++++++
- docs/adr/0005-comparacion-lambda-render.md  | 165 ++++++++++++++++++++++++++++
- docs/adr/ADR-0006.md                        | 114 +++++++++++++++++++
- docs/arc42/02-restricciones.md              |  30 ++++-
- docs/arc42/06-vista-de-ejecucion.md         | 131 ++++++++++++++++------
- docs/arc42/07-despliegue.md                 | 110 ++++++++++++++-----
- docs/arc42/09-decisiones-arquitectonicas.md |  19 ++++
- docs/arc42/10-requisitos-de-calidad.md      |   3 +-
- docs/c4/02-contenedores.md                  |  32 ++++--
- docs/c4/03-componentes.md                   |  67 +++--------
- 13 files changed, 797 insertions(+), 134 deletions(-)
