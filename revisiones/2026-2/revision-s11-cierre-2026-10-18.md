# Revisión documental S11 · cierre domingo 2026-10-18

Revisión documental retrospectiva solicitada por el docente el **3 de noviembre de 2026**, sobre los 23 proyectos del listado vigente. Se mantiene el cierre al final del domingo en Colombia. No se recalculan notas ni se reemplazan matrices, planillas o estados históricos de evaluación.

**Cierre:** 2026-10-18 a las 23:59:59 COT. Límite exclusivo: **2026-10-19T05:00:00Z**.

La evidencia se reconstruye desde el historial de la rama principal y los snapshots citados, contrastando fusiones de PR y ejecuciones de CI cuando están disponibles. La fecha de un commit no prueba por sí sola cuándo se publicó: un merge local o un avance de rama puede alterar el recorrido de primer padre; las reservas específicas se indican por equipo. Solo se atribuye CI al cierre cuando su resultado terminó dentro del plazo. Código integrado, prueba, despliegue y aceptación funcional son evidencias distintas. No se ejecutó software estudiantil ni se realizaron verificaciones vivas retrospectivas.

Se conservan las confirmaciones docentes registradas el 20/oct: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. Esta confirmación posterior a S11 no demuestra que todo ello existiera al cierre del 18/oct; tampoco acredita cada cambio de S12/S13.

[Índice cronológico](revision-semanas-11-13-2026-11-03.md) · [Ficha S11](../../fichas/semana-11-evidencia-s11.md) · [Issues y PR](revision-issues-pr-s11-s13.md#s11--cierre-2026-10-18).

<a id="as-202620-audioshare"></a>

## AudioShare

Snapshot: [a0834d568625bca8094c17b736d93978ad812430](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/a0834d568625bca8094c17b736d93978ad812430), fecha Git **2026-10-18T23:16:26-05:00**.

Documenta fallos concretos del flujo Flutter–API–SQLite y decide mantener el monolito. El diseño distingue la idempotencia deseada del comportamiento actual: PLAY puede repetirse y cambiar startAt; crear sala tampoco es idempotente. Hay recuperación y pruebas previstas, pero no todas las mitigaciones están implementadas.

**Contraste con la ficha:**
- Tabla de fallos y diseño de idempotencia presentes; ADR-0009 evalúa no extraer.
- Separar pruebas existentes de casos de caída, timeout y fallo parcial aún propuestos.

**README y URL institucional:** README documenta https://audioshare.iscoutb.dev como aplicación pública; el backend sirve la interfaz web y API. No se verificó retrospectivamente funcionamiento ni versión publicada.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39198629143); Publicar imagen: success (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39198629188); Flutter: success (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39198629121)

**Issues al cierre:** 2 abiertas y 2 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-audioshare).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/modos-de-fallo.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/modos-de-fallo.md)
- [docs/idempotencia-y-saga.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/idempotencia-y-saga.md)
- [docs/adr/0009-no-extraer-modulos-como-servicios.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/adr/0009-no-extraer-modulos-como-servicios.md)
- [Ejecución 39198629143](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39198629143)
- [Ejecución 39198629188](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39198629188)
- [Ejecución 39198629121](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39198629121)

<a id="as-202620-clubs-utb"></a>

## Clubs UTB

Snapshot: [1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f), fecha Git **2026-10-18T20:35:24-05:00**.

Identifica fallos de LinkClub, propone idempotencia para publicaciones y adopta ADR-0008 de no extraer. La tabla de fallos aún es general y las mitigaciones declaradas necesitan contrastarse contra cada ruta; una clave única no sustituye el tratamiento completo de reintentos y errores.

**Contraste con la ficha:**
- Hay diseño de Idempotency-Key y decisión de extracción.
- Precisar no respuesta, demora y duplicado con estado implementado o pendiente; CI de backend y contrato falla.

**README y URL institucional:** README solo muestra localhost; no URL pública concreta ni subdominio institucional documentado.

**CI y publicación:** .github/workflows/contrato.yml: failure (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39186049497); .github/workflows/backend-tests.yml: failure (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39186048698)

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-clubs-utb).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/arc42/tabla_fallos.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/arc42/tabla_fallos.md)
- [docs/resilience/idempotencia.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/resilience/idempotencia.md)
- [docs/adr/0008-no-extraer-publicaciones.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/adr/0008-no-extraer-publicaciones.md)
- [Ejecución 39186049497](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39186049497)
- [Ejecución 39186048698](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39186048698)

<a id="as-202620-dinamikutb"></a>

## DinamikUTB

Snapshot: [37872ff7dbb08be833b92c0a4b6d1ca3152464a1](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/37872ff7dbb08be833b92c0a4b6d1ca3152464a1), fecha Git **2026-10-18T23:58:04-05:00**.

Analiza Flutter–FastAPI y base de datos, con timeout/reintentos e idempotencia del cambio de estado. ADR-0010 compara extraer requisitos, extraer alertas o mantener el monolito y justifica no extraer por transacción única, costo y ausencia de carga diferenciada.

**Contraste con la ficha:**
- Fallos, mitigaciones y alternativas explícitas en arc42§11 y ADR.
- El CI de este commit finaliza unos segundos después del cierre; no presentarlo como resultado disponible el domingo.

**README y URL institucional:** README: frontend GitHub Pages y API Render externos; sin iscoutb.dev.

**CI y publicación:** No hay resultado completado del commit acreditado antes del cierre. Resultados terminados o iniciados después del cierre excluidos: CI https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/39202115357; Deploy frontend (GitHub Pages) https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/39202115452

**Issues al cierre:** 2 abiertas y 15 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-dinamikutb).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/adr/0010-extraccion-de-modulo.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/adr/0010-extraccion-de-modulo.md)
- [docs/arc42/11-risks-and-technical-debt.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/11-risks-and-technical-debt.md)
- [backend/tests/test_idempotencia.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/backend/tests/test_idempotencia.py)

<a id="as-202620-drift"></a>

## Drift

Snapshot: [1cead90c02d284f9261addd19e5979ab114b9aea](https://github.com/ISCOUTB/AS_202620_Drift/commit/1cead90c02d284f9261addd19e5979ab114b9aea), fecha Git **2026-10-18T22:20:50-05:00**.

Analiza resiliencia de las fuentes externas, especialmente Steam, con timeout, reintentos acotados, validación y respaldo. ADR-0009 compara extracción y permanencia, conserva el monolito y justifica que saga/outbox no aplican al flujo actual. Quedan por medir latencia degradada y revisar registros del despliegue.

**Contraste con la ficha:**
- Modos de fallo ligados a integración real y pruebas de duplicados.
- No equiparar respaldo/caché con disponibilidad externa o mediciones de producción.

**README y URL institucional:** README documenta frontend https://drift.iscoutb.dev y API bajo /api; Azure y Vercel son despliegues externos separados.

**CI y publicación:** Build and deploy Python app to Azure Web App - drift-utb-202620: success (https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39194258310); CI: success (https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39194258318)

**Issues al cierre:** 5 abiertas y 15 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-drift).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/adr/0009-decision-extraccion-integracion-steam.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/adr/0009-decision-extraccion-integracion-steam.md)
- [docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md)
- [Ejecución 39194258310](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39194258310)
- [Ejecución 39194258318](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39194258318)

<a id="as-202620-elmapita"></a>

## ElMapita

Snapshot: [f3bcfa83e80f5c8d0e30a01b656d89160c907d64](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/f3bcfa83e80f5c8d0e30a01b656d89160c907d64), fecha Git **2026-10-04T22:11:20-05:00**.

El snapshot de cierre conserva el trabajo previo de mapas/visor 3D y no contiene ADR-0008 ni la documentación específica de extracción añadida después. Por ello no corresponde atribuir a S11 los avances S12. La confirmación docente posterior de presentación y funcionamiento se conserva como evidencia de ese momento, no retroactiva.

**Contraste con la ficha:**
- Faltan en este corte el análisis específico de los tres fallos, diseño de idempotencia y decisión de extracción.
- No tener URL pública en README no demuestra ausencia de trabajo.

**README y URL institucional:** README no contiene URL pública concreta; tu-proyecto.supabase.co es ejemplo, no despliegue.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/37258414405)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-elmapita).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [README.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/README.md)
- [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/arc42/arc42-template-EN.md)
- [Ejecución 37258414405](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/37258414405)

<a id="as-202620-enagenda"></a>

## EnAgenda

Snapshot: [4bec22f3821493014e8352ece8274bb2950e97db](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/4bec22f3821493014e8352ece8274bb2950e97db), fecha Git **2026-10-11T23:47:24-05:00**.

Permanece en la base del 11/oct, con flujo de invitaciones y controles previos. No se acredita una entrega específica S11 con tabla de fallos, diseño completo de idempotencia y ADR de extracción. El estado anterior no permite atribuirle la persistencia y taller incorporados la semana siguiente.

**Contraste con la ficha:**
- Revisar fallos parciales de invitaciones en lote y recuperación.
- CI antiguo aprobado no acredita nuevos entregables S11.

**README y URL institucional:** README conserva host-asignado y localhost; no URL de despliegue concreta ni iscoutb.dev.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/38205222318); pages build and deployment: success (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/38205222629)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-enagenda).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/README.md)
- [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/08-conceptos-transversales.md)
- [Ejecución 38205222318](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/38205222318)
- [Ejecución 38205222629](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/38205222629)

<a id="as-202620-gimnasioutb"></a>

## GimnasioUTB

Snapshot: [2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf), fecha Git **2026-10-18T22:02:01-05:00**.

Documenta fallos de app–API–PostgreSQL, incluidos commit incierto, reintentos y contención. La transacción con bloqueo por fila está implementada; idempotencia, timeouts y notificaciones/outbox permanecen diseño. ADR-0005 razona no extraer notificaciones todavía.

**Contraste con la ficha:**
- No confundir serialización del contador con deduplicación de solicitudes.
- Separación implementado/diseño/futuro explícita; falta probar recuperaciones propuestas.

**README y URL institucional:** README documenta API https://gimnasio-utb.iscoutb.dev; no es evidencia de frontend web.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/39192779430)

**Issues al cierre:** 16 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-gimnasioutb).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/s11-fallos-parciales.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/s11-fallos-parciales.md)
- [docs/adr/0005-no-extraer-notificaciones.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/adr/0005-no-extraer-notificaciones.md)
- [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js)
- [Ejecución 39192779430](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/39192779430)

<a id="as-202620-inventrack"></a>

## InvenTrack

Snapshot: [28506a8eabcde2234e56698d13ae1d8ae8d0ee24](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/28506a8eabcde2234e56698d13ae1d8ae8d0ee24), fecha Git **2026-10-18T22:29:12-05:00**.

Entrega análisis de fallos, decisión de no extraer inventario e idempotencia/sagas. ADR-0011 reconoce que los comandos aún no son idempotentes; esto corrige conceptualmente la tabla que atribuye deduplicación al lock porSKU. La serialización impide carreras, pero no evita repetir dos descuentos válidos.

**Contraste con la ficha:**
- Reconciliar tabla y arc42 con ADR-0011: no prometer idempotencia por exclusión mutua.
- Separar integración local vigente de escenarios HTTP/distribuidos futuros.

**README y URL institucional:** README documenta API https://inventrack.iscoutb.dev y alternativa Render; no frontend web independiente.

**CI y publicación:** Run Tests: success (https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/39194936605)

**Issues al cierre:** 0 abiertas y 7 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-inventrack).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/retos/fallos-distribuidos-s11.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/retos/fallos-distribuidos-s11.md)
- [docs/adr/0011-idempotencia-y-sagas-en-movimientos.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/adr/0011-idempotencia-y-sagas-en-movimientos.md)
- [docs/adr/0010-decision-extraccion-microservicios.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/adr/0010-decision-extraccion-microservicios.md)
- [Ejecución 39194936605](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/39194936605)

<a id="as-202620-laplacita"></a>

## LaPlacita

Snapshot: [0c9ce082b5850baf1ecda75e82d20757d0101234](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/0c9ce082b5850baf1ecda75e82d20757d0101234), fecha Git **2026-10-18T21:56:00-05:00**.

La integración cliente–API y PostgreSQL tiene modos de fallo, diseño de idempotencia y decisión razonada de no extraer servicios. La idempotencia de creación de pedidos ya se implementó dentro del proceso; no equivale a durabilidad entre reinicios ni a protección de varios procesos.

**Contraste con la ficha:**
- La clave es opcional y permanece en memoria; el cliente aún no la envía en esta revisión.
- Saga, outbox y reconciliación aparecen como propuestas, no como operación acreditada.

**README y URL institucional:** README documenta API externa Azure; no documenta en raíz un dominio propio iscoutb.dev para la solución.

**CI y publicación:** Deploy Dokploy (laboratorio de la U): success (https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39192292623); CI LaPlacita: success (https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39192292599)

**Issues al cierre:** 0 abiertas y 14 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-laplacita).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencias/evidencias-s11.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/evidencias/evidencias-s11.md)
- [docs/adr/0019-no-extraccion-a-servicios.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/adr/0019-no-extraccion-a-servicios.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/README.md)

<a id="as-202620-lostvault"></a>

## LostVault

Snapshot: [34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f](https://github.com/ISCOUTB/AS_202620_LostVault/commit/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f), fecha Git **2026-10-18T20:43:15-05:00**.

La S11 documenta fallos de reclamación HTTP y justifica mantener verificación de identidad dentro del monolito. La API incorpora repetición idempotente y exclusión dentro de un proceso, mientras el cliente Flutter todavía utiliza adaptadores en memoria.

**Contraste con la ficha:**
- Timeout, backoff y circuit breaker del cliente están diseñados, no implementados.
- El candado y las claves en RAM no coordinan instancias serverless; la identidad no es una verificación documental real.

**README y URL institucional:** README sin URL pública concreta de la solución; no se acredita dominio iscoutb.dev documentado.

**CI y publicación:** Build: success (https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39186637112); Flutter checks: success (https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39186637229); Backend checks: success (https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39186637073)

**Issues al cierre:** 0 abiertas y 1 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-lostvault).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/fallos-parciales/s11-fallos-parciales.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/fallos-parciales/s11-fallos-parciales.md)
- [docs/adr/0005-no-extraer-verificacion-identidad.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/adr/0005-no-extraer-verificacion-identidad.md)
- [backend/main.py](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/backend/main.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/README.md)

<a id="as-202620-mapsutb"></a>

## mapsutb

Snapshot: [4b8fa088faec96772e76c8c4f2782919ec87a9b9](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/4b8fa088faec96772e76c8c4f2782919ec87a9b9), fecha Git **2026-10-16T12:38:48-05:00**.

La S11 analiza las integraciones del mapa y mantiene los módulos en el mismo despliegue con una decisión explícita de no extracción. Existe cliente web con búsqueda de zonas, espacios y salones; el CI y el despliegue Firebase del hash de corte concluyeron antes del domingo.

**Contraste con la ficha:**
- La analítica admite pérdida de eventos; no se debe presentar como entrega garantizada.
- Despliegue Firebase documentado no cumple por sí mismo el dominio institucional solicitado.

**README y URL institucional:** README documenta frontend https://mapsutb.web.app, externo a iscoutb.dev.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/38941879075); Despliegue web (Firebase Hosting): success (https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/38941878838)

**Issues al cierre:** 2 abiertas y 52 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-mapsutb).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencia-s11.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/evidencia-s11.md)
- [docs/adr/0016-no-extraer-modulos-por-ahora.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/adr/0016-no-extraer-modulos-por-ahora.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/README.md)

<a id="as-202620-pideutb"></a>

## PideUtb

Snapshot: [2395d7812aa86ae98c177d58cbea0e927d9593d5](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/2395d7812aa86ae98c177d58cbea0e927d9593d5), fecha Git **2026-10-18T18:40:46-05:00**.

S11 identifica fallos parciales del flujo de pago y panel, integra pruebas e idempotencia, y argumenta por qué no extraer pagos. La conciliación reconoce la ventana entre escrituras; el despliegue y los filtros externos se distinguen de la lógica en proceso.

**Contraste con la ficha:**
- No presentar las dos escrituras de pago como una única transacción indivisible.
- La integración con un proveedor real requiere su evidencia y no se deduce de las pruebas locales del webhook.

**README y URL institucional:** README documenta frontend https://pideutb.iscoutb.dev y API https://api-pideutb.iscoutb.dev.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39177528726)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-pideutb).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencia-s11.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/evidencia-s11.md)
- [docs/adr/0009-no-extraer-un-servicio.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/adr/0009-no-extraer-un-servicio.md)
- [backend/tests/test_fallos_parciales.py](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/backend/tests/test_fallos_parciales.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/README.md)

<a id="as-202620-proyecto-campusmarket"></a>

## CampusMarket

Snapshot: [a237dd2f22b02bb547f87a07d15b6d31ea0dc758](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/a237dd2f22b02bb547f87a07d15b6d31ea0dc758), fecha Git **2026-10-18T23:51:37-05:00**.

S11 identifica Flutter→FastAPI→MySQL como integración principal y distingue las llamadas internas de Catálogo. Documenta fallos, propone idempotencia transaccional y justifica mantener Catálogo en el monolito; las mitigaciones pendientes no se publican como implementadas.

**Contraste con la ficha:**
- La creación de publicaciones no tiene aún deduplicación persistente por Idempotency-Key.
- Imágenes y SQL tienen compensaciones parciales, no atomicidad distribuida.
- El run de flujo Web/Android empezó antes del cierre, pero terminó después; su resultado final queda fuera del corte.

**README y URL institucional:** README documenta API https://campusmarket.iscoutb.dev; frontend GitHub Pages externo.

**CI y publicación:** S10 contrato del cliente en despliegue publico: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586378); Compose y persistencia del MVP: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586404); Pruebas del backend: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586343); Validación Flutter MVP: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586312); Flujo real Web y Android: sin resultado final dentro del corte (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586366)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-proyecto-campusmarket).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencias/evidencia-s11-2026-10-18.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/evidencias/evidencia-s11-2026-10-18.md)
- [docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md)
- [backend/app/publicaciones/repository.py](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/backend/app/publicaciones/repository.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/README.md)

<a id="as-202620-recobra"></a>

## Recobra

Snapshot: [15e39a1bffec7c0383f90b2a38c2a9304e2b2052](https://github.com/ISCOUTB/AS_202620_Recobra/commit/15e39a1bffec7c0383f90b2a38c2a9304e2b2052), fecha Git **2026-10-18T12:41:29-05:00**.

S11 documenta modos de fallo e idempotencia/reconciliación y conserva la decisión de no extraer Emparejamiento. Ya hay cuentas, reclamaciones, moderación y privacidad en el snapshot, por lo que los ADR anteriores deben leerse con sus enmiendas y no como descripción íntegra del estado actual.

**Contraste con la ficha:**
- Las transiciones entre contextos usan pasos recuperables; no prometer una transacción global.
- El ADR original mantiene referencias históricas a módulos y datos antes inexistentes: contrastar con código y enmiendas posteriores al mismo cierre.

**README y URL institucional:** README documenta https://recobra.iscoutb.dev y cliente /app/, además de endpoints API.

**CI y publicación:** ci: success (https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39150751474)

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-recobra).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/adr/0012-no-extraer-emparejamiento.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/adr/0012-no-extraer-emparejamiento.md)
- [docs/adr/0020-consistencia-entre-publicaciones-y-reclamaciones.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/adr/0020-consistencia-entre-publicaciones-y-reclamaciones.md)
- [src/application/use-cases/consistencia-reclamaciones.spec.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/src/application/use-cases/consistencia-reclamaciones.spec.ts)
- [README.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/README.md)

<a id="as-202620-routb"></a>

## ROUTB

Snapshot: [1bd9425e2675bd7531426b6e31e78546b3e55f2e](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/1bd9425e2675bd7531426b6e31e78546b3e55f2e), fecha Git **2026-10-18T16:39:27-05:00**.

S11 identifica fallos en las integraciones de movilidad y formaliza no extraer el módulo de solicitudes, preservando la atomicidad local del control de cupos. Hay API institucional documentada y CI del commit de corte aprobado.

**Contraste con la ficha:**
- No confundir timeout de la aplicación con garantía de entrega de notificaciones.
- El avance presentado confirmado por el docente no sustituye verificación completa de todas las integraciones.

**README y URL institucional:** README documenta API https://routb.iscoutb.dev; no URL de frontend web independiente acreditada.

**CI y publicación:** CI ROUTB: success (https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39168805661)

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-routb).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/adr/0017-decision-extraccion-modulo-requests.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/adr/0017-decision-extraccion-modulo-requests.md)
- [docs/adr/0003-control-atomico-de-cupos.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/adr/0003-control-atomico-de-cupos.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/README.md)

<a id="as-202620-shareu"></a>

## ShareU

Snapshot: [39508608eae4c1a56a5e4fc11a055bf6afb2c003](https://github.com/ISCOUTB/AS_202620_ShareU/commit/39508608eae4c1a56a5e4fc11a055bf6afb2c003), fecha Git **2026-09-28T19:56:57-05:00**.

S11 conserva el commit del 28/sept: no hay nuevo código integrado en esa ventana. La línea base contiene búsqueda y decisiones de modularidad, pero no se encontró todavía la evidencia específica de fallos e idempotencia ni ADR de no extracción exigidos para S11.

**Contraste con la ficha:**
- No confundir ausencia de commits nuevos con inexistencia del proyecto.
- CI falla y README no documenta una URL pública de la solución.

**README y URL institucional:** README solo contiene URLs locales, no despliegue público concreto ni iscoutb.dev.

**CI y publicación:** .github/workflows/tests.yml: failure (https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458)

**Issues al cierre:** 10 abiertas y 10 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-shareu).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md)

<a id="as-202620-sistema-de-calificacion-automatica"></a>

## Calificación automática

Snapshot: [98a9dcc8f22c77ac5d0dfcea4055865e7727a21e](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e), fecha Git **2026-10-18T22:40:44-05:00**.

Documenta los fallos de Redis, proveedor LLM y cliente con mitigaciones trazables y ADR que justifica no extraer módulos. El worker deduplica temporalmente; perder el trabajo tras BLPOP y marcar antes de procesar siguen siendo límites reconocidos, no garantías de procesamiento de calificaciones.

**Contraste con la ficha:**
- Timeouts y deduplicación tienen rutas de código y pruebas citadas.
- El acuse de recepción y la deduplicación de carga en API permanecen como planes declarados.

**README y URL institucional:** README publica frontend/API en Render, sin dominio iscoutb.dev.

**CI y publicación:** [{'name': 'CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/39195829181', 'observed_completed_by': '2026-10-19T03:42:24Z', 'sha': '98a9dcc8f22c77ac5d0dfcea4055865e7727a21e'}]

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-sistema-de-calificacion-automatica).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/evidencia/modos-de-fallo.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/evidencia/modos-de-fallo.md)
- [docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md)
- [backend/infraestructura/cola.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/backend/infraestructura/cola.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/README.md)

<a id="as-202620-taia--task-artificial-intelligence-assistant"></a>

## TAIA

Snapshot: [e755759bd80ef94ffe809cc6ceee0c1d2a0044c6](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6), fecha Git **2026-10-18T15:43:53-05:00**.

La tabla de fallos cubre Gemini y Telegram con timeout, traducción de errores y decisión razonada de conservar el monolito. El reclamo atómico evita ejecutar dos veces la misma confirmación, pero no vuelve atómica la posterior escritura de tarea; el envío de Telegram puede duplicarse y se reconoce como pendiente.

**Contraste con la ficha:**
- Timeout de Gemini de 20 segundos está implementado, aunque supera el objetivo de latencia citado por el equipo.
- Conservar la diferencia entre idempotencia del registro y entrega externa exactamente una vez.

**README y URL institucional:** README publica API provisional sslip.io y referencia Render, sin iscoutb.dev.

**CI y publicación:** [{'name': 'CD', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39164766522', 'observed_completed_by': '2026-10-18T20:45:41Z', 'sha': 'e755759bd80ef94ffe809cc6ceee0c1d2a0044c6'}, {'name': 'CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39164635628', 'observed_completed_by': '2026-10-18T20:45:31Z', 'sha': 'e755759bd80ef94ffe809cc6ceee0c1d2a0044c6'}]

**Issues al cierre:** 3 abiertas y 4 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-taia--task-artificial-intelligence-assistant).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/modos_fallo_s11.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/modos_fallo_s11.md)
- [docs/adr/0008-mantener-monolito-sin-extraer-modulos.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/adr/0008-mantener-monolito-sin-extraer-modulos.md)
- [backend/app/modules/ai/adapters/outbound/sqlalchemy_conversation_store.py](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/backend/app/modules/ai/adapters/outbound/sqlalchemy_conversation_store.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/README.md)

<a id="as-202620-tienda-virtual-utb"></a>

## Tienda virtual UTB

Snapshot: [c58fddfe790932538b37f62017d307ef56bf90d5](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/c58fddfe790932538b37f62017d307ef56bf90d5), fecha Git **2026-10-18T21:06:47-05:00**.

La decisión de no extraer y el diseño de idempotencia/saga están presentes y distinguen propuesta de implementación. La tabla de fallos todavía se apoya en operaciones futuras y describe módulos como reservados; necesita cubrir no respuesta, demora y duplicación en la integración real de catálogo e inventario.

**Contraste con la ficha:**
- Las mitigaciones de caché, reintentos y mensajería se declaran diseño, no ejecución.
- Actualizar la trazabilidad y las descripciones que quedaron rezagadas respecto al código.

**README y URL institucional:** README sin URL pública de despliegue identificada.

**CI y publicación:** [{'name': 'Pruebas', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/39188436440', 'observed_completed_by': '2026-10-19T02:07:49Z', 'sha': 'c58fddfe790932538b37f62017d307ef56bf90d5'}]

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-tienda-virtual-utb).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/modos-fallo-s11.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/modos-fallo-s11.md)
- [docs/idempotencia-saga-s11.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/idempotencia-saga-s11.md)
- [docs/adr/0010-no-extraer-modulos.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/adr/0010-no-extraer-modulos.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/README.md)

<a id="as-202620-utb-tracker"></a>

## UTB Tracker

Snapshot: [277098684766fdf35f12b9d6713ee78c423a08b4](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/277098684766fdf35f12b9d6713ee78c423a08b4), fecha Git **2026-10-18T23:20:54-05:00**.

Hay idempotencia de préstamos, utilidades de resiliencia y ADR para conservar el monolito. Falta una tabla completa de no respuesta, respuesta tardía y duplicación con mitigación por caso; el pipeline del corte falla, de modo que no se acredita suite verde.

**Contraste con la ficha:**
- Las pruebas secuenciales de reenvío no prueban concurrencia.
- Una utilidad de resiliencia aislada no demuestra que toda integración la aplique.

**README y URL institucional:** README contiene instrucciones locales, sin URL pública de despliegue.

**CI y publicación:** [{'name': '.github/workflows/ci.yml', 'conclusion': 'failure', 'url': 'https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/39199034464', 'observed_completed_by': '2026-10-19T04:21:09Z', 'sha': '277098684766fdf35f12b9d6713ee78c423a08b4'}]

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-utb-tracker).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/adr/0005-monolito-vs-microservicios.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/docs/adr/0005-monolito-vs-microservicios.md)
- [app/core/resilience.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/app/core/resilience.py)
- [app/services/loans.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/app/services/loans.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/README.md)

<a id="as-202620-uniteam"></a>

## uniTeam

Snapshot: [2c73ffce2d9b92e71697a7313f829789b4471639](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/2c73ffce2d9b92e71697a7313f829789b4471639), fecha Git **2026-10-13T10:44:44-05:00**.

La aplicación y las integraciones existen, pero la entrega específica de fallos parciales permanece incompleta: falta tabla de tres modos, diseño de idempotencia de creación de tareas y decisión explícita de extraer o no. Tanto CI como el comprobador de despliegue consultados fallan.

**Contraste con la ficha:**
- Incorporar el análisis concreto a riesgos y aspectos.
- Un fallo del comprobador de despliegue no demuestra ausencia de código ni equivale a todos los tests fallidos.

**README y URL institucional:** README publica frontend/API Render, sin iscoutb.dev.

**CI y publicación:** [{'name': 'Comprobación del despliegue', 'conclusion': 'failure', 'url': 'https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/39183414508', 'observed_completed_by': '2026-10-19T01:01:43Z', 'sha': '2c73ffce2d9b92e71697a7313f829789b4471639'}, {'name': 'CI', 'conclusion': 'failure', 'url': 'https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/38424683694', 'observed_completed_by': '2026-10-13T15:45:55Z', 'sha': '2c73ffce2d9b92e71697a7313f829789b4471639'}]

**Issues al cierre:** 0 abiertas y 1 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-uniteam).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/arc42/arc42-uniteam.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/arc42/arc42-uniteam.md)
- [app/api/seguridad.py](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/app/api/seguridad.py)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/.github/workflows/ci.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/README.md)

<a id="as-202620-xald"></a>

## XALD

Snapshot: [405a39e0feff40a8414841b6936d5a2dc4488ba4](https://github.com/ISCOUTB/AS_202620_XALD/commit/405a39e0feff40a8414841b6936d5a2dc4488ba4), fecha Git **2026-10-18T22:00:24-05:00**.

Documenta fallos y mitigaciones de sincronización, idempotencia y decisión razonada de no extraer el módulo Gemini. El código deduplica por identificador y versión solo mientras vive el proceso; memoria, reinicios y pruebas secuenciales limitan la garantía.

**Contraste con la ficha:**
- Los pendientes declarados con plan son válidos como diseño, no implementación.
- No confundir una prueba secuencial de reenvíos con carga concurrente.

**README y URL institucional:** README publica API https://xald-backend.onrender.com, no frontend ni iscoutb.dev.

**CI y publicación:** [{'name': 'Android CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/39192603030', 'observed_completed_by': '2026-10-19T03:01:42Z', 'sha': '405a39e0feff40a8414841b6936d5a2dc4488ba4'}]

**Issues al cierre:** 0 abiertas y 6 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-xald).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/arc42/08-Cross-cutting%20Concepts.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/arc42/08-Cross-cutting%20Concepts.md)
- [docs/adr/0013-extraer-o-no-integracion-gemini.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/adr/0013-extraer-o-no-integracion-gemini.md)
- [backend/app/main.py](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/backend/app/main.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/README.md)

<a id="as-202620-verifacts"></a>

## Verifacts

Snapshot: [e98575318f313fde96ef4c56603fbbc4f2984ae3](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/e98575318f313fde96ef4c56603fbbc4f2984ae3), fecha Git **2026-10-18T12:39:38-05:00**.

La entrega identifica integración, modos de fallo, diseño de idempotencia y decisión de no extraer análisis. Varias promesas de timeout, códigos HTTP y WAL/reintentos no coinciden todavía con la implementación; deben quedar como pendientes explícitos y enlazarse desde riesgos y aspectos.

**Contraste con la ficha:**
- El keep-alive exitoso solo acredita el sondeo que ejecuta, no la suite ni el Quality Gate.
- No inferir garantías reales de red a partir de una tabla de diseño.

**README y URL institucional:** README sin URL pública de despliegue identificada; remite a documentos de despliegue.

**CI y publicación:** [{'name': 'Keep-alive Render', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/39202238102', 'observed_completed_by': '2026-10-19T04:59:46Z', 'sha': 'e98575318f313fde96ef4c56603fbbc4f2984ae3'}]

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s11-as-202620-verifacts).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/entregas/entrega-modos-fallo-idempotencia-adr.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/e98575318f313fde96ef4c56603fbbc4f2984ae3/docs/entregas/entrega-modos-fallo-idempotencia-adr.md)
- [docs/adr/0009-decision-extraccion-modulo-analisis.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/e98575318f313fde96ef4c56603fbbc4f2984ae3/docs/adr/0009-decision-extraccion-modulo-analisis.md)
- [app/persistence/repository.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/e98575318f313fde96ef4c56603fbbc4f2984ae3/app/persistence/repository.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/e98575318f313fde96ef4c56603fbbc4f2984ae3/README.md)

