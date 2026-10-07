# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Drift |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Jerry Daniel Buelvas Mejia (`JerryDBM`) · Mauricio Andres Fernandez Espinosa (`maufern4ndez`) · Luis Mario Perez Diaz (`lmpdiaz12`) · Joshua David Reyes Leones (`JoshuaR01` y `JoshXX`, mismo correo); ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://drift-utb-202620-g5fvchdcgpcthkeg.mexicocentral-01.azurewebsites.net · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `3dee7e265eec021cbbba4af4d337e13c982df316` · 2026-10-04T22:03:23-05:00 | 7/10 | 3.8 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `3dee7e265eec021cbbba4af4d337e13c982df316` · 2026-10-04T22:03:23-05:00 | 2/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 8 | S8 | `74709aa` (2026-09-27T23:58:28-05:00) | 10/10 | 5.0 (prop. prov.; 2 filas de despliegue diferidas) | sí |
| 7 | S7 | `9334a03` (2026-09-20T20:19:47-05:00) | 10/10 | 5.0 | si |
| 6 | S6 | `5f7fa4c` (2026-09-13T22:07:49-05:00) | 5/8 | 3.5 (prelim.) | si |
| 5 | CORTE1 | `74337a3` (2026-09-08T02:53:31Z) | 7/12 | 3.3 | si |
| 4 | S4 | `4254f4a` (2026-08-30T19:13:01-05:00) | 7/10 | 3.8 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `b7ec296c` · 2026-08-09T22:59:42-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `23fb8c29` · 2026-08-16T22:39:37-05:00 | 6/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `0d006bba` · 2026-08-23T18:05:58-05:00 | 5/9 | no se publica | sí |

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Cerrar la cadena de la corrección GameCatalogRepository hacia aspecto, ADR, prueba que falle ante erosión y evidencia del escenario. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Distinguir mediciones de septiembre de un experimento nuevo del reto asignado, con factores de confusión y límites. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Reintegrar scanner SonarCloud de forma verificable y aportar Quality Gate de la revisión. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Alinear C4/arc42/ADR con la persistencia y forma de ejecución reales; usar ADR sustituto donde cambie una decisión aceptada. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Confirmar consigna oficial S10 y demostrar el flujo principal en el despliegue antes de la sustentación. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Erosión aplicación→infraestructura corregida mediante puerto explícito en S9; [backend/app/application/usecases/sync_playstation_catalog.py:3–20](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/backend/app/application/usecases/sync_playstation_catalog.py#L3-L20). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Decisión explícita de no incorporar IA generativa, [docs/adr/0007-evaluacion-de-incorporación-coponente-generativo.md:17–27](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0007-evaluacion-de-incorporaci%C3%B3n-coponente-generativo.md#L17-L27). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/aspectos.md` en prosa, sin la tabla de 8 columnas ni enlaces a escenarios ni al ADR | S1 | sí | Ver feedback S1/S2 y S3 |
| Ficha del problema sin tensiones de calidad | S1 | sí | Ver feedback S1/S2 |
| Desbalance de contribución en el periodo | S2 | sí (51 vs 9 commits en S3) | Ver feedback S1/S2 y S3 |
| README con arranque contradictorio (mvn sin pom.xml / uvicorn solo backend) y sin comando único | S3 | sí | Ver feedback S3 |
| Sin pipeline: prueba existe sin evidencia de verde | S3 | sí | Ver feedback S3 |
| Matriz de estilos sin referencia a los escenarios E1–E5 | S3 | sí | Ver feedback S3 |
| Prueba automatizada del recorrido completo | S4 | si | |
| Tabla de trazabilidad en docs/aspectos.md | S4 | si | |
| ADR con trazabilidad y marcado de reemplazo | S4 | si | |
| README con requisitos previos y comando de arranque | S4 | si | |
| Evidencia de run de CI en verde | S4 | si | |
| Verificar/crear etiqueta corte-1 | S5 | sí (el propio equipo la reconoce pendiente en `docs/correciones.md`) | Se calificó el último commit ≤ cierre (`d110d6d0`); se les pidió crear la etiqueta antes del próximo corte, ya tienen el procedimiento escrito. |
| Registrar ADR del reto con alternativas y decisión | S5 | sí (autoadmitido pendiente) | El propio equipo lo marca "Pendiente, corresponde al reto que será asignado" en `docs/correciones.md`. |
| Medir línea base con procedimiento | S5 | sí (autoadmitido parcial) | Método de verificación definido en `docs/escenarios.md`; falta ejecutar la medición y registrar el resultado. |
| Completar aspectos.md con 8 columnas | S5 | cerrado | `docs/aspectos.md` ya tiene las 8 columnas del contrato con las 5 filas E1-E5. |
| Añadir rechazos con motivo en ia.md | S5 | cerrado | Registro 11 de `docs/ia.md` descarta una alternativa con motivo técnico explícito. |
| Evidenciar run de CI en verde | S5 | cerrado | Run verde confirmado sobre el commit calificado, antes del cierre. |
| ADR con marca de reemplazo y trazabilidad | S5 | cerrado | ADR-0001 marca "Superada parcialmente por ADR-0002" con enlace; corrige el hallazgo preliminar. |
| Nombres de ADR enuncian el tema, no la decisión | S5 | sí | 0001 y 0002 comparten el título "Selección de Arquitectura Base"; deberían titularse por la decisión (p. ej. "Adoptar Next.js/FastAPI..."). |
| Tres commits llegaron después del cierre (2026-09-07T05:22Z–06:26Z) | S5 | — (no se calificaron) | Se les avisó que solo cuenta lo anterior al cierre; esos commits corrigen duplicación de pruebas y documentan en ia.md. |
| dbb98d3 elimina duplicación en tests de búsqueda | S5 | no (resuelto tarde) | — |
| 75881e4 elimina duplicación en test de búsqueda (corte 1) | S5 | no (resuelto tarde) | — |
| e77a240 actualiza README con validación | S5 | no (resuelto tarde) | — |
| c12dda8 documenta proceso de corte vertical en ia.md | S5 | no (resuelto tarde) | — |
| 74337a3 actualiza README con instrucciones de prueba vertical | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz | S5 | si | |
| secciones arc42 7/8/11 | S5 | si | |
| trazabilidad E3-E5 | S5 | si | |
| commit en ADR-0001 | S5 | si | |
| verificación de pipeline | S5 | si | |
| README con comando único | S5 | si | |
| Mapa de contextos con relaciones tipificadas | S6 | si | |
| Tabla módulo-datos con dueño único | S6 | si | |
| Lista de violaciones con plan de corrección | S6 | si | |
| Sección 8 de arc42 | S6 | si | |
| C4 nivel 3 y ADR si aplica | S6 | si | |
| Trazabilidad completa en aspectos.md | S6 | si | |
| Registro de rechazos en ia.md | S6 | si | |
| Instrucciones de arranque y prueba en README | S6 | si | |
| Evidencia de ejecución de CI | S6 | si | |
| Correcciones a correcciones.md y enlaces subidas después del cierre (commits 1cab45e, df8f512, 11577b9, 6e275a6, 6d0a1b8, 2026-09-10T22:15:10Z a 22:21:13Z) no estaban en el estado calificado. | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz (a HEAD sigue en docs/correciones.md). | S5 | si | |
| Enlaces rotos en docs/aspectos.md y docs/correciones.md. | S5 | si | |
| Celdas pendientes en la tabla de trazabilidad (E3-E5). | S5 | si | |
| Nomenclatura de ADR no conforme. | S5 | si | |
| Falta SonarCloud en el pipeline. | S5 | si | |
| Contrato OpenAPI/AsyncAPI versionado (S7) | S7 | no (resuelto) | Tres contratos ejecutables versionados en el hash calificado. |
| Prueba de contrato ejecutada por el pipeline (S7) | S7 | no (resuelto) | `ci.yml` instala Schemathesis y ejecuta pytest sobre backend/tests, incluida test_contract.py. |
| Evidencia de que la prueba de contrato falla ante un cambio incompatible (S7) | S7 | no (resuelto) | Evidencia del fallo controlado documentada y run 35549837357 en rojo. |
| ADR de estrategia de integración síncrona o asíncrona (S7) | S7 | no (resuelto) | ADR-0004 con alternativa descartada y escenario E2. |
| Evidencia pública de SonarCloud con Quality Gate, pendiente desde S6 | S7 | sí | Falta el run del scanner y la URL pública con Quality Gate. |
| C4 nivel 2 con protocolo y formato en cada flecha | S7 | no (resuelto) | `docs/c4/contenedores.md` releído; relaciones con protocolo y formato. |
| Trazabilidad de ADR-0001 y ADR-0003 (commit y enlaces pendientes) | S7 | si | |
| Prueba de sustitución del adaptador para E2, declarada pendiente en docs/aspectos.md | S7 | si | |
| 2026-09-15T11:04-11:27 -05:00: b2bf164, 56f979b, 66dccb3, 7483132, 579ff78 y 430b9a0 reescriben y renombran el documento S6 y ajustan los enlaces del README después del cierre 2026-09-14T05:00Z. | S6 | no (resuelto tarde) | — |
| 2026-09-15T10:40:25-05:00: 418196c elimina matrices de cumplimiento y secciones de conclusión del paquete S6 tras el cierre. | S6 | no (resuelto tarde) | — |
| Evidencia pública de SonarCloud (run exitoso del scanner y URL del análisis con Quality Gate) para el hash revisado. | S6 | si | |
| Lista de no conformidades de propiedad con entidad, dueño esperado y ubicación observada, más su plan de corrección. | S6 | si | |
| Tipificación de las relaciones del mapa de contextos con el vocabulario de la semana. | S6 | si | |
| Trazabilidad de ADR-0003 (commit de implementación y enlace correcto al ADR de referencia) y de ADR-0001. | S6 | si | |
| Prueba específica de sustitución del adaptador externo para el escenario E2, hoy citada con una prueba que no la cubre. | S6 | si | |
| Ninguno: commits_tardios_post_cierre está vacío y el último commit (9334a03) es anterior al cierre; los ajustes de contrato y su evidencia se registraron el 2026-09-20. | S7 | no (resuelto tarde) | — |
| Aportar la línea de ci.yml que ejecuta la prueba de contrato y la URL del run. | S7 | no (resuelto) | La línea está en ci.yml; la URL del run queda como corroboración externa. |
| Aportar el registro del cambio incompatible que hizo fallar la prueba, o un run en rojo. | S7 | no (resuelto) | docs/evidencias/cambio_incompatible_evidencia.md y commits 6397c09/715347d. |
| Aportar la URL pública de SonarCloud con Quality Gate y el run que invocó el scanner. | S7 | sí | Sin evidencia pública de SonarCloud. |
| Completar la evidencia de correspondencia contrato-código (main.py frente a openapi.yaml). | S7 | no (resuelto) | Rutas del contrato localizadas en backend/app/main.py. |
| Aportar el contenido de arc42 sección 6, C4 de contenedores y docs/aspectos.md. | S7 | no (resuelto) | Los tres artefactos releídos en el hash calificado. |
| Despliegue accesible desde fuera con URL y health check. | S8 | sí (diferido: URL por Moodle) | |
| Infraestructura como codigo versionada y README de recreacion del entorno. | S8 | no (resuelto: `infra/azure/main.bicep`, `deployment/vercel/`) | |
| Pipeline en verde sobre master y analisis SonarCloud auditable. | S8 | sí (CI en verde; SonarCloud sin paso del scanner en CI) | |
| Logs estructurados y metrica consultable ligada al escenario E1. | S8 | no (resuelto: `observability.py`, `/metrics` con `drift_search_latency_ms`) | |
| Estimacion de costo mensual con supuestos; limite de costo y 'sin tarjeta' en arc42 seccion 2. | S8 | no (resuelto: `Estimacion_costos.md` y `arc42_2` §2.7) | |
| arc42 seccion 7 y un ADR por decision de plataforma con alternativa descartada. | S8 | no (resuelto: `arc42_7` y ADR-0005/0006) | |
| Nombres de ADR: el ADR-0007 usa `ó` acentuada y no es kebab-case ASCII. | S9 | sí | Ver feedback S9 |
| Sin dependencias añadidas en el periodo de S9 (diff `74709aa..8a00556` vacío); verificación sobre el conjunto preexistente. | S9 | sí | Ver feedback S9 |
| SonarCloud: run del scanner y URL pública con Quality Gate, pendiente desde S6. | S9 | sí | Ver feedback S9 |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público en ISCOUTB con nombre conforme, rama master; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Seis rutas presentes; arc42 no incluye sección 11, deuda de completitud aunque existe directorio. [docs/aspectos.md:48–58](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/aspectos.md#L48-L58). |
| Estado calificado identificable | Cumple | Snapshot y fecha completos en encabezado; coincide con la punta actual. |
| Nombres de ADR según la convención | No cumple | ADR-0007 usa acento y nombre no conforme al patrón; [docs/adr/0007-evaluacion-de-incorporación-coponente-generativo.md:1–7](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0007-evaluacion-de-incorporaci%C3%B3n-coponente-generativo.md#L1-L7). |
| ADR aceptados no reescritos | No verificado | El historial de ADR previos requiere confirmar inmutabilidad desde aceptación; no se declara resuelto el hallazgo anterior. Los ADR nuevos no reemplazan expresamente los reescritos. |
| docs/ia.md al día para la semana | Cumple | Registros nuevos de revisión y organización S9 con validación y alternativas descartadas por razones técnicas; [docs/ia.md:831–919](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/ia.md#L831-L919). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI y Azure deployment success en el hash, pero el scanner fue añadido y revertido antes del cierre. El workflow actual no invoca SonarCloud; [.github/workflows/ci.yml:1–54](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/.github/workflows/ci.yml#L1-L54), [sonar-project.properties:1–6](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/sonar-project.properties#L1-L6). Archivo de propiedades por sí solo no prueba análisis/Gate. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Snapshot sin credenciales reales; referencias de Actions, permisos y ejemplos de patrón. No se certificó revisión exhaustiva de todos los blobs históricos. |
| Contribución de todos los integrantes | No verificado | Ocho firmas, 384 commits agregados. Sin atribuir variantes por parecido; correspondencia completa con cuatro integrantes no verificada. Punta actual: 8 firmas y 384 commits agregados; no equivalen automáticamente a personas. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Ocho firmas y 384 commits en S9; variantes sin consolidación por persona no se contabilizan como ocho integrantes. En HEAD: 8 firmas y 384 commits agregados.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Luis Mario Perez Diaz | `lmpdiaz12` | 51 (S3) | — | — | Autor del ADR y de la mayor parte del periodo |
| Mauricio Andres Fernandez Espinosa | `maufern4ndez` | 19 (S3) | — | — | — |
| Joshua David Reyes Leones | `JoshuaR01` (+ `JoshXX`, mismo correo) | 18 (S3) | — | — | dos identidades consolidadas |
| Jerry Daniel Buelvas Mejia | `JerryDBM` | 9 (S3) | — | — | — |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Qué devuelve la búsqueda si Steam se cae y el catálogo de PlayStation está vacío después de un reinicio?
- ¿Cómo cambia el costo por búsqueda si se elimina la caché o se replica el backend, y qué límite gratuito se alcanza primero?
- ¿Qué cambiarían tras repetir la medición controlando caché caliente, arranque en frío y variación de Steam?
