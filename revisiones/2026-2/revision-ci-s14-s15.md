# CI por snapshot · cortes S14 y seguimiento S15

Consulta 18/nov/2026 UTC. Para cada SHA reconstruido se consulta GitHub Actions y se muestra la última ejecución por nombre cuyo estado es `completed` y cuyo `updated_at` es anterior al límite exclusivo (S14: 9/nov 05:00 UTC; S15: 16/nov 05:00 UTC). No se atribuyen al corte resultados terminados después. `updated_at` es un límite conservador; no se reconstruyó cada intento de una ejecución reintentada. La ausencia de un run recuperado no equivale a fallo ni prueba ausencia de todo CI externo. Los estados de commit de otros proveedores no fueron reconstituidos.

Los runs se separan por su nombre: pruebas/construcción, publicación de imagen o Pages y comprobación de disponibilidad son funciones diferentes. `success` no implica aceptación funcional; un workflow puede tolerar u omitir un control, como se precisa en el [informe de evidencia](revision-semanas-14-15-2026-11-17.md). Una sonda posterior al despliegue no acredita todos los recorridos de la aplicación. No se ejecutó código estudiantil.

## AudioShare

### S14

Snapshot [7f21843741e2](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/7f21843741e25f704fbb55dfa29c77fa64ddf27f).

- [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42549483816): `success`; creado 2026-11-09T02:10:55Z; última actualización 2026-11-09T02:12:03Z.
- [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42549483854): `success`; creado 2026-11-09T02:10:55Z; última actualización 2026-11-09T02:12:44Z.
- [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42549483794): `success`; creado 2026-11-09T02:10:55Z; última actualización 2026-11-09T02:13:03Z.

### S15

Snapshot [11d39721156a](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/11d39721156a247dc53fea3bcbee67674d9b6e25).

- [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42925008057): `success`; creado 2026-11-10T23:38:21Z; última actualización 2026-11-10T23:39:37Z.
- [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42925008043): `success`; creado 2026-11-10T23:38:21Z; última actualización 2026-11-10T23:39:45Z.
- [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/42925007964): `success`; creado 2026-11-10T23:38:21Z; última actualización 2026-11-10T23:40:41Z.

## Clubs_UTB

### S14

Snapshot [7091ca83d59b](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/7091ca83d59b3a6391fad4fabbfdbb3d07686735).

- [.github/workflows/backend-tests.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/42560309551): `failure`; creado 2026-11-09T04:10:24Z; última actualización 2026-11-09T04:10:24Z.
- [.github/workflows/contrato.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/42560311106): `failure`; creado 2026-11-09T04:10:25Z; última actualización 2026-11-09T04:10:25Z.

### S15

Snapshot [af14e9281186](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/af14e9281186f8a4e749712a025b9e08f010465c).

- [contrato](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/43667549442): `success`; creado 2026-11-15T02:23:22Z; última actualización 2026-11-15T02:23:44Z.
- [Backend tests](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/43667549467): `success`; creado 2026-11-15T02:23:22Z; última actualización 2026-11-15T02:23:53Z.

## DinamikUTB

### S14

Snapshot [ad917c9b9394](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/ad917c9b93940a244761b2a307d71137cdac3d1b).

- [Auditoría de dependencias](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243503): `success`; creado 2026-11-05T02:26:44Z; última actualización 2026-11-05T02:27:03Z.
- [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41966455736): `success`; creado 2026-11-05T04:13:26Z; última actualización 2026-11-05T04:14:59Z.
- [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243457): `failure`; creado 2026-11-05T02:26:44Z; última actualización 2026-11-05T02:30:33Z.

### S15

Snapshot [ad917c9b9394](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/ad917c9b93940a244761b2a307d71137cdac3d1b).

- [Auditoría de dependencias](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/42613636960): `success`; creado 2026-11-09T12:01:54Z; última actualización 2026-11-09T12:02:24Z.
- [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41966455736): `success`; creado 2026-11-05T04:13:26Z; última actualización 2026-11-05T04:14:59Z.
- [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/41955243457): `failure`; creado 2026-11-05T02:26:44Z; última actualización 2026-11-05T02:30:33Z.
- [github_actions in /. - Update #1689965470](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/42607755126): `success`; creado 2026-11-09T11:16:52Z; última actualización 2026-11-09T11:17:30Z.
- [pub in /frontend - Update #1689966965](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/42607791746): `success`; creado 2026-11-09T11:17:08Z; última actualización 2026-11-09T11:19:00Z.

## Drift

### S14

Snapshot [2d86f2d4b2ac](https://github.com/ISCOUTB/AS_202620_Drift/commit/2d86f2d4b2acc41142a93cb2662f53f47cd1b653).

- [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/42561849137): `success`; creado 2026-11-09T04:26:35Z; última actualización 2026-11-09T04:27:55Z.
- [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/42561849125): `success`; creado 2026-11-09T04:26:35Z; última actualización 2026-11-09T04:29:00Z.

### S15

Snapshot [2d86f2d4b2ac](https://github.com/ISCOUTB/AS_202620_Drift/commit/2d86f2d4b2acc41142a93cb2662f53f47cd1b653).

- [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/42561849137): `success`; creado 2026-11-09T04:26:35Z; última actualización 2026-11-09T04:27:55Z.
- [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/42561849125): `success`; creado 2026-11-09T04:26:35Z; última actualización 2026-11-09T04:29:00Z.
- [github_actions in /. - Update #1706223322](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/43768930080): `success`; creado 2026-11-15T22:22:24Z; última actualización 2026-11-15T22:22:59Z.
- [github_actions in / for SonarSource/sonarqube-scan-action - Update #1706223428](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/43768933289): `success`; creado 2026-11-15T22:22:26Z; última actualización 2026-11-15T22:23:11Z.
- [pip in /backend - Update #1706223260](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/43768930034): `success`; creado 2026-11-15T22:22:24Z; última actualización 2026-11-15T22:23:16Z.
- [npm_and_yarn in /frontend - Update #1706223267](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/43768929895): `success`; creado 2026-11-15T22:22:24Z; última actualización 2026-11-15T22:23:21Z.
- [pip in /backend for anyio, pydantic, pydantic-core, typing-inspection, schemathesis - Update #1706223372](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/43768932641): `success`; creado 2026-11-15T22:22:25Z; última actualización 2026-11-15T22:24:04Z.

## ElMapita

### S14

Snapshot [899bece9b4dd](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/899bece9b4ddda9fb27381c966c0b720c93b0fee).

- [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41396450324): `success`; creado 2026-11-02T05:51:37Z; última actualización 2026-11-02T05:53:34Z.
- [docker in /backend - Update #1674905068](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/41489376212): `success`; creado 2026-11-02T17:15:09Z; última actualización 2026-11-02T17:15:47Z.

### S15

Snapshot [7bf5bb2c120e](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/7bf5bb2c120e06c6c023d42f0dce1de7bd4ba077).

- [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/42581447260): `success`; creado 2026-11-09T07:46:35Z; última actualización 2026-11-09T07:49:14Z.
- [docker in /backend - Update #1690903903](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/42662722413): `success`; creado 2026-11-09T17:14:47Z; última actualización 2026-11-09T17:15:13Z.

## EnAgenda

### S14

Snapshot [a6dde3025c68](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b).

- [Taller mensajes y consistencia](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): `success`; creado 2026-10-26T03:57:41Z; última actualización 2026-10-26T03:57:50Z.
- [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): `failure`; creado 2026-10-26T03:57:41Z; última actualización 2026-10-26T03:58:08Z.
- [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521): `success`; creado 2026-10-26T03:57:41Z; última actualización 2026-10-26T03:58:27Z.

### S15

Snapshot [a6dde3025c68](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b).

- [Taller mensajes y consistencia](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284): `success`; creado 2026-10-26T03:57:41Z; última actualización 2026-10-26T03:57:50Z.
- [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410): `failure`; creado 2026-10-26T03:57:41Z; última actualización 2026-10-26T03:58:08Z.
- [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609521): `success`; creado 2026-10-26T03:57:41Z; última actualización 2026-10-26T03:58:27Z.

## GimnasioUTB

### S14

Snapshot [02ee41ef6fee](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/02ee41ef6fee89cdd624be7e2d70a86837b86c82).

- [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/42554463034): `success`; creado 2026-11-09T03:05:48Z; última actualización 2026-11-09T03:06:03Z.

### S15

Snapshot [9cf2b34ef0eb](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/9cf2b34ef0ebe74b649a416f68737f8a199a8e72).

No se recuperó una ejecución completada de ese SHA anterior al límite; no se declara éxito ni fallo.

## InvenTrack

### S14

Snapshot [2f338566adc3](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/2f338566adc35641e4d7cee1deb5dbc4afbb7bb8).

- [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/42556529986): `success`; creado 2026-11-09T03:27:47Z; última actualización 2026-11-09T03:28:48Z.

### S15

Snapshot [b36f889aad0b](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/b36f889aad0bec880aab8a7b8298255e976c87ba).

- [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/43789460138): `success`; creado 2026-11-16T01:59:48Z; última actualización 2026-11-16T02:00:39Z.

## LaPlacita

### S14

Snapshot [749242f3bba7](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/749242f3bba7c9b074e28bb2139e5530e088c757).

- [Deploy Dokploy (laboratorio de la U)](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/42288072311): `success`; creado 2026-11-06T20:24:22Z; última actualización 2026-11-06T20:26:46Z.
- [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/42288072133): `success`; creado 2026-11-06T20:24:22Z; última actualización 2026-11-06T20:27:29Z.
- [npm_and_yarn in /backend - Update #1687100365](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/42433224061): `success`; creado 2026-11-08T01:12:19Z; última actualización 2026-11-08T01:12:50Z.
- [github_actions in /. - Update #1687100368](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/42433224043): `success`; creado 2026-11-08T01:12:19Z; última actualización 2026-11-08T01:12:55Z.
- [npm_and_yarn in /frontend - Update #1687100360](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/42433224020): `success`; creado 2026-11-08T01:12:19Z; última actualización 2026-11-08T01:12:55Z.
- [docker in /backend, /frontend - Update #1687100540](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/42433226599): `success`; creado 2026-11-08T01:12:21Z; última actualización 2026-11-08T01:12:56Z.
- [npm_and_yarn in /backend for next, react, react-dom - Update #1687100460](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/42433226273): `success`; creado 2026-11-08T01:12:21Z; última actualización 2026-11-08T01:13:21Z.
- [npm_and_yarn in /frontend for @radix-ui/react-accordion, @radix-ui/react-alert-dialog, @radix-ui/react-aspect-ratio, @radix-ui/react-avatar, @radix-ui/react-checkbox, @radix-ui/react-collapsible, @radix-ui/react-context-menu, @radix-ui/react-dialog, @radix-ui/react-dropdown-menu, @radix-ui/react-hover-card, @radix-ui/react-label, @radix-ui/react-menubar, @radix-ui/react-navigation-menu, @radix-ui/react-popover, @radix-ui/react-progress, @radix-ui/react-radio-group, @radix-ui/react-scroll-area, @radix-ui/...](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/42433225782): `success`; creado 2026-11-08T01:12:20Z; última actualización 2026-11-08T01:17:30Z.

### S15

Snapshot [c4faebdb8298](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/c4faebdb829895f047aebade4ce24001065a6513).

- [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/43741258708): `success`; creado 2026-11-15T17:28:04Z; última actualización 2026-11-15T17:31:12Z.

## LostVault

### S14

Snapshot [f66f298434af](https://github.com/ISCOUTB/AS_202620_LostVault/commit/f66f298434af615573e92a778f88614bba53b7d3).

- [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/42560740805): `success`; creado 2026-11-09T04:14:56Z; última actualización 2026-11-09T04:15:14Z.
- [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/42560740976): `success`; creado 2026-11-09T04:14:56Z; última actualización 2026-11-09T04:15:55Z.
- [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/42560740795): `success`; creado 2026-11-09T04:14:56Z; última actualización 2026-11-09T04:17:29Z.

### S15

Snapshot [f66f298434af](https://github.com/ISCOUTB/AS_202620_LostVault/commit/f66f298434af615573e92a778f88614bba53b7d3).

- [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/42560740805): `success`; creado 2026-11-09T04:14:56Z; última actualización 2026-11-09T04:15:14Z.
- [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/42560740976): `success`; creado 2026-11-09T04:14:56Z; última actualización 2026-11-09T04:15:55Z.
- [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/42560740795): `success`; creado 2026-11-09T04:14:56Z; última actualización 2026-11-09T04:17:29Z.

## PROYECTO_CAMPUSMARKET

### S14

Snapshot [2d2848922db7](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/2d2848922db799389ffdcf0db4ef50437cd27ef2).

- [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42138355890): `success`; creado 2026-11-06T00:38:59Z; última actualización 2026-11-06T00:39:33Z.
- [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42138355822): `success`; creado 2026-11-06T00:38:59Z; última actualización 2026-11-06T00:40:55Z.
- [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42138355897): `success`; creado 2026-11-06T00:38:59Z; última actualización 2026-11-06T00:42:31Z.
- [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42138355941): `success`; creado 2026-11-06T00:38:59Z; última actualización 2026-11-06T00:43:52Z.
- [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42138355883): `success`; creado 2026-11-06T00:38:59Z; última actualización 2026-11-06T00:49:46Z.

### S15

Snapshot [c79c73d47936](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/c79c73d47936790b0f248bdea5c0a700ce8fe017).

- [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110841): `success`; creado 2026-11-09T06:27:15Z; última actualización 2026-11-09T06:29:11Z.
- [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110656): `failure`; creado 2026-11-09T06:27:14Z; última actualización 2026-11-09T06:30:24Z.
- [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110636): `success`; creado 2026-11-09T06:27:14Z; última actualización 2026-11-09T06:31:19Z.
- [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110702): `success`; creado 2026-11-09T06:27:14Z; última actualización 2026-11-09T06:32:01Z.
- [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110863): `success`; creado 2026-11-09T06:27:15Z; última actualización 2026-11-09T06:36:03Z.

## PideUtb

### S14

Snapshot [602b55fbfe97](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/602b55fbfe97a24f7ebe247cacbbccc50e560684).

- [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/42422992215): `success`; creado 2026-11-07T22:57:23Z; última actualización 2026-11-07T23:00:52Z.

### S15

Snapshot [602b55fbfe97](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/602b55fbfe97a24f7ebe247cacbbccc50e560684).

- [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/42422992215): `success`; creado 2026-11-07T22:57:23Z; última actualización 2026-11-07T23:00:52Z.

## ROUTB

### S14

Snapshot [cad53b1b2054](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/cad53b1b2054f30fa8dc6527fdee44ead440aff1).

- [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/42564185422): `success`; creado 2026-11-09T04:52:57Z; última actualización 2026-11-09T04:54:45Z.

### S15

Snapshot [e6fe8c818238](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/e6fe8c818238fbf0cbe658214d4b32b3e9c11ce6).

- [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/43669244266): `success`; creado 2026-11-15T02:45:20Z; última actualización 2026-11-15T02:47:25Z.
- [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/43693161605): `success`; creado 2026-11-15T08:09:14Z; última actualización 2026-11-15T08:09:22Z.

## Recobra

### S14

Snapshot [7142bb96d8c2](https://github.com/ISCOUTB/AS_202620_Recobra/commit/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b).

- [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/42527932254): `success`; creado 2026-11-08T21:59:39Z; última actualización 2026-11-08T22:02:09Z.

### S15

Snapshot [7142bb96d8c2](https://github.com/ISCOUTB/AS_202620_Recobra/commit/7142bb96d8c253b1a71ba1ec72aebb3597d9b29b).

- [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/42527932254): `success`; creado 2026-11-08T21:59:39Z; última actualización 2026-11-08T22:02:09Z.
- [github_actions in /. - Update #1697149763](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/43132111201): `success`; creado 2026-11-12T01:06:07Z; última actualización 2026-11-12T01:06:39Z.
- [docker in /. - Update #1697149795](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/43132111359): `success`; creado 2026-11-12T01:06:07Z; última actualización 2026-11-12T01:07:11Z.
- [npm_and_yarn in / for ajv, supertest, @types/supertest - Update #1697150136](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/43132118668): `success`; creado 2026-11-12T01:06:11Z; última actualización 2026-11-12T01:07:20Z.
- [pub in /mobile - Update #1697149770](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/43132111234): `success`; creado 2026-11-12T01:06:07Z; última actualización 2026-11-12T01:08:11Z.

## ShareU

### S14

Snapshot [20aeb0b77409](https://github.com/ISCOUTB/AS_202620_ShareU/commit/20aeb0b77409ca8d98341e9a94fef73b31ad7073).

- [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/41746144074): `failure`; creado 2026-11-04T00:20:56Z; última actualización 2026-11-04T00:20:56Z.

### S15

Snapshot [20aeb0b77409](https://github.com/ISCOUTB/AS_202620_ShareU/commit/20aeb0b77409ca8d98341e9a94fef73b31ad7073).

- [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/41746144074): `failure`; creado 2026-11-04T00:20:56Z; última actualización 2026-11-04T00:20:56Z.

## Sistema-de-calificacion-automatica

### S14

Snapshot [b3d7699fb085](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/b3d7699fb08524de28e8cee8dfde2610cbbf1182).

- [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/42561334967): `success`; creado 2026-11-09T04:21:03Z; última actualización 2026-11-09T04:23:34Z.

### S15

Snapshot [201864022a37](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/201864022a378b1d98c53bca62017e4fa47cb7dc).

- [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/43514210787): `success`; creado 2026-11-13T21:50:23Z; última actualización 2026-11-13T21:53:02Z.

## TAIA_-Task-Artificial-Intelligence-Assistant

### S14

Snapshot [7342f349752a](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/7342f349752af2b26f1d9df7e313fbcc1b9656d4).

No se recuperó una ejecución completada de ese SHA anterior al límite; no se declara éxito ni fallo.

### S15

Snapshot [7342f349752a](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/7342f349752af2b26f1d9df7e313fbcc1b9656d4).

No se recuperó una ejecución completada de ese SHA anterior al límite; no se declara éxito ni fallo.

## TIENDA-VIRTUAL-UTB

### S14

Snapshot [28c688e65adf](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/28c688e65adfb9f49ac9602b538d1f6d365b395c).

- [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/42560128666): `success`; creado 2026-11-09T04:08:32Z; última actualización 2026-11-09T04:10:02Z.

### S15

Snapshot [28c688e65adf](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/28c688e65adfb9f49ac9602b538d1f6d365b395c).

- [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/42560128666): `success`; creado 2026-11-09T04:08:32Z; última actualización 2026-11-09T04:10:02Z.

## UTB_TRACKER

### S14

Snapshot [60570b9dc2f2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/60570b9dc2f25b8135e6dc90fcb809f47477eba2).

- [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/42559084958): `success`; creado 2026-11-09T03:56:45Z; última actualización 2026-11-09T03:59:09Z.

### S15

Snapshot [f6b1e672f506](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/f6b1e672f506622f9c2d83f0f48802ab620f77e0).

- [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/43801645838): `success`; creado 2026-11-16T04:02:29Z; última actualización 2026-11-16T04:07:18Z.

## Verifacts

### S14

Snapshot [2753a4ffe072](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/2753a4ffe07288cabb7c636e5ae65daf481ce2c2).

- [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/42154186937): `success`; creado 2026-11-06T03:03:43Z; última actualización 2026-11-06T03:04:29Z.
- [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/42154186800): `success`; creado 2026-11-06T03:03:43Z; última actualización 2026-11-06T03:04:45Z.

### S15

Snapshot [035383e19e44](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/035383e19e44ef26cefabfab7d71e30f37f0beed).

- [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/42741684410): `success`; creado 2026-11-10T02:17:08Z; última actualización 2026-11-10T02:17:57Z.
- [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/42741684420): `success`; creado 2026-11-10T02:17:08Z; última actualización 2026-11-10T02:18:00Z.

## XALD

### S14

Snapshot [7aac07e5b2bf](https://github.com/ISCOUTB/AS_202620_XALD/commit/7aac07e5b2bfd1e96a7127d012f1c33ff9958a78).

- [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/42555357336): `success`; creado 2026-11-09T03:15:14Z; última actualización 2026-11-09T03:17:19Z.

### S15

Snapshot [7aac07e5b2bf](https://github.com/ISCOUTB/AS_202620_XALD/commit/7aac07e5b2bfd1e96a7127d012f1c33ff9958a78).

- [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/42555357336): `success`; creado 2026-11-09T03:15:14Z; última actualización 2026-11-09T03:17:19Z.
- [docker in /backend - Update #1691695393](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/42719060357): `success`; creado 2026-11-09T23:16:10Z; última actualización 2026-11-09T23:16:38Z.
- [github_actions in /. - Update #1691695383](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/42719060381): `success`; creado 2026-11-09T23:16:10Z; última actualización 2026-11-09T23:16:42Z.

## mapsutb

### S14

Snapshot [03e331d44360](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/03e331d4436039869e27ce2dc1adda2d520fa833).

- [CI](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200516007): `success`; creado 2026-10-25T14:04:18Z; última actualización 2026-10-25T14:05:51Z.
- [Despliegue web (Firebase Hosting)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40200515940): `success`; creado 2026-10-25T14:04:18Z; última actualización 2026-10-25T14:06:17Z.
- [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/42561782224): `success`; creado 2026-11-09T04:25:53Z; última actualización 2026-11-09T04:26:04Z.
- [Sincronizar hallazgos de Sonar a GitHub Issues](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/42540596935): `success`; creado 2026-11-09T00:30:53Z; última actualización 2026-11-09T00:31:05Z.

### S15

Snapshot [78a8a5450532](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/78a8a545053237a58410e28d6f0002629c527e63).

- [CI](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/43040786035): `success`; creado 2026-11-11T14:40:51Z; última actualización 2026-11-11T14:42:45Z.
- [Despliegue web (Firebase Hosting)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/43040785975): `success`; creado 2026-11-11T14:40:51Z; última actualización 2026-11-11T14:42:50Z.
- [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/43804449443): `success`; creado 2026-11-16T04:29:52Z; última actualización 2026-11-16T04:30:06Z.
- [Sincronizar hallazgos de Sonar a GitHub Issues](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/43781128703): `success`; creado 2026-11-16T00:34:01Z; última actualización 2026-11-16T00:34:13Z.

## uniTeam

### S14

Snapshot [5e18bc227e0a](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/5e18bc227e0aae35a3f3d797a8405d108a789ef7).

- [seguridad-dependencias](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393152938): `success`; creado 2026-11-02T05:17:34Z; última actualización 2026-11-02T05:18:03Z.
- [CI](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393152995): `success`; creado 2026-11-02T05:17:34Z; última actualización 2026-11-02T05:18:17Z.
- [github_actions in / for actions/upload-artifact - Update #1672457512](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393291550): `success`; creado 2026-11-02T05:18:57Z; última actualización 2026-11-02T05:19:38Z.
- [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/42541531581): `failure`; creado 2026-11-09T00:41:17Z; última actualización 2026-11-09T00:41:26Z.
- [github_actions in /. - Update #1688480332](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/42555342974): `success`; creado 2026-11-09T03:15:05Z; última actualización 2026-11-09T03:15:33Z.
- [npm_and_yarn in /web - Update #1688480307](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/42555342940): `success`; creado 2026-11-09T03:15:05Z; última actualización 2026-11-09T03:16:06Z.
- [pip in /. - Update #1688480303](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/42555343196): `success`; creado 2026-11-09T03:15:05Z; última actualización 2026-11-09T03:18:01Z.

### S15

Snapshot [5e18bc227e0a](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/5e18bc227e0aae35a3f3d797a8405d108a789ef7).

- [seguridad-dependencias](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393152938): `success`; creado 2026-11-02T05:17:34Z; última actualización 2026-11-02T05:18:03Z.
- [CI](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393152995): `success`; creado 2026-11-02T05:17:34Z; última actualización 2026-11-02T05:18:17Z.
- [github_actions in / for actions/upload-artifact - Update #1672457512](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/41393291550): `success`; creado 2026-11-02T05:18:57Z; última actualización 2026-11-02T05:19:38Z.
- [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/43782179326): `failure`; creado 2026-11-16T00:44:44Z; última actualización 2026-11-16T00:44:52Z.
- [github_actions in /. - Update #1688480332](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/42555342974): `success`; creado 2026-11-09T03:15:05Z; última actualización 2026-11-09T03:15:33Z.
- [npm_and_yarn in /web - Update #1688480307](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/42555342940): `success`; creado 2026-11-09T03:15:05Z; última actualización 2026-11-09T03:16:06Z.
- [pip in /. - Update #1688480303](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/42555343196): `success`; creado 2026-11-09T03:15:05Z; última actualización 2026-11-09T03:18:01Z.
- [github_actions in /. - Update #1706853425](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/43797055411): `success`; creado 2026-11-16T03:15:17Z; última actualización 2026-11-16T03:15:52Z.
- [npm_and_yarn in /web - Update #1706853914](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/43797065688): `success`; creado 2026-11-16T03:15:22Z; última actualización 2026-11-16T03:16:27Z.
