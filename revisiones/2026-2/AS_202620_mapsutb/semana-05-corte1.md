# Semana 5 · Primer corte · mapsutb

> Revisión definitiva post-cierre — 2026-09-07. Reemplaza la revisión manual preliminar del 2026-09-03. Cierre: `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado calificado | etiqueta `corte-1` → `7e56ad372dbfebd8c7c38f74b19006e14f9e72e3` (2026-08-09T23:27:46-05:00) — **existe y es anterior al cierre**, pero corresponde al commit de evidencia S1 |
| HEAD para el overall | `f40775df512ca3d35f07a804602076486c5bf3e1` (2026-09-06T22:35:28-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log -1 corte-1`; `git log -1 --until=cierre HEAD`; `git ls-tree -r corte-1`; `git log f0d036a..HEAD`; `git grep` (patrones de secretos); `git shortlog -sne HEAD`; búsqueda de `correcciones.md` en raíz de HEAD (no existe) |
| Revisor | agente de revisión, solo lectura; no se ejecutó código del equipo |
| Alcance externo no disponible | restricción asignada al equipo y PDF de Moodle |

## Nota sobre la etiqueta

`corte-1` sigue apuntando al mismo commit `7e56ad3` que en la revisión preliminar del 03/09: el equipo **no la movió** en la semana que tuvo para corregir. Ese commit es, literalmente, anterior al cierre — pero corresponde con claridad al estado de la evidencia S1 (solo `README.md`, `docs/ficha-problema.md`, `docs/aspectos.md`, `docs/ia.md`; nada de ADR, C4, código ni pruebas). Por la regla del protocolo para este caso ("apunta a un estado de una semana anterior"), se revisa igual el contenido de la etiqueta para la matriz de la ficha, y la fila de versionado de la matriz transversal queda en **No cumple**, con esta discrepancia como motivo.

## Matriz de la ficha (evaluada sobre el contenido de `corte-1` = `7e56ad3`)

| Criterio de evaluación | Estado | Observaciones |
|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | No cumple | Existe y es anterior al cierre (`7e56ad3`, 09/08), pero es el mismo commit de la evidencia S1: no contiene ninguna respuesta al reto. Sigue sin moverse tras la revisión preliminar. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No verificado | El adjunto de Moodle no está disponible en el kit. |
| Impacto de la restricción localizado en requisitos, C4 y código | No verificado | No se dispone de la restricción asignada. En `corte-1` no hay C4 ni código (`git ls-tree -r corte-1`: solo 4 archivos); `docs/aspectos.md` en ese estado deja C4, ADR, código, pruebas y evidencia "Aún no iniciado". |
| Línea base medida y verificable antes del cambio | No cumple | En `corte-1`, `docs/aspectos.md` solo declara el umbral objetivo (≤3 s, ≤5 m); no hay cifra medida ni procedimiento. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | No cumple | `corte-1` no tiene `docs/adr/`. |
| Cambio implementado y ejecutable de extremo a extremo | No cumple | `corte-1` no tiene código (`lib/`) ni comando de arranque más allá del título del README. |
| Límites declarados conservados tras el cambio | No cumple | No hay C4 ni código en `corte-1` para contrastar. |
| Prueba que cubre el cambio, en verde en el pipeline | No cumple | `corte-1` no tiene `test/` ni `.github/workflows/`. |
| Resultado contrastado con el umbral del escenario y reproducible | No cumple | No hay resultado medido en `corte-1`. |
| Cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia navegable | No cumple | `docs/aspectos.md` en `corte-1` tiene C4 "por definir", "Sin ADR aún" y código/pruebas/evidencia "Aún no iniciado": la fila A-01 no llega a ninguna parte. |
| Salida de IA aceptada/corregida/rechazada con motivo técnico | No cumple | `docs/ia.md` en `corte-1` solo tiene las dos entradas del 07/08 (declarar/especificar), anteriores al periodo del corte. |
| Sustentación del reto | No verificado | Lo resuelve el docente en la sesión. |

**Recuento: 0 de 12.**

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Observaciones |
|---|---|---|
| a. Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon sin autenticación de `ISCOUTB/AS_202620_mapsutb` responde el 2026-09-07. |
| b. Estructura mínima presente | No cumple | En `corte-1` faltan `docs/arc42/`, `docs/adr/` y `docs/c4/` (solo README, ficha-problema, aspectos e ia). En HEAD existen pero como `docs/Arc42/` y `docs/C4/` (mayúsculas fuera de convención). |
| c. Estado calificado identificable | No cumple | La etiqueta existe pero corresponde a un estado de una semana anterior (S1), no al corte 1; ver nota arriba. |
| d. Nombres de ADR según la convención | No cumple | En HEAD, `docs/adr/0002.md` no lleva título en kebab-case (solo el número); `0001-patrones-de-diseno.md` sí cumple. En `corte-1` no hay ADR. |
| e. ADR aceptados no reescritos | No cumple | `docs/adr/0001-patrones-de-diseno.md` fue reescrito en múltiples commits entre el 23/08 y el 31/08 sin dejarlo "reemplazado" con un ADR nuevo (confirmado también en HEAD actual). |
| f. `docs/ia.md` al día para la semana | No cumple | Última entrada 30/08 (`docs/ia.md`, entrada "Verificar"); no hay entrada del trabajo de S5/corte-1 en HEAD `f40775d`. |
| g. Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` con los patrones del contrato sin coincidencias en HEAD; sin `.env` versionado. |
| h. Contribución de todos los integrantes | Cumple | `git shortlog -sne HEAD`: CarlosManrique-1397 (41), i-matallana (37+2, dos correos = Isabel Paez Matallana), charlygz21 (13), nerlis-otero (6). Los cuatro integrantes tienen commits. |

## Estado global del proyecto (overall · HEAD `f40775d`)

- El HEAD avanzó respecto al 03/09: conversión de `.adoc` a `.md`, el ADR 0002 (patrones de diseño, con cambio de alcance que descarta la realidad aumentada) y un corte vertical de Repository/Observer (`lib/services/ubicacion_service.dart`) fusionado por PR #1 el 31/08.
- Pese a ese avance, **`docs/aspectos.md` sigue sin actualizar en HEAD**: la fila A-01 sigue diciendo "Sin ADR aún", C4 "por definir" y código/pruebas/evidencia "Aún no iniciado", contradiciendo que el ADR 0002 y el código ya existen desde el 30-31/08. La cadena de trazabilidad está rota también en HEAD, no solo en la etiqueta.
- El único test es `test/app_smoke_test.dart` (prueba de humo del esqueleto); no cubre el cambio de ubicación. Sigue sin existir `.github/workflows/`.
- No hay medición de línea base ni resultado reproducible contra umbral en ningún punto del historial.
- El 06/09 (la noche antes del cierre) se agregaron cuatro archivos vacíos `FeedbackCorreccioner/FeedbackS1..S4` (commits de `charlygz21`, 22:34–22:35), sin contenido; no aportan evidencia y no hay `correcciones.md` en la raíz de HEAD ni de `corte-1`, así que no hay correcciones del equipo que adjudicar en este lote.
- El repositorio sigue sin mover la etiqueta `corte-1` al commit real del corte, pese a que la revisión preliminar ya señaló el problema el 03/09.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia |
|---|---:|---:|---|
| Diagnóstico del reto | no demostrado | 0,00 | La etiqueta apunta a S1; no hay diagnóstico del reto en el estado calificado ni referencia a la restricción asignada. |
| Alternativas y decisión | no demostrado | 0,00 | No hay ADR en `corte-1`. |
| Aplicación sobre el corte vertical | no demostrado | 0,00 | `corte-1` no contiene código ni arranque. |
| Pruebas, medición y trazabilidad | no demostrado | 0,00 | No hay pruebas, medición ni cadena completa en la etiqueta. |
| Sustentación del reto | lo fija el docente | pendiente | Requiere sesión. |
| **Subtotal técnico** | | **0,00 / 4,00** | No es la nota total sobre 5,00. |

## No verificado

- Restricción asignada al equipo (no disponible en el kit).
- PDF de dos páginas de Moodle.
- Sustentación (la fija el docente en sesión).

## Hallazgos

- `corte-1` sigue fijada en el commit de S1 tras la revisión preliminar; el equipo no la corrigió antes del cierre.
- El HEAD acumula avance real (ADR 0002, código Repository/Observer) que no está entregado por la etiqueta y que, aun en HEAD, no está reflejado en `docs/aspectos.md`.
- ADR 0001 reescrito sin declarar reemplazo; `docs/adr/0002.md` fuera de la convención de nombres.
- Sin `correcciones.md`: no hay objeciones del equipo a la revisión preliminar que adjudicar.

## Preguntas para la sustentación

- ¿Por qué `corte-1` sigue apuntando al commit de la evidencia S1 pese a que la revisión preliminar ya lo señaló el 03/09?
- ¿Cuál fue la restricción asignada y qué evidencia (aún no etiquetada) demuestra que el ADR 0002 y el cambio de ubicación responden a ella?
- ¿Qué impide actualizar `docs/aspectos.md` para que refleje el ADR y el código que ya existen en HEAD?
