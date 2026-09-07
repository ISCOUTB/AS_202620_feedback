# semana-05-corte1 · Drift

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03. No existe la etiqueta `corte-1`; se calificó el último commit anterior al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado calificado | sin etiqueta `corte-1`; último commit ≤ cierre: `d110d6d0dd4ebfbb1e37af4ce8b6ce95eb0cb039` (`2026-09-06T23:34:21-05:00`, *test: add vertical slice search test*) |
| Cierre | `2026-09-07T05:00:00Z` |
| HEAD (real, tras el cierre) | `c12dda8e104a810ea3fdcce4565126cbbda08a52` (`2026-09-07T01:26:25-05:00` → `2026-09-07T06:26:25Z`, posterior al cierre); tres commits más entre el estado calificado y HEAD |
| Comandos ejecutados | `git tag --list` (vacío); `git log --until=... HEAD`; `git ls-tree -r --name-only`; `git log --diff-filter=A -- docs/adr/`; `git log --follow` sobre los ADR; lectura de `docs/aspectos.md`, `docs/escenarios.md`, `docs/ia.md`, `docs/correciones.md`, `backend/tests/`; `git grep` de secretos (exit 1); `git shortlog -sne`; `curl .../actions/runs?per_page=30` (1 llamada) |
| Restricción asignada | No disponible en el kit ni citada explícitamente como tal en el repositorio. |

El equipo tiene un archivo de correcciones en `docs/correciones.md` (nombre y ruta distintos de `correcciones.md` en la raíz, se toma igual como el documento de correcciones del equipo); se adjudica en la sección dedicada más abajo.

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| 1. Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` sin salida | **No cumple** | El propio `docs/correciones.md` (punto 11) reconoce que la etiqueta está "Pendiente" y describe los comandos para crearla; nunca se ejecutaron. |
| 2. PDF de dos páginas | No hay PDF en el repositorio | **No verificado** | Debe comprobarse en Moodle. |
| 3. Impacto de la restricción en requisitos, C4 y código | `docs/aspectos.md` y `docs/escenarios.md` siguen describiendo E1-E5 de la línea base (mantenibilidad, rendimiento, etc.); ningún artefacto declara una restricción nueva | **No cumple** | El propio `docs/correciones.md` (punto 12) reconoce que el "ADR del reto" está "Pendiente" porque la restricción "será asignada para la evaluación". |
| 4. Línea base medida y verificable | `docs/escenarios.md` define umbrales (p.ej. E1 ≤3s p95, 50 usuarios concurrentes) y un método de verificación por escenario, pero sin ejecutar la medición | **No cumple** | `docs/correciones.md` (punto 13) lo reconoce como "Parcialmente corregido": método definido, medición real pendiente. |
| 5. ADR del reto | `docs/adr/` solo contiene 0001 y 0002, ambos "Selección de Arquitectura Base" (arquitectura hexagonal + cambio de stack Java/Spring → Next.js/FastAPI) | **No cumple** | Ninguno de los dos ADR responde a una restricción nueva asignada para este corte. |
| 6. Cambio implementado extremo a extremo | Últimos commits ≤ cierre: `test: add vertical slice search test` (`d110d6d`), y tras el cierre `fix: eliminar duplicacion...`, `Update README...`, `Document vertical cut...` | **No cumple** | Es una prueba y limpieza sobre el recorrido de búsqueda ya existente (ADR-0002), no un cambio ligado a una restricción nueva. |
| 7. Límites C4 conservados | `docs/c4/contexto.md` y `contenedores.md` no cambiaron en estos commits | **No verificado** | No hay cambio de arquitectura que contrastar. |
| 8. Prueba que cubre el cambio, en verde en pipeline | `curl .../actions/runs`: `d110d6d0` success (`2026-09-07T04:37:43Z`, antes del cierre) | **No cumple** | El run verde cubre la suite existente (`backend/tests/test_search_games.py`, `test_health.py`), no una prueba de una restricción nueva. |
| 9. Resultado contrastado con umbral | Sin medición ejecutada (ver criterio 4) | **No cumple** | — |
| 10. Cadena de trazabilidad navegable | `docs/aspectos.md` tiene 8 columnas (`ID…Evidencia`); siguiendo E1: llega a C4, ADR-0002, código y prueba, pero Evidencia = "Pendiente de medición de rendimiento" | **No cumple** | La cadena llega hasta la evidencia de calidad y se rompe ahí; no hay fila para una restricción nueva. |
| 11. Salida de IA con motivo técnico, de este corte | `docs/ia.md`, Registro 10 y 11 (06/09/2026): comando único de ejecución y organización de scripts, con un "Descartado" explícito y su motivo (mantener `start.py` en la raíz) | **Cumple** | Hay entradas fechadas dentro de la ventana de S5 con motivo técnico, aunque no tratan la restricción del reto sino tareas de arranque/organización. |
| 12. Sustentación del reto | — | **No verificado** | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| a. Repositorio en la organización, convención y público | Clon anónimo exitoso de `github.com/ISCOUTB/AS_202620_Drift` | **Cumple** | — |
| b. Estructura mínima | `git ls-tree` en `d110d6d0`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` presentes | **Cumple** | — |
| c. Estado calificado identificable | Sin etiqueta; `d110d6d0`, `2026-09-06T23:34:21-05:00` | **No cumple** | Falta la etiqueta `corte-1`; el equipo lo reconoce como pendiente en su propio `docs/correciones.md`. |
| d. Nombres de ADR según convención | `0001-arquitectura-base.md`, `0002-arquitectura-base.md` | **No cumple** | Ambos títulos enuncian el tema ("Arquitectura Base"), no la decisión que cada uno registra; hallazgo arrastrado de la revisión preliminar. |
| e. ADR aceptados no reescritos | ADR-0001 declara "Estado: Superada parcialmente por ADR-0002…"; ADR-0002 es un archivo nuevo con la decisión actualizada (stack tecnológico) y enlaza de vuelta a 0001 | **Cumple** | El patrón de reemplazo con enlace sí se siguió; corrige el hallazgo preliminar que solo constataba dos ADR sin evaluar la relación entre ellos. |
| f. `docs/ia.md` al día para la semana | Ver criterio 11 | **Cumple** | — |
| g. Sin credenciales | `git grep` con la regex del contrato: exit 1; sin `.env` versionado | **Cumple** | — |
| h. Contribución de todos los integrantes | `git shortlog -sne d110d6d0`: lmpdiaz12/Luis Mario Perez Diaz (misma persona) 67, JerryDBM/Sherry (misma persona) 65, JoshuaR01/JoshXX (misma persona) 56, maufern4ndez/Mauricio (misma persona) 49 | **Cumple** | 4 identidades consolidadas, participación razonablemente balanceada (rango 49-67), mejora respecto al desbalance de S3 (51 vs 9). |

## Estado global del proyecto (overall · HEAD)

HEAD (`c12dda8e`, `2026-09-07T06:26:25Z`) es **posterior al cierre**: tres commits (`dbb98d3`, `75881e4`, `e77a240`, `c12dda8`) llegaron después de `2026-09-07T05:00:00Z` y corrigen duplicación de código en las pruebas de búsqueda y documentan el proceso en `ia.md`. No se evaluaron para la nota porque son posteriores al cierre; se listan aquí porque el CONTRATO pide notar entregas tardías. El repositorio, en su estado calificado, tiene una línea base considerablemente mejorada frente a la revisión preliminar (aspectos.md con 8 columnas, ia.md con rechazos, ADR con marca de reemplazo, CI con SonarCloud, README con comando único) pero **no ejecutó lo específico del reto de S5**: ni la etiqueta, ni el ADR de la restricción, ni la medición de línea base, tres puntos que el propio equipo reconoce pendientes en `docs/correciones.md`.

## Correcciones del equipo

`docs/correciones.md` responde punto por punto a la revisión preliminar de `semana-05-corte1.md` (2026-09-03). Se verificó cada punto contra el estado real del repositorio en el commit calificado (`d110d6d0`):

| Corrección (resumen) | Adjudicación | Justificación |
|---|---|---|
| 1, 8, 14. `docs/aspectos.md` con tabla de 8 columnas y trazabilidad | **Aceptada** | Verificado: `docs/aspectos.md` tiene la tabla de 8 columnas (`ID…Evidencia`) con las 5 filas E1-E5 completas. Corrige la fila "Cadena aspecto…navegable" de la matriz preliminar. |
| 2. Ficha del problema con tensiones de calidad | **Aceptada** | El aspecto de mantenibilidad y su justificación aparecen en `docs/aspectos.md`; no se profundizó más allá por estar fuera del alcance de corte1 (línea base). |
| 3. Desbalance de contribución (51 vs 9 en S3) | **Aceptada como hecho, no como corrección de fondo** | El desbalance de S3 es historia y no se recalifica; sí se confirma que en el estado actual (`d110d6d0`) la distribución mejoró a un rango 49-67 entre los 4 integrantes. |
| 4. README con arranque contradictorio | **Aceptada** | El README documenta backend (uvicorn/FastAPI) y frontend (Next.js) de forma consistente con el stack real (ADR-0002); ya no menciona Maven/Spring. |
| 5, 16. Pipeline/CI en verde | **Aceptada** | `curl .../actions/runs` confirma runs verdes para varios commits, incluido el estado calificado `d110d6d0` (2026-09-07T04:37:43Z, antes del cierre). |
| 6. Matriz de estilos con referencia a E1-E5 | **Aceptada** | `docs/aspectos.md` y `docs/escenarios.md` sí enlazan cada escenario a E1-E5. |
| 7. Prueba automatizada del recorrido completo | **Aceptada parcialmente** | La prueba existe (`backend/tests/test_search_games.py`, recorrido `GET /games/search → SearchGames → GameRepository → SteamGameRepository`), pero la evidencia citada en el propio `docs/correciones.md` referencia por error `test_health.py`, que no es esa prueba. Se acepta el hecho (la prueba existe), no la cita de evidencia. |
| 9. ADR con trazabilidad y marca de reemplazo | **Aceptada** | Confirmado en el criterio transversal (e): ADR-0001 marca "Superada parcialmente por ADR-0002" con enlace. |
| 10. README con requisitos previos y comando de arranque | **Aceptada** | `README.md` tiene sección "Requisitos previos" y "Ejecución" con comando único (`scripts/start.py`). |
| 11. Etiqueta `corte-1` | **Rechazada (autoadmitida pendiente)** | El propio archivo la marca "Pendiente" y da los comandos para crearla; nunca se ejecutaron. No hay etiqueta en el repositorio. |
| 12. ADR del reto | **Rechazada (autoadmitida pendiente)** | El propio archivo la marca "Pendiente", condicionada a que "se defina el reto arquitectónico". No hay ADR de una restricción nueva. |
| 13. Medir línea base con procedimiento | **Rechazada (autoadmitida parcial)** | El propio archivo la marca "Parcialmente corregido": el método de verificación existe, la medición real no se ejecutó ni se registró un resultado. |
| 15. Rechazos con motivo en `docs/ia.md` | **Aceptada** | Confirmado: Registro 11 ("Se descartó mantener `start.py` en la raíz…") con motivo explícito. |

En conjunto: 10 de 13 puntos se aceptan porque el estado del repositorio los sostiene; los 3 restantes (etiqueta, ADR del reto, medición) los reconoce el propio equipo como pendientes, y la evidencia confirma que siguen sin resolverse — son precisamente los tres puntos que definen si hubo o no respuesta al reto de este corte.

## Nivel de rúbrica sugerido (propuesta al docente)

| Criterio | Nivel | Puntaje | Evidencia |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia | 0,00 | Sin restricción diagnosticada; el propio equipo reconoce que el ADR del reto está pendiente. |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | Los ADR visibles son de arquitectura base, no del reto. |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | El único cambio de código es una prueba sobre funcionalidad ya existente. |
| Pruebas, medición y trazabilidad | Nivel básico | 0,00 | Método de medición definido pero sin ejecutar; sin resultado contra umbral. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico verificable** | | **0,00 / 4,00** | La nota final la fija Moodle. |

## Recuento

**2 de 12 criterios Cumple** (salida de IA de este corte; nótese que la etiqueta sigue sin existir, a diferencia de AudioShare).

## No verificado

- PDF adjunto en Moodle.
- Coincidencia del diagnóstico con la restricción asignada (no disponible).
- Conservación de límites C4 (sin cambio de arquitectura que contrastar).
- Sustentación del reto.

## Hallazgos

- Drift es el equipo que más avanzó en cerrar deuda de estructura y trazabilidad (aspectos.md, ia.md, ADR con reemplazo, CI con SonarCloud) frente a la revisión preliminar, pero **no llegó a responder el reto específico de este corte**: ni la etiqueta, ni el ADR de una restricción nueva, ni la medición de línea base — los tres puntos que el propio equipo documenta como pendientes en `docs/correciones.md`.
- Tres commits llegaron después del cierre (`2026-09-07T05:22Z`–`06:26Z`): corrección de duplicación en pruebas y documentación en `ia.md`. No se calificaron por ser posteriores al cierre.
- `docs/correciones.md` está en `docs/`, no en la raíz del repositorio; se aceptó igual como el documento de correcciones del equipo.
- Persiste el hallazgo de nombres de ADR que enuncian el tema y no la decisión.

## Preguntas para la sustentación

1. ¿Cuál era la restricción asignada para este corte, y por qué `docs/correciones.md` describe su ADR como "pendiente, corresponde al reto que será asignado" en vez de tenerlo ya resuelto?
2. ¿Qué impidió ejecutar la medición de línea base si el método ya estaba definido en `docs/escenarios.md`?
3. ¿Por qué no se creó la etiqueta `corte-1` a tiempo, si el equipo ya tenía documentado el procedimiento exacto para hacerlo?
