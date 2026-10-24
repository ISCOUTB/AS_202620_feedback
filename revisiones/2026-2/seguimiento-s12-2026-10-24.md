# Seguimiento actual de S12 · 24 de octubre de 2026

Consulta del **24 de octubre de 2026**, alrededor de las 08:00 COT (UTC−5), sobre los 23 proyectos del roster vigente y sus ramas principales. Es seguimiento actual, no recalificación. **S12 sigue abierta hasta el final del 25 de octubre en Colombia** (límite exclusivo: 26/oct 05:00 UTC). Se conservan notas, planillas, matrices y cortes históricos.

## Alcance y lectura

Se volvieron a consultar las puntas de las ramas principales, README completos, issues, PR y CI relevantes. Los cambios se contrastan con el [seguimiento del 22/oct](seguimiento-s12-2026-10-22.md). Una PR abierta no se atribuye a la rama principal y un workflow verde no prueba operaciones que ese workflow omite. **No se ejecutó código de estudiantes ni se hizo una nueva auditoría funcional de los 23 sitios.** Los SHA y enlaces fijan la evidencia consultada; los estados externos pueden cambiar después.

Los próximos pasos usan la [ficha S12](../../fichas/semana-12-evidencia-s12.md): operaciones reales y garantías, contraste de dos operaciones, caché o exclusión argumentada, invalidación tras escritura, garantías de eventos si existen, ADR comparativo de la decisión de datos más costosa de revertir, C4 nivel 2 y arc42 §8. No se exige añadir caché ni broker si no se necesita; no se califica aquí el taller de mensajes.

## Cambios destacados y prioridades

- **Dinamik:** autenticación/roles y Compose integrados; F7 (recrear/resembrar la base demo antes del 25/oct) sigue declarada pendiente. CI/Pages no acreditan esa operación; no se verificaron condiciones del proveedor.
- **QuantIA, InvenTrack, LaPlacita y Tienda:** nuevos avances de ingesta, garantías, persistencia o interfaz reconocidos; los pendientes se ajustan a esos cambios, sin recalificar.
- **Tracker:** 48 pruebas y despliegue exitosos; no mantener el fallo antiguo como vigente. Proteger la configuración de la base de pruebas antes de operaciones destructivas; el verde no acredita Sonar, retirado del workflow.
- **ROUTB y PideUtb:** PR de S12/identidad visual ya fusionadas. ROUTB debe retirar de su documentación la caché eliminada; Pide requiere aceptación visual separada. Sus jobs Sonar verdes no acreditan análisis ni Quality Gate real.
- **uniTeam:** README ahora DuckDNS; el sondeo sigue en Render y no diagnostica el nuevo dominio. Conserva cálculo de cobertura, pero cambió su publicación y la espera de Quality Gate.
- **TAIA:** nueva punta sin CI/CD correspondiente en los runs consultados; corregir el filtro paths. **VeriFacts:** 66 pruebas y Quality Gate aprobados; el prototipo de mensajería sigue aislado/simulado, no es integración productiva.

## Recuento actual

**172 issues: 45 abiertas y 127 cerradas**; motivos de cierre: **126 completed; 1 duplicate**. **21 abiertas sin responsable**. Se excluyen pull requests. [Inventario completo](seguimiento-issues-2026-10-24.md).

README: **9 con endpoint institucional** (incluye API/backend), **7 externos** y **7 sin URL pública concreta**. [URLs y alcance](seguimiento-despliegues-2026-10-24.md).

Se mantienen las confirmaciones docentes: TAIA y ElMapita presentaron avances funcionando; PideUtb presentó actualización y tiene despliegues; ROUTB entregó avance y Recobra presentó. Esto no añade pruebas de funcionamiento ni cambia notas.

<a id="audioshare"></a>

## AudioShare

Rama **master**, [1af6e5ca727e60ef64cda6e31af71ab73bc9c9da](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da), fecha del commit 2026-10-19T06:41:04Z (UTC).

La rama principal y el README no cambian respecto al seguimiento del 22 de octubre. Se mantienen la pista compartida y los controles de pausa/reanudación, con CI, Flutter y publicación de imagen exitosos para esa misma punta. La URL institucional sigue sirviendo el cliente legado según el README; no atribuirle automáticamente el build Flutter web.

**Próximos pasos:**
- Tabla crear sala/PLAY/pausa → garantía, separando transacción SQLite y publicación NDJSON; declarar comportamiento si falla entre ambos.
- Definir invalidación o URL versionada de /track (max-age=3600), y actualizar arc42 §8 que aún describe MockAudioService.
- ADR de decisión de datos más costosa de revertir con comparación y garantías de entrega/reconexión de eventos.

**Tablero:** 2 abiertas / 2 cerradas; 2 abiertas sin responsable. **README:** Institucional. Endpoint institucional; la imagen publicada sirve cliente legado, no Flutter web.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/2): fusionada 2026-09-01T14:56:35Z; [#1](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/1): fusionada 2026-08-31T03:06:48Z.

**CI/sondeos consultados:** [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299344): success; [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299270): success; [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299234): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/README.md) · [docs/arc42/src/08_concepts.adoc](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/arc42/src/08_concepts.adoc) · [src/app.ts](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/app.ts) · [docs/idempotencia-y-saga.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/idempotencia-y-saga.md).

<a id="sistema-de-calificacion-automatica"></a>

## QuantIA

Rama **master**, [044d92347c71416f6192973eec84b22a7b6136f7](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/044d92347c71416f6192973eec84b22a7b6136f7), fecha del commit 2026-10-23T20:38:30Z (UTC).

Hay avances nuevos en recepción de lotes: errores de almacenamiento/bitácora se reportan por hoja sin abortar todo el lote, el encolado tiene un presupuesto temporal de lote, las hojas se leen de una en una con límite de 20 MB y la confirmación pasa a un hilo fuera del event loop. Se reutiliza el cliente Redis y un timeout al consumir ya no se trata como cola vacía. También se corrigen equivalencias/distractores, mensajes de carga, límite diario y división por cero en el panel. CI actual registra frontend y backend exitosos, incluida la suite completa, contrato y modos de fallo. README y documentos de arquitectura no cambiaron: conservan deuda de almacenamiento efímero, falta de acuse en la cola y reintento no automatizado. Estas mejoras no acreditan persistencia durable ni cierran S12 por sí solas.

**Próximos pasos:**
- Actualizar la tabla operación→garantía para recibir, registrar y consumir hojas, diferenciando archivo/bitácora, publicación y BLPOP sin acuse; contrastar al menos dos recorridos con el código nuevo.
- Volver a medir EC-07 con almacenamiento y Redis reales: el plazo de encolado no limita por sí solo la lectura/escritura completa del lote. Conservar límites de disco efímero, reconciliación y entrega ante pérdida del worker.
- Resolver el ADR comparativo de persistencia/R-06 y justificar caché o no caché con política de invalidación; sincronizar README, arc42 §8 y C4 con la implementación actual. Publicar dominio institucional.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin responsable. **README:** Externo. Sitio y API en Render, sin subdominio institucional.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin fusión registrada.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40020805501): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/044d92347c71416f6192973eec84b22a7b6136f7/README.md) · [docs/arc42/arc42-template-ES.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/044d92347c71416f6192973eec84b22a7b6136f7/docs/arc42/arc42-template-ES.md) · [docs/evidencia/modos-de-fallo.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/044d92347c71416f6192973eec84b22a7b6136f7/docs/evidencia/modos-de-fallo.md) · [backend/ingesta/recepcion.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/044d92347c71416f6192973eec84b22a7b6136f7/backend/ingesta/recepcion.py) · [backend/infraestructura/almacen.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/044d92347c71416f6192973eec84b22a7b6136f7/backend/infraestructura/almacen.py) · [backend/infraestructura/cola.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/044d92347c71416f6192973eec84b22a7b6136f7/backend/infraestructura/cola.py) · [backend/api/main.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/044d92347c71416f6192973eec84b22a7b6136f7/backend/api/main.py) · [backend/tests/test_durabilidad_recepcion.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/044d92347c71416f6192973eec84b22a7b6136f7/backend/tests/test_durabilidad_recepcion.py).

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [a237dd2f22b02bb547f87a07d15b6d31ea0dc758](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/a237dd2f22b02bb547f87a07d15b6d31ea0dc758), fecha del commit 2026-10-19T04:51:37Z (UTC).

No hay cambios en la rama principal respecto al 22 de octubre. La PR #60 permanece abierta, sin incorporación a master. Se mantienen los workflows exitosos de Compose/persistencia y contrato del cliente, y el fallo del workflow de flujo real observado previamente en Android. La documentación del despliegue distingue correctamente API institucional y frontend Pages; no anunciar toda la validación como verde.

**Próximos pasos:**
- Tabla crear/cambiar estado/ocultar publicación → garantía, distinguiendo transacciones MySQL de compensación SQL/archivos.
- Decidir caché o no caché de catálogo y actualización tras crear/cambiar visibilidad; incorporarlo a arc42 §8.
- ADR de costo comparativo de reversión de datos; reproducir/corregir flujo Android y resolver PR #60 sin llamar todo CI verde.

**Tablero:** 1 abiertas / 0 cerradas; 1 abiertas sin responsable. **README:** Institucional. API institucional, interfaz Flutter en GitHub Pages: cumplimiento parcial del sitio. Azure aparece solo como histórico.

**PR consultadas:** [#59](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/59): fusionada 2026-10-19T04:51:37Z; [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60): abierta, no integrada; [#57](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/57): fusionada 2026-10-19T04:17:24Z; [#58](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/58): fusionada 2026-10-19T04:04:00Z; [#56](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/56): fusionada 2026-10-19T03:17:47Z; [#55](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/55): fusionada 2026-10-12T04:50:45Z; [#54](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/54): fusionada 2026-10-04T07:14:35Z; [#53](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/53): fusionada 2026-10-04T06:38:56Z; [#52](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/52): fusionada 2026-10-04T04:04:41Z; [#51](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/51): fusionada 2026-10-04T03:06:42Z; [#50](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/50): fusionada 2026-10-03T21:52:57Z; [#49](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/49): fusionada 2026-10-03T21:06:43Z; [#48](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/48): fusionada 2026-10-03T12:34:44Z; [#47](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/47): fusionada 2026-10-03T12:16:51Z; [#46](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/46): fusionada 2026-10-02T05:11:13Z; [#45](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/45): fusionada 2026-10-02T04:55:41Z; [#44](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/44): fusionada 2026-09-28T04:50:19Z; [#43](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/43): fusionada 2026-09-28T04:16:49Z; [#42](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/42): fusionada 2026-09-18T00:35:06Z; [#41](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/41): fusionada 2026-09-16T06:28:41Z; [#40](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/40): fusionada 2026-09-16T05:51:55Z; [#39](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/39): fusionada 2026-09-15T12:47:51Z; [#38](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/38): fusionada 2026-09-15T06:06:58Z; [#37](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/37): fusionada 2026-09-15T05:25:33Z; [#36](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/36): fusionada 2026-09-13T05:42:06Z; [#35](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/35): fusionada 2026-09-13T05:05:38Z; [#34](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/34): fusionada 2026-09-13T02:51:03Z; [#32](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/32): fusionada 2026-09-06T21:05:15Z; [#31](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/31): fusionada 2026-09-06T20:13:45Z; [#30](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/30): fusionada 2026-09-06T20:06:07Z.

**CI/sondeos consultados:** [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586404): success; [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586378): success; [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586366): failure; [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586343): success; [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586312): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/README.md) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/arc42/08-conceptos-transversales.md) · [backend/app/publicaciones/repository.py](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/backend/app/publicaciones/repository.py).

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, [b82c8e511133a868e8b1c321fb7be3b70d6afed5](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/b82c8e511133a868e8b1c321fb7be3b70d6afed5), fecha del commit 2026-10-20T14:09:32Z (UTC).

La rama principal y el README permanecen sin cambios respecto al 22 de octubre. Los dos workflows consultados continúan fallidos y la PR #1 sigue abierta; no se atribuye integración por la existencia de la PR. Sigue siendo necesario conciliar las afirmaciones de PostgreSQL/Supabase con el adaptador en memoria conectado al flujo de publicaciones, y documentar la URL pública real.

**Próximos pasos:**
- Contrastar crear/listar publicaciones y declarar garantía real en memoria, no atribuir transacción PostgreSQL al adaptador conectado.
- Definir caché/no caché y política tras escritura; sincronizar C4 con almacén real y estado planeado de PostgreSQL/Dokploy.
- ADR comparativo de decisión de datos/reversión; actualizar arc42 §8 y documentar URL iscoutb.dev.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin responsable. **README:** Sin URL concreta. README raíz sin URL pública concreta.

**PR consultadas:** [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3): fusionada 2026-10-05T05:46:36Z; [#2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2): fusionada 2026-09-21T04:56:52Z; [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta, no integrada.

**CI/sondeos consultados:** [.github/workflows/contrato.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39436726678): failure; [.github/workflows/backend-tests.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39436724661): failure. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/b82c8e511133a868e8b1c321fb7be3b70d6afed5/README.md) · [docs/arc42/08_conceptos_transversales.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/b82c8e511133a868e8b1c321fb7be3b70d6afed5/docs/arc42/08_conceptos_transversales.md) · [backend/src/linkclub/adapters/inbound/api/publicacion_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/b82c8e511133a868e8b1c321fb7be3b70d6afed5/backend/src/linkclub/adapters/inbound/api/publicacion_router.py).

<a id="dinamikutb"></a>

## Dinamik

Rama **master**, [8dad79338a66cd7054a0bde3f98661f785f5c378](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/8dad79338a66cd7054a0bde3f98661f785f5c378), fecha del commit 2026-10-24T05:05:10Z (UTC).

Hay avance importante integrado mediante las PR #36 y #37: autenticación JWT, roles y restricciones de acceso, auditoría de cambios, pantallas de login/perfil/gestión y preparación de API/Compose con PostgreSQL y CORS. La PR #35 está cerrada sin fusionar; no confundirla con las integraciones posteriores. El CI actual registra backend, frontend y scanner Sonar exitosos, además de Pages. README y arc42 todavía dicen que Usuarios no tiene código y mantienen F7 pendiente: recrear/resembrar la base de demostración antes del 25 de octubre. El Compose y el build de Pages no prueban que esa operación se haya realizado; expiración del 27 de octubre y condiciones del proveedor son afirmaciones del equipo, no verificadas aquí.

**Próximos pasos:**
- Atender y documentar F7 antes del plazo declarado del 25/oct: evidencia de recreación/resembrado o migración y verificación de datos/health. No darlo por resuelto por CI o Compose; usar solamente datos sintéticos de demo.
- Actualizar README, C4 y arc42 para reconocer autenticación/roles y la implementación de Usuarios. Publicar URL institucional real y aclarar cuál entorno sirve la API.
- Completar tabla de garantías y contrastar consulta/actualización: el servicio sigue leyendo y haciendo commit sin control de versión, con última escritura ganadora. Justificar caché/no caché e invalidación; ADR comparativo del costo de reversión y arc42 §8.

**Tablero:** 2 abiertas / 15 cerradas; 1 abiertas sin responsable. **README:** Externo. README mantiene frontend Pages y backend Render; no publica URL institucional. F7 sigue pendiente en la documentación.

**PR consultadas:** [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35): cerrada sin fusión registrada; [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37): fusionada 2026-10-23T03:04:11Z; [#36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36): fusionada 2026-10-23T01:01:46Z; [#33](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/33): fusionada 2026-09-27T17:38:37Z; [#32](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/32): fusionada 2026-09-22T03:51:10Z; [#31](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/31): fusionada 2026-09-22T03:16:20Z; [#30](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/30): fusionada 2026-09-21T18:41:30Z; [#29](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/29): fusionada 2026-09-21T17:48:40Z; [#12](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/12): fusionada 2026-09-07T04:26:25Z; [#11](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/11): fusionada 2026-09-07T03:57:51Z; [#10](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/10): fusionada 2026-08-31T18:47:14Z; [#9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/9): fusionada 2026-08-31T18:32:43Z; [#8](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/8): fusionada 2026-08-31T05:11:21Z; [#7](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/7): fusionada 2026-08-31T04:52:24Z; [#6](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/6): fusionada 2026-08-31T04:21:48Z; [#5](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/5): fusionada 2026-08-31T03:00:17Z; [#4](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/4): fusionada 2026-08-24T03:26:31Z; [#3](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/3): fusionada 2026-08-24T03:10:21Z; [#2](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/2): fusionada 2026-08-24T02:31:51Z; [#1](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/1): fusionada 2026-08-24T02:02:03Z.

**CI/sondeos consultados:** [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40064883930): success; [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40064883888): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/README.md) · [docs/arc42/08-cross-cutting-concepts.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/docs/arc42/08-cross-cutting-concepts.md) · [backend/app/requisitos/service.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/backend/app/requisitos/service.py) · [backend/app/usuarios/dependencies.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/backend/app/usuarios/dependencies.py) · [backend/app/usuarios/service.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/backend/app/usuarios/service.py) · [backend/app/requisitos/router.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/backend/app/requisitos/router.py) · [deploy/compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/deploy/compose.lab.yaml) · [docs/arc42/11-risks-and-technical-debt.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/docs/arc42/11-risks-and-technical-debt.md).

<a id="drift"></a>

## Drift

Rama **master**, [aa1578a1e81709418b502154999c2420352dd86e](https://github.com/ISCOUTB/AS_202620_Drift/commit/aa1578a1e81709418b502154999c2420352dd86e), fecha del commit 2026-10-21T04:53:31Z (UTC).

La rama principal no cambia respecto al 22 de octubre; continúan disponibles la matriz de seis operaciones y garantías, la invalidación por fuente y el ADR 0010 sobre costo de reversión. Los runs de CI y Azure de esa punta figuran exitosos. Se conserva la distinción entre evidencia simulada con sustituto de httpx y rendimiento real de producción; no volver a marcar esos artefactos S12 como ausentes.

**Próximos pasos:**
- Revisar/aceptar ADR 0010 con equipo; su conclusión es identidad/contrato público del juego, no persistencia, como decisión actual más costosa.
- Repetir experimento con dependencias reales y enlazar run/resultado, manteniendo separación de simulación, red real y latencia HTTP extremo a extremo.
- Probar y decidir límites de edad/aviso para tasa stale, catálogo por instancia/reinicio y respuesta vacía sin aviso si falta fallback; conservar pruebas de sync atómico y TTL.

**Tablero:** 5 abiertas / 15 cerradas; 5 abiertas sin responsable. **README:** Institucional. Frontend/backend institucionales y alternativas Azure/Vercel documentadas. No se repitió prueba funcional.

**PR consultadas:** [#31](https://github.com/ISCOUTB/AS_202620_Drift/pull/31): fusionada 2026-10-21T04:53:32Z; [#30](https://github.com/ISCOUTB/AS_202620_Drift/pull/30): fusionada 2026-10-19T03:20:50Z; [#29](https://github.com/ISCOUTB/AS_202620_Drift/pull/29): fusionada 2026-10-19T03:07:18Z; [#28](https://github.com/ISCOUTB/AS_202620_Drift/pull/28): fusionada 2026-10-19T02:08:58Z; [#27](https://github.com/ISCOUTB/AS_202620_Drift/pull/27): fusionada 2026-10-12T19:42:41Z; [#26](https://github.com/ISCOUTB/AS_202620_Drift/pull/26): fusionada 2026-10-12T19:15:32Z; [#25](https://github.com/ISCOUTB/AS_202620_Drift/pull/25): fusionada 2026-10-12T04:49:54Z; [#24](https://github.com/ISCOUTB/AS_202620_Drift/pull/24): fusionada 2026-10-11T05:28:23Z; [#23](https://github.com/ISCOUTB/AS_202620_Drift/pull/23): fusionada 2026-10-11T05:21:57Z; [#22](https://github.com/ISCOUTB/AS_202620_Drift/pull/22): fusionada 2026-10-11T04:53:50Z; [#21](https://github.com/ISCOUTB/AS_202620_Drift/pull/21): fusionada 2026-10-11T03:47:58Z.

**CI/sondeos consultados:** [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39546508693): success; [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39546508600): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/README.md) · [docs/arc42/arc42_8_conceptos_transversales.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/docs/arc42/arc42_8_conceptos_transversales.md) · [docs/adr/0010-costo-de-reversion-de-las-decisiones-de-datos.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/docs/adr/0010-costo-de-reversion-de-las-decisiones-de-datos.md) · [docs/evidencias/s12-steam-degradado.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/docs/evidencias/s12-steam-degradado.md) · [backend/app/application/usecases/sync_playstation_catalog.py](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/backend/app/application/usecases/sync_playstation_catalog.py) · [backend/app/infrastructure/persistence/in_memory_playstation_catalog.py](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/backend/app/infrastructure/persistence/in_memory_playstation_catalog.py) · [backend/app/infrastructure/external/single_flight_cache.py](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/backend/app/infrastructure/external/single_flight_cache.py).

<a id="elmapita"></a>

## ElMapita

Rama **main**, [0421885424d13478cf33c717fdd933a4748d9025](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/0421885424d13478cf33c717fdd933a4748d9025), fecha del commit 2026-10-19T08:33:59Z (UTC).

La rama principal y el README no cambian respecto al 22 de octubre; el CI de esa punta continúa registrado como exitoso. Se conserva la confirmación docente de presentación y funcionamiento. Falta publicar la dirección exacta del despliegue bajo iscoutb.dev: localhost y un ejemplo de Supabase no satisfacen el requisito documental.

**Próximos pasos:**
- Publicar URL exacta iscoutb.dev del despliegue mostrado, sin inventar host.
- Tabla operaciones reales (cargar edificio/registro o rol) → garantía y dos recorridos de código; definir invalidación/versionado al reemplazar modelo, no solo TTL.
- ADR comparativo del costo de revertir datos y llevar consistencia/caché a arc42 §8, hoy solo errores/privacidad/internacionalización.

**Tablero:** 1 abiertas / 0 cerradas; 1 abiertas sin responsable. **README:** Sin URL concreta. README solo localhost y placeholder Supabase. Presentación y funcionamiento confirmados por el docente; brecha documental, no ausencia de despliegue.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/39223716465): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/README.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/docs/arc42/arc42-template-EN.md).

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [6e546a956d3235ce820c9909edbf13f9415f1d93](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/6e546a956d3235ce820c9909edbf13f9415f1d93), fecha del commit 2026-10-21T13:36:21Z (UTC).

No hay cambios en la rama principal respecto al 22 de octubre. Se conserva el avance de registro/login y usuarios PostgreSQL, mientras Invitaciones sigue en memoria. El CI de esa punta sigue fallido y Pages figura exitoso; esto no equivale a pruebas aprobadas ni demuestra la disponibilidad del backend. El README todavía no describe el nuevo módulo ni una URL pública concreta.

**Próximos pasos:**
- Corregir CI y agregar pruebas registro/login/migración; diferenciar persistencia PostgreSQL de Usuarios y memoria de Invitaciones.
- Tabla registrar usuario/crear y responder invitaciones → garantías, incluida atomicidad de lote y concurrencia; contrastar dos operaciones.
- Decidir caché/no caché, ADR comparativo persistencia/identidad, actualizar C4/arc42 §8 y README con URL pública iscoutb.dev real.

**Tablero:** 1 abiertas / 0 cerradas; 0 abiertas sin responsable. **README:** Sin URL concreta. Declara contenedor Dokploy desplegado, pero URL pública pendiente; no hay host concreto.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/2): fusionada 2026-09-28T02:39:59Z.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/39609478651): failure; [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/39609478211): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/README.md) · [src/usuarios/aplicacion/registrar_usuario.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/src/usuarios/aplicacion/registrar_usuario.py) · [app/web.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/app/web.py) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/docs/arc42/08-conceptos-transversales.md) · [src/invitaciones/infraestructura/repositorio_memoria.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/src/invitaciones/infraestructura/repositorio_memoria.py).

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, [1a706525f6a660c216bc11655c754f65bbbe8bfe](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/1a706525f6a660c216bc11655c754f65bbbe8bfe), fecha del commit 2026-10-20T18:38:58Z (UTC).

Sin cambios en la rama principal desde el seguimiento del 22 de octubre. El CI publicado sigue exitoso, pero el workflow no incorpora test:postgres. El README mantiene la frase de que Flutter no está integrado pese a existir llamadas HTTP en el cliente; corregir la documentación sin confundirla con una ausencia de código. Las 16 issues abiertas con responsables requieren conciliación con lo implementado, no equivalen a 16 defectos confirmados.

**Próximos pasos:**
- Completar tabla operación→garantía para consulta, entrada y salida y contrastar dos operaciones con transacciones PostgreSQL.
- Justificar no caché o documentar invalidación; comparar costo de reversión en un ADR y consolidar arc42 §8/C4.
- Incorporar pruebas PostgreSQL en CI y actualizar README y tablero con evidencia.

**Tablero:** 16 abiertas / 0 cerradas; 0 abiertas sin responsable. **README:** Institucional. Backend institucional; no acredita interfaz Flutter pública.

**PR consultadas:** [#17](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/17): fusionada 2026-10-19T01:09:26Z.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/39476599936): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/README.md) · [docs/arc42/arc42_gimnasio_utb.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/docs/arc42/arc42_gimnasio_utb.md) · [docs/Flutter/lib/core/api/aforo_api.dart](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/docs/Flutter/lib/core/api/aforo_api.dart) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/.github/workflows/ci.yml).

<a id="inventrack"></a>

## InvenTrack

Rama **main**, [f9df6a32b63c2a19b134822bfe95db06031708f0](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/f9df6a32b63c2a19b134822bfe95db06031708f0), fecha del commit 2026-10-24T06:56:01Z (UTC).

Hay avance S12: docs/aspectos.md incorpora una tabla de cinco operaciones y garantías, con límites explícitos de memoria, una instancia y ausencia de deduplicación durable. La lectura de registrar_entrada y registrar_salida confirma el lock por SKU; esto no aporta durabilidad ni coordinación entre réplicas. También se refactorizó el router para centralizar errores. El CI vigente ejecutó Pytest con cobertura, validación del contrato y el paso de scanner correctamente; no se infiere un Quality Gate independiente solo del scanner.

**Próximos pasos:**
- Añadir rutas y pruebas concretas a la tabla para dejar trazables dos operaciones; no confundir respuestas HTTP distintas con pérdida automática de idempotencia del efecto.
- Justificar no caché o definir diseño e invalidación; documentar comparativamente la decisión de datos más costosa de revertir.
- Llevar consistencia/caché a arc42 §8 y alinear C4 con RAM dentro del proceso, diferenciando SQL futuro.

**Tablero:** 0 abiertas / 7 cerradas; 0 abiertas sin responsable. **README:** Institucional. API institucional y alternativa Render; frontend Flutter sigue pendiente en el README.

**CI/sondeos consultados:** [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40072153783): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/f9df6a32b63c2a19b134822bfe95db06031708f0/README.md) · [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/f9df6a32b63c2a19b134822bfe95db06031708f0/docs/aspectos.md) · [app/inventario/application/registrar_movimiento.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/f9df6a32b63c2a19b134822bfe95db06031708f0/app/inventario/application/registrar_movimiento.py) · [app/inventario/infrastructure/router.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/f9df6a32b63c2a19b134822bfe95db06031708f0/app/inventario/infrastructure/router.py) · [docs/c4/containers.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/f9df6a32b63c2a19b134822bfe95db06031708f0/docs/c4/containers.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/f9df6a32b63c2a19b134822bfe95db06031708f0/docs/arc42/arc42-template-EN.md).

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [6d4e1293c7660119e05c1c4f9559f970ddb6f2d6](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/6d4e1293c7660119e05c1c4f9559f970ddb6f2d6), fecha del commit 2026-10-22T19:07:21Z (UTC).

Avance sustancial S12: ya existe tabla de 14 operaciones, caché de catálogo write-through, política tras escritura, C4 sin Redis y ADR de identidad del pedido como decisión de datos más costosa de revertir. La creación ahora espera confirmación de PostgreSQL y el seguimiento exige token o sesión del dueño; se contrastaron esas rutas con código. La cola incorpora reintentos y DLQ, pero ambas son en memoria y no garantizan entrega tras caída del proceso. La PR de actualización de Next/React está fusionada. El CI y el despliegue Dokploy figuran exitosos; el job de despliegue pasó pruebas con base real, contrato y health check.

**Próximos pasos:**
- Publicar la URL institucional vigente y corregir frases históricas del README que aún llaman al frontend placeholder y a la persistencia pendiente.
- Añadir prueba de caída de PostgreSQL durante actualizarProducto para demostrar que no cambia la caché; mantener explícito el límite de un solo proceso y la ausencia de invalidación entre réplicas.
- Ratificar ADR0024, hoy propuesto, y actualizar su alternativa SERIAL que todavía dice que esperar la base contradice la creación, pese al cambio de ADR0026.
- Acotar at-least-once a reintentos/cola volátil, probar recuperación o documentar pérdida de pendientes/DLQ tras reinicio; no equiparar polling con un plazo extremo a extremo garantizado.

**Tablero:** 0 abiertas / 14 cerradas; 0 abiertas sin responsable. **README:** Sin URL concreta. README raíz aún sin URL vigente concreta. Azure figura retirado; el CI de Dokploy exitoso no sustituye publicar la dirección.

**PR consultadas:** [#15](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/15): fusionada 2026-10-22T19:07:22Z.

**CI/sondeos consultados:** [Deploy Dokploy (laboratorio de la U)](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39837330233): success; [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39837330073): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/6d4e1293c7660119e05c1c4f9559f970ddb6f2d6/README.md) · [docs/evidencias/evidencias-s12.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/6d4e1293c7660119e05c1c4f9559f970ddb6f2d6/docs/evidencias/evidencias-s12.md) · [docs/adr/0024-identidad-del-pedido.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/6d4e1293c7660119e05c1c4f9559f970ddb6f2d6/docs/adr/0024-identidad-del-pedido.md) · [docs/adr/0026-escrituras-at-least-once-y-creacion-confirmada.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/6d4e1293c7660119e05c1c4f9559f970ddb6f2d6/docs/adr/0026-escrituras-at-least-once-y-creacion-confirmada.md) · [backend/src/http/crear-pedido.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/6d4e1293c7660119e05c1c4f9559f970ddb6f2d6/backend/src/http/crear-pedido.js) · [backend/src/modules/catalogo/index.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/6d4e1293c7660119e05c1c4f9559f970ddb6f2d6/backend/src/modules/catalogo/index.js) · [backend/src/persistencia/despachador.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/6d4e1293c7660119e05c1c4f9559f970ddb6f2d6/backend/src/persistencia/despachador.js).

<a id="lostvault"></a>

## LostVault

Rama **main**, [e19be366f7e922a8a9c9abd4a808899f14b2999b](https://github.com/ISCOUTB/AS_202620_LostVault/commit/e19be366f7e922a8a9c9abd4a808899f14b2999b), fecha del commit 2026-10-20T16:16:33Z (UTC).

La rama principal no cambió desde el seguimiento anterior. Se mantiene la API FastAPI incorporada con JWT, lock e Idempotency-Key, pero el almacenamiento continúa en RAM. Los workflows publicados siguen verdes; Backend checks prueba backend/test_api.py, no la suite api/tests de la nueva API. El README raíz sigue describiendo el corte Flutter y no publica una URL desplegada.

**Próximos pasos:**
- Incluir api/tests en CI y aclarar el enlace entre api/, backend/ y el cliente Flutter.
- Publicar URL real iscoutb.dev en el README raíz sin inventar dominio.
- Completar tabla de garantías y dos operaciones, caché o exclusión razonada, ADR comparativo y C4/arc42 §8 coherentes con límites de proceso y reinicio.

**Tablero:** 0 abiertas / 1 cerradas; 0 abiertas sin responsable. **README:** Sin URL concreta. README raíz sin URL pública concreta. La nueva API no prueba por sí sola despliegue.

**PR consultadas:** [#19](https://github.com/ISCOUTB/AS_202620_LostVault/pull/19): fusionada 2026-10-20T16:16:34Z; [#18](https://github.com/ISCOUTB/AS_202620_LostVault/pull/18): fusionada 2026-10-19T01:43:15Z; [#17](https://github.com/ISCOUTB/AS_202620_LostVault/pull/17): fusionada 2026-10-19T01:32:11Z; [#16](https://github.com/ISCOUTB/AS_202620_LostVault/pull/16): fusionada 2026-10-05T03:30:54Z; [#15](https://github.com/ISCOUTB/AS_202620_LostVault/pull/15): fusionada 2026-10-05T02:31:39Z; [#14](https://github.com/ISCOUTB/AS_202620_LostVault/pull/14): fusionada 2026-10-05T00:42:49Z; [#13](https://github.com/ISCOUTB/AS_202620_LostVault/pull/13): fusionada 2026-09-28T04:39:31Z; [#12](https://github.com/ISCOUTB/AS_202620_LostVault/pull/12): fusionada 2026-09-28T03:17:55Z; [#11](https://github.com/ISCOUTB/AS_202620_LostVault/pull/11): cerrada sin fusión registrada; [#10](https://github.com/ISCOUTB/AS_202620_LostVault/pull/10): fusionada 2026-09-21T04:55:35Z; [#9](https://github.com/ISCOUTB/AS_202620_LostVault/pull/9): fusionada 2026-09-13T23:43:59Z; [#8](https://github.com/ISCOUTB/AS_202620_LostVault/pull/8): fusionada 2026-09-13T18:41:09Z; [#2](https://github.com/ISCOUTB/AS_202620_LostVault/pull/2): cerrada sin fusión registrada; [#6](https://github.com/ISCOUTB/AS_202620_LostVault/pull/6): fusionada 2026-08-24T22:41:15Z; [#5](https://github.com/ISCOUTB/AS_202620_LostVault/pull/5): fusionada 2026-08-24T18:27:25Z.

**CI/sondeos consultados:** [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39455997158): success; [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39455997151): success; [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39455997101): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/README.md) · [api/app/store.py](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/api/app/store.py) · [api/README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/api/README.md) · [.github/workflows/backend.yml](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/.github/workflows/backend.yml).

<a id="mapsutb"></a>

## MapsUTB

Rama **master**, [4b8fa088faec96772e76c8c4f2782919ec87a9b9](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/4b8fa088faec96772e76c8c4f2782919ec87a9b9), fecha del commit 2026-10-16T17:38:48Z (UTC).

La rama principal permanece sin cambios desde el 16 de octubre. La sonda de disponibilidad del 24 de octubre a las 12:36 UTC terminó correctamente; es un sondeo, no una prueba integral. Las issues Sonar de complejidad y ternario siguen abiertas y sin responsable. El README publica Firebase, todavía sin dirección institucional; no confundir este proyecto con ElMapita.

**Próximos pasos:**
- Asignar y resolver las dos issues Sonar con evidencia de cierre.
- Publicar URL institucional exacta, manteniendo Firebase como alternativa si corresponde.
- Completar tabla de operaciones/garantías, invalidación de caché interna del grafo además de HTTP, ADR de reversión y arc42 §8.

**Tablero:** 2 abiertas / 52 cerradas; 2 abiertas sin responsable. **README:** Externo. Sitio Firebase, fuera de iscoutb.dev; distinto de ElMapita.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z.

**CI/sondeos consultados:** [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40094634256): success; [Sincronizar hallazgos de Sonar a GitHub Issues](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40093576618): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/README.md) · [docs/arc42/08_concepts.adoc](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/arc42/08_concepts.adoc) · [lib/features/busqueda/indice_busqueda.dart](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/lib/features/busqueda/indice_busqueda.dart).

<a id="pideutb"></a>

## PideUtb

Rama **master**, [ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f), fecha del commit 2026-10-23T15:04:06Z (UTC).

La PR de identidad visual ya se fusionó el 23 de octubre: integra el sistema de diseño, la hoja de estilos y el índice del README. El CI de master pasó contratos, dependencias y Pytest en Python 3.11/3.12 con comprobación de ejecución PostgreSQL. Atención al alcance: el job SonarCloud termina success, pero sus pasos de análisis, cobertura y espera del Quality Gate quedaron skipped; no acredita un Gate aprobado. La aceptación visual de las pantallas a 375 px, ambos temas y teclado no fue verificada en esta revisión. Se conserva la confirmación docente de presentación y despliegues.

**Próximos pasos:**
- Verificar y registrar aceptación visual según su guía de diseño; el verde de pruebas backend no la sustituye.
- Restablecer evidencia de análisis y Quality Gate reales o documentar el análisis omitido; no reportarlo aprobado por el nombre del job.
- Para S12, distinguir el UPDATE condicional de marcar_pagado de actualizar_estado, que actualiza por id sin estado esperado; contrastar carreras y ajustar las garantías declaradas. Completar ADR comparativo de reversión y conciliar intervalos/documentación.

**Tablero:** 1 abiertas / 0 cerradas; 1 abiertas sin responsable. **README:** Institucional. Sitio, panel y API institucionales. Presentación y despliegues confirmados por docente; sin nueva aceptación visual independiente.

**PR consultadas:** [#29](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/29): fusionada 2026-10-23T15:04:06Z; [#28](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/28): fusionada 2026-10-20T14:55:39Z; [#27](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/27): fusionada 2026-10-18T23:40:46Z; [#26](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/26): fusionada 2026-10-18T22:31:12Z; [#25](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/25): fusionada 2026-10-18T18:31:49Z; [#24](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/24): fusionada 2026-10-18T17:05:21Z; [#23](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/23): fusionada 2026-10-18T15:44:46Z; [#22](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/22): fusionada 2026-10-18T02:49:18Z; [#21](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/21): fusionada 2026-10-18T02:12:59Z; [#20](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/20): fusionada 2026-10-18T01:32:03Z; [#19](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/19): fusionada 2026-10-14T15:16:39Z; [#18](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/18): fusionada 2026-10-12T19:27:07Z; [#16](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/16): fusionada 2026-10-12T19:04:21Z; [#17](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/17): fusionada 2026-10-12T19:03:14Z; [#15](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/15): fusionada 2026-10-04T17:47:55Z.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39975061857): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/README.md) · [docs/sistema-de-diseno.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/docs/sistema-de-diseno.md) · [sitio/estilos.css](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/sitio/estilos.css) · [backend/app/pedidos/repository.py](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/backend/app/pedidos/repository.py) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/docs/arc42/arc42.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/.github/workflows/ci.yml).

<a id="recobra"></a>

## Recobra

Rama **master**, [aacc1ec4094573e15758a245e6c6954a5b76fd48](https://github.com/ISCOUTB/AS_202620_Recobra/commit/aacc1ec4094573e15758a245e6c6954a5b76fd48), fecha del commit 2026-10-21T23:19:18Z (UTC).

Sin nuevos commits respecto al seguimiento del 22 de octubre. Se mantienen los avances S12 ya reconocidos: caché HTTP/ETag, estrategia de eventos y ADR comparativo de reversión. El CI de esa punta continúa exitoso; no se presenta como una nueva ejecución de hoy. Siguen siendo relevantes los límites declarados de EventEmitter no durable y la cobertura PostgreSQL de siete de nueve adaptadores; los e2e completos aún usan RAM. Presentación confirmada por el docente.

**Próximos pasos:**
- Extender pruebas PostgreSQL a Reclamaciones y Sesiones y a los e2e completos.
- Corregir la afirmación de que desplegar invalida lugares: un navegador puede conservar la respuesta durante max-age; mantener explícito el TTL de miniaturas tras borrado.
- Conservar límites de cola/eventos, y aportar evidencia de restauración de backups y alertas operativas sin negar los artefactos S12 existentes.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin responsable. **README:** Institucional. Vitrina y app institucionales. Docente confirmó presentación; no se añadió una auditoría funcional.

**CI/sondeos consultados:** [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39692648288): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/README.md) · [docs/adr/0025-diseno-de-cache-y-politica-de-invalidacion.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/docs/adr/0025-diseno-de-cache-y-politica-de-invalidacion.md) · [docs/adr/0027-la-decision-de-datos-mas-costosa-de-revertir.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/docs/adr/0027-la-decision-de-datos-mas-costosa-de-revertir.md) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/docs/arc42/arc42.md).

<a id="routb"></a>

## ROUTB

Rama **master**, [5d686a594d3e3515233e60b4e6b33330ded05572](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/5d686a594d3e3515233e60b4e6b33330ded05572), fecha del commit 2026-10-23T14:47:48Z (UTC).

La PR de S12 se fusionó el 23 de octubre e incorpora cambios reales de mapas en Flutter, paradas de solicitudes y retiro del endpoint y de geocode_cache del backend mediante migración. Ya hay tabla de operaciones y ADR de costo de reversión, pero arc42 §8.6–8.7, ADR0020 y la política de invalidación describen la caché retirada como vigente. Corregir esa contradicción; route_cache es otra caché que permanece. El CI de master pasó migraciones, pruebas, contrato y build; el job titulado SonarCloud Scan & Quality Gate solo ejecuta un mensaje de reserva sin scanner, por lo que no acredita análisis ni Gate. El docente confirmó avance presentado.

**Próximos pasos:**
- Actualizar arc42, ADR0020, política de caché y C4 a la geocodificación en cliente y distinguirla de route_cache.
- Contrastar dos operaciones de solicitudes/cupos; el chequeo previo antes de INSERT no basta por sí solo para prometer ausencia de duplicados concurrentes: citar restricción y prueba o acotar garantía.
- Sustituir la reserva de Sonar por evidencia real de análisis/Gate; actualizar instrucciones de despliegue Render frente a Dokploy.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin responsable. **README:** Institucional. Backend institucional. README conserva instrucciones antiguas de Render; docente confirmó avance presentado.

**PR consultadas:** [#52](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/52): fusionada 2026-10-23T14:47:48Z; [#51](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/51): fusionada 2026-10-18T21:39:27Z; [#50](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/50): fusionada 2026-10-13T03:02:26Z; [#49](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/49): fusionada 2026-10-12T00:30:24Z; [#48](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/48): fusionada 2026-10-11T23:52:36Z; [#47](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/47): cerrada sin fusión registrada; [#46](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/46): fusionada 2026-10-03T23:20:32Z; [#45](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/45): fusionada 2026-10-03T22:57:29Z; [#44](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/44): fusionada 2026-10-03T19:53:46Z; [#43](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/43): fusionada 2026-10-03T05:18:30Z; [#42](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/42): fusionada 2026-10-03T01:18:46Z; [#41](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/41): cerrada sin fusión registrada; [#40](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/40): fusionada 2026-09-28T02:58:07Z; [#39](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/39): fusionada 2026-09-26T19:17:57Z; [#38](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/38): cerrada sin fusión registrada.

**CI/sondeos consultados:** [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40077189117): success; [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39972693861): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5d686a594d3e3515233e60b4e6b33330ded05572/README.md) · [docs/arc42/08_conceptos_transversales.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5d686a594d3e3515233e60b4e6b33330ded05572/docs/arc42/08_conceptos_transversales.md) · [docs/adr/0020-decision-datos-mas-costosa-de-revertir.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5d686a594d3e3515233e60b4e6b33330ded05572/docs/adr/0020-decision-datos-mas-costosa-de-revertir.md) · [backend/migrations/versions/009_retirar_geocode_cache.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5d686a594d3e3515233e60b4e6b33330ded05572/backend/migrations/versions/009_retirar_geocode_cache.py) · [backend/app/modules/requests/application/create_request.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5d686a594d3e3515233e60b4e6b33330ded05572/backend/app/modules/requests/application/create_request.py) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5d686a594d3e3515233e60b4e6b33330ded05572/.github/workflows/ci.yml).

<a id="shareu"></a>

## ShareU

Rama **master**, [39508608eae4c1a56a5e4fc11a055bf6afb2c003](https://github.com/ISCOUTB/AS_202620_ShareU/commit/39508608eae4c1a56a5e4fc11a055bf6afb2c003), fecha del commit 2026-09-29T00:56:57Z (UTC).

La rama principal no ha cambiado desde el seguimiento del 22 de octubre. Se mantiene el corte vertical de búsqueda SQLite, las PR #22 y #23 abiertas y el último workflow de pruebas fallido. No atribuir a master cambios que continúan en esas PR. Las diez issues abiertas incluyen cinco sin responsable; el tablero no certifica el estado de implementación.

**Próximos pasos:**
- Completar la tabla operación→garantía y contrastar dos operaciones reales; justificar no caché o definir invalidación de documentos/metadatos.
- Comparar el costo de reversión de decisiones de datos en un ADR y consolidar consistencia/caché en arc42 §8.
- Publicar URL oficial iscoutb.dev, resolver el pipeline y conciliar issues solapadas con evidencia.

**Tablero:** 10 abiertas / 10 cerradas; 5 abiertas sin responsable. **README:** Sin URL concreta. README mantiene placeholders Vercel/Render, no URL pública concreta.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta, no integrada; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta, no integrada; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z.

**CI/sondeos consultados:** [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458): failure; [Tests](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479388452): failure (otra revisión/rama; no acredita la punta principal). El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md) · [docs/c4/nivel2.mmd](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/c4/nivel2.mmd) · [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/.github/workflows/tests.yml).

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [5aa16fcf0152361901bf2500291235550ca40951](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/5aa16fcf0152361901bf2500291235550ca40951), fecha del commit 2026-10-22T18:55:56Z (UTC).

Desde el corte previo se actualizaron Dockerfile y documentación de Dokploy, conservando la URL institucional de la API. Se mantiene la confirmación docente de presentación y despliegue funcionando. No hay run de CI/CD para la punta nueva entre los runs consultados: los últimos exitosos corresponden al 20 de octubre, no al commit actual. El filtro paths agregado al workflow se interpreta como una cadena, no como lista YAML, por falta de espacio tras los guiones; además las rutas de workflow deben apuntar a su ubicación real. Esto requiere corregir el disparador y obtener evidencia nueva, sin concluir que el sitio esté caído.

**Próximos pasos:**
- Corregir paths en CI y verificar un run sobre la punta actual, distinguiendo validación del repositorio y funcionamiento del despliegue.
- Completar tabla de garantías y dos operaciones contrastadas: límites transaccionales de confirmar/notificar frente a crear tarea y enviar Telegram.
- Justificar caché/no caché, comparar costo de reversión en ADR y alinear PostgreSQL en C4 y consistencia/caché en arc42 §8.

**Tablero:** 3 abiertas / 4 cerradas; 2 abiertas sin responsable. **README:** Institucional. API institucional; Flutter sigue descrito como arquitectura objetivo. Presentación y funcionamiento confirmados por el docente.

**PR consultadas:** [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z; [#14](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/14): fusionada 2026-09-17T01:53:44Z; [#13](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/13): fusionada 2026-09-16T01:48:07Z; [#12](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/12): fusionada 2026-09-14T01:01:35Z; [#11](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/11): fusionada 2026-09-12T17:29:59Z; [#10](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/10): fusionada 2026-09-12T15:26:17Z; [#9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/9): fusionada 2026-09-11T02:08:20Z; [#8](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/8): fusionada 2026-09-11T00:36:16Z.

**CI/sondeos consultados:** [CD](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39441872010): success (otra revisión/rama; no acredita la punta principal); [CI](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39441578508): success (otra revisión/rama; no acredita la punta principal). El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/5aa16fcf0152361901bf2500291235550ca40951/README.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/5aa16fcf0152361901bf2500291235550ca40951/.github/workflows/ci.yml) · [backend/Dockerfile](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/5aa16fcf0152361901bf2500291235550ca40951/backend/Dockerfile) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/5aa16fcf0152361901bf2500291235550ca40951/docs/arc42/08-conceptos-transversales.md) · [docs/c4/C4-C2.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/5aa16fcf0152361901bf2500291235550ca40951/docs/c4/C4-C2.md).

<a id="tienda-virtual-utb"></a>

## Tienda Virtual

Rama **main**, [33005869413b2b69d502008fd7e163d094c16b6c](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/33005869413b2b69d502008fd7e163d094c16b6c), fecha del commit 2026-10-23T06:18:03Z (UTC).

Hay avance sustancial desde el 22 de octubre: frontend v4 y pnpm, migraciones Alembic, esquema PostgreSQL, bloqueo optimista y políticas RLS con rol de aplicación. arc42 §8 ya describe propiedad de tablas y pruebas reales contra PostgreSQL; no corresponde seguir diciendo que la persistencia no existe. El CI actual tiene frontend y backend exitosos, mientras Sonar falla al consultar metadatos JRE con HTTP403; no es un fallo de pruebas ni un Quality Gate evaluado. Los endpoints de pedidos y saga siguen explícitamente como diseño, aunque existan sus tablas.

**Próximos pasos:**
- Completar la tabla operación→garantía con catálogo/inventario reales y contrastar dos rutas; distinguir esquema disponible de endpoint implementado.
- Preservar no-store del proxy y explicar refresco/invalidez tras escritura; comparar en ADR el costo de revertir decisiones de datos, no solo enumerar nuevas migraciones.
- Ratificar ADR propuestos; documentar exportación previa y restauración antes de aplicar la migración que elimina tablas antiguas; corregir Sonar y publicar dominio iscoutb.dev.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin responsable. **README:** Externo. Sitio sslip externo; dominio definitivo pendiente. No se verificó redespliegue ni aceptación visual.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/1): fusionada 2026-10-21T16:14:34Z.

**CI/sondeos consultados:** [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/39910660527): failure. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/33005869413b2b69d502008fd7e163d094c16b6c/README.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/33005869413b2b69d502008fd7e163d094c16b6c/docs/arc42/arc42-template-EN.md) · [docs/adr/0013-migraciones-alembic-y-esquema.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/33005869413b2b69d502008fd7e163d094c16b6c/docs/adr/0013-migraciones-alembic-y-esquema.md) · [docs/adr/0014-seguridad-rls.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/33005869413b2b69d502008fd7e163d094c16b6c/docs/adr/0014-seguridad-rls.md) · [backend/app/modules/inventory/models.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/33005869413b2b69d502008fd7e163d094c16b6c/backend/app/modules/inventory/models.py) · [backend/tests/test_rls.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/33005869413b2b69d502008fd7e163d094c16b6c/backend/tests/test_rls.py) · [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/33005869413b2b69d502008fd7e163d094c16b6c/.github/workflows/tests.yml).

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [fc10670eee6e56139e6ee77c27b70d83fbeb39e9](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/fc10670eee6e56139e6ee77c27b70d83fbeb39e9), fecha del commit 2026-10-24T08:28:15Z (UTC).

Se reconoce la corrección del bloqueo observado el 22 de octubre: el run de hoy registra 48 pruebas aprobadas contra PostgreSQL y deploy exitoso. Hay nuevos módulos de salones/horarios, autenticación/roles, migración Alembic y cliente Flutter. Las fixtures ya siembran sin IDs explícitos y evitan el desfase previo de secuencias. El job Sonar fue retirado, por lo que el verde actual no acredita análisis ni Quality Gate; tampoco prueba visualmente el cliente Flutter. El README permanece antiguo y sin URL pública.

**Próximos pasos:**
- Actualizar README con PostgreSQL, Alembic, módulos y resultado vigente; publicar URL oficial iscoutb.dev y evidencia separada de frontend y análisis estático.
- Para S12, explicitar garantías de crear/devolver préstamo y operaciones de salones, con pruebas concurrentes: las secuenciales no demuestran ausencia de carreras. Completar caché/no caché, ADR de reversión y arc42 §8.
- Proteger las pruebas destructivas: la fixture usa DATABASE_URL si falta TEST_DATABASE_URL antes de drop_all/create_all; exigir una base de pruebas identificada y rechazar cualquier destino de producción.

**Tablero:** 1 abiertas / 0 cerradas; 1 abiertas sin responsable. **README:** Sin URL concreta. README raíz solo publica localhost; su cifra de siete pruebas y SQLite en CI está desactualizada.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/2): fusionada 2026-10-06T06:08:06Z.

**CI/sondeos consultados:** [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40078165385): success; [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40066463106): failure (otra revisión/rama; no acredita la punta principal). El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/fc10670eee6e56139e6ee77c27b70d83fbeb39e9/README.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/fc10670eee6e56139e6ee77c27b70d83fbeb39e9/.github/workflows/ci.yml) · [tests/conftest.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/fc10670eee6e56139e6ee77c27b70d83fbeb39e9/tests/conftest.py) · [tests/test_loans.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/fc10670eee6e56139e6ee77c27b70d83fbeb39e9/tests/test_loans.py) · [app/services/loans.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/fc10670eee6e56139e6ee77c27b70d83fbeb39e9/app/services/loans.py) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/fc10670eee6e56139e6ee77c27b70d83fbeb39e9/docs/arc42/arc42.md) · [frontend/README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/fc10670eee6e56139e6ee77c27b70d83fbeb39e9/frontend/README.md).

<a id="uniteam"></a>

## uniTeam

Rama **master**, [facff6f0549f813e08e53461840993e91b29a07c](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/facff6f0549f813e08e53461840993e91b29a07c), fecha del commit 2026-10-23T19:43:29Z (UTC).

Las PR #6, #7 y #8 se fusionaron; hay ajustes de código/nginx y cambio a análisis automático de SonarCloud. El README ya publica dominios DuckDNS. El CI vigente pasa pruebas MySQL, compilación frontend e imágenes; conserva generación de cobertura con --cov, pero eliminó su publicación y el job Sonar con espera del Quality Gate. El README afirma que no existe CI, en contradicción con workflow y run actuales. El sondeo del 24 de octubre falla seis verificaciones, pero sigue consultando Render: ese resultado no demuestra caída de los dominios DuckDNS.

**Próximos pasos:**
- Alinear sonda, README y guía con los dominios reales; publicar el subdominio iscoutb.dev requerido sin inventarlo.
- Restablecer trazabilidad de análisis/cobertura y verificar por separado el Quality Gate; no equiparar CI verde con gate aprobado.
- Completar tabla de garantías de crear tarea/cambiar estado y límites del bus en proceso; invalidación de JWKS y clientes abiertos, ADR comparativo de reversión y arc42 §8.

**Tablero:** 0 abiertas / 1 cerradas; 0 abiertas sin responsable. **README:** Externo. README ahora publica DuckDNS, no Render ni iscoutb.dev. La sonda aún apunta a Render.

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/8): fusionada 2026-10-23T05:15:01Z; [#7](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/7): fusionada 2026-10-23T04:57:30Z; [#6](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/6): fusionada 2026-10-23T04:38:54Z; [#5](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/5): fusionada 2026-10-13T15:44:45Z; [#4](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/4): fusionada 2026-10-04T21:23:33Z; [#3](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/3): fusionada 2026-09-21T16:46:49Z; [#2](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/2): fusionada 2026-09-14T01:20:18Z.

**CI/sondeos consultados:** [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40094373315): failure; [CI](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40013691251): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/facff6f0549f813e08e53461840993e91b29a07c/README.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/facff6f0549f813e08e53461840993e91b29a07c/.github/workflows/ci.yml) · [.github/workflows/despliegue.yml](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/facff6f0549f813e08e53461840993e91b29a07c/.github/workflows/despliegue.yml) · [docs/arc42/arc42-uniteam.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/facff6f0549f813e08e53461840993e91b29a07c/docs/arc42/arc42-uniteam.md) · [app/application/bus.py](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/facff6f0549f813e08e53461840993e91b29a07c/app/application/bus.py).

<a id="verifacts"></a>

## VeriFacts

Rama **master**, [ef99fd34b8d27bc16c2201617252620482024ed6](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/ef99fd34b8d27bc16c2201617252620482024ed6), fecha del commit 2026-10-24T04:45:49Z (UTC).

El seguimiento S12 del 22 de octubre sigue respaldado por la misma tabla de garantías, política de no caché y ADR de costo de reversión. Se añadió un prototipo separado de mensajería con contrato, consumidor idempotente, reintentos y DLQ, y un ADR que decide no incorporarlo al sistema actual. El último run registra 66 pruebas aprobadas y Quality Gate PASSED. Los límites están explícitos: broker en memoria, reloj y proveedor simulados, carrera forzada sin concurrencia real, sin durabilidad ni medición real de latencia; el prototipo no modifica app ni integra el extractor real. No debe confundirse este taller con una nueva arquitectura productiva ni calificarse aquí.

**Próximos pasos:**
- Mantener separadas las garantías del producto y del prototipo; conservar límites de concurrencia, reinicios, retención y latencia al presentar evidencia.
- Actualizar README: aún conserva cifras 20/44 y pendiente de token Sonar pese el run actual aprobado; publicar dominio iscoutb.dev con certificado válido.
- Acotar afirmaciones de linearizabilidad al modelo demostrado; mantener pendientes las mitigaciones SSRF/historial y la alineación C4 con nginx, sin dar por corregido código por la sola existencia del ADR.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin responsable. **README:** Externo. HTTP sslip externo; falta dominio institucional con certificado válido.

**CI/sondeos consultados:** [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40063628495): success; [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40063628470): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/ef99fd34b8d27bc16c2201617252620482024ed6/README.md) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/ef99fd34b8d27bc16c2201617252620482024ed6/docs/arc42/08-conceptos-transversales.md) · [docs/adr/0012-modelo-almacenamiento-sqlite-costo-reversion.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/ef99fd34b8d27bc16c2201617252620482024ed6/docs/adr/0012-modelo-almacenamiento-sqlite-costo-reversion.md) · [docs/adr/0013-no-incorporar-mensajeria-asincrona.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/ef99fd34b8d27bc16c2201617252620482024ed6/docs/adr/0013-no-incorporar-mensajeria-asincrona.md) · [docs/mensajeria/limites-del-experimento.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/ef99fd34b8d27bc16c2201617252620482024ed6/docs/mensajeria/limites-del-experimento.md) · [docs/mensajeria/evidencia-ejecucion.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/ef99fd34b8d27bc16c2201617252620482024ed6/docs/mensajeria/evidencia-ejecucion.md) · [tests/test_messaging.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/ef99fd34b8d27bc16c2201617252620482024ed6/tests/test_messaging.py).

<a id="xald"></a>

## XALD

Rama **master**, [405a39e0feff40a8414841b6936d5a2dc4488ba4](https://github.com/ISCOUTB/AS_202620_XALD/commit/405a39e0feff40a8414841b6936d5a2dc4488ba4), fecha del commit 2026-10-19T03:00:24Z (UTC).

No hay cambios en la rama principal desde el seguimiento del 22 de octubre; el último CI consultado continúa exitoso y corresponde a esa misma punta. Se mantiene la documentación de idempotencia/sincronización, sin que seis issues cerradas acrediten todos los pendientes S12: cinco cierres son completed y uno duplicate.

**Próximos pasos:**
- Convertir la tabla de idempotencia en operación→garantía y contrastar guardar local/registrar remoto, acotando memoria, durabilidad y convergencia.
- Justificar no caché o definir invalidación; comparar costo de reversión de datos y distinguir memoria actual de Room futuro en C4 y arc42 §8.
- Publicar URL exacta bajo iscoutb.dev y registrar tareas S12 verificables, sin inferir avance por el número de cierres.

**Tablero:** 0 abiertas / 6 cerradas; 0 abiertas sin responsable. **README:** Externo. Backend Render, fuera del dominio institucional.

**PR consultadas:** [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z; [#24](https://github.com/ISCOUTB/AS_202620_XALD/pull/24): fusionada 2026-09-27T16:24:00Z; [#23](https://github.com/ISCOUTB/AS_202620_XALD/pull/23): fusionada 2026-09-20T17:34:35Z; [#22](https://github.com/ISCOUTB/AS_202620_XALD/pull/22): cerrada sin fusión registrada; [#21](https://github.com/ISCOUTB/AS_202620_XALD/pull/21): cerrada sin fusión registrada; [#20](https://github.com/ISCOUTB/AS_202620_XALD/pull/20): fusionada 2026-09-20T16:21:31Z; [#19](https://github.com/ISCOUTB/AS_202620_XALD/pull/19): fusionada 2026-09-16T04:45:22Z; [#18](https://github.com/ISCOUTB/AS_202620_XALD/pull/18): fusionada 2026-09-14T03:06:22Z; [#15](https://github.com/ISCOUTB/AS_202620_XALD/pull/15): fusionada 2026-09-13T16:09:58Z.

**CI/sondeos consultados:** [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/39192603030): success. El alcance y las limitaciones se describen arriba.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/README.md) · [docs/arc42/08-Cross-cutting Concepts.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/arc42/08-Cross-cutting%20Concepts.md) · [docs/c4/c2.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/c4/c2.md) · [backend/app/main.py](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/backend/app/main.py).
