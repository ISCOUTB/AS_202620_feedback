# Semana 5 · Primer corte · PideUtb

> Revisión manual preliminar completa, realizada el 2026-09-03 antes del cierre. El equipo puede cambiar el repositorio hasta el 2026-09-07T05:00:00Z; el estado y la propuesta pueden cambiar en la pasada definitiva.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | etiqueta `corte-1` ausente; HEAD preliminar `1636f20d14f254dffd9aa9c1eb43e138fba73043` (2026-08-30T22:17:18-05:00) |
| HEAD para el overall | `1636f20d14f254dffd9aa9c1eb43e138fba73043` |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | revisión manual con inspección Git; sin ejecutar código |
| Alcance externo no disponible | restricción asignada y PDF de Moodle |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git log -1 --format='%H %cI' corte-1` | No cumple | `git tag --list` no devuelve etiquetas. Se revisa HEAD como estado preliminar. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | documento adjunto en la entrega de Moodle | No verificado | El adjunto de Moodle no está disponible. `ficha_problema.pdf` pertenece a la línea base y no sustituye el PDF del corte. |
| Impacto de la restricción localizado en requisitos, C4 y código | apartado de diagnóstico citando elemento y escenario afectados | No verificado | No se proporcionó la restricción asignada y no hay diagnóstico de S5. El último commit es de S4. |
| Línea base medida y verificable antes del cambio | cifra con herramienta y procedimiento | No cumple | `arc42.md:557-559` aclara que las cifras son objetivos iniciales, no resultados experimentales. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/NNNN-*.md` ligado al escenario de calidad | No cumple | Solo existe `docs/adr/0001-estilo-arquitectonico.md`, creado el 23/08 para decidir el estilo; no hay ADR del reto. |
| Cambio implementado y ejecutable de extremo a extremo | commit que implementa el ADR y comando de arranque del README | No cumple | No hay commits desde el inicio de S5. El flujo documentado en `README.md:58-70` es el corte vertical de S4 y no se vincula a un reto nuevo. |
| Límites declarados conservados tras el cambio | correspondencia del C4 con la estructura del código | No cumple | No existe cambio de S5 que contrastar; el C4 está embebido en `arc42.md:372-453`, fuera de `docs/c4/`. |
| Prueba que cubre el cambio, en verde en el pipeline | ruta de la prueba y URL del run anterior a la etiqueta | No cumple | `backend/tests/test_pedidos.py:15-41` cubre S4. No hay workflow ni prueba del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | medición con herramienta, carga y procedimiento | No cumple | No hay resultados de medición; `arc42.md:557-559` declara que los umbrales aún no fueron medidos. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | fila de `docs/aspectos.md` recorrida celda a celda | No cumple | `docs/aspectos.md:120-126` tiene seis columnas, no las ocho del contrato, y cuatro filas incompletas. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | entrada de `docs/ia.md` de este corte | No cumple | `docs/ia.md:33-46` registra S4; no hay entrada de S5 ni un rechazo con motivo técnico. |
| Sustentación del reto | sesión de sustentación | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | URL `github.com/ISCOUTB/AS_202620_<PROYECTO>` y respuesta de la API sin autenticación | Cumple | El clon sin autenticación de `ISCOUTB/AS_202620_PideUtb` respondió el 2026-09-03. |
| Estructura mínima presente | salida de `git ls-tree` con las seis rutas del apartado 2 | No cumple | Faltan `docs/arc42/` y `docs/c4/`; `arc42.md` está en la raíz. |
| Estado calificado identificable | etiqueta de la entrega, o hash y `%cI` del último commit anterior al cierre | Cumple | Ante la ausencia de tag, HEAD `1636f20` del 30/08 es el último commit visible anterior al cierre y queda citado. |
| Nombres de ADR según la convención | `ls docs/adr` sin salida en el filtro del apartado 4 | Cumple | `docs/adr/0001-estilo-arquitectonico.md` cumple el patrón. |
| ADR aceptados no reescritos | historial de cada ADR anterior sin commits de reescritura, o reemplazo declarado | Cumple | El ADR 0001 aparece en un único commit del 23/08. |
| `docs/ia.md` al día para la semana | commits sobre el archivo dentro del periodo revisado, con lo rechazado y su motivo | No cumple | Último cambio el 30/08 y contenido hasta S4 (`docs/ia.md:33-46`); no hay S5. |
| Sin credenciales en el repositorio ni en el historial | `git grep` y `git log -S` sin coincidencias | Cumple | Búsquedas de patrones de secretos, `.env` versionado y llaves privadas sin coincidencias; se excluyeron falsos positivos conceptuales de librerías. |
| Contribución de todos los integrantes | `git shortlog -sne` con todos los integrantes del equipo | Cumple | Tres personas consolidadas: daniarriet, Santiago Cuesta/Santiago-C0 y ruddy2000utb-droid. |

## Estado global del proyecto (overall · HEAD)

- HEAD conserva un corte vertical legible de pedidos: arranque documentado (`README.md:13-39`), flujo (`README.md:58-70`) y tres pruebas funcionales (`backend/tests/test_pedidos.py:15-41`). No se ejecutó el código.
- No hay commits de S5, etiqueta, ADR del reto, línea base ni medición. Por tanto, el avance acumulado llega a S4 y no muestra respuesta al parcial.
- El C4 y arc42 están en un archivo raíz, no en las carpetas contractuales; `docs/aspectos.md:120-126` no tiene las ocho columnas y deja cuatro filas pendientes.
- No existe workflow de CI ni run que consultar. Las pruebas locales declaradas no demuestran verde en pipeline.
- Se versionó `.venv-1/` completo, incluidos binarios y dependencias; debe retirarse del control de versiones.
- `docs/ia.md:46` afirma revisión y ejecución local, pero no documenta una salida rechazada o corregida con motivo técnico para S5.

## Nivel de rúbrica sugerido

Propuesta preliminar al docente. La sustentación no se infiere del repositorio.

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | no demostrado | 0,00 | Falta restricción externa y no hay trabajo de S5. |
| Alternativas y decisión | no demostrado | 0,00 | No existe ADR del reto. |
| Aplicación sobre el corte vertical | no demostrado | 0,00 | El flujo existente corresponde a S4 y no hay commits nuevos. |
| Pruebas, medición y trazabilidad | no demostrado | 0,00 | No hay prueba del reto, run de CI ni medición reproducible. |
| Sustentación del reto | lo fija el docente | pendiente | Requiere sesión. |
| **Subtotal técnico** | | **0,00 / 4,00** | No es la nota total sobre 5,00. |

## Recuento

**0 de 12 criterios Cumple.** La restricción, el PDF y la sustentación quedan No verificados; los otros criterios no se satisfacen para S5.

## No verificados

- Restricción asignada: hace falta la consigna individual del equipo.
- PDF de dos páginas: hace falta el adjunto de Moodle.
- Sustentación: la resuelve el docente en sesión.

## Hallazgos

- No existe `corte-1` ni actividad de S5; HEAD sigue en el cierre de S4.
- Falta toda la cadena evaluable del reto: diagnóstico, ADR, cambio, prueba, medición y trazabilidad.
- El repositorio versiona un entorno virtual completo y mantiene desviaciones estructurales.

## Preguntas para la sustentación

- ¿Cuál fue la restricción asignada y dónde está documentada su respuesta?
- ¿Qué línea base midieron y qué resultado obtuvieron después del cambio, usando qué carga y procedimiento?
- ¿Cómo demostrarán en CI que la prueba específica del reto pasa antes de crear `corte-1`?
