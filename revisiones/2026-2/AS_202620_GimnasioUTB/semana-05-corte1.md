# Semana 05 · Primer corte · GimnasioUTB

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03, previa al cierre `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | Sin etiqueta `corte-1`; último commit ≤ cierre = `9b9f7c8160ee18d97eb933357cfb05c3e942ad4e` · 2026-09-06T21:26:32-05:00 (= HEAD) |
| Cierre | `2026-09-07T05:00:00Z` |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list` (vacío); `git log HEAD`; `git ls-tree`; `git shortlog -sne`; `git grep` de secretos; `curl` a `actions/runs?per_page=8` (1 llamada) |
| Restricción asignada | No disponible en el kit; no se identifica un reto/restricción nueva declarada en el repositorio para Corte 1 |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` no devuelve nada | No cumple | Falta crear la etiqueta; se revisó el último commit ≤ cierre, `9b9f7c8` (anotado aquí). |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay ruta en el repo | No verificado | Adjunto de Moodle no accesible desde el kit. |
| Impacto de la restricción localizado en requisitos, C4 y código | `docs/aspectos.md` solo desarrolla el escenario S1 (consistencia de aforo), ya evaluado en S2-S4; `docs/correcciones.md` (commits `7094a6c`…`9b9f7c8`, 2026-09-06) documenta limpieza de README, glosario y aspectos, no un diagnóstico nuevo | No cumple | No hay declaración de una restricción nueva ni de su impacto. |
| Línea base medida y verificable antes del cambio | `docs/aspectos.md` cita pruebas de dominio e integración de S1, pero ninguna cifra de línea base para un escenario nuevo | No cumple | Sin restricción nueva no hay línea base que medir. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/` solo contiene `0001-arquitectura-hexagonal.md` (decisión de S3) | No cumple | No hay ADR nuevo para el reto de Corte 1. |
| Cambio implementado y ejecutable de extremo a extremo | Commits del cierre (`7094a6c`, `a71aece`, `9b9f7c8`) solo tocan `README.md`, `docs/aspectos.md`, `docs/ia.md` y crean `correcciones.md`; el adaptador de PostgreSQL sigue "pendiente" (README:81, `aforo-memoria.adapter.js` en memoria) | No cumple | No hay incremento de código; el propio README admite que la persistencia declarada en el corte vertical (PostgreSQL) no está implementada. |
| Límites declarados conservados tras el cambio | Sin cambio de código no hay límites nuevos que verificar; el puerto `AforoRepositoryPort` (README:81) mantiene la separación hexagonal ya evaluada | No verificado | No aplica una comparación antes/después de un cambio del reto. |
| Prueba que cubre el cambio, en verde en el pipeline | Run sobre `9b9f7c8`, éxito, 2026-09-07T02:26:35Z (`https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/...`); cubre `tests/domain/aforo.test.js` y `tests/aforo.integration.test.js`, pruebas ya existentes de S1/S4 | No cumple | Pipeline en verde, pero sin prueba de un cambio del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición, herramienta ni procedimiento para un escenario nuevo; `docs/aspectos.md` deja como pendiente la "prueba de carga con peticiones concurrentes contra PostgreSQL" | No cumple | Falta resultado reproducible. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | La fila de `docs/aspectos.md` (S1) enlaza Escenario→ADR-0001→código (`domain/aforo.js`, `application/registrar-acceso.usecase.js`, adaptadores)→pruebas, con honestidad sobre lo pendiente | Cumple (solo para S1, no para un reto de Corte 1) | La cadena de la línea base es navegable, pero no existe una fila para el reto nuevo. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md`, entrada "Semana 5" (6 de septiembre de 2026, Gemini): acepta la unificación del README y el glosario, y explícitamente **rechaza/ajusta** la estructura inicial de `correcciones.md` "para evitar un listado general y clasificar las correcciones por entrega semanal", con motivo técnico | Cumple | Entrada referida al trabajo de esta semana, con lo aceptado y lo rechazado explícitos. |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r --name-only HEAD` devuelve README.md, docs/adr/, docs/arc42/, docs/aspectos.md, docs/c4/, docs/ia.md | Cumple | Desviación de forma: arc42 es un único archivo `arc42_gimnasio_utb.md` en vez de secciones 1-12 separadas; C4 incluye `.png` junto a los `.md`. |
| Estado calificado identificable | Sin etiqueta `corte-1`; se usa el último commit ≤ cierre, `9b9f7c8` | No cumple | Falta la etiqueta exigida por el contrato. |
| Nombres de ADR según la convención | `docs/adr/0001-arquitectura-hexagonal.md` pasa `NNNN-titulo-en-kebab-case.md` | Cumple | — |
| ADR aceptados no reescritos | `docs/adr/0001-arquitectura-hexagonal.md` fue aceptado en `92f4a53` (2026-08-23, estado "Aceptada") y editado en contenido por `c271073`, `b556737`, `59b6d3e` y `47a18d0` (2026-08-30): cambia los escenarios citados (ES1/ES7/ES8 → ES1/ES2/ES3/ES4) y reescribe consecuencias | No cumple | El ADR aceptado fue editado en su contenido después de aceptarse; debía escribirse un ADR nuevo que lo reemplazara con enlace, no editar el aceptado. |
| `docs/ia.md` al día para la semana | Entrada "Semana 5" fechada 2026-09-06, referida al trabajo de esta semana (glosario, README, correcciones.md) | Cumple | — |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de secretos sin coincidencias (exit 1); sin `.env` versionado | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: PedroPambi 48, RodrigoFacioLince 15, Sebastian Caicedo (dos identidades consolidadas) 14 | Cumple | Los 3 integrantes tienen commits en el historial. |

## Estado global del proyecto (overall · HEAD)

- **HEAD**: `9b9f7c8160ee18d97eb933357cfb05c3e942ad4e` · 2026-09-06T21:26:32-05:00 · "Update IA documentation with new project details".
- CI en verde en HEAD (run 2026-09-07T02:26:35Z).
- El trabajo de la noche del cierre (commits `7094a6c`, `a71aece`, `9b9f7c8`) fue exclusivamente documental: limpieza de README/aspectos/glosario y creación de `correcciones.md`, sin tocar código de `src/`.
- El corte vertical sigue con persistencia en memoria; el adaptador PostgreSQL declarado en el README continúa pendiente, sin que esto se presente como el reto de Corte 1 (es deuda ya conocida desde S4).
- No se identifica una respuesta al reto de restricción nueva en ningún punto del historial hasta el cierre.

## Nivel de rúbrica sugerido (propuesta al docente, NO nota aplicada)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia evaluable del reto | 0,00 | No hay declaración de una restricción nueva ni de su impacto. |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | Único ADR es de la línea base (S3). |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | Los commits del cierre son documentales; no hay incremento de código. |
| Pruebas, medición y trazabilidad | Básico | 0,60 | La cadena de `docs/aspectos.md` es navegable para S1 y el registro de IA está al día, pero no hay medición ni prueba de un cambio del reto. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico** | | **0,60 / 4,00** | Propuesta al docente; la nota final se fija en Moodle. |

## Recuento

2 de 12 criterios Cumple (cadena de trazabilidad de la línea base y registro de IA al día; ambos referidos a S1, no al reto de Corte 1).

## No verificado

- PDF de dos páginas en Moodle.
- Conservación de límites tras el cambio (no hubo cambio del reto que verificar).
- Sustentación del equipo.

## Hallazgos

- Falta la etiqueta `corte-1`: se revisó el último commit ≤ cierre (`9b9f7c8`), anotado como discrepancia de versionado.
- No se identifica diagnóstico, ADR, cambio de código ni medición para un reto/restricción nueva de Corte 1; el trabajo del cierre fue limpieza documental de hallazgos de S2-S4.
- El registro de IA sí está al día y documenta explícitamente un rechazo con motivo técnico (estructura de `correcciones.md`).
- La persistencia en PostgreSQL sigue pendiente (deuda conocida desde S4, no oculta).
- arc42 en archivo único en vez de secciones 1-12 separadas: desviación de estructura, no ausencia.
- El ADR-0001, ya aceptado desde S3, fue editado en su contenido en cuatro commits del 2026-08-30 (cambia los escenarios de calidad citados y las consecuencias); debía escribirse un ADR nuevo que lo reemplazara, dejando el original marcado como "reemplazado" con enlace.

## Correcciones del equipo

`correcciones.md` está en la raíz del repositorio, pero no contradice ninguna fila de la revisión preliminar publicada: es un registro cronológico de ajustes documentales por semana (S2, S3, S4), sin ninguna afirmación que dispute un hallazgo de la revisión de S4/S5. No se adjudica ninguna corrección porque no hay disputa formal; su contenido se usó como evidencia para actualizar las filas de trazabilidad y de registro de IA arriba.

| Corrección | Adjudicación | Justificación |
|---|---|---|
| (ninguna disputa formal presentada) | No aplica | `correcciones.md` es un log de cambios ya hechos por entrega, no una impugnación de hallazgos; se verificó directamente en el repo y se incorporó a la matriz. |

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada al equipo para el Corte 1, y por qué el trabajo previo al cierre se limitó a depurar documentación de entregas anteriores?
2. ¿Cuándo esperan implementar el adaptador de PostgreSQL que el propio README declara pendiente, y cómo afecta eso a la garantía de la Arquitectura Hexagonal que citan en el ADR-0001?
3. ¿Qué prueba de carga o medición contra un umbral tienen previsto ejecutar una vez exista ese adaptador?
