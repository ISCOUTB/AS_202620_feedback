# semana-05-corte1 · ShareU

> Revisión DEFINITIVA post-cierre, realizada el 2026-09-07. Reemplaza la revisión manual preliminar del 2026-09-03. Cierre de la actividad: `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | etiqueta `corte-1` → `a5d08c1e2b91f9613726d5e46b1e8ba32774d87c` (2026-09-07T07:21:53-05:00 = 2026-09-07T12:21:53Z) |
| Discrepancia de versionado | La etiqueta existe pero apunta a un commit **posterior al cierre** (12:21:53Z > 05:00:00Z). El último commit admisible (≤ cierre) es `1728495` (2026-09-06T22:55:04-05:00 = 2026-09-07T03:55:04Z, "Eliminar shareu_base 2.zip"), con contenido funcionalmente idéntico al de la etiqueta para efectos de esta ficha. Se revisó el contenido de la etiqueta, como indica la regla del kit, pero la fila de versionado queda "No cumple". |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log` (tag, fallback, HEAD, ventana S4→corte-1, ventana post-tag→HEAD); `git ls-tree -r` sobre la etiqueta, el fallback y HEAD; `git show` de ADR, `docs/ia.md`, `docs/aspectos/aspectos.md`; `git grep` (patrón de credenciales, §9); `git shortlog -sne`; `curl` a `actions/runs?per_page=30` (una sola llamada) |
| Revisor | revisión manual local, solo lectura; no se ejecutó código estudiantil |
| `correcciones.md` | No existe en la etiqueta ni en HEAD. Se omite la sección de adjudicación. |

## Qué pasó con la etiqueta (hallazgo principal)

El equipo subió el reto por la interfaz web de GitHub como cargas de archivos ZIP ("Add files via upload") la noche del cierre y la madrugada siguiente. La secuencia de commits es:

```
3ae0981 2026-09-06T22:51:07-05:00 (03:51:07Z)  Add files via upload      ← antes del cierre
1728495 2026-09-06T22:55:04-05:00 (03:55:04Z)  Eliminar shareu_base 2.zip ← antes del cierre (fallback admisible)
c4e5a5a 2026-09-07T07:19:47-05:00 (12:19:47Z)  Add files via upload      ← DESPUÉS del cierre
a5d08c1 2026-09-07T07:21:53-05:00 (12:21:53Z)  Add files via upload      ← DESPUÉS del cierre; aquí quedó `corte-1`
```
El equipo colocó la etiqueta sobre un commit subido más de 7 horas después del cierre. El contenido de ambos estados (fallback y etiqueta) es, en la práctica, el mismo árbol duplicado por la carga de ZIPs (ver abajo), así que la discrepancia de versionado no cambia la conclusión sobre el reto, pero sí la fila de versionado de la matriz transversal.

Además, después de la etiqueta el equipo siguió modificando el árbol (fusión de un codespace, borrado de `Corte_1/docs/requirements.txt`), reorganizando todo bajo una carpeta nueva `Corte_1/`. Eso se registra en `overall`.

## Estructura entregada (hallazgo transversal)

El árbol de la etiqueta **no es la estructura mínima en la raíz del repositorio**: la carga de ZIP creó una carpeta `AS_202620_ShareU-master/` que contiene una copia completa del proyecto, y dentro de esa carpeta hay además una segunda copia bajo `shareu_base/` (con su propio `docs/adr/0001-...md`, sus propios `tests/`, etc.). Es decir, hay **tres copias parciales del mismo árbol** conviviendo en el mismo commit. Por CONTRATO §2 esto es una desviación de estructura (los artefactos existen, pero no en la raíz ni sin duplicarse), no una ausencia.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `corte-1` → `a5d08c1` en `2026-09-07T12:21:53Z`, posterior a `2026-09-07T05:00:00Z` | No cumple | Etiqueta posterior al cierre por más de 7 horas; ver discrepancia arriba |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No accesible desde el repositorio | No verificado | Depende del adjunto de Moodle |
| Impacto de la restricción localizado en requisitos, C4 y código | `git show corte-1:AS_202620_ShareU-master/docs/aspectos/aspectos.md` solo declara el aspecto de usabilidad de la S3; no hay sección nueva de diagnóstico de restricción | No cumple | Ningún documento del árbol nombra una restricción nueva ni su impacto; no hay indicio de diagnóstico del reto |
| Línea base medida y verificable antes del cambio | Sin archivo de medición, cifra ni procedimiento en ninguna de las tres copias del árbol | No cumple | No hay herramienta ni procedimiento documentado |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/` (en las tres copias) solo contiene `0001-estilo-arquitectonico.md`, con fecha de agosto | No cumple | No existe ADR del reto |
| Cambio implementado y ejecutable de extremo a extremo | Ningún commit entre S4 y la etiqueta modifica `app/`; los commits de la ventana son solo cargas y borrados de ZIP | No cumple | No hay cambio de código atribuible al reto |
| Límites declarados conservados tras el cambio | No hay cambio del reto que comparar contra `docs/c4/nivel1.mmd` / `nivel-2.md` | No cumple | No aplica: sin cambio no hay límites que verificar |
| Prueba que cubre el cambio, en verde en el pipeline | `curl -s https://api.github.com/repos/ISCOUTB/AS_202620_ShareU/actions/runs?per_page=30` → `"total_count": 0` | No cumple | El pipeline nunca se ha ejecutado en este repositorio, ni antes ni después de la etiqueta |
| Resultado contrastado con el umbral del escenario y reproducible | Sin medición en el árbol | No cumple | No hay umbral ni cifra que contrastar |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos/aspectos.md` en `corte-1` solo tiene el aspecto de usabilidad de S3-S4, sin fila nueva | No cumple | No hay fila del reto que recorrer |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md` en `corte-1` tiene 4 entradas, todas fechadas en la semana 3-4 (comparación arquitectónica, esqueleto, corte vertical de búsqueda, CI) | No cumple | Ninguna entrada se refiere al trabajo de este corte |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| a. Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_ShareU`, clon anónimo exitoso | Cumple | — |
| b. Estructura mínima presente | README.md, docs/arc42/arc42.md, docs/adr/0001-*.md, docs/c4/, docs/aspectos/aspectos.md, docs/ia.md presentes, pero triplicados bajo `AS_202620_ShareU-master/` y `AS_202620_ShareU-master/shareu_base/` | Cumple | Desviación de estructura grave (tres copias del árbol en el mismo commit); no ausencia de artefacto |
| c. Estado calificado identificable | La etiqueta `corte-1` existe y resuelve a un commit concreto | Cumple | Identificable, aunque posterior al cierre (ver fila siguiente) |
| Versionado (commit anterior al cierre) | `a5d08c1` es 2026-09-07T12:21:53Z, posterior a `2026-09-07T05:00:00Z` | No cumple | Discrepancia explicada arriba; fallback admisible `1728495` con contenido equivalente |
| d. Nombres de ADR según la convención | `0001-estilo-arquitectonico.md` cumple `NNNN-titulo-en-kebab-case.md` | Cumple | Único ADR del repositorio |
| e. ADR aceptados no reescritos | `git log --follow` sobre el ADR muestra un único punto de entrada | Cumple | Sin reescrituras detectadas |
| f. `docs/ia.md` al día para la semana | Última entrada referida a S3-S4 (corte vertical de búsqueda y CI); nada del reto de esta semana | No cumple | No está al día para el corte 1 |
| g. Sin credenciales en el repositorio ni en el historial | `git grep -nIE '(AKIA...\|BEGIN...\|ghp_...\|xox...\|sk-...\|password\|secret\|token\|api_?key)'` sobre HEAD: sin coincidencias | Cumple | Búsqueda sin resultados |
| h. Contribución de todos los integrantes | `git shortlog -sne HEAD`: Dayana (6), luiscorredor (2), Nicolas-HH (1), steven (1) — los 4 integrantes declarados aparecen | Cumple | Mejora respecto a la revisión preliminar (que solo veía 2 cuentas); ahora los 4 integrantes tienen commits propios |

## Estado global del proyecto (overall · revisado en HEAD)

- **HEAD revisado**: `8ba5a79b17cba43794b7df685cc67ee5d35e7208` (2026-09-07T08:09:39-05:00), *"Delete Corte_1/docs/requirements.txt"*
- **Veredicto**: con pendientes graves
- Resumen: después de colocar la etiqueta `corte-1` (ya de por sí posterior al cierre), el equipo siguió reorganizando el árbol: fusionó un PR de un codespace ("Pending changes exported from your codespace") y movió todo el contenido a una carpeta `Corte_1/` en la raíz, sin resolver la duplicación anterior. El repositorio en HEAD sigue sin ADR del reto, sin diagnóstico, sin medición y sin ejecución de pipeline (0 runs totales). La reorganización por sí sola no constituye una respuesta al reto.

Pendientes que siguen abiertos:
- Aclarar y corregir la etiqueta `corte-1` para que apunte a un commit anterior al cierre, o asumir la sanción de la entrega tardía.
- Deshacer la triplicación del árbol (`AS_202620_ShareU-master/`, `shareu_base/`, `Corte_1/`) y dejar una sola copia en la raíz.
- Responder al reto: diagnóstico con línea base medida, ADR nuevo, implementación, pruebas y medición contra umbral.
- Configurar y ejecutar el pipeline al menos una vez (0 runs totales hasta la fecha de esta revisión).
- Referir `docs/ia.md` y la fila de `docs/aspectos/aspectos.md` al trabajo de este corte.
- Adjuntar el PDF de dos páginas en Moodle.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia evaluable del reto | 0,00 | Ninguna de las tres copias del árbol contiene un diagnóstico de restricción nueva |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | El único ADR es de agosto (estilo arquitectónico), sin relación con un reto nuevo |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | Ningún commit entre S4 y la etiqueta toca `app/` |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | 0 runs de CI en toda la vida del repositorio; sin medición |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio |
| **Subtotal técnico verificable** | | **0,00 / 4,00** | No constituye el total sobre 5,00 |

## Recuento

0 de 12 criterios Cumple (2 No verificado, 10 No cumple).

## No verificado / pendientes

- PDF adjunto en Moodle.
- Sustentación del reto.

## Hallazgos para la planilla

- La etiqueta `corte-1` apunta a un commit posterior al cierre (`a5d08c1`, 2026-09-07T12:21:53Z); el fallback admisible es `1728495` con contenido equivalente.
- El árbol de la etiqueta tiene tres copias superpuestas del proyecto (`AS_202620_ShareU-master/`, su `shareu_base/` interno, y de nuevo todo bajo `Corte_1/` en HEAD tras la etiqueta): desviación de estructura grave por cargas de ZIP vía la interfaz web.
- No hay ADR, diagnóstico, medición ni cambio de código atribuibles al reto del corte 1.
- El pipeline de CI nunca se ha ejecutado: `actions/runs` devuelve `total_count: 0`.
- `docs/ia.md` y `docs/aspectos/aspectos.md` siguen fechados en S3-S4, sin entradas del reto.
- Mejora respecto a la revisión preliminar: ahora los 4 integrantes declarados tienen commits propios en el historial (antes solo se veían 2).
- El equipo siguió subiendo cambios después de colocar la etiqueta (fusión de codespace, reorganización a `Corte_1/`), sin resolver los pendientes de fondo.

## Preguntas para la sustentación

1. ¿Por qué la etiqueta `corte-1` quedó sobre un commit de más de 7 horas después del cierre, y qué se subió en esas dos últimas cargas?
2. ¿Cuál fue la restricción asignada al equipo, y por qué no hay ningún documento en el repositorio que la nombre o la diagnostique?
3. ¿Por qué el árbol quedó triplicado (`AS_202620_ShareU-master/`, `shareu_base/`, `Corte_1/`) y cuál de las copias es la que el equipo considera vigente?
