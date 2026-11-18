# Seguimiento documental de S14 y S15 · reconstrucción al 17 de noviembre de 2026

Revisión factual retrospectiva de los **23 proyectos** del listado vigente, solicitada por el docente. **No es una evaluación académica ni un cierre de notas**: no se modifican calificaciones, matrices, planillas ni estados históricos. La [actualización y conciliación S13](actualizacion-s13-2026-11-17.md) complementa, sin sobrescribir, su informe histórico.

## Fechas y alcance

- **S13 (referencia):** hasta 1/nov/2026, 23:59:59 Colombia; límite exclusivo 2/nov a las 05:00 UTC.
- **S14:** hasta 8/nov/2026, 23:59:59 Colombia; límite exclusivo **2026-11-09T05:00:00Z**. La [ficha vigente](../../fichas/semana-14-evidencia-s14.md) trata la medición de atributos de calidad, resultados frente al umbral y documentación de la revisión de pares en arc42 §11. Aquí solo se registran artefactos y declaraciones verificables, no se asignan resultados de rúbrica.
- **S15:** seguimiento del período hasta 15/nov/2026, 23:59:59 Colombia; límite exclusivo **2026-11-16T05:00:00Z**. **No se crea una entrega oficial S15:** el [calendario vigente](../../scripts/cron/calendario.json) pasa de S14 a la entrega final S16. Su fecha es una ventana de observación, no un nuevo plazo académico.

Los snapshots se reconstruyen del historial accesible de la rama principal. Una fecha Git no demuestra por sí sola cuándo se publicó un commit: no se dispone de un archivo íntegro de movimientos de rama. Las fusiones de PR y ejecuciones CI se contrastan cuando consta su fecha. Ausencia de cambios en la rama observada no equivale a ausencia de trabajo en otras ramas, herramientas o entornos. Las pruebas o mediciones descritas son **reportes del repositorio**, salvo indicación expresa; no se ejecutó código estudiantil.

Un workflow presente no acredita una ejecución. CI, imagen publicada, despliegue y aceptación funcional son estados diferentes. Los resultados posteriores al límite no se trasladan al cierre. No se verificó retrospectivamente la operación de URLs; la comprobación viva del [17/nov](seguimiento-despliegues-2026-11-17.md) tampoco prueba su estado en semanas anteriores. Un endpoint API institucional no acredita frontend institucional, y falta de URL documentada no prueba falta de trabajo.

Se conservan las confirmaciones docentes anteriores: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. No equivalen a aceptación de cada cambio posterior ni se atribuyen automáticamente a esta ventana.

[CI por snapshot y corte](revision-ci-s14-s15.md) · [Issues y PR por corte](revision-issues-pr-s14-s15.md) · [Seguimiento actual posterior](seguimiento-2026-11-17.md).

## Evidencia por proyecto

<a id="audioshare"></a>

## AudioShare

### S14

Snapshot [7f21843741e2](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/7f21843741e25f704fbb55dfa29c77fa64ddf27f) · fecha Git 2026-11-08T21:11:09-05:00.

Incorpora documentación EC-01 con umbral de 100 ms, procedimiento de captura y distinción entre simulaciones y observaciones físicas históricas (34 y 333,5 ms de octubre); no son mediciones nuevas de noviembre ni acreditan sincronización acústica. Actualiza arc42 §11 con seguimiento que el equipo denomina revisión de pares, cuya fuente es el informe docente del 5/nov, no un acta independiente de compañeros. Añade auditoría de dependencias al workflow, campo commit en /health y prueba de salud. README documenta https://audioshare.iscoutb.dev para frontend Flutter Web y API; el propio texto distingue cambio integrado de cambio aún no desplegado.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/7f21843741e25f704fbb55dfa29c77fa64ddf27f/README.md) · [docs/evidencia-a01-ec01.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/7f21843741e25f704fbb55dfa29c77fa64ddf27f/docs/evidencia-a01-ec01.md) · [docs/arc42/src/11_risks_and_technical_debt.adoc](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/7f21843741e25f704fbb55dfa29c77fa64ddf27f/docs/arc42/src/11_risks_and_technical_debt.adoc) · [src/app.ts](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/7f21843741e25f704fbb55dfa29c77fa64ddf27f/src/app.ts).


CI/publicación del snapshot: [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42549483816): `success`, actualizado 2026-11-09T02:12:03Z; [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42549483854): `success`, actualizado 2026-11-09T02:12:44Z; [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42549483794): `success`, actualizado 2026-11-09T02:13:03Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


### S15

Snapshot [11d39721156a](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/11d39721156a247dc53fea3bcbee67674d9b6e25) · fecha Git 2026-11-10T18:38:35-05:00.

Integra código de sala de seis dígitos, caducidad, controles del emisor, salida/expulsión, eventos y posición de reproducción, con pruebas backend y Flutter. Los cuatro commits de 9–10/nov son posteriores al cierre S14 aunque sus mensajes lleven S14. README mantiene el mismo origen institucional para frontend y API.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/11d39721156a247dc53fea3bcbee67674d9b6e25/README.md) · [docs/evidencia-a01-ec01.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/11d39721156a247dc53fea3bcbee67674d9b6e25/docs/evidencia-a01-ec01.md) · [docs/arc42/src/11_risks_and_technical_debt.adoc](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/11d39721156a247dc53fea3bcbee67674d9b6e25/docs/arc42/src/11_risks_and_technical_debt.adoc) · [src/app.ts](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/11d39721156a247dc53fea3bcbee67674d9b6e25/src/app.ts).


CI/publicación del snapshot: [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42925008057): `success`, actualizado 2026-11-10T23:39:37Z; [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42925008043): `success`, actualizado 2026-11-10T23:39:45Z; [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42925007964): `success`, actualizado 2026-11-10T23:40:41Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


<a id="clubs_utb"></a>

## Clubs_UTB

### S14

Snapshot [7091ca83d59b](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7091ca83d59b3a6391fad4fabbfdbb3d07686735) · fecha Git 2026-11-08T23:10:12-05:00.

Añade docs/mediciones_calidad.md y ajusta Dockerfile. El documento describe Postman contra Dokploy y declara 20 solicitudes con promedio de 195,75 ms frente a umbral de 800 ms, junto con procedimientos de otros atributos. Es resultado declarado por el equipo; esta revisión no repite la prueba. No hay modificación de arc42 §11 en el delta S13→S14. README dice que hay dominio institucional pero no proporciona URL pública concreta.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7091ca83d59b3a6391fad4fabbfdbb3d07686735/README.md) · [docs/mediciones_calidad.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7091ca83d59b3a6391fad4fabbfdbb3d07686735/docs/mediciones_calidad.md) · [docs/arc42/11_riesgos_y_deuda_tecnica.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/7091ca83d59b3a6391fad4fabbfdbb3d07686735/docs/arc42/11_riesgos_y_deuda_tecnica.md).


CI/publicación del snapshot: [.github/workflows/contrato.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/42560311106): `failure`, actualizado 2026-11-09T04:10:25Z; [.github/workflows/backend-tests.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/42560309551): `failure`, actualizado 2026-11-09T04:10:24Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


### S15

Snapshot [af14e9281186](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/af14e9281186f8a4e749712a025b9e08f010465c) · fecha Git 2026-11-14T21:01:41-05:00.

Reescribe documentación de mediciones, arc42 y lista de errores; modifica autenticación, publicaciones, persistencia PostgreSQL, contrato OpenAPI y pruebas. README añade https://api-linkclub.iscoutb.dev, explícitamente API, y /health; no es URL de frontend. Contrato y tests pasan en el snapshot, a diferencia de los workflows fallidos del corte S14. No se convierte ese resultado en aceptación funcional.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/af14e9281186f8a4e749712a025b9e08f010465c/README.md) · [docs/mediciones_calidad.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/af14e9281186f8a4e749712a025b9e08f010465c/docs/mediciones_calidad.md) · [docs/arc42/11_riesgos_y_deuda_tecnica.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/af14e9281186f8a4e749712a025b9e08f010465c/docs/arc42/11_riesgos_y_deuda_tecnica.md).


CI/publicación del snapshot: [Backend tests](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/43667549467): `success`, actualizado 2026-11-15T02:23:53Z; [contrato](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/43667549442): `success`, actualizado 2026-11-15T02:23:44Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


<a id="dinamikutb"></a>

## DinamikUTB

### S14

Snapshot [ad917c9b9394](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/ad917c9b93940a244761b2a307d71137cdac3d1b) · fecha Git 2026-11-04T21:26:30-05:00.

Integra cambios del frontend Flutter, Dockerfiles, configuración API, workflows y Sonar. README documenta frontend externo https://iscoutb.github.io/AS_202620_DinamikUTB/ y API institucional https://api-dinamikutb.iscoutb.dev; el frontend no está documentado bajo iscoutb.dev. No aparece nuevo documento de medición S14 en el delta inspeccionado. La publicación de Pages exitosa no corrige el resultado failure de CI.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/README.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/.github/workflows/ci.yml) · [frontend/Dockerfile](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/frontend/Dockerfile).


CI/publicación del snapshot: [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41966455736): `success`, actualizado 2026-11-05T04:14:59Z; [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41956575675): `success`, actualizado 2026-11-05T02:40:43Z; [Auditoría de dependencias](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243503): `success`, actualizado 2026-11-05T02:27:03Z; [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243511): `success`, actualizado 2026-11-05T02:28:33Z; [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243457): `failure`, actualizado 2026-11-05T02:30:33Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


### S15

Snapshot [ad917c9b9394](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/ad917c9b93940a244761b2a307d71137cdac3d1b) · fecha Git 2026-11-04T21:26:30-05:00.

El snapshot de rama principal no cambia respecto de S14. No se infiere ausencia de trabajo en otras ramas o fuera del repositorio. Permanece la distinción entre API institucional y frontend GitHub Pages; ejecuciones programadas posteriores no alteran la fecha del código.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/README.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/.github/workflows/ci.yml) · [frontend/Dockerfile](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/ad917c9b93940a244761b2a307d71137cdac3d1b/frontend/Dockerfile).


CI/publicación del snapshot: [Auditoría de dependencias](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/42613636960): `success`, actualizado 2026-11-09T12:02:24Z; [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41966455736): `success`, actualizado 2026-11-05T04:14:59Z; [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41956575675): `success`, actualizado 2026-11-05T02:40:43Z; [Auditoría de dependencias](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243503): `success`, actualizado 2026-11-05T02:27:03Z; [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243511): `success`, actualizado 2026-11-05T02:28:33Z; [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243457): `failure`, actualizado 2026-11-05T02:30:33Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


<a id="drift"></a>

## Drift

### S14

Snapshot [2d86f2d4b2ac](https://github.com/ISCOUTB/AS_202620_Drift/commit/2d86f2d4b2acc41142a93cb2662f53f47cd1b653) · fecha Git 2026-11-08T23:26:32-05:00.

Integra PR #56, #60 y #61 según historial de merges. Añade scripts k6, resultados JSON y dos informes E1: cinco corridas locales con upstream simulado (p95 mediano declarado 632 ms) frente al umbral de 3000 ms, y medición del despliegue con consultas distintas (p95 declarado 9,05 s). El informe separa los entornos y no extrapola el resultado local al despliegue. Actualiza arc42 §11, ADR-0013 y registro de IA. README documenta https://drift.iscoutb.dev para frontend/backend, además de Azure API y Vercel frontend externos.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/2d86f2d4b2acc41142a93cb2662f53f47cd1b653/README.md) · [docs/evidencias/s14-medicion-e1.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/2d86f2d4b2acc41142a93cb2662f53f47cd1b653/docs/evidencias/s14-medicion-e1.md) · [docs/evidencias/s14-e1-medicion.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/2d86f2d4b2acc41142a93cb2662f53f47cd1b653/docs/evidencias/s14-e1-medicion.md) · [docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/2d86f2d4b2acc41142a93cb2662f53f47cd1b653/docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md).


CI/publicación del snapshot: [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/42561849137): `success`, actualizado 2026-11-09T04:27:55Z; [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/42561849125): `success`, actualizado 2026-11-09T04:29:00Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


### S15

Snapshot [2d86f2d4b2ac](https://github.com/ISCOUTB/AS_202620_Drift/commit/2d86f2d4b2acc41142a93cb2662f53f47cd1b653) · fecha Git 2026-11-08T23:26:32-05:00.

Sin cambio de snapshot principal durante la ventana S15. Conserva informes y datos S14, no una nueva medición semanal. Las mejoras posteriores al 15/nov no se incorporan retrospectivamente a este corte.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/2d86f2d4b2acc41142a93cb2662f53f47cd1b653/README.md) · [docs/evidencias/s14-medicion-e1.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/2d86f2d4b2acc41142a93cb2662f53f47cd1b653/docs/evidencias/s14-medicion-e1.md) · [docs/evidencias/s14-e1-medicion.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/2d86f2d4b2acc41142a93cb2662f53f47cd1b653/docs/evidencias/s14-e1-medicion.md) · [docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/2d86f2d4b2acc41142a93cb2662f53f47cd1b653/docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md).


CI/publicación del snapshot: [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/42561849137): `success`, actualizado 2026-11-09T04:27:55Z; [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/42561849125): `success`, actualizado 2026-11-09T04:29:00Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


<a id="elmapita"></a>

## ElMapita

### S14

Snapshot [899bece9b4dd](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/899bece9b4ddda9fb27381c966c0b720c93b0fee) · fecha Git 2026-11-01T23:51:18-06:00.

Integra modelado de amenazas, guardas de autorización y pruebas, auditoría de dependencias, privacidad y cambios CI. Son commits etiquetados S13 pero fechados después del cierre S13 al convertir zona UTC−6 a Colombia: 2/nov. Se atribuyen a la ventana S14, sin reescribir S13. README no documenta URL pública concreta; eso no contradice la confirmación docente de que Mapita presentó y funciona.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/899bece9b4ddda9fb27381c966c0b720c93b0fee/README.md) · [docs/seguridad/amenazas.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/899bece9b4ddda9fb27381c966c0b720c93b0fee/docs/seguridad/amenazas.md).


CI/publicación del snapshot: [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41396450324): `success`, actualizado 2026-11-02T05:53:34Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


### S15

Snapshot [7bf5bb2c120e](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/7bf5bb2c120e06c6c023d42f0dce1de7bd4ba077) · fecha Git 2026-11-09T01:46:24-06:00.

El commit del 9/nov a 01:46 UTC−6 equivale a 02:46 COT y queda después del cierre S14. Añade ATAM ligero, benchmark EC-01, ajustes offline/caché e idempotencia y pruebas. El informe del equipo aclara que el benchmark se ejecutó contra Render anterior, no Dokploy vigente; no valida el despliegue actual. README sigue sin URL institucional concreta. No se transforma la aceptación docente previa en aceptación de estos cambios.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/7bf5bb2c120e06c6c023d42f0dce1de7bd4ba077/README.md) · [docs/seguridad/amenazas.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/7bf5bb2c120e06c6c023d42f0dce1de7bd4ba077/docs/seguridad/amenazas.md) · [docs/atam/atam-ligero.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/7bf5bb2c120e06c6c023d42f0dce1de7bd4ba077/docs/atam/atam-ligero.md).


CI/publicación del snapshot: [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/42581447260): `success`, actualizado 2026-11-09T07:49:14Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


<a id="enagenda"></a>

## EnAgenda

### S14

Snapshot [a6dde3025c68](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b) · fecha Git 2026-10-25T22:57:38-05:00.

La rama master conserva el snapshot del 25/oct: no aparecen commits nuevos en primer padre respecto de S13. README describe Dokploy pero mantiene http://[host-asignado]/health y /metrics, no URL pública concreta. La falta de URL documentada no prueba que no exista trabajo o despliegue.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [docs/despliegue/medicion-dokploy.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/despliegue/medicion-dokploy.md).


CI/publicación del snapshot: [Taller mensajes y consistencia](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): `success`, actualizado 2026-10-26T03:57:50Z; [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): `failure`, actualizado 2026-10-26T03:58:08Z; [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521): `success`, actualizado 2026-10-26T03:58:27Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


### S15

Snapshot [a6dde3025c68](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b) · fecha Git 2026-10-25T22:57:38-05:00.

Continúa el mismo snapshot principal y documentación. Se conserva CI histórico fallido y workflow de Pages exitoso como resultados distintos; no son ejecuciones nuevas de S15. No se revisaron cambios no integrados en otras ramas.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) · [docs/despliegue/medicion-dokploy.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/despliegue/medicion-dokploy.md).


CI/publicación del snapshot: [Taller mensajes y consistencia](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): `success`, actualizado 2026-10-26T03:57:50Z; [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): `failure`, actualizado 2026-10-26T03:58:08Z; [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521): `success`, actualizado 2026-10-26T03:58:27Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


<a id="gimnasioutb"></a>

## GimnasioUTB

### S14

Snapshot [02ee41ef6fee](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/02ee41ef6fee89cdd624be7e2d70a86837b86c82) · fecha Git 2026-11-08T22:05:22-05:00.

El delta modifica únicamente docs/arc42/arc42_gimnasio_utb.md. Documenta contraste de mediciones: duración de suite de 111 ms no se usa como latencia del escenario, y Q3 queda sin medición de atraso. En §11.5 el propio equipo declara no disponer de fuente que permita atribuir observaciones a revisión por pares. README documenta https://gimnasio-utb.iscoutb.dev como backend API; sus verificaciones históricas son reportes del equipo.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/02ee41ef6fee89cdd624be7e2d70a86837b86c82/README.md) · [docs/arc42/arc42_gimnasio_utb.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/02ee41ef6fee89cdd624be7e2d70a86837b86c82/docs/arc42/arc42_gimnasio_utb.md).


CI/publicación del snapshot: [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/42554463034): `success`, actualizado 2026-11-09T03:06:03Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


### S15

Snapshot [9cf2b34ef0eb](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/9cf2b34ef0ebe74b649a416f68737f8a199a8e72) · fecha Git 2026-11-15T00:36:36-05:00.

Agrega estructura Android/APK, lectura QR e identidades de prueba, y modifica interfaz Flutter, API y pruebas. README conserva URL del backend institucional; no es una demostración del frontend. No se encontró run asociado al SHA final en la consulta API; no significa que no exista CI en otros commits.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/9cf2b34ef0ebe74b649a416f68737f8a199a8e72/README.md) · [docs/arc42/arc42_gimnasio_utb.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/9cf2b34ef0ebe74b649a416f68737f8a199a8e72/docs/arc42/arc42_gimnasio_utb.md).


CI/publicación del snapshot: sin ejecución asociada recuperada antes del límite. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


<a id="inventrack"></a>

## InvenTrack

### S14

Snapshot [2f338566adc3](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/2f338566adc35641e4d7cee1deb5dbc4afbb7bb8) · fecha Git 2026-11-08T22:27:36-05:00.

Actualiza experimento de 20 salidas concurrentes de inventario, umbral p95 de 400 ms y valor declarado 32,891 ms en ejecución del 6/nov. Arc42 §11 incorpora observaciones que el equipo atribuye a revisión de pares y explicita límites de persistencia, autenticación e idempotencia. README documenta API https://inventrack.iscoutb.dev y alternativa Render; advierte que redespliegue y operación pública requieren verificación externa.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/2f338566adc35641e4d7cee1deb5dbc4afbb7bb8/README.md) · [docs/retos/corte-2-experimento.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/2f338566adc35641e4d7cee1deb5dbc4afbb7bb8/docs/retos/corte-2-experimento.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/2f338566adc35641e4d7cee1deb5dbc4afbb7bb8/docs/arc42/arc42-template-EN.md).


CI/publicación del snapshot: [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/42556529986): `success`, actualizado 2026-11-09T03:28:48Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


### S15

Snapshot [b36f889aad0b](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/b36f889aad0bec880aab8a7b8298255e976c87ba) · fecha Git 2026-11-15T20:59:37-05:00.

Incorpora frontend Flutter móvil, catálogo de productos y contrato OpenAPI; agrega JSON con cinco corridas del 15/nov, p95 entre 27,729 y 33,788 ms y 100 respuestas HTTP 200 declaradas. Mantiene la cifra del 6/nov como histórico, no como serie cruda reconstruida. README sigue identificando la URL institucional como API, no frontend web desplegado.


Fuentes: [README.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/b36f889aad0bec880aab8a7b8298255e976c87ba/README.md) · [docs/retos/corte-2-experimento.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/b36f889aad0bec880aab8a7b8298255e976c87ba/docs/retos/corte-2-experimento.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/b36f889aad0bec880aab8a7b8298255e976c87ba/docs/arc42/arc42-template-EN.md).


CI/publicación del snapshot: [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/43789460138): `success`, actualizado 2026-11-16T02:00:39Z. Publicar una imagen o Pages no demuestra despliegue institucional ni aceptación funcional.


<a id="laplacita"></a>

## LaPlacita


### S14

Snapshot reconstruido: [749242f3bba7](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/749242f3bba7c9b074e28bb2139e5530e088c757), fecha Git 2026-11-06T15:24:19-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_LaPlacita/compare/eb8d3ffb5e44aa982b8279c91e68ba0bb1837884...749242f3bba7c9b074e28bb2139e5530e088c757).

Integra cambios de pedidos por tienda, cancelación y administración general; el historial de primer padre registra PR #34–#40. La evidencia S14 define ESC-01, denominadores de pedidos procesados/perdidos/duplicados y perfiles de carga, estrés y fallo de base. Conserva resultados JSON/TXT locales y mediciones de lectura/escritura en producción, distinguiendo 429 del borde y 503 de base. arc42 §11.8 registra señalamientos de revisión externa; no se convierte esa revisión en constancia de revisión auténtica de pares.


**README y URL:** Frontend/PWA: https://laplacita-app.iscoutb.dev; API: https://laplacita-test.iscoutb.dev/api/v1. Ambos documentados en README. [README del snapshot](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/749242f3bba7c9b074e28bb2139e5530e088c757/README.md).


**Fuentes estáticas:** [docs/evidencias/evidencias-s14.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/749242f3bba7c9b074e28bb2139e5530e088c757/docs/evidencias/evidencias-s14.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/749242f3bba7c9b074e28bb2139e5530e088c757/docs/arc42/arc42-template-EN.md) · [backend/scripts/medir-carga.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/749242f3bba7c9b074e28bb2139e5530e088c757/backend/scripts/medir-carga.js)


### S15

Snapshot reconstruido: [c4faebdb8298](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/c4faebdb829895f047aebade4ce24001065a6513), fecha Git 2026-11-15T12:28:01-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_LaPlacita/compare/749242f3bba7c9b074e28bb2139e5530e088c757...c4faebdb829895f047aebade4ce24001065a6513).

Integra PR #47 y #48: endurecimiento de API/documentación y revisión de arquitectura. La evidencia S14 se amplía con mediciones fechadas 10 y 15 de noviembre, incluidas ejecuciones PostgreSQL; estas ampliaciones pertenecen a S15 y no se atribuyen al cierre S14.


**README y URL:** Frontend/PWA: https://laplacita-app.iscoutb.dev; API: https://laplacita-test.iscoutb.dev/api/v1. Ambos documentados en README. [README del snapshot](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/c4faebdb829895f047aebade4ce24001065a6513/README.md).


**Fuentes estáticas:** [docs/evidencias/evidencias-s14.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/c4faebdb829895f047aebade4ce24001065a6513/docs/evidencias/evidencias-s14.md) · [backend/next.config.mjs](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/c4faebdb829895f047aebade4ce24001065a6513/backend/next.config.mjs) · [docs/c4/componentes.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/c4faebdb829895f047aebade4ce24001065a6513/docs/c4/componentes.md)


<a id="lostvault"></a>

## LostVault


### S14

Snapshot reconstruido: [f66f298434af](https://github.com/ISCOUTB/AS_202620_LostVault/commit/f66f298434af615573e92a778f88614bba53b7d3), fecha Git 2026-11-08T23:14:53-05:00, rama `main`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_LostVault/compare/58c5c9524e3d1dd51d970e36a38bab690e10470e...f66f298434af615573e92a778f88614bba53b7d3).

El historial registra integración de API/reclamaciones (PR #25) y medición de atributos (PR #26). La evidencia mide búsqueda GET /objects con umbral p95 de 2.000 ms bajo 200 concurrentes. El equipo reporta 1.867 ms en estado estable y 2.279 ms en primera ráfaga, y diferencia tiempo de navegador/servidor. Conserva resultados crudos y scripts; el entorno declarado es la API externa Vercel, no un subdominio institucional. arc42 §11 añade la reserva de escalado y medición. No se infiere aprobación funcional a partir de esos resultados declarados.


**README y URL:** README raíz sin URL de despliegue concreta. La evidencia S14 identifica https://backend-nu-self-91.vercel.app como API externa; no acredita frontend ni iscoutb.dev. [README del snapshot](https://github.com/ISCOUTB/AS_202620_LostVault/blob/f66f298434af615573e92a778f88614bba53b7d3/README.md).


**Fuentes estáticas:** [docs/medicion/s14-medicion-atributos.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/f66f298434af615573e92a778f88614bba53b7d3/docs/medicion/s14-medicion-atributos.md) · [docs/medicion/s14-resultados-crudos.json](https://github.com/ISCOUTB/AS_202620_LostVault/blob/f66f298434af615573e92a778f88614bba53b7d3/docs/medicion/s14-resultados-crudos.json) · [docs/arc42/11_riesgos.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/f66f298434af615573e92a778f88614bba53b7d3/docs/arc42/11_riesgos.md)


### S15

Snapshot reconstruido: [f66f298434af](https://github.com/ISCOUTB/AS_202620_LostVault/commit/f66f298434af615573e92a778f88614bba53b7d3), fecha Git 2026-11-08T23:14:53-05:00, rama `main`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_LostVault/compare/f66f298434af615573e92a778f88614bba53b7d3...f66f298434af615573e92a778f88614bba53b7d3).

No se observa nuevo commit en la cadena principal entre ambos cortes; se conserva el snapshot S14. Esto describe historia Git, no ausencia de trabajo fuera del repositorio.


**README y URL:** README raíz sin URL de despliegue concreta. La evidencia S14 identifica https://backend-nu-self-91.vercel.app como API externa; no acredita frontend ni iscoutb.dev. [README del snapshot](https://github.com/ISCOUTB/AS_202620_LostVault/blob/f66f298434af615573e92a778f88614bba53b7d3/README.md).


**Fuentes estáticas:** [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/f66f298434af615573e92a778f88614bba53b7d3/README.md)


<a id="proyecto_campusmarket"></a>

## PROYECTO_CAMPUSMARKET


### S14

Snapshot reconstruido: [2d2848922db7](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/2d2848922db799389ffdcf0db4ef50437cd27ef2), fecha Git 2026-11-05T19:38:56-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/compare/f6a90d2094d90cd34c81e6e857bcb6c53e3c567e...2d2848922db799389ffdcf0db4ef50437cd27ef2).

Integra catálogo por universidad, favoritos, mensajería y documentación/publicación del incremento 2 (historial PR #81–#91). La evidencia S14 EC-01 preserva el umbral de nueve de diez búsquedas mostradas en dos segundos y distingue medición HTTP de resultado visible. Documenta imagen ensayada, datos JSON y validaciones; no se equipara su auto-reporte con verificación independiente ni con aceptación funcional. La revisión auténtica de pares permanece diferenciada de la preparación técnica/documental.


**README y URL:** README documenta interfaz https://campusmarket.iscoutb.dev/app/ y API/Swagger en https://campusmarket.iscoutb.dev/docs; ambas comparten host institucional. [README del snapshot](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/2d2848922db799389ffdcf0db4ef50437cd27ef2/README.md).


**Fuentes estáticas:** [docs/evidencias/evidencia-s14-ec01-2026-11-05.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/2d2848922db799389ffdcf0db4ef50437cd27ef2/docs/evidencias/evidencia-s14-ec01-2026-11-05.md) · [docs/evidencias/datos/ec01-s14-2026-11-05.json](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/2d2848922db799389ffdcf0db4ef50437cd27ef2/docs/evidencias/datos/ec01-s14-2026-11-05.json) · [docs/arc42/11-riesgos-y-deuda-tecnica.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/2d2848922db799389ffdcf0db4ef50437cd27ef2/docs/arc42/11-riesgos-y-deuda-tecnica.md)


### S15

Snapshot reconstruido: [c79c73d47936](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/c79c73d47936790b0f248bdea5c0a700ce8fe017), fecha Git 2026-11-09T01:27:11-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/compare/2d2848922db799389ffdcf0db4ef50437cd27ef2...c79c73d47936790b0f248bdea5c0a700ce8fe017).

El PR #93 figura integrado el 9 de noviembre a las 01:27 COT, después del cierre S14. Actualiza auditoría documental S1–S14, README, arc42, C4 y workflows; por tanto se registra en S15 aunque el documento mencione S14. No cambia retrospectivamente el snapshot del 8 de noviembre.


**README y URL:** README documenta interfaz https://campusmarket.iscoutb.dev/app/ y API/Swagger en https://campusmarket.iscoutb.dev/docs; ambas comparten host institucional. [README del snapshot](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/README.md).


**Fuentes estáticas:** [README.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/README.md) · [docs/arc42/ARC42.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/arc42/ARC42.md)


<a id="pideutb"></a>

## PideUtb


### S14

Snapshot reconstruido: [602b55fbfe97](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/602b55fbfe97a24f7ebe247cacbbccc50e560684), fecha Git 2026-11-07T17:57:20-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_PideUtb/compare/e81e272b20498968b1016a261dee8bce250422da...602b55fbfe97a24f7ebe247cacbbccc50e560684).

El historial registra PR #39–#43: fotografías de carta, ajustes de pantalla, documentación del costo de separar módulos, corrección de retroceso de estados y sugeridos/recogida/aviso/comprobante. El archivo evidencia-s14.md ya declara fecha 18 de octubre: no se presenta como medición nueva de noviembre. Describe ESC-03, tiempo de sondeo/red/servidor, cambio de sondeo de 8 a 5 segundos y reserva para reacción humana; el cumplimiento del flujo completo depende de esa reacción. arc42 mantiene riesgos y deuda separados del cambio implementado.


**README y URL:** README documenta frontend https://pideutb.iscoutb.dev y API https://api-pideutb.iscoutb.dev/docs, con health y métricas separados. [README del snapshot](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/602b55fbfe97a24f7ebe247cacbbccc50e560684/README.md).


**Fuentes estáticas:** [docs/evidencia-s14.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/602b55fbfe97a24f7ebe247cacbbccc50e560684/docs/evidencia-s14.md) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/602b55fbfe97a24f7ebe247cacbbccc50e560684/docs/arc42/arc42.md) · [backend/app/pedidos/service.py](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/602b55fbfe97a24f7ebe247cacbbccc50e560684/backend/app/pedidos/service.py)


### S15

Snapshot reconstruido: [602b55fbfe97](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/602b55fbfe97a24f7ebe247cacbbccc50e560684), fecha Git 2026-11-07T17:57:20-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_PideUtb/compare/602b55fbfe97a24f7ebe247cacbbccc50e560684...602b55fbfe97a24f7ebe247cacbbccc50e560684).

No se observa nuevo commit en la cadena principal entre ambos cortes; se conserva el snapshot S14. La confirmación docente de presentación y despliegues se mantiene, sin extenderla automáticamente a todos los cambios nuevos.


**README y URL:** README documenta frontend https://pideutb.iscoutb.dev y API https://api-pideutb.iscoutb.dev/docs, con health y métricas separados. [README del snapshot](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/602b55fbfe97a24f7ebe247cacbbccc50e560684/README.md).


**Fuentes estáticas:** [README.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/602b55fbfe97a24f7ebe247cacbbccc50e560684/README.md)


<a id="routb"></a>

## ROUTB


### S14

Snapshot reconstruido: [cad53b1b2054](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/cad53b1b2054f30fa8dc6527fdee44ead440aff1), fecha Git 2026-11-08T23:52:54-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_ROUTB/compare/5f13a93fb2edf5977c582662537f2af32bd1a4d2...cad53b1b2054f30fa8dc6527fdee44ead440aff1).

Integra cambios visuales y evidencia de medición S14. El equipo documenta tres rondas de 100 peticiones secuenciales contra GET /trips/ y umbral p95 de 3,99 s. Declara p95 máximo de 631,76 ms en Dokploy con respuesta vacía y 2.564,52 ms en local con cinco viajes y PostgreSQL de pruebas. Son entornos y cargas distintos, no una prueba de concurrencia. arc42 §11.4 distingue señalamientos externos de ausencia de comentarios formales de pares al cierre.


**README y URL:** README documenta https://routb.iscoutb.dev como base API y /health. No se presenta como frontend Flutter web. Se conserva la confirmación docente de entrega de avance. [README del snapshot](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/cad53b1b2054f30fa8dc6527fdee44ead440aff1/README.md).


**Fuentes estáticas:** [docs/evidencia/SEMANA14.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/cad53b1b2054f30fa8dc6527fdee44ead440aff1/docs/evidencia/SEMANA14.md) · [docs/evidencia/medicion-semana14.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/cad53b1b2054f30fa8dc6527fdee44ead440aff1/docs/evidencia/medicion-semana14.md) · [docs/arc42/11_riesgos_y_deuda_tecnica.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/cad53b1b2054f30fa8dc6527fdee44ead440aff1/docs/arc42/11_riesgos_y_deuda_tecnica.md)


### S15

Snapshot reconstruido: [e6fe8c818238](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6), fecha Git 2026-11-14T21:45:16-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_ROUTB/compare/cad53b1b2054f30fa8dc6527fdee44ead440aff1...e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6).

Los commits de 13–14 de noviembre incorporan cambios de cuentas/perfil/teléfono/vehículo, rutas/paradas, salida/cancelación de viajes, notificaciones y pruebas; aparecen ADR 24–28 y migraciones. Son avances posteriores, no evidencia del cierre S14. El README conserva la configuración de despliegue desde rama Changes; la presencia del código en principal no demuestra qué revisión estaba desplegada.


**README y URL:** README documenta https://routb.iscoutb.dev como base API y /health. No se presenta como frontend Flutter web. Se conserva la confirmación docente de entrega de avance. [README del snapshot](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6/README.md).


**Fuentes estáticas:** [docs/evidencia/CHANGELOG-api.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6/docs/evidencia/CHANGELOG-api.md) · [backend/tests/test_trips_flow.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6/backend/tests/test_trips_flow.py) · [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6/README.md)


<a id="recobra"></a>

## Recobra


### S14

Snapshot reconstruido: [7142bb96d8c2](https://github.com/ISCOUTB/AS_202620_Recobra/commit/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b), fecha Git 2026-11-08T16:55:27-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_Recobra/compare/0dda9abd2c76ef9b10724221225c0ed228197c39...7142bb96d8c253b1a71ba1ec72aebb3597d9b29b).

Añade medición S14 y arc42 §11.4 con señalamientos de revisión externa. El equipo declara medición de búsqueda en producción el 8 de noviembre, con 20/50/100/200 conexiones, pero solo dos publicaciones existentes y filtro que devuelve una lista vacía. Usa p97,5 como cota del p95; identifica explícitamente la revisión desplegada como inferida del HEAD y no confirmada en panel. Se mantienen esas reservas: no es evidencia independiente de versión publicada ni de carga con un catálogo representativo.


**README y URL:** README diferencia vitrina https://recobra.iscoutb.dev/, Flutter web /app/ y rutas API /publicaciones, /health y /metrics en el mismo host. [README del snapshot](https://github.com/ISCOUTB/AS_202620_Recobra/blob/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b/README.md).


**Fuentes estáticas:** [docs/medicion-s14.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b/docs/medicion-s14.md) · [docs/evidencia/medicion-s14-dokploy.json](https://github.com/ISCOUTB/AS_202620_Recobra/blob/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b/docs/evidencia/medicion-s14-dokploy.json) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b/docs/arc42/arc42.md)


### S15

Snapshot reconstruido: [7142bb96d8c2](https://github.com/ISCOUTB/AS_202620_Recobra/commit/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b), fecha Git 2026-11-08T16:55:27-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_Recobra/compare/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b...7142bb96d8c253b1a71ba1ec72aebb3597d9b29b).

No se observa nuevo commit en la cadena principal entre cortes; permanece el snapshot S14. Se conserva la presentación confirmada por el docente, sin inferir nueva aceptación funcional.


**README y URL:** README diferencia vitrina https://recobra.iscoutb.dev/, Flutter web /app/ y rutas API /publicaciones, /health y /metrics en el mismo host. [README del snapshot](https://github.com/ISCOUTB/AS_202620_Recobra/blob/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b/README.md).


**Fuentes estáticas:** [README.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b/README.md)


<a id="shareu"></a>

## ShareU


### S14

Snapshot reconstruido: [20aeb0b77409](https://github.com/ISCOUTB/AS_202620_ShareU/commit/20aeb0b77409ca8d98341e9a94fef73b31ad7073), fecha Git 2026-11-03T19:20:52-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_ShareU/compare/2c0ca6f50285cc803bb344e748a3121cf99d3767...20aeb0b77409ca8d98341e9a94fef73b31ad7073).

Añade un sitio descomprimido con páginas, integración Firebase y API, además de Dockerfiles y compose bajo Dockploy. Se constata código añadido; no se equipara la ausencia de una medición S14 identificada con ausencia de desarrollo. En el delta revisado no aparece documento específico de medición S14 con escenario/umbral y resultados ni incorporación explícita de revisión de pares a arc42 §11.


**README y URL:** README raíz documenta direcciones localhost/127.0.0.1 para desarrollo, pero no URL pública concreta ni subdominio iscoutb.dev. [README del snapshot](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/README.md).


**Fuentes estáticas:** [Dockploy/compose.lab.yml](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/Dockploy/compose.lab.yml) · [shareuwensite-main/README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/shareuwensite-main/README.md) · [shareuwensite-main/api/main.py](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/shareuwensite-main/api/main.py)


### S15

Snapshot reconstruido: [20aeb0b77409](https://github.com/ISCOUTB/AS_202620_ShareU/commit/20aeb0b77409ca8d98341e9a94fef73b31ad7073), fecha Git 2026-11-03T19:20:52-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_ShareU/compare/20aeb0b77409ca8d98341e9a94fef73b31ad7073...20aeb0b77409ca8d98341e9a94fef73b31ad7073).

No se observa nuevo commit en la cadena principal entre cortes; permanece el snapshot S14. No se infiere estado de despliegue desde los Dockerfiles.


**README y URL:** README raíz documenta direcciones localhost/127.0.0.1 para desarrollo, pero no URL pública concreta ni subdominio iscoutb.dev. [README del snapshot](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/README.md).


**Fuentes estáticas:** [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/20aeb0b77409ca8d98341e9a94fef73b31ad7073/README.md)


<a id="sistema-de-calificacion-automatica"></a>

## Sistema-de-calificacion-automatica


### S14

Snapshot reconstruido: [b3d7699fb085](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/b3d7699fb08524de28e8cee8dfde2610cbbf1182), fecha Git 2026-11-08T23:21:01-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/compare/f4548a92bf7ab5f633d8e1fa52eb5ddaaa8a9ebc...b3d7699fb08524de28e8cee8dfde2610cbbf1182).

Integra lectura OMR, cálculo de resultados, revisión manual, endpoints y frontend, además de pruebas y evidencia S14. El documento de medición EC-01–EC-04 registra tres repeticiones: las entradas de lectura son sintéticas; EC-03 y EC-04 se miden localmente, no en el despliegue. Distingue tiempo de procesamiento de CPU/memoria del servidor no medidas. arc42 §11 registra que no hubo revisión de pares; no se transforma una revisión externa en una revisión de pares realizada.


**README y URL:** README documenta frontend https://calificacion.iscoutb.dev y API https://api-calificacion.iscoutb.dev, diferenciando health y revision.txt. La afirmación de despliegue del equipo no equivale a prueba funcional retrospectiva. [README del snapshot](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/b3d7699fb08524de28e8cee8dfde2610cbbf1182/README.md).


**Fuentes estáticas:** [docs/evidencia/medicion-s14.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/b3d7699fb08524de28e8cee8dfde2610cbbf1182/docs/evidencia/medicion-s14.md) · [docs/arc42/arc42-template-ES.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/b3d7699fb08524de28e8cee8dfde2610cbbf1182/docs/arc42/arc42-template-ES.md) · [backend/worker/main.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/b3d7699fb08524de28e8cee8dfde2610cbbf1182/backend/worker/main.py)


### S15

Snapshot reconstruido: [201864022a37](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/201864022a378b1d98c53bca62017e4fa47cb7dc), fecha Git 2026-11-13T16:50:14-05:00, rama `master`. [Comparación con corte anterior](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/compare/b3d7699fb08524de28e8cee8dfde2610cbbf1182...201864022a378b1d98c53bca62017e4fa47cb7dc).

Los commits del 13 de noviembre acotan rutas y URL admitidas por herramientas de medición, agregan pruebas y corrigen una comparación en OMR. También ajustan scripts de repetición S14: son correcciones posteriores al corte y se registran en S15, sin reatribuirlas a la entrega anterior.


**README y URL:** README documenta frontend https://calificacion.iscoutb.dev y API https://api-calificacion.iscoutb.dev, diferenciando health y revision.txt. La afirmación de despliegue del equipo no equivale a prueba funcional retrospectiva. [README del snapshot](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/201864022a378b1d98c53bca62017e4fa47cb7dc/README.md).


**Fuentes estáticas:** [backend/herramientas/rutas.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/201864022a378b1d98c53bca62017e4fa47cb7dc/backend/herramientas/rutas.py) · [backend/tests/test_rutas_de_las_herramientas.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/201864022a378b1d98c53bca62017e4fa47cb7dc/backend/tests/test_rutas_de_las_herramientas.py) · [docs/evidencia/medicion-s14/repetir-local.sh](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/201864022a378b1d98c53bca62017e4fa47cb7dc/docs/evidencia/medicion-s14/repetir-local.sh)


<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA_-Task-Artificial-Intelligence-Assistant

### S14

Snapshot: [7342f349752af2b26f1d9df7e313fbcc1b9656d4](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/7342f349752af2b26f1d9df7e313fbcc1b9656d4).

Añade documentación de medición S1 (extracción y registro) y S3 (latencia) en `docs/evidencia_s14.md`, apoyada en el arnés y resultados de `docs/evaluacion_ia/`. El documento describe una corrida por configuración y diferencia extracción de persistencia, y latencia del modelo de la ruta desplegada completa. Son resultados declarados por el equipo, no repetidos en esta revisión. El merge local de S14 incorpora por segundo padre el consentimiento, migración 0005 y política de privacidad que el informe S13 ya había documentado en `44e1cc0`; no se contabilizan como avance nuevo S14. El historial actual de primer padre por sí solo no reconstruye esa publicación previa. La nota sobre ausencia de revisión entre pares es una afirmación del equipo, no una confirmación docente; no se adopta como exención.

**README/URL:** API institucional `https://taia-sistema.iscoutb.dev`, con `/health`, `/metrics` y `/docs`; la URL API no acredita frontend web.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/7342f349752af2b26f1d9df7e313fbcc1b9656d4/README.md) · [docs/evaluacion_ia/contraste_umbrales.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/7342f349752af2b26f1d9df7e313fbcc1b9656d4/docs/evaluacion_ia/contraste_umbrales.md) · [docs/arc42/11-riesgos-y-deudas-tecnicas.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/7342f349752af2b26f1d9df7e313fbcc1b9656d4/docs/arc42/11-riesgos-y-deudas-tecnicas.md)

### S15

Snapshot principal: [7342f349752af2b26f1d9df7e313fbcc1b9656d4](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/7342f349752af2b26f1d9df7e313fbcc1b9656d4).

Sin delta en main. Se observa código de pantallas de bienvenida, registro, acceso, tareas, calendario y perfil en la rama `val`, commit [5ed1975](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/5ed1975) con fecha Git 15/nov; no está integrado en main ni se atribuye despliegue o aceptación. Fecha Git no prueba fecha de push.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/7342f349752af2b26f1d9df7e313fbcc1b9656d4/README.md) · [Comparación S14→S15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/compare/7342f349752af2b26f1d9df7e313fbcc1b9656d4...7342f349752af2b26f1d9df7e313fbcc1b9656d4)

<a id="tienda-virtual-utb"></a>

## TIENDA-VIRTUAL-UTB

### S14

Snapshot: [28c688e65adfb9f49ac9602b538d1f6d365b395c](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/28c688e65adfb9f49ac9602b538d1f6d365b395c).

Incorpora `docs/medicion-escenario-4.md`: seis corridas declaradas de cinco usuarios concurrentes sobre catálogo e inventario, API local con PostgreSQL 17 y RLS; el reporte distingue ese entorno de Dokploy, red real y frontend. Añade `docs/arc42/11-riesgos-y-deuda-tecnica.md` con límites y estados de riesgos y `docs/revision-pares.md`. El documento de medición indica que los comentarios de otros equipos siguen pendientes de recibir; no se confunde autoanálisis con recepción confirmada de pares. El historial contiene merges de PR #14 y #15.

**README/URL:** Aplicación documentada bajo `https://tiendautb-sistema-n0ojjk-fde272-144-24-4-187.sslip.io/`, dominio externo, no subdominio iscoutb.dev.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/28c688e65adfb9f49ac9602b538d1f6d365b395c/README.md) · [docs/medicion-escenario-4.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/28c688e65adfb9f49ac9602b538d1f6d365b395c/docs/medicion-escenario-4.md) · [docs/arc42/11-riesgos-y-deuda-tecnica.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/28c688e65adfb9f49ac9602b538d1f6d365b395c/docs/arc42/11-riesgos-y-deuda-tecnica.md)

### S15

Snapshot: [28c688e65adfb9f49ac9602b538d1f6d365b395c](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/28c688e65adfb9f49ac9602b538d1f6d365b395c).

Mismo snapshot que S14: sin delta de código o documentación en el recorrido de la rama principal durante esta ventana; no se infiere ausencia de trabajo en otras ramas o medios.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/28c688e65adfb9f49ac9602b538d1f6d365b395c/README.md) · [Comparación S14→S15](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/compare/28c688e65adfb9f49ac9602b538d1f6d365b395c...28c688e65adfb9f49ac9602b538d1f6d365b395c)

<a id="utb_tracker"></a>

## UTB_TRACKER

### S14

Snapshot: [60570b9dc2f25b8135e6dc90fcb809f47477eba2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/60570b9dc2f25b8135e6dc90fcb809f47477eba2).

Incorpora medición QS-03/QS-02 en `docs/calidad/medicion-qs03.md`, con scripts de siembra y carga, 50/150/300 usuarios y dos corridas por nivel declaradas sobre PostgreSQL 18.1 local y Uvicorn en loopback. No equivale a medición de interacción del cliente móvil ni de red de producción. El delta incluye notificaciones Firebase, controles backend, documentación de amenazas/privacidad y cambios arc42. El historial registra merges PR #5–#9; SonarCloud autenticado se retiró del workflow el 6 de noviembre, por lo que no se infiere análisis Sonar a partir de un CI verde.

**README/URL:** README apunta a API/Swagger y salud en `https://129-80-171-141.nip.io`; no documenta URL concreta institucional ni frontend web.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/60570b9dc2f25b8135e6dc90fcb809f47477eba2/README.md) · [docs/calidad/medicion-qs03.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/60570b9dc2f25b8135e6dc90fcb809f47477eba2/docs/calidad/medicion-qs03.md) · [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/60570b9dc2f25b8135e6dc90fcb809f47477eba2/docs/arc42/arc42.md)

### S15

Snapshot: [f6b1e672f506622f9c2d83f0f48802ab620f77e0](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/f6b1e672f506622f9c2d83f0f48802ab620f77e0).

Integra roles/permisos, autenticación por correo, perfil, auditoría, salones y nuevas pruebas; merges PR #14 y #15 constan en el historial. Restaura Sonar en el workflow, pero el paso de análisis tiene `continue-on-error: true`: el resultado global no demuestra Quality Gate aprobado. El job de despliegue depende de pruebas y consulta `/salud`; su existencia no prueba ejecución ni aceptación funcional. README continúa usando nip.io y solo menciona iscoutb.dev genéricamente, sin subdominio concreto.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/f6b1e672f506622f9c2d83f0f48802ab620f77e0/README.md) · [Comparación S14→S15](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/compare/60570b9dc2f25b8135e6dc90fcb809f47477eba2...f6b1e672f506622f9c2d83f0f48802ab620f77e0)

<a id="verifacts"></a>

## Verifacts

### S14

Snapshot: [2753a4ffe07288cabb7c636e5ae65daf481ce2c2](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/2753a4ffe07288cabb7c636e5ae65daf481ce2c2).

Añade entrega de medición Q-01/Q-05 y apartado de riesgos/revisión de pares en arc42 §11. El documento compara resultados declarados locales, Render y Dokploy; describe carga secuencial y distingue arranque frío/caliente. La medición Dokploy y las observaciones de pares son reportes del equipo, no ensayos ni recepción de pares verificados independientemente aquí. README incorpora dominio institucional y diferencia interfaz web, health, Swagger, métricas y POST de análisis.

**README/URL:** Interfaz `https://verifacts.iscoutb.dev`; endpoints API `/analysis`, `/health`, `/docs` y `/metrics` diferenciados.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/2753a4ffe07288cabb7c636e5ae65daf481ce2c2/README.md) · [docs/entregas/entrega-medicion-escenario-revision-pares.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/2753a4ffe07288cabb7c636e5ae65daf481ce2c2/docs/entregas/entrega-medicion-escenario-revision-pares.md) · [docs/arc42/11-riesgos-y-deuda-tecnica.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/2753a4ffe07288cabb7c636e5ae65daf481ce2c2/docs/arc42/11-riesgos-y-deuda-tecnica.md)

### S15

Snapshot: [035383e19e44ef26cefabfab7d71e30f37f0beed](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/035383e19e44ef26cefabfab7d71e30f37f0beed).

Único delta observado: cambio de formato en el enlace de `/analysis` del README el 9 de noviembre. No se infiere nuevo comportamiento del producto ni nuevo despliegue a partir de ese cambio.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/035383e19e44ef26cefabfab7d71e30f37f0beed/README.md) · [Comparación S14→S15](https://github.com/ISCOUTB/AS_202620_Verifacts/compare/2753a4ffe07288cabb7c636e5ae65daf481ce2c2...035383e19e44ef26cefabfab7d71e30f37f0beed)

<a id="xald"></a>

## XALD

### S14

Snapshot: [7aac07e5b2bfd1e96a7127d012f1c33ff9958a78](https://github.com/ISCOUTB/AS_202620_XALD/commit/7aac07e5b2bfd1e96a7127d012f1c33ff9958a78).

Añade `docs/medicion-esc05.md` y referencias en arc42 §10/§11: procedimiento de 30 transacciones en conflicto, LWW, tres repeticiones remotas propuestas y prueba local. En el snapshot las filas de resultados y la conclusión mantienen marcadores `___`; por ello el archivo acredita documentación del procedimiento, no cifras de ejecución completadas. Declara simulación secuencial con un cliente HTTP, no dos dispositivos ni validación de la cola Android; separa estado en memoria de persistencia.

**README/URL:** API externa `https://xald-backend.onrender.com`, con health, métricas y docs; no URL institucional documentada.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/7aac07e5b2bfd1e96a7127d012f1c33ff9958a78/README.md) · [docs/medicion-esc05.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/7aac07e5b2bfd1e96a7127d012f1c33ff9958a78/docs/medicion-esc05.md) · [docs/arc42/11-Risks and Technical Debts.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/7aac07e5b2bfd1e96a7127d012f1c33ff9958a78/docs/arc42/11-Risks%20and%20Technical%20Debts.md)

### S15

Snapshot: [7aac07e5b2bfd1e96a7127d012f1c33ff9958a78](https://github.com/ISCOUTB/AS_202620_XALD/commit/7aac07e5b2bfd1e96a7127d012f1c33ff9958a78).

Mismo snapshot que S14: sin delta de código o documentación en el recorrido de la rama principal durante esta ventana; no se infiere ausencia de trabajo en otras ramas o medios.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/7aac07e5b2bfd1e96a7127d012f1c33ff9958a78/README.md) · [Comparación S14→S15](https://github.com/ISCOUTB/AS_202620_XALD/compare/7aac07e5b2bfd1e96a7127d012f1c33ff9958a78...7aac07e5b2bfd1e96a7127d012f1c33ff9958a78)

<a id="mapsutb"></a>

## mapsutb

### S14

Snapshot: [03e331d4436039869e27ce2dc1adda2d520fa833](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833).

El snapshot de rama principal coincide con S13 y data del 25 de octubre. No aparecen nuevos cambios en esta rama durante S14. Esto no demuestra ausencia de trabajo fuera de ella. La documentación y medición etiquetadas S14 que llegan el 11 de noviembre se consignan como evidencia posterior, no se retrotraen al cierre.

**README/URL:** Frontend externo `https://mapsutb.web.app/`, health estático `/health.json`; la URL de métricas apunta a la rama `metricas`, no a una API del producto.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/README.md) · [docs/arc42/11_technical_risks.adoc](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/03e331d4436039869e27ce2dc1adda2d520fa833/docs/arc42/11_technical_risks.adoc)

### S15

Snapshot: [78a8a545053237a58410e28d6f0002629c527e63](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/78a8a545053237a58410e28d6f0002629c527e63).

El 11 de noviembre incorpora documentación S12/S13/S14, protocolo AsyncAPI y prototipo aislado de cola, modelo de amenazas/privacidad, seguridad CI y análisis de disponibilidad. `docs/evidencia-s14.md` declara expresamente entrega posterior al cierre S14. Publica muestras, scripts y resumen de seis ventanas de siete días y 60 pares de peticiones de cliente; los resultados son declarados y respaldados por artefactos, no reproducidos aquí. Señala huecos de muestreo y diferencia sondeo horario de disponibilidad continua; arc42 §11 incluye observaciones y estados de pares. Todo esto se registra en S15 sin trasladarlo retrospectivamente a S14.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/78a8a545053237a58410e28d6f0002629c527e63/README.md) · [Comparación S14→S15](https://github.com/ISCOUTB/AS_202620_mapsutb/compare/03e331d4436039869e27ce2dc1adda2d520fa833...78a8a545053237a58410e28d6f0002629c527e63)

Evidencia posterior específica: [docs/evidencia-s14.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/78a8a545053237a58410e28d6f0002629c527e63/docs/evidencia-s14.md) · [docs/arc42/11_technical_risks.adoc](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/78a8a545053237a58410e28d6f0002629c527e63/docs/arc42/11_technical_risks.adoc)

<a id="uniteam"></a>

## uniTeam

### S14

Snapshot: [5e18bc227e0aae35a3f3d797a8405d108a789ef7](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/5e18bc227e0aae35a3f3d797a8405d108a789ef7).

Dos merges registrados el 2 de noviembre (PR #26 y #27) modifican únicamente `.github/workflows/seguridad.yml` frente al snapshot S13. El workflow configura pip-audit y npm audit, con instalación npm `--ignore-scripts`; configuración no acredita ejecución exitosa ni despliegue. No hay nuevo archivo de medición o modificación de arc42 §11 en este delta de rama principal.

**README/URL:** Frontend `https://uniteam-web.duckdns.org` y API `https://uniteam-api.duckdns.org` diferenciados; ambos externos, no iscoutb.dev.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/5e18bc227e0aae35a3f3d797a8405d108a789ef7/README.md) · [.github/workflows/seguridad.yml](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/5e18bc227e0aae35a3f3d797a8405d108a789ef7/.github/workflows/seguridad.yml) · [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/5e18bc227e0aae35a3f3d797a8405d108a789ef7/README.md)

### S15

Snapshot: [5e18bc227e0aae35a3f3d797a8405d108a789ef7](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/5e18bc227e0aae35a3f3d797a8405d108a789ef7).

Mismo snapshot que S14: sin delta de código o documentación en el recorrido de la rama principal durante esta ventana; no se infiere ausencia de trabajo en otras ramas o medios.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/5e18bc227e0aae35a3f3d797a8405d108a789ef7/README.md) · [Comparación S14→S15](https://github.com/ISCOUTB/AS_202620_uniTeam/compare/5e18bc227e0aae35a3f3d797a8405d108a789ef7...5e18bc227e0aae35a3f3d797a8405d108a789ef7)
