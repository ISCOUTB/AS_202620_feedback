# semana-05-corte1 · AudioShare

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03. El estado calificado es la etiqueta `corte-1`, ya existente y anterior al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado calificado | etiqueta `corte-1` → `cb65d13134b220c020d0facaa00d0a779d584245` (`2026-09-06T22:00:48-05:00`, *Update README.md*) |
| Cierre | `2026-09-07T05:00:00Z` |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log -1 corte-1`; `git checkout corte-1`; `git ls-tree -r --name-only`; `git log --format=... HEAD` (histórico completo); `git log --diff-filter=A -- docs/adr/`; `git grep` de secretos (regex del contrato, exit 1 = sin coincidencias); `git ls-files | grep '\.env$'`; `git shortlog -sne`; `curl .../actions/runs?per_page=30` (1 llamada) |
| Restricción asignada | No disponible en el kit ni citada en el repositorio; no se pudo verificar contra qué restricción específica debía responder el equipo. |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| 1. Etiqueta `corte-1` sobre un commit anterior al cierre | `git log -1 --format='%H %cI' corte-1` → `cb65d131…`, `2026-09-06T22:00:48-05:00` (`2026-09-07T03:00:48Z`), anterior al cierre `05:00:00Z` | **Cumple** | La etiqueta apareció entre la revisión preliminar y el cierre. |
| 2. PDF de dos páginas | No hay PDF en el repositorio (correcto, va en Moodle) | **No verificado** | Debe comprobarse en Moodle. |
| 3. Impacto de la restricción en requisitos, C4 y código | `docs/aspectos.md` (aspecto A-01) sigue describiendo la sincronización de audio de la línea base (EC-01…EC-04); no aparece una restricción nueva ni en `docs/arc42/src/02_architecture_constraints.adoc` ni en el único ADR | **No cumple** | No hay diagnóstico de una restricción nueva en ningún artefacto del repo. |
| 4. Línea base medida y verificable | `docs/aspectos.md`: EC-02/EC-03 declaran explícitamente "medición de latencia real queda pendiente" y "caso específico de pausa/reanudación queda pendiente" | **No cumple** | Ninguna cifra con herramienta y procedimiento. |
| 5. ADR del reto | `docs/adr/` solo contiene `0001-usar-monolito-modular.md` (commit de creación `84e2e03`, 2026-08-23, anterior a S5); último cambio al ADR es `924d133` (2026-09-04), edición de texto, no ADR nuevo | **No cumple** | Es el ADR de la línea base, no responde a una restricción nueva. |
| 6. Cambio implementado extremo a extremo | Commits de S5 (`9bb6b6a`…`cb65d13`): integrar corte vertical A-01 a `master`, diagramas C4, ajustar Node 20→22 en CI, editar README; ninguno introduce funcionalidad nueva ligada a una restricción | **No cumple** | El único cambio funcional (`869f3a9` "Implementar corte vertical A-01") es anterior al cierre de S4, no de S5. |
| 7. Límites C4 conservados | `docs/c4/C4 Nivel 2 - Contenedores.mmd` sigue describiendo 4 contenedores frente a un monolito Node implementado en `src/` | **No cumple** | Discrepancia arrastrada de S4; sin cambio S5 que la agrave o resuelva, pero tampoco hay nada que "conservar" porque no hubo cambio del reto. |
| 8. Prueba que cubre el cambio, en verde en pipeline | `curl .../actions/runs`: `cb65d131` success (`2026-09-07T03:00:50Z` y `03:21:03Z`); commits previos de S5 (`3373bb8`, `7afe7c6`, `03ee2f7`, `924d133`, `ee26081`, `9bb6b6a`) en `failure` | **No cumple** | El run verde corresponde a un commit de solo README/Node version, no a una prueba del reto; no existe prueba nueva que cubrir. |
| 9. Resultado contrastado con umbral | Sin medición reportada (ver criterio 4) | **No cumple** | No hay resultado que contrastar. |
| 10. Cadena de trazabilidad navegable | `docs/aspectos.md` trae 9 columnas (`ID…Pruebas`) y "Resumen de trazabilidad"; recorrida la fila A-01/EC-02: llega a ADR-0001, C4 nivel 2, código y prueba, pero la celda de prueba dice explícitamente que la medición real está pendiente | **No cumple** | La cadena existe pero se rompe en la evidencia de calidad (no hay medición), y no incluye ninguna fila para una restricción nueva. |
| 11. Salida de IA con motivo técnico, de este corte | `docs/ia.md`: última sección fechada "Semana 4"; el pie dice "Documento actualizado durante la semana 5, previo al corte 1" pero no agrega ninguna entrada fechada o etiquetada como S5/reto | **No cumple** | La actualización de S5 es solo la línea de estado, no una entrada de uso de IA de este corte. |
| 12. Sustentación del reto | — | **No verificado** | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| a. Repositorio en la organización, convención y público | Clon anónimo de `github.com/ISCOUTB/AS_202620_AudioShare` exitoso | **Cumple** | — |
| b. Estructura mínima | `git ls-tree` en `cb65d13`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` presentes | **Cumple** | arc42 en AsciiDoc (desviación de formato, ya anotada desde S2). |
| c. Estado calificado identificable | `corte-1` → `cb65d131…`, `2026-09-06T22:00:48-05:00` | **Cumple** | — |
| d. Nombres de ADR según convención | `docs/adr/0001-usar-monolito-modular.md` | **Cumple** | — |
| e. ADR aceptados no reescritos | Único ADR, sin marca de "reescrito tras aceptación" en su historial de commits (`924d133` es edición de contenido, sin cambio de estado declarado) | **No verificado** | El ADR no declara explícitamente su estado (aceptado/propuesto) en el texto revisado; no se puede confirmar si el cambio de `924d133` ocurrió antes o después de una aceptación formal. |
| f. `docs/ia.md` al día para la semana | Ver criterio 11 | **No cumple** | Sin entrada de S5. |
| g. Sin credenciales | `git grep` con la regex del contrato: exit 1 (sin coincidencias); `git ls-files` sin `.env` | **Cumple** | — |
| h. Contribución de todos los integrantes | `git shortlog -sne cb65d13`: Elian 45, Yeiver 38, cardonavincent26-design 36, Santiago 30 | **Cumple** | 4 identidades para 4 integrantes; `cardonavincent26-design` sigue sin confirmación oficial contra matrícula (arrastrado de S2). |

## Estado global del proyecto (overall · HEAD)

HEAD coincide con `corte-1` (`cb65d131…`). El repositorio tiene una línea base sólida (arc42, C4, ADR, corte vertical A-01 con prueba de integración y CI) pero **no hay ninguna evidencia de que el equipo haya recibido o respondido una restricción nueva**: los únicos cambios entre el cierre de S4 y la etiqueta son la integración del corte vertical A-01 (que en realidad pertenece a S4), diagramas C4, y ajustes cosméticos de README/CI. El pipeline sí corre y el último run es verde, pero sobre el mismo contenido de la línea base, no sobre una prueba nueva.

## Nivel de rúbrica sugerido (propuesta al docente)

| Criterio | Nivel | Puntaje | Evidencia |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia | 0,00 | No se identifica una restricción nueva ni una línea base medida para ella. |
| Alternativas y decisión | Sin evidencia | 0,00 | El único ADR es el de la línea base (S3). |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | Los cambios de S5 no implementan una restricción nueva. |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | Sin medición, sin prueba nueva, sin umbral contrastado. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico verificable** | | **0,00 / 4,00** | La nota final (sobre 5,00 con sustentación) la fija Moodle. |

## Recuento

**1 de 12 criterios Cumple** (solo la etiqueta `corte-1`).

## No verificado

- Coincidencia del diagnóstico con la restricción asignada (no disponible).
- PDF adjunto en Moodle.
- Estado formal (aceptado/propuesto) del ADR-0001 en el momento de su última edición.
- Sustentación del reto.

## Hallazgos

- La etiqueta `corte-1` ya existe y apunta a un commit anterior al cierre: mejora respecto a la revisión preliminar.
- No hay evidencia de que el equipo haya recibido o diagnosticado una restricción nueva para este corte; todo el trabajo de S5 consolida la línea base de S4 (corte vertical A-01, C4, README, CI).
- `docs/ia.md` no agrega ninguna entrada de este corte pese a declararse "actualizado durante la semana 5".
- El pipeline corre y el último run es verde, pero no cubre ninguna funcionalidad nueva.
- El C4 de contenedores sigue sin coincidir con el monolito implementado (arrastrado de S4).

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada para este corte, y por qué no hay ningún artefacto del repositorio (ADR, aspecto, sección de arc42) que la mencione?
2. Si no se implementó un cambio para el reto, ¿qué se entregó como diagnóstico y decisión en el PDF de Moodle, y con qué evidencia del repositorio se sostiene?
3. ¿Por qué el C4 de contenedores describe cuatro contenedores si la implementación (`src/`) y el ADR-0001 declaran un monolito modular de un solo proceso?
