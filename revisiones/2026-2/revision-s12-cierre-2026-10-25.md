# Revisión documental S12 · cierre domingo 2026-10-25

Revisión documental retrospectiva solicitada por el docente el **3 de noviembre de 2026**, sobre los 23 proyectos del listado vigente. Se mantiene el cierre al final del domingo en Colombia. No se recalculan notas ni se reemplazan matrices, planillas o estados históricos de evaluación.

**Cierre:** 2026-10-25 a las 23:59:59 COT. Límite exclusivo: **2026-10-26T05:00:00Z**.

La evidencia se reconstruye desde el historial de la rama principal y los snapshots citados, contrastando fusiones de PR y ejecuciones de CI cuando están disponibles. La fecha de un commit no prueba por sí sola cuándo se publicó: un merge local o un avance de rama puede alterar el recorrido de primer padre; las reservas específicas se indican por equipo. Solo se atribuye CI al cierre cuando su resultado terminó dentro del plazo. Código integrado, prueba, despliegue y aceptación funcional son evidencias distintas. No se ejecutó software estudiantil ni se realizaron verificaciones vivas retrospectivas.

Se conservan las confirmaciones docentes registradas el 20/oct: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. Esta confirmación posterior a S11 no demuestra que todo ello existiera al cierre del 18/oct; tampoco acredita cada cambio de S12/S13.

[Índice cronológico](revision-semanas-11-13-2026-11-03.md) · [Ficha S12](../../fichas/semana-12-evidencia-s12.md) · [Issues y PR](revision-issues-pr-s11-s13.md#s12--cierre-2026-10-25).

<a id="as-202620-audioshare"></a>

## AudioShare

Snapshot: [8de5ac1daacd189b38d732a0d3d2e916ee29a281](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/8de5ac1daacd189b38d732a0d3d2e916ee29a281), fecha Git **2026-10-25T23:47:47-05:00**.

Añade garantías por operación y contraste de crear sala, PLAY y subir MP3. SQLite confirma crear sala en transacción y la pista usa archivo temporal/renombrado; la caché HTTP revalida el demo y evita almacenar pistas de sala. Reconoce que PLAY puede divergir en memoria si falla la persistencia y que los eventos NDJSON no tienen replay.

**Contraste con la ficha:**
- ADR-0011 compara la fuente de verdad y el almacenamiento de pistas; no exige Redis.
- Faltan pruebas del fallo entre persistir y publicar, idempotencia de PLAY y reconciliación de temporales.

**README y URL institucional:** README documenta https://audioshare.iscoutb.dev como aplicación pública; el backend sirve la interfaz web y API. No se verificó retrospectivamente funcionamiento ni versión publicada.

**CI y publicación:** Flutter: failure (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898215); CI: success (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898219); Publicar imagen: success (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898269)

**Issues al cierre:** 2 abiertas y 2 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-audioshare).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/consistencia-operaciones.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/docs/consistencia-operaciones.md)
- [docs/diseno-cache.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/docs/diseno-cache.md)
- [docs/adr/0011-fuente-de-verdad-y-almacenamiento-de-pistas.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/docs/adr/0011-fuente-de-verdad-y-almacenamiento-de-pistas.md)
- [src/modules/session/infrastructure/persistence/sqlite-room-repository.ts](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/src/modules/session/infrastructure/persistence/sqlite-room-repository.ts)
- [Ejecución 40270898215](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898215)
- [Ejecución 40270898219](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898219)
- [Ejecución 40270898269](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898269)

<a id="as-202620-clubs-utb"></a>

## Clubs UTB

Snapshot: [eaa7e033a5a0eb6b9e6c7a456e4dd95fb736b8b5](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/eaa7e033a5a0eb6b9e6c7a456e4dd95fb736b8b5), fecha Git **2026-10-25T23:47:55-05:00**.

Avanza en publicaciones, imágenes y cabecera de idempotencia; agrega tabla de garantías y ADR de persistencia multimedia. La tabla describe validaciones y restricciones, pero no define con precisión la garantía de lectura/escritura ni demuestra dos operaciones transaccionales completas. Debe concretar caché e invalidación y reconciliar documentación con las rutas reales.

**Contraste con la ficha:**
- No confundir restricción única/idempotencia con consistencia global.
- Workflow backend y contrato fallan; no se acredita suite aprobada.

**README y URL institucional:** README solo muestra localhost; no URL pública concreta ni subdominio institucional documentado. ADR-0009 usa api-linkclub.iscoutb.dev en un ejemplo de archivo estático, pero no sustituye una URL de despliegue vigente documentada en README ni prueba funcionamiento.

**CI y publicación:** .github/workflows/backend-tests.yml: failure (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40270923811); .github/workflows/contrato.yml: failure (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40270924660)

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-clubs-utb).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/arc42/tabla_garantia_consistencia.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/eaa7e033a5a0eb6b9e6c7a456e4dd95fb736b8b5/docs/arc42/tabla_garantia_consistencia.md)
- [docs/adr/0009-estrategia-persistencia-multimedia.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/eaa7e033a5a0eb6b9e6c7a456e4dd95fb736b8b5/docs/adr/0009-estrategia-persistencia-multimedia.md)
- [backend/src/linkclub/adapters/inbound/api/publicacion_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/eaa7e033a5a0eb6b9e6c7a456e4dd95fb736b8b5/backend/src/linkclub/adapters/inbound/api/publicacion_router.py)
- [Ejecución 40270923811](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40270923811)
- [Ejecución 40270924660](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40270924660)

<a id="as-202620-dinamikutb"></a>

## DinamikUTB

Snapshot: [834d26371ef79aab268b394ea32ed9b12cef967e](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/834d26371ef79aab268b394ea32ed9b12cef967e), fecha Git **2026-10-25T23:56:29-05:00**.

Incorpora historial transaccional de cambios de requisitos: estado e historial comparten commit y prueba de rollback. Explicita que no usa caché de dominio ni broker, distingue logs de auditoría durable y compara el costo de revertir el historial. La pantalla reúne consultas sin snapshot común; persisten última escritura gana, referencias sin FK y respaldo sin demostrar.

**Contraste con la ficha:**
- Tabla de garantías, dos operaciones, no-caché justificada, ADR-0011 y C4 aportan evidencia S12.
- CI falla aunque el despliegue GitHub Pages pasa; esos estados no se sustituyen.

**README y URL institucional:** README añade https://dinamikutb.iscoutb.dev como despliegue del laboratorio y /health; no confundir con frontend separado, aún conserva Pages/Render.

**CI y publicación:** Deploy frontend (GitHub Pages): success (https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40271620975); CI: failure (https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40271620947)

**Issues al cierre:** 2 abiertas y 15 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-dinamikutb).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/evidencia-s12.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/834d26371ef79aab268b394ea32ed9b12cef967e/docs/evidencia-s12.md)
- [docs/adr/0011-historial-de-cambios-transaccional.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/834d26371ef79aab268b394ea32ed9b12cef967e/docs/adr/0011-historial-de-cambios-transaccional.md)
- [backend/app/requisitos/service.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/834d26371ef79aab268b394ea32ed9b12cef967e/backend/app/requisitos/service.py)
- [Ejecución 40271620975](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40271620975)
- [Ejecución 40271620947](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40271620947)

<a id="as-202620-drift"></a>

## Drift

Snapshot: [d9a181630f9c7cc9daf3d58705092b245cdc7c73](https://github.com/ISCOUTB/AS_202620_Drift/commit/d9a181630f9c7cc9daf3d58705092b245cdc7c73), fecha Git **2026-10-25T17:37:33-05:00**.

Consolida consistencia y cachés locales por fuente, e incorpora evidencia de Steam degradado y C4 actualizado. ADR-0010 compara alternativas y concluye que el contrato público/identidad del juego es más costoso de revertir que el almacenamiento RAM actual. No declara MySQL implementado y mantiene separados datos curados, datos externos y perfil local del navegador.

**Contraste con la ficha:**
- Costos son estimaciones, no horas observadas.
- La prueba de degradación con shim es evidencia controlada, no medición del proveedor real en producción.

**README y URL institucional:** README documenta frontend https://drift.iscoutb.dev y API bajo /api; Azure y Vercel son despliegues externos separados.

**CI y publicación:** Build and deploy Python app to Azure Web App - drift-utb-202620: success (https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074); CI: success (https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067)

**Issues al cierre:** 5 abiertas y 15 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-drift).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/adr/0010-costo-de-reversion-de-las-decisiones-de-datos.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/d9a181630f9c7cc9daf3d58705092b245cdc7c73/docs/adr/0010-costo-de-reversion-de-las-decisiones-de-datos.md)
- [docs/arc42/arc42_8_conceptos_transversales.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/d9a181630f9c7cc9daf3d58705092b245cdc7c73/docs/arc42/arc42_8_conceptos_transversales.md)
- [docs/evidencias/s12-steam-degradado.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/d9a181630f9c7cc9daf3d58705092b245cdc7c73/docs/evidencias/s12-steam-degradado.md)
- [Ejecución 40241076074](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074)
- [Ejecución 40241076067](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067)

<a id="as-202620-elmapita"></a>

## ElMapita

Snapshot: [537a7716cc37df3fae1b7e2331e0114c93871ee5](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/537a7716cc37df3fae1b7e2331e0114c93871ee5), fecha Git **2026-10-25T11:26:51-05:00**.

El snapshot fechado el 25/oct incorpora cache-aside con TTL, invalidación de POIs tras escritura, modelos 3D inmutables por versión y propagación de errores de base como 503. La tabla distingue garantías efectivas y reconoce POST no idempotente, lecturas sin snapshot y offline incompleto; ADR-0010 justifica PostgreSQL/PostGIS. Su integración exacta antes del cierre no queda acreditada: el CI disponible es del 28/oct.

**Contraste con la ficha:**
- Caché de edificios 10 min, POIs 5 min y URLs firmadas 50 min; invalidación explícita solo donde hay escritura API.
- Publicación/eventos en memoria no son outbox durable; recuperar metadatos offline sigue pendiente.

**README y URL institucional:** README no contiene URL pública concreta; tu-proyecto.supabase.co es ejemplo, no despliegue.

**CI y publicación:** No hay resultado completado del commit acreditado antes del cierre. Resultados terminados o iniciados después del cierre excluidos: CI https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40654274728

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-elmapita).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.
- Fecha de commit 25/oct; CI aparece 28/oct. No se prueba que 537a771 estuviera publicado en main antes del cierre; tratarlo como snapshot candidato, no integración definitiva.

**Fuentes:**
- [docs/datos/consistencia-operaciones.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/537a7716cc37df3fae1b7e2331e0114c93871ee5/docs/datos/consistencia-operaciones.md)
- [docs/datos/diseno-cache.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/537a7716cc37df3fae1b7e2331e0114c93871ee5/docs/datos/diseno-cache.md)
- [docs/adr/0010-postgresql-postgis-fuente-de-verdad.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/537a7716cc37df3fae1b7e2331e0114c93871ee5/docs/adr/0010-postgresql-postgis-fuente-de-verdad.md)
- [backend/src/modules/pois/application/use-cases.ts](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/537a7716cc37df3fae1b7e2331e0114c93871ee5/backend/src/modules/pois/application/use-cases.ts)

<a id="as-202620-enagenda"></a>

## EnAgenda

Snapshot: [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), fecha Git **2026-10-25T22:57:38-05:00**.

Integra PostgreSQL/SQLAlchemy y migraciones para usuarios, eventos e invitaciones, con tabla de garantías y contraste de rollback y límites. Decide no introducir caché ni broker de negocio; ADR de persistencia compara costo de reversión. Mantiene un flujo heredado en memoria y un taller de mensajes aislado, por lo que no debe describirse todo el sistema como durable.

**Contraste con la ficha:**
- Pruebas SQLite acreditan atomicidad, no coordinación multiworker de PostgreSQL.
- Taller aprobado y Pages aprobado coexisten con CI general fallido; no prueban despliegue de aplicación.

**README y URL institucional:** README conserva host-asignado y localhost; no URL de despliegue concreta ni iscoutb.dev.

**CI y publicación:** Taller mensajes y consistencia: success (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284); CI: failure (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410); pages build and deployment: success (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-enagenda).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/adr/0004-persistir-datos-en-postgresql.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/adr/0004-persistir-datos-en-postgresql.md)
- [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/arc42/08-conceptos-transversales.md)
- [src/invitaciones/aplicacion/agregar_invitados.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/src/invitaciones/aplicacion/agregar_invitados.py)
- [docs/talleres/mensajes-consistencia/README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/talleres/mensajes-consistencia/README.md)
- [Ejecución 40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284)
- [Ejecución 40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410)
- [Ejecución 40266609521](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521)

<a id="as-202620-gimnasioutb"></a>

## GimnasioUTB

Snapshot: [5fa232b25e3122474291e5cc41ead96f9b567856](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/5fa232b25e3122474291e5cc41ead96f9b567856), fecha Git **2026-10-25T23:21:32-05:00**.

Define garantías por operación: escrituras del aforo serializadas y lectura con frescura objetivo de 2 s. Diseña caché write-through versionada y log append-only PostgreSQL como historial/idempotencia y fuente futura de eventos. El contador transaccional existe, pero la caché, log e idempotencia descritos no se presentan como implementados.

**Contraste con la ficha:**
- ADR-0006 fundamenta la decisión del log; conservar distinción diseño frente a código.
- CI aprobado no convierte en medido el objetivo de frescura ni valida componentes futuros.

**README y URL institucional:** README documenta API https://gimnasio-utb.iscoutb.dev; no es evidencia de frontend web.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360)

**Issues al cierre:** 16 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-gimnasioutb).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/s12-datos-eventos.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/docs/s12-datos-eventos.md)
- [docs/adr/0006-log-de-eventos-de-acceso.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/docs/adr/0006-log-de-eventos-de-acceso.md)
- [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js)
- [Ejecución 40268686360](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360)

<a id="as-202620-inventrack"></a>

## InvenTrack

Snapshot: [1269ffb40890a34dac7daa924cfcc85c7e0e5778](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/1269ffb40890a34dac7daa924cfcc85c7e0e5778), fecha Git **2026-10-25T23:40:41-05:00**.

Mantiene repositorios en memoria y decisiones explícitas de almacenamiento, con comparación de alternativas/costo de reversión. Integra eventos de auditoría de movimientos con broker simulado, reintentos y deduplicación; sus garantías siguen limitadas al proceso, sin almacenamiento durable ni coordinación entre réplicas.

**Contraste con la ficha:**
- ADR-0015 complementa sin reescribir ADR previo; cifras de esfuerzo son estimaciones.
- Distinguir clave transmitida al evento de deduplicación HTTP del comando: esta última llega en S13.

**README y URL institucional:** README documenta API https://inventrack.iscoutb.dev y alternativa Render; no frontend web independiente.

**CI y publicación:** Run Tests: success (https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40270300788)

**Issues al cierre:** 0 abiertas y 7 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-inventrack).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/adr/0015-completar-decision-de-almacenamiento-y-reversion.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/1269ffb40890a34dac7daa924cfcc85c7e0e5778/docs/adr/0015-completar-decision-de-almacenamiento-y-reversion.md)
- [docs/evidencia-mensajeria-s12.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/1269ffb40890a34dac7daa924cfcc85c7e0e5778/docs/evidencia-mensajeria-s12.md)
- [app/inventario/infrastructure/router.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/1269ffb40890a34dac7daa924cfcc85c7e0e5778/app/inventario/infrastructure/router.py)
- [Ejecución 40270300788](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40270300788)

<a id="as-202620-laplacita"></a>

## LaPlacita

Snapshot: [3d003b62ffe92c659699bd1236424fb397bc2eee](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/3d003b62ffe92c659699bd1236424fb397bc2eee), fecha Git **2026-10-24T22:25:42-05:00**.

La evidencia S12 ya contiene tabla de operaciones y garantías, estrategia de caché, decisión de identidad del pedido y confirmación de creación después de PostgreSQL. Distingue la lectura desde Maps, la durabilidad en PostgreSQL y el desfase del sondeo; el diseño depende de una sola instancia.

**Contraste con la ficha:**
- No extrapolar consistencia local a varias réplicas.
- La persistencia de todas las transiciones y la coherencia después de reinicios requieren conservar los límites documentados; no confundir caché de dominio con service worker.

**README y URL institucional:** README documenta API externa Azure; no documenta en raíz un dominio propio iscoutb.dev para la solución.

**CI y publicación:** CI LaPlacita: success (https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40158232304)

**Issues al cierre:** 0 abiertas y 14 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-laplacita).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencias/evidencias-s12.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/docs/evidencias/evidencias-s12.md)
- [docs/adr/0024-identidad-del-pedido.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/docs/adr/0024-identidad-del-pedido.md)
- [docs/adr/0026-escrituras-at-least-once-y-creacion-confirmada.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/docs/adr/0026-escrituras-at-least-once-y-creacion-confirmada.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/README.md)

<a id="as-202620-lostvault"></a>

## LostVault

Snapshot: [3a6e157110bd3c63e76de9cce68c63991e747468](https://github.com/ISCOUTB/AS_202620_LostVault/commit/3a6e157110bd3c63e76de9cce68c63991e747468), fecha Git **2026-10-25T23:46:40-05:00**.

S12 diferencia la garantía fuerte pretendida de reclamación de la garantía efectiva dentro de un solo proceso, y documenta caché CDN de consultas con ventana máxima declarada de 90 segundos. PostgreSQL y el outbox son decisiones/diseños, no prueba de persistencia desplegada.

**Contraste con la ficha:**
- La invalidación elegida es expiración explícitamente justificada, con respuesta de escritura sin caché.
- Hay dos implementaciones de reclamación: backend es la referencia documentada; api no se presenta como desplegada ni cubierta por CI.

**README y URL institucional:** README sin URL pública concreta de la solución; no se acredita dominio iscoutb.dev documentado.

**CI y publicación:** Build: success (https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589); Flutter checks: success (https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466); Backend checks: success (https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424)

**Issues al cierre:** 0 abiertas y 1 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-lostvault).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/datos/consistencia.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/docs/datos/consistencia.md)
- [docs/datos/cache.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/docs/datos/cache.md)
- [docs/adr/0006-postgresql-fuente-de-verdad.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/docs/adr/0006-postgresql-fuente-de-verdad.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/README.md)

<a id="as-202620-mapsutb"></a>

## mapsutb

Snapshot: [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), fecha Git **2026-10-25T09:04:14-05:00**.

S12 aporta garantías de siete operaciones, cachés diferenciadas e invalidación por despliegue y recarga; además corrige la retención de lecturas fallidas mediante evict. El ADR compara decisiones y explica el costo de revertir los datos del campus de solo lectura derivados de OSM.

**Contraste con la ficha:**
- La analítica es como máximo una vez, sin broker.
- Hay datos JSON como almacenes del cliente, no una base de datos ni servicio backend independiente.

**README y URL institucional:** README documenta frontend https://mapsutb.web.app, externo a iscoutb.dev.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200516007); Despliegue web (Firebase Hosting): success (https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200515940)

**Issues al cierre:** 0 abiertas y 54 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-mapsutb).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencia-s12.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/docs/evidencia-s12.md)
- [docs/adr/0018-datos-del-campus-solo-lectura-derivados-de-osm.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/docs/adr/0018-datos-del-campus-solo-lectura-derivados-de-osm.md)
- [docs/arc42/08_concepts.adoc](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/docs/arc42/08_concepts.adoc)
- [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md)

<a id="as-202620-pideutb"></a>

## PideUtb

Snapshot: [ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f), fecha Git **2026-10-23T10:04:06-05:00**.

S12 documenta garantías por operación y una decisión argumentada de no añadir caché de dominio, respaldada por mediciones del equipo. La notificación efectiva del panel es sondeo; el bus en proceso sin suscriptores no equivale a entrega de eventos al navegador.

**Contraste con la ficha:**
- ADR-0010 decide sondeo frente a empuje, pero no reemplaza por sí solo el ADR comparativo de la decisión de datos más costosa de revertir pedido en la ficha.
- Mantener el contraste de transiciones concurrentes contra código; una base única no convierte automáticamente una secuencia de operaciones en atómica.

**README y URL institucional:** README documenta frontend https://pideutb.iscoutb.dev y API https://api-pideutb.iscoutb.dev.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39975061857)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-pideutb).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencia-s12.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/docs/evidencia-s12.md)
- [docs/adr/0010-notificar-al-panel-por-sondeo.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/docs/adr/0010-notificar-al-panel-por-sondeo.md)
- [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/docs/arc42/arc42.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/README.md)

<a id="as-202620-proyecto-campusmarket"></a>

## CampusMarket

Snapshot: [bba9513f965184ceea1c36eda722c4ac9fcc70b7](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/bba9513f965184ceea1c36eda722c4ac9fcc70b7), fecha Git **2026-10-25T23:34:37-05:00**.

S12 registra operaciones reales y garantías limitadas a transacciones locales; decide no agregar caché de dominio ni proyecciones asíncronas y justifica MySQL como fuente de verdad. Las pruebas del taller de mensajes son aisladas y no introducen un broker productivo.

**Contraste con la ficha:**
- La revisión de reportes y el ocultamiento en otro contexto no son una sola transacción.
- Persisten límites de idempotencia y reconciliación entre archivos e información SQL.

**README y URL institucional:** README documenta API https://campusmarket.iscoutb.dev; frontend GitHub Pages externo.

**CI y publicación:** Compose y persistencia del MVP: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786849); Pruebas del backend: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786840); Validación Flutter MVP: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786871); Flujo real Web y Android: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786823); S10 contrato del cliente en despliegue publico: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786825)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-proyecto-campusmarket).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencias/evidencia-s12-2026-10-25.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/bba9513f965184ceea1c36eda722c4ac9fcc70b7/docs/evidencias/evidencia-s12-2026-10-25.md)
- [docs/adr/0022-mantener-mysql-como-fuente-de-verdad-y-evitar-proyecciones-asincronas.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/bba9513f965184ceea1c36eda722c4ac9fcc70b7/docs/adr/0022-mantener-mysql-como-fuente-de-verdad-y-evitar-proyecciones-asincronas.md)
- [backend/app/administracion/repository.py](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/bba9513f965184ceea1c36eda722c4ac9fcc70b7/backend/app/administracion/repository.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/bba9513f965184ceea1c36eda722c4ac9fcc70b7/README.md)

<a id="as-202620-recobra"></a>

## Recobra

Snapshot: [00f9291c4e59b315a65ba2af348ed449b28319c7](https://github.com/ISCOUTB/AS_202620_Recobra/commit/00f9291c4e59b315a65ba2af348ed449b28319c7), fecha Git **2026-10-24T09:04:29-05:00**.

S12 añade diseño de caché e invalidación, reintentos y cola de eventos fallidos, y compara decisiones para identificar PostgreSQL y sus escrituras atómicas como el mayor costo de reversión. Separa las garantías de una sentencia de la consistencia eventual entre contextos.

**Contraste con la ficha:**
- No hay transacciones globales entre los contextos; el análisis debe reconocer reconciliación y límites de entrega.
- Los resultados del taller de mensajes no acreditan por sí solos comportamiento bajo toda falla en producción.

**README y URL institucional:** README documenta https://recobra.iscoutb.dev y cliente /app/, además de endpoints API.

**CI y publicación:** ci: success (https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40100869755)

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-recobra).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/adr/0025-diseno-de-cache-y-politica-de-invalidacion.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/docs/adr/0025-diseno-de-cache-y-politica-de-invalidacion.md)
- [docs/adr/0026-entrega-de-avisos-con-eventos-reintentos-y-cola-de-fallidos.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/docs/adr/0026-entrega-de-avisos-con-eventos-reintentos-y-cola-de-fallidos.md)
- [docs/adr/0027-la-decision-de-datos-mas-costosa-de-revertir.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/docs/adr/0027-la-decision-de-datos-mas-costosa-de-revertir.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/README.md)

<a id="as-202620-routb"></a>

## ROUTB

Snapshot: [22c2953553a9fc3518fb63576ac622d8bf5e80df](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/22c2953553a9fc3518fb63576ac622d8bf5e80df), fecha Git **2026-10-25T18:22:49-05:00**.

S12 incorpora una comparación del costo de reversión del esquema de estados/cupos, refuerza concurrencia y documenta notificaciones asíncronas. El árbol también incluye la retirada de geocode_cache, por lo que los ADR y textos antiguos de caché deben leerse como historia.

**Contraste con la ficha:**
- Reconciliar la política de caché geográfica con la migración 009 que retira ese almacén.
- El mayor costo de datos se argumenta sobre estados y cupos; no confundirlo con el costo de separar todo el monolito.

**README y URL institucional:** README documenta API https://routb.iscoutb.dev; no URL de frontend web independiente acreditada.

**CI y publicación:** CI ROUTB: success (https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934)

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-routb).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/adr/0020-decision-datos-mas-costosa-de-revertir.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/docs/adr/0020-decision-datos-mas-costosa-de-revertir.md)
- [docs/adr/0021-integridad-solicitudes-y-concurrencia.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/docs/adr/0021-integridad-solicitudes-y-concurrencia.md)
- [backend/migrations/versions/009_retirar_geocode_cache.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/backend/migrations/versions/009_retirar_geocode_cache.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/README.md)

<a id="as-202620-shareu"></a>

## ShareU

Snapshot: [2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767), fecha Git **2026-10-25T17:52:08-05:00**.

S12 integra adaptador Firestore detrás del módulo de documentos y decisiones sobre identidad de datos. Las pruebas utilizan un cliente falso; el ADR de Firestore sigue rotulado propuesto, y arc42 conserva referencias a SQLite que deben reconciliarse con la implementación.

**Contraste con la ficha:**
- La prueba con Firestore falso no valida índices, cuotas ni publicación real.
- La sección 8 revisada no consolida aún garantías por operación ni la política completa de caché/invalidación.

**README y URL institucional:** README solo contiene URLs locales, no despliegue público concreto ni iscoutb.dev.

**CI y publicación:** .github/workflows/tests.yml: failure (https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282)

**Issues al cierre:** 10 abiertas y 10 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-shareu).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/adr/0011-identidad-de-datos-y-propiedad-por-modulo.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/docs/adr/0011-identidad-de-datos-y-propiedad-por-modulo.md)
- [docs/adr/0012-persistencia-en-firestore.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/docs/adr/0012-persistencia-en-firestore.md)
- [app/documentos/repository.py](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/app/documentos/repository.py)
- [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/docs/arc42/arc42.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/README.md)

<a id="as-202620-sistema-de-calificacion-automatica"></a>

## Calificación automática

Snapshot: [561d520b138a1689d9bec9bdff597bdae66a6952](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/561d520b138a1689d9bec9bdff597bdae66a6952), fecha Git **2026-10-25T20:08:51-05:00**.

La entrega de datos ya incluye tabla de consistencia, identidad de hoja derivada de bitácora, caché de propuestas e invalidación. Redis pasa a entrega al menos una vez con trabajos en curso, confirmación, reintentos y fallidos; la documentación reconoce que un único consumidor y Redis sin persistencia limitan la garantía.

**Contraste con la ficha:**
- ADR-0018 argumenta el costo de cambiar identidad y bitácora; ADR-0019 documenta caché de propuestas.
- No confundir la marca temporal de deduplicación con caché de datos ni al menos una vez con exactamente una vez.

**README y URL institucional:** README publica frontend/API en Render, sin dominio iscoutb.dev.

**CI y publicación:** [{'name': 'CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40252791139', 'observed_completed_by': '2026-10-26T01:10:57Z', 'sha': '561d520b138a1689d9bec9bdff597bdae66a6952'}]

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-sistema-de-calificacion-automatica).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/evidencia/consistencia-y-cache.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/docs/evidencia/consistencia-y-cache.md)
- [docs/adr/0018-dar-a-la-hoja-una-identidad-propia-y-derivar-su-estado-de-la-bitacora.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/docs/adr/0018-dar-a-la-hoja-una-identidad-propia-y-derivar-su-estado-de-la-bitacora.md)
- [backend/infraestructura/consumo.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/backend/infraestructura/consumo.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/README.md)

<a id="as-202620-taia--task-artificial-intelligence-assistant"></a>

## TAIA

Snapshot: [e903230d220735b43c9c53c42c64c66524ce0ff9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/e903230d220735b43c9c53c42c64c66524ce0ff9), fecha Git **2026-10-25T10:08:51-05:00**.

arc42 ya declara garantías por operación y compara confirmación del asistente, recordatorios y lecturas contra el código. No usar caché de negocio está razonado; también se diseña la invalidación para una eventual caché. ADR-0009 identifica la base compartida y las referencias lógicas entre módulos como decisión de datos difícil de revertir.

**Contraste con la ficha:**
- No penalizar la ausencia deliberada de caché: hay justificación y política futura.
- Las operaciones entre módulos no forman una transacción global; recordatorios conservan consistencia eventual frente a tareas.

**README y URL institucional:** README publica API https://taia-sistema.iscoutb.dev; no equivale a frontend web.

**CI y publicación:** []

**Issues al cierre:** 3 abiertas y 4 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-taia--task-artificial-intelligence-assistant).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.
- Sin run del SHA exacto acreditado como completado antes del corte; no se traslada verde de otro commit.

**Fuentes:**
- [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/docs/arc42/08-conceptos-transversales.md)
- [docs/adr/0009-base-compartida-con-referencias-logicas-entre-modulos.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/docs/adr/0009-base-compartida-con-referencias-logicas-entre-modulos.md)
- [backend/app/modules/ai/adapters/outbound/sqlalchemy_conversation_store.py](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/backend/app/modules/ai/adapters/outbound/sqlalchemy_conversation_store.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/README.md)

<a id="as-202620-tienda-virtual-utb"></a>

## Tienda virtual UTB

Snapshot: [647bcbd413354775e85a9444f97a2db82725c5f1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/647bcbd413354775e85a9444f97a2db82725c5f1), fecha Git **2026-10-25T11:53:06-05:00**.

La tabla de consistencia cubre compras, cancelación, vencimiento y catálogo con transacciones y control de concurrencia. La caché de catálogo es un diseño explícitamente no implementado, con invalidación posterior al commit y recuperación por TTL. ADR-0018 explica el costo de separar la transacción compartida de pedidos e inventario.

**Contraste con la ficha:**
- Las garantías documentadas distinguen transacción local de aislamiento serializable general.
- No se acredita una mejora de latencia ni caché en producción solo por existir el diseño.

**README y URL institucional:** README publica URL sslip.io, no iscoutb.dev.

**CI y publicación:** [{'name': 'Pruebas', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995', 'observed_completed_by': '2026-10-25T16:54:43Z', 'sha': '647bcbd413354775e85a9444f97a2db82725c5f1'}]

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-tienda-virtual-utb).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/consistencia-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/consistencia-s12.md)
- [docs/cache-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/cache-s12.md)
- [docs/adr/0018-transaccion-compartida-pedidos-inventario.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/adr/0018-transaccion-compartida-pedidos-inventario.md)
- [backend/app/modules/orders/service.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/backend/app/modules/orders/service.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/README.md)

<a id="as-202620-utb-tracker"></a>

## UTB Tracker

Snapshot: [d63644217a1573445702f76268f84a82b3cff504](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/d63644217a1573445702f76268f84a82b3cff504), fecha Git **2026-10-25T23:35:44-05:00**.

La entrega de S12 entra antes del cierre mediante PR #4 y documenta garantías por operación, brechas de concurrencia, diseño de caché e invalidación y costo de los identificadores enteros. El outbox se escribe con el préstamo, pero el propio análisis distingue duplicados, ausencia de orden y necesidad de operar el worker.

**Contraste con la ficha:**
- Caché propuesta no implementada; no usarla como evidencia de optimización efectiva.
- El merge d636442 se incluye: ocurrió el domingo a las 23:35 COT aunque el primer padre del grafo actual recorre una rama de frontend.

**README y URL institucional:** README contiene instrucciones locales, sin URL pública de despliegue.

**CI y publicación:** [{'name': 'UTB Tracker CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40269883908', 'observed_completed_by': '2026-10-26T04:38:09Z', 'sha': 'd63644217a1573445702f76268f84a82b3cff504'}]

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-utb-tracker).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [app/services/loans.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d63644217a1573445702f76268f84a82b3cff504/app/services/loans.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d63644217a1573445702f76268f84a82b3cff504/README.md)
- [Evidencia](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/4)

<a id="as-202620-uniteam"></a>

## uniTeam

Snapshot: [0a44bd5a8d9374423b08fef87e46672cd6ad501b](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/0a44bd5a8d9374423b08fef87e46672cd6ad501b), fecha Git **2026-10-25T19:55:53-05:00**.

El cierre incorpora garantías de datos por operación, MySQL como fuente de verdad y una decisión justificada de no cachear proyectos, tareas ni membresías. Se distingue esa decisión de la caché técnica JWKS y se compara el costo de migrar los datos mediante ADR-0016; el taller local de mensajería permanece separado del flujo real.

**Contraste con la ficha:**
- La regla HTTP private/no-store se describe como propuesta, no implementada.
- CI pasa, mientras la comprobación del despliegue falla: son verificaciones diferentes.

**README y URL institucional:** README publica frontend/API DuckDNS, sin iscoutb.dev.

**CI y publicación:** [{'name': 'Comprobación del despliegue', 'conclusion': 'failure', 'url': 'https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40252045358', 'observed_completed_by': '2026-10-26T01:00:19Z', 'sha': '0a44bd5a8d9374423b08fef87e46672cd6ad501b'}, {'name': 'CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40251714762', 'observed_completed_by': '2026-10-26T00:57:28Z', 'sha': '0a44bd5a8d9374423b08fef87e46672cd6ad501b'}]

**Issues al cierre:** 0 abiertas y 1 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-uniteam).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/arc42/arc42-uniteam.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/arc42/arc42-uniteam.md)
- [docs/adr/0016-conservar-mysql-como-fuente-de-verdad.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/adr/0016-conservar-mysql-como-fuente-de-verdad.md)
- [app/api/dependencias.py](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/app/api/dependencias.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/README.md)

<a id="as-202620-xald"></a>

## XALD

Snapshot: [1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00](https://github.com/ISCOUTB/AS_202620_XALD/commit/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00), fecha Git **2026-10-25T23:04:58-05:00**.

arc42 incorpora garantías por operación, diseño de caché e invalidación y sincronización con reintentos. Distingue memoria vigente de Room/SQLCipher futuros; la cola aún se pierde al morir el proceso y falta el Worker periódico. No se localiza un ADR que compare cuál decisión de datos sería la más costosa de revertir.

**Contraste con la ficha:**
- El ADR-0014 decide la forma de sincronizar, no sustituye el análisis comparativo de reversión del modelo de datos.
- Caché e invalidación son propuestas; backend no cachea porque solo recibe escrituras.

**README y URL institucional:** README publica API https://xald-backend.onrender.com, no frontend ni iscoutb.dev.

**CI y publicación:** [{'name': 'Android CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501', 'observed_completed_by': '2026-10-26T04:07:12Z', 'sha': '1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00'}]

**Issues al cierre:** 0 abiertas y 6 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-xald).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/arc42/08-Cross-cutting%20Concepts.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/arc42/08-Cross-cutting%20Concepts.md)
- [docs/adr/0014-sincronizacion-asincrona-con-reintentos.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/adr/0014-sincronizacion-asincrona-con-reintentos.md)
- [backend/app/main.py](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/backend/app/main.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/README.md)

<a id="as-202620-verifacts"></a>

## Verifacts

Snapshot: [cf2075dcae6ba48507ba47b59aede18afb4df449](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/cf2075dcae6ba48507ba47b59aede18afb4df449), fecha Git **2026-10-24T12:50:57-05:00**.

Ya documenta consistencia por operación, decisión de no usar caché con alternativas e invalidación, y costo comparativo de conservar contenido completo sin propietario en SQLite. El guardado confirma antes de responder; la recarga de historial puede quedar desactualizada y no se promete una instantánea global entre páginas.

**Contraste con la ficha:**
- El mayor costo de reversión incluye migración y gobierno de datos, no solo cambiar de motor.
- El historial global sin propietario sigue siendo riesgo aceptado, no control de acceso implementado.

**README y URL institucional:** README publica HTTP sslip.io, no iscoutb.dev.

**CI y publicación:** [{'name': 'SonarCloud', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40117996296', 'observed_completed_by': '2026-10-24T17:52:06Z', 'sha': 'cf2075dcae6ba48507ba47b59aede18afb4df449'}, {'name': 'Tests', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40117996304', 'observed_completed_by': '2026-10-24T17:51:45Z', 'sha': 'cf2075dcae6ba48507ba47b59aede18afb4df449'}]

**Issues al cierre:** 0 abiertas y 3 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s12-as-202620-verifacts).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/cf2075dcae6ba48507ba47b59aede18afb4df449/docs/arc42/08-conceptos-transversales.md)
- [docs/adr/0012-modelo-almacenamiento-sqlite-costo-reversion.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/cf2075dcae6ba48507ba47b59aede18afb4df449/docs/adr/0012-modelo-almacenamiento-sqlite-costo-reversion.md)
- [app/persistence/repository.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/cf2075dcae6ba48507ba47b59aede18afb4df449/app/persistence/repository.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/cf2075dcae6ba48507ba47b59aede18afb4df449/README.md)

