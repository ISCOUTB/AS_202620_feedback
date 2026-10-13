# Segundo corte · S10 · LaPlacita · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_LaPlacita |
| Rama evaluada | `master` |
| Hash calificado | `2c711d44b31a41a09306f7840da480a21e8c749a` |
| Fecha del commit | 2026-10-12T17:41:41-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

ESC-01: supervivencia y consistencia de pedidos tras reinicio, subconjunto del escenario de picos

Se evalúa técnicamente el escenario declarado; no se afirma asignación docente verificada.

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

El nuevo ensayo de staging acredita tres supervivientes de tres y corrige el arranque antes del POST. El UPSERT sigue sin orden garantizado y la respuesta HTTP no espera la durabilidad. C4 conserva PostgreSQL como planeado.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencias/evidencias-s10.md:49–91](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/evidencias/evidencias-s10.md#L49-L91)
2. [backend/app/api/v1/pedidos/route.js:9–21](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/app/api/v1/pedidos/route.js#L9-L21)
3. [backend/src/metricas.js:1–27](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/metricas.js#L1-L27)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** Monolito modular e integración síncrona entre módulos siguen vigentes. PostgreSQL ya existe como espejo/rehidratación opcional y la confirmación en segundo plano es una limitación aceptada. Hay deriva documental en C4 y una garantía de orden de escrituras que el adaptador no implementa.

**Arquitectura declarada:** Cinco contextos en un backend Next.js; llamadas ESM síncronas y dueño único Pedidos para estado/PIN. ADR0014 incorpora PostgreSQL en Dokploy; API Azure. Redis, identidad de tenant y clientes completos siguen pendientes.

**Arquitectura implementada:** Los Route Handlers llaman a funciones públicas de módulos, sin pasar por corte-vertical.js (ese archivo es un ejecutable de demostración). POST pedidos espera rehidratación y llama crearPedido; este modifica Map y lanza espejo SQL. Confirmación de pago y entrega usan métodos de intención. PostgreSQL se carga al arranque del módulo; el proceso mantiene estado local y writes en vuelo.

**Hallazgos materiales: 2.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · C4 conserva PostgreSQL planeado y un protocolo de persistencia incorrecto

**Naturaleza:** documentación desactualizada. **Prioridad:** Baja. **Confianza:** Alta: comparación directa de vistas y código..

**Motivo de prioridad:** Baja: el código y el ADR reciente coinciden; la discrepancia está en las vistas que guían operación y mantenimiento.

**Declaración contrastada:**

- [docs/c4/contenedores.md:18–33](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/c4/contenedores.md#L18-L33) — C4 presenta PostgreSQL como planeado y dibuja REST hacia la BD.
- [docs/c4/componentes.md:20–26](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/c4/componentes.md#L20-L26) — C4 de componentes aún clasifica PostgreSQL como futuro.

**Implementación contrastada:**

- [docs/adr/0014-base-de-datos-postgresql-dokploy.md:48–58](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/adr/0014-base-de-datos-postgresql-dokploy.md#L48-L58) — ADR0014 ya adopta PostgreSQL gestionado con Dokploy y DATABASE_URL.
- [backend/src/persistencia/index.js:92–108](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/persistencia/index.js#L92-L108) — El adaptador abre Pool pg y carga pedidos mediante SQL.
- [backend/src/modules/pedidos/index.js:14–16](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/modules/pedidos/index.js#L14-L16) — Pedidos importa el adaptador de escritura y rehidratación.

**Efecto y alcance:** La vista de contenedores clasifica PostgreSQL como futuro y dibuja HTTP REST/JSON a la BD; la de componentes también lo marca planeado. ADR0014 y el adaptador actual ya contienen conexión pg y SQL, por lo que onboarding y análisis de fallos parten de una topología vieja.

**Corrección propuesta:** Actualizar C4 con PostgreSQL implementado condicional a DATABASE_URL, relación PostgreSQL/TCP mediante pg, Maps como cache/estado local y espejo asíncrono. Mantener Redis y auth marcados futuros.

<a id="deriva-d2"></a>

### D2 · La supuesta cola de persistencia inicia UPSERT independientes

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta sobre ausencia de encadenamiento; media sobre manifestación de reordenamiento bajo carga..

**Motivo de prioridad:** Media: falta una garantía de orden de persistencia del estado del pedido; existe riesgo plausible de estado atrasado, pero no se reprodujo ni se observó pérdida efectiva.

**Declaración contrastada:**

- [docs/adr/0014-base-de-datos-postgresql-dokploy.md:18–20](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/adr/0014-base-de-datos-postgresql-dokploy.md#L18-L20) — El requisito exige conservar el último estado confirmado.
- [docs/evidencias/evidencias-s10.md:168–176](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/evidencias/evidencias-s10.md#L168-L176) — La ventana de pérdida por crash está aceptada, pero no una inversión de orden sin crash.

**Implementación contrastada:**

- [backend/src/persistencia/index.js:49–54](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/persistencia/index.js#L49-L54) — El comentario promete una cola de UPSERT encadenados.
- [backend/src/persistencia/index.js:188–210](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/persistencia/index.js#L188-L210) — Cada escritura arranca inmediatamente; ultimaEscritura solo se reemplaza.
- [backend/src/persistencia/index.js:162–185](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/persistencia/index.js#L162-L185) — escribirFila envía el UPSERT al pool sin comprobar versión causal.
- [backend/src/modules/pedidos/index.js:108–117](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/modules/pedidos/index.js#L108-L117) — Cada transición del pedido dispara una escritura.
- [backend/app/api/v1/pagos/\[pedidoId\]/confirmar/route.js:10–21](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/app/api/v1/pagos/%5BpedidoId%5D/confirmar/route.js#L10-L21) — La ruta de confirmación llega al módulo de pagos y responde sin esperar el espejo SQL.

**Efecto y alcance:** El objetivo de conservar el último estado confirmado y el comentario de serialización no se sustentan en la ruta de escritura: cada llamada invoca escribirFila inmediatamente; ultimaEscritura solo se reasigna. Un pool puede solapar escrituras y no se impone orden causal por pedido. Existe riesgo de persistir una instantánea atrasada sin caída de proceso, distinto de la ventana de pérdida ya aceptada. No se afirma que haya ocurrido.

**Corrección propuesta:** Capturar una instantánea inmutable por mutación y encadenar su persistencia a la promesa anterior (idealmente por pedido), o usar versión creciente/UPDATE condicional. Añadir prueba que retrase y reordene dos escrituras y compruebe el estado final; conservar documentado el límite fire-and-forget.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Rutas de pedidos/pago/entrega seguidas hasta módulo dueño. Es monolito modular, no se exige hexagonal; imports ESM directos son decisión aceptada.

**Persistencia:** Inspeccionados esquema compuesto tienda_id/pedido_id, rehidratación, writes y contadores. El POST espera lista() al inicio, por lo que no se repite como pendiente el bug de rehidratación que ya corrigieron. El orden de UPSERT no está serializado.

**API y autorización:** Separación de vistaPublica sin PIN y métodos de intención presente. Identidad de tenant y auth diferidas explícitamente en ADR0013; no se atribuye seguridad de autorización al parámetro tiendaId.

**Despliegue:** Workflow Azure y ADR0014 contrastados. Accesibilidad de PostgreSQL desde Azure no verificada; el propio informe declara pendiente la prueba en Azure y prueba intermedia Dokploy. No se infiere caída.

**Asincronía:** Módulos síncronos, espejo PostgreSQL fire-and-forget aceptado. No se exige broker ni persistencia antes del 201 como obligación hoy; el hallazgo de orden es distinto del riesgo de caída entre memoria y commit.

**Observabilidad:** Contadores locales y logger JSON revisados; health es liveness puro. Notificaciones en rutas figuran como deuda V-05 en evidencia S10; no se confunden invocaciones del demo con notificaciones del tráfico HTTP.

**Fuentes de la cobertura:**

- [docs/adr/0008-ratificacion-estrategia-integracion-sincrona.md:22–32](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/adr/0008-ratificacion-estrategia-integracion-sincrona.md#L22-L32)
- [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:104–117](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L104-L117)
- [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:138–141](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L138-L141)
- [backend/app/api/v1/pedidos/route.js:14–22](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/app/api/v1/pedidos/route.js#L14-L22)
- [backend/src/modules/pedidos/index.js:94–117](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/modules/pedidos/index.js#L94-L117)
- [backend/src/modules/entrega/index.js:31–54](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/modules/entrega/index.js#L31-L54)
- [backend/src/corte-vertical.js:15–39](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/corte-vertical.js#L15-L39)
- [docs/evidencias/evidencias-s10.md:137–153](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/docs/evidencias/evidencias-s10.md#L137-L153)
- [backend/src/metricas.js:1–25](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/metricas.js#L1-L25)
- [backend/src/health.js:1–9](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/backend/src/health.js#L1-L9)
- [.github/workflows/deploy-backend.yml:39–65](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/2c711d44b31a41a09306f7840da480a21e8c749a/.github/workflows/deploy-backend.yml#L39-L65)

**Límites adicionales:** Auditoría estática nueva del SHA indicado mediante git show, sin checkout ni ejecución de código estudiantil, sin lectura de PDF, sin publicar ni cambiar notas. No se verificaron el runtime desplegado, secretos/configuración de panel, cargas, CI en vivo ni disponibilidad. Los documentos de pruebas aportan intención y alcance, no una ejecución independiente de esta auditoría.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:59.427982+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`2c711d44b31a41a09306f7840da480a21e8c749a`](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/2c711d44b31a41a09306f7840da480a21e8c749a) (2026-10-12T17:41:41-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Semana 10 · Segundo corte · LaPlacita

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_LaPlacita |
| Estado revisado | `3a04706d27e49fb93c90c68f469442fb6f392710` en `origin/master` (2026-10-04T15:39:16-05:00) |
| Rama remota principal | `origin/master` |
| Observación | 2026-10-06T21:31:50.274455+00:00 |
| Punta revisada para S10 | `3a04706d27e49fb93c90c68f469442fb6f392710` (2026-10-04T15:39:16-05:00) |
| S9 congelado, solo como línea base | `3a04706d27e49fb93c90c68f469442fb6f392710` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** ESC-03/PIN es el escenario de calidad utilizado en S9. No se encontró una fuente que lo declare reto operativo asignado para S10; el plan de identidad/persistencia de Corte 2 tampoco demuestra una asignación. Fuente o búsqueda: [docs/evidencias/evidencias-s9.md:24-39](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L24-L39) y [docs/evidencias/evidencias-s9.md:315-326](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L315-L326); búsqueda en README, ADR, arc42 y evidencias. La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `50b92f8558f2f57d01aeee14dfe202c9e076e74f`: el delta hasta esta punta modifica 64 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master 3a04706d27e49fb93c90c68f469442fb6f392710, anterior al cierre futuro; debe recongelarse al cierre. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://laplacita-app.graymoss-fdd72159.canadacentral.azurecontainerapps.io/api/v1/health: HTTP 200 en 9.980 s; inicio 2026-10-06T21:24:19Z. URL publicada en [docs/evidencia-despliegue-azure.md:5-9](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencia-despliegue-azure.md#L5-L9). Solo sonda de salud, sin probar flujo de pedidos. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | ESC-03/PIN es el escenario de calidad utilizado en S9. No se encontró una fuente que lo declare reto operativo asignado para S10; el plan de identidad/persistencia de Corte 2 tampoco demuestra una asignación. [docs/evidencias/evidencias-s9.md:24-39](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L24-L39) y [docs/evidencias/evidencias-s9.md:315-326](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L315-L326); búsqueda en README, ADR, arc42 y evidencias |
| Línea base medida y reproducible | No verificado | [docs/evidencias/evidencias-s9.md:129-167](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L129-L167) es línea base/resultado reproducible de S9; falta identificar su pertinencia al reto asignado S10. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:52-124](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L52-L124) registra cambio concreto y alternativas, pero su adecuación al escenario operativo asignado queda pendiente. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [src/modules/pedidos/index.js:83-96](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/src/modules/pedidos/index.js#L83-L96) y [app/api/v1/pedidos/[pedidoId]/route.js:14-28](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/app/api/v1/pedidos/%5BpedidoId%5D/route.js#L14-L28) confirman corrección implementada. No se declara respuesta S10 sin conocer el reto. |
| Resultado contrastado con el umbral | No verificado | [docs/evidencias/evidencias-s9.md:106-174](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L106-L174) contrasta defecto/umbral de S9; faltan identificación y experimento S10 sobre despliegue. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | [.github/workflows/ci.yml:25-78](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/.github/workflows/ci.yml#L25-L78) define pruebas y scanner; [docs/semana-08.md:175-185](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/semana-08.md#L175-L185) documenta métrica. Run/gate actual y métrica específica del reto pendientes; no hay defensa observada. |
| Secretos protegidos | No verificado | El equipo documenta su barrido en [docs/evidencias/evidencias-s9.md:280-295](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L280-L295). La revisión independiente ampliada fue cancelada dos veces por la herramienta y no se repite por otra vía: no se afirma limpieza ni exposición a partir de ese bloqueo; comprobación pendiente del revisor. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/aspectos.md:9-36](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/aspectos.md#L9-L36) sigue sin enlace C4 para A-06 ni evidencia navegable; [docs/evidencias/evidencias-s9.md:325-326](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L325-L326) y [README.md:247](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/README.md#L247) dicen Sonar informativo aunque el workflow ya eliminó esa condición. Hay avance real, pero documentos no están plenamente reconciliados. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:124](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L124) precisa 0007 a partir de defecto real; sin asignación confirmada no se da por confirmación/reemplazo del reto S10. |
| Sustentación del reto sobre el entorno desplegado | No verificado | La califica el docente en entorno desplegado y pipeline en vivo. |

Recuento descriptivo: 2 Cumple, 1 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Asignación operativa S10 no verificada; ESC-03 no se presume esa asignación. |
| Decisión e implementación | No verificado | Pendiente | Respuesta S9 sólida y acotada, pendiente contraste con el reto S10. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Pipeline y señales existentes, pero gate vigente, secretos y operación del reto pendientes. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Cadena C4/evidencia y coherencia documental aún parciales; no se recalifica S9. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | Pendiente docente. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_LaPlacita; [docs/evidencias/evidencias-s9.md:8-10](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L8-L10). |
| Estructura mínima presente | Cumple | Árbol Git con las seis rutas mínimas; [docs/aspectos.md:9-17](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/aspectos.md#L9-L17) y ADR/código/evidencia enlazados existentes. |
| Estado calificado identificable | Cumple | origin/master 3a04706d27e49fb93c90c68f469442fb6f392710; hash/fecha y corte en cabecera. |
| Nombres de ADR según la convención | Cumple | Los archivos 0001–0013 de docs/adr siguen NNNN-titulo-en-kebab-case; [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:1-7](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L1-L7). |
| ADR aceptados no reescritos | No cumple | Historial verificado de 0003/0009/0010 contiene ediciones posteriores a aceptación, por ejemplo [4f380512](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/4f3805127ec8e55890ea029b8c4489c1c7932753) y [c99f542b](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/c99f542b48b9b51f93da24464cfa7250091fa00d). [docs/aspectos.md:23-25](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/aspectos.md#L23-L25) reconoce arrastre; ADR-0013 sí complementa sin reescribir 0007. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:54-58](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/ia.md#L54-L58) registra S9 y rechazo técnico. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/ci.yml:51-78](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/.github/workflows/ci.yml#L51-L78) ya no contiene continue-on-error, pero scanner sigue condicionado a token y no espera Quality Gate. [docs/semana-08.md:119-129](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/semana-08.md#L119-L129) mantiene ejecución/URL de gate pendientes. Única consulta PR del hash vacía; no se infiere inexistencia de runs push. No hay trío verificable del contrato para este cierre. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El equipo documenta su barrido en [docs/evidencias/evidencias-s9.md:280-295](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L280-L295). La revisión independiente ampliada fue cancelada dos veces por la herramienta y no se repite por otra vía: no se afirma limpieza ni exposición a partir de ese bloqueo; comprobación pendiente del revisor. |
| Contribución de todos los integrantes | No verificado | Las correspondencias de la planilla anterior están declaradas inferidas y pendientes de docente. No se convierten cuatro firmas en cuatro personas verificadas; confirmar atribución y contribución sustantiva. |

## Estado global del proyecto (overall)

Punta observada de `origin/master`: `3a04706d27e49fb93c90c68f469442fb6f392710` (2026-10-04T15:39:16-05:00). Hay 0 commits posteriores al estado congelado S9. La punta coincide con el estado S9. Se retiró el setter genérico HTTP y el PIN deja de salir por la lectura de pedido. Persisten tiendaId suministrado por el llamante, estado en memoria y deuda declarada V-02/V-04/V-05/V-06. La eliminación de continue-on-error es un avance específico, no prueba Quality Gate ni protección de rama.

- Completar C4 y enlaces de evidencia en A-06.
- Resolver identidad de tenant y persistencia antes de declarar seguridad integral.
- Acreditar scanner/run/Quality Gate y corregir documentos que aún llaman informativo al job.
- Resolver historial de ADR aceptados y confirmar autoría sin inferencias.
- Asignación S10 y comprobación independiente de credenciales pendientes.

### Hallazgos anteriores cerrados o delimitados

- La ausencia preliminar de entrega S9 queda cerrada: existe porción real, ADR y evidencia de defecto/medición.
- Se corrige la exposición del PIN en GET y el setter genérico del borde HTTP; no se da por resuelta autorización.
- Registro IA y ADR de no generación incorporados.
- Se retiró continue-on-error del job Sonar; falta demostrar el gate y su bloqueo.

## Preparación de la sustentación

1. Fallo: si un cliente proporciona tiendaId ajeno o reinicia la instancia, ¿qué protege el pedido y qué observación detectaría el problema?
2. Costo: ¿cómo cambia la cuenta al introducir PostgreSQL y autenticación de tenants y qué supuesto de la capa gratuita deja de valer?
3. Medición: después de observar la exposición del PIN, ¿qué canal o consumidor medirían a continuación y qué evidencia los haría cambiar el diseño?

## Próximos pasos

Para el segundo corte, identifiquen el escenario operativo asignado y prueben su respuesta en el despliegue con línea base reproducible. Actualicen los documentos de Sonar, hagan verificable el Quality Gate y preparen la defensa de identidad por establecimiento, persistencia y costos.

</details>
