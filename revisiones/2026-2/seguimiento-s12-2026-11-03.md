# Seguimiento de los 23 proyectos · 3 de noviembre de 2026

Consulta del **3 de noviembre de 2026**, con observaciones fechadas por proyecto (UTC). Seguimiento documental de los 23 proyectos del listado vigente, sin recalificar ni cerrar S12 automáticamente. Calificaciones, planillas, matrices y cortes históricos permanecen intactos.

**43 issues abiertas y 132 cerradas** (131 completed; 1 duplicate); 19 abiertas sin asignar. Conteo del corte, excluyendo PR.

README: **12 con algún endpoint institucional; 5 con enlaces externos; 6 sin URL pública concreta**. Un endpoint API no demuestra frontend publicado; ausencia de URL no demuestra ausencia de trabajo o despliegue.

Se conservan las confirmaciones del docente: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. No equivalen a pruebas funcionales nuevas de este corte.

Se consultaron README, historial, issues (excluyendo PR), propuestas y CI sin ejecutar código estudiantil. No se completaron pruebas de sitios en vivo: se intentaron abrir frontend y health documentados de LaPlacita, PideUtb y CampusMarket, pero la herramienta no pudo acceder a esas seis URLs y no entregó estado HTTP. Esto no demuestra caída ni funcionamiento. Código fusionado, CI, publicación y aceptación funcional son evidencias distintas. Los estados OPEN/CLOSED y motivos son de GitHub Issues; el conector no expone estados personalizados de Projects y no se obtuvieron columnas de tablero.

[Issues y motivos](seguimiento-issues-2026-11-03.md) · [README y despliegues](seguimiento-despliegues-2026-11-03.md) · [Antecedentes del 2/nov](seguimiento-s12-2026-11-02.md)

## Cambios respecto al 2/nov

- **DinamikUTB**: Desde el 2/nov incorpora dos commits, ambos limitados a frontend/lib/usuarios/welcome_screen.dart: modifica tiempos y arranque de la animación, centra un panel translúcido desplegable, ajusta dimensiones del título y cambia la insignia a PORTAL UNIVERSITARIO UTB. No cambia backend, README, issues ni PR. La nueva punta pasa 100 pruebas backend y 25 Flutter, con analyze sin incidencias; la repetición de las 100 pruebas para Sonar no se suma como casos distintos. Pip-audit vuelve a informar cero vulnerabilidades conocidas. El build web termina, pero la publicación frontend vuelve a fallar al hacer push a GHCR por permission_denied: write_package. Sonar envía el análisis, sin evidencia de Quality Gate vinculante en estos logs. Se mantienen las URLs institucionales web/API y los pendientes de seguridad e historial señalados el 2/nov; los dos cambios visuales no los resuelven. No se hizo prueba viva ni se acredita una revisión servida nueva.
- **GimnasioUTB**: Main y README no cambian desde el 2/nov, pero la PR #25 de Dependabot actualiza su punta a 55391e4: propone pg 8.23.1 y dependency-cruiser 18.7.0 mediante package.json y lock. Dos ejecuciones CI, push y pull_request, pasan sobre esa misma revisión; los logs de cada una repiten 19 pruebas de aplicación, 14 contractuales y nueve del prototipo, fitness functions, auditoría sin hallazgos y 129 firmas verificadas. Son ejecuciones de la PR, no cambios integrados ni pruebas de PostgreSQL real o Flutter. Continúan once PR abiertas y dieciséis issues abiertos con responsables, sin cambios de estado. README conserva la API institucional; no acredita una interfaz Flutter pública ni el token configurado en Dokploy.
- **LaPlacita**: PR #34–36 integradas desde el 2/nov: acceso del personal al panel y confirmación de pagos, pedido por tienda con varios productos y un código/PIN, cancelación lógica exclusiva de admin y separación de pedidos actuales/anteriores. README y contrato actualizados; ADR0032/0033 siguen propuestos, pendientes de validación grupal. Logs del HEAD: 161 pruebas pasan y 1 omitida, contrato 34/34, lint/build, auditoría/SBOM y scanner/gate Sonar aprobados. Deploy de backend registra Dokploy200 y health200, pero no prueba por sí solo el SHA servido ni el frontend manual. No hay evidencia nueva que cierre Azure legado y sesión STRIDE previstos para el 3/nov, rate-limit del 4/nov o ensayo real de rotación; son compromisos del equipo, no plazos docentes añadidos.
- **PideUtb**: PR #39/#40 integradas desde el 2/nov: migración009 y 25 fotografías para los 37 productos (12 conservan marcador), y animaciones limitadas a cambios reales con soporte de movimiento reducido. README corrige conteo a 587 pruebas. CI nuevo del HEAD comprobado en logs: 584 pasan/3 omitidas en cada Python3.11/3.12, 26 recorridos de navegador locales aprobados, contrato e imagen aprobados. Revalidación de límites: SonarCloud termina verde porque omite análisis al faltar SONAR_TOKEN; auditoría de producción no encuentra vulnerabilidades conocidas, pero auditoría del lock CI detecta certifi/pytest y continúa sin bloquear. No se acredita aplicación productiva de migración009 ni despliegue/aceptación nueva por estos resultados.
- **CampusMarket**: PR81–91 fusionados después del baseline. PR81 añade doce universidades de Cartagena, universidad opcional en registro/perfil y publicaciones, catálogo filtrable Toda Cartagena/Mi universidad. La afiliación es declarada, no identidad institucional verificada; universidad de publicación nueva se toma del perfil al crearla, sin reasignación retroactiva. PR82 promueve primera imagen universitaria por digest; PR83 corrige referencia productiva fija de S10; PR84 consolida trazabilidad. El histórico S10 8/9 se explica por referencia de revisión anterior, sin retirar criterios. PR85 incorpora Favoritos persistentes, mensajería comprador-vendedor y universidad visible. Mensajería HTTP/JSON con refresco manual; no implica tiempo real, push ni cifrado extremo a extremo. PR86 separa contrato desplegado/candidato y revisión de ejecución (elimina dependencia HEAD^1); PR87 promueve digest 11d92aa9b66f1a4c6b879a6e8cd62cc3c102a37c034a44cbde27442b73694fa7; PR88 versiona construcción y ensayos; PR89/91 documentan cierre limitado; PR90 actualiza referencia S10 a 46ede525. HEAD actual d5b8b50 tiene cinco workflows y siete jobs success, con logs leídos. No confundir con ocho checks del commit anterior 494c433 documentados en README. S10 del HEAD confirma 9/9 criterios, 58 solicitudes, 9 comprobaciones de salud, revisión 46ede525 y catálogo de 5 publicaciones antes/después con hash idéntico. Esto sí es evidencia de CI sobre endpoint público, no una inspección operativa viva realizada por esta auditoría. La aceptación manual del despliegue se declara en los documentos, sin capturas del operador incorporadas al repositorio; backup independiente, restauración y rollback productivos siguen sin acreditarse. No se repitió pip-audit en los cinco workflows del HEAD documental.
- **ROUTB**: Master y README no cambian desde el 2/nov. Nueva PR dependabot #69 (pytest9.0.3→9.2.0), abierta: son 13 PR abiertas, #57–69. Su CI aprueba 107 pruebas y 2 de contrato; build de imagen se omite en esa PR y Sonar sigue siendo un echo sin scanner. La falla de #67 continúa en su run ya conocido; no es falla nueva de master ni integración. Se renueva purga programada exitosa. Master conserva su CI de push aprobado, sin acreditar nueva migración/despliegue productivo; rama Changes observada en fe11e5b.
- **UTB Tracker**: Se fusionan PR #6, #7 y #8: seis commits llevan main de c76288e a fb7378d e incorporan validaciones de duración/fechas y autocancelación de préstamos de salones, manejo de errores Flutter y ajustes de seguridad/estilo. La suite del run 41554222766 vuelve a pasar 78 pruebas. El CI ahora figura success, pero no hay remediación de dependencias: el lock conserva Starlette 0.50.0 y PyJWT 2.12.1; pip-audit añade 20 identificadores de exclusión y continue-on-error: true. Su log informa una vulnerabilidad conocida restante (PYSEC-2026-176 en PyJWT), con 28 entradas ignoradas. El documento sigue proponiendo actualizar la mayoría de esos hallazgos y describiendo un gate bloqueante que ya no coincide con el workflow. Deploy SSH sí termina, registra checkout fb7378d, Alembic y reinicio systemd, sin health/smoke posterior. Release APK publica v1.0.3; compilar/publicar no acredita el recorrido en dispositivo. README raíz e issue abierta no cambian: sigue Ausente la URL pública y desactualizada la descripción SQLite/Alembic. Persiste el fallback de pruebas a DATABASE_URL seguido de drop_all; el notificador sigue siendo simulado.
- **XALD**: master (a79a608), README, experimental (7676801) y seis issues cerradas no cambian frente al 2/nov; se conservan cinco cierres completed y uno duplicate. Se abre PR Dependabot #42 para uvicorn 0.30.0→0.54.0, elevando los PR abiertos de catorce a quince; su ejecución Android CI 41544247152 termina success, sin que eso implique integración. La última ejecución de master sigue siendo 41375620434 del 2/nov, exitosa en Android, backend, auditoría y deploy-backend, ya revisada el día anterior. No hay publicación nueva de master acreditada en este corte. README mantiene la API Render y clasificación Externo. Persisten la validación integrada en dispositivo y trazabilidad de revisión servida, así como los pendientes de ejecución de cola y deduplicación; no se infieren resueltos por una actualización Dependabot sin fusionar.

Los demás proyectos se revalidaron. No se añaden secciones individuales repetidas por sondas rutinarias o evidencia sin cambios sustantivos. Este informe resume el delta y enlaza el corte anterior para conservar los antecedentes sin duplicarlos.

<a id="audioshare"></a>

## AudioShare

Rama **master**, [b2eb60d34a3ee41e2c632aa78e5a7021356461da](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/b2eb60d34a3ee41e2c632aa78e5a7021356461da), fecha del commit 2026-11-02T04:37:45Z (UTC). Observación: 2026-11-03T13:07:16.739870Z.

Sin novedades desde la revisión del 2/nov: master, README, issues, PR y ejecuciones se mantienen. Se releyeron los logs de la misma punta: CI y Flutter continúan verdes, con 36 pruebas Flutter aprobadas y una omitida; la instalación sigue reportando seis vulnerabilidades del árbol completo. La publicación de imagen ya observada el 2/nov no demuestra que Dokploy sirva esa revisión. El README mantiene audioshare.iscoutb.dev para frontend/API y su comprobación histórica del cliente legado. Permanecen dos issues abiertos sin responsable y la PR #8 abierta. No se repitió una prueba viva.

**Próximos pasos:**
- Redesplegar mediante el flujo Dokploy y demostrar frontend, API y sincronización entre dispositivos; publicar imagen Docker Hub no acredita la revisión servida.
- Implementar y probar controles de acceso por sala, cuotas de subida y límites de tasa; acompañar borrado/caducidad con una política y aviso que no prometan supresión ya operativa.
- Integrar auditoría de producción al CI y resolver o justificar con análisis completo los seis hallazgos de desarrollo; actualizar la acción Sonar que emite advertencia de seguridad.
- Documentar la prueba Flutter omitida y validar descarga, reintento y reingreso en dispositivos reales.

**Issues:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar. Motivos: 2 completed.

**README:** Institucional. README mantiene un mismo origen institucional para frontend y API. Conserva su comprobación histórica del 26/oct de cliente legado y /rooms 404; no se repitió prueba viva.

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/8): abierta; [#9](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/9): fusionada 2026-10-26T04:47:48Z; [#7](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/7): fusionada 2026-10-26T03:42:05Z; [#2](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/2): fusionada 2026-09-01T14:56:35Z

**CI consultado:** [CI 41389534440](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534440): success (misma punta); [Publicar imagen 41389534404](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534404): success (misma punta); [Flutter 41389534313](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534313): success (misma punta); [Flutter 41387713791](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713791): success (otra revisión o PR); [Publicar imagen 41387713751](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713751): success (otra revisión o PR); [CI 41387713744](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41387713744): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b2eb60d34a3ee41e2c632aa78e5a7021356461da/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_AudioShare/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_AudioShare/pulls) · [b2eb60d34a3ee41e2c632aa78e5a7021356461da](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/b2eb60d34a3ee41e2c632aa78e5a7021356461da) · [Antecedentes](seguimiento-s12-2026-11-02.md#audioshare).

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, [795beed409c880229dc3439e5882b3cb6aef3415](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/795beed409c880229dc3439e5882b3cb6aef3415), fecha del commit 2026-11-02T02:51:33Z (UTC). Observación: 2026-11-03T13:07:16.740110Z.

Sin novedades desde el 2/nov: master y README no cambian; se mantiene la ausencia de una URL pública concreta en README, sin inferir ausencia de trabajo. Los mismos dos workflows de backend y contrato continúan en failure; sus colecciones de jobs consultadas siguen vacías, por lo que no hay job identificable del cual recuperar logs ni evidencia nueva de pruebas ejecutadas. Se conserva como declaración del equipo el reescaneo limpio, no como auditoría CI verificada. No hay issues reales: los tres elementos del endpoint son PR, con #1 abierta y #2/#3 integradas históricamente.

**Próximos pasos:**
- Restablecer ambos workflows y aportar pruebas/backend, contrato y escaneo reproducible posteriores a las actualizaciones; no dar por corregido el CI por cambios en los tests.
- Priorizar hash de contraseñas y fallo de arranque sin JWT_SECRET; la autenticación de upload no resuelve límites de tamaño, SVG ni validación de contenido.
- Corregir idempotencia por autor/operación, exposición de matrícula y permisos por rol; conciliar privacidad que aún describe subida sin sesión con el cambio implementado.
- Completar decisiones y marcadores de privacidad/retención, y publicar URL exacta de frontend/API en README.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Ausente. README declara Dokploy y HTTPS, pero no ofrece un host público concreto; localhost y variables API_URL no cuentan como URL pública.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta; [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3): fusionada 2026-10-05T05:46:36Z; [#2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2): fusionada 2026-09-21T04:56:52Z

**CI consultado:** [.github/workflows/backend-tests.yml 41379945028](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379945028): failure (misma punta); [.github/workflows/contrato.yml 41379943754](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379943754): failure (misma punta); [.github/workflows/contrato.yml 41351122397](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41351122397): failure (otra revisión o PR); [.github/workflows/backend-tests.yml 41351121190](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41351121190): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/795beed409c880229dc3439e5882b3cb6aef3415/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pulls) · [795beed409c880229dc3439e5882b3cb6aef3415](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/795beed409c880229dc3439e5882b3cb6aef3415) · [Antecedentes](seguimiento-s12-2026-11-02.md#clubs_utb).

<a id="dinamikutb"></a>

## DinamikUTB

Rama **master**, [f9510698da53b8e48a115db462544898934d3e66](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/f9510698da53b8e48a115db462544898934d3e66), fecha del commit 2026-11-03T00:44:02Z (UTC). Observación: 2026-11-03T13:07:16.772454Z.

Desde el 2/nov incorpora dos commits, ambos limitados a frontend/lib/usuarios/welcome_screen.dart: modifica tiempos y arranque de la animación, centra un panel translúcido desplegable, ajusta dimensiones del título y cambia la insignia a PORTAL UNIVERSITARIO UTB. No cambia backend, README, issues ni PR. La nueva punta pasa 100 pruebas backend y 25 Flutter, con analyze sin incidencias; la repetición de las 100 pruebas para Sonar no se suma como casos distintos. Pip-audit vuelve a informar cero vulnerabilidades conocidas. El build web termina, pero la publicación frontend vuelve a fallar al hacer push a GHCR por permission_denied: write_package. Sonar envía el análisis, sin evidencia de Quality Gate vinculante en estos logs. Se mantienen las URLs institucionales web/API y los pendientes de seguridad e historial señalados el 2/nov; los dos cambios visuales no los resuelven. No se hizo prueba viva ni se acredita una revisión servida nueva.

**Próximos pasos:**
- Resolver el permiso GHCR write_package y repetir publicación de la misma punta; después documentar digest/commit efectivamente servido y recorrido navegador web/API institucional, sin confundir CI con despliegue.
- Validar la bienvenida en tamaños de pantalla reducidos, carga lenta/fallida de la imagen y preferencia de animaciones reducidas; añadir pruebas de esa interacción antes de afirmar aceptación visual.
- Eliminar la contraseña temporal compartida o impedir activación/login hasta completar establecimiento de clave de un solo uso. Añadir prueba negativa de activación previa al cambio y validar roles/datos académicos en actualizaciones.
- Conectar /auth/mi-perfil y /estudiantes/{codigo}/administrativo al servicio transaccional de historial, conservando actor, y probar esos endpoints; retirar el porcentaje de cumplimiento fijo 75 de estadísticas.
- Corregir S13/arc42: /password/recuperar responde 503 siempre (no SMTP operativo); requirements fija versiones sin hashes; /metrics exige token o queda 404 en producción. No atribuir CSP de la API a la protección del frontend sin evidenciar cabeceras reales del sitio.
- Añadir evidencia de Quality Gate con resultado específico de esta revisión; mantener separados scan enviado y gate aprobado. Verificar concurrencia sobre PostgreSQL y restauración de respaldos antes de considerar cerrada la deuda.
- Probar y definir tratamiento de JWT anteriores sin sig: el condicional actual solo comprueba la firma de contraseña cuando sig tiene valor; las sesiones legadas no quedan cubiertas por la nueva revocación.

**Issues:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. README conserva explícitos frontend https://dinamikutb.iscoutb.dev y API https://api.dinamikutb.iscoutb.dev. Los estados Activo son declaración del equipo, no prueba viva de esta auditoría.

**PR consultadas:** [#46](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/46): abierta; [#48](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/48): abierta; [#47](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/47): abierta; [#45](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/45): abierta; [#44](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/44): abierta; [#43](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/43): abierta; [#42](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/42): abierta; [#41](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/41): abierta; [#40](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/40): abierta; [#39](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/39): abierta; [#38](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/38): abierta; [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35): cerrada sin merge; [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37): fusionada 2026-10-23T03:04:11Z; [#36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36): fusionada 2026-10-23T01:01:46Z

**CI consultado:** [Publish frontend image 41554940766](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41554940766): failure (misma punta); [Auditoría de dependencias 41554940542](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41554940542): success (misma punta); [CI 41554940516](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41554940516): success (misma punta); [CI 41552403502](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41552403502): success (otra revisión o PR); [Publish frontend image 41552403430](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41552403430): failure (otra revisión o PR); [Auditoría de dependencias 41552403379](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41552403379): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/f9510698da53b8e48a115db462544898934d3e66/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_DinamikUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pulls) · [f9510698da53b8e48a115db462544898934d3e66](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/f9510698da53b8e48a115db462544898934d3e66) · [Antecedentes](seguimiento-s12-2026-11-02.md#dinamikutb).

<a id="drift"></a>

## Drift

Rama **master**, [be72a2f455ef2157ab6e36b9dd0d5a550e2086c5](https://github.com/ISCOUTB/AS_202620_Drift/commit/be72a2f455ef2157ab6e36b9dd0d5a550e2086c5), fecha del commit 2026-11-02T05:53:05Z (UTC). Observación: 2026-11-03T13:07:16.805417Z.

Sin novedades desde el 2/nov: master, README, veinte issues, PR y runs no cambian. La revisión de los mismos logs mantiene 207 pruebas backend y 176 casos contractuales aprobados, auditoría sin vulnerabilidades conocidas y Quality Gate PASSED. Continúan las advertencias de contrato: una operación responde solo 401/403 y dos quedan mayoritariamente limitadas por 429, sin ejecutar esa lógica. El mismo CD de Azure figura aprobado; no es evidencia nueva ni prueba funcional del dominio institucional. Permanecen cinco issues abiertos sin asignar y ninguna PR abierta. README conserva la URL institucional y alternativas Azure/Vercel.

**Próximos pasos:**
- Completar casos contractuales autenticados para sincronización y ajustar tasa/aislamiento para ejecutar la lógica de búsqueda y compatibilidad, manteniendo pruebas negativas de 401/429.
- Demostrar configuración del token administrativo/proxy y recorrido frontend/API institucional de la revisión desplegada; Azure CD no sustituye esa aceptación.
- Mantener requirements y lock sincronizados y probar las versiones efectivamente desplegadas; documentar excepciones de Dependabot cerradas sin merge.
- Conservar como pendientes la retención/redacción de logs y la discrepancia entre retención declarada de IP y limpieza efectiva del limitador.

**Issues:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. Se conservan frontend/API institucional bajo /api, API alternativa Azure y frontend alternativo Vercel; sin prueba funcional nueva.

**PR consultadas:** [#55](https://github.com/ISCOUTB/AS_202620_Drift/pull/55): cerrada sin merge; [#56](https://github.com/ISCOUTB/AS_202620_Drift/pull/56): fusionada 2026-11-02T05:53:06Z; [#52](https://github.com/ISCOUTB/AS_202620_Drift/pull/52): cerrada sin merge

**CI consultado:** [CI 41396593756](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41396593756): success (misma punta); [Build and deploy Python app to Azure Web App - drift-utb-202620 41396593677](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41396593677): success (misma punta); [CI 41388246330](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41388246330): success (otra revisión o PR); [Build and deploy Python app to Azure Web App - drift-utb-202620 41387265404](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41387265404): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Drift/blob/be72a2f455ef2157ab6e36b9dd0d5a550e2086c5/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Drift/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Drift/pulls) · [be72a2f455ef2157ab6e36b9dd0d5a550e2086c5](https://github.com/ISCOUTB/AS_202620_Drift/commit/be72a2f455ef2157ab6e36b9dd0d5a550e2086c5) · [Antecedentes](seguimiento-s12-2026-11-02.md#drift).

<a id="elmapita"></a>

## ElMapita

Rama **main**, [899bece9b4ddda9fb27381c966c0b720c93b0fee](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/899bece9b4ddda9fb27381c966c0b720c93b0fee), fecha del commit 2026-11-02T05:51:18Z (UTC). Observación: 2026-11-03T13:07:16.835826Z.

La punta main, README, issue #1 y las dieciséis PR abiertas no cambian desde el 2/nov. Solo aparece una nueva ejecución automática de Dependabot para Docker, aprobada; no equivale a cambio integrado ni a una nueva suite del proyecto. Se revalidaron logs del mismo CI: 78 pruebas backend y 30 Flutter pasan, pero E2E conserva un fallo tolerado, analyze 28 hallazgos y Sonar falla por autorización/proyecto con Quality Gate omitido. La auditoría de producción sigue reportando cuatro vulnerabilidades, dos altas y dos moderadas. README continúa sin URL pública concreta. Se preserva la confirmación docente histórica de que presentó y funciona; esta revisión documental no la invalida ni recalifica.

**Próximos pasos:**
- Completar migración de roles existentes a app_metadata y alinear el cliente Flutter, que aún lee userMetadata; verificar acceso administrativo después del cambio.
- Hacer vinculantes E2E y análisis relevante, resolver los 28 hallazgos y restaurar Sonar/Quality Gate; no presentar el verde agregado como todas las comprobaciones aprobadas.
- Revisar los cuatro hallazgos de producción y sus excepciones, sincronizar documentos que aún describen roles/redacción anteriores y probar las PR antes de integrar.
- Añadir URL exacta institucional en README, separando frontend/API, y evidencia fechada de la revisión actual sin invalidar la confirmación docente previa.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Ausente. README exacto no contiene URL pública concreta: la referencia tu-proyecto.supabase.co es un marcador. Se conserva aparte la confirmación docente de funcionamiento.

**PR consultadas:** [#15](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/15): abierta; [#18](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/18): abierta; [#17](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/16): abierta; [#14](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/14): abierta; [#13](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/13): abierta; [#12](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/12): abierta; [#10](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/9): abierta; [#11](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/11): abierta; [#8](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/8): abierta; [#6](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/6): abierta; [#7](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/7): abierta; [#4](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/4): abierta; [#3](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/3): abierta; [#5](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/5): abierta; [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z

**CI consultado:** [CI 41396450324](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41396450324): success (misma punta); [CI 41393881243](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41393881243): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/899bece9b4ddda9fb27381c966c0b720c93b0fee/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ElMapita/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ElMapita/pulls) · [899bece9b4ddda9fb27381c966c0b720c93b0fee](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/899bece9b4ddda9fb27381c966c0b720c93b0fee) · [Antecedentes](seguimiento-s12-2026-11-02.md#elmapita).

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), fecha del commit 2026-10-26T03:57:38Z (UTC). Observación: 2026-11-03T13:07:16.840350Z.

Sin novedades desde el 2/nov: master y README permanecen iguales; la PR #5 sigue abierta con la misma punta, y #4 continúa cerrada sin merge. Se releyó el fallo de CI de #5: la colección se interrumpe por ImportError, attempted relative import with no known parent package, en experimentos/mensajes_consistencia/test_simulador.py. No es una nueva ejecución ni una integración en master. El workflow de mensajería permanece aprobado por separado, sin convertir la suite general en verde. Issue #1 sin cambios. README default sigue sin una URL pública concreta; los hosts de ejemplo no cuentan como despliegue.

**Próximos pasos:**
- Corregir el empaquetado/import de test_simulador y reejecutar CI completo de la PR, incluidos contrato y build, antes de integrar.
- Conciliar las dos fallas de salud/métricas declaradas localmente con el resultado reproducible de CI; adjuntar auditoría fechada posterior al cambio de pytest.
- Mantener claramente separado lo propuesto en PR de lo integrado en master, y el correo simulado del envío real.
- Documentar URL institucional concreta y alcance PostgreSQL frente a rutas heredadas en memoria.

**Issues:** 1 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Ausente. README de master conserva host pendiente y marcadores [host-asignado]; no hay URL pública concreta. El README de la PR #5 tampoco modifica ese dato.

**PR consultadas:** [#5](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/5): abierta; [#4](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/4): cerrada sin merge; [#3](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/3): fusionada 2026-10-26T03:57:38Z; [#2](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/2): fusionada 2026-09-28T02:39:59Z

**CI consultado:** [CI 41389200867](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/41389200867): failure (otra revisión o PR); [Taller mensajes y consistencia 41389200795](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/41389200795): success (otra revisión o PR); [CI 40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): failure (misma punta); [Taller mensajes y consistencia 40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_EnAgenda/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_EnAgenda/pulls) · [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b) · [Antecedentes](seguimiento-s12-2026-11-02.md#enagenda).

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, [e0a458097202bb48e25c79d22614d759e3549ee0](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/e0a458097202bb48e25c79d22614d759e3549ee0), fecha del commit 2026-11-02T00:33:07Z (UTC). Observación: 2026-11-03T13:07:16.848574Z.

Main y README no cambian desde el 2/nov, pero la PR #25 de Dependabot actualiza su punta a 55391e4: propone pg 8.23.1 y dependency-cruiser 18.7.0 mediante package.json y lock. Dos ejecuciones CI, push y pull_request, pasan sobre esa misma revisión; los logs de cada una repiten 19 pruebas de aplicación, 14 contractuales y nueve del prototipo, fitness functions, auditoría sin hallazgos y 129 firmas verificadas. Son ejecuciones de la PR, no cambios integrados ni pruebas de PostgreSQL real o Flutter. Continúan once PR abiertas y dieciséis issues abiertos con responsables, sin cambios de estado. README conserva la API institucional; no acredita una interfaz Flutter pública ni el token configurado en Dokploy.

**Próximos pasos:**
- Revisar PR #25 con pg 8.23.1 y dependency-cruiser 18.7.0 y comprobar regresión PostgreSQL real antes de integrarla; CI verde de la rama no acredita main.
- Configurar/rotar el token de operador como secreto en Dokploy y demostrar lecturas, rechazo sin credencial y escritura autorizada sobre el despliegue actual; no compartir el secreto en evidencia.
- Ejecutar las pruebas Flutter añadidas e integración PostgreSQL con base aislada, además del recorrido de extremo a extremo.
- Mantener límites del token compartido (sin identidad individual), completar timeout del pool y control de tasa/proxy, y verificar retención de logs.
- Reducir dependencias Flutter no usadas y revisar las PR propuestas; no inferir durabilidad ni broker de producción a partir del prototipo.

**Issues:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README mantiene https://gimnasio-utb.iscoutb.dev como backend/API, no como interfaz Flutter pública.

**PR consultadas:** [#25](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/25): abierta; [#30](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/30): abierta; [#29](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/29): abierta; [#27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/27): abierta; [#28](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/28): abierta; [#26](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/26): abierta; [#24](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/24): abierta; [#23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/22): abierta; [#21](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/21): abierta; [#20](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/20): abierta; [#31](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/31): fusionada 2026-11-02T00:33:07Z; [#19](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/19): fusionada 2026-11-02T00:23:36Z; [#18](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/18): fusionada 2026-10-26T00:15:00Z

**CI consultado:** [CI 41541577567](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541577567): success (otra revisión o PR); [CI 41367755427](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41367755427): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/e0a458097202bb48e25c79d22614d759e3549ee0/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pulls) · [e0a458097202bb48e25c79d22614d759e3549ee0](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/e0a458097202bb48e25c79d22614d759e3549ee0) · [Antecedentes](seguimiento-s12-2026-11-02.md#gimnasioutb).

<a id="inventrack"></a>

## InvenTrack

Rama **main**, [190db13b6591c3e38da125700b2d791bbf8b25e3](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/190db13b6591c3e38da125700b2d791bbf8b25e3), fecha del commit 2026-11-02T04:04:45Z (UTC). Observación: 2026-11-03T13:07:16.861886Z.

Sin novedades desde el 2/nov: main, README, siete issues cerrados, cuatro PR abiertas y runs se mantienen. Los mismos jobs de la punta siguen aprobados, con pip-audit sin vulnerabilidades conocidas y Quality Gate PASSED; no se presentan como una ejecución nueva. README conserva la API institucional y alternativa Render, así como las limitaciones de la comprobación pública histórica: no acredita el despliegue de commits posteriores ni acceso autorizado de negocio. No se hizo prueba viva. Se mantienen la separación entre 503 preventivo y caída, y la deuda de identidad/roles, durabilidad y retención.

**Próximos pasos:**
- Acreditar el commit realmente servido después del redespliegue con /health y estados esperados, conservando separado el 503 preventivo de una caída; comprobar acceso interno autorizado sin revelar el token.
- Revisar las cuatro PR de dependencias, mantener hashes completos y ejecutar suite y auditoría antes de integrar.
- Conservar negocio deshabilitado hasta identidad/roles y auditoría de actor; el token interno no sustituye autorización de usuarios.
- Completar persistencia/recuperación durables y retención/redacción de logs; mantener explícitos los límites de locks, idempotencia, broker y DLQ en memoria.

**Issues:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: 7 completed.

**README:** Institucional. README conserva API institucional y alternativa Render, y mantiene explícito que la revisión actual requiere verificación pública posterior al redespliegue; no acredita frontend.

**PR consultadas:** [#11](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/11): abierta; [#10](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/8): abierta

**CI consultado:** [Run Tests 41386451056](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386451056): success (misma punta); [Run Tests 41386175523](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386175523): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/190db13b6591c3e38da125700b2d791bbf8b25e3/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_InvenTrack/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_InvenTrack/pulls) · [190db13b6591c3e38da125700b2d791bbf8b25e3](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/190db13b6591c3e38da125700b2d791bbf8b25e3) · [Antecedentes](seguimiento-s12-2026-11-02.md#inventrack).

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [d2fd2cd7ea984997bcf6e6775fa797fe0315974c](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/d2fd2cd7ea984997bcf6e6775fa797fe0315974c), fecha del commit 2026-11-02T19:16:38Z (UTC). Observación: 2026-11-03T13:04:01.027Z.

PR #34–36 integradas desde el 2/nov: acceso del personal al panel y confirmación de pagos, pedido por tienda con varios productos y un código/PIN, cancelación lógica exclusiva de admin y separación de pedidos actuales/anteriores. README y contrato actualizados; ADR0032/0033 siguen propuestos, pendientes de validación grupal. Logs del HEAD: 161 pruebas pasan y 1 omitida, contrato 34/34, lint/build, auditoría/SBOM y scanner/gate Sonar aprobados. Deploy de backend registra Dokploy200 y health200, pero no prueba por sí solo el SHA servido ni el frontend manual. No hay evidencia nueva que cierre Azure legado y sesión STRIDE previstos para el 3/nov, rate-limit del 4/nov o ensayo real de rotación; son compromisos del equipo, no plazos docentes añadidos.

**Próximos pasos:**
- Validar en equipo STRIDE y ADR0030–0033, conservando el estado propuesto donde corresponda; revisar #28/#30 antes de integrar.
- Acreditar retiro o mitigación de Azure legado y resultado de la sesión prevista para el 3/nov; aplicar y comprobar rate-limit previsto para el 4/nov y registrar ensayo real de rotación.
- Verificar con autorización que backend nuevo preceda al frontend manual, vincular SHA servido y probar agrupación multitienda, compatibilidad v1, cancelación por admin, aislamiento y conservación de pedidos. Un webhook y health200 no equivalen a aceptación integral.

**Issues:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. Motivos: 14 completed.

**README:** Institucional. README mantiene app/PWA y panel institucionales separados de la API. Azure no es URL vigente del README, pero S13 mantiene pendiente acreditar su apagado; la documentación de retiro no demuestra retiro operativo. Sin prueba viva nueva.

**PR consultadas:** [#27](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/27): abierta; [#16](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/16): abierta; [#26](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/26): abierta; [#17](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/17): abierta; [#25](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/25): abierta; [#30](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/30): abierta; [#28](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/28): abierta; [#23](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/23): abierta; [#21](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/21): abierta; [#20](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/20): abierta; [#36](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/36): fusionada 2026-11-02T19:16:39Z; [#35](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/35): fusionada 2026-11-02T18:47:20Z; [#34](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/34): fusionada 2026-11-02T18:18:08Z

**CI consultado:** [CI LaPlacita 41508431779](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431779): success (misma punta); [Deploy Dokploy (laboratorio de la U) 41508431488](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431488): success (misma punta); [CI LaPlacita 41507908812](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41507908812): success (otra revisión o PR); [Deploy Dokploy (laboratorio de la U) 41503869984](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41503869984): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/d2fd2cd7ea984997bcf6e6775fa797fe0315974c/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_LaPlacita/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_LaPlacita/pulls) · [d2fd2cd7ea984997bcf6e6775fa797fe0315974c](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/d2fd2cd7ea984997bcf6e6775fa797fe0315974c) · [41508431779](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431779) · [41508431488](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431488) · [41507908812](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41507908812) · [41503870095](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41503870095) · [41503869984](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41503869984) · [41503292075](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41503292075) · [41499268607](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41499268607) · [41499268543](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41499268543) · [125493643241](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431488/job/125493643241) · [125493644860](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431779/job/125493644860) · [125493645080](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431779/job/125493645080) · [125494233285](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431779/job/125494233285) · [125494233455](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431779/job/125494233455) · [125494474279](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41508431779/job/125494474279) · [34](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/34) · [35](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/35) · [36](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/36) · [Antecedentes](seguimiento-s12-2026-11-02.md#laplacita).

<a id="lostvault"></a>

## LostVault

Rama **main**, [58c5c9524e3d1dd51d970e36a38bab690e10470e](https://github.com/ISCOUTB/AS_202620_LostVault/commit/58c5c9524e3d1dd51d970e36a38bab690e10470e), fecha del commit 2026-11-02T03:43:13Z (UTC). Observación: 2026-11-03T13:04:01.027Z.

Revalidación del 3/nov frente al 2/nov: misma punta, README, issues, PR y resultados CI; se conserva el feedback previo sin presentar avances anteriores como nuevos. PR #23/#24 y tres workflows aprobados permanecen en el mismo estado ya registrado ayer. README continúa sin URL concreta de frontend/API; panel.iscoutb.dev es referencia de administración, no endpoint del proyecto.

**Próximos pasos:**
- Publicar en README URLs concretas y roles de frontend/API del despliegue institucional; no usar el panel de administración como URL de aplicación.
- Convertir el análisis manual de dependencias en auditoría reproducible de CI con versiones instaladas, decisiones de actualización y regresiones.
- Priorizar identidad real y persistencia de reclamaciones; verificar configuración, workers, acceso, retención y respaldos del entorno autorizado. No repetir carga contra el panel sin autorización.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Ausente. README sigue sin URL concreta de aplicación. Documento S13 cita panel.iscoutb.dev como panel/servidor de administración: no se convierte en endpoint funcional del proyecto ni acredita despliegue vivo.

**PR consultadas:** [#21](https://github.com/ISCOUTB/AS_202620_LostVault/pull/21): abierta; [#24](https://github.com/ISCOUTB/AS_202620_LostVault/pull/24): fusionada 2026-11-02T03:43:13Z; [#23](https://github.com/ISCOUTB/AS_202620_LostVault/pull/23): fusionada 2026-11-02T03:19:11Z; [#22](https://github.com/ISCOUTB/AS_202620_LostVault/pull/22): fusionada 2026-10-26T04:46:41Z

**CI consultado:** [Flutter checks 41384608380](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384608380): success (misma punta); [Backend checks 41384608353](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384608353): success (misma punta); [Build 41384608212](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384608212): success (misma punta); [Backend checks 41384596340](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384596340): success (otra revisión o PR); [Build 41384596238](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384596238): success (otra revisión o PR); [Flutter checks 41384596216](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384596216): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_LostVault/blob/58c5c9524e3d1dd51d970e36a38bab690e10470e/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_LostVault/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_LostVault/pulls) · [58c5c9524e3d1dd51d970e36a38bab690e10470e](https://github.com/ISCOUTB/AS_202620_LostVault/commit/58c5c9524e3d1dd51d970e36a38bab690e10470e) · [41384608380](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384608380) · [41384608353](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384608353) · [41384608212](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384608212) · [41384596340](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384596340) · [41384596238](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384596238) · [41384596216](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384596216) · [41384473380](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384473380) · [41384473271](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384473271) · [Antecedentes](seguimiento-s12-2026-11-02.md#lostvault).

<a id="mapsutb"></a>

## mapsutb

Rama **master**, [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), fecha del commit 2026-10-25T14:04:14Z (UTC). Observación: 2026-11-03T13:04:01.027Z.

Misma punta, README, 54 issues cerradas y dos PR integradas históricas. Solo se renuevan sonda de disponibilidad y sincronización Sonar programadas, exitosas; es actividad rutinaria, no avance funcional nuevo ni migración institucional. README mantiene frontend Firebase mapsutb.web.app.

**Próximos pasos:**
- Mantener evidencia reproducible de recarga/reintento del grafo y distinguir sonda de disponibilidad de aceptación funcional.
- Publicar frontend bajo iscoutb.dev y actualizar README; no confundir mapsutb con ElMapita.

**Issues:** 0 abiertas / 54 cerradas; 0 abiertas sin asignar. Motivos: 54 completed.

**README:** Externo. Frontend Firebase externo; README no publica API institucional separada.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z

**CI consultado:** [Sonda de disponibilidad (métrica Escenario 6) 41635909404](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41635909404): success (misma punta); [Sincronizar hallazgos de Sonar a GitHub Issues 41634211896](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41634211896): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_mapsutb/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_mapsutb/pulls) · [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833) · [41635909404](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41635909404) · [41634211896](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41634211896) · [41626929453](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41626929453) · [41618710728](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41618710728) · [41610553621](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41610553621) · [41603192765](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41603192765) · [41595915738](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41595915738) · [41590397023](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/41590397023) · [Antecedentes](seguimiento-s12-2026-11-02.md#mapsutb).

<a id="pideutb"></a>

## PideUtb

Rama **master**, [d36136024c1d9c2e1fafbdc94ff38d9a31350c05](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/d36136024c1d9c2e1fafbdc94ff38d9a31350c05), fecha del commit 2026-11-02T23:14:22Z (UTC). Observación: 2026-11-03T13:04:01.027Z.

PR #39/#40 integradas desde el 2/nov: migración009 y 25 fotografías para los 37 productos (12 conservan marcador), y animaciones limitadas a cambios reales con soporte de movimiento reducido. README corrige conteo a 587 pruebas. CI nuevo del HEAD comprobado en logs: 584 pasan/3 omitidas en cada Python3.11/3.12, 26 recorridos de navegador locales aprobados, contrato e imagen aprobados. Revalidación de límites: SonarCloud termina verde porque omite análisis al faltar SONAR_TOKEN; auditoría de producción no encuentra vulnerabilidades conocidas, pero auditoría del lock CI detecta certifi/pytest y continúa sin bloquear. No se acredita aplicación productiva de migración009 ni despliegue/aceptación nueva por estos resultados.

**Próximos pasos:**
- Antes de la demo prevista para el 3/nov, acreditar SHA servido y aplicación de migraciones008/009; verificar 25 fotos correctas, 12 marcadores y recorrido cliente–pasarela de pruebas–mostrador en el entorno objetivo.
- Configurar o acreditar análisis/gate Sonar real: el job verde actual omite el scanner. Revisar los hallazgos certifi/pytest del lock CI y su excepción no bloqueante sin confundirlos con dependencia productiva.
- Conservar pruebas de retorno, caducidad, limpieza y animación accesible; distinguir 584/3 por versión Python y 26 E2E locales de evidencia productiva. Verificar retiro o mitigación de todos los servicios legados.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. README mantiene sitio y mostrador institucionales en pideutb.iscoutb.dev, API/salud/métricas en api-pideutb.iscoutb.dev. Frontend y API siguen en orígenes diferentes. No se verificó en vivo la publicación de las nuevas fotos/animaciones.

**PR consultadas:** [#40](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/40): fusionada 2026-11-02T23:14:22Z; [#37](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/37): fusionada 2026-10-30T03:53:01Z; [#38](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/38): fusionada 2026-10-30T06:16:11Z

**CI consultado:** [CI 41543855363](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363): success (misma punta); [CI 41543254941](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543254941): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/d36136024c1d9c2e1fafbdc94ff38d9a31350c05/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_PideUtb/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_PideUtb/pulls) · [d36136024c1d9c2e1fafbdc94ff38d9a31350c05](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/d36136024c1d9c2e1fafbdc94ff38d9a31350c05) · [41543855363](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363) · [41543254941](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543254941) · [41543168478](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543168478) · [41506059470](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41506059470) · [41504937273](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41504937273) · [41504864755](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41504864755) · [41013098666](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41013098666) · [41012632402](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41012632402) · [125614416882](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363/job/125614416882) · [125614417241](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363/job/125614417241) · [125614417283](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363/job/125614417283) · [125614417325](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363/job/125614417325) · [125614417334](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363/job/125614417334) · [125614417365](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363/job/125614417365) · [125614417481](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41543855363/job/125614417481) · [39](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/39) · [40](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/40) · [009_fotos_de_la_carta.sql](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/d36136024c1d9c2e1fafbdc94ff38d9a31350c05/backend/migraciones/009_fotos_de_la_carta.sql) · [Antecedentes](seguimiento-s12-2026-11-02.md#pideutb).

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [d5b8b500e309e5997a6063f20b6c7da6682ef785](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/d5b8b500e309e5997a6063f20b6c7da6682ef785), fecha del commit 2026-11-03T10:35:17Z (UTC). Observación: 2026-11-03T13:04:01.027Z.

PR81–91 fusionados después del baseline. PR81 añade doce universidades de Cartagena, universidad opcional en registro/perfil y publicaciones, catálogo filtrable Toda Cartagena/Mi universidad. La afiliación es declarada, no identidad institucional verificada; universidad de publicación nueva se toma del perfil al crearla, sin reasignación retroactiva. PR82 promueve primera imagen universitaria por digest; PR83 corrige referencia productiva fija de S10; PR84 consolida trazabilidad. El histórico S10 8/9 se explica por referencia de revisión anterior, sin retirar criterios. PR85 incorpora Favoritos persistentes, mensajería comprador-vendedor y universidad visible. Mensajería HTTP/JSON con refresco manual; no implica tiempo real, push ni cifrado extremo a extremo. PR86 separa contrato desplegado/candidato y revisión de ejecución (elimina dependencia HEAD^1); PR87 promueve digest 11d92aa9b66f1a4c6b879a6e8cd62cc3c102a37c034a44cbde27442b73694fa7; PR88 versiona construcción y ensayos; PR89/91 documentan cierre limitado; PR90 actualiza referencia S10 a 46ede525. HEAD actual d5b8b50 tiene cinco workflows y siete jobs success, con logs leídos. No confundir con ocho checks del commit anterior 494c433 documentados en README. S10 del HEAD confirma 9/9 criterios, 58 solicitudes, 9 comprobaciones de salud, revisión 46ede525 y catálogo de 5 publicaciones antes/después con hash idéntico. Esto sí es evidencia de CI sobre endpoint público, no una inspección operativa viva realizada por esta auditoría. La aceptación manual del despliegue se declara en los documentos, sin capturas del operador incorporadas al repositorio; backup independiente, restauración y rollback productivos siguen sin acreditarse. No se repitió pip-audit en los cinco workflows del HEAD documental.

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

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/d5b8b500e309e5997a6063f20b6c7da6682ef785/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pulls) · [d5b8b500e309e5997a6063f20b6c7da6682ef785](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/d5b8b500e309e5997a6063f20b6c7da6682ef785) · [41620519911](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519911) · [41620519792](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519792) · [41620519767](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519767) · [41620519719](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519719) · [41620519703](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519703) · [41618964919](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41618964919) · [41618964912](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41618964912) · [41618964686](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41618964686) · [cierre-productivo-incremento2-2026-11-03.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/d5b8b500e309e5997a6063f20b6c7da6682ef785/docs/evidencias/cierre-productivo-incremento2-2026-11-03.md) · [cierre-universidades-cartagena-2026-11-02.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/d5b8b500e309e5997a6063f20b6c7da6682ef785/docs/evidencias/cierre-universidades-cartagena-2026-11-02.md) · [81](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/81) · [82](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/82) · [83](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/83) · [84](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/84) · [85](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/85) · [86](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/86) · [87](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/87) · [88](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/88) · [89](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/89) · [90](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/90) · [91](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/91) · [125864742981](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519719/job/125864742981) · [125864743407](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519792/job/125864743407) · [125864743173](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519703/job/125864743173) · [125864743791](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519911/job/125864743791) · [125864743483](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519767/job/125864743483) · [125864743897](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519767/job/125864743897) · [125864743915](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41620519767/job/125864743915) · [Antecedentes](seguimiento-s12-2026-11-02.md#proyecto_campusmarket).

<a id="recobra"></a>

## Recobra

Rama **master**, [0dda9abd2c76ef9b10724221225c0ed228197c39](https://github.com/ISCOUTB/AS_202620_Recobra/commit/0dda9abd2c76ef9b10724221225c0ed228197c39), fecha del commit 2026-10-29T02:32:33Z (UTC). Observación: 2026-11-03T13:04:01.027Z.

Revalidación del 3/nov frente al 2/nov: misma punta, README, issues, PR y resultados CI; se conserva el feedback previo sin presentar avances anteriores como nuevos. CI de master conserva éxito y las 10 PR de dependencias siguen abiertas; no confundir sus fallos de rama ya conocidos con un fallo nuevo del master. Se preserva presentación docente previamente acreditada.

**Próximos pasos:**
- Acreditar acciones operativas de protección/rotación y respaldo programado sin publicar credenciales ni datos personales.
- Revisar y probar dependencias, mantener diferenciados avisos aceptados/mitigados y respetar vencimiento documentado.
- Aportar aceptación funcional en despliegue de límites, origen, cabeceras y avisos, separada del CI.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README distingue vitrina, Flutter Web y API del mismo host institucional. Presentación docente preservada; sin nueva auditoría funcional.

**PR consultadas:** [#10](https://github.com/ISCOUTB/AS_202620_Recobra/pull/10): abierta; [#9](https://github.com/ISCOUTB/AS_202620_Recobra/pull/9): abierta; [#8](https://github.com/ISCOUTB/AS_202620_Recobra/pull/8): abierta; [#7](https://github.com/ISCOUTB/AS_202620_Recobra/pull/7): abierta; [#6](https://github.com/ISCOUTB/AS_202620_Recobra/pull/6): abierta; [#5](https://github.com/ISCOUTB/AS_202620_Recobra/pull/5): abierta; [#3](https://github.com/ISCOUTB/AS_202620_Recobra/pull/3): abierta; [#2](https://github.com/ISCOUTB/AS_202620_Recobra/pull/2): abierta; [#4](https://github.com/ISCOUTB/AS_202620_Recobra/pull/4): abierta; [#1](https://github.com/ISCOUTB/AS_202620_Recobra/pull/1): abierta

**CI consultado:** [ci 40806972927](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927): success (misma punta); [ci 40806929507](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806929507): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Recobra/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Recobra/pulls) · [0dda9abd2c76ef9b10724221225c0ed228197c39](https://github.com/ISCOUTB/AS_202620_Recobra/commit/0dda9abd2c76ef9b10724221225c0ed228197c39) · [40806972927](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927) · [40806929507](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806929507) · [40806601497](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806601497) · [40806323418](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806323418) · [40806123064](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806123064) · [40805651574](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40805651574) · [40804928538](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40804928538) · [40804901296](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40804901296) · [Antecedentes](seguimiento-s12-2026-11-02.md#recobra).

<a id="routb"></a>

## ROUTB

Rama **master**, [5f13a93fb2edf5977c582662537f2af32bd1a4d2](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/5f13a93fb2edf5977c582662537f2af32bd1a4d2), fecha del commit 2026-11-02T04:49:00Z (UTC). Observación: 2026-11-03T13:04:01.027Z.

Master y README no cambian desde el 2/nov. Nueva PR dependabot #69 (pytest9.0.3→9.2.0), abierta: son 13 PR abiertas, #57–69. Su CI aprueba 107 pruebas y 2 de contrato; build de imagen se omite en esa PR y Sonar sigue siendo un echo sin scanner. La falla de #67 continúa en su run ya conocido; no es falla nueva de master ni integración. Se renueva purga programada exitosa. Master conserva su CI de push aprobado, sin acreditar nueva migración/despliegue productivo; rama Changes observada en fe11e5b.

**Próximos pasos:**
- Revisar las 13 PR #57–69 por compatibilidad y riesgo antes de integrar; #67 sigue requiriendo resolver controlador psycopg/migración, y éxito de #69 no equivale a integración ni build de imagen en esa PR.
- Acreditar en entorno autorizado migración010, imagen/SHA realmente servido y aceptación funcional de autocompletado/privacidad; README referencia Changes para despliegue, distinta de master.
- Mantener alcance real de pip-audit y distinguir job Sonar echo de análisis/gate; conservar límites del prototipo de mensajería/cola en memoria y evidencia operativa de purga.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend institucional documentado; no se atribuye URL web de frontend al backend. Avance entregado según docente.

**PR consultadas:** [#69](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/69): abierta; [#68](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/68): abierta; [#67](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/67): abierta; [#66](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/66): abierta; [#64](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/64): abierta; [#63](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/63): abierta; [#65](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/65): abierta; [#61](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/61): abierta; [#60](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/60): abierta; [#59](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/59): abierta; [#57](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/57): abierta; [#58](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/58): abierta; [#62](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/62): abierta; [#56](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/56): fusionada 2026-11-02T04:49:01Z; [#55](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/55): fusionada 2026-11-02T02:41:05Z; [#54](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/54): fusionada 2026-10-25T23:22:50Z

**CI consultado:** [Purga periódica de datos de ubicación 41601350180](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41601350180): success (misma punta); [CI ROUTB 41549294394](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41549294394): success (otra revisión o PR); [CI ROUTB 41390533932](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41390533932): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5f13a93fb2edf5977c582662537f2af32bd1a4d2/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ROUTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ROUTB/pulls) · [5f13a93fb2edf5977c582662537f2af32bd1a4d2](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/5f13a93fb2edf5977c582662537f2af32bd1a4d2) · [41601350180](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41601350180) · [41549294394](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41549294394) · [41549143010](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41549143010) · [41549142681](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41549142681) · [41411210448](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41411210448) · [41390732747](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41390732747) · [41390712873](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41390712873) · [41390697621](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41390697621) · [125100712178](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41390533932/job/125100712178) · [125101016370](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41390533932/job/125101016370) · [125632537567](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41549294394/job/125632537567) · [125633062295](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41549294394/job/125633062295) · [69](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/69) · [Antecedentes](seguimiento-s12-2026-11-02.md#routb).

<a id="shareu"></a>

## ShareU

Rama **master**, [2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767), fecha del commit 2026-10-25T22:52:08Z (UTC). Observación: 2026-11-03T13:04:01.027Z.

Revalidación del 3/nov frente al 2/nov: misma punta, README, issues, PR y resultados CI; se conserva el feedback previo sin presentar avances anteriores como nuevos. Se mantienen diez issues abiertas, diez cerradas, PR #22/#23 abiertas y workflow de la punta fallido sin jobs; no hay ejecución nueva que permita atribuir la falla exclusivamente a Sonar. README conserva placeholders Vercel/Render.

**Próximos pasos:**
- Conciliar README/C4/ADR con Firestore y publicar URLs institucionales concretas de frontend/API.
- Corregir workflow con evidencia de pruebas del repositorio y resiliencia; no atribuir falla exclusivamente a Sonar ni presentar cliente sustituido como persistencia productiva.

**Issues:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: 10 completed.

**README:** Ausente. README solo ofrece placeholders Vercel/Render y localhost, no endpoints públicos concretos.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z

**CI consultado:** [.github/workflows/tests.yml 40242189282](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282): failure (misma punta); [.github/workflows/tests.yml 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458): failure (otra revisión o PR); [Tests 36479388452](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479388452): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_ShareU/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_ShareU/pulls) · [2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767) · [40242189282](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282) · [36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458) · [36480560316](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36480560316) · [36479877131](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479877131) · [36479388452](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479388452) · [36379843854](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36379843854) · [35632045274](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/35632045274) · [35561494254](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/35561494254) · [Antecedentes](seguimiento-s12-2026-11-02.md#shareu).

<a id="sistema-de-calificacion-automatica"></a>

## Calificación automática

Rama **master**, [f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc), fecha del commit 2026-11-02T01:05:36Z (UTC). Observación: 2026-11-03T13:07:50.138Z.

Sin cambios frente al 2/nov en master (f4548a9), README, issues, PR ni ejecuciones CI recientes. La rama despliegue conserva 99b1a28. Se revalida el mismo run 41370619522, exitoso en backend, frontend, dependencias y publicación de la rama de despliegue; no es una ejecución nueva ni demuestra por sí solo la revisión servida hoy. El README sigue clasificando como Institucional al publicar frontend y API bajo iscoutb.dev, con revision.txt; conserva Render como antecedente. La evidencia del recorrido API→worker incorporada previamente corresponde al 30/oct, no a una comprobación en vivo del 3/nov. Persisten los pendientes de autenticación/autorización, concurrencia, recuperación y trazabilidad del flujo completo.

**Próximos pasos:**
- Vincular revision.txt y un recorrido frontend→API→worker a la revisión efectivamente servida; la evidencia incorporada describe una revisión del 30/oct.
- Resolver autenticación y autorización antes de cargar datos reales; conservar los límites declarados del presupuesto por proceso y validar concurrencia y recuperación.
- Acreditar respaldo/restauración y EC-07 con el lote objetivo en el entorno servido; no confundir ingesta/worker con calificación OMR integral.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin merge

**CI consultado:** [CI 41370619522](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41370619522): success (misma punta); [CI 41338415453](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41338415453): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pulls) · [f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc) · [Antecedentes](seguimiento-s12-2026-11-02.md#sistema-de-calificacion-automatica).

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [44e1cc001e60f70a9d156506d81921a743836517](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/44e1cc001e60f70a9d156506d81921a743836517), fecha del commit 2026-11-01T18:28:43Z (UTC). Observación: 2026-11-03T13:07:50.594Z.

Sin cambios frente al 2/nov en main (44e1cc0), README, siete issues, diez PR cerrados ni resultado de los últimos workflows. Se releen los logs del mismo run 41336869271 del 1/nov: 340 pruebas exitosas, ambas auditorías de locks Python sin avisos y comprobación Dart/OSV. El Quality Gate sigue en ERROR por new_security_rating=3 frente a umbral 1; CI failure y CD skipped. No existe ejecución nueva que corrija el bloqueo. El README mantiene la API institucional y la política enlazada; permanecen sus descripciones desactualizadas sobre cliente e integraciones. Se conservan T-02/T-08 implementadas en repositorio, sin extender esa evidencia a producción. Se preserva la confirmación docente de que TAIA presentó y funciona; esta auditoría no la recalifica ni añade una nueva prueba en vivo.

**Próximos pasos:**
- Resolver los hallazgos de seguridad de Sonar y obtener Quality Gate OK de la revisión corregida; 340 pruebas exitosas no significan CI completo verde.
- Validar sesiones, renovación/revocación y consentimiento en la revisión servida, incluida migración de cuentas existentes; no seguir marcando T-02/T-08 como ausentes en código.
- Actualizar README y ADR-0011 para reflejar cliente, webhook, métricas JWT, respaldo y alertas reales; mantener límites de alertas en memoria y ausencia de notificación externa.
- Añadir pruebas/análisis Flutter al pipeline y recorridos integrados en dispositivo; la verificación Dart/OSV no ejecuta Flutter.

**Issues:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: 4 completed.

**README:** Institucional. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#17](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/17): fusionada 2026-10-30T22:18:28Z; [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z

**CI consultado:** [CD 41337016910](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41337016910): skipped (misma punta); [CI 41336869271](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336869271): failure (misma punta); [CI 41336725295](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336725295): failure (otra revisión o PR); [CD 41322405688](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41322405688): skipped (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/44e1cc001e60f70a9d156506d81921a743836517/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pulls) · [124938454800](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336869271/job/124938454800) · [124938454992](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336869271/job/124938454992) · [44e1cc001e60f70a9d156506d81921a743836517](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/44e1cc001e60f70a9d156506d81921a743836517) · [Antecedentes](seguimiento-s12-2026-11-02.md#taia_-task-artificial-intelligence-assistant).

<a id="tienda-virtual-utb"></a>

## Tienda virtual UTB

Rama **main**, [4edb4a4105eb48aae35a3205c0998431088d91fd](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/4edb4a4105eb48aae35a3205c0998431088d91fd), fecha del commit 2026-11-02T00:19:42Z (UTC). Observación: 2026-11-03T13:07:51.062Z.

Sin cambios frente al 2/nov en main (4edb4a4), README, cero issues y trece PR fusionados. La última ejecución 41366553356 es la misma: frontend/backend success y job sonarcloud success, pero descarga del repositorio, recuperación de cobertura y análisis SonarCloud aparecen skipped; no acredita un Quality Gate nuevo. El README conserva la URL temporal sslip.io, clasificación Externo. La entrega de amenazas/privacidad y la auditoría local documentada siguen siendo evidencia documental: no hay cambio de código o dependencias ni ejecución SCA nueva observados. Permanecen pendientes las mitigaciones priorizadas, SCA reproducible bloqueante, dominio institucional y respaldo/restauración.

**Próximos pasos:**
- Implementar y probar las mitigaciones priorizadas: limitación de intentos, protección de sesión/cabeceras, restricciones del proxy y consentimiento persistido.
- Integrar SCA reproducible y bloqueante sobre las dependencias reales; resolver hallazgos de herramientas de build/pruebas sin presentarlos como inexistentes.
- Restablecer análisis Sonar/Quality Gate realmente ejecutado; sustituir URL temporal por dominio institucional y verificar respaldo/restauración.
- Mantener caché como propuesta; medir invalidación/concurrencia antes de atribuir implementación.

**Issues:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#13](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/13): fusionada 2026-11-02T00:19:42Z; [#12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/12): fusionada 2026-10-25T02:58:28Z; [#11](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/11): fusionada 2026-10-24T20:15:26Z

**CI consultado:** [Pruebas 41366553356](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/41366553356): success (misma punta); [Pruebas 41366314063](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/41366314063): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/4edb4a4105eb48aae35a3205c0998431088d91fd/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pulls) · [4edb4a4105eb48aae35a3205c0998431088d91fd](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/4edb4a4105eb48aae35a3205c0998431088d91fd) · [Antecedentes](seguimiento-s12-2026-11-02.md#tienda-virtual-utb).

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [fb7378dac4cdb0b95cf1bdfe22454a255051f990](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/fb7378dac4cdb0b95cf1bdfe22454a255051f990), fecha del commit 2026-11-03T00:37:47Z (UTC). Observación: 2026-11-03T13:07:51.491Z.

Se fusionan PR #6, #7 y #8: seis commits llevan main de c76288e a fb7378d e incorporan validaciones de duración/fechas y autocancelación de préstamos de salones, manejo de errores Flutter y ajustes de seguridad/estilo. La suite del run 41554222766 vuelve a pasar 78 pruebas. El CI ahora figura success, pero no hay remediación de dependencias: el lock conserva Starlette 0.50.0 y PyJWT 2.12.1; pip-audit añade 20 identificadores de exclusión y continue-on-error: true. Su log informa una vulnerabilidad conocida restante (PYSEC-2026-176 en PyJWT), con 28 entradas ignoradas. El documento sigue proponiendo actualizar la mayoría de esos hallazgos y describiendo un gate bloqueante que ya no coincide con el workflow. Deploy SSH sí termina, registra checkout fb7378d, Alembic y reinicio systemd, sin health/smoke posterior. Release APK publica v1.0.3; compilar/publicar no acredita el recorrido en dispositivo. README raíz e issue abierta no cambian: sigue Ausente la URL pública y desactualizada la descripción SQLite/Alembic. Persiste el fallback de pruebas a DATABASE_URL seguido de drop_all; el notificador sigue siendo simulado.

**Próximos pasos:**
- Restablecer una auditoría bloqueante, retirar continue-on-error y actualizar Starlette/PyJWT con compatibilidad verificada; revisar y documentar cada excepción, responsable y vencimiento. No confundir 28 entradas ignoradas con correcciones ni ocultar PYSEC-2026-176.
- Alinear el documento de dependencias con el workflow real: hoy afirma bloqueo y actualización mientras CI excluye hallazgos y continúa ante el error.
- Eliminar el fallback destructivo a DATABASE_URL o validar inequívocamente una base aislada antes de drop_all; el comentario que promete no tocar producción contradice el código.
- Añadir health/smoke y trazabilidad tras deploy; probar préstamos, autocancelación y expiración con cliente/APK v1.0.3 en entorno servido. El notificador simulado no acredita entrega externa.
- Publicar URL pública en README y corregir SQLite/Alembic desactualizados; convertir el aviso de claves inseguras en un rechazo verificable en producción y revisar datos personales escritos en logs.

**Issues:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Ausente. El README raíz solo publica direcciones locales; la URL pública continúa ausente.

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/8): fusionada 2026-11-03T00:37:47Z; [#7](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/7): fusionada 2026-11-03T00:25:29Z; [#6](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/6): fusionada 2026-11-03T00:13:54Z

**CI consultado:** [Release APK 41555375916](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41555375916): success (misma punta); [UTB Tracker CI 41554222766](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41554222766): success (misma punta); [UTB Tracker CI 41552753836](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41552753836): failure (otra revisión o PR); [Release APK 40132197969](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132197969): success (otra revisión o PR); [.github/workflows/ci.yml 40066463106](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40066463106): failure (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/fb7378dac4cdb0b95cf1bdfe22454a255051f990/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pulls) · [125649027551](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41554222766/job/125649027551) · [125649839370](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41554222766/job/125649839370) · [125652869304](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/41555375916/job/125652869304) · [fb7378dac4cdb0b95cf1bdfe22454a255051f990](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/fb7378dac4cdb0b95cf1bdfe22454a255051f990) · [v1.0.3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/releases/tag/v1.0.3) · [Antecedentes](seguimiento-s12-2026-11-02.md#utb_tracker).

<a id="uniteam"></a>

## uniTeam

Rama **master**, [5e18bc227e0aae35a3f3d797a8405d108a789ef7](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/5e18bc227e0aae35a3f3d797a8405d108a789ef7), fecha del commit 2026-11-02T05:17:31Z (UTC). Observación: 2026-11-03T13:07:52.138Z.

master (5e18bc2), README, issue cerrada y PR no cambian frente al 2/nov: quedan diez PR abiertos. Se relee la auditoría del mismo run 41393152938: pip-audit informa 48 entradas en cuatro paquetes aunque el job finaliza success. El workflow actual continúa canalizando la salida a tee sin pipefail; ese verde no acredita ausencia ni remediación de vulnerabilidades. CI de la misma punta conserva success en MySQL, frontend e imágenes. Hay cuatro nuevas sondas programadas fallidas desde el corte anterior; la última, run 41635489222 del 3/nov a las 12:24 UTC, vuelve a fallar seis comprobaciones contra las direcciones Render antiguas. No demuestra una caída de las URL DuckDNS publicadas en el README, que conservan clasificación Externo. No se acredita despliegue ni prueba integrada nuevos.

**Próximos pasos:**
- Hacer bloqueante la auditoría preservando el código de salida (pipefail o mecanismo equivalente) y resolver/justificar hallazgos Python con evidencia reproducible.
- Actualizar la sonda a las URL DuckDNS vigentes y repetir las seis comprobaciones antes de interpretar salud.
- Implementar y probar controles de seguridad que los ADR/modelo describen como pendientes; distinguir documentación, actualización de dependencias y mitigación efectiva.
- Publicar frontend y API institucionales; conservar caché como propuesta y taller SQLite separado.

**Issues:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#13](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/13): abierta; [#18](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/18): abierta; [#21](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/21): abierta; [#22](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/22): abierta; [#17](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/16): abierta; [#14](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/14): abierta; [#15](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/15): abierta; [#12](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/12): abierta; [#11](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/11): abierta; [#27](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/27): fusionada 2026-11-02T05:17:31Z; [#26](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/26): fusionada 2026-11-02T05:06:05Z; [#25](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/25): fusionada 2026-11-02T04:55:58Z

**CI consultado:** [Comprobación del despliegue 41635489222](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41635489222): failure (misma punta); [seguridad-dependencias 41393369597](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393369597): success (otra revisión o PR); [CI 41393369587](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393369587): success (otra revisión o PR); [CI 41393152995](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393152995): success (misma punta); [seguridad-dependencias 41393152938](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393152938): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/5e18bc227e0aae35a3f3d797a8405d108a789ef7/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_uniTeam/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_uniTeam/pulls) · [125108695377](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393152938/job/125108695377) · [125915498343](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41635489222/job/125915498343) · [5e18bc227e0aae35a3f3d797a8405d108a789ef7](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/5e18bc227e0aae35a3f3d797a8405d108a789ef7) · [Antecedentes](seguimiento-s12-2026-11-02.md#uniteam).

<a id="xald"></a>

## XALD

Rama **master**, [a79a6085acf3bca4f861473f99094c43899e2b35](https://github.com/ISCOUTB/AS_202620_XALD/commit/a79a6085acf3bca4f861473f99094c43899e2b35), fecha del commit 2026-11-02T02:03:07Z (UTC). Observación: 2026-11-03T13:07:52.607Z.

master (a79a608), README, experimental (7676801) y seis issues cerradas no cambian frente al 2/nov; se conservan cinco cierres completed y uno duplicate. Se abre PR Dependabot #42 para uvicorn 0.30.0→0.54.0, elevando los PR abiertos de catorce a quince; su ejecución Android CI 41544247152 termina success, sin que eso implique integración. La última ejecución de master sigue siendo 41375620434 del 2/nov, exitosa en Android, backend, auditoría y deploy-backend, ya revisada el día anterior. No hay publicación nueva de master acreditada en este corte. README mantiene la API Render y clasificación Externo. Persisten la validación integrada en dispositivo y trazabilidad de revisión servida, así como los pendientes de ejecución de cola y deduplicación; no se infieren resueltos por una actualización Dependabot sin fusionar.

**Próximos pasos:**
- Validar controles y sincronización en dispositivo con trazabilidad a la revisión servida; health 200 no sustituye la validación del deploy ni del flujo completo.
- Mantener pendientes ejecutor real de procesarPendientes y persistencia de cola/deduplicación hasta aportar evidencia; no inferirlos de la entrega de seguridad.
- Revisar y probar los 15 PR de dependencias antes de integrarlos; conservar análisis reproducible sobre lo que realmente se despliega.
- Publicar API institucional y conciliar experimental con master sin restaurar documentación obsoleta.

**Issues:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. Motivos: 5 completed; 1 duplicate.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** [#42](https://github.com/ISCOUTB/AS_202620_XALD/pull/42): abierta; [#41](https://github.com/ISCOUTB/AS_202620_XALD/pull/41): abierta; [#40](https://github.com/ISCOUTB/AS_202620_XALD/pull/40): abierta; [#39](https://github.com/ISCOUTB/AS_202620_XALD/pull/39): abierta; [#34](https://github.com/ISCOUTB/AS_202620_XALD/pull/34): abierta; [#38](https://github.com/ISCOUTB/AS_202620_XALD/pull/38): abierta; [#37](https://github.com/ISCOUTB/AS_202620_XALD/pull/37): abierta; [#33](https://github.com/ISCOUTB/AS_202620_XALD/pull/33): abierta; [#35](https://github.com/ISCOUTB/AS_202620_XALD/pull/35): abierta; [#32](https://github.com/ISCOUTB/AS_202620_XALD/pull/32): abierta; [#29](https://github.com/ISCOUTB/AS_202620_XALD/pull/29): abierta; [#31](https://github.com/ISCOUTB/AS_202620_XALD/pull/31): abierta; [#36](https://github.com/ISCOUTB/AS_202620_XALD/pull/36): abierta; [#28](https://github.com/ISCOUTB/AS_202620_XALD/pull/28): abierta; [#30](https://github.com/ISCOUTB/AS_202620_XALD/pull/30): abierta; [#27](https://github.com/ISCOUTB/AS_202620_XALD/pull/27): fusionada 2026-11-02T02:03:07Z; [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z

**CI consultado:** [Android CI 41544247152](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/41544247152): success (otra revisión o PR); [Android CI 41375620434](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/41375620434): success (misma punta)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_XALD/blob/a79a6085acf3bca4f861473f99094c43899e2b35/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_XALD/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_XALD/pulls) · [a79a6085acf3bca4f861473f99094c43899e2b35](https://github.com/ISCOUTB/AS_202620_XALD/commit/a79a6085acf3bca4f861473f99094c43899e2b35) · [Antecedentes](seguimiento-s12-2026-11-02.md#xald).

<a id="verifacts"></a>

## Verifacts

Rama **master**, [559612b61ee4cea46cef6d00f857d2e5c2794f03](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/559612b61ee4cea46cef6d00f857d2e5c2794f03), fecha del commit 2026-10-28T05:41:24Z (UTC). Observación: 2026-11-03T13:07:53.110Z.

Sin cambios frente al 2/nov en master (559612b del 28/oct), README, tres issues cerradas completed, cero PR ni ejecuciones CI recientes. Los mismos runs Tests 40639475382 y SonarCloud 40639475319 conservan success; no acreditan un despliegue nuevo. README mantiene explícitamente la referencia externa sslip.io solo por HTTP y el dominio iscoutb.dev/TLS como pendiente, clasificación Externo. Se mantienen pendientes controles SSRF, límites, timeout y protección del historial; retención y supresión continúan como propuestas. Sonar no sustituye evidencia SCA reproducible ni validación del recorrido navegador/persistencia.

**Próximos pasos:**
- Aportar pip-audit/npm audit fechados con revisión y versiones resueltas.
- Implementar y probar controles prioritarios; distinguir propuesta de operación.
- Completar subdominio institucional/TLS y recorrido navegador/persistencia con trazabilidad.

**Issues:** 0 abiertas / 3 cerradas; 0 abiertas sin asignar. Motivos: 3 completed.

**README:** Externo. Referencia documental del README actual; no comprobada en vivo en esta auditoría.

**PR consultadas:** Sin PR en la consulta.

**CI consultado:** [Tests 40639475382](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382): success (misma punta); [SonarCloud 40639475319](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319): success (misma punta); [SonarCloud 40636370321](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40636370321): success (otra revisión o PR); [Tests 40636370228](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40636370228): success (otra revisión o PR)

**Fuentes:** [README](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/README.md) · [issues](https://github.com/ISCOUTB/AS_202620_Verifacts/issues) · [pulls](https://github.com/ISCOUTB/AS_202620_Verifacts/pulls) · [559612b61ee4cea46cef6d00f857d2e5c2794f03](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/559612b61ee4cea46cef6d00f857d2e5c2794f03) · [Antecedentes](seguimiento-s12-2026-11-02.md#verifacts).

