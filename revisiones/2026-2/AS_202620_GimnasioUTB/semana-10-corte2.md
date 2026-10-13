# Segundo corte · S10 · GimnasioUTB · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_GimnasioUTB |
| Rama evaluada | `main` |
| Hash calificado | `46742e5feaa3c8a06b7aebeb7a31fb93628e40b6` |
| Fecha del commit | 2026-10-11T14:41:07-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

S1: consistencia del contador de aforo con20 entradasconcurrentes (antecedenteS9, pertinenciaS10 supuestoexplícito)

Se evalúa técnicamente el escenario declarado; no se afirma asignación docente verificada.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Básico | 0,60 / 1,00 |
| C2 · Decisión e implementación | Competente | 0,80 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Básico | 0,60 / 1,00 |
| C4 · Evolución arquitectónica trazable | Competente | 0,80 / 1,00 |
| C5 · Sustentación del reto | Calificación comunicada por el docente | 0,76 / 1,00 |

**Subtotal técnico: 2,80 / 4,00. Total consolidado C1–C5: 3,56 / 5,00.**

Calificación de sustentación comunicada por el docente: **3,80 / 5,00**, incorporada como **C5 = 0,76 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

La concurrencia con PostgreSQL y FOR UPDATE tiene implementación y ADR coherentes. La instrumentación es parcial y el CI no ejecuta la prueba PostgreSQL del escenario. Hay actualización operacional, pero no un experimento nuevo completo sobre el despliegue.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/s9-cadena-verificada.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/docs/s9-cadena-verificada.md#L7-L34) — C1
2. [docs/adr/0004-concurrencia-postgresql.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/docs/adr/0004-concurrencia-postgresql.md#L13-L81) — C2
3. [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/.github/workflows/ci.yml#L15-L23) — C3

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** No se observó deriva material en el backend de aforo examinado. Las vistas vigentes separan explícitamente el contador implementado de Flutter, QR, autenticación y notificaciones futuros.

**Arquitectura declarada:** Monolito Node/Express con puertos y adaptadores. Un módulo de aforo, dominio puro y transacción PostgreSQL síncrona respecto de la respuesta HTTP; Compose/Dokploy y observabilidad por proceso.

**Arquitectura implementada:** src/server.js monta /api/v1/aforo e inyecta los casos de uso; el arranque ejecutable inyecta AforoPostgresAdapter. POST → router → registrarAcceso → actualizarAforo(callback de dominio) → BEGIN/SELECT FOR UPDATE/UPDATE/COMMIT. GET usa caso de consulta. createApp sin argumentos usa memoria para pruebas, como se declara.

**Hallazgos materiales: 0.** No se observó deriva material en los recorridos inspeccionados; esto no acredita conformidad exhaustiva ni ejecución correcta en producción.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Seguidas ambas rutas reales desde server.js al router, caso de uso, puerto y adaptador. No se encontró import de Express/pg en el caso de uso examinado; no se confunde composition root con fuga de infraestructura.

**Persistencia:** Se revisó adaptador PostgreSQL, transacción, rollback y selección en arranque. No se validó ejecución ni supervivencia del volumen tras redeploy.

**API y autorización:** README/OpenAPI contrastados con GET y POST; 400 de dominio/JSON y 503 de repositorio existen. Autenticación/identidad se declaran futuras y no se califican como deriva.

**Despliegue:** Compose contiene PostgreSQL, inicializador y API dependiente de db-init; la API chequea /ready. Panel/proxy/TLS efectivos no verificados.

**Asincronía:** await de persistencia antes del 201; WebSocket y FCM fuera de alcance explícito. APIs async de Node no equivalen a comunicación por eventos.

**Observabilidad:** /health estático, /ready lee repositorio y /metrics cuenta accesos locales; logs y cierre SIGTERM presentes. No se infiere SLA, p95 ni métricas persistentes.

**Fuentes de la cobertura:**

- [README.md:5–26](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/README.md#L5-L26)
- [docs/adr/0001-arquitectura-hexagonal.md:15–41](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/docs/adr/0001-arquitectura-hexagonal.md#L15-L41)
- [docs/adr/0003-comunicacion-sincrona-asincrona.md:13–26](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/docs/adr/0003-comunicacion-sincrona-asincrona.md#L13-L26)
- [docs/arc42/arc42_gimnasio_utb.md:97–114](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/docs/arc42/arc42_gimnasio_utb.md#L97-L114)
- [docs/c4/C4_Level3.md:36–48](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/docs/c4/C4_Level3.md#L36-L48)
- [docs/openapi.yaml:83–113](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/docs/openapi.yaml#L83-L113)
- [src/server.js:25–65](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/src/server.js#L25-L65)
- [src/server.js:70–88](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/src/server.js#L70-L88)
- [src/modules/aforo/infrastructure/http/aforo.router.js:14–61](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/src/modules/aforo/infrastructure/http/aforo.router.js#L14-L61)
- [src/modules/aforo/application/registrar-acceso.usecase.js:1–19](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/src/modules/aforo/application/registrar-acceso.usecase.js#L1-L19)
- [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js:39–59](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js#L39-L59)
- [deploy/compose.lab.yaml:22–55](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6/deploy/compose.lab.yaml#L22-L55)

**Límites adicionales:** Auditoría estática nueva del SHA indicado mediante git show, sin checkout ni ejecución de código estudiantil, sin lectura de PDF, sin publicar ni cambiar notas. No se verificaron el runtime desplegado, secretos/configuración de panel, cargas, CI en vivo ni disponibilidad. Los documentos de pruebas aportan intención y alcance, no una ejecución independiente de esta auditoría.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:59.849908+00:00 confirmó el hash anterior como último commit de `main` antes del límite exclusivo. La punta observada es [`46742e5feaa3c8a06b7aebeb7a31fb93628e40b6`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6) (2026-10-11T14:41:07-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Semana 10 · Segundo corte · GimnasioUTB

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_GimnasioUTB |
| Estado revisado | `c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec` en `origin/main` (2026-10-05T18:16:08-05:00) |
| Rama remota principal | `origin/main` |
| Observación | 2026-10-06T21:31:50.150883+00:00 |
| Punta revisada para S10 | `c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec` (2026-10-05T18:16:08-05:00) |
| S9 congelado, solo como línea base | `af4796d6320766611d9fc01d7112a1c0e4112b40` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** Se encontró S1 (20 transiciones concurrentes del contador) y su verificación S9; no una fuente que lo identifique como escenario operativo asignado para el segundo corte. Fuente o búsqueda: [docs/s9-cadena-verificada.md:3-20](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/s9-cadena-verificada.md#L3-L20); [docs/arc42/arc42_gimnasio_utb.md:268-285](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/arc42/arc42_gimnasio_utb.md#L268-L285); búsqueda textual en README, ADR y documentos de evidencia. La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `9b9f7c8160ee18d97eb933357cfb05c3e942ad4e`: el delta hasta esta punta modifica 54 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta de main c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec, anterior al cierre futuro; identificación preliminar, no congelación definitiva. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://gimnasio-utb.iscoutb.dev/health: HTTP 200 en 6.266 s; /ready: 200 en 4.817 s; /metrics: 200 en 5.310 s. Comprobación iniciada 2026-10-06T21:16:54Z. URL publicada en [README.md:40-46](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L40-L46). No se probó el flujo mutante de acceso. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Se encontró S1 (20 transiciones concurrentes del contador) y su verificación S9; no una fuente que lo identifique como escenario operativo asignado para el segundo corte. [docs/s9-cadena-verificada.md:3-20](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/s9-cadena-verificada.md#L3-L20); [docs/arc42/arc42_gimnasio_utb.md:268-285](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/arc42/arc42_gimnasio_utb.md#L268-L285); búsqueda textual en README, ADR y documentos de evidencia |
| Línea base medida y reproducible | No verificado | [docs/s9-cadena-verificada.md:22-44](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/s9-cadena-verificada.md#L22-L44) permite reproducir la prueba del adaptador, pero no se puede identificarla como línea base del reto asignado. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0004-concurrencia-postgresql.md:57-81](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/adr/0004-concurrencia-postgresql.md#L57-L81) justifica la concurrencia; [docs/arc42/arc42_gimnasio_utb.md:249-255](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/arc42/arc42_gimnasio_utb.md#L249-L255) reconoce que Dokploy carece de ADR independiente. Falta correspondencia con el reto S10. |
| Respuesta implementada o configurada sobre el MVP | No verificado | Hay backend transaccional y Compose posterior a S9; [README.md:40-46](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L40-L46). Sin asignación confirmada no se acredita que sea la respuesta al reto. |
| Resultado contrastado con el umbral | No verificado | [docs/arc42/arc42_gimnasio_utb.md:268-285](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/arc42/arc42_gimnasio_utb.md#L268-L285) acota la medición S1 y declara otras métricas no medidas; falta umbral del reto confirmado. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Health/ready y métricas HTTP fueron accesibles; logs JSON declarados en [README.md:70-88](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L70-L88). El contador de operaciones no mide pérdida de actualizaciones: [docs/arc42/arc42_gimnasio_utb.md:237-241](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/arc42/arc42_gimnasio_utb.md#L237-L241). CI sin PostgreSQL ni Sonar y métrica del escenario asignado pendiente. |
| Secretos protegidos | Cumple | Barrido estático del árbol textual, incluidos ejemplos y documentación: sin candidatos de credenciales reales; no hay .env versionado. [.github/workflows/ci.yml:11-23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/.github/workflows/ci.yml#L11-L23) y variables de entorno en [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js:14-27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js#L14-L27). Los PDF se excluyeron. No equivale a una certificación exhaustiva de secretos. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/arc42/arc42_gimnasio_utb.md:249-255](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/arc42/arc42_gimnasio_utb.md#L249-L255) reconoce deployment Dokploy sin ADR independiente; [docs/aspectos.md:29-35](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/aspectos.md#L29-L35) sigue sin cadena navegable completa. La alineación de arc42 distingue ahora implementación y futuro. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | No se localizó decisión anterior confirmada/reemplazada por la medición de un reto S10 identificado. [docs/arc42/arc42_gimnasio_utb.md:247-285](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/arc42/arc42_gimnasio_utb.md#L247-L285). |
| Sustentación del reto sobre el entorno desplegado | No verificado | La sustentación y la ejecución del pipeline en vivo las observa y califica el docente. |

Recuento descriptivo: 3 Cumple, 1 No cumple y 8 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Falta confirmar el reto asignado; S1 verificado en adaptador no se presume reto S10. |
| Decisión e implementación | No verificado | Pendiente | ADR-0004 y código reales; falta evaluar adecuación y costo respecto de la asignación. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Sondas 200 y JSON presentes; falta run actual verificable y métrica del reto. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Actualización tardía de arc42 presente; cadena de aspectos y ADR de despliegue incompletos. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | Pendiente de sesión docente sobre despliegue y pipeline en vivo. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_GimnasioUTB; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Árbol Git con README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md; índice en [README.md:108-121](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L108-L121). |
| Estado calificado identificable | Cumple | Punta preliminar origin/main c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec; fecha anterior al cierre futuro S10. No modifica S9. |
| Nombres de ADR según la convención | No cumple | [docs/adr/ADR0001.md:1-8](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/adr/ADR0001.md#L1-L8) no sigue NNNN-titulo-en-kebab-case y duplica el número de [docs/adr/0001-arquitectura-hexagonal.md:1-5](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/adr/0001-arquitectura-hexagonal.md#L1-L5). |
| ADR aceptados no reescritos | No cumple | El ADR-0001 ya aceptado sigue reescrito sin reemplazo: historial verificado en [3fae092f](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/3fae092fe6d33872772f106dc2737f88339ba82c) y estado canónico [docs/adr/0001-arquitectura-hexagonal.md:1-15](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/adr/0001-arquitectura-hexagonal.md#L1-L15). La punta añade otra edición tardía. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:100-112](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/ia.md#L100-L112) incorpora S9 con correcciones/rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [README.md:86-88](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L86-L88) declara ausencia de PostgreSQL en CI y de SonarCloud/Quality Gate; no se verificó run de esta punta. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Barrido estático del árbol textual, incluidos ejemplos y documentación: sin candidatos de credenciales reales; no hay .env versionado. [.github/workflows/ci.yml:11-23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/.github/workflows/ci.yml#L11-L23) y variables de entorno en [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js:14-27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js#L14-L27). Los PDF se excluyeron. No equivale a una certificación exhaustiva de secretos. El recorrido histórico ampliado está pendiente de completar; no se afirma ausencia histórica por el resultado del árbol actual. |
| Contribución de todos los integrantes | No verificado | Historial agregado a la punta: 5 grupos por correo idéntico frente a 3 integrantes; firmas distintas no se atribuyen por semejanza. Se requiere confirmar correspondencia cuenta–persona, sin publicar correos. |

## Estado global del proyecto (overall)

Punta observada de `origin/main`: `c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec` (2026-10-05T18:16:08-05:00). Hay 3 commits posteriores al estado congelado S9. Después del cierre se añadieron Dockerfile/Compose y documentación de Dokploy; las sondas públicas responden. Esto cierra deuda operativa en la punta, pero no altera S9. [README.md:40-46](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L40-L46) distingue PostgreSQL de Compose, UI sin integración y ausencia de prueba de retención tras redeploy.

- Convertir aspectos en cadena de ocho columnas con enlaces reales a C4, código, prueba y medición.
- Formalizar mediante ADR la decisión de no incorporar generación y la plataforma Dokploy.
- Incluir PostgreSQL real en CI y aportar scanner, run y Quality Gate público.
- Conservar ADR aceptados y resolver duplicación del 0001. Confirmar cuentas sin inferir personas.
- Identificar el escenario asignado de S10 y levantar una línea base del despliegue.

### Hallazgos anteriores cerrados o delimitados

- Ya existe registro IA S9 con rechazo técnico y auditoría de erosión; V1 y V2 están corregidas en código.
- La prueba de fallo por pérdida de bloqueo está documentada; no sigue simplemente «sin evidencia».
- En la punta posterior al cierre ya existen Dockerfile, Compose, URL pública y arc42 de despliegue; no modificar notas S8/S9 por ello.

## Preparación de la sustentación

1. Fallo: si PostgreSQL deja de responder o el pool se agota, ¿qué timeout y señal operativa impedirán que las solicitudes queden esperando indefinidamente?
2. Costo: ¿qué recursos consume el Compose completo y cuál es el límite que obliga a abandonar el alojamiento sin costo?
3. Medición: ¿qué cambiarían al pasar de 20 llamadas directas al adaptador a carga HTTP y qué resultado justificaría esa decisión?

## Próximos pasos

El despliegue responde a las sondas de salud y disponibilidad. Para el segundo corte, identifiquen el escenario operativo asignado y midan su línea base y respuesta en ese entorno; la prueba del adaptador y el contador de operaciones no sustituyen una medición del flujo HTTP. Formalicen el despliegue en ADR y preparen el pipeline en vivo.

</details>
