# Seguimiento de los 23 proyectos · 5 de noviembre de 2026

Consulta del **5 de noviembre de 2026**, con lecturas de GitHub durante este corte y comprobaciones vivas fechadas por separado. Seguimiento documental de los 23 proyectos vigentes, posterior al cierre de S13, sin recalificar ni reabrir semanas. Calificaciones, planillas, matrices y cortes históricos permanecen intactos.

**43 issues abiertas y 132 cerradas** (131 completed; 1 duplicate), 19 abiertas sin asignar. Conteo excluyendo PR, revalidado hoy.

README: **13 con algún endpoint institucional; 5 con enlaces externos; 5 sin URL pública concreta**. La clasificación institucional puede corresponder solo a API, no acredita frontend institucional. Verifacts cambia de Externo a Institucional; Dinamik conserva API institucional pero mueve frontend a Pages externo.

Se conservan las confirmaciones docentes: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. No equivalen a nuevas pruebas funcionales de este corte.

Código fusionado, CI, publicación y aceptación funcional son evidencias distintas. OPEN/CLOSED y state_reason son estados/motivos de GitHub Issues, no estados personalizados del tablero Projects, que no se obtuvieron. Ausencia de issues o URL no demuestra ausencia de trabajo. No se ejecutó código estudiantil ni se modificaron sus repositorios. La revisión se realizó con conectores GitHub; el entorno de ejecución local no estuvo disponible.

[Índice cronológico S11–S13](revision-semanas-11-13-2026-11-03.md): se conservan los cierres y no se atribuyen retroactivamente los incrementos de hoy a esas entregas.

[Issues y motivos](seguimiento-issues-2026-11-05.md) · [README y despliegues](seguimiento-despliegues-2026-11-05.md) · [Corte anterior](seguimiento-2026-11-04.md)

## Cambios del corte

- [DinamikUTB](#dinamikutb): Se concreta la separación: frontend en GitHub Pages y API/PostgreSQL en Dokploy. README y build cambian a https://iscoutb.github.io/AS_202620_DinamikUTB/ y https://api-dinamikutb.iscoutb.dev. Pages elimina CNAME y usa base-href /AS_202620_DinamikUTB/. El run 41966455736 construye y publica esta punta el 5/nov a las 04:14:56 UTC. La portada se vio renderizada en la comprobación independiente de hoy; el health de la API nueva mostró «404 page not found», sin código HTTP capturado ni login probado.
- [LaPlacita](#laplacita): La punta incorpora PR37–39 y commits directos posteriores: despliegue automatizado por aplicación, ubicación/portada, cancelación por dueño autenticado antes de Listo (404 para pedido ajeno, 409 fuera de ventana, historial conservado), imágenes de tiendas por estado en Garage/PostgreSQL, mejoras de menú/carrito/contraseña y proxy que retira Content-Encoding/Content-Length tras descompresión. Las pruebas de dominio cubren propiedad, ventana e idempotencia; no se ejecutó prueba HTTP productiva propia.
- [mapsutb](#mapsutb): Sin cambio de código, README, issues ni PR. Nuevas ejecuciones programadas de sonda y sincronización Sonar pasan sobre la misma punta; no acreditan migración ni aceptación funcional nueva. README describe Flutter monolítico sin backend propio: no se exige una API inexistente como si estuviera implementada. Frontend y health estático siguen en Firebase externo.
- [Recobra](#recobra): Master e implementación no cambian. PR abiertas pasan de 10 a 11: #2 Node25 cierra sin merge; #12 propone Node26 para build/runtime, #11 acción Sonar 8.4.0 y #4 renueva ajv/supertest/@types. Ninguna está integrada. Los tres CI nuevos aprueban jobs de pruebas/build, pero Quality Gate se omite por limitarse a push. Logs de #11/#12 muestran SONAR_TOKEN vacío, error «Not authorized or organization not found», salida 3 tolerada con continue-on-error: no acreditan nuevo análisis Sonar. Tests directos usan Node20 mientras contenedor propuesto usa Node26. Se conserva presentación docente.
- [ROUTB](#routb): Sin cambio de master, README, issues ni PR. Nueva purga programada aprobada, no despliegue nuevo. PR72 continúa fusionada solo en Changes, no master; CI de esa rama no debe atribuirse a la punta principal ni al sitio. Se conserva avance entregado según docente.
- [uniTeam](#uniteam): Sin cambio de código, README, issues ni PR. Cuatro nuevas sondas programadas fallan; el log de la última vuelve a usar uniteam-web.onrender.com y uniteam-api.onrender.com, no los destinos DuckDNS de README. Fallan seis comprobaciones: no prueban caída de DuckDNS. Sigue sin remediación nueva el antecedente de auditoría con 48 entradas en cuatro paquetes pese a job verde.
- [Verifacts](#verifacts): Dos commits cambian exclusivamente README, docs/despliegue.md y ADR0010. Ahora se publica https://verifacts.iscoutb.dev, con API /health, /docs, /metrics y POST /analysis: pasa de Externo a Institucional. No se debe seguir marcando el dominio como ausente documentalmente. HTTPS, backend conectado, acceso móvil y persistencia son declaraciones del equipo, sin prueba viva independiente en este corte. No cambia implementación, infraestructura, dependencias ni pruebas. Tests confirma 66 passed, 3 warnings; construcción y smoke pasan. El análisis Sonar sí se ejecuta y espera el gate: QUALITY GATE STATUS: PASSED. Esto no acredita despliegue. docs/despliegue.md conserva instrucciones heredadas para abrir HTTP/desactivar HTTPS automático: deben retirarse, sin recomendar debilitar seguridad. Persisten controles SSRF, propiedad del historial, timeout, tamaño, idempotencia/WAL y SCA declarados pendientes.

<a id="audioshare"></a>

## AudioShare

Rama **master**, [b2eb60d34a3ee41e2c632aa78e5a7021356461da](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/b2eb60d34a3ee41e2c632aa78e5a7021356461da), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Redesplegar mediante el flujo Dokploy y demostrar frontend, API y sincronización entre dispositivos; publicar imagen Docker Hub no acredita la revisión servida.
- Implementar y probar controles de acceso por sala, cuotas de subida y límites de tasa; acompañar borrado/caducidad con una política y aviso que no prometan supresión ya operativa.
- Integrar auditoría de producción al CI y resolver o justificar con análisis completo los seis hallazgos de desarrollo; actualizar la acción Sonar que emite advertencia de seguridad.
- Documentar la prueba Flutter omitida y validar descarga, reintento y reingreso en dispositivos reales.

**Issues:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar. Motivos: 2 completed.

**README:** Institucional. README mantiene un mismo origen institucional para frontend y API. Conserva su comprobación histórica del 26/oct de cliente legado y /rooms 404; no se repitió prueba viva.

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/8): abierta; [#9](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/9): fusionada 2026-10-26T04:47:48Z; [#7](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/7): fusionada 2026-10-26T03:42:05Z; [#2](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/2): fusionada 2026-09-01T14:56:35Z [Colección](https://github.com/ISCOUTB/AS_202620_AudioShare/pulls).

**CI consultado:** [CI 41389534440](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534440): success (misma punta); [Publicar imagen 41389534404](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534404): success (misma punta); [Flutter 41389534313](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534313): success (misma punta); [Flutter 41387713791](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713791): success (otra revisión o PR); [Publicar imagen 41387713751](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713751): success (otra revisión o PR); [CI 41387713744](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713744): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b2eb60d34a3ee41e2c632aa78e5a7021356461da/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_AudioShare/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_AudioShare/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#audioshare).

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, [7fdc502e0a876e77479d40fadb942fdb10a07d52](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7fdc502e0a876e77479d40fadb942fdb10a07d52), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Revisar la validación de los workflows y obtener una ejecución verificable con jobs/logs, además de comprobar la construcción del contenedor.
- Documentar URL exacta de frontend y API en iscoutb.dev dentro de README y demostrar la revisión publicada.
- Corregir idempotencia por autor/operación, exposición de matrícula y permisos por rol; conciliar privacidad que aún describe subida sin sesión con el cambio implementado.
- Completar decisiones y marcadores de privacidad/retención, y publicar URL exacta de frontend/API en README.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Ausente. README declara Dokploy y HTTPS, pero no ofrece un host público concreto; localhost y variables API_URL no cuentan como URL pública.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta; [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3): fusionada 2026-10-05T05:46:36Z; [#2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2): fusionada 2026-09-21T04:56:52Z [Colección](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pulls).

**CI consultado:** [.github/workflows/contrato.yml 41661273849](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41661273849): failure (misma punta); [.github/workflows/backend-tests.yml 41661271676](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41661271676): failure (misma punta); [.github/workflows/backend-tests.yml 41379945028](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379945028): failure (otra revisión o PR); [.github/workflows/contrato.yml 41379943754](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379943754): failure (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7fdc502e0a876e77479d40fadb942fdb10a07d52/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#clubs_utb).

<a id="dinamikutb"></a>

## DinamikUTB

Rama **master**, [ad917c9b93940a244761b2a307d71137cdac3d1b](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/ad917c9b93940a244761b2a307d71137cdac3d1b), observada el 5/nov/2026.

Se concreta la separación: frontend en GitHub Pages y API/PostgreSQL en Dokploy. README y build cambian a https://iscoutb.github.io/AS_202620_DinamikUTB/ y https://api-dinamikutb.iscoutb.dev. Pages elimina CNAME y usa base-href /AS_202620_DinamikUTB/. El run 41966455736 construye y publica esta punta el 5/nov a las 04:14:56 UTC. La portada se vio renderizada en la comprobación independiente de hoy; el health de la API nueva mostró «404 page not found», sin código HTTP capturado ni login probado.

Se eliminan el workflow GHCR y el servicio web/FRONTEND_IMAGE del Compose de laboratorio: queda superado el señalamiento anterior de que aún consumía la imagen web. No es reparación del permiso GHCR, sino retirada de esa ruta.

CI ejecuta 100 pruebas backend y 25 Flutter aprobadas, pero Sonar termina QUALITY GATE STATUS: FAILED (salida 3): fallo real del gate, no de credenciales. README todavía afirma gate verde. Auditoría de dependencias pasa. Pages publica independientemente del workflow CI.

CORS documentado usa https://iscoutb.github.io; API lee CORS_ORIGINS de entorno. No se verificó configuración efectiva ni preflight. El Dockerfile frontend alternativo usa nginx-unprivileged y puerto 8080, pero Compose raíz apunta a 80 y healthcheck sin :8080. Esta discrepancia afecta la alternativa Docker, no Pages ni Compose de laboratorio ya sin web.

**Próximos pasos:**
- Corregir Quality Gate y afirmación de README; comprobar API nueva, CORS y login desde Pages con revisión servida.
- Conciliar puerto/healthcheck solo si se mantiene la alternativa Docker; no atribuirlo a Pages.
- Conservar pendientes de JWT legado sin sig, concurrencia PostgreSQL y restauración de respaldos.

**Issues:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional por API; frontend externo Pages. Frontend https://iscoutb.github.io/AS_202620_DinamikUTB/; API https://api-dinamikutb.iscoutb.dev. No equivale a frontend institucional.

**PR consultadas:** 9 abiertas: #38, #40, #41, #43–48. #39/#42 cerradas sin merge. Últimas fusiones #37/#36/#33 permanecen históricas. [Colección](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pulls).

**CI consultado:** [Pages 41966455736](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41966455736): success; [CI 41955243457](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243457): failure, Quality Gate FAILED; [auditoría 41955243503](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243503): success. Los tres sobre la punta citada.

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_DinamikUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pulls) · [frontend/Dockerfile](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/frontend/Dockerfile) · [docker-compose.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/docker-compose.yml) · [deploy/compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/deploy/compose.lab.yaml) · [.github/workflows/deploy-pages.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/.github/workflows/deploy-pages.yml) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#dinamikutb).

<a id="drift"></a>

## Drift

Rama **master**, [be72a2f455ef2157ab6e36b9dd0d5a550e2086c5](https://github.com/ISCOUTB/AS_202620_Drift/commit/be72a2f455ef2157ab6e36b9dd0d5a550e2086c5), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Completar casos contractuales autenticados para sincronización y ajustar tasa/aislamiento para ejecutar la lógica de búsqueda y compatibilidad, manteniendo pruebas negativas de 401/429.
- Demostrar configuración del token administrativo/proxy y recorrido frontend/API institucional de la revisión desplegada; Azure CD no sustituye esa aceptación.
- Mantener requirements y lock sincronizados y probar las versiones efectivamente desplegadas; documentar excepciones de Dependabot cerradas sin merge.
- Conservar como pendientes la retención/redacción de logs y la discrepancia entre retención declarada de IP y limpieza efectiva del limitador.

**Issues:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. Se conservan frontend/API institucional bajo /api, API alternativa Azure y frontend alternativo Vercel; sin prueba funcional nueva.

**PR consultadas:** [#56](https://github.com/ISCOUTB/AS_202620_Drift/pull/56): fusionada 2026-11-02T05:53:06Z; [#55](https://github.com/ISCOUTB/AS_202620_Drift/pull/55): cerrada sin merge; [#54](https://github.com/ISCOUTB/AS_202620_Drift/pull/54): fusionada 2026-11-02T04:13:34Z [Colección](https://github.com/ISCOUTB/AS_202620_Drift/pulls).

**CI consultado:** [CI 41396593756](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41396593756): success (misma punta); [Build and deploy Python app to Azure Web App - drift-utb-202620 41396593677](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41396593677): success (misma punta); [CI 41388246330](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41388246330): success (otra revisión o PR); [Build and deploy Python app to Azure Web App - drift-utb-202620 41387265404](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41387265404): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_Drift/blob/be72a2f455ef2157ab6e36b9dd0d5a550e2086c5/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Drift/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Drift/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#drift).

<a id="elmapita"></a>

## ElMapita

Rama **main**, [899bece9b4ddda9fb27381c966c0b720c93b0fee](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/899bece9b4ddda9fb27381c966c0b720c93b0fee), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior. Se conserva la confirmación docente de presentación y funcionamiento; la ausencia de URL en README no la invalida.

**Próximos pasos:**
- Completar migración de roles existentes a app_metadata y alinear el cliente Flutter, que aún lee userMetadata; verificar acceso administrativo después del cambio.
- Hacer vinculantes E2E y análisis relevante, resolver los 28 hallazgos y restaurar Sonar/Quality Gate; no presentar el verde agregado como todas las comprobaciones aprobadas.
- Revisar los cuatro hallazgos de producción y sus excepciones, sincronizar documentos que aún describen roles/redacción anteriores y probar las PR antes de integrar.
- Añadir URL exacta institucional en README, separando frontend/API, y evidencia fechada de la revisión actual sin invalidar la confirmación docente previa.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Ausente. README exacto no contiene URL pública concreta: la referencia tu-proyecto.supabase.co es un marcador. Se conserva aparte la confirmación docente de funcionamiento.

**PR consultadas:** [#18](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/18): abierta; [#17](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/16): abierta; [#15](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/15): abierta; [#14](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/14): abierta; [#13](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/13): abierta; [#12](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/12): abierta; [#11](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/11): abierta; [#10](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/7): abierta; [#6](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/6): abierta; [#5](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/5): abierta; [#4](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/4): abierta; [#3](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/3): abierta; [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z [Colección](https://github.com/ISCOUTB/AS_202620_ElMapita/pulls).

**CI consultado:** [CI 41396450324](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41396450324): success (misma punta); [CI 41393881243](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41393881243): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/899bece9b4ddda9fb27381c966c0b720c93b0fee/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ElMapita/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ElMapita/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#elmapita).

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Corregir el empaquetado/import de test_simulador y reejecutar CI completo de la PR, incluidos contrato y build, antes de integrar.
- Conciliar las dos fallas de salud/métricas declaradas localmente con el resultado reproducible de CI; adjuntar auditoría fechada posterior al cambio de pytest.
- Mantener claramente separado lo propuesto en PR de lo integrado en master, y el correo simulado del envío real.
- Documentar URL institucional concreta y alcance PostgreSQL frente a rutas heredadas en memoria.

**Issues:** 1 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Ausente. README de master conserva host pendiente y marcadores [host-asignado]; no hay URL pública concreta. El README de la PR #5 tampoco modifica ese dato.

**PR consultadas:** [#5](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/5): abierta; [#4](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/4): cerrada sin merge; [#3](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/3): fusionada 2026-10-26T03:57:38Z; [#2](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/2): fusionada 2026-09-28T02:39:59Z [Colección](https://github.com/ISCOUTB/AS_202620_EnAgenda/pulls).

**CI consultado:** [CI 41389200867](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/41389200867): failure (otra revisión o PR); [Taller mensajes y consistencia 41389200795](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/41389200795): success (otra revisión o PR); [CI 40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): failure (misma punta); [Taller mensajes y consistencia 40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): success (misma punta)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_EnAgenda/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_EnAgenda/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#enagenda).

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, [e0a458097202bb48e25c79d22614d759e3549ee0](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/e0a458097202bb48e25c79d22614d759e3549ee0), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Revisar PR #25 con pg 8.23.1 y dependency-cruiser 18.7.0 y comprobar regresión PostgreSQL real antes de integrarla; CI verde de la rama no acredita main.
- Configurar/rotar el token de operador como secreto en Dokploy y demostrar lecturas, rechazo sin credencial y escritura autorizada sobre el despliegue actual; no compartir el secreto en evidencia.
- Ejecutar las pruebas Flutter añadidas e integración PostgreSQL con base aislada, además del recorrido de extremo a extremo.
- Mantener límites del token compartido (sin identidad individual), completar timeout del pool y control de tasa/proxy, y verificar retención de logs.
- Reducir dependencias Flutter no usadas y revisar las PR propuestas; no inferir durabilidad ni broker de producción a partir del prototipo.

**Issues:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README mantiene https://gimnasio-utb.iscoutb.dev como backend/API, no como interfaz Flutter pública.

**PR consultadas:** [#30](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/30): abierta; [#29](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/29): abierta; [#28](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/28): abierta; [#27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/27): abierta; [#26](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/26): abierta; [#25](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/25): abierta; [#24](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/24): abierta; [#23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/22): abierta; [#21](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/21): abierta; [#20](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/20): abierta; [#31](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/31): fusionada 2026-11-02T00:33:07Z; [#19](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/19): fusionada 2026-11-02T00:23:36Z; [#18](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/18): fusionada 2026-10-26T00:15:00Z [Colección](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pulls).

**CI consultado:** [CI 41541577567](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541577567): success (otra revisión o PR); [CI 41367755427](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41367755427): success (misma punta)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/e0a458097202bb48e25c79d22614d759e3549ee0/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#gimnasioutb).

<a id="inventrack"></a>

## InvenTrack

Rama **main**, [190db13b6591c3e38da125700b2d791bbf8b25e3](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/190db13b6591c3e38da125700b2d791bbf8b25e3), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Acreditar el commit realmente servido después del redespliegue con /health y estados esperados, conservando separado el 503 preventivo de una caída; comprobar acceso interno autorizado sin revelar el token.
- Revisar las cuatro PR de dependencias, mantener hashes completos y ejecutar suite y auditoría antes de integrar.
- Conservar negocio deshabilitado hasta identidad/roles y auditoría de actor; el token interno no sustituye autorización de usuarios.
- Completar persistencia/recuperación durables y retención/redacción de logs; mantener explícitos los límites de locks, idempotencia, broker y DLQ en memoria.

**Issues:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: 7 completed.

**README:** Institucional. README conserva API institucional y alternativa Render, y mantiene explícito que la revisión actual requiere verificación pública posterior al redespliegue; no acredita frontend.

**PR consultadas:** [#11](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/11): abierta; [#10](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/8): abierta [Colección](https://github.com/ISCOUTB/AS_202620_InvenTrack/pulls).

**CI consultado:** [Run Tests 41386451056](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386451056): success (misma punta); [Run Tests 41386175523](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386175523): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/190db13b6591c3e38da125700b2d791bbf8b25e3/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_InvenTrack/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_InvenTrack/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#inventrack).

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [b37f29e6d0a9daf1fd49e22561ba7c388f8cbb51](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/b37f29e6d0a9daf1fd49e22561ba7c388f8cbb51), observada el 5/nov/2026.

La punta incorpora PR37–39 y commits directos posteriores: despliegue automatizado por aplicación, ubicación/portada, cancelación por dueño autenticado antes de Listo (404 para pedido ajeno, 409 fuera de ventana, historial conservado), imágenes de tiendas por estado en Garage/PostgreSQL, mejoras de menú/carrito/contraseña y proxy que retira Content-Encoding/Content-Length tras descompresión. Las pruebas de dominio cubren propiedad, ventana e idempotencia; no se ejecutó prueba HTTP productiva propia.

ADR0036 aceptado ratifica ADR0032–0034 sin reescribir originales; ADR0035 de imágenes está aceptado. No equivale a acta de reunión ni aceptación del despliegue.

CI acredita 168 pruebas aprobadas/1 omitida, contrato 34/34 y Quality Gate PASSED. Auditoría backend sin vulnerabilidades; frontend conserva 8 moderadas porque el umbral bloqueante es high.

Deploy41892183494 pasa sobre esta punta: backend skipped y frontend success. Su log de 4/nov18:58:29 UTC registra /api/version con huella 8da2de19d55f25ed, coincidente con la calculada para esta revisión. Es evidencia del workflow sobre contenido publicado, no prueba viva propia del 5/nov ni aceptación funcional integral; la huella excluye Dockerfile/entorno y otras rutas.

evidencias-s14.md tiene tabla nueva pero conserva párrafo obsoleto de frontend manual y health sin huella. Retiro/mitigación Azure, rate-limit, ensayo de rotación, mediciones y reunión STRIDE siguen pendientes.

**Próximos pasos:**
- Actualizar evidencias S14 con runs/huellas y retirar párrafo de frontend manual/health sin huella.
- Acreditar prueba funcional, cancelación por dueño, imágenes/aislamiento y mediciones ESC01/ESC05 sobre revisión servida.
- Mantener abiertos retiro/mitigación Azure, rate-limit, ensayo de rotación y reunión STRIDE; no confundir automatización con esos compromisos.

**Issues:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. Motivos: 14 completed.

**README:** Institucional. Frontend https://laplacita-app.iscoutb.dev, /panel y /privacidad; API https://laplacita-test.iscoutb.dev/api/v1, /docs y /api/v1/health. Publicación frontend acreditada por log, no aceptación propia.

**PR consultadas:** 10 abiertas: #16, #17, #20, #21, #23, #25–28, #30. Nuevas fusiones #37 (4/nov16:42:35Z), #38 (17:55:18Z), #39 (17:58:26Z). [Colección](https://github.com/ISCOUTB/AS_202620_LaPlacita/pulls).

**CI consultado:** [CI41892183771](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41892183771): success, gate PASSED. [Deploy41892183494](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41892183494): success, backend skipped, frontend publicado. [Log de huella](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41892183494/job/126792289945). Misma punta.

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/b37f29e6d0a9daf1fd49e22561ba7c388f8cbb51/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_LaPlacita/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_LaPlacita/pulls) · [docs/adr/0036-ratificacion-funcionalidades-de-pedidos.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/b37f29e6d0a9daf1fd49e22561ba7c388f8cbb51/docs/adr/0036-ratificacion-funcionalidades-de-pedidos.md) · [docs/evidencias/evidencias-s14.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/b37f29e6d0a9daf1fd49e22561ba7c388f8cbb51/docs/evidencias/evidencias-s14.md) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#laplacita).

<a id="lostvault"></a>

## LostVault

Rama **main**, [2b21f071cf0ff4cffa414fb1e964d719084ec04c](https://github.com/ISCOUTB/AS_202620_LostVault/commit/2b21f071cf0ff4cffa414fb1e964d719084ec04c), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Documentar en README URL institucional exacta y distinguir frontend/API; comprobar el recorrido de login, creación, reclamación y borrado en el despliegue.
- Sustituir usuario único temporal y almacenamiento en memoria por autenticación y persistencia apropiadas, con pruebas y recuperación verificables.
- Reconciliar instrucciones de api/README.md que aún remiten a api/.env.example, eliminado por la PR25.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Ausente. README raíz sin URL pública concreta. Panel de administración y dominio de ejemplo del contrato no identifican frontend/API del proyecto.

**PR consultadas:** [#21](https://github.com/ISCOUTB/AS_202620_LostVault/pull/21): abierta; [#25](https://github.com/ISCOUTB/AS_202620_LostVault/pull/25): fusionada 2026-11-03T16:39:55Z; [#24](https://github.com/ISCOUTB/AS_202620_LostVault/pull/24): fusionada 2026-11-02T03:43:13Z; [#23](https://github.com/ISCOUTB/AS_202620_LostVault/pull/23): fusionada 2026-11-02T03:19:11Z [Colección](https://github.com/ISCOUTB/AS_202620_LostVault/pulls).

**CI consultado:** [Backend checks 41679698418](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41679698418): success (misma punta); [Build 41679698393](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41679698393): success (misma punta); [Flutter checks 41679698370](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41679698370): success (misma punta); [Flutter checks 41676511218](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41676511218): success (otra revisión o PR); [Build 41676511209](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41676511209): success (otra revisión o PR); [Backend checks 41676511119](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41676511119): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_LostVault/blob/2b21f071cf0ff4cffa414fb1e964d719084ec04c/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_LostVault/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_LostVault/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#lostvault).

<a id="mapsutb"></a>

## mapsutb

Rama **master**, [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), observada el 5/nov/2026.

Sin cambio de código, README, issues ni PR. Nuevas ejecuciones programadas de sonda y sincronización Sonar pasan sobre la misma punta; no acreditan migración ni aceptación funcional nueva. README describe Flutter monolítico sin backend propio: no se exige una API inexistente como si estuviera implementada. Frontend y health estático siguen en Firebase externo.

**Próximos pasos:**
- Mantener evidencia reproducible de recarga/reintento del grafo y distinguir sonda de disponibilidad de aceptación funcional.
- Publicar frontend bajo iscoutb.dev y actualizar README; no confundir mapsutb con ElMapita.

**Issues:** 0 abiertas / 54 cerradas; 0 abiertas sin asignar. Motivos: 54 completed.

**README:** Externo. Frontend Firebase externo; README no publica API institucional separada.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z [Colección](https://github.com/ISCOUTB/AS_202620_mapsutb/pulls).

**CI consultado:** [Sonda 42027454727](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/42027454727) y [sincronización Sonar 42025610387](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/42025610387): success, 5/nov, misma punta.

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_mapsutb/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_mapsutb/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#mapsutb).

<a id="pideutb"></a>

## PideUtb

Rama **master**, [d36136024c1d9c2e1fafbdc94ff38d9a31350c05](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/d36136024c1d9c2e1fafbdc94ff38d9a31350c05), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior. PR41 y PR42 permanecen abiertas; #42 apunta a la rama de documentación de #41, no master. Su CI verde no acredita integración y el scanner omitido no acredita Quality Gate. Se conserva presentación y despliegues confirmados por el docente.

**Próximos pasos:**
- Revisar e integrar en orden PR41 y PR42; verificar el destino efectivo de la segunda antes de fusionar.
- Validar concurrencia en PostgreSQL y recorrido del mostrador sin retroceso de estado; documentar después la revisión realmente desplegada.
- Distinguir la consulta pública de Sonar reportada por el equipo del scanner omitido en este CI; acreditar Quality Gate sobre la revisión evaluada.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. README mantiene sitio y mostrador institucionales en pideutb.iscoutb.dev, API/salud/métricas en api-pideutb.iscoutb.dev. Frontend y API siguen en orígenes diferentes. No se verificó en vivo la publicación de las nuevas fotos/animaciones.

**PR consultadas:** [#42](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/42): abierta; [#41](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/41): abierta; [#40](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/40): fusionada 2026-11-02T23:14:22Z; [#39](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/39): fusionada 2026-11-02T19:01:29Z; [#38](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/38): fusionada 2026-10-30T06:16:11Z [Colección](https://github.com/ISCOUTB/AS_202620_PideUtb/pulls).

**CI consultado:** [CI 41716632513](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41716632513): success (otra revisión o PR); [CI 41543855363](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363): success (misma punta)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/d36136024c1d9c2e1fafbdc94ff38d9a31350c05/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_PideUtb/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_PideUtb/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#pideutb).

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [d5b8b500e309e5997a6063f20b6c7da6682ef785](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/d5b8b500e309e5997a6063f20b6c7da6682ef785), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Completar evidencia operativa pospromoción: healthy e ID de db, Image ID/configuración efectiva y montajes de api y db. El health público pasó en S10, pero no acredita esos datos internos.
- Acreditar copia externa independiente y restauración verificable de MySQL y fotografías; conservar abierto T13-10. Un dump dentro del contenedor o persistencia tras recreación en CI no equivalen a recuperación independiente.
- Documentar rollback productivo solo si se realiza de forma autorizada y con recuperación segura: actualmente se acredita ensayo sintético, no ejecución productiva.
- Aportar evidencia accesible y redactada de un anuncio nuevo con universidad declarada no nula y, para aceptación UI, persistencia de Favoritos tras nuevo login. No convertir afiliación declarada en identidad verificada.
- Conservar trazabilidad y distinguir SHA de orquestación HEAD del SHA productivo; mantener checks verdes y no recalificar ni cerrar semanas por estos incrementos posteriores a S13.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. README vigente declara Flutter Web institucional /app/ y API, y promoción del Incremento2 por digest. S10 en CI acredita endpoint público y revisión 46ede525; aceptación funcional manual reportada separadamente. Pages/Azure conservados como historia, sin prueba viva propia nueva.

**PR consultadas:** [#76](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/76): abierta (borrador); [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60): abierta; [#1](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/1): abierta; [#91](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/91): fusionada 2026-11-03T10:35:18Z; [#90](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/90): fusionada 2026-11-03T10:02:06Z; [#89](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/89): fusionada 2026-11-03T10:06:40Z [Colección](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pulls).

**CI consultado:** [S10 contrato del cliente en despliegue publico 41620519911](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519911): success (misma punta); [Compose y persistencia del MVP 41620519792](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519792): success (misma punta); [Flujo real Web y Android 41620519767](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519767): success (misma punta); [Validación Flutter MVP 41620519719](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519719): success (misma punta); [Pruebas del backend 41620519703](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519703): success (misma punta); [Pruebas del backend 41618964919](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41618964919): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/d5b8b500e309e5997a6063f20b6c7da6682ef785/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#proyecto_campusmarket).

<a id="recobra"></a>

## Recobra

Rama **master**, [0dda9abd2c76ef9b10724221225c0ed228197c39](https://github.com/ISCOUTB/AS_202620_Recobra/commit/0dda9abd2c76ef9b10724221225c0ed228197c39), observada el 5/nov/2026.

Master e implementación no cambian. PR abiertas pasan de 10 a 11: #2 Node25 cierra sin merge; #12 propone Node26 para build/runtime, #11 acción Sonar 8.4.0 y #4 renueva ajv/supertest/@types. Ninguna está integrada. Los tres CI nuevos aprueban jobs de pruebas/build, pero Quality Gate se omite por limitarse a push. Logs de #11/#12 muestran SONAR_TOKEN vacío, error «Not authorized or organization not found», salida 3 tolerada con continue-on-error: no acreditan nuevo análisis Sonar. Tests directos usan Node20 mientras contenedor propuesto usa Node26. Se conserva presentación docente.

**Próximos pasos:**
- Revisar compatibilidad de dependencias y probar imagen con el runtime propuesto antes de integrar.
- Obtener análisis/gate real sobre revisión concreta, sin confundir fallo tolerado con Sonar aprobado.
- Mantener protección/rotación y respaldo operativo pendientes. Presentación docente conservada.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README distingue vitrina, Flutter Web y API del mismo host institucional. Presentación docente preservada; sin nueva auditoría funcional.

**PR consultadas:** 11 abiertas: #1, #3–12. #2 cerrada sin merge el 5/nov01:06:59 UTC. Ninguna fusionada. [Colección](https://github.com/ISCOUTB/AS_202620_Recobra/pulls).

**CI consultado:** [#12: 41946258555](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/41946258555), [#11: 41946255709](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/41946255709), [#4: 41946320494](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/41946320494): success en propuestas, no master; gates skipped. Logs scanner [#11](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/41946255709/job/126979082731) y [#12](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/41946258555/job/126979091845) confirman fallo tolerado.

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Recobra/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Recobra/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#recobra).

<a id="routb"></a>

## ROUTB

Rama **master**, [6ad56f4f94be5e2af59664e24fe1be39058d8ecf](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/6ad56f4f94be5e2af59664e24fe1be39058d8ecf), observada el 5/nov/2026.

Sin cambio de master, README, issues ni PR. Nueva purga programada aprobada, no despliegue nuevo. PR72 continúa fusionada solo en Changes, no master; CI de esa rama no debe atribuirse a la punta principal ni al sitio. Se conserva avance entregado según docente.

**Próximos pasos:**
- Integrar o validar por separado el rediseño que permanece en Changes y documentar qué revisión se despliega.
- Restablecer medición reproducible de rendimiento si se pretende mantener la afirmación de 50 solicitudes; la prueba contractual aislada no la sustituye.
- Activar y acreditar análisis Sonar real y comprobar recorrido funcional sobre despliegue institucional, separándolo de build de imagen y purga programada.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend institucional documentado; no se atribuye URL web de frontend al backend. Avance entregado según docente.

**PR consultadas:** [#72](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/72): fusionada 2026-11-04T02:06:59Z; [#71](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/71): fusionada 2026-11-03T23:13:56Z; [#70](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/70): fusionada 2026-11-03T22:32:19Z [Colección](https://github.com/ISCOUTB/AS_202620_ROUTB/pulls).

**CI consultado:** [Purga 41992552797](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41992552797): success, misma punta. [CI master 41737498880](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41737498880): success histórico; [CI Changes 41758602129](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41758602129): otra revisión.

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/6ad56f4f94be5e2af59664e24fe1be39058d8ecf/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ROUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ROUTB/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#routb).

<a id="shareu"></a>

## ShareU

Rama **master**, [20aeb0b77409ca8d98341e9a94fef73b31ad7073](https://github.com/ISCOUTB/AS_202620_ShareU/commit/20aeb0b77409ca8d98341e9a94fef73b31ad7073), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Unificar rutas reales de Dockerfiles y compose y precisar qué frontend se pretende publicar; validar construcción en el flujo del equipo.
- Documentar en README las URLs institucionales exactas una vez configuradas, distinguiendo API/frontend y dominios previstos de servicio verificado.
- Recuperar diagnóstico del workflow fallido sin jobs y registrar revisión desplegada, salud y recorrido funcional; no sustituirlo por una mera configuración o por CI omitido.

**Issues:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: 10 completed.

**README:** Ausente. README conserva <URL Vercel>/<URL Render>; los dominios previstos en Compose no son URLs publicadas en README. Sin prueba viva nueva.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z [Colección](https://github.com/ISCOUTB/AS_202620_ShareU/pulls).

**CI consultado:** [.github/workflows/tests.yml 41746144074](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/41746144074): failure (misma punta); [.github/workflows/tests.yml 41694681482](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/41694681482): failure (otra revisión o PR); [Tests 36479388452](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479388452): failure (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ShareU/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ShareU/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#shareu).

<a id="sistema-de-calificacion-automatica"></a>

## Calificación automática

Rama **master**, [f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Vincular revision.txt y un recorrido frontend→API→worker a la revisión efectivamente servida; la evidencia incorporada describe una revisión del 30/oct.
- Resolver autenticación y autorización antes de cargar datos reales; conservar los límites declarados del presupuesto por proceso y validar concurrencia y recuperación.
- Acreditar respaldo/restauración y EC-07 con el lote objetivo en el entorno servido; no confundir ingesta/worker con calificación OMR integral.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin merge [Colección](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pulls).

**CI consultado:** [CI 41370619522](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41370619522): success (misma punta); [CI 41338415453](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41338415453): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#sistema-de-calificacion-automatica).

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [44e1cc001e60f70a9d156506d81921a743836517](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/44e1cc001e60f70a9d156506d81921a743836517), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior. Se conserva la confirmación docente de presentación y funcionamiento.

**Próximos pasos:**
- Resolver los hallazgos de seguridad de Sonar y obtener Quality Gate OK de la revisión corregida; 340 pruebas exitosas no significan CI completo verde.
- Validar sesiones, renovación/revocación y consentimiento en la revisión servida, incluida migración de cuentas existentes; no seguir marcando T-02/T-08 como ausentes en código.
- Actualizar README y ADR-0011 para reflejar cliente, webhook, métricas JWT, respaldo y alertas reales; mantener límites de alertas en memoria y ausencia de notificación externa.
- Añadir pruebas/análisis Flutter al pipeline y recorridos integrados en dispositivo; la verificación Dart/OSV no ejecuta Flutter.

**Issues:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: 4 completed.

**README:** Institucional. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#17](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/17): fusionada 2026-10-30T22:18:28Z; [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z [Colección](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pulls).

**CI consultado:** [CD 41337016910](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41337016910): skipped (misma punta); [CI 41336869271](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336869271): failure (misma punta); [CI 41336725295](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336725295): failure (otra revisión o PR); [CD 41322405688](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41322405688): skipped (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/44e1cc001e60f70a9d156506d81921a743836517/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#taia_-task-artificial-intelligence-assistant).

<a id="tienda-virtual-utb"></a>

## Tienda virtual UTB

Rama **main**, [172a41f45b0268b5c8e778bcb0cf761550431e74](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/172a41f45b0268b5c8e778bcb0cf761550431e74), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Conservar trazabilidad de las brechas de privacidad y acreditar cada corrección en código y pruebas; la eliminación de la tabla no sustituye la solución.
- Restablecer análisis Sonar efectivo y auditoría SCA reproducible bloqueante; separar resultado del job de pasos realmente ejecutados.
- Documentar URL institucional en README y verificar respaldo/restauración y recorrido funcional de pedidos.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#13](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/13): fusionada 2026-11-02T00:19:42Z; [#12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/12): fusionada 2026-10-25T02:58:28Z; [#11](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/11): fusionada 2026-10-24T20:15:26Z [Colección](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pulls).

**CI consultado:** [Pruebas 41651885651](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/41651885651): success (misma punta); [Pruebas 41366553356](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/41366553356): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/172a41f45b0268b5c8e778bcb0cf761550431e74/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#tienda-virtual-utb).

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [c0ac4594261350b4d7184a3536d6150dbdab2fc5](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/c0ac4594261350b4d7184a3536d6150dbdab2fc5), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior. Se repitió hoy la lectura en navegador de /salud: status ok y database connected, sin hash servido ni flujo integral.

**Próximos pasos:**
- Verificar correspondencia y permisos del token/proyecto/organización Sonar, actualizar la acción obsoleta y obtener análisis y Quality Gate reales antes de desplegar la punta actual.
- Publicar URL de API bajo iscoutb.dev en README y diferenciarla de la app Android.
- Demostrar worker persistente, envío FCM/SMTP real, reintento e idempotencia en dispositivo; el código y los tests no acreditan entrega de mensajes en producción.
- Vincular revisión servida con el commit y completar recorrido funcional, más allá del endpoint de salud.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Externo. API nip.io y cliente Android diferenciados; respuesta de salud observada hoy, no revisión servida identificada.

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/8): fusionada 2026-11-03T00:37:47Z; [#7](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/7): fusionada 2026-11-03T00:25:29Z; [#6](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/6): fusionada 2026-11-03T00:13:54Z [Colección](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pulls).

**CI consultado:** [UTB Tracker CI 41785768543](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41785768543): failure (misma punta); [UTB Tracker CI 41784349055](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41784349055): success (otra revisión o PR); [Release APK 41555375916](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41555375916): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/c0ac4594261350b4d7184a3536d6150dbdab2fc5/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#utb_tracker).

<a id="uniteam"></a>

## uniTeam

Rama **master**, [5e18bc227e0aae35a3f3d797a8405d108a789ef7](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/5e18bc227e0aae35a3f3d797a8405d108a789ef7), observada el 5/nov/2026.

Sin cambio de código, README, issues ni PR. Cuatro nuevas sondas programadas fallan; el log de la última vuelve a usar uniteam-web.onrender.com y uniteam-api.onrender.com, no los destinos DuckDNS de README. Fallan seis comprobaciones: no prueban caída de DuckDNS. Sigue sin remediación nueva el antecedente de auditoría con 48 entradas en cuatro paquetes pese a job verde.

**Próximos pasos:**
- Hacer bloqueante la auditoría preservando el código de salida (pipefail o mecanismo equivalente) y resolver/justificar hallazgos Python con evidencia reproducible.
- Actualizar la sonda a las URL DuckDNS vigentes y repetir las seis comprobaciones antes de interpretar salud.
- Implementar y probar controles de seguridad que los ADR/modelo describen como pendientes; distinguir documentación, actualización de dependencias y mitigación efectiva.
- Publicar frontend y API institucionales; conservar caché como propuesta y taller SQLite separado.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#22](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/22): abierta; [#21](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/21): abierta; [#18](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/18): abierta; [#17](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/16): abierta; [#15](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/15): abierta; [#14](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/14): abierta; [#13](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/13): abierta; [#12](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/12): abierta; [#11](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/11): abierta; [#27](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/27): fusionada 2026-11-02T05:17:31Z; [#26](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/26): fusionada 2026-11-02T05:06:05Z; [#25](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/25): fusionada 2026-11-02T04:55:58Z [Colección](https://github.com/ISCOUTB/AS_202620_uniTeam/pulls).

**CI consultado:** Sondas [41886206046](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41886206046), [41942813183](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41942813183), [41980540780](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41980540780) y [42027032709](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/42027032709): failure sobre la misma punta; última 5/nov12:25:42 UTC.

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/5e18bc227e0aae35a3f3d797a8405d108a789ef7/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_uniTeam/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_uniTeam/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#uniteam).

<a id="xald"></a>

## XALD

Rama **master**, [a79a6085acf3bca4f861473f99094c43899e2b35](https://github.com/ISCOUTB/AS_202620_XALD/commit/a79a6085acf3bca4f861473f99094c43899e2b35), observada el 5/nov/2026.

La consulta del 5/nov conserva la misma punta, README e issues del corte del 4/nov. No se acredita una nueva implementación o publicación por la mera ausencia de cambios. Los pendientes siguientes se conservan del seguimiento anterior.

**Próximos pasos:**
- Validar controles y sincronización en dispositivo con trazabilidad a la revisión servida; health 200 no sustituye la validación del deploy ni del flujo completo.
- Mantener pendientes ejecutor real de procesarPendientes y persistencia de cola/deduplicación hasta aportar evidencia; no inferirlos de la entrega de seguridad.
- Revisar y probar los 15 PR de dependencias antes de integrarlos; conservar análisis reproducible sobre lo que realmente se despliega.
- Publicar API institucional y conciliar experimental con master sin restaurar documentación obsoleta.

**Issues:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. Motivos: 5 completed; 1 duplicate.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#42](https://github.com/ISCOUTB/AS_202620_XALD/pull/42): abierta; [#41](https://github.com/ISCOUTB/AS_202620_XALD/pull/41): abierta; [#40](https://github.com/ISCOUTB/AS_202620_XALD/pull/40): abierta; [#39](https://github.com/ISCOUTB/AS_202620_XALD/pull/39): abierta; [#38](https://github.com/ISCOUTB/AS_202620_XALD/pull/38): abierta; [#37](https://github.com/ISCOUTB/AS_202620_XALD/pull/37): abierta; [#36](https://github.com/ISCOUTB/AS_202620_XALD/pull/36): abierta; [#35](https://github.com/ISCOUTB/AS_202620_XALD/pull/35): abierta; [#34](https://github.com/ISCOUTB/AS_202620_XALD/pull/34): abierta; [#33](https://github.com/ISCOUTB/AS_202620_XALD/pull/33): abierta; [#32](https://github.com/ISCOUTB/AS_202620_XALD/pull/32): abierta; [#31](https://github.com/ISCOUTB/AS_202620_XALD/pull/31): abierta; [#30](https://github.com/ISCOUTB/AS_202620_XALD/pull/30): abierta; [#29](https://github.com/ISCOUTB/AS_202620_XALD/pull/29): abierta; [#28](https://github.com/ISCOUTB/AS_202620_XALD/pull/28): abierta; [#27](https://github.com/ISCOUTB/AS_202620_XALD/pull/27): fusionada 2026-11-02T02:03:07Z; [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z [Colección](https://github.com/ISCOUTB/AS_202620_XALD/pulls).

**CI consultado:** [Android CI 41544247152](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/41544247152): success (otra revisión o PR)

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_XALD/blob/a79a6085acf3bca4f861473f99094c43899e2b35/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_XALD/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_XALD/pulls) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#xald).

<a id="verifacts"></a>

## Verifacts

Rama **master**, [d9ea00ae0e295871b20b0150c3f3c24464d0313d](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/d9ea00ae0e295871b20b0150c3f3c24464d0313d), observada el 5/nov/2026.

Dos commits cambian exclusivamente README, docs/despliegue.md y ADR0010. Ahora se publica https://verifacts.iscoutb.dev, con API /health, /docs, /metrics y POST /analysis: pasa de Externo a Institucional. No se debe seguir marcando el dominio como ausente documentalmente. HTTPS, backend conectado, acceso móvil y persistencia son declaraciones del equipo, sin prueba viva independiente en este corte. No cambia implementación, infraestructura, dependencias ni pruebas. Tests confirma 66 passed, 3 warnings; construcción y smoke pasan. El análisis Sonar sí se ejecuta y espera el gate: QUALITY GATE STATUS: PASSED. Esto no acredita despliegue. docs/despliegue.md conserva instrucciones heredadas para abrir HTTP/desactivar HTTPS automático: deben retirarse, sin recomendar debilitar seguridad. Persisten controles SSRF, propiedad del historial, timeout, tamaño, idempotencia/WAL y SCA declarados pendientes.

**Próximos pasos:**
- Verificar dominio/TLS, frontend/API y persistencia con fecha y revisión servida.
- Retirar instrucciones heredadas de HTTP y desactivación de HTTPS.
- Implementar controles pendientes y aportar SCA reproducible sobre versiones resueltas.

**Issues:** 0 abiertas / 3 cerradas; 0 abiertas sin asignar. Motivos: 3 completed.

**README:** Institucional. Frontend https://verifacts.iscoutb.dev; API /health, /docs, /metrics y POST /analysis del mismo host. Documentación actualizada, no prueba viva propia.

**PR consultadas:** Sin PR en la consulta. [Colección](https://github.com/ISCOUTB/AS_202620_Verifacts/pulls).

**CI consultado:** [Tests 41981739393](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/41981739393): success, 66 pruebas. [SonarCloud 41981739404](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/41981739404): success, gate PASSED. Ambos de la punta actual.

**Fuentes:** [README inmutable](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/d9ea00ae0e295871b20b0150c3f3c24464d0313d/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Verifacts/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Verifacts/pulls) · [docs/despliegue.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/d9ea00ae0e295871b20b0150c3f3c24464d0313d/docs/despliegue.md) · [docs/adr/0010-despliegue-laboratorio-dokploy.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/d9ea00ae0e295871b20b0150c3f3c24464d0313d/docs/adr/0010-despliegue-laboratorio-dokploy.md) · [Antecedentes del 4/nov](seguimiento-2026-11-04.md#verifacts).

## Comprobación viva limitada del 5/nov

Observación independiente en navegador entre **2026-11-05 12:59 y 13:00 UTC** (07:59–08:00 Colombia), sin iniciar sesión ni realizar operaciones. El navegador no expuso cabeceras HTTP: no se presentan códigos medidos.

- [Dinamik frontend Pages](https://iscoutb.github.io/AS_202620_DinamikUTB/): se renderiza la portada morada completa, título DinamikUTB, «¿Aún no sabes qué te falta para graduarte?» y botón «Iniciar sesión». Acredita renderizado de portada, no autenticación ni flujo integral.
- [Dinamik API /health vigente](https://api-dinamikutb.iscoutb.dev/health): contenido visible «404 page not found». No se obtuvo respuesta de salud. No confundir con el hostname anterior api.dinamikutb.iscoutb.dev ni afirmar código HTTP medido.
- [UTB Tracker /salud](https://129-80-171-141.nip.io/salud): contenido visible {"status":"ok","proyecto":"UTB Tracker","version":"1.0.0","database":"connected"}. Acredita esa respuesta, no el hash servido, entrega de notificaciones ni la aplicación completa.
- ShareU: el README conserva marcadores; no se repitió prueba viva en este corte.

La disponibilidad observada es limitada a esa sesión y no demuestra aceptación funcional integral ni correspondencia del servicio con un commit.
