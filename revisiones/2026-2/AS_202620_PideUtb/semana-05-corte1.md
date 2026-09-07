# Semana 5 · Primer corte · PideUtb

> Revisión definitiva post-cierre — 2026-09-07. Reemplaza la revisión manual preliminar del 2026-09-03. Cierre: `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado calificado | no existe etiqueta `corte-1` (`git tag --list` vacío); por la regla de fallback se califica el último commit ≤ cierre: `1636f20d14f254dffd9aa9c1eb43e138fba73043` (2026-08-30T22:17:18-05:00) |
| HEAD para el overall | `c198b7a4200de2da7d2bc9da6ae34ddbb0b1d6ee` (2026-09-07T13:36:05-05:00) — **posterior al cierre** |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log -1 --until=cierre HEAD`; `git log 1636f20..HEAD`; `git diff --stat 1636f20 HEAD`; `git ls-tree -r 1636f20`; `git show 1636f20:docs/aspectos.md`, `docs/ia.md`; `git grep` (secretos); `git shortlog -sne HEAD`; búsqueda de `correcciones.md` en todo el historial (no existe) |
| Revisor | agente de revisión, solo lectura; no se ejecutó código del equipo |
| Alcance externo no disponible | restricción asignada y PDF de Moodle |

## Nota sobre el cierre

El equipo siguió empujando commits **el mismo lunes 7 de septiembre entre las 08:19 y las 13:36** (hora Colombia), todos posteriores al cierre `05:00:00Z`. No crearon la etiqueta `corte-1` en ningún momento, ni antes ni después del cierre. Por la regla de fallback, se califica el último commit anterior al cierre (`1636f20`, del 30/08 — el mismo que ya evaluó la revisión preliminar), y la fila de versionado de la matriz transversal queda en **No cumple**. La actividad posterior al cierre se resume en la sección **overall**, pero no cuenta para la nota de este corte.

## Matriz de la ficha (evaluada sobre `1636f20`, 30/08)

| Criterio de evaluación | Estado | Observaciones |
|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | No cumple | No existe la etiqueta en ningún momento del historial, ni antes ni después del cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No verificado | El adjunto de Moodle no está disponible. |
| Impacto de la restricción localizado en requisitos, C4 y código | No verificado | No se dispone de la restricción asignada; en `1636f20` no hay commits posteriores a S4 que documenten un diagnóstico nuevo. |
| Línea base medida y verificable antes del cambio | No cumple | `arc42.md` en ese estado declara los umbrales como objetivos iniciales, no resultados medidos. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | No cumple | Solo `docs/adr/0001-estilo-arquitectonico.md` (23/08, decisión de estilo de S3); no hay ADR del reto. |
| Cambio implementado y ejecutable de extremo a extremo | No cumple | No hay commits de S5 en `1636f20`; el flujo de pedidos documentado es el corte vertical de S4. |
| Límites declarados conservados tras el cambio | No cumple | No hay cambio de S5 que contrastar. |
| Prueba que cubre el cambio, en verde en el pipeline | No cumple | `backend/tests/test_pedidos.py` cubre S4; no hay workflow de CI en `1636f20` (`.github/` no existe). |
| Resultado contrastado con el umbral del escenario y reproducible | No cumple | No hay medición de S5. |
| Cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia navegable | No cumple | `docs/aspectos.md` en `1636f20` es narrativo (secciones por atributo de calidad), sin las 8 columnas del contrato ni fila del reto. |
| Salida de IA aceptada/corregida/rechazada con motivo técnico | No cumple | `docs/ia.md` en `1636f20` llega a "Uso de IA en la cuarta entrega"; no hay entrada de S5/corte-1. |
| Sustentación del reto | No verificado | Lo resuelve el docente en la sesión. |

**Recuento: 0 de 12.**

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Observaciones |
|---|---|---|
| a. Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon sin autenticación de `ISCOUTB/AS_202620_PideUtb` responde el 2026-09-07. Nota: el `origin` remoto de HEAD aparece como `ISCOUTB/-AS_202620_PideUtb` (con guion) en dos mensajes de merge post-cierre — posible renombrado temporal del repo; no afecta la URL canónica verificada. |
| b. Estructura mínima presente | No cumple | En `1636f20` falta `docs/arc42/` (arc42 está en la raíz) y `docs/c4/` (C4 embebido en `arc42.md`). En HEAD post-cierre se creó `docs/C4/` (mayúsculas, fuera de convención) y se movió `arc42.md` a `docs/`, pero sigue sin ser `docs/arc42/` con secciones. |
| c. Estado calificado identificable | No cumple | Sin etiqueta; se cita el hash y fecha del último commit ≤ cierre (`1636f20`, 30/08). |
| d. Nombres de ADR según la convención | Cumple | `docs/adr/0001-estilo-arquitectonico.md` pasa el filtro (aunque el título es temático, no la decisión). |
| e. ADR aceptados no reescritos | Cumple | Un único commit de creación (23/08, `b5f0310`), sin reescrituras posteriores hasta HEAD. |
| f. `docs/ia.md` al día para la semana | No cumple | Última entrada corresponde a S4; no hay entrada de S5 ni post-cierre. |
| g. Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` con los patrones del contrato sin coincidencias reales en HEAD (los "token" detectados son identificadores de librerías vendidas en `.venv-1/`, no secretos). Sin `.env` versionado. |
| h. Contribución de todos los integrantes | Cumple | `git shortlog -sne HEAD`: daniarriet (21), Santiago Cuesta/Santiago-C0 (9+1, mismo correo `sjcm082005@gmail.com`), ruddy2000utb-droid (2). Los tres integrantes tienen commits. |

## Estado global del proyecto (overall · HEAD `c198b7a`, posterior al cierre)

- El equipo trabajó activamente el lunes 7/09 de 08:19 a 13:36, ya después del cierre `05:00:00Z`: movieron `arc42.md` a `docs/`, crearon `docs/C4/` con tres niveles en Mermaid, ajustaron `docs/aspectos.md` y cambiaron el actor "Estudiante" por "Usuario" en varios documentos.
- Nada de esa actividad post-cierre constituye una respuesta al reto de corte 1: no hay ADR nuevo, no hay diagnóstico de una restricción externa, no hay medición ni prueba específica, y `docs/aspectos.md` sigue sin las 8 columnas del contrato ni fila trazable a un cambio del reto.
- `docs/C4/` quedó con mayúsculas (fuera de convención) y sin fusionar con una carpeta `docs/arc42/` real (sigue siendo un único `docs/arc42.md`).
- Sigue sin existir `.github/workflows/`; no hay pipeline de CI en ningún punto del historial.
- El repositorio sigue versionando `.venv-1/` completo (entorno virtual de Python con dependencias y binarios).
- No existe `correcciones.md` en ningún commit del historial (`git log --all --diff-filter=A -- '*correcciones*'` vacío): no hay objeciones del equipo que adjudicar en este lote.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia |
|---|---:|---:|---|
| Diagnóstico del reto | no demostrado | 0,00 | Falta restricción externa y no hay trabajo de S5 en el estado calificado. |
| Alternativas y decisión | no demostrado | 0,00 | No existe ADR del reto, ni antes ni después del cierre. |
| Aplicación sobre el corte vertical | no demostrado | 0,00 | El flujo existente corresponde a S4; los cambios post-cierre son cosméticos (reorganización de carpetas, cambio de actor). |
| Pruebas, medición y trazabilidad | no demostrado | 0,00 | No hay prueba del reto, CI ni medición reproducible en ningún estado del repositorio. |
| Sustentación del reto | lo fija el docente | pendiente | Requiere sesión. |
| **Subtotal técnico** | | **0,00 / 4,00** | No es la nota total sobre 5,00. |

## No verificado

- Restricción asignada al equipo (no disponible en el kit).
- PDF de dos páginas de Moodle.
- Sustentación (la fija el docente en sesión).

## Hallazgos

- No existe `corte-1` ni antes ni después del cierre; el equipo trabajó el mismo día del cierre pero después de la hora límite, y esa actividad no puede contar para la nota.
- Ningún commit, ni antes ni después del cierre, documenta diagnóstico, ADR, medición o prueba del reto de corte 1.
- `.venv-1/` sigue versionado; `docs/C4/` quedó fuera de convención (mayúsculas) incluso en la corrección post-cierre.
- Sin `correcciones.md`: no hay objeciones del equipo a la revisión preliminar que adjudicar.

## Preguntas para la sustentación

- ¿Por qué no se creó la etiqueta `corte-1` en ningún momento, ni siquiera con los commits del lunes 7/09?
- ¿Cuál fue la restricción asignada y qué evidencia (en cualquier estado del repositorio) responde a ella?
- ¿Qué impide sacar `.venv-1/` del control de versiones y añadir un pipeline de CI?
