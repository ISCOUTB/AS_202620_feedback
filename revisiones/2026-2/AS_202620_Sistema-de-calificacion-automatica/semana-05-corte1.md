# semana-05-corte1 · Calificación automática

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `cede35e` (2026-08-30T23:51:34-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Commit calificado cede35e 2026-08-30T23:51:34-05:00; sin salida de git tag --list en la evidencia | No verificado | No se pudo confirmar la etiqueta; haría falta ejecutar git tag --list y git log -1 corte-1 |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay documento adjunto en la evidencia del repositorio | No verificado | Depende de la entrega en Moodle; no verificable desde el repo |
| Impacto de la restricción localizado en requisitos, C4 y código | ADR-0004 y ADR-0005 localizan impacto en RNF-01, RF-06/07, EC-05 y C4 (LLM punteado) | No verificado | No se pudo contrastar con la restricción asignada porque no fue proporcionada |
| Línea base medida y verificable antes del cambio | ADR-0002 declara que no existe medición de CPU por hoja; aspectos.md A-01 declara 'CI y medición pendientes' | No cumple | No hay cifra con herramienta y procedimiento; falta línea base verificable |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/0004-quitar-validacion-simbolica-obligatoria-de-la-clave.md y docs/adr/0005-acotar-el-llm-a-la-generacion-de-distractores-diagnosticos.md incluyen contexto, alternativas, fuerzas, decisión y consecuencias, ligados a EC-05 | Cumple | Estructuralmente cumplen; falta confirmar que sean los del reto sin la restricción asignada |
| Cambio implementado y ejecutable de extremo a extremo | No se identificó commit que implemente el ADR del reto en código; README documenta arranque con docker compose up | No verificado | El cambio parece documental; sin commit de implementación visible |
| Límites declarados conservados tras el cambio | C4 Nivel 1 muestra LLM como opcional punteado, consistente con ADR-0005; backend con módulos de ADR-0002 | No verificado | Nivel 2 del C4 no visible completo; no se pudo verificar correspondencia total |
| Prueba que cubre el cambio, en verde en el pipeline | .github/workflows/ci.yml existe; sin runs_ci en la evidencia | No verificado | Falta URL de run en verde anterior a la etiqueta |
| Resultado contrastado con el umbral del escenario y reproducible | aspectos.md A-01 declara 'CI y medición pendientes'; sin herramienta, carga ni procedimiento | No cumple | Resultado no contrastado con umbral; medición no reproducible |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md fila A-04: Código Pendiente, Pruebas Pendiente, Evidencia Pendiente; A-01 tiene enlaces | No cumple | La fila del aspecto tocado por el reto (A-04) no es navegable de punta a punta |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md existe con entradas hasta 2026-08-30; contenido no visible en la evidencia | No verificado | No se pudo verificar la columna de rechazado con motivo técnico |
| Sustentación del reto | Sesión de sustentación, no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_Sistema-de-calificacion-automatica en ISCOUTB, visible; autores: scp1109, josueacademico17-source, SusanaRosales, Mariadelmar-restrepo | Cumple | Los cuatro integrantes declarados aparecen en el historial |
| Estructura mínima | Árbol incluye docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | Cumple la estructura mínima |
| Estado que se califica (versionado) | Commit calificado cede35e 2026-08-30T23:51:34-05:00, anterior al cierre; sin salida de git tag --list | No verificado | No se pudo confirmar la etiqueta corte-1 |
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
- Confirmar etiqueta corte-1
- Contrastar diagnóstico con la restricción asignada
- Medir línea base y resultado contra umbral
- Evidenciar pipeline en verde
- Completar trazabilidad de A-04
- Verificar contenido de docs/ia.md

## Recuento y nota sugerida

1 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1 (falta git tag --list)
- PDF de dos páginas (depende de Moodle)
- Restricción asignada (no proporcionada)
- Cambio implementado (sin commit visible)
- Límites C4 (Nivel 2 no visible)
- Prueba en pipeline (sin runs_ci)
- docs/ia.md (contenido no visible)
- Sustentación (no verificable desde el repo)
- Versionado transversal (etiqueta no confirmada)
- IA transversal (contenido no visible)
- Pipeline transversal (sin runs_ci)

## Hallazgos para la planilla

- No se confirmó la etiqueta corte-1 en la evidencia.
- La restricción asignada al equipo no fue proporcionada; el diagnóstico no se puede contrastar.
- No hay línea base medida con herramienta y procedimiento.
- La fila A-04 de aspectos.md tiene código, pruebas y evidencia pendientes.
- No hay runs de CI visibles para verificar pruebas en verde.
- docs/ia.md existe pero su contenido no fue accesible en la evidencia.
- El C4 Nivel 1 refleja el LLM acotado, pero el Nivel 2 no se pudo verificar completo.
