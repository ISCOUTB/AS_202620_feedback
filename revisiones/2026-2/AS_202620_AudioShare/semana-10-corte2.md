# Segundo corte · S10 · AudioShare · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_AudioShare |
| Rama evaluada | `master` |
| Hash calificado | `1da287c662986033871ef0e044ed29894b978593` |
| Fecha del commit | 2026-10-12T17:35:29-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

Escenario documentado

Se evalúa el escenario declarado; asignación docente no verificada.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Competente | 0,80 / 1,00 |
| C2 · Decisión e implementación | Básico | 0,60 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Competente | 0,80 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Calificación comunicada por el docente | 0,80 / 1,00 |

**Subtotal técnico: 2,80 / 4,00. Total consolidado C1–C5: 3,60 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,00 / 5,00**, incorporada como **C5 = 0,80 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

El protocolo de sincronización incorpora medición y mutación, pero la comparación mezcla relojes. Flutter aún no integra /time ni ACK, y la arquitectura conserva desalineaciones.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencia-a01-ec01.md:8–64](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docs/evidencia-a01-ec01.md#L8-L64)
2. [docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md:3–7](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md#L3-L7)
3. [.github/workflows/ci.yml:1–23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/.github/workflows/ci.yml#L1-L23)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** Tres desalineaciones confirmadas: propiedad de estado ya reconocida y dos vistas documentales rezagadas. Audio físico, auth y consumo Flutter del stream están declarados pendientes; no se penalizan como arquitectura futura incumplida. Se excluyen los tres commits posteriores al corte.

**Arquitectura declarada:** Monolito modular Session/Sync/Audio, SQLite backend, Flutter por HTTP/JSON y distribución NDJSON.

**Arquitectura implementada:** createApp conecta SessionApplication→SQLiteRoomRepository; /play invoca SyncCoordinator y Session; Flutter ViewModel→RoomRepository→ApiClient. Stream y medición ACK en backend; audio cliente simulado.

**Hallazgos materiales: 3.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · C4 omite Flutter y conserva solo la vista del cliente web legado

**Naturaleza:** documentación desactualizada. **Prioridad:** Media. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** La vista principal omite Flutter y atribuye recepción de eventos al único cliente representado; el web legado sí existe como fallback.

**Declaración contrastada:**

- [docs/c4/C4 Nivel 2 - Contenedores.mmd:23–30](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docs/c4/C4%20Nivel%202%20-%20Contenedores.mmd#L23-L30) — C4 describe exclusivamente WebClient servido desde public/ y AppServer con API REST/NDJSON.
- [docs/c4/C4 Nivel 2 - Contenedores.mmd:44–47](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docs/c4/C4%20Nivel%202%20-%20Contenedores.mmd#L44-L47) — C4 atribuye al cliente web llamadas REST y recepción de eventos NDJSON, con SQLite detrás del servidor.

**Implementación contrastada:**

- [src/app.ts:74–84](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/app.ts#L74-L84) — Express elige build/web cuando se solicita Flutter y existe index.html; en otro caso conserva public/ como fallback.
- [src/server.ts:1–5](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/server.ts#L1-L5) — El bootstrap llama createApp con serveFlutterWeb: true.
- [lib/features/session/data/repositories/room_repository.dart:42–58](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/lib/features/session/data/repositories/room_repository.dart#L42-L58) — RoomRepository consulta salas por GET y realiza play/pause por POST seguido de otra consulta GET.
- [README.md:128–134](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/README.md#L128-L134) — README distingue cliente Flutter implementado, audio simulado y consumo NDJSON/control de acceso pendientes.

**Efecto y alcance:** La vista incompleta de las alternativas de cliente no permite distinguir el fallback public/ del cliente Flutter preferido por el bootstrap ni qué alternativa consume actualmente NDJSON.

**Corrección propuesta:** Actualizar L2 con Flutter y web legado como alternativas; marcar NDJSON, /time y ACK como pendientes de integrar en Flutter. No presentar ADR-0007 propuesto como decisión ya aceptada.

<a id="deriva-d2"></a>

### D2 · Session sigue escribiendo el estado que el diseño asigna a Sync

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** Es una violación de propiedad reconocida explícitamente por el propio diseño, no un hallazgo basado en nombres de carpetas.

**Declaración contrastada:**

- [docs/contextos-delimitados.md:122–129](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docs/contextos-delimitados.md#L122-L129) — El mapa de contextos califica la copia del estado Sync en Session como NC-10 y propone conservar solo referencias.

**Implementación contrastada:**

- [src/app.ts:212–215](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/app.ts#L212-L215) — play toma el evento de Sync y entrega su startAt a sessions.startPlayback.
- [src/modules/session/application/session-application.ts:29–40](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/modules/session/application/session-application.ts#L29-L40) — SessionApplication.startPlayback modifica la reproducción de la sala mediante el repositorio de Session.
- [src/modules/session/infrastructure/persistence/sqlite-room-repository.ts:132–145](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/modules/session/infrastructure/persistence/sqlite-room-repository.ts#L132-L145) — El repositorio SQLite de Session actualiza status, playback_state y start_at dentro de la tabla rooms.

**Efecto y alcance:** La evolución del estado de sincronización exige modificar también el modelo y persistencia de Session; existen dos representaciones acopladas.

**Corrección propuesta:** Cerrar NC-10: hacer a Sync dueño del estado persistido y publicar una interfaz que Session consulte, o registrar formalmente un modelo compartido deliberado con responsabilidades y pruebas. La no conformidad ya estaba reconocida; no se presenta como descubrimiento nuevo.

<a id="deriva-d3"></a>

### D3 · La plataforma principal de arc42/ADR no coincide con la guía operativa vigente

**Naturaleza:** documentación desactualizada. **Prioridad:** Baja. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** El laboratorio ya era alternativa permitida; se trata de reconciliar cuál entorno es principal, no de un despliegue inválido.

**Declaración contrastada:**

- [docs/arc42/src/07_deployment_view.adoc:16–18](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docs/arc42/src/07_deployment_view.adoc#L16-L18) — arc42 identifica Azure Container Apps como entorno público principal y el laboratorio como alternativa.

**Implementación contrastada:**

- [README.md:185–193](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/README.md#L185-L193) — README identifica Dokploy como plataforma productiva que ejecuta docker-compose.yml.
- [docker-compose.yml:10–23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docker-compose.yml#L10-L23) — Compose materializa una sola API con DATABASE_FILE y volumen persistente local.

**Efecto y alcance:** Una persona que siga arc42 puede preparar Azure cuando README guía a Dokploy.

**Corrección propuesta:** Registrar Dokploy como entorno principal actual, conservar Azure como alternativa si sigue vigente y enlazar la decisión de transición sin reescribir la historia.

### Cobertura y límites de la auditoría

**Capas y dominio:** Composición y propiedad Session/Sync/Audio; se siguió /play hasta escritura SQLite.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [src/app.ts:50–57](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/app.ts#L50-L57) — createApp instancia SessionApplication con SQLiteRoomRepository y mantiene audio, streams y mediciones en memoria.
- [src/app.ts:212–223](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/app.ts#L212-L223) — La ruta play obtiene startAt de SyncCoordinator, lo pasa a Session y distribuye los eventos a los receptores conectados.

**Persistencia:** SQLite a través del repositorio de Session; volumen Compose.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [src/modules/session/infrastructure/persistence/sqlite-room-repository.ts:132–145](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/modules/session/infrastructure/persistence/sqlite-room-repository.ts#L132-L145) — El repositorio SQLite de Session actualiza status, playback_state y start_at dentro de la tabla rooms.
- [docker-compose.yml:17–23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docker-compose.yml#L17-L23) — Compose configura DATABASE_FILE y monta audioshare-data en /app/data.

**API y autorización:** REST de salas y controles; control de acceso explícitamente pendiente. ADR7 propuesto no se trata como obligación aceptada.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [README.md:128–134](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/README.md#L128-L134) — README distingue cliente Flutter implementado, audio simulado y consumo NDJSON/control de acceso pendientes.
- [docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md:3–7](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md#L3-L7) — ADR7 figura como propuesto y complementa ADR5 sin reemplazarlo.
- [docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md:64–68](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md#L64-L68) — ADR7 reconoce que Flutter todavía no consulta /time ni envía ACK y que la prueba simulada excluye la salida física de audio.

**Despliegue:** Bootstrap Express, Flutter estático y Compose con un servicio/volumen.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [src/app.ts:74–84](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/app.ts#L74-L84) — Express elige build/web cuando se solicita Flutter y existe index.html; en otro caso conserva public/ como fallback.
- [docker-compose.yml:10–29](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docker-compose.yml#L10-L29) — Compose define un servicio API con SQLite en volumen nombrado y healthcheck HTTP.

**Asincronía:** NDJSON realmente emitido; Flutter solo hace REST y snapshots.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [src/app.ts:137–165](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/app.ts#L137-L165) — La ruta stream valida sala/receptor y abre una respuesta application/x-ndjson.
- [src/app.ts:217–223](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/app.ts#L217-L223) — El servidor envía el evento de sincronización y el paquete de audio a cada cliente registrado en el stream.
- [lib/features/session/presentation/viewmodels/session_view_model.dart:49–75](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/lib/features/session/presentation/viewmodels/session_view_model.dart#L49-L75) — El ViewModel inicia/pausa AudioService y actualiza un snapshot de sincronización a partir del resultado REST.

**Observabilidad:** Contadores y ACK/sync report implementados; no son medición de audio físico.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [src/app.ts:366–390](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/app.ts#L366-L390) — El endpoint ACK convierte el instante al reloj servidor, registra el arranque y actualiza métricas de dispersión.
- [src/app.ts:445–457](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/src/app.ts#L445-L457) — Express expone /health con la lista de módulos y /metrics mediante metricsHandler.
- [docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md:64–68](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1da287c662986033871ef0e044ed29894b978593/docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md#L64-L68) — ADR7 reconoce que Flutter todavía no consulta /time ni envía ACK y que la prueba simulada excluye la salida física de audio.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:48.697435+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`240605533aac563c80a1cab648d6ce7dcea2f6f1`](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/240605533aac563c80a1cab648d6ce7dcea2f6f1) (2026-10-13T01:49:15-05:00). Hay **3 commits posteriores al cierre**. Se registran como actividad posterior, sin revisión sustantiva ni modificación de los puntajes congelados.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Segundo corte S10 · avance preliminar · AudioShare

**Preliminar, no es cierre ni calificación final.** Cierre previsto: **2026-10-12T05:00:00Z**.

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_AudioShare](https://github.com/ISCOUTB/AS_202620_AudioShare) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `cb65d13134b220c020d0facaa00d0a779d584245` |
| Base S8 | `e4789d887fe59b2ace65bd1d2680f79758db5b54` |
| Estado revisado | `6a03a9718776420d46ed40f7addc5667206908cd` en `origin/master` (2026-10-04T23:15:57-05:00) |
| S9 congelada | `6a03a9718776420d46ed40f7addc5667206908cd` · 2026-10-04T23:15:57-05:00 |
| Punta actual / S10 preliminar | `6a03a9718776420d46ed40f7addc5667206908cd` · 2026-10-04T23:15:57-05:00 |
| Comprobación | 2026-10-06T21:16:50Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Evolución desde S5 hasta la punta

Base tomada del informe S5 publicado y resuelta por Git, sin etiquetas: `cb65d13134b220c020d0facaa00d0a779d584245`. En el delta S5→HEAD cambian 61 rutas no PDF (conteo de árboles; no mide mérito). Desde S5 se incorporaron contratos OpenAPI/AsyncAPI, cliente Flutter, despliegue, logs y métricas; en S9 la implementación productiva no cambió, pero sí documentación y una prueba. El avance del corte se examina sobre esa evolución completa y no solo S8→S9.

## Escenario operativo asignado

No verificado. Se buscaron asignación/escenario operativo/reto S10 en README, ADR, escenarios y documentos de evidencias. EC-01 (sincronización ≤100 ms) y EC-02 (≤200 ms) son objetivos generales del producto, no prueba de asignación docente; [README.md:226–234](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L226-L234). Hace falta la consigna específica del equipo.

## Matriz de evidencia S10

Se omite la fila de PDF de dos páginas por exclusión docente. Quedan 12 filas observables o pendientes; este recuento no es una fórmula de nota.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master identificada en el encabezado, anterior al cierre futuro; la revisión es preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://audioshare.iscoutb.dev/health: HTTP 200, 5.847381 s, 2026-10-06T21:16:50Z; cuerpo JSON status=ok. URL declarada en [README.md:151–159](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L151-L159). Solo accesibilidad/health: flujo principal no probado. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Hay EC-01/EC-02 genéricos, pero no asignación oficial del escenario S10; [README.md:226–234](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L226-L234). |
| Línea base medida y reproducible | No verificado | No hay línea base del reto identificada; el test de constantes no la sustituye; [tests/sync-a01.test.ts:5–18](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/tests/sync-a01.test.ts#L5-L18). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | ADR-0005 es de sincronización y ADR-0004 sigue refiriéndose a Azure, mientras README declara Dokploy; no se acredita respuesta al reto asignado; [docs/adr/0005 Validación-sincronización-inicial.md:17–49](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0005%20Validaci%C3%B3n-sincronizaci%C3%B3n-inicial.md#L17-L49), [README.md:185–193](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L185-L193). |
| Respuesta implementada o configurada sobre el MVP | No verificado | Desde S5 se añadieron Flutter, contratos, despliegue y observabilidad. En S9 no hay cambio productivo; falta identificar cuál de los cambios desde S5 responde al escenario asignado o demostrar por qué no cambiarlo. |
| Resultado contrastado con el umbral | No verificado | EC-01/EC-02 sin resultado real contrastado con umbral; falta conocer el reto S10; [README.md:203–210](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L203-L210). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | Flutter continúa en failure; hay health y logger JSON, pero la métrica solo es proxy de actividad, no mide desfase y falta vínculo con reto asignado; [src/shared/metrics.ts:1–13](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/src/shared/metrics.ts#L1-L13), [src/shared/logger.ts:1–31](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/src/shared/logger.ts#L1-L31). |
| Secretos protegidos | Cumple | No se encontraron secretos reales en el árbol de la punta. Ver alcance del barrido. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | README declara Dokploy pero arc42 §7/ADR-0004 representan Azure y la matriz sigue sin la decisión nueva; [README.md:185–193](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L185-L193), [docs/arc42/src/07_deployment_view.adoc:13–24](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/arc42/src/07_deployment_view.adoc#L13-L24), [docs/aspectos.md:38–43](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/aspectos.md#L38-L43). |
| Decisión anterior confirmada o reemplazada con evidencia | No cumple | ADR-0005 complementa decisiones sin confirmación experimental; no hay medición del sistema que confirme o reemplace la anterior; [docs/adr/0005 Validación-sincronización-inicial.md:61–78](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0005%20Validaci%C3%B3n-sincronizaci%C3%B3n-inicial.md#L61-L78). |
| Sustentación del reto sobre el entorno desplegado | No verificado | Se resuelve por el docente en sustentación sobre despliegue y ejecución de pipeline en vivo. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | No se localizó evidencia de asignación oficial del escenario; no se sustituye por un escenario genérico. |
| Decisión e implementación | No verificado | Pendiente | No se puede juzgar la respuesta al escenario asignado hasta identificarlo. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Hay evidencia técnica parcial descrita en la matriz; falta vincularla con el escenario asignado y verificar la operación completa. |
| Evolución arquitectónica trazable | No verificado | Pendiente | La coherencia documental se informa en la matriz; falta demostrar la evolución específica exigida por el reto. |
| Sustentación del reto | Pendiente del docente | Pendiente | Sustentación sobre el entorno desplegado y pipeline en vivo; no se puntúa desde el repositorio. |

Escala aplicable: 0,00 / 0,60 / 0,80 / 1,00 por criterio. **No se calcula total mientras haya criterios pendientes.** No se usa la fórmula semanal. Cualquier nivel es propuesta al docente; la sustentación queda a su cargo.

## Matriz transversal · punta actual

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público por HTTPS y rama remota master; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Presentes README, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md; [docs/aspectos.md:36–43](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/aspectos.md#L36-L43). arc42 usa AsciiDoc, desviación de formato frente a Markdown. |
| Estado calificado identificable | Cumple | Hash y fecha completos en el encabezado, elegidos por git log --until sobre origin/master. |
| Nombres de ADR según la convención | No cumple | El nombre [docs/adr/0005 Validación-sincronización-inicial.md:1–7](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0005%20Validaci%C3%B3n-sincronizaci%C3%B3n-inicial.md#L1-L7) contiene espacio y acentos; no pasa NNNN-kebab-case. |
| ADR aceptados no reescritos | No cumple | ADR-0001 ya estaba aceptado en 924d133 y fue modificado en 354f1f5: se verificaron ambas versiones y el diff. El texto actual solo dice complementado, sin preservar la versión aceptada mediante reemplazo; [docs/adr/0001-usar-monolito-modular.md:1–8](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0001-usar-monolito-modular.md#L1-L8). |
| docs/ia.md al día para la semana | No cumple | Hubo cambios de S9, pero el registro específico no separa una salida rechazada con motivo técnico y mantiene Estado «semana 7»; [docs/ia.md:112–112](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L112-L112), [docs/ia.md:363–389](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L363-L389). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Scanner configurado en [sonar-project.properties:1–5](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/sonar-project.properties#L1-L5) y [.github/workflows/ci.yml:18–23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/.github/workflows/ci.yml#L18-L23); la organización configurada no es isco-utb. CI success, Flutter failure en el hash. Falta análisis público y Quality Gate atribuibles a esta revisión. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Sin credenciales reales en el árbol: coincidencias solo con referencias a secrets de Actions. Barrido histórico completo no concluyó; no se certifica el historial. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas de autor visibles, distribuidas en el historial. No se inventa la correspondencia entre cuentas y los cuatro integrantes; falta mapa verificable para acreditar a todas las personas. Punta actual: 4 firmas y 206 commits agregados; no equivalen automáticamente a personas. |

## Actions en la punta actual

- [Flutter: failure](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/37262748991), 2026-10-05T04:16:00Z, SHA exacto del estado indicado.
- [Publicar imagen: success](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/37262748932), 2026-10-05T04:16:00Z, SHA exacto del estado indicado.
- [CI: success](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/37262748924), 2026-10-05T04:16:00Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Barrido del snapshot completo de texto, incluidos docs y ejemplos: las coincidencias fueron referencias a secretos del almacén de Actions, no valores. No hay .env versionado. El recorrido histórico con git log -S no terminó por cancelación del entorno: la fila transversal conserva No verificado.

## Estado global del proyecto (overall)

La punta coincide con S9. Se incorporaron dos ADR y una prueba adicional, pero esta no valida la sincronización real. La aplicación responde al health check actual, lo cual no demuestra flujo de audio ni identidad entre despliegue y commit. La documentación reconoce audio simulado y mediciones pendientes. CI de backend e imagen están en verde; Flutter sigue en rojo. La plataforma declarada cambió a Dokploy sin alinear completamente la vista de despliegue y ADR.

El delta S9 contiene 9 commits respecto de S8; hay 0 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Antes del cierre

- Sustituir la prueba de constantes por una que invoque la lógica real y falle al introducir un defecto de sincronización; registrar procedimiento y resultado.
- Completar la cadena A-01 hacia ADR-0005, código exacto, prueba y medición reproducible.
- Aportar mediciones de receptores y comparación con umbral, sin presentar un ejemplo sintético como experimento.
- Localizar la consigna oficial S10 y definir línea base, hipótesis, variables y montaje.
- Corregir Flutter CI, evidenciar SonarCloud/Quality Gate del hash y alinear Dokploy con ADR/C4/arc42.
- Hacer específica la auditoría de erosión y la verificación de dependencias; registrar rechazo técnico propio de la entrega.

## Tres preguntas de sustentación

1. ¿Qué ocurriría si un receptor recibe startAt después del instante programado y qué prueba real detectaría el desfase?
2. ¿Qué consumo y persistencia necesita Dokploy y quién asume el costo al salir del recurso académico gratuito?
3. La prueba actual produce 40 ms por construcción: ¿qué cambiarían al medir relojes, red y reproducción física reales?

</details>
