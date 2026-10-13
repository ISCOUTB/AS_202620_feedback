# Segundo corte · S10 · mapsutb · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_mapsutb |
| Rama evaluada | `master` |
| Hash calificado | `1b296a37c575a751e99df1a1b288d70efba03d56` |
| Fecha del commit | 2026-10-02T12:58:33-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

Escenario2: ruteo sin conexión y ruta mostrada ≤5 s

Se valora el escenario documentado disponible; no se afirma asignación docente verificada ni nueva entrega específica S10. Evidencias previas se usan como estado del repositorio, no se traslada ni promedia su nota anterior.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Básico | 0,60 / 1,00 |
| C2 · Decisión e implementación | Competente | 0,80 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Básico | 0,60 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Calificación comunicada por el docente | 0,80 / 1,00 |

**Subtotal técnico: 2,60 / 4,00. Total consolidado C1–C5: 3,40 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,00 / 5,00**, incorporada como **C5 = 0,80 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

Dijkstra, sus alternativas y costo están justificados e implementados. Las medidas son posteriores y no identifican una línea base anterior. Logs y sonda aportan observabilidad parcial; C4 aún declara ausente MapaRepository. No se mezcla la línea base de caché con la de ruteo.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencia-s9.md:50–62](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L50-L62)
2. [docs/adr/0013-ruteo-dijkstra-grafo-propio.md:17–59](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0013-ruteo-dijkstra-grafo-propio.md#L17-L59)
3. [docs/c4/C2.md:39–50](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/c4/C2.md#L39-L50)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** El monolito Flutter implementa ruteo local con Dijkstra y mapa OSM conforme a ADR0012/0013. Las principales diferencias son documentales: vistas antiguas todavía muestran Google Maps SDK y GPS real aunque el punto de entrada conecta un generador simulado.

**Arquitectura declarada:** Una app Flutter, sin backend propio; Repository para JSON/grafo, Adapter para servicios externos y Observer de ubicación. ADR0012 reemplaza Google Maps SDK por flutter_map/OSM; ADR0013 concreta Dijkstra offline. Hosting web Firebase y sondas externas.

**Arquitectura implementada:** main.dart compone ZonaRepositoryLocal y MapaRepositoryLocal, crea UbicacionServiceSimulado y los inyecta en MapaScreen. La pantalla carga grafo/zonas, escucha el stream y llama ServicioRuteo; MapaWidget solicita teselas OSM. Geocoding/Static Maps/Analytics solo se componen si existen defines; no hay base de datos propia.

**Hallazgos materiales: 2.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · Las vistas principales no incorporan por completo los ADR de OSM y ruteo

**Naturaleza:** documentación desactualizada. **Prioridad:** Baja. **Confianza:** Alta..

**Motivo de prioridad:** Baja: son vistas y alcance desactualizados; las decisiones nuevas están formalizadas y el código las sigue.

**Declaración contrastada:**

- [docs/arc42/05_building_block_view.md:18–29](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/arc42/05_building_block_view.md#L18-L29) — Arc42 conserva el SDK Google como mapa base embebido.
- [README.md:53–57](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/README.md#L53-L57) — README afirma que routing solo es un molde pendiente.

**Implementación contrastada:**

- [docs/adr/0012-mapa-base-flutter-map-osm.md:5–9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0012-mapa-base-flutter-map-osm.md#L5-L9) — ADR0012 reemplaza explícitamente la elección Google Maps SDK.
- [lib/adapters/mapa_widget.dart:95–110](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/adapters/mapa_widget.dart#L95-L110) — MapaWidget realmente carga teselas OSM con flutter_map.
- [lib/routing/servicio_ruteo.dart:28–53](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/servicio_ruteo.dart#L28-L53) — ServicioRuteo implementa rutas por grafo e ids de zona.
- [lib/features/mapas_ruteo/presentation/screens/mapa_screen.dart:113–120](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/features/mapas_ruteo/presentation/screens/mapa_screen.dart#L113-L120) — La pantalla llama al cálculo de ruta durante su flujo real.

**Efecto y alcance:** Arc42 sigue dibujando un SDK Google embebido y el README dice que routing solo contiene .gitkeep, aunque el mapa solicita teselas OSM y Dijkstra está implementado y llamado. Esto cambia dependencias operativas y alcance disponible, no significa que la elección OSM sea deriva de implementación.

**Corrección propuesta:** Actualizar README/C4/arc42 en conjunto: OSM para mapa base, Dijkstra actual y tour aún pendiente. Dibujar por separado Geocoding/Static Maps opcionales; separar cálculo offline de carga de teselas.

<a id="deriva-d2"></a>

### D2 · La vista de ejecución describe GPS actual, pero el arranque compone ubicación simulada

**Naturaleza:** documentación desactualizada. **Prioridad:** Media. **Confianza:** Alta: composición y generación del stream verificadas..

**Motivo de prioridad:** Media: la vista presenta como posición actual del usuario un flujo que realmente parte de un simulador; afecta la interpretación funcional del origen de las rutas, sin afirmar que GPS real ya sea obligación del incremento.

**Declaración contrastada:**

- [docs/arc42/06_runtime_view.md:36–43](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/arc42/06_runtime_view.md#L36-L43) — La secuencia representa lecturas reales del sensor GPS.
- [docs/arc42/06_runtime_view.md:57–64](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/arc42/06_runtime_view.md#L57-L64) — La explicación atribuye el origen de ruta a posición actual del usuario.

**Implementación contrastada:**

- [lib/main.dart:47–51](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/main.dart#L47-L51) — El punto de composición instancia UbicacionServiceSimulado.
- [lib/services/ubicacion_service.dart:15–25](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/services/ubicacion_service.dart#L15-L25) — El adaptador declara que no usa GPS real.
- [lib/services/ubicacion_service.dart:41–51](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/services/ubicacion_service.dart#L41-L51) — Timer genera desplazamientos aleatorios sobre un punto fijo.
- [lib/features/mapas_ruteo/presentation/screens/mapa_screen.dart:55–63](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/features/mapas_ruteo/presentation/screens/mapa_screen.dart#L55-L63) — MapaScreen usa ese stream como posición.

**Efecto y alcance:** El flujo documentado recibe posición del sensor; el flujo ejecutable emite coordenadas aleatorias alrededor de un punto fijo cada segundo y usa ese stream para origen de rutas. La interfaz no demuestra ubicación real por tener Observer. La implementación se identifica como simulada en código, por lo que se reporta como desajuste de la vista actual, no como obligación de implementar una función futura.

**Corrección propuesta:** Marcar el sensor/GPS real como objetivo y mostrar el simulador en la vista actual; identificar visiblemente modo demostración en UI. Cuando se integre GPS, sustituir el adaptador y probar permisos, ausencia de señal y precisión sin alterar el contrato Observer.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Se siguió main→MapaScreen→repositorios/ServicioRuteo→MapaWidget. No se exige DDD/hexagonal; los patrones elegidos sí son reconocibles. Ruteo conoce ids de zona y grafo, no importa Zona.

**Persistencia:** Assets locales y caches en memoria; no existe obligación actual de BD remota. No se valida precisión del grafo ni del levantamiento.

**API y autorización:** APIs externas condicionales y contrato OpenAPI de consumidor presentes; no API backend propia ni auth interna que exigir. README advierte que dart-define queda embebido, por lo que no se inventa garantía de secretos ocultos.

**Despliegue:** Workflow build web/Firebase, health estático generado y configuración de hosting revisados. Docker/nginx es alternativa de laboratorio, no sustitución silenciosa del hosting. No se abre producción.

**Asincronía:** Stream basado en Timer simula Observer; Dijkstra local no necesita red. Analytics se invoca con ignore() desde selección de destino; no hay broker implícito.

**Observabilidad:** Logs de ruta_calculada/ruta_mostrada revisados; README declara sonda de disponibilidad del health, no disponibilidad del algoritmo/GPS. Workflow revisado estáticamente; cifras, runtime de sensor y resultados CI no verificados.

**Fuentes de la cobertura:**

- [docs/adr/0013-ruteo-dijkstra-grafo-propio.md:25–36](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0013-ruteo-dijkstra-grafo-propio.md#L25-L36)
- [lib/main.dart:47–68](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/main.dart#L47-L68)
- [lib/main.dart:78–97](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/main.dart#L78-L97)
- [lib/features/mapas_ruteo/presentation/screens/mapa_screen.dart:66–69](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/features/mapas_ruteo/presentation/screens/mapa_screen.dart#L66-L69)
- [lib/adapters/mapa_widget.dart:20–22](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/adapters/mapa_widget.dart#L20-L22)
- [lib/routing/servicio_ruteo.dart:56–76](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/servicio_ruteo.dart#L56-L76)
- [README.md:82–102](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/README.md#L82-L102)
- [README.md:158–166](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/README.md#L158-L166)
- [.github/workflows/deploy.yml:33–57](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/.github/workflows/deploy.yml#L33-L57)

**Límites adicionales:** Auditoría estática nueva del SHA indicado mediante git show, sin checkout ni ejecución de código estudiantil, sin lectura de PDF, sin publicar ni cambiar notas. No se verificaron el runtime desplegado, secretos/configuración de panel, cargas, CI en vivo ni disponibilidad. Los documentos de pruebas aportan intención y alcance, no una ejecución independiente de esta auditoría.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:46:04.996618+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`1b296a37c575a751e99df1a1b288d70efba03d56`](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/1b296a37c575a751e99df1a1b288d70efba03d56) (2026-10-02T12:58:33-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Semana 10 · Segundo corte · mapsutb

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_mapsutb |
| Estado revisado | `1b296a37c575a751e99df1a1b288d70efba03d56` en `origin/master` (2026-10-02T12:58:33-05:00) |
| Rama remota principal | `origin/master` |
| Observación | 2026-10-06T21:31:50.415821+00:00 |
| Punta revisada para S10 | `1b296a37c575a751e99df1a1b288d70efba03d56` (2026-10-02T12:58:33-05:00) |
| S9 congelado, solo como línea base | `1b296a37c575a751e99df1a1b288d70efba03d56` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** Se localizaron Escenario 2 de ruteo, Escenario 7 de reversión y el taller con necesidad de reversión. Ninguno acredita por sí mismo el escenario operativo asignado específicamente al corte S10. Fuente o búsqueda: [docs/evidencia-s9.md:50-62](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L50-L62) y [docs/adr/0015-cache-del-sitio-revalidar.md:13-24](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L13-L24); búsqueda en README, ADR y docs/taller-despliegue.md. La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `e8bad4c286e5b985b324234b644e3b1fe961b626`: el delta hasta esta punta modifica 117 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master 1b296a37c575a751e99df1a1b288d70efba03d56; preliminar anterior al cierre futuro. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://mapsutb.web.app/health.json: HTTP 200, 7.064 s; inicio 2026-10-06T21:25:41Z. JSON declara commit 1b296a37c575a751e99df1a1b288d70efba03d56 y despliegue 2026-10-02T17:59:58Z. HEAD / devuelve 200. Es health estático; no demuestra ejecución de ruteo/GPS en navegador. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Se localizaron Escenario 2 de ruteo, Escenario 7 de reversión y el taller con necesidad de reversión. Ninguno acredita por sí mismo el escenario operativo asignado específicamente al corte S10. [docs/evidencia-s9.md:50-62](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L50-L62) y [docs/adr/0015-cache-del-sitio-revalidar.md:13-24](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L13-L24); búsqueda en README, ADR y docs/taller-despliegue.md |
| Línea base medida y reproducible | No verificado | Existen mediciones de cálculo/pantalla y caché: [docs/evidencia-s9.md:50-62](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L50-L62) y [docs/adr/0015-cache-del-sitio-revalidar.md:13-24](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L13-L24). Falta fijar cuál es la línea base del reto asignado S10. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0013-ruteo-dijkstra-grafo-propio.md:17-59](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0013-ruteo-dijkstra-grafo-propio.md#L17-L59) y [docs/adr/0015-cache-del-sitio-revalidar.md:26-55](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L26-L55) contienen alternativas y costo; falta asignación para valorar pertinencia S10. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [lib/routing/servicio_ruteo.dart:56-101](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/servicio_ruteo.dart#L56-L101) y [firebase.json:8-16](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/firebase.json#L8-L16) implementan respuestas reales a necesidades detectadas; no se presume que sean el reto asignado. |
| Resultado contrastado con el umbral | No verificado | Cálculo/pantalla documentados; no hay contraste atribuible al reto S10 confirmado. HEAD / observado 2026-10-06T21:25:55Z devuelve Cache-Control: max-age=3600, aunque [docs/adr/0015-cache-del-sitio-revalidar.md:26-35](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L26-L35) declara revalidación HTML/JS/JSON: comprobar por ruta la política efectiva; no se verificó el JS en esta pasada. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Health declara mismo hash; [lib/routing/servicio_ruteo.dart:62-75](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/servicio_ruteo.dart#L62-L75) produce evento estructurado de cálculo y [.github/workflows/ci.yml:44-64](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/.github/workflows/ci.yml#L44-L64) pipeline/gate. Run actual, métrica del reto y barrido independiente pendientes. |
| Secretos protegidos | No verificado | El equipo declara su barrido en [docs/evidencia-s9.md:104-109](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L104-L109). El barrido independiente agregado fue cancelado por la herramienta y no se completó en el único reintento; no hay base para certificar limpieza integral ni para atribuir exposición al equipo. La comprobación permanece pendiente del revisor. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/c4/C2.md:39-50](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/c4/C2.md#L39-L50) aún declara MapaRepository y plano pendientes, aunque existen en [lib/routing/mapa_repository.dart:8-29](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/mapa_repository.dart#L8-L29). [docs/aspectos.md:7-9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/aspectos.md#L7-L9) conserva Google Maps/coordenadas 0,0 como descripción anterior. Alinear C4/aspectos con el incremento real. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0015-cache-del-sitio-revalidar.md:13-24](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L13-L24) usa una observación para complementar 0007/0010; buen antecedente técnico, pero no se puntúa como evolución del reto S10 aún no identificado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | La sesión docente debe ejecutar el despliegue y pipeline en vivo; no se puntúa por documentación. |

Recuento descriptivo: 2 Cumple, 1 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Asignación S10 no confirmada; ruteo y reversión son antecedentes distintos. |
| Decisión e implementación | No verificado | Pendiente | Decisiones argumentadas y código reales, pertinencia al reto pendiente. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Health versionado y logging presentes; ejecución/gate y política de caché efectiva por ruta pendientes. |
| Evolución arquitectónica trazable | No verificado | Pendiente | C4/aspectos desactualizados; ADR-0015 vincula decisión a observación pero no se presume reto S10. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | Pendiente docente. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_mapsutb; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes en árbol; arc42 mezcla adoc y md como desviación de formato, sin tratar artefactos existentes como ausentes; [docs/aspectos.md:5-9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/aspectos.md#L5-L9). |
| Estado calificado identificable | Cumple | origin/master 1b296a37c575a751e99df1a1b288d70efba03d56; fecha/corte en cabecera. |
| Nombres de ADR según la convención | Cumple | Listado docs/adr 0001–0015 conforme; [docs/adr/0015-cache-del-sitio-revalidar.md:1-9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L1-L9). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0001-patrones-de-diseno.md:5-14](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0001-patrones-de-diseno.md#L5-L14) reconoce ediciones aceptadas; el historial confirma cambios antes del reemplazo. ADR-0015 sí complementa decisiones sin reescribirlas; es una mejora de práctica, no eliminación del historial. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:21-25](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/ia.md#L21-L25) contiene S9 y rechazos motivados. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [.github/workflows/ci.yml:44-64](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/.github/workflows/ci.yml#L44-L64) contiene suite, scanner y gate. El conector consultó una vez el hash con filtro PR y devolvió cero registros; no demuestra falta de runs push. Los runs enlazados en [docs/evidencia-s9.md:52](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L52) son evidencia documental; falta trío de comprobación pública vigente para este hash. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El equipo declara su barrido en [docs/evidencia-s9.md:104-109](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L104-L109). El barrido independiente agregado fue cancelado por la herramienta y no se completó en el único reintento; no hay base para certificar limpieza integral ni para atribuir exposición al equipo. La comprobación permanece pendiente del revisor. |
| Contribución de todos los integrantes | No verificado | La planilla anterior mantiene correspondencias cuenta–persona por confirmar. No se atribuyen identidades por nombres parecidos ni se reutilizan conteos anteriores como comprobación vigente. |

## Estado global del proyecto (overall)

Punta observada de `origin/master`: `1b296a37c575a751e99df1a1b288d70efba03d56` (2026-10-02T12:58:33-05:00). Hay 0 commits posteriores al estado congelado S9. Punta igual al cierre S9; health declara ese mismo commit. Se cerraron varios pendientes preliminares. Persiste GPS real y entradas de zona provisionales. El nuevo ADR de caché es una respuesta fundada en medición; la política HTTP efectiva de la raíz merece revisión porque se observó max-age=3600.

- Convertir rutas en enlaces navegables de A-01 y corregir C4 que todavía dice MapaRepository pendiente.
- Separar medición de cálculo/pantalla de GPS real y precisión geográfica; no afirmar un flujo físico completo desde un test sintético.
- Verificar política de caché efectiva por URL y qué ve un usuario previo a un rollback.
- Aportar run/Quality Gate del hash, confirmar atribución y completar barrido independiente pendiente.
- Identificar el reto S10 antes de puntuar su respuesta.

### Hallazgos anteriores cerrados o delimitados

- ADR-0014 ahora aceptado por el equipo; no sigue pendiente de decisión.
- Evidencia S9 incluye medición de pantalla además del algoritmo.
- La sección de dependencias coincide con las incorporaciones flutter_map/latlong2.
- A-01 ya reconoce la pantalla implementada; queda otro texto anterior en C4.
- URL y health hoy accesibles, con commit desplegado igual al revisado.

## Preparación de la sustentación

1. Fallo: si el GPS entrega una posición errónea o el usuario conserva una versión cacheada, ¿qué señal evita una ruta engañosa y cómo verificarán el rollback desde su navegador?
2. Costo: ¿cuál de las cuotas de Hosting/teselas/transferencia rompe primero el presupuesto cero y cómo cambia al revalidar recursos?
3. Medición: ¿qué cambiarían si el tiempo de cálculo sigue siendo bajo pero el usuario tarda o se localiza a más de 10 metros del camino real?

## Próximos pasos

El health público identifica el mismo commit revisado. Para el segundo corte, confirmen el escenario asignado y midan su línea base/respuesta sobre el entorno real. Comprueben la caché efectiva de cada recurso y la experiencia tras una reversión, y alineen C4 y aspectos con el código ya entregado.

</details>
