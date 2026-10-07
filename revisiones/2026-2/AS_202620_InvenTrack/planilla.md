# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo InvenTrack. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | InvenTrack |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Javier Alejandro Carta Lacharme · Esteban Javier Peluffo Marquez · Felix Andres Taborda Jimenez · Jose Gabriel Vargas Perez — cuentas abajo; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://inventrack.iscoutb.dev · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `main` · `35a9c63dd603bab989a18ed17ca56063c5616585` · 2026-10-04T22:14:10-05:00 | 8/10 | Pendiente por limitación de verificación; intervalo documental 4.2–4.6, sin descontar la comprobación bloqueada | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `main` · `35a9c63dd603bab989a18ed17ca56063c5616585` · 2026-10-04T22:14:10-05:00 | 3/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 8 | S8 | `48aeecf` (2026-09-27T23:48:02-05:00) | 10/10 | 5.0 | sí, definitiva |
| 7 | S7 | `f10fd01` (2026-09-20T23:01:13-05:00) | 9/10 | 4.6 | sí, auditada |
| 6 | S6 | `d6f2b19` (2026-09-13T23:37:36-05:00) | 7/8 | 4.5 | si |
| 5 | CORTE1 | `ac951e3` (2026-09-08T10:11:58-05:00) | 9/12 | 4.0 | si |
| 4 | S4 | `d7ba824` (2026-08-30T23:39:33-05:00) | 5/10 | 3.0 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `06920209` · 2026-08-09T16:03:46-05:00 | 4/9 | 2,8 * | sí |
| 2 | S2 | `db90ff2` (2026-08-16T21:22:20-05:00) | 9/9 | no aplica | si |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `dd4ea1cb8` · 2026-08-23T23:46:24-05:00 | 9/9 | no se publica | sí (actualizada tras el cierre) |

S8 se califica sobre 10 de las 12 filas de la ficha: quedan pendientes de calificar las dos filas de despliegue (URL del sistema accesible desde fuera de la red de la universidad y health check consultable), porque la URL se entrega por Moodle. La nota publicada es provisional.

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Medir catálogo/stock con la carga y condiciones de ESC-04; la sonda /health no es un sustituto. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar el registro inmutable/reemplazo de ADR anteriores y aportar run/scanner/Quality Gate público del hash revisado. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Terminar la verificación independiente de secretos e identidad de contribuciones; la limitación de herramienta no demuestra exposición. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Identificar escenario S10, línea base del despliegue y resultado reproducible. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Se cierra «sin porción S9»: app/main.py y tests/test_metrics.py cambian dentro del periodo. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| ASP-03 ya enlaza ocho eslabones y existe mutación documentada que falla. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Hay auditoría de límites con universo de dependencias nuevo vacío explícito; se corrige la lectura anterior que penalizaba no añadir paquetes. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| ADR-0008 formaliza no incorporar generación; ADR-0009 reconoce el problema de inmutabilidad, aunque su resolución es parcial. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Sondas del despliegue institucional responden; la falta de URL/health no sigue abierta como ausencia de artefacto. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Javier Carta Lacharme sin commits ni cuenta atribuible | S1 | Cerrado en S3: `jxviercarta-a11y` firma 3 commits en el periodo (atribución por confirmar con el docente) | Verificar acceso al repositorio y empezar a contribuir (la contribución individual se califica en el final) |
| `docs/aspectos.md` en prosa, sin la tabla de 8 columnas del contrato | S1 | Cerrado en S3 (`8ba799f`): tabla de 8 columnas con enlace al ADR desde ASP-01 | Convertir a tabla ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia; además enlazar el ADR 0001 desde la fila del aspecto y desde ESC-01/ESC-02 |
| `docs/adr/README.md` haría fallar el filtro de nombres de ADR (placeholder) | S2 | Cerrado en S3 (`2abab34` lo eliminó) | Resuelto |
| ADR 0001 en estado «propuesto» y no alcanzable desde `aspectos.md` ni desde los escenarios que lo motivan | S3 | Parcialmente cerrado: los dos enlaces ya existen (ASP-01 y ESC-01); sigue «propuesto, pendiente de ratificación» | Ratificar (aceptar) el ADR |
| `ia.md` sin lo rechazado y su motivo en la entrada S3 | S3 | Cerrado en S3 (`8ba799f`): columna «Rechazado / motivo» llena | Resuelto |
| Prueba sin pipeline ni evidencia de ejecución | S3 | Cerrado en S3 (`3e2a54b`): workflow añadido y CI en verde sobre el hash calificado | Resuelto |
| arc42 actualizado tras el cierre (2fc55e1, b4904bd) | S4 | no (resuelto tarde) | — |
| Módulo de inventario añadido tras el cierre (666c4e4) | S4 | no (resuelto tarde) | — |
| ADR-0002 eliminado tras el cierre (64ab86f) | S4 | no (resuelto tarde) | — |
| aspectos.md y containers.md corregidos tras el cierre (4e6957e, 3de2988) | S4 | no (resuelto tarde) | — |
| Confirmar si arc42 secciones 4-6 y 12 quedaron redactadas a HEAD | S4 | si | |
| Añadir evidencia de análisis estático SonarCloud | S4 | si | |
| Completar celda de Pruebas en docs/aspectos.md | S4 | si | |
| Etiqueta `corte-1` ausente | S5 | No (creada 2026-09-06, `2988b03`) | Resuelto. |
| Respuesta al reto sin diagnóstico, ADR ni incremento identificado | S5 | Sí (más grave de lo esperado) | El equipo escribió ADR-0002, reporte de medición y trazabilidad completos sobre control de concurrencia (ASP-02), pero `git diff --stat` confirma que ningún archivo de `app/` cambió: el mecanismo de lock que describen no existe en el código y las cifras de medición no son reproducibles. Implementar realmente el mecanismo antes de sustentar. |
| Umbral de rendimiento definido sin medición ejecutada | S2 | Sí | Aportar herramienta, carga, procedimiento y resultado. |
| Módulo de inventario de HEAD sin fila propia en `docs/aspectos.md` | S5 | No (resuelto) | ASP-02 ya tiene fila completa en `docs/aspectos.md`, aunque la celda de código no refleja un cambio real (ver hallazgo crítico). |
| Registro de IA sin entrada del Corte 1 | S5 | No (resuelto) | `docs/ia.md` tiene entrada del 2026-09-06 para el Reto Corte 1 con rechazo explícito y motivo técnico. |
| Enlace del README a `docs/c4/container.md` no existe | S5 | No verificado en esta revisión | No se reinspeccionó este enlace puntual; confirmar en el próximo corte. |
| La corrección 'Update and rename feedback.md to correcciones.md' (ac951e3, 2026-09-08) es posterior al cierre. | S2 | no (resuelto tarde) | — |
| Se añadieron ADR-0001 y ADR-0002, código, CI y trazabilidad en commits posteriores al cierre (7b0aad5, bcb133d, 8d149c1). | S2 | no (resuelto tarde) | — |
| El commit cf9d7d3 define Flutter como frontend, decisión de stack posterior a la entrega s2. | S2 | no (resuelto tarde) | — |
| No hay runs_ci citables que confirmen la ejecución del pipeline a HEAD. | S2 | si | |
| Faltaba CI/ADR en s2; a HEAD ya existen, pero la evidencia de ejecución no está registrada. | S2 | si | |
| Secciones 5, 6 y glosario de arc42: se agregaron después del cierre (commits 22bd660, c870f2b y otros entre 2026-09-06 y 2026-09-08). | S4 | no (resuelto tarde) | — |
| Prueba de corte vertical: tests/productos/test_api_corte_vertical.py se agregó en HEAD pero no existe en d7ba824. | S4 | no (resuelto tarde) | — |
| Fila de aspectos con columna Pruebas completa: se resolvió en HEAD con la trazabilidad del corte 1 (commit bb4ef0c). | S4 | no (resuelto tarde) | — |
| SonarCloud: sonar-project.properties se agregó en HEAD, no en el commit calificado. | S4 | no (resuelto tarde) | — |
| En HEAD aún no se verifica ejecución de SonarCloud en un run; no hay evidencia de análisis estático en los runs disponibles. | S4 | si | |
| correcciones.md creado en ac951e3 (2026-09-08) tras el cierre, renombrando feedback.md. | S5 | no (resuelto tarde) | — |
| Frontend definido como Flutter en cf9d7d3 (2026-09-07) tras el cierre, actualizando README y containers.md. | S5 | no (resuelto tarde) | — |
| Integrar SonarCloud al pipeline de CI. | S5 | si | |
| Verificar que correcciones.md responda a todos los hallazgos S1-S4. | S5 | si | |
| Equilibrar la distribución de contribuciones. | S5 | si | |
| Mapa de contextos del dominio con relaciones tipificadas | S6 | si | |
| Tabla módulo a datos con dueño único por entidad | S6 | si | |
| Lista de violaciones de propiedad de datos con plan de corrección | S6 | si | |
| Lenguaje ubicuo y mapa de contextos en arc42 sección 8 | S6 | si | |
| C4 nivel 3 | S6 | si | |
| Evidencia de ejecución de SonarCloud en CI | S6 | si | |
| Tabla de aspectos convertida a 8 columnas después del cierre de S2 (correcciones.md, sección Semana 2); verificada en docs/aspectos.md de ac951e3. | S5 | no (resuelto tarde) | — |
| ADR-0001 actualizado a Aceptado después del cierre de S3 (correcciones.md, sección Semana 3); verificado en docs/adr/0001 de ac951e3. | S5 | no (resuelto tarde) | — |
| Corte vertical y mecanismo de consistencia implementados después de S4 (correcciones.md, sección Semana 4); verificados en app/productos, app/inventario y tests de ac951e3. | S5 | no (resuelto tarde) | — |
| correcciones.md sin estructura de índice trazable (criterio 3 de la ficha S5). | S5 | si | |
| Sin evidencia de ejecución de SonarCloud. | S5 | si | |
| PDF en Moodle y sustentación pendientes de verificación. | S5 | si | |
| Verificar sección 8 de arc42 (lenguaje ubicuo y mapa de contextos) | S6 | si | |
| Evidenciar ejecución del pipeline CI | S6 | si | |
| Evidencia reproducible de fallo de la prueba contractual ante un cambio incompatible | S7 | Sí | Aportar run en rojo o commit reproducible. |
| Versión contradictoria entre el contrato ejecutable y `docs/api/inventrack-contrato.md` | S7 | Sí | Alinear la documentación con la versión 0.1.0 del OpenAPI. |
| SonarCloud deshabilitado al cierre S7 | S7 | No (resuelto tarde) | La punta S8 restituye scanner, proyecto público y run en verde. |
| Despliegue público, health check e infraestructura como código ausentes | S8 | Sí | Elegir plataforma, desplegar y versionar el entorno. |
| Sin logs estructurados, métrica consultable ni estimación de costo | S8 | Sí | Instrumentar observabilidad y calcular el consumo mensual. |
| Vista de despliegue productiva y ADR de plataforma ausentes | S8 | Sí | Completar arc42 §7 y registrar la decisión. |
| Sin porción de sistema, cadena, prueba ni medición en el periodo S9 (solo despliegue a Dokploy) | S9 | Sí | Entregar la porción construida con IA con su cadena completa antes del cierre. |
| Auditoría de erosión del periodo de generación S9 | S9 | Sí | Documentar si cruzó límites de contexto o reglas de propiedad de datos de S6, y su corrección. |
| ADR de decisión sobre el componente generativo | S9 | Sí | La ausencia de decisión no es la decisión de no incorporarlo. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_InvenTrack; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Árbol Git contiene seis rutas mínimas; tabla de aspectos [docs/aspectos.md:15-19](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/aspectos.md#L15-L19) y documentos enlazados existentes. |
| Estado calificado identificable | Cumple | main, 35a9c63dd603bab989a18ed17ca56063c5616585, fecha y corte en cabecera. |
| Nombres de ADR según la convención | Cumple | Listado docs/adr: 0001–0009, todos NNNN-titulo-en-kebab-case; [docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md:1-15](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md#L1-L15). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md:7-15](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md#L7-L15) reconoce ediciones aceptadas de 0002/0004/0005 y declara consolidación futura; no marca cada decisión anterior reemplazada con enlaces. Historial del periodo incluye restauración [193e2628](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/193e2628757f3e8987ae5a01a90b8e8cce45d7a0). La corrección de política se reconoce, pero no borra las reescrituras. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:23-25](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/ia.md#L23-L25) contiene usos hasta S9, aceptado y rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [sonar-project.properties:1-7](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/sonar-project.properties#L1-L7) y [.github/workflows/test.yml:23-45](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/.github/workflows/test.yml#L23-L45) acreditan configuración/scanner. Una consulta de runs del commit (limitada a pull_request por el conector) no devolvió registros; no acredita ausencia de push ni éxito. No se verificó el Quality Gate público para este hash; además el YAML no incluye espera/bloqueo explícito de Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | No verificado | La auditoría del equipo declara ausencia de credenciales en [docs/evidencia-ia-corte-s6.md:176-180](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s6.md#L176-L180). Las referencias de secretos de CI son variables en [.github/workflows/test.yml:37-41](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/.github/workflows/test.yml#L37-L41). El barrido independiente ampliado fue cancelado por la herramienta y el único reintento no lo completó; no se convierte esa limitación en evidencia de exposición ni en un árbol limpio verificado. |
| Contribución de todos los integrantes | No verificado | El historial contiene varias firmas; las atribuciones por semejanza no se usan. La planilla previa reconoce correspondencias pendientes. Se debe validar cuenta–integrante y distribución, sin publicar correos. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Historial de la punta: 236 commits y 7 firmas de autor distintas (firmas, no personas). El historial contiene varias firmas; las atribuciones por semejanza no se usan. La planilla previa reconoce correspondencias pendientes. Se debe validar cuenta–integrante y distribución, sin publicar correos.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Javier Alejandro Carta Lacharme | `jxviercarta-a11y` (atribución por confirmar) | 3 (S3) | 0 | — | Apareció en S3 (ficha, README, C4) |
| Esteban Javier Peluffo Marquez | Esteban Peluffo (correo omitido) | 3 (S3) | 0 | — | ia.md y entrega semanal |
| Felix Andres Taborda Jimenez | FlexT21 + «Felix Taborda» (mismo noreply, consolidado) | 1 (S3) | 0 | — | Correspondencia por confirmar con el docente |
| Jose Gabriel Vargas Perez | Josephva24 + «Jose Vargas» (mismo correo `[correo omitido]`, consolidado) | 6 (S3) | 0 | — | ADR, esqueleto, workflow de CI y ajustes de trazabilidad |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Fallo: si se reinicia o replica el proceso, ¿qué ocurre con stock, locks y el historial p95 y cómo detectarán inconsistencias?
- Costo: ¿qué volumen o necesidad de persistencia obligaría a abandonar el presupuesto cero y qué alternativa compararon?
- Medición: si las consultas reales de stock incumplen 400 ms aunque /health sea rápido, ¿qué cambio harían y con qué experimento lo validarían?
