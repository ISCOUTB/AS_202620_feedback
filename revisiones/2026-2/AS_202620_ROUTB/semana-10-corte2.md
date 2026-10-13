# Segundo corte · S10 · ROUTB · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_ROUTB |
| Rama evaluada | `master` |
| Hash calificado | `adde017b72d73f210eef6cb48d97cdf1687f5141` |
| Fecha del commit | 2026-10-12T22:02:26-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

Resiliencia de routing/geocodificación ante fallos OSRM/Photon/Nominatim: 0HTTP500, fallback tipado, p95<3,99 s; escenario ampliado en el delta elegible.

Se evalúa técnicamente el escenario declarado; no se afirma asignación docente verificada.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Competente | 0,80 / 1,00 |
| C2 · Decisión e implementación | Competente | 0,80 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Competente | 0,80 / 1,00 |
| C4 · Evolución arquitectónica trazable | Competente | 0,80 / 1,00 |
| C5 · Sustentación del reto | Calificación comunicada por el docente | 0,80 / 1,00 |

**Subtotal técnico: 3,20 / 4,00. Total consolidado C1–C5: 4,00 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,00 / 5,00**, incorporada como **C5 = 0,80 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

El nuevo experimento incluye 50 observaciones de base y 50 de fallo, con ajuste de timeout y caché. Las pruebas simulan timeout sin esperar y no demuestran degradación de extremo a extremo real. El CI está verde, pero el paso Sonar es un echo.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencia/corte2-fallo-escenario.md:3–26](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/docs/evidencia/corte2-fallo-escenario.md#L3-L26)
2. [backend/app/shared/routing/service.py:54–64](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/shared/routing/service.py#L54-L64)
3. [backend/app/main.py:32–47](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/main.py#L32-L47)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** Las capas y servicios públicos de cupos se respetan en el flujo principal, pero la nueva operación de recalcular rutas escribe datos de Trips desde Requests. Push sigue dentro de la respuesta síncrona y el manifiesto Render contradice el timeout ratificado.

**Arquitectura declarada:** Monolito modular FastAPI con capas (no hexagonal), PostgreSQL/PostGIS, JWT y Flutter por repositorios/ApiClient. Dueño único por entidad; cupos mediante UPDATE condicional. Integración REST principal; FCM secundario no bloqueante; ADR0014 fija timeout 1,4 s.

**Arquitectura implementada:** main monta routers autenticados. PATCH requests/{id}/accept llama caso de uso, reserva cupos por trips.application y confirma; después llama recálculo de ruta y send_push inline. order_stops ejecuta UPDATE trips desde Requests. render.yaml selecciona rama Changes y timeout 3.0; config lee esa variable con default 1.4. Geocode usa Photon→Nominatim y cache; purga SQL está programada en workflow con salida exitosa si falta secreto.

**Hallazgos materiales: 3.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · Requests modifica directamente los datos de ruta cuyo dueño es Trips

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta: llamada alcanzable y SQL exacto verificados..

**Motivo de prioridad:** Media: se viola el dueño de los datos de ruta y se reparte la responsabilidad de actualización; las reservas atómicas de cupos no se consideran rotas.

**Declaración contrastada:**

- [docs/evidencia/propiedad_de_datos.md:3–14](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/docs/evidencia/propiedad_de_datos.md#L3-L14) — La matriz asigna a Trips la creación, modificación y validación del recorrido.

**Implementación contrastada:**

- [backend/app/modules/requests/infrastructure/router.py:125–133](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/modules/requests/infrastructure/router.py#L125-L133) — El router llama al caso de uso de aceptar una solicitud.
- [backend/app/modules/requests/application/manage_request.py:124–133](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/modules/requests/application/manage_request.py#L124-L133) — El caso de uso llama al recálculo después del commit de cupos.
- [backend/app/modules/requests/application/order_stops.py:53–70](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/modules/requests/application/order_stops.py#L53-L70) — Requests ejecuta UPDATE trips sobre geometría y métricas de ruta.

**Efecto y alcance:** La operación real accept_request llama refresh_trip_route_and_stop_eta y esta ejecuta UPDATE trips sobre route_geom, route_distance_m, route_duration_s y route_source. El límite de dueño único deja de proteger la actualización de rutas y la lógica de derivación queda repartida. Los cupos sí usan reserve/release públicos y no forman parte de este hallazgo.

**Corrección propuesta:** Mover la actualización de geometría y métricas de viaje a una operación pública de trips.application; Requests entrega las paradas/ids y conserva sus propias ETA. Eliminar también el import de helper privado de create_trip, o promoverlo a contrato público. Añadir regla de dependencias/escrituras entre módulos.

<a id="deriva-d2"></a>

### D2 · El envío FCM secundario permanece en el camino síncrono de la respuesta

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta sobre dependencia temporal; runtime externo no verificado..

**Motivo de prioridad:** Media: una dependencia secundaria de red entra en el presupuesto de respuesta de una operación ya confirmada; no se conoce si FCM está activo ni su latencia efectiva.

**Declaración contrastada:**

- [docs/adr/0013-notificaciones-push-fcm.md:28–29](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/docs/adr/0013-notificaciones-push-fcm.md#L28-L29) — ADR0013 exige que push no bloquee la transacción ni la respuesta.
- [docs/adr/0004-integracion-sincrona-rest.md:38–41](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/docs/adr/0004-integracion-sincrona-rest.md#L38-L41) — ADR0004 separa notificaciones secundarias del flujo principal.

**Implementación contrastada:**

- [backend/app/modules/requests/application/manage_request.py:124–149](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/modules/requests/application/manage_request.py#L124-L149) — La llamada send_push ocurre después del commit pero antes del return.
- [backend/app/modules/notifications/application/send_notification.py:79–107](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/modules/notifications/application/send_notification.py#L79-L107) — send_push espera messaging.send_each y procesa el resultado.
- [backend/app/modules/requests/infrastructure/router.py:125–133](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/modules/requests/infrastructure/router.py#L125-L133) — El router espera el caso de uso para construir la respuesta.

**Efecto y alcance:** ADR0013 exige que push no bloquee el flujo principal. El commit sucede antes y las excepciones se contienen, pero accept_request espera send_push y este llama send_each antes de retornar. Con FCM configurado, latencia/timeout de entrega se suma a la respuesta REST aunque la reserva ya esté confirmada. No se afirma que FCM esté configurado ni que haya lentitud real.

**Corrección propuesta:** Desacoplar envío después del commit mediante tarea/background worker con su propia sesión y timeout, o ratificar que es síncrono best-effort y acotar su presupuesto. Si se necesita entrega garantizada, usar outbox/reintentos; no reutilizar una sesión request cerrada en la tarea.

<a id="deriva-d3"></a>

### D3 · La configuración Render sobreescribe el timeout ratificado de 1,4 s con 3,0 s

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta sobre contradicción del manifiesto; no verificable el valor remoto actual..

**Motivo de prioridad:** Media: una recreación del despliegue con el manifiesto restaura el valor descartado y debilita una mitigación de latencia; no se ha verificado el valor real de producción.

**Declaración contrastada:**

- [docs/adr/0014-fallback-geocode-cache.md:19–31](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/docs/adr/0014-fallback-geocode-cache.md#L19-L31) — ADR0014 ratifica timeout 1.4 s y descarta 3.0 s.

**Implementación contrastada:**

- [render.yaml:21–24](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/render.yaml#L21-L24) — El manifiesto Render inyecta explícitamente 3.0 s.
- [backend/app/core/config.py:42–45](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/core/config.py#L42-L45) — Config prioriza la variable de entorno sobre el default 1.4 s.
- [backend/app/shared/geocode/service.py:98–105](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/shared/geocode/service.py#L98-L105) — El cliente HTTP utiliza el valor efectivo de config.

**Efecto y alcance:** La configuración versionada que recrea Render introduce ROUTING_TIMEOUT_SECONDS=3.0, anulando el default 1.4 que sostiene el presupuesto de ADR0014. Una recreación con ese manifiesto no conserva la mitigación documentada; el valor efectivo del panel y la latencia en producción no se verificaron.

**Corrección propuesta:** Cambiar el manifiesto a 1.4 o eliminar el override para usar el default ratificado; revisar la variable efectiva del panel con autorización y añadir prueba estática que compare configuración de despliegue y ADR/config. Medir nuevamente bajo condiciones relevantes, sin prometer el p95 a partir del valor nominal.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Leídos ADR0002, routers y casos de uso de aceptación/rechazo, servicios públicos de cupos y recálculo de ruta. Dependencia de aplicación a SQLAlchemy es aceptada; no se exige hexagonal por tener carpetas domain/application/infrastructure.

**Persistencia:** Cupos actualizados condicionalmente por Trips y misma transacción de aceptación. Se detecta escritura cruzada de geometría/distancia/duración, no de cupos. Purga y PostGIS son configuración/código, su aplicación remota no verificada.

**API y autorización:** Routers usan get_current_user/UserIdentity y verifican propiedad del conductor; auth JWT inspeccionada en topología de llamadas. Consentimiento previo/revocación declarado y caso de uso revisado. No se presume que endpoints admin futuros estén completos.

**Despliegue:** Docker, render.yaml, timeout config y ADR0014 contrastados. Rama de despliegue Changes figura en el manifiesto; auditoría exclusiva del SHA de master suministrado, no se inspecciona otra rama ni se infiere qué commit corre remoto.

**Asincronía:** FCM ocurre después del commit pero send_push se ejecuta antes de retornar el caso de uso y espera send_each. Se distingue no abortar transacción de no bloquear respuesta.

**Observabilidad:** Middleware de acceso JSON y /health estático presentes. No se infiere salud de PostGIS de health; no se validó métrica de carga ni se ejecutó workflow de purga/CI. Ausencia de secreto de purga no puede concluirse leyendo su guardia.

**Fuentes de la cobertura:**

- [docs/adr/0002-usar-arquitectura-interna-por-capas.md:15–26](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/docs/adr/0002-usar-arquitectura-interna-por-capas.md#L15-L26)
- [docs/adr/0002-usar-arquitectura-interna-por-capas.md:49–51](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/docs/adr/0002-usar-arquitectura-interna-por-capas.md#L49-L51)
- [backend/app/main.py:32–69](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/main.py#L32-L69)
- [backend/app/modules/trips/application/request_seats.py:47–73](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/modules/trips/application/request_seats.py#L47-L73)
- [docs/adr/0012-sugerencias-matching-y-orden-de-paradas.md:26–34](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/docs/adr/0012-sugerencias-matching-y-orden-de-paradas.md#L26-L34)
- [docs/adr/0011-consentimiento-y-privacidad-de-ubicacion.md:18–33](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/docs/adr/0011-consentimiento-y-privacidad-de-ubicacion.md#L18-L33)
- [backend/app/modules/users/application/location_consent.py:24–57](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/modules/users/application/location_consent.py#L24-L57)
- [backend/app/shared/geocode/service.py:193–214](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/app/shared/geocode/service.py#L193-L214)
- [.github/workflows/purge-location-data.yml:3–22](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/.github/workflows/purge-location-data.yml#L3-L22)
- [backend/Dockerfile:12–27](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/backend/Dockerfile#L12-L27)
- [render.yaml:1–24](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/adde017b72d73f210eef6cb48d97cdf1687f5141/render.yaml#L1-L24)

**Límites adicionales:** Auditoría estática nueva del SHA indicado mediante git show, sin checkout ni ejecución de código estudiantil, sin lectura de PDF, sin publicar ni cambiar notas. No se verificaron el runtime desplegado, secretos/configuración de panel, cargas, CI en vivo ni disponibilidad. Los documentos de pruebas aportan intención y alcance, no una ejecución independiente de esta auditoría.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:46:05.211820+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`adde017b72d73f210eef6cb48d97cdf1687f5141`](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/adde017b72d73f210eef6cb48d97cdf1687f5141) (2026-10-12T22:02:26-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Semana 10 · Segundo corte · ROUTB

> **Revisión preliminar**, realizada el 6 de octubre de 2026. El cierre de S10 todavía no ha ocurrido. No constituye nota aplicada ni evaluación de sustentación.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_ROUTB |
| Estado revisado | `7c6573e68a5fdab019fab8fddfe1acb2a451cb27` en `origin/master` (2026-10-03T18:20:32-05:00) |
| Rama remota principal | `origin/master` |
| Base S8 | `eae667ef4339d3e8e89461b1e5f865a08eb21d10` |
| Estado preliminar S10 / HEAD | `7c6573e68a5fdab019fab8fddfe1acb2a451cb27` · 2026-10-03T18:20:32-05:00 |
| Cierre previsto S10 | 2026-10-12T05:00:00Z |
| Observación | 2026-10-06T21:18:51Z |

## Escenario operativo asignado y alcance

**No verificado.** La reserva grupal de S9 es una decisión del equipo; el rendimiento GET /trips/ es un escenario de calidad propio. No se localizó en las fuentes inspeccionadas un enunciado oficial que los asigne como reto S10. [docs/evidencia/SEMANA9.md:9–22](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/SEMANA9.md#L9-L22), [docs/adr/0007-reserva-grupal-de-cupos.md:37–43](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0007-reserva-grupal-de-cupos.md#L37-L43) y [docs/evidencia/medicion-reserva-grupal-semana9.md:3–9](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/medicion-reserva-grupal-semana9.md#L3-L9).

Se revisaron README, ADR, arc42 y evidencias/experimentos. Un escenario de calidad elegido por el equipo no demuestra cuál le asignó el docente. Antes de valorar la respuesta del reto hay que disponer del enunciado o una referencia oficial equipo–escenario. Las evidencias S6–S9 se describen como línea base, sin recalificarlas por existir.

**PDF excluido por instrucción docente:** se omite su fila; no se leyó ningún PDF ni se cuenta como incumplimiento. La matriz conserva 12 comprobaciones. Se realizaron únicamente consultas HTTP de lectura indicadas abajo. No se ejecutó código del equipo ni se probó el flujo principal.

## Matriz de comprobación S10

| Criterio | Evidencia técnica esperada | Estado preliminar | Observaciones y evidencia |
|---|---|---|---|
| Estado de S10 identificable y anterior al cierre | Rama principal, hash y fecha; estado preliminar | Cumple | HEAD 7c6573e68a5fdab019fab8fddfe1acb2a451cb27, 2026-10-03T18:20:32-05:00, anterior al cierre futuro; preliminar. |
| Despliegue accesible en el momento de la revisión | Respuesta HTTP, tiempo y hora | Cumple | GET de lectura a https://as-202620-routb.onrender.com/health, iniciado 2026-10-06T21:18:51Z: HTTP 200 en 26,971224 s. URL en [README.md:105–106](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/README.md#L105-L106). No se probó reserva/login ni se confirmó versión desplegada; un health 200 no demuestra flujo principal. |
| Hipótesis, montaje, variables y umbral declarados | Caracterización del escenario operativo asignado | No verificado | Falta asignación S10. Umbral propio GET /trips/ en [docs/evidencia/medicion-reserva-grupal-semana9.md:3–9](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/medicion-reserva-grupal-semana9.md#L3-L9) no la acredita. |
| Línea base medida y reproducible | Herramienta, carga y procedimiento del escenario asignado | No verificado | Base externa 585,10 ms y procedimiento documentados; falta identificar que correspondan al reto asignado y a un despliegue comparable. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | ADR y respuesta al escenario asignado | No verificado | ADR-0007 fundamenta reserva grupal, pero no identifica asignación S10: [docs/adr/0007-reserva-grupal-de-cupos.md:7–65](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0007-reserva-grupal-de-cupos.md#L7-L65). |
| Respuesta implementada o configurada sobre el MVP | Cambio trazable correspondiente al reto | No verificado | Código y transacción de reserva existen; despliegue con esa versión y respuesta al reto no comprobados. La divergencia histórica está reconocida en [docs/evidencia/prueba-reserva-grupal-semana9.md:53–57](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/prueba-reserva-grupal-semana9.md#L53-L57). |
| Resultado contrastado con el umbral | Medición final comparable con línea base | No verificado | Resultado externo S9 contrastado; medición interna pendiente, sin escenario S10 confirmado: [docs/evidencia/medicion-reserva-grupal-semana9.md:27–32](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/medicion-reserva-grupal-semana9.md#L27-L32). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | Run y observabilidad del escenario asignado | No verificado | CI success y health 200; pendiente métrica y observabilidad de la asignación, pipeline bloqueante y scanner Sonar: [.github/workflows/ci.yml:29–67](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/.github/workflows/ci.yml#L29-L67). |
| Secretos protegidos | Barrido del contrato | No verificado | Barrido independiente bloqueado por herramienta; no se asume exposición ni limpieza por declaración documental. |
| C4, arc42, ADR y contratos correspondientes al MVP | Consistencia documental y trazabilidad | No verificado | Aspectos/ADR/contrato se actualizan para reserva grupal: [docs/aspectos.md:12](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/aspectos.md#L12). Falta contrastar documentación completa del MVP y estado desplegado con el escenario S10; no se recalifica la porción S9. |
| Decisión anterior confirmada o reemplazada con evidencia | Relación explícita entre medición y decisión | No verificado | ADR-0007 conserva decisión atómica de ADR-0003, pero la confirmación mediante experimento específico de S10 queda pendiente: [docs/adr/0007-reserva-grupal-de-cupos.md:37–42](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0007-reserva-grupal-de-cupos.md#L37-L42). |
| Sustentación del reto sobre el entorno desplegado | Sesión y pipeline en vivo; lo resuelve el docente | No verificado | Sustentación sobre despliegue y pipeline en vivo pendiente del docente. |

## Rúbrica del segundo corte · cinco criterios

Escala de la ficha: **0,00 · 0,60 · 0,80 · 1,00 por criterio**. No se aplica la fórmula semanal. Una comprobación pendiente conserva puntaje pendiente; no se convierte automáticamente en cero.

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Escenario asignado no identificado; escenario de rendimiento propio no sustituye la consigna. |
| Decisión e implementación | No verificado | Pendiente | Reserva grupal implementada y justificada en S9; no se acredita respuesta al reto y versión pública. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Faltan correspondencia de métrica con reto y verificación de seguridad bloqueada; no se penaliza al equipo por el entorno revisor. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Se dispone de trazabilidad S9, pendiente evolución específica S10 y correspondencia con el despliegue. |
| Sustentación del reto | Pendiente del docente | Pendiente | Pendiente de sustentación sobre el despliegue y ejecución del pipeline en vivo; no se infiere desde el repositorio. |

**Total: pendiente, no calculado.** La correspondencia con la asignación y la sustentación impiden proponer un total responsable.

## Matriz transversal · CONTRATO §11

| Criterio transversal | Estado | Evidencia y observaciones |
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

## Estado global (overall)

HEAD: `7c6573e68a5fdab019fab8fddfe1acb2a451cb27` · 2026-10-03T18:20:32-05:00. La punta coincide con S9. Cinco commits nuevos desde S8, con reserva grupal y documentación; CI final success. Health público responde 200. La evidencia del 2-oct señalaba producción 0.2.0 frente a contrato 0.3.0; en esta revisión solo se comprobó salud y no se afirma que esa divergencia esté corregida. La medición interna, Sonar y asignación S10 siguen pendientes. El barrido de seguridad quedó bloqueado por herramienta.

Recuento descriptivo: **2 Cumple, 0 No cumple, 10 No verificado, sobre 12.** No es una nota ni sustituye la rúbrica.

## Próximos pasos

Identifiquen el escenario operativo asignado antes de presentar la reserva grupal o el rendimiento como respuesta al segundo corte. Salud responde, pero aún deben demostrar el flujo sobre la versión desplegada, línea base y resultado comparables, observabilidad del reto y pipeline bloqueante. La sustentación permanece pendiente.

## Tres preguntas para la sustentación

1. Fallo: ¿cómo evitan aceptar dos grupos simultáneos sin capacidad suficiente y liberar dos veces los cupos al repetir una cancelación?
2. Costo: ¿qué límite de Render o Supabase agotaría primero el presupuesto cero y cómo afectaría la latencia caliente y fría?
3. Medición: ante el aumento del p95 externo frente a la base, ¿qué repetirían para separar efecto de red, versión desplegada y cambio funcional?

## Delta arquitectónico desde el primer corte

Base publicada de S5: `343bb9d6565c1a81bdad542efde3fbb56b07e2ca`; comparación git contra HEAD `7c6573e68a5fdab019fab8fddfe1acb2a451cb27`: 237 rutas cambiadas, de ellas 14 en ADR/arc42/C4 (sin leer PDF). Se inspeccionaron las decisiones, contratos, código y evidencia citados en las filas. El delta sirve para examinar evolución y consistencia del MVP, no para recalificar las entregas S6–S9. La correspondencia con el escenario asignado S10 sigue pendiente.

</details>
