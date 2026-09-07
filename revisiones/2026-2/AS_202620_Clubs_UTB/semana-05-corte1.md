# semana-05-corte1 · Clubs UTB

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03. No existe la etiqueta `corte-1`; se calificó el último commit anterior al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado calificado | sin etiqueta `corte-1`; último commit ≤ cierre: `4ede977c7cccc335d878019ce06cba2e23cf76d2` (`2026-09-06T22:41:55-05:00`, *quite el C2 y lo reemplaze con el C3*) |
| Cierre | `2026-09-07T05:00:00Z` |
| Comandos ejecutados | `git tag --list` (vacío); `git log -1 --until=... HEAD`; `git ls-tree -r --name-only`; `git log --format=...` completo; `git log --diff-filter=A -- docs/adr/`; `git show --stat` de los dos últimos commits; `git grep` de secretos (exit 1); `git shortlog -sne` |
| Restricción asignada | No disponible en el kit ni citada en el repositorio. |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| 1. Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` sin salida | **No cumple** | Se calificó el último commit ≤ cierre: `4ede977c`, `2026-09-06T22:41:55-05:00`. |
| 2. PDF de dos páginas | No hay PDF en el repositorio | **No verificado** | Debe comprobarse en Moodle. |
| 3. Impacto de la restricción en requisitos, C4 y código | `docs/aspectos.md` sigue con las filas U1-U3/C1-C3 de la línea base; sin restricción nueva declarada en `docs/arc42/02_restricciones.md` ni en ADR | **No cumple** | No hay diagnóstico de una restricción nueva. |
| 4. Línea base medida y verificable | Ninguna fila de `docs/aspectos.md` reporta una cifra medida con herramienta/procedimiento | **No cumple** | Todas las celdas de Código/Pruebas dicen "Pendiente" salvo U2. |
| 5. ADR del reto | Único ADR: `docs/adr/0001-hexagonal.md` (aceptado 23/08/2026, editado el 30/08 en `c6c46e3`) | **No cumple** | Es el ADR de la arquitectura base; no hay ADR del reto. |
| 6. Cambio implementado extremo a extremo | Últimos dos commits (`4cfcfb6` "Agregación de endpoint get y post para el corte vertical", `4ede977` "quite el C2 y lo reemplaze con el C3") añaden un router de publicaciones y editan una línea de `10_requisitos_de_calidad.md` | **No cumple** | El endpoint nuevo no está vinculado a ninguna restricción diagnosticada ni a `docs/aspectos.md`; el segundo commit es un cambio de una línea sin ADR ni trazabilidad. |
| 7. Límites C4 conservados | `docs/c4/contexto.md` (contexto y contenedores) no cambió en estos commits | **No verificado** | No hay cambio de arquitectura que contrastar contra el C4. |
| 8. Prueba que cubre el cambio, en verde en pipeline | `backend/tests/test_publicaciones.py` agregado junto al endpoint (`4cfcfb6`); CI ("Backend tests") en verde para `4cfcfb6e` (2026-09-06T23:58:26Z) y `4ede977c` (2026-09-07T03:42:14Z) | **No cumple** | Hay prueba y CI verde para el endpoint nuevo, pero el endpoint no responde a ninguna restricción diagnosticada: no hay "cambio del reto" que cubrir. |
| 9. Resultado contrastado con umbral | Sin medición ni umbral reportado para ningún escenario | **No cumple** | — |
| 10. Cadena de trazabilidad navegable | `docs/aspectos.md` tiene 7 columnas (`ID…Pruebas`), sin columna `Evidencia`; la fila U2 llega a ADR y código, las demás terminan en "Pendiente" | **No cumple** | Falta la columna Evidencia (desviación de estructura) y la cadena no llega a un aspecto del reto. |
| 11. Salida de IA con motivo técnico, de este corte | `docs/ia.md` solo tiene registros hasta S3-S4; sin commit sobre `docs/ia.md` desde entonces | **No cumple** | Sin entrada de S5. |
| 12. Sustentación del reto | — | **No verificado** | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| a. Repositorio en la organización, convención y público | Clon anónimo exitoso de `github.com/ISCOUTB/AS_202620_Clubs_UTB` | **Cumple** | — |
| b. Estructura mínima | `git ls-tree` en `4ede977c`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` presentes | **Cumple** | `docs/c4/` contiene un solo archivo `contexto.md` con ambos niveles (desviación de organización, no de contenido). |
| c. Estado calificado identificable | Sin etiqueta; `4ede977c`, `2026-09-06T22:41:55-05:00` | **No cumple** | Falta la etiqueta `corte-1` exigida por la ficha. |
| d. Nombres de ADR según convención | `docs/adr/0001-hexagonal.md` | **Cumple** | — |
| e. ADR aceptados no reescritos | ADR-0001 aceptado el 23/08/2026; editado en `c6c46e3` (30/08/2026, "correción de feedback") sin nuevo ADR ni marca de reemplazo | **No cumple** | Se modificó contenido de un ADR ya aceptado en lugar de escribir uno nuevo. |
| f. `docs/ia.md` al día para la semana | Última entrada visible es de S3-S4 | **No cumple** | Sin entrada de S5. |
| g. Sin credenciales | `git grep` con la regex del contrato: exit 1; sin `.env` versionado | **Cumple** | — |
| h. Contribución de todos los integrantes | `git shortlog -sne 4ede977c`: Zavod Dev 37, Josh Ortega/Josh4OP 19, Luis-Salas-Reyes/Luis Daniel 10, deortahollman-star 5 | **Cumple** | 4 identidades consolidadas para 4 integrantes; distribución desigual (Zavod Dev concentra ~57% de los commits), anotar para la sustentación. |

## Estado global del proyecto (overall · HEAD)

HEAD coincide con el estado calificado (`4ede977c`). Entre el cierre de S4 y el cierre de S5 el equipo solo agregó un endpoint CRUD de publicaciones con su prueba (ambos con CI en verde) y corrigió una referencia de una línea en `10_requisitos_de_calidad.md`. No hay ningún artefacto (ADR, aspecto, medición) que documente una restricción nueva asignada para este corte, ni se creó la etiqueta `corte-1`. La línea base de S1-S4 se mantiene sin deterioro visible.

## Nivel de rúbrica sugerido (propuesta al docente)

| Criterio | Nivel | Puntaje | Evidencia |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia | 0,00 | No hay diagnóstico de restricción nueva en ningún artefacto. |
| Alternativas y decisión | Sin evidencia | 0,00 | El único ADR es el de arquitectura hexagonal (línea base). |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | El endpoint agregado no está ligado a una restricción diagnosticada. |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | Hay CI verde, pero sobre una funcionalidad sin trazabilidad a un aspecto de calidad medido. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico verificable** | | **0,00 / 4,00** | La nota final la fija Moodle. |

## Recuento

**0 de 12 criterios Cumple.**

## No verificado

- PDF adjunto en Moodle.
- Coincidencia del diagnóstico con la restricción asignada (no disponible).
- Conservación de límites C4 (no hay cambio de arquitectura que contrastar).
- Sustentación del reto.

## Hallazgos

- No existe la etiqueta `corte-1`; se calificó el último commit anterior al cierre.
- No hay evidencia de que el equipo haya recibido o diagnosticado una restricción nueva.
- El único cambio funcional de S5 (endpoint de publicaciones) no está vinculado a ningún aspecto de calidad ni ADR.
- El ADR-0001, ya aceptado, fue editado después de su aceptación sin registrar un ADR de reemplazo (arrastrado de la revisión preliminar).
- `docs/aspectos.md` carece de la columna Evidencia y mantiene la mayoría de sus filas en "Pendiente".
- `docs/ia.md` no tiene ninguna entrada de S5.
- Distribución de commits desigual entre los cuatro integrantes (un integrante concentra más de la mitad).

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada, y por qué el endpoint de publicaciones agregado en los últimos commits no se documenta como respuesta a ella?
2. ¿Por qué no se creó la etiqueta `corte-1` antes del cierre, y a qué commit habría correspondido?
3. ¿Qué motivó la edición del ADR-0001 (ya aceptado) en lugar de escribir un ADR nuevo que lo reemplazara?
