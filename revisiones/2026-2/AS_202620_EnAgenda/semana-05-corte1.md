# Semana 05 · Primer corte · EnAgenda

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03, hecha antes del cierre `2026-09-07T05:00:00Z`. Se repite sobre el estado etiquetado `corte-1`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | etiqueta `corte-1` → `31773adcf58856520e4985c0e178256d34814fe0` · 2026-09-06T23:39:52-05:00 (anterior al cierre) |
| Cierre | `2026-09-07T05:00:00Z` |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log corte-1`; `git checkout corte-1`; `git ls-tree`; `git shortlog -sne`; `git grep` de secretos; `curl` a `actions/runs?per_page=15` (1 llamada) |
| Restricción asignada | No disponible en el kit; el repositorio tampoco declara un reto nuevo para Corte 1 (ver más abajo, el propio equipo lo confirma en `docs/correcciones.md`) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` devuelve `corte-1` → `31773ad` (2026-09-06T23:39:52-05:00), anterior al cierre | Cumple | Etiqueta creada la misma noche del cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay ruta en el repo; adjunto de Moodle no accesible desde el kit | No verificado | Requiere revisión en Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | `docs/correcciones.md` (commit `ffc9aae`, 2026-09-06T23:32:30-05:00) declara explícitamente en su §5 que "para este corte no se incorpora una nueva funcionalidad ni se formula un reto diferente al trabajo existente" | No cumple | El propio equipo admite no haber diagnosticado una restricción nueva; el trabajo del cierre fue corregir feedback de S4, no responder al reto de Corte 1. |
| Línea base medida y verificable antes del cambio | No existe una cifra de línea base para un escenario nuevo; `docs/arc42/10-requisitos-de-calidad.md` mantiene los umbrales ya conocidos de S4 | No cumple | Sin restricción diagnosticada no hay línea base que medir. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/` solo contiene `0001-usar-monolito-modular.md`, aceptado el 2026-08-23 | No cumple | No hay ADR nuevo para el reto de Corte 1. |
| Cambio implementado y ejecutable de extremo a extremo | Commits `6d61a7b`…`31773ad` (2026-09-06) solo tocan `docs/c4/` y `docs/aspectos.md`; no hay cambio de código en `src/` o `app/` entre S4 y `corte-1` | No cumple | No hay incremento sobre el corte vertical; el README sigue arrancando con `python app\web.py` (línea 112) sin cambios funcionales. |
| Límites declarados conservados tras el cambio | El C4 de contenedores se corrigió (Aplicación Flask / Módulo de Invitaciones / Repositorio en memoria) para alinearse con el código, pero no hubo cambio de código que pusiera esos límites a prueba | No verificado | La corrección documental es positiva, pero no hay un cambio del reto que verificar contra los límites. |
| Prueba que cubre el cambio, en verde en el pipeline | Run `34079...` sobre `31773ad`, CI success, 2026-09-07T04:40:19Z (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/34079...); cubre `tests/test_invitaciones.py`, prueba ya existente de S4 | No cumple | Pipeline en verde, pero ninguna prueba nueva cubre un cambio del reto porque no existe cambio. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición, herramienta ni procedimiento para un escenario nuevo | No cumple | No hay resultado que contrastar. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md` (fila A-01) ahora enlaza C4, ADR, código y pruebas, pero la celda Evidencia apunta a `correcciones-feedback.md`, archivo que no existe (el real es `docs/correcciones.md`) | No cumple | Mejoró respecto a S4, pero la cadena se rompe en la última celda: enlace roto = hueco. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md` no tiene entradas posteriores al 30/08/2026; nada referido al trabajo de corrección de esta semana ni a un reto de Corte 1 | No cumple | Falta registrar el uso de IA (si lo hubo) para las correcciones de C4/aspectos del cierre. |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `https://github.com/ISCOUTB/AS_202620_EnAgenda` sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r --name-only corte-1` devuelve README.md, docs/adr/, docs/arc42/, docs/aspectos.md, docs/c4/, docs/ia.md | Cumple | Nombres de arc42 con espacios y tildes (`02- restricciones.md`, `03-contexto y alcance.md`), desviación de forma ya señalada desde S1. |
| Estado calificado identificable | Etiqueta `corte-1` → `31773ad`, anterior al cierre | Cumple | — |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md` pasa `NNNN-titulo-en-kebab-case.md` | Cumple | — |
| ADR aceptados no reescritos | Aceptado en `c38adfb`; sin cambios de contenido posteriores, solo el rename histórico ya reportado en S4 | Cumple | — |
| `docs/ia.md` al día para la semana | Última entrada es del 30/08/2026 (S4); nada del trabajo de corrección de la noche del cierre (2026-09-06) | No cumple | No registra el uso de IA (si lo hubo) para las correcciones del cierre. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de secretos solo encuentra la palabra `token` como campo de dominio de invitaciones (`app/web.py`, `src/invitaciones/...`, `tests/test_invitaciones.py`); sin `.env` versionado | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne corte-1`: Daoisttl0FB3/gabimoralesc30 63 commits, Jein-12/jeimy4637 52, eliabarnedocondef10-gif 12 | Cumple | Los 3 integrantes tienen commits en el historial. |

## Estado global del proyecto (overall · HEAD)

- **HEAD**: `942e112bc11f5415b81c82c5c048e1b07d7d792d` · 2026-09-06T23:56:39-05:00 · "Fix formatting in ia.md documentation" — 17 minutos después de la etiqueta `corte-1`, ambos antes del cierre.
- CI en verde en `HEAD` (run `34084959301`, 2026-09-07T04:56:42Z).
- El proyecto sigue con la línea base de S4 (aplicación Flask, módulo de invitaciones, pruebas y CI en verde) más las correcciones de C4 y trazabilidad hechas la noche del 2026-09-06.
- El propio equipo documenta, en `docs/correcciones.md`, que el trabajo de cierre fue exclusivamente corrección de feedback anterior y que **no formuló un reto ni una restricción nueva para el Corte 1**.
- No se detectan entregas posteriores al cierre.

## Nivel de rúbrica sugerido (propuesta al docente, NO nota aplicada)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia evaluable del reto | 0,00 | El equipo confirma en `docs/correcciones.md` §5 que no diagnosticó una restricción nueva. |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | Único ADR es de la línea base (S3), sin ADR de Corte 1. |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | No hay cambio de código entre S4 y `corte-1`; solo correcciones documentales. |
| Pruebas, medición y trazabilidad | Básico | 0,60 | Cadena de `docs/aspectos.md` mejoró (enlaza C4/ADR/código/pruebas) pero la celda Evidencia queda rota y no hay medición del reto. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico** | | **0,60 / 4,00** | Propuesta al docente; la nota final se fija en Moodle. |

## Recuento

1 de 12 criterios Cumple (el criterio 1, etiqueta válida).

## No verificado

- PDF de dos páginas en Moodle.
- Conservación de límites tras el cambio (no hubo cambio del reto que verificar).
- Sustentación del equipo.
- Registro de IA para las correcciones de la noche del cierre (podría existir y no estar en `docs/ia.md`).

## Hallazgos

- El equipo no respondió al reto de restricción nueva de Corte 1; en cambio dedicó la noche del cierre a corregir hallazgos de S4 (C4 desalineado y trazabilidad de aspectos), lo cual documenta honestamente en `docs/correcciones.md`.
- La celda Evidencia de `docs/aspectos.md` enlaza a `correcciones-feedback.md`, que no existe (el archivo real es `docs/correcciones.md`): enlace roto.
- `docs/ia.md` no tiene entrada para el trabajo de corrección de esta semana.
- Nombres de archivo de arc42 con espacios y tildes persisten desde S1.

## Correcciones del equipo

`docs/correcciones.md` (no está en la raíz, sino en `docs/`) no contradice ninguna fila de la revisión preliminar publicada: es un documento de "corrección de feedback" que describe ajustes a C4 y a `docs/aspectos.md`, y en su §5 **confirma expresamente** que no se formuló un reto ni una restricción nueva para este corte. No hay puntos que adjudicar como Aceptada/Rechazada porque el documento no disputa hallazgos — los corrige donde aplica (C4, trazabilidad) y admite el resto. Esas correcciones ya quedaron reflejadas arriba (fila "Cadena aspecto→...→evidencia" y matriz transversal de estructura).

| Corrección | Adjudicación | Justificación |
|---|---|---|
| (ninguna disputa formal presentada) | No aplica | `docs/correcciones.md` es un registro de cambios hechos, no una impugnación de la revisión preliminar; su contenido se verificó directamente en el repo y se incorporó a la matriz. |

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada al equipo para el Corte 1, y por qué el trabajo de la noche del cierre se limitó a corregir feedback de S4 en lugar de abordarla?
2. ¿Qué herramienta de IA (si alguna) se usó para las correcciones de C4 y `docs/aspectos.md` del 2026-09-06, y por qué no quedó registrada en `docs/ia.md`?
3. ¿Cómo pretenden completar diagnóstico, ADR, cambio y medición del reto antes de la sustentación?
