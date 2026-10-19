# Segundo corte · S10 · XALD · consolidación al cierre

**Actualización del feedback: 19 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_XALD |
| Rama evaluada | `master` |
| Hash calificado | `9236ff97218b632eeb9a1910f6083968e2c22909` |
| Fecha del commit | 2026-10-04T23:53:02-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

ESC-05: conflictos de sincronización Last-Write-Wins

Se valora el escenario documentado disponible; no se afirma asignación docente verificada ni nueva entrega específica S10. Evidencias previas se usan como estado del repositorio, no se traslada ni promedia su nota anterior.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Básico | 0,60 / 1,00 |
| C2 · Decisión e implementación | Básico | 0,60 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Básico | 0,60 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Calificación docente: 4,00 / 5,00 | 0,80 / 1,00 |

**Subtotal técnico: 2,40 / 4,00. C5 docente: 0,80 / 1,00. Total S10: 3,20 / 5,00.**

C5 incorpora la calificación de sustentación 4,00 / 5,00 indicada por el docente el 18 de octubre de 2026 y sincronizada en esta publicación. Su aporte es 4,00 / 5 = 0,80. Los puntajes C1–C4 y el hash técnico del cierre se conservan; no se infiere la sustentación del repositorio.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

LWW y el contador existen, pero 30/30 no demuestra concurrencia ni la versión ganadora: el script cuenta respuestas 202 y conflictos y no comprueba el estado final. Falta línea base. Cliente HTTP, persistencia, cifrado y coherencia documental siguen parciales.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/adr/0011-resolucion-conflictos-lww.md:9–32](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L9-L32)
2. [backend/scripts/medir_esc05.py:61–79](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/scripts/medir_esc05.py#L61-L79)
3. [docs/EVIDENCIA-S9.md:34–40](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L34-L40)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** El aislamiento modular Kotlin se mantiene y la excepción syncqueue→DTO de core está reconocida. El alcance implementado es un prototipo en memoria y una API independiente. Las vistas todavía representan captura/UI, persistencia cifrada y sincronización reales; además el contrato de aceptación afirma un encolado que el handler no realiza. No se reclama Gemini real ni persistencia remota aplazada como incumplimiento.

**Arquitectura declarada:** Android offline-first con orquestación :app, interfaces de parser/aigemini/corefinanciero/syncqueue y backend FastAPI LWW. ADR-0012 acepta Gemini mock; ADR-0011 acepta estado LWW solo en memoria. C4/arc42 aún muestran UI/SMS, Room cifrado y conector HTTP móvil como actuales.

**Arquitectura implementada:** MainActivity presenta Hello Android y no invoca ProcesarNotificacionUseCase. El caso de uso existe y llama interfaces, pero core y cola almacenan mutableListOf; cola no hace HTTP. Backend valida API key y DTO, conserva solo fecha por ID para LWW e incrementa métricas; no persiste payload ni lo inserta en una cola de procesamiento.

**Hallazgos materiales: 2.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · La arquitectura de ejecución publicada mezcla diseño objetivo con prototipo en memoria

**Naturaleza:** documentación desactualizada. **Prioridad:** Media. **Confianza:** alta.

**Declaración contrastada:**

- [docs/arc42/05-Building Block View.md:30–48](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/arc42/05-Building%20Block%20View.md#L30-L48) — Describe arranque AppModule, UI/SMS, Room cifrado y sincronización real.
- [docs/c4/c2.md:23–32](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/c4/c2.md#L23-L32) — Presenta los conectores SMS, Gemini y backend sin marcar objetivo.

**Implementación contrastada:**

- [XALDAPP/app/src/main/java/com/proyecto/xald/MainActivity.kt:16–38](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/app/src/main/java/com/proyecto/xald/MainActivity.kt#L16-L38) — Entrada Android solo muestra saludo y no conecta el caso de uso.
- [XALDAPP/app/src/main/java/ProcesarNotificacionUseCase.kt:12–39](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/app/src/main/java/ProcesarNotificacionUseCase.kt#L12-L39) — Orquestación disponible por interfaces; no es bootstrap de AppModule.
- [XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/GestorCoreFinanciero.kt:9–24](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/GestorCoreFinanciero.kt#L9-L24) — Datos locales son una lista en memoria, sin Room/KeyStore.
- [XALDAPP/syncqueue/src/main/java/ColaSincronizacion.kt:9–23](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/syncqueue/src/main/java/ColaSincronizacion.kt#L9-L23) — Cola solo añade/consulta una lista, sin envío HTTP.
- [docs/EVIDENCIA-S9.md:34–40](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L34-L40) — El propio equipo mantiene abierta la brecha documental del prototipo.

**Efecto y alcance:** Las vistas atribuyen al artefacto garantías offline-first, cifrado y conectividad no implementadas. La auditoría S9 ya reconoce la brecha, pero no sustituye una vista de ejecución consistente. No se afirma fuga de datos reales ni se penaliza el aplazamiento explícito de Gemini.

**Corrección propuesta:** Separar claramente vista actual y objetivo; marcar UI/SMS, Room/cifrado y envío HTTP como pendientes. Documentar que el flujo es de componentes/pruebas, no integrado a la actividad Android. Para reclamar end-to-end, cablear la entrada real al caso de uso y demostrar persistencia/reinicio y envío autenticado.

<a id="deriva-d2"></a>

### D2 · El ACK de sincronización promete encolado aunque únicamente guarda una marca temporal

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** alta.

**Declaración contrastada:**

- [docs/api/contrato.md:34–40](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/api/contrato.md#L34-L40) — Define 202 como transacción recibida y encolada.

**Implementación contrastada:**

- [backend/app/main.py:103–133](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L103-L133) — El handler actualiza timestamp/métricas y devuelve mensaje encolada; no conserva datos ni encola.
- [docs/adr/0011-resolucion-conflictos-lww.md:13–19](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L13-L19) — La decisión vigente acota LWW a diccionario de fechas en memoria.

**Efecto y alcance:** El consumidor recibe ACEPTADO/encolada sin que exista cola ni almacenamiento del cuerpo de la transacción en el handler. Si un futuro cliente usa ese ACK para retirar su copia pendiente, no hay respaldo recuperable del payload en este backend. La app actual no implementa ese consumidor; no se afirma pérdida real en producción.

**Corrección propuesta:** Alinear semántica de API/ADR: declarar aceptación de una simulación de versiones, sin promesa de cola, o conservar payload completo y encolarlo antes del ACK. Añadir una prueba de recuperación del cuerpo aceptado/estado de cola, sin exigir persistencia durable si sigue fuera del corte.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Orquestador depende de interfaces; implementaciones internal. Se revisó dependencia Gradle syncqueue→core y su DTO público.

Límite: La excepción del DTO se reconoce en S9; no se llama deriva a toda referencia entre módulos.

- [docs/adr/0007-contratos-por-modulo.md:27–40](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0007-contratos-por-modulo.md#L27-L40) — Contratos y orquestación centralizada.
- [docs/EVIDENCIA-S9.md:8–13](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L8-L13) — Excepción explícita para el DTO de sincronización.
- [XALDAPP/syncqueue/build.gradle.kts:23–30](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/syncqueue/build.gradle.kts#L23-L30) — Dependencia real al módulo dueño del DTO.

**Persistencia:** Core/cola en listas, backend en diccionario; ningún motor SQL ejecutable en los caminos inspeccionados.

Límite: ADR-0011 acepta no persistencia remota; no se convierte migración futura en hallazgo de implementación.

- [docs/adr/0011-resolucion-conflictos-lww.md:27–32](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L27-L32) — Límites de estado en memoria aceptados.
- [backend/app/main.py:54–56](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L54-L56) — Estado LWW en memoria.

**API y autorización:** X-API-Key falla cerrado y DTO Pydantic valida campos. El DTO móvil contiene menos campos que el REST y no hay adaptador consumidor implementado.

Límite: No se declara incompatibilidad de un cliente en ejecución que aún no existe; falta futura traducción.

- [backend/app/main.py:62–65](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L62-L65) — Validación constante de llave y fallo cerrado.
- [backend/app/dtos.py:10–17](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/dtos.py#L10-L17) — Modelo de entrada REST.
- [XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/PayloadSincronizacionDTO.kt:7–12](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/PayloadSincronizacionDTO.kt#L7-L12) — Contrato interno Kotlin, no serializador REST.

**Despliegue:** README/Render describen servicio Docker; entrada Android y Manifest revisados.

Límite: No se verificó despliegue remoto, distribución APK ni configuración de secretos.

- [README.md:28–34](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/README.md#L28-L34) — Artefactos de infraestructura del backend.
- [XALDAPP/app/src/main/AndroidManifest.xml:14–24](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/app/src/main/AndroidManifest.xml#L14-L24) — Actividad lanzadora declarada.

**Asincronía:** Caso de uso encola en memoria de forma local; no worker HTTP, reintento o confirmación móvil en código revisado.

Límite: No se exige integración Gemini real: ADR-0012 acepta mock.

- [XALDAPP/syncqueue/src/main/java/ColaSincronizacion.kt:9–23](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/syncqueue/src/main/java/ColaSincronizacion.kt#L9-L23) — Cola local sin procesamiento.
- [docs/adr/0012-aplazamiento-integracion-gemini.md:17–25](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0012-aplazamiento-integracion-gemini.md#L17-L25) — Mock mantenido explícitamente en este corte.

**Observabilidad:** JSON por solicitud, métricas de transacciones/conflictos y /health. Un conflicto cuenta ID repetido, no confirma persistencia de datos.

Límite: No se reproducen mediciones ESC-05 ni garantía de cero transacciones perdidas; no se observa estado operacional.

- [backend/app/main.py:44–52](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L44-L52) — Contadores Prometheus.
- [backend/app/main.py:74–85](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L74-L85) — Middleware JSON de solicitudes.
- [backend/app/main.py:113–122](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L113-L122) — Definición real del contador de conflictos.

**Límites adicionales:** Auditoría estática por git show al hash fijo, sin checkout, ejecución de código estudiantil, lectura de PDF, escritura en GitHub, pruebas en producción ni cambios de notas. No certifica ausencia de defectos fuera de las rutas revisadas.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:46:16.166728+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`9236ff97218b632eeb9a1910f6083968e2c22909`](https://github.com/ISCOUTB/AS_202620_XALD/commit/9236ff97218b632eeb9a1910f6083968e2c22909) (2026-10-04T23:53:02-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

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

</details>
