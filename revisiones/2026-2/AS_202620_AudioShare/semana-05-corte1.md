# semana-05-corte1 · AudioShare

> Revisión manual preliminar completa realizada el 2026-09-03, antes del cierre. El equipo puede modificar el repositorio y la evaluación definitiva debe repetirse después de `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado preliminar revisado | `1a5179910ec4ba6191422bc31fc4028bce4468a8` (`2026-09-03T18:01:42-05:00`) |
| Referencia | `HEAD`; no existe la etiqueta `corte-1` |
| Cierre | `2026-09-07T05:00:00Z` |
| Revisor | revisión manual local, solo lectura; no se ejecutó código |

La restricción asignada y el PDF adjunto en Moodle no estuvieron disponibles. La evidencia interna permite comprobar la línea base, pero no demuestra qué reto externo debía responder el equipo.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` sin salida; `HEAD` `1a517991`, 2026-09-03 | No cumple | Se usa `HEAD` como estado preliminar por ausencia de etiqueta. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | El adjunto de Moodle no está disponible en el kit | No verificado | Debe comprobarse en Moodle; un archivo del repositorio no sustituye el adjunto. |
| Impacto de la restricción localizado en requisitos, C4 y código | No se declara cuál es el reto S5; `docs/aspectos.md:34-39` describe EC-01–EC-04 de la línea base | No verificado | Sin la restricción asignada no puede juzgarse correspondencia; el repositorio tampoco identifica una restricción nueva. |
| Línea base medida y verificable antes del cambio | `docs/aspectos.md:37-39` marca pendientes las mediciones y casos específicos; `docs/aspectos.md:103-107` solo transcribe un resultado de pruebas | No cumple | No hay cifra inicial obtenida con herramienta, carga y procedimiento. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo `docs/adr/0001-usar-monolito-modular.md`, fechado 2026-08-23 y todavía “propuesto” (`:1-6`); su implementación y pruebas siguen pendientes (`:46-51`) | No cumple | Es la decisión de estilo de la línea base, no un ADR identificable del reto S5. |
| Cambio implementado y ejecutable de extremo a extremo | `README.md:49-72` documenta el corte vertical A-01; desde el inicio de S5 los cambios son el merge `dd2025c` y tres correcciones documentales | No cumple | No se identifica un cambio que responda a una restricción nueva. No se ejecutó el sistema. |
| Límites declarados conservados tras el cambio | C4 declara cuatro contenedores (`docs/c4/Contenedor - Nivel 2.mmd:12-44`), mientras README declara un monolito modular (`README.md:29-32`) | No cumple | La representación de contenedores no corresponde al único proceso implementado; tampoco hay cambio S5 identificable que comparar. |
| Prueba que cubre el cambio, en verde en el pipeline | `tests/a01.test.ts` se describe en `README.md:19-27`; no existe `.github/workflows/` en el árbol | No cumple | La prueba cubre el corte vertical base, no un cambio S5, y no hay run de CI verificable. |
| Resultado contrastado con el umbral del escenario y reproducible | Los umbrales aparecen en `docs/aspectos.md:36-39`, pero las mediciones específicas quedan pendientes (`:37-39`) | No cumple | Falta resultado, herramienta, carga y procedimiento reproducible. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:34-39` enlaza requisito, ADR, C4, código y pruebas, pero usa diez columnas y no incluye `Evidencia`; varias pruebas/mediciones están pendientes | No cumple | La cadena se rompe en evidencia de calidad. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md:59-72` registra S1–S4; `docs/ia.md:93-100` declara que continuará actualizándose | No cumple | No hay entrada del reto S5. |
| Sustentación del reto | Requiere la sesión de sustentación | No verificado | Lo fija el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `github.com/ISCOUTB/AS_202620_AudioShare` completado el 2026-09-03 | Cumple | Nombre y visibilidad comprobados por protocolo Git. |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md` en `1a517991` | Cumple | arc42 usa AsciiDoc, desviación de formato respecto a Markdown. |
| Estado calificado identificable | `HEAD` `1a5179910ec4ba6191422bc31fc4028bce4468a8`, `2026-09-03T18:01:42-05:00` | Cumple | Estado preliminar identificable; falta la etiqueta exigida por la ficha. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md` | Cumple | Nombre conforme. |
| ADR aceptados no reescritos | `docs/adr/0001-usar-monolito-modular.md:3` continúa en estado “propuesto” | Cumple | No hay un ADR aceptado que pueda evaluarse como reescrito. |
| `docs/ia.md` al día para la semana | Última entrada visible: Semana 4 (`docs/ia.md:68-72`) | No cumple | Falta S5. |
| Sin credenciales en el repositorio ni en el historial | `git grep` y búsqueda histórica de `BEGIN PRIVATE KEY` sin coincidencias; no hay `.env` versionado | Cumple | Comprobación sobre HEAD e historial. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: cuatro identidades consolidadas para cuatro integrantes | Cumple | No se publican correos. |

## Estado global del proyecto (overall · HEAD)

- **HEAD revisado:** `1a5179910ec4ba6191422bc31fc4028bce4468a8`, `Revise README for clarity and organization`.
- **Veredicto:** línea base ejecutable y documentada, respuesta al reto S5 no identificable.
- El README ofrece un comando de arranque y uno de pruebas (`README.md:6-27`), y la prueba A-01 recorre sesión, persistencia, sincronización y audio.
- La trazabilidad mejoró en S5, pero aún carece de la columna y la evidencia de calidad exigidas (`docs/aspectos.md:34-39`).
- El C4 de contenedores sigue describiendo una solución distribuida que contradice el monolito implementado.
- No hay workflow, medición reproducible, ADR del reto ni registro de IA S5.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia | 0,00 | No se declara el reto S5 ni una línea base medida. |
| Alternativas y decisión | Sin evidencia | 0,00 | El único ADR pertenece a la línea base y sigue propuesto. |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | Hay corte vertical base, pero ningún cambio trazable a una restricción nueva. |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | No hay CI ni medición; la tabla termina antes de Evidencia. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico verificable** |  | **0,00 / 4,00** | No constituye total sobre 5,00. |

## Recuento

**0 de 12 criterios Cumple.** Revisión preliminar; no se propone total sobre 5,00 sin sustentación.

## No verificado

- Coincidencia del diagnóstico con la restricción asignada.
- PDF adjunto en Moodle.
- Sustentación del reto.

## Hallazgos

- Falta la etiqueta `corte-1`.
- La línea base de S4 está documentada, pero no hay respuesta identificable al reto S5.
- Falta medición antes/después contra un umbral reproducible.
- Falta CI y un run en verde que cubra el cambio.
- C4 e implementación representan límites diferentes.
- Falta la entrada de IA de S5.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada y qué archivos o componentes cambian específicamente por ella?
2. ¿Cuál fue la cifra de línea base, con qué herramienta, carga y procedimiento se obtuvo, y cuál fue el resultado posterior?
3. ¿Por qué el C4 representa cuatro contenedores si la implementación y el ADR declaran un monolito modular?
