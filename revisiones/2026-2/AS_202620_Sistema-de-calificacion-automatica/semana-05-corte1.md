# semana-05-corte1 · Calificación automática

> Revisión manual preliminar completa realizada el 2026-09-03, antes del cierre. El equipo puede modificar el repositorio y la evaluacion definitiva debe repetirse despues de `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `cede35e` (2026-08-30T23:51:34-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | revisión manual local, solo lectura; no se ejecutó código |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Consulta manual `git tag --list`: no existe `corte-1`; se revisó el HEAD anterior al cierre | No cumple | Falta la etiqueta exigida por la ficha. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay documento adjunto en la evidencia del repositorio | No verificado | Depende de la entrega en Moodle; no verificable desde el repo |
| Impacto de la restricción localizado en requisitos, C4 y código | ADR-0004 y ADR-0005 localizan impacto en RNF-01, RF-06/07, EC-05 y C4 (LLM punteado) | No verificado | No se pudo contrastar con la restricción asignada porque no fue proporcionada |
| Línea base medida y verificable antes del cambio | ADR-0002 declara que no existe medición de CPU por hoja; aspectos.md A-01 declara 'CI y medición pendientes' | No cumple | No hay cifra con herramienta y procedimiento; falta línea base verificable |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/0004-quitar-validacion-simbolica-obligatoria-de-la-clave.md y docs/adr/0005-acotar-el-llm-a-la-generacion-de-distractores-diagnosticos.md incluyen contexto, alternativas, fuerzas, decisión y consecuencias, ligados a EC-05 | No cumple | Estructuralmente cumplen; falta confirmar que sean los del reto sin la restricción asignada |
| Cambio implementado y ejecutable de extremo a extremo | No se identificó commit que implemente el ADR del reto en código; README documenta arranque con docker compose up | No cumple | El cambio parece documental; sin commit de implementación visible |
| Límites declarados conservados tras el cambio | C4 Nivel 1 muestra LLM como opcional punteado, consistente con ADR-0005; backend con módulos de ADR-0002 | No cumple | Nivel 2 del C4 no visible completo; no se pudo verificar correspondencia total |
| Prueba que cubre el cambio, en verde en el pipeline | .github/workflows/ci.yml existe; sin runs_ci en la evidencia | No cumple | Falta URL de run en verde anterior a la etiqueta |
| Resultado contrastado con el umbral del escenario y reproducible | aspectos.md A-01 declara 'CI y medición pendientes'; sin herramienta, carga ni procedimiento | No cumple | Resultado no contrastado con umbral; medición no reproducible |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md fila A-04: Código Pendiente, Pruebas Pendiente, Evidencia Pendiente; A-01 tiene enlaces | No cumple | La fila del aspecto tocado por el reto (A-04) no es navegable de punta a punta |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md existe con entradas hasta 2026-08-30; contenido no visible en la evidencia | No cumple | No se pudo verificar la columna de rechazado con motivo técnico |
| Sustentación del reto | Sesión de sustentación, no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_Sistema-de-calificacion-automatica en ISCOUTB, visible; autores: scp1109, josueacademico17-source, SusanaRosales, Mariadelmar-restrepo | Cumple | Los cuatro integrantes declarados aparecen en el historial |
| Estructura mínima | Árbol incluye docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | Cumple la estructura mínima |
| Estado que se califica (versionado) | Consulta Git manual confirma que no existe la etiqueta `corte-1`; se identifica HEAD como estado preliminar | No cumple | Falta el estado versionado exigido por la ficha. |
| Convenciones de ADR | 5 ADR en docs/adr con nombres NNNN-kebab-case; 0001 reemplazado por 0002 | Cumple | Cumple la convención de no editar aceptados |
| Tabla de aspectos | docs/aspectos.md con 8 columnas y 5 aspectos; A-01 con enlaces a código, pruebas y evidencia | Cumple | A-02 a A-05 con celdas Pendiente; A-04 sin código/pruebas/evidencia |
| Registro de uso de IA | docs/ia.md existe con 6 commits en el log; contenido no visible en la evidencia | No verificado | No se pudo verificar la columna de rechazado con motivo técnico |
| README | README.md describe el sistema, arranque con docker compose up y pruebas | Cumple | Cumple |
| Pipeline y análisis estático | .github/workflows/ci.yml existe; sin runs_ci en la evidencia | No verificado | No se pudo verificar ejecución en verde |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `cede35e4229f8dae2aad95e6ffe92b453b4715a8 2026-08-30T23:51:34-05:00 Las secciones 5 y 6 describen el estado real del código`
- **Veredicto**: con pendientes
- Resumen: Proyecto con base sólida de documentación y corte vertical A-01 construido; la respuesta al reto del corte 1 no está completamente evidenciada (etiqueta, restricción, medición, pipeline, trazabilidad A-04).

Pendientes que siguen abiertos:
- Crear la etiqueta `corte-1` sobre el estado que se someterá antes del cierre.
- Contrastar diagnóstico con la restricción asignada
- Medir línea base y resultado contra umbral
- Evidenciar pipeline en verde
- Completar trazabilidad de A-04
- Verificar contenido de docs/ia.md

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

- No se confirmó la etiqueta corte-1 en la evidencia.
- La restricción asignada al equipo no fue proporcionada; el diagnóstico no se puede contrastar.
- No hay línea base medida con herramienta y procedimiento.
- La fila A-04 de aspectos.md tiene código, pruebas y evidencia pendientes.
- No hay runs de CI visibles para verificar pruebas en verde.
- docs/ia.md existe pero su contenido no fue accesible en la evidencia.
- El C4 Nivel 1 refleja el LLM acotado, pero el Nivel 2 no se pudo verificar completo.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada y dónde se localiza su impacto en requisitos, C4 y código?
2. ¿Cuál fue la cifra de línea base, con qué herramienta y procedimiento se obtuvo, y cuál fue el resultado posterior?
3. ¿Qué ADR y commit implementan el reto, y qué prueba del pipeline demuestra el cambio?
