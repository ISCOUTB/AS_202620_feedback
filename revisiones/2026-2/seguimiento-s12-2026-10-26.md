# Seguimiento de los 23 proyectos · 26 de octubre de 2026

Consulta del **26 de octubre de 2026**, desde las 08:13 COT (13:13 UTC), sobre los 23 proyectos del listado vigente. Seguimiento documental, no recalificación. **No se cierra S12 automáticamente** ni se recalifica con este seguimiento. Se conservan calificaciones, planillas, matrices y cortes históricos.

**43 abiertas y 132 cerradas** (131 completed; 1 duplicate); 19 abiertas sin asignar. Pull requests excluidas.

README: **10 con algún endpoint institucional; 6 con enlaces externos; 7 sin URL pública concreta**. Las direcciones institucionales incluyen APIs, no prueban que toda interfaz esté publicada.

Se conservan las confirmaciones del docente: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. Estas declaraciones no son pruebas funcionales automatizadas de este corte.

Se leyeron repositorios y resultados de GitHub sin ejecutar código estudiantil ni modificar sus issues o despliegues. Los PDF se excluyen. Código fusionado, CI, publicación y aceptación funcional son evidencias distintas. No se repitieron pruebas funcionales en vivo. No se obtuvieron estados personalizados de GitHub Projects; OPEN/CLOSED y motivos de cierre pertenecen a issues, no a columnas de tablero.

[Issues y motivos de cierre](seguimiento-issues-2026-10-26.md) · [README y despliegues](seguimiento-despliegues-2026-10-26.md) · [Corte anterior](seguimiento-s12-2026-10-25.md)

<a id="audioshare"></a>

## AudioShare

Rama **master**, [8de5ac1daacd189b38d732a0d3d2e916ee29a281](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/8de5ac1daacd189b38d732a0d3d2e916ee29a281), fecha del commit 2026-10-26T04:47:47Z (UTC).

Integra PR7 y PR9: decisiones de persistencia/consistencia y prototipo aislado de sincronización por mensajes, con deduplicación, reintentos y DLQ volátiles. El CI de Node y la publicación de imagen pasan; Flutter falla en analyze, por lo que sus pruebas y build web quedan omitidos. El README ahora dice que Docker compila Flutter Web, pero también reporta que el dominio aún sirve el cliente legado y /rooms devuelve 404: es observación del equipo, no prueba independiente de este corte; publicar imagen no acredita redespliegue.

**Próximos pasos:**
- Corregir flutter analyze y repetir pruebas/build del mismo commit.
- Redesplegar y verificar /rooms, cliente Flutter y recorrido real; conservar límites del simulador volátil.

**Issues GitHub:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar. Motivos: 2 completed.

**README:** Institucional. Mismo origen institucional para API/cliente; el equipo reporta que todavía sirve legado y requiere redespliegue. La imagen nueva no prueba activación.

**PR consultadas:** [#9](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/9): fusionada 2026-10-26T04:47:48Z; [#8](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/7): fusionada 2026-10-26T03:42:05Z; [#2](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/2): fusionada 2026-09-01T14:56:35Z; [#1](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/1): fusionada 2026-08-31T03:06:48Z.

**CI consultado:** [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898269): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898219): success (misma punta); [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898215): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/README.md) · [evidencia-taller-mensajeria.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/docs/evidencia-taller-mensajeria.md) · [README.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/experiments/messaging-prototype/README.md) · [package.json](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/package.json) · [40270898269](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898269) · [40270898219](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898219) · [40270898215](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898215)

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, [7c7200f1d2669a0dd63cb7fa0b3587135357b78c](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7c7200f1d2669a0dd63cb7fa0b3587135357b78c), fecha del commit 2026-10-26T05:40:17Z (UTC).

Corrige el operador Python inválido señalado ayer y ahora pasa Idempotency-Key al caso de uso/repositorio PostgreSQL de publicaciones, en lugar de ignorarlo. Añade recursos/feed y prototipo de mensajería con outbox en memoria. Persisten almacenamiento/comparación directa de contraseña sin hash y secreto JWT predeterminado; no se reproduce su valor. La búsqueda de idempotencia no compara autor ni payload antes de devolver una publicación previa: revisar alcance y conflicto de claves. Los dos workflows actuales siguen fallando sin jobs disponibles; no se demuestra que las pruebas hayan corrido. README actualizado afirma despliegue HTTPS, pero no publica una URL concreta.

**Próximos pasos:**
- Usar hash de contraseñas y rechazar arranque inseguro sin configuración JWT.
- Aislar claves de idempotencia por autor/operación, validar payload y probar duplicados concurrentes/conflictivos.
- Resolver workflows fallidos y publicar URL exacta de frontend/API en README.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. Declara HTTPS/Dokploy, pero sin URL pública concreta del sitio en README.

**PR consultadas:** [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3): fusionada 2026-10-05T05:46:36Z; [#2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2): fusionada 2026-09-21T04:56:52Z; [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta.

**CI consultado:** [.github/workflows/backend-tests.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275481686): failure (misma punta); [.github/workflows/contrato.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275480682): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/README.md) · [auth_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/inbound/api/auth_router.py) · [publicacion_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/inbound/api/publicacion_router.py) · [crear_publicacion.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/application/use_cases/crear_publicacion.py) · [publicacion_repository.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/outbound/postgres/publicacion_repository.py) · [outbox.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/outbound/messaging/outbox.py) · [40275481686](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275481686) · [40275480682](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275480682)

<a id="dinamikutb"></a>

## Dinamik

Rama **master**, [834d26371ef79aab268b394ea32ed9b12cef967e](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/834d26371ef79aab268b394ea32ed9b12cef967e), fecha del commit 2026-10-26T04:56:29Z (UTC).

Añade historial transaccional, documentación S12 y API institucional en README. ADR0012 cambia el plan: laboratorio como referencia y Render como respaldo temporal sin recrear su BD; el equipo reporta comprobación externa del 26/oct con health 200, sin verificación independiente aquí. F7 aún conserva el plan viejo de recreación y debe reconciliarse. CI backend: 84 pruebas pasan y una falla porque el monkeypatch del modelo sigue activo al consultar historial; el log no demuestra pérdida de atomicidad. Frontend y Pages pasan, Sonar se omite. El frontend sigue documentado en GitHub Pages: contar API institucional no equivale a frontend institucional ni a demostrar el cambio efectivo de API_BASE_URL.

**Próximos pasos:**
- Reconciliar F7 con ADR0012: documentar transición efectiva a laboratorio y retiro de Render, sin exigir el plan antiguo de recreación.
- Restaurar el monkeypatch antes de consultar historial y repetir CI backend/atomicidad.
- Verificar API_BASE_URL del frontend, acceso externo y respaldos del volumen; publicar frontend bajo iscoutb.dev.

**Issues GitHub:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. Nuevo subdominio institucional solo para API; frontend Pages externo. README dice despliegue en curso y ADR0012 reporta verificación externa: reconciliar fechas. No comprobación funcional propia.

**PR consultadas:** [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35): cerrada sin fusión registrada; [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37): fusionada 2026-10-23T03:04:11Z; [#36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36): fusionada 2026-10-23T01:01:46Z; [#33](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/33): fusionada 2026-09-27T17:38:37Z; [#32](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/32): fusionada 2026-09-22T03:51:10Z.

**CI consultado:** [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40271620975): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40271620947): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/834d26371ef79aab268b394ea32ed9b12cef967e/README.md) · [evidencia-s12.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/834d26371ef79aab268b394ea32ed9b12cef967e/docs/evidencia-s12.md) · [11-risks-and-technical-debt.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/834d26371ef79aab268b394ea32ed9b12cef967e/docs/arc42/11-risks-and-technical-debt.md) · [0012-despliegue-en-servidor-del-laboratorio.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/834d26371ef79aab268b394ea32ed9b12cef967e/docs/adr/0012-despliegue-en-servidor-del-laboratorio.md) · [40271620975](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40271620975) · [40271620947](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40271620947)

<a id="drift"></a>

## Drift

Rama **master**, [d9a181630f9c7cc9daf3d58705092b245cdc7c73](https://github.com/ISCOUTB/AS_202620_Drift/commit/d9a181630f9c7cc9daf3d58705092b245cdc7c73), fecha del commit 2026-10-25T22:37:33Z (UTC).

PR32 integrado: actualiza S12, ADR0010, arc42 y C4 con almacenamiento de navegador y ausencia de brokers; explicita costo de reversión de datos. CI y despliegue Azure ejecutados con éxito para la punta actual. Esto no convierte las mediciones simuladas previas en rendimiento real ni acredita aceptación funcional en el dominio institucional.

**Próximos pasos:**
- Validar recorrido real en el despliegue institucional y conservar evidencias separadas de Azure.
- Repetir mediciones relevantes con dependencias reales y distinguir decisiones de datos de implementación.

**Issues GitHub:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. Frontend y API /api; API alternativa; Frontend alternativo

**PR consultadas:** [#32](https://github.com/ISCOUTB/AS_202620_Drift/pull/32): fusionada 2026-10-25T22:37:33Z; [#31](https://github.com/ISCOUTB/AS_202620_Drift/pull/31): fusionada 2026-10-21T04:53:32Z; [#30](https://github.com/ISCOUTB/AS_202620_Drift/pull/30): fusionada 2026-10-19T03:20:50Z; [#29](https://github.com/ISCOUTB/AS_202620_Drift/pull/29): fusionada 2026-10-19T03:07:18Z; [#28](https://github.com/ISCOUTB/AS_202620_Drift/pull/28): fusionada 2026-10-19T02:08:58Z.

**CI consultado:** [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/d9a181630f9c7cc9daf3d58705092b245cdc7c73/README.md) · [40241076074](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074) · [40241076067](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067)

<a id="elmapita"></a>

## ElMapita

Rama **main**, [0421885424d13478cf33c717fdd933a4748d9025](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/0421885424d13478cf33c717fdd933a4748d9025), fecha del commit 2026-10-19T08:33:59Z (UTC).

Sin nueva punta ni cambio del README respecto al 25/oct. CI de esa punta continúa exitoso. Se conserva la presentación y funcionamiento confirmados por el docente; sigue faltando URL pública concreta en README y no se infiere falta de despliegue por ese vacío documental.

**Próximos pasos:**
- Publicar URL exacta del despliegue operativo en README bajo iscoutb.dev.
- Conservar y completar evidencia S12 sin confundir ausencia documental con ausencia de avance.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/39223716465): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/README.md) · [39223716465](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/39223716465)

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), fecha del commit 2026-10-26T03:57:38Z (UTC).

PR3 integra documentación de consistencia y prototipo aislado de envío automático de invitaciones, con proveedor simulado, deduplicación, reintentos y DLQ en memoria. Su workflow específico ejecuta pruebas y demo con éxito; no envía correos reales ni integra Flask/BD/Dokploy. El CI general ahora falla al recolectar test_simulador.py por import relativo sin paquete reconocido, no por el error DATABASE_URL del corte anterior; contrato y Docker quedan omitidos. Pages publica documentación estática, no aceptación de la API. README mantiene host pendiente, sin URL pública concreta.

**Próximos pasos:**
- Corregir empaquetado/import del prototipo para que pytest general pueda recolectarlo y repetir contrato/build.
- Mantener separada evidencia de correo simulado de envío real; definir persistencia/proveedor antes de integrar.
- Documentar URL institucional concreta y alcance de rutas PostgreSQL frente a las heredadas en memoria.

**Issues GitHub:** 1 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

**PR consultadas:** [#3](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/3): fusionada 2026-10-26T03:57:38Z; [#2](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/2): fusionada 2026-09-28T02:39:59Z.

**CI consultado:** [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): failure (misma punta); [Taller mensajes y consistencia](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/talleres/mensajes-consistencia/README.md) · [ci.yml](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/.github/workflows/ci.yml) · [40266609521](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521) · [40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410) · [40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284)

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, [5fa232b25e3122474291e5cc41ead96f9b567856](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/5fa232b25e3122474291e5cc41ead96f9b567856), fecha del commit 2026-10-26T04:21:32Z (UTC).

Integra S12/ADR0006 y taller asíncrono aislado. El run actual pasa 12 pruebas base, 11 de contrato y nueve de mensajería, además de auditorías de arquitectura y dependencias; el fallo antiguo de auditoría está superado. La cola, deduplicación y DLQ son volátiles y el endpoint de aforo permanece síncrono; caché/event-log son diseños, no integración productiva. El workflow no configura PostgreSQL ni ejecuta su prueba específica: no atribuirle validación de esa base. README sigue describiendo backend institucional.

**Próximos pasos:**
- Ejecutar integración PostgreSQL con base aislada y evidenciar el recorrido Flutter/API.
- Conservar límites del prototipo y no afirmar durabilidad, broker ni caché operativa a partir del diseño.

**Issues GitHub:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend; interfaz Flutter pública no acreditada

**PR consultadas:** [#18](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/18): fusionada 2026-10-26T00:15:00Z; [#17](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/17): fusionada 2026-10-19T01:09:26Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/README.md) · [limites-experimento.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/docs/taller-mensajeria/limites-experimento.md) · [evidencia-pruebas.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/docs/taller-mensajeria/evidencia-pruebas.md) · [ci.yml](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/.github/workflows/ci.yml) · [40268686360](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360)

<a id="inventrack"></a>

## InvenTrack

Rama **main**, [1269ffb40890a34dac7daa924cfcc85c7e0e5778](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/1269ffb40890a34dac7daa924cfcc85c7e0e5778), fecha del commit 2026-10-26T04:40:41Z (UTC).

Integra auditoría asíncrona en las rutas reales de entradas/salidas mediante BackgroundTasks y simulador local, con correlación, métricas, deduplicación y reintentos; CI ejecuta 29 pruebas y contrato con éxito. ADR0015 completa almacenamiento en memoria y costos de reversión estimados. No es broker durable ni despliegue verificado. La clave X-Idempotency-Key se usa en el evento después de modificar stock: la deduplicación del consumidor no evita repetir la operación HTTP de inventario. Scanner exitoso no acredita por sí solo Quality Gate.

**Próximos pasos:**
- Probar repetición de POST con la misma clave y separar idempotencia de operación de deduplicación de auditoría.
- Documentar/validar pérdida tras reinicio y ventana entre actualización de stock y publicación, antes de exigir durabilidad.
- Acreditar despliegue de esta punta y frontend institucional por separado.

**Issues GitHub:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: 7 completed.

**README:** Institucional. API; API alternativa

**CI consultado:** [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40270300788): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/1269ffb40890a34dac7daa924cfcc85c7e0e5778/README.md) · [evidencia-mensajeria-s12.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/1269ffb40890a34dac7daa924cfcc85c7e0e5778/docs/evidencia-mensajeria-s12.md) · [0015-completar-decision-de-almacenamiento-y-reversion.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/1269ffb40890a34dac7daa924cfcc85c7e0e5778/docs/adr/0015-completar-decision-de-almacenamiento-y-reversion.md) · [registrar_movimiento.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/1269ffb40890a34dac7daa924cfcc85c7e0e5778/app/inventario/application/registrar_movimiento.py) · [router.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/1269ffb40890a34dac7daa924cfcc85c7e0e5778/app/inventario/infrastructure/router.py) · [0016-integrar-eventos-de-auditoria-en-movimientos.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/1269ffb40890a34dac7daa924cfcc85c7e0e5778/docs/adr/0016-integrar-eventos-de-auditoria-en-movimientos.md) · [40270300788](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40270300788)

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [3d003b62ffe92c659699bd1236424fb397bc2eee](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/3d003b62ffe92c659699bd1236424fb397bc2eee), fecha del commit 2026-10-25T03:25:42Z (UTC).

Sin nueva punta ni README desde el corte del 25. Se mantienen la integración Garage/PostgreSQL, protecciones de pago/entrega y evidencia de CI de la misma punta. Las ocho PR de dependencias #16–23 siguen abiertas; no se cuentan como funcionalidades fusionadas. README continúa sin URL pública vigente concreta. No se repitió aceptación funcional en vivo.

**Próximos pasos:**
- Publicar en README la URL vigente de frontend y API bajo iscoutb.dev, diferenciándola del despliegue Azure retirado.
- Cerrar las deudas de persistencia de idempotencia y reintentos con evidencia ejecutada; revisar las actualizaciones de dependencias sin confundirlas con avances integrados.

**Issues GitHub:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. Motivos: 14 completed.

**README:** Sin URL concreta. Solo Azure explícitamente retirado; ninguna URL pública vigente concreta en README raíz.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/22): abierta; [#21](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/21): abierta; [#20](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/20): abierta; [#19](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/19): abierta; [#18](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/18): abierta; [#17](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/16): abierta; [#15](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/15): fusionada 2026-10-22T19:07:22Z.

**CI consultado:** [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40158232304): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/README.md) · [40158232304](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40158232304)

<a id="lostvault"></a>

## LostVault

Rama **main**, [3a6e157110bd3c63e76de9cce68c63991e747468](https://github.com/ISCOUTB/AS_202620_LostVault/commit/3a6e157110bd3c63e76de9cce68c63991e747468), fecha del commit 2026-10-26T04:46:40Z (UTC).

PR #20 y #22 integradas: nueva estrategia S12, middleware Cache-Control y validación de expiración JWT en backend/main.py; taller de mensajería con outbox transaccional SQLite, consumidor idempotente, reintentos y fallidos. En la punta actual CI ejecuta y aprueba 27 pruebas backend y 18 del taller, además de la demo; Flutter y Build pasan. Es simulador local de un proceso, sin red ni conexión a la API desplegada; backend sigue en memoria y PostgreSQL permanece propuesto. Backend checks continúa sin probar la implementación separada api/. PR #21 sigue abierta; no incorporar su contenido como fusionado. README no documenta URL pública vigente.

**Próximos pasos:**
- Conectar persistencia y eventos al flujo real solo tras implementar y validar PostgreSQL; mantener explícito que el taller SQLite no es mensajería productiva.
- Añadir cobertura de api/ o aclarar cuál implementación se despliega; publicar frontend/API institucionales y comprobar autorización y consistencia multiinstancia.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de trabajo o despliegue.

**PR consultadas:** [#21](https://github.com/ISCOUTB/AS_202620_LostVault/pull/21): abierta; [#22](https://github.com/ISCOUTB/AS_202620_LostVault/pull/22): fusionada 2026-10-26T04:46:41Z; [#20](https://github.com/ISCOUTB/AS_202620_LostVault/pull/20): fusionada 2026-10-26T01:52:55Z; [#19](https://github.com/ISCOUTB/AS_202620_LostVault/pull/19): fusionada 2026-10-20T16:16:34Z; [#18](https://github.com/ISCOUTB/AS_202620_LostVault/pull/18): fusionada 2026-10-19T01:43:15Z; [#17](https://github.com/ISCOUTB/AS_202620_LostVault/pull/17): fusionada 2026-10-19T01:32:11Z; [#16](https://github.com/ISCOUTB/AS_202620_LostVault/pull/16): fusionada 2026-10-05T03:30:54Z; [#15](https://github.com/ISCOUTB/AS_202620_LostVault/pull/15): fusionada 2026-10-05T02:31:39Z; [#14](https://github.com/ISCOUTB/AS_202620_LostVault/pull/14): fusionada 2026-10-05T00:42:49Z; [#13](https://github.com/ISCOUTB/AS_202620_LostVault/pull/13): fusionada 2026-09-28T04:39:31Z.

**CI consultado:** [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589): success (misma punta); [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466): success (misma punta); [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/README.md) · [40270806589](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589) · [40270806466](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466) · [40270806424](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424) · [e19be366f7e922a8a9c9abd4a808899f14b2999b...3a6e157110bd3c63e76de9cce68c63991e747468](https://github.com/ISCOUTB/AS_202620_LostVault/compare/e19be366f7e922a8a9c9abd4a808899f14b2999b...3a6e157110bd3c63e76de9cce68c63991e747468) · [taller-mensajeria.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/docs/mensajeria/taller-mensajeria.md)

<a id="mapsutb"></a>

## mapsutb

Rama **master**, [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), fecha del commit 2026-10-25T14:04:14Z (UTC).

Se incorporó ADR0018 y evidencia S12 de datos/caché; una lectura fallida de zonas o grafo ya no queda cacheada. La fijación de firebase-tools 15.34.0 supera el error previo del despliegue: el run exacto ejecutó pruebas Flutter, build, publicación Firebase y URL/health con éxito. Las issues #55 y #56 están cerradas completed. Las sondas programadas posteriores pasan, sin equivaler a aceptación manual integral. README sigue en Firebase, fuera del dominio institucional; no confundir este proyecto con ElMapita.

**Próximos pasos:**
- Mantener la evidencia del arreglo y los cierres; verificar comportamiento de recarga/reintento del grafo con escenarios reproducibles.
- Publicar frontend bajo iscoutb.dev y actualizar README; distinguir disponibilidad de sonda de aceptación del recorrido funcional.

**Issues GitHub:** 0 abiertas / 54 cerradas; 0 abiertas sin asignar. Motivos: 54 completed.

**README:** Externo. Frontend Firebase externo; sonda CI disponible, sin nueva aceptación funcional propia.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z.

**CI consultado:** [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40316263516): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40308409011): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40301979335): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40294747964): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40287933483): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40283175702): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [40316263516](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40316263516) · [40308409011](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40308409011) · [40301979335](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40301979335) · [40294747964](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40294747964) · [40287933483](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40287933483) · [40283175702](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40283175702) · [4b8fa088faec96772e76c8c4f2782919ec87a9b9...03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/compare/4b8fa088faec96772e76c8c4f2782919ec87a9b9...03e331d4436039869e27ce2dc1adda2d520fa833) · [40200515940](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200515940) · [55](https://github.com/ISCOUTB/AS_202620_mapsutb/issues/55) · [56](https://github.com/ISCOUTB/AS_202620_mapsutb/issues/56)

<a id="pideutb"></a>

## PideUtb

Rama **master**, [ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f), fecha del commit 2026-10-23T15:04:06Z (UTC).

Sin cambios de punta, README ni CI desde el 25. Se conserva la identidad visual integrada en PR #29 y el workflow exitoso de la misma revisión; los pasos Sonar/análisis/Quality Gate omitidos no acreditan un gate aprobado. El docente confirmó actualización presentada y despliegues. README mantiene sitio y API institucionales, sin nueva prueba manual de esta revisión.

**Próximos pasos:**
- Conservar la separación de frontend/API documentados y aportar evidencia funcional del rediseño, no inferida de pruebas backend.
- Ejecutar análisis y Quality Gate reales y atender las deudas S12 pendientes con pruebas trazables.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. Frontend/panel y API institucionales; docente confirma presentación/despliegues; sin nueva verificación visual.

**PR consultadas:** [#29](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/29): fusionada 2026-10-23T15:04:06Z; [#28](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/28): fusionada 2026-10-20T14:55:39Z; [#27](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/27): fusionada 2026-10-18T23:40:46Z; [#26](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/26): fusionada 2026-10-18T22:31:12Z; [#25](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/25): fusionada 2026-10-18T18:31:49Z; [#24](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/24): fusionada 2026-10-18T17:05:21Z; [#23](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/23): fusionada 2026-10-18T15:44:46Z; [#22](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/22): fusionada 2026-10-18T02:49:18Z; [#21](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/21): fusionada 2026-10-18T02:12:59Z; [#20](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/20): fusionada 2026-10-18T01:32:03Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39975061857): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/README.md) · [39975061857](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39975061857)

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [bba9513f965184ceea1c36eda722c4ac9fcc70b7](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/bba9513f965184ceea1c36eda722c4ac9fcc70b7), fecha del commit 2026-10-26T04:34:37Z (UTC).

PR #61–65 fusionadas: estrategia de datos S12, correcciones de evidencia/C4 y estabilización del flujo Android, más taller aislado de mensajería. La punta actual pasa backend, Flutter, Compose/persistencia, contrato público y flujo real Web/Android; el job Android ejecutó el emulador y no fue omitido. Esto supera fallos de revisiones anteriores, sin transferirles el resultado. El taller usa SQLite, deduplicación, reintentos/DLQ y backoff real con sleeper inyectable; no integra broker ni outbox productivo. README distingue API iscoutb.dev y frontend GitHub Pages: el requisito de dominio de toda la solución sigue parcial.

**Próximos pasos:**
- Conservar evidencia exacta del flujo Web/Android reparado y separar CI controlado de aceptación manual del despliegue.
- Mover/documentar el frontend bajo iscoutb.dev y mantener explícito el carácter aislado del taller frente a MySQL productivo.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. Cumplimiento parcial: API institucional, frontend externo GitHub Pages. Azure es histórico.

**PR consultadas:** [#65](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/65): fusionada 2026-10-26T04:34:38Z; [#64](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/64): fusionada 2026-10-26T03:51:27Z; [#63](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/63): fusionada 2026-10-26T03:03:33Z; [#62](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/62): fusionada 2026-10-26T01:31:24Z; [#61](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/61): fusionada 2026-10-26T00:57:55Z; [#59](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/59): fusionada 2026-10-19T04:51:37Z; [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60): abierta; [#57](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/57): fusionada 2026-10-19T04:17:24Z; [#58](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/58): fusionada 2026-10-19T04:04:00Z; [#56](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/56): fusionada 2026-10-19T03:17:47Z.

**CI consultado:** [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786871): success (misma punta); [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786849): success (misma punta); [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786840): success (misma punta); [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786825): success (misma punta); [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786823): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/bba9513f965184ceea1c36eda722c4ac9fcc70b7/README.md) · [40269786871](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786871) · [40269786849](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786849) · [40269786840](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786840) · [40269786825](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786825) · [40269786823](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786823) · [a237dd2f22b02bb547f87a07d15b6d31ea0dc758...bba9513f965184ceea1c36eda722c4ac9fcc70b7](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/compare/a237dd2f22b02bb547f87a07d15b6d31ea0dc758...bba9513f965184ceea1c36eda722c4ac9fcc70b7)

<a id="recobra"></a>

## Recobra

Rama **master**, [00f9291c4e59b315a65ba2af348ed449b28319c7](https://github.com/ISCOUTB/AS_202620_Recobra/commit/00f9291c4e59b315a65ba2af348ed449b28319c7), fecha del commit 2026-10-24T14:04:29Z (UTC).

Sin nuevos commits, README ni runs desde el 25. Se conserva la evidencia del run exacto: 37 pruebas de adaptadores PostgreSQL y restauración de 23 filas en nueve tablas, además del Quality Gate previamente verificado. Los e2e de mensajería inyectan fallos y el resto de e2e usa memoria; no acreditan respaldos programados productivos ni alertas recibidas por personas. README distingue vitrina, Flutter Web y API. Se conserva la presentación confirmada por el docente.

**Próximos pasos:**
- Validar programación real de respaldos, restauración y RTO en el entorno objetivo, sin presentar la prueba CI como operación productiva.
- Completar alerta hacia personas y aceptación del recorrido desplegado con fuentes verificables.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README aclara vitrina, Flutter Web y API en mismo host institucional; no se añade auditoría funcional.

**CI consultado:** [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40100869755): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/README.md) · [40100869755](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40100869755)

<a id="routb"></a>

## ROUTB

Rama **master**, [22c2953553a9fc3518fb63576ac622d8bf5e80df](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/22c2953553a9fc3518fb63576ac622d8bf5e80df), fecha del commit 2026-10-25T23:22:49Z (UTC).

PR #53 y #54 integradas: garantía de solicitud activa única, migración 010 y pruebas de concurrencia; documentación alineada con Dokploy; taller de notificaciones con contrato, deduplicación, reintentos y DLQ. CI de la punta pasa pruebas/contrato, ciclo Alembic y build Docker. El bot Sonar sí publica Quality Gate aprobado para ambas PR (en #54 informa tres issues nuevas); esta evidencia es distinta del job Actions que sigue siendo un echo. El taller es aislado y en memoria, no mensajería productiva durable. La evidencia declara migración 010 aún no aplicada a Supabase desarrollo/producción; el CI no prueba aplicación en ese entorno. Se conserva avance entregado según docente.

**Próximos pasos:**
- Aplicar y verificar la migración 010 en el entorno autorizado antes de atribuir la garantía de unicidad al despliegue real.
- Mantener explícita la pérdida de cola en reinicio del prototipo y su no integración productiva; resolver observaciones Sonar y aportar aceptación funcional.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend institucional y guía actualizada a Dokploy; aplicación de migración 010 al entorno objetivo aún no confirmada.

**PR consultadas:** [#54](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/54): fusionada 2026-10-25T23:22:50Z; [#53](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/53): fusionada 2026-10-25T18:04:34Z; [#52](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/52): fusionada 2026-10-23T14:47:48Z; [#51](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/51): fusionada 2026-10-18T21:39:27Z; [#50](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/50): fusionada 2026-10-13T03:02:26Z; [#49](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/49): fusionada 2026-10-12T00:30:24Z; [#48](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/48): fusionada 2026-10-11T23:52:36Z; [#47](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/47): cerrada sin fusión registrada; [#46](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/46): fusionada 2026-10-03T23:20:32Z; [#45](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/45): fusionada 2026-10-03T22:57:29Z.

**CI consultado:** [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40291687022): success (misma punta); [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/README.md) · [40291687022](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40291687022) · [40244499934](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934) · [5d686a594d3e3515233e60b4e6b33330ded05572...22c2953553a9fc3518fb63576ac622d8bf5e80df](https://github.com/ISCOUTB/AS_202620_ROUTB/compare/5d686a594d3e3515233e60b4e6b33330ded05572...22c2953553a9fc3518fb63576ac622d8bf5e80df) · [53#issuecomment-6401195876](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/53#issuecomment-6401195876) · [54#issuecomment-6404835108](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/54#issuecomment-6404835108) · [SEMANA12.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/docs/evidencia/SEMANA12.md)

<a id="shareu"></a>

## ShareU

Rama **master**, [2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767), fecha del commit 2026-10-25T22:52:08Z (UTC).

Nuevo commit incorpora repositorio Firestore para documentos, ADR0010–0012, modos de fallo y pruebas con sustitución del cliente. El README sigue describiendo SQLite/datos reiniciados y placeholders de despliegue: hay deriva documental respecto del nuevo repositorio. El run de la punta falla y no devuelve jobs ejecutados; no acredita pruebas aprobadas ni permite atribuir esta falla actual exclusivamente a Sonar. PR #22 y #23 siguen abiertas y sus propuestas no están integradas. No se verificó persistencia real en Firebase ni despliegue.

**Próximos pasos:**
- Conciliar README/C4/ADR con Firestore actual y publicar URL institucional concreta de frontend/API.
- Corregir y ejecutar el workflow con evidencia de pruebas del repositorio y resiliencia; validar persistencia en el entorno objetivo sin dar por real la simulación de cliente.

**Issues GitHub:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: 10 completed.

**README:** Sin URL concreta. Placeholders Vercel/Render y localhost, no URL pública concreta vigente.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z.

**CI consultado:** [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/README.md) · [40242189282](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282) · [39508608eae4c1a56a5e4fc11a055bf6afb2c003...2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/compare/39508608eae4c1a56a5e4fc11a055bf6afb2c003...2c0ca6f50285cc803bb344e748a3121cf99d3767)

<a id="sistema-de-calificacion-automatica"></a>

## QuantIA

Rama **master**, [561d520b138a1689d9bec9bdff597bdae66a6952](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/561d520b138a1689d9bec9bdff597bdae66a6952), fecha del commit 2026-10-26T01:08:51Z (UTC).

Avance real desde el 25/oct: separa hoja_id de trabajo_id, implementa caché de propuestas con invalidación y contrato 1.4.0, y sustituye la cola sin acuse por consumo Redis con acuse, reintentos, recuperación y lista de fallidos. El CI exacto acredita 193 pruebas backend, 73 frontend y un paso específico de 17 pruebas de mensajería. Por tanto, ya no corresponde mantener «sin acuse» como pendiente vigente. El ensayo documentado es local; el procesamiento aún abre/registra imágenes (no OMR), supone un solo worker y Redis sin persistencia sigue siendo un riesgo.

**Próximos pasos:**
- Validar el consumidor actualizado en el entorno desplegado y documentar la revisión exacta, sin confundir ensayo local con Render.
- Resolver persistencia de Redis/almacén y estrategia antes de añadir un segundo worker; conservar explícito que OMR aún no está implementado.
- Publicar frontend y API bajo iscoutb.dev.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Frontend y API Render; no dominio institucional. Sin sondeo directo en esta revisión.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin fusión registrada.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40252791139): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40248478029): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40247817142): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/README.md) · [40252791139](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40252791139) · [40248478029](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40248478029) · [taller-mensajeria.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/docs/evidencia/taller-mensajeria.md)

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [e903230d220735b43c9c53c42c64c66524ce0ff9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/e903230d220735b43c9c53c42c64c66524ce0ff9), fecha del commit 2026-10-25T15:08:51Z (UTC).

Corrige el disparador YAML de CI, construye y arranca la imagen contra PostgreSQL de prueba, incorpora comprobación del Quality Gate para el commit y alinea despliegue/C4 con Dokploy mediante ADR-0010. Retira Terraform histórico y añade consistencia y decisión de no cachear lecturas. CI/CD exitosos consultados corresponden a d4d4371, no a la punta documental posterior; el CD acredita solicitud por webhook, no finalización ni salud del despliegue. Se conserva funcionamiento y presentación confirmados por el docente.

**Próximos pasos:**
- Verificar en Dokploy la revisión efectivamente desplegada y su salud; el webhook exitoso no lo acredita por sí solo.
- Reconciliar README y ADR sobre respaldo Render/TLS, y mantener la distinción entre API entregada y Flutter objetivo.

**Issues GitHub:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: 4 completed.

**README:** Institucional. API institucional; README también enlaza Render como alternativa histórica, sin confirmar respaldo activo. Flutter sigue arquitectura objetivo. Funcionamiento confirmado por docente; webhook CD no acredita fin del despliegue.

**PR consultadas:** [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z; [#14](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/14): fusionada 2026-09-17T01:53:44Z; [#13](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/13): fusionada 2026-09-16T01:48:07Z; [#12](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/12): fusionada 2026-09-14T01:01:35Z; [#11](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/11): fusionada 2026-09-12T17:29:59Z; [#10](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/10): fusionada 2026-09-12T15:26:17Z; [#9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/9): fusionada 2026-09-11T02:08:20Z; [#8](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/8): fusionada 2026-09-11T00:36:16Z.

**CI consultado:** [CD](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203934640): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203750864): success (otra revisión/rama; no acredita la punta); [CD](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39441872010): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39441578508): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/README.md) · [40203934640](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203934640) · [40203750864](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203750864) · [ci.yml](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/.github/workflows/ci.yml) · [0010-despliegue-con-dokploy-y-docker-compose.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/docs/adr/0010-despliegue-con-dokploy-y-docker-compose.md)

<a id="tienda-virtual-utb"></a>

## Tienda Virtual

Rama **main**, [647bcbd413354775e85a9444f97a2db82725c5f1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/647bcbd413354775e85a9444f97a2db82725c5f1), fecha del commit 2026-10-25T16:53:06Z (UTC).

Entrega documentación S12 de consistencia y caché, ADR de transacción compartida pedidos/inventario y mejoras de navegación de pedidos. Corrige la importación de legado: acepta un nombre JSON controlado, rechaza rutas y enlaces simbólicos, y agrega pruebas. El CI exacto pasa frontend/backend, contrato, RLS y comprobación Alembic; Sonar aparece success con análisis omitido, no acredita Quality Gate. La caché Redis sigue propuesta, mientras la lectura actual del catálogo usa no-store; no presentar diseño como implementación.

**Próximos pasos:**
- Implementar y medir la caché propuesta solo tras validar invalidación y concurrencia; mantener inventario y autorización fuera de ella.
- Restablecer ejecución verificable de Sonar/Quality Gate y reemplazar URL temporal por subdominio institucional con TLS válido.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Frontend sslip temporal; el equipo documenta certificado autofirmado pendiente y despliegue 0.5.0. No se sorteó aviso TLS ni se verificó el sitio en vivo.

**PR consultadas:** [#12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/12): fusionada 2026-10-25T02:58:28Z; [#11](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/11): fusionada 2026-10-24T20:15:26Z; [#10](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/10): fusionada 2026-10-24T19:40:05Z; [#9](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/9): fusionada 2026-10-24T19:22:55Z; [#8](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/8): fusionada 2026-10-24T19:22:38Z; [#7](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/7): fusionada 2026-10-24T19:22:22Z; [#6](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/6): fusionada 2026-10-24T19:22:12Z; [#5](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/5): fusionada 2026-10-24T19:21:59Z; [#4](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/4): fusionada 2026-10-24T19:21:48Z; [#3](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/3): fusionada 2026-10-24T19:21:38Z.

**CI consultado:** [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995): success (misma punta); [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40212692658): success (otra revisión/rama; no acredita la punta); [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40156471490): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/README.md) · [40213830995](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995) · [40212692658](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40212692658) · [cache-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/cache-s12.md) · [consistencia-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/consistencia-s12.md) · [archivos_legado.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/backend/app/archivos_legado.py)

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [31932f0006542c6f3f6222071bb1a9c36b6f888a](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/31932f0006542c6f3f6222071bb1a9c36b6f888a), fecha del commit 2026-10-26T06:03:01Z (UTC).

Fusiona outbox, worker idempotente y reintentos del taller, junto con documentación de consistencia/caché y avances de administración de salones, roles y cliente. El bloqueo transitorio de múltiples cabezas Alembic ya fue corregido; la punta actual acredita 78 pruebas de tests/ sobre PostgreSQL 16 aislado y deploy con migraciones/reinicio exitosos. Ese comando excluye app/tests/ y no prueba todo el cliente. El notificador sigue simulado y el worker requiere operación separada; la caché es diseño no implementado. Persiste el fallback a DATABASE_URL de la fixture fuera de CI antes de borrar/recrear tablas.

**Próximos pasos:**
- Eliminar el fallback destructivo a DATABASE_URL o exigir validación inequívoca de BD de pruebas antes de drop_all.
- Documentar y verificar operación del worker y notificación real si se pretende incluirla en el despliegue; conservar el alcance tests/ de CI.
- Publicar URL exacta institucional en README y validar los flujos nuevos del cliente; no presentar caché propuesta como activa.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README raíz sin endpoint público vigente. Solo en código: https://129-80-171-141.nip.io; release APK v1.0.2 publicado, no prueba de sitio institucional.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/4): fusionada 2026-10-26T04:35:44Z; [#3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/3): fusionada 2026-10-25T18:20:31Z; [#2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/2): fusionada 2026-10-06T06:08:06Z.

**CI consultado:** [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926): success (misma punta); [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40269883908): success (otra revisión/rama; no acredita la punta); [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40239492098): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/README.md) · [40278118926](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926) · [40269883908](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40269883908) · [limites-del-experimento.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/mensajeria/limites-del-experimento.md) · [conftest.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/tests/conftest.py) · [consistencia-por-operacion.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/datos/consistencia-por-operacion.md)

<a id="uniteam"></a>

## uniTeam

Rama **master**, [0a44bd5a8d9374423b08fef87e46672cd6ad501b](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/0a44bd5a8d9374423b08fef87e46672cd6ad501b), fecha del commit 2026-10-26T00:55:53Z (UTC).

Integra PR #9 y #10: taller de mensajería SQLite con contrato, deduplicación, reintentos y fallidos, explícitamente aislado de la API/auditoría real, más estrategia de consistencia y ADR que conserva MySQL como fuente de verdad. CI de la punta pasa. La sonda de despliegue más reciente falla contra direcciones Render antiguas; el README publica DuckDNS, por lo que ese fallo no demuestra caída del despliegue actual. Las políticas de caché propuestas no deben darse por habilitadas.

**Próximos pasos:**
- Actualizar las sondas a las direcciones desplegadas vigentes y completar migración a iscoutb.dev.
- Mantener aislado el taller; si se integra, diseñar publicación atómica con la tarea y aceptación del efecto externo.
- Distinguir política de caché/documentación de controles efectivamente habilitados.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Externo. Frontend y API DuckDNS. Sonda sigue consultando Render; su fallo no determina disponibilidad de DuckDNS.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/4): fusionada 2026-10-04T21:23:33Z; [#2](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/2): fusionada 2026-09-14T01:20:18Z; [#10](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/10): fusionada 2026-10-26T00:55:53Z; [#9](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/9): fusionada 2026-10-26T00:55:34Z; [#8](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/8): fusionada 2026-10-23T05:15:01Z; [#7](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/7): fusionada 2026-10-23T04:57:30Z; [#6](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/6): fusionada 2026-10-23T04:38:54Z; [#5](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/5): fusionada 2026-10-13T15:44:45Z; [#3](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/3): fusionada 2026-09-21T16:46:49Z.

**CI consultado:** [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40282509675): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40252045358): failure (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40251714762): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/README.md) · [40282509675](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40282509675) · [40252045358](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40252045358) · [0015-taller-de-mensajeria-local-aislado.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/adr/0015-taller-de-mensajeria-local-aislado.md) · [0016-conservar-mysql-como-fuente-de-verdad.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/adr/0016-conservar-mysql-como-fuente-de-verdad.md)

<a id="xald"></a>

## XALD

Rama **master**, [1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00](https://github.com/ISCOUTB/AS_202620_XALD/commit/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00), fecha del commit 2026-10-26T04:04:58Z (UTC).

Incorpora sincronización HTTP con contrato versionado, correlación, deduplicación, backoff y fallidos en los módulos del producto, además de ADR y documentación de límites. CI exacto pasa 21 pruebas backend, pruebas Gradle de módulos, contrato y paso de health tras hook Render. No obstante, la documentación reconoce que nadie invoca automáticamente procesarPendientes: el envío se dispara en pruebas, no como tarea automática de la app. Cola y deduplicación siguen en memoria; la evidencia E2E es local con fallo inyectado y conserva placeholders de commit/run.

**Próximos pasos:**
- Conectar procesarPendientes a un ejecutor real con conectividad y persistir cola/marcas antes de prometer entrega tras reinicios.
- Completar referencias de commit/run en evidencia y distinguir E2E local del funcionamiento en dispositivo/Render.
- Publicar el endpoint bajo iscoutb.dev y verificar persistencia y sincronización de extremo a extremo.

**Issues GitHub:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. Motivos: 5 completed; 1 duplicate.

**README:** Externo. Backend Render. El CI incluye paso de health exitoso; no es verificación funcional propia ni evidencia de frontend institucional.

**PR consultadas:** [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z; [#24](https://github.com/ISCOUTB/AS_202620_XALD/pull/24): fusionada 2026-09-27T16:24:00Z; [#23](https://github.com/ISCOUTB/AS_202620_XALD/pull/23): fusionada 2026-09-20T17:34:35Z; [#22](https://github.com/ISCOUTB/AS_202620_XALD/pull/22): cerrada sin fusión registrada; [#21](https://github.com/ISCOUTB/AS_202620_XALD/pull/21): cerrada sin fusión registrada; [#20](https://github.com/ISCOUTB/AS_202620_XALD/pull/20): fusionada 2026-09-20T16:21:31Z; [#19](https://github.com/ISCOUTB/AS_202620_XALD/pull/19): fusionada 2026-09-16T04:45:22Z; [#18](https://github.com/ISCOUTB/AS_202620_XALD/pull/18): fusionada 2026-09-14T03:06:22Z; [#15](https://github.com/ISCOUTB/AS_202620_XALD/pull/15): fusionada 2026-09-13T16:09:58Z.

**CI consultado:** [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501): success (misma punta); [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40250732162): success (otra revisión/rama; no acredita la punta); [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40250688201): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/README.md) · [40267222501](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501) · [40250732162](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40250732162) · [limites-del-experimento.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/mensajes/limites-del-experimento.md) · [evidencia.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/mensajes/evidencia.md)

<a id="verifacts"></a>

## VeriFacts

Rama **master**, [cf2075dcae6ba48507ba47b59aede18afb4df449](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/cf2075dcae6ba48507ba47b59aede18afb4df449), fecha del commit 2026-10-24T17:50:57Z (UTC).

Sin cambio de punta ni README desde el corte del 25/oct. Se mantienen tres issues cerradas completed y la evidencia anterior de 66 pruebas, smoke de imagen y SonarCloud exitosos para la misma revisión. No hay nueva implementación que permita retirar los límites documentados: prototipo de mensajería aislado y dominio institucional/certificado pendientes. El cierre documental de issues no equivale a aceptación funcional.

**Próximos pasos:**
- Completar dominio iscoutb.dev y certificado, diferenciando interfaz y API.
- Mantener explícito qué mensajería es prototipo y aportar aceptación funcional del sistema integrado antes de cerrar pendientes.

**Issues GitHub:** 0 abiertas / 3 cerradas; 0 abiertas sin asignar. Motivos: 3 completed.

**README:** Externo. Referencia HTTP sslip. README declara pendiente dominio institucional/certificado; frontend / y API /docs,/health separados conceptualmente.

**CI consultado:** [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40117996304): success (misma punta); [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40117996296): success (misma punta); [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40116574370): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/cf2075dcae6ba48507ba47b59aede18afb4df449/README.md) · [40117996304](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40117996304) · [40117996296](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40117996296)

