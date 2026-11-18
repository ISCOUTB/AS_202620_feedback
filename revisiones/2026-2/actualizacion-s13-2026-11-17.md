# Actualización factual S13 · conciliación del 17 de noviembre de 2026

Nueva consulta del **17/nov Colombia (18/nov UTC)** de los 23 proyectos, al cierre original del **1/nov/2026, 23:59:59 Colombia**, límite exclusivo **2026-11-02T05:00:00Z**. Complementa la [revisión original](revision-s13-cierre-2026-11-01.md); no recalifica, no reemplaza sus snapshots con versiones actuales y no modifica matrices, planillas ni calificaciones.

Se revisaron nuevamente los archivos y README citados. **Se conservan los 23 snapshots históricos**: en Dinamik y TAIA, merges posteriores alteran el recorrido de primer padre, por lo que no es válido reemplazar automáticamente la evidencia S13 por el resultado de un `rev-list --first-parent` actual. Las precisiones y fuentes se detallan por proyecto. En AudioShare se precisa arquitectura documentada frente a versión efectivamente desplegada. Los cambios de noviembre quedan en el [seguimiento S14/S15](revision-semanas-14-15-2026-11-17.md), no retroactivos.

No se ejecutó código ni se verificó funcionamiento retrospectivo. Se mantienen las confirmaciones docentes previas de TAIA, ElMapita, ROUTB, PideUtb y Recobra sin extenderlas a cambios nuevos. README, código, reportes de equipo, CI, publicación y aceptación funcional se distinguen. No se reproducen notas ni valoraciones individuales.

## AudioShare

Coincide snapshot y URL institucional. Precisión: README describe la arquitectura Flutter Web + API, pero reporta observación del 26/oct con cliente legado y /rooms 404; por tanto no debe leerse «sirve interfaz web y API» como comprobación de la versión desplegada al cierre. El mismo README pide redespliegue. Las verificaciones del 8/nov pertenecen a S14, no prueban retroactivamente S13.

Fuentes: [snapshot](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/b2eb60d34a3ee41e2c632aa78e5a7021356461da) · [README del corte](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b2eb60d34a3ee41e2c632aa78e5a7021356461da/README.md).

## Clubs_UTB

Coincide snapshot. README no contiene dominio institucional concreto. La URL API que aparece posteriormente en S15 no se atribuye a S13. Los cuatro archivos citados por el informe existen en el snapshot; no se deduce operación pública del ejemplo de ADR.

Fuentes: [snapshot](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/795beed409c880229dc3439e5882b3cb6aef3415) · [README del corte](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/795beed409c880229dc3439e5882b3cb6aef3415/README.md).

## DinamikUTB

Se confirma el snapshot publicado df258e3, aunque NO coincide con la selección automática por primer padre del historial actual (3d27bc6). Un merge posterior altera el recorrido: no corresponde corregir el histórico con ese algoritmo. El run de auditoría 41391421776 acredita push de master con head_sha df258e3 creado 2026-11-02T04:59:23Z y finalizado failure a las 04:59:50Z, ambos antes del límite 05:00Z. README en df258e3 distingue frontend dinamikutb.iscoutb.dev y API api.dinamikutb.iscoutb.dev. Esas URLs cambian en S14; no mezclar con api-dinamikutb.iscoutb.dev ni Pages del snapshot posterior.

Fuentes: [snapshot](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/df258e304538eae925acf1b3cc43267112eda6d1) · [README del corte](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/df258e304538eae925acf1b3cc43267112eda6d1/README.md).

[Run del push anterior al cierre](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41391421776).

## Drift

Coincide snapshot 5d64cede y exclusión de PR #56 del corte: el merge be72a2f es 2/nov 00:53 COT. README identifica drift.iscoutb.dev para frontend/backend y /api; Azure y Vercel siguen siendo externos. Los archivos citados están presentes. Mediciones S14 no se trasladan a este cierre.

Fuentes: [snapshot](https://github.com/ISCOUTB/AS_202620_Drift/commit/5d64cede9a3559349d7481a917bb89003ebfe33d) · [README del corte](https://github.com/ISCOUTB/AS_202620_Drift/blob/5d64cede9a3559349d7481a917bb89003ebfe33d/README.md).

## ElMapita

Coincide snapshot fc0f186 y conversión de zona: 29/oct 19:52:42 UTC−6 es 20:52:42 COT. Los cambios 8cd8600, 5c9a5fd y 899bece del 1/nov UTC−6 ocurren ya el 2/nov en Colombia, después del límite S13. README carece de URL pública concreta y Supabase es ejemplo. Se conserva la confirmación docente de presentación y funcionamiento sin convertirla en aceptación de seguridad.

Fuentes: [snapshot](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/fc0f186153d117a5b0d9db715d521e154a8a2ef2) · [README del corte](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/fc0f186153d117a5b0d9db715d521e154a8a2ef2/README.md).

## EnAgenda

Coincide snapshot a6dde302, sin avance de rama principal en S13 ni S14/S15. README mantiene localhost y host-asignado: no URL concreta. Los archivos citados existen. Eso describe integración y documentación, no ausencia absoluta de trabajo ni prueba de inexistencia de despliegue.

Fuentes: [snapshot](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b) · [README del corte](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md).

## GimnasioUTB

Coincide snapshot e0a45809. README identifica gimnasio-utb.iscoutb.dev como backend API; no frontend web. Están presentes los archivos de amenazas, ADR-0007 y CI citados. Las verificaciones de infraestructura son reportes históricos del equipo, no pruebas ejecutadas ahora. Los cambios QR/Android de S15 son posteriores.

Fuentes: [snapshot](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/e0a458097202bb48e25c79d22614d759e3549ee0) · [README del corte](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/e0a458097202bb48e25c79d22614d759e3549ee0/README.md).

## InvenTrack

Coincide snapshot 190db13b. README identifica inventrack.iscoutb.dev como API y Render como alternativa y advierte necesidad de verificar redespliegue público del commit. Los cuatro archivos citados existen. El frontend Flutter incorporado en S15 no existe como evidencia del cierre S13.

Fuentes: [snapshot](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/190db13b6591c3e38da125700b2d791bbf8b25e3) · [README del corte](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/190db13b6591c3e38da125700b2d791bbf8b25e3/README.md).

## LaPlacita

Snapshot coincidente: [eb8d3ffb5e44](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884). README confirma frontend/PWA laplacita-app.iscoutb.dev y API laplacita-test.iscoutb.dev/api/v1. Los archivos de amenazas y evidencia S13 citados existen en el snapshot; los cambios administrativos y mediciones de noviembre se mantienen en S14/S15, sin incorporarlos retroactivamente.

**Fuentes:** [docs/evidencias/evidencias-s13.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884/docs/evidencias/evidencias-s13.md) · [docs/evidencias/sesion-stride-31-10.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884/docs/evidencias/sesion-stride-31-10.md) · [backend/tests/seguridad-s13.test.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884/backend/tests/seguridad-s13.test.js) · [README.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884/README.md)

## LostVault

Snapshot coincidente: [58c5c9524e3d](https://github.com/ISCOUTB/AS_202620_LostVault/commit/58c5c9524e3d1dd51d970e36a38bab690e10470e). README raíz sigue sin URL pública concreta. La API externa Vercel identificada en la medición S14 no se introduce como evidencia S13. El documento de seguridad y workflow backend citados existen en el snapshot.

**Fuentes:** [docs/seguridad/amenazas-dependencias-privacidad.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/58c5c9524e3d1dd51d970e36a38bab690e10470e/docs/seguridad/amenazas-dependencias-privacidad.md) · [.github/workflows/backend.yml](https://github.com/ISCOUTB/AS_202620_LostVault/blob/58c5c9524e3d1dd51d970e36a38bab690e10470e/.github/workflows/backend.yml) · [backend/main.py](https://github.com/ISCOUTB/AS_202620_LostVault/blob/58c5c9524e3d1dd51d970e36a38bab690e10470e/backend/main.py) · [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/58c5c9524e3d1dd51d970e36a38bab690e10470e/README.md)

## PROYECTO_CAMPUSMARKET

Snapshot coincidente: [f6a90d2094d9](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e). README del snapshot ya separa Flutter Web /app/ de API/Swagger en campusmarket.iscoutb.dev. El reporte de publicación del 1 de noviembre existe en el corte; sigue siendo evidencia documental, no aceptación funcional independiente. Favoritos, mensajería y auditoría posterior no se retrotraen a S13.

**Fuentes:** [docs/evidencias/evidencia-s13-amenazas-2026-11-01.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e/docs/evidencias/evidencia-s13-amenazas-2026-11-01.md) · [docs/evidencias/cierre-web-institucional-2026-11-01.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e/docs/evidencias/cierre-web-institucional-2026-11-01.md) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e/docs/arc42/08-conceptos-transversales.md) · [README.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e/README.md)

## PideUtb

Snapshot coincidente: [e81e272b2049](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/e81e272b20498968b1016a261dee8bce250422da). README confirma sitio pideutb.iscoutb.dev y API api-pideutb.iscoutb.dev con /docs y /health. Evidencia S13, arc42 y workflow citados existen en ese snapshot. Las fusiones del 2 y 7 de noviembre quedan fuera de S13.

**Fuentes:** [docs/evidencia-s13.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/docs/evidencia-s13.md) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/docs/arc42/arc42.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/.github/workflows/ci.yml) · [README.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e81e272b20498968b1016a261dee8bce250422da/README.md)

## ROUTB

Snapshot coincidente: [5f13a93fb2ed](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/5f13a93fb2edf5977c582662537f2af32bd1a4d2). README documenta API routb.iscoutb.dev y /health, no un frontend web. Mantiene configuración de publicación desde rama Changes; un snapshot en principal no prueba la versión desplegada. Los commits rotulados Semana 13 del 3 de noviembre quedan fuera del cierre del 1 de noviembre, aunque su título mencione esa semana.

**Fuentes:** [docs/evidencia/SEMANA13.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5f13a93fb2edf5977c582662537f2af32bd1a4d2/docs/evidencia/SEMANA13.md) · [docs/adr/0023-estrategia-de-seguridad-stride-y-auditoria-de-dependencias.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5f13a93fb2edf5977c582662537f2af32bd1a4d2/docs/adr/0023-estrategia-de-seguridad-stride-y-auditoria-de-dependencias.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5f13a93fb2edf5977c582662537f2af32bd1a4d2/.github/workflows/ci.yml) · [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5f13a93fb2edf5977c582662537f2af32bd1a4d2/README.md)

## Recobra

Snapshot coincidente: [0dda9abd2c76](https://github.com/ISCOUTB/AS_202620_Recobra/commit/0dda9abd2c76ef9b10724221225c0ed228197c39). README confirma vitrina /, cliente Flutter /app/ y rutas API en recobra.iscoutb.dev. Los tres documentos de seguridad citados existen en el snapshot. La medición añadida el 8 de noviembre pertenece a S14, no a S13.

**Fuentes:** [docs/seguridad/modelo-de-amenazas.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/docs/seguridad/modelo-de-amenazas.md) · [docs/seguridad/analisis-de-dependencias.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/docs/seguridad/analisis-de-dependencias.md) · [docs/seguridad/privacidad.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/docs/seguridad/privacidad.md) · [README.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/0dda9abd2c76ef9b10724221225c0ed228197c39/README.md)

## ShareU

Snapshot coincidente: [2c0ca6f50285](https://github.com/ISCOUTB/AS_202620_ShareU/commit/2c0ca6f50285cc803bb344e748a3121cf99d3767). README conserva solo URLs locales de operación, además de enlaces de repositorio/SonarCloud; no documenta URL pública institucional. Los archivos arc42, ADR Firestore y workflow citados existen. La incorporación del sitio Firebase del 3 de noviembre queda fuera de S13.

**Fuentes:** [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/docs/arc42/arc42.md) · [docs/adr/0012-persistencia-en-firestore.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/docs/adr/0012-persistencia-en-firestore.md) · [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/.github/workflows/tests.yml) · [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/2c0ca6f50285cc803bb344e748a3121cf99d3767/README.md)

## Sistema-de-calificacion-automatica

Snapshot coincidente: [f4548a92bf7a](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc). README separa frontend calificacion.iscoutb.dev, API api-calificacion.iscoutb.dev y revision.txt. El modelo de amenazas, workflow y ADR de presupuesto de carga citados existen en el snapshot. La lectura OMR y sus mediciones añadidas el 8 de noviembre no se atribuyen a S13.

**Fuentes:** [docs/evidencia/modelo-de-amenazas.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/docs/evidencia/modelo-de-amenazas.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/.github/workflows/ci.yml) · [docs/adr/0022-poner-un-presupuesto-de-carga-delante-del-almacen.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/docs/adr/0022-poner-un-presupuesto-de-carga-delante-del-almacen.md) · [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc/README.md)


## XALD

SHA coincide. README confirma API Render externa; existen modelo de amenazas, análisis de dependencias y privacidad en docs/seguridad. No incorporar medición ESC-05 del 8/nov en S13.

[Snapshot](https://github.com/ISCOUTB/AS_202620_XALD/commit/a79a6085acf3bca4f861473f99094c43899e2b35) · [README del snapshot](https://github.com/ISCOUTB/AS_202620_XALD/blob/a79a6085acf3bca4f861473f99094c43899e2b35/README.md)

## TIENDA-VIRTUAL-UTB

SHA coincide. README confirma URL sslip.io externa y el árbol contiene docs/seguridad-amenazas-privacidad.md. La medición escenario 4 y documento de riesgos incorporados el 8/nov permanecen fuera de S13.

[Snapshot](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/4edb4a4105eb48aae35a3205c0998431088d91fd) · [README del snapshot](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/4edb4a4105eb48aae35a3205c0998431088d91fd/README.md)

## Verifacts

SHA coincide. README confirma referencia HTTP sslip.io y declara URL institucional pendiente. No sustituir retrospectivamente por verifacts.iscoutb.dev: este enlace se incorpora el 5/nov. Existe la entrega de amenazas/dependencias/privacidad citada.

[Snapshot](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/559612b61ee4cea46cef6d00f857d2e5c2794f03) · [README del snapshot](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/559612b61ee4cea46cef6d00f857d2e5c2794f03/README.md)

## uniTeam

SHA coincide. README separa frontend y API DuckDNS; existen documentos amenazas/dependencias/privacidad y workflow seguridad. Los merges de ajuste del scanner a las 00:06 y 00:17 COT del 2/nov son posteriores al cierre y no se retrotraen.

[Snapshot](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/4666db95938f1cad94001a28f83c7b67922f368c) · [README del snapshot](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/4666db95938f1cad94001a28f83c7b67922f368c/README.md)

## mapsutb

SHA coincide. README apunta al frontend Firebase externo. No hay archivo específico S13 ni modelo de amenazas en ese snapshot; la documentación de seguridad y evidencias S13/S14 aparece el 11/nov y queda como actualización posterior.

[Snapshot](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833) · [README del snapshot](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md)

## UTB_TRACKER

SHA coincide. README del snapshot no publica URL externa; existe ADR de JWT, pero los documentos específicos de seguridad añadidos por PR #5 el 2/nov son posteriores. No trasladar a S13 ni nip.io ni funcionalidades de noviembre.

[Snapshot](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/31932f0006542c6f3f6222071bb1a9c36b6f888a) · [README del snapshot](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/31932f0006542c6f3f6222071bb1a9c36b6f888a/README.md)

## TAIA_-Task-Artificial-Intelligence-Assistant

El SHA histórico 44e1cc0 se conserva. El primer padre actual conduce a 023dc7f porque el merge local 7342f34 del 8/nov coloca 44e1cc0 como segundo padre. Por ello el algoritmo simple de primer padre no invalida el snapshot histórico, respaldado entonces por CI fechado el 1/nov. README de 44e1cc0 confirma API institucional; existen política de privacidad y consentimiento. No presentar esos cambios como nuevos en S14. No se volvió a verificar el resultado de los runs históricos en esta conciliación.

[Snapshot](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/44e1cc001e60f70a9d156506d81921a743836517) · [README del snapshot](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/44e1cc001e60f70a9d156506d81921a743836517/README.md)



## Conciliación de issues y PR

Reconsulta del 18/nov/2026 UTC. Se conserva íntegro el [informe histórico de S11–S13](revision-issues-pr-s11-s13.md#s13--cierre-2026-11-01): esta conciliación no reemplaza la revisión, no recalifica ni modifica estados de evaluación.

**Corte exclusivo:** 2026-11-02T05:00:00Z (1/nov a las 23:59:59 Colombia). Ventana de fusiones S13: desde 2026-10-26T05:00:00Z hasta el corte exclusivo. Las colecciones completas de issues y eventos de GitHub permitieron reconstruir cierre/reapertura anterior al corte; se excluyeron PR del conteo de issues. Las PR se cuentan mediante `merged_at`, en cualquier rama destino, como en el informe original. Integración no equivale a despliegue ni aceptación funcional. No se consultaron estados personalizados de Projects.

| Proyecto | Issues abiertas S13 | Issues cerradas S13 | PR fusionadas S13 | Contra informe del 3/nov |
|---|---:|---:|---:|---|
| [AudioShare](https://github.com/ISCOUTB/AS_202620_AudioShare/issues?q=is%3Aissue) | 2 | 2 | 0 | Coincide |
| [Clubs_UTB](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/issues?q=is%3Aissue) | 0 | 0 | 0 | Coincide |
| [DinamikUTB](https://github.com/ISCOUTB/AS_202620_DinamikUTB/issues?q=is%3Aissue) | 2 | 15 | 0 | Coincide |
| [Drift](https://github.com/ISCOUTB/AS_202620_Drift/issues?q=is%3Aissue) | 5 | 15 | 8 | Coincide |
| [ElMapita](https://github.com/ISCOUTB/AS_202620_ElMapita/issues?q=is%3Aissue) | 1 | 0 | 0 | Coincide |
| [EnAgenda](https://github.com/ISCOUTB/AS_202620_EnAgenda/issues?q=is%3Aissue) | 1 | 0 | 0 | Coincide |
| [GimnasioUTB](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/issues?q=is%3Aissue) | 16 | 0 | 2 | Coincide |
| [InvenTrack](https://github.com/ISCOUTB/AS_202620_InvenTrack/issues?q=is%3Aissue) | 0 | 7 | 0 | Coincide |
| [LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/issues?q=is%3Aissue) | 0 | 14 | 4 | Coincide |
| [LostVault](https://github.com/ISCOUTB/AS_202620_LostVault/issues?q=is%3Aissue) | 0 | 1 | 2 | Coincide |
| [PROYECTO_CAMPUSMARKET](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/issues?q=is%3Aissue) | 1 | 0 | 14 | Coincide |
| [PideUtb](https://github.com/ISCOUTB/AS_202620_PideUtb/issues?q=is%3Aissue) | 1 | 0 | 9 | Coincide |
| [ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/issues?q=is%3Aissue) | 0 | 0 | 2 | Coincide |
| [Recobra](https://github.com/ISCOUTB/AS_202620_Recobra/issues?q=is%3Aissue) | 0 | 0 | 0 | Coincide |
| [ShareU](https://github.com/ISCOUTB/AS_202620_ShareU/issues?q=is%3Aissue) | 10 | 10 | 0 | Coincide |
| [Sistema-de-calificacion-automatica](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/issues?q=is%3Aissue) | 0 | 0 | 0 | Coincide |
| [TAIA_-Task-Artificial-Intelligence-Assistant](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/issues?q=is%3Aissue) | 3 | 4 | 1 | Coincide |
| [TIENDA-VIRTUAL-UTB](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/issues?q=is%3Aissue) | 0 | 0 | 1 | Coincide |
| [UTB_TRACKER](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/issues?q=is%3Aissue) | 1 | 0 | 0 | Coincide |
| [Verifacts](https://github.com/ISCOUTB/AS_202620_Verifacts/issues?q=is%3Aissue) | 0 | 3 | 0 | Coincide |
| [XALD](https://github.com/ISCOUTB/AS_202620_XALD/issues?q=is%3Aissue) | 0 | 6 | 1 | Coincide |
| [mapsutb](https://github.com/ISCOUTB/AS_202620_mapsutb/issues?q=is%3Aissue) | 0 | 54 | 0 | Coincide |
| [uniTeam](https://github.com/ISCOUTB/AS_202620_uniTeam/issues?q=is%3Aissue) | 0 | 1 | 5 | Coincide |

**Total reconciliado:** 43 abiertas, 132 cerradas y 49 PR fusionadas. Los 23 proyectos coinciden con el informe histórico; no se encontró diferencia de conteos. No hay corrección histórica que aplicar.

Los motivos históricos de cierre no se reescriben usando metadata actual. Se mantienen los motivos y reservas del informe original. Esta pasada verifica estados y cantidades; no demuestra retrospectivamente el estado de un tablero ni el funcionamiento de una aplicación.
