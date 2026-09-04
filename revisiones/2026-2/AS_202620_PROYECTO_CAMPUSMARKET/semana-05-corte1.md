# Semana 5 · Primer corte · CampusMarket

> Revisión manual preliminar completa, realizada el 2026-09-03 antes del cierre. El equipo puede cambiar el repositorio hasta el 2026-09-07T05:00:00Z; el estado y la propuesta pueden cambiar en la pasada definitiva.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | etiqueta `corte-1` ausente; HEAD preliminar `f3f436713bc79a7da4d5792c4f0876cc85fcdd3c` (2026-08-30T22:55:30-05:00) |
| HEAD para el overall | `f3f436713bc79a7da4d5792c4f0876cc85fcdd3c` |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | revisión manual con inspección Git; sin ejecutar código |
| Alcance externo no disponible | restricción asignada y PDF de Moodle |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git log -1 --format='%H %cI' corte-1` | No cumple | `git tag --list` no devuelve etiquetas. Se revisa HEAD como estado preliminar. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | documento adjunto en la entrega de Moodle | No verificado | El adjunto de Moodle no está disponible en el kit. |
| Impacto de la restricción localizado en requisitos, C4 y código | apartado de diagnóstico citando elemento y escenario afectados | No verificado | No se proporcionó la restricción asignada y no hay diagnóstico de S5; HEAD se identifica como S4 (`README.md:17`, `59-65`). |
| Línea base medida y verificable antes del cambio | cifra con herramienta y procedimiento | No cumple | `docs/arc42/10-escenarios-de-calidad.md:5` indica que las medidas son iniciales y podrán ajustarse; no hay medición previa ejecutada. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/NNNN-*.md` ligado al escenario de calidad | No cumple | Solo existe `docs/adr/0001-usar-monolito-modular.md`, creado el 23/08 para el estilo de S3. |
| Cambio implementado y ejecutable de extremo a extremo | commit que implementa el ADR y comando de arranque del README | No cumple | No hay commits de S5. El flujo Flutter, FastAPI y SQLite (`README.md:59-73`) corresponde a S4. |
| Límites declarados conservados tras el cambio | correspondencia del C4 con la estructura del código | No cumple | No existe cambio del reto que contrastar; los C4 presentes describen la línea base S4 (`README.md:114-126`). |
| Prueba que cubre el cambio, en verde en el pipeline | ruta de la prueba y URL del run anterior a la etiqueta | No cumple | `backend/tests/test_publicaciones_vertical.py:11-45` y el run exitoso #12 cubren S4, no un cambio de S5. |
| Resultado contrastado con el umbral del escenario y reproducible | medición con herramienta, carga y procedimiento | No cumple | No hay resultado de S5 ni comparación antes/después. Los escenarios solo formulan umbrales (`10-escenarios-de-calidad.md:23,43,63,86`). |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | fila de `docs/aspectos.md` recorrida celda a celda | No cumple | ASP-03 a ASP-05 trazan S3/S4 (`docs/aspectos.md:13-15`); no hay fila ni evidencia del reto de S5. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | entrada de `docs/ia.md` de este corte | No cumple | `docs/ia.md:28-38` llega a S4; no hay entrada de S5. |
| Sustentación del reto | sesión de sustentación | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | URL `github.com/ISCOUTB/AS_202620_<PROYECTO>` y respuesta de la API sin autenticación | Cumple | El clon sin autenticación de `ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` respondió el 2026-09-03. |
| Estructura mínima presente | salida de `git ls-tree` con las seis rutas del apartado 2 | Cumple | Están README, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. |
| Estado calificado identificable | etiqueta de la entrega, o hash y `%cI` del último commit anterior al cierre | Cumple | Ante la ausencia de tag, HEAD `f3f4367` del 30/08 es el último commit visible anterior al cierre y queda citado. |
| Nombres de ADR según la convención | `ls docs/adr` sin salida en el filtro del apartado 4 | Cumple | `0001-usar-monolito-modular.md` cumple el patrón. |
| ADR aceptados no reescritos | historial de cada ADR anterior sin commits de reescritura, o reemplazo declarado | Cumple | El ADR 0001 aparece en un único commit, `dbdd9c4` del 23/08. |
| `docs/ia.md` al día para la semana | commits sobre el archivo dentro del periodo revisado, con lo rechazado y su motivo | No cumple | Último cambio el 30/08; `docs/ia.md:28-38` solo cubre S4. |
| Sin credenciales en el repositorio ni en el historial | `git grep` y `git log -S` sin coincidencias | Cumple | Búsquedas de patrones de secretos, `.env` versionado y llaves privadas sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne` con todos los integrantes del equipo | Cumple | Tres personas consolidadas: nilver-garcia/Nnigarp, camilixo92 y Carulla-sd. |

## Estado global del proyecto (overall · HEAD)

- La base acumulada de S4 es coherente: estructura contractual completa, C4 como código, corte vertical Flutter → FastAPI → SQLite (`README.md:59-87`) y trazabilidad ASP-05 (`README.md:167-173`).
- El workflow ejecuta `python -m pytest backend/tests -q` (`.github/workflows/backend-tests.yml:13-30`). La consulta única a Actions del 2026-09-03 confirmó el run de HEAD `f3f4367` en `success`; URL publicada: https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/33219659253.
- No existe actividad de S5. El repositorio no muestra etiqueta, diagnóstico, ADR, cambio, prueba, medición ni trazabilidad específica del parcial.
- `docs/aspectos.md:11-12` conserva dos filas con huecos, aunque las filas S3/S4 son navegables. El ADR 0001 no enlaza explícitamente el commit que lo implementa.
- No se encontró configuración de SonarCloud. El arranque está documentado, pero no fue ejecutado durante esta revisión.

## Nivel de rúbrica sugerido

Propuesta preliminar al docente. La sustentación no se infiere del repositorio.

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | no demostrado | 0,00 | Falta la restricción externa y no hay actividad de S5. |
| Alternativas y decisión | no demostrado | 0,00 | No hay ADR del reto. |
| Aplicación sobre el corte vertical | no demostrado | 0,00 | El corte vertical existente pertenece a S4. |
| Pruebas, medición y trazabilidad | no demostrado | 0,00 | CI de S4 en verde, pero sin prueba ni medición del reto. |
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
- La base acumulada está mejor estructurada que la entrega de S5, que aún no existe.
- Faltan SonarCloud y el enlace del ADR al commit que lo implementa.

## Preguntas para la sustentación

- ¿Cuál fue la restricción asignada y qué componente, escenario y riesgo afecta?
- ¿Qué alternativa descartaron y qué dato haría revisar la decisión tomada?
- ¿Qué medición antes/después ejecutarán y cómo la reproducirá otra persona?
