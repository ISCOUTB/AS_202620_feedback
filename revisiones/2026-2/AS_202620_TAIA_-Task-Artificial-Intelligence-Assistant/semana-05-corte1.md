# semana-05-corte1 · TAIA

> Revisión DEFINITIVA post-cierre, realizada el 2026-09-07. Reemplaza la revisión manual preliminar del 2026-09-03. Cierre de la actividad: `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | No existe la etiqueta `corte-1` (solo existe `corrections-s4`). Se revisó el último commit ≤ cierre: `a3f4d826dd90bfc7e29ff9eb7d944b71ca99ecf7` (2026-09-06T04:13:11-05:00 = 2026-09-06T09:13:11Z), que también es HEAD | 
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log` (fallback, HEAD, ventana S4→HEAD); `git ls-tree` de `docs/adr`; `git show` de `docs/ia.md`, `docs/aspectos.md`, `correcciones.md`; `git grep` (patrón de credenciales, §9); `git shortlog -sne`; `curl` a `actions/runs?per_page=10` (una sola llamada) |
| Revisor | revisión manual local, solo lectura; no se ejecutó código estudiantil |
| `correcciones.md` | Existe en HEAD, pero versa sobre las semanas 1 a 4 ("Justificación de la calificación de las semanas 1 a 4"), no sobre el corte 1. No contiene ningún punto que contradiga la matriz preliminar de este corte. Se resume abajo y se marca fuera de alcance. |

## Qué se hizo en la ventana del corte (S4 → cierre)

```
a3f4d82 2026-09-06T04:13:11-05:00  feat: update ia.md and add corrections.md based on automated evaluation feedback
c8796c7 2026-09-06T02:11:19-05:00  docs: complete arc42 architecture views
ce99b54 2026-09-06T01:47:31-05:00  ci: fix pytest root configuration
2f3ca0d 2026-09-06T01:39:22-05:00  ci: configure automated test workflow
bda515c 2026-09-06T01:35:51-05:00  ci: add automated test workflow
1668579 2026-09-06T01:29:55-05:00  feat: update name, remove templates, and translate titles to Spanish in arc42
42c5b03 2026-09-06T00:20:34-05:00  feat: add traceability section to architectural decision record for Adr-01
c087303 2026-08-30T18:54:10-05:00  docs: change prueba (readme) add ia entry (ia.md) change c2 text  ← commit calificado en la preliminar de S4
```
Todos los commits nuevos (2026-09-06) son: completar el arc42, configurar por primera vez un pipeline de CI, y escribir `correcciones.md`/actualizar `docs/ia.md` justificando las notas de S1-S4. **Ninguno de estos commits responde al reto del corte 1**: no hay ADR nuevo, no hay diagnóstico de una restricción, no hay cambio de código de dominio, no hay medición contra un umbral.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` → solo `corrections-s4`; no existe `corte-1` | No cumple | Se revisó el último commit admisible, `a3f4d82` (2026-09-06T09:13:11Z) |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No accesible desde el repositorio | No verificado | Depende del adjunto de Moodle |
| Impacto de la restricción localizado en requisitos, C4 y código | Ningún documento del árbol nombra una restricción nueva; `docs/adr/` sigue con un único ADR de agosto | No cumple | Sin indicio de diagnóstico de una restricción nueva |
| Línea base medida y verificable antes del cambio | Sin archivo de medición ni cifra en el árbol | No cumple | No hay herramienta ni procedimiento documentado |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `git ls-tree HEAD:docs/adr` → solo `0001-estilo-arquitectonico.md`; el commit `42c5b03` solo añadió una sección de trazabilidad al ADR existente | No cumple | No existe ADR del reto; el ADR 0001 se editó, pero no es un ADR nuevo del reto |
| Cambio implementado y ejecutable de extremo a extremo | Los commits de la ventana son documentación (arc42, ia.md) y configuración de CI; ningún archivo bajo `backend/app/` o dominio cambia | No cumple | No hay cambio de código atribuible a un reto de restricción |
| Límites declarados conservados tras el cambio | Sin cambio del reto que comparar | No cumple | No aplica: sin cambio no hay límites que verificar |
| Prueba que cubre el cambio, en verde en el pipeline | `curl -s .../actions/runs?per_page=10` → primer pipeline de la historia del repositorio, con 2 fallos (`2f3ca0da`, `bda515c1`) y luego 4 éxitos, el último sobre `a3f4d826` en `2026-09-06T09:22:42Z`, antes del cierre | No cumple | El pipeline por fin corre y termina en verde, pero cubre las pruebas existentes del corte vertical de S4, no un cambio nuevo del reto |
| Resultado contrastado con el umbral del escenario y reproducible | Sin medición en el árbol | No cumple | No hay umbral ni cifra que contrastar |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md` tiene una sola fila (A-01), sin cambios en la ventana, referida al corte vertical de S4 | No cumple | No hay fila del reto que recorrer |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md` actualizado en `a3f4d82`, pero su contenido nuevo documenta el proceso de escribir `correcciones.md` (justificación de S1-S4), no una salida de IA sobre el reto de este corte | No cumple | Ninguna entrada se refiere al diagnóstico, ADR o medición de un reto nuevo |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| a. Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant`, clon anónimo exitoso | Cumple | — |
| b. Estructura mínima presente | README.md, docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md presentes | Cumple | — |
| c. Estado calificado identificable | Sin etiqueta; se usó el último commit ≤ cierre, `a3f4d82`, identificable y documentado | Cumple | Identificable pese a no haber etiqueta |
| Versionado (commit anterior al cierre) | No existe `corte-1` | No cumple | Falta el estado versionado exigido por la ficha |
| d. Nombres de ADR según la convención | `0001-estilo-arquitectonico.md` cumple el patrón | Cumple | Único ADR del repositorio |
| e. ADR aceptados no reescritos | El commit `42c5b03` **edita** el ADR 0001 (añade sección de trazabilidad) en vez de crear uno nuevo o declarar reemplazo | No cumple | CONTRATO §4: un ADR aceptado no se edita; si cambia, se escribe otro y el anterior queda "reemplazado" con enlace. Aquí no hay ni ADR nuevo ni marca de reemplazo |
| f. `docs/ia.md` al día para la semana | Última entrada (2026-09-06) documenta la redacción de `correcciones.md` sobre S1-S4, no trabajo nuevo de código o arquitectura de esta semana | No cumple | No hay entrada referida al reto del corte 1 |
| g. Sin credenciales en el repositorio ni en el historial | `git grep` (patrón AKIA/BEGIN.../ghp_/xox.../sk-/password/secret/token/api_key) sobre HEAD: sin coincidencias | Cumple | — |
| h. Contribución de todos los integrantes | `git shortlog -sne HEAD`: val (17+2 con dos correos), dei0811 (8), mark (3), luis20072002 (1) — los 4 integrantes declarados aparecen | Cumple | val firma con dos correos (`@gmail.com` y `@email.com`); se consolida como una sola persona |

## Estado global del proyecto (overall · revisado en HEAD)

- **HEAD revisado**: `a3f4d826dd90bfc7e29ff9eb7d944b71ca99ecf7` (2026-09-06T04:13:11-05:00), *"feat: update ia.md and add corrections.md based on automated evaluation feedback"*
- **Veredicto**: con pendientes
- Resumen: en la última noche antes del cierre el equipo hizo un trabajo real pero dirigido a otra cosa: completó el arc42, montó por primera vez un pipeline de CI (con dos intentos fallidos antes de dejarlo en verde) y escribió un documento extenso justificando las notas de las semanas 1 a 4. Ese esfuerzo no se tradujo en una respuesta al reto de este corte: no hay restricción diagnosticada, ADR nuevo, cambio de código ni medición. Además, la única edición sobre el ADR existente lo modifica sin marcarlo como reemplazado, lo que incumple la regla de no editar ADR aceptados.

Pendientes que siguen abiertos:
- Diagnosticar la restricción asignada (o, si nunca llegó, alguna del arc42) con una línea base medida.
- Escribir el ADR del reto (nuevo, no una edición del 0001) con alternativas, fuerzas, decisión y consecuencias.
- Implementar el cambio sobre el corte vertical existente y ejecutar las pruebas correspondientes.
- Medir el resultado contra el umbral del escenario.
- Crear la etiqueta `corte-1`.
- Referir `docs/ia.md` y `docs/aspectos.md` al trabajo del reto.
- Corregir la edición del ADR-0001: o se revierte, o se declara "reemplazado" y se crea el ADR nuevo correspondiente.
- Adjuntar el PDF de dos páginas en Moodle.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia evaluable del reto | 0,00 | No se identifica una respuesta a una restricción nueva |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | El único ADR es de agosto y se editó, no se reemplazó, para añadir trazabilidad ajena al reto |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | Ningún cambio de código en la ventana corresponde a una restricción nueva |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | El pipeline por fin corre en verde, pero sobre las pruebas existentes, no sobre un cambio del reto |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio |
| **Subtotal técnico verificable** | | **0,00 / 4,00** | No constituye el total sobre 5,00 |

## Recuento

0 de 12 criterios Cumple (2 No verificado, 10 No cumple).

## No verificado / pendientes

- PDF adjunto en Moodle.
- Sustentación del reto.

## Hallazgos para la planilla

- No existe la etiqueta `corte-1`; se revisó el último commit admisible, `a3f4d82` (2026-09-06T09:13:11Z), que coincide con HEAD.
- El equipo dedicó la última noche a completar arc42, montar CI por primera vez (ahora en verde) y escribir `correcciones.md` sobre S1-S4, pero no atacó el reto del corte 1.
- El commit `42c5b03` edita el ADR-0001 aceptado (añade trazabilidad) sin crear un ADR nuevo ni marcarlo como reemplazado: incumple CONTRATO §4.
- `correcciones.md` existe pero no contradice ningún punto de la revisión preliminar del corte 1; versa sobre S1-S4, fuera del alcance de esta revisión.
- Mejora real respecto a la preliminar: ahora hay pipeline de CI configurado y en verde (antes no existía `.github/workflows`).
- `docs/aspectos.md` sigue con una sola fila (A-01, corte vertical de S4); no hay fila del reto.

## Preguntas para la sustentación

1. ¿Qué restricción se les asignó, y por qué el trabajo de la última noche se dirigió a completar S1-S4 en vez de al reto del corte 1?
2. ¿Por qué se editó el ADR-0001 en vez de crear un ADR nuevo, y el equipo lo entiende como una violación de la regla de "ADR aceptado no se edita"?
3. Con el pipeline ya en verde, ¿qué haría falta para escribir la prueba y la medición del reto, y en qué escenario de calidad se apoyaría?
