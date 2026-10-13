# Segundo corte · S10 · DinamikUTB · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_DinamikUTB |
| Rama evaluada | `master` |
| Hash calificado | `5dc9acf9335fec70e274a2e5c494b3805b0e9646` |
| Fecha del commit | 2026-10-05T22:06:45-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

Q-01: exactitud de requisitos; Q-05 como soporte operacional

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

El resultado declarado de 20/20 no coincide con el CI fallido y no constituye una línea base operacional. Hay health check, JSON y métricas, pero las cadenas arquitectónicas están incompletas y algunos controles documentados no están implementados.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencia-s9.md:25–29](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/evidencia-s9.md#L25-L29)
2. [backend/app/main.py:38–80](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/main.py#L38-L80)
3. [docs/aspectos.md:9–18](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/aspectos.md#L9-L18)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** Una vista C4 rezagada. No se hallaron escrituras cruzadas entre Requisitos y Estudiantes en el recorrido inspeccionado. La ausencia de autenticación está declarada y limitada a datos sintéticos; no se presentó como erosión nueva ni como acceso real a estudiantes.

**Arquitectura declarada:** Monolito modular FastAPI/Flutter, servicios por contexto; SQLite local/PostgreSQL Render según ADR7. Usuarios, Programas y Ayuda previstos.

**Arquitectura implementada:** Frontend RequisitosService→GET /requisitos→service→SQLAlchemy; PUT modifica por ID en el servicio. Main incorpora routers Requisitos/Estudiantes, health SQL y métricas HTTP.

**Hallazgos materiales: 1.** Prioridad máxima: **Baja**.

<a id="deriva-d1"></a>

### D1 · C4 muestra SQLite sin distinguir PostgreSQL del ambiente desplegado

**Naturaleza:** documentación desactualizada. **Prioridad:** Baja. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** README y ADR7 ya aclaran correctamente los dos ambientes; la desalineación queda en una vista.

**Declaración contrastada:**

- [docs/c4/contenedores.puml:11–21](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/c4/contenedores.puml#L11-L21) — El C4 de contenedores muestra una sola BD SQLite sin distinguir el entorno PostgreSQL desplegado.

**Implementación contrastada:**

- [docs/adr/0007-persistencia-render-postgres.md:27–33](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/adr/0007-persistencia-render-postgres.md#L27-L33) — ADR7 elige PostgreSQL en Render y conserva SQLite para desarrollo local mediante DATABASE_URL.
- [backend/app/core/database.py:7–21](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/core/database.py#L7-L21) — La conexión acepta postgres/postgresql y los adapta a psycopg, aunque el fallback local sea SQLite.

**Efecto y alcance:** Puede inducir una configuración de almacenamiento equivocada si C4 se lee de forma aislada.

**Corrección propuesta:** Separar en C4 SQLite local y PostgreSQL desplegado y marcar como previstos los módulos sin implementación. Conservar ADR3 como historia y enlazar ADR7 vigente.

### Cobertura y límites de la auditoría

**Capas y dominio:** Requisitos escribe su entidad y Estudiantes se mantiene separado; relaciones futuras se distinguen explícitamente del código.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [docs/arc42/08-cross-cutting-concepts.md:39–53](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/arc42/08-cross-cutting-concepts.md#L39-L53) — arc42 distingue las relaciones diseñadas de las implementadas y marca Usuarios/Programas/Ayuda sin código.
- [backend/app/requisitos/router.py:15–31](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/requisitos/router.py#L15-L31) — GET y PUT de requisitos delegan consulta/actualización al servicio con una sesión de BD.
- [backend/app/requisitos/service.py:1–20](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/requisitos/service.py#L1-L20) — El servicio consulta y actualiza únicamente Requisito mediante SQLAlchemy.

**Persistencia:** DATABASE_URL normalizada a psycopg; SQLite por defecto local. No se exigió inversión hexagonal a un monolito que la descartó.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/app/core/database.py:7–24](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/core/database.py#L7-L24) — La configuración normaliza URLs PostgreSQL a psycopg y crea engine/sessionmaker, con SQLite por defecto.
- [docs/adr/0007-persistencia-render-postgres.md:27–33](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/adr/0007-persistencia-render-postgres.md#L27-L33) — ADR7 elige PostgreSQL en Render y conserva SQLite para desarrollo local mediante DATABASE_URL.

**API y autorización:** Routers solo inyectan DB; README reconoce ausencia de auth y prohíbe datos reales. Tabla de tácticas de seguridad debe leerse como diseño pendiente, no implementación.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/app/requisitos/router.py:10–31](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/requisitos/router.py#L10-L31) — El router inyecta get_db y no incluye una dependencia de autenticación en las operaciones mostradas.
- [README.md:351–355](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/README.md#L351-L355) — README declara que no existe autenticación y restringe el entorno desplegado a datos de ejemplo.
- [docs/arc42/08-cross-cutting-concepts.md:45–53](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/arc42/08-cross-cutting-concepts.md#L45-L53) — La tabla de implementación solo marca Requisitos y Estudiantes con código funcional.

**Despliegue:** Render/Postgres declarado, DATABASE_URL externa; C4 desactualizado identificado.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [docs/adr/0007-persistencia-render-postgres.md:27–40](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/adr/0007-persistencia-render-postgres.md#L27-L40) — ADR7 describe separación SQLite local/Postgres desplegado, recreación periódica y trazabilidad a database.py/render.yaml.
- [backend/app/core/database.py:16–21](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/core/database.py#L16-L21) — database.py lee DATABASE_URL y usa sqlite:///./dinamikutb.db como valor local por defecto.

**Asincronía:** Cliente HTTP async en Dart, endpoint y SQL síncronos; async de lenguaje no implica mensajería ni microservicios.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [frontend/lib/requisitos/requisitos_service.dart:14–25](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/frontend/lib/requisitos/requisitos_service.dart#L14-L25) — El cliente Flutter llama GET /requisitos/{estudianteId} y deserializa la lista recibida.
- [backend/app/requisitos/router.py:15–31](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/requisitos/router.py#L15-L31) — GET y PUT de requisitos delegan consulta/actualización al servicio con una sesión de BD.

**Observabilidad:** Middleware mide HTTP, /health ejecuta SELECT 1 y /metrics texto; no se verificó exposición ni telemetría real.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/app/main.py:38–54](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/main.py#L38-L54) — El middleware registra método, ruta, status y duración de cada petición HTTP.
- [backend/app/main.py:69–80](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/main.py#L69-L80) — /health ejecuta SELECT 1 con respuesta 503 ante fallo; /metrics devuelve texto Prometheus.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:54.161744+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`5dc9acf9335fec70e274a2e5c494b3805b0e9646`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/5dc9acf9335fec70e274a2e5c494b3805b0e9646) (2026-10-05T22:06:45-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Segundo corte S10 · avance preliminar · DinamikUTB

**Preliminar, no es cierre ni calificación final.** Cierre previsto: **2026-10-12T05:00:00Z**.

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_DinamikUTB](https://github.com/ISCOUTB/AS_202620_DinamikUTB) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `72bfc7e206eac4147dd244c03fa09b4b32b9a7e7` |
| Base S8 | `287c65d46a8469142baf5dc57da296c0bc80e0fb` |
| Estado revisado | `5dc9acf9335fec70e274a2e5c494b3805b0e9646` en `origin/master` (2026-10-05T22:06:45-05:00) |
| S9 congelada | `2326dd7f9d4dda08ba557ea6602b0a7085c97bee` · 2026-10-04T21:47:16-05:00 |
| Punta actual / S10 preliminar | `5dc9acf9335fec70e274a2e5c494b3805b0e9646` · 2026-10-05T22:06:45-05:00 |
| Comprobación | 2026-10-06T21:23:08Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Evolución desde S5 hasta la punta

Base tomada del informe S5 publicado y resuelta por Git, sin etiquetas: `72bfc7e206eac4147dd244c03fa09b4b32b9a7e7`. En el delta S5→HEAD cambian 66 rutas no PDF (conteo de árboles; no mide mérito). Desde S5 hay contrato API y sus pruebas, despliegue Render/PostgreSQL y GitHub Pages, health con base de datos, logs JSON y métricas. La punta añade pruebas de Q-01, pero su CI falla; no se recalifican S6–S9 por existir.

## Escenario operativo asignado

No verificado. La búsqueda en README, ADR, evidencia-s9, aspectos y arc42 encontró Q-01 y Q-05 generales, pero no una asignación operativa oficial de S10 al equipo. Se requiere esa consigna para evaluar hipótesis/respuesta sin inventarla.

## Matriz de evidencia S10

Se omite la fila de PDF de dos páginas por exclusión docente. Quedan 12 filas observables o pendientes; este recuento no es una fórmula de nota.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | HEAD master identificable y anterior al cierre futuro; estado preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | URL declarada en [README.md:357–363](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/README.md#L357-L363); GET /health a las 2026-10-06T21:23:08Z: HTTP 200, 11.443435 s, JSON status=ok. Una primera solicitud agotó tiempo; esta respuesta no prueba flujo de negocio ni disponibilidad sostenida. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Q-01/Q-05 son objetivos generales; no se identificó asignación docente específica S10; [docs/aspectos.md:11–15](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/aspectos.md#L11-L15). |
| Línea base medida y reproducible | No verificado | No hay línea base identificada del escenario asignado. El conteo de tests de Q-01 no se sustituye por línea base operacional; [docs/evidencia-s9.md:25–29](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/evidencia-s9.md#L25-L29). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | Existen ADR de plataforma y de verificación IA, pero no se confirma decisión para el reto asignado, aún desconocido; [docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md:51–57](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md#L51-L57). |
| Respuesta implementada o configurada sobre el MVP | No verificado | Desde S5 se incorporan contrato API, Render/PostgreSQL, logs y métricas; la punta amplía pruebas y fija acciones, todavía sin vínculo confirmado con escenario asignado; [backend/tests/test_requisitos.py:83–167](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/tests/test_requisitos.py#L83-L167). |
| Resultado contrastado con el umbral | No verificado | La evidencia actual afirma 20/20 después del cierre S9, pero CI HEAD falla; no se acredita resultado operativo ni resultado global verde. Además un caso usa id no entero y espera 404 mientras el router exige int; [backend/tests/test_requisitos.py:157–167](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/tests/test_requisitos.py#L157-L167), [backend/app/requisitos/router.py:20–30](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/requisitos/router.py#L20-L30). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | Hay health con SELECT 1, logs JSON y métricas, pero CI HEAD falla y no se vinculó métrica con reto S10; [backend/app/main.py:38–80](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/backend/app/main.py#L38-L80). Persisten lectura/escritura sin autenticación, reconocidas en [docs/arc42/11-risks-and-technical-debt.md:7–13](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/arc42/11-risks-and-technical-debt.md#L7-L13). |
| Secretos protegidos | Cumple | Sin secretos reales en snapshot actual; se conserva el límite de no certificar toda la historia. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | A-01 mejora pero otras cadenas siguen Pendiente y faltan vínculos navegables de código/pruebas. La documentación de seguridad describe controles todavía no implementados; [docs/aspectos.md:9–18](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/aspectos.md#L9-L18), [docs/arc42/11-risks-and-technical-debt.md:7–13](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/arc42/11-risks-and-technical-debt.md#L7-L13). |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | ADR-0008 declara que no reemplaza decisiones y no hay demostración correspondiente al reto asignado; [docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md:51–69](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md#L51-L69). |
| Sustentación del reto sobre el entorno desplegado | No verificado | Pendiente del docente en sustentación sobre despliegue y pipeline en vivo. |

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
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público ISCOUTB/AS_202620_DinamikUTB, rama master; [README.md:1–5](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Las seis rutas mínimas están presentes; arc42 01–12 y C4 en fuentes PlantUML, [docs/aspectos.md:9–18](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/aspectos.md#L9-L18). |
| Estado calificado identificable | Cumple | Punta master 5dc9acf9335fec70e274a2e5c494b3805b0e9646 de 2026-10-05T22:06:45-05:00; preliminar anterior a cierre S10. |
| Nombres de ADR según la convención | Cumple | Los nueve ADR cumplen NNNN-kebab-case; [docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md:1–9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md#L1-L9), [docs/adr/0009-no-incorporacion-componente-generativo.md:1–9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0009-no-incorporacion-componente-generativo.md#L1-L9). |
| ADR aceptados no reescritos | No verificado | Hay ediciones históricas de ADR-0001/0002/0005/0006; falta terminar contraste independiente de las versiones aceptadas. No se presume cerrado el arrastre de inmutabilidad. |
| docs/ia.md al día para la semana | Cumple | La punta añade entrada específica de hash inventado, verificado y rechazado, junto al registro de trabajo S9; [docs/ia.md:14–16](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/ia.md#L14-L16), [docs/ia.md:39–39](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/ia.md#L39-L39). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI de HEAD concluye failure aunque Deploy frontend success. Configuración y scanner existen; no se acredita pipeline integral en verde ni Quality Gate de esta revisión; [.github/workflows/ci.yml:55–78](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/.github/workflows/ci.yml#L55-L78). |
| Sin credenciales en el repositorio ni en el historial | No verificado | Barrido del snapshot sin valores de credencial: solo secretos de Actions y permisos id-token. Sin .env versionado. Historial completo no certificado. |
| Contribución de todos los integrantes | No verificado | Siete firmas, 294 commits agregados en S9. Variantes de identidad no equivalen a siete personas; falta correspondencia verificable completa con los cuatro integrantes. Punta actual: 7 firmas y 299 commits agregados; no equivalen automáticamente a personas. |

## Actions en la punta actual

- [CI: failure](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/37407435759), 2026-10-06T03:06:47Z, SHA exacto del estado indicado.
- [Deploy frontend (GitHub Pages): success](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/37407435758), 2026-10-06T03:06:47Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Lectura estática del código, ejemplos y documentación: las coincidencias son SONAR_TOKEN del almacén de Actions y permiso id-token, no valores de secretos. No hay .env versionado. No se certificó todo el historial; esa limitación es transversal, no se descuenta de la fila S9 comprobada en snapshot.

## Estado global del proyecto (overall)

S9 aporta nueva verificación documental, política de identificadores oficiales, auditoría y decisión sobre IA generativa; no cambia producción. Después del cierre se añadieron casos para Q-01, entradas de IA, ampliación de inventario y documentación de despliegue. Esa mejoría es tardía y no cambia S9. La punta declara 20/20, pero su CI falla: hay que conciliar la afirmación con un run exacto y corregir el caso de id no entero. Las rutas académicas siguen sin autenticación; los documentos limitan el despliegue a datos ficticios, sin que el revisor consulte registros personales.

El delta S9 contiene 9 commits respecto de S8; hay 5 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Antes del cierre

- Aportar escenario S10 asignado, línea base y experimento reproducible sobre el MVP.
- Corregir CI HEAD y adjuntar resultados de las pruebas ampliadas; no declarar 20/20 solo por contarlas.
- Convertir rutas de código/pruebas de A-01 en enlaces y verificar cadena completa con medición.
- Terminar controles de identidad y autorización antes de cargar información real; mantener datos ficticios mientras tanto.
- Comprobar Quality Gate público y fijar fecha real de vencimiento/renovación de la base Render.

## Tres preguntas de sustentación

1. ¿Qué sucede con Q-01 y /health si Render pierde PostgreSQL o expira la instancia, y cómo demostrarían recuperación sin datos reales?
2. ¿Cuál es la fecha concreta de expiración de la base gratuita y qué opción conserva datos dentro del presupuesto?
3. ¿Qué cambiarían en la estrategia de pruebas al descubrir que contar 20 casos no garantiza un run verde ni cubre autorización?

</details>
