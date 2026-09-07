# semana-05-corte1 · LostVault

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03, previa al cierre `2026-09-07T05:00:00Z`. **Se verificó específicamente la advertencia de esa revisión** (la etiqueta `corte-1` podía haberse movido tras el 2026-09-03) y **se confirma que no cambió nada**: la etiqueta sigue apuntando al mismo commit, sin actividad nueva del equipo.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | etiqueta `corte-1` → `952af8f4f2230a4cd2258d361629579da8a6ade6` · 2026-08-30T22:13:14-05:00 (anterior al cierre) |
| Cierre | `2026-09-07T05:00:00Z` |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log corte-1`; `git log 952af8f..HEAD` (**0 commits**, confirma que la etiqueta no se movió ni hay commits nuevos); `git ls-tree`; `git grep` de secretos; `curl` a `actions/runs?per_page=5` (1 llamada) |
| Restricción asignada | No disponible en el kit; el repositorio tampoco declara un reto/restricción nueva de Corte 1 |

## Verificación puntual solicitada

Se confirmó explícitamente lo que pedía la nota de este lote: **la etiqueta `corte-1` NO fue actualizada** después de la revisión preliminar del 2026-09-03. `git log 952af8f..HEAD` no devuelve ningún commit — el repositorio está exactamente en el mismo estado que se revisó entonces. El contenido etiquetado sigue siendo la evidencia de S4 (corte vertical de AS-03/Seguridad), sin diagnóstico, ADR, cambio ni medición de un reto propio de Corte 1.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` confirma `corte-1` → `952af8f` (2026-08-30T22:13:14-05:00), anterior al cierre | Cumple | La etiqueta existe y es válida en cuanto a fecha, pero su contenido es la línea base de S4, sin cambios posteriores. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay ruta en el repo | No verificado | Adjunto de Moodle no accesible desde el kit. |
| Impacto de la restricción localizado en requisitos, C4 y código | `docs/aspectos.md` solo documenta AS-03 de la línea base (S2-S4); no hay declaración de una restricción nueva de Corte 1 | No cumple | Sin restricción nueva, no hay diagnóstico que localizar. |
| Línea base medida y verificable antes del cambio | `docs/arc42/10_requisitos_calidad.md` define umbrales (99%, p95≤2s) sin medición ejecutada; no hay línea base de un reto nuevo | No cumple | No aplica: no hay reto nuevo que tenga línea base. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/` solo contiene `0001-estilo-arquitectonico.md`, sin cambios desde la revisión anterior | No cumple | Ningún ADR nuevo para un reto de Corte 1. |
| Cambio implementado y ejecutable de extremo a extremo | Sin commits nuevos desde `952af8f`; el corte vertical de AS-03 (línea base) sigue siendo lo único ejecutable, documentado en README (`flutter run -d chrome`) | No cumple | No hay incremento sobre el corte vertical. |
| Límites declarados conservados tras el cambio | Sin cambio no hay límites nuevos que verificar | No verificado | No aplica una comparación antes/después. |
| Prueba que cubre el cambio, en verde en el pipeline | Run sobre `952af8f`, éxito, 2026-09-01T21:21:20Z (`https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/...`); cubre `test/claim_object_use_case_test.dart`, `test/widget_test.dart`, `test/architecture_structure_test.dart`, todas de la línea base | No cumple | Pipeline en verde, pero sin prueba de un cambio del reto (porque no lo hay). |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición nueva; solo umbrales declarados sin ejecutar en `docs/arc42/10_requisitos_calidad.md` | No cumple | Sin cambio del reto no hay resultado que contrastar. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md` tiene fila AS-03 navegable hasta pruebas (línea base), pero ninguna fila para un reto de Corte 1 | No cumple | La cadena de la línea base es navegable; la del reto no existe. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md` registra hasta S3 (2026-08-24, commit `edd78d7`); sin entrada nueva para el corte 1 | No cumple | Sin cambios desde la revisión preliminar. |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Repositorio `ISCOUTB/AS_202620_LostVault` público, clonado sin autenticación | Cumple | — |
| Estructura mínima presente | `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md` presentes en HEAD | Cumple | Persisten `REVISION_CORREGIDA.md`, `ejecutable/` y `front_end/` como residuos: `REVISION_CORREGIDA.md` (2026-08-24) afirma que esas carpetas "se eliminan", pero `git ls-tree` confirma que ambas siguen presentes en el commit etiquetado. |
| Estado calificado identificable | Etiqueta `corte-1` confirmada sobre `952af8f`, anterior al cierre | Cumple | — |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md` sigue el formato `NNNN-titulo-en-kebab-case.md` | Cumple | Solo existe un ADR; ninguno del reto de Corte 1. |
| ADR aceptados no reescritos | Sin cambios desde la revisión anterior | Cumple | — |
| `docs/ia.md` al día para la semana | Última entrada del 2026-08-24 (S3); sin entrada de Corte 1 | No cumple | Sin cambios desde la revisión preliminar. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de secretos sin coincidencias; sin `.env` versionado | Cumple | — |
| Contribución de todos los integrantes | Los 4 integrantes declarados aparecen en el historial (Roy Gonzalez, Fausto-4/Jose Faustino España, shamarallorente-blip/Shamara Llorente, weller-rar), consolidados | Cumple | — |

## Estado global del proyecto (overall · HEAD)

- **HEAD** = etiqueta `corte-1` = `952af8f4f2230a4cd2258d361629579da8a6ade6` · 2026-08-30T22:13:14-05:00. Sin commits posteriores.
- **Veredicto:** con pendientes graves — el equipo no realizó ningún trabajo nuevo entre la revisión preliminar (2026-09-03) y el cierre (2026-09-07T05:00:00Z), pese a haber tenido cuatro días adicionales.
- El proyecto conserva una línea base arquitectónica completa (arc42, C4, ADR-0001, corte vertical AS-03 ejecutable y probado, CI en verde), pero cero avance sobre el reto de Corte 1.
- Persisten residuos (`ejecutable/`, `front_end/`) que un documento interno del propio equipo (`REVISION_CORREGIDA.md`, 2026-08-24) afirmaba haber eliminado.

## Nivel de rúbrica sugerido (propuesta al docente, NO nota aplicada)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia evaluable del reto | 0,00 | No se identifica una respuesta a ninguna restricción nueva; sin cambios desde la revisión preliminar. |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | El único ADR es de la línea base (S3). |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | Cero commits nuevos desde `952af8f`. |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | El CI de la línea base sigue en verde, pero no demuestra ninguna medición del reto. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico** | | **0,00 / 4,00** | Propuesta al docente; la nota final se fija en Moodle. |

## Recuento

1 de 12 criterios Cumple (etiqueta válida por fecha, aunque su contenido es de S4).

## No verificado

- Coincidencia del diagnóstico con la restricción asignada (no disponible en el kit).
- PDF adjunto en Moodle.
- Sustentación del reto.
- Conservación de límites tras un cambio que no existe.

## Hallazgos

- **El equipo no hizo ningún cambio entre el 2026-08-30 y el cierre**: la etiqueta `corte-1` sigue apuntando al mismo commit que en la revisión preliminar, confirmado con `git log 952af8f..HEAD` (0 commits).
- No hay ADR, diagnóstico, cambio de código ni medición para un reto/restricción nueva de Corte 1.
- `docs/ia.md` no registra ningún uso de IA posterior a S3.
- Persisten `ejecutable/` y `front_end/` como residuos que un documento propio del equipo decía haber eliminado desde el 24 de agosto.
- `docs/aspectos.md` no usa las 8 columnas exactas del contrato (usa columnas propias como "Escenario relacionado" y "Decisión/compromiso"), aunque la fila AS-03 sí es navegable hasta pruebas.

## Correcciones del equipo

No se encontró `correcciones.md` en la raíz del repositorio ni en HEAD. Existe `REVISION_CORREGIDA.md`, pero es un documento de 2026-08-24 (previo a S4), sin relación con el reto de Corte 1 ni con la revisión preliminar de esta semana — no contradice ningún hallazgo de `semana-05-corte1.md`. No aplica esta sección.

## Preguntas para la sustentación

1. ¿Por qué no hubo ningún commit nuevo entre el 30 de agosto y el cierre del primer corte, pese a la revisión preliminar del 3 de septiembre que señalaba la ausencia de respuesta al reto?
2. ¿Cuál fue la restricción asignada al equipo y dónde se localiza su impacto en requisitos, C4 y código?
3. ¿Por qué siguen presentes `ejecutable/` y `front_end/` si `REVISION_CORREGIDA.md` afirma desde agosto que fueron eliminados?
