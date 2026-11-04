# Seguimiento de los 23 proyectos · 4 de noviembre de 2026

Consulta del **4 de noviembre de 2026**, con observaciones fechadas por proyecto (UTC). Seguimiento documental de los 23 proyectos del listado vigente, posterior al cierre de S13, sin recalificar ni reabrir semanas. Calificaciones, planillas, matrices y cortes históricos permanecen intactos.

**43 issues abiertas y 132 cerradas** (131 completed; 1 duplicate); 19 abiertas sin asignar. Conteo del corte, excluyendo PR.

README: **12 con algún endpoint institucional; 6 con enlaces externos; 5 sin URL pública concreta**. Un endpoint API no demuestra frontend publicado; ausencia de URL no demuestra ausencia de trabajo o despliegue.

Se conservan las confirmaciones del docente: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. No equivalen a pruebas funcionales nuevas de este corte.

Se consultaron README, historial, issues (excluyendo PR), propuestas y CI sin ejecutar código estudiantil. Código fusionado, CI, publicación y aceptación funcional son evidencias distintas. Los estados OPEN/CLOSED y motivos corresponden a GitHub Issues; no se obtuvieron estados personalizados del tablero Projects. Las comprobaciones vivas, cuando se completan, se describen con alcance y fecha; no equivalen a aceptación funcional integral.

Los cierres dominicales de S11 (18/oct), S12 (25/oct) y S13 (1/nov), a las 23:59:59 Colombia, se conservan en el [índice cronológico](revision-semanas-11-13-2026-11-03.md). Los avances de este corte no se atribuyen retroactivamente a esas entregas.

[Issues y motivos](seguimiento-issues-2026-11-04.md) · [README y despliegues](seguimiento-despliegues-2026-11-04.md) · [Antecedentes del 3/nov](seguimiento-s12-2026-11-03.md)

## Cambios respecto al 3/nov

- **Clubs UTB**: Corrige backend/Dockerfile encadenando mkdir, chown y chmod mediante && en una sola instrucción RUN. Es una corrección de construcción, no una funcionalidad ni un despliegue acreditado. Las nuevas ejecuciones de backend-tests y contrato figuran failure y ambas devuelven cero jobs: no se puede afirmar que las pruebas hayan corrido ni atribuir la causa sin logs. README sigue sin URL pública concreta; cero issues reales y PR #1 pendiente. Los cambios son posteriores al cierre dominical de S13.
- **DinamikUTB**: Cambia la ruta automática de publicación: deploy-pages se activa con push a master y publish-frontend-image queda solo manual. Pages construye y publica correctamente la punta actual (run 41697699386; log de publicación a las 18:53 UTC del 3/nov), con CNAME dinamikutb.iscoutb.dev y API institucional como destino. CI de master y auditoría pasan. Esto no corrige ni demuestra resuelto el antiguo permiso GHCR: el Compose de Dokploy continúa consumiendo FRONTEND_IMAGE y el workflow Pages no actualiza esa imagen ni dispara Dokploy. README mantiene web/API institucionales y afirma entorno Dokploy activo, por lo que conviene aclarar cuál sirve el dominio. La sonda web no entregó respuesta; una comprobación independiente posterior en navegador (4/nov, 13:01:39–13:02:12 UTC) mostró «404 page not found» en frontend y «upstream connect error…remote connection failure» en API/health. No se capturaron códigos HTTP ni hash servido: son errores observados en esa sesión, no prueba de caída global ni fallo del workflow Pages. La PR #40 actualiza checkout, sigue sin integrar y falla Sonar aunque backend/Flutter y auditoría pasan; no debe confundirse con el CI verde de master. No se atribuyen estos cambios posteriores al cierre a S13.
- **LostVault**: PR #25 integrada en main añade inicio de sesión JWT temporal de usuario único configurado, alta de objetos y borrado permitido solo a quien los reportó, con validación 422 y puerto configurable. El contrato OpenAPI se actualiza en la punta posterior. El almacenamiento sigue en memoria y DATABASE_URL se declara pero aún no se usa; no es autenticación multiusuario ni persistencia productiva. Tres workflows de la punta aprueban; el log Backend checks acredita 27 pruebas de API y 18 de mensajería. README raíz sigue sin URL pública concreta del proyecto; el panel de administración no equivale a frontend/API publicado. No se acredita despliegue ni aceptación funcional nueva.
- **PideUtb**: Master y README no cambian. Se abren PR #41 (documentación y ADR del costo de separar el esquema de datos, destino master) y #42 (corrección propuesta del avance concurrente de pedidos), apilada sobre la rama de #41, no directamente sobre master. La lectura del diff confirma que #42 añade estado esperado al UPDATE y respuesta 409 si otra operación ganó; no se ejecutó una reproducción propia ni se acredita incidente productivo. Su CI de rama aprueba: log Python3.11 registra 589 pruebas aprobadas y 3 omitidas, más 107 con PostgreSQL. El job Sonar vuelve a omitir el análisis por ausencia de SONAR_TOKEN: verde no acredita Quality Gate de esa revisión. Las dos PR siguen abiertas, de modo que cambios, conteo 592 y afirmaciones del equipo no son implementación fusionada ni despliegue. Se conserva la presentación y despliegues confirmados por el docente.
- **ROUTB**: PR #70/#71 integradas en master después del cierre S13: ajustes de Dependabot y aislamiento de pruebas con advisory lock PostgreSQL, coordenadas aisladas y OSRM simulado. El test anterior de 50 respuestas se reduce a una respuesta contractual por caso: no acredita rendimiento con 50 solicitudes. CI de la punta aprueba 108 pruebas y 2 de contrato, auditoría y construcción de imagen; Sonar sigue siendo un echo de reserva, sin scanner/Quality Gate real. Las 13 PR de dependencias antes abiertas figuran cerradas sin merge. PR #72 de rediseño visual se fusionó únicamente en Changes, no en master: no debe atribuirse a la versión principal ni al sitio. README mantiene routb.iscoutb.dev como API, sin nuevo frontend institucional acreditado. Se conserva avance confirmado por el docente, sin reabrir S13.
- **ShareU**: Desde el 3/nov se incorpora el sitio extraído en shareuwensite-main (archivos HTML/JS y configuración Firebase) y configuración Docker/Dokploy. Dockploy/compose.lab.yml prevé shareu.iscoutb.dev para web y api-shareu.iscoutb.dev para API, pero apunta a deploy/Dockerfile.api y ../../deploy/Dockerfile.web: el árbol de esa revisión solo contiene los Dockerfiles en Dockploy/. Es una discrepancia de rutas comprobada por lectura, no un despliegue fallido reproducido. Además el servicio web construye app/frontend (Next.js), no automáticamente el sitio HTML recién incorporado. README raíz conserva placeholders Vercel/Render, por lo que no documenta aún URL pública concreta. Workflow de la punta termina failure sin jobs devueltos; no permite atribuir la causa a Sonar ni acreditar publicación. Se mantienen 10 issues abiertas/10 cerradas y PR22/23 abiertas. En comprobación independiente de navegador del 4/nov 13:01:39–13:02:12 UTC, las raíces https://shareu.iscoutb.dev y https://api-shareu.iscoutb.dev mostraron «404 page not found». Es contenido visible, sin captura del código HTTP ni del hash servido; la raíz de la API no sustituye su endpoint de salud.
- **Tienda virtual UTB**: El commit 172a41f modifica únicamente docs/seguridad-amenazas-privacidad.md: retira la tabla de ocho brechas entre promesas de privacidad y código, y conserva el apartado de derechos e incidentes. No contiene cambios de implementación que acrediten subsanar consentimiento, supresión, rectificación o retención; eliminar la tabla no cierra esos pendientes. El nuevo run 41651885651 pasa frontend y backend, pero el job Sonar figura success con checkout, cobertura y análisis skipped, por lo que no demuestra un nuevo análisis ni Quality Gate. README mantiene frontend sslip.io externo y no documenta dominio institucional. Cero issues y trece PR fusionadas permanecen sin cambios.
- **UTB Tracker**: Avance sustantivo hasta c0ac459: dependencias actualizadas (Starlette 1.3.1 y PyJWT 2.15.1), retiradas las exclusiones y continue-on-error de pip-audit, aislamiento de tests sin fallback a DATABASE_URL y notificador real Firebase Admin/SMTP en código. El run 41785768543 pasa 79 pruebas, incluida concurrencia PostgreSQL con una reserva aceptada y otra rechazada, y pip-audit informa cero vulnerabilidades conocidas. Sin embargo, el análisis Sonar falla por «Not authorized or project not found»: es un bloqueo de acceso/configuración antes de obtener Quality Gate; deploy de esa punta queda skipped. El run anterior 41784349055 sí registra checkout d844ad6, migraciones, reinicio y /salud con database connected tras un reintento por 502, por lo que el 502 previo no se mantiene como caída vigente. Una lectura independiente actual también observa salud OK, sin hash servido ni validación funcional del flujo completo. README añade API nip.io externa, no iscoutb.dev. La entrega push al dispositivo y operación permanente del worker aún requieren evidencia específica.

Los demás proyectos se revalidaron. No se añaden secciones individuales repetidas por sondas rutinarias o evidencia sin cambios sustantivos. Este informe resume el delta y enlaza el corte anterior para conservar los antecedentes sin duplicarlos.

<a id="audioshare"></a>

## AudioShare

Rama **master**, [b2eb60d34a3ee41e2c632aa78e5a7021356461da](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/b2eb60d34a3ee41e2c632aa78e5a7021356461da), fecha del commit 2026-11-02T04:37:45Z (UTC). Observación: 2026-11-04T13:02:00Z.

Sin cambios sustantivos respecto al corte del 3/nov: se revalidaron la punta principal, README, issues excluyendo PR, propuestas y ejecuciones recientes. Se conservan los avances y pendientes del informe anterior; no se presenta el CI histórico como ejecución nueva ni se acredita una nueva revisión desplegada.

**Próximos pasos:**
- Redesplegar mediante el flujo Dokploy y demostrar frontend, API y sincronización entre dispositivos; publicar imagen Docker Hub no acredita la revisión servida.
- Implementar y probar controles de acceso por sala, cuotas de subida y límites de tasa; acompañar borrado/caducidad con una política y aviso que no prometan supresión ya operativa.
- Integrar auditoría de producción al CI y resolver o justificar con análisis completo los seis hallazgos de desarrollo; actualizar la acción Sonar que emite advertencia de seguridad.
- Documentar la prueba Flutter omitida y validar descarga, reintento y reingreso en dispositivos reales.

**Issues:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar. Motivos: 2 completed.

**README:** Institucional. README mantiene un mismo origen institucional para frontend y API. Conserva su comprobación histórica del 26/oct de cliente legado y /rooms 404; no se repitió prueba viva.

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/8): abierta; [#9](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/9): fusionada 2026-10-26T04:47:48Z; [#7](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/7): fusionada 2026-10-26T03:42:05Z; [#2](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/2): fusionada 2026-09-01T14:56:35Z

**CI consultado:** [CI 41389534440](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534440): success (misma punta); [Publicar imagen 41389534404](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534404): success (misma punta); [Flutter 41389534313](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534313): success (misma punta); [Flutter 41387713791](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713791): success (otra revisión o PR); [Publicar imagen 41387713751](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713751): success (otra revisión o PR); [CI 41387713744](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713744): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b2eb60d34a3ee41e2c632aa78e5a7021356461da/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_AudioShare/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_AudioShare/pulls) · [b2eb60d34a3ee41e2c632aa78e5a7021356461da](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/b2eb60d34a3ee41e2c632aa78e5a7021356461da) · [41389534440](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534440) · [41389534404](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534404) · [41389534313](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534313) · [41387713791](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713791) · [41387713751](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713751) · [41387713744](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713744) · [Antecedentes](seguimiento-s12-2026-11-03.md#audioshare).

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, [7fdc502e0a876e77479d40fadb942fdb10a07d52](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7fdc502e0a876e77479d40fadb942fdb10a07d52), fecha del commit 2026-11-03T15:11:23Z (UTC). Observación: 2026-11-04T13:02:00Z.

Corrige backend/Dockerfile encadenando mkdir, chown y chmod mediante && en una sola instrucción RUN. Es una corrección de construcción, no una funcionalidad ni un despliegue acreditado. Las nuevas ejecuciones de backend-tests y contrato figuran failure y ambas devuelven cero jobs: no se puede afirmar que las pruebas hayan corrido ni atribuir la causa sin logs. README sigue sin URL pública concreta; cero issues reales y PR #1 pendiente. Los cambios son posteriores al cierre dominical de S13.

**Próximos pasos:**
- Revisar la validación de los workflows y obtener una ejecución verificable con jobs/logs, además de comprobar la construcción del contenedor.
- Documentar URL exacta de frontend y API en iscoutb.dev dentro de README y demostrar la revisión publicada.
- Corregir idempotencia por autor/operación, exposición de matrícula y permisos por rol; conciliar privacidad que aún describe subida sin sesión con el cambio implementado.
- Completar decisiones y marcadores de privacidad/retención, y publicar URL exacta de frontend/API en README.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Ausente. README declara Dokploy y HTTPS, pero no ofrece un host público concreto; localhost y variables API_URL no cuentan como URL pública.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta; [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3): fusionada 2026-10-05T05:46:36Z; [#2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2): fusionada 2026-09-21T04:56:52Z

**CI consultado:** [.github/workflows/contrato.yml 41661273849](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41661273849): failure (misma punta); [.github/workflows/backend-tests.yml 41661271676](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41661271676): failure (misma punta); [.github/workflows/backend-tests.yml 41379945028](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379945028): failure (otra revisión o PR); [.github/workflows/contrato.yml 41379943754](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379943754): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7fdc502e0a876e77479d40fadb942fdb10a07d52/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pulls) · [7fdc502e0a876e77479d40fadb942fdb10a07d52](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7fdc502e0a876e77479d40fadb942fdb10a07d52) · [41661273849](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41661273849) · [41661271676](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41661271676) · [41379945028](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379945028) · [41379943754](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379943754) · [41351122397](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41351122397) · [41351121190](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41351121190) · [Antecedentes](seguimiento-s12-2026-11-03.md#clubs_utb).

<a id="dinamikutb"></a>

## DinamikUTB

Rama **master**, [87a28a0d8cb53ff4e693dd451013018bd0d21068](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/87a28a0d8cb53ff4e693dd451013018bd0d21068), fecha del commit 2026-11-03T18:50:49Z (UTC). Observación: 2026-11-04T13:02:00Z.

Cambia la ruta automática de publicación: deploy-pages se activa con push a master y publish-frontend-image queda solo manual. Pages construye y publica correctamente la punta actual (run 41697699386; log de publicación a las 18:53 UTC del 3/nov), con CNAME dinamikutb.iscoutb.dev y API institucional como destino. CI de master y auditoría pasan. Esto no corrige ni demuestra resuelto el antiguo permiso GHCR: el Compose de Dokploy continúa consumiendo FRONTEND_IMAGE y el workflow Pages no actualiza esa imagen ni dispara Dokploy. README mantiene web/API institucionales y afirma entorno Dokploy activo, por lo que conviene aclarar cuál sirve el dominio. La sonda web no entregó respuesta; una comprobación independiente posterior en navegador (4/nov, 13:01:39–13:02:12 UTC) mostró «404 page not found» en frontend y «upstream connect error…remote connection failure» en API/health. No se capturaron códigos HTTP ni hash servido: son errores observados en esa sesión, no prueba de caída global ni fallo del workflow Pages. La PR #40 actualiza checkout, sigue sin integrar y falla Sonar aunque backend/Flutter y auditoría pasan; no debe confundirse con el CI verde de master. No se atribuyen estos cambios posteriores al cierre a S13.

**Próximos pasos:**
- Unificar la documentación y el destino efectivo del dominio: aclarar frontend en Pages frente al servicio web de Dokploy que aún consume GHCR.
- Verificar DNS/TLS, carga real de Flutter y comunicación con API, incluyendo login y recorrido de negocio; publicar evidencia de la revisión realmente servida.
- Revisar el fallo Sonar de la PR #40 antes de integrarla; conservar la distinción con master aprobado.
- Añadir evidencia de Quality Gate con resultado específico de esta revisión; mantener separados scan enviado y gate aprobado. Verificar concurrencia sobre PostgreSQL y restauración de respaldos antes de considerar cerrada la deuda.
- Probar y definir tratamiento de JWT anteriores sin sig: el condicional actual solo comprueba la firma de contraseña cuando sig tiene valor; las sesiones legadas no quedan cubiertas por la nueva revocación.

**Issues:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. README documenta frontend https://dinamikutb.iscoutb.dev y API https://api.dinamikutb.iscoutb.dev. Pages publicó el artefacto y devuelve como entorno http://dinamikutb.iscoutb.dev/. Navegador independiente 4/nov 13:01:39–13:02:12 UTC: frontend muestra «404 page not found» y API/health «upstream connect error…remote connection failure». Sin captura del código HTTP ni hash servido, no se acredita aceptación funcional; el health 200 del README es una declaración del equipo.

**PR consultadas:** [#48](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/48): abierta; [#47](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/47): abierta; [#46](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/46): abierta; [#45](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/45): abierta; [#44](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/44): abierta; [#43](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/43): abierta; [#42](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/42): abierta; [#41](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/41): abierta; [#40](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/40): abierta; [#39](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/39): abierta; [#38](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/38): abierta; [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37): fusionada 2026-10-23T03:04:11Z; [#36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36): fusionada 2026-10-23T01:01:46Z; [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35): cerrada sin merge

**CI consultado:** [Auditoría de dependencias 41698218476](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41698218476): success (otra revisión o PR); [CI 41698218474](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41698218474): failure (otra revisión o PR); [Deploy frontend (GitHub Pages) 41697699386](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41697699386): success (misma punta); [Auditoría de dependencias 41697699384](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41697699384): success (misma punta); [CI 41697699255](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41697699255): success (misma punta); [Publish frontend image 41554940766](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41554940766): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/87a28a0d8cb53ff4e693dd451013018bd0d21068/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_DinamikUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pulls) · [87a28a0d8cb53ff4e693dd451013018bd0d21068](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/87a28a0d8cb53ff4e693dd451013018bd0d21068) · [41698218476](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41698218476) · [41698218474](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41698218474) · [41698212138](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41698212138) · [41698211787](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41698211787) · [41697914048](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41697914048) · [41697699386](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41697699386) · [deploy-pages.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/87a28a0d8cb53ff4e693dd451013018bd0d21068/.github/workflows/deploy-pages.yml) · [publish-frontend-image.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/87a28a0d8cb53ff4e693dd451013018bd0d21068/.github/workflows/publish-frontend-image.yml) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/87a28a0d8cb53ff4e693dd451013018bd0d21068/deploy/compose.lab.yaml) · [40](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/40) · [Antecedentes](seguimiento-s12-2026-11-03.md#dinamikutb).

<a id="drift"></a>

## Drift

Rama **master**, [be72a2f455ef2157ab6e36b9dd0d5a550e2086c5](https://github.com/ISCOUTB/AS_202620_Drift/commit/be72a2f455ef2157ab6e36b9dd0d5a550e2086c5), fecha del commit 2026-11-02T05:53:05Z (UTC). Observación: 2026-11-04T13:02:00Z.

Sin cambios sustantivos respecto al corte del 3/nov: se revalidaron la punta principal, README, issues excluyendo PR, propuestas y ejecuciones recientes. Se conservan los avances y pendientes del informe anterior; no se presenta el CI histórico como ejecución nueva ni se acredita una nueva revisión desplegada.

**Próximos pasos:**
- Completar casos contractuales autenticados para sincronización y ajustar tasa/aislamiento para ejecutar la lógica de búsqueda y compatibilidad, manteniendo pruebas negativas de 401/429.
- Demostrar configuración del token administrativo/proxy y recorrido frontend/API institucional de la revisión desplegada; Azure CD no sustituye esa aceptación.
- Mantener requirements y lock sincronizados y probar las versiones efectivamente desplegadas; documentar excepciones de Dependabot cerradas sin merge.
- Conservar como pendientes la retención/redacción de logs y la discrepancia entre retención declarada de IP y limpieza efectiva del limitador.

**Issues:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. Se conservan frontend/API institucional bajo /api, API alternativa Azure y frontend alternativo Vercel; sin prueba funcional nueva.

**PR consultadas:** [#56](https://github.com/ISCOUTB/AS_202620_Drift/pull/56): fusionada 2026-11-02T05:53:06Z; [#55](https://github.com/ISCOUTB/AS_202620_Drift/pull/55): cerrada sin merge; [#54](https://github.com/ISCOUTB/AS_202620_Drift/pull/54): fusionada 2026-11-02T04:13:34Z

**CI consultado:** [CI 41396593756](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41396593756): success (misma punta); [Build and deploy Python app to Azure Web App - drift-utb-202620 41396593677](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41396593677): success (misma punta); [CI 41388246330](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41388246330): success (otra revisión o PR); [Build and deploy Python app to Azure Web App - drift-utb-202620 41387265404](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41387265404): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Drift/blob/be72a2f455ef2157ab6e36b9dd0d5a550e2086c5/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Drift/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Drift/pulls) · [be72a2f455ef2157ab6e36b9dd0d5a550e2086c5](https://github.com/ISCOUTB/AS_202620_Drift/commit/be72a2f455ef2157ab6e36b9dd0d5a550e2086c5) · [41396721922](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41396721922) · [41396593756](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41396593756) · [41396593677](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41396593677) · [41388246330](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41388246330) · [41387404463](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41387404463) · [41387274649](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41387274649) · [Antecedentes](seguimiento-s12-2026-11-03.md#drift).

<a id="elmapita"></a>

## ElMapita

Rama **main**, [899bece9b4ddda9fb27381c966c0b720c93b0fee](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/899bece9b4ddda9fb27381c966c0b720c93b0fee), fecha del commit 2026-11-02T05:51:18Z (UTC). Observación: 2026-11-04T13:02:00Z.

Sin cambios sustantivos respecto al corte del 3/nov: se revalidaron la punta principal, README, issues excluyendo PR, propuestas y ejecuciones recientes. Se conservan los avances y pendientes del informe anterior; no se presenta el CI histórico como ejecución nueva ni se acredita una nueva revisión desplegada.

**Próximos pasos:**
- Completar migración de roles existentes a app_metadata y alinear el cliente Flutter, que aún lee userMetadata; verificar acceso administrativo después del cambio.
- Hacer vinculantes E2E y análisis relevante, resolver los 28 hallazgos y restaurar Sonar/Quality Gate; no presentar el verde agregado como todas las comprobaciones aprobadas.
- Revisar los cuatro hallazgos de producción y sus excepciones, sincronizar documentos que aún describen roles/redacción anteriores y probar las PR antes de integrar.
- Añadir URL exacta institucional en README, separando frontend/API, y evidencia fechada de la revisión actual sin invalidar la confirmación docente previa.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Ausente. README exacto no contiene URL pública concreta: la referencia tu-proyecto.supabase.co es un marcador. Se conserva aparte la confirmación docente de funcionamiento.

**PR consultadas:** [#18](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/18): abierta; [#17](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/16): abierta; [#15](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/15): abierta; [#14](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/14): abierta; [#13](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/13): abierta; [#12](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/12): abierta; [#11](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/11): abierta; [#10](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/7): abierta; [#6](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/6): abierta; [#5](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/5): abierta; [#4](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/4): abierta; [#3](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/3): abierta; [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z

**CI consultado:** [CI 41396450324](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41396450324): success (misma punta); [CI 41393881243](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41393881243): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/899bece9b4ddda9fb27381c966c0b720c93b0fee/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ElMapita/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ElMapita/pulls) · [899bece9b4ddda9fb27381c966c0b720c93b0fee](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/899bece9b4ddda9fb27381c966c0b720c93b0fee) · [41489376212](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41489376212) · [41396450324](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41396450324) · [41394696431](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41394696431) · [41393881243](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41393881243) · [41393871744](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41393871744) · [41393870912](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41393870912) · [Antecedentes](seguimiento-s12-2026-11-03.md#elmapita).

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), fecha del commit 2026-10-26T03:57:38Z (UTC). Observación: 2026-11-04T13:02:00Z.

Sin cambios sustantivos respecto al corte del 3/nov: se revalidaron la punta principal, README, issues excluyendo PR, propuestas y ejecuciones recientes. Se conservan los avances y pendientes del informe anterior; no se presenta el CI histórico como ejecución nueva ni se acredita una nueva revisión desplegada.

**Próximos pasos:**
- Corregir el empaquetado/import de test_simulador y reejecutar CI completo de la PR, incluidos contrato y build, antes de integrar.
- Conciliar las dos fallas de salud/métricas declaradas localmente con el resultado reproducible de CI; adjuntar auditoría fechada posterior al cambio de pytest.
- Mantener claramente separado lo propuesto en PR de lo integrado en master, y el correo simulado del envío real.
- Documentar URL institucional concreta y alcance PostgreSQL frente a rutas heredadas en memoria.

**Issues:** 1 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Ausente. README de master conserva host pendiente y marcadores [host-asignado]; no hay URL pública concreta. El README de la PR #5 tampoco modifica ese dato.

**PR consultadas:** [#5](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/5): abierta; [#4](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/4): cerrada sin merge; [#3](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/3): fusionada 2026-10-26T03:57:38Z; [#2](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/2): fusionada 2026-09-28T02:39:59Z

**CI consultado:** [CI 41389200867](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/41389200867): failure (otra revisión o PR); [Taller mensajes y consistencia 41389200795](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/41389200795): success (otra revisión o PR); [CI 40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): failure (misma punta); [Taller mensajes y consistencia 40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_EnAgenda/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_EnAgenda/pulls) · [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b) · [41389200867](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/41389200867) · [41389200795](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/41389200795) · [40266609521](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521) · [40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410) · [40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284) · [40266600206](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266600206) · [Antecedentes](seguimiento-s12-2026-11-03.md#enagenda).

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, [e0a458097202bb48e25c79d22614d759e3549ee0](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/e0a458097202bb48e25c79d22614d759e3549ee0), fecha del commit 2026-11-02T00:33:07Z (UTC). Observación: 2026-11-04T13:02:00Z.

Sin cambios sustantivos respecto al corte del 3/nov: se revalidaron la punta principal, README, issues excluyendo PR, propuestas y ejecuciones recientes. Se conservan los avances y pendientes del informe anterior; no se presenta el CI histórico como ejecución nueva ni se acredita una nueva revisión desplegada.

**Próximos pasos:**
- Revisar PR #25 con pg 8.23.1 y dependency-cruiser 18.7.0 y comprobar regresión PostgreSQL real antes de integrarla; CI verde de la rama no acredita main.
- Configurar/rotar el token de operador como secreto en Dokploy y demostrar lecturas, rechazo sin credencial y escritura autorizada sobre el despliegue actual; no compartir el secreto en evidencia.
- Ejecutar las pruebas Flutter añadidas e integración PostgreSQL con base aislada, además del recorrido de extremo a extremo.
- Mantener límites del token compartido (sin identidad individual), completar timeout del pool y control de tasa/proxy, y verificar retención de logs.
- Reducir dependencias Flutter no usadas y revisar las PR propuestas; no inferir durabilidad ni broker de producción a partir del prototipo.

**Issues:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README mantiene https://gimnasio-utb.iscoutb.dev como backend/API, no como interfaz Flutter pública.

**PR consultadas:** [#30](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/30): abierta; [#29](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/29): abierta; [#28](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/28): abierta; [#27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/27): abierta; [#26](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/26): abierta; [#25](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/25): abierta; [#24](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/24): abierta; [#23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/22): abierta; [#21](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/21): abierta; [#20](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/20): abierta; [#31](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/31): fusionada 2026-11-02T00:33:07Z; [#19](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/19): fusionada 2026-11-02T00:23:36Z; [#18](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/18): fusionada 2026-10-26T00:15:00Z

**CI consultado:** [CI 41541577567](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541577567): success (otra revisión o PR); [CI 41367755427](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41367755427): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/e0a458097202bb48e25c79d22614d759e3549ee0/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pulls) · [e0a458097202bb48e25c79d22614d759e3549ee0](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/e0a458097202bb48e25c79d22614d759e3549ee0) · [41541577567](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541577567) · [41541570786](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541570786) · [41541430019](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541430019) · [41541425290](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541425290) · [41541424862](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541424862) · [41541424703](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541424703) · [Antecedentes](seguimiento-s12-2026-11-03.md#gimnasioutb).

<a id="inventrack"></a>

## InvenTrack

Rama **main**, [190db13b6591c3e38da125700b2d791bbf8b25e3](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/190db13b6591c3e38da125700b2d791bbf8b25e3), fecha del commit 2026-11-02T04:04:45Z (UTC). Observación: 2026-11-04T13:02:00Z.

Sin cambios sustantivos respecto al corte del 3/nov: se revalidaron la punta principal, README, issues excluyendo PR, propuestas y ejecuciones recientes. Se conservan los avances y pendientes del informe anterior; no se presenta el CI histórico como ejecución nueva ni se acredita una nueva revisión desplegada.

**Próximos pasos:**
- Acreditar el commit realmente servido después del redespliegue con /health y estados esperados, conservando separado el 503 preventivo de una caída; comprobar acceso interno autorizado sin revelar el token.
- Revisar las cuatro PR de dependencias, mantener hashes completos y ejecutar suite y auditoría antes de integrar.
- Conservar negocio deshabilitado hasta identidad/roles y auditoría de actor; el token interno no sustituye autorización de usuarios.
- Completar persistencia/recuperación durables y retención/redacción de logs; mantener explícitos los límites de locks, idempotencia, broker y DLQ en memoria.

**Issues:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: 7 completed.

**README:** Institucional. README conserva API institucional y alternativa Render, y mantiene explícito que la revisión actual requiere verificación pública posterior al redespliegue; no acredita frontend.

**PR consultadas:** [#11](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/11): abierta; [#10](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/8): abierta

**CI consultado:** [Run Tests 41386451056](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386451056): success (misma punta); [Run Tests 41386175523](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386175523): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/190db13b6591c3e38da125700b2d791bbf8b25e3/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_InvenTrack/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_InvenTrack/pulls) · [190db13b6591c3e38da125700b2d791bbf8b25e3](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/190db13b6591c3e38da125700b2d791bbf8b25e3) · [41436852813](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41436852813) · [41386451056](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386451056) · [41386175523](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386175523) · [41385526380](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41385526380) · [41385316356](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41385316356) · [41385220045](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41385220045) · [Antecedentes](seguimiento-s12-2026-11-03.md#inventrack).

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [d2fd2cd7ea984997bcf6e6775fa797fe0315974c](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/d2fd2cd7ea984997bcf6e6775fa797fe0315974c), fecha del commit 2026-11-02T19:16:38Z (UTC). Observación: 2026-11-04T13:02:00Z.

Revalidación del 4/nov frente al 3/nov: misma punta principal, README, issues y PR; no se identifica avance sustantivo nuevo. Se conserva la retroalimentación anterior sin trasladar cambios posteriores a las semanas cerradas. No aparece evidencia nueva que cierre los compromisos de Azure legado, STRIDE, rate-limit o ensayo de rotación. Los resultados de pruebas y despliegue citados el 3/nov son antecedentes, no verificaciones nuevas.

**Próximos pasos:**
- Validar en equipo STRIDE y ADR0030–0033, conservando el estado propuesto donde corresponda; revisar #28/#30 antes de integrar.
- Acreditar retiro o mitigación de Azure legado y resultado de la sesión prevista para el 3/nov; aplicar y comprobar rate-limit previsto para el 4/nov y registrar ensayo real de rotación.
- Verificar con autorización que backend nuevo preceda al frontend manual, vincular SHA servido y probar agrupación multitienda, compatibilidad v1, cancelación por admin, aislamiento y conservación de pedidos. Un webhook y health200 no equivalen a aceptación integral.

**Issues:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. Motivos: 14 completed.

**README:** Institucional. README mantiene app/PWA y panel institucionales separados de la API. Azure no es URL vigente del README, pero S13 mantiene pendiente acreditar su apagado; la documentación de retiro no demuestra retiro operativo. Sin prueba viva nueva.

**PR consultadas:** [#30](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/30): abierta; [#28](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/28): abierta; [#27](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/27): abierta; [#26](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/26): abierta; [#25](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/25): abierta; [#23](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/23): abierta; [#21](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/21): abierta; [#20](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/20): abierta; [#17](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/16): abierta; [#36](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/36): fusionada 2026-11-02T19:16:39Z; [#35](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/35): fusionada 2026-11-02T18:47:20Z; [#34](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/34): fusionada 2026-11-02T18:18:08Z

**CI consultado:** [CI LaPlacita 41508431779](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431779): success (misma punta); [Deploy Dokploy (laboratorio de la U) 41508431488](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431488): success (misma punta); [CI LaPlacita 41507908812](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41507908812): success (otra revisión o PR); [Deploy Dokploy (laboratorio de la U) 41503869984](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41503869984): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/d2fd2cd7ea984997bcf6e6775fa797fe0315974c/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_LaPlacita/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_LaPlacita/pulls) · [Antecedentes](seguimiento-s12-2026-11-03.md#laplacita).

<a id="lostvault"></a>

## LostVault

Rama **main**, [2b21f071cf0ff4cffa414fb1e964d719084ec04c](https://github.com/ISCOUTB/AS_202620_LostVault/commit/2b21f071cf0ff4cffa414fb1e964d719084ec04c), fecha del commit 2026-11-03T16:59:04Z (UTC). Observación: 2026-11-04T13:02:00Z.

PR #25 integrada en main añade inicio de sesión JWT temporal de usuario único configurado, alta de objetos y borrado permitido solo a quien los reportó, con validación 422 y puerto configurable. El contrato OpenAPI se actualiza en la punta posterior. El almacenamiento sigue en memoria y DATABASE_URL se declara pero aún no se usa; no es autenticación multiusuario ni persistencia productiva. Tres workflows de la punta aprueban; el log Backend checks acredita 27 pruebas de API y 18 de mensajería. README raíz sigue sin URL pública concreta del proyecto; el panel de administración no equivale a frontend/API publicado. No se acredita despliegue ni aceptación funcional nueva.

**Próximos pasos:**
- Documentar en README URL institucional exacta y distinguir frontend/API; comprobar el recorrido de login, creación, reclamación y borrado en el despliegue.
- Sustituir usuario único temporal y almacenamiento en memoria por autenticación y persistencia apropiadas, con pruebas y recuperación verificables.
- Reconciliar instrucciones de api/README.md que aún remiten a api/.env.example, eliminado por la PR25.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Ausente. README raíz sin URL pública concreta. Panel de administración y dominio de ejemplo del contrato no identifican frontend/API del proyecto.

**PR consultadas:** [#21](https://github.com/ISCOUTB/AS_202620_LostVault/pull/21): abierta; [#25](https://github.com/ISCOUTB/AS_202620_LostVault/pull/25): fusionada 2026-11-03T16:39:55Z; [#24](https://github.com/ISCOUTB/AS_202620_LostVault/pull/24): fusionada 2026-11-02T03:43:13Z; [#23](https://github.com/ISCOUTB/AS_202620_LostVault/pull/23): fusionada 2026-11-02T03:19:11Z

**CI consultado:** [Backend checks 41679698418](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41679698418): success (misma punta); [Build 41679698393](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41679698393): success (misma punta); [Flutter checks 41679698370](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41679698370): success (misma punta); [Flutter checks 41676511218](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41676511218): success (otra revisión o PR); [Build 41676511209](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41676511209): success (otra revisión o PR); [Backend checks 41676511119](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41676511119): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LostVault/blob/2b21f071cf0ff4cffa414fb1e964d719084ec04c/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_LostVault/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_LostVault/pulls) · [25](https://github.com/ISCOUTB/AS_202620_LostVault/pull/25) · [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/2b21f071cf0ff4cffa414fb1e964d719084ec04c/api/README.md) · [lostvault-api.yaml](https://github.com/ISCOUTB/AS_202620_LostVault/blob/2b21f071cf0ff4cffa414fb1e964d719084ec04c/docs/contracts/lostvault-api.yaml) · [126069776756](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41679698418/job/126069776756) · [Antecedentes](seguimiento-s12-2026-11-03.md#lostvault).

<a id="mapsutb"></a>

## mapsutb

Rama **master**, [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), fecha del commit 2026-10-25T14:04:14Z (UTC). Observación: 2026-11-04T13:02:00Z.

Revalidación del 4/nov frente al 3/nov: misma punta principal, README, issues y PR; no se identifica avance sustantivo nuevo. Se conserva la retroalimentación anterior sin trasladar cambios posteriores a las semanas cerradas. Se renuevan sondas y sincronización Sonar programadas con éxito; son actividad rutinaria, no una migración institucional ni una nueva aceptación funcional.

**Próximos pasos:**
- Mantener evidencia reproducible de recarga/reintento del grafo y distinguir sonda de disponibilidad de aceptación funcional.
- Publicar frontend bajo iscoutb.dev y actualizar README; no confundir mapsutb con ElMapita.

**Issues:** 0 abiertas / 54 cerradas; 0 abiertas sin asignar. Motivos: 54 completed.

**README:** Externo. Frontend Firebase externo; README no publica API institucional separada.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z

**CI consultado:** [Sonda de disponibilidad (métrica Escenario 6) 41829405984](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41829405984): success (misma punta); [Sincronizar hallazgos de Sonar a GitHub Issues 41827737186](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41827737186): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_mapsutb/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_mapsutb/pulls) · [Antecedentes](seguimiento-s12-2026-11-03.md#mapsutb).

<a id="pideutb"></a>

## PideUtb

Rama **master**, [d36136024c1d9c2e1fafbdc94ff38d9a31350c05](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/d36136024c1d9c2e1fafbdc94ff38d9a31350c05), fecha del commit 2026-11-02T23:14:22Z (UTC). Observación: 2026-11-04T13:02:00Z.

Master y README no cambian. Se abren PR #41 (documentación y ADR del costo de separar el esquema de datos, destino master) y #42 (corrección propuesta del avance concurrente de pedidos), apilada sobre la rama de #41, no directamente sobre master. La lectura del diff confirma que #42 añade estado esperado al UPDATE y respuesta 409 si otra operación ganó; no se ejecutó una reproducción propia ni se acredita incidente productivo. Su CI de rama aprueba: log Python3.11 registra 589 pruebas aprobadas y 3 omitidas, más 107 con PostgreSQL. El job Sonar vuelve a omitir el análisis por ausencia de SONAR_TOKEN: verde no acredita Quality Gate de esa revisión. Las dos PR siguen abiertas, de modo que cambios, conteo 592 y afirmaciones del equipo no son implementación fusionada ni despliegue. Se conserva la presentación y despliegues confirmados por el docente.

**Próximos pasos:**
- Revisar e integrar en orden PR41 y PR42; verificar el destino efectivo de la segunda antes de fusionar.
- Validar concurrencia en PostgreSQL y recorrido del mostrador sin retroceso de estado; documentar después la revisión realmente desplegada.
- Distinguir la consulta pública de Sonar reportada por el equipo del scanner omitido en este CI; acreditar Quality Gate sobre la revisión evaluada.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. README mantiene sitio y mostrador institucionales en pideutb.iscoutb.dev, API/salud/métricas en api-pideutb.iscoutb.dev. Frontend y API siguen en orígenes diferentes. No se verificó en vivo la publicación de las nuevas fotos/animaciones.

**PR consultadas:** [#42](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/42): abierta; [#41](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/41): abierta; [#40](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/40): fusionada 2026-11-02T23:14:22Z; [#39](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/39): fusionada 2026-11-02T19:01:29Z; [#38](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/38): fusionada 2026-10-30T06:16:11Z

**CI consultado:** [CI 41716632513](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41716632513): success (otra revisión o PR); [CI 41543855363](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/d36136024c1d9c2e1fafbdc94ff38d9a31350c05/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_PideUtb/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_PideUtb/pulls) · [41](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/41) · [42](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/42) · [repository.py](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/34e05e72f6d8ee788718d050518a063bf9262f98/backend/app/pedidos/repository.py) · [126197946185](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41716550853/job/126197946185) · [126197945753](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41716550853/job/126197945753) · [Antecedentes](seguimiento-s12-2026-11-03.md#pideutb).

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [d5b8b500e309e5997a6063f20b6c7da6682ef785](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/d5b8b500e309e5997a6063f20b6c7da6682ef785), fecha del commit 2026-11-03T10:35:17Z (UTC). Observación: 2026-11-04T13:02:00Z.

Revalidación del 4/nov frente al 3/nov: misma punta principal, README, issues y PR; no se identifica avance sustantivo nuevo. Se conserva la retroalimentación anterior sin trasladar cambios posteriores a las semanas cerradas. Conserva el incremento de universidades, favoritos y mensajería ya informado, así como CI sobre endpoint público y sus límites de aceptación manual, backup/restauración y rollback productivo.

**Próximos pasos:**
- Completar evidencia operativa pospromoción: healthy e ID de db, Image ID/configuración efectiva y montajes de api y db. El health público pasó en S10, pero no acredita esos datos internos.
- Acreditar copia externa independiente y restauración verificable de MySQL y fotografías; conservar abierto T13-10. Un dump dentro del contenedor o persistencia tras recreación en CI no equivalen a recuperación independiente.
- Documentar rollback productivo solo si se realiza de forma autorizada y con recuperación segura: actualmente se acredita ensayo sintético, no ejecución productiva.
- Aportar evidencia accesible y redactada de un anuncio nuevo con universidad declarada no nula y, para aceptación UI, persistencia de Favoritos tras nuevo login. No convertir afiliación declarada en identidad verificada.
- Conservar trazabilidad y distinguir SHA de orquestación HEAD del SHA productivo; mantener checks verdes y no recalificar ni cerrar semanas por estos incrementos posteriores a S13.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. README vigente declara Flutter Web institucional /app/ y API, y promoción del Incremento2 por digest. S10 en CI acredita endpoint público y revisión 46ede525; aceptación funcional manual reportada separadamente. Pages/Azure conservados como historia, sin prueba viva propia nueva.

**PR consultadas:** [#76](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/76): abierta (borrador); [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60): abierta; [#1](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/1): abierta; [#91](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/91): fusionada 2026-11-03T10:35:18Z; [#90](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/90): fusionada 2026-11-03T10:02:06Z; [#89](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/89): fusionada 2026-11-03T10:06:40Z

**CI consultado:** [S10 contrato del cliente en despliegue publico 41620519911](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519911): success (misma punta); [Compose y persistencia del MVP 41620519792](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519792): success (misma punta); [Flujo real Web y Android 41620519767](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519767): success (misma punta); [Validación Flutter MVP 41620519719](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519719): success (misma punta); [Pruebas del backend 41620519703](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519703): success (misma punta); [Pruebas del backend 41618964919](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41618964919): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/d5b8b500e309e5997a6063f20b6c7da6682ef785/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pulls) · [Antecedentes](seguimiento-s12-2026-11-03.md#proyecto_campusmarket).

<a id="recobra"></a>

## Recobra

Rama **master**, [0dda9abd2c76ef9b10724221225c0ed228197c39](https://github.com/ISCOUTB/AS_202620_Recobra/commit/0dda9abd2c76ef9b10724221225c0ed228197c39), fecha del commit 2026-10-29T02:32:33Z (UTC). Observación: 2026-11-04T13:02:00Z.

Revalidación del 4/nov frente al 3/nov: misma punta principal, README, issues y PR; no se identifica avance sustantivo nuevo. Se conserva la retroalimentación anterior sin trasladar cambios posteriores a las semanas cerradas. Se preserva la presentación confirmada por el docente; las diez propuestas de dependencias continúan abiertas, separadas del CI aprobado de master.

**Próximos pasos:**
- Acreditar acciones operativas de protección/rotación y respaldo programado sin publicar credenciales ni datos personales.
- Revisar y probar dependencias, mantener diferenciados avisos aceptados/mitigados y respetar vencimiento documentado.
- Aportar aceptación funcional en despliegue de límites, origen, cabeceras y avisos, separada del CI.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README distingue vitrina, Flutter Web y API del mismo host institucional. Presentación docente preservada; sin nueva auditoría funcional.

**PR consultadas:** [#10](https://github.com/ISCOUTB/AS_202620_Recobra/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_Recobra/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_Recobra/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_Recobra/pull/7): abierta; [#6](https://github.com/ISCOUTB/AS_202620_Recobra/pull/6): abierta; [#5](https://github.com/ISCOUTB/AS_202620_Recobra/pull/5): abierta; [#4](https://github.com/ISCOUTB/AS_202620_Recobra/pull/4): abierta; [#3](https://github.com/ISCOUTB/AS_202620_Recobra/pull/3): abierta; [#2](https://github.com/ISCOUTB/AS_202620_Recobra/pull/2): abierta; [#1](https://github.com/ISCOUTB/AS_202620_Recobra/pull/1): abierta

**CI consultado:** [ci 40806972927](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927): success (misma punta); [ci 40806929507](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806929507): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Recobra/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Recobra/pulls) · [Antecedentes](seguimiento-s12-2026-11-03.md#recobra).

<a id="routb"></a>

## ROUTB

Rama **master**, [6ad56f4f94be5e2af59664e24fe1be39058d8ecf](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/6ad56f4f94be5e2af59664e24fe1be39058d8ecf), fecha del commit 2026-11-03T23:13:56Z (UTC). Observación: 2026-11-04T13:02:00Z.

PR #70/#71 integradas en master después del cierre S13: ajustes de Dependabot y aislamiento de pruebas con advisory lock PostgreSQL, coordenadas aisladas y OSRM simulado. El test anterior de 50 respuestas se reduce a una respuesta contractual por caso: no acredita rendimiento con 50 solicitudes. CI de la punta aprueba 108 pruebas y 2 de contrato, auditoría y construcción de imagen; Sonar sigue siendo un echo de reserva, sin scanner/Quality Gate real. Las 13 PR de dependencias antes abiertas figuran cerradas sin merge. PR #72 de rediseño visual se fusionó únicamente en Changes, no en master: no debe atribuirse a la versión principal ni al sitio. README mantiene routb.iscoutb.dev como API, sin nuevo frontend institucional acreditado. Se conserva avance confirmado por el docente, sin reabrir S13.

**Próximos pasos:**
- Integrar o validar por separado el rediseño que permanece en Changes y documentar qué revisión se despliega.
- Restablecer medición reproducible de rendimiento si se pretende mantener la afirmación de 50 solicitudes; la prueba contractual aislada no la sustituye.
- Activar y acreditar análisis Sonar real y comprobar recorrido funcional sobre despliegue institucional, separándolo de build de imagen y purga programada.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend institucional documentado; no se atribuye URL web de frontend al backend. Avance entregado según docente.

**PR consultadas:** [#72](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/72): fusionada 2026-11-04T02:06:59Z; [#71](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/71): fusionada 2026-11-03T23:13:56Z; [#70](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/70): fusionada 2026-11-03T22:32:19Z

**CI consultado:** [Purga periódica de datos de ubicación 41797451769](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41797451769): success (misma punta); [CI ROUTB 41758602129](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41758602129): success (otra revisión o PR); [CI ROUTB 41737498880](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41737498880): success (misma punta); [Purga periódica de datos de ubicación 41601350180](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41601350180): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/6ad56f4f94be5e2af59664e24fe1be39058d8ecf/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ROUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ROUTB/pulls) · [70](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/70) · [71](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/71) · [72](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/72) · [test_matching_suggestions.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/6ad56f4f94be5e2af59664e24fe1be39058d8ecf/backend/tests/test_matching_suggestions.py) · [126270347828](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41737498880/job/126270347828) · [126270953761](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41737498880/job/126270953761) · [Antecedentes](seguimiento-s12-2026-11-03.md#routb).

<a id="shareu"></a>

## ShareU

Rama **master**, [20aeb0b77409ca8d98341e9a94fef73b31ad7073](https://github.com/ISCOUTB/AS_202620_ShareU/commit/20aeb0b77409ca8d98341e9a94fef73b31ad7073), fecha del commit 2026-11-04T00:20:52Z (UTC). Observación: 2026-11-04T13:02:00Z.

Desde el 3/nov se incorpora el sitio extraído en shareuwensite-main (archivos HTML/JS y configuración Firebase) y configuración Docker/Dokploy. Dockploy/compose.lab.yml prevé shareu.iscoutb.dev para web y api-shareu.iscoutb.dev para API, pero apunta a deploy/Dockerfile.api y ../../deploy/Dockerfile.web: el árbol de esa revisión solo contiene los Dockerfiles en Dockploy/. Es una discrepancia de rutas comprobada por lectura, no un despliegue fallido reproducido. Además el servicio web construye app/frontend (Next.js), no automáticamente el sitio HTML recién incorporado. README raíz conserva placeholders Vercel/Render, por lo que no documenta aún URL pública concreta. Workflow de la punta termina failure sin jobs devueltos; no permite atribuir la causa a Sonar ni acreditar publicación. Se mantienen 10 issues abiertas/10 cerradas y PR22/23 abiertas. En comprobación independiente de navegador del 4/nov 13:01:39–13:02:12 UTC, las raíces https://shareu.iscoutb.dev y https://api-shareu.iscoutb.dev mostraron «404 page not found». Es contenido visible, sin captura del código HTTP ni del hash servido; la raíz de la API no sustituye su endpoint de salud.

**Próximos pasos:**
- Unificar rutas reales de Dockerfiles y compose y precisar qué frontend se pretende publicar; validar construcción en el flujo del equipo.
- Documentar en README las URLs institucionales exactas una vez configuradas, distinguiendo API/frontend y dominios previstos de servicio verificado.
- Recuperar diagnóstico del workflow fallido sin jobs y registrar revisión desplegada, salud y recorrido funcional; no sustituirlo por una mera configuración o por CI omitido.

**Issues:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: 10 completed.

**README:** Ausente. README raíz conserva <URL Vercel>/<URL Render>, no URLs concretas. Dockploy/compose.lab.yml prevé https://shareu.iscoutb.dev (frontend) y https://api-shareu.iscoutb.dev (API); no constan en README ni se verificó funcionamiento. Comprobación viva limitada 4/nov13:01:39–13:02:12UTC: ambas raíces mostraron «404 page not found», sin código HTTP ni hash servido; no se probó /health.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z

**CI consultado:** [.github/workflows/tests.yml 41746144074](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/41746144074): failure (misma punta); [.github/workflows/tests.yml 41694681482](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/41694681482): failure (otra revisión o PR); [Tests 36479388452](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479388452): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ShareU/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ShareU/pulls) · [a019060c6eac1902a339942f31504f7b03b4f584](https://github.com/ISCOUTB/AS_202620_ShareU/commit/a019060c6eac1902a339942f31504f7b03b4f584) · [compose.lab.yml](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/Dockploy/compose.lab.yml) · [Dockerfile.api](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/Dockploy/Dockerfile.api) · [41746144074](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/41746144074) · [Antecedentes](seguimiento-s12-2026-11-03.md#shareu).

<a id="sistema-de-calificacion-automatica"></a>

## Calificación automática

Rama **master**, [f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc), fecha del commit 2026-11-02T01:05:36Z (UTC). Observación: 2026-11-04T13:03:00Z.

Sin cambios sustantivos frente al 3/nov: misma punta master f4548a9, README institucional, cero issues y una PR cerrada. Se revalida el mismo CI 41370619522 exitoso; no es una publicación nueva ni acredita la revisión servida hoy. Se conservan como antecedentes las pruebas API→worker del 30/oct, sin repetirlas como comprobación actual. Persisten autenticación/autorización, concurrencia, recuperación y trazabilidad del flujo completo.

**Próximos pasos:**
- Vincular revision.txt y un recorrido frontend→API→worker a la revisión efectivamente servida; la evidencia incorporada describe una revisión del 30/oct.
- Resolver autenticación y autorización antes de cargar datos reales; conservar los límites declarados del presupuesto por proceso y validar concurrencia y recuperación.
- Acreditar respaldo/restauración y EC-07 con el lote objetivo en el entorno servido; no confundir ingesta/worker con calificación OMR integral.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin merge

**CI consultado:** [CI 41370619522](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41370619522): success (misma punta); [CI 41338415453](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41338415453): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pulls) · [Antecedentes](seguimiento-s12-2026-11-03.md#sistema-de-calificacion-automatica).

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [44e1cc001e60f70a9d156506d81921a743836517](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/44e1cc001e60f70a9d156506d81921a743836517), fecha del commit 2026-11-01T18:28:43Z (UTC). Observación: 2026-11-04T13:03:00Z.

Sin cambios sustantivos frente al 3/nov: misma punta main 44e1cc0, README, siete issues y diez PR cerradas. El último CI sigue fallido y CD omitido en los mismos runs del 1/nov; el antecedente de 340 pruebas aprobadas y Quality Gate en ERROR no es una ejecución nueva. La API institucional está documentada, sin frontend web separado acreditado. Se conserva la confirmación docente de que TAIA presentó y funciona, sin añadir una nueva aceptación funcional.

**Próximos pasos:**
- Resolver los hallazgos de seguridad de Sonar y obtener Quality Gate OK de la revisión corregida; 340 pruebas exitosas no significan CI completo verde.
- Validar sesiones, renovación/revocación y consentimiento en la revisión servida, incluida migración de cuentas existentes; no seguir marcando T-02/T-08 como ausentes en código.
- Actualizar README y ADR-0011 para reflejar cliente, webhook, métricas JWT, respaldo y alertas reales; mantener límites de alertas en memoria y ausencia de notificación externa.
- Añadir pruebas/análisis Flutter al pipeline y recorridos integrados en dispositivo; la verificación Dart/OSV no ejecuta Flutter.

**Issues:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: 4 completed.

**README:** Institucional. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#17](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/17): fusionada 2026-10-30T22:18:28Z; [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z

**CI consultado:** [CD 41337016910](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41337016910): skipped (misma punta); [CI 41336869271](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336869271): failure (misma punta); [CI 41336725295](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336725295): failure (otra revisión o PR); [CD 41322405688](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41322405688): skipped (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/44e1cc001e60f70a9d156506d81921a743836517/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pulls) · [Antecedentes](seguimiento-s12-2026-11-03.md#taia_-task-artificial-intelligence-assistant).

<a id="tienda-virtual-utb"></a>

## Tienda virtual UTB

Rama **main**, [172a41f45b0268b5c8e778bcb0cf761550431e74](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/172a41f45b0268b5c8e778bcb0cf761550431e74), fecha del commit 2026-11-03T14:15:19Z (UTC). Observación: 2026-11-04T13:03:00Z.

El commit 172a41f modifica únicamente docs/seguridad-amenazas-privacidad.md: retira la tabla de ocho brechas entre promesas de privacidad y código, y conserva el apartado de derechos e incidentes. No contiene cambios de implementación que acrediten subsanar consentimiento, supresión, rectificación o retención; eliminar la tabla no cierra esos pendientes. El nuevo run 41651885651 pasa frontend y backend, pero el job Sonar figura success con checkout, cobertura y análisis skipped, por lo que no demuestra un nuevo análisis ni Quality Gate. README mantiene frontend sslip.io externo y no documenta dominio institucional. Cero issues y trece PR fusionadas permanecen sin cambios.

**Próximos pasos:**
- Conservar trazabilidad de las brechas de privacidad y acreditar cada corrección en código y pruebas; la eliminación de la tabla no sustituye la solución.
- Restablecer análisis Sonar efectivo y auditoría SCA reproducible bloqueante; separar resultado del job de pasos realmente ejecutados.
- Documentar URL institucional en README y verificar respaldo/restauración y recorrido funcional de pedidos.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#13](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/13): fusionada 2026-11-02T00:19:42Z; [#12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/12): fusionada 2026-10-25T02:58:28Z; [#11](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/11): fusionada 2026-10-24T20:15:26Z

**CI consultado:** [Pruebas 41651885651](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/41651885651): success (misma punta); [Pruebas 41366553356](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/41366553356): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/172a41f45b0268b5c8e778bcb0cf761550431e74/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pulls) · [172a41f45b0268b5c8e778bcb0cf761550431e74](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/172a41f45b0268b5c8e778bcb0cf761550431e74) · [41651885651](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/41651885651) · [Antecedentes](seguimiento-s12-2026-11-03.md#tienda-virtual-utb).

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [c0ac4594261350b4d7184a3536d6150dbdab2fc5](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/c0ac4594261350b4d7184a3536d6150dbdab2fc5), fecha del commit 2026-11-04T06:28:10Z (UTC). Observación: 2026-11-04T13:03:00Z.

Avance sustantivo hasta c0ac459: dependencias actualizadas (Starlette 1.3.1 y PyJWT 2.15.1), retiradas las exclusiones y continue-on-error de pip-audit, aislamiento de tests sin fallback a DATABASE_URL y notificador real Firebase Admin/SMTP en código. El run 41785768543 pasa 79 pruebas, incluida concurrencia PostgreSQL con una reserva aceptada y otra rechazada, y pip-audit informa cero vulnerabilidades conocidas. Sin embargo, el análisis Sonar falla por «Not authorized or project not found»: es un bloqueo de acceso/configuración antes de obtener Quality Gate; deploy de esa punta queda skipped. El run anterior 41784349055 sí registra checkout d844ad6, migraciones, reinicio y /salud con database connected tras un reintento por 502, por lo que el 502 previo no se mantiene como caída vigente. Una lectura independiente actual también observa salud OK, sin hash servido ni validación funcional del flujo completo. README añade API nip.io externa, no iscoutb.dev. La entrega push al dispositivo y operación permanente del worker aún requieren evidencia específica.

**Próximos pasos:**
- Verificar correspondencia y permisos del token/proyecto/organización Sonar, actualizar la acción obsoleta y obtener análisis y Quality Gate reales antes de desplegar la punta actual.
- Publicar URL de API bajo iscoutb.dev en README y diferenciarla de la app Android.
- Demostrar worker persistente, envío FCM/SMTP real, reintento e idempotencia en dispositivo; el código y los tests no acreditan entrega de mensajes en producción.
- Vincular revisión servida con el commit y completar recorrido funcional, más allá del endpoint de salud.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Externo. README ahora documenta API nip.io y /salud; pasa de Ausente a Externo. No es subdominio iscoutb.dev ni frontend web. Comprobación independiente de navegador del 4/nov 13:01:39–13:02:12 UTC mostró status ok y database connected; no se capturó código HTTP ni hash servido, y no equivale a validar la app completa.

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/8): fusionada 2026-11-03T00:37:47Z; [#7](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/7): fusionada 2026-11-03T00:25:29Z; [#6](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/6): fusionada 2026-11-03T00:13:54Z

**CI consultado:** [UTB Tracker CI 41785768543](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41785768543): failure (misma punta); [UTB Tracker CI 41784349055](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41784349055): success (otra revisión o PR); [Release APK 41555375916](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41555375916): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/c0ac4594261350b4d7184a3536d6150dbdab2fc5/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pulls) · [41785768543](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41785768543) · [41784349055](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41784349055) · [ci.yml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/c0ac4594261350b4d7184a3536d6150dbdab2fc5/.github/workflows/ci.yml) · [conftest.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/c0ac4594261350b4d7184a3536d6150dbdab2fc5/tests/conftest.py) · [test_performance.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/c0ac4594261350b4d7184a3536d6150dbdab2fc5/tests/test_performance.py) · [worker.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/c0ac4594261350b4d7184a3536d6150dbdab2fc5/app/messaging/worker.py) · [sonar-project.properties](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/c0ac4594261350b4d7184a3536d6150dbdab2fc5/sonar-project.properties) · [Antecedentes](seguimiento-s12-2026-11-03.md#utb_tracker).

<a id="uniteam"></a>

## uniTeam

Rama **master**, [5e18bc227e0aae35a3f3d797a8405d108a789ef7](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/5e18bc227e0aae35a3f3d797a8405d108a789ef7), fecha del commit 2026-11-02T05:17:31Z (UTC). Observación: 2026-11-04T13:03:00Z.

Sin cambio de código, README, issue ni PR frente al 3/nov: master 5e18bc2 y diez PR abiertas. Cuatro nuevas sondas programadas repiten el fallo conocido; el run 41829009244 del 4/nov 12:24 UTC falla seis comprobaciones y sus logs confirman que apuntan a las antiguas URL Render, no a las DuckDNS documentadas. Esto no prueba caída actual de DuckDNS ni un despliegue nuevo. Se conserva como antecedente la auditoría con 48 entradas en cuatro paquetes pese al job verde; no hay evidencia nueva de remediación.

**Próximos pasos:**
- Hacer bloqueante la auditoría preservando el código de salida (pipefail o mecanismo equivalente) y resolver/justificar hallazgos Python con evidencia reproducible.
- Actualizar la sonda a las URL DuckDNS vigentes y repetir las seis comprobaciones antes de interpretar salud.
- Implementar y probar controles de seguridad que los ADR/modelo describen como pendientes; distinguir documentación, actualización de dependencias y mitigación efectiva.
- Publicar frontend y API institucionales; conservar caché como propuesta y taller SQLite separado.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#22](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/22): abierta; [#21](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/21): abierta; [#18](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/18): abierta; [#17](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/16): abierta; [#15](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/15): abierta; [#14](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/14): abierta; [#13](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/13): abierta; [#12](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/12): abierta; [#11](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/11): abierta; [#27](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/27): fusionada 2026-11-02T05:17:31Z; [#26](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/26): fusionada 2026-11-02T05:06:05Z; [#25](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/25): fusionada 2026-11-02T04:55:58Z

**CI consultado:** [Comprobación del despliegue 41829009244](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41829009244): failure (misma punta); [seguridad-dependencias 41393369597](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393369597): success (otra revisión o PR); [CI 41393369587](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393369587): success (otra revisión o PR); [CI 41393152995](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393152995): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/5e18bc227e0aae35a3f3d797a8405d108a789ef7/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_uniTeam/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_uniTeam/pulls) · [41829009244](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41829009244) · [Antecedentes](seguimiento-s12-2026-11-03.md#uniteam).

<a id="xald"></a>

## XALD

Rama **master**, [a79a6085acf3bca4f861473f99094c43899e2b35](https://github.com/ISCOUTB/AS_202620_XALD/commit/a79a6085acf3bca4f861473f99094c43899e2b35), fecha del commit 2026-11-02T02:03:07Z (UTC). Observación: 2026-11-04T13:03:00Z.

Sin cambios sustantivos frente al 3/nov: master a79a608, README externo Render, seis issues cerradas (cinco completed y una duplicate), y quince PR abiertas. La PR Dependabot #42 sigue abierta y su CI exitoso no acredita integración. Los runs recientes son los mismos ya revisados; no se observa publicación nueva de master. Persisten validación integrada en dispositivo, trazabilidad del hash servido y ejecución durable de cola/deduplicación.

**Próximos pasos:**
- Validar controles y sincronización en dispositivo con trazabilidad a la revisión servida; health 200 no sustituye la validación del deploy ni del flujo completo.
- Mantener pendientes ejecutor real de procesarPendientes y persistencia de cola/deduplicación hasta aportar evidencia; no inferirlos de la entrega de seguridad.
- Revisar y probar los 15 PR de dependencias antes de integrarlos; conservar análisis reproducible sobre lo que realmente se despliega.
- Publicar API institucional y conciliar experimental con master sin restaurar documentación obsoleta.

**Issues:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. Motivos: 5 completed; 1 duplicate.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#42](https://github.com/ISCOUTB/AS_202620_XALD/pull/42): abierta; [#41](https://github.com/ISCOUTB/AS_202620_XALD/pull/41): abierta; [#40](https://github.com/ISCOUTB/AS_202620_XALD/pull/40): abierta; [#39](https://github.com/ISCOUTB/AS_202620_XALD/pull/39): abierta; [#38](https://github.com/ISCOUTB/AS_202620_XALD/pull/38): abierta; [#37](https://github.com/ISCOUTB/AS_202620_XALD/pull/37): abierta; [#36](https://github.com/ISCOUTB/AS_202620_XALD/pull/36): abierta; [#35](https://github.com/ISCOUTB/AS_202620_XALD/pull/35): abierta; [#34](https://github.com/ISCOUTB/AS_202620_XALD/pull/34): abierta; [#33](https://github.com/ISCOUTB/AS_202620_XALD/pull/33): abierta; [#32](https://github.com/ISCOUTB/AS_202620_XALD/pull/32): abierta; [#31](https://github.com/ISCOUTB/AS_202620_XALD/pull/31): abierta; [#30](https://github.com/ISCOUTB/AS_202620_XALD/pull/30): abierta; [#29](https://github.com/ISCOUTB/AS_202620_XALD/pull/29): abierta; [#28](https://github.com/ISCOUTB/AS_202620_XALD/pull/28): abierta; [#27](https://github.com/ISCOUTB/AS_202620_XALD/pull/27): fusionada 2026-11-02T02:03:07Z; [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z

**CI consultado:** [Android CI 41544247152](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/41544247152): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_XALD/blob/a79a6085acf3bca4f861473f99094c43899e2b35/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_XALD/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_XALD/pulls) · [Antecedentes](seguimiento-s12-2026-11-03.md#xald).

<a id="verifacts"></a>

## Verifacts

Rama **master**, [559612b61ee4cea46cef6d00f857d2e5c2794f03](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/559612b61ee4cea46cef6d00f857d2e5c2794f03), fecha del commit 2026-10-28T05:41:24Z (UTC). Observación: 2026-11-04T13:03:00Z.

Sin cambios sustantivos frente al 3/nov: master 559612b, README, tres issues cerradas completed, cero PR y los mismos runs de pruebas/Sonar exitosos del 28/oct. No acreditan despliegue nuevo. README sigue documentando sslip.io por HTTP, con dominio institucional/TLS pendiente. Se mantienen las necesidades de SSRF, límites, timeout, protección del historial, retención/supresión y SCA reproducible.

**Próximos pasos:**
- Aportar pip-audit/npm audit fechados con revisión y versiones resueltas.
- Implementar y probar controles prioritarios; distinguir propuesta de operación.
- Completar subdominio institucional/TLS y recorrido navegador/persistencia con trazabilidad.

**Issues:** 0 abiertas / 3 cerradas; 0 abiertas sin asignar. Motivos: 3 completed.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** Sin PR en la consulta.

**CI consultado:** [Tests 40639475382](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382): success (misma punta); [SonarCloud 40639475319](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319): success (misma punta); [SonarCloud 40636370321](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40636370321): success (otra revisión o PR); [Tests 40636370228](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40636370228): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Verifacts/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Verifacts/pulls) · [Antecedentes](seguimiento-s12-2026-11-03.md#verifacts).


## Comprobación viva limitada

Observación independiente en navegador cloud: **2026-11-04T13:01:39Z/2026-11-04T13:02:12Z**. Se leyó el contenido visible sin iniciar sesión ni ejecutar operaciones. No se capturaron códigos HTTP; las cadenas de error se reproducen como contenido, no como códigos medidos.

- [https://dinamikutb.iscoutb.dev/](https://dinamikutb.iscoutb.dev/): `404 page not found`. Frontend no accesible en esta observación.
- [https://api.dinamikutb.iscoutb.dev/health](https://api.dinamikutb.iscoutb.dev/health): `upstream connect error or disconnect/reset before headers. reset reason: remote connection failure`. Health no obtenido desde este navegador.
- [https://shareu.iscoutb.dev/](https://shareu.iscoutb.dev/): `404 page not found`. Dominio configurado, no se acredita frontend.
- [https://api-shareu.iscoutb.dev/](https://api-shareu.iscoutb.dev/): `404 page not found`. Raíz configurada, no prueba ausencia de otros endpoints API.
- [https://129-80-171-141.nip.io/salud](https://129-80-171-141.nip.io/salud): `{"status":"ok","proyecto":"UTB Tracker","version":"1.0.0","database":"connected"}`. Respuesta salud y base de datos declarada conectada; sin acreditar hash servido ni flujo funcional.

Estos resultados no acreditan una revisión servida específica ni aceptación funcional integral; la raíz de una API no sustituye sus endpoints de salud o negocio.
