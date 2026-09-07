# semana-05-corte1 · Calificación automática

> Revisión DEFINITIVA post-cierre, realizada el 2026-09-07. Reemplaza la revisión manual preliminar del 2026-09-03. Cierre de la actividad: `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | etiqueta `corte-1` → `201acacb0afbe7821d558f65a18eeca9c8f773db` (2026-09-06T23:34:17-05:00 = 2026-09-07T04:34:17Z, **anterior al cierre**) | 
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log` (tag, fallback, ventana S4→corte-1); `git show --stat` del commit del reto; `git show` del ADR-0006, `docs/ia.md`, `docs/aspectos.md`, README; `git log --follow` sobre ADR-0002; `git grep` (patrón de credenciales, §9); `git shortlog -sne`; `curl` a `actions/runs?per_page=10` (una sola llamada) |
| Revisor | revisión manual local, solo lectura; no se ejecutó código estudiantil |
| `correcciones.md` | No existe con ese nombre exacto. El equipo dejó `correcciones_feedback.md` en la raíz, con el mismo propósito (contradecir la revisión preliminar); se trató como tal. |

## El reto del corte 1

El commit `201acac` ("Reto del primer corte: registrar la recepcion en una bitacora antes de encolar") es, por sí solo, la respuesta completa al reto: 22 archivos, 1674 líneas añadidas, con diagnóstico medido, ADR-0006, implementación, 13 pruebas nuevas y medición posterior. Es un solo commit para todo el ejercicio, lo que dificulta ver el proceso paso a paso en el historial, pero el contenido cumple lo pedido por la ficha.

- **Restricción trabajada:** el equipo declara en `correcciones_feedback.md` (nota B) que la restricción asignada por Moodle nunca llegó, y que por eso trabajó sobre R-06 (deuda de persistencia/almacenamiento), ya declarada en el arc42 desde antes del corte. Es una sustitución razonable dado que la ficha instruye "si no está disponible, anótalo y sigue con el resto".
- **Diagnóstico con línea base medida:** `backend/herramientas/medir_ec07.py` ejercitó el endpoint real `POST /examenes/{id}/hojas` con un lote de 200 hojas sobre el commit anterior (`cede35e`). Resultado: confirmación en 0,126 s (umbral ≤10 s, cumple) pero **100 % de pérdida silenciosa** cuando la cola cae a mitad de lote (umbral 0 %, no cumple). Documentado en `docs/evidencia/medicion-ec07.md` con los tres JSON de evidencia (`medicion-ec07-antes.json`, `-cola-caida.json`, `-despues.json`).
- **ADR-0006:** compara 4 alternativas (no tocar nada / cola con ACK-Streams / PostgreSQL / bitácora de recepción propia) con argumentos a favor y en contra de cada una, decide la bitácora de solo-agregado, declara qué no cierra (R-06 sigue abierto), y liga a EC-07, RF-01, C4 Nivel 2 y `docs/aspectos.md`. Precisa el ADR-0002 sin reemplazarlo.
- **Cambio:** `backend/infraestructura/bitacora.py`, cambios en `ingesta/recepcion.py`, `infraestructura/cola.py` y `modelo.py`. El README mantiene el arranque de un solo comando (`docker compose up`), sin alterarlo.
- **Pruebas y CI:** `backend/tests/test_durabilidad_recepcion.py` (nuevo) y ajustes a `test_recepcion.py`. `curl -s .../actions/runs?per_page=10` muestra el run sobre `201acacb` en `2026-09-07T04:43:04Z` con `conclusion: success`, **antes del cierre** (05:00:00Z).
- **Medición posterior:** 200/200 hojas reportadas, 0 % de pérdida, 1,744 s en operación normal, 7,842 s con la cola caída (dentro del umbral de 10 s). Las 13 pruebas nuevas se validaron con 6 mutaciones; una mutación (nombre de cola hardcodeado) no fue detectada por ninguna prueba, y el equipo lo declaró como hueco conocido en vez de ocultarlo.
- **Trazabilidad:** la fila A-01 de `docs/aspectos.md` enlaza el escenario EC-07, los ADR 0002 y 0006, el código, las pruebas y la evidencia de medición, celda por celda, sin huecos.
- **IA:** `docs/ia.md`, entrada 7 (2026-09-06), referida específicamente a este reto, con una lista de rechazos técnicos justificados (p. ej. se rechazó marcar la hoja como "rechazada" cuando en realidad estaba almacenada, porque induciría al docente a resubir y duplicar; se corrigió tras probar con Docker que el primer diseño tardaba 7,1 s por reintento y rompía el techo de 10 s con un lote completo).

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `corte-1` → `201acac`, 2026-09-07T04:34:17Z, antes de 05:00:00Z | Cumple | — |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No accesible desde el repositorio | No verificado | Depende del adjunto de Moodle |
| Impacto de la restricción localizado en requisitos, C4 y código | ADR-0006: RF-01/EC-07, relaciones 3 y 4 del C4 Nivel 2, `ingesta/recepcion.py`, `infraestructura/cola.py` | Cumple | Restricción sustituida por R-06 ante la ausencia del dato de Moodle (declarado en `correcciones_feedback.md`, nota B) |
| Línea base medida y verificable antes del cambio | `docs/evidencia/medicion-ec07.md` + `medicion-ec07-antes.json`; herramienta `medir_ec07.py`, carga de 200 hojas, medida en `cede35e` | Cumple | Procedimiento reproducible con herramienta versionada en el repositorio |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/0006-registrar-la-recepcion-en-una-bitacora-antes-de-encolar.md`: 4 alternativas, fuerzas (R-06, RNF-12/13, ADR-0002), decisión, consecuencias | Cumple | Precisa el ADR-0002 sin reemplazarlo, con enlace explícito |
| Cambio implementado y ejecutable de extremo a extremo | `backend/infraestructura/bitacora.py` (nuevo), `ingesta/recepcion.py`, `cola.py`, `modelo.py`; README conserva `docker compose up` | Cumple | Arranque de un solo comando no se alteró |
| Límites declarados conservados tras el cambio | `docs/c4/doc-c4.md` actualizado (34 líneas); el cambio usa los contenedores ya existentes (Almacén de imágenes, Cola de trabajos), sin agregar ni quitar contenedores | Cumple | No hay contenedores nuevos que reconciliar |
| Prueba que cubre el cambio, en verde en el pipeline | `test_durabilidad_recepcion.py` (nuevo, 224 líneas); run `201acacb` en `2026-09-07T04:43:04Z`, `success`, antes del cierre | Cumple | `curl -s https://api.github.com/repos/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs?per_page=10` |
| Resultado contrastado con el umbral del escenario y reproducible | 200/200 reportadas, 0 % pérdida (umbral 0 %), 1,744 s y 7,842 s (umbral ≤10 s); herramienta y procedimiento versionados | Cumple | `docs/evidencia/medicion-ec07.md` documenta limitaciones del método |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | Fila A-01 de `docs/aspectos.md`: escenario, C4, ADR 0002+0006, 6 archivos de código, 4 archivos de prueba, evidencia con cifras | Cumple | Celda por celda sin huecos |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md`, entrada 7 (2026-09-06): 4 rechazos con motivo técnico explícito, referidos a este reto | Cumple | Incluye un rechazo detectado ejecutando el sistema con Docker (latencia de reintento), no solo leyendo código |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| a. Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_Sistema-de-calificacion-automatica`, clon anónimo exitoso | Cumple | — |
| b. Estructura mínima presente | README.md, docs/arc42, docs/adr (6 ADR), docs/c4, docs/aspectos.md, docs/ia.md | Cumple | — |
| c. Estado calificado identificable | `corte-1` → `201acac`, hash y fecha verificables | Cumple | — |
| d. Nombres de ADR según la convención | 0001 a 0006, todos `NNNN-titulo-en-kebab-case.md` | Cumple | — |
| e. ADR aceptados no reescritos | `git log --follow` sobre 0002 muestra un único commit de creación; 0006 declara precisar (no reemplazar) 0002 | Cumple | — |
| f. `docs/ia.md` al día para la semana | Entrada 7, 2026-09-06, referida al reto de este corte | Cumple | — |
| g. Sin credenciales en el repositorio ni en el historial | `git grep` (patrón AKIA/BEGIN.../ghp_/xox.../sk-/password/secret/token/api_key) sobre HEAD: sin coincidencias | Cumple | — |
| h. Contribución de todos los integrantes | `git shortlog -sne HEAD`: scp1109 (35), josueacademico17-source (16), SusanaRosales (7), Mariadelmar-restrepo (3) — los 4 integrantes declarados | Cumple | — |

## Estado global del proyecto (overall · revisado en HEAD)

- **HEAD revisado**: coincide con `corte-1` (`201acacb...`), sin commits posteriores.
- **Veredicto**: sin pendientes graves
- Resumen: el equipo entregó el reto completo antes del cierre, en un solo commit voluminoso: diagnóstico medido, ADR con alternativas reales, implementación, pruebas provocadas a fallar deliberadamente, medición contrastada con umbral y trazabilidad completa. La principal debilidad de forma es que todo el ejercicio quedó en un único commit, lo que reduce la legibilidad del proceso en el historial aunque no afecta el contenido evaluado.

Pendientes que siguen abiertos:
- Adjuntar el PDF de dos páginas en Moodle (no verificable desde el repositorio).
- Considerar partir trabajo de esta magnitud en varios commits para dejar rastro del proceso, no solo del resultado.
- El hueco declarado en ADR-0006 (mutación del nombre de cola no detectada por ninguna prueba) queda como trabajo futuro, ya reconocido por el propio equipo.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sobresaliente | 1,00 | Mide antes de decidir (0,126 s / 100 % pérdida), distingue que la latencia no es el problema y que la pérdida silenciosa sí lo es, prioriza por riesgo (duplicación + hojas invisibles) |
| Alternativas y decisión | Sobresaliente | 1,00 | ADR-0006 compara 4 alternativas con fuerzas y descarta la más "ortodoxa" (Streams+XACK) con argumento técnico verificado, no por preferencia |
| Aplicación sobre el corte vertical | Competente | 0,80 | Funciona de extremo a extremo, arranque reproducible con un comando, conserva límites del C4; no se evidenció degradación controlada adicional más allá de lo medido |
| Pruebas, medición y trazabilidad | Sobresaliente | 1,00 | Cadena navegable, contrasta con umbral, reproducible, con salida de IA justificada técnicamente y un hueco de cobertura declarado en vez de ocultado |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio |
| **Subtotal técnico verificable** | | **3,80 / 4,00** | No constituye el total sobre 5,00 |

## Recuento

10 de 12 criterios Cumple (2 No verificado: PDF y sustentación).

## No verificado / pendientes

- PDF adjunto en Moodle.
- Sustentación del reto.

## Hallazgos para la planilla

- El reto se resolvió completo, antes del cierre, con diagnóstico medido, ADR-0006, implementación, pruebas y medición contrastada con umbral.
- Todo el ejercicio quedó en un solo commit (`201acac`); recomendable dividir el trabajo en varios commits en próximas entregas.
- La restricción de Moodle nunca llegó al equipo; se sustituyó razonablemente por la deuda R-06 ya declarada.
- El pipeline corrió en verde sobre el commit de la etiqueta antes del cierre.
- Corrección a la revisión preliminar de S4 (ver sección de correcciones): los runs de CI, el C4 Nivel 2 y el contenido de `docs/ia.md` sí estaban presentes y completos en `cede35e`; la preliminar los marcó `No verificado`/`No cumple` sin citar el contenido.

## Correcciones del equipo

`correcciones_feedback.md` (equivalente a `correcciones.md` para este ejercicio) impugna, sobre todo, la revisión preliminar de las semanas S1-S4, no la de este corte. Por la regla de la ficha ("las evidencias S1-S4 son línea base y no se recalifican"), esos puntos no cambian ninguna nota ya puesta de S1-S4, pero sí corrigen hechos que también aparecían citados en la matriz preliminar del corte 1 (filas de pipeline, C4 e IA), y por eso se adjudican aquí. El contenido de `correcciones_feedback.md` se trató como hipótesis del estudiante, verificada contra el repositorio real, no como hecho.

| Corrección | Adjudicación | Justificación |
|---|---|---|
| Hallazgo 1: existen 21+ runs de CI en verde, incluido uno sobre `cede35e`/el commit calificado, con la URL ya versionada en `docs/aspectos.md` | Aceptada | `curl` a `actions/runs` confirma runs `success` sobre los commits citados, incluido `201acacb` antes del cierre; afecta directamente la fila de pipeline de este corte, que aquí queda "Cumple" |
| Hallazgo 2: el C4 Nivel 2 está completo en el commit revisado (no es un boceto "previsto") | Aceptada | `git show` de `docs/c4/doc-c4.md`/`docs/aspectos.md` en `corte-1` muestra el diagrama completo con 5 contenedores y relaciones; sostiene la fila "Límites declarados conservados" de este corte |
| Hallazgo 3: `docs/ia.md` tiene 6-7 entradas completas con "qué se rechazó y por qué" | Aceptada | Verificado directamente: la entrada 7 referida a este corte tiene 4 rechazos con motivo técnico; sostiene la fila de IA de este corte |
| Hallazgo 4: dos filas de la preliminar de S4/corte-1 marcadas "No cumple" con una observación que en realidad describe un "No verificado" ("estructuralmente cumplen, falta confirmar...") | Aceptada como corrección metodológica | La distinción importa para el recuento; en esta revisión definitiva las filas equivalentes del corte 1 se evaluaron con evidencia citada y quedaron "Cumple", no "No cumple" ni "No verificado" |
| Hallazgo 5: `docs/ia.md` recibió veredictos distintos en dos matrices por el mismo motivo declarado | Aceptada | Inconsistencia real entre revisiones anteriores del kit; en esta revisión definitiva se usa un solo criterio y una sola cita |
| Hallazgo 6 / nota B: la restricción de Moodle nunca llegó al equipo; se trabajó sobre R-06 en su lugar | Aceptada | Consistente con lo que también reportan los otros tres equipos de este lote; el ejercicio sobre R-06 es sustantivo y se evalúa como tal en la matriz de este corte |
| Hallazgo 7: sección 9 del arc42 y glosario ya cumplían en `cede35e` (S4) | Aceptada, pero fuera del alcance de esta revisión | Corresponde a la evidencia S4, ya calificada y no recalificable por la ficha; se deja anotado para la planilla, no cambia el corte 1 |
| Hallazgo 8: la tabla de contribución por integrante de la planilla tenía cifras desactualizadas (27/9/1/3 en vez de 34/16/7/3 en `cede35e`) | Aceptada | `git shortlog -sn` confirma las cifras del equipo; se corrige la tabla de contribución de la planilla |

## Preguntas para la sustentación

1. ¿Por qué se decidió resolver el reto completo en un solo commit, y qué parte del proceso (medición, decisión, implementación) ocurrió en qué orden real?
2. La mutación del nombre de la cola no fue detectada por ninguna prueba: ¿qué prueba nueva la cubriría y por qué no se incluyó ya?
3. Si la restricción real asignada por Moodle resulta ser distinta de R-06, ¿qué tan reutilizable es la bitácora de recepción para ese otro escenario?
