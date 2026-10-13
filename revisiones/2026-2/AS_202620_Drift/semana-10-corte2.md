# Segundo corte · S10 · Drift · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_Drift |
| Rama evaluada | `master` |
| Hash calificado | `04874b8744dfa345a7fa7e12775e629c410fc870` |
| Fecha del commit | 2026-10-12T14:42:40-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

E6: degradación de una fuente bajo carga

Se evalúa técnicamente el escenario declarado; no se afirma asignación docente verificada.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Sobresaliente | 1,00 / 1,00 |
| C2 · Decisión e implementación | Competente | 0,80 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Competente | 0,80 / 1,00 |
| C4 · Evolución arquitectónica trazable | Competente | 0,80 / 1,00 |
| C5 · Sustentación del reto | Calificación comunicada por el docente | 0,96 / 1,00 |

**Subtotal técnico: 3,40 / 4,00. Total consolidado C1–C5: 4,36 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,80 / 5,00**, incorporada como **C5 = 0,96 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

E6 tiene tres corridas de base y tres de fallo controladas, con respuesta mediante timeout, caché y logs. El experimento es simulado y excluye TLS y el efecto en producción. Persisten coherencia parcial y una métrica de fuentes vacía.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencias/e6-degradacion-bajo-carga.md:16–101](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/docs/evidencias/e6-degradacion-bajo-carga.md#L16-L101)
2. [docs/adr/0008-persistencia-ejecucion-y-degradacion-de-fuentes.md:99–159](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/docs/adr/0008-persistencia-ejecucion-y-degradacion-de-fuentes.md#L99-L159)
3. [backend/app/infrastructure/observability.py:9–95](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/infrastructure/observability.py#L9-L95)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** No se identificó deriva material vigente en la muestra. ADR8 sustituye explícitamente MySQL/async por memoria y consultas síncronas concurrentes; las adendas C4 actualizan las figuras históricas. No se denunció como deriva la ausencia de MySQL/cola ni la conservación de diagramas anteriores acompañados de su actualización.

**Arquitectura declarada:** Puertos y adaptadores en frontend/backend; fuentes Steam, CheapShark y PlayStation; memoria, hilos y degradación por fuente según ADR8.

**Arquitectura implementada:** GET /games/search→SearchGames→GameRepository→Combined anidado→Resilient Steam/fallback + CheapShark + PlayStation. Catálogo PlayStation busca remotamente ante miss; POST sync reemplaza memoria.

**Hallazgos materiales: 0.** No se observó deriva material en los recorridos inspeccionados; esto no acredita conformidad exhaustiva ni ejecución correcta en producción.

### Cobertura y límites de la auditoría

**Capas y dominio:** SearchGames y SyncPlayStationCatalog dependen de puertos de dominio; main es composition root, no violación por importar adaptadores.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/app/application/usecases/search_games.py:1–12](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/application/usecases/search_games.py#L1-L12) — SearchGames recibe GameRepository y delega la búsqueda por su puerto de dominio.
- [backend/app/application/usecases/sync_playstation_catalog.py:3–20](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/application/usecases/sync_playstation_catalog.py#L3-L20) — SyncPlayStationCatalog obtiene catálogo desde GameCatalogSource y lo reemplaza mediante GameCatalogRepository.
- [backend/app/main.py:120–155](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/main.py#L120-L155) — main compone CombinedGameRepository anidados con Steam/fallback, CheapShark y catálogo PlayStation.

**Persistencia:** Catálogo/repo/cachés en memoria coherentes con ADR8; no persistencia compartida prometida. Cache miss PlayStation puede llamar a fuente externa.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [docs/adr/0008-persistencia-ejecucion-y-degradacion-de-fuentes.md:97–114](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/docs/adr/0008-persistencia-ejecucion-y-degradacion-de-fuentes.md#L97-L114) — ADR8 reemplaza MySQL/actualización asíncrona por memoria y consultas síncronas en hilos, aceptando pérdida al reiniciar.
- [backend/app/infrastructure/persistence/in_memory_playstation_catalog.py:25–36](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/infrastructure/persistence/in_memory_playstation_catalog.py#L25-L36) — InMemoryPlayStationCatalog mantiene una lista en memoria y reemplaza su contenido protegido por lock.
- [backend/app/infrastructure/persistence/in_memory_playstation_catalog.py:55–71](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/infrastructure/persistence/in_memory_playstation_catalog.py#L55-L71) — Ante ausencia de coincidencias locales, el catálogo consulta search_catalog de la fuente remota si existe.

**API y autorización:** Búsqueda pública y sincronización HTTP; no se identificó requisito vigente de identidad en estas rutas. No se ensayó exposición.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/app/main.py:223–254](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/main.py#L223-L254) — GET /games/search ejecuta el caso de uso y proyecta resultados con precios y unavailable_sources.
- [backend/app/main.py:293–299](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/main.py#L293-L299) — POST /games/sync/playstation invoca directamente el caso de sincronización.

**Despliegue:** Dos contenedores laboratorio, /api con proxy, sin volúmenes; adenda C4 distingue Azure/Vercel y laboratorio.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [deploy/compose.lab.yaml:7–16](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/deploy/compose.lab.yaml#L7-L16) — Compose especifica dos servicios detrás del proxy y declara que no hay BD ni volúmenes.
- [deploy/compose.lab.yaml:41–60](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/deploy/compose.lab.yaml#L41-L60) — Compose limita cada servicio a 192 MiB y compila el frontend con /api como base pública.
- [docs/c4/contenedores.md:171–190](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/docs/c4/contenedores.md#L171-L190) — La adenda C4 describe memoria, fuentes concurrentes síncronas y coexistencia de Azure/Vercel con Dokploy.

**Asincronía:** ThreadPoolExecutor por secundaria con espera restante y shutdown(wait=False); no cola/scheduler. Primaria sin deadline propio reconocida.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/app/infrastructure/persistence/combined_game_repository.py:92–123](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/infrastructure/persistence/combined_game_repository.py#L92-L123) — Combined lanza la fuente secundaria en un hilo, calcula el tiempo restante y marca timeout/error sin esperar al hilo al cerrar.
- [docs/adr/0008-persistencia-ejecucion-y-degradacion-de-fuentes.md:143–148](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/docs/adr/0008-persistencia-ejecucion-y-degradacion-de-fuentes.md#L143-L148) — ADR8 reconoce que Steam depende de su timeout HTTP, que no hay circuito de corte y que una lista vacía no lleva aviso.

**Observabilidad:** unavailable_sources, métricas y logs del recorrido; caso de cero resultados y hilos residuales ya reconocidos como riesgos, no cierre total.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/app/main.py:268–288](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/main.py#L268-L288) — La ruta de búsqueda reúne fuentes no disponibles y registra duración/resultados en métricas y log.
- [backend/app/infrastructure/persistence/combined_game_repository.py:156–174](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/backend/app/infrastructure/persistence/combined_game_repository.py#L156-L174) — _mark_unavailable añade la fuente a los juegos presentes y emite un evento source_unavailable.
- [docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md:69–78](https://github.com/ISCOUTB/AS_202620_Drift/blob/04874b8744dfa345a7fa7e12775e629c410fc870/docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md#L69-L78) — arc42 registra como abiertos o aceptados los límites de resultados vacíos, timeout primario, hilos y memoria.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:53.940060+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`04874b8744dfa345a7fa7e12775e629c410fc870`](https://github.com/ISCOUTB/AS_202620_Drift/commit/04874b8744dfa345a7fa7e12775e629c410fc870) (2026-10-12T14:42:40-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Segundo corte S10 · avance preliminar · Drift

**Preliminar, no es cierre ni calificación final.** Cierre previsto: **2026-10-12T05:00:00Z**.

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_Drift](https://github.com/ISCOUTB/AS_202620_Drift) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `74337a3c9c2a67c807e0018fe865979b29aa330c` |
| Base S8 | `74709aa4f6b9255b4792e4aafd01be2bdae8ff0e` |
| Estado revisado | `3dee7e265eec021cbbba4af4d337e13c982df316` en `origin/master` (2026-10-04T22:03:23-05:00) |
| S9 congelada | `3dee7e265eec021cbbba4af4d337e13c982df316` · 2026-10-04T22:03:23-05:00 |
| Punta actual / S10 preliminar | `3dee7e265eec021cbbba4af4d337e13c982df316` · 2026-10-04T22:03:23-05:00 |
| Comprobación | 2026-10-06T21:25:06Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Evolución desde S5 hasta la punta

Base tomada del informe S5 publicado y resuelta por Git, sin etiquetas: `74337a3c9c2a67c807e0018fe865979b29aa330c`. En el delta S5→HEAD cambian 78 rutas no PDF (conteo de árboles; no mide mérito). Desde S5 se amplían integración de tiendas y compatibilidad, contratos, resiliencia, despliegue Azure y prototipo serverless, logs/métricas y puertos de catálogo. La evaluación del reto debe vincular un cambio concreto de esa evolución con la consigna, todavía no identificada.

## Escenario operativo asignado

No verificado. E1 de rendimiento, E2 de mantenibilidad y el Taller de Arquitecturas Serverless están documentados. Ninguno se presenta como asignación oficial del escenario operativo S10 al equipo. No se confunden resultados de S6/S8 ni taller con la consigna del corte; [docs/evidencias/Evidencia_TallerS8.md:3–30](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/Evidencia_TallerS8.md#L3-L30).

## Matriz de evidencia S10

Se omite la fila de PDF de dos páginas por exclusión docente. Quedan 12 filas observables o pendientes; este recuento no es una fórmula de nota.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Estado master identificable y anterior al cierre futuro; preliminar. |
| Despliegue accesible en el momento de la revisión | No verificado | URL Azure declarada en [docs/evidencias/evidencia_semana8.md:11–17](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/evidencia_semana8.md#L11-L17); GET /health a las 2026-10-06T21:25:06Z agotó 20.002775 s sin bytes (curl 28, HTTP 000). Esto no prueba caída permanente; accesibilidad no confirmada y flujo principal no ejecutado. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Existe E1 general y evaluación de taller serverless, sin constancia de asignación oficial S10; [docs/evidencias/Evidencia_TallerS8.md:3–30](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/Evidencia_TallerS8.md#L3-L30). |
| Línea base medida y reproducible | No verificado | La línea base de E1 es reproducible documentalmente, pero no se confirma como línea base del escenario asignado S10; [docs/evidencias/e1-linea-base.md:3–24](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/e1-linea-base.md#L3-L24). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | ADR-0004/0006 argumentan integración y despliegue; falta relacionarlos con el reto asignado y comprobar coherencia del costo; [docs/adr/0004-estrategia-de-integracion.md:17–26](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0004-estrategia-de-integracion.md#L17-L26). |
| Respuesta implementada o configurada sobre el MVP | No verificado | Hay cambios desde S5 de catálogo, compatibilidad, despliegue y puertos; no se puede atribuir respuesta al reto hasta identificar su consigna. Corrección S9 verificada en [backend/app/application/usecases/sync_playstation_catalog.py:3–20](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/backend/app/application/usecases/sync_playstation_catalog.py#L3-L20). |
| Resultado contrastado con el umbral | No verificado | E1 tiene p95 14.63→1.24 s y taller Vercel 1.66 s, pero son experimentos anteriores y no prueba identificada del reto S10; [docs/evidencias/e1-linea-base.md:15–49](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/e1-linea-base.md#L15-L49), [docs/evidencias/Evidencia_TallerS8.md:8–12](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/Evidencia_TallerS8.md#L8-L12). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Pipeline CI/deploy success, logger JSON y drift_search_latency_ms implementados; falta demostrar métrica y degradación del escenario asignado sobre despliegue. [backend/app/infrastructure/observability.py:9–74](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/backend/app/infrastructure/observability.py#L9-L74), [backend/app/main.py:129–139](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/backend/app/main.py#L129-L139). |
| Secretos protegidos | Cumple | Sin secretos reales en snapshot; no confundir id-token:write con una credencial. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | ADR-0004 describe persistencia MySQL/actualización asíncrona mientras catálogo nuevo es en memoria y la invocación es síncrona; la matriz no incorpora la corrección de puerto. [docs/adr/0004-estrategia-de-integracion.md:17–26](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0004-estrategia-de-integracion.md#L17-L26), [backend/app/application/usecases/sync_playstation_catalog.py:18–25](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/backend/app/application/usecases/sync_playstation_catalog.py#L18-L25), [docs/aspectos.md:52–58](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/aspectos.md#L52-L58). |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | La corrección confirma dirección de dependencias por inspección, pero no existe decisión previa confirmada/reemplazada con evidencia del reto S10 identificado; [docs/evidencias/evidencias_semana9.md:600–610](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/evidencias_semana9.md#L600-L610). |
| Sustentación del reto sobre el entorno desplegado | No verificado | La sustentación corresponde al docente y requiere entorno desplegado y pipeline en vivo. |

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
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público en ISCOUTB con nombre conforme, rama master; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Seis rutas presentes; arc42 no incluye sección 11, deuda de completitud aunque existe directorio. [docs/aspectos.md:48–58](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/aspectos.md#L48-L58). |
| Estado calificado identificable | Cumple | Snapshot y fecha completos en encabezado; coincide con la punta actual. |
| Nombres de ADR según la convención | No cumple | ADR-0007 usa acento y nombre no conforme al patrón; [docs/adr/0007-evaluacion-de-incorporación-coponente-generativo.md:1–7](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0007-evaluacion-de-incorporaci%C3%B3n-coponente-generativo.md#L1-L7). |
| ADR aceptados no reescritos | No verificado | El historial de ADR previos requiere confirmar inmutabilidad desde aceptación; no se declara resuelto el hallazgo anterior. Los ADR nuevos no reemplazan expresamente los reescritos. |
| docs/ia.md al día para la semana | Cumple | Registros nuevos de revisión y organización S9 con validación y alternativas descartadas por razones técnicas; [docs/ia.md:831–919](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/ia.md#L831-L919). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI y Azure deployment success en el hash, pero el scanner fue añadido y revertido antes del cierre. El workflow actual no invoca SonarCloud; [.github/workflows/ci.yml:1–54](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/.github/workflows/ci.yml#L1-L54), [sonar-project.properties:1–6](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/sonar-project.properties#L1-L6). Archivo de propiedades por sí solo no prueba análisis/Gate. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Snapshot sin credenciales reales; referencias de Actions, permisos y ejemplos de patrón. No se certificó revisión exhaustiva de todos los blobs históricos. |
| Contribución de todos los integrantes | No verificado | Ocho firmas, 384 commits agregados. Sin atribuir variantes por parecido; correspondencia completa con cuatro integrantes no verificada. Punta actual: 8 firmas y 384 commits agregados; no equivalen automáticamente a personas. |

## Actions en la punta actual

- [CI: success](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/37257975825), 2026-10-05T03:05:21Z, SHA exacto del estado indicado.
- [Build and deploy Python app to Azure Web App - drift-utb-202620: success](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/37257975779), 2026-10-05T03:05:21Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
El barrido del árbol revisado no identificó claves reales. Las coincidencias fueron permisos id-token y textos de ejemplos en documentación; no hay .env versionado. El historial completo no se certifica en esta pasada; no afecta al criterio S9 limitado al snapshot.

## Estado global del proyecto (overall)

La punta conserva la corrección de erosión de aplicación hacia infraestructura y añade funcionalidad de catálogo/UI. Los tres cambios de análisis SonarCloud fueron revertidos antes del cierre: CI y despliegue verdes no prueban scanner ni Quality Gate. Las mediciones publicadas son antiguas y se deben distinguir del trabajo S9 y del reto S10. Persiste diferencia entre la persistencia MySQL descrita y los adaptadores en memoria.

El delta S9 contiene 19 commits respecto de S8; hay 0 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Antes del cierre

- Cerrar la cadena de la corrección GameCatalogRepository hacia aspecto, ADR, prueba que falle ante erosión y evidencia del escenario.
- Distinguir mediciones de septiembre de un experimento nuevo del reto asignado, con factores de confusión y límites.
- Reintegrar scanner SonarCloud de forma verificable y aportar Quality Gate de la revisión.
- Alinear C4/arc42/ADR con la persistencia y forma de ejecución reales; usar ADR sustituto donde cambie una decisión aceptada.
- Confirmar consigna oficial S10 y demostrar el flujo principal en el despliegue antes de la sustentación.

## Tres preguntas de sustentación

1. ¿Qué devuelve la búsqueda si Steam se cae y el catálogo de PlayStation está vacío después de un reinicio?
2. ¿Cómo cambia el costo por búsqueda si se elimina la caché o se replica el backend, y qué límite gratuito se alcanza primero?
3. ¿Qué cambiarían tras repetir la medición controlando caché caliente, arranque en frío y variación de Steam?

</details>
