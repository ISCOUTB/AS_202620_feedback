# semana-05-corte1 · ElMapita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `4806374` (2026-09-01T08:39:54-06:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | hash_calificado 4806374, fecha 2026-09-01T08:39:54-06:00 (anterior al cierre); no se aportó salida de `git tag --list` ni `git log -1 corte-1` | No verificado | El commit calificado es anterior al cierre, pero no se pudo confirmar la existencia de la etiqueta. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | docs/cortes/corte-1.pdf presente en el árbol; contenido binario no legible desde la evidencia; adjunto de Moodle no disponible | No verificado | No se pudo verificar que el PDF tenga dos páginas ni los contenidos exigidos. |
| Impacto de la restricción localizado en requisitos, C4 y código | La restricción asignada al equipo no fue proporcionada en la solicitud; sin ella no se puede juzgar el diagnóstico | No verificado | Falta la restricción para contrastar el diagnóstico con lo exigido. |
| Línea base medida y verificable antes del cambio | docs/aspectos.md filas EC-01 a EC-04: columna Evidencia = 'Pendiente'; sin cifra, herramienta ni procedimiento | No cumple | No hay estado inicial medido y verificable. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existe docs/adr/0001-estilo-arquitectonico-propuesto.md (2026-08-22); sin ADR nuevo entre S4 y corte-1 | No cumple | El ADR existente es de la decisión de estilo, no del reto de la semana 5. |
| Cambio implementado y ejecutable de extremo a extremo | README.md documenta scripts/dev.sh y dev.ps1; no se identifica commit que implemente un cambio del reto | No verificado | Sin la restricción ni un ADR del reto no se puede localizar el cambio. |
| Límites declarados conservados tras el cambio | docs/c4/C4_L1_Context.md y C4_L2_Container.md presentes; no hay cambio del reto que contrastar con la estructura | No verificado | No se pudo verificar correspondencia tras un cambio inexistente o no identificado. |
| Prueba que cubre el cambio, en verde en el pipeline | .github/workflows/ci.yml existe; no se aportaron runs_ci; docs/aspectos.md marca pruebas como '(pendiente)' | No verificado | Sin runs anteriores a la etiqueta no se puede confirmar ejecución en verde. |
| Resultado contrastado con el umbral del escenario y reproducible | docs/aspectos.md Evidencia = 'Pendiente' en EC-01 a EC-04; sin herramienta, carga ni procedimiento | No cumple | No hay medición reproducible contra umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md: Pruebas '(pendiente)' y Evidencia 'Pendiente' en las 4 filas; celdas sin enlaces | No cumple | La cadena se rompe en Pruebas y Evidencia. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md con commits 2026-08-30 y 2026-08-07; contenido no disponible en la evidencia | No verificado | No se pudo leer el archivo para verificar la entrada de este corte. |
| Sustentación del reto | Sesión de sustentación; no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | shortlog HEAD: RobotDRMX 12, Rodrigo Vazquez Rico 1, dgarza2705 1; Angel Fabian Gutierrez Gomez sin commits | No cumple | Falta consolidar identidades; un integrante declarado no aparece en el historial. |
| Estructura mínima | ls-tree: docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Se versiona un archivo temporal de Word: docs/~$rteVertical_ElMapitaUTB.docx. |
| Estado del repositorio que se califica | hash_calificado 4806374 anterior al cierre; sin confirmación de la etiqueta corte-1 | No verificado | Falta salida de `git tag --list` y `git log -1 corte-1`. |
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
- Confirmar etiqueta corte-1

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Existencia de la etiqueta corte-1
- Contenido del PDF de dos páginas
- Diagnóstico del impacto de la restricción (restricción no proporcionada)
- Cambio implementado del reto
- Conservación de límites C4 tras el cambio
- Prueba en verde en pipeline (sin runs_ci)
- Contenido de docs/ia.md
- Sustentación (sesión)

## Hallazgos para la planilla

- No se proporcionó la restricción asignada, necesaria para evaluar el diagnóstico.
- docs/aspectos.md deja Pruebas y Evidencia en 'Pendiente' en EC-01 a EC-04.
- No hay ADR del reto; solo ADR-0001 del 2026-08-22.
- Angel Fabian Gutierrez Gomez no aparece en el historial de HEAD.
- Archivo temporal docs/~$rteVertical_ElMapitaUTB.docx versionado.
- Sin runs de CI ni mediciones reproducibles en la evidencia.
- docs/cortes/corte-1.pdf presente pero sin contenido verificable.
