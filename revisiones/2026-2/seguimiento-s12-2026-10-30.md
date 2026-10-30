# Seguimiento de los 23 proyectos · 30 de octubre de 2026

Consulta del **30 de octubre de 2026**, con observaciones fechadas por proyecto (UTC), sobre los 23 proyectos del listado vigente. Seguimiento documental, no recalificación. **No se cierra S12 automáticamente** ni se recalifica con este seguimiento. Se conservan calificaciones, planillas, matrices y cortes históricos.

**43 abiertas y 132 cerradas** (131 completed; 1 duplicate); 19 abiertas sin asignar. Pull requests excluidas.

README: **10 con algún endpoint institucional; 6 con enlaces externos; 7 sin URL pública concreta**. Las direcciones institucionales incluyen APIs, no prueban que toda interfaz esté publicada.

Se conservan las confirmaciones del docente: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. Estas declaraciones no son pruebas funcionales automatizadas de este corte.

Se leyeron repositorios y resultados de GitHub sin ejecutar código estudiantil ni modificar sus issues o despliegues. Código fusionado, CI, publicación y aceptación funcional son evidencias distintas. No se repitieron pruebas funcionales en vivo. El conector disponible no expone estados personalizados de GitHub Projects; no se obtuvieron estados del tablero; OPEN/CLOSED y motivos de cierre pertenecen a issues, no a columnas de tablero.

[Issues y motivos de cierre](seguimiento-issues-2026-10-30.md) · [README y despliegues](seguimiento-despliegues-2026-10-30.md) · [Corte anterior](seguimiento-s12-2026-10-29.md)

## Cambios respecto al corte anterior

- **AudioShare**: Incorpora identificadores únicos de receptores, reingreso idempotente a una sala y rechazo 409 si se reutiliza un identificador con otro rol. Añade descarga temporal completa de MP3 con validación, limpieza y reintento en plataformas nativas; en web conserva reproducción desde URL, por lo que no debe atribuirse descarga local a ese cliente. El estado de pista y volumen se gestionan por receptor. El fallo Flutter del corte anterior queda superado: el CI de esta punta pasa analyze, 36 pruebas con una omitida y build web; backend pasa 44 pruebas y la publicación de imagen termina con éxito. No se acredita redespliegue: el README conserva el reporte del equipo del 26/oct sobre cliente legado y /rooms 404, y explica que Dokploy construye desde Compose, sin consumir la imagen Docker Hub publicada. Sin verificación funcional en vivo en este corte.
- **ElMapita**: Integra mapa 3D del campus con capas, selección de destino, animaciones, georreferencia, ubicación y avisos de llegada por vibración; incorpora navegación entre mapa/lugares e idiomas español/inglés. El código y las pruebas están en main, aunque docs/ia.md todavía describe una parte como sin commit: debe reconciliarse esa bitácora. El CI de la punta pasa 30 pruebas Flutter, build web y 56 pruebas unitarias backend. El verde global sigue siendo parcial: flutter analyze informa 28 hallazgos; E2E GET / falla con 404 frente a 200 y se neutraliza con echo; SonarCloud falla por autorización/proyecto no encontrado y omite el gate. El equipo documenta comprobaciones en teléfono y calibración aproximada con OpenStreetMap, no verificadas independientemente aquí. El README continúa sin URL pública concreta y Compose sigue dirigido al backend. Se conserva la confirmación docente de que ElMapita presentó y funciona, sin atribuir aceptación de estas nuevas funciones a este corte.
- **PideUtb**: Integra PR #35–38: migración 008 y configuración por defecto para alinear el mostrador con el establecimiento de los pedidos; activos CSS/JS con huella para evitar mezclas de caché; recuperación del pedido y su token en localStorage con caducidad de seis horas, confirmación antes de perder un código y sondeo hasta el estado final. También incorpora validación/codificación de identificadores y referencias, contraste de productos agotados, controles táctiles y reducción del alfabeto de canje para evitar caracteres confundibles. El CI de la punta acredita 556 pruebas Python aprobadas y tres omitidas, más 26 recorridos de navegador contra servicios locales del runner; las 103 PostgreSQL son un subconjunto reejecutado. La imagen del sitio se construye y verifica sus referencias con huella, sin demostrar publicación ni despliegue. El check externo SonarCloud Code Analysis pasa; el job Actions SonarCloud omite el análisis por configuración, por lo que su verde no lo acredita. El gate fallido de PR37 queda superado por el comentario actualizado aprobado y las validaciones añadidas, no se presenta como fallo vigente. PR35 enumera configuración, migración y redespliegue en Dokploy aún sin evidencia operativa independiente en este corte. PR37 reporta Render legado con no-server: no se verificó aquí su retiro definitivo ni el estado de los demás servicios legados, y no se ha acreditado exposición efectiva. La demo del 3/nov es un plan del equipo. Se conserva presentación y despliegues confirmados por docente, sin nueva aceptación de producción ni cobros reales.
- **CampusMarket**: Integra PR #66–75: Idempotency-Key transaccional para crear publicaciones, reutilización ante reintentos y rechazo de la misma clave con otro contenido; Flutter conserva la clave durante el reintento. Las cinco ejecuciones de CI de la punta pasan: los logs acreditan 87 pruebas backend y cuatro de contrato separadas, más siete Flutter, así como flujos Chrome desktop/mobile y Android en emulador. Se implementa trazabilidad de imagen, exportación del artefacto probado y publicación GHCR; el run 41026286264 confirma publicación de la imagen cuya revisión fuente es 2154e788, no la punta documental actual. El ensayo manual 41051624793 ejecutado desde 66936889 acredita descarga autenticada por digest, identidad OCI, MySQL, degradación/recuperación, persistencia SQL y archivos tras recreación y limpieza aislada. Esto supera el pendiente antiguo del cuerpo de PR73; PR74 corrige el digest y PR75 actualiza su evidencia. La decisión operativa mantiene aplazada la promoción GHCR en Dokploy hasta acreditar respaldo recuperable, montajes, acceso desde servidor y rollback. El CI de contrato público sigue observando la etiqueta de revisión 78564167, no prueba que se sirva la punta actual; no se atribuye a esa cabecera una auditoría del código desplegado. No se introducen pagos ni se acredita una migración productiva. README mantiene API institucional y frontend externo GitHub Pages.
- **Calificación automática**: Cinco commits nuevos en master añaden infraestructura del laboratorio: Compose con API, worker separado, Redis con AOF y volúmenes nombrados para cola, imágenes y bitácora; corrigen el seguimiento de mensajes con prefijos del panel y empates de tiempo por intento. El CI exacto acredita 196 pruebas backend y 73 Flutter, compilación web y publicación efectiva de la rama despliegue, verificada en 66bf050. Esa publicación no demuestra que Dokploy haya terminado ni valida el recorrido público. El código de despliegue documenta frontend https://calificacion.iscoutb.dev y API https://api-calificacion.iscoutb.dev, pero README sigue sin cambios con Render: desfase documental, no falta de trabajo ni inexistencia de despliegue. El equipo reporta uso de una hoja sintética en el laboratorio; no se repitió esa aceptación. No corresponde seguir describiendo Redis sin persistencia como el único diseño actual: AOF/volúmenes ya están en Compose, mientras su recuperación operativa y respaldo requieren evidencia. El alcance OMR y la operación con múltiples workers siguen pendientes.

Los demás proyectos fueron revalidados; sin novedades sustantivas se conserva su feedback individual anterior, sin añadir secciones repetidas.

<a id="audioshare"></a>

## AudioShare

Rama **master**, [da3c4058629e3e8bbadc559541bdeb61ca57c55a](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/da3c4058629e3e8bbadc559541bdeb61ca57c55a), fecha del commit 2026-10-30T05:03:11Z (UTC).

Incorpora identificadores únicos de receptores, reingreso idempotente a una sala y rechazo 409 si se reutiliza un identificador con otro rol. Añade descarga temporal completa de MP3 con validación, limpieza y reintento en plataformas nativas; en web conserva reproducción desde URL, por lo que no debe atribuirse descarga local a ese cliente. El estado de pista y volumen se gestionan por receptor. El fallo Flutter del corte anterior queda superado: el CI de esta punta pasa analyze, 36 pruebas con una omitida y build web; backend pasa 44 pruebas y la publicación de imagen termina con éxito. No se acredita redespliegue: el README conserva el reporte del equipo del 26/oct sobre cliente legado y /rooms 404, y explica que Dokploy construye desde Compose, sin consumir la imagen Docker Hub publicada. Sin verificación funcional en vivo en este corte.

**Próximos pasos:**
- Redesplegar la revisión actual mediante el flujo Dokploy documentado y adjuntar evidencia fechada de frontend, API y sincronización entre receptores en el dominio institucional.
- Separar validación nativa de descarga local y reproducción web por URL; probar fallo de descarga, reintento y reingreso conservando rol.
- Documentar el motivo y alcance de la prueba Flutter omitida; no equiparar imagen publicada con versión servida.

**Issues GitHub:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar. Motivos: 2 completed.

**README:** Institucional. README documenta https://audioshare.iscoutb.dev como origen compartido de frontend y API. Conserva observación del equipo del 26/oct: cliente legado y GET /rooms 404. El CI actual compila Flutter y publica imagen, pero Dokploy construye desde Compose y no consume esa imagen Docker Hub. Redespliegue y funcionamiento actual no verificados.

**PR consultadas:** [#9](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/9): fusionada 2026-10-26T04:47:48Z; [#8](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/7): fusionada 2026-10-26T03:42:05Z; [#2](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/2): fusionada 2026-09-01T14:56:35Z; [#1](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/1): fusionada 2026-08-31T03:06:48Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229901): success (misma punta); [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229863): success (misma punta); [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229849): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:03:53Z (UTC).

**Fuentes:** [evidencia-taller-mensajeria.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/docs/evidencia-taller-mensajeria.md) · [package.json](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/package.json) · [40270898269](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898269) · [40270898219](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898219) · [40270898215](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898215) · [README actual](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/da3c4058629e3e8bbadc559541bdeb61ca57c55a/README.md) · [Issues consultadas](https://github.com/ISCOUTB/AS_202620_AudioShare/issues) · [CI actual](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229901) · [CI actual](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229863) · [CI actual](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229849) · [Cambios de audio y reingreso](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/da3c4058629e3e8bbadc559541bdeb61ca57c55a)

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, [7c7200f1d2669a0dd63cb7fa0b3587135357b78c](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7c7200f1d2669a0dd63cb7fa0b3587135357b78c), fecha del commit 2026-10-26T05:40:17Z (UTC).

Revalidación del 30/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 29/oct. Corrige el operador Python inválido señalado en el corte previo y ahora pasa Idempotency-Key al caso de uso/repositorio PostgreSQL de publicaciones, en lugar de ignorarlo. Añade recursos/feed y prototipo de mensajería con outbox en memoria. Persisten almacenamiento/comparación directa de contraseña sin hash y secreto JWT predeterminado; no se reproduce su valor. La búsqueda de idempotencia no compara autor ni payload antes de devolver una publicación previa: revisar alcance y conflicto de claves. Los dos workflows actuales siguen fallando sin jobs disponibles; no se demuestra que las pruebas hayan corrido. README actualizado afirma despliegue HTTPS, pero no publica una URL concreta.

**Próximos pasos:**
- Usar hash de contraseñas y rechazar arranque inseguro sin configuración JWT.
- Aislar claves de idempotencia por autor/operación, validar payload y probar duplicados concurrentes/conflictivos.
- Resolver workflows fallidos y publicar URL exacta de frontend/API en README.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. Declara HTTPS/Dokploy, pero sin URL pública concreta del sitio en README.

**PR consultadas:** [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3): fusionada 2026-10-05T05:46:36Z; [#2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2): fusionada 2026-09-21T04:56:52Z; [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta.

**CI consultado:** [.github/workflows/backend-tests.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275481686): failure (misma punta); [.github/workflows/contrato.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275480682): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:03:53Z (UTC).

**Fuentes:** [auth_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/inbound/api/auth_router.py) · [publicacion_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/inbound/api/publicacion_router.py) · [crear_publicacion.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/application/use_cases/crear_publicacion.py) · [publicacion_repository.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/outbound/postgres/publicacion_repository.py) · [outbox.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/outbound/messaging/outbox.py) · [40275481686](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275481686) · [40275480682](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275480682) · [README actual](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/README.md) · [Issues consultadas](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/issues) · [CI actual](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275481686) · [CI actual](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275480682)

<a id="dinamikutb"></a>

## DinamikUTB

Rama **master**, [822baaa371ec94827d09319a09e13f11f7123f64](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/822baaa371ec94827d09319a09e13f11f7123f64), fecha del commit 2026-10-27T17:08:57Z (UTC).

Revalidación del 30/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 29/oct. Integra nuevas pantallas administrativas, currículo y gestión de cuentas, además de imagen Flutter/Nginx para el laboratorio. El README de frontend separa https://dinamikutb.iscoutb.dev (web) y https://api.dinamikutb.iscoutb.dev (API), sujetos a aprovisionamiento; ADR0006 marca GitHub Pages como reemplazado. El README raíz sigue describiendo el primer dominio como API y conserva enlaces anteriores: hay desalineación documental. Publicar la imagen GHCR termina correctamente, pero no acredita redeploy en Dokploy. CI de la misma punta falla: pytest no recolecta por ImportError de RequisitoPrograma; Flutter registra 20 pruebas aprobadas y cuatro fallidas (tres de validación de correo y una de registro de estudiantes); SonarCloud queda omitido. Los routers nuevos de currículo, programas y reportes no se incorporan en app/main.py consultado; su existencia no demuestra rutas disponibles. No se verificó funcionamiento en vivo.

**Próximos pasos:**
- Resolver el ImportError de RequisitoPrograma y las cuatro pruebas Flutter; repetir CI en la misma punta.
- Integrar y probar los routers nuevos antes de afirmar disponibilidad de currículo, programas y reportes.
- Unificar README raíz y frontend con los dominios realmente provisionados; distinguir API/web, retirar referencias vigentes obsoletas y acreditar redeploy Dokploy con recorrido funcional.

**Issues GitHub:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. README raíz y frontend discrepan en roles/dominios. GHCR acredita imagen, no despliegue ni DNS/TLS o aceptación; no se prescribe recrear la base antigua de Render.

**PR consultadas:** [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35): cerrada sin fusión registrada; [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37): fusionada 2026-10-23T03:04:11Z; [#36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36): fusionada 2026-10-23T01:01:46Z; [#33](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/33): fusionada 2026-09-27T17:38:37Z; [#32](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/32): fusionada 2026-09-22T03:51:10Z; [#31](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/31): fusionada 2026-09-22T03:16:20Z; [#30](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/30): fusionada 2026-09-21T18:41:30Z; [#29](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/29): fusionada 2026-09-21T17:48:40Z; [#12](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/12): fusionada 2026-09-07T04:26:25Z; [#11](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/11): fusionada 2026-09-07T03:57:51Z.

**CI consultado:** [Publish frontend image](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40549937090): success (misma punta); [Publish frontend image](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831470): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831321): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:03:53Z (UTC).

**Fuentes:** [evidencia-s12.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/evidencia-s12.md) · [11-risks-and-technical-debt.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/arc42/11-risks-and-technical-debt.md) · [0012-despliegue-en-servidor-del-laboratorio.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/adr/0012-despliegue-en-servidor-del-laboratorio.md) · [40549937090](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40549937090) · [40547831321](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831321) · [0006-plataforma-despliegue-frontend.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/adr/0006-plataforma-despliegue-frontend.md) · [main.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/backend/app/main.py) · [publish-frontend-image.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/.github/workflows/publish-frontend-image.yml) · [README actual](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/README.md) · [Issues consultadas](https://github.com/ISCOUTB/AS_202620_DinamikUTB/issues) · [CI actual](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40549937090) · [CI actual](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831470) · [CI actual](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831321)

<a id="drift"></a>

## Drift

Rama **master**, [d9a181630f9c7cc9daf3d58705092b245cdc7c73](https://github.com/ISCOUTB/AS_202620_Drift/commit/d9a181630f9c7cc9daf3d58705092b245cdc7c73), fecha del commit 2026-10-25T22:37:33Z (UTC).

Revalidación del 30/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 29/oct. PR32 integrado: actualiza S12, ADR0010, arc42 y C4 con almacenamiento de navegador y ausencia de brokers; explicita costo de reversión de datos. CI y despliegue Azure ejecutados con éxito para la punta actual. Esto no convierte las mediciones simuladas previas en rendimiento real ni acredita aceptación funcional en el dominio institucional.

**Próximos pasos:**
- Validar recorrido real en el despliegue institucional y conservar evidencias separadas de Azure.
- Repetir mediciones relevantes con dependencias reales y distinguir decisiones de datos de implementación.

**Issues GitHub:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. Frontend y API /api; API alternativa; Frontend alternativo

**PR consultadas:** [#32](https://github.com/ISCOUTB/AS_202620_Drift/pull/32): fusionada 2026-10-25T22:37:33Z; [#31](https://github.com/ISCOUTB/AS_202620_Drift/pull/31): fusionada 2026-10-21T04:53:32Z; [#30](https://github.com/ISCOUTB/AS_202620_Drift/pull/30): fusionada 2026-10-19T03:20:50Z; [#29](https://github.com/ISCOUTB/AS_202620_Drift/pull/29): fusionada 2026-10-19T03:07:18Z; [#28](https://github.com/ISCOUTB/AS_202620_Drift/pull/28): fusionada 2026-10-19T02:08:58Z; [#27](https://github.com/ISCOUTB/AS_202620_Drift/pull/27): fusionada 2026-10-12T19:42:41Z; [#26](https://github.com/ISCOUTB/AS_202620_Drift/pull/26): fusionada 2026-10-12T19:15:32Z; [#25](https://github.com/ISCOUTB/AS_202620_Drift/pull/25): fusionada 2026-10-12T04:49:54Z; [#24](https://github.com/ISCOUTB/AS_202620_Drift/pull/24): fusionada 2026-10-11T05:28:23Z; [#23](https://github.com/ISCOUTB/AS_202620_Drift/pull/23): fusionada 2026-10-11T05:21:57Z.

**CI consultado:** [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:03:53Z (UTC).

**Fuentes:** [40241076074](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074) · [40241076067](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067) · [README actual](https://github.com/ISCOUTB/AS_202620_Drift/blob/d9a181630f9c7cc9daf3d58705092b245cdc7c73/README.md) · [Issues consultadas](https://github.com/ISCOUTB/AS_202620_Drift/issues) · [CI actual](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074) · [CI actual](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067)

<a id="elmapita"></a>

## ElMapita

Rama **main**, [fc0f186153d117a5b0d9db715d521e154a8a2ef2](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/fc0f186153d117a5b0d9db715d521e154a8a2ef2), fecha del commit 2026-10-30T01:52:42Z (UTC).

Integra mapa 3D del campus con capas, selección de destino, animaciones, georreferencia, ubicación y avisos de llegada por vibración; incorpora navegación entre mapa/lugares e idiomas español/inglés. El código y las pruebas están en main, aunque docs/ia.md todavía describe una parte como sin commit: debe reconciliarse esa bitácora. El CI de la punta pasa 30 pruebas Flutter, build web y 56 pruebas unitarias backend. El verde global sigue siendo parcial: flutter analyze informa 28 hallazgos; E2E GET / falla con 404 frente a 200 y se neutraliza con echo; SonarCloud falla por autorización/proyecto no encontrado y omite el gate. El equipo documenta comprobaciones en teléfono y calibración aproximada con OpenStreetMap, no verificadas independientemente aquí. El README continúa sin URL pública concreta y Compose sigue dirigido al backend. Se conserva la confirmación docente de que ElMapita presentó y funciona, sin atribuir aceptación de estas nuevas funciones a este corte.

**Próximos pasos:**
- Documentar en README la URL exacta bajo iscoutb.dev, separando API y frontend; aportar evidencia fechada del despliegue de esta punta.
- Hacer vinculante el E2E de backend, atender los 28 hallazgos de analyze y restablecer SonarCloud/Quality Gate antes de describir el CI como completo.
- Reconciliar docs/ia.md con los commits publicados y validar en dispositivos reales permisos de ubicación, guía de llegada, calibración y cambio de idioma.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta. Compose nuevo solo para API; FRONTEND_URL en configuración no prueba frontend ni despliegue activo. Se conserva aceptación docente previa, distinta de la publicación de esta punta.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40988421889): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:03:53Z (UTC).

**Fuentes:** [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/ddcfbbcfacaff506d587dad60c06a744fe7f66ae/deploy/compose.lab.yaml) · [ci.yml](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/ddcfbbcfacaff506d587dad60c06a744fe7f66ae/.github/workflows/ci.yml) · [40781174318](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40781174318) · [123142939572](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40781174318/job/123142939572) · [123143208608](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40781174318/job/123143208608) · [README actual](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/fc0f186153d117a5b0d9db715d521e154a8a2ef2/README.md) · [Issues consultadas](https://github.com/ISCOUTB/AS_202620_ElMapita/issues) · [CI actual](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40988421889) · [Funciones de mapa publicadas](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/fc0f186153d117a5b0d9db715d521e154a8a2ef2) · [Bitácora del equipo](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/fc0f186153d117a5b0d9db715d521e154a8a2ef2/docs/ia.md)

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), fecha del commit 2026-10-26T03:57:38Z (UTC).

Revalidación del 30/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 29/oct. PR3 integra documentación de consistencia y prototipo aislado de envío automático de invitaciones, con proveedor simulado, deduplicación, reintentos y DLQ en memoria. Su workflow específico ejecuta pruebas y demo con éxito; no envía correos reales ni integra Flask/BD/Dokploy. El CI general ahora falla al recolectar test_simulador.py por import relativo sin paquete reconocido, no por el error DATABASE_URL del corte anterior; contrato y Docker quedan omitidos. Pages publica documentación estática, no aceptación de la API. README mantiene host pendiente, sin URL pública concreta.

**Próximos pasos:**
- Corregir empaquetado/import del prototipo para que pytest general pueda recolectarlo y repetir contrato/build.
- Mantener separada evidencia de correo simulado de envío real; definir persistencia/proveedor antes de integrar.
- Documentar URL institucional concreta y alcance de rutas PostgreSQL frente a las heredadas en memoria.

**Issues GitHub:** 1 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

**PR consultadas:** [#3](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/3): fusionada 2026-10-26T03:57:38Z; [#2](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/2): fusionada 2026-09-28T02:39:59Z.

**CI consultado:** [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): failure (misma punta); [Taller mensajes y consistencia](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:03:53Z (UTC).

**Fuentes:** [ci.yml](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/.github/workflows/ci.yml) · [40266609521](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521) · [40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410) · [40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284) · [README actual](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [Issues consultadas](https://github.com/ISCOUTB/AS_202620_EnAgenda/issues) · [CI actual](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521) · [CI actual](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410) · [CI actual](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284)

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, [5fa232b25e3122474291e5cc41ead96f9b567856](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/5fa232b25e3122474291e5cc41ead96f9b567856), fecha del commit 2026-10-26T04:21:32Z (UTC).

Revalidación del 30/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 29/oct. Integra S12/ADR0006 y taller asíncrono aislado. El run actual pasa 12 pruebas base, 11 de contrato y nueve de mensajería, además de auditorías de arquitectura y dependencias; el fallo antiguo de auditoría está superado. La cola, deduplicación y DLQ son volátiles y el endpoint de aforo permanece síncrono; caché/event-log son diseños, no integración productiva. El workflow no configura PostgreSQL ni ejecuta su prueba específica: no atribuirle validación de esa base. README sigue describiendo backend institucional.

**Próximos pasos:**
- Ejecutar integración PostgreSQL con base aislada y evidenciar el recorrido Flutter/API.
- Conservar límites del prototipo y no afirmar durabilidad, broker ni caché operativa a partir del diseño.

**Issues GitHub:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend; interfaz Flutter pública no acreditada

**PR consultadas:** [#18](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/18): fusionada 2026-10-26T00:15:00Z; [#17](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/17): fusionada 2026-10-19T01:09:26Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:03:53Z (UTC).

**Fuentes:** [limites-experimento.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/docs/taller-mensajeria/limites-experimento.md) · [evidencia-pruebas.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/docs/taller-mensajeria/evidencia-pruebas.md) · [ci.yml](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/.github/workflows/ci.yml) · [40268686360](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360) · [README actual](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/README.md) · [Issues consultadas](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/issues) · [CI actual](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360)

<a id="inventrack"></a>

## InvenTrack

Rama **main**, [972a12775ffc073a1efe9e6c9435be497c5187d6](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/972a12775ffc073a1efe9e6c9435be497c5187d6), fecha del commit 2026-10-27T21:37:20Z (UTC).

Revalidación del 30/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 29/oct. Corrige la brecha de idempotencia HTTP: reserva/serializa la clave antes de modificar stock, conserva fingerprint y resultado, devuelve replay sin nuevo movimiento/evento y responde 409 ante payload incompatible. ADR0017 explicita almacenamiento volátil por proceso y la ventana stock/publicación sin outbox. El CI de la punta actual pasa 32 pruebas y vuelve a ejecutar una prueba de contrato incluida en el conjunto, no 33 pruebas distintas; el scanner Sonar termina, sin acreditar por sí solo Quality Gate. La nueva evidencia de despliegue del equipo reporta que el 27/oct no pudo resolver DNS/TLS institucional y obtuvo 503 en /health y /metrics de Render. Esto entra en tensión con las declaraciones anteriores de despliegue/verificación del README. Son observaciones del equipo, no una prueba independiente actual ni demostración de inexistencia de despliegue; falta publicar/verificar esta punta en servicio. El documento de CI cita todavía la revisión anterior.

**Próximos pasos:**
- Actualizar evidencia de CI al run actual y vincular Quality Gate al análisis correspondiente.
- Acreditar hash desplegado, /health, /metrics y recorrido funcional institucional; distinguir API de frontend.
- Mantener explícitos límites de idempotencia en memoria, reinicios y varias réplicas; adoptar registro/outbox durable cuando se requiera recuperación.

**Issues GitHub:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: 7 completed.

**README:** Institucional. README conserva API institucional y alternativa Render. Evidencia del equipo del 27/oct reporta DNS/TLS institucional no verificable y 503 en health/metrics de Render; no es comprobación independiente del corte. Hay que reconciliar ese reporte con las declaraciones previas de despliegue/verificación del README.

**CI consultado:** [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40588329661): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:03:53Z (UTC).

**Fuentes:** [evidencia-mensajeria-s12.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/evidencia-mensajeria-s12.md) · [0015-completar-decision-de-almacenamiento-y-reversion.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/adr/0015-completar-decision-de-almacenamiento-y-reversion.md) · [registrar_movimiento.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/app/inventario/application/registrar_movimiento.py) · [router.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/app/inventario/infrastructure/router.py) · [0016-integrar-eventos-de-auditoria-en-movimientos.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/adr/0016-integrar-eventos-de-auditoria-en-movimientos.md) · [40588329661](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40588329661) · [evidencia-despliegue-s12.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/evidencia-despliegue-s12.md) · [0017-idempotencia-http-en-comandos-de-inventario.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/adr/0017-idempotencia-http-en-comandos-de-inventario.md) · [idempotency.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/app/inventario/infrastructure/idempotency.py) · [README actual](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/README.md) · [Issues consultadas](https://github.com/ISCOUTB/AS_202620_InvenTrack/issues) · [CI actual](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40588329661)

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [15af0876468939cc2de6e6d1298cfdddae32972f](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/15af0876468939cc2de6e6d1298cfdddae32972f), fecha del commit 2026-10-28T19:19:31Z (UTC).

Revalidación del 30/oct: misma punta y README del corte anterior. Integra PR #24 y un complemento posterior: controles de sesión/rol en escrituras de tienda y notificaciones, auditoría de dependencias, aviso de privacidad, procedimiento de rotación documentado y decisión explícita de no implementar ETag ni LISTEN/NOTIFY con una instancia. El CI actual pasa sus cinco jobs. El workflow de despliegue también figura success, pero el log del webhook responde «Branch Not Match» antes de comprobar health=200: esa salud no identifica el commit servido y NO acredita redespliegue de la revisión. Las comprobaciones HTTP y de interfaz descritas por el equipo son locales, no aceptación independiente de producción. README continúa sin URL pública vigente concreta. Las PR de dependencias abiertas no son cambios fusionados.

**Próximos pasos:**
- Corregir la selección de rama del webhook y aportar evidencia de que Dokploy sirve esta revisión; validar controles y cabeceras en el entorno objetivo.
- Documentar en README las URL exactas de frontend y API bajo iscoutb.dev; no reutilizar el enlace Azure retirado.
- Completar límites de uso, protección de secretos, constancia/versionado del consentimiento y reconciliar privacidad con el flujo real; el procedimiento de rotación escrito no es un ensayo ejecutado.

**Issues GitHub:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. Motivos: 14 completed.

**README:** Sin URL concreta. Solo Azure explícitamente retirado; ninguna URL pública vigente concreta en README raíz.

**PR consultadas:** [#29](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/29): abierta; [#19](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/19): cerrada sin fusión registrada; [#23](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/23): abierta; [#21](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/21): abierta; [#22](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/22): cerrada sin fusión registrada; [#28](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/28): abierta; [#18](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/18): cerrada sin fusión registrada; [#27](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/27): abierta; [#26](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/26): abierta; [#25](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/25): abierta; [#24](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/24): fusionada 2026-10-28T15:28:19Z; [#20](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/20): abierta; [#17](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/16): abierta; [#15](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/15): fusionada 2026-10-22T19:07:22Z.

**CI consultado:** [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40753448484): success (misma punta); [Deploy Dokploy (laboratorio de la U)](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40753448422): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:05:44Z (UTC).

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/15af0876468939cc2de6e6d1298cfdddae32972f/README.md) · [Issues GitHub](https://github.com/ISCOUTB/AS_202620_LaPlacita/issues) · [PR](https://github.com/ISCOUTB/AS_202620_LaPlacita/pulls) · [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40753448484) · [Deploy Dokploy (laboratorio de la U)](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40753448422)

<a id="lostvault"></a>

## LostVault

Rama **main**, [3a6e157110bd3c63e76de9cce68c63991e747468](https://github.com/ISCOUTB/AS_202620_LostVault/commit/3a6e157110bd3c63e76de9cce68c63991e747468), fecha del commit 2026-10-26T04:46:40Z (UTC).

Revalidación del 30/oct: misma punta y README que el corte anterior. Continúan integradas PR #20 y #22: Cache-Control, expiración JWT en backend/main.py y taller aislado de outbox SQLite, deduplicación y reintentos. Los tres workflows de la misma punta siguen exitosos; se conserva el alcance previamente verificado de 27 pruebas backend y 18 del taller, no cobertura de la implementación separada api/. PostgreSQL/outbox productivos siguen propuestos y el backend conserva memoria. PR #21 continúa abierta; README sigue sin URL pública concreta.

**Próximos pasos:**
- Conectar persistencia y eventos al flujo real solo tras implementar y validar PostgreSQL; mantener explícito que el taller SQLite no es mensajería productiva.
- Añadir cobertura de api/ o aclarar cuál implementación se despliega; publicar frontend/API institucionales y comprobar autorización y consistencia multiinstancia.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de trabajo o despliegue.

**PR consultadas:** [#21](https://github.com/ISCOUTB/AS_202620_LostVault/pull/21): abierta; [#22](https://github.com/ISCOUTB/AS_202620_LostVault/pull/22): fusionada 2026-10-26T04:46:41Z; [#20](https://github.com/ISCOUTB/AS_202620_LostVault/pull/20): fusionada 2026-10-26T01:52:55Z; [#19](https://github.com/ISCOUTB/AS_202620_LostVault/pull/19): fusionada 2026-10-20T16:16:34Z; [#18](https://github.com/ISCOUTB/AS_202620_LostVault/pull/18): fusionada 2026-10-19T01:43:15Z; [#17](https://github.com/ISCOUTB/AS_202620_LostVault/pull/17): fusionada 2026-10-19T01:32:11Z; [#16](https://github.com/ISCOUTB/AS_202620_LostVault/pull/16): fusionada 2026-10-05T03:30:54Z; [#15](https://github.com/ISCOUTB/AS_202620_LostVault/pull/15): fusionada 2026-10-05T02:31:39Z; [#14](https://github.com/ISCOUTB/AS_202620_LostVault/pull/14): fusionada 2026-10-05T00:42:49Z; [#13](https://github.com/ISCOUTB/AS_202620_LostVault/pull/13): fusionada 2026-09-28T04:39:31Z; [#12](https://github.com/ISCOUTB/AS_202620_LostVault/pull/12): fusionada 2026-09-28T03:17:55Z; [#11](https://github.com/ISCOUTB/AS_202620_LostVault/pull/11): cerrada sin fusión registrada; [#10](https://github.com/ISCOUTB/AS_202620_LostVault/pull/10): fusionada 2026-09-21T04:55:35Z; [#9](https://github.com/ISCOUTB/AS_202620_LostVault/pull/9): fusionada 2026-09-13T23:43:59Z; [#8](https://github.com/ISCOUTB/AS_202620_LostVault/pull/8): fusionada 2026-09-13T18:41:09Z.

**CI consultado:** [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589): success (misma punta); [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466): success (misma punta); [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:05:44Z (UTC).

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/README.md) · [Issues GitHub](https://github.com/ISCOUTB/AS_202620_LostVault/issues) · [PR](https://github.com/ISCOUTB/AS_202620_LostVault/pulls) · [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589) · [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466) · [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424)

<a id="mapsutb"></a>

## mapsutb

Rama **master**, [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), fecha del commit 2026-10-25T14:04:14Z (UTC).

Revalidación del 30/oct: misma punta y README que el corte anterior. La sonda programada más reciente y la sincronización de hallazgos de Sonar terminan exitosamente para la misma punta. Se conserva la evidencia previa de publicación Firebase del commit que fijó firebase-tools 15.34.0; no es una nueva aceptación manual ni un nuevo despliegue. README sigue en mapsutb.web.app, fuera de iscoutb.dev; no confundir con ElMapita.

**Próximos pasos:**
- Mantener la evidencia del arreglo y los cierres; verificar comportamiento de recarga/reintento del grafo con escenarios reproducibles.
- Publicar frontend bajo iscoutb.dev y actualizar README; distinguir disponibilidad de sonda de aceptación del recorrido funcional.

**Issues GitHub:** 0 abiertas / 54 cerradas; 0 abiertas sin asignar. Motivos: 54 completed.

**README:** Externo. Frontend Firebase externo; sonda CI disponible, sin nueva aceptación funcional propia.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z.

**CI consultado:** [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41056184917): success (misma punta); [Sincronizar hallazgos de Sonar a GitHub Issues](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41054399872): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:05:44Z (UTC).

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [Issues GitHub](https://github.com/ISCOUTB/AS_202620_mapsutb/issues) · [PR](https://github.com/ISCOUTB/AS_202620_mapsutb/pulls) · [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41056184917) · [Sincronizar hallazgos de Sonar a GitHub Issues](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41054399872)

<a id="pideutb"></a>

## PideUtb

Rama **master**, [e81e272b20498968b1016a261dee8bce250422da](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/e81e272b20498968b1016a261dee8bce250422da), fecha del commit 2026-10-30T06:16:11Z (UTC).

Integra PR #35–38: migración 008 y configuración por defecto para alinear el mostrador con el establecimiento de los pedidos; activos CSS/JS con huella para evitar mezclas de caché; recuperación del pedido y su token en localStorage con caducidad de seis horas, confirmación antes de perder un código y sondeo hasta el estado final. También incorpora validación/codificación de identificadores y referencias, contraste de productos agotados, controles táctiles y reducción del alfabeto de canje para evitar caracteres confundibles. El CI de la punta acredita 556 pruebas Python aprobadas y tres omitidas, más 26 recorridos de navegador contra servicios locales del runner; las 103 PostgreSQL son un subconjunto reejecutado. La imagen del sitio se construye y verifica sus referencias con huella, sin demostrar publicación ni despliegue. El check externo SonarCloud Code Analysis pasa; el job Actions SonarCloud omite el análisis por configuración, por lo que su verde no lo acredita. El gate fallido de PR37 queda superado por el comentario actualizado aprobado y las validaciones añadidas, no se presenta como fallo vigente. PR35 enumera configuración, migración y redespliegue en Dokploy aún sin evidencia operativa independiente en este corte. PR37 reporta Render legado con no-server: no se verificó aquí su retiro definitivo ni el estado de los demás servicios legados, y no se ha acreditado exposición efectiva. La demo del 3/nov es un plan del equipo. Se conserva presentación y despliegues confirmados por docente, sin nueva aceptación de producción ni cobros reales.

**Próximos pasos:**
- Aportar evidencia del commit servido y de la configuración/migración 008 en el entorno objetivo; repetir allí el recorrido cliente–pasarela de pruebas–mostrador antes de la demo que el equipo anuncia para el 3/nov, manteniendo el reinicio de demo restringido al entorno de prueba.
- Verificar retiro o mitigación de todos los servicios legados con evidencia operativa, sin darlo por acreditado solo por una respuesta no-server reportada por el equipo.
- Conservar pruebas de recarga/retorno, caducidad y limpieza del pedido/token, y medir accesibilidad con los activos realmente desplegados; el almacenamiento persistente requiere mantener las defensas documentadas.
- Reconciliar el resumen del PR38 con su código final: el alfabeto ya se redujo y la suite vigente ejecuta 556 aprobadas/3 omitidas. No sumar las reejecuciones de PostgreSQL ni las dos versiones Python como pruebas nuevas.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. README documenta frontend/panel y API bajo iscoutb.dev. Docente confirma presentación/despliegues; no se repitió verificación funcional de producción. Pruebas de navegador verificadas en CI usan localhost y pasarela simulada, no cobros reales.

**PR consultadas:** [#35](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/35): fusionada 2026-10-29T20:20:16Z; [#36](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/36): fusionada 2026-10-29T21:41:18Z; [#37](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/37): fusionada 2026-10-30T03:53:01Z; [#38](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/38): fusionada 2026-10-30T06:16:11Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41013098666): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:05:44Z (UTC).

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/README.md) · [PR #35](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/35) · [PR #36](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/36) · [PR #37](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/37) · [PR #38](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/38) · [CI punta](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41013098666) · [pytest Python3.12](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41013098666/job/123923180001) · [Navegador CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41013098666/job/123923179986) · [Imagen sitio CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41013098666/job/123923179980) · [Sonar externo](https://github.com/ISCOUTB/AS_202620_PideUtb/runs/123923326783) · [Gate PR37](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/37#issuecomment-6514204345) · [Validaciones frontend](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/sitio/app.js) · [Migración008](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/backend/migraciones/008_el_mostrador_al_establecimiento_de_la_carta.sql) · [Alfabeto canje final](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/backend/app/pedidos/service.py) · [Razón cambio gate](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/docs/calidad-sonarcloud.md)

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [40be256f52d74ad8c9148886f040845658a38855](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/40be256f52d74ad8c9148886f040845658a38855), fecha del commit 2026-10-30T12:43:07Z (UTC).

Integra PR #66–75: Idempotency-Key transaccional para crear publicaciones, reutilización ante reintentos y rechazo de la misma clave con otro contenido; Flutter conserva la clave durante el reintento. Las cinco ejecuciones de CI de la punta pasan: los logs acreditan 87 pruebas backend y cuatro de contrato separadas, más siete Flutter, así como flujos Chrome desktop/mobile y Android en emulador. Se implementa trazabilidad de imagen, exportación del artefacto probado y publicación GHCR; el run 41026286264 confirma publicación de la imagen cuya revisión fuente es 2154e788, no la punta documental actual. El ensayo manual 41051624793 ejecutado desde 66936889 acredita descarga autenticada por digest, identidad OCI, MySQL, degradación/recuperación, persistencia SQL y archivos tras recreación y limpieza aislada. Esto supera el pendiente antiguo del cuerpo de PR73; PR74 corrige el digest y PR75 actualiza su evidencia. La decisión operativa mantiene aplazada la promoción GHCR en Dokploy hasta acreditar respaldo recuperable, montajes, acceso desde servidor y rollback. El CI de contrato público sigue observando la etiqueta de revisión 78564167, no prueba que se sirva la punta actual; no se atribuye a esa cabecera una auditoría del código desplegado. No se introducen pagos ni se acredita una migración productiva. README mantiene API institucional y frontend externo GitHub Pages.

**Próximos pasos:**
- Acreditar respaldo y restauración de MySQL/uploads, montajes reales, acceso GHCR desde Dokploy e imagen anterior recuperable antes de promover el digest; conservar la separación entre ensayo aislado y producción.
- Vincular el commit, digest y cabecera del servicio realmente publicado; la etiqueta observada por el contrato público no acredita automáticamente la revisión fusionada.
- Publicar y documentar el frontend bajo iscoutb.dev, manteniendo explícita la separación respecto del dominio API.
- Mantener evidencia de concurrencia, reintentos y conflicto de Idempotency-Key en el entorno objetivo, sin equiparar pruebas de CI con aceptación de usuarios.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. Cumplimiento parcial: API bajo iscoutb.dev, frontend GitHub Pages externo. CI público registra health/catálogo y etiqueta antigua; no es aceptación independiente ni acredita promoción GHCR en Dokploy. Azure es histórico.

**PR consultadas:** [#75](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/75): fusionada 2026-10-30T12:43:07Z; [#74](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/74): fusionada 2026-10-30T11:53:43Z; [#73](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/73): fusionada 2026-10-30T11:12:50Z; [#72](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/72): fusionada 2026-10-30T09:47:36Z; [#71](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/71): fusionada 2026-10-30T08:56:13Z; [#70](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/70): fusionada 2026-10-30T08:06:09Z; [#69](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/69): fusionada 2026-10-30T07:30:22Z; [#68](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/68): fusionada 2026-10-30T06:56:17Z; [#67](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/67): fusionada 2026-10-30T06:17:29Z; [#66](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/66): fusionada 2026-10-30T03:09:11Z; [#65](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/65): fusionada 2026-10-26T04:34:38Z; [#64](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/64): fusionada 2026-10-26T03:51:27Z; [#63](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/63): fusionada 2026-10-26T03:03:33Z; [#62](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/62): fusionada 2026-10-26T01:31:24Z; [#61](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/61): fusionada 2026-10-26T00:57:55Z; [#59](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/59): fusionada 2026-10-19T04:51:37Z; [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60): abierta; [#57](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/57): fusionada 2026-10-19T04:17:24Z; [#58](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/58): fusionada 2026-10-19T04:04:00Z; [#56](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/56): fusionada 2026-10-19T03:17:47Z; [#55](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/55): fusionada 2026-10-12T04:50:45Z; [#54](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/54): fusionada 2026-10-04T07:14:35Z; [#53](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/53): fusionada 2026-10-04T06:38:56Z; [#52](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/52): fusionada 2026-10-04T04:04:41Z; [#51](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/51): fusionada 2026-10-04T03:06:42Z; [#1](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/1): abierta.

**CI consultado:** [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456331): success (misma punta); [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456304): success (misma punta); [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456301): success (misma punta); [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456260): success (misma punta); [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456247): success (misma punta); [Preparar publicacion GHCR](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41026286264): success (otra revisión/rama; no acredita la punta); [Ensayo aislado de imagen GHCR](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41051624793): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:05:44Z (UTC).

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/40be256f52d74ad8c9148886f040845658a38855/README.md) · [Issues GitHub](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/issues) · [PR](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pulls) · [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456331) · [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456304) · [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456301) · [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456260) · [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456247) · [PR #66](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/66) · [PR #70](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/70) · [PR #72](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/72) · [PR #73](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/73) · [PR #74](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/74) · [PR #75](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/75) · [Idempotencia transaccional](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/40be256f52d74ad8c9148886f040845658a38855/backend/app/publicaciones/repository.py) · [Decisión de no promover aún](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/40be256f52d74ad8c9148886f040845658a38855/docs/operacion/decision-migracion-ghcr.md) · [Evidencia GHCR](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/40be256f52d74ad8c9148886f040845658a38855/docs/operacion/evidencia-ghcr-cierre.md) · [Publicación GHCR](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41026286264) · [Ensayo aislado GHCR](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41051624793)

<a id="recobra"></a>

## Recobra

Rama **master**, [0dda9abd2c76ef9b10724221225c0ed228197c39](https://github.com/ISCOUTB/AS_202620_Recobra/commit/0dda9abd2c76ef9b10724221225c0ed228197c39), fecha del commit 2026-10-29T02:32:33Z (UTC).

Revalidación del 30/oct: misma punta y README del corte anterior. Incorpora seguridad S13: límites de uso, CSP y CORS, tratamiento del origen detrás de Cloudflare, auditoría y avisos operativos, controles de dependencias/secretos y documentación de privacidad que reconoce a Cloudflare. Los seis jobs de la punta pasan; los logs backend acreditan 215 pruebas unitarias, 124 e2e y 10 de contrato. La auditoría verde no significa ausencia de vulnerabilidades: acepta 13 avisos individuales con alcance documentado y vencimiento al 15/dic, mientras npm informa siete paquetes afectados de producción. Los ajustes observados en producción son reportes del equipo, no pruebas repetidas por este seguimiento. Siguen pendientes acciones operativas de protección/rotación y respaldo programado descritas por el equipo; CI no demuestra que se hayan ejecutado. Las diez PR nuevas de Dependabot están abiertas, no fusionadas. README conserva vitrina, Flutter Web y API institucionales. Se mantiene presentación confirmada por docente.

**Próximos pasos:**
- Acreditar las acciones operativas pendientes y el respaldo programado sin publicar credenciales ni datos personales.
- Revisar y probar las PR de dependencias; conservar la distinción entre avisos aceptados y mitigados y cumplir su vencimiento.
- Validar límites, origen del cliente, cabeceras y entrega de avisos en el despliegue actual; aportar evidencia de aceptación funcional independiente del CI.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README aclara vitrina, Flutter Web y API en mismo host institucional; no se añade auditoría funcional.

**PR consultadas:** [#10](https://github.com/ISCOUTB/AS_202620_Recobra/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_Recobra/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_Recobra/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_Recobra/pull/7): abierta; [#6](https://github.com/ISCOUTB/AS_202620_Recobra/pull/6): abierta; [#5](https://github.com/ISCOUTB/AS_202620_Recobra/pull/5): abierta; [#3](https://github.com/ISCOUTB/AS_202620_Recobra/pull/3): abierta; [#2](https://github.com/ISCOUTB/AS_202620_Recobra/pull/2): abierta; [#4](https://github.com/ISCOUTB/AS_202620_Recobra/pull/4): abierta; [#1](https://github.com/ISCOUTB/AS_202620_Recobra/pull/1): abierta.

**CI consultado:** [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:05:44Z (UTC).

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/README.md) · [Issues GitHub](https://github.com/ISCOUTB/AS_202620_Recobra/issues) · [PR](https://github.com/ISCOUTB/AS_202620_Recobra/pulls) · [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927)

<a id="routb"></a>

## ROUTB

Rama **master**, [22c2953553a9fc3518fb63576ac622d8bf5e80df](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/22c2953553a9fc3518fb63576ac622d8bf5e80df), fecha del commit 2026-10-25T23:22:49Z (UTC).

Revalidación del 30/oct: misma punta y README que el corte anterior. Continúan integradas PR #53/#54 y la garantía de solicitud activa única, pero la evidencia de migración 010 no acredita aplicación a Supabase objetivo. El taller de notificaciones permanece aislado y en memoria, no mensajería productiva durable. Se conserva la evidencia previa de gate Sonar del bot, distinta del job Actions que es un echo, y el avance entregado según docente.

**Próximos pasos:**
- Aplicar y verificar la migración 010 en el entorno autorizado antes de atribuir la garantía de unicidad al despliegue real.
- Mantener explícita la pérdida de cola en reinicio del prototipo y su no integración productiva; resolver observaciones Sonar y aportar aceptación funcional.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend institucional y guía actualizada a Dokploy; aplicación de migración 010 al entorno objetivo aún no confirmada.

**PR consultadas:** [#54](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/54): fusionada 2026-10-25T23:22:50Z; [#53](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/53): fusionada 2026-10-25T18:04:34Z; [#52](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/52): fusionada 2026-10-23T14:47:48Z; [#51](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/51): fusionada 2026-10-18T21:39:27Z; [#50](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/50): fusionada 2026-10-13T03:02:26Z; [#49](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/49): fusionada 2026-10-12T00:30:24Z; [#48](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/48): fusionada 2026-10-11T23:52:36Z; [#47](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/47): cerrada sin fusión registrada; [#46](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/46): fusionada 2026-10-03T23:20:32Z; [#45](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/45): fusionada 2026-10-03T22:57:29Z; [#44](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/44): fusionada 2026-10-03T19:53:46Z; [#43](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/43): fusionada 2026-10-03T05:18:30Z; [#42](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/42): fusionada 2026-10-03T01:18:46Z; [#41](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/41): cerrada sin fusión registrada; [#40](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/40): fusionada 2026-09-28T02:58:07Z.

**CI consultado:** [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41024762224): success (misma punta); [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:05:44Z (UTC).

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/README.md) · [Issues GitHub](https://github.com/ISCOUTB/AS_202620_ROUTB/issues) · [PR](https://github.com/ISCOUTB/AS_202620_ROUTB/pulls) · [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41024762224) · [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934)

<a id="shareu"></a>

## ShareU

Rama **master**, [2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767), fecha del commit 2026-10-25T22:52:08Z (UTC).

Revalidación del 30/oct: misma punta y README que el corte anterior. La revisión actual mantiene repositorio Firestore y pruebas con cliente sustituido, mientras README conserva SQLite, reinicio de datos y placeholders de despliegue: sigue la deriva documental. El workflow de la punta permanece fallido; no acredita pruebas aprobadas ni autoriza atribuir la falla exclusivamente a Sonar. PR #22 y #23 siguen abiertas. Persistencia real Firebase y despliegue no se verificaron.

**Próximos pasos:**
- Conciliar README/C4/ADR con Firestore actual y publicar URL institucional concreta de frontend/API.
- Corregir y ejecutar el workflow con evidencia de pruebas del repositorio y resiliencia; validar persistencia en el entorno objetivo sin dar por real la simulación de cliente.

**Issues GitHub:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: 10 completed.

**README:** Sin URL concreta. Placeholders Vercel/Render y localhost, no URL pública concreta vigente.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z.

**CI consultado:** [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:04:30Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/README.md) · [40242189282](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282) · [issues?state=all&per_page=100](https://api.github.com/repos/ISCOUTB/AS_202620_ShareU/issues?state=all&per_page=100) · [pulls?state=all&sort=updated&direction=desc&per_page=30](https://api.github.com/repos/ISCOUTB/AS_202620_ShareU/pulls?state=all&sort=updated&direction=desc&per_page=30) · [runs?per_page=15](https://api.github.com/repos/ISCOUTB/AS_202620_ShareU/actions/runs?per_page=15)

<a id="sistema-de-calificacion-automatica"></a>

## Calificación automática

Rama **master**, [d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc), fecha del commit 2026-10-30T06:04:55Z (UTC).

Cinco commits nuevos en master añaden infraestructura del laboratorio: Compose con API, worker separado, Redis con AOF y volúmenes nombrados para cola, imágenes y bitácora; corrigen el seguimiento de mensajes con prefijos del panel y empates de tiempo por intento. El CI exacto acredita 196 pruebas backend y 73 Flutter, compilación web y publicación efectiva de la rama despliegue, verificada en 66bf050. Esa publicación no demuestra que Dokploy haya terminado ni valida el recorrido público. El código de despliegue documenta frontend https://calificacion.iscoutb.dev y API https://api-calificacion.iscoutb.dev, pero README sigue sin cambios con Render: desfase documental, no falta de trabajo ni inexistencia de despliegue. El equipo reporta uso de una hoja sintética en el laboratorio; no se repitió esa aceptación. No corresponde seguir describiendo Redis sin persistencia como el único diseño actual: AOF/volúmenes ya están en Compose, mientras su recuperación operativa y respaldo requieren evidencia. El alcance OMR y la operación con múltiples workers siguen pendientes.

**Próximos pasos:**
- Actualizar README con las URLs institucionales exactas del frontend y API, la rama despliegue y la relación vigente con Render; reconciliar las decisiones históricas sin borrarlas.
- Acreditar la revisión realmente servida por Dokploy y el recorrido frontend → API → worker con datos sintéticos. Publicar una rama compilada no equivale a finalizar el despliegue.
- Probar reinicio, recuperación y respaldo de cola e imágenes/bitácora en el entorno objetivo; documentar el límite de AOF everysec y validar concurrencia antes de añadir más workers.
- Conservar explícito que procesamiento de imágenes no implica OMR implementado y separar evidencia del equipo de aceptación independiente.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. README todavía enlaza Render. Fuera del README, deploy/compose.lab.yaml y CI documentan https://calificacion.iscoutb.dev (frontend) y https://api-calificacion.iscoutb.dev (API). Se verificó publicación de rama despliegue, no ejecución final en Dokploy ni funcionamiento público. Ausencia de esos enlaces en README no significa ausencia de trabajo o de despliegue.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin fusión registrada.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41012021649): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41010670473): failure (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:04:30Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc/README.md) · [561d520b138a1689d9bec9bdff597bdae66a6952...d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/compare/561d520b138a1689d9bec9bdff597bdae66a6952...d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc/deploy/compose.lab.yaml) · [ci.yml](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc/.github/workflows/ci.yml) · [seguir_trabajo.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc/backend/herramientas/seguir_trabajo.py) · [test_mensajeria.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc/backend/tests/test_mensajeria.py) · [41012021649](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41012021649) · [123919804063](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41012021649/job/123919804063) · [123919803811](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41012021649/job/123919803811) · [123920280929](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41012021649/job/123920280929) · [66bf0507d47da2ff7fc23a491d348d3c1c32bce0](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/66bf0507d47da2ff7fc23a491d348d3c1c32bce0) · [issues](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pulls)

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [e903230d220735b43c9c53c42c64c66524ce0ff9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/e903230d220735b43c9c53c42c64c66524ce0ff9), fecha del commit 2026-10-25T15:08:51Z (UTC).

Sin cambios de punta ni README desde el 29/oct. Se conserva la evidencia de CI/CD exitosos para d4d4371, anterior a la punta documental; el CD solicita un webhook y no acredita finalización ni salud de Dokploy. Siguen pendientes la conciliación del respaldo Render/TLS y la diferencia entre API entregada y Flutter objetivo. Se mantiene la presentación y funcionamiento confirmados por el docente.

**Próximos pasos:**
- Verificar en Dokploy la revisión efectivamente desplegada y su salud; el webhook exitoso no lo acredita por sí solo.
- Reconciliar README y ADR sobre respaldo Render/TLS, y mantener la distinción entre API entregada y Flutter objetivo.

**Issues GitHub:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: 4 completed.

**README:** Institucional. API institucional; README también enlaza Render como alternativa histórica, sin confirmar respaldo activo. Flutter sigue arquitectura objetivo. Funcionamiento confirmado por docente; webhook CD no acredita fin del despliegue.

**PR consultadas:** [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z; [#14](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/14): fusionada 2026-09-17T01:53:44Z; [#13](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/13): fusionada 2026-09-16T01:48:07Z; [#12](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/12): fusionada 2026-09-14T01:01:35Z.

**CI consultado:** [CD](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203934640): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203750864): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:04:30Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/README.md) · [40203934640](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203934640) · [40203750864](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203750864) · [ci.yml](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/.github/workflows/ci.yml) · [0010-despliegue-con-dokploy-y-docker-compose.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/docs/adr/0010-despliegue-con-dokploy-y-docker-compose.md) · [issues?state=all&per_page=100](https://api.github.com/repos/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/issues?state=all&per_page=100) · [pulls?state=all&sort=updated&direction=desc&per_page=30](https://api.github.com/repos/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pulls?state=all&sort=updated&direction=desc&per_page=30) · [runs?per_page=15](https://api.github.com/repos/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs?per_page=15)

<a id="tienda-virtual-utb"></a>

## Tienda virtual UTB

Rama **main**, [647bcbd413354775e85a9444f97a2db82725c5f1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/647bcbd413354775e85a9444f97a2db82725c5f1), fecha del commit 2026-10-25T16:53:06Z (UTC).

Sin cambios de punta, README ni PRs desde el 29/oct. El último workflow de la revisión actual permanece exitoso para frontend/backend, contrato, RLS y Alembic; el análisis Sonar estaba omitido y ese estado no acredita un Quality Gate nuevo. Siguen vigentes la transacción compartida pedidos/inventario y la importación de legado endurecida ya reportadas, mientras Redis es caché propuesta y el catálogo usa no-store.

**Próximos pasos:**
- Implementar y medir la caché propuesta solo tras validar invalidación y concurrencia; mantener inventario y autorización fuera de ella.
- Restablecer ejecución verificable de Sonar/Quality Gate y reemplazar URL temporal por subdominio institucional con TLS válido.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Frontend sslip temporal; el equipo documenta certificado autofirmado pendiente y despliegue 0.5.0. No se sorteó aviso TLS ni se verificó el sitio en vivo.

**PR consultadas:** [#12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/12): fusionada 2026-10-25T02:58:28Z; [#11](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/11): fusionada 2026-10-24T20:15:26Z; [#10](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/10): fusionada 2026-10-24T19:40:05Z; [#9](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/9): fusionada 2026-10-24T19:22:55Z; [#8](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/8): fusionada 2026-10-24T19:22:38Z.

**CI consultado:** [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:04:30Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/README.md) · [40213830995](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995) · [cache-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/cache-s12.md) · [consistencia-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/consistencia-s12.md) · [archivos_legado.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/backend/app/archivos_legado.py) · [issues?state=all&per_page=100](https://api.github.com/repos/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/issues?state=all&per_page=100) · [pulls?state=all&sort=updated&direction=desc&per_page=30](https://api.github.com/repos/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pulls?state=all&sort=updated&direction=desc&per_page=30) · [runs?per_page=15](https://api.github.com/repos/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs?per_page=15)

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [31932f0006542c6f3f6222071bb1a9c36b6f888a](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/31932f0006542c6f3f6222071bb1a9c36b6f888a), fecha del commit 2026-10-26T06:03:01Z (UTC).

Sin cambios de punta ni README desde el 29/oct. Se conserva la evidencia exacta de 78 pruebas en tests/ sobre PostgreSQL 16 aislado y despliegue con migraciones/reinicio exitosos; no vuelve a presentarse como vigente el bloqueo Alembic ya corregido. El comando excluye app/tests/ y no prueba todo el cliente. Persisten notificador simulado, worker de operación separada, caché propuesta y precaución por fallback destructivo a DATABASE_URL fuera de CI.

**Próximos pasos:**
- Eliminar el fallback destructivo a DATABASE_URL o exigir validación inequívoca de BD de pruebas antes de drop_all.
- Documentar y verificar operación del worker y notificación real si se pretende incluirla en el despliegue; conservar el alcance tests/ de CI.
- Publicar URL exacta institucional en README y validar los flujos nuevos del cliente; no presentar caché propuesta como activa.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README raíz sin endpoint público vigente. Solo en código: https://129-80-171-141.nip.io; release APK v1.0.2 publicado, no prueba de sitio institucional.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/4): fusionada 2026-10-26T04:35:44Z; [#3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/3): fusionada 2026-10-25T18:20:31Z; [#2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/2): fusionada 2026-10-06T06:08:06Z.

**CI consultado:** [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926): success (misma punta); [Release APK](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132197969): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:04:30Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/README.md) · [40278118926](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926) · [40132197969](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132197969) · [limites-del-experimento.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/mensajeria/limites-del-experimento.md) · [conftest.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/tests/conftest.py) · [consistencia-por-operacion.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/datos/consistencia-por-operacion.md) · [issues?state=all&per_page=100](https://api.github.com/repos/ISCOUTB/AS_202620_UTB_TRACKER/issues?state=all&per_page=100) · [pulls?state=all&sort=updated&direction=desc&per_page=30](https://api.github.com/repos/ISCOUTB/AS_202620_UTB_TRACKER/pulls?state=all&sort=updated&direction=desc&per_page=30) · [runs?per_page=15](https://api.github.com/repos/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs?per_page=15)

<a id="uniteam"></a>

## uniTeam

Rama **master**, [0a44bd5a8d9374423b08fef87e46672cd6ad501b](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/0a44bd5a8d9374423b08fef87e46672cd6ad501b), fecha del commit 2026-10-26T00:55:53Z (UTC).

Sin cambios de punta ni README desde el 29/oct. El cron del 30/oct vuelve a fallar seis comprobaciones, pero sus logs consultan las direcciones Render antiguas y no DuckDNS publicado en README. No demuestra caída del despliegue actual. Se mantienen taller SQLite aislado de la API/auditoría, MySQL como fuente de verdad y política de caché propuesta, no habilitada.

**Próximos pasos:**
- Actualizar la sonda de despliegue para comprobar las direcciones DuckDNS vigentes y repetir sus seis casos antes de interpretar salud.
- Conservar la distinción entre taller SQLite aislado y API real; implementar y medir la política de caché si se adopta.
- Publicar frontend y API bajo iscoutb.dev.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Externo. Frontend y API DuckDNS. Sonda sigue consultando Render; su fallo no determina disponibilidad de DuckDNS.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/4): fusionada 2026-10-04T21:23:33Z; [#2](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/2): fusionada 2026-09-14T01:20:18Z; [#10](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/10): fusionada 2026-10-26T00:55:53Z; [#9](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/9): fusionada 2026-10-26T00:55:34Z; [#8](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/8): fusionada 2026-10-23T05:15:01Z.

**CI consultado:** [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41055680050): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41014571895): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:04:30Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/README.md) · [0015-taller-de-mensajeria-local-aislado.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/adr/0015-taller-de-mensajeria-local-aislado.md) · [0016-conservar-mysql-como-fuente-de-verdad.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/adr/0016-conservar-mysql-como-fuente-de-verdad.md) · [40873650648](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40873650648) · [40829731319](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40829731319) · [40796088035](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40796088035) · [40744900068](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40744900068) · [40251714762](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40251714762) · [issues?state=all&per_page=100](https://api.github.com/repos/ISCOUTB/AS_202620_uniTeam/issues?state=all&per_page=100) · [pulls?state=all&sort=updated&direction=desc&per_page=30](https://api.github.com/repos/ISCOUTB/AS_202620_uniTeam/pulls?state=all&sort=updated&direction=desc&per_page=30) · [runs?per_page=15](https://api.github.com/repos/ISCOUTB/AS_202620_uniTeam/actions/runs?per_page=15) · [41055680050](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41055680050) · [41014571895](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41014571895)

<a id="xald"></a>

## XALD

Rama **master**, [1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00](https://github.com/ISCOUTB/AS_202620_XALD/commit/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00), fecha del commit 2026-10-26T04:04:58Z (UTC).

Sin cambios respecto al 29/oct: master, README y experimental conservan las mismas puntas. La actividad lateral documental ya reportada no está integrada en master ni cuenta como implementación nueva. Se mantiene CI exitoso en master y experimental, con deploy-backend omitido en esta última. Siguen pendientes activar y verificar procesarPendientes en operación real, persistir cola y deduplicación y validar el recorrido en dispositivo; pruebas y health no bastan para acreditarlo.

**Próximos pasos:**
- Conciliar la documentación de experimental con master antes de proponer integración: evitar reintroducir descripciones obsoletas del cliente HTTP y mantener las mitigaciones pendientes explícitas.
- Conectar procesarPendientes a un ejecutor real con conectividad y persistir cola/marcas antes de prometer entrega tras reinicios.
- Completar referencias de commit/run en evidencia y distinguir E2E local del funcionamiento en dispositivo/Render.
- Publicar el endpoint bajo iscoutb.dev y verificar persistencia y sincronización de extremo a extremo.

**Issues GitHub:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. Motivos: 5 completed; 1 duplicate.

**README:** Externo. Backend Render. El CI incluye paso de health exitoso; no es verificación funcional propia ni evidencia de frontend institucional.

**PR consultadas:** [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z; [#24](https://github.com/ISCOUTB/AS_202620_XALD/pull/24): fusionada 2026-09-27T16:24:00Z; [#23](https://github.com/ISCOUTB/AS_202620_XALD/pull/23): fusionada 2026-09-20T17:34:35Z; [#22](https://github.com/ISCOUTB/AS_202620_XALD/pull/22): cerrada sin fusión registrada.

**CI consultado:** [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501): success (misma punta); [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40798851273): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:04:30Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/README.md) · [40267222501](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501) · [40250035779](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40250035779) · [limites-del-experimento.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/mensajes/limites-del-experimento.md) · [evidencia.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/mensajes/evidencia.md) · [1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00...7676801c00b935d02a3dac52d3ad06939dba9764](https://github.com/ISCOUTB/AS_202620_XALD/compare/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00...7676801c00b935d02a3dac52d3ad06939dba9764) · [40798851273](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40798851273) · [issues?state=all&per_page=100](https://api.github.com/repos/ISCOUTB/AS_202620_XALD/issues?state=all&per_page=100) · [pulls?state=all&sort=updated&direction=desc&per_page=30](https://api.github.com/repos/ISCOUTB/AS_202620_XALD/pulls?state=all&sort=updated&direction=desc&per_page=30) · [runs?per_page=15](https://api.github.com/repos/ISCOUTB/AS_202620_XALD/actions/runs?per_page=15)

<a id="verifacts"></a>

## Verifacts

Rama **master**, [559612b61ee4cea46cef6d00f857d2e5c2794f03](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/559612b61ee4cea46cef6d00f857d2e5c2794f03), fecha del commit 2026-10-28T05:41:24Z (UTC).

Sin cambios de punta, README, issues ni PR desde el 29/oct. Se conservan los cuatro commits documentales S12/S13 ya reportados, no avances nuevos de hoy: controles SSRF, límites de carga, timeout, protección del historial y TLS pendientes; retención de 30 días y delete_analysis propuestos, no implementados. Sigue pendiente un reporte SCA reproducible; el workflow revisado no ejecuta pip-audit ni npm audit. CI de la misma punta: 66 pruebas, build/smoke de imagen y análisis Sonar exitosos, sin acreditar redespliegue ni nuevo Quality Gate. Los ocho casos HTTP son evidencia aportada previamente por el equipo, no nueva aceptación independiente.

**Próximos pasos:**
- Aportar salidas fechadas de pip-audit y npm audit con revisión y versiones resueltas; reconciliar la tabla SCA y no presentar el análisis Sonar como auditoría de dependencias.
- Implementar y probar los controles de mayor riesgo del modelo de amenazas; marcar retención y supresión como diseño hasta que existan código, operación y evidencia.
- Mantener separadas caché estática activa, propuestas de caché de backend y garantías de SQLite en un nodo; las seis pruebas de consistencia existentes no son código nuevo de este incremento.
- Completar subdominio iscoutb.dev y TLS; conservar trazabilidad de los ocho casos HTTP previos y añadir recorrido de navegador/persistencia si se pretende aceptación integral.

**Issues GitHub:** 0 abiertas / 3 cerradas; 0 abiertas sin asignar. Motivos: 3 completed.

**README:** Externo. Referencia HTTP sslip. README declara pendiente dominio institucional/certificado; frontend / y API /docs,/health separados conceptualmente.

**CI consultado:** [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382): success (misma punta); [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-30T13:04:30Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/README.md) · [40639475382](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382) · [40639475319](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319) · [entrega-consistencia-cache-costo-reversion.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/docs/entregas/entrega-consistencia-cache-costo-reversion.md) · [entrega-seguridad-amenazas-dependencias-privacidad.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/docs/entregas/entrega-seguridad-amenazas-dependencias-privacidad.md) · [tests.yml](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/.github/workflows/tests.yml) · [service.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/app/modules/content/service.py) · [repository.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/app/persistence/repository.py) · [evidencia-aceptacion.txt](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/evidencia-aceptacion.txt) · [issues?state=all&per_page=100](https://api.github.com/repos/ISCOUTB/AS_202620_Verifacts/issues?state=all&per_page=100) · [pulls?state=all&sort=updated&direction=desc&per_page=30](https://api.github.com/repos/ISCOUTB/AS_202620_Verifacts/pulls?state=all&sort=updated&direction=desc&per_page=30) · [runs?per_page=15](https://api.github.com/repos/ISCOUTB/AS_202620_Verifacts/actions/runs?per_page=15)

