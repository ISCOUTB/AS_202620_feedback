# Segundo corte · S10 · Verifacts · consolidación al cierre

**Actualización del feedback: 19 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_Verifacts |
| Rama evaluada | `master` |
| Hash calificado | `6c08cc536ac7bd294c749548bd70276044ee511e` |
| Fecha del commit | 2026-10-10T18:23:32-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

Q-01: tiempo análisis y arranque frío Render; decisión mantener Render+keepalive

Se evalúa técnicamente el escenario declarado; no se afirma asignación docente verificada.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Competente | 0,80 / 1,00 |
| C2 · Decisión e implementación | Básico | 0,60 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Básico | 0,60 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Calificación docente: 4,00 / 5,00 | 0,80 / 1,00 |

**Subtotal técnico: 2,60 / 4,00. C5 docente: 0,80 / 1,00. Total S10: 3,40 / 5,00.**

C5 incorpora la calificación de sustentación 4,00 / 5,00 indicada por el docente el 18 de octubre de 2026 y sincronizada en esta publicación. Su aporte es 4,00 / 5 = 0,80. Los puntajes C1–C4 y el hash técnico del cierre se conservan; no se infiere la sustentación del repositorio.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

Se documentan estados warm y cold, pero faltan POST en frío, hash desplegado y efecto tras la mitigación. Persisten afirmaciones de causalidad y costo incompatibles con la rectificación del ADR-0008, además de documentación parcial.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencia/medicion-render-s10.md:3–61](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/docs/evidencia/medicion-render-s10.md#L3-L61)
2. [docs/adr/0008-mantener-render-mitigar-arranque-frio.md:39–65](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/docs/adr/0008-mantener-render-mitigar-arranque-frio.md#L39-L65)
3. [app/observability.py:136–178](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/observability.py#L136-L178)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** La implementación recorre API→servicios públicos de normalización/análisis/scoring→repositorio SQLite y mantiene la propiedad de datos. La documentación de bloques/C4 conserva un flujo que no es el real y llama pendiente a POST /analysis. Las limitaciones de SQLite efímero y RuleAnalyzer están expresamente aceptadas, por lo que no son deriva.

**Arquitectura declarada:** Monolito modular API/Content/Analysis/Scoring con contexto separado de Historial, frontend React/Vite, REST síncrono y SQLite. ADR-0006 conserva semántica de señales de estilo, no veracidad; ADR-0008 mantiene Render y acepta almacenamiento efímero.

**Arquitectura implementada:** POST /analysis orquesta desde routes.py: extrae/normaliza Content, invoca Analysis, calcula Scoring y guarda/lee Historial por funciones públicas del repositorio. Analysis no llama a Historial; Content no encadena Analysis. /analysis GET expone historial. SQLite solo se abre en repository.py. Frontend consume HTTP; middleware instala logs y métricas.

**Hallazgos materiales: 1.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · Las vistas de bloques y componentes no reflejan quién orquesta el análisis

**Naturaleza:** documentación desactualizada. **Prioridad:** Media. **Confianza:** alta.

**Declaración contrastada:**

- [docs/c4/03-componentes.md:5–16](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/docs/c4/03-componentes.md#L5-L16) — Dibuja Análisis→Historial como dependencia interna.
- [docs/arc42/05-vista-de-bloques.md:24–48](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/docs/arc42/05-vista-de-bloques.md#L24-L48) — Describe API como esqueleto solo health y analysis pendiente.

**Implementación contrastada:**

- [app/api/routes.py:4–12](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/api/routes.py#L4-L12) — API importa interfaces públicas de los servicios y del Historial.
- [app/api/routes.py:62–101](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/api/routes.py#L62-L101) — API orquesta normalización, análisis, puntuación y persistencia.
- [app/modules/analysis/service.py:1–7](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/modules/analysis/service.py#L1-L7) — Analysis solo invoca RuleAnalyzer.

**Efecto y alcance:** Asignan las dependencias a componentes que no las tienen y presentan POST /analysis como futuro; un mantenedor puede extender el módulo equivocado o evaluar una frontera inexistente. No se evidencia acceso SQL fuera del dueño de Historial.

**Corrección propuesta:** Actualizar C4 con Ingesta/API→Análisis y API→Historial, y arc42 §5 con POST/GET /analysis implementados; remitir a la vista de ejecución §6 que ya explica la orquestación. No forzar una capa nueva si la orquestación actual sigue siendo la decisión elegida.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Imports revisados en todos los módulos: Scoring recibe Finding reexportado por servicio de Analysis; API orquesta mediante funciones públicas. No se exige hexagonal.

Límite: No se ejecutaron pruebas de fronteras.

- [docs/arc42/08-conceptos-transversales.md:17–22](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/docs/arc42/08-conceptos-transversales.md#L17-L22) — Los módulos internos no deben conocer HTTP.
- [app/modules/content/service.py:4–14](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/modules/content/service.py#L4-L14) — Normalización devuelve error Python, sin HTTP.
- [app/modules/scoring/service.py:1–14](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/modules/scoring/service.py#L1-L14) — Dependencia pública y cálculo del score.

**Persistencia:** Repositorio concentra conexión y CRUD SQLite; memoria de API no sustituye persistencia del análisis. Render Free efímero es reconocido.

Límite: No se exige durabilidad que ADR reciente aplaza; no se comprobaron datos reales.

- [app/persistence/repository.py:13–19](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/persistence/repository.py#L13-L19) — Conexión SQLite encapsulada.
- [app/persistence/repository.py:95–136](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/persistence/repository.py#L95-L136) — Escritura/commit de análisis.
- [docs/adr/0008-mantener-render-mitigar-arranque-frio.md:64–65](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/docs/adr/0008-mantener-render-mitigar-arranque-frio.md#L64-L65) — Riesgo aceptado de pérdida del historial al reiniciar/redesplegar.

**API y autorización:** Análisis acepta exactamente texto o URL; traduce errores de contenido; historial paginado y contador en cabecera. No hay identidad de usuario en el corte.

Límite: No se deriva fallo de autorización sin una promesa de autenticación en alcance; contrato no ejecutado.

- [app/api/routes.py:21–35](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/api/routes.py#L21-L35) — Validación de origen mutuamente excluyente.
- [app/api/routes.py:129–153](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/api/routes.py#L129-L153) — Ruta pública de historial y paginación.

**Despliegue:** Render API Docker y frontend estático; prototipo Lambda no es producción elegida por ADR-0008.

Límite: No se verificó live URL, keepalive ni SLA; costo/mediciones reportados por autores no reproducidos.

- [render.yaml:1–25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/render.yaml#L1-L25) — Infraestructura versionada API y frontend.
- [docs/adr/0008-mantener-render-mitigar-arranque-frio.md:1–8](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/docs/adr/0008-mantener-render-mitigar-arranque-frio.md#L1-L8) — ADR vigente de continuidad en Render.

**Asincronía:** Respuesta POST espera cálculo y commit SQLite; no hay cola/eventos reclamados en este corte.

Límite: No se confunde biblioteca de extracción URL con arquitectura asíncrona.

- [app/api/routes.py:85–113](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/api/routes.py#L85-L113) — Cálculo y persistencia antes de responder.

**Observabilidad:** main instala observability; logs JSON y métricas en app.observability. Semántica score limitada por ADR-0006.

Límite: No se comprobó agregación multiproceso o estado externo; riesgo alto inalcanzable es decisión aceptada, no bug nuevo.

- [app/main.py:28–30](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/app/main.py#L28-L30) — Instalación de middleware y router.
- [docs/adr/0006-semantica-del-resultado.md:34–46](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/6c08cc536ac7bd294c749548bd70276044ee511e/docs/adr/0006-semantica-del-resultado.md#L34-L46) — Semántica y umbrales aceptados.

**Límites adicionales:** Auditoría estática por git show al hash fijo, sin checkout, ejecución de código estudiantil, lectura de PDF, escritura en GitHub, pruebas en producción ni cambios de notas. No certifica ausencia de defectos fuera de las rutas revisadas.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:46:16.110926+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`6c08cc536ac7bd294c749548bd70276044ee511e`](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/6c08cc536ac7bd294c749548bd70276044ee511e) (2026-10-10T18:23:32-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Segundo corte S10 · revisión preliminar actualizada · Verifacts

**Preliminar; no es la calificación del corte.** Cierre futuro: **2026-10-12T05:00:00Z**. Se revisa la punta actual de la misma rama y se conservan intactas la matriz, nota y evidencia histórica de S9.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_Verifacts |
| Rama principal | `master` (reconfirmada por Git) |
| Estado revisado | `5c643bd03f19630d6459da79fb13fb2d5f943c7b` · 2026-10-07T15:32:38-05:00 |
| Base de la pasada anterior | `4f0652291c47f5093da1230b245a980614220e80` |
| Base S5 publicada | `67f8cea03e6a7b827aced6b60d3af8cf4307b237` |
| Observado | 2026-10-10T13:13:22Z |
| Delta desde la pasada anterior | 4 commits; 10 rutas no PDF afectadas, incluidas tres reubicaciones/renombres |
| Delta S5→punta | 70 commits; contexto evolutivo, sin recalificar S5–S9 |

## Alcance y método

Lectura del kit en el estado de feedback `1c24720331066744b3a3ef1d3e9f92fcc3cb0202`, ficha S10, matriz/planilla anteriores; revisión estática del delta completo no PDF, historial y archivos pertinentes del estado actual mediante Git. No se ejecutaron código, pruebas, mutaciones, mediciones ni despliegues del equipo, ni se activó o reanudó ningún escáner. Se leyeron runs de CI ya existentes y se hizo únicamente un GET público de salud. Los comandos al final son próximos pasos para el equipo, no resultados ejecutados. No se leyó ningún PDF: su criterio se excluye por decisión docente, sin penalización, quedando doce filas. No se consultaron etiquetas para seleccionar el estado.

Las cifras experimentales y los costos citados por el equipo se atribuyen a sus documentos. CI exitoso no equivale a observación del flujo desplegado, Gate satisfactorio o sustentación. Un límite de acceso/verificación se marca NV, sin inventar fallos. No se imprimen valores de secretos ni correos.

## Escenario operativo y procedencia

El equipo ahora identifica expresamente la comparación Render frente a AWS Lambda como «Reto Operativo de la Semana 10» en [docs/adr/0005-comparacion-lambda-render.md:7–36](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L7-L36). Eso corrige la ausencia de una identificación S10 en su propia documentación. No se encontró en los materiales revisados una consigna/asignación oficial independiente del equipo: su correspondencia con el escenario asignado sigue No verificado. Se reconoce y evalúa la evidencia técnica legible del escenario declarado; no se presenta su autorrotulado como confirmación docente. Esta reserva mantiene pendientes los criterios primero y segundo de la rúbrica, sin convertir la falta de fuente externa en incumplimiento técnico.

## Hallazgo central del experimento

La tabla nueva denomina «contraste equivalente» a una comparación que todavía mezcla entornos y cargas: [docs/adr/0005-comparacion-lambda-render.md:27–35](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L27-L35) declara Python 3.12, 512 MB y texto de 10.000 caracteres para ambos; el resultado de 46,9 ms enlazado procede de Windows 11/Python 3.14.7/uvicorn local, 200 corridas y un cliente ([docs/evidencia/medicion-q01-q05.md:3–12](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/evidencia/medicion-q01-q05.md#L3-L12)), mientras el evento SAM contiene un texto de 63 caracteres ([serverless-prototype/events/analysis_event.json:1–21](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/events/analysis_event.json#L1-L21)). El cuerpo JSON se contó como dato, sin ejecutar código del equipo. El P95 SAM de 20.005,9 ms era explícitamente GET /health en la base anterior ([docs/adr/0005-comparacion-lambda-render.md:65–91](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/4f0652291c47f5093da1230b245a980614220e80/docs/adr/0005-comparacion-lambda-render.md#L65-L91)) y ahora se atribuye a GET /health y POST /analysis sin dos series separadas ([docs/adr/0005-comparacion-lambda-render.md:64–88](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L64-L88)). No hay CSV en el árbol revisado; el nombre citado sigue ignorado ([serverless-prototype/.gitignore:1–3](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/.gitignore#L1-L3)). Los dos comandos del ADR omiten --out y, según [serverless-prototype/medir_cold_start.py:66–70](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/medir_cold_start.py#L66-L70) y [serverless-prototype/medir_cold_start.py:90–93](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/medir_cold_start.py#L90-L93), escribirían el mismo archivo. No se acusa inexistencia de toda medición: existe la medición local S9, pero no es evidencia equivalente de Render/SAM ni una corrida del revisor.

Además, `lambda_handler.py` importa `app.main` a nivel de módulo y `content/service.py` importa `trafilatura` también a nivel de módulo ([serverless-prototype/lambda_handler.py:1–5](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/lambda_handler.py#L1-L5); [app/modules/content/service.py:1–4](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/app/modules/content/service.py#L1-L4)). Por tanto la causalidad «import dentro del handler» del ADR requiere corrección/profiling. La emulación no demuestra por sí sola una cota inferior del tiempo real AWS ni que Render cumpla el umbral en toda condición. El propio ADR reconoce reposo/despertar; la medición de health de hoy no identifica esa causa.

## Matriz de preparación S10

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Rama remota master comprobada mediante git ls-remote --symref; punta 5c643bd03f19630d6459da79fb13fb2d5f943c7b, fecha 2026-10-07T15:32:38-05:00. Es anterior al cierre futuro 2026-10-12T05:00:00Z. [Commit inmutable](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/5c643bd03f19630d6459da79fb13fb2d5f943c7b). Solo preparación preliminar; no se seleccionaron etiquetas. |
| Despliegue accesible en el momento de la revisión | No verificado | [docs/despliegue.md:1–2](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/despliegue.md#L1-L2) identifica la API. GET https://verifacts-api.onrender.com/health iniciado el 2026-10-10T13:05:25Z: HTTP 200, 25,359958 s, cuerpo {"status":"ok"}. Una petición puntual; no se probó POST /analysis, ni se identificó la revisión desplegada, ni se infiere la causa de la latencia. El resultado acredita accesibilidad del health check, no el flujo principal ni Q-01. Corrección documental del 10 de octubre: la [ficha S10, instrucción 2](https://github.com/ISCOUTB/AS_202620_feedback/blob/bb8bb783d0e07d78621b71527de5d49396f9d5a9/fichas/semana-10-corte2.md#L36-L37) exige comprobar el flujo principal además del health check. Esa comprobación conjunta queda No verificado porque no se probó el flujo principal en el momento de la revisión. Se conserva la evidencia positiva de salud; este límite de verificación no acredita un fallo del despliegue. No se realizó una nueva comprobación externa para esta corrección. |
| Hipótesis, montaje, variables y umbral declarados | Cumple | [docs/adr/0005-comparacion-lambda-render.md:7–36](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L7-L36) contiene hipótesis de penalización serverless, plataformas, montaje SAM, variables y P95 ≤ 3.000 ms. Cumple la declaración del escenario que propone el equipo; la asignación oficial sigue No verificado. Las contradicciones de control y medición se evalúan en línea base/resultados, no se ocultan. |
| Línea base medida y reproducible | No cumple | [docs/adr/0005-comparacion-lambda-render.md:81–101](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L81-L101) usa P95 local de 46,9 ms como base Render y añade ~250–350 ms en red sin serie, fecha ni procedimiento. [docs/evidencia/medicion-q01-q05.md:3–12](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/evidencia/medicion-q01-q05.md#L3-L12) sí acredita una medición declarada local; [scripts/medir_q01_q05.py:33–37](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/scripts/medir_q01_q05.py#L33-L37) y [scripts/medir_q01_q05.py:52–73](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/scripts/medir_q01_q05.py#L52-L73) describen su carga/procedimiento. No hay una base Render equivalente a SAM: evento de 63 caracteres en [serverless-prototype/events/analysis_event.json:19](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/events/analysis_event.json#L19) frente a 10.000 y runtimes distintos. Incumplimiento técnico, independiente de la asignación oficial. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No cumple | [docs/adr/0005-comparacion-lambda-render.md:106–138](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L106-L138) registra costos, alternativas y mantener Render; [docs/adr/0005-comparacion-lambda-render.md:140–170](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L140-L170) explica reversión y consecuencias. Se reconoce ese ADR y la restricción de no desplegar AWS. No alcanza la coherencia completa: la elección y el punto de quiebre se apoyan en Duration SAM trasladada a latencia/costo de nube sin comparación equivalente; la explicación de imports «dentro del handler» no corresponde a [serverless-prototype/lambda_handler.py:1–5](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/lambda_handler.py#L1-L5) y [app/modules/content/service.py:1–4](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/app/modules/content/service.py#L1-L4), que importan en nivel de módulo. No se exige migrar: mantener Render es admisible si se demuestra con evidencia válida. Tarifas/cifras son supuestos del equipo, no precios verificados por el revisor. |
| Respuesta implementada o configurada sobre el MVP | No cumple | [render.yaml:1–25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/render.yaml#L1-L25) y [Dockerfile:1–27](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/Dockerfile#L1-L27) configuran el despliegue actual; [serverless-prototype/template.yaml:1–36](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/template.yaml#L1-L36) y [serverless-prototype/lambda_handler.py:1–5](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/lambda_handler.py#L1-L5) contienen el prototipo de la misma API. Existen implementaciones desde S5, sin cambio productivo de app/ ni de infraestructura en los cuatro commits nuevos. [docs/adr/0005-comparacion-lambda-render.md:47–50](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L47-L50) declara SAM local y [docs/adr/0005-comparacion-lambda-render.md:125–138](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L125-L138) mantiene Render. Falta demostrar que no cambiar resuelve el reto, pues la comparación que lo fundamenta no controla operación, carga y entorno. No se exige cambio por cambiar ni despliegue a AWS como requisito añadido. |
| Resultado contrastado con el umbral | No cumple | [docs/adr/0005-comparacion-lambda-render.md:64–104](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L64-L104) sí presenta tabla frente a 3.000 ms y límites; pero reutiliza 20.005,9 ms para dos operaciones, compara P95 local con Duration SAM y trata un log health de 15,18 ms como base. El log está declarado como docker local en [docs/despliegue.md:34](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/despliegue.md#L34). La afirmación «100 % ... menos de 300 ms» carece de serie y no concuerda con el rango ~250–350 ms del propio ADR. No se ha demostrado que la emulación sea cota inferior de AWS. La observación health de esta revisión tampoco es un P95 ni prueba del tiempo de análisis. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | Cumple | [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824175) y [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824211) concluyen success para el hash revisado, en runs creados 2026-10-07T20:32:51Z. [.github/workflows/tests.yml:24–60](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/tests.yml#L24-L60) define pruebas, build/smoke health y consulta de métricas; [app/api/routes.py:57–59](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/app/api/routes.py#L57-L59) define health; [app/observability.py:19–34](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/app/observability.py#L19-L34) logs JSON y [app/observability.py:94–125](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/app/observability.py#L94-L125) histograma de duración por ruta/método, ligado a Q-01 en [docs/escenarios-de-calidad.md:45–63](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/escenarios-de-calidad.md#L45-L63). Correlación en [app/observability.py:147–174](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/app/observability.py#L147-L174). Cumple la instrumentación, con health observado y CI existente; no acredita experimento comparativo, Gate ni recuperación controlada. El middleware mide después de entrar a la aplicación y no demuestra la espera de activación de la plataforma. |
| Secretos protegidos | No verificado | [.gitignore:15–20](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.gitignore#L15-L20) excluye formatos de secretos y [.github/workflows/sonarcloud.yml:34–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L34-L38) usa referencia al almacén, no un valor. Se leyó el delta sustantivo y las configuraciones pertinentes sin detectar valores de credenciales en ese alcance. No se ejecutó ni reanudó un escáner ni se hizo un barrido completo nuevo de árbol/historial; no se hereda como verificación actual el Cumple del 6-oct. [docs/auditoria-s9.md:53–60](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/auditoria-s9.md#L53-L60) es una declaración del equipo. NV es límite de comprobación, no hallazgo de exposición ni razón para asignar insuficiente automáticamente. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | Se reparan los enlaces A-06 ([docs/aspectos.md:25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/aspectos.md#L25)), README ([README.md:185–191](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/README.md#L185-L191)) y el índice ADR ([docs/arc42/09-decisiones-arquitectonicas.md:12–18](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L12-L18)); la aclaración MLAnalyzer está en [docs/adr/0002-contextos-sin-cambios.md:36–43](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0002-contextos-sin-cambios.md#L36-L43). Persisten contradicciones: [docs/arc42/03-contexto-y-alcance.md:112–118](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/03-contexto-y-alcance.md#L112-L118) dice que extracción URL no existe, aunque [app/modules/content/service.py:17–36](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/app/modules/content/service.py#L17-L36) la implementa; [docs/arc42/10-requisitos-de-calidad.md:41–54](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/10-requisitos-de-calidad.md#L41-L54) mantiene P95 y frontend como pendientes sin incorporar la evidencia local existente. [docs/aspectos.md:68–70](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/aspectos.md#L68-L70) también deja pendiente P95. C4/contrato existen, pero la representación global y la trazabilidad del nuevo contraste no están cerradas. |
| Decisión anterior confirmada o reemplazada con evidencia | No cumple | [docs/adr/0005-comparacion-lambda-render.md:125–138](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L125-L138) reafirma Render y [docs/adr/0005-comparacion-lambda-render.md:176–178](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L176-L178) enlaza ADR-0004, pero el experimento no confirma todavía esa elección con cargas equivalentes. [docs/adr/0007-no-incorporar-componente-generativo.md:17–40](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0007-no-incorporar-componente-generativo.md#L17-L40) es un nuevo ADR real sobre otra decisión y reconoce el motor actual; no demuestra la comparación de plataformas. Además ADR-0005 conserva «Aceptado — 2026-09-25» ([docs/adr/0005-comparacion-lambda-render.md:1–5](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L1-L5)) pese a una reescritura sustantiva en el commit nuevo; no aparece en la tabla de enmiendas [docs/arc42/09-decisiones-arquitectonicas.md:20–27](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L20-L27). |
| Sustentación del reto sobre el entorno desplegado | No verificado | La sesión, defensa del escenario asignado, prueba del flujo y pipeline en vivo los verifica el docente. No se infieren desde documentación ni runs anteriores. |

**Recuento de comprobación:** 3/12 Cumple, 6/12 No cumple y 3/12 No verificado. Este recuento **no se convierte con la fórmula semanal en una nota de corte**. La diferencia frente a la pasada anterior incluye verificaciones y límites actualizados, no solo correcciones del equipo.

## Rúbrica específica de cinco criterios

Propuesta al docente; escala 0,00 / 0,60 / 0,80 / 1,00. Los dos primeros criterios siguen pendientes por procedencia oficial del escenario; se reconocen los avances legibles sin relajar el método usado en las demás evaluaciones.

| Criterio | Nivel sugerido | Puntaje | Evidencia y límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Pendiente de confirmar la asignación oficial. La hipótesis, variables y umbral del escenario declarado ya existen; condicionalmente describen una caracterización básica, con línea base comparativa aún no reproducible. [docs/adr/0005-comparacion-lambda-render.md:7–36](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L7-L36); [docs/evidencia/medicion-q01-q05.md:3–12](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/evidencia/medicion-q01-q05.md#L3-L12). |
| Decisión e implementación | No verificado | Pendiente | Pendiente de confirmar la asignación oficial. Se reconoce decisión Render, prototipo SAM, costo/consecuencias y nuevo ADR-0007. El sustento técnico de mantener la plataforma es parcial por comparación no equivalente; sin fijar puntaje mientras no se confirme el escenario. [docs/adr/0005-comparacion-lambda-render.md:106–170](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L106-L170). |
| Operación, seguridad y observabilidad | Básico | 0.60 | Hay CI del hash, health público, JSON, correlación e histograma. No se demuestra el comportamiento de activación/recuperación ni una medición operativa controlada del contraste; el temporizador [app/observability.py:147–173](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/app/observability.py#L147-L173) empieza al entrar al middleware, por lo que no prueba la espera exterior de arranque. Gate actual y alcance completo de secretos permanecen NV; no se convierten en incidentes. [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824175) y [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824211). |
| Evolución arquitectónica trazable | Básico | 0.60 | Renombres, enlaces, registro IA, nota MLAnalyzer y ADR-0007 son correcciones reales. Persisten vistas desactualizadas, reescritura del ADR-0005 aceptado y comparación sin evidencia equivalente. [docs/arc42/09-decisiones-arquitectonicas.md:12–27](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L12-L27); [docs/arc42/03-contexto-y-alcance.md:112–118](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/03-contexto-y-alcance.md#L112-L118). |
| Sustentación del reto | Lo fija el docente | Pendiente | Pendiente de sesión sobre entorno desplegado y pipeline en vivo. No se suma como cero. |

**No se publica total final.** Las celdas pendientes no equivalen a cero; sustentación y nota final corresponden al docente. La falta de un nuevo barrido integral de secretos no se convierte en exposición confirmada ni rebaja automática a insuficiente.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Acceso público por git ls-remote y clon sin autenticación de https://github.com/ISCOUTB/AS_202620_Verifacts; rama master confirmada. [README.md:695–702](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/README.md#L695-L702). |
| Estructura mínima presente | Cumple | El árbol contiene código, README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md. [docs/aspectos.md:17–25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/aspectos.md#L17-L25); [docs/arc42/09-decisiones-arquitectonicas.md:12–18](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L12-L18); [docs/ia.md:12–25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L12-L25). El renombre arc42 §8 corrige la ruta; estructura presente no equivale a coherencia/completitud de todas sus secciones. |
| Estado calificado identificable | Cumple | master · 5c643bd03f19630d6459da79fb13fb2d5f943c7b · 2026-10-07T15:32:38-05:00. Punta anterior al cierre futuro; revisión preliminar. [Commit](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/5c643bd03f19630d6459da79fb13fb2d5f943c7b). |
| Nombres de ADR según la convención | Cumple | Los siete archivos del árbol siguen NNNN-titulo-en-kebab-case.md. Renombre de ADR-0006 sin cambio de contenido y nuevo ADR-0007; índice navegable en [docs/arc42/09-decisiones-arquitectonicas.md:12–18](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L12-L18). Se cierra la desviación de nombre, no las cuestiones de inmutabilidad. |
| ADR aceptados no reescritos | No cumple | La nueva tabla reconoce adiciones previas a ADR-0001…0004 y nota a ADR-0002 ([docs/arc42/09-decisiones-arquitectonicas.md:20–27](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L20-L27)), pero no borra la reescritura histórica ni sustituye la regla del contrato. Además ADR-0005 ya aceptado ([docs/adr/0005-comparacion-lambda-render.md:3–5](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L3-L5)) cambia contexto, montaje y resultados en el delta actual sin nuevo ADR ni reemplazo explícito. [Diff inmutable](https://github.com/ISCOUTB/AS_202620_Verifacts/compare/4f0652291c47f5093da1230b245a980614220e80...5c643bd03f19630d6459da79fb13fb2d5f943c7b). |
| docs/ia.md al día para la semana | Cumple | Actualizado el 7-oct dentro del delta: corrige MLAnalyzer como propuesta no incorporada y registra aceptación/corrección/rechazo con motivos ([docs/ia.md:19–25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L19-L25) y [docs/ia.md:27–46](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L27-L46)). Cierra la ausencia previa de registro y su falsa afirmación ML. Las entradas rotuladas S9 son corrección tardía visible hoy, no evidencia incorporada retroactivamente a S9. No se presume cobertura de interacciones no declaradas; revisar la redacción que presenta riesgo de latencia LLM como incumplimiento medido sin experimento del modelo. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824175) y [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824211) success en el hash actual; scanner/configuración en [.github/workflows/sonarcloud.yml:26–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L26-L38) y [sonar-project.properties:1–6](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/sonar-project.properties#L1-L6). El documento ahora declara Gate VERDE/OK y 99,1 % de cobertura con fecha 7-oct ([docs/despliegue.md:37](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/despliegue.md#L37)); se atribuye al equipo. Consulta pública del evaluador a https://sonarcloud.io/api/qualitygates/project_status?projectKey=ISCOUTB_AS_202620_Verifacts iniciada 2026-10-10T13:06:42Z: HTTP 403 en 5,059115 s; consulta a https://sonarcloud.io/api/project_analyses/search?project=ISCOUTB_AS_202620_Verifacts&ps=5 iniciada 13:06:48Z: HTTP 403 en 6,651586 s. No se pudo ligar el Gate a una revisión. Por tanto el Gate actual queda No verificado, no «rojo» ni «verde confirmado por el evaluador». El workflow ejecuta el scanner, pero no declara espera del Gate ([.github/workflows/sonarcloud.yml:26–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L26-L38); [sonar-project.properties:1–9](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/sonar-project.properties#L1-L9)). La exigencia conjunta no queda demostrada y sigue abierta; una limitación HTTP no se publica como Gate fallido. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Lectura acotada del delta y configuraciones sin credenciales visibles; referencia de CI [.github/workflows/sonarcloud.yml:34–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L34-L38) y exclusiones [.gitignore:15–20](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.gitignore#L15-L20). No hay barrido completo nuevo de árbol/historial. La afirmación del equipo en [docs/auditoria-s9.md:53–60](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/auditoria-s9.md#L53-L60) no sustituye esa comprobación. Se conserva la observación anterior únicamente como histórica. |
| Contribución de todos los integrantes | No verificado | Recuento por git log del 10-oct: 304 commits, tres firmas de autor con 241, 37 y 26 commits; son firmas, no tres personas verificadas. La base contiene 300 commits (294 sin merges y 6 merges), y la punta 304 (298 y 6): cuatro adicionales. El agrupamiento usa firmas %an, sin .mailmap; no consolida personas. [Equipo.md:3–8](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/Equipo.md#L3-L8) y [README.md:701–702](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/README.md#L701-L702) enumeran dos integrantes, frente a tres en EQUIPOS del curso. No se infieren correspondencias por nombre ni se modifica la tabla individual histórica; matrícula y vínculo cuenta/persona pendientes. |

## Estado global del proyecto (overall)

Punta `5c643bd03f19630d6459da79fb13fb2d5f943c7b` de `master`. Cuatro commits del 7-oct posteriores a la base S9 congelada: renombres y nueva ubicación de auditoría; nuevo ADR-0007; índice/tabla de enmiendas; aclaraciones de IA/MLAnalyzer; nueva redacción experimental y estado de Gate declarado; corrección de clasificación de errores en el script de mutaciones. El delta no modifica `app/`, pruebas, workflows ni configuración productiva. El prototipo SAM, eventos y medición local ya estaban antes: no son implementación ni experimento nuevos por haberse ampliado el ADR.

### Observaciones actuales y límites

- GET https://verifacts-api.onrender.com/health iniciado el 2026-10-10T13:05:25Z: HTTP 200, 25,359958 s, cuerpo {"status":"ok"}. Una petición puntual; no se probó POST /analysis, ni se identificó la revisión desplegada, ni se infiere la causa de la latencia.
- [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824175) y [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824211): success, mismo hash revisado. Tests incluye pytest y build/smoke de Docker según workflow; SonarCloud incluye pytest/cobertura y scanner. No se ejecutó el script comparativo ni el de mutaciones como parte de esta revisión.
- El documento ahora declara Gate VERDE/OK y 99,1 % de cobertura con fecha 7-oct ([docs/despliegue.md:37](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/despliegue.md#L37)); se atribuye al equipo. Consulta pública del evaluador a https://sonarcloud.io/api/qualitygates/project_status?projectKey=ISCOUTB_AS_202620_Verifacts iniciada 2026-10-10T13:06:42Z: HTTP 403 en 5,059115 s; consulta a https://sonarcloud.io/api/project_analyses/search?project=ISCOUTB_AS_202620_Verifacts&ps=5 iniciada 13:06:48Z: HTTP 403 en 6,651586 s. No se pudo ligar el Gate a una revisión. Por tanto el Gate actual queda No verificado, no «rojo» ni «verde confirmado por el evaluador». El workflow ejecuta el scanner, pero no declara espera del Gate ([.github/workflows/sonarcloud.yml:26–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L26-L38); [sonar-project.properties:1–9](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/sonar-project.properties#L1-L9)).
- El recuento de autoría se refrescó hoy: 304 commits, tres firmas con 241/37/26; no se infieren personas por nombres. Se mantiene la discrepancia de dos integrantes declarados por el repositorio frente a tres del listado docente.
- Las constataciones del 6-oct sobre health, seguridad y CI anterior conservan valor histórico, pero no se presentan como observaciones de hoy.

### Correcciones verificadas y cierres acotados

- ADR-0006 renombrado a 0006-semantica-del-resultado.md sin alterar su contenido; auditoría trasladada a docs/ y arc42 §8 a nombre con guiones. Se resuelven las rutas específicas citadas antes en A-06/README; no se afirma que todos los enlaces estén comprobados. [docs/aspectos.md:25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/aspectos.md#L25); [README.md:185–191](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/README.md#L185-L191).
- ADR-0007 existe realmente y está indexado; evalúa alternativas generativas y mantiene el motor determinista. [docs/adr/0007-no-incorporar-componente-generativo.md:1–40](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0007-no-incorporar-componente-generativo.md#L1-L40); [docs/arc42/09-decisiones-arquitectonicas.md:18](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L18).
- MLAnalyzer queda rectificado como no implementado en IA y nota fechada de ADR-0002. [docs/ia.md:19](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L19); [docs/adr/0002-contextos-sin-cambios.md:36–43](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0002-contextos-sin-cambios.md#L36-L43).
- IA ya contiene el balance aceptado/corregido/rechazado con motivos y entradas del periodo; es corrección tardía respecto de S9. [docs/ia.md:23–46](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L23-L46).
- La tabla de enmiendas existe y declara adiciones históricas. Se cierra solo su ausencia documental, no la infracción de inmutabilidad. [docs/arc42/09-decisiones-arquitectonicas.md:20–27](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L20-L27).
- pytest-cov se añade al inventario de dependencias; persiste falta de versión fijada. [docs/auditoria-s9.md:44–51](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/auditoria-s9.md#L44-L51).
- El script de mutaciones distingue ahora retorno 1 de pytest (fallo de prueba) de otros códigos de infraestructura. Corrección estática real; no se ejecutó y no cambia la evaluación S9. [scripts/mutaciones_s9.py:33–40](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/scripts/mutaciones_s9.py#L33-L40).
- [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824175) y [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824211) están success para el nuevo hash. Sustituye las URLs de la punta anterior como evidencia CI actual; no cierra Gate.
- ADR-0005 ya identifica S10 y enumera hipótesis/variables/umbral. Cierra la ausencia de esos elementos declarativos, sin confirmar origen oficial ni validez experimental. [docs/adr/0005-comparacion-lambda-render.md:7–36](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L7-L36).

### Hallazgos abiertos

- Confirmar mediante la consigna docente que la comparación Render/Lambda es el escenario operativo asignado S10; el nuevo rótulo del equipo no basta como prueba independiente.
- Construir comparación realmente equivalente: mismo payload de 10.000 caracteres, runtime/carga definidos, cliente y métricas comparables; distinguir Render público, aplicación local y SAM emulado; separar frío/caliente y publicar series por operación con fecha y commit. [docs/adr/0005-comparacion-lambda-render.md:27–35](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L27-L35); [serverless-prototype/events/analysis_event.json:19](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/events/analysis_event.json#L19).
- No reutilizar como POST /analysis el P95 anteriormente rotulado GET /health sin nuevas series verificables; conservar salidas distintas con --out y explicar por qué Duration SAM no es automáticamente latencia real ni costo facturable AWS. [docs/adr/0005-comparacion-lambda-render.md:64–101](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L64-L101); [serverless-prototype/medir_cold_start.py:66–93](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/medir_cold_start.py#L66-L93).
- Registrar la evolución del ADR-0005 mediante nuevo ADR/reemplazo trazable y corregir causalidad de imports; la tabla de enmiendas ya existe, pero no cubre esa reescritura. [docs/arc42/09-decisiones-arquitectonicas.md:20–27](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L20-L27); [serverless-prototype/lambda_handler.py:1–5](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/lambda_handler.py#L1-L5).
- Actualizar arc42 §3/§10 y pendientes de aspectos/README para distinguir lo implementado, la medición local ya publicada y lo aún no medido en producción. [docs/arc42/03-contexto-y-alcance.md:112–118](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/03-contexto-y-alcance.md#L112-L118); [docs/arc42/10-requisitos-de-calidad.md:41–54](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/10-requisitos-de-calidad.md#L41-L54); [README.md:622–630](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/README.md#L622-L630).
- Proporcionar evidencia pública del Quality Gate asociada a la revisión y aclarar bloqueo de integración; la declaración OK es nueva, el revisor obtuvo 403. Scanner success no acredita gate ni protección de rama. [docs/despliegue.md:37](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/despliegue.md#L37).
- Fijar pytest-cov en el cierre de dependencias: ya aparece en el inventario de auditoría, pero el workflow conserva pip install pytest-cov sin versión y no está en requirements.txt. [docs/auditoria-s9.md:44–51](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/auditoria-s9.md#L44-L51); [.github/workflows/sonarcloud.yml:26–32](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L26-L32); [requirements.txt:1–7](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/requirements.txt#L1-L7).
- Demostrar persistencia/recuperación tras reinicio/redeploy y separar su costo del escenario gratuito: [docs/costos.md:14–18](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/costos.md#L14-L18) y [docs/costos.md:29–35](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/costos.md#L29-L35) reconocen almacenamiento efímero y despertar lento. Health puntual no prueba recuperación de datos.
- Aclarar matrícula y correspondencia de las firmas de Git con los integrantes; el recuento de firmas no permite concluir quién contribuyó o faltó.
- Completar la verificación de seguridad de árbol/historial fuera del alcance acotado de esta pasada; NV no es exposición confirmada.

## Delta S5→S10, sin recalificar entregas previas

[Comparación inmutable](https://github.com/ISCOUTB/AS_202620_Verifacts/compare/67f8cea03e6a7b827aced6b60d3af8cf4307b237...5c643bd03f19630d6459da79fb13fb2d5f943c7b): 70 commits. En ADR/arc42/C4, 15 rutas afectadas, 873 inserciones y 136 eliminaciones según Git, incluyendo renombre arc42 §8. Las vistas C4 actuales corresponden a frontend/API/SQLite ([docs/c4/02-contenedores.md:26–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/c4/02-contenedores.md#L26-L38); [docs/c4/03-componentes.md:19–30](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/c4/03-componentes.md#L19-L30)); el contrato sigue enlazado y probado por la suite ([docs/arc42/09-decisiones-arquitectonicas.md:38–47](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L38-L47)). Esto acredita evolución del proyecto, no elimina las contradicciones documentales ni prueba el resultado del escenario de corte.

## Para completar antes del cierre

Priorizar la consigna oficial, una comparación equivalente y auditable, y el registro correcto de la decisión. Conservar outputs separados y su manifiesto (commit, fecha, máquina/runtime, operación, payload, calentamiento, concurrencia, número de corridas y métrica). Actualizar arc42 y enlaces de evidencia para que el lector pueda distinguir medición local, emulación y producción. Aportar Gate/revisión verificables y demostrar en sustentación comportamiento tras inactividad y persistencia/recuperación. La elección de mantener Render puede ser válida, pero necesita su demostración.

## Tres preguntas para la sustentación

1. ¿Cómo distinguen el tiempo de activación de Render de duration_ms del middleware, y qué ocurre con el historial SQLite después de reiniciar o redeplegar? Demuéstrenlo en el entorno desplegado.
2. ¿Cómo cambiaría el punto de quiebre de costo si el POST usa realmente 10.000 caracteres y se separan invocaciones frías/calientes? ¿Qué parte de Duration medida en SAM están suponiendo facturable en AWS?
3. ¿Qué resultado de una comparación controlada les haría cambiar la decisión de mantener Render, y cómo registrarían ese cambio sin reescribir el ADR-0005 aceptado?

## Comandos sugeridos al equipo, no ejecutados por el revisor

Comprobación manual puntual del estudiante; no ejecutada como siguiente paso por el revisor. No mide P95.

```text
curl --connect-timeout 10 --max-time 60 -sS -w '
http=%{http_code} tiempo=%{time_total}s
' https://verifacts-api.onrender.com/health
```

Suite local del estudiante; comando revisado, no ejecutado por el revisor.

```text
python -m pytest -q
```

PowerShell, desde la raíz, con SAM CLI/Docker instalados. Antes, corregir el evento analysis a la misma carga de 10.000 caracteres y acordar el procedimiento comparativo; guardar manifiesto y series publicables. Estos comandos solo producen emulación local, no despliegan AWS, y no fueron ejecutados por el revisor.

```text
Set-Location serverless-prototype
Copy-Item -Recurse ..\app .\app
sam build --use-container
python medir_cold_start.py --runs 15 --event events/health_event.json --out cold_start_health.csv
python medir_cold_start.py --runs 15 --event events/analysis_event.json --out cold_start_analysis.csv
```

## Precisión metodológica del recuento de contribuciones

Verificación adicional del 2026-10-10T13:15Z: git rev-list --count da 300 en la base 4f065229 y 304 en 5c643bd0, delta exacto 4. Incluye merges: 6 en ambos; sin merges son 294 y 298. Las firmas crudas contadas mediante git log --format=%an son 241/33/26 en la base y 241/37/26 en la punta, sin .mailmap en ninguno y sin consolidar nombres como personas. No hay aparición de nueva firma en el delta. La identificación histórica 240+31 corresponde a otro recuento antiguo; la planilla publicada ya contiene actualización agregada del 6-oct con 300 (241/33/26). No se altera la tabla individual histórica ni se atribuyen identidades por parecido.

</details>
