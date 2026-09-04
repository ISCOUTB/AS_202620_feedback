# Semana 5 · Primer corte · mapsutb

> Revisión manual preliminar completa, realizada el 2026-09-03 antes del cierre. El equipo puede cambiar el repositorio hasta el 2026-09-07T05:00:00Z; el estado y la propuesta pueden cambiar en la pasada definitiva.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | etiqueta `corte-1` → `7e56ad372dbfebd8c7c38f74b19006e14f9e72e3` (2026-08-09T23:27:46-05:00) |
| HEAD para el overall | `e113f833d08f307b44b8901e9a46ce85c40359e2` (2026-08-31T20:11:24-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | revisión manual con inspección Git; sin ejecutar código |
| Alcance externo no disponible | restricción asignada y PDF de Moodle |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git log -1 --format='%H %cI' corte-1` | No cumple | Existe, pero apunta al commit de S1 `7e56ad3`, no al trabajo del corte; el tag solo contiene `README.md` y tres documentos iniciales. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | documento adjunto en la entrega de Moodle | No verificado | El adjunto de Moodle no está disponible en el kit. |
| Impacto de la restricción localizado en requisitos, C4 y código | apartado de diagnóstico citando elemento y escenario afectados | No verificado | No se proporcionó la restricción asignada. Además, en el tag no hay C4 ni código y `docs/aspectos.md:7` deja ambos pendientes. |
| Línea base medida y verificable antes del cambio | cifra con herramienta y procedimiento | No cumple | En el tag, `docs/aspectos.md:16` solo declara umbrales de 3 s y 5 m; no registra una medición ejecutada ni procedimiento. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/NNNN-*.md` ligado al escenario de calidad | No cumple | El árbol del tag no contiene `docs/adr/`. |
| Cambio implementado y ejecutable de extremo a extremo | commit que implementa el ADR y comando de arranque del README | No cumple | El tag no contiene código y `README.md:1` es solo el título del repositorio. |
| Límites declarados conservados tras el cambio | correspondencia del C4 con la estructura del código | No cumple | El tag no contiene C4 ni código para contrastar. |
| Prueba que cubre el cambio, en verde en el pipeline | ruta de la prueba y URL del run anterior a la etiqueta | No cumple | El tag no contiene pruebas ni workflow de CI. |
| Resultado contrastado con el umbral del escenario y reproducible | medición con herramienta, carga y procedimiento | No cumple | No hay resultado medido en el tag; `docs/aspectos.md:16` enuncia un objetivo, no evidencia de medición. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | fila de `docs/aspectos.md` recorrida celda a celda | No cumple | `docs/aspectos.md:7` tiene C4 por definir, sin ADR y código, pruebas y evidencia aún no iniciados. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | entrada de `docs/ia.md` de este corte | No cumple | `docs/ia.md:9-10` registra usos del 07/08, previos al corte; no hay entrada de S5. |
| Sustentación del reto | sesión de sustentación | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | URL `github.com/ISCOUTB/AS_202620_<PROYECTO>` y respuesta de la API sin autenticación | Cumple | El clon sin autenticación de `ISCOUTB/AS_202620_mapsutb` respondió el 2026-09-03. |
| Estructura mínima presente | salida de `git ls-tree` con las seis rutas del apartado 2 | No cumple | En `corte-1` faltan `docs/arc42/`, `docs/adr/` y `docs/c4/`; solo están README, aspectos e IA. |
| Estado calificado identificable | etiqueta de la entrega, o hash y `%cI` del último commit anterior al cierre | Cumple | `corte-1` identifica inequívocamente `7e56ad3` del 09/08, aunque es el estado equivocado para esta entrega. |
| Nombres de ADR según la convención | `ls docs/adr` sin salida en el filtro del apartado 4 | No cumple | No existe directorio de ADR en el estado etiquetado. |
| ADR aceptados no reescritos | historial de cada ADR anterior sin commits de reescritura, o reemplazo declarado | No cumple | No hay ADR en el estado etiquetado que permita demostrar esta regla. |
| `docs/ia.md` al día para la semana | commits sobre el archivo dentro del periodo revisado, con lo rechazado y su motivo | No cumple | En `corte-1`, `docs/ia.md:9-10` solo contiene entradas del 07/08. |
| Sin credenciales en el repositorio ni en el historial | `git grep` y `git log -S` sin coincidencias | Cumple | Búsquedas de patrones de secretos, `.env` versionado y llaves privadas sin coincidencias en HEAD. |
| Contribución de todos los integrantes | `git shortlog -sne` con todos los integrantes del equipo | Cumple | En HEAD aparecen cuatro personas consolidadas: CarlosManrique-1397, i-matallana, charlygz21 y nerlis-otero; `i-matallana` usa dos correos. |

## Estado global del proyecto (overall · HEAD)

- HEAD `e113f833` incorpora trabajo posterior a la etiqueta: un flujo visible de zonas y ubicación simulada (`lib/main.dart:30-59`, `lib/services/ubicacion_service.dart:15-21`) y un ADR 0002 con alternativas y consecuencias (`docs/adr/0002.md:54-66`, `196-203`).
- Ese avance no está entregado por la etiqueta. Tampoco prueba correspondencia con la restricción externa.
- El diagnóstico y la trazabilidad global siguen desalineados: `docs/aspectos.md:7` aún habla de realidad aumentada, C4 por definir y ausencia de ADR, mientras el ADR 0002 descarta RA (`docs/adr/0002.md:17-33`).
- La estructura sigue fuera de convención por `docs/Arc42/` y `docs/C4/`, y `docs/adr/0002.md` no cumple el nombre `NNNN-titulo-en-kebab-case.md`.
- El ADR 0001 fue reescrito en varios commits entre el 23/08 y el 31/08. El contrato exige crear un ADR sustituto y conservar el aceptado.
- El único test visible es una prueba de humo del esqueleto (`test/app_smoke_test.dart:6-18`); no cubre el cambio de ubicación. No hay workflow ni run de CI que consultar.
- No hay medición de línea base ni resultado reproducible contra umbral. `docs/ia.md` llega al 30/08 y no registra el trabajo de S5.
- El repositorio versiona `.dart_tool/`, artefacto local que debe excluirse.

## Nivel de rúbrica sugerido

Propuesta preliminar al docente. La sustentación no se infiere del repositorio.

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | no demostrado | 0,00 | La etiqueta apunta a S1; falta la restricción externa y no hay diagnóstico del reto en el estado entregado. |
| Alternativas y decisión | no demostrado | 0,00 | No hay ADR en `corte-1`. |
| Aplicación sobre el corte vertical | no demostrado | 0,00 | `corte-1` no contiene código ni arranque reproducible. |
| Pruebas, medición y trazabilidad | no demostrado | 0,00 | No hay pruebas, medición ni cadena completa en la etiqueta. |
| Sustentación del reto | lo fija el docente | pendiente | Requiere sesión. |
| **Subtotal técnico** | | **0,00 / 4,00** | No es la nota total sobre 5,00. |

## Recuento

**0 de 12 criterios Cumple.** La restricción, el PDF y la sustentación siguen No verificados; los demás criterios no se satisfacen en la etiqueta.

## No verificados

- Restricción asignada: hace falta la consigna individual del equipo.
- PDF de dos páginas: hace falta el adjunto de Moodle.
- Sustentación: la resuelve el docente en sesión.

## Hallazgos

- `corte-1` está fijada en el commit inicial de S1 y deja fuera todo el avance actual.
- El HEAD presenta un cambio arquitectónico y código nuevo, pero no medición, prueba específica, CI ni trazabilidad actualizada.
- Hay reescritura de ADR aceptado y desviaciones de estructura y versionado de artefactos locales.

## Preguntas para la sustentación

- ¿Cuál fue la restricción asignada y qué evidencia demuestra que el cambio de ubicación/Observer responde a ella?
- ¿Qué medición inicial ejecutaron, con qué herramienta, carga y procedimiento, y cuál fue el resultado posterior?
- ¿Por qué `corte-1` sigue en S1 y cómo van a conservar la historia de ADR sin reescribir decisiones aceptadas?
