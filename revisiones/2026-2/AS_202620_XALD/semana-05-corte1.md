# Primer corte · reto de línea base arquitectónica · XALD

> Revisión manual preliminar completa, realizada antes del cierre. El equipo puede cambiar el repositorio y la valoración debe repetirse después del 2026-09-07T05:00:00Z.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `6081fedef33d8e194e24a3b8d3261215a4d90120` (2026-09-03T20:41:50-05:00) |
| Etiqueta `corte-1` | Ausente |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | Revisión manual con Codex, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` no devolvió etiquetas; HEAD `6081fed` | No cumple | La valoración preliminar usa HEAD. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay PDF versionado y Moodle no está disponible | No verificado | Debe comprobarse en Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | `docs/adr/0003-restriccion-os.md:2-9` documenta Android como restricción, pero no hay diagnóstico que la identifique como reto S5 | No verificado | La restricción asignada no está en el kit. |
| Línea base medida y verificable antes del cambio | `docs/arc42/arc42-template-EN.md:483-535` declara umbrales y herramientas, sin resultados medidos | No cumple | Definir cómo medir no demuestra una línea base. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Los ADR 0001-0005 registran decisiones y consecuencias; ninguno se declara como reto S5 ni contiene la comparación completa exigida | No cumple | Falta un ADR identificable del corte. |
| Cambio implementado y ejecutable de extremo a extremo | Los seis commits más recientes, de `ea868f9` a `6081fed`, son vacíos: el árbol de HEAD es idéntico al de `9a75929`; `README.md:10-43` describe pruebas de la línea base | No cumple | Los mensajes anuncian revisiones documentales, pero no contienen cambios ni implementan el reto. |
| Límites declarados conservados tras el cambio | El C4 declara Backend XALD, pero el árbol de código en HEAD contiene los cinco módulos Android sin backend | No cumple | Ya existe una divergencia entre diseño e implementación. |
| Prueba que cubre el cambio, en verde en el pipeline | `Cortevertical.kt` existe y el run `https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/33352959352` fue exitoso; no cubre un cambio S5 identificable | No cumple | El verde de la base no prueba la respuesta al reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No se encontró resultado de medición, solo umbrales previstos | No cumple | Falta herramienta ejecutada, carga y resultado. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:7-11` mantiene `Pendiente` en evidencia y en varias celdas de código/pruebas | No cumple | Ninguna fila del reto llega completa hasta evidencia. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md:9-19` registra decisiones generales; el commit `6081fed` titulado “revision de IA.MD” es vacío y no modifica el archivo | No cumple | No hay entrada atribuible al corte ni al reto nuevo. |
| Sustentación del reto | Requiere la sesión con el equipo | No verificado | Lo fija el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `ISCOUTB/AS_202620_XALD` | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | Las seis rutas obligatorias están presentes en HEAD | Cumple | Hay desviaciones internas, pero no ausencia. |
| Estado calificado identificable | HEAD `6081fed`, sin etiqueta `corte-1` | No cumple | En el corte se exige etiqueta. |
| Nombres de ADR según la convención | `0001-patron-offline-first.md` a `0006-seleccion-de-estilo-arquitectonico.md` | Cumple | Convención corregida. |
| ADR aceptados no reescritos | ADR aprobados 0001 y 0002 fueron modificados después de su aprobación (`4ca7f92` y otros) | No cumple | Los cambios debieron registrarse como reemplazo o ADR nuevo. |
| `docs/ia.md` al día para la semana | No hay cambio efectivo atribuible al reto S5 | No cumple | Tanto `015655a` como el nuevo `6081fed`, titulados como actualización de IA, son commits vacíos. |
| Sin credenciales en el repositorio ni en el historial | Barridos en HEAD e historial sin patrones de credenciales | Cumple | Sin hallazgos. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` muestra las cuatro identidades documentadas en EQUIPOS.md | Cumple | Los cuatro integrantes tienen contribución visible. |

## Estado global del proyecto en HEAD

- **HEAD revisado:** `6081fedef33d8e194e24a3b8d3261215a4d90120`, `revision de IA.MD`.
- **Veredicto:** con pendientes de coherencia y sin respuesta S5 verificable.
- El proyecto tiene código modular Android, C4, ADR, CI verde y participación de todo el equipo.
- La documentación declara umbrales, pero no resultados medidos; la tabla de aspectos sigue incompleta.
- El backend dibujado no aparece en el estado implementado y no existe etiqueta `corte-1`.
- Los seis commits publicados el 3 de septiembre no cambian el árbol del repositorio; sus mensajes no constituyen evidencia de avance.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje preliminar | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | No hay reto identificado ni línea base medida. |
| Alternativas y decisión | Insuficiente | 0,00 | No existe ADR atribuible al reto S5. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | No se identifica cambio S5 y hay divergencia C4/código. |
| Pruebas, medición y trazabilidad | Básico | 0,60 | Hay CI verde para la base, sin medición ni cadena completa del reto. |
| Sustentación del reto | Pendiente del docente | — | No verificable desde el repositorio. |
| **Subtotal técnico preliminar** |  | **0,60 / 4,00** | No es la nota final del corte. |

## Recuento

0 de 12 criterios de la ficha cumplen. El recuento no se convierte mediante la fórmula semanal porque este corte tiene rúbrica propia.

## Pendientes y preguntas para la sustentación

- ¿Cuál fue la restricción asignada y qué cambio concreto responde a ella?
- ¿Dónde está la línea base ejecutada y el resultado contra el umbral?
- ¿Por qué el C4 muestra un backend que no aparece en el árbol implementado?
- ¿Qué evidencia completa la fila del reto en `docs/aspectos.md`?
