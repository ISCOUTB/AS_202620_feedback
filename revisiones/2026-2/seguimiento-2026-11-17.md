# Seguimiento de los 23 proyectos · 17 de noviembre de 2026

Consulta del **17/nov Colombia, 18/nov UTC**. Seguimiento factual desde el [6/nov](seguimiento-2026-11-06.md), sin cierre automático de semanas ni evaluación académica nueva. **Calificaciones, planillas y matrices históricas permanecen intactas.**

**41 issues abiertas y 138 cerradas**, excluyendo PR. README: **15 con algún endpoint institucional, 5 con enlaces externos y 3 sin URL pública concreta**. API institucional no equivale a frontend institucional. La falta de documentación no demuestra falta de trabajo.

Se conservan las confirmaciones docentes: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. No se presentan como pruebas funcionales nuevas.

Código integrado, reportes del equipo, CI, publicación y aceptación funcional son evidencias distintas. Las comprobaciones vivas se limitan a GET públicos de salud cuando se indica expresamente; no se ejecutó código estudiantil, no se iniciaron sesiones ni se probaron flujos con datos. Los estados y motivos de cierre son de GitHub Issues: no se obtuvieron estados personalizados de Projects. No se modificaron repositorios, issues ni despliegues estudiantiles.

[Detalle de issues](seguimiento-issues-2026-11-17.md) · [README y despliegues](seguimiento-despliegues-2026-11-17.md).

## Cambios relevantes

- Clubs UTB documenta API institucional y recupera CI; Drift concentra el despliegue en laboratorio. ShareU documenta dominios institucionales, aunque su propio registro aún indica 404. ElMapita documenta dominio fuera de README.
- AudioShare, ROUTB, UTB Tracker, XALD, uniTeam y el sistema de calificación incorporan funcionalidad; PideUtb integra recogida y avisos, y ya ejecuta Playwright. Los cambios integrados no certifican por sí solos funcionamiento desplegado.
- Dinamik mantiene fallo de Quality Gate; Gimnasio falla auditoría de dependencias; ElMapita permite continuar tras fallo de Sonar. PideUtb, ShareU y Tienda omiten análisis Sonar, y ROUTB no lo ejecuta realmente.
- uniTeam conserva una sonda dirigida a Render, distinta de sus URL DuckDNS documentadas. Su fallo no debe confundirse con CI ni atribuirse directamente a esos dominios actuales.
- EnAgenda conserva la misma punta principal; Verifacts solo cambia el formato de un enlace. Las mediciones y observaciones de pares se presentan como evidencia documental del equipo, no como mediciones repetidas ni calificaciones.

## AudioShare

Rama **master**, [8ac4492f734d8f89b00c7fbc0d735c663f6e435f](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/8ac4492f734d8f89b00c7fbc0d735c663f6e435f), 2026-11-17T06:24:07-05:00.

**Avances:** Se incorporan códigos de sala de seis dígitos, caducidad, llave de emisor, control de intentos, expulsión/salida, eventos y seek, junto con cliente Flutter actualizado. Se añade workflow APK y corrección compileSdk 36. docs/despliegue.md registra incidente transitorio de almacenamiento y pruebas del equipo; no son pruebas propias.

**Issues:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar; motivos {'completed': 2}. PR excluidas.

**README (institucional):** Frontend y API: https://audioshare.iscoutb.dev. README conserva una referencia histórica a /health sin commit; docs/despliegue.md declara redespliegue de 11d3972 el 17/nov.

**Verificación viva:** GET /health respondió HTTP 200, status ok y storage ok; startedAt 2026-11-17T18:58:02.144Z y commit unknown. Esta observación es posterior y distinta del registro documental de 11d3972: no permite acreditar la revisión actualmente servida.

**CI:** CI, Flutter, publicación de imagen y APK pasan para la punta. En APK el paso Publicar la Release está omitido; la construcción exitosa no acredita una Release pública.

[CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/44073650968): success · [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/44073650900): success · [APK de Android](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/44073650843): success · [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/44073650783): success

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/8): abierta

**Próximos pasos técnicos:** Acreditar SHA servido y contrastar README con redespliegue; verificar caducidad, IP detrás de proxy y sincronización/audio entre dispositivos. APK compilado no equivale a prueba en dispositivo.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/8ac4492f734d8f89b00c7fbc0d735c663f6e435f/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_AudioShare/issues) · [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions).

## Clubs_UTB

Rama **master**, [fef47d0b0daea094835aea09dac962bec6bfe4de](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/fef47d0b0daea094835aea09dac962bec6bfe4de), 2026-11-17T16:01:12-05:00.

**Avances:** Cambios en API y tests de UUID, login/registro, publicación, seguridad e idempotencia, ajustes de Docker y pantallas móviles de eventos. Los workflows que fallaban en el corte anterior ahora pasan.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar; motivos {}. PR excluidas.

**README (institucional):** README ahora documenta API https://api-linkclub.iscoutb.dev y /health. Declara interfaz móvil Flutter, no frontend web publicado.

**Verificación viva:** GET https://api-linkclub.iscoutb.dev/health: HTTP 200 con status ok y database online. Es comprobación puntual de salud, no recorrido de login/publicación/eventos.

**CI:** Backend tests y contrato pasan en la punta actual.

[Backend tests](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/44175387389): success · [contrato](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/44175387120): success

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta

**Próximos pasos técnicos:** Contrastar registro/login y permisos con el servicio publicado, y comprobar pantallas móviles en dispositivo; mantener documentación alineada con contrato y esquema desplegados.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/fef47d0b0daea094835aea09dac962bec6bfe4de/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/issues) · [CI](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions).

## DinamikUTB

Rama **master**, [aba565eeceb2f4f44331b26439480beb9ab4b179](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/aba565eeceb2f4f44331b26439480beb9ab4b179), 2026-11-17T13:56:38-05:00.

**Avances:** Fija Flutter 3.47.5 en CI/Pages, actualiza dependencias, retira servicio web del Compose y añade usuario de demostración administrador con prueba de creación. PR40 cerrado sin merge; aparecen PR49–51 abiertas.

**Issues:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar; motivos {'completed': 15}. PR excluidas.

**README (institucional):** API https://api-dinamikutb.iscoutb.dev; frontend externo https://iscoutb.github.io/AS_202620_DinamikUTB/. API institucional no convierte Pages en frontend institucional.

**Verificación viva:** GET https://api-dinamikutb.iscoutb.dev/health: HTTP 200, status ok. No se comprobó login, CORS ni recorrido desde Pages.

**CI:** Auditoría de dependencias pasa; CI falla por Quality Gate FAILED de Sonar, aunque pytest y flutter test pasan. Run 44153301190, job 134288049087. No se observó publicación Pages para la punta en las últimas 20 ejecuciones consultadas.

[Auditoría de dependencias](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/44153301302): success · [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/44153301190): failure

**PR consultadas:** [#51](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/51): abierta; [#50](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/50): abierta; [#49](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/49): abierta; [#46](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/46): abierta; [#48](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/48): abierta; [#47](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/47): abierta; [#45](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/45): abierta; [#44](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/44): abierta; [#43](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/43): abierta; [#41](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/41): abierta; [#38](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/38): abierta

**Próximos pasos técnicos:** Resolver Quality Gate y acreditar publicación exacta del frontend y API; probar login/CORS y documentar frontend institucional si se exige web bajo iscoutb.dev.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/aba565eeceb2f4f44331b26439480beb9ab4b179/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_DinamikUTB/issues) · [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions).

## Drift

Rama **master**, [a0e18f99f9a98b2220b4bf1d753cef62eb3308e3](https://github.com/ISCOUTB/AS_202620_Drift/commit/a0e18f99f9a98b2220b4bf1d753cef62eb3308e3), 2026-11-16T19:54:17-05:00.

**Avances:** PR60/61 integran documentación y mediciones; PR62 integra cuentas Google, favoritos, alertas, PostgreSQL, Xbox, IsThereAnyDeal y página Explorar. PR65 corrige pruebas de sesión que dependían de fecha fija. PR63/64 permanecen abiertas, además de PR57.

**Issues:** 1 abiertas / 19 cerradas; 1 abiertas sin asignar; motivos {'completed': 19}. PR excluidas.

**README (institucional):** README ahora documenta https://drift.iscoutb.dev para frontend/backend/PostgreSQL en laboratorio; API con prefijo /api. Se retiran los despliegues Azure/Vercel.

**Verificación viva:** GET https://drift.iscoutb.dev/api/health: HTTP 200, status ok. No se validó OAuth, persistencia, proveedores ni alertas.

**CI:** CI 43991386520 pasa en HEAD; jobs dependencias, backend, frontend conectado a API y SonarQube Cloud pasan. Esto no acredita despliegue o aceptación funcional del nuevo flujo.

[CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/43991386520): success

**PR consultadas:** [#65](https://github.com/ISCOUTB/AS_202620_Drift/pull/65): fusionada 2026-11-17T00:54:18Z; [#64](https://github.com/ISCOUTB/AS_202620_Drift/pull/64): abierta; [#62](https://github.com/ISCOUTB/AS_202620_Drift/pull/62): fusionada 2026-11-17T00:22:42Z; [#63](https://github.com/ISCOUTB/AS_202620_Drift/pull/63): abierta; [#57](https://github.com/ISCOUTB/AS_202620_Drift/pull/57): abierta; [#61](https://github.com/ISCOUTB/AS_202620_Drift/pull/61): fusionada 2026-11-09T04:26:33Z; [#60](https://github.com/ISCOUTB/AS_202620_Drift/pull/60): fusionada 2026-11-09T03:49:24Z

**Próximos pasos técnicos:** Verificar migración/datos y OAuth en el despliegue institucional; enlazar revisión servida y evidencia de favoritos/alertas/proveedores.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Drift/blob/a0e18f99f9a98b2220b4bf1d753cef62eb3308e3/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Drift/issues) · [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions).

## ElMapita

Rama **main**, [231742e479ed4c9c31b6d717eb9e9d9f5f6bc922](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/231742e479ed4c9c31b6d717eb9e9d9f5f6bc922), 2026-11-16T19:49:17-05:00.

**Avances:** Añade documentación de despliegue Dokploy, Compose/env, gitignore y ADR0013; el commit previo añade documentación de mediciones, caché y pruebas Flutter. Se conserva confirmación docente de presentación y funcionamiento, sin convertirla en nueva prueba integral.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar; motivos {}. PR excluidas.

**README (ausente):** README no ofrece URL pública concreta. Los nuevos docs/adr/0013-despliegue-iscoutb-dev.md y docs/despliegue-iscoutb-dev.md documentan backend https://elmapita.iscoutb.dev; interfaz móvil Flutter. La documentación fuera de README no se cuenta como URL en README.

**Verificación viva:** GET https://elmapita.iscoutb.dev/health: HTTP 200, status ok y checks.supabase ok; timestamp 2026-11-18T00:49:21.141Z.

**CI:** Run 43990721749 resulta success, pero SonarCloud (Quality Gate) falla con Not authorized or project not found; paso de gate omitido. Workflow tiene continue-on-error: true para Sonar. Los demás jobs pasan. No presentar el success global como gate Sonar aprobado.

[CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/43990721749): success

**PR consultadas:** [#15](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/15): abierta; [#18](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/18): abierta; [#17](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/16): abierta; [#14](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/14): abierta; [#13](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/13): abierta; [#12](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/12): abierta; [#10](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/9): abierta; [#11](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/11): abierta; [#8](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/8): abierta; [#6](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/6): abierta; [#7](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/7): abierta; [#4](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/4): abierta; [#3](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/3): abierta; [#5](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/5): abierta

**Próximos pasos técnicos:** Llevar URL del backend al README, conciliar referencias antiguas a Render y restablecer análisis Sonar autenticado.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/231742e479ed4c9c31b6d717eb9e9d9f5f6bc922/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ElMapita/issues) · [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions).

## EnAgenda

Rama **master**, [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), 2026-10-25T22:57:38-05:00.

**Avances:** Punta principal sin cambios desde el corte previo. Se revalidaron README, issues, PR y ejecuciones; no se atribuye el PR5 abierto a la rama principal.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar; motivos {'completed': 1}. PR excluidas.

**README (ausente):** README conserva URL pública pendiente de asignar y marcadores http://[host-asignado]/health, no URL real.

**Verificación viva:** No hay endpoint público concreto documentado que verificar; no equivale a ausencia de trabajo o despliegue.

**CI:** En HEAD: CI 40266609410 failure; Taller mensajes y consistencia 40266609284 success y pages build and deployment 40266609521 success. Ejecuciones más recientes de CI/taller son otra revisión, no la punta principal.

[pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521): success · [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): failure · [Taller mensajes y consistencia](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): success

**PR consultadas:** [#5](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/5): abierta

**Próximos pasos técnicos:** Documentar host exacto HTTPS bajo iscoutb.dev y verificarlo; resolver fallo CI en rama principal distinguiéndolo del taller y publicación Pages.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_EnAgenda/issues) · [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions).

## GimnasioUTB

Rama **main**, [b1cb5375314775b32975f40f4c966e8bcb9bef37](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/b1cb5375314775b32975f40f4c966e8bcb9bef37); fecha 2026-11-17T21:46:36Z.

**Avances:** Integra autenticación/perfiles Supabase, migración y reconciliación de identidades, QR y validación PostgreSQL/TLS. CI de la punta falla en auditoría de dependencias altas/críticas; pruebas unitarias/integración, contrato, mensajería y fitness functions pasan. Firmas/procedencia omitida tras fallo.

**Issues:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: {}.

**README:** API https://gimnasio-utb.iscoutb.dev. No frontend web público documentado. [Fuente](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/b1cb5375314775b32975f40f4c966e8bcb9bef37/README.md).

**PR consultadas:** [#32](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/32): open; [#29](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/29): closed; [#25](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/25): open; [#23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/23): open; [#27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/27): closed.

**CI punta:** [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/44183397709): failure.

**Próximos pasos:** Revisar auditoría de dependencias y comprobar versión desplegada y flujo QR/autenticación; código integrado no acredita publicación.

## InvenTrack

Rama **main**, [95baaf045943e6da5229a8d04fc7314bce905cc7](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/95baaf045943e6da5229a8d04fc7314bce905cc7); fecha 2026-11-17T09:01:15Z.

**Avances:** Añade frontend Flutter/plataformas móviles, sincronización de catálogo y correcciones de contrato/router; configura token interno y separa datos de negocio. README aclara que la punta requiere redespliegue/verificación pública y mantiene datos de negocio deshabilitados hasta completar autenticación/autorización. CI aprueba tests, análisis Sonar, contrato y pip-audit; ejecutar análisis no equivale a verificar Quality Gate.

**Issues:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: {'completed': 7}.

**README:** API https://inventrack.iscoutb.dev y API externa https://inventrack-api.onrender.com. README no da URL de frontend. [Fuente](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/95baaf045943e6da5229a8d04fc7314bce905cc7/README.md).

**PR consultadas:** [#12](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/12): closed; [#14](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/14): open; [#10](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/10): closed; [#13](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/13): open; [#11](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/11): open.

**CI punta:** [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/44051745711): success.

**Próximos pasos:** Comprobar redespliegue y restricciones de acceso antes de habilitar datos; documentar interfaz Flutter separada de las API.

## LaPlacita

Rama **master**, [c4faebdb829895f047aebade4ce24001065a6513](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/c4faebdb829895f047aebade4ce24001065a6513); fecha 2026-11-15T17:28:01Z.

**Avances:** PR47 integra correcciones de cabeceras/topes y pruebas de laboratorio; PR48 integra documentación y muestras crudas de rendimiento/QoS, incluidos fallos, recuperación PostgreSQL y red degradada simulada. Laboratorio Podman aislado, no Dokploy ni BD del equipo. CI punta aprueba backend, frontend, auditoría/SBOM, contrato y análisis Sonar. No acredita nueva publicación ni QoS productiva.

**Issues:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. Motivos: {'completed': 14}.

**README:** Frontend https://laplacita-app.iscoutb.dev; API https://laplacita-test.iscoutb.dev/api/v1. [Fuente](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/c4faebdb829895f047aebade4ce24001065a6513/README.md).

**PR consultadas:** [#48](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/48): fusionado 2026-11-15T17:28:01Z; [#46](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/46): open; [#28](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/28): open; [#47](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/47): fusionado 2026-11-14T15:37:49Z; [#30](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/30): closed.

**CI punta:** [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/43741258708): success.

**Próximos pasos:** Mantener separación laboratorio/producción y comprobar versión servida; revisar PR de dependencias abiertos.

## LostVault

Rama **main**, [f66f298434af615573e92a778f88614bba53b7d3](https://github.com/ISCOUTB/AS_202620_LostVault/commit/f66f298434af615573e92a778f88614bba53b7d3); fecha 2026-11-09T04:14:53Z.

**Avances:** PR26 fusionado incorpora scripts, resultados crudos y medición del Escenario 4 sobre Vercel, más riesgos R11–R13. El equipo reporta diferencias entre primera ráfaga y estado estable, y reconoce sesgo de un solo navegador. Se leyó evidencia, no se repitió carga. Flutter checks, Backend checks y Build pasan en HEAD.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: {'completed': 1}.

**README:** Sin URL pública concreta en README. La API externa https://backend-nu-self-91.vercel.app aparece en docs/medicion/s14-medicion-atributos.md, no en README ni dominio institucional. [Fuente](https://github.com/ISCOUTB/AS_202620_LostVault/blob/f66f298434af615573e92a778f88614bba53b7d3/README.md).

**PR consultadas:** [#26](https://github.com/ISCOUTB/AS_202620_LostVault/pull/26): fusionado 2026-11-09T04:14:54Z; [#25](https://github.com/ISCOUTB/AS_202620_LostVault/pull/25): fusionado 2026-11-03T16:39:55Z; [#24](https://github.com/ISCOUTB/AS_202620_LostVault/pull/24): fusionado 2026-11-02T03:43:13Z; [#23](https://github.com/ISCOUTB/AS_202620_LostVault/pull/23): fusionado 2026-11-02T03:19:11Z; [#21](https://github.com/ISCOUTB/AS_202620_LostVault/pull/21): open.

**CI punta:** [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/42560740976): success; [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/42560740805): success; [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/42560740795): success.

**Próximos pasos:** Documentar URLs frontend/API en README bajo iscoutb.dev; repetir medición con instrumento independiente y comprobar caché/escalado.

## PROYECTO_CAMPUSMARKET

Rama **master**, [c79c73d47936790b0f248bdea5c0a700ce8fe017](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/c79c73d47936790b0f248bdea5c0a700ce8fe017); fecha 2026-11-09T06:27:11Z.

**Avances:** PR93 fusionado actualiza trazabilidad, arc42/C4 y descargas verificadas Gradle/Gitleaks para CI. README registra lectura del 8/nov: /app y /docs 200, /health ok, /universidades 500. Es evidencia histórica del equipo, no prueba repetida hoy. HEAD documental se separa del runtime productivo. Flujo real Web y Android pasa en tres jobs web-desktop, web-mobile y android; el job Android sí ejecutó emulador, los pasos omitidos corresponden a otras plataformas de la matriz.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: {}.

**README:** Frontend https://campusmarket.iscoutb.dev/app/; API https://campusmarket.iscoutb.dev. Pages/Azure se conservan como históricos. [Fuente](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/README.md).

**PR consultadas:** [#93](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/93): fusionado 2026-11-09T06:27:11Z; [#92](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/92): fusionado 2026-11-06T00:38:57Z; [#91](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/91): fusionado 2026-11-03T10:35:18Z; [#90](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/90): fusionado 2026-11-03T10:02:06Z; [#89](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/89): fusionado 2026-11-03T10:06:40Z.

**CI punta:** [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110863): success; [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110841): success; [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110702): success; [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110656): failure; [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110636): success.

**Próximos pasos:** Revalidar /universidades sin inferir salud global de /health; conservar separados HEAD documental y runtime, y verificar recuperación/backup independiente.

## PideUtb

Rama **master**, [602b55fbfe97a24f7ebe247cacbbccc50e560684](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/602b55fbfe97a24f7ebe247cacbbccc50e560684); fecha 2026-11-07T22:57:20Z.

**Avances:** PR41, PR42 y PR43 fusionados: coste de separación, corrección de transiciones del mostrador, recogida programada y avisos/comprobante. PR44 permanece abierto con fotografías/carta y cambios visuales/idioma: CI pasa, todavía no integrado. CI HEAD master pasa incluido recorrido Playwright ahora ejecutado, pytest 3.11/3.12, imagen, contrato y dependencias. Job SonarCloud success pero análisis y Quality Gate skipped: no describir como Sonar aprobado. Se conserva confirmación docente de presentación/despliegues, sin nueva aceptación funcional.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: {}.

**README:** Frontend https://pideutb.iscoutb.dev; API https://api-pideutb.iscoutb.dev/docs. [Fuente](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/602b55fbfe97a24f7ebe247cacbbccc50e560684/README.md).

**PR consultadas:** [#44](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/44): open; [#43](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/43): fusionado 2026-11-07T22:57:21Z; [#42](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/42): fusionado 2026-11-07T22:52:56Z; [#41](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/41): fusionado 2026-11-07T22:50:24Z; [#40](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/40): fusionado 2026-11-02T23:14:22Z.

**CI punta:** [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/42422992215): success.

**Próximos pasos:** Revisar PR44 sin atribuir fotos a master; comprobar publicación y recorridos de recogida/avisos reales y configuración de Sonar.

## ROUTB

Rama **master**, [e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6); fecha 2026-11-14T21:45:16-05:00. Consulta 18/nov UTC, 17/nov Colombia.

**Avances:** El PR #79 se fusionó hacia master el 15/nov a las 02:45:17 UTC. La rama principal ya incorpora cambios de rutas, solicitudes, perfil/vehículo, notificaciones y cliente Flutter que antes permanecían separados en Changes. Añade scripts/medir_rendimiento.py y scripts/sembrar_viajes_medicion.py, con medición enlazada desde README. CI de la punta aprobó pruebas backend/contrato/migraciones, Flutter, auditoría pip y construcción Docker. El job Sonar solo ejecutó un mensaje de reserva sin token: no acredita análisis ni Quality Gate. La purga programada también pasó, pero no prueba publicación de interfaz. PR #80 de FastAPI sigue abierto hacia Changes, con CI fallido en su propia revisión, no en master.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —. PR excluidas del conteo. Estados Projects no consultados.

**README:** Institucional (API). README:117–118 documenta https://routb.iscoutb.dev y /health como backend; no documenta frontend web independiente.

**CI:** [CI ROUTB 43669244266](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/43669244266): success (misma punta); [Purga periódica de datos de ubicación 44044396070](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/44044396070): success (misma punta); [Purga periódica de datos de ubicación 43830731632](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/43830731632): success (misma punta); [Purga periódica de datos de ubicación 43693161605](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/43693161605): success (misma punta)

**Próximos pasos técnicos:** Verificar revisión realmente desplegada y recorrido cliente/API; habilitar análisis Sonar efectivo y revisar compatibilidad del PR #80 antes de integrarlo.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ROUTB/issues) · [PR](https://github.com/ISCOUTB/AS_202620_ROUTB/pulls) · [CI](https://github.com/ISCOUTB/AS_202620_ROUTB/actions). No se ejecutó código estudiantil ni se hizo comprobación viva propia.

## Recobra

Rama **master**, [7142bb96d8c253b1a71ba1ec72aebb3597d9b29b](https://github.com/ISCOUTB/AS_202620_Recobra/commit/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b); fecha 2026-11-08T16:55:27-05:00. Consulta 18/nov UTC, 17/nov Colombia.

**Avances:** Desde el corte anterior cambian cinco archivos documentales: README enlaza docs/medicion-s14.md, con datos versionados en docs/evidencia/medicion-s14-dokploy.json; arc42 añade observaciones externas RV-01 a RV-15. Es evidencia reportada por el equipo, no una repetición propia. El run de master 42527932254 pasa backend, Flutter, adapters contra PostgreSQL, respaldo/restauración, seguridad y, a diferencia del antecedente, el paso de análisis y el Quality Gate están ejecutados con success. Esto no acredita despliegue nuevo. Hay 11 PR abiertas de dependencias; #11 cerró sin merge y fue sustituida por #13.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —. PR excluidas del conteo. Estados Projects no consultados.

**README:** Institucional (frontend y API). README:35–37 distingue https://recobra.iscoutb.dev/ (vitrina), /app/ (Flutter Web) y /publicaciones, /health, /health/ready, /metrics (API).

**CI:** [ci 42527932254](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/42527932254): success (misma punta)

**Próximos pasos técnicos:** Mantener separación entre medición documentada, CI y aceptación del servicio; revisar dependencias propuestas y verificar runtime/despliegue sin dar por integradas las PR abiertas.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Recobra/blob/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Recobra/issues) · [PR](https://github.com/ISCOUTB/AS_202620_Recobra/pulls) · [CI](https://github.com/ISCOUTB/AS_202620_Recobra/actions). No se ejecutó código estudiantil ni se hizo comprobación viva propia.

## ShareU

Rama **master**, [e1298422516716cdd168ec65baba42b979fbc7c0](https://github.com/ISCOUTB/AS_202620_ShareU/commit/e1298422516716cdd168ec65baba42b979fbc7c0); fecha 2026-11-16T21:17:49-05:00. Consulta 18/nov UTC, 17/nov Colombia.

**Avances:** Se fusionaron PR #23 (división de arc42) y #29 (PyYAML). La punta incorpora cambios en autenticación de escritura, outbox, búsqueda/caché, documentación, scripts de medición y Compose local. El workflow Tests 44001934319 pasa pruebas/contrato, medición y auditorías; SonarCloud quedó skipped. La medición publicada se identifica como local ASGI, no rendimiento demostrado del despliegue. Siguen seis PR abiertas, incluida #22, aunque ya existe CI verde en master. La issue #20 continúa abierta pese al merge de #23: estado de issue e implementación no son equivalentes.

**Issues:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: {'completed': 10}. PR excluidas del conteo. Estados Projects no consultados.

**README:** Institucional documentado, no operativo acreditado. README:141–144 ahora identifica https://shareu.iscoutb.dev y https://api-shareu.iscoutb.dev, pero el propio equipo los registra con HTTP 404 al 16/nov. Es documentación nueva, no comprobación viva de esta revisión.

**CI:** [Tests 44001934319](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/44001934319): success (misma punta)

**Próximos pasos técnicos:** Comprobar publicación y revisión servida de los dos dominios; habilitar Sonar; reconciliar issues con cambios fusionados. Revisar referencia Dockploy/compose.lab.yml en Compose: el árbol contiene compose.lab.yaml.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ShareU/blob/e1298422516716cdd168ec65baba42b979fbc7c0/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ShareU/issues) · [PR](https://github.com/ISCOUTB/AS_202620_ShareU/pulls) · [CI](https://github.com/ISCOUTB/AS_202620_ShareU/actions). No se ejecutó código estudiantil ni se hizo comprobación viva propia.

## Sistema de calificación automática

Rama **master**, [201864022a378b1d98c53bca62017e4fa47cb7dc](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/201864022a378b1d98c53bca62017e4fa47cb7dc); fecha 2026-11-13T16:50:14-05:00. Consulta 18/nov UTC, 17/nov Colombia.

**Avances:** Hay implementación nueva de lectura óptica de hojas, procesamiento de cola, calificación contra clave y revisión manual, junto con pantallas de exámenes/resultados/revisión y contrato API 1.8.0. Se versionan herramientas y muestras de medición; no se ejecutaron aquí. El último commit restringe selección de URL de API a una lista fija. CI 43514210787 pasa pruebas backend y Flutter, escenarios de integración, OSV y compila/publica rama despliegue. Publicar esa rama es evidencia de preparación/publicación de artefactos, no constatación independiente de que Dokploy sirve la revisión. El README reconoce ausencia de revisión entre pares, sin atribuirle motivo en este seguimiento.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —. PR excluidas del conteo. Estados Projects no consultados.

**README:** Institucional (frontend y API). README:19–21 y 267–269 identifica https://calificacion.iscoutb.dev, https://api-calificacion.iscoutb.dev/health y frontend /revision.txt; conserva alternativas históricas Render, que no sustituyen los endpoints institucionales.

**CI:** [CI 43514210787](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/43514210787): success (misma punta)

**Próximos pasos técnicos:** Consultar revision.txt y salud para contrastar revisión servida, y validar recorrido de carga/lectura/revisión manual con datos autorizados; mantener diferencias entre medición local, pruebas y aceptación funcional.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/201864022a378b1d98c53bca62017e4fa47cb7dc/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/issues) · [PR](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pulls) · [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions). No se ejecutó código estudiantil ni se hizo comprobación viva propia.

## TAIA

Rama **main**, [7342f349752af2b26f1d9df7e313fbcc1b9656d4](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/7342f349752af2b26f1d9df7e313fbcc1b9656d4); fecha 2026-11-08T09:21:57-05:00. Consulta 18/nov UTC, 17/nov Colombia.

**Avances:** La única diferencia respecto al corte anterior es docs/evidencia_s14.md, agregado el 8/nov: resume mediciones preexistentes. No se reproduce aquí su autoevaluación ni sus notas. El documento distingue extracción del modelo de persistencia, y latencia del modelo de extremo a extremo; además cita como revisado un commit anterior a la punta actual. No hay nuevo run para 7342f349 en las ejecuciones consultadas: el último CI visible sigue siendo failure sobre 44e1cc001 (1/nov), con CD skipped. No se atribuye ese run a la nueva punta. Se conserva la confirmación docente de presentación y funcionamiento, no una validación nueva.

**Issues:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: {'completed': 4}. PR excluidas del conteo. Estados Projects no consultados.

**README:** Institucional (API). README:9–12 y 118–120 documenta https://taia-sistema.iscoutb.dev como API, /health, /metrics y /docs; Render es alternativa. No equivale a URL frontend web.

**CI:** [CD 41337016910](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41337016910): skipped (otra revisión); [CD 41336898586](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336898586): skipped (otra revisión); [CI 41336869271](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336869271): failure (otra revisión)

**Próximos pasos técnicos:** Obtener CI de la revisión actual y comprobar medición del recorrido completo y persistencia, sin convertir métricas parciales en aceptación integral.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/7342f349752af2b26f1d9df7e313fbcc1b9656d4/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/issues) · [PR](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pulls) · [CI](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions). No se ejecutó código estudiantil ni se hizo comprobación viva propia.

## Tienda virtual UTB

Rama **main**, [28c688e65adfb9f49ac9602b538d1f6d365b395c](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/28c688e65adfb9f49ac9602b538d1f6d365b395c); fecha 2026-11-08T23:08:30-05:00. Consulta 18/nov UTC, 17/nov Colombia.

**Avances:** Los PR #14 y #15 fusionan documentación de medición del escenario 4, observaciones de pares y estado de señalamientos en arc42 §11. La diferencia con el corte anterior se limita a siete archivos documentales. PR #16 de registro de IA sigue abierta. Pruebas 42560128666 pasa frontend, backend, contrato, RLS y migraciones en la punta actual, mientras todos los pasos del job Sonar están skipped aunque el job figure success. No hay nueva publicación ni funcionamiento vivo constatados por esta revisión.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —. PR excluidas del conteo. Estados Projects no consultados.

**README:** Externo. README:7 y 150 conserva https://tiendautb-sistema-n0ojjk-fde272-144-24-4-187.sslip.io/; no documenta subdominio iscoutb.dev. URLs localhost son instrucciones locales.

**CI:** [Pruebas 42560128666](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/42560128666): success (misma punta)

**Próximos pasos técnicos:** Documentar URL institucional y contrastar servicio publicado; activar análisis Sonar real y mantener trazabilidad entre cambios documentales y correcciones implementadas.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/28c688e65adfb9f49ac9602b538d1f6d365b395c/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/issues) · [PR](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pulls) · [CI](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions). No se ejecutó código estudiantil ni se hizo comprobación viva propia.

## UTB_TRACKER

Rama **main**, [662d3fea4cfec953d26a1bfa673f8b973506e9b2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/662d3fea4cfec953d26a1bfa673f8b973506e9b2); fecha 2026-11-17T00:52:41Z.

**Avances:** Integra catálogo de salones, disponibilidad y equipos fijos, permisos por rol y perfil/correo institucional. PR #18 y #19 fusionadas; la última incorpora migración idempotente para cargar 59 salones faltantes. No se infiere que el catálogo esté visible en todas las sesiones únicamente por el merge.

**Issues:** 4 abiertas / 1 cerradas. Motivos: {'completed': 1}. PR excluidas.

**README:** Externo: API y Swagger en https://129-80-171-141.nip.io; README menciona iscoutb.dev genéricamente, sin subdominio institucional concreto. Cliente móvil no equivale a frontend web publicado.

**Verificación viva:** GET /salud: HTTP 200, status ok y database connected. No prueba catálogo ni recorrido móvil. Consulta 18/nov UTC (17/nov Colombia).

**CI:** Run 43991170043: test y deploy success. El paso Sonar está configurado con continue-on-error: true; un workflow verde por sí solo no convierte ese control en puerta obligatoria.

[UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/43991170043): success

**PR consultadas:** [#19](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/19): fusionada 2026-11-17T00:52:41Z; [#18](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/18): fusionada 2026-11-16T23:59:20Z; [#17](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/17): fusionada 2026-11-16T17:35:46Z; [#16](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/16): fusionada 2026-11-16T17:33:42Z; [#15](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/15): fusionada 2026-11-16T03:08:37Z; [#14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/14): fusionada 2026-11-15T01:19:48Z; [#9](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/9): fusionada 2026-11-09T03:56:42Z; [#8](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/8): fusionada 2026-11-03T00:37:47Z; [#7](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/7): fusionada 2026-11-03T00:25:29Z; [#6](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/6): fusionada 2026-11-03T00:13:54Z

**Próximos pasos técnicos:** Comprobar catálogo, roles y flujo móvil en la versión servida; conciliar issues #10–#13 abiertas con implementación fusionada y documentar subdominio institucional.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/662d3fea4cfec953d26a1bfa673f8b973506e9b2/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/issues) · [PR](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pulls).


## Verifacts

Rama **master**, [035383e19e44ef26cefabfab7d71e30f37f0beed](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/035383e19e44ef26cefabfab7d71e30f37f0beed); fecha 2026-11-10T02:17:02Z.

**Avances:** Único cambio desde el corte previo: convierte el endpoint POST /analysis en enlace Markdown en README. No cambia código funcional ni infraestructura; no se atribuye nueva medición o aceptación.

**Issues:** 0 abiertas / 3 cerradas. Motivos: {'completed': 3}. PR excluidas.

**README:** Institucional: frontend https://verifacts.iscoutb.dev; API /analysis (POST), salud /health, Swagger /docs y métricas /metrics en el mismo origen.

**Verificación viva:** GET /health: HTTP 200 y status ok. Sin nueva prueba de análisis o historial. Consulta 18/nov UTC (17/nov Colombia).

**CI:** Tests y SonarCloud success en la punta consultada; no acreditan un despliegue nuevo.

[Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/42741684420): success · [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/42741684410): success

**PR consultadas:** 

**Próximos pasos técnicos:** Mantener diferenciada la evidencia documental del estado servido y los flujos funcionales; el cambio de enlace no resuelve ni vuelve a evaluar pendientes anteriores.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/035383e19e44ef26cefabfab7d71e30f37f0beed/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Verifacts/issues) · [PR](https://github.com/ISCOUTB/AS_202620_Verifacts/pulls).


## XALD

Rama **master**, [ab45384399ccdd2009ebc94725e9b4de7b480efb](https://github.com/ISCOUTB/AS_202620_XALD/commit/ab45384399ccdd2009ebc94725e9b4de7b480efb); fecha 2026-11-17T16:15:38Z.

**Avances:** Integra sincronización remota PostgreSQL, worker diferido y cliente IA; añade cambios de validación/límites del backend y pruebas, además de ajustes Gradle y ofuscación release. PR #45 fusionada tiene destino experimental, no es la prueba de integración a master; la punta master se verificó separadamente.

**Issues:** 0 abiertas / 6 cerradas. Motivos: {'completed': 5, 'duplicate': 1}. PR excluidas.

**README:** Externo: API https://xald-backend.onrender.com, salud /health y /docs. README mantiene cliente Android y requiere configurar endpoint/clave localmente; no documenta subdominio iscoutb.dev.

**Verificación viva:** GET /health agotó 15 segundos de espera. Resultado inconcluso, no se declara caída. Consulta 18/nov UTC (17/nov Colombia).

**CI:** Run push 44123721549 de master: build-and-test, backend-tests y deploy-backend success; el último ejecuta hook Render y comprobación /health. No equivale a aceptación de la app.

[Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/44123738286): success · [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/44123721549): success

**PR consultadas:** [#45](https://github.com/ISCOUTB/AS_202620_XALD/pull/45): fusionada 2026-11-17T16:18:00Z; [#44](https://github.com/ISCOUTB/AS_202620_XALD/pull/44): abierta; [#36](https://github.com/ISCOUTB/AS_202620_XALD/pull/36): abierta; [#35](https://github.com/ISCOUTB/AS_202620_XALD/pull/35): abierta; [#34](https://github.com/ISCOUTB/AS_202620_XALD/pull/34): abierta; [#39](https://github.com/ISCOUTB/AS_202620_XALD/pull/39): abierta; [#33](https://github.com/ISCOUTB/AS_202620_XALD/pull/33): abierta; [#43](https://github.com/ISCOUTB/AS_202620_XALD/pull/43): abierta; [#29](https://github.com/ISCOUTB/AS_202620_XALD/pull/29): abierta; [#30](https://github.com/ISCOUTB/AS_202620_XALD/pull/30): abierta

**Próximos pasos técnicos:** Documentar host institucional y demostrar sincronización, persistencia y recuperación desde APK con la revisión servida, sin exponer claves.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_XALD/blob/ab45384399ccdd2009ebc94725e9b4de7b480efb/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_XALD/issues) · [PR](https://github.com/ISCOUTB/AS_202620_XALD/pulls).


## mapsutb

Rama **master**, [78a8a545053237a58410e28d6f0002629c527e63](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/78a8a545053237a58410e28d6f0002629c527e63); fecha 2026-11-11T14:40:47Z.

**Avances:** Añade documentación de amenazas/privacidad, contrato y prototipo aislado de mensajería, análisis del escenario 6 por ventanas de siete días, mediciones y revisión de pares reportadas por el equipo. El prototipo no se presenta como mensajería integrada en el producto. Continúan PR abiertas de pantalla y dependencias.

**Issues:** 0 abiertas / 54 cerradas. Motivos: {'completed': 54}. PR excluidas.

**README:** Externo: frontend Firebase https://mapsutb.web.app y salud /health.json; la métrica histórica se publica en rama metricas, no es una API institucional. README no documenta subdominio iscoutb.dev.

**Verificación viva:** GET /health.json: HTTP 200, status ok y commit 78a8a545053237a58410e28d6f0002629c527e63, coincidente con la punta. No prueba navegación o ubicación. Consulta 18/nov UTC (17/nov Colombia).

**CI:** CI push 43040786035 y despliegue Firebase 43040785975 success en la punta; sonda 44210054302 success. Una sonda verde no prueba navegación ni ubicación.

[Despliegue web (Firebase Hosting)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/43040785975): success · [CI](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/43040786035): success · [Sincronizar hallazgos de Sonar a GitHub Issues](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/44208205029): success · [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/44210054302): success

**PR consultadas:** [#64](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/64): abierta; [#63](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/63): abierta; [#62](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/62): abierta; [#61](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/61): abierta; [#60](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/60): abierta; [#59](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/59): abierta; [#58](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/58): abierta; [#57](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/57): abierta; [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z

**Próximos pasos técnicos:** Separar resultados reportados, disponibilidad de la sonda y prueba funcional de mapas; documentar URL institucional y revisar PR abiertas.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/78a8a545053237a58410e28d6f0002629c527e63/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_mapsutb/issues) · [PR](https://github.com/ISCOUTB/AS_202620_mapsutb/pulls).


## uniTeam

Rama **master**, [98b04800904618b132354037efd3677b171ad296](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/98b04800904618b132354037efd3677b171ad296); fecha 2026-11-17T15:32:33Z.

**Avances:** PR #33 y #34 fusionadas: WebSocket con rutas/pruebas y actualización del tablero, seguida por rediseño frontend. README publica DuckDNS, pero la sonda de disponibilidad aún consulta los antiguos hosts Render.

**Issues:** 0 abiertas / 1 cerradas. Motivos: {'completed': 1}. PR excluidas.

**README:** Externo: frontend https://uniteam-web.duckdns.org y API https://uniteam-api.duckdns.org. La sonda configura uniteam-web.onrender.com y uniteam-api.onrender.com: sus seis fallos no prueban caída de los hosts DuckDNS.

**Verificación viva:** GET a web y /health de los hosts DuckDNS devolvió 503 desde el intermediario Envoy, con error de conexión upstream. No se pudo verificar el servicio de origen; no se atribuye ese 503 a la aplicación. Consulta 18/nov UTC (17/nov Colombia).

**CI:** CI 44115523572 y seguridad-dependencias 44115523525 success; comprobación del despliegue 44209643234 failure (seis comprobaciones, hosts Render). README aún afirma ausencia de workflow CI, contradicha por runs actuales.

[seguridad-dependencias](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/44115523525): success · [CI](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/44115523572): success · [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/44209643234): failure

**PR consultadas:** [#34](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/34): fusionada 2026-11-17T15:32:33Z; [#31](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/31): abierta; [#33](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/33): fusionada 2026-11-17T14:51:24Z; [#30](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/30): cerrada sin merge; [#32](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/32): abierta; [#18](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/18): cerrada sin merge; [#28](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/28): abierta; [#29](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/29): abierta; [#13](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/13): abierta; [#27](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/27): fusionada 2026-11-02T05:17:31Z

**Próximos pasos técnicos:** Alinear sonda y README con los dominios activos; documentar subdominio institucional y verificar autenticación, pertenencia y notificación WebSocket en despliegue.

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/98b04800904618b132354037efd3677b171ad296/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_uniTeam/issues) · [PR](https://github.com/ISCOUTB/AS_202620_uniTeam/pulls).

