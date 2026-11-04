# Revisión documental S13 · cierre domingo 2026-11-01

Revisión documental retrospectiva solicitada por el docente el **3 de noviembre de 2026**, sobre los 23 proyectos del listado vigente. Se mantiene el cierre al final del domingo en Colombia. No se recalculan notas ni se reemplazan matrices, planillas o estados históricos de evaluación.

**Cierre:** 2026-11-01 a las 23:59:59 COT. Límite exclusivo: **2026-11-02T05:00:00Z**.

La evidencia se reconstruye desde el historial de la rama principal y los snapshots citados, contrastando fusiones de PR y ejecuciones de CI cuando están disponibles. La fecha de un commit no prueba por sí sola cuándo se publicó: un merge local o un avance de rama puede alterar el recorrido de primer padre; las reservas específicas se indican por equipo. Solo se atribuye CI al cierre cuando su resultado terminó dentro del plazo. Código integrado, prueba, despliegue y aceptación funcional son evidencias distintas. No se ejecutó software estudiantil ni se realizaron verificaciones vivas retrospectivas.

Se conservan las confirmaciones docentes registradas el 20/oct: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. Esta confirmación posterior a S11 no demuestra que todo ello existiera al cierre del 18/oct; tampoco acredita cada cambio de S12/S13.

[Índice cronológico](revision-semanas-11-13-2026-11-03.md) · [Ficha S13](../../fichas/semana-13-evidencia-s13.md) · [Issues y PR](revision-issues-pr-s11-s13.md#s13--cierre-2026-11-01).

<a id="as-202620-audioshare"></a>

## AudioShare

Snapshot: [b2eb60d34a3ee41e2c632aa78e5a7021356461da](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/b2eb60d34a3ee41e2c632aa78e5a7021356461da), fecha Git **2026-11-01T23:37:45-05:00**.

Entrega amenazas priorizadas, privacidad y análisis de dependencias con decisiones explícitas. Reporta cero avisos en producción tras corregir body-parser, pero seis en el árbol completo, incluidos dos críticos de desarrollo aceptados con plan de migración. La API continúa con riesgos de autorización y subida de archivos; la publicación de imagen no acredita que la instancia pública haya sido redeplegada.

**Contraste con la ficha:**
- Amenazas ancladas al sistema y separación entre lectura de código y ataques no ejecutados.
- npm audit está propuesto, no ejecutado por el workflow de CI del corte; el análisis local no acredita ese criterio del pipeline.

**README y URL institucional:** README documenta https://audioshare.iscoutb.dev como aplicación pública; el backend sirve la interfaz web y API. No se verificó retrospectivamente funcionamiento ni versión publicada.

**CI y publicación:** Flutter: success (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534313); CI: success (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534440); Publicar imagen: success (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534404)

**Issues al cierre:** 2 abiertas y 2 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-audioshare).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/amenazas-priorizadas.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b2eb60d34a3ee41e2c632aa78e5a7021356461da/docs/amenazas-priorizadas.md)
- [docs/analisis-dependencias.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b2eb60d34a3ee41e2c632aa78e5a7021356461da/docs/analisis-dependencias.md)
- [docs/privacidad.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b2eb60d34a3ee41e2c632aa78e5a7021356461da/docs/privacidad.md)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b2eb60d34a3ee41e2c632aa78e5a7021356461da/.github/workflows/ci.yml)
- [Ejecución 41389534313](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534313)
- [Ejecución 41389534440](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534440)
- [Ejecución 41389534404](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/41389534404)

<a id="as-202620-clubs-utb"></a>

## Clubs UTB

Snapshot: [795beed409c880229dc3439e5882b3cb6aef3415](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/795beed409c880229dc3439e5882b3cb6aef3415), fecha Git **2026-11-01T21:51:33-05:00**.

Añade amenazas con probabilidad, impacto, responsables y estado, además de privacidad y revisión de dependencias. El código confirma el riesgo principal: auth_router guarda y compara contraseñas sin hash. La subida ya exige sesión, pero faltan límites, roles y otros controles; la privacidad todavía contiene decisiones y canales por completar.

**Contraste con la ficha:**
- La tabla no explicita categorías STRIDE y debe vincularse sistemáticamente con C4.
- pip-audit limpio es reporte local del equipo, no auditoría acreditada en pipeline; los workflows siguen fallando.
- Priorizar hash de contraseñas, secretos sin valor predeterminado y autorización; no publicar datos reales hasta cerrar estos riesgos.

**README y URL institucional:** README solo muestra localhost; no URL pública concreta ni subdominio institucional documentado. ADR-0009 usa api-linkclub.iscoutb.dev en un ejemplo de archivo estático, pero no sustituye una URL de despliegue vigente documentada en README ni prueba funcionamiento.

**CI y publicación:** .github/workflows/backend-tests.yml: failure (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379945028); .github/workflows/contrato.yml: failure (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379943754)

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-clubs-utb).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/arc42/tabla_amenazas.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/795beed409c880229dc3439e5882b3cb6aef3415/docs/arc42/tabla_amenazas.md)
- [docs/arc42/analisis_dependencias.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/795beed409c880229dc3439e5882b3cb6aef3415/docs/arc42/analisis_dependencias.md)
- [docs/arc42/privacidad.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/795beed409c880229dc3439e5882b3cb6aef3415/docs/arc42/privacidad.md)
- [backend/src/linkclub/adapters/inbound/api/auth_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/795beed409c880229dc3439e5882b3cb6aef3415/backend/src/linkclub/adapters/inbound/api/auth_router.py)
- [Ejecución 41379945028](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379945028)
- [Ejecución 41379943754](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/41379943754)

<a id="as-202620-dinamikutb"></a>

## DinamikUTB

Snapshot: [df258e304538eae925acf1b3cc43267112eda6d1](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/df258e304538eae925acf1b3cc43267112eda6d1), fecha Git **2026-11-01T23:59:20-05:00**.

Amplía gestión e historial y documenta por separado frontend y API institucionales. Sin embargo, el material S13 está incompleto: arc42 enlaza docs/modelado-de-amenazas.md, que no existe en el snapshot, y la sección de riesgos vuelve a afirmar que usuarios e historial están pendientes pese al código incorporado. La auditoría de dependencias falla antes del cierre.

**Contraste con la ficha:**
- Reconciliar arc42§8/§11 con autenticación, historial y CORS reales; no aceptar enlaces ausentes como tabla STRIDE o privacidad.
- Agregar resultados del scanner, decisiones sobre hallazgos y plan priorizado verificable; el fallo de CI general termina después del cierre.

**README y URL institucional:** README distingue frontend https://dinamikutb.iscoutb.dev y API https://api.dinamikutb.iscoutb.dev.

**CI y publicación:** Auditoría de dependencias: failure (https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41391421776) Resultados terminados o iniciados después del cierre excluidos: Deploy frontend (GitHub Pages) https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41392155273; CI https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41391421837

**Issues al cierre:** 2 abiertas y 15 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-dinamikutb).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/arc42/08-cross-cutting-concepts.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/df258e304538eae925acf1b3cc43267112eda6d1/docs/arc42/08-cross-cutting-concepts.md)
- [docs/arc42/11-risks-and-technical-debt.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/df258e304538eae925acf1b3cc43267112eda6d1/docs/arc42/11-risks-and-technical-debt.md)
- [.github/workflows/dependency-audit.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/df258e304538eae925acf1b3cc43267112eda6d1/.github/workflows/dependency-audit.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/df258e304538eae925acf1b3cc43267112eda6d1/README.md)
- [Ejecución 41391421776](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41391421776)

<a id="as-202620-drift"></a>

## Drift

Snapshot: [5d64cede9a3559349d7481a917bb89003ebfe33d](https://github.com/ISCOUTB/AS_202620_Drift/commit/5d64cede9a3559349d7481a917bb89003ebfe33d), fecha Git **2026-11-01T23:13:33-05:00**.

Integra antes del cierre el modelo STRIDE, privacidad, autenticación administrativa y limitación de tasa, con ADR-0011/0012 y análisis de dependencias en CI. El reporte revisa avisos corregidos y riesgos aceptados; permanece pendiente decidir la retención/desactivación del access log. Se excluye PR #56, integrado después del domingo, aunque sus commits tengan fecha anterior.

**Contraste con la ficha:**
- Corte acreditado por PR #54 y CI de master en 5d64cede.
- Auditorías y pruebas aprobadas no prueban aceptación funcional de la URL institucional ni equivalencia con Azure.

**README y URL institucional:** README documenta frontend https://drift.iscoutb.dev y API bajo /api; Azure y Vercel son despliegues externos separados.

**CI y publicación:** Build and deploy Python app to Azure Web App - drift-utb-202620: success (https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41387265404); CI: success (https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41387265389)

**Issues al cierre:** 5 abiertas y 15 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-drift).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/seguridad/modelo-amenazas.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/5d64cede9a3559349d7481a917bb89003ebfe33d/docs/seguridad/modelo-amenazas.md)
- [docs/seguridad/privacidad.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/5d64cede9a3559349d7481a917bb89003ebfe33d/docs/seguridad/privacidad.md)
- [docs/evidencias/s13-analisis-dependencias.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/5d64cede9a3559349d7481a917bb89003ebfe33d/docs/evidencias/s13-analisis-dependencias.md)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_Drift/blob/5d64cede9a3559349d7481a917bb89003ebfe33d/.github/workflows/ci.yml)
- [Ejecución 41387265404](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41387265404)
- [Ejecución 41387265389](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/41387265389)

<a id="as-202620-elmapita"></a>

## ElMapita

Snapshot: [fc0f186153d117a5b0d9db715d521e154a8a2ef2](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/fc0f186153d117a5b0d9db715d521e154a8a2ef2), fecha Git **2026-10-29T20:52:42-05:00**.

Llega al corte con mejoras de mapa 3D, selección, ubicación y doble pestaña/idiomas integradas en octubre, pero sin los cambios de seguridad del 2/nov. No se encontraron en este snapshot una entrega STRIDE/privacidad y análisis de dependencias S13 completos. Se conserva la confirmación docente de que presentó y funciona, sin convertirla en validación de seguridad.

**Contraste con la ficha:**
- Las correcciones 8cd8600 y posteriores ocurren después de 05:00Z del 2/nov y quedan fuera del cierre colombiano.
- README no documenta URL institucional concreta; no confundir esto con falta de aplicación funcional.

**README y URL institucional:** README no contiene URL pública concreta; tu-proyecto.supabase.co es ejemplo, no despliegue.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40988421889)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-elmapita).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [README.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/fc0f186153d117a5b0d9db715d521e154a8a2ef2/README.md)
- [docs/datos/consistencia-operaciones.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/fc0f186153d117a5b0d9db715d521e154a8a2ef2/docs/datos/consistencia-operaciones.md)
- [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/fc0f186153d117a5b0d9db715d521e154a8a2ef2/docs/arc42/arc42-template-EN.md)
- [Ejecución 40988421889](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/40988421889)

<a id="as-202620-enagenda"></a>

## EnAgenda

Snapshot: [a6dde3025c6864eb8c2871c6e9732b205f68001b](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b), fecha Git **2026-10-25T22:57:38-05:00**.

La rama principal no cambia respecto al corte S12. No se acredita nueva entrega S13 de amenazas priorizadas, privacidad y dependencias; el trabajo de seguridad posterior o sin integrar no puede sumarse al domingo. Continúan las limitaciones de concurrencia real, restauración y despliegue documentadas en S12.

**Contraste con la ficha:**
- Mismo hash a6dde302 en S12/S13; esto describe integración, no ausencia absoluta de trabajo en ramas.
- Completar STRIDE sobre C4, responsables, resultados de auditoría y tratamiento de datos de usuarios/invitados.

**README y URL institucional:** README conserva host-asignado y localhost; no URL de despliegue concreta ni iscoutb.dev.

**CI y publicación:** Taller mensajes y consistencia: success (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284); CI: failure (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410); pages build and deployment: success (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-enagenda).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md)
- [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/arc42/08-conceptos-transversales.md)
- [Ejecución 40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284)
- [Ejecución 40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410)
- [Ejecución 40266609521](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521)

<a id="as-202620-gimnasioutb"></a>

## GimnasioUTB

Snapshot: [e0a458097202bb48e25c79d22614d759e3549ee0](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/e0a458097202bb48e25c79d22614d759e3549ee0), fecha Git **2026-11-01T19:33:07-05:00**.

Entrega STRIDE concreto, priorización, responsables y riesgos residuales; agrega autenticación de operador, controles de cuerpo/CORS, ADR-0007 y auditoría npm en CI. Documenta la corrección deqs y resultado sin avisos, además de privacidad. El token compartido sigue sin identidad individual y persisten timeouts, límite de tasa en proxy y limpieza de dependencias Flutter pendientes.

**Contraste con la ficha:**
- Log de eventos sigue diseño, no historial implementado.
- CI incluye npm audit y verificación de firmas; Dependabot posterior al cierre no se contabiliza.

**README y URL institucional:** README documenta API https://gimnasio-utb.iscoutb.dev; no es evidencia de frontend web.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41367755427) Resultados terminados o iniciados después del cierre excluidos: npm_and_yarn in / for pg, dependency-cruiser - Update #1675802818 https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541430019; github_actions in /. - Update #1675802707 https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541424703; docker in /. - Update #1675802703 https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541424862; npm_and_yarn in /. - Update #1675802701 https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41541425290

**Issues al cierre:** 16 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-gimnasioutb).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/s13-seguridad-amenazas.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/e0a458097202bb48e25c79d22614d759e3549ee0/docs/s13-seguridad-amenazas.md)
- [docs/adr/0007-autenticacion-operador-y-cors.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/e0a458097202bb48e25c79d22614d759e3549ee0/docs/adr/0007-autenticacion-operador-y-cors.md)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/e0a458097202bb48e25c79d22614d759e3549ee0/.github/workflows/ci.yml)
- [Ejecución 41367755427](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/41367755427)

<a id="as-202620-inventrack"></a>

## InvenTrack

Snapshot: [190db13b6591c3e38da125700b2d791bbf8b25e3](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/190db13b6591c3e38da125700b2d791bbf8b25e3), fecha Git **2026-11-01T23:04:45-05:00**.

Añade idempotencia HTTP en memoria, amenazas priorizadas, responsables y revisión de dependencias con auditoría en CI. Reconoce como riesgo crítico que operaciones de inventario son públicas sin autenticación y que reinicios pierden stock, historial, eventos y claves. El reporte de despliegue distingue API pública de una versión nueva aún por acreditar.

**Contraste con la ficha:**
- Prioridad inmediata: control de acceso e identidad del actor antes de datos reales.
- Lock, deduplicación, DLQ e idempotencia están acotados a una instancia y no son persistencia durable.

**README y URL institucional:** README documenta API https://inventrack.iscoutb.dev y alternativa Render; no frontend web independiente.

**CI y publicación:** Run Tests: success (https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386451056) Resultados terminados o iniciados después del cierre excluidos: pip in /. - Update #1673819067 https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41436852813

**Issues al cierre:** 0 abiertas y 7 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-inventrack).

**Límites y evidencia posterior:**
- Revisión estática de snapshot; no se ejecutó código estudiantil ni se verificó retrospectivamente la operación del despliegue.

**Fuentes:**
- [docs/evidencia-seguridad-s13.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/190db13b6591c3e38da125700b2d791bbf8b25e3/docs/evidencia-seguridad-s13.md)
- [docs/adr/0017-idempotencia-http-en-comandos-de-inventario.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/190db13b6591c3e38da125700b2d791bbf8b25e3/docs/adr/0017-idempotencia-http-en-comandos-de-inventario.md)
- [app/inventario/infrastructure/idempotency.py](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/190db13b6591c3e38da125700b2d791bbf8b25e3/app/inventario/infrastructure/idempotency.py)
- [.github/workflows/test.yml](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/190db13b6591c3e38da125700b2d791bbf8b25e3/.github/workflows/test.yml)
- [Ejecución 41386451056](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/41386451056)

<a id="as-202620-laplacita"></a>

## LaPlacita

Snapshot: [eb8d3ffb5e44aa982b8279c91e68ba0bb1837884](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884), fecha Git **2026-11-01T11:20:53-05:00**.

Al cierre S13 están integrados el modelo STRIDE, prioridades, responsables y estados, privacidad y decisiones de reducción de superficie pública. CI verifica pruebas, contratos, construcción y auditoría de dependencias del backend y frontend; el README ya distingue los dos dominios institucionales.

**Contraste con la ficha:**
- Separar amenazas mitigadas de riesgos aceptados y pendientes, incluidos límites operativos y retiro de infraestructura anterior.
- La publicación del frontend y la aceptación funcional no se deducen del build verde.

**README y URL institucional:** README documenta frontend https://laplacita-app.iscoutb.dev y API https://laplacita-test.iscoutb.dev/api/v1.

**CI y publicación:** CI LaPlacita: success (https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/41325870183)

**Issues al cierre:** 0 abiertas y 14 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-laplacita).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencias/evidencias-s13.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884/docs/evidencias/evidencias-s13.md)
- [docs/evidencias/sesion-stride-31-10.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884/docs/evidencias/sesion-stride-31-10.md)
- [backend/tests/seguridad-s13.test.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884/backend/tests/seguridad-s13.test.js)
- [README.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884/README.md)

<a id="as-202620-lostvault"></a>

## LostVault

Snapshot: [58c5c9524e3d1dd51d970e36a38bab690e10470e](https://github.com/ISCOUTB/AS_202620_LostVault/commit/58c5c9524e3d1dd51d970e36a38bab690e10470e), fecha Git **2026-11-01T22:43:13-05:00**.

S13 añade amenazas priorizadas, responsables, privacidad y revisión documental de dependencias. El propio documento deja pendientes la verificación real de identidad, persistencia compartida, limitación de tasa y actualización de PyJWT; no acredita una auditoría automatizada de dependencias en el pipeline.

**Contraste con la ficha:**
- El workflow backend no incorpora todavía pip-audit; CI de pruebas verde no acredita ese criterio.
- panel.iscoutb.dev se cita como panel de administración, no como URL pública de la solución.
- La ubicación y configuración del despliegue descritas por el equipo siguen sin verificación funcional independiente.

**README y URL institucional:** README sin URL pública concreta de solución; no confundir panel.iscoutb.dev con aplicación.

**CI y publicación:** Backend checks: success (https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384608353); Flutter checks: success (https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384608380); Build: success (https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/41384608212)

**Issues al cierre:** 0 abiertas y 1 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-lostvault).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/seguridad/amenazas-dependencias-privacidad.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/58c5c9524e3d1dd51d970e36a38bab690e10470e/docs/seguridad/amenazas-dependencias-privacidad.md)
- [.github/workflows/backend.yml](https://github.com/ISCOUTB/AS_202620_LostVault/blob/58c5c9524e3d1dd51d970e36a38bab690e10470e/.github/workflows/backend.yml)
- [backend/main.py](https://github.com/ISCOUTB/AS_202620_LostVault/blob/58c5c9524e3d1dd51d970e36a38bab690e10470e/backend/main.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/58c5c9524e3d1dd51d970e36a38bab690e10470e/README.md)

<a id="as-202620-mapsutb"></a>

## mapsutb

Snapshot: [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833), fecha Git **2026-10-25T09:04:14-05:00**.

S13 conserva exactamente el mismo commit de S12. En el árbol revisado no se encontró una evidencia específica S13 ni una tabla STRIDE con responsables, prioridades y resultados revisados de análisis de dependencias; el análisis estático existente no sustituye esos entregables.

**Contraste con la ficha:**
- No trasladar el buen resultado de CI y Firebase a cumplimiento automático de seguridad S13.
- Completar el modelado sobre C4, privacidad y decisiones de dependencias con evidencias fechadas.

**README y URL institucional:** README documenta frontend https://mapsutb.web.app, externo a iscoutb.dev.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200516007); Despliegue web (Firebase Hosting): success (https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200515940)

**Issues al cierre:** 0 abiertas y 54 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-mapsutb).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/arc42/08_concepts.adoc](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/docs/arc42/08_concepts.adoc)
- [docs/arc42/11_technical_risks.adoc](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/docs/arc42/11_technical_risks.adoc)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/.github/workflows/ci.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md)

<a id="as-202620-pideutb"></a>

## PideUtb

Snapshot: [e81e272b20498968b1016a261dee8bce250422da](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/e81e272b20498968b1016a261dee8bce250422da), fecha Git **2026-10-30T01:16:11-05:00**.

S13 presenta STRIDE aplicado a sus componentes, tratamiento mínimo de datos y una auditoría que separa dependencias de producción de herramientas de pruebas. El job de dependencias del hash de corte sí terminó correctamente; también el recorrido con navegador en CI.

**Contraste con la ficha:**
- El agotamiento del login por scrypt, la trazabilidad individual de entrega y las métricas públicas siguen como riesgos documentados.
- SonarCloud y Quality Gate están omitidos por configuración en el run inspeccionado: el job verde no representa un análisis ejecutado.
- El recorrido de CI no es una nueva aceptación funcional de producción.

**README y URL institucional:** README documenta frontend https://pideutb.iscoutb.dev y API https://api-pideutb.iscoutb.dev.

**CI y publicación:** CI: success (https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/41013098666)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-pideutb).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencia-s13.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/docs/evidencia-s13.md)
- [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/docs/arc42/arc42.md)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/.github/workflows/ci.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/README.md)

<a id="as-202620-proyecto-campusmarket"></a>

## CampusMarket

Snapshot: [f6a90d2094d90cd34c81e6e857bcb6c53e3c567e](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e), fecha Git **2026-11-01T20:09:10-05:00**.

S13 integra el modelo de amenazas con prioridad, estado y responsables; añade auditoría Python y decisiones sobre los hallazgos. La corrección de dependencias y la consolidación de arc42 están fusionadas antes del cierre; el README ya documenta Flutter Web en /app/ y la API institucional.

**Contraste con la ficha:**
- La evidencia de publicación del 1/nov es reporte del equipo y checks, no una nueva aceptación funcional independiente.
- Siguen pendientes cobertura de dependencias Dart e imágenes, prueba de carga controlada y respaldo/restauración productivos acreditados.
- No usar correcciones de PR posteriores al domingo como evidencia de este cierre.

**README y URL institucional:** README documenta API https://campusmarket.iscoutb.dev y frontend https://campusmarket.iscoutb.dev/app/.

**CI y publicación:** Compose y persistencia del MVP: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41370937423); S10 contrato del cliente en despliegue publico: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41370937320); Pruebas del backend: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41370937258); Validación Flutter MVP: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41370937307); Flujo real Web y Android: success (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/41370937299)

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-proyecto-campusmarket).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencias/evidencia-s13-amenazas-2026-11-01.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e/docs/evidencias/evidencia-s13-amenazas-2026-11-01.md)
- [docs/evidencias/cierre-web-institucional-2026-11-01.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e/docs/evidencias/cierre-web-institucional-2026-11-01.md)
- [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e/docs/arc42/08-conceptos-transversales.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e/README.md)

<a id="as-202620-recobra"></a>

## Recobra

Snapshot: [0dda9abd2c76ef9b10724221225c0ed228197c39](https://github.com/ISCOUTB/AS_202620_Recobra/commit/0dda9abd2c76ef9b10724221225c0ed228197c39), fecha Git **2026-10-28T21:32:33-05:00**.

S13 modela amenazas sobre C4, incorpora controles de uso, cabeceras y privacidad, y deja revisadas las decisiones sobre dependencias con vencimiento. En el run exacto funcionan los jobs de seguridad y el Quality Gate, además de pruebas contra PostgreSQL y de cliente.

**Contraste con la ficha:**
- El escaneo no equivale a cero vulnerabilidades: hay avisos aceptados según alcance, con fecha de revisión y plan de migración.
- El modelo registra acciones operativas de protección de acceso aún pendientes del administrador; no se consideran resueltas por un barrido de código.
- Se conserva la presentación confirmada por el docente, sin convertirla en aceptación de cada cambio posterior.

**README y URL institucional:** README documenta https://recobra.iscoutb.dev y cliente /app/, además de endpoints API.

**CI y publicación:** ci: success (https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40806972927)

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-recobra).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/seguridad/modelo-de-amenazas.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/docs/seguridad/modelo-de-amenazas.md)
- [docs/seguridad/analisis-de-dependencias.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/docs/seguridad/analisis-de-dependencias.md)
- [docs/seguridad/privacidad.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/docs/seguridad/privacidad.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/README.md)

<a id="as-202620-routb"></a>

## ROUTB

Snapshot: [5f13a93fb2edf5977c582662537f2af32bd1a4d2](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/5f13a93fb2edf5977c582662537f2af32bd1a4d2), fecha Git **2026-11-01T23:49:00-05:00**.

S13 añade STRIDE sobre C4, prioridades, responsables, privacidad y un ADR de seguridad. La revisión de dependencias concluye actualizando cuatro paquetes; el job pip-audit del commit final termina aprobado antes del cierre dominical.

**Contraste con la ficha:**
- El propio documento distingue riesgos aceptados como ausencia de SMS/OTP y almacenamiento de tokens en el dispositivo.
- El job rotulado SonarCloud Scan & Quality Gate solo ejecuta un mensaje de reserva sin token: no acredita análisis ni gate.
- Build de imagen y pruebas no demuestran una publicación funcional de ese mismo hash.

**README y URL institucional:** README documenta API https://routb.iscoutb.dev; no URL de frontend web independiente acreditada.

**CI y publicación:** CI ROUTB: success (https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/41390533932)

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-routb).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/evidencia/SEMANA13.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5f13a93fb2edf5977c582662537f2af32bd1a4d2/docs/evidencia/SEMANA13.md)
- [docs/adr/0023-estrategia-de-seguridad-stride-y-auditoria-de-dependencias.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5f13a93fb2edf5977c582662537f2af32bd1a4d2/docs/adr/0023-estrategia-de-seguridad-stride-y-auditoria-de-dependencias.md)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5f13a93fb2edf5977c582662537f2af32bd1a4d2/.github/workflows/ci.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5f13a93fb2edf5977c582662537f2af32bd1a4d2/README.md)

<a id="as-202620-shareu"></a>

## ShareU

Snapshot: [2c0ca6f50285cc803bb344e748a3121cf99d3767](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767), fecha Git **2026-10-25T17:52:08-05:00**.

S13 tiene el mismo hash de S12, sin nuevas incorporaciones en principal. No se encontró un modelo STRIDE específico con priorización, dueños y estados ni un resultado revisado de auditoría de dependencias en el conjunto revisado; persisten inconsistencias entre documentación de SQLite y código Firestore.

**Contraste con la ficha:**
- No atribuir la actualización Firebase del 3/nov a esta semana.
- Faltan evidencia pública de URL y validación funcional; la ausencia en README no demuestra que no exista trabajo de despliegue.

**README y URL institucional:** README solo contiene URLs locales, no despliegue público concreto ni iscoutb.dev.

**CI y publicación:** .github/workflows/tests.yml: failure (https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/40242189282)

**Issues al cierre:** 10 abiertas y 10 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-shareu).

**Límites y evidencia posterior:**
- Lectura de código y documentación; no se ejecutó software estudiantil ni se verificó producción retrospectivamente.
- Estados GitHub/PR/issues se integran por separado; no se infiere estado histórico del tablero.

**Fuentes:**
- [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/docs/arc42/arc42.md)
- [docs/adr/0012-persistencia-en-firestore.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/docs/adr/0012-persistencia-en-firestore.md)
- [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/.github/workflows/tests.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/README.md)

<a id="as-202620-sistema-de-calificacion-automatica"></a>

## Calificación automática

Snapshot: [f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc), fecha Git **2026-11-01T20:05:36-05:00**.

Presenta STRIDE ligado a C4, prioridades, responsables, estado de mitigaciones, privacidad y riesgos del componente generativo. OSV-Scanner está incorporado en CI y se documenta el hallazgo de certifi y su corrección. No equivale a seguridad terminada: autenticación antes de usar hojas reales, escaneo de imágenes y aislamiento efectivo de Redis siguen condicionados o pendientes.

**Contraste con la ficha:**
- Se distinguen mitigaciones implementadas, riesgo aceptado y controles aún por comprobar.
- El inventario de privacidad incluye imágenes, nombres de archivo e IP; no deben usarse datos reales sin resolver los controles declarados.

**README y URL institucional:** README publica frontend https://calificacion.iscoutb.dev y API https://api-calificacion.iscoutb.dev.

**CI y publicación:** [{'name': 'CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/41370619522', 'observed_completed_by': '2026-11-02T01:08:56Z', 'sha': 'f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc'}]

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-sistema-de-calificacion-automatica).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/evidencia/modelo-de-amenazas.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/docs/evidencia/modelo-de-amenazas.md)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/.github/workflows/ci.yml)
- [docs/adr/0022-poner-un-presupuesto-de-carga-delante-del-almacen.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/docs/adr/0022-poner-un-presupuesto-de-carga-delante-del-almacen.md)
- [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/README.md)

<a id="as-202620-taia--task-artificial-intelligence-assistant"></a>

## TAIA

Snapshot: [44e1cc001e60f70a9d156506d81921a743836517](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/44e1cc001e60f70a9d156506d81921a743836517), fecha Git **2026-11-01T13:28:43-05:00**.

Incluye modelo de amenazas priorizado, controles de sesiones, límites de uso, consentimiento, privacidad y riesgos de IA. Documenta auditoría Python y Dart y actualización de dependencias; el CI del commit de cierre falla y CD está omitido, por lo que los cambios fusionados no acreditan publicación de esa revisión.

**Contraste con la ficha:**
- El modelo vincula amenazas a C4, responsables y controles concretos, incluidos prompt injection y fuga de datos.
- Reconciliar textos residuales que aún llaman pendiente al consentimiento con la tabla que lo marca hecho; verificar el Quality Gate y el despliegue antes de afirmar aceptación.

**README y URL institucional:** README publica API https://taia-sistema.iscoutb.dev; no equivale a frontend web.

**CI y publicación:** [{'name': 'CD', 'conclusion': 'skipped', 'url': 'https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41337016910', 'observed_completed_by': '2026-11-01T18:31:01Z', 'sha': '44e1cc001e60f70a9d156506d81921a743836517'}, {'name': 'CI', 'conclusion': 'failure', 'url': 'https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/41336869271', 'observed_completed_by': '2026-11-01T18:30:57Z', 'sha': '44e1cc001e60f70a9d156506d81921a743836517'}]

**Issues al cierre:** 3 abiertas y 4 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-taia--task-artificial-intelligence-assistant).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/modelo_amenazas.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/44e1cc001e60f70a9d156506d81921a743836517/docs/modelo_amenazas.md)
- [docs/politica_privacidad.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/44e1cc001e60f70a9d156506d81921a743836517/docs/politica_privacidad.md)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/44e1cc001e60f70a9d156506d81921a743836517/.github/workflows/ci.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/44e1cc001e60f70a9d156506d81921a743836517/README.md)

<a id="as-202620-tienda-virtual-utb"></a>

## Tienda virtual UTB

Snapshot: [4edb4a4105eb48aae35a3205c0998431088d91fd](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/4edb4a4105eb48aae35a3205c0998431088d91fd), fecha Git **2026-11-01T19:19:42-05:00**.

Aporta amenazas priorizadas, inventario de privacidad y una revisión concreta de dependencias: declara cero hallazgos Python y trece npm, con exposición y decisiones. Sin embargo, los workflows del corte no incluyen pip-audit ni npm/pnpm audit; la auditoría documentada es local y no satisface por sí sola ejecución en pipeline.

**Contraste con la ficha:**
- Persisten medidas pendientes y discrepancias entre política de privacidad y retención real, como el carrito sin caducidad.
- Pruebas verdes no sustituyen un análisis de dependencias ejecutado y revisado en CI.

**README y URL institucional:** README publica URL sslip.io, no iscoutb.dev.

**CI y publicación:** [{'name': 'Pruebas', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/41366553356', 'observed_completed_by': '2026-11-02T00:21:10Z', 'sha': '4edb4a4105eb48aae35a3205c0998431088d91fd'}]

**Issues al cierre:** 0 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-tienda-virtual-utb).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/seguridad-amenazas-privacidad.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/4edb4a4105eb48aae35a3205c0998431088d91fd/docs/seguridad-amenazas-privacidad.md)
- [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/4edb4a4105eb48aae35a3205c0998431088d91fd/.github/workflows/tests.yml)
- [frontend/lib/carrito.ts](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/4edb4a4105eb48aae35a3205c0998431088d91fd/frontend/lib/carrito.ts)
- [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/4edb4a4105eb48aae35a3205c0998431088d91fd/README.md)

<a id="as-202620-utb-tracker"></a>

## UTB Tracker

Snapshot: [31932f0006542c6f3f6222071bb1a9c36b6f888a](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/31932f0006542c6f3f6222071bb1a9c36b6f888a), fecha Git **2026-10-26T01:03:01-05:00**.

Al cierre conserva la base de S12 y mejoras de administración, pero no contiene la entrega específica S13 de amenazas, dependencias y privacidad. Esta aparece en PR #5 fusionado el lunes 2 de noviembre a las 00:08 COT, después del domingo; debe registrarse como avance posterior y no atribuirse al cierre.

**Contraste con la ficha:**
- JWT y controles previos no sustituyen una tabla STRIDE priorizada, privacidad y análisis de dependencias con decisiones.
- No se incorporan en S13 los arreglos de seguridad del 2 y 3 de noviembre.

**README y URL institucional:** README contiene instrucciones locales, sin URL pública de despliegue.

**CI y publicación:** [{'name': 'UTB Tracker CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40278118926', 'observed_completed_by': '2026-10-26T06:11:09Z', 'sha': '31932f0006542c6f3f6222071bb1a9c36b6f888a'}]

**Issues al cierre:** 1 abiertas y 0 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-utb-tracker).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/arc42/arc42.md)
- [docs/adr/0004-seguridad-jwt.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/docs/adr/0004-seguridad-jwt.md)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/.github/workflows/ci.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/README.md)
- [Evidencia](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/5)

<a id="as-202620-uniteam"></a>

## uniTeam

Snapshot: [4666db95938f1cad94001a28f83c7b67922f368c](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/4666db95938f1cad94001a28f83c7b67922f368c), fecha Git **2026-11-01T23:55:58-05:00**.

Tiene amenazas STRIDE por componente, prioridades, responsables, privacidad y ADR de mitigaciones. El scanner de dependencias corre en verde, pero el informe conserva placeholders de URL, fecha, commit y hallazgos: no acredita revisión de resultados. Muchas mitigaciones prioritarias siguen pendientes; el plan admite que se hizo primero el escaneo por bajo costo.

**Contraste con la ficha:**
- Completar decisiones sobre resultados reales del análisis, no presentar una plantilla como informe cerrado.
- Alinear el orden de ejecución con riesgos prioritarios y distinguir controles propuestos de hechos.

**README y URL institucional:** README publica frontend/API DuckDNS, sin iscoutb.dev.

**CI y publicación:** [{'name': 'CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41391140332', 'observed_completed_by': '2026-11-02T04:56:46Z', 'sha': '4666db95938f1cad94001a28f83c7b67922f368c'}, {'name': 'seguridad-dependencias', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41391140342', 'observed_completed_by': '2026-11-02T04:56:26Z', 'sha': '4666db95938f1cad94001a28f83c7b67922f368c'}]

**Issues al cierre:** 0 abiertas y 1 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-uniteam).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/seguridad/amenazas.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/4666db95938f1cad94001a28f83c7b67922f368c/docs/seguridad/amenazas.md)
- [docs/seguridad/dependencias.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/4666db95938f1cad94001a28f83c7b67922f368c/docs/seguridad/dependencias.md)
- [docs/seguridad/privacidad.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/4666db95938f1cad94001a28f83c7b67922f368c/docs/seguridad/privacidad.md)
- [.github/workflows/seguridad.yml](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/4666db95938f1cad94001a28f83c7b67922f368c/.github/workflows/seguridad.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/4666db95938f1cad94001a28f83c7b67922f368c/README.md)

<a id="as-202620-xald"></a>

## XALD

Snapshot: [a79a6085acf3bca4f861473f99094c43899e2b35](https://github.com/ISCOUTB/AS_202620_XALD/commit/a79a6085acf3bca4f861473f99094c43899e2b35), fecha Git **2026-11-01T21:03:07-05:00**.

Entrega STRIDE relacionado con conectores/C4, amenazas priorizadas, privacidad y riesgos de Gemini. La auditoría de dependencias documenta hallazgos, correcciones y runs fallidos/recuperados; CI del cierre pasa. Persisten condiciones importantes: autenticación del móvil, validación del origen SMS, consentimiento informado y almacenamiento persistente/cifrado no quedan resueltos solo por el diseño.

**Contraste con la ficha:**
- El permiso RECEIVE_SMS de Android no reemplaza la autorización informada, reconocido por el equipo.
- Separar controles implementados de mitigaciones planeadas; la integración Gemini sigue condicionada.

**README y URL institucional:** README publica API https://xald-backend.onrender.com, no frontend ni iscoutb.dev.

**CI y publicación:** [{'name': 'Android CI', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/41375620434', 'observed_completed_by': '2026-11-02T02:04:45Z', 'sha': 'a79a6085acf3bca4f861473f99094c43899e2b35'}]

**Issues al cierre:** 0 abiertas y 6 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-xald).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/seguridad/modelo-amenazas.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/a79a6085acf3bca4f861473f99094c43899e2b35/docs/seguridad/modelo-amenazas.md)
- [docs/seguridad/analisis-dependencias.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/a79a6085acf3bca4f861473f99094c43899e2b35/docs/seguridad/analisis-dependencias.md)
- [docs/seguridad/privacidad.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/a79a6085acf3bca4f861473f99094c43899e2b35/docs/seguridad/privacidad.md)
- [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_XALD/blob/a79a6085acf3bca4f861473f99094c43899e2b35/.github/workflows/ci.yml)
- [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/a79a6085acf3bca4f861473f99094c43899e2b35/README.md)

<a id="as-202620-verifacts"></a>

## Verifacts

Snapshot: [559612b61ee4cea46cef6d00f857d2e5c2794f03](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/559612b61ee4cea46cef6d00f857d2e5c2794f03), fecha Git **2026-10-28T00:41:24-05:00**.

Presenta amenazas priorizadas y privacidad, reconociendo como pendientes SSRF, límites de extracción, timeouts, exposición del historial y TLS del laboratorio. El documento describe análisis de dependencias, pero los workflows inspeccionados no ejecutan pip-audit/npm audit: los runs Tests/SonarCloud verdes no prueban ese criterio.

**Contraste con la ficha:**
- La tabla distingue algunas medidas implementadas de diseño, pero no acredita ejecución de las mitigaciones críticas priorizadas.
- No confundir análisis estático SonarCloud con análisis de dependencias ni intención de borrado a 30 días con retención aplicada.

**README y URL institucional:** README publica HTTP sslip.io, no iscoutb.dev.

**CI y publicación:** [{'name': 'Tests', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475382', 'observed_completed_by': '2026-10-28T05:42:31Z', 'sha': '559612b61ee4cea46cef6d00f857d2e5c2794f03'}, {'name': 'SonarCloud', 'conclusion': 'success', 'url': 'https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40639475319', 'observed_completed_by': '2026-10-28T05:42:39Z', 'sha': '559612b61ee4cea46cef6d00f857d2e5c2794f03'}]

**Issues al cierre:** 0 abiertas y 3 cerradas, excluyendo PR. [Eventos, motivos disponibles y PR de la ventana](revision-issues-pr-s11-s13.md#s13-as-202620-verifacts).

**Límites y evidencia posterior:**
- Revisión documental y estática; no se ejecutó código estudiantil ni se verificó funcionamiento histórico del despliegue.
- Reconstrucción por historial de rama principal y fecha de commit, contrastada con CI; no es un registro completo de todas las fechas de push.

**Fuentes:**
- [docs/entregas/entrega-seguridad-amenazas-dependencias-privacidad.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/docs/entregas/entrega-seguridad-amenazas-dependencias-privacidad.md)
- [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/.github/workflows/tests.yml)
- [app/persistence/repository.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/app/persistence/repository.py)
- [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/README.md)

