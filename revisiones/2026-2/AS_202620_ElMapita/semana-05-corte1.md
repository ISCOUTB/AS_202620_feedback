# semana-05-corte1 · ElMapita

> Revisión manual preliminar completa realizada el 2026-09-03, antes del cierre. El equipo puede modificar el repositorio y la evaluacion definitiva debe repetirse despues de `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `4806374` (2026-09-01T08:39:54-06:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | revisión manual local, solo lectura; no se ejecutó código |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Consulta manual `git tag --list`: no existe `corte-1`; se revisó el HEAD anterior al cierre | No cumple | Falta la etiqueta exigida por la ficha. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | `docs/cortes/corte-1.pdf` fue inspeccionado: tiene 8 páginas y documenta el corte vertical de línea base; el adjunto de Moodle no está disponible | No verificado | El PDF versionado no cumple la extensión de dos páginas ni demuestra la respuesta al reto; no sustituye la verificación del adjunto de Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | La restricción asignada al equipo no fue proporcionada en la solicitud; sin ella no se puede juzgar el diagnóstico | No verificado | Falta la restricción para contrastar el diagnóstico con lo exigido. |
| Línea base medida y verificable antes del cambio | docs/aspectos.md filas EC-01 a EC-04: columna Evidencia = 'Pendiente'; sin cifra, herramienta ni procedimiento | No cumple | No hay estado inicial medido y verificable. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existe docs/adr/0001-estilo-arquitectonico-propuesto.md (2026-08-22); sin ADR nuevo entre S4 y corte-1 | No cumple | El ADR existente es de la decisión de estilo, no del reto de la semana 5. |
| Cambio implementado y ejecutable de extremo a extremo | README.md documenta scripts/dev.sh y dev.ps1; no se identifica commit que implemente un cambio del reto | No cumple | Sin la restricción ni un ADR del reto no se puede localizar el cambio. |
| Límites declarados conservados tras el cambio | docs/c4/C4_L1_Context.md y C4_L2_Container.md presentes; no hay cambio del reto que contrastar con la estructura | No cumple | No se pudo verificar correspondencia tras un cambio inexistente o no identificado. |
| Prueba que cubre el cambio, en verde en el pipeline | .github/workflows/ci.yml existe; no se aportaron runs_ci; docs/aspectos.md marca pruebas como '(pendiente)' | No cumple | Sin runs anteriores a la etiqueta no se puede confirmar ejecución en verde. |
| Resultado contrastado con el umbral del escenario y reproducible | docs/aspectos.md Evidencia = 'Pendiente' en EC-01 a EC-04; sin herramienta, carga ni procedimiento | No cumple | No hay medición reproducible contra umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md: Pruebas '(pendiente)' y Evidencia 'Pendiente' en las 4 filas; celdas sin enlaces | No cumple | La cadena se rompe en Pruebas y Evidencia. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md con commits 2026-08-30 y 2026-08-07; contenido no disponible en la evidencia | No cumple | No se pudo leer el archivo para verificar la entrada de este corte. |
| Sustentación del reto | Sesión de sustentación; no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | shortlog HEAD: RobotDRMX 12, Rodrigo Vazquez Rico 1, dgarza2705 1; Angel Fabian Gutierrez Gomez sin commits | No cumple | Falta consolidar identidades; un integrante declarado no aparece en el historial. |
| Estructura mínima | ls-tree: docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Se versiona un archivo temporal de Word: docs/~$rteVertical_ElMapitaUTB.docx. |
| Estado del repositorio que se califica | Consulta Git manual confirma que no existe la etiqueta `corte-1`; se identifica HEAD como estado preliminar | No cumple | Falta el estado versionado exigido por la ficha. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico-propuesto.md con contexto, alternativas, decisión, consecuencias y nombre según convención | Cumple | Solo hay un ADR; no se evidencia reescritura posterior. |
| Tabla de aspectos | docs/aspectos.md: Pruebas '(pendiente)' y Evidencia 'Pendiente' en EC-01 a EC-04 | No cumple | Filas con huecos no defendibles. |
| Registro de uso de IA | docs/ia.md existe con commits 2026-08-30 y 2026-08-07; contenido no disponible | No verificado | No se pudo verificar la columna de rechazos con motivo técnico. |
| README | README.md describe el sistema, comandos de arranque (scripts/dev.sh, dev.ps1) y cómo probar | Cumple | El arranque requiere configuración previa de .env, declarada en prerrequisitos. |
| Pipeline y análisis estático | .github/workflows/ci.yml presente; sin runs_ci ni evidencia de SonarCloud | No verificado | No se pudo confirmar ejecución en verde. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `4806374a4d643707611720836e59dd436e7a441f 2026-09-01T08:39:54-06:00 corte-1`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene estructura y documentación base, pero la entrega del corte 1 no evidencia la respuesta al reto: falta ADR del reto, línea base medida, trazabilidad completa y pruebas en CI.

Pendientes que siguen abiertos:
- ADR del reto
- Línea base medida y verificable
- Cadena de trazabilidad completa en docs/aspectos.md
- Prueba en verde en pipeline
- Medición reproducible contra umbral
- Registro de IA con motivo técnico verificable
- Crear la etiqueta `corte-1` sobre el estado que se someterá antes del cierre.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia evaluable del reto | 0,00 | No se identifica una respuesta a la restricción nueva; la restricción asignada tampoco está disponible. |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | Los ADR visibles corresponden a decisiones de la línea base o son anteriores al inicio de S5. |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | No hay cambio trazable a una restricción nueva. |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | Las pruebas o el CI de la línea base no demuestran una medición antes/después del reto. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico verificable** |  | **0,00 / 4,00** | No constituye el total sobre 5,00. |

## Recuento

0 de 12 criterios Cumple.

## No verificado / pendientes

- Coincidencia del diagnóstico con la restricción asignada, porque la asignación no está disponible en el kit.
- PDF adjunto en Moodle.
- Sustentación del reto.

## Hallazgos para la planilla

- No se proporcionó la restricción asignada, necesaria para evaluar el diagnóstico.
- docs/aspectos.md deja Pruebas y Evidencia en 'Pendiente' en EC-01 a EC-04.
- No hay ADR del reto; solo ADR-0001 del 2026-08-22.
- Angel Fabian Gutierrez Gomez no aparece en el historial de HEAD.
- Archivo temporal docs/~$rteVertical_ElMapitaUTB.docx versionado.
- Sin runs de CI ni mediciones reproducibles en la evidencia.
- docs/cortes/corte-1.pdf presente pero sin contenido verificable.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada y dónde se localiza su impacto en requisitos, C4 y código?
2. ¿Cuál fue la cifra de línea base, con qué herramienta y procedimiento se obtuvo, y cuál fue el resultado posterior?
3. ¿Qué ADR y commit implementan el reto, y qué prueba del pipeline demuestra el cambio?
