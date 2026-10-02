> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · mapsutb

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `0190115c72b90116b2c12d9555a4f8e5c75f1bb0` en `origin/master` (2026-10-01T14:53:58-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual **sí tiene commits del periodo S9**: el estado calificado de S8 (`8cfe4581`) fue
superado por diez commits del 2026-10-01 (`f1b3fe4`…`0190115`). Bajo CONTRATO §12, el periodo S9
(`8cfe4581..origin/master`) es el que se califica; la base de S8 solo se cita como contexto. Esta
pasada **no tiene corte**: se califica la punta actual. La fila de credenciales y la matriz
transversal se deciden sobre el estado en la punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Ruteo interno del campus (contexto Ruteo, aspecto A-01): `lib/routing/grafo.dart`, `lib/routing/mapa_repository.dart` y `lib/routing/servicio_ruteo.dart` (Dijkstra), sobre `assets/data/grafo.json` (78 nodos, 90 tramos); pantalla en `lib/features/mapas_ruteo/presentation/screens/mapa_screen.dart`. Commits del periodo `e543b4d`, `443f470`, `b679886`, `265da7f`. `docs/evidencia-s9.md:7-16`. | Cumple | Porción del sistema real y no un ejercicio aparte; el registro de IA (`docs/ia.md`, entrada 01/10/2026) la declara construida con Claude Code sobre datos levantados por el equipo. |
| Cadena completa navegable para esa porción | `docs/aspectos.md:7` fila **A-01**: requisito RF-01 → C4 (`docs/c4/C2.md`, `docs/c4/C3.md`) → ADR `0011`, `0012`, `0013` → código `lib/routing/` → pruebas `test/ruteo_test.dart`, `test/grafo_test.dart` → evidencia (run de CI y medición del Escenario 2). | Cumple | La cadena llega a código, prueba y medición. Salvedad de forma: la celda Código de A-01 aún dice «Pendiente: pantalla de mapa con `flutter_map`» cuando esa pantalla ya existe en el tip; anotado como hallazgo. |
| ADR con la decisión argumentada por el equipo | `docs/adr/0013-ruteo-dijkstra-grafo-propio.md` (Dijkstra con montículo propio; descarta A*, tabla precalculada y servicio externo, cada uno con su motivo técnico frente a restricciones del proyecto); `docs/adr/0011-fuente-datos-geograficos-osm.md` (descarta Google Maps/Earth por sus términos §2(d)); `docs/adr/0012-mapa-base-flutter-map-osm.md` (reemplaza Google Maps SDK por la restricción «sin tarjeta»). | Cumple | Los tres ADR argumentan con las restricciones de arc42 §2 y con alternativas descartadas; la decisión es del equipo, no una adopción de lo propuesto por la herramienta. |
| Prueba que falla ante el defecto que cubre | `test/ruteo_test.dart:105-112` incluye una prueba de mutación: `rutaMutanteMenosTramos` (búsqueda por número de tramos) devuelve A–C con 50 m y la verificación de 20 m la rechaza. Procedimiento en rojo documentado en `docs/evidencia-s9.md:33-49` (cambiar `d + t.metros` por `d + 1` y ejecutar `flutter test test/ruteo_test.dart`). | Cumple | Se aporta prueba de mutación y procedimiento documentado; la ejecución concreta se confirma en CI (ver fila de medición). |
| Medición del escenario asociado | Escenario 2 (ruta en ≤ 5 s): 100 rutas sobre el grafo real, **p95 0,92 ms, máximo 3,6 ms**, contraste con el umbral en `docs/evidencia-s9.md:50-57` y `test/ruteo_test.dart:184-197` (la prueba afirma p95 < 500 ms y lo imprime). Run de CI del hash revisado en verde: [36917674285](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/36917674285). | Cumple | El equipo cita el run [36913480665](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/36913480665) para la cifra p95; no se consultó individualmente por la regla de una sola llamada de API por equipo. El CI de la punta (misma prueba) está en verde. Falta medir la parte de pantalla. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | `docs/ia.md`, entradas del 01/10/2026 (cambios en `265da7f`, `e543b4d`, `bb3e0f0`, `f1d0aff`, `f1b3fe4`). Rechazos con motivo técnico: `package:collection` para la cola, A*, coordenadas desde Google Maps/Earth, asignar «Bohíos» a la Zona T sin evidencia. Corrección: complejidad cognitiva 25 en `rutaEntreNodos`. | Cumple | El extracto del periodo existe y trae aceptado, corregido y rechazado con motivo. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | `docs/evidencia-s9.md:72-82` contrasta las reglas de S6/ADR 0006 sobre el código: `grep '^import' lib/routing/*.dart` solo da `dart:*`, `flutter/services`, `core/log.dart` y `grafo.dart` (sin acoplarse al modelo `Zona`); las escrituras se rastrean con el patrón de la ficha; hallazgo sobre `scripts/campo/analizar_campo.py` escribiendo `zonas.json`, con control (`--escribir-repo` y validación por `test/grafo_test.dart`). | Cumple | Verificado por el revisor: los imports de `lib/routing/` coinciden con lo declarado y no hay escrituras de datos de otro contexto en ejecución. |
| Dependencias propuestas verificadas en su registro oficial | Periodo sobre `pubspec.yaml`: se añaden `flutter_map: ^8.3.2` (`pubspec.yaml:16`) y `latlong2: ^0.10.1` (`pubspec.yaml:17`); el asset `assets/data/grafo.json` (`:28`). Verificación en pub.dev: `flutter_map` 8.3.2 existe y coincide; `latlong2` 0.10.1 existe y coincide. El script de campo usa `defusedxml`, verificado en PyPI (0.7.1). | Cumple | Salvedad: `docs/evidencia-s9.md:83-88` afirma «ninguna dependencia nueva» y que `flutter_map` «se agregará» después; el manifiesto del tip ya las trae. La comprobación se hizo contra el registro oficial y son legítimas; la sección 8 de la evidencia quedó desactualizada. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta: única coincidencia material `.github/workflows/sonda-disponibilidad.yml:31` (`x-access-token:${GITHUB_TOKEN}`), que es una interpolación de variable, no un secreto; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | Sin credenciales reales; los demás resultados son nombres de tipos y parámetros. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | `docs/adr/0014-sin-componente-generativo.md` justifica no incorporarlo (costo y tarjeta, funcionamiento sin conexión, casos resueltos con búsqueda de texto y grafo), pero su estado es **«Propuesto — pendiente de confirmación del equipo»**; `docs/evidencia-s9.md:97-101` lo repite. | No cumple | Existe el ADR y está argumentado, pero la decisión aún no se tomó: el propio equipo lo deja *Propuesto*. La ficha exige el ADR que justifica la decisión de no incorporarlo, no la propuesta de hacerlo; la ausencia de decisión no es la decisión. Puede pasar a Cumple si el equipo lo marca *Aceptado* antes del cierre. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_mapsutb`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre conforme y visibilidad pública. |
| Estructura mínima presente | En `0190115c`: `docs/arc42/`, `docs/adr/` (0001-0014), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2; arc42 en `.adoc`/`.md`. |
| Estado calificado identificable | `0190115c72b90116b2c12d9555a4f8e5c75f1bb0` en `origin/master`, commit del 2026-10-01T14:53:58-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. Supera el hash de S8 (`8cfe4581`). |
| Nombres de ADR según la convención | `docs/adr/0001-*` … `0014-*`, todos `NNNN-titulo-en-kebab-case.md`; el filtro del contrato §4 no devuelve nada. | Cumple | Catorce ADR conformes. |
| ADR aceptados no reescritos | `git log --follow docs/adr/0001-patrones-de-diseno.md`: reescrituras de contenido posteriores a su creación y aceptación (`1e370a0`…`3e8335c`, 28–31/08/2026). El ADR declara desde el 2026-08-30 «Reemplazado por ADR 0002», pero los cambios de decisión se hicieron editando el aceptado. | No cumple | No conformidad de la base (S4/S8), aún visible en la punta: la prohibición del contrato §4 es editar un ADR aceptado. El reemplazo ahora está declarado, pero no borra las reescrituras. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md`: última modificación `265da7f` (2026-10-01T14:24:53-05:00), dentro del periodo S9; entradas del 01/10/2026 con aceptado/corregido/rechazado. | Cumple | El registro crece dentro del periodo revisado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties`; `.github/workflows/ci.yml:53` invoca el scanner y `:60-61` espera el Quality Gate (`-Dsonar.qualitygate.wait=true`); run de CI del hash revisado en verde ([36917674285](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/36917674285)); panel público en `README.md:110` (`sonarcloud.io/summary/new_code?id=ISCOUTB_AS_202620_mapsutb`). Además, 6 runs del hash revisado, todos `success` (CI, despliegue y cuatro sondas). | Cumple | Las tres piezas del contrato §8 están: configuración, línea del workflow y URL pública con Quality Gate ligada al run revisado. |
| Sin credenciales en el repositorio ni en el historial | `git grep` del contrato y `git log -S` sin credenciales reales; sin `.env` versionado. | Cumple | Única coincidencia material: `${GITHUB_TOKEN}` interpolado en un workflow. |
| Contribución de todos los integrantes | `git shortlog -sne` consolidado por correo idéntico: `CarlosManrique-1397` (53); `i-matallana` (41+2, dos correos); `charly`/`charlygz21` (36+25+22+2, un mismo correo en tres identidades); `nerlis-otero` (22). | Cumple | Cuatro personas = cuatro integrantes declarados en `EQUIPOS.md`. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `0190115c72b90116b2c12d9555a4f8e5c75f1bb0` (2026-10-01T14:53:58-05:00) (`origin/master`)
- **Veredicto**: entrega S9 sustantiva y trazada; una deuda de decisión y varias de forma
- Resumen: en el periodo S9 el equipo construyó el ruteo a pie completo (grafo peatonal derivado de
  OpenStreetMap y levantamiento propio, Repository, servicio Dijkstra, pantalla con `flutter_map`),
  con pruebas (incluida una de mutación), medición del Escenario 2 (p95 0,92 ms frente al umbral de
  5 s), ADR 0011-0013 argumentados con alternativas, auditoría de erosión contrastada sobre el código
  y un `docs/ia.md` que registra lo aceptado, lo corregido y lo rechazado. El pipeline de la punta
  está en verde, con SonarCloud y Quality Gate visibles. Lo que falta es cerrar la decisión sobre el
  componente generativo (ADR 0014 en *Propuesto*) y corregir desajustes de forma: la celda Código de
  A-01 declara pendiente una pantalla que ya existe, y la sección 8 de `docs/evidencia-s9.md` afirma
  «ninguna dependencia nueva» cuando `pubspec.yaml` ya añade `flutter_map` y `latlong2`. Se mantienen
  no conformidades de base: ADR 0001 reescrito tras su aceptación.

Pendientes que siguen abiertos:
- ADR 0014 en estado *Propuesto*: falta la decisión del equipo sobre el componente generativo.
- `docs/aspectos.md:7` (A-01) con la celda Código desactualizada (pantalla de mapa ya construida).
- `docs/evidencia-s9.md:83-88` desactualizada respecto de `pubspec.yaml` en las dependencias.
- ADR 0001 editado tras su aceptación sin crear un ADR nuevo en ese momento (reemplazo declarado después).
- GPS real y coordenadas definitivas de las zonas, declarados pendientes por el propio equipo.

## Recuento y nota sugerida

**9 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.6 = 1 + 4 × (9/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, las nueve filas resueltas por artefactos del periodo se deciden sobre
`8cfe4581..origin/master`; la fila de credenciales se resuelve sobre el estado en la punta.

## No verificado / pendientes

- Componente generativo: **No cumple**. El ADR 0014 existe y está argumentado, pero sigue en estado
  *Propuesto*; la decisión de no incorporarlo no está tomada.
- Medición del Escenario 2: p95 de cálculo verificado; la parte de pantalla queda pendiente de medir.
- GPS real y coordenadas definitivas de las 11 zonas: pendientes según ADR 0011/0012.
- `docs/evidencia-s9.md` §8 debe alinearse con las dependencias realmente añadidas.

## Hallazgos para la planilla

- Periodo S9 con diez commits (2026-10-01): ruteo con Dijkstra, grafo peatonal, pantalla de mapa y herramientas de campo.
- La ficha pasa a 9/10: nueve criterios con artefacto del periodo; el único No cumple es el ADR del componente generativo, aún *Propuesto*.
- `docs/aspectos.md:7` (A-01) declara pendiente la pantalla de mapa (`b679886`) que ya está en la punta: actualizar la celda Código.
- `docs/evidencia-s9.md:83-88` dice «ninguna dependencia nueva» mientras `pubspec.yaml:16-17` añade `flutter_map` y `latlong2` (ambas verificadas en pub.dev).
- Pipeline de la punta en verde (run 36917674285) con SonarCloud y Quality Gate públicos; se mantiene la no conformidad de ADR aceptados reescritos (ADR 0001).
- Se cierra el arrastre de S8 sobre despliegue/observabilidad/SonarCloud para la punta.
