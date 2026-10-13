# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ROUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Diego Jose Baron Ruiz (`diegobrr999-commits`) · Julian David Manjarrez Guzman (`juliandmanjarrez-tech`) · Keiner Enrique Mendivil Diaz (`MKeinerrr`, dos correos) · Junior Jose Orozco Atencio (`junior14700`); ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://as-202620-routb.onrender.com · ver comprobación y límites en S10 |
| Última revisión | 2026-10-13 · consolidación S10 al cierre; S9 permanece sin cambios |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `7c6573e68a5fdab019fab8fddfe1acb2a451cb27` · 2026-10-03T18:20:32-05:00 | 9/10 | Pendiente por limitación de verificación; intervalo documental 4.6–5.0, sin descontar la comprobación bloqueada | sí, 2026-10-06 |
| 10 | Segundo corte · consolidado al cierre | `master` · `adde017b72d73f210eef6cb48d97cdf1687f5141` · 2026-10-12T22:02:26-05:00 | C1 0,80; C2 0,80; C3 0,80; C4 0,80 (cada uno /1) | Total 4,00/5; técnica 3,20/4 + C5 docente 0,80/1; ver [S10](semana-10-corte2.md) | sí, 2026-10-13 |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `68b0b05` · 2026-08-09T14:48:08-05:00 | 5/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `14e6688` · 2026-08-16T12:44:08-05:00 | 2/9 | no aplica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `1ed002b` · 2026-08-23T20:31:54-05:00 | 6/9 | no se publica | sí |
| 4 | S4 | `83b8c5e` (2026-08-30T19:33:15-05:00) | 10/10 | 5.0 | si |
| 5 | CORTE1 | `343bb9d` (2026-09-09T21:10:40-05:00) | 8/12 | 3.7 | si |
| 6 | S6 | `5b48dd0` (2026-09-13T23:43:22-05:00) | 4/8 | 3.0 (prelim.) | si |
| 7 | S7 | `fe266aa` (2026-09-20T21:32:01-05:00) | 9/10 | 4.6 | si |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `eae667e` (2026-09-27T21:58:06-05:00) | 10/10 (2 filas de despliegue diferidas) | 5.0 (provisional) | si |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Feedback S10 vigente · 13 de octubre de 2026

Límite exclusivo: **2026-10-13T05:00:00Z**, fin del 12 de octubre en Colombia. Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

**Subtotal técnico: 3,20 / 4,00. Total consolidado C1–C5: 4,00 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,00 / 5,00**, incorporada como **C5 = 0,80 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

El nuevo experimento incluye 50 observaciones de base y 50 de fallo, con ajuste de timeout y caché. Las pruebas simulan timeout sin esperar y no demuestran degradación de extremo a extremo real. El CI está verde, pero el paso Sonar es un echo.

Fuentes y alcance completos: [informe S10](semana-10-corte2.md#fundamento-técnico-y-comentarios-vigentes). Las referencias de identidad, contribución y despliegue heredadas conservan sus fechas originales; no constituyen una nueva verificación en esta consolidación.

### Deriva arquitectónica al cierre S10

Requests escribe Trips; push síncrono y timeout distinto del ADR.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · Requests modifica directamente los datos de ruta cuyo dueño es Trips:** La operación real accept_request llama refresh_trip_route_and_stop_eta y esta ejecuta UPDATE trips sobre route_geom, route_distance_m, route_duration_s y route_source. El límite de dueño único deja de proteger la actualización de rutas y la lógica de derivación queda repartida. Los cupos sí usan reserve/release públicos y no forman parte de este hallazgo. **Acción:** Mover la actualización de geometría y métricas de viaje a una operación pública de trips.application; Requests entrega las paradas/ids y conserva sus propias ETA. Eliminar también el import de helper privado de create_trip, o promoverlo a contrato público. Añadir regla de dependencias/escrituras entre módulos. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · El envío FCM secundario permanece en el camino síncrono de la respuesta:** ADR0013 exige que push no bloquee el flujo principal. El commit sucede antes y las excepciones se contienen, pero accept_request espera send_push y este llama send_each antes de retornar. Con FCM configurado, latencia/timeout de entrega se suma a la respuesta REST aunque la reserva ya esté confirmada. No se afirma que FCM esté configurado ni que haya lentitud real. **Acción:** Desacoplar envío después del commit mediante tarea/background worker con su propia sesión y timeout, o ratificar que es síncrono best-effort y acotar su presupuesto. Si se necesita entrega garantizada, usar outbox/reintentos; no reutilizar una sesión request cerrada en la tarea. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).
- **Media · La configuración Render sobreescribe el timeout ratificado de 1,4 s con 3,0 s:** La configuración versionada que recrea Render introduce ROUTING_TIMEOUT_SECONDS=3.0, anulando el default 1.4 que sostiene el presupuesto de ADR0014. Una recreación con ese manifiesto no conserva la mitigación documentada; el valor efectivo del panel y la latencia en producción no se verificaron. **Acción:** Cambiar el manifiesto a 1.4 o eliminar el override para usar el default ratificado; revisar la variable efectiva del panel con autorización y añadir prueba estática que compare configuración de despliegue y ADR/config. Medir nuevamente bajo condiciones relevantes, sin prometer el p95 a partir del valor nominal. [Contraste y evidencia](semana-10-corte2.md#deriva-d3).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Seguimiento anterior a la consolidación S10; estados históricos superados</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Identificar enunciado oficial de S10 y construir baseline/experimento comparable. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Confirmar versión pública: la evidencia histórica registró API sin seat_count; health 200 no cierra ese problema. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Obtener medición interna oficial en el mismo despliegue y declarar sus diferencias con la medición externa. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Integrar scanner Sonar y aportar run/Gate correspondientes al estado revisado. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar barrido de seguridad cuando el entorno de revisión lo permita; no es un defecto demostrado del proyecto. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Revalidar historial de ADR y confirmar mapeo explícito de identidades. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| La preliminar sin entrega S9 queda superada por reserva grupal, ADR, pruebas, medición y registro IA. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Se aporta auditoría de erosión E1–E6 con cambios observables y ADR de no incorporar generación. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La salud pública anteriormente diferida pudo comprobarse ahora por HTTP; no modifica S8 retroactivamente. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/ia.md` sin contenido real | S1 (08-09) | no (S3 resuelto; en S5 hay entrada específica del reto) | Ya registra por semana con aceptado/rechazado/justificación |
| `docs/aspectos.md` sin 8 columnas ni enlaces | S1 (08-09) | no (S3 resuelto; en S5 la fila 1 llega hasta la evidencia del reto) | Ya tiene la tabla y enlaza el ADR |
| Tensiones de calidad del problema sin declarar | S1 (08-09) | sin verificar en esta pasada | Revisar en el próximo corte |
| Escenarios sin las seis partes y con medidas sin condición de carga | S2 (08-16) | no (S3 resuelto) | Tabla con seis partes y cifras |
| C4 de contexto sin leyenda ni flechas etiquetadas | S2 (08-16) | sin verificar en esta pasada | Revisar en el próximo corte |
| ADR sin enlace desde el escenario motivador (10.2) | S3 | no (en S5, `docs/aspectos.md` enlaza los ADR desde cada fila) | — |
| README sin comando único de arranque (multi-paso) | S3 | no (resuelto: `uvicorn app.main:app --reload` y `flutter run`) | — |
| Sin workflow ni evidencia de prueba en verde | S3 | no (resuelto: `.github/workflows/ci.yml`, runs verdes) | — |
| Completar arc42 secciones 7, 8 y 11 | S4 | sin verificar en esta pasada | Revisar en el próximo corte |
| Completar filas 1 y 3 de docs/aspectos.md | S4 | no (resuelto en S5) | — |
| Integrar SonarCloud al pipeline | S4 | parcial: **integrado pero consistentemente en rojo** desde el 05/09 | Corregir los hallazgos de SonarCloud; no basta con tener el workflow, tiene que pasar |
| Enlazar ADR 0001 con commit de implementación | S4 | sin verificar en esta pasada | — |
| Registrar medición de línea base | S4 | no (resuelto en S5) | — |
| Crear etiqueta corte-1 | S5 | no (creada, antes del cierre) | — |
| Diagnóstico y línea base del reto | S5 | no (resuelto, aunque sin confirmar que responda a la restricción asignada) | Confirmar en la sustentación cuál fue la restricción individual asignada |
| ADR del reto | S5 | no (resuelto, nivel competente) | Añadir criterio de reconsideración y costo de reversión |
| Implementación y pruebas | S5 | no (resuelto) | — |
| Medición contra umbral | S5 | no (resuelto) | — |
| Completar celdas vacías de docs/aspectos.md | S5 | no (resuelto) | — |
| Configurar SonarCloud | S5 | sí, sigue en rojo | Resolver los hallazgos de SonarCloud antes del próximo corte |
| Registrar uso de IA de la semana 5 | S5 | no (resuelto) | — |
| 6f6e40c (2026-09-07T13:23:46-05:00) 'Evaluación de retroalimentación de IA' actualiza docs/ia.md después del cierre. | S5 | no (resuelto tarde) | — |
| 5c89522 (2026-09-09T21:10:11-05:00) 'S6' y 343bb9d (2026-09-09T21:10:40-05:00) 'Delete' son posteriores al cierre y no forman parte del estado calificado. | S5 | no (resuelto tarde) | — |
| correcciones.md no existe en la raíz del estado calificado ni en HEAD. | S5 | si | |
| No hay evidencia de que hallazgos S1-S4 hayan sido respondidos formalmente. | S5 | si | |
| Verificar contenido de correcciones.md | S5 | si | |
| Verificar contenido de docs/ia.md | S5 | si | |
| Verificar run de CI asociado al hash | S5 | si | |
| Entregar PDF en Moodle | S5 | si | |
| Sustentación del corte | S5 | si | |
| Contrato OpenAPI o AsyncAPI versionado con rutas y esquemas. | S7 | si | |
| Prueba de contrato invocada desde el pipeline y evidencia de fallo ante cambio incompatible. | S7 | si | |
| ADR de estrategia de integracion sincrona o asincrona ligado a un escenario de calidad. | S7 | si | |
| Evidencia auditable de SonarCloud: configuracion, run exitoso y URL del Quality Gate. | S7 | si | |
| Comando unico de arranque y prueba en el README. | S7 | si | |
| Contenido verificable del registro de uso de IA. | S7 | si | |
| Contrato de API en formato ejecutable, versionado y con esquemas de datos. | S7 | si | |
| Correspondencia contrato-API y versión de la API con historial en git. | S7 | si | |
| Prueba de contrato ejecutada por el pipeline y evidencia de que falla ante un cambio incompatible. | S7 | si | |
| ADR de la estrategia de integración (síncrona o asíncrona) ligado a un escenario de calidad. | S7 | si | |
| Evidencia pública de SonarCloud (scanner en el workflow, run del hash revisado y Quality Gate). | S7 | si | |
| Evidencia pública de SonarCloud (scanner, run y Quality Gate) para el hash 5b48dd0 | S6 | si | |
| Contenido de docs/propiedad_de_datos.md (tabla módulo a datos con dueño único) | S6 | si | |
| Lista de no conformidades y plan (docs/evidencia/hallazgos.md) | S6 | si | |
| Contenido de docs/ia.md (uso de IA y lo rechazado) | S6 | si | |
| Contenido del contrato con rutas y esquemas | S7 | si | |
| Correspondencia contrato–código y versión de la API | S7 | si | |
| Ejecución de la prueba de contrato en el pipeline | S7 | si | |
| Run en rojo o evidencia del cambio incompatible | S7 | si | |
| C4 nivel 2 con protocolo y formato en cada flecha | S7 | si | |
| SonarCloud con run exitoso y Quality Gate público | S7 | si | |
| Declarar URL pública y health check verificables. | S8 | sí (diferido) | Fila diferida por decisión docente: la URL se entrega por Moodle. El README ya declara la URL y la ruta `/health` existe. |
| SonarCloud sin invocación en el workflow ni URL pública del Quality Gate. | S6 | si | Falta la evidencia del contrato §8. |
| ADR 0001, 0002, 0003, 0005 y 0006 editados después de aceptarse sin reemplazo declarado. | S8 | si | Crear un ADR sucesor en vez de editar uno aceptado. |
| Punta sin commits nuevos desde S8 (`eae667e`, 2026-09-27): el periodo S9 está vacío. | S9 (prelim.) | si | Empujar la evidencia S9 antes del cierre del 2026-10-05. |
| Sin porción nueva construida con IA, sin ADR y sin extracto de `docs/ia.md` del periodo S9. | S9 (prelim.) | si | Aportar la porción real del sistema y su cadena para la evidencia S9. |
| Sin prueba que falle ante el defecto del periodo ni medición del escenario en S9. | S9 (prelim.) | si | Adjuntar run en rojo o procedimiento documentado y la medición contra umbral. |
| Sin auditoría de erosión ni decisión sobre el componente generativo. | S9 (prelim.) | si | Documentar límites de contexto/propiedad de datos y el ADR del componente generativo (o de no incorporarlo). |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Repositorio ISCOUTB/AS_202620_ROUTB visible por clon git público, rama master. |
| Estructura mínima presente | Cumple | Árbol con README, docs/arc42, adr, c4, aspectos e ia. Cadena [docs/aspectos.md:5–12](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/aspectos.md#L5-L12). |
| Estado calificado identificable | Cumple | 7c6573e68a5fdab019fab8fddfe1acb2a451cb27, 2026-10-03T18:20:32-05:00, último master ≤ cierre; HEAD coincide. |
| Nombres de ADR según la convención | Cumple | Ocho ADR con nombre NNNN-kebab-case.md; nuevos [docs/adr/0007-reserva-grupal-de-cupos.md:1–5](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0007-reserva-grupal-de-cupos.md#L1-L5) y [docs/adr/0008-no-componente-generativo.md:1–5](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0008-no-componente-generativo.md#L1-L5). |
| ADR aceptados no reescritos | No verificado | Las revisiones previas señalaban edición de ADR 0001/0002/0003/0005/0006. Se mantiene como antecedente pendiente de comprobación histórica completa en esta pasada; no se eleva texto previo no revalidado a evidencia nueva. Los nuevos ADR no sustituyen explícitamente esos registros. |
| docs/ia.md al día para la semana | Cumple | Entrada S9 del 2-oct con decisiones y rechazo: [docs/ia.md:109–119](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/ia.md#L109-L119). No se acredita todavía un registro del reto S10. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [CI final success](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/37161463477), pero [.github/workflows/ci.yml:29–67](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/.github/workflows/ci.yml#L29-L67) ejecuta pytest/build sin scanner Sonar. [README.md:91–95](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/README.md#L91-L95) contiene enlace genérico; falta cadena scanner→run→Gate de la revisión. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Barrido snapshot/histórico interrumpido por herramienta; no se presume limpio el historial ni se afirma un incidente. Debe completarse sin publicar valores sensibles. |
| Contribución de todos los integrantes | No verificado | 71 commits distribuidos en cuatro nombres de autor; aporte concentrado (60 de 71 bajo una firma). [README.md:36–41](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/README.md#L36-L41) lista miembros sin correspondencia completa con cuentas. Confirmar mapeo; no se deduce por parecido. |

## Contribución por integrante

Actualización agregada del 2026-10-06: 71 commits, cuatro nombres de autor; 60 bajo una firma. Mapeo completo persona–cuenta pendiente, sin adivinar identidades.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Keiner Enrique Mendivil Diaz | `MKeinerrr` | 53+2 (dos correos, consolidado) | | | Autor de casi todo el reto S5 |
| Diego Jose Baron Ruiz | `diegobrr999-commits` | 6 | | | C4 en S2 |
| Julian David Manjarrez Guzman | `juliandmanjarrez-tech` | 3 | | | C4 en S2 |
| Junior Jose Orozco Atencio | `junior14700` | 2 | | | Restricciones en S2 |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Fallo: ¿cómo evitan aceptar dos grupos simultáneos sin capacidad suficiente y liberar dos veces los cupos al repetir una cancelación?
- Costo: ¿qué límite de Render o Supabase agotaría primero el presupuesto cero y cómo afectaría la latencia caliente y fría?
- Medición: ante el aumento del p95 externo frente a la base, ¿qué repetirían para separar efecto de red, versión desplegada y cambio funcional?

</details>
