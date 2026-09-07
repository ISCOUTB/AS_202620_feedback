# Primer corte · reto de línea base arquitectónica · Verifacts

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión manual preliminar
> hecha antes del cierre (2026-09-02). Se repite sobre el estado admisible tras
> `2026-09-07T05:00:00Z`.

## Hallazgo crítico: el repositorio calificado ya no es accesible

| Campo | Valor |
|---|---|
| Repositorio esperado | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado a la fecha de esta revisión | **No accesible.** `git clone` falla ("could not read Username"); la API devuelve `404 Not Found`; el listado completo y paginado de los 191 repositorios públicos de la organización `ISCOUTB` (`GET /orgs/ISCOUTB/repos`, dos páginas, `public_repos: 191`) **no contiene ningún repositorio con "Verifacts" en el nombre**, ni variantes de mayúsculas o guiones probadas (`AS_202620_VeriFacts`, `AS_202620_Verifacts2`, `AS_202620-Verifacts`, `AS_202620_veriFacts`) |
| Última vez visto accesible | 2026-09-02T13:32:53-05:00, commit `8764f9f1684560bddb9a61e07ffa0d1249b8199d` (revisión preliminar) |
| Búsqueda de rastro | `GET /search/commits?q=hash:8764f9f…` → 0 resultados; búsqueda de repositorios públicos por "verifacts" en todo GitHub no devuelve ninguna copia con ese historial |
| Repo personal hallado | `https://github.com/PedroC1213/Verifacts` (público) — **no es el mismo proyecto**: 12 commits, todos entre 2026-08-07 y 2026-08-16 (`bf6d4a7` es el último), es decir **anterior** incluso al primer commit conocido del repositorio de la organización (2026-08-18, según `EQUIPOS.md`). Contiene solo `README.md`, `docs/` (aspectos, IA, restricciones, árbol de utilidad, C4 de contexto) y un PDF de resumen — un estado embrionario de S1/S2, sin corte vertical, sin ADR, sin pruebas, sin CI. No se puede usar como sustituto del estado que debía calificarse. |
| `correcciones.md` | No se pudo comprobar (repositorio inaccesible); tampoco está en el repo personal de Pedro |

**No se puede calificar el corte 1 de este equipo desde el repositorio.** El repositorio que la
revisión preliminar evaluó el 2026-09-02 (commit `8764f9f`, con corte vertical, `POST /analysis`,
pruebas y documentación descritos en esa revisión) desapareció de la organización `ISCOUTB` en
algún momento entre esa fecha y el cierre. No podemos determinar desde fuera si fue borrado,
transferido fuera de la organización o puesto en privado — cualquiera de las tres deja el
repositorio inaccesible para un evaluador externo, que es como debe poder verse un repositorio
público según el CONTRATO §1. Esto **no es una desviación menor de nombre o de estructura: es la
pérdida de la entrega misma.**

## Matriz de la ficha

Todas las filas quedan **No verificado** por la razón anterior, salvo la primera y la última,
que sí se pueden decidir con la evidencia disponible.

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | El repositorio no es accesible; no se puede comprobar `git tag` | No cumple | Sin importar si existía o no la etiqueta, el estado no es verificable ahora mismo. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Fuera del alcance de este kit (Moodle); no hay repositorio que contrastar | No verificado | Debe comprobarse en Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | Repositorio inaccesible | No verificado | No se puede leer ningún artefacto del estado calificado. |
| Línea base medida y verificable antes del cambio | Repositorio inaccesible | No verificado | Ídem. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Repositorio inaccesible | No verificado | Ídem. |
| Cambio implementado y ejecutable de extremo a extremo | Repositorio inaccesible | No verificado | Ídem. |
| Límites declarados conservados tras el cambio | Repositorio inaccesible | No verificado | Ídem. |
| Prueba que cubre el cambio, en verde en el pipeline | Repositorio inaccesible; no se pudo consultar Actions sin el nombre del repositorio válido | No verificado | Ídem. |
| Resultado contrastado con el umbral del escenario y reproducible | Repositorio inaccesible | No verificado | Ídem. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | Repositorio inaccesible | No verificado | Ídem. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | Repositorio inaccesible | No verificado | Ídem. |
| Sustentación del reto | No verificable desde el repositorio bajo ninguna circunstancia | No verificado | Lo fija el docente; en este caso además es la única vía posible para que el equipo demuestre su trabajo, dado que el repositorio no está disponible. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_Verifacts` responde 404 vía API y clon anónimo; ausente de los 191 repositorios públicos listados de la organización | No cumple | Hallazgo crítico: el repositorio no está donde debía estar. |
| Estructura mínima presente | No verificable | No verificado | Repositorio inaccesible. |
| Estado calificado identificable | No verificable | No verificado | Repositorio inaccesible. |
| Nombres de ADR según la convención | No verificable | No verificado | Repositorio inaccesible. |
| ADR aceptados no reescritos | No verificable | No verificado | Repositorio inaccesible. |
| `docs/ia.md` al día para la semana | No verificable | No verificado | Repositorio inaccesible. |
| Sin credenciales en el repositorio ni en el historial | No verificable | No verificado | Repositorio inaccesible. |
| Contribución de todos los integrantes | No verificable | No verificado | Repositorio inaccesible. |

## Estado global del proyecto en HEAD

- **No hay HEAD que evaluar.** El repositorio de la organización no responde. La última fotografía disponible es la de la revisión preliminar del 2026-09-02, que describía una base S4 completada tarde (corte vertical con `POST /analysis`, pruebas), pero sin evidencia S5 (sin etiqueta, sin ADR del reto, sin medición, `docs/ia.md` desactualizado desde el 2026-08-24) y con autoría concentrada en un solo integrante confirmado y un segundo con pocas contribuciones, y un tercer integrante sin ningún commit.
- El único repositorio público con "Verifacts" atribuible a un integrante del equipo (`PedroC1213/Verifacts`) es un borrador temprano, anterior incluso al arranque del repositorio de curso, y no permite reconstruir el estado perdido.
- **Se recomienda contactar urgentemente al equipo y a la organización de GitHub** para esclarecer qué ocurrió con el repositorio antes de aplicar cualquier nota, y confirmar si existe una copia accesible (por ejemplo, en un fork privado que el equipo pueda hacer público, o restaurando el repositorio si fue borrado por error).

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | No evaluable | — | Repositorio inaccesible. |
| Alternativas y decisión | No evaluable | — | Repositorio inaccesible. |
| Aplicación sobre el corte vertical | No evaluable | — | Repositorio inaccesible. |
| Pruebas, medición y trazabilidad | No evaluable | — | Repositorio inaccesible. |
| Sustentación del reto | Pendiente del docente | — | No verificable desde el repositorio. |
| **Subtotal técnico** |  | **No evaluable** | El equipo debe restablecer el acceso al repositorio antes de poder calificar el corte. |

## Recuento

0 de 12 criterios de la ficha se pueden marcar "Cumple" (1 "No cumple" por la etiqueta ausente en un repositorio inaccesible; el resto "No verificado" por la misma razón). En la matriz transversal: 1 "No cumple", 7 "No verificado".

## No verificado

- Prácticamente toda la matriz de la ficha y la matriz transversal, porque el repositorio de la organización no es accesible desde el 2026-09-02 hasta la fecha de esta revisión (2026-09-07).
- Si el repositorio fue transferido, borrado o puesto en privado, y en qué fecha exacta.
- Si `PedroC1213/Verifacts` guarda alguna relación real con el proyecto de curso más allá del nombre.

## Hallazgos

- **Crítico:** el repositorio `ISCOUTB/AS_202620_Verifacts` no existe en la organización a la fecha de esta revisión (191/191 repositorios públicos listados, ninguno coincide); tampoco resuelve por clon anónimo ni por la API. Esto bloquea la calificación completa del corte 1 desde el repositorio.
- El único repositorio público relacionado por nombre y por integrante (`PedroC1213/Verifacts`) es un borrador embrionario de agosto, anterior al propio arranque del repositorio de curso, y no sustituye la evidencia perdida.
- Este hallazgo debe escalarse al docente antes de aplicar cualquier nota: puede tratarse de un error operativo (transferencia accidental, cambio de visibilidad) más que de una decisión del equipo, y el plazo para restablecerlo debería resolverse con criterio humano, no solo con esta revisión automatizada.

## Preguntas para la sustentación

- ¿Qué pasó con el repositorio `ISCOUTB/AS_202620_Verifacts`? ¿Fue transferido, puesto en privado o borrado, y cuándo?
- ¿Pueden restablecer el acceso público al repositorio con su historial completo intacto, para que se pueda verificar que no hubo alteración retroactiva?
- Dado que no se puede verificar nada del corte 1 desde el repositorio, ¿pueden presentar en la sesión el diagnóstico, el ADR, el cambio y la medición que preparó el equipo?
