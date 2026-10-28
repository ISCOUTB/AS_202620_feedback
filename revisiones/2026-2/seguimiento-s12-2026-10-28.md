# Seguimiento de los 23 proyectos · 28 de octubre de 2026

Consulta del **28 de octubre de 2026**, entre las 07:56 y las 08:03 COT (12:56–13:03 UTC), sobre los 23 proyectos del listado vigente. Seguimiento documental, no recalificación. **No se cierra S12 automáticamente** ni se recalifica con este seguimiento. Se conservan calificaciones, planillas, matrices y cortes históricos.

**43 abiertas y 132 cerradas** (131 completed; 1 duplicate); 19 abiertas sin asignar. Pull requests excluidas.

README: **10 con algún endpoint institucional; 6 con enlaces externos; 7 sin URL pública concreta**. Las direcciones institucionales incluyen APIs, no prueban que toda interfaz esté publicada.

Se conservan las confirmaciones del docente: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. Estas declaraciones no son pruebas funcionales automatizadas de este corte.

Se leyeron repositorios y resultados de GitHub sin ejecutar código estudiantil ni modificar sus issues o despliegues. Los PDF se excluyen. Código fusionado, CI, publicación y aceptación funcional son evidencias distintas. No se repitieron pruebas funcionales en vivo. No se obtuvieron estados personalizados de GitHub Projects; OPEN/CLOSED y motivos de cierre pertenecen a issues, no a columnas de tablero.

[Issues y motivos de cierre](seguimiento-issues-2026-10-28.md) · [README y despliegues](seguimiento-despliegues-2026-10-28.md) · [Corte anterior](seguimiento-s12-2026-10-27.md)

## Cambios respecto al corte anterior

- **DinamikUTB**: Integra nuevas pantallas administrativas, currículo y gestión de cuentas, además de imagen Flutter/Nginx para el laboratorio. El README de frontend separa https://dinamikutb.iscoutb.dev (web) y https://api.dinamikutb.iscoutb.dev (API), sujetos a aprovisionamiento; ADR0006 marca GitHub Pages como reemplazado. El README raíz sigue describiendo el primer dominio como API y conserva enlaces anteriores: hay desalineación documental. Publicar la imagen GHCR termina correctamente, pero no acredita redeploy en Dokploy. CI de la misma punta falla: pytest no recolecta por ImportError de RequisitoPrograma; Flutter registra 20 pruebas aprobadas y cuatro fallidas (tres de validación de correo y una de registro de estudiantes); SonarCloud queda omitido. Los routers nuevos de currículo, programas y reportes no se incorporan en app/main.py consultado; su existencia no demuestra rutas disponibles. No se verificó funcionamiento en vivo.
- **ElMapita**: Integra caché TTL/LRU del backend, invalidación de POIs, limpieza de versiones de modelos del cliente y mensajería en memoria con reintentos, DLQ y auditoría. Añade reconciliación al arrancar y cada diez minutos desde POIs persistidos para reconstruir la proyección de auditoría: mitigación específica, no outbox ni bus durable. El CI global aparece exitoso y confirma 56 pruebas unitarias backend; sin embargo, el E2E GET / falla (404 frente a 200 esperado) y su error se neutraliza con echo. SonarCloud falla por autorización/proyecto no encontrado y omite Quality Gate; es no bloqueante. El README continúa sin URL pública concreta. Se conserva la confirmación docente de que ElMapita presentó y funciona; no se atribuye esa aceptación a esta punta ni se verificó su nuevo despliegue.
- **InvenTrack**: Corrige la brecha de idempotencia HTTP: reserva/serializa la clave antes de modificar stock, conserva fingerprint y resultado, devuelve replay sin nuevo movimiento/evento y responde 409 ante payload incompatible. ADR0017 explicita almacenamiento volátil por proceso y la ventana stock/publicación sin outbox. El CI de la punta actual pasa 32 pruebas y vuelve a ejecutar una prueba de contrato incluida en el conjunto, no 33 pruebas distintas; el scanner Sonar termina, sin acreditar por sí solo Quality Gate. La nueva evidencia de despliegue del equipo reporta que el 27/oct no pudo resolver DNS/TLS institucional y obtuvo 503 en /health y /metrics de Render. Esto entra en tensión con las declaraciones anteriores de despliegue/verificación del README. Son observaciones del equipo, no una prueba independiente actual ni demostración de inexistencia de despliegue; falta publicar/verificar esta punta en servicio. El documento de CI cita todavía la revisión anterior.
- **Verifacts**: Cuatro commits documentales posteriores al corte anterior formalizan consistencia/caché/costo de reversión (S12) y amenazas, dependencias y privacidad (S13), sin cambios de código ni README. Se documentan controles pendientes de SSRF, límites de carga, timeout, protección del historial y TLS; la retención de 30 días y delete_analysis siguen siendo propuestas, no capacidades presentes en el repositorio consultado. El documento declara auditoría SCA, pero el workflow revisado no ejecuta pip-audit ni npm audit y la tabla de versiones no coincide con el entorno instalado en el CI actual: hace falta un reporte reproducible, no asumir dependencias libres de vulnerabilidades. El CI de la punta pasa 66 pruebas, build/smoke de imagen y análisis Sonar; no acredita redespliegue ni un nuevo Quality Gate. Se conserva la evidencia de ocho casos HTTP aportada por el equipo, sin nueva aceptación independiente; dominio HTTP sslip y mensajería aislada no cambian.

Los demás proyectos fueron revalidados; sin novedades sustantivas se conserva su feedback individual anterior, sin añadir secciones repetidas.

<a id="audioshare"></a>

## AudioShare

Rama **master**, [8de5ac1daacd189b38d732a0d3d2e916ee29a281](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/8de5ac1daacd189b38d732a0d3d2e916ee29a281), fecha del commit 2026-10-26T04:47:47Z (UTC).

Revalidación del 28/oct: sin cambios de punta, README, issues ni PR frente al corte del 27; los resultados de CI consultados permanecen iguales. Integra PR7 y PR9: decisiones de persistencia/consistencia y prototipo aislado de sincronización por mensajes, con deduplicación, reintentos y DLQ volátiles. El CI de Node y la publicación de imagen pasan; Flutter falla en analyze, por lo que sus pruebas y build web quedan omitidos. El README ahora dice que Docker compila Flutter Web, pero también reporta que el dominio aún sirve el cliente legado y /rooms devuelve 404: es observación del equipo, no prueba independiente de este corte; publicar imagen no acredita redespliegue.

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

Revalidación del 28/oct: sin cambios de punta, README, issues ni PR frente al corte del 27; los resultados de CI consultados permanecen iguales. Corrige el operador Python inválido señalado en el corte previo y ahora pasa Idempotency-Key al caso de uso/repositorio PostgreSQL de publicaciones, en lugar de ignorarlo. Añade recursos/feed y prototipo de mensajería con outbox en memoria. Persisten almacenamiento/comparación directa de contraseña sin hash y secreto JWT predeterminado; no se reproduce su valor. La búsqueda de idempotencia no compara autor ni payload antes de devolver una publicación previa: revisar alcance y conflicto de claves. Los dos workflows actuales siguen fallando sin jobs disponibles; no se demuestra que las pruebas hayan corrido. README actualizado afirma despliegue HTTPS, pero no publica una URL concreta.

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

## DinamikUTB

Rama **master**, [822baaa371ec94827d09319a09e13f11f7123f64](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/822baaa371ec94827d09319a09e13f11f7123f64), fecha del commit 2026-10-27T17:08:57Z (UTC).

Integra nuevas pantallas administrativas, currículo y gestión de cuentas, además de imagen Flutter/Nginx para el laboratorio. El README de frontend separa https://dinamikutb.iscoutb.dev (web) y https://api.dinamikutb.iscoutb.dev (API), sujetos a aprovisionamiento; ADR0006 marca GitHub Pages como reemplazado. El README raíz sigue describiendo el primer dominio como API y conserva enlaces anteriores: hay desalineación documental. Publicar la imagen GHCR termina correctamente, pero no acredita redeploy en Dokploy. CI de la misma punta falla: pytest no recolecta por ImportError de RequisitoPrograma; Flutter registra 20 pruebas aprobadas y cuatro fallidas (tres de validación de correo y una de registro de estudiantes); SonarCloud queda omitido. Los routers nuevos de currículo, programas y reportes no se incorporan en app/main.py consultado; su existencia no demuestra rutas disponibles. No se verificó funcionamiento en vivo.

**Próximos pasos:**
- Resolver el ImportError de RequisitoPrograma y las cuatro pruebas Flutter; repetir CI en la misma punta.
- Integrar y probar los routers nuevos antes de afirmar disponibilidad de currículo, programas y reportes.
- Unificar README raíz y frontend con los dominios realmente provisionados; distinguir API/web, retirar referencias vigentes obsoletas y acreditar redeploy Dokploy con recorrido funcional.

**Issues GitHub:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. README raíz y frontend discrepan en roles/dominios. GHCR acredita imagen, no despliegue ni DNS/TLS o aceptación; no se prescribe recrear la base antigua de Render.

**PR consultadas:** [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35): cerrada sin fusión registrada; [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37): fusionada 2026-10-23T03:04:11Z; [#36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36): fusionada 2026-10-23T01:01:46Z; [#33](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/33): fusionada 2026-09-27T17:38:37Z; [#32](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/32): fusionada 2026-09-22T03:51:10Z; [#31](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/31): fusionada 2026-09-22T03:16:20Z; [#30](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/30): fusionada 2026-09-21T18:41:30Z; [#29](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/29): fusionada 2026-09-21T17:48:40Z; [#12](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/12): fusionada 2026-09-07T04:26:25Z; [#11](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/11): fusionada 2026-09-07T03:57:51Z; [#10](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/10): fusionada 2026-08-31T18:47:14Z; [#9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/9): fusionada 2026-08-31T18:32:43Z; [#8](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/8): fusionada 2026-08-31T05:11:21Z; [#7](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/7): fusionada 2026-08-31T04:52:24Z; [#6](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/6): fusionada 2026-08-31T04:21:48Z; [#5](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/5): fusionada 2026-08-31T03:00:17Z; [#4](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/4): fusionada 2026-08-24T03:26:31Z; [#3](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/3): fusionada 2026-08-24T03:10:21Z; [#2](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/2): fusionada 2026-08-24T02:31:51Z; [#1](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/1): fusionada 2026-08-24T02:02:03Z.

**CI consultado:** [Publish frontend image](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40549937090): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831321): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/README.md) · [evidencia-s12.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/evidencia-s12.md) · [11-risks-and-technical-debt.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/arc42/11-risks-and-technical-debt.md) · [0012-despliegue-en-servidor-del-laboratorio.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/adr/0012-despliegue-en-servidor-del-laboratorio.md) · [40549937090](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40549937090) · [40547831321](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831321) · [README.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/frontend/README.md) · [0006-plataforma-despliegue-frontend.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/docs/adr/0006-plataforma-despliegue-frontend.md) · [main.py](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/backend/app/main.py) · [publish-frontend-image.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/.github/workflows/publish-frontend-image.yml)

<a id="drift"></a>

## Drift

Rama **master**, [d9a181630f9c7cc9daf3d58705092b245cdc7c73](https://github.com/ISCOUTB/AS_202620_Drift/commit/d9a181630f9c7cc9daf3d58705092b245cdc7c73), fecha del commit 2026-10-25T22:37:33Z (UTC).

Revalidación del 28/oct: sin cambios de punta, README, issues ni PR frente al corte del 27; los resultados de CI consultados permanecen iguales. PR32 integrado: actualiza S12, ADR0010, arc42 y C4 con almacenamiento de navegador y ausencia de brokers; explicita costo de reversión de datos. CI y despliegue Azure ejecutados con éxito para la punta actual. Esto no convierte las mediciones simuladas previas en rendimiento real ni acredita aceptación funcional en el dominio institucional.

**Próximos pasos:**
- Validar recorrido real en el despliegue institucional y conservar evidencias separadas de Azure.
- Repetir mediciones relevantes con dependencias reales y distinguir decisiones de datos de implementación.

**Issues GitHub:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. Frontend y API /api; API alternativa; Frontend alternativo

**PR consultadas:** [#32](https://github.com/ISCOUTB/AS_202620_Drift/pull/32): fusionada 2026-10-25T22:37:33Z; [#31](https://github.com/ISCOUTB/AS_202620_Drift/pull/31): fusionada 2026-10-21T04:53:32Z; [#30](https://github.com/ISCOUTB/AS_202620_Drift/pull/30): fusionada 2026-10-19T03:20:50Z; [#29](https://github.com/ISCOUTB/AS_202620_Drift/pull/29): fusionada 2026-10-19T03:07:18Z; [#28](https://github.com/ISCOUTB/AS_202620_Drift/pull/28): fusionada 2026-10-19T02:08:58Z; [#27](https://github.com/ISCOUTB/AS_202620_Drift/pull/27): fusionada 2026-10-12T19:42:41Z; [#26](https://github.com/ISCOUTB/AS_202620_Drift/pull/26): fusionada 2026-10-12T19:15:32Z; [#25](https://github.com/ISCOUTB/AS_202620_Drift/pull/25): fusionada 2026-10-12T04:49:54Z; [#24](https://github.com/ISCOUTB/AS_202620_Drift/pull/24): fusionada 2026-10-11T05:28:23Z; [#23](https://github.com/ISCOUTB/AS_202620_Drift/pull/23): fusionada 2026-10-11T05:21:57Z; [#22](https://github.com/ISCOUTB/AS_202620_Drift/pull/22): fusionada 2026-10-11T04:53:50Z; [#21](https://github.com/ISCOUTB/AS_202620_Drift/pull/21): fusionada 2026-10-11T03:47:58Z.

**CI consultado:** [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/d9a181630f9c7cc9daf3d58705092b245cdc7c73/README.md) · [40241076074](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076074) · [40241076067](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/40241076067)

<a id="elmapita"></a>

## ElMapita

Rama **main**, [537a7716cc37df3fae1b7e2331e0114c93871ee5](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/537a7716cc37df3fae1b7e2331e0114c93871ee5), fecha del commit 2026-10-25T16:26:51Z (UTC).

Integra caché TTL/LRU del backend, invalidación de POIs, limpieza de versiones de modelos del cliente y mensajería en memoria con reintentos, DLQ y auditoría. Añade reconciliación al arrancar y cada diez minutos desde POIs persistidos para reconstruir la proyección de auditoría: mitigación específica, no outbox ni bus durable. El CI global aparece exitoso y confirma 56 pruebas unitarias backend; sin embargo, el E2E GET / falla (404 frente a 200 esperado) y su error se neutraliza con echo. SonarCloud falla por autorización/proyecto no encontrado y omite Quality Gate; es no bloqueante. El README continúa sin URL pública concreta. Se conserva la confirmación docente de que ElMapita presentó y funciona; no se atribuye esa aceptación a esta punta ni se verificó su nuevo despliegue.

**Próximos pasos:**
- Corregir el E2E y hacer explícitos/bloqueantes los checks necesarios; resolver autorización/configuración de SonarCloud.
- Documentar en README URLs reales de frontend/API bajo iscoutb.dev y el commit desplegado, sin sustituir la aceptación docente previa por CI.
- Validar recuperación tras reinicio y límites del reconciliador; no presentar auditoría en memoria como durabilidad del bus.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40654274728): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/537a7716cc37df3fae1b7e2331e0114c93871ee5/README.md) · [40654274728](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40654274728) · [0009-mensajeria-asincrona-simulador-en-memoria.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/537a7716cc37df3fae1b7e2331e0114c93871ee5/docs/adr/0009-mensajeria-asincrona-simulador-en-memoria.md) · [diseno-cache.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/537a7716cc37df3fae1b7e2331e0114c93871ee5/docs/datos/diseno-cache.md) · [poi-audit.reconciler.ts](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/537a7716cc37df3fae1b7e2331e0114c93871ee5/backend/src/modules/pois/application/poi-audit.reconciler.ts) · [ci.yml](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/537a7716cc37df3fae1b7e2331e0114c93871ee5/.github/workflows/ci.yml)

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), fecha del commit 2026-10-26T03:57:38Z (UTC).

Revalidación del 28/oct: sin cambios de punta, README, issues ni PR frente al corte del 27; los resultados de CI consultados permanecen iguales. PR3 integra documentación de consistencia y prototipo aislado de envío automático de invitaciones, con proveedor simulado, deduplicación, reintentos y DLQ en memoria. Su workflow específico ejecuta pruebas y demo con éxito; no envía correos reales ni integra Flask/BD/Dokploy. El CI general ahora falla al recolectar test_simulador.py por import relativo sin paquete reconocido, no por el error DATABASE_URL del corte anterior; contrato y Docker quedan omitidos. Pages publica documentación estática, no aceptación de la API. README mantiene host pendiente, sin URL pública concreta.

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

Revalidación del 28/oct: sin cambios de punta, README, issues ni PR frente al corte del 27; los resultados de CI consultados permanecen iguales. Integra S12/ADR0006 y taller asíncrono aislado. El run actual pasa 12 pruebas base, 11 de contrato y nueve de mensajería, además de auditorías de arquitectura y dependencias; el fallo antiguo de auditoría está superado. La cola, deduplicación y DLQ son volátiles y el endpoint de aforo permanece síncrono; caché/event-log son diseños, no integración productiva. El workflow no configura PostgreSQL ni ejecuta su prueba específica: no atribuirle validación de esa base. README sigue describiendo backend institucional.

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

Rama **main**, [972a12775ffc073a1efe9e6c9435be497c5187d6](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/972a12775ffc073a1efe9e6c9435be497c5187d6), fecha del commit 2026-10-27T21:37:20Z (UTC).

Corrige la brecha de idempotencia HTTP: reserva/serializa la clave antes de modificar stock, conserva fingerprint y resultado, devuelve replay sin nuevo movimiento/evento y responde 409 ante payload incompatible. ADR0017 explicita almacenamiento volátil por proceso y la ventana stock/publicación sin outbox. El CI de la punta actual pasa 32 pruebas y vuelve a ejecutar una prueba de contrato incluida en el conjunto, no 33 pruebas distintas; el scanner Sonar termina, sin acreditar por sí solo Quality Gate. La nueva evidencia de despliegue del equipo reporta que el 27/oct no pudo resolver DNS/TLS institucional y obtuvo 503 en /health y /metrics de Render. Esto entra en tensión con las declaraciones anteriores de despliegue/verificación del README. Son observaciones del equipo, no una prueba independiente actual ni demostración de inexistencia de despliegue; falta publicar/verificar esta punta en servicio. El documento de CI cita todavía la revisión anterior.

**Próximos pasos:**
- Actualizar evidencia de CI al run actual y vincular Quality Gate al análisis correspondiente.
- Acreditar hash desplegado, /health, /metrics y recorrido funcional institucional; distinguir API de frontend.
- Mantener explícitos límites de idempotencia en memoria, reinicios y varias réplicas; adoptar registro/outbox durable cuando se requiera recuperación.

**Issues GitHub:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: 7 completed.

**README:** Institucional. README conserva API institucional y alternativa Render. Evidencia del equipo del 27/oct reporta DNS/TLS institucional no verificable y 503 en health/metrics de Render; no es comprobación independiente del corte. Hay que reconciliar ese reporte con las declaraciones previas de despliegue/verificación del README.

**CI consultado:** [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40588329661): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/README.md) · [evidencia-mensajeria-s12.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/evidencia-mensajeria-s12.md) · [0015-completar-decision-de-almacenamiento-y-reversion.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/adr/0015-completar-decision-de-almacenamiento-y-reversion.md) · [registrar_movimiento.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/app/inventario/application/registrar_movimiento.py) · [router.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/app/inventario/infrastructure/router.py) · [0016-integrar-eventos-de-auditoria-en-movimientos.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/adr/0016-integrar-eventos-de-auditoria-en-movimientos.md) · [40588329661](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40588329661) · [evidencia-despliegue-s12.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/evidencia-despliegue-s12.md) · [0017-idempotencia-http-en-comandos-de-inventario.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/docs/adr/0017-idempotencia-http-en-comandos-de-inventario.md) · [idempotency.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/972a12775ffc073a1efe9e6c9435be497c5187d6/app/inventario/infrastructure/idempotency.py)

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [3d003b62ffe92c659699bd1236424fb397bc2eee](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/3d003b62ffe92c659699bd1236424fb397bc2eee), fecha del commit 2026-10-25T03:25:42Z (UTC).

Sin cambios de punta, README o issues desde el corte del 27. Sigue pasando el CI de la misma revisión. Las ocho PR de dependencias #16–23 permanecen abiertas; no son funcionalidades fusionadas. Se mantienen integración Garage/PostgreSQL y deudas de idempotencia/reintentos documentadas. README continúa sin URL pública vigente concreta; no se repitió aceptación funcional en vivo.

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

Sin cambios de punta ni README desde el 27. Continúan integradas PR #20 y #22: Cache-Control, expiración JWT en backend/main.py y taller aislado de outbox SQLite, deduplicación y reintentos. Los tres workflows de la misma punta siguen exitosos; se conserva el alcance previamente verificado de 27 pruebas backend y 18 del taller, no cobertura de la implementación separada api/. PostgreSQL/outbox productivos siguen propuestos y el backend conserva memoria. PR #21 continúa abierta; README sigue sin URL pública concreta.

**Próximos pasos:**
- Conectar persistencia y eventos al flujo real solo tras implementar y validar PostgreSQL; mantener explícito que el taller SQLite no es mensajería productiva.
- Añadir cobertura de api/ o aclarar cuál implementación se despliega; publicar frontend/API institucionales y comprobar autorización y consistencia multiinstancia.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de trabajo o despliegue.

**PR consultadas:** [#21](https://github.com/ISCOUTB/AS_202620_LostVault/pull/21): abierta; [#22](https://github.com/ISCOUTB/AS_202620_LostVault/pull/22): fusionada 2026-10-26T04:46:41Z; [#20](https://github.com/ISCOUTB/AS_202620_LostVault/pull/20): fusionada 2026-10-26T01:52:55Z; [#19](https://github.com/ISCOUTB/AS_202620_LostVault/pull/19): fusionada 2026-10-20T16:16:34Z; [#18](https://github.com/ISCOUTB/AS_202620_LostVault/pull/18): fusionada 2026-10-19T01:43:15Z; [#17](https://github.com/ISCOUTB/AS_202620_LostVault/pull/17): fusionada 2026-10-19T01:32:11Z; [#16](https://github.com/ISCOUTB/AS_202620_LostVault/pull/16): fusionada 2026-10-05T03:30:54Z; [#15](https://github.com/ISCOUTB/AS_202620_LostVault/pull/15): fusionada 2026-10-05T02:31:39Z; [#14](https://github.com/ISCOUTB/AS_202620_LostVault/pull/14): fusionada 2026-10-05T00:42:49Z; [#13](https://github.com/ISCOUTB/AS_202620_LostVault/pull/13): fusionada 2026-09-28T04:39:31Z.

**CI consultado:** [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589): success (misma punta); [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466): success (misma punta); [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/README.md) · [40270806589](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589) · [40270806466](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466) · [40270806424](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424) · [taller-mensajeria.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/docs/mensajeria/taller-mensajeria.md)

<a id="mapsutb"></a>

## mapsutb

Rama **master**, [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), fecha del commit 2026-10-25T14:04:14Z (UTC).

Sin nuevos commits ni README desde el 27; las issues #55 y #56 continúan cerradas completed. La sonda programada más reciente y la sincronización de hallazgos de Sonar terminan exitosamente para la misma punta. Se conserva la evidencia previa de publicación Firebase del commit que fijó firebase-tools 15.34.0; no es una nueva aceptación manual ni un nuevo despliegue. README sigue en mapsutb.web.app, fuera de iscoutb.dev; no confundir con ElMapita.

**Próximos pasos:**
- Mantener la evidencia del arreglo y los cierres; verificar comportamiento de recarga/reintento del grafo con escenarios reproducibles.
- Publicar frontend bajo iscoutb.dev y actualizar README; distinguir disponibilidad de sonda de aceptación del recorrido funcional.

**Issues GitHub:** 0 abiertas / 54 cerradas; 0 abiertas sin asignar. Motivos: 54 completed.

**README:** Externo. Frontend Firebase externo; sonda CI disponible, sin nueva aceptación funcional propia.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z.

**CI consultado:** [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40688643477): success (misma punta); [Sincronizar hallazgos de Sonar a GitHub Issues](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40686708521): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200516007): success (misma punta); [Despliegue web (Firebase Hosting)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200515940): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [40688643477](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40688643477) · [40686708521](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40686708521) · [40200516007](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200516007) · [40200515940](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200515940)

<a id="pideutb"></a>

## PideUtb

Rama **master**, [ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f), fecha del commit 2026-10-23T15:04:06Z (UTC).

Sin cambios de punta, README, PR ni CI desde el 27. PR #30 permanece abierta con carrito multiproducto, migración 004, catálogo y contrato 3.0.0. El CI del head de la PR ejecuta Python 3.11/3.12, contrato y auditoría: el log Python 3.12 acredita 407 pruebas aprobadas y tres omitidas, además, una ejecución focalizada de 103 pruebas de repositorios y autenticación para comprobar PostgreSQL (subconjunto reejecutado, no 103 casos adicionales). Sonar bot informa gate aprobado con siete issues nuevas y 0% de cobertura nueva; es evidencia separada de los pasos Sonar omitidos en Actions. La pasarela es simulada, no aceptación de cobros reales ni despliegue confirmado de la PR. R-11 mantiene rechazo indistinguible de pendiente para el comprador; R-12 exige desactivar el simulador antes de cobros reales. Se conserva actualización presentada y despliegues confirmados por docente.

**Próximos pasos:**
- Revisar e integrar PR #30 con migración 004 y contrato 3.0.0 solo tras validar la compatibilidad y el recorrido objetivo; el CI de la rama no prueba despliegue.
- Exponer al comprador el estado del intento/rechazo (R-11) y verificar que PIDEUTB_URL_PASARELA_SIMULADA esté desactivada antes de cobros reales (R-12); la demostración no es pasarela real.
- Revisar las siete issues Sonar y el alcance de cobertura, separando el gate del bot del scanner omitido en Actions.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. Frontend/panel y API institucionales; docente confirma presentación/despliegues; sin nueva verificación visual.

**PR consultadas:** [#30](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/30): abierta; [#29](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/29): fusionada 2026-10-23T15:04:06Z; [#28](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/28): fusionada 2026-10-20T14:55:39Z; [#27](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/27): fusionada 2026-10-18T23:40:46Z; [#26](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/26): fusionada 2026-10-18T22:31:12Z; [#25](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/25): fusionada 2026-10-18T18:31:49Z; [#24](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/24): fusionada 2026-10-18T17:05:21Z; [#23](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/23): fusionada 2026-10-18T15:44:46Z; [#22](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/22): fusionada 2026-10-18T02:49:18Z; [#21](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/21): fusionada 2026-10-18T02:12:59Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39975061857): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/40446958696): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/README.md) · [39975061857](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39975061857) · [40446958696](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/40446958696) · [30](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/30) · [30#issuecomment-6433366872](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/30#issuecomment-6433366872) · [arc42.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/1c2c2412620ded70f2176d660cba052923bc25d8/docs/arc42/arc42.md)

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [bba9513f965184ceea1c36eda722c4ac9fcc70b7](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/bba9513f965184ceea1c36eda722c4ac9fcc70b7), fecha del commit 2026-10-26T04:34:37Z (UTC).

Sin cambios de punta, README o issues desde el 27. Los cinco workflows de la misma revisión siguen exitosos: backend, Flutter, Compose/persistencia, contrato público y Web/Android, con emulador Android previamente verificado. Continúan integradas PR #61–65 y su taller aislado SQLite, sin broker/outbox productivo. PR #60 sigue abierta. README mantiene API institucional y frontend GitHub Pages, por lo que el requisito de dominio de toda la solución sigue parcial. No hay aceptación funcional nueva de este corte.

**Próximos pasos:**
- Conservar evidencia exacta del flujo Web/Android reparado y separar CI controlado de aceptación manual del despliegue.
- Mover/documentar el frontend bajo iscoutb.dev y mantener explícito el carácter aislado del taller frente a MySQL productivo.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. Cumplimiento parcial: API institucional, frontend externo GitHub Pages. Azure es histórico.

**PR consultadas:** [#65](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/65): fusionada 2026-10-26T04:34:38Z; [#64](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/64): fusionada 2026-10-26T03:51:27Z; [#63](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/63): fusionada 2026-10-26T03:03:33Z; [#62](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/62): fusionada 2026-10-26T01:31:24Z; [#61](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/61): fusionada 2026-10-26T00:57:55Z; [#59](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/59): fusionada 2026-10-19T04:51:37Z; [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60): abierta; [#57](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/57): fusionada 2026-10-19T04:17:24Z; [#58](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/58): fusionada 2026-10-19T04:04:00Z; [#56](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/56): fusionada 2026-10-19T03:17:47Z; [#1](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/1): abierta.

**CI consultado:** [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786825): success (misma punta); [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786823): success (misma punta); [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786849): success (misma punta); [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786840): success (misma punta); [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786871): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/bba9513f965184ceea1c36eda722c4ac9fcc70b7/README.md) · [40269786825](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786825) · [40269786823](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786823) · [40269786849](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786849) · [40269786840](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786840) · [40269786871](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/40269786871)

<a id="recobra"></a>

## Recobra

Rama **master**, [00f9291c4e59b315a65ba2af348ed449b28319c7](https://github.com/ISCOUTB/AS_202620_Recobra/commit/00f9291c4e59b315a65ba2af348ed449b28319c7), fecha del commit 2026-10-24T14:04:29Z (UTC).

Sin nuevos commits, README, issues ni runs desde el 27. El run exacto continúa exitoso; se conserva la evidencia previamente verificada de 37 pruebas PostgreSQL y restauración de 23 filas en nueve tablas, sin inferir respaldos productivos programados. Los e2e de mensajería inyectan fallos y otros usan memoria; tampoco demuestran alertas recibidas por personas. README distingue vitrina, Flutter Web y API institucionales. Se conserva presentación confirmada por docente.

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

Sin cambios de punta, README o issues desde el 27; nueva ejecución programada de purga termina exitosamente y el CI de la misma punta sigue aprobado. Continúan integradas PR #53/#54 y la garantía de solicitud activa única, pero la evidencia de migración 010 no acredita aplicación a Supabase objetivo. El taller de notificaciones permanece aislado y en memoria, no mensajería productiva durable. Se conserva la evidencia previa de gate Sonar del bot, distinta del job Actions que es un echo, y el avance entregado según docente.

**Próximos pasos:**
- Aplicar y verificar la migración 010 en el entorno autorizado antes de atribuir la garantía de unicidad al despliegue real.
- Mantener explícita la pérdida de cola en reinicio del prototipo y su no integración productiva; resolver observaciones Sonar y aportar aceptación funcional.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend institucional y guía actualizada a Dokploy; aplicación de migración 010 al entorno objetivo aún no confirmada.

**PR consultadas:** [#54](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/54): fusionada 2026-10-25T23:22:50Z; [#53](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/53): fusionada 2026-10-25T18:04:34Z; [#52](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/52): fusionada 2026-10-23T14:47:48Z; [#51](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/51): fusionada 2026-10-18T21:39:27Z; [#50](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/50): fusionada 2026-10-13T03:02:26Z; [#49](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/49): fusionada 2026-10-12T00:30:24Z; [#48](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/48): fusionada 2026-10-11T23:52:36Z; [#47](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/47): cerrada sin fusión registrada; [#46](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/46): fusionada 2026-10-03T23:20:32Z; [#45](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/45): fusionada 2026-10-03T22:57:29Z.

**CI consultado:** [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40655023567): success (misma punta); [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/README.md) · [40655023567](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40655023567) · [40244499934](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934) · [53#issuecomment-6401195876](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/53#issuecomment-6401195876) · [54#issuecomment-6404835108](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/54#issuecomment-6404835108) · [SEMANA12.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/docs/evidencia/SEMANA12.md)

<a id="shareu"></a>

## ShareU

Rama **master**, [2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767), fecha del commit 2026-10-25T22:52:08Z (UTC).

Sin cambios de punta, README o issues desde el 27. La revisión actual mantiene repositorio Firestore y pruebas con cliente sustituido, mientras README conserva SQLite, reinicio de datos y placeholders de despliegue: sigue la deriva documental. El workflow de la punta permanece fallido; no acredita pruebas aprobadas ni autoriza atribuir la falla exclusivamente a Sonar. PR #22 y #23 siguen abiertas. Persistencia real Firebase y despliegue no se verificaron.

**Próximos pasos:**
- Conciliar README/C4/ADR con Firestore actual y publicar URL institucional concreta de frontend/API.
- Corregir y ejecutar el workflow con evidencia de pruebas del repositorio y resiliencia; validar persistencia en el entorno objetivo sin dar por real la simulación de cliente.

**Issues GitHub:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: 10 completed.

**README:** Sin URL concreta. Placeholders Vercel/Render y localhost, no URL pública concreta vigente.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z.

**CI consultado:** [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/README.md) · [40242189282](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282)

<a id="sistema-de-calificacion-automatica"></a>

## Calificación automática

Rama **master**, [561d520b138a1689d9bec9bdff597bdae66a6952](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/561d520b138a1689d9bec9bdff597bdae66a6952), fecha del commit 2026-10-26T01:08:51Z (UTC).

Sin cambios de punta ni README desde el corte del 27/oct; se conserva el CI exitoso exacto de esa revisión. La implementación de acuse, reintentos, recuperación y fallidos en Redis, la identidad hoja_id y la caché de propuestas ya constan en el corte anterior, no son avances nuevos de hoy. Persisten los límites documentados: procesamiento de imágenes sin OMR, un solo worker y Redis sin persistencia; no hay nueva aceptación del consumidor desplegado.

**Próximos pasos:**
- Validar el consumidor actualizado en el entorno desplegado y documentar la revisión exacta, sin confundir ensayo local con Render.
- Resolver persistencia de Redis/almacén y estrategia antes de añadir un segundo worker; conservar explícito que OMR aún no está implementado.
- Publicar frontend y API bajo iscoutb.dev.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Frontend y API Render; no dominio institucional. Sin sondeo directo en esta revisión.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin fusión registrada.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40252791139): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/README.md) · [40252791139](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40252791139) · [taller-mensajeria.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/561d520b138a1689d9bec9bdff597bdae66a6952/docs/evidencia/taller-mensajeria.md)

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [e903230d220735b43c9c53c42c64c66524ce0ff9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/e903230d220735b43c9c53c42c64c66524ce0ff9), fecha del commit 2026-10-25T15:08:51Z (UTC).

Sin cambios de punta ni README desde el 27/oct. Se conserva la evidencia de CI/CD exitosos para d4d4371, anterior a la punta documental; el CD solicita un webhook y no acredita finalización ni salud de Dokploy. Siguen pendientes la conciliación del respaldo Render/TLS y la diferencia entre API entregada y Flutter objetivo. Se mantiene la presentación y funcionamiento confirmados por el docente.

**Próximos pasos:**
- Verificar en Dokploy la revisión efectivamente desplegada y su salud; el webhook exitoso no lo acredita por sí solo.
- Reconciliar README y ADR sobre respaldo Render/TLS, y mantener la distinción entre API entregada y Flutter objetivo.

**Issues GitHub:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: 4 completed.

**README:** Institucional. API institucional; README también enlaza Render como alternativa histórica, sin confirmar respaldo activo. Flutter sigue arquitectura objetivo. Funcionamiento confirmado por docente; webhook CD no acredita fin del despliegue.

**PR consultadas:** [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z; [#14](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/14): fusionada 2026-09-17T01:53:44Z; [#13](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/13): fusionada 2026-09-16T01:48:07Z; [#12](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/12): fusionada 2026-09-14T01:01:35Z; [#11](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/11): fusionada 2026-09-12T17:29:59Z; [#10](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/10): fusionada 2026-09-12T15:26:17Z; [#9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/9): fusionada 2026-09-11T02:08:20Z; [#8](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/8): fusionada 2026-09-11T00:36:16Z.

**CI consultado:** [CD](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203934640): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203750864): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/README.md) · [40203934640](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203934640) · [40203750864](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/40203750864) · [ci.yml](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/.github/workflows/ci.yml) · [0010-despliegue-con-dokploy-y-docker-compose.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e903230d220735b43c9c53c42c64c66524ce0ff9/docs/adr/0010-despliegue-con-dokploy-y-docker-compose.md)

<a id="tienda-virtual-utb"></a>

## Tienda virtual UTB

Rama **main**, [647bcbd413354775e85a9444f97a2db82725c5f1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/647bcbd413354775e85a9444f97a2db82725c5f1), fecha del commit 2026-10-25T16:53:06Z (UTC).

Sin cambios de punta, README ni PRs desde el 27/oct. El último workflow de la revisión actual permanece exitoso para frontend/backend, contrato, RLS y Alembic; el análisis Sonar estaba omitido y ese estado no acredita un Quality Gate nuevo. Siguen vigentes la transacción compartida pedidos/inventario y la importación de legado endurecida ya reportadas, mientras Redis es caché propuesta y el catálogo usa no-store.

**Próximos pasos:**
- Implementar y medir la caché propuesta solo tras validar invalidación y concurrencia; mantener inventario y autorización fuera de ella.
- Restablecer ejecución verificable de Sonar/Quality Gate y reemplazar URL temporal por subdominio institucional con TLS válido.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Frontend sslip temporal; el equipo documenta certificado autofirmado pendiente y despliegue 0.5.0. No se sorteó aviso TLS ni se verificó el sitio en vivo.

**PR consultadas:** [#12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/12): fusionada 2026-10-25T02:58:28Z; [#11](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/11): fusionada 2026-10-24T20:15:26Z; [#10](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/10): fusionada 2026-10-24T19:40:05Z; [#9](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/9): fusionada 2026-10-24T19:22:55Z; [#8](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/8): fusionada 2026-10-24T19:22:38Z; [#7](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/7): fusionada 2026-10-24T19:22:22Z; [#6](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/6): fusionada 2026-10-24T19:22:12Z; [#5](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/5): fusionada 2026-10-24T19:21:59Z; [#4](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/4): fusionada 2026-10-24T19:21:48Z; [#3](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/3): fusionada 2026-10-24T19:21:38Z; [#2](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/2): fusionada 2026-10-24T19:21:28Z; [#1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/1): fusionada 2026-10-21T16:14:34Z.

**CI consultado:** [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/README.md) · [40213830995](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995) · [cache-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/cache-s12.md) · [consistencia-s12.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/docs/consistencia-s12.md) · [archivos_legado.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/backend/app/archivos_legado.py)

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [31932f0006542c6f3f6222071bb1a9c36b6f888a](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/31932f0006542c6f3f6222071bb1a9c36b6f888a), fecha del commit 2026-10-26T06:03:01Z (UTC).

Sin cambios de punta ni README desde el 27/oct. Se conserva la evidencia exacta de 78 pruebas en tests/ sobre PostgreSQL 16 aislado y despliegue con migraciones/reinicio exitosos; no vuelve a presentarse como vigente el bloqueo Alembic ya corregido. El comando excluye app/tests/ y no prueba todo el cliente. Persisten notificador simulado, worker de operación separada, caché propuesta y precaución por fallback destructivo a DATABASE_URL fuera de CI.

**Próximos pasos:**
- Eliminar el fallback destructivo a DATABASE_URL o exigir validación inequívoca de BD de pruebas antes de drop_all.
- Documentar y verificar operación del worker y notificación real si se pretende incluirla en el despliegue; conservar el alcance tests/ de CI.
- Publicar URL exacta institucional en README y validar los flujos nuevos del cliente; no presentar caché propuesta como activa.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README raíz sin endpoint público vigente. Solo en código: https://129-80-171-141.nip.io; release APK v1.0.2 publicado, no prueba de sitio institucional.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/4): fusionada 2026-10-26T04:35:44Z; [#3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/3): fusionada 2026-10-25T18:20:31Z; [#2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/2): fusionada 2026-10-06T06:08:06Z.

**CI consultado:** [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926): success (misma punta); [Release APK](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132197969): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/README.md) · [40278118926](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926) · [40132197969](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132197969) · [limites-del-experimento.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/mensajeria/limites-del-experimento.md) · [conftest.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/tests/conftest.py) · [consistencia-por-operacion.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/datos/consistencia-por-operacion.md)

<a id="uniteam"></a>

## uniTeam

Rama **master**, [0a44bd5a8d9374423b08fef87e46672cd6ad501b](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/0a44bd5a8d9374423b08fef87e46672cd6ad501b), fecha del commit 2026-10-26T00:55:53Z (UTC).

Sin cambios de punta ni README desde el 27/oct. El cron del 28/oct vuelve a fallar seis comprobaciones, pero sus logs apuntan a las direcciones Render antiguas y no a DuckDNS publicado en README. No demuestra caída del despliegue actual. Se mantienen taller SQLite aislado de la API/auditoría, MySQL como fuente de verdad y política de caché propuesta, no habilitada.

**Próximos pasos:**
- Actualizar la sonda de despliegue para comprobar las direcciones DuckDNS vigentes y repetir sus seis casos antes de interpretar salud.
- Conservar la distinción entre taller SQLite aislado y API real; implementar y medir la política de caché si se adopta.
- Publicar frontend y API bajo iscoutb.dev.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Externo. Frontend y API DuckDNS. Sonda sigue consultando Render; su fallo no determina disponibilidad de DuckDNS.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/4): fusionada 2026-10-04T21:23:33Z; [#2](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/2): fusionada 2026-09-14T01:20:18Z; [#10](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/10): fusionada 2026-10-26T00:55:53Z; [#9](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/9): fusionada 2026-10-26T00:55:34Z; [#8](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/8): fusionada 2026-10-23T05:15:01Z; [#7](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/7): fusionada 2026-10-23T04:57:30Z; [#6](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/6): fusionada 2026-10-23T04:38:54Z; [#5](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/5): fusionada 2026-10-13T15:44:45Z; [#3](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/3): fusionada 2026-09-21T16:46:49Z.

**CI consultado:** [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40688141415): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40462765164): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40429798256): failure (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40251714762): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/README.md) · [40462765164](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40462765164) · [40429798256](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40429798256) · [40251714762](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40251714762) · [0015-taller-de-mensajeria-local-aislado.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/adr/0015-taller-de-mensajeria-local-aislado.md) · [0016-conservar-mysql-como-fuente-de-verdad.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/docs/adr/0016-conservar-mysql-como-fuente-de-verdad.md) · [40688141415](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40688141415)

<a id="xald"></a>

## XALD

Rama **master**, [1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00](https://github.com/ISCOUTB/AS_202620_XALD/commit/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00), fecha del commit 2026-10-26T04:04:58Z (UTC).

Sin cambios de punta ni README desde el 27/oct; el CI exacto permanece exitoso. No aparece evidencia nueva de activación automática de procesarPendientes: el envío sigue disparado en pruebas, con cola/deduplicación en memoria. La sincronización HTTP, contrato y backoff ya reportados no acreditan entrega persistente tras reinicios ni funcionamiento completo en dispositivo. El paso health de Render no sustituye aceptación funcional.

**Próximos pasos:**
- Conectar procesarPendientes a un ejecutor real con conectividad y persistir cola/marcas antes de prometer entrega tras reinicios.
- Completar referencias de commit/run en evidencia y distinguir E2E local del funcionamiento en dispositivo/Render.
- Publicar el endpoint bajo iscoutb.dev y verificar persistencia y sincronización de extremo a extremo.

**Issues GitHub:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. Motivos: 5 completed; 1 duplicate.

**README:** Externo. Backend Render. El CI incluye paso de health exitoso; no es verificación funcional propia ni evidencia de frontend institucional.

**PR consultadas:** [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z; [#24](https://github.com/ISCOUTB/AS_202620_XALD/pull/24): fusionada 2026-09-27T16:24:00Z; [#23](https://github.com/ISCOUTB/AS_202620_XALD/pull/23): fusionada 2026-09-20T17:34:35Z; [#22](https://github.com/ISCOUTB/AS_202620_XALD/pull/22): cerrada sin fusión registrada; [#21](https://github.com/ISCOUTB/AS_202620_XALD/pull/21): cerrada sin fusión registrada; [#20](https://github.com/ISCOUTB/AS_202620_XALD/pull/20): fusionada 2026-09-20T16:21:31Z; [#19](https://github.com/ISCOUTB/AS_202620_XALD/pull/19): fusionada 2026-09-16T04:45:22Z; [#18](https://github.com/ISCOUTB/AS_202620_XALD/pull/18): fusionada 2026-09-14T03:06:22Z; [#15](https://github.com/ISCOUTB/AS_202620_XALD/pull/15): fusionada 2026-09-13T16:09:58Z; [#10](https://github.com/ISCOUTB/AS_202620_XALD/pull/10): fusionada 2026-09-07T02:54:50Z; [#9](https://github.com/ISCOUTB/AS_202620_XALD/pull/9): fusionada 2026-09-07T02:20:49Z; [#8](https://github.com/ISCOUTB/AS_202620_XALD/pull/8): fusionada 2026-08-31T03:18:04Z; [#7](https://github.com/ISCOUTB/AS_202620_XALD/pull/7): fusionada 2026-08-30T03:44:22Z; [#6](https://github.com/ISCOUTB/AS_202620_XALD/pull/6): cerrada sin fusión registrada; [#5](https://github.com/ISCOUTB/AS_202620_XALD/pull/5): fusionada 2026-08-29T05:06:12Z; [#4](https://github.com/ISCOUTB/AS_202620_XALD/pull/4): fusionada 2026-08-29T03:11:54Z; [#3](https://github.com/ISCOUTB/AS_202620_XALD/pull/3): fusionada 2026-08-24T03:02:56Z; [#2](https://github.com/ISCOUTB/AS_202620_XALD/pull/2): fusionada 2026-08-24T00:16:44Z; [#1](https://github.com/ISCOUTB/AS_202620_XALD/pull/1): fusionada 2026-08-16T18:45:28Z.

**CI consultado:** [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501): success (misma punta); [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40250035779): failure (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/README.md) · [40267222501](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501) · [40250035779](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40250035779) · [limites-del-experimento.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/mensajes/limites-del-experimento.md) · [evidencia.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/docs/mensajes/evidencia.md)

<a id="verifacts"></a>

## Verifacts

Rama **master**, [559612b61ee4cea46cef6d00f857d2e5c2794f03](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/559612b61ee4cea46cef6d00f857d2e5c2794f03), fecha del commit 2026-10-28T05:41:24Z (UTC).

Cuatro commits documentales posteriores al corte anterior formalizan consistencia/caché/costo de reversión (S12) y amenazas, dependencias y privacidad (S13), sin cambios de código ni README. Se documentan controles pendientes de SSRF, límites de carga, timeout, protección del historial y TLS; la retención de 30 días y delete_analysis siguen siendo propuestas, no capacidades presentes en el repositorio consultado. El documento declara auditoría SCA, pero el workflow revisado no ejecuta pip-audit ni npm audit y la tabla de versiones no coincide con el entorno instalado en el CI actual: hace falta un reporte reproducible, no asumir dependencias libres de vulnerabilidades. El CI de la punta pasa 66 pruebas, build/smoke de imagen y análisis Sonar; no acredita redespliegue ni un nuevo Quality Gate. Se conserva la evidencia de ocho casos HTTP aportada por el equipo, sin nueva aceptación independiente; dominio HTTP sslip y mensajería aislada no cambian.

**Próximos pasos:**
- Aportar salidas fechadas de pip-audit y npm audit con revisión y versiones resueltas; reconciliar la tabla SCA y no presentar el análisis Sonar como auditoría de dependencias.
- Implementar y probar los controles de mayor riesgo del modelo de amenazas; marcar retención y supresión como diseño hasta que existan código, operación y evidencia.
- Mantener separadas caché estática activa, propuestas de caché de backend y garantías de SQLite en un nodo; las seis pruebas de consistencia existentes no son código nuevo de este incremento.
- Completar subdominio iscoutb.dev y TLS; conservar trazabilidad de los ocho casos HTTP previos y añadir recorrido de navegador/persistencia si se pretende aceptación integral.

**Issues GitHub:** 0 abiertas / 3 cerradas; 0 abiertas sin asignar. Motivos: 3 completed.

**README:** Externo. Referencia HTTP sslip. README declara pendiente dominio institucional/certificado; frontend / y API /docs,/health separados conceptualmente.

**CI consultado:** [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382): success (misma punta); [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/README.md) · [40639475382](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382) · [40639475319](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319) · [entrega-consistencia-cache-costo-reversion.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/docs/entregas/entrega-consistencia-cache-costo-reversion.md) · [entrega-seguridad-amenazas-dependencias-privacidad.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/docs/entregas/entrega-seguridad-amenazas-dependencias-privacidad.md) · [tests.yml](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/.github/workflows/tests.yml) · [service.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/app/modules/content/service.py) · [repository.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/app/persistence/repository.py) · [evidencia-aceptacion.txt](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/evidencia-aceptacion.txt)

