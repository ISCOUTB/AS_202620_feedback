# Segundo corte · S10 · ShareU · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_ShareU |
| Rama evaluada | `master` |
| Hash calificado | `39508608eae4c1a56a5e4fc11a055bf6afb2c003` |
| Fecha del commit | 2026-09-28T19:56:57-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

Usabilidad: localizar documento en ≤3 interacciones

Se valora el escenario documentado disponible; no se afirma asignación docente verificada ni nueva entrega específica S10. Evidencias previas se usan como estado del repositorio, no se traslada ni promedia su nota anterior.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Básico | 0,60 / 1,00 |
| C2 · Decisión e implementación | Básico | 0,60 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Básico | 0,60 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Pendiente docente | Pendiente |

**Subtotal técnico: 2,40 / 4,00. Total sobre 5,00 pendiente de C5.**

C5 sigue pendiente de calificación docente. No se registra como cero ni se estima a partir del repositorio.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

La muestra sintética de 2≤3 no aporta una línea base operacional. La fachada, la métrica real de búsquedas sin resultados, JSON y request_id dan observabilidad parcial. CI, URL y archivos declarados ausentes impiden el nivel competente. La consolidación reconoce esa observabilidad parcial bajo el alcance de revisión del repositorio.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencia/evidencia-s9.md:18–61](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L18-L61)
2. [app/main.py:24–105](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/main.py#L24-L105)
3. [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:9–86](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L9-L86)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** El corte de búsqueda conserva las fronteras de servicio del monolito. Se detectan dos desalineaciones documentales relevantes: topología/recreación del despliegue y garantía de verificación del contrato. Auth, almacenamiento externo y correo están expresamente fuera del corte actual.

**Arquitectura declarada:** Monolito modular FastAPI con Documentos dueño de SQLite; Búsqueda consulta su servicio y registra métricas por Administración. Next.js separado. Correo asíncrono y autenticación completa son futuros.

**Arquitectura implementada:** app.main monta cinco routers. GET /busqueda/documentos → buscar_documentos → obtener_documentos → repositorio SQLite; el filtro y ranking ocurren en Búsqueda. Frontend en app/frontend solicita una sola llamada HTTP. Usuarios/Calificaciones son ping. Middleware JSON y métricas en proceso.

**Hallazgos materiales: 2.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · La vista de despliegue afirma artefactos y rutas que este snapshot no contiene

**Naturaleza:** documentación desactualizada. **Prioridad:** Media. **Confianza:** alta.

**Declaración contrastada:**

- [docs/arc42/arc42.md:269–285](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L269-L285) — Afirma Dockerfile, Blueprint render.yaml y build de /frontend para el despliegue.
- [README.md:88–103](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md#L88-L103) — Indica docker compose y cd frontend como recorridos operativos.

**Implementación contrastada:**

- [app/frontend/lib/api.ts:22–32](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/frontend/lib/api.ts#L22-L32) — El cliente implementado está bajo app/frontend y consume una URL configurable.
- [.github/workflows/tests.yml:7–32](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/.github/workflows/tests.yml#L7-L32) — El workflow versionado ejecuta tests y análisis, sin publicar infraestructura.

**Efecto y alcance:** No permite reproducir desde el repositorio la topología Render/Vercel descrita; dificulta distinguir despliegue real de diseño. No demuestra que un servicio remoto esté caído.

**Corrección propuesta:** Marcar el despliegue como no verificable hasta aportar manifiestos y URL comprobable; corregir ruta a app/frontend y documentar comandos realmente disponibles. La inspección completa de ls-tree no encontró Dockerfile, compose ni render.yaml.

<a id="deriva-d2"></a>

### D2 · La prueba de contrato anunciada no está implementada en la suite versionada

**Naturaleza:** documentación desactualizada. **Prioridad:** Media. **Confianza:** alta.

**Declaración contrastada:**

- [docs/arc42/arc42.md:353–360](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L353-L360) — Asegura que tests/test_contrato.py valida respuestas contra OpenAPI y detiene cambios incompatibles.

**Implementación contrastada:**

- [tests/test_busqueda.py:9–24](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/tests/test_busqueda.py#L9-L24) — Las pruebas existentes comprueban algunos campos y cantidades, sin validar todo el esquema.
- [.github/workflows/tests.yml:25–26](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/.github/workflows/tests.yml#L25-L26) — CI ejecuta pytest con la etiqueta incluye prueba de contrato.

**Efecto y alcance:** Se declara una protección contra incompatibilidades que pytest no aporta: un cambio de esquema puede no ser detectado por las aserciones funcionales parciales.

**Corrección propuesta:** Añadir una prueba que cargue docs/api/openapi.yaml, resuelva referencias y valide respuestas/casos inválidos, más una mutación incompatible; mientras tanto retirar la garantía. Inspeccionados los cinco archivos de tests: ninguno carga OpenAPI/YAML/JSON Schema y test_contrato.py no existe.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Router→servicio Búsqueda→servicio Documentos; no acceso lateral directo a tablas. Se revisó también fachada Administración.

Límite: No se exige hexagonal, descartada explícitamente.

- [app/busqueda/router.py:19–37](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/busqueda/router.py#L19-L37) — Entrada real de búsqueda.
- [app/busqueda/service.py:5–6](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/busqueda/service.py#L5-L6) — Dependencias mediante servicios públicos.
- [app/busqueda/service.py:73–84](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/busqueda/service.py#L73-L84) — Filtra, ordena y registra métricas.

**Persistencia:** SQLite encapsulado en documentos.repository; inicialización y semillas locales.

Límite: La separación Calificaciones está propuesta y pendiente; no se trata su ausencia como deriva.

- [app/documentos/repository.py:21–30](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/documentos/repository.py#L21-L30) — Conexión SQLite configurada por ruta.
- [app/documentos/repository.py:74–85](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/documentos/repository.py#L74-L85) — Lectura de documentos encapsulada.
- [docs/arc42/arc42.md:368–370](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L368-L370) — Calificaciones pendiente de implementación.

**API y autorización:** Contrato coincide en ruta central y rango de min_calificacion; autenticación sin implementar está reconocida.

Límite: No se ejecutaron contratos ni se verificó toda respuesta dinámica.

- [docs/api/openapi.yaml:159–169](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/api/openapi.yaml#L159-L169) — Rango y forma de respuesta de búsqueda.
- [docs/arc42/arc42.md:390–396](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L390-L396) — Deudas explícitas, incluida autenticación.

**Despliegue:** Se contrastaron README, arc42, árbol Git, frontend y workflow.

Límite: Paneles Render/Vercel y tráfico real no inspeccionados.



**Asincronía:** Almacenamiento externo y correo/outbox no son recorridos implementados.

Límite: No se considera falta de cola incumplimiento actual.

- [docs/arc42/arc42.md:222–226](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L222-L226) — Declara integraciones como futuras.
- [docs/arc42/arc42.md:252–255](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L252-L255) — Contrato de eventos todavía fuera del alcance.

**Observabilidad:** Middleware registra campos JSON y cabecera request ID; búsquedas registran métricas.

Límite: Métricas en memoria; sin comprobación operacional ni garantía del camino de excepciones.

- [app/main.py:75–93](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/main.py#L75-L93) — Middleware de solicitudes.
- [app/administracion/service.py:1–8](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/administracion/service.py#L1-L8) — Fachada pública de métricas.

**Límites adicionales:** Auditoría estática por git show al hash fijo, sin checkout, ejecución de código estudiantil, lectura de PDF, escritura en GitHub, pruebas en producción ni cambios de notas. No certifica ausencia de defectos fuera de las rutas revisadas.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:46:10.266961+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`39508608eae4c1a56a5e4fc11a055bf6afb2c003`](https://github.com/ISCOUTB/AS_202620_ShareU/commit/39508608eae4c1a56a5e4fc11a055bf6afb2c003) (2026-09-28T19:56:57-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Semana 10 · Segundo corte · ShareU

**Revisión preliminar abierta al cierre del 2026-10-12T05:00:00Z.** No reemplaza S9 definitiva ni aplica la fórmula semanal.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_ShareU |
| Rama principal remota | `master` |
| Estado revisado | `39508608eae4c1a56a5e4fc11a055bf6afb2c003` en `origin/master` (2026-09-28T19:56:57-05:00) |
| Línea base S8 | `332f67f726969e0c73b98dd4705aea6c37e5603b` |
| Punta actual / S10 preliminar | `39508608eae4c1a56a5e4fc11a055bf6afb2c003` · 2026-09-28T19:56:57-05:00 |
| Cierre S9 | 2026-10-05T05:00:00Z |
| Cierre eventual S10 | 2026-10-12T05:00:00Z |
| Revisión | 2026-10-06 (UTC) |

## Evolución desde S5 publicado

Base S5: `19ce7197b4bc53c0a685f4722e0f3ae5538750be`. El delta hasta la punta contiene 20 commits y 42 rutas modificadas (PDF excluidos). Añade contrato de API, frontend Next, observabilidad, métrica y corrección de frontera; IaC y ADR de plataforma anunciados siguen sin versionarse. Se contrastaron código, documentación, ADR y contratos; este recorrido aporta contexto de evolución, no recalifica S6–S9 ni acredita por sí mismo respuesta al escenario asignado.

## Alcance y método

Se consultó la rama principal remota mediante git y se eligió su último commit anterior o igual al cierre S9; no se consultaron etiquetas. S10 es preliminar y usa la punta actual. Se comparó S9 con la línea base S8; no se vuelven a puntuar entregas anteriores por existir. No se ejecutó código, pruebas ni despliegues del equipo. Los registros de ejecución del repositorio se distinguen de la comprobación externa. Por exclusión docente no se abrieron PDFs ni se evaluó su presencia, contenido, extensión o ubicación.

La consulta general de Actions se verificó mediante GET /actions/runs (100 registros como máximo); se distinguen el hash, la rama y la conclusión de cada run. Un intento inicial filtrado a pull requests no se usó para decidir. No se consultaron jobs ni logs adicionales.

## Escenario operativo oficialmente asignado

**No verificado.** No se encontró documento que identifique el escenario operativo oficialmente asignado para S10. El presupuesto de tres interacciones es el escenario genérico de usabilidad del producto y sustenta S9; no se lo convierte en asignación del corte. [docs/aspectos/aspectos.md:15–30](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/aspectos/aspectos.md#L15-L30) No se sustituye la asignación por un escenario genérico de calidad, una práctica S8/S9 o una hipótesis del revisor.

## Despliegue observado

GET https://shareu-backend.onrender.com/health respondió HTTP 404 en 3,982095 s, comprobación terminada el 2026-10-06T21:16:28Z. No se confirmó el health de la aplicación ni se probó el flujo principal; la URL figura en arc42 §7 y el README conserva marcadores.

## Matriz de comprobación S10

Se omite expresamente la fila de PDF por exclusión docente. Quedan 12 filas; su recuento es diagnóstico y no es la fórmula de calificación.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | origin/master 39508608eae4c1a56a5e4fc11a055bf6afb2c003, 2026-09-28T19:56:57-05:00; punta actual previa al cierre futuro, preliminar. |
| Despliegue accesible en el momento de la revisión | No cumple | GET https://shareu-backend.onrender.com/health respondió HTTP 404 en 3,982095 s, comprobación terminada el 2026-10-06T21:16:28Z. No se confirmó el health de la aplicación ni se probó el flujo principal; la URL figura en arc42 §7 y el README conserva marcadores. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | No se encontró documento que identifique el escenario operativo oficialmente asignado para S10. El presupuesto de tres interacciones es el escenario genérico de usabilidad del producto y sustenta S9; no se lo convierte en asignación del corte. [docs/aspectos/aspectos.md:15–30](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/aspectos/aspectos.md#L15-L30) |
| Línea base medida y reproducible | No verificado | [docs/evidencia/evidencia-s9.md:18–43](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L18-L43). Medición S9 sintética disponible; no identifica línea base reproducible del escenario asignado. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:9–86](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L9-L86). Decisión técnica S9 documentada; falta relación con asignación S10 y aceptación formal. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [app/administracion/service.py:1–8](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/administracion/service.py#L1-L8). Respuesta de frontera implementada en S9; no se identifica cambio ni despliegue del reto asignado. |
| Resultado contrastado con el umbral | No verificado | [docs/evidencia/evidencia-s9.md:18–43](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L18-L43). Resultado 2≤3 de S9; no acredita experimento del reto S10 sin la asignación. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | [.github/workflows/tests.yml:22–32](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/.github/workflows/tests.yml#L22-L32) y [run 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458) failure. [app/main.py:24–46](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/main.py#L24-L46) configura logs; health público devuelve 404. No queda demostrada operación observable del reto. |
| Secretos protegidos | Cumple | Barrido del contrato sobre HEAD, docs y ejemplos sin credenciales identificadas; sin .env versionado; búsqueda histórica de patrones de claves privadas/tokens de alta confianza sin coincidencias. [docs/evidencia/evidencia-s9.md:75–80](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L75-L80). Resultado acotado al barrido, no garantía absoluta. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/evidencia/evidencia-s9.md:56–61](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L56-L61) reconoce Dockerfile, render.yaml, ADR 0005–0007 y tests/test_contrato.py ausentes; árbol confirma ausencia. [README.md:123–124](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md#L123-L124) sigue declarando esa prueba inexistente. Documentación no representa coherentemente el MVP. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:9–86](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L9-L86). No se identifica confirmación/reemplazo de decisión anterior a partir de un experimento del escenario S10 asignado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Evaluación exclusiva de la sustentación docente sobre despliegue y pipeline en vivo. |

## Rúbrica propia del corte · propuesta al docente

Niveles admitidos: insuficiente 0,00; básico 0,60; competente 0,80; sobresaliente 1,00. No verificado no equivale a cero.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | No hay asignación oficial identificada; usabilidad genérica no la sustituye. |
| Decisión e implementación | No verificado | Pendiente | Se verifica la fachada S9, sin vínculo acreditado al reto asignado. |
| Operación, seguridad y observabilidad | Insuficiente | 0.00 | Health público 404 y pipeline failure impiden acreditar operación observable. [run 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458) |
| Evolución arquitectónica trazable | Básico | 0.60 | Documentación actualizada parcialmente; declara IaC, ADR de plataforma y prueba de contrato ausentes. [docs/evidencia/evidencia-s9.md:56–61](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L56-L61) |
| Sustentación del reto | Lo fija el docente | Pendiente | Sustentación pendiente. |

**Sin total final:** faltan la asignación verificada y la sustentación, que solo califica el docente con el entorno desplegado y el pipeline en vivo.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon anónimo público de https://github.com/ISCOUTB/AS_202620_ShareU; organización y nombre conformes. |
| Estructura mínima presente | No cumple | [README.md:191–200](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md#L191-L200). Aspectos e IA existen en subcarpetas, no docs/aspectos.md y docs/ia.md. Desviación de ruta, no ausencia. |
| Estado calificado identificable | Cumple | origin/master 39508608eae4c1a56a5e4fc11a055bf6afb2c003, 2026-09-28T19:56:57-05:00; último ≤ cierre S9 y punta preliminar S10. |
| Nombres de ADR según la convención | Cumple | Los seis ADR Markdown 0001–0004, 0008 y 0009 siguen NNNN-kebab-case; [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:1–4](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L1-L4). Archivos PDF excluidos expresamente del criterio por decisión docente. |
| ADR aceptados no reescritos | Cumple | Historial de ADR leído: 0002/0003/0004/0008/0009 creados una vez; ADR-0001 solo movimientos de ruta sin edición de contenido. [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:1–7](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L1-L7) nuevo en 3950860. |
| docs/ia.md al día para la semana | Cumple | [docs/ia/ia.md:33](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/ia/ia.md#L33). Nueva entrada del periodo S9; ruta desviada evaluada por contenido. Aún no hay actividad adicional S10. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/tests.yml:22–32](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/.github/workflows/tests.yml#L22-L32). Consulta general Actions confirma [run 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458) en el hash revisado, conclusión failure (2026-09-29T00:59:44Z). Sin run exitoso de scanner y Quality Gate de esta revisión acreditados. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del contrato sobre HEAD, docs y ejemplos sin credenciales identificadas; sin .env versionado; búsqueda histórica de patrones de claves privadas/tokens de alta confianza sin coincidencias. [docs/evidencia/evidencia-s9.md:75–80](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L75-L80). Resultado acotado al barrido, no garantía absoluta. |
| Contribución de todos los integrantes | No verificado | 50 commits en cuatro grupos por identidad de correo; dos firmas se consolidan por coincidencia exacta, sin publicar correos. No se deduce la correspondencia completa con los cuatro integrantes solo por nombres de cuenta; validación docente pendiente, sin afirmar ausencia individual. |

## Estado global del proyecto (overall)

La punta actual de `master` es `39508608eae4c1a56a5e4fc11a055bf6afb2c003` (2026-09-28T19:56:57-05:00) y coincide con S9 congelada: no hay commits tardíos hasta esta revisión. Hay una corrección de erosión comprobable y medición sintética explícita. La cadena conserva una omisión de C4. El pipeline sigue fallando y la URL de salud no entrega el health esperado; la infraestructura y decisiones de plataforma documentadas siguen ausentes.

### Hallazgos abiertos

- Identificar el escenario oficialmente asignado y su línea base medida para S10.
- Pipeline de la punta en rojo: [run 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458).
- Health de la URL declarada respondió 404; confirmar URL vigente y restablecer despliegue.
- Completar ID y C4 en la tabla de trazabilidad; normalizar rutas de aspectos e IA. [docs/aspectos/aspectos.md:50–56](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/aspectos/aspectos.md#L50-L56)
- Versionar los archivos declarados ausentes o corregir documentos: Dockerfile, render.yaml, ADR 0005–0007 y prueba de contrato. [docs/evidencia/evidencia-s9.md:56–61](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L56-L61)
- Actualizar Next a una versión corregida tras revisar el aviso oficial: el registro de next 14.2.15 confirma advertencia de seguridad. [app/frontend/package.json:11–14](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/frontend/package.json#L11-L14)
- Ratificar ADR-0008/0009 y resolver marcadores documentales sin atribuir al equipo decisiones pendientes.

### Hallazgos cerrados o corregidos en esta revisión

- El cruce búsqueda→interno de administración está corregido mediante fachada y prueba de fronteras. [app/busqueda/service.py:5–6](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/busqueda/service.py#L5-L6)
- Se corrige el hallazgo preliminar de dependencias: no añadir paquetes no obliga a fallar; hay auditoría nueva del periodo y existencia contrastada en registros oficiales.
- Se excluye el hallazgo de convención sobre PDF por decisión docente; los ADR Markdown sí siguen la convención.

## Preparación concreta para S10

Antes del corte, documenten el escenario operativo asignado y su línea base reproducible. La URL de salud respondió 404 y el pipeline de la punta falla: corrijan ambos y aporten el run exitoso. Sincronicen la documentación con los archivos realmente versionados, y midan la respuesta al reto sobre el MVP desplegado.

## Tres preguntas de sustentación

1. Si se reinicia el backend y se pierden los contadores en memoria, ¿cómo distinguirán una mejora real de una métrica reiniciada?
2. ¿Qué costo y cambio de plataforma requiere conservar SQLite y métricas entre reinicios o escalar a más de una réplica?
3. ¿Qué cambiarían en el experimento después de comprobar que cinco documentos sintéticos se encuentran en dos interacciones, y cómo validarían que representa el uso real?

</details>
