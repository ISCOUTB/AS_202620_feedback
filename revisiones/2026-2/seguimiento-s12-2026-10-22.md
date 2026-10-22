# Seguimiento actual de S12 · 22 de octubre de 2026

Consulta del 22 de octubre de 2026, aproximadamente 09:38–09:43 COT (UTC−5), sobre las ramas principales de los 23 repositorios. Es una instantánea de seguimiento, no una nueva calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia (límite exclusivo: 26/oct 05:00 UTC). Se conservan matrices, planillas y notas anteriores.

## Cómo leer este seguimiento

Se revisaron commits de la rama principal, PR relevantes, issues abiertas/cerradas, README completo, archivos de arquitectura/código y resultados CI publicados. Las PR abiertas se describen aparte: no se atribuyen a master/main. **No se ejecutó código estudiantil**. La inspección estática y un job verde tienen alcances distintos; las pruebas omitidas o que apuntan a otro directorio no acreditan la funcionalidad nueva. No se calculan notas ni se reemplazan matrices históricas.

Las recomendaciones siguientes actualizan los pendientes de trabajo, no reescriben los cierres de S11 ni el snapshot S12 del 19/oct. Los avances de Drift, Recobra y VeriFacts ya incluyen artefactos S12 que antes faltaban; no deben seguir tratándose como ausentes.

## Referencia de criterios S12

Según la [ficha vigente](../../fichas/semana-12-evidencia-s12.md): tabla operación→garantía y contraste de dos operaciones reales; diseño de caché o exclusión argumentada e invalidación tras escritura; garantías de eventos si existen; ADR de la decisión de datos más costosa de revertir con costo comparativo; almacenes/brokers reales en C4 nivel 2 y consistencia/caché en arc42 §8. No se exige crear caché ni broker sin necesidad, ni se evalúa aquí el taller de mensajes. Una transacción o prueba secuencial no demuestra por sí sola todas las garantías concurrentes.

## Resumen del corte

- [Issues](seguimiento-issues-2026-10-22.md): **45 abiertas, 127 cerradas**; 126 completed y una duplicate; 21 abiertas sin asignar. Totales sin cambio frente al 20/oct.
- [README y dominio](seguimiento-despliegues-2026-10-22.md): **9 institucionales (incluye API), 7 externos, 7 sin URL concreta**.
- Drift, Recobra y VeriFacts muestran avances sustanciales en documentación/decisiones S12. EnAgenda incorpora usuarios PostgreSQL y registro/login; LostVault agrega API en RAM; Tienda fusiona frontend/proxy.
- Tienda pasa pruebas frontend/backend pero el scanner falla por HTTP403 al consultar metadatos JRE. Tracker y EnAgenda tienen pruebas fallidas; distinguir estos bloqueos.
- Presentaciones docentes preservadas: TAIA y ElMapita funcionando; PideUtb con despliegues; ROUTB y Recobra presentaron.

<a id="audioshare"></a>

## AudioShare

Rama **master**, punta consultada [1af6e5ca727e60ef64cda6e31af71ab73bc9c9da](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da), fecha del commit 2026-10-19T06:41:04Z (UTC).

Sin commits nuevos desde 20 de octubre. Audio de pista y pausa/reanudación ya constaban en punta 19 de octubre. README reconoce que la imagen sirve cliente legado, no Flutter Web.

**Próximos pasos:**
- Tabla crear sala/PLAY/pausa → garantía, separando transacción SQLite y publicación NDJSON; declarar comportamiento si falla entre ambos.
- Definir invalidación o URL versionada de /track (max-age=3600), y actualizar arc42 §8 que aún describe MockAudioService.
- ADR de decisión de datos más costosa de revertir con comparación y garantías de entrega/reconexión de eventos.

**Tablero:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar. **README:** Institucional. URL institucional del cliente legado; no acredita despliegue de Flutter web.

**CI/sondeos consultados:** [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299344): success; [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299270): success; [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299234): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/README.md) · [docs/arc42/src/08_concepts.adoc](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/arc42/src/08_concepts.adoc) · [src/app.ts](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/app.ts) · [docs/idempotencia-y-saga.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/idempotencia-y-saga.md).

<a id="sistema-de-calificacion-automatica"></a>

## QuantIA

Rama **master**, punta consultada [98a9dcc8f22c77ac5d0dfcea4055865e7727a21e](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e), fecha del commit 2026-10-19T03:40:44Z (UTC).

Sin commits nuevos desde 20 de octubre; CI success. README sigue con Render y riesgos reconocidos de almacén efímero.

**Próximos pasos:**
- Tabla recepción/encolado/consumo → garantía, distinguir bitácora, BLPOP sin ack y deduplicación TTL de persistencia durable.
- Decidir caché o no caché con motivo e invalidación tras cambios de examen/carga, no confundir marca de deduplicación con caché de lectura.
- ADR comparativo de decisión de datos/reversión, cerrar R-06 y reflejar consistencia/caché en arc42 §8.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. **README:** Externo. Frontend y API en Render, fuera del dominio requerido.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/39195829181): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/README.md) · [docs/arc42/arc42-template-ES.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/arc42/arc42-template-ES.md) · [docs/evidencia/modos-de-fallo.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/evidencia/modos-de-fallo.md).

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, punta consultada [a237dd2f22b02bb547f87a07d15b6d31ea0dc758](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/a237dd2f22b02bb547f87a07d15b6d31ea0dc758), fecha del commit 2026-10-19T04:51:37Z (UTC).

Sin commits nuevos; PR #60 abierta documental. CI backend y otros success, run de flujo real falla Android pero web-desktop/web-mobile success.

**Próximos pasos:**
- Tabla crear/cambiar estado/ocultar publicación → garantía, distinguiendo transacciones MySQL de compensación SQL/archivos.
- Decidir caché o no caché de catálogo y actualización tras crear/cambiar visibilidad; incorporarlo a arc42 §8.
- ADR de costo comparativo de reversión de datos; reproducir/corregir flujo Android y resolver PR #60 sin llamar todo CI verde.

**Tablero:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. **README:** Institucional. API institucional; frontend en GitHub Pages. Cumplimiento parcial del sitio.

**PR relevantes:** [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60) abierta, no integrada.

**CI/sondeos consultados:** [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586404): success; [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586378): success; [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586366): failure. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/README.md) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/arc42/08-conceptos-transversales.md) · [backend/app/publicaciones/repository.py](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/backend/app/publicaciones/repository.py).

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, punta consultada [b82c8e511133a868e8b1c321fb7be3b70d6afed5](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/b82c8e511133a868e8b1c321fb7be3b70d6afed5), fecha del commit 2026-10-20T14:09:32Z (UTC).

Punta 20 de octubre actualiza registro IA solamente; publicaciones siguen InMemoryPublicacionAdapter en router. README no URL pública. Dos últimos runs failure; jobs de uno vacíos, causa no verificada.

**Próximos pasos:**
- Contrastar crear/listar publicaciones y declarar garantía real en memoria, no atribuir transacción PostgreSQL al adaptador conectado.
- Definir caché/no caché y política tras escritura; sincronizar C4 con almacén real y estado planeado de PostgreSQL/Dokploy.
- ADR comparativo de decisión de datos/reversión; actualizar arc42 §8 y documentar URL iscoutb.dev.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. **README:** Sin URL concreta. Sin URL pública concreta en el README raíz.

**PR relevantes:** [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1) abierta, no integrada.

**CI/sondeos consultados:** [.github/workflows/contrato.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39436726678): failure; [.github/workflows/backend-tests.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39436724661): failure. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/b82c8e511133a868e8b1c321fb7be3b70d6afed5/README.md) · [docs/arc42/08_conceptos_transversales.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/b82c8e511133a868e8b1c321fb7be3b70d6afed5/docs/arc42/08_conceptos_transversales.md) · [backend/src/linkclub/adapters/inbound/api/publicacion_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/b82c8e511133a868e8b1c321fb7be3b70d6afed5/backend/src/linkclub/adapters/inbound/api/publicacion_router.py).

<a id="dinamikutb"></a>

## Dinamik

Rama **master**, punta consultada [37872ff7dbb08be833b92c0a4b6d1ca3152464a1](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/37872ff7dbb08be833b92c0a4b6d1ca3152464a1), fecha del commit 2026-10-19T04:58:04Z (UTC).

Master no cambió; PR #35 abierta en su rama de trabajo incorpora PostgreSQL 16 Compose, no MySQL 8.4 pese título. No equivale a despliegue fusionado. README declara expiración el 27 de octubre y plan recrear/resembrar el 25 de octubre, no verificado con proveedor.

**Próximos pasos:**
- Completar tabla GET/PUT de requisitos → garantía, probar concurrencia y evitar inferir serializabilidad del commit.
- Justificar no caché o definir invalidación tras PUT, y reflejarlo en arc42 §8.
- Comparar costo de revertir motor/esquema/persistencia en ADR; revisar PR #35 título/diff, respaldo y restauración antes del plazo declarado y publicar dominio institucional real.

**Tablero:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. **README:** Externo. Frontend en GitHub Pages y API en Render. Expiración del 27/oct y plan del 25/oct declarados por el equipo, no verificados con el proveedor.

**PR relevantes:** [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35) abierta, no integrada.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/README.md) · [docs/arc42/08-cross-cutting-concepts.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/08-cross-cutting-concepts.md) · [backend/app/requisitos/service.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/backend/app/requisitos/service.py).

<a id="drift"></a>

## Drift

Rama **master**, punta consultada [aa1578a1e81709418b502154999c2420352dd86e](https://github.com/ISCOUTB/AS_202620_Drift/commit/aa1578a1e81709418b502154999c2420352dd86e), fecha del commit 2026-10-21T04:53:31Z (UTC).

PR #31 merge 21 de octubre aporta arc42 §8.13 seis operaciones/garantías, §8.14 actualización/invalidación por fuente y ADR 0010 de costo comparativo (Propuesto). Código rechaza sync vacío conservando catálogo, usa lock para replace/lectura y TTL single-flight. CI success. Evidencia de latencia está explícitamente simulada y usó shim en vez de httpx.

**Próximos pasos:**
- Revisar/aceptar ADR 0010 con equipo; su conclusión es identidad/contrato público del juego, no persistencia, como decisión actual más costosa.
- Repetir experimento con dependencias reales y enlazar run/resultado, manteniendo separación de simulación, red real y latencia HTTP extremo a extremo.
- Probar y decidir límites de edad/aviso para tasa stale, catálogo por instancia/reinicio y respuesta vacía sin aviso si falta fallback; conservar pruebas de sync atómico y TTL.

**Tablero:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. **README:** Institucional. URL institucional para frontend/backend; no se repitió prueba funcional del sitio.

**PR relevantes:** [#31](https://github.com/ISCOUTB/AS_202620_Drift/pull/31) fusionada 2026-10-21T04:53:32Z.

**CI/sondeos consultados:** [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39546508693): success; [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39546508600): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/README.md) · [docs/arc42/arc42_8_conceptos_transversales.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/docs/arc42/arc42_8_conceptos_transversales.md) · [docs/adr/0010-costo-de-reversion-de-las-decisiones-de-datos.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/docs/adr/0010-costo-de-reversion-de-las-decisiones-de-datos.md) · [docs/evidencias/s12-steam-degradado.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/docs/evidencias/s12-steam-degradado.md) · [backend/app/application/usecases/sync_playstation_catalog.py](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/backend/app/application/usecases/sync_playstation_catalog.py) · [backend/app/infrastructure/persistence/in_memory_playstation_catalog.py](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/backend/app/infrastructure/persistence/in_memory_playstation_catalog.py) · [backend/app/infrastructure/external/single_flight_cache.py](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/backend/app/infrastructure/external/single_flight_cache.py).

<a id="elmapita"></a>

## ElMapita

Rama **main**, punta consultada [0421885424d13478cf33c717fdd933a4748d9025](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/0421885424d13478cf33c717fdd933a4748d9025), fecha del commit 2026-10-19T08:33:59Z (UTC).

Sin commits desde 20 de octubre; CI success. Presentación y funcionamiento confirmados por docente; README solo localhost/Supabase placeholder, brecha documental no ausencia de despliegue.

**Próximos pasos:**
- Publicar URL exacta iscoutb.dev del despliegue mostrado, sin inventar host.
- Tabla operaciones reales (cargar edificio/registro o rol) → garantía y dos recorridos de código; definir invalidación/versionado al reemplazar modelo, no solo TTL.
- ADR comparativo del costo de revertir datos y llevar consistencia/caché a arc42 §8, hoy solo errores/privacidad/internacionalización.

**Tablero:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. **README:** Sin URL concreta. Solo localhost y un placeholder de Supabase. El docente confirmó presentación y funcionamiento; falta reflejar la URL.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/39223716465): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/README.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/docs/arc42/arc42-template-EN.md).

<a id="enagenda"></a>

## EnAgenda

Rama **master**, punta consultada [6e546a956d3235ce820c9909edbf13f9415f1d93](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/6e546a956d3235ce820c9909edbf13f9415f1d93), fecha del commit 2026-10-21T13:36:21Z (UTC).

Dos commits 21 de octubre añaden PostgreSQL/SQLAlchemy/Alembic para usuarios y rutas/templates de registro/login/panel/logout con CSRF. Registrar_usuario hace commit/rollback y unicidad correo. Invitaciones siguen memoria; README y arc42 no reflejan nuevo módulo. Último CI falla Ejecutar pruebas, contrato/build skipped; Pages success no sustituye tests.

**Próximos pasos:**
- Corregir CI y agregar pruebas registro/login/migración; diferenciar persistencia PostgreSQL de Usuarios y memoria de Invitaciones.
- Tabla registrar usuario/crear y responder invitaciones → garantías, incluida atomicidad de lote y concurrencia; contrastar dos operaciones.
- Decidir caché/no caché, ADR comparativo persistencia/identidad, actualizar C4/arc42 §8 y README con URL pública iscoutb.dev real.

**Tablero:** 1 abiertas / 0 cerradas; 0 abiertas sin asignar. **README:** Sin URL concreta. README declara contenedor desplegado, pero no publica dirección concreta.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/39609478651): failure; [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/39609478211): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/README.md) · [src/usuarios/aplicacion/registrar_usuario.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/src/usuarios/aplicacion/registrar_usuario.py) · [app/web.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/app/web.py) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/docs/arc42/08-conceptos-transversales.md) · [src/invitaciones/infraestructura/repositorio_memoria.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/src/invitaciones/infraestructura/repositorio_memoria.py).

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, punta consultada [1a706525f6a660c216bc11655c754f65bbbe8bfe](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/1a706525f6a660c216bc11655c754f65bbbe8bfe), fecha del commit 2026-10-20T18:38:58Z (UTC).

El 20 de octubre se documentaron endpoints y ejemplos de uso; el CI de la punta consultada terminó correctamente. El README todavía niega integración funcional aunque ya existen llamadas HTTP desde Flutter: corregir esa contradicción documental.

**Próximos pasos:**
- Tabla de garantías de consulta/entrada/salida y contraste con transacción PostgreSQL.
- Decidir caché e invalidación del contador o justificar no caché; ADR decisión de datos más costosa y arc42 §8.
- Actualizar README/C4 con integración Flutter; llevar test:postgres a CI. Los 16 tickets abiertos no equivalen a 16 tareas no implementadas: conciliar evidencia y backlog.

**Tablero:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. **README:** Institucional. Backend, no URL web de Flutter demostrada. README sigue negando integración funcional aunque el commit 2227faf incorpora llamadas HTTP de Flutter.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/39476599936): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/README.md) · [docs/arc42/arc42_gimnasio_utb.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/docs/arc42/arc42_gimnasio_utb.md) · [docs/Flutter/lib/core/api/aforo_api.dart](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/docs/Flutter/lib/core/api/aforo_api.dart) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/.github/workflows/ci.yml).

<a id="inventrack"></a>

## InvenTrack

Rama **main**, punta consultada [28506a8eabcde2234e56698d13ae1d8ae8d0ee24](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/28506a8eabcde2234e56698d13ae1d8ae8d0ee24), fecha del commit 2026-10-19T03:29:12Z (UTC).

La punta no cambia desde el 19 de octubre y Run Tests termina correctamente. La API utiliza RAM como almacén primario, no como caché; el despliegue de la interfaz Flutter continúa pendiente en la documentación.

**Próximos pasos:**
- Tabla entrada/salida/consulta → garantía real; lock local no da durabilidad ni coordinación entre réplicas.
- Justificar no caché o declarar invalidación por stock/producto; ADR costo de reversión.
- Corregir C4: RAM pertenece al proceso API, SQL futuro no desplegado; actualizar backlog S12 aunquesiete issues cerradas.

**Tablero:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. **README:** Institucional. API únicamente, Flutter pendiente; RAM almacén primario, no caché.

**CI/sondeos consultados:** [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/39194936605): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/README.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/arc42/arc42-template-EN.md) · [app/inventario/application/registrar_movimiento.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/app/inventario/application/registrar_movimiento.py) · [docs/c4/containers.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/c4/containers.md).

<a id="laplacita"></a>

## LaPlacita

Rama **master**, punta consultada [0c9ce082b5850baf1ecda75e82d20757d0101234](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/0c9ce082b5850baf1ecda75e82d20757d0101234), fecha del commit 2026-10-19T02:56:00Z (UTC).

La punta no cambia desde el 19 de octubre. Ya existe portal de tienda y catálogo PostgreSQL; el README desactualizado no demuestra ausencia de funcionalidad. El workflow de despliegue Dokploy figura exitoso, pero falta publicar su URL vigente.

**Próximos pasos:**
- Publicar URL real iscoutb.dev en README; actualizar instrucciones Azure y limitación antigua 'persistencia pendiente'.
- Tabla garantías crear/cambiar pedido distinguiendo RAM y escritura asíncrona PostgreSQL; verificardos operaciones.
- Caché/invalidación o exclusión justificada; ADR decisión de datos más costosa y arc42 §8; Redis/outbox siguen futuros.

**Tablero:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. **README:** Sin URL concreta. README declara Azure retirado13-oct y Dokploy actual, dice URL arriba sin darla. No afirmar ausencia de despliegue: CI Deploy Dokploy success.

**CI/sondeos consultados:** [Deploy Dokploy (laboratorio de la U)](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39192292623): success; [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39192292599): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/README.md) · [backend/src/modules/pedidos/index.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/backend/src/modules/pedidos/index.js) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/arc42/arc42-template-EN.md).

<a id="lostvault"></a>

## LostVault

Rama **main**, punta consultada [e19be366f7e922a8a9c9abd4a808899f14b2999b](https://github.com/ISCOUTB/AS_202620_LostVault/commit/e19be366f7e922a8a9c9abd4a808899f14b2999b), fecha del commit 2026-10-20T16:16:33Z (UTC).

La PR #19 se fusionó el 20 de octubre: agrega una API FastAPI con JWT, salud, Dockerfile, Idempotency-Key de 24 horas y lock. api/app/store.py conserva datos en diccionarios RAM: no aporta durabilidad al reinicio ni coordinación multirréplica. Los tres workflows aparecen verdes, pero Backend checks ejecuta backend/test_api.py y no la nueva suite api/tests.

**Próximos pasos:**
- Integrar api/tests en CI y aclarar relación api/ frente backend/ y cliente Flutter.
- Publicar URL real iscoutb.dev en raíz, no local ni inventada.
- Tabla garantías con límites de proceso/reinicio; caché o no caché razonado; ADR almacenamiento más costoso, C4 y arc42 §8 coherentes.

**Tablero:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. **README:** Sin URL concreta. README raíz sin URL pública. Nueva api/ no implica despliegue.

**PR relevantes:** [#19](https://github.com/ISCOUTB/AS_202620_LostVault/pull/19) fusionada 2026-10-20T16:16:34Z.

**CI/sondeos consultados:** [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39455997158): success; [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39455997151): success; [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39455997101): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/README.md) · [api/app/store.py](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/api/app/store.py) · [api/app/service.py](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/api/app/service.py) · [api/README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/api/README.md) · [.github/workflows/backend.yml](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/.github/workflows/backend.yml).

<a id="mapsutb"></a>

## MapsUTB

Rama **master**, punta consultada [4b8fa088faec96772e76c8c4f2782919ec87a9b9](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/4b8fa088faec96772e76c8c4f2782919ec87a9b9), fecha del commit 2026-10-16T17:38:48Z (UTC).

No hay commits nuevos desde el 16 de octubre. La sonda programada del 22 de octubre a las 14:32 UTC terminó correctamente; su alcance no equivale a una prueba funcional integral. Las issues Sonar #55 y #56 permanecen abiertas y sin asignar. MapsUTB es un proyecto distinto de ElMapita.

**Próximos pasos:**
- Publicar dirección institucional real iscoutb.dev manteniendo Firebase como alternativa si aplica.
- Asignar/refactorizar complejidad y ternario de indice_busqueda.dart;52 cierres son Sonar, no52 funcionalidades.
- Tabla operación→garantía; incluir caché interna grafo además HTTP y su invalidación; ADR reversión datos; arc42 §8.

**Tablero:** 2 abiertas / 52 cerradas; 2 abiertas sin asignar. **README:** Externo. Firebase, no subdominio iscoutb.dev. MapsUTB NO es ElMapita.

**CI/sondeos consultados:** [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39796473716): success; [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39787858353): success; [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39780556003): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/README.md) · [lib/features/busqueda/indice_busqueda.dart](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/lib/features/busqueda/indice_busqueda.dart) · [docs/arc42/08_concepts.adoc](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/arc42/08_concepts.adoc).

<a id="pideutb"></a>

## PideUtb

Rama **master**, punta consultada [913847779bdf2ec398ce0aca35a822b6f8217cfc](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/913847779bdf2ec398ce0aca35a822b6f8217cfc), fecha del commit 2026-10-20T14:55:37Z (UTC).

La PR #28, fusionada el 20 de octubre, corrige el cálculo del ADR 0009: distingue una estimación de 704 MB, límites de 416 MB y una cuota de 512 MB. La PR #29 de interfaz institucional sigue abierta: su CI verde no convierte esos cambios en contenido integrado de master.

El docente confirmó actualización presentada y despliegues.

**Próximos pasos:**
- Contrastar avance de estado con UPDATE condicionado al estado esperado y prueba de carrera; tabla actual sobrestima atomicidad.
- ADR decisión de datos más costosa de revertir, no confundir con no extraer pagos; alinear sondeo5 s frente8 s y pasarela C4.
- Revisar/integrar PR #29 según equipo; desglosar issue1 genérica en tareas con responsable y criterio.

**Tablero:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. **README:** Institucional. Docente confirmó actualización presentada y despliegues.

**PR relevantes:** [#29](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/29) abierta, no integrada; [#28](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/28) fusionada 2026-10-20T14:55:39Z.

**CI/sondeos consultados:** [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39443709932): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/913847779bdf2ec398ce0aca35a822b6f8217cfc/README.md) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/913847779bdf2ec398ce0aca35a822b6f8217cfc/docs/arc42/arc42.md).

<a id="recobra"></a>

## Recobra

Rama **master**, punta consultada [aacc1ec4094573e15758a245e6c6954a5b76fd48](https://github.com/ISCOUTB/AS_202620_Recobra/commit/aacc1ec4094573e15758a245e6c6954a5b76fd48), fecha del commit 2026-10-21T23:19:18Z (UTC).

Avance sustancial del 21 de octubre: ADR0025 documenta caché HTTP/ETag e invalidación; ADR0026 define cuatro eventos, tres reintentos, cola de fallidos y reproceso cada cinco minutos; ADR0027 compara seis decisiones y estima reversión en 6–9 días-persona. arc42 §8 contiene la tabla de garantías y C4 corrige coincidencias en memoria. El CI incluye backend, Flutter, adaptadores contra PostgreSQL real, scanner y Quality Gate exitosos. Se contrastaron middleware, pruebas de caché, entrega de eventos y persistencia de la cola.

El docente confirmó presentación.

**Próximos pasos:**
- Extender suite PostgreSQL de 7/9 adaptadores a Reclamaciones/Sesiones y e2e completos; hoy estos últimos RAM.
- Conservar límites: EventEmitter no durable; publicacion.creada fuera del nuevo contrato sin recálculo de coincidencias; fallo al guardar cola depende conciliación de 3 días y cola de 7 días.
- Corregir afirmación 'despliegue invalida lugares': navegador con max-age=3600 puede conservar durante 1 hora; TTL de 60 s miniaturas tras borrado aceptado explícitamente, no invalidación inmediata.
- Añadir evidencia de backup/restauración y alerta cola; son próximos pasos, no negar que ahora existen caché, ADR y arc42 §8.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. **README:** Institucional. Docente confirmó presentación, no una certificación de funcionamiento por auditoría.

**CI/sondeos consultados:** [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39692648288): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/README.md) · [docs/adr/0025-diseno-de-cache-y-politica-de-invalidacion.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/docs/adr/0025-diseno-de-cache-y-politica-de-invalidacion.md) · [docs/adr/0026-entrega-de-avisos-con-eventos-reintentos-y-cola-de-fallidos.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/docs/adr/0026-entrega-de-avisos-con-eventos-reintentos-y-cola-de-fallidos.md) · [docs/adr/0027-la-decision-de-datos-mas-costosa-de-revertir.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/docs/adr/0027-la-decision-de-datos-mas-costosa-de-revertir.md) · [src/observabilidad/politica-de-cache.middleware.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/src/observabilidad/politica-de-cache.middleware.ts) · [test/cache.e2e-spec.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/test/cache.e2e-spec.ts) · [docs/c4/C4-C2.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/docs/c4/C4-C2.md) · [src/application/use-cases/entrega-de-eventos.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/src/application/use-cases/entrega-de-eventos.ts).

<a id="routb"></a>

## ROUTB

Rama **master**, punta consultada [1bd9425e2675bd7531426b6e31e78546b3e55f2e](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/1bd9425e2675bd7531426b6e31e78546b3e55f2e), fecha del commit 2026-10-18T21:39:27Z (UTC).

Master no cambia desde el 18 de octubre y no hay PR abiertas. Existe un CI exitoso del 22 de octubre en otra rama: no se atribuye a master. La purga programada del 22 de octubre terminó correctamente, lo que tampoco constituye una nueva validación integral del producto.

El docente confirmó que entregó avance.

**Próximos pasos:**
- Tabla operación→garantía para creación/aceptación/rechazo, no solo ACID genérico.
- Invalidación de geocodificación ante fuente/parámetros; TTL de 7 días no basta como política tras cambios relevantes; no confundir con cupos.
- ADR mayor reversión de datos/costo y arc42 §8; actualizar guía desplegar Dokploy frente Render. Conciliar trabajo de ramas antes atribuir integración.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. **README:** Institucional. Backend; README mantiene pasos antiguos de Render. Docente confirmó presentación.

**CI/sondeos consultados:** [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39746384267): success; [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39567852703): success; [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39392058843): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/README.md) · [docs/arc42/08_conceptos_transversales.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/arc42/08_conceptos_transversales.md) · [backend/app/shared/geocode/service.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/backend/app/shared/geocode/service.py).

<a id="shareu"></a>

## ShareU

Rama **master**, punta consultada [39508608eae4c1a56a5e4fc11a055bf6afb2c003](https://github.com/ISCOUTB/AS_202620_ShareU/commit/39508608eae4c1a56a5e4fc11a055bf6afb2c003), fecha del commit 2026-09-29T00:56:57Z (UTC).

Se mantiene el corte vertical de búsqueda con SQLite, pero la rama principal no registra cambios desde el 28 de septiembre (Colombia). El README aún contiene marcadores URL Vercel/URL Render, no enlaces desplegados concretos. Las PR #22 y #23 siguen abiertas; no se deben presentar como incorporadas. El último workflow tests.yml sigue fallido. Para S12, elaborar la tabla operación→garantía y contrastar dos operaciones reales; justificar no usar caché o definir invalidación tras modificar documentos/metadatos, y comparar el costo de reversión de las decisiones de datos. Consolidar estas decisiones en arc42 §8 y distinguir correo/outbox previsto de mensajería implementada. Revisar los solapamientos de issues #12/#18 y asignar las cinco abiertas sin responsable.

**Tablero:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. **README:** Sin URL concreta. Los campos URL Vercel/URL Render siguen sin completar.

**PR relevantes:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23) abierta, no integrada; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22) abierta, no integrada.

**CI/sondeos consultados:** [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458): failure; [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36480560316): failure; [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479877131): failure. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md) · [docs/c4/nivel2.mmd](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/c4/nivel2.mmd).

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, punta consultada [6565118773cadbffd41c213358facc5735c9783c](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/6565118773cadbffd41c213358facc5735c9783c), fecha del commit 2026-10-20T14:41:39Z (UTC).

Se reconoce la presentación y el despliegue funcionando confirmados por el docente. El README ya publica la API en https://taia-sistema.iscoutb.dev y sus rutas de salud/documentación; es evidencia del backend, no de una aplicación Flutter ya entregada. CI y CD del último commit terminaron correctamente. No se mantienen como vigentes las comprobaciones fallidas sobre el antiguo dominio sslip. Para S12, completar la tabla operación→garantía, acotar las transacciones de confirmación y notificación frente a crear tareas/enviar Telegram, justificar no usar caché o definir invalidación, y seleccionar comparativamente la decisión de datos más costosa de revertir. Anotar PostgreSQL en C4 nivel2 y consolidar consistencia/caché en arc42 §8. Actualizar las tres issues abiertas antiguas y asignar las dos sin responsable; su antigüedad no niega el avance demostrado.

**Tablero:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. **README:** Institucional. Ahora publica API institucional, salud y documentación; no acredita entrega de una interfaz Flutter. Despliegue funcionando confirmado por docente.

**CI/sondeos consultados:** [CD](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39441872010): success; [CI](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39441578508): success; [CD](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39309238475): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/6565118773cadbffd41c213358facc5735c9783c/README.md) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/6565118773cadbffd41c213358facc5735c9783c/docs/arc42/08-conceptos-transversales.md) · [docs/c4/C4-C2.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/6565118773cadbffd41c213358facc5735c9783c/docs/c4/C4-C2.md) · [docs/modos_fallo_s11.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/6565118773cadbffd41c213358facc5735c9783c/docs/modos_fallo_s11.md).

<a id="tienda-virtual-utb"></a>

## Tienda Virtual

Rama **main**, punta consultada [d66926b932b47490fede78be66091e7823dffacf](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/d66926b932b47490fede78be66091e7823dffacf), fecha del commit 2026-10-21T17:43:36Z (UTC).

Hay avance nuevo: PR #1 fusionada el 21 de octubre, rediseño del frontend, proxy interno same-origin y corrección de la URL pública usada al compilar. El README ya publica una URL sslip concreta, pero aún falta el subdominio iscoutb.dev exigido. En el último run pasan frontend y backend, incluidos contrato y pruebas; falla únicamente el scanner Sonar al consultar metadatos JRE con HTTP403. No atribuir este run a un Quality Gate Reliability B: no llega a acreditar ese análisis. Revisar la configuración/permisos del scanner sin publicar credenciales. Para S12, añadir garantías por operación y contrastar dos rutas actuales, preservar la decisión de no cachear en el proxy y explicar refresco tras escritura; comparar decisiones de datos por costo de reversión y reunirlo en arc42 §8. Sin issues registradas no significa sin trabajo: convertir pendientes de despliegue, scanner y S12 en tareas verificables.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. **README:** Externo. Ahora publica URL sslip concreta; falta dominio institucional.

**PR relevantes:** [#1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/1) fusionada 2026-10-21T16:14:34Z.

**CI/sondeos consultados:** [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/39646371465): failure; [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/39633659220): failure; [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/39633008821): failure. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/d66926b932b47490fede78be66091e7823dffacf/README.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/d66926b932b47490fede78be66091e7823dffacf/docs/arc42/arc42-template-EN.md) · [docs/adr/0012-proxy-interno-api.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/d66926b932b47490fede78be66091e7823dffacf/docs/adr/0012-proxy-interno-api.md) · [docs/c4/container.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/d66926b932b47490fede78be66091e7823dffacf/docs/c4/container.md).

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, punta consultada [7ee2d75a385eb2fb312dae9b938d3fd126895635](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/7ee2d75a385eb2fb312dae9b938d3fd126895635), fecha del commit 2026-10-20T15:19:57Z (UTC).

Los hotfix del 20 de octubre son posteriores al corte previo, pero el último CI sigue fallido: 17 pruebas pasan y 5 de autenticación fallan. El log registra colisión usuarios_pkey al registrar usuarios, seguida de errores de login y de lectura de id; revisar el aislamiento/siembra y secuencia de claves de PostgreSQL antes de concluir que el problema es solo Sonar. Scanner y despliegue quedaron omitidos por ese fallo. El README todavía afirma siete pruebas en verde y solo publica localhost: actualizarlo con el estado actual y la URL real bajo iscoutb.dev. Para S12, declarar garantías al crear recursos/prestar equipos, contrastarlas con transacciones/bloqueo y evidencia concurrente, justificar caché/no caché e invalidación, y comparar el costo de revertir la decisión de datos. Dividir la única issue genérica, vacía y sin asignar en tareas con aceptación y responsables.

**Tablero:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. **README:** Sin URL concreta. Solo localhost; falta URL pública concreta.

**CI/sondeos consultados:** [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/39447469154): failure; [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/39446524341): failure; [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/39445552038): failure. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/7ee2d75a385eb2fb312dae9b938d3fd126895635/README.md) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/7ee2d75a385eb2fb312dae9b938d3fd126895635/docs/arc42/arc42.md) · [app/services/loans.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/7ee2d75a385eb2fb312dae9b938d3fd126895635/app/services/loans.py) · [app/services/resources.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/7ee2d75a385eb2fb312dae9b938d3fd126895635/app/services/resources.py).

<a id="uniteam"></a>

## uniTeam

Rama **master**, punta consultada [2c73ffce2d9b92e71697a7313f829789b4471639](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/2c73ffce2d9b92e71697a7313f829789b4471639), fecha del commit 2026-10-13T15:44:44Z (UTC).

La rama principal sigue en el despliegue Dokploy integrado el 13 de octubre, pero el README conserva URLs Render y no publica un subdominio iscoutb.dev. La comprobación programada del 22 de octubre a las 07:38 Colombia falla en sus seis verificaciones de esos endpoints; es evidencia de ese sondeo, no una certificación de indisponibilidad permanente ni del estado de un dominio Dokploy no documentado. Para S12, completar la tabla de garantías para crear tarea y cambiar estado, aclarando el límite del bus en proceso ante fallos de consumidores; completar invalidación de JWKS y del flujo de estados en clientes abiertos, comparar costos de reversión de datos y terminar arc42 §8. La única issue cerrada es de prueba (hola mundo); registrar pendientes reales y enlazar evidencia.

**Tablero:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. **README:** Externo. README conserva Render aunque hay configuración Dokploy; no inventar el dominio actual.

**CI/sondeos consultados:** [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/39779970282): failure; [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/39735536558): failure; [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/39702641780): failure. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/README.md) · [docs/arc42/arc42-uniteam.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/arc42/arc42-uniteam.md) · [docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md) · [app/application/bus.py](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/app/application/bus.py).

<a id="verifacts"></a>

## VeriFacts

Rama **master**, punta consultada [9cac28456536b832d475e006a957d50fbd874756](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/9cac28456536b832d475e006a957d50fbd874756), fecha del commit 2026-10-22T05:18:49Z (UTC).

Se reconoce avance sustancial de S12: arc42 §8.6–8.9 ya contiene la tabla operación→garantía, contraste de crear/consultar, justificación de no usar caché de aplicación, diseño condicional e invalidación; ADR0012 compara cinco decisiones y argumenta el mayor costo de revertir contenido completo sin propietario. La revisión estática confirma INSERT/commit y lectura por otra conexión, seis pruebas de consistencia, refresh del historial tras POST y caché de estáticos nginx. El run Sonar del 22 de octubre registra 50 pruebas aprobadas y QUALITY GATE STATUS: PASSED; ya no corresponde afirmar que solo hay pings o scanner no verificado. Pendientes: publicar dominio iscoutb.dev con certificado válido; actualizar README que aún mezcla 20/44 pruebas y token Sonar pendiente; acotar la palabra linearizable al modelo y pruebas realmente observados, sin equiparar pruebas secuenciales a prueba de concurrencia. Alinear C4 con el proxy nginx de despliegue y continuar las mitigaciones SSRF/historial sin propietario declaradas pendientes, sin tratar el ADR como corrección de código.

**Tablero:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. **README:** Externo. URL pública HTTP sslip; falta dominio institucional con certificado válido.

**CI/sondeos consultados:** [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/39727407103): success; [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/39727407032): success; [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/39692583748): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/9cac28456536b832d475e006a957d50fbd874756/README.md) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/9cac28456536b832d475e006a957d50fbd874756/docs/arc42/08-conceptos-transversales.md) · [docs/adr/0012-modelo-almacenamiento-sqlite-costo-reversion.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/9cac28456536b832d475e006a957d50fbd874756/docs/adr/0012-modelo-almacenamiento-sqlite-costo-reversion.md) · [tests/test_consistencia.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/9cac28456536b832d475e006a957d50fbd874756/tests/test_consistencia.py) · [app/persistence/repository.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/9cac28456536b832d475e006a957d50fbd874756/app/persistence/repository.py) · [app/api/routes.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/9cac28456536b832d475e006a957d50fbd874756/app/api/routes.py) · [frontend/nginx.conf](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/9cac28456536b832d475e006a957d50fbd874756/frontend/nginx.conf).

<a id="xald"></a>

## XALD

Rama **master**, punta consultada [405a39e0feff40a8414841b6936d5a2dc4488ba4](https://github.com/ISCOUTB/AS_202620_XALD/commit/405a39e0feff40a8414841b6936d5a2dc4488ba4), fecha del commit 2026-10-19T03:00:24Z (UTC).

Se mantiene la documentación de idempotencia/sincronización del 18 de octubre (Colombia) y CI Android/backend exitoso; no hay cambios nuevos en la rama principal desde el seguimiento anterior. El README publica backend Render, pero no subdominio iscoutb.dev. Para S12, transformar la tabla de casos de idempotencia en operación→garantía y contrastar guardar local/registrar remoto sin prometer durabilidad o convergencia que no ofrece el almacenamiento en memoria. Justificar no usar caché o definir su invalidación, comparar el costo de reversión de las decisiones de datos y actualizar C4 nivel2 con almacenes propios/tecnología, distinguiendo memoria actual de Room futuro. Las seis issues están cerradas, pero una tiene razón duplicate y solo cinco completed; ese cierre no acredita pendientes S12 resueltos.

**Tablero:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. **README:** Externo. Backend Render, fuera del dominio requerido.

**CI/sondeos consultados:** [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/39192603030): success; [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/39192133664): success; [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/39192041562): success. Consultar el alcance descrito arriba; un workflow no sustituye todas las pruebas.

**Fuentes de contenido:** [README](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/README.md) · [docs/arc42/08-Cross-cutting Concepts.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/arc42/08-Cross-cutting Concepts.md) · [docs/c4/c2.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/c4/c2.md) · [backend/app/main.py](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/backend/app/main.py).
