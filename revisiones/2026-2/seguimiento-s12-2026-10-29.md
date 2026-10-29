# Seguimiento de los 23 proyectos · 29 de octubre de 2026

Consulta del **29 de octubre de 2026**, con observaciones fechadas por proyecto (UTC), sobre los 23 proyectos del listado vigente. Seguimiento documental, no recalificación. **No se cierra S12 automáticamente** ni se recalifica con este seguimiento. Se conservan calificaciones, planillas, matrices y cortes históricos.

**43 abiertas y 132 cerradas** (131 completed; 1 duplicate); 19 abiertas sin asignar. Pull requests excluidas.

README: **10 con algún endpoint institucional; 6 con enlaces externos; 7 sin URL pública concreta**. Las direcciones institucionales incluyen APIs, no prueban que toda interfaz esté publicada.

Se conservan las confirmaciones del docente: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. Estas declaraciones no son pruebas funcionales automatizadas de este corte.

Se leyeron repositorios y resultados de GitHub sin ejecutar código estudiantil ni modificar sus issues o despliegues. Código fusionado, CI, publicación y aceptación funcional son evidencias distintas. No se repitieron pruebas funcionales en vivo. El conector disponible no expone estados personalizados de GitHub Projects; no se obtuvieron estados del tablero; OPEN/CLOSED y motivos de cierre pertenecen a issues, no a columnas de tablero.

[Issues y motivos de cierre](seguimiento-issues-2026-10-29.md) · [README y despliegues](seguimiento-despliegues-2026-10-29.md) · [Corte anterior](seguimiento-s12-2026-10-28.md)

## Cambios respecto al corte anterior

- **ElMapita**: Añade configuración reproducible de Dokploy en deploy/compose.lab.yaml, ejemplo de variables y exclusión de deploy/.env. El Compose despliega solo la API NestJS, no Flutter, y mantiene Supabase externo; el dominio institucional que figura como FRONTEND_URL es configuración y no acredita un frontend ni despliegue activo. El README sigue sin URL pública concreta. El nuevo CI global figura exitoso: confirma 56 pruebas unitarias backend y construcción de imagen, pero el E2E GET / vuelve a fallar (404 frente a 200 esperado) y el workflow neutraliza su error con echo. SonarCloud falla por autorización/proyecto no encontrado y omite su Quality Gate; no bloquea el resultado global. Se conserva la confirmación docente de que ElMapita presentó y funciona, sin atribuirla a esta nueva punta ni a una verificación en vivo de este corte.
- **LaPlacita**: Integra PR #24 y un complemento posterior: controles de sesión/rol en escrituras de tienda y notificaciones, auditoría de dependencias, aviso de privacidad, procedimiento de rotación documentado y decisión explícita de no implementar ETag ni LISTEN/NOTIFY con una instancia. El CI actual pasa sus cinco jobs. El workflow de despliegue también figura success, pero el log del webhook responde «Branch Not Match» antes de comprobar health=200: esa salud no identifica el commit servido y NO acredita redespliegue de la revisión. Las comprobaciones HTTP y de interfaz descritas por el equipo son locales, no aceptación independiente de producción. README continúa sin URL pública vigente concreta. Las PR de dependencias abiertas no son cambios fusionados.
- **PideUtb**: PR #30–34 ya fusionadas: catálogo y carrito multiproducto, promociones, migraciones 004–007, contrato 4.0.0 y autorización de consulta; se publica el estado del intento de pago para distinguir rechazo de espera, por lo que la limitación R-11 descrita antes queda corregida en código. También se integran radios accesibles, validación de URL de pasarela y revalidación de caché/tema claro. El CI de la punta acredita 454 pruebas aprobadas y tres omitidas; las 103 pruebas focalizadas PostgreSQL son un subconjunto reejecutado, no casos adicionales. PR32 aún señala configuración incorrecta del panel: la fusión no demuestra que se haya corregido ni activado el simulador. PR34 documenta servicios legados activos con riesgo de autorización reportado por el equipo, sin exposición efectiva de datos comprobada en este seguimiento; la corrección del repositorio actual no demuestra retiro o mitigación del legado. No se sondearon esos servicios. Los recorridos de navegador son reportes del equipo, no validación independiente ni aceptación de cobros reales. Se conserva presentación y despliegues confirmados por docente.
- **Recobra**: Incorpora seguridad S13: límites de uso, CSP y CORS, tratamiento del origen detrás de Cloudflare, auditoría y avisos operativos, controles de dependencias/secretos y documentación de privacidad que reconoce a Cloudflare. Los seis jobs de la punta pasan; los logs backend acreditan 215 pruebas unitarias, 124 e2e y 10 de contrato. La auditoría verde no significa ausencia de vulnerabilidades: acepta 13 avisos individuales con alcance documentado y vencimiento al 15/dic, mientras npm informa siete paquetes afectados de producción. Los ajustes observados en producción son reportes del equipo, no pruebas repetidas por este seguimiento. Siguen pendientes acciones operativas de protección/rotación y respaldo programado descritas por el equipo; CI no demuestra que se hayan ejecutado. Las diez PR nuevas de Dependabot están abiertas, no fusionadas. README conserva vitrina, Flutter Web y API institucionales. Se mantiene presentación confirmada por docente.
- **XALD**: La rama principal master y su README permanecen sin cambios desde el 28/oct, con CI exacto exitoso. Como actividad lateral, experimental recibió una resolución de conflicto el 29/oct; el compare contra master muestra diferencias solo en dos documentos arc42 de riesgos/fallos de integración, no nueva implementación. El CI de esa rama pasa backend, módulos Android y contrato; deploy-backend está omitido. No hay PR abierta ni integración de este delta en master, por lo que no se presenta como entrega principal ni redespliegue. Sigue pendiente activar y verificar procesarPendientes en operación real, con persistencia de cola/deduplicación; el envío disparado en pruebas y un health exitoso no acreditan el recorrido completo en dispositivo.

Los demás proyectos fueron revalidados; sin novedades sustantivas se conserva su feedback individual anterior, sin añadir secciones repetidas.

<a id="audioshare"></a>

## AudioShare

Rama **master**, [8de5ac1daacd189b38d732a0d3d2e916ee29a281](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/8de5ac1daacd189b38d732a0d3d2e916ee29a281), fecha del commit 2026-10-26T04:47:47Z (UTC).

Revalidación del 29/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 28/oct. Integra PR7 y PR9: decisiones de persistencia/consistencia y prototipo aislado de sincronización por mensajes, con deduplicación, reintentos y DLQ volátiles. El CI de Node y la publicación de imagen pasan; Flutter falla en analyze, por lo que sus pruebas y build web quedan omitidos. El README ahora dice que Docker compila Flutter Web, pero también reporta que el dominio aún sirve el cliente legado y /rooms devuelve 404: es observación del equipo, no prueba independiente de este corte; publicar imagen no acredita redespliegue.

**Próximos pasos:**
- Corregir flutter analyze y repetir pruebas/build del mismo commit.
- Redesplegar y verificar /rooms, cliente Flutter y recorrido real; conservar límites del simulador volátil.

**Issues GitHub:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar. Motivos: 2 completed.

**README:** Institucional. Mismo origen institucional para API/cliente; el equipo reporta que todavía sirve legado y requiere redespliegue. La imagen nueva no prueba activación.

**PR consultadas:** [#9](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/9): fusionada 2026-10-26T04:47:48Z; [#8](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/7): fusionada 2026-10-26T03:42:05Z; [#2](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/2): fusionada 2026-09-01T14:56:35Z; [#1](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/1): fusionada 2026-08-31T03:06:48Z.

**CI consultado:** [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898215): failure (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898219): success (misma punta); [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898269): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:08:07.788Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/README.md) · [evidencia-taller-mensajeria.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/docs/evidencia-taller-mensajeria.md) · [README.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/experiments/messaging-prototype/README.md) · [package.json](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8de5ac1daacd189b38d732a0d3d2e916ee29a281/package.json) · [40270898269](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898269) · [40270898219](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898219) · [40270898215](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/40270898215)

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, [7c7200f1d2669a0dd63cb7fa0b3587135357b78c](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7c7200f1d2669a0dd63cb7fa0b3587135357b78c), fecha del commit 2026-10-26T05:40:17Z (UTC).

Revalidación del 29/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 28/oct. Corrige el operador Python inválido señalado en el corte previo y ahora pasa Idempotency-Key al caso de uso/repositorio PostgreSQL de publicaciones, en lugar de ignorarlo. Añade recursos/feed y prototipo de mensajería con outbox en memoria. Persisten almacenamiento/comparación directa de contraseña sin hash y secreto JWT predeterminado; no se reproduce su valor. La búsqueda de idempotencia no compara autor ni payload antes de devolver una publicación previa: revisar alcance y conflicto de claves. Los dos workflows actuales siguen fallando sin jobs disponibles; no se demuestra que las pruebas hayan corrido. README actualizado afirma despliegue HTTPS, pero no publica una URL concreta.

**Próximos pasos:**
- Usar hash de contraseñas y rechazar arranque inseguro sin configuración JWT.
- Aislar claves de idempotencia por autor/operación, validar payload y probar duplicados concurrentes/conflictivos.
- Resolver workflows fallidos y publicar URL exacta de frontend/API en README.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. Declara HTTPS/Dokploy, pero sin URL pública concreta del sitio en README.

**PR consultadas:** [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3): fusionada 2026-10-05T05:46:36Z; [#2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2): fusionada 2026-09-21T04:56:52Z; [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta.

**CI consultado:** [.github/workflows/backend-tests.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275481686): failure (misma punta); [.github/workflows/contrato.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275480682): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:08:07.683Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/README.md) · [auth_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/inbound/api/auth_router.py) · [publicacion_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/inbound/api/publicacion_router.py) · [crear_publicacion.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/application/use_cases/crear_publicacion.py) · [publicacion_repository.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/outbound/postgres/publicacion_repository.py) · [outbox.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/backend/src/linkclub/adapters/outbound/messaging/outbox.py) · [40275481686](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275481686) · [40275480682](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275480682)

<a id="dinamikutb"></a>

## DinamikUTB

Rama **master**, [822baaa371ec94827d09319a09e13f11f7123f64](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/822baaa371ec94827d09319a09e13f11f7123f64), fecha del commit 2026-10-27T17:08:57Z (UTC).

Revalidación del 29/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 28/oct. Integra nuevas pantallas administrativas, currículo y gestión de cuentas, además de imagen Flutter/Nginx para el laboratorio. El README de frontend separa https://dinamikutb.iscoutb.dev (web) y https://api.dinamikutb.iscoutb.dev (API), sujetos a aprovisionamiento; ADR0006 marca GitHub Pages como reemplazado. El README raíz sigue describiendo el primer dominio como API y conserva enlaces anteriores: hay desalineación documental. Publicar la imagen GHCR termina correctamente, pero no acredita redeploy en Dokploy. CI de la misma punta falla: pytest no recolecta por ImportError de RequisitoPrograma; Flutter registra 20 pruebas aprobadas y cuatro fallidas (tres de validación de correo y una de registro de estudiantes); SonarCloud queda omitido. Los routers nuevos de currículo, programas y reportes no se incorporan en app/main.py consultado; su existencia no demuestra rutas disponibles. No se verificó funcionamiento en vivo.

**Próximos pasos:**
- Resolver el ImportError de RequisitoPrograma y las cuatro pruebas Flutter; repetir CI en la misma punta.
- Integrar y probar los routers nuevos antes de afirmar disponibilidad de currículo, programas y reportes.
- Unificar README raíz y frontend con los dominios realmente provisionados; distinguir API/web, retirar referencias vigentes obsoletas y acreditar redeploy Dokploy con recorrido funcional.

**Issues GitHub:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. README raíz y frontend discrepan en roles/dominios. GHCR acredita imagen, no despliegue ni DNS/TLS o aceptación; no se prescribe recrear la base antigua de Render.

**PR consultadas:** [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35): cerrada sin fusión registrada; [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37): fusionada 2026-10-23T03:04:11Z; [#36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36): fusionada 2026-10-23T01:01:46Z; [#33](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/33): fusionada 2026-09-27T17:38:37Z; [#32](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/32): fusionada 2026-09-22T03:51:10Z; [#31](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/31): fusionada 2026-09-22T03:16:20Z; [#30](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/30): fusionada 2026-09-21T18:41:30Z; [#29](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/29): fusionada 2026-09-21T17:48:40Z; [#12](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/12): fusionada 2026-09-07T04:26:25Z; [#11](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/11): fusionada 2026-09-07T03:57:51Z; [#10](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/10): fusionada 2026-08-31T18:47:14Z; [#9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/9): fusionada 2026-08-31T18:32:43Z; [#8](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/8): fusionada 2026-08-31T05:11:21Z; [#7](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/7): fusionada 2026-08-31T04:52:24Z; [#6](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/6): fusionada 2026-08-31T04:21:48Z; [#5](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/5): fusionada 2026-08-31T03:00:17Z; [#4](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/4): fusionada 2026-08-24T03:26:31Z; [#3](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/3): fusionada 2026-08-24T03:10:21Z; [#2](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/2): fusionada 2026-08-24T02:31:51Z; [#1](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/1): fusionada 2026-08-24T02:02:03Z.

**CI consultado:** [Publish frontend image](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40549937090): success (misma punta); [Publish frontend image](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831470): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831321): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:08:07.486Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/README.md) · [evidencia-s12.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/evidencia-s12.md) · [11-risks-and-technical-debt.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/arc42/11-risks-and-technical-debt.md) · [0012-despliegue-en-servidor-del-laboratorio.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/adr/0012-despliegue-en-servidor-del-laboratorio.md) · [40549937090](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40549937090) · [40547831321](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831321) · [README.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/frontend/README.md) · [0006-plataforma-despliegue-frontend.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/adr/0006-plataforma-despliegue-frontend.md) · [main.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/backend/app/main.py) · [publish-frontend-image.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/.github/workflows/publish-frontend-image.yml)

<a id="drift"></a>

## Drift

Rama **master**, [d9a181630f9c7cc9daf3d58705092b245cdc7c73](https://github.com/ISCOUTB/AS_202620_Drift/commit/d9a181630f9c7cc9daf3d58705092b245cdc7c73), fecha del commit 2026-10-25T22:37:33Z (UTC).

Revalidación del 29/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 28/oct. PR32 integrado: actualiza S12, ADR0010, arc42 y C4 con almacenamiento de navegador y ausencia de brokers; explicita costo de reversión de datos. CI y despliegue Azure ejecutados con éxito para la punta actual. Esto no convierte las mediciones simuladas previas en rendimiento real ni acredita aceptación funcional en el dominio institucional.

**Próximos pasos:**
- Validar recorrido real en el despliegue institucional y conservar evidencias separadas de Azure.
- Repetir mediciones relevantes con dependencias reales y distinguir decisiones de datos de implementación.

**Issues GitHub:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. Frontend y API /api; API alternativa; Frontend alternativo

**PR consultadas:** [#32](https://github.com/ISCOUTB/AS_202620_Drift/pull/32): fusionada 2026-10-25T22:37:33Z; [#31](https://github.com/ISCOUTB/AS_202620_Drift/pull/31): fusionada 2026-10-21T04:53:32Z; [#30](https://github.com/ISCOUTB/AS_202620_Drift/pull/30): fusionada 2026-10-19T03:20:50Z; [#29](https://github.com/ISCOUTB/AS_202620_Drift/pull/29): fusionada 2026-10-19T03:07:18Z; [#28](https://github.com/ISCOUTB/AS_202620_Drift/pull/28): fusionada 2026-10-19T02:08:58Z; [#27](https://github.com/ISCOUTB/AS_202620_Drift/pull/27): fusionada 2026-10-12T19:42:41Z; [#26](https://github.com/ISCOUTB/AS_202620_Drift/pull/26): fusionada 2026-10-12T19:15:32Z; [#25](https://github.com/ISCOUTB/AS_202620_Drift/pull/25): fusionada 2026-10-12T04:49:54Z; [#24](https://github.com/ISCOUTB/AS_202620_Drift/pull/24): fusionada 2026-10-11T05:28:23Z; [#23](https://github.com/ISCOUTB/AS_202620_Drift/pull/23): fusionada 2026-10-11T05:21:57Z; [#22](https://github.com/ISCOUTB/AS_202620_Drift/pull/22): fusionada 2026-10-11T04:53:50Z; [#21](https://github.com/ISCOUTB/AS_202620_Drift/pull/21): fusionada 2026-10-11T03:47:58Z.

**CI consultado:** [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:08:07.536Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/d9a181630f9c7cc9daf3d58705092b245cdc7c73/README.md) · [40241076074](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074) · [40241076067](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067)

<a id="elmapita"></a>

## ElMapita

Rama **main**, [ddcfbbcfacaff506d587dad60c06a744fe7f66ae](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/ddcfbbcfacaff506d587dad60c06a744fe7f66ae), fecha del commit 2026-10-28T22:35:38Z (UTC).

Añade configuración reproducible de Dokploy en deploy/compose.lab.yaml, ejemplo de variables y exclusión de deploy/.env. El Compose despliega solo la API NestJS, no Flutter, y mantiene Supabase externo; el dominio institucional que figura como FRONTEND_URL es configuración y no acredita un frontend ni despliegue activo. El README sigue sin URL pública concreta. El nuevo CI global figura exitoso: confirma 56 pruebas unitarias backend y construcción de imagen, pero el E2E GET / vuelve a fallar (404 frente a 200 esperado) y el workflow neutraliza su error con echo. SonarCloud falla por autorización/proyecto no encontrado y omite su Quality Gate; no bloquea el resultado global. Se conserva la confirmación docente de que ElMapita presentó y funciona, sin atribuirla a esta nueva punta ni a una verificación en vivo de este corte.

**Próximos pasos:**
- Publicar en README la URL institucional exacta y distinguir API NestJS de frontend Flutter; validar el dominio y hash realmente desplegados, no inferirlos del ejemplo de variables.
- Corregir el E2E y hacer bloqueantes las verificaciones necesarias; resolver acceso/configuración de SonarCloud y acreditar su Quality Gate.
- Conservar explícitos los límites de mensajería en memoria y reconciliación, sin presentarlos como outbox o broker durable.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta. Compose nuevo solo para API; FRONTEND_URL en configuración no prueba frontend ni despliegue activo. Se conserva aceptación docente previa, distinta de la publicación de esta punta.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40781174318): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:08:07.694Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/ddcfbbcfacaff506d587dad60c06a744fe7f66ae/README.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/ddcfbbcfacaff506d587dad60c06a744fe7f66ae/deploy/compose.lab.yaml) · [ci.yml](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/ddcfbbcfacaff506d587dad60c06a744fe7f66ae/.github/workflows/ci.yml) · [40781174318](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40781174318) · [123142939572](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40781174318/job/123142939572) · [123143208608](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40781174318/job/123143208608)

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), fecha del commit 2026-10-26T03:57:38Z (UTC).

Revalidación del 29/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 28/oct. PR3 integra documentación de consistencia y prototipo aislado de envío automático de invitaciones, con proveedor simulado, deduplicación, reintentos y DLQ en memoria. Su workflow específico ejecuta pruebas y demo con éxito; no envía correos reales ni integra Flask/BD/Dokploy. El CI general ahora falla al recolectar test_simulador.py por import relativo sin paquete reconocido, no por el error DATABASE_URL del corte anterior; contrato y Docker quedan omitidos. Pages publica documentación estática, no aceptación de la API. README mantiene host pendiente, sin URL pública concreta.

**Próximos pasos:**
- Corregir empaquetado/import del prototipo para que pytest general pueda recolectarlo y repetir contrato/build.
- Mantener separada evidencia de correo simulado de envío real; definir persistencia/proveedor antes de integrar.
- Documentar URL institucional concreta y alcance de rutas PostgreSQL frente a las heredadas en memoria.

**Issues GitHub:** 1 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

**PR consultadas:** [#3](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/3): fusionada 2026-10-26T03:57:38Z; [#2](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/2): fusionada 2026-09-28T02:39:59Z.

**CI consultado:** [Taller mensajes y consistencia](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): failure (misma punta); [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:08:07.395Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/talleres/mensajes-consistencia/README.md) · [ci.yml](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/.github/workflows/ci.yml) · [40266609521](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521) · [40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410) · [40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284)

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, [5fa232b25e3122474291e5cc41ead96f9b567856](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/5fa232b25e3122474291e5cc41ead96f9b567856), fecha del commit 2026-10-26T04:21:32Z (UTC).

Revalidación del 29/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 28/oct. Integra S12/ADR0006 y taller asíncrono aislado. El run actual pasa 12 pruebas base, 11 de contrato y nueve de mensajería, además de auditorías de arquitectura y dependencias; el fallo antiguo de auditoría está superado. La cola, deduplicación y DLQ son volátiles y el endpoint de aforo permanece síncrono; caché/event-log son diseños, no integración productiva. El workflow no configura PostgreSQL ni ejecuta su prueba específica: no atribuirle validación de esa base. README sigue describiendo backend institucional.

**Próximos pasos:**
- Ejecutar integración PostgreSQL con base aislada y evidenciar el recorrido Flutter/API.
- Conservar límites del prototipo y no afirmar durabilidad, broker ni caché operativa a partir del diseño.

**Issues GitHub:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend; interfaz Flutter pública no acreditada

**PR consultadas:** [#18](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/18): fusionada 2026-10-26T00:15:00Z; [#17](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/17): fusionada 2026-10-19T01:09:26Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:08:07.442Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/README.md) · [limites-experimento.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/docs/taller-mensajeria/limites-experimento.md) · [evidencia-pruebas.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/docs/taller-mensajeria/evidencia-pruebas.md) · [ci.yml](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/.github/workflows/ci.yml) · [40268686360](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360)

<a id="inventrack"></a>

## InvenTrack

Rama **main**, [972a12775ffc073a1efe9e6c9435be497c5187d6](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/972a12775ffc073a1efe9e6c9435be497c5187d6), fecha del commit 2026-10-27T21:37:20Z (UTC).

Revalidación del 29/oct: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al corte del 28/oct. Corrige la brecha de idempotencia HTTP: reserva/serializa la clave antes de modificar stock, conserva fingerprint y resultado, devuelve replay sin nuevo movimiento/evento y responde 409 ante payload incompatible. ADR0017 explicita almacenamiento volátil por proceso y la ventana stock/publicación sin outbox. El CI de la punta actual pasa 32 pruebas y vuelve a ejecutar una prueba de contrato incluida en el conjunto, no 33 pruebas distintas; el scanner Sonar termina, sin acreditar por sí solo Quality Gate. La nueva evidencia de despliegue del equipo reporta que el 27/oct no pudo resolver DNS/TLS institucional y obtuvo 503 en /health y /metrics de Render. Esto entra en tensión con las declaraciones anteriores de despliegue/verificación del README. Son observaciones del equipo, no una prueba independiente actual ni demostración de inexistencia de despliegue; falta publicar/verificar esta punta en servicio. El documento de CI cita todavía la revisión anterior.

**Próximos pasos:**
- Actualizar evidencia de CI al run actual y vincular Quality Gate al análisis correspondiente.
- Acreditar hash desplegado, /health, /metrics y recorrido funcional institucional; distinguir API de frontend.
- Mantener explícitos límites de idempotencia en memoria, reinicios y varias réplicas; adoptar registro/outbox durable cuando se requiera recuperación.

**Issues GitHub:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: 7 completed.

**README:** Institucional. README conserva API institucional y alternativa Render. Evidencia del equipo del 27/oct reporta DNS/TLS institucional no verificable y 503 en health/metrics de Render; no es comprobación independiente del corte. Hay que reconciliar ese reporte con las declaraciones previas de despliegue/verificación del README.

**CI consultado:** [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40588329661): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:08:10.152Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/README.md) · [evidencia-mensajeria-s12.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/evidencia-mensajeria-s12.md) · [0015-completar-decision-de-almacenamiento-y-reversion.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/adr/0015-completar-decision-de-almacenamiento-y-reversion.md) · [registrar_movimiento.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/app/inventario/application/registrar_movimiento.py) · [router.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/app/inventario/infrastructure/router.py) · [0016-integrar-eventos-de-auditoria-en-movimientos.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/adr/0016-integrar-eventos-de-auditoria-en-movimientos.md) · [40588329661](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40588329661) · [evidencia-despliegue-s12.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/evidencia-despliegue-s12.md) · [0017-idempotencia-http-en-comandos-de-inventario.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/adr/0017-idempotencia-http-en-comandos-de-inventario.md) · [idempotency.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/app/inventario/infrastructure/idempotency.py)

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [15af0876468939cc2de6e6d1298cfdddae32972f](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/15af0876468939cc2de6e6d1298cfdddae32972f), fecha del commit 2026-10-28T19:19:31Z (UTC).

Integra PR #24 y un complemento posterior: controles de sesión/rol en escrituras de tienda y notificaciones, auditoría de dependencias, aviso de privacidad, procedimiento de rotación documentado y decisión explícita de no implementar ETag ni LISTEN/NOTIFY con una instancia. El CI actual pasa sus cinco jobs. El workflow de despliegue también figura success, pero el log del webhook responde «Branch Not Match» antes de comprobar health=200: esa salud no identifica el commit servido y NO acredita redespliegue de la revisión. Las comprobaciones HTTP y de interfaz descritas por el equipo son locales, no aceptación independiente de producción. README continúa sin URL pública vigente concreta. Las PR de dependencias abiertas no son cambios fusionados.

**Próximos pasos:**
- Corregir la selección de rama del webhook y aportar evidencia de que Dokploy sirve esta revisión; validar controles y cabeceras en el entorno objetivo.
- Documentar en README las URL exactas de frontend y API bajo iscoutb.dev; no reutilizar el enlace Azure retirado.
- Completar límites de uso, protección de secretos, constancia/versionado del consentimiento y reconciliar privacidad con el flujo real; el procedimiento de rotación escrito no es un ensayo ejecutado.

**Issues GitHub:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. Motivos: 14 completed.

**README:** Sin URL concreta. Solo Azure explícitamente retirado; ninguna URL pública vigente concreta en README raíz.

**PR consultadas:** [#29](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/29): abierta; [#19](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/19): cerrada sin fusión registrada; [#23](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/23): abierta; [#21](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/21): abierta; [#22](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/22): cerrada sin fusión registrada; [#28](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/28): abierta; [#18](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/18): cerrada sin fusión registrada; [#27](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/27): abierta; [#26](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/26): abierta; [#25](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/25): abierta; [#24](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/24): fusionada 2026-10-28T15:28:19Z; [#20](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/20): abierta; [#17](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/16): abierta; [#15](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/15): fusionada 2026-10-22T19:07:22Z.

**CI consultado:** [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40753448484): success (misma punta); [Deploy Dokploy (laboratorio de la U)](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40753448422): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:23.723Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/15af0876468939cc2de6e6d1298cfdddae32972f/README.md) · [40753448484](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40753448484) · [40753448422](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40753448422) · [24](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/24) · [evidencias-s13.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/15af0876468939cc2de6e6d1298cfdddae32972f/docs/evidencias/evidencias-s13.md) · [123045949069](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40753448422/job/123045949069)

<a id="lostvault"></a>

## LostVault

Rama **main**, [3a6e157110bd3c63e76de9cce68c63991e747468](https://github.com/ISCOUTB/AS_202620_LostVault/commit/3a6e157110bd3c63e76de9cce68c63991e747468), fecha del commit 2026-10-26T04:46:40Z (UTC).

Revalidación del 29/oct: misma punta y README que el corte anterior. Continúan integradas PR #20 y #22: Cache-Control, expiración JWT en backend/main.py y taller aislado de outbox SQLite, deduplicación y reintentos. Los tres workflows de la misma punta siguen exitosos; se conserva el alcance previamente verificado de 27 pruebas backend y 18 del taller, no cobertura de la implementación separada api/. PostgreSQL/outbox productivos siguen propuestos y el backend conserva memoria. PR #21 continúa abierta; README sigue sin URL pública concreta.

**Próximos pasos:**
- Conectar persistencia y eventos al flujo real solo tras implementar y validar PostgreSQL; mantener explícito que el taller SQLite no es mensajería productiva.
- Añadir cobertura de api/ o aclarar cuál implementación se despliega; publicar frontend/API institucionales y comprobar autorización y consistencia multiinstancia.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de trabajo o despliegue.

**PR consultadas:** [#21](https://github.com/ISCOUTB/AS_202620_LostVault/pull/21): abierta; [#22](https://github.com/ISCOUTB/AS_202620_LostVault/pull/22): fusionada 2026-10-26T04:46:41Z; [#20](https://github.com/ISCOUTB/AS_202620_LostVault/pull/20): fusionada 2026-10-26T01:52:55Z; [#19](https://github.com/ISCOUTB/AS_202620_LostVault/pull/19): fusionada 2026-10-20T16:16:34Z; [#18](https://github.com/ISCOUTB/AS_202620_LostVault/pull/18): fusionada 2026-10-19T01:43:15Z; [#17](https://github.com/ISCOUTB/AS_202620_LostVault/pull/17): fusionada 2026-10-19T01:32:11Z; [#16](https://github.com/ISCOUTB/AS_202620_LostVault/pull/16): fusionada 2026-10-05T03:30:54Z; [#15](https://github.com/ISCOUTB/AS_202620_LostVault/pull/15): fusionada 2026-10-05T02:31:39Z; [#14](https://github.com/ISCOUTB/AS_202620_LostVault/pull/14): fusionada 2026-10-05T00:42:49Z; [#13](https://github.com/ISCOUTB/AS_202620_LostVault/pull/13): fusionada 2026-09-28T04:39:31Z; [#12](https://github.com/ISCOUTB/AS_202620_LostVault/pull/12): fusionada 2026-09-28T03:17:55Z; [#11](https://github.com/ISCOUTB/AS_202620_LostVault/pull/11): cerrada sin fusión registrada; [#10](https://github.com/ISCOUTB/AS_202620_LostVault/pull/10): fusionada 2026-09-21T04:55:35Z; [#9](https://github.com/ISCOUTB/AS_202620_LostVault/pull/9): fusionada 2026-09-13T23:43:59Z; [#8](https://github.com/ISCOUTB/AS_202620_LostVault/pull/8): fusionada 2026-09-13T18:41:09Z.

**CI consultado:** [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589): success (misma punta); [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466): success (misma punta); [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:23.723Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/README.md) · [40270806589](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589) · [40270806466](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466) · [40270806424](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424) · [taller-mensajeria.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/docs/mensajeria/taller-mensajeria.md)

<a id="mapsutb"></a>

## mapsutb

Rama **master**, [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), fecha del commit 2026-10-25T14:04:14Z (UTC).

Revalidación del 29/oct: misma punta y README que el corte anterior. La sonda programada más reciente y la sincronización de hallazgos de Sonar terminan exitosamente para la misma punta. Se conserva la evidencia previa de publicación Firebase del commit que fijó firebase-tools 15.34.0; no es una nueva aceptación manual ni un nuevo despliegue. README sigue en mapsutb.web.app, fuera de iscoutb.dev; no confundir con ElMapita.

**Próximos pasos:**
- Mantener la evidencia del arreglo y los cierres; verificar comportamiento de recarga/reintento del grafo con escenarios reproducibles.
- Publicar frontend bajo iscoutb.dev y actualizar README; distinguir disponibilidad de sonda de aceptación del recorrido funcional.

**Issues GitHub:** 0 abiertas / 54 cerradas; 0 abiertas sin asignar. Motivos: 54 completed.

**README:** Externo. Frontend Firebase externo; sonda CI disponible, sin nueva aceptación funcional propia.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z.

**CI consultado:** [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40874157867): success (misma punta); [Sincronizar hallazgos de Sonar a GitHub Issues](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40872245102): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:23.723Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [40874157867](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40874157867) · [40872245102](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40872245102)

<a id="pideutb"></a>

## PideUtb

Rama **master**, [70a98045f2effa9830ffb7c55199cb0cf7d13ccf](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/70a98045f2effa9830ffb7c55199cb0cf7d13ccf), fecha del commit 2026-10-29T04:38:50Z (UTC).

PR #30–34 ya fusionadas: catálogo y carrito multiproducto, promociones, migraciones 004–007, contrato 4.0.0 y autorización de consulta; se publica el estado del intento de pago para distinguir rechazo de espera, por lo que la limitación R-11 descrita antes queda corregida en código. También se integran radios accesibles, validación de URL de pasarela y revalidación de caché/tema claro. El CI de la punta acredita 454 pruebas aprobadas y tres omitidas; las 103 pruebas focalizadas PostgreSQL son un subconjunto reejecutado, no casos adicionales. PR32 aún señala configuración incorrecta del panel: la fusión no demuestra que se haya corregido ni activado el simulador. PR34 documenta servicios legados activos con riesgo de autorización reportado por el equipo, sin exposición efectiva de datos comprobada en este seguimiento; la corrección del repositorio actual no demuestra retiro o mitigación del legado. No se sondearon esos servicios. Los recorridos de navegador son reportes del equipo, no validación independiente ni aceptación de cobros reales. Se conserva presentación y despliegues confirmados por docente.

**Próximos pasos:**
- Aportar evidencia del valor corregido en el panel y de la revisión efectivamente publicada; verificar recorrido y revalidación de archivos tras el despliegue, sin confundir pago simulado con cobro real.
- Gestionar por responsables autorizados el retiro o mitigación de los servicios legados y dejar evidencia; no dar por cerrado el riesgo solo por fusionar código o documentación.
- Mantener el simulador desactivado antes de habilitar cobros reales y completar la evidencia de migraciones y contrato 4.0.0 en el entorno objetivo.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. Frontend/panel y API institucionales; docente confirma presentación/despliegues; sin nueva verificación visual.

**PR consultadas:** [#34](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/34): fusionada 2026-10-29T04:38:50Z; [#33](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/33): fusionada 2026-10-29T04:08:48Z; [#32](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/32): fusionada 2026-10-28T19:23:55Z; [#31](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/31): fusionada 2026-10-28T19:13:51Z; [#30](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/30): fusionada 2026-10-28T15:51:22Z; [#29](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/29): fusionada 2026-10-23T15:04:06Z; [#28](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/28): fusionada 2026-10-20T14:55:39Z; [#27](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/27): fusionada 2026-10-18T23:40:46Z; [#26](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/26): fusionada 2026-10-18T22:31:12Z; [#25](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/25): fusionada 2026-10-18T18:31:49Z; [#24](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/24): fusionada 2026-10-18T17:05:21Z; [#23](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/23): fusionada 2026-10-18T15:44:46Z; [#22](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/22): fusionada 2026-10-18T02:49:18Z; [#21](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/21): fusionada 2026-10-18T02:12:59Z; [#20](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/20): fusionada 2026-10-18T01:32:03Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/40818917596): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:23.723Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/70a98045f2effa9830ffb7c55199cb0cf7d13ccf/README.md) · [40818917596](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/40818917596) · [30](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/30) · [30#issuecomment-6433366872](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/30#issuecomment-6433366872) · [arc42.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/1c2c2412620ded70f2176d660cba052923bc25d8/docs/arc42/arc42.md) · [31](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/31) · [32](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/32) · [33](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/33) · [34](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/34) · [123266507508](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/40818917596/job/123266507508)

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [bba9513f965184ceea1c36eda722c4ac9fcc70b7](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/bba9513f965184ceea1c36eda722c4ac9fcc70b7), fecha del commit 2026-10-26T04:34:37Z (UTC).

Revalidación del 29/oct: misma punta y README que el corte anterior. Los cinco workflows de la misma revisión siguen exitosos: backend, Flutter, Compose/persistencia, contrato público y Web/Android, con emulador Android previamente verificado. Continúan integradas PR #61–65 y su taller aislado SQLite, sin broker/outbox productivo. PR #60 sigue abierta. README mantiene API institucional y frontend GitHub Pages, por lo que el requisito de dominio de toda la solución sigue parcial. No hay aceptación funcional nueva de este corte.

**Próximos pasos:**
- Conservar evidencia exacta del flujo Web/Android reparado y separar CI controlado de aceptación manual del despliegue.
- Mover/documentar el frontend bajo iscoutb.dev y mantener explícito el carácter aislado del taller frente a MySQL productivo.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. Cumplimiento parcial: API institucional, frontend externo GitHub Pages. Azure es histórico.

**PR consultadas:** [#65](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/65): fusionada 2026-10-26T04:34:38Z; [#64](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/64): fusionada 2026-10-26T03:51:27Z; [#63](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/63): fusionada 2026-10-26T03:03:33Z; [#62](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/62): fusionada 2026-10-26T01:31:24Z; [#61](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/61): fusionada 2026-10-26T00:57:55Z; [#59](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/59): fusionada 2026-10-19T04:51:37Z; [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60): abierta; [#57](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/57): fusionada 2026-10-19T04:17:24Z; [#58](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/58): fusionada 2026-10-19T04:04:00Z; [#56](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/56): fusionada 2026-10-19T03:17:47Z; [#55](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/55): fusionada 2026-10-12T04:50:45Z; [#54](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/54): fusionada 2026-10-04T07:14:35Z; [#53](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/53): fusionada 2026-10-04T06:38:56Z; [#52](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/52): fusionada 2026-10-04T04:04:41Z; [#51](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/51): fusionada 2026-10-04T03:06:42Z.

**CI consultado:** [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786871): success (misma punta); [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786849): success (misma punta); [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786840): success (misma punta); [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786825): success (misma punta); [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786823): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:23.723Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/bba9513f965184ceea1c36eda722c4ac9fcc70b7/README.md) · [40269786871](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786871) · [40269786849](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786849) · [40269786840](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786840) · [40269786825](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786825) · [40269786823](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786823)

<a id="recobra"></a>

## Recobra

Rama **master**, [0dda9abd2c76ef9b10724221225c0ed228197c39](https://github.com/ISCOUTB/AS_202620_Recobra/commit/0dda9abd2c76ef9b10724221225c0ed228197c39), fecha del commit 2026-10-29T02:32:33Z (UTC).

Incorpora seguridad S13: límites de uso, CSP y CORS, tratamiento del origen detrás de Cloudflare, auditoría y avisos operativos, controles de dependencias/secretos y documentación de privacidad que reconoce a Cloudflare. Los seis jobs de la punta pasan; los logs backend acreditan 215 pruebas unitarias, 124 e2e y 10 de contrato. La auditoría verde no significa ausencia de vulnerabilidades: acepta 13 avisos individuales con alcance documentado y vencimiento al 15/dic, mientras npm informa siete paquetes afectados de producción. Los ajustes observados en producción son reportes del equipo, no pruebas repetidas por este seguimiento. Siguen pendientes acciones operativas de protección/rotación y respaldo programado descritas por el equipo; CI no demuestra que se hayan ejecutado. Las diez PR nuevas de Dependabot están abiertas, no fusionadas. README conserva vitrina, Flutter Web y API institucionales. Se mantiene presentación confirmada por docente.

**Próximos pasos:**
- Acreditar las acciones operativas pendientes y el respaldo programado sin publicar credenciales ni datos personales.
- Revisar y probar las PR de dependencias; conservar la distinción entre avisos aceptados y mitigados y cumplir su vencimiento.
- Validar límites, origen del cliente, cabeceras y entrega de avisos en el despliegue actual; aportar evidencia de aceptación funcional independiente del CI.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README aclara vitrina, Flutter Web y API en mismo host institucional; no se añade auditoría funcional.

**PR consultadas:** [#10](https://github.com/ISCOUTB/AS_202620_Recobra/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_Recobra/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_Recobra/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_Recobra/pull/7): abierta; [#6](https://github.com/ISCOUTB/AS_202620_Recobra/pull/6): abierta; [#5](https://github.com/ISCOUTB/AS_202620_Recobra/pull/5): abierta; [#3](https://github.com/ISCOUTB/AS_202620_Recobra/pull/3): abierta; [#2](https://github.com/ISCOUTB/AS_202620_Recobra/pull/2): abierta; [#4](https://github.com/ISCOUTB/AS_202620_Recobra/pull/4): abierta; [#1](https://github.com/ISCOUTB/AS_202620_Recobra/pull/1): abierta.

**CI consultado:** [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:23.723Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/README.md) · [40806972927](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927) · [modelo-de-amenazas.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/docs/seguridad/modelo-de-amenazas.md) · [analisis-de-dependencias.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/docs/seguridad/analisis-de-dependencias.md) · [privacidad.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/docs/seguridad/privacidad.md) · [123228138789](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927/job/123228138789) · [123228138817](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927/job/123228138817)

<a id="routb"></a>

## ROUTB

Rama **master**, [22c2953553a9fc3518fb63576ac622d8bf5e80df](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/22c2953553a9fc3518fb63576ac622d8bf5e80df), fecha del commit 2026-10-25T23:22:49Z (UTC).

Revalidación del 29/oct: misma punta y README que el corte anterior. Continúan integradas PR #53/#54 y la garantía de solicitud activa única, pero la evidencia de migración 010 no acredita aplicación a Supabase objetivo. El taller de notificaciones permanece aislado y en memoria, no mensajería productiva durable. Se conserva la evidencia previa de gate Sonar del bot, distinta del job Actions que es un echo, y el avance entregado según docente.

**Próximos pasos:**
- Aplicar y verificar la migración 010 en el entorno autorizado antes de atribuir la garantía de unicidad al despliegue real.
- Mantener explícita la pérdida de cola en reinicio del prototipo y su no integración productiva; resolver observaciones Sonar y aportar aceptación funcional.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend institucional y guía actualizada a Dokploy; aplicación de migración 010 al entorno objetivo aún no confirmada.

**PR consultadas:** [#54](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/54): fusionada 2026-10-25T23:22:50Z; [#53](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/53): fusionada 2026-10-25T18:04:34Z; [#52](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/52): fusionada 2026-10-23T14:47:48Z; [#51](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/51): fusionada 2026-10-18T21:39:27Z; [#50](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/50): fusionada 2026-10-13T03:02:26Z; [#49](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/49): fusionada 2026-10-12T00:30:24Z; [#48](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/48): fusionada 2026-10-11T23:52:36Z; [#47](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/47): cerrada sin fusión registrada; [#46](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/46): fusionada 2026-10-03T23:20:32Z; [#45](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/45): fusionada 2026-10-03T22:57:29Z; [#44](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/44): fusionada 2026-10-03T19:53:46Z; [#43](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/43): fusionada 2026-10-03T05:18:30Z; [#42](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/42): fusionada 2026-10-03T01:18:46Z; [#41](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/41): cerrada sin fusión registrada; [#40](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/40): fusionada 2026-09-28T02:58:07Z.

**CI consultado:** [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40840394096): success (misma punta); [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:23.723Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/README.md) · [40840394096](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40840394096) · [40244499934](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934) · [53#issuecomment-6401195876](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/53#issuecomment-6401195876) · [54#issuecomment-6404835108](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/54#issuecomment-6404835108) · [SEMANA12.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/docs/evidencia/SEMANA12.md)

<a id="shareu"></a>

## ShareU

Rama **master**, [2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767), fecha del commit 2026-10-25T22:52:08Z (UTC).

Revalidación del 29/oct: misma punta y README que el corte anterior. La revisión actual mantiene repositorio Firestore y pruebas con cliente sustituido, mientras README conserva SQLite, reinicio de datos y placeholders de despliegue: sigue la deriva documental. El workflow de la punta permanece fallido; no acredita pruebas aprobadas ni autoriza atribuir la falla exclusivamente a Sonar. PR #22 y #23 siguen abiertas. Persistencia real Firebase y despliegue no se verificaron.

**Próximos pasos:**
- Conciliar README/C4/ADR con Firestore actual y publicar URL institucional concreta de frontend/API.
- Corregir y ejecutar el workflow con evidencia de pruebas del repositorio y resiliencia; validar persistencia en el entorno objetivo sin dar por real la simulación de cliente.

**Issues GitHub:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: 10 completed.

**README:** Sin URL concreta. Placeholders Vercel/Render y localhost, no URL pública concreta vigente.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z.

**CI consultado:** [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:23.723Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/README.md) · [40242189282](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282)

<a id="sistema-de-calificacion-automatica"></a>

## Calificación automática

Rama **master**, [561d520b138a1689d9bec9bdff597bdae66a6952](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/561d520b138a1689d9bec9bdff597bdae66a6952), fecha del commit 2026-10-26T01:08:51Z (UTC).

Sin cambios de punta ni README desde el corte del 28/oct; se conserva el CI exitoso exacto de esa revisión. La implementación de acuse, reintentos, recuperación y fallidos en Redis, la identidad hoja_id y la caché de propuestas ya constan en el corte anterior, no son avances nuevos de hoy. Persisten los límites documentados: procesamiento de imágenes sin OMR, un solo worker y Redis sin persistencia; no hay nueva aceptación del consumidor desplegado.

**Próximos pasos:**
- Validar el consumidor actualizado en el entorno desplegado y documentar la revisión exacta, sin confundir ensayo local con Render.
- Resolver persistencia de Redis/almacén y estrategia antes de añadir un segundo worker; conservar explícito que OMR aún no está implementado.
- Publicar frontend y API bajo iscoutb.dev.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Frontend y API Render; no dominio institucional. Sin sondeo directo en esta revisión.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin fusión registrada.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40252791139): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:28.981Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/README.md) · [40252791139](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40252791139) · [taller-mensajeria.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/docs/evidencia/taller-mensajeria.md)

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [e903230d220735b43c9c53c42c64c66524ce0ff9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/e903230d220735b43c9c53c42c64c66524ce0ff9), fecha del commit 2026-10-25T15:08:51Z (UTC).

Sin cambios de punta ni README desde el 28/oct. Se conserva la evidencia de CI/CD exitosos para d4d4371, anterior a la punta documental; el CD solicita un webhook y no acredita finalización ni salud de Dokploy. Siguen pendientes la conciliación del respaldo Render/TLS y la diferencia entre API entregada y Flutter objetivo. Se mantiene la presentación y funcionamiento confirmados por el docente.

**Próximos pasos:**
- Verificar en Dokploy la revisión efectivamente desplegada y su salud; el webhook exitoso no lo acredita por sí solo.
- Reconciliar README y ADR sobre respaldo Render/TLS, y mantener la distinción entre API entregada y Flutter objetivo.

**Issues GitHub:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: 4 completed.

**README:** Institucional. API institucional; README también enlaza Render como alternativa histórica, sin confirmar respaldo activo. Flutter sigue arquitectura objetivo. Funcionamiento confirmado por docente; webhook CD no acredita fin del despliegue.

**PR consultadas:** [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z; [#14](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/14): fusionada 2026-09-17T01:53:44Z; [#13](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/13): fusionada 2026-09-16T01:48:07Z; [#12](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/12): fusionada 2026-09-14T01:01:35Z; [#11](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/11): fusionada 2026-09-12T17:29:59Z; [#10](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/10): fusionada 2026-09-12T15:26:17Z; [#9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/9): fusionada 2026-09-11T02:08:20Z; [#8](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/8): fusionada 2026-09-11T00:36:16Z.

**CI consultado:** [CD](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203934640): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203750864): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:28.981Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/README.md) · [40203934640](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203934640) · [40203750864](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203750864) · [ci.yml](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/.github/workflows/ci.yml) · [0010-despliegue-con-dokploy-y-docker-compose.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/docs/adr/0010-despliegue-con-dokploy-y-docker-compose.md)

<a id="tienda-virtual-utb"></a>

## Tienda virtual UTB

Rama **main**, [647bcbd413354775e85a9444f97a2db82725c5f1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/647bcbd413354775e85a9444f97a2db82725c5f1), fecha del commit 2026-10-25T16:53:06Z (UTC).

Sin cambios de punta, README ni PRs desde el 28/oct. El último workflow de la revisión actual permanece exitoso para frontend/backend, contrato, RLS y Alembic; el análisis Sonar estaba omitido y ese estado no acredita un Quality Gate nuevo. Siguen vigentes la transacción compartida pedidos/inventario y la importación de legado endurecida ya reportadas, mientras Redis es caché propuesta y el catálogo usa no-store.

**Próximos pasos:**
- Implementar y medir la caché propuesta solo tras validar invalidación y concurrencia; mantener inventario y autorización fuera de ella.
- Restablecer ejecución verificable de Sonar/Quality Gate y reemplazar URL temporal por subdominio institucional con TLS válido.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Frontend sslip temporal; el equipo documenta certificado autofirmado pendiente y despliegue 0.5.0. No se sorteó aviso TLS ni se verificó el sitio en vivo.

**PR consultadas:** [#12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/12): fusionada 2026-10-25T02:58:28Z; [#11](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/11): fusionada 2026-10-24T20:15:26Z; [#10](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/10): fusionada 2026-10-24T19:40:05Z; [#9](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/9): fusionada 2026-10-24T19:22:55Z; [#8](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/8): fusionada 2026-10-24T19:22:38Z; [#7](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/7): fusionada 2026-10-24T19:22:22Z; [#6](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/6): fusionada 2026-10-24T19:22:12Z; [#5](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/5): fusionada 2026-10-24T19:21:59Z; [#4](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/4): fusionada 2026-10-24T19:21:48Z; [#3](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/3): fusionada 2026-10-24T19:21:38Z; [#2](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/2): fusionada 2026-10-24T19:21:28Z; [#1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/1): fusionada 2026-10-21T16:14:34Z.

**CI consultado:** [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:28.981Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/README.md) · [40213830995](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995) · [cache-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/cache-s12.md) · [consistencia-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/consistencia-s12.md) · [archivos_legado.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/backend/app/archivos_legado.py)

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [31932f0006542c6f3f6222071bb1a9c36b6f888a](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/31932f0006542c6f3f6222071bb1a9c36b6f888a), fecha del commit 2026-10-26T06:03:01Z (UTC).

Sin cambios de punta ni README desde el 28/oct. Se conserva la evidencia exacta de 78 pruebas en tests/ sobre PostgreSQL 16 aislado y despliegue con migraciones/reinicio exitosos; no vuelve a presentarse como vigente el bloqueo Alembic ya corregido. El comando excluye app/tests/ y no prueba todo el cliente. Persisten notificador simulado, worker de operación separada, caché propuesta y precaución por fallback destructivo a DATABASE_URL fuera de CI.

**Próximos pasos:**
- Eliminar el fallback destructivo a DATABASE_URL o exigir validación inequívoca de BD de pruebas antes de drop_all.
- Documentar y verificar operación del worker y notificación real si se pretende incluirla en el despliegue; conservar el alcance tests/ de CI.
- Publicar URL exacta institucional en README y validar los flujos nuevos del cliente; no presentar caché propuesta como activa.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README raíz sin endpoint público vigente. Solo en código: https://129-80-171-141.nip.io; release APK v1.0.2 publicado, no prueba de sitio institucional.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/4): fusionada 2026-10-26T04:35:44Z; [#3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/3): fusionada 2026-10-25T18:20:31Z; [#2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/2): fusionada 2026-10-06T06:08:06Z.

**CI consultado:** [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926): success (misma punta); [Release APK](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132197969): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:28.981Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/README.md) · [40278118926](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926) · [40132197969](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132197969) · [limites-del-experimento.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/mensajeria/limites-del-experimento.md) · [conftest.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/tests/conftest.py) · [consistencia-por-operacion.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/datos/consistencia-por-operacion.md)

<a id="uniteam"></a>

## uniTeam

Rama **master**, [0a44bd5a8d9374423b08fef87e46672cd6ad501b](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/0a44bd5a8d9374423b08fef87e46672cd6ad501b), fecha del commit 2026-10-26T00:55:53Z (UTC).

Sin cambios de punta ni README desde el 28/oct. El cron del 29/oct vuelve a fallar seis comprobaciones, pero sus logs consultan las direcciones Render antiguas y no DuckDNS publicado en README. No demuestra caída del despliegue actual. Se mantienen taller SQLite aislado de la API/auditoría, MySQL como fuente de verdad y política de caché propuesta, no habilitada.

**Próximos pasos:**
- Actualizar la sonda de despliegue para comprobar las direcciones DuckDNS vigentes y repetir sus seis casos antes de interpretar salud.
- Conservar la distinción entre taller SQLite aislado y API real; implementar y medir la política de caché si se adopta.
- Publicar frontend y API bajo iscoutb.dev.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Externo. Frontend y API DuckDNS. Sonda sigue consultando Render; su fallo no determina disponibilidad de DuckDNS.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/4): fusionada 2026-10-04T21:23:33Z; [#2](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/2): fusionada 2026-09-14T01:20:18Z; [#10](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/10): fusionada 2026-10-26T00:55:53Z; [#9](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/9): fusionada 2026-10-26T00:55:34Z; [#8](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/8): fusionada 2026-10-23T05:15:01Z; [#7](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/7): fusionada 2026-10-23T04:57:30Z; [#6](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/6): fusionada 2026-10-23T04:38:54Z; [#5](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/5): fusionada 2026-10-13T15:44:45Z; [#3](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/3): fusionada 2026-09-21T16:46:49Z.

**CI consultado:** [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40873650648): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40829731319): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40796088035): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40744900068): failure (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40251714762): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:28.981Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/README.md) · [0015-taller-de-mensajeria-local-aislado.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/adr/0015-taller-de-mensajeria-local-aislado.md) · [0016-conservar-mysql-como-fuente-de-verdad.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/adr/0016-conservar-mysql-como-fuente-de-verdad.md) · [40873650648](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40873650648) · [40829731319](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40829731319) · [40796088035](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40796088035) · [40744900068](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40744900068) · [40251714762](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40251714762)

<a id="xald"></a>

## XALD

Rama **master**, [1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00](https://github.com/ISCOUTB/AS_202620_XALD/commit/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00), fecha del commit 2026-10-26T04:04:58Z (UTC).

La rama principal master y su README permanecen sin cambios desde el 28/oct, con CI exacto exitoso. Como actividad lateral, experimental recibió una resolución de conflicto el 29/oct; el compare contra master muestra diferencias solo en dos documentos arc42 de riesgos/fallos de integración, no nueva implementación. El CI de esa rama pasa backend, módulos Android y contrato; deploy-backend está omitido. No hay PR abierta ni integración de este delta en master, por lo que no se presenta como entrega principal ni redespliegue. Sigue pendiente activar y verificar procesarPendientes en operación real, con persistencia de cola/deduplicación; el envío disparado en pruebas y un health exitoso no acreditan el recorrido completo en dispositivo.

**Próximos pasos:**
- Conciliar la documentación de experimental con master antes de proponer integración: evitar reintroducir descripciones obsoletas del cliente HTTP y mantener las mitigaciones pendientes explícitas.
- Conectar procesarPendientes a un ejecutor real con conectividad y persistir cola/marcas antes de prometer entrega tras reinicios.
- Completar referencias de commit/run en evidencia y distinguir E2E local del funcionamiento en dispositivo/Render.
- Publicar el endpoint bajo iscoutb.dev y verificar persistencia y sincronización de extremo a extremo.

**Issues GitHub:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. Motivos: 5 completed; 1 duplicate.

**README:** Externo. Backend Render. El CI incluye paso de health exitoso; no es verificación funcional propia ni evidencia de frontend institucional.

**PR consultadas:** [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z; [#24](https://github.com/ISCOUTB/AS_202620_XALD/pull/24): fusionada 2026-09-27T16:24:00Z; [#23](https://github.com/ISCOUTB/AS_202620_XALD/pull/23): fusionada 2026-09-20T17:34:35Z; [#22](https://github.com/ISCOUTB/AS_202620_XALD/pull/22): cerrada sin fusión registrada; [#21](https://github.com/ISCOUTB/AS_202620_XALD/pull/21): cerrada sin fusión registrada; [#20](https://github.com/ISCOUTB/AS_202620_XALD/pull/20): fusionada 2026-09-20T16:21:31Z; [#19](https://github.com/ISCOUTB/AS_202620_XALD/pull/19): fusionada 2026-09-16T04:45:22Z; [#18](https://github.com/ISCOUTB/AS_202620_XALD/pull/18): fusionada 2026-09-14T03:06:22Z; [#15](https://github.com/ISCOUTB/AS_202620_XALD/pull/15): fusionada 2026-09-13T16:09:58Z; [#10](https://github.com/ISCOUTB/AS_202620_XALD/pull/10): fusionada 2026-09-07T02:54:50Z; [#9](https://github.com/ISCOUTB/AS_202620_XALD/pull/9): fusionada 2026-09-07T02:20:49Z; [#8](https://github.com/ISCOUTB/AS_202620_XALD/pull/8): fusionada 2026-08-31T03:18:04Z; [#7](https://github.com/ISCOUTB/AS_202620_XALD/pull/7): fusionada 2026-08-30T03:44:22Z; [#6](https://github.com/ISCOUTB/AS_202620_XALD/pull/6): cerrada sin fusión registrada; [#5](https://github.com/ISCOUTB/AS_202620_XALD/pull/5): fusionada 2026-08-29T05:06:12Z; [#4](https://github.com/ISCOUTB/AS_202620_XALD/pull/4): fusionada 2026-08-29T03:11:54Z; [#3](https://github.com/ISCOUTB/AS_202620_XALD/pull/3): fusionada 2026-08-24T03:02:56Z; [#2](https://github.com/ISCOUTB/AS_202620_XALD/pull/2): fusionada 2026-08-24T00:16:44Z; [#1](https://github.com/ISCOUTB/AS_202620_XALD/pull/1): fusionada 2026-08-16T18:45:28Z.

**CI consultado:** [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501): success (misma punta); [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40798851273): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:28.981Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/README.md) · [40267222501](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501) · [40250035779](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40250035779) · [limites-del-experimento.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/mensajes/limites-del-experimento.md) · [evidencia.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/mensajes/evidencia.md) · [1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00...7676801c00b935d02a3dac52d3ad06939dba9764](https://github.com/ISCOUTB/AS_202620_XALD/compare/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00...7676801c00b935d02a3dac52d3ad06939dba9764) · [40798851273](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40798851273)

<a id="verifacts"></a>

## Verifacts

Rama **master**, [559612b61ee4cea46cef6d00f857d2e5c2794f03](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/559612b61ee4cea46cef6d00f857d2e5c2794f03), fecha del commit 2026-10-28T05:41:24Z (UTC).

Sin cambios de punta, README, issues ni PR desde el 28/oct. Se conservan los cuatro commits documentales S12/S13 ya reportados, no avances nuevos de hoy: controles SSRF, límites de carga, timeout, protección del historial y TLS pendientes; retención de 30 días y delete_analysis propuestos, no implementados. Sigue pendiente un reporte SCA reproducible; el workflow revisado no ejecuta pip-audit ni npm audit. CI de la misma punta: 66 pruebas, build/smoke de imagen y análisis Sonar exitosos, sin acreditar redespliegue ni nuevo Quality Gate. Los ocho casos HTTP son evidencia aportada previamente por el equipo, no nueva aceptación independiente.

**Próximos pasos:**
- Aportar salidas fechadas de pip-audit y npm audit con revisión y versiones resueltas; reconciliar la tabla SCA y no presentar el análisis Sonar como auditoría de dependencias.
- Implementar y probar los controles de mayor riesgo del modelo de amenazas; marcar retención y supresión como diseño hasta que existan código, operación y evidencia.
- Mantener separadas caché estática activa, propuestas de caché de backend y garantías de SQLite en un nodo; las seis pruebas de consistencia existentes no son código nuevo de este incremento.
- Completar subdominio iscoutb.dev y TLS; conservar trazabilidad de los ocho casos HTTP previos y añadir recorrido de navegador/persistencia si se pretende aceptación integral.

**Issues GitHub:** 0 abiertas / 3 cerradas; 0 abiertas sin asignar. Motivos: 3 completed.

**README:** Externo. Referencia HTTP sslip. README declara pendiente dominio institucional/certificado; frontend / y API /docs,/health separados conceptualmente.

**CI consultado:** [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382): success (misma punta); [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Observación:** 2026-10-29T13:10:28.981Z (UTC).

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/README.md) · [40639475382](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382) · [40639475319](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319) · [entrega-consistencia-cache-costo-reversion.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/docs/entregas/entrega-consistencia-cache-costo-reversion.md) · [entrega-seguridad-amenazas-dependencias-privacidad.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/docs/entregas/entrega-seguridad-amenazas-dependencias-privacidad.md) · [tests.yml](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/.github/workflows/tests.yml) · [service.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/app/modules/content/service.py) · [repository.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/app/persistence/repository.py) · [evidencia-aceptacion.txt](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/evidencia-aceptacion.txt)

