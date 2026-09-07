# Primer corte · reto de línea base arquitectónica · TRACTAR

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión manual preliminar
> hecha antes del cierre (2026-09-03). Se repite sobre el estado admisible tras
> `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` (redirige a `AS_202620_UTB_TRACKER`, mismo repositorio) |
| Etiqueta `corte-1` | Ausente — `git tag --list` no devuelve etiquetas |
| Estado calificado (fallback) | `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849` · 2026-08-31T12:27:23-05:00 · "Fix: solved the text problem" (último commit ≤ cierre; también es HEAD: no hubo commits nuevos entre el 2026-09-03 y el cierre) |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`, `git tag --list`, `git log -1 --until=cierre HEAD`, `git log` completo, `ls docs/adr`, `git log --follow` sobre cada ADR, `tail docs/ia.md`, `cat docs/aspectos.md`, `git shortlog -sne HEAD`, `git grep` de credenciales, `git ls-files` para `.env`, `curl` a la API de Actions (con redirect al repo renombrado) |
| `correcciones.md` | No existe en el repositorio (ni en el estado calificado ni en HEAD) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` vacío; se usa el fallback `7cfb872` (anterior al cierre) | No cumple | Sin etiqueta. El fallback coincide con el HEAD actual: el equipo no publicó nada nuevo entre la revisión preliminar y el cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay PDF versionado en el repositorio; Moodle está fuera del alcance de este kit | No verificado | Debe comprobarse en Moodle; no sustituye la ausencia de evidencia en el repo (CONTRATO §12). |
| Impacto de la restricción localizado en requisitos, C4 y código | Los commits de S5 (`292aea7`, `7cfb872`) corrigen texto de C4 y arreglan una errata; no hay commit ni sección que declare una restricción nueva asignada, ni el escenario de calidad que afecta | No cumple | No se pudo ubicar cuál fue la restricción asignada al equipo (no está en el kit ni en el repo). |
| Línea base medida y verificable antes del cambio | `docs/arc42/arc42.md` declara escenarios y umbrales (ej. tiempo de respuesta), pero ninguna sección aporta una cifra medida con herramienta y procedimiento para el reto | No cumple | Un umbral planeado no es una línea base medida. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/0001-estilo-arquitectonico.md` y `0002-cambio-stack-fastapi-flutter.md` son de S3/S4 (estilo y stack); ninguno nuevo apareció en S5 | No cumple | `git log --diff-filter=A -- docs/adr/` no muestra ADR creado en la ventana S5. |
| Cambio implementado y ejecutable de extremo a extremo | Los tres commits de S5 (`e88a3d6`, `292aea7`, `7cfb872`) son "S4 Advances", corrección de C4 y corrección de texto — documentales/tardíos de S4, no una respuesta a un reto nuevo | No cumple | No hay commit atribuible a diagnosticar-decidir-implementar un reto. |
| Límites declarados conservados tras el cambio | `docs/c4/` describe la línea base actual; no existe un cambio del reto que comparar contra el C4 | No verificado | No aplica evaluarlo sin un cambio identificado. |
| Prueba que cubre el cambio, en verde en el pipeline | El run del commit HEAD `7cfb8729` concluyó `success` (`https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/33419672964`); cubre la suite existente, no una prueba nueva del reto | No cumple | El pipeline en verde certifica la base, no una prueba del reto (que no existe). |
| Resultado contrastado con el umbral del escenario y reproducible | No se encontró ninguna medición posterior a un cambio, con herramienta/carga/procedimiento | No cumple | Nada que contrastar. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md` mantiene las filas A-01 a A-06 de la línea base S4; ninguna fila nueva corresponde al reto S5 | No cumple | No hay fila del corte 1. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md` (2 entradas) sin cambios desde `e84871f` (2026-08-16); ambas entradas son de S2 | No cumple | Sin registro de IA referido al trabajo de este corte. |
| Sustentación del reto | No verificable desde el repositorio | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo exitoso; GitHub redirige `AS_202620_TRACTAR` → `AS_202620_UTB_TRACKER` (mismo repo, renombrado) | Cumple | El nombre del repo cambió respecto a la convención `AS_202620_<PROYECTO>`; conviene actualizar la referencia en EQUIPOS.md, pero sigue siendo público y localizable. |
| Estructura mínima presente | `git ls-tree` en HEAD muestra `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`, `README.md` | Cumple | Las seis rutas están. |
| Estado calificado identificable | Sin etiqueta `corte-1`; fallback `7cfb872` = HEAD, anterior al cierre | No cumple | Falta la etiqueta exigida por el corte. |
| Nombres de ADR según la convención | `0001-estilo-arquitectonico.md`, `0002-cambio-stack-fastapi-flutter.md` | Cumple | Ambos siguen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | `git log --follow` sobre cada ADR muestra un solo commit (el de creación) para cada archivo; no hay ediciones posteriores | Cumple | Se corrige la revisión preliminar: no se encontró reescritura de un ADR ya aceptado; el cambio de nombre del proyecto (Tractar → UTB Tracker) no tocó estos archivos. |
| `docs/ia.md` al día para la semana | Último cambio `e84871f`, 2026-08-16 | No cumple | Sin entrada de S5. |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE …` sobre HEAD: código de salida 1 (sin coincidencias); `git ls-files \| grep '\.env$'`: sin resultado | Cumple | Sin hallazgos. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: 13+7 commits de "Sebastian Garcia Devoz"/"Sebas" (mismo correo) + 1 de correo institucional = una sola persona con tres identidades; Joriel Barros, Geronimo Cadena y Mateo Millan sin commits | No cumple | Persiste desde S1: solo un integrante de cuatro tiene contribución visible. |

## Estado global del proyecto en HEAD

- HEAD = fallback `7cfb872` (no hay commits posteriores a la revisión preliminar; el equipo no volvió a tocar el repositorio antes del cierre).
- El proyecto conserva la base documental de S2-S4 (arc42, C4, dos ADR, `docs/aspectos.md`) y pipeline en verde a HEAD, pero **no hay ninguna evidencia identificable de una respuesta al reto del corte 1**: sin restricción diagnosticada, sin ADR nuevo, sin cambio, sin medición, sin fila de trazabilidad nueva, sin entrada de IA del corte.
- La autoría sigue concentrada en un solo integrante (con tres identidades de git); el hallazgo es idéntico al de S1-S4 y sigue sin resolverse.
- No se pudo ubicar la restricción asignada a este equipo en ningún artefacto del kit ni del repositorio.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | No hay diagnóstico ni línea base medida del reto. |
| Alternativas y decisión | Insuficiente | 0,00 | No existe ADR identificable del reto. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | No se identifica un cambio S5 sobre el corte vertical. |
| Pruebas, medición y trazabilidad | Insuficiente | 0,00 | Sin prueba nueva, sin medición, sin fila de trazabilidad del reto. |
| Sustentación del reto | Pendiente del docente | — | No verificable desde el repositorio. |
| **Subtotal técnico** |  | **0,00 / 4,00** | Propuesta al docente; no es la nota final. |

## Recuento

0 de 12 criterios de la ficha cumplen (matriz de la ficha). En la matriz transversal: 4 de 8 cumplen.

## No verificado

- PDF de dos páginas en Moodle (fuera del alcance de este kit).
- Límites del C4 tras el cambio (no hay cambio del reto que comparar).
- Sustentación del reto.

## Hallazgos

- Sin etiqueta `corte-1`; se calificó sobre el último commit ≤ cierre (`7cfb872`), idéntico al HEAD actual.
- No hay ninguna respuesta identificable al reto del corte 1: ni diagnóstico, ni ADR, ni cambio, ni medición, ni entrada de IA referida a este corte.
- La restricción asignada al equipo no se pudo ubicar en el kit ni en el repositorio.
- La contribución sigue concentrada en un solo integrante (tres identidades de git de la misma persona); tres integrantes sin commits en todo el semestre.
- El repositorio fue renombrado de `AS_202620_TRACTAR` a `AS_202620_UTB_TRACKER` (GitHub redirige); sigue siendo público y accesible.

## Preguntas para la sustentación

- ¿Cuál fue la restricción asignada al equipo y dónde está su diagnóstico con estado inicial medido?
- ¿Qué alternativas se compararon para responder al reto y por qué no quedaron registradas en un ADR?
- ¿Por qué no existe la etiqueta `corte-1` y por qué el repositorio no tuvo actividad entre la revisión preliminar (2026-09-03) y el cierre (2026-09-07)?
- ¿Cómo se distribuyó el trabajo entre los cuatro integrantes, dado que el historial solo muestra commits de uno?
