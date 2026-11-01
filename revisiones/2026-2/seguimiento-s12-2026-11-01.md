# Seguimiento de los 23 proyectos · 1 de noviembre de 2026

Consulta del **1 de noviembre de 2026**, con observaciones fechadas por proyecto (UTC). Seguimiento documental de los 23 proyectos del listado vigente, sin recalificar ni cerrar S12 automáticamente. Calificaciones, planillas, matrices y cortes históricos permanecen intactos.

**43 issues abiertas y 132 cerradas** (131 completed; 1 duplicate); 19 abiertas sin asignar. Sin cambios de conteo respecto al 31/oct.

README: **10 con algún endpoint institucional; 6 con enlaces externos; 7 sin URL pública concreta**. Un endpoint API no demuestra frontend publicado; ausencia de URL no demuestra ausencia de trabajo o despliegue.

Se conservan las confirmaciones del docente: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. No equivalen a pruebas funcionales nuevas de este corte.

Se consultaron README, historial, issues (excluyendo PR), propuestas y CI sin ejecutar código estudiantil. No se probaron sitios en vivo: código fusionado, CI, publicación y aceptación funcional son evidencias distintas. Los estados OPEN/CLOSED y motivos son de GitHub Issues; el conector no expone estados personalizados de Projects y no se obtuvieron columnas de tablero.

[Issues y motivos](seguimiento-issues-2026-11-01.md) · [README y despliegues](seguimiento-despliegues-2026-11-01.md) · [Antecedentes del 31/oct](seguimiento-s12-2026-10-31.md)

## Cambios respecto al 31/oct

- **Drift**: Integra controles de seguridad, dependencias y auditorías; CI y Quality Gate pasan. Azure registra publicación de paquete, sin comprobar el recorrido institucional. La PR #52 falla en Sonar por autorización/organización y no es el CI de master.
- **InvenTrack**: Actualiza dependencias y endurece la exposición en producción: rutas de negocio deshabilitadas por defecto y endpoints internos protegidos. CI, 34 pruebas y auditoría aprobados; no hay redespliegue acreditado.
- **LaPlacita**: Dependencias todavía propuestas: #29 cerrada sin merge, #28 y #30 abiertas con CI aprobado y Sonar omitido. La punta principal y el problema del webhook no cambian.
- **TAIA**: Incorpora alertas y verificadores; 324 pruebas aprobadas, pero falla el Quality Gate por new_security_rating=3 frente a umbral 1. CD omitido; no acredita despliegue de la nueva punta.

Los demás proyectos se revalidaron. No se añaden secciones individuales repetidas por sondas rutinarias o evidencia sin cambios sustantivos. Este informe resume el delta y enlaza el corte anterior para conservar los antecedentes sin duplicarlos.

<a id="audioshare"></a>

## AudioShare

Rama **master**, [da3c4058629e3e8bbadc559541bdeb61ca57c55a](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/da3c4058629e3e8bbadc559541bdeb61ca57c55a), fecha del commit 2026-10-30T05:03:11Z (UTC). Observación: 2026-11-01T13:02:36.043Z.

Revalidación del 1/nov: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al 31/oct. Se conserva el feedback anterior.

**Próximos pasos:**
- Redesplegar la revisión actual mediante el flujo Dokploy documentado y adjuntar evidencia fechada de frontend, API y sincronización entre receptores en el dominio institucional.
- Separar validación nativa de descarga local y reproducción web por URL; probar fallo de descarga, reintento y reingreso conservando rol.
- Documentar el motivo y alcance de la prueba Flutter omitida; no equiparar imagen publicada con versión servida.

**Issues:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar. Motivos: 2 completed.

**README:** Institucional. README conserva origen compartido frontend/API y reporte del equipo del 26/oct sobre cliente legado y /rooms 404. No se repitió prueba viva.

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/8): abierta; [#9](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/9): fusionada 2026-10-26T04:47:48Z; [#7](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/7): fusionada 2026-10-26T03:42:05Z; [#2](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/2): fusionada 2026-09-01T14:56:35Z

**CI consultado:** [CI 41006229901](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229901): success (misma punta); [Publicar imagen 41006229863](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229863): success (misma punta); [Flutter 41006229849](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229849): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/da3c4058629e3e8bbadc559541bdeb61ca57c55a/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_AudioShare/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_AudioShare/pulls) · [da3c4058629e3e8bbadc559541bdeb61ca57c55a](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/da3c4058629e3e8bbadc559541bdeb61ca57c55a) · [41006229901](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229901) · [41006229863](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229863) · [41006229849](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41006229849) · [Antecedentes](seguimiento-s12-2026-10-31.md#audioshare).

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, [7c7200f1d2669a0dd63cb7fa0b3587135357b78c](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7c7200f1d2669a0dd63cb7fa0b3587135357b78c), fecha del commit 2026-10-26T05:40:17Z (UTC). Observación: 2026-11-01T13:02:36.210Z.

Revalidación del 1/nov: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al 31/oct. Se conserva el feedback anterior.

**Próximos pasos:**
- Usar hash de contraseñas y rechazar arranque inseguro sin configuración JWT.
- Aislar claves de idempotencia por autor/operación, validar payload y probar duplicados concurrentes/conflictivos.
- Resolver workflows fallidos y publicar URL exacta de frontend/API en README.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README declara HTTPS/Dokploy, pero no publica URL pública concreta del proyecto.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta; [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3): fusionada 2026-10-05T05:46:36Z; [#2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2): fusionada 2026-09-21T04:56:52Z

**CI consultado:** [.github/workflows/backend-tests.yml 40275481686](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275481686): failure (misma punta); [.github/workflows/contrato.yml 40275480682](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275480682): failure (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7c7200f1d2669a0dd63cb7fa0b3587135357b78c/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pulls) · [7c7200f1d2669a0dd63cb7fa0b3587135357b78c](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7c7200f1d2669a0dd63cb7fa0b3587135357b78c) · [40275481686](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275481686) · [40275480682](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40275480682) · [Antecedentes](seguimiento-s12-2026-10-31.md#clubs_utb).

<a id="dinamikutb"></a>

## DinamikUTB

Rama **master**, [822baaa371ec94827d09319a09e13f11f7123f64](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/822baaa371ec94827d09319a09e13f11f7123f64), fecha del commit 2026-10-27T17:08:57Z (UTC). Observación: 2026-11-01T13:02:35.942Z.

Revalidación del 1/nov: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al 31/oct. Se conserva el feedback anterior.

**Próximos pasos:**
- Resolver el ImportError de RequisitoPrograma y las cuatro pruebas Flutter; repetir CI en la misma punta.
- Integrar y probar los routers nuevos antes de afirmar disponibilidad de currículo, programas y reportes.
- Unificar README raíz y frontend con los dominios realmente provisionados; distinguir API/web, retirar referencias vigentes obsoletas y acreditar redeploy Dokploy con recorrido funcional.

**Issues:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. README raíz conserva endpoint institucional descrito como backend y enlaces externos; discrepa con README frontend (web y API separados). No se acredita redeploy.

**PR consultadas:** [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37): fusionada 2026-10-23T03:04:11Z; [#36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36): fusionada 2026-10-23T01:01:46Z; [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35): cerrada sin merge

**CI consultado:** [Publish frontend image 40549937090](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40549937090): success (misma punta); [CI 40547831321](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831321): failure (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/822baaa371ec94827d09319a09e13f11f7123f64/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_DinamikUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pulls) · [822baaa371ec94827d09319a09e13f11f7123f64](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/822baaa371ec94827d09319a09e13f11f7123f64) · [40549937090](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40549937090) · [40547831470](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831470) · [40547831321](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40547831321) · [Antecedentes](seguimiento-s12-2026-10-31.md#dinamikutb).

<a id="drift"></a>

## Drift

Rama **master**, [a5391102b14ccc879ef624af9f61f6818d163586](https://github.com/ISCOUTB/AS_202620_Drift/commit/a5391102b14ccc879ef624af9f61f6818d163586), fecha del commit 2026-11-01T06:59:39Z (UTC). Observación: 2026-11-01T13:02:36.085Z.

Desde el 31/oct integra 18 commits y siete PR (#33–36 y #49–51): actualiza dependencias/acciones y locks, incorpora auditorías pip-audit/npm audit al CI, token administrativo para sincronización y métricas, límite de tasa por IP, CORS acotado, registro de sincronización y documentación STRIDE/privacidad con aviso en el frontend. La punta pasa cuatro jobs CI: 207 pruebas backend y 163 casos de contrato, en conteos separados (el contrato advierte desajuste de validación en tres operaciones); build/smoke frontend local; auditorías sin vulnerabilidades conocidas; Quality Gate PASSED. La corrida Sonar repite 201 pruebas de la suite, no suma casos distintos. Azure CD confirma el paquete ./backend desplegado con éxito en el slot Production; esto no verifica frontend/API institucional ni aceptación funcional en vivo. Las PR #37–48 están cerradas sin merge individual: #51 integra actualizaciones compatibles y rechaza pydantic-core independiente. PR #52 permanece abierta con CI fallido exclusivamente en Sonar por autorización/organización, no es el CI de master. README mantiene los mismos endpoints y añade configuración de seguridad.

**Próximos pasos:**
- Acreditar configuración de DRIFT_ADMIN_TOKEN y proxy confiable en Azure/Dokploy, y registrar pruebas positivas/negativas de sincronización, métricas y límite de tasa junto al recorrido frontend/API institucional. El éxito Azure no sustituye ese recorrido.
- Resolver el acceso Sonar para PR de Dependabot sin eludir controles y regenerar/ensayar requirements.lock al evaluar PR #52; sus cambios de requirements.txt no quedan probados por jobs que instalan versiones fijas.
- Revisar los avisos de Schemathesis en búsqueda, sincronización y compatibilidad: el verde contractual incluye rechazo mayoritario de datos generados en esas tres operaciones. Conservar conteos separados de casos contractuales, suite pytest y reejecución de cobertura.
- Reconciliar la afirmación de retención máxima de IP de 60 segundos con la limpieza efectiva: security.py depura una clave cuando vuelve a usarse y limpia inactivas al alcanzar max_clients, no hay caducidad global cada 60 s. Mantener explícitos los límites por proceso y el backend Vercel sin limitador.
- Definir retención/redacción de logs y resolver el pendiente de registro de consultas; el aviso/documento es evidencia del equipo, no validación jurídica ni aceptación funcional.

**Issues:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. README mantiene origen institucional frontend/API y alternativas Azure API y Vercel frontend; añade token para métricas/sincronización. Azure CD de esta punta exitoso no acredita publicación institucional ni aceptación funcional.

**PR consultadas:** [#52](https://github.com/ISCOUTB/AS_202620_Drift/pull/52): abierta; [#51](https://github.com/ISCOUTB/AS_202620_Drift/pull/51): fusionada 2026-11-01T06:59:39Z; [#50](https://github.com/ISCOUTB/AS_202620_Drift/pull/50): fusionada 2026-11-01T06:34:21Z; [#49](https://github.com/ISCOUTB/AS_202620_Drift/pull/49): fusionada 2026-11-01T06:19:58Z

**CI consultado:** [Build and deploy Python app to Azure Web App - drift-utb-202620 41282982275](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982275): success (misma punta); [CI 41282982366](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982366): success (misma punta); [CI 41283105843](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283105843): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Drift/blob/a5391102b14ccc879ef624af9f61f6818d163586/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Drift/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Drift/pulls) · [a5391102b14ccc879ef624af9f61f6818d163586](https://github.com/ISCOUTB/AS_202620_Drift/commit/a5391102b14ccc879ef624af9f61f6818d163586) · [41283092379](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283092379) · [41283090108](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283090108) · [41283090906](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283090906) · [41283089037](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283089037) · [41283088572](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283088572) · [41283085609](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283085609) · [41283085267](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283085267) · [41283082907](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283082907) · [41283080604](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283080604) · [41283081202](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283081202) · [41283078364](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283078364) · [41282986169](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282986169) · [41282986325](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282986325) · [41282986327](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282986327) · [41282982275](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982275) · [41282982366](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982366) · [41283105843](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283105843) · [d9a181630f9c7cc9daf3d58705092b245cdc7c73...a5391102b14ccc879ef624af9f61f6818d163586](https://github.com/ISCOUTB/AS_202620_Drift/compare/d9a181630f9c7cc9daf3d58705092b245cdc7c73...a5391102b14ccc879ef624af9f61f6818d163586) · [security.py](https://github.com/ISCOUTB/AS_202620_Drift/blob/a5391102b14ccc879ef624af9f61f6818d163586/backend/app/infrastructure/api/security.py) · [main.py](https://github.com/ISCOUTB/AS_202620_Drift/blob/a5391102b14ccc879ef624af9f61f6818d163586/backend/app/main.py) · [ci.yml](https://github.com/ISCOUTB/AS_202620_Drift/blob/a5391102b14ccc879ef624af9f61f6818d163586/.github/workflows/ci.yml) · [privacidad.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/a5391102b14ccc879ef624af9f61f6818d163586/docs/seguridad/privacidad.md) · [modelo-amenazas.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/a5391102b14ccc879ef624af9f61f6818d163586/docs/seguridad/modelo-amenazas.md) · [s13-analisis-dependencias.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/a5391102b14ccc879ef624af9f61f6818d163586/docs/evidencias/s13-analisis-dependencias.md) · [arc42-11-riesgos-y-deuda-tecnica.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/a5391102b14ccc879ef624af9f61f6818d163586/docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_Drift/blob/a5391102b14ccc879ef624af9f61f6818d163586/deploy/compose.lab.yaml) · [49](https://github.com/ISCOUTB/AS_202620_Drift/pull/49) · [50](https://github.com/ISCOUTB/AS_202620_Drift/pull/50) · [51](https://github.com/ISCOUTB/AS_202620_Drift/pull/51) · [52](https://github.com/ISCOUTB/AS_202620_Drift/pull/52) · [124778519332](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982275/job/124778519332) · [124778571532](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982275/job/124778571532) · [124778519723](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982366/job/124778519723) · [124778519833](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982366/job/124778519833) · [124778613934](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982366/job/124778613934) · [124778739392](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41282982366/job/124778739392) · [124778870297](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283105843/job/124778870297) · [124778870452](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283105843/job/124778870452) · [124778976203](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283105843/job/124778976203) · [124779095051](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41283105843/job/124779095051) · [Antecedentes](seguimiento-s12-2026-10-31.md#drift).

<a id="elmapita"></a>

## ElMapita

Rama **main**, [fc0f186153d117a5b0d9db715d521e154a8a2ef2](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/fc0f186153d117a5b0d9db715d521e154a8a2ef2), fecha del commit 2026-10-30T01:52:42Z (UTC). Observación: 2026-11-01T13:02:35.911Z.

Revalidación del 1/nov: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al 31/oct. Se conserva el feedback anterior.

**Próximos pasos:**
- Documentar en README la URL exacta bajo iscoutb.dev, separando API y frontend; aportar evidencia fechada del despliegue de esta punta.
- Hacer vinculante el E2E de backend, atender los 28 hallazgos de analyze y restablecer SonarCloud/Quality Gate antes de describir el CI como completo.
- Reconciliar docs/ia.md con los commits publicados y validar en dispositivos reales permisos de ubicación, guía de llegada, calibración y cambio de idioma.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README no publica URL pública concreta; los placeholders/locales no cuentan. Se conserva confirmación docente: presentó y funciona, distinta de la publicación de la punta.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z

**CI consultado:** [CI 40988421889](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40988421889): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/fc0f186153d117a5b0d9db715d521e154a8a2ef2/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ElMapita/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ElMapita/pulls) · [fc0f186153d117a5b0d9db715d521e154a8a2ef2](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/fc0f186153d117a5b0d9db715d521e154a8a2ef2) · [40988421889](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40988421889) · [Antecedentes](seguimiento-s12-2026-10-31.md#elmapita).

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), fecha del commit 2026-10-26T03:57:38Z (UTC). Observación: 2026-11-01T13:02:36.152Z.

Revalidación del 1/nov: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al 31/oct. Se conserva el feedback anterior.

**Próximos pasos:**
- Corregir empaquetado/import del prototipo para que pytest general pueda recolectarlo y repetir contrato/build.
- Mantener separada evidencia de correo simulado de envío real; definir persistencia/proveedor antes de integrar.
- Documentar URL institucional concreta y alcance de rutas PostgreSQL frente a las heredadas en memoria.

**Issues:** 1 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README conserva host asignado como marcador; no hay URL pública concreta.

**PR consultadas:** [#3](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/3): fusionada 2026-10-26T03:57:38Z; [#2](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/2): fusionada 2026-09-28T02:39:59Z

**CI consultado:** [CI 40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): failure (misma punta); [Taller mensajes y consistencia 40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_EnAgenda/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_EnAgenda/pulls) · [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b) · [40266609521](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521) · [40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410) · [40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284) · [Antecedentes](seguimiento-s12-2026-10-31.md#enagenda).

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, [5fa232b25e3122474291e5cc41ead96f9b567856](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/5fa232b25e3122474291e5cc41ead96f9b567856), fecha del commit 2026-10-26T04:21:32Z (UTC). Observación: 2026-11-01T13:02:36.122Z.

Revalidación del 1/nov: sin novedades sustantivas de punta, README, issues, PR ni resultados de CI frente al 31/oct. Se conserva el feedback anterior.

**Próximos pasos:**
- Ejecutar integración PostgreSQL con base aislada y evidenciar el recorrido Flutter/API.
- Conservar límites del prototipo y no afirmar durabilidad, broker ni caché operativa a partir del diseño.

**Issues:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README declara backend institucional, no acredita una interfaz Flutter pública.

**PR consultadas:** [#18](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/18): fusionada 2026-10-26T00:15:00Z; [#17](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/17): fusionada 2026-10-19T01:09:26Z

**CI consultado:** [CI 40268686360](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5fa232b25e3122474291e5cc41ead96f9b567856/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pulls) · [5fa232b25e3122474291e5cc41ead96f9b567856](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/5fa232b25e3122474291e5cc41ead96f9b567856) · [40268686360](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/40268686360) · [Antecedentes](seguimiento-s12-2026-10-31.md#gimnasioutb).

<a id="inventrack"></a>

## InvenTrack

Rama **main**, [110a73718ce4b2833efead3e50cbc160b3757e5d](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/110a73718ce4b2833efead3e50cbc160b3757e5d), fecha del commit 2026-10-31T19:17:16Z (UTC). Observación: 2026-11-01T13:02:36.228Z.

Desde el 31/oct integra tres commits: actualiza dependencias y lockfile, añade pip-audit con hashes al CI e incorpora política de exposición en producción. Sin token, /metrics y documentación interna responden 404; /productos e /inventario quedan deshabilitados con 503 por defecto. Compose y Render fijan producción y negocio deshabilitado; el token interno no implementa usuarios/roles. La punta pasa 34 pruebas (dos nuevas de política), reejecuta una de contrato ya incluida, supera Quality Gate y pip-audit no encuentra vulnerabilidades conocidas. README cambia para describir restricciones pero mantiene API institucional/Render; no se verificó redespliegue ni funcionamiento público. La evidencia S13 añade responsables, pero conserva pasajes de escaneo pendiente y hallazgos previos; S12 de despliegue no cambia y aún cita el corte anterior.

**Próximos pasos:**
- Actualizar evidencia S13 y tabla de amenazas con dependencias/lock/run actuales y retirar afirmaciones obsoletas de escaneo pendiente; conciliar también README que más abajo sigue declarando /docs y /metrics disponibles.
- Aportar hash realmente servido y comprobaciones fechadas de /health, 404 sin token, acceso interno autorizado y 503 previsto en rutas de negocio. No confundir el bloqueo preventivo con una caída ni con autenticación/autorización completa.
- Conservar negocio deshabilitado hasta identidad/roles, auditoría de actor y pruebas negativas; documentar gestión del token interno y ampliar cobertura de /redoc, /openapi.json y rutas /inventario.
- Mantener límites de persistencia, idempotencia, locks, broker y DLQ en memoria; completar recuperación durable y retención/redacción de logs antes de datos reales.

**Issues:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: 7 completed.

**README:** Institucional. README conserva API institucional y Render, ahora declara superficies internas restringidas y datos de negocio deshabilitados hasta autenticación/autorización. No se verificó que esta configuración esté servida; no acredita frontend.

**PR consultadas:** Sin PR en la consulta.

**CI consultado:** [Run Tests 41233503062](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41233503062): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/110a73718ce4b2833efead3e50cbc160b3757e5d/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_InvenTrack/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_InvenTrack/pulls) · [110a73718ce4b2833efead3e50cbc160b3757e5d](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/110a73718ce4b2833efead3e50cbc160b3757e5d) · [41233503062](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41233503062) · [16cdc6e98960957c38a8b39e53b512d5c56a8f71...110a73718ce4b2833efead3e50cbc160b3757e5d](https://github.com/ISCOUTB/AS_202620_InvenTrack/compare/16cdc6e98960957c38a8b39e53b512d5c56a8f71...110a73718ce4b2833efead3e50cbc160b3757e5d) · [main.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/110a73718ce4b2833efead3e50cbc160b3757e5d/app/main.py) · [test_health.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/110a73718ce4b2833efead3e50cbc160b3757e5d/tests/test_health.py) · [test.yml](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/110a73718ce4b2833efead3e50cbc160b3757e5d/.github/workflows/test.yml) · [requirements.txt](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/110a73718ce4b2833efead3e50cbc160b3757e5d/requirements.txt) · [evidencia-seguridad-s13.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/110a73718ce4b2833efead3e50cbc160b3757e5d/docs/evidencia-seguridad-s13.md) · [evidencia-despliegue-s12.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/110a73718ce4b2833efead3e50cbc160b3757e5d/docs/evidencia-despliegue-s12.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/110a73718ce4b2833efead3e50cbc160b3757e5d/deploy/compose.lab.yaml) · [render.yaml](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/110a73718ce4b2833efead3e50cbc160b3757e5d/render.yaml) · [124632372693](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41233503062/job/124632372693) · [124632372870](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41233503062/job/124632372870) · [Antecedentes](seguimiento-s12-2026-10-31.md#inventrack).

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [d02facd0ad6d3edace4b5585b3a961d372a9a76a](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/d02facd0ad6d3edace4b5585b3a961d372a9a76a), fecha del commit 2026-10-30T14:10:01Z (UTC). Observación: 2026-11-01T13:05:40.185Z.

Misma punta master y mismo README que el 31/oct. La novedad está en dependencias sin integrar: PR #29 cerrada sin fusión, #30 abierta (38 actualizaciones frontend) y #28 rebasada (3 actualizaciones backend). Sus diffs solo modifican package.json/package-lock.json de cada componente. Los nuevos runs de #28 y #30 pasan test, frontend (lint/build), contract-test y audit; sonar se omite en ambas PR. Continúan diez PR abiertas de dependencias. No hay nuevo despliegue ni cambio del código integrado: el último deploy sigue siendo 41068478596 de otra revisión, con el límite ya señalado en el informe del 31/oct.

**Próximos pasos:**
- Revisar compatibilidad de #28/#30 y el resto de PR abiertas; no atribuir sus checks a master ni presentar sonar omitido como Quality Gate nuevo.
- Corregir selección de rama del webhook y vincular commit servido; health=200 tras «Branch Not Match» no acredita redespliegue.
- Publicar frontend/API vigentes bajo iscoutb.dev en README y acreditar sesión STRIDE, validación de ADR, rotación y límites antes de medir escrituras.

**Issues:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. Motivos: 14 completed.

**README:** Sin URL concreta. Solo Azure explícitamente retirado; ninguna URL pública vigente concreta en README raíz.

**PR consultadas:** [#30](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/30): abierta; [#28](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/28): abierta; [#25](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/25): abierta; [#27](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/27): abierta; [#26](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/26): abierta; [#23](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/23): abierta; [#21](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/21): abierta; [#20](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/20): abierta; [#17](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/16): abierta; [#29](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/29): cerrada sin merge; [#19](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/19): cerrada sin merge; [#22](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/22): cerrada sin merge

**CI consultado:** [CI LaPlacita 41260671606](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41260671606): success (otra revisión o PR); [CI LaPlacita 41069624061](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41069624061): success (misma punta); [Deploy Dokploy (laboratorio de la U) 41068478596](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41068478596): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/d02facd0ad6d3edace4b5585b3a961d372a9a76a/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_LaPlacita/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_LaPlacita/pulls) · [41260671606](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41260671606) · [41260509747](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41260509747) · [41069624061](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41069624061) · [41068478596](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41068478596) · [28](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/28) · [29](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/29) · [30](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/30) · [29#issuecomment-6551685405](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/29#issuecomment-6551685405) · [Antecedentes](seguimiento-s12-2026-10-31.md#laplacita).

<a id="lostvault"></a>

## LostVault

Rama **main**, [3a6e157110bd3c63e76de9cce68c63991e747468](https://github.com/ISCOUTB/AS_202620_LostVault/commit/3a6e157110bd3c63e76de9cce68c63991e747468), fecha del commit 2026-10-26T04:46:40Z (UTC). Observación: 2026-11-01T13:05:40.185Z.

Sin cambios de punta, README, issues, PR ni CI frente al 31/oct. PR #21 sigue abierta; los tres workflows de main continúan success. Se conservan los límites previos: backend en memoria, taller SQLite aislado y PostgreSQL/outbox productivos propuestos; no se ha aportado evidencia nueva de producción.

**Próximos pasos:**
- Implementar y validar persistencia/eventos del flujo real antes de llamar productivo al taller aislado.
- Aclarar implementación desplegada y cobertura de api/; publicar frontend/API institucionales y verificar autorización y consistencia.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de trabajo o despliegue.

**PR consultadas:** [#21](https://github.com/ISCOUTB/AS_202620_LostVault/pull/21): abierta; [#22](https://github.com/ISCOUTB/AS_202620_LostVault/pull/22): fusionada 2026-10-26T04:46:41Z; [#20](https://github.com/ISCOUTB/AS_202620_LostVault/pull/20): fusionada 2026-10-26T01:52:55Z; [#19](https://github.com/ISCOUTB/AS_202620_LostVault/pull/19): fusionada 2026-10-20T16:16:34Z

**CI consultado:** [Flutter checks 40271156565](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40271156565): success (otra revisión o PR); [Backend checks 40271156552](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40271156552): success (otra revisión o PR); [Build 40270806589](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589): success (misma punta); [Flutter checks 40270806466](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466): success (misma punta); [Backend checks 40270806424](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424): success (misma punta); [Build 40270552931](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270552931): skipped (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LostVault/blob/3a6e157110bd3c63e76de9cce68c63991e747468/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_LostVault/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_LostVault/pulls) · [40270806589](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806589) · [40270806466](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806466) · [40270806424](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/40270806424) · [Antecedentes](seguimiento-s12-2026-10-31.md#lostvault).

<a id="mapsutb"></a>

## mapsutb

Rama **master**, [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), fecha del commit 2026-10-25T14:04:14Z (UTC). Observación: 2026-11-01T13:05:40.185Z.

Misma punta, README, issues y PR que el 31/oct. Nuevas ejecuciones programadas de sonda y sincronización Sonar terminan success sobre la misma punta (últimas: 41306379026 y 41305531595). Es continuidad operativa de los workflows, no nuevo desarrollo, redespliegue ni aceptación funcional independiente. Se conservan los 54 issues cerrados.

**Próximos pasos:**
- Mantener evidencia reproducible de recarga/reintento del grafo y distinguir sonda de disponibilidad de aceptación funcional.
- Publicar frontend bajo iscoutb.dev y actualizar README; no confundir mapsutb con ElMapita.

**Issues:** 0 abiertas / 54 cerradas; 0 abiertas sin asignar. Motivos: 54 completed.

**README:** Externo. Frontend Firebase externo; sonda CI disponible, sin nueva aceptación funcional propia.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z

**CI consultado:** [Sonda de disponibilidad (métrica Escenario 6) 41306379026](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41306379026): success (misma punta); [Sincronizar hallazgos de Sonar a GitHub Issues 41305531595](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41305531595): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_mapsutb/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_mapsutb/pulls) · [41306379026](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41306379026) · [41305531595](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41305531595) · [Antecedentes](seguimiento-s12-2026-10-31.md#mapsutb).

<a id="pideutb"></a>

## PideUtb

Rama **master**, [e81e272b20498968b1016a261dee8bce250422da](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/e81e272b20498968b1016a261dee8bce250422da), fecha del commit 2026-10-30T06:16:11Z (UTC). Observación: 2026-11-01T13:05:40.185Z.

Sin cambios de punta, README, issues, PR ni CI frente al 31/oct. Se mantienen integradas PR #35–38 y exitoso el CI 41013098666; no son avances nuevos del 1/nov. Se conserva la actualización presentada y los despliegues según docente, sin atribuir a las pruebas locales de CI aceptación de producción, cobros reales ni ejecución de migración/configuración 008.

**Próximos pasos:**
- Aportar commit servido y aplicación de configuración/migración 008; verificar recorrido cliente–pasarela de pruebas–mostrador en entorno objetivo antes de la demo planificada para el 3/nov.
- Verificar retiro o mitigación de todos los servicios legados; no inferirlo de no-server reportado para uno.
- Conservar pruebas de retorno/caducidad/limpieza y distinguir 556 Python aprobadas/3 omitidas, 26 recorridos locales y subconjuntos reejecutados del CI previamente acreditado.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. README documenta frontend/panel y API bajo iscoutb.dev. Docente confirma presentación/despliegues; no se repitió verificación funcional de producción. Pruebas de navegador verificadas en CI usan localhost y pasarela simulada, no cobros reales.

**PR consultadas:** [#38](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/38): fusionada 2026-10-30T06:16:11Z; [#37](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/37): fusionada 2026-10-30T03:53:01Z; [#36](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/36): fusionada 2026-10-29T21:41:18Z

**CI consultado:** [CI 41013098666](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41013098666): success (misma punta); [CI 41012632402](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41012632402): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_PideUtb/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_PideUtb/pulls) · [41013098666](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41013098666) · [Antecedentes](seguimiento-s12-2026-10-31.md#pideutb).

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [40be256f52d74ad8c9148886f040845658a38855](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/40be256f52d74ad8c9148886f040845658a38855), fecha del commit 2026-10-30T12:43:07Z (UTC). Observación: 2026-11-01T13:05:40.185Z.

Sin cambios frente al 31/oct: master y README conservan 40be256; PR #76 sigue abierta y draft en fd7a3cc, sin merge. Sus seis workflows oficiales permanecen success; Web/Android conserva intento 2 exitoso, no falla vigente. Los cinco workflows de master también siguen success. El ensayo aislado PASS ya documentado no es novedad, publicación GHCR ni despliegue; permanecen respaldo/restauración, montajes, acceso GHCR, rollback y autorización de promoción pendientes.

**Próximos pasos:**
- Revisar #76 y conciliar cuerpo/README del fork con checks oficiales; no confundir head de PR o merge de prueba con integración a master.
- Acreditar respaldo/restauración de MySQL/uploads, montajes, acceso GHCR y rollback; vincular commit/digest/cabecera del servicio real antes de promover.
- Publicar y aceptar funcionalmente frontend institucional solo bajo autorización; mantener GitHub Pages como frontend vigente documentado mientras tanto.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional (parcial: API; frontend externo). Cumplimiento parcial: API bajo iscoutb.dev y frontend GitHub Pages externo. PR #76 prepara /app/ pero continúa draft, sin merge ni despliegue acreditado. CI/ensayos aislados no prueban promoción en Dokploy; Azure es histórico.

**PR consultadas:** [#76](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/76): abierta (borrador); [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60): abierta; [#1](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/1): abierta; [#75](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/75): fusionada 2026-10-30T12:43:07Z; [#74](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/74): fusionada 2026-10-30T11:53:43Z; [#73](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/73): fusionada 2026-10-30T11:12:50Z

**CI consultado:** [Flujo real Web y Android 41103146052](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103146052): success (otra revisión o PR); [S10 contrato del cliente en despliegue publico 41103146015](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103146015): success (otra revisión o PR); [Pruebas del backend 41103145836](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103145836): success (otra revisión o PR); [Web institucional aislada 41103145483](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103145483): success (otra revisión o PR); [Validación Flutter MVP 41103145458](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103145458): success (otra revisión o PR); [Compose y persistencia del MVP 41103145446](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103145446): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/40be256f52d74ad8c9148886f040845658a38855/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pulls) · [41103146052](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103146052) · [41103146015](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103146015) · [41103145836](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103145836) · [41103145483](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103145483) · [41103145458](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103145458) · [41103145446](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41103145446) · [41057456301](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456301) · [41057456260](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456260) · [41057456247](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456247) · [41057456331](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456331) · [41057456304](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41057456304) · [76](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/76) · [Antecedentes](seguimiento-s12-2026-10-31.md#proyecto_campusmarket).

<a id="recobra"></a>

## Recobra

Rama **master**, [0dda9abd2c76ef9b10724221225c0ed228197c39](https://github.com/ISCOUTB/AS_202620_Recobra/commit/0dda9abd2c76ef9b10724221225c0ed228197c39), fecha del commit 2026-10-29T02:32:33Z (UTC). Observación: 2026-11-01T13:05:40.185Z.

Sin cambios de punta, README, issues, PR ni CI frente al 31/oct. Diez PR de Dependabot continúan abiertas y no integradas; el CI 40806972927 de la punta sigue success. Se conserva presentación confirmada por docente y los controles S13 previamente revisados, sin convertir avisos aceptados en dependencias libres de vulnerabilidades ni dar por ejecutadas rotación y respaldo programado.

**Próximos pasos:**
- Acreditar acciones operativas de protección/rotación y respaldo programado sin publicar credenciales ni datos personales.
- Revisar y probar dependencias, mantener diferenciados avisos aceptados/mitigados y respetar vencimiento documentado.
- Aportar aceptación funcional en despliegue de límites, origen, cabeceras y avisos, separada del CI.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README aclara vitrina, Flutter Web y API en mismo host institucional; no se añade auditoría funcional.

**PR consultadas:** [#10](https://github.com/ISCOUTB/AS_202620_Recobra/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_Recobra/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_Recobra/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_Recobra/pull/7): abierta; [#6](https://github.com/ISCOUTB/AS_202620_Recobra/pull/6): abierta; [#5](https://github.com/ISCOUTB/AS_202620_Recobra/pull/5): abierta; [#3](https://github.com/ISCOUTB/AS_202620_Recobra/pull/3): abierta; [#2](https://github.com/ISCOUTB/AS_202620_Recobra/pull/2): abierta; [#4](https://github.com/ISCOUTB/AS_202620_Recobra/pull/4): abierta; [#1](https://github.com/ISCOUTB/AS_202620_Recobra/pull/1): abierta

**CI consultado:** [ci 40806972927](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927): success (misma punta); [ci 40806929507](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806929507): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Recobra/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Recobra/pulls) · [40806972927](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927) · [Antecedentes](seguimiento-s12-2026-10-31.md#recobra).

<a id="routb"></a>

## ROUTB

Rama **master**, [22c2953553a9fc3518fb63576ac622d8bf5e80df](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/22c2953553a9fc3518fb63576ac622d8bf5e80df), fecha del commit 2026-10-25T23:22:49Z (UTC). Observación: 2026-11-01T13:05:40.185Z.

Misma punta, README, issues y PR que el 31/oct. La nueva ejecución programada de purga 41287619351 termina success sobre la misma punta; no representa código nuevo ni prueba aplicación de migración 010. Se preservan avance entregado según docente, garantía de solicitud activa única integrada y límites previamente descritos: migración objetivo no acreditada y taller de notificaciones aislado/en memoria.

**Próximos pasos:**
- Aplicar y verificar migración 010 en entorno autorizado antes de atribuir al despliegue la unicidad implementada.
- Mantener explícita pérdida de cola al reiniciar y no integración productiva del prototipo; conservar diferencia entre gate Sonar del bot y job Actions echo.
- Aportar aceptación funcional del entorno desplegado.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional (backend). Backend institucional y guía actualizada a Dokploy; aplicación de migración 010 al entorno objetivo aún no confirmada.

**PR consultadas:** [#54](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/54): fusionada 2026-10-25T23:22:50Z; [#53](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/53): fusionada 2026-10-25T18:04:34Z; [#52](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/52): fusionada 2026-10-23T14:47:48Z

**CI consultado:** [Purga periódica de datos de ubicación 41287619351](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41287619351): success (misma punta); [CI ROUTB 40244499934](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934): success (misma punta); [CI ROUTB 40244472745](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244472745): success (otra revisión o PR); [Purga periódica de datos de ubicación 40175780746](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40175780746): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/22c2953553a9fc3518fb63576ac622d8bf5e80df/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ROUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ROUTB/pulls) · [41287619351](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41287619351) · [40244499934](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40244499934) · [Antecedentes](seguimiento-s12-2026-10-31.md#routb).

<a id="shareu"></a>

## ShareU

Rama **master**, [2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767), fecha del commit 2026-10-25T22:52:08Z (UTC). Observación: 2026-11-01T13:05:40.185Z.

Sin cambios de punta, README, issues, PR ni CI frente al 31/oct. PR #22/#23 siguen abiertas; el workflow de la punta 40242189282 permanece failure. Persisten diez issues abiertos (cinco sin asignar). La deriva README SQLite frente al repositorio Firestore y las pruebas con cliente sustituido ya fueron reportadas; no hay nueva prueba de persistencia real ni despliegue.

**Próximos pasos:**
- Conciliar README/C4/ADR con Firestore y publicar URLs institucionales concretas de frontend/API.
- Corregir workflow con evidencia de pruebas del repositorio y resiliencia; no atribuir falla exclusivamente a Sonar ni presentar cliente sustituido como persistencia productiva.

**Issues:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: 10 completed.

**README:** Sin URL concreta. Placeholders Vercel/Render y localhost, no URL pública concreta vigente.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z

**CI consultado:** [.github/workflows/tests.yml 40242189282](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282): failure (misma punta); [.github/workflows/tests.yml 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458): failure (otra revisión o PR); [Tests 36479388452](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479388452): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ShareU/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ShareU/pulls) · [40242189282](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282) · [Antecedentes](seguimiento-s12-2026-10-31.md#shareu).

<a id="sistema-de-calificacion-automatica"></a>

## Calificación automática

Rama **master**, [d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc), fecha del commit 2026-10-30T06:04:55Z (UTC). Observación: 2026-11-01T13:05:14.807Z.

Sin cambios frente al 31/oct en master, README, issues, PR, CI ni rama despliegue. Se mantiene el desfase README Render frente a endpoints institucionales documentados fuera de él. Publicación de rama compilada no acredita ejecución final en Dokploy ni recorrido público.

**Próximos pasos:**
- Actualizar README con frontend y API institucionales y relación vigente con Render.
- Acreditar revisión servida y recorrido frontend→API→worker.
- Mantener pendientes recuperación/respaldo/concurrencia y alcance OMR según corte31.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. README externo; no confundir ausencia de enlaces institucionales en README con ausencia de trabajo.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin merge

**CI consultado:** [CI 41012021649](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41012021649): success (misma punta); [CI 41010670473](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41010670473): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/d6b87a7d13adac8527b9bf3360ab142e5d2a8ffc/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pulls) · [Antecedentes](seguimiento-s12-2026-10-31.md#sistema-de-calificacion-automatica).

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [04151d0ddbd598851d931f449eb4bad00eb7a052](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/04151d0ddbd598851d931f449eb4bad00eb7a052), fecha del commit 2026-11-01T00:30:00Z (UTC). Observación: 2026-11-01T13:05:14.807Z.

19 commits incorporan seis alertas de aplicación en memoria y logs con runbook, validación estructural reproducible del modelo de amenazas y verificación del lock Dart/OSV en CI. El job de pruebas de la punta exacta acredita 324 pruebas Python, build/smoke, auditoría de ambos locks Python y consulta OSV de paquetes Pub sin avisos. Sin embargo, Quality Gate termina ERROR por new_security_rating=3 frente a umbral 1; CI failure y CD skipped. README y PR/issues sin cambio. Se conserva que TAIA presentó y funciona, confirmado por el docente; no se verificó en vivo ni se acredita despliegue de esta punta.

**Próximos pasos:**
- Diagnosticar y resolver los hallazgos de seguridad de Sonar y aportar Quality Gate OK de la revisión corregida; no confundir 324 pruebas exitosas con CI íntegro verde.
- Actualizar README y ADR-0011 para reflejar cliente inicial, webhook, métricas JWT, respaldo y alertas reales; conservar antecedentes.
- Conservar alcance de alertas en memoria/por proceso, sin notificación externa, y validar operación y recuperación de alertas en el entorno servido; el runbook declara riesgo residual medio.
- Agregar pruebas/análisis Flutter al pipeline y validar flujos integrados en dispositivo; el verificador de dependencias Dart no ejecuta Flutter.
- Mantener abiertos consentimiento T-02 y renovación/revocación T-08; vincular revisión efectivamente servida con evidencia de recorrido.

**Issues:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: 4 completed.

**README:** Institucional. README permanece idéntico. Solo API institucional, no frontend público; mantiene Render alternativo y descripción desactualizada de Flutter.

**PR consultadas:** [#17](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/17): fusionada 2026-10-30T22:18:28Z; [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z

**CI consultado:** [CD 41257615761](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41257615761): skipped (misma punta); [CI 41257504570](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41257504570): failure (misma punta); [CD 41218318236](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41218318236): skipped (otra revisión o PR); [CI 41218143081](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41218143081): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/04151d0ddbd598851d931f449eb4bad00eb7a052/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pulls) · [Antecedentes](seguimiento-s12-2026-10-31.md#taia_-task-artificial-intelligence-assistant).

<a id="tienda-virtual-utb"></a>

## Tienda virtual UTB

Rama **main**, [647bcbd413354775e85a9444f97a2db82725c5f1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/647bcbd413354775e85a9444f97a2db82725c5f1), fecha del commit 2026-10-25T16:53:06Z (UTC). Observación: 2026-11-01T13:05:14.807Z.

Sin cambios frente al31/oct en punta, README, issues, PR ni CI. Se conserva URL sslip temporal y alcance de CI ya documentado; no afirmar Quality Gate nuevo ni caché implementada.

**Próximos pasos:**
- Reemplazar URL temporal por subdominio institucional con TLS válido.
- Restablecer Sonar/Quality Gate verificable; medir invalidación/concurrencia antes de implementar la caché propuesta.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Solo frontend recibe dominio público según README; backend no público. Sin prueba viva ni evasión de aviso TLS.

**PR consultadas:** [#12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/12): fusionada 2026-10-25T02:58:28Z; [#11](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/11): fusionada 2026-10-24T20:15:26Z; [#10](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/10): fusionada 2026-10-24T19:40:05Z

**CI consultado:** [Pruebas 40213830995](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40213830995): success (misma punta); [Pruebas 40212692658](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40212692658): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/647bcbd413354775e85a9444f97a2db82725c5f1/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pulls) · [Antecedentes](seguimiento-s12-2026-10-31.md#tienda-virtual-utb).

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [31932f0006542c6f3f6222071bb1a9c36b6f888a](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/31932f0006542c6f3f6222071bb1a9c36b6f888a), fecha del commit 2026-10-26T06:03:01Z (UTC). Observación: 2026-11-01T13:05:14.807Z.

Sin cambios frente al31/oct en punta, README, issues, PR ni CI. README raíz sin URL pública concreta. Se mantiene evidencia previa de 78 pruebas en tests/ y migraciones/reinicio exitosos; no reabrir el antiguo bloqueo Alembic.

**Próximos pasos:**
- Eliminar fallback destructivo a DATABASE_URL o validar inequívocamente base de pruebas.
- Documentar y verificar worker/notificación real; actualizar README con URL y estado PostgreSQL/pruebas.
- Conservar distinción entre tests/ y app/tests/, caché propuesta y flujos cliente no acreditados.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. Sin endpoint público vigente en README; APK publicado no acredita sitio institucional.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/4): fusionada 2026-10-26T04:35:44Z; [#3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/3): fusionada 2026-10-25T18:20:31Z; [#2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/2): fusionada 2026-10-06T06:08:06Z

**CI consultado:** [UTB Tracker CI 40278118926](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926): success (misma punta); [UTB Tracker CI 40269883908](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40269883908): success (otra revisión o PR); [Release APK 40132197969](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132197969): success (otra revisión o PR); [.github/workflows/ci.yml 40066463106](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40066463106): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pulls) · [Antecedentes](seguimiento-s12-2026-10-31.md#utb_tracker).

<a id="uniteam"></a>

## uniTeam

Rama **master**, [0a44bd5a8d9374423b08fef87e46672cd6ad501b](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/0a44bd5a8d9374423b08fef87e46672cd6ad501b), fecha del commit 2026-10-26T00:55:53Z (UTC). Observación: 2026-11-01T13:05:14.807Z.

Punta, README, issues y PR sin cambios frente al31/oct. Nuevas sondas programadas vuelven a fallar: último run41306168069, seis comprobaciones contra frontend/API antiguos de Render según log. Es repetición de la misma evidencia, no cambio sustantivo ni prueba de caída de DuckDNS.

True

**Próximos pasos:**
- Actualizar sonda a direcciones DuckDNS vigentes y repetir seis comprobaciones antes de interpretar salud.
- Publicar frontend y API bajo iscoutb.dev; conservar taller SQLite separado y caché como propuesta.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Externo. Frontend/API DuckDNS en README; sonda usa Render, por lo que no determina disponibilidad actual de DuckDNS.

**PR consultadas:** [#4](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/4): fusionada 2026-10-04T21:23:33Z; [#2](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/2): fusionada 2026-09-14T01:20:18Z; [#10](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/10): fusionada 2026-10-26T00:55:53Z

**CI consultado:** [Comprobación del despliegue 41306168069](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41306168069): failure (misma punta); [CI 40251714762](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40251714762): success (misma punta); [CI 40251687342](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40251687342): cancelled (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0a44bd5a8d9374423b08fef87e46672cd6ad501b/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_uniTeam/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_uniTeam/pulls) · [Antecedentes](seguimiento-s12-2026-10-31.md#uniteam).

<a id="xald"></a>

## XALD

Rama **master**, [1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00](https://github.com/ISCOUTB/AS_202620_XALD/commit/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00), fecha del commit 2026-10-26T04:04:58Z (UTC). Observación: 2026-11-01T13:05:14.807Z.

Sin cambios frente al31/oct en master, README, issues, PR, CI ni experimental. Actividad lateral documental ya reportada no integrada en master; no es implementación nueva. Mantener distinción de CI exitoso en ambas ramas y deploy omitido en experimental.

**Próximos pasos:**
- Conciliar experimental con master sin reintroducir descripciones obsoletas.
- Activar ejecutor real de procesarPendientes y persistir cola/deduplicación; validar en dispositivo.
- Publicar API institucional y conservar evidencia verificable de revisión/run.

**Issues:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. Motivos: 5 completed; 1 duplicate.

**README:** Externo. Backend Render; no acredita frontend institucional ni recorrido funcional propio.

**PR consultadas:** [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z; [#24](https://github.com/ISCOUTB/AS_202620_XALD/pull/24): fusionada 2026-09-27T16:24:00Z

**CI consultado:** [Android CI 40798851273](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40798851273): success (otra revisión o PR); [Android CI 40267222501](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40267222501): success (misma punta); [.github/workflows/ci.yml 40250035779](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40250035779): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_XALD/blob/1eb5544b4835d103a4faa2c0574ce9f9cb3a0a00/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_XALD/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_XALD/pulls) · [Antecedentes](seguimiento-s12-2026-10-31.md#xald).

<a id="verifacts"></a>

## Verifacts

Rama **master**, [559612b61ee4cea46cef6d00f857d2e5c2794f03](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/559612b61ee4cea46cef6d00f857d2e5c2794f03), fecha del commit 2026-10-28T05:41:24Z (UTC). Observación: 2026-11-01T13:05:14.807Z.

Sin cambios frente al31/oct en punta, README, issues, PR ni CI. Mantener controles SSRF/límites/timeout/protección historial/TLS pendientes y retención/supresión como propuestas; Sonar no sustituye SCA reproducible. No acreditar redespliegue nuevo.

**Próximos pasos:**
- Aportar pip-audit/npm audit fechados con revisión y versiones resueltas.
- Implementar y probar controles prioritarios; distinguir propuesta de operación.
- Completar subdominio institucional/TLS y recorrido navegador/persistencia con trazabilidad.

**Issues:** 0 abiertas / 3 cerradas; 0 abiertas sin asignar. Motivos: 3 completed.

**README:** Externo. Referencia externa HTTP sslip; dominio institucional y certificado siguen declarados pendientes.

**PR consultadas:** Sin PR en la consulta.

**CI consultado:** [Tests 40639475382](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382): success (misma punta); [SonarCloud 40639475319](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319): success (misma punta); [SonarCloud 40636370321](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40636370321): success (otra revisión o PR); [Tests 40636370228](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40636370228): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Verifacts/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Verifacts/pulls) · [Antecedentes](seguimiento-s12-2026-10-31.md#verifacts).

