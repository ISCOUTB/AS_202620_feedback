# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Calificación automática |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://quantia-utb.onrender.com · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `72011933ff2238eaec697f565572fec6872a3cbc` · 2026-10-04T22:36:29-05:00 | 9/10 | Pendiente por limitación de verificación; intervalo documental 4.6–5.0, sin descontar la comprobación bloqueada | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `72011933ff2238eaec697f565572fec6872a3cbc` · 2026-10-04T22:36:29-05:00 | 3/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `4f6f568` · 2026-08-09T13:16:43-05:00 | 7/9 | no aplica | sí |
| 2 | S2 | `d4302f4` (2026-08-16T23:17:26-05:00) | 3/9 | no aplica | si |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `dd422fb` · 2026-08-23T23:52:23-05:00 | 6/9 | no se publica | sí |
| 4 | S4 | `cede35e` (2026-08-30T23:51:34-05:00) | 6/10 | 3.4 | si |
| 5 | CORTE1 | `8b0d00b` (2026-09-07T14:29:28-05:00) | 8/12 | 3.7 | si |
| 6 | S6 | `a47d5bd` (2026-09-13T23:21:55-05:00) | 3/8 | 2.5 (prelim.) | si |
| 7 | S7 | `2269ca5` (2026-09-20T21:48:00-05:00) | 10/10 | 5.0 (propuesta) | sí |
| 8 | S8 | `1f8f76d` (2026-09-27T19:55:57-05:00) | 10/10 graduables (2 filas de despliegue pendientes) | 5.0 (provisional) | si |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Aportar escenario operativo asignado para S10 y distinguirlo de EC-07/EC-08 elegidos en el proyecto. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Integrar scanner Sonar con run y Quality Gate del hash; demostrar bloqueo de integración. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Mitigar el consumo de cuota de POST /distractores sin autenticación, riesgo reconocido en ADR-0013; no se usó esa ruta durante esta revisión. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Mantener revisión humana de calidad y equivalencias; el 73 % válido no habilita aceptación automática de propuestas. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Conservar constancia del ajuste de enlaces ADR-0007, sin adoptar una excepción local a la regla del curso. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar barrido independiente de secretos cuando se resuelva el bloqueo del entorno revisor; no es incumplimiento demostrado del equipo. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| La prueba automática de dueño único sigue pendiente (V-5), aunque la porción declara propiedad y la auditoría de erosión está documentada. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| La ausencia de porción, cadena y extracto IA de la preliminar queda superada por RF-11/A-06. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La evaluación generativa, costo/latencia y proveedor externo en C4 ya cuentan con evidencia; dataset y resultados se inspeccionaron. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| El ADR-0014 aclara que la edición histórica del ADR-0007 fue de cuatro enlaces; no borra el hecho ni modifica el contrato. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| El frontend y health check antes diferidos pudieron consultarse en la revisión actual, sin recalificar S8. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/adr` versionado como blob vacío, no como directorio | S1 (08-09) | no (S3 resuelto) | Directorio con 0001, 0002 y 0003 |
| Ficha del problema fuera del repositorio («Informe Inicial» de Moodle) | S1 (08-09) | no (resuelto en `dd422fb`) | `docs/Ficha-problema.md` subida el 23-ago 23:52 |
| Solo 1 cuenta contribuyendo al historial | S1 (08-09) | no (S3 resuelto) | 4 cuentas en el historial |
| `docs/aspectos.md` sin enlaces desde las filas a los escenarios | S2 (16-ago) | no (S3 resuelto) | Tabla ADD con enlaces a EC y ADR |
| Restricciones sin categorías organizativas ni legales | S2 (16-ago) | no (S3 resuelto) | Categorías completas en arc42 §2 |
| Esqueleto ejecutable prometido en ADR-0001 y no entregado al cierre | S3 | parcial: entró 2 h después del cierre (`e976c92` 01:58) — no cuenta para S3 | Para S4: el esqueleto debe traer run en verde del pipeline; respetar los cierres |
| Matriz comparativa de estilos contra el árbol de utilidad ausente | S3 | no (resuelto) | §4.1 con filas por EC-01…EC-07 |
| ADR sin hipervínculo desde el escenario motivador EC-04 | S3 | no (resuelto) | EC-04 y EC-05 con enlaces al ADR |
| 2 commits posteriores al cierre (`88294cc` 01:00, `e976c92` 01:58) | S3 (cierre) | registrado | Entregar dentro del cierre de la actividad; lo tardío no califica |
| C4 nivel 2 incompleto en docs/c4/doc-c4.md | S4 | si | Corregido: el equipo demostró (correcciones_feedback.md, hallazgo 2) que el Nivel 2 ya estaba completo en cede35e; aceptado. |
| Fila A-01 de aspectos.md con C2 pendiente | S4 | si | Resuelto para el corte 1: la fila A-01 ahora enlaza C4 Nivel 2 real, ADR 0002+0006, código y pruebas sin huecos. |
| Verificación de CI sin runs | S4 | si | Corregido: 21+ runs en verde confirmados por curl a actions/runs, incluido uno sobre el commit calificado; aceptado (hallazgo 1 de correcciones_feedback.md). |
| Secciones 7 y 8 del arc42 pendientes (declarado) | S4 | si | Fuera del alcance de esta revisión de corte 1 (evidencia S4, no recalificable); queda anotado. |
| Confirmar etiqueta corte-1 | S5 | si | Confirmada: corte-1 -> 201acac, 2026-09-07T04:34:17Z, antes del cierre. |
| Contrastar diagnóstico con la restricción asignada | S5 | si | La restricción de Moodle no llegó al equipo; se trabajó sobre R-06 (deuda declarada) con diagnóstico medido y aceptado. |
| Medir línea base y resultado contra umbral | S5 | si | Resuelto: 100% de pérdida silenciosa medida antes del cambio, 0% después, dentro del umbral de 10s. |
| Evidenciar pipeline en verde | S5 | si | Resuelto: run success sobre 201acacb a las 2026-09-07T04:43:04Z, antes del cierre. |
| Completar trazabilidad de A-04 | S5 | si | No se revisó A-04 en este corte; el reto tocó A-01. Sigue abierto para A-04. |
| Verificar contenido de docs/ia.md | S5 | si | Verificado: entrada 7 (2026-09-06) con 4 rechazos y motivo técnico, referida a este corte. |
| ADR y estructura docs/adr creados después del cierre (commits 9a80cf0 a 201acac, 2026-08-30 en adelante). | S2 | no (resuelto tarde) | — |
| Pipeline CI agregado tras el cierre (.github/workflows/ci.yml solo en HEAD). | S2 | no (resuelto tarde) | — |
| README actualizado con arranque y prueba tras el cierre (commit 02c39d8 2026-08-30T14:05:57-05:00). | S2 | no (resuelto tarde) | — |
| docs/aspectos.md actualizado con A-04 y retiro de tensión T-2 tras el cierre (commit 9469642 2026-08-30T14:11:19-05:00). | S2 | no (resuelto tarde) | — |
| Código y evidencia del aspecto A-01 agregados después del cierre (59e182e y db99e99, 2026-08-30). | S2 | no (resuelto tarde) | — |
| Escenarios de calidad con medida numérica en arc42 sección 10. | S2 | si | |
| Árbol de utilidad priorizado por impacto y riesgo. | S2 | si | |
| Tabla de aspectos navegable hasta código, ADR, pruebas y evidencia. | S2 | si | |
| Clasificación de restricciones en técnicas, organizativas y legales. | S2 | si | |
| 8b0d00b (2026-09-07T14:29:28-05:00) renombra correcciones_feedback.md a correcciones.md: corrige la fila 2 de la ficha S5 después del cierre. | S5 | no (resuelto tarde) | — |
| docs/ia.md sigue ausente en HEAD. | S5 | si | |
| Correcciones trazables en correcciones.md no se pudieron contrastar: no se verificó su contenido ni respuesta a hallazgos S1-S4. | S5 | si | |
| No hay runs_ci citados para respaldar el pipeline en HEAD. | S5 | si | |
| Renombrado de correcciones_feedback.md a correcciones.md en 8b0d00b (2026-09-07T14:29:28-05:00), posterior al cierre | S5 | no (resuelto tarde) | — |
| Verificar contenido de correcciones.md a HEAD | S5 | si | |
| Confirmar run de CI para el hash calificado | S5 | si | |
| PDF en Moodle | S5 | si | |
| Sustentación | S5 | si | |
| Confirmar organización ISCOUTB | S5 | si | |
| Adjuntar run de CI del hash calificado | S5 | si | |
| Confirmar docs/ia.md con rechazos documentados | S5 | si | |
| Contrato de API en formato ejecutable versionado en el repositorio. | S7 | si | |
| Prueba de contrato ejecutada por el pipeline y evidencia de que falla ante un cambio incompatible. | S7 | si | |
| Evidencia auditable de SonarCloud (workflow, run exitoso y URL pública con Quality Gate). | S7 | si | |
| Verificación de la tabla de aspectos, el registro de IA, la sección 6 del arc42 y el C4 nivel 2. | S7 | si | |
| Aportar runs de CI y URL pública de SonarCloud con Quality Gate para el hash a47d5bd. | S6 | si | |
| Incluir contenido de docs/aspectos.md y verificar sus ocho columnas. | S6 | si | |
| Incluir contenido de docs/ia.md con lo aceptado y lo rechazado. | S6 | si | |
| Incluir arc42 §8 con lenguaje ubicuo y mapa de contextos. | S6 | si | |
| Aportar lista de no conformidades de propiedad con ubicación y plan, o el recorrido que concluyó ausencia. | S6 | si | |
| Aportar diff contra el hash de S5 y C4 nivel 3/ADR si los límites cambiaron. | S6 | si | |
| arc42 seccion 7 (Deployment View) con una caja por pieza y donde se ejecuta | S8 | si | |
| ADR por decision de plataforma con alternativa descartada y capa gratuita verificada | S8 | si | |
| Estimacion de costo mensual con volumen supuesto y punto de ruptura de la capa gratuita | S8 | si | |
| URL publica desplegada y health check con hora y codigo de respuesta | S8 | si | |
| Evidencia de pipeline en verde y de SonarCloud (configuracion, run y analisis publico) | S8 | si | |
| Limite de costo y restriccion de tarjeta en arc42 seccion 2 | S8 | si | |
| Tabla de aspectos sin huecos (no verificable con la evidencia aportada) | S8 | si | |
| R-06 (persistencia) y V-5 (verificacion automatica de propiedad de datos) siguen abiertos | S8 | si | |
| Evidencia auditable de SonarCloud: configuracion, invocacion del scanner en el workflow y URL publica con Quality Gate. | S6 | sí | El análisis corre desde la interfaz de SonarCloud; ningún paso del pipeline lo ejecuta. El equipo lo reconoce en `correcciones.md` y `docs/ia.md`. |
| `ADR-0007` editado despues de aceptarse, sin reemplazo declarado. | S8 | sí | La edición (2026-09-26) solo actualiza enlaces de documentación; se registra por la regla del §4. |
| Punta sin commits nuevos desde S8 (`1f8f76d`, 2026-09-27): el periodo S9 está vacío. | S9 (prelim.) | si | Empujar la evidencia S9 antes del cierre del 2026-10-05. |
| Sin porción nueva construida con IA, sin ADR y sin extracto de `docs/ia.md` del periodo S9. | S9 (prelim.) | si | Aportar la porción real del sistema y su cadena para la evidencia S9. |
| Componente generativo (LLM para distractores, ADR-0005) sin conjunto de evaluación, costo por operación ni latencia, ni contenedor externo en el C4 nivel 2. | S9 (prelim.) | si | Evaluar el componente con resultados, costo y latencia, y reflejarlo en el C4 nivel 2. |
| Sin auditoría de erosión del periodo ni verificación de dependencias añadidas en S9. | S9 (prelim.) | si | Documentar límites de contexto/propiedad de datos y las dependencias del periodo. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon git público ISCOUTB/AS_202620_Sistema-de-calificacion-automatica; rama master y nombre conforme. |
| Estructura mínima presente | Cumple | README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md presentes; la fila [docs/aspectos.md:40](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/aspectos.md#L40) enlaza la porción. |
| Estado calificado identificable | Cumple | 72011933ff2238eaec697f565572fec6872a3cbc, 2026-10-04T22:36:29-05:00, último master anterior al cierre; HEAD coincide. |
| Nombres de ADR según la convención | Cumple | Inventario docs/adr: 0001–0014, nombres conformes NNNN-kebab-case.md. [docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md:1–6](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md#L1-L6). |
| ADR aceptados no reescritos | No cumple | Historial de ADR-0007 confirma creación c0f976d y edición 1c8bcfb el 26-sep tras aceptación. ADR-0014 explica cuatro cambios de enlace y conserva la decisión, pero no reemplaza el ADR ni borra la edición: [docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md:14–26](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md#L14-L26), [docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md:64–68](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md#L64-L68). Su regla local más flexible no modifica el contrato del curso; queda aclarada la naturaleza del cambio, no cumplimiento retroactivo. |
| docs/ia.md al día para la semana | Cumple | Entrada S9 actualizada hasta el commit final; acepta, corrige y rechaza con motivo técnico: [docs/ia.md:215–232](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/ia.md#L215-L232). S10 requiere registro de su trabajo cuando se identifique el reto. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [CI del hash final success](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/37260121474). [.github/workflows/ci.yml:20–60](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/.github/workflows/ci.yml#L20-L60) instala y prueba backend/frontend sin invocación Sonar; enlace genérico en [README.md:67–68](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/README.md#L67-L68) no acredita scanner ni Quality Gate del hash. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El barrido independiente de snapshot e historial no concluyó por interrupción de herramienta. La revisión documental [docs/evidencia/auditoria-s9.md:130–146](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/evidencia/auditoria-s9.md#L130-L146) explica las coincidencias de patrones citados, pero no sustituye la verificación pendiente. |
| Contribución de todos los integrantes | Cumple | README mapea explícitamente las cuatro cuentas a integrantes: [README.md:9–13](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/README.md#L9-L13). Shortlog del hash observado: cuatro firmas con 91, 44, 27 y 23 commits (185 total); sin correos publicados. Esta evidencia acredita presencia, no igualdad de esfuerzo ni comprensión individual. |

## Contribución por integrante

Actualización agregada del 2026-10-06: 185 commits en cuatro firmas explícitamente asociadas a los cuatro integrantes en README: distribución 91/44/27/23. No se publican correos ni se infiere comprensión individual.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits (a S8, `1f8f76d`) | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Sebastian Canas Plata | scp1109 | 83 | — | — | Historial completo del semestre |
| Josue David Ortega De Arco | josueacademico17-source | 37 | — | — | Desde la semana 3 |
| Susana Marcela Rosales Castellar | SusanaRosales | 24 | — | — | Desde S3 |
| Maria Del Mar Restrepo Licona | Mariadelmar-restrepo | 17 | — | — | Desde S3 |

Corrección aceptada (hallazgo 8 de `correcciones_feedback.md`): la tabla anterior daba 27/9/1/3; `git shortlog -sn` sobre `cede35e` y `corte-1` confirma 34-35/16/7/3.

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Fallo: si el proveedor devuelve 429, JSON inválido o tarda más del límite, ¿cómo mantienen disponible la calificación y comprueban esa independencia en el despliegue?
- Costo: con los tokens medidos por solicitud, ¿cuántos exámenes agotan primero la cuota y cómo impedirán que una ruta pública la consuma sin control?
- Medición: al observar 44 de 60 propuestas válidas y errores de etiquetado, ¿qué cambiarían en el conjunto, la revisión o la implementación antes de ampliar el uso?
