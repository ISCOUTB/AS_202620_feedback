# semana-05-corte1 · DinamikUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `10d50eb` (2026-09-01T01:23:25-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | hash_calificado 10d50eb con fecha 2026-09-01T01:23:25-05:00, anterior al cierre 2026-09-07T05:00:00Z; sin salida de git tag --list ni git log -1 corte-1 | No verificado | No se pudo confirmar que la etiqueta corte-1 exista y apunte a ese commit. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay documento adjunto en la evidencia del repositorio | No verificado | El PDF se entrega en Moodle; no es verificable desde el repositorio. |
| Impacto de la restricción localizado en requisitos, C4 y código | No se conoce la restricción asignada al equipo; no se identifica un apartado de diagnóstico en los documentos visibles | No verificado | Falta la restricción asignada para juzgar si el diagnóstico localiza lo que debía. |
| Línea base medida y verificable antes del cambio | No se encontró una cifra con herramienta y procedimiento asociada a una restricción nueva | No verificado | Los escenarios Q-01 a Q-08 tienen medidas, pero no se puede vincular ninguna a la restricción del reto. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/0002-seleccion-tecnologia-backend-frontend.md existe con alternativas, factores, decisión y consecuencias, ligado a Q-01/Q-02/Q-03 | No verificado | No se puede confirmar que sea el ADR del reto sin conocer la restricción asignada. |
| Cambio implementado y ejecutable de extremo a extremo | README.md documenta start.bat; backend y frontend presentes | No verificado | Sin la restricción no se puede identificar qué cambio se esperaba ni verificar que funcione de extremo a extremo. |
| Límites declarados conservados tras el cambio | docs/c4/contenedores.puml y contexto.puml presentes; estructura backend/app/<modulo>/ coincide con ADR-0001 | No verificado | No se puede verificar la conservación de límites tras un cambio no identificado. |
| Prueba que cubre el cambio, en verde en el pipeline | backend/tests/test_requisitos.py y frontend/test/widget_test.dart existen; .github/workflows/ci.yml presente | No verificado | No hay runs_ci en la evidencia; se necesita URL de un run anterior a la etiqueta. |
| Resultado contrastado con el umbral del escenario y reproducible | No se encontró medición con herramienta, carga y procedimiento | No verificado | Falta evidencia de medición reproducible. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md existe y los ADRs referencian aspectos A-01 a A-08 | No verificado | No se pudo recorrer la fila del aspecto tocado por el reto; falta el contenido de docs/aspectos.md. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md existe con 13 commits en el historial | No verificado | No se pudo comprobar el contenido; falta el archivo. |
| Sustentación del reto | La ficha indica que se resuelve en sesión | No verificado | Lo resuelve el docente en la sustentación. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_DinamikUTB en ISCOUTB, visible; autores consolidados en 4 personas (Juan José Vargas Pérez, Luis Daniel Padilla Leottau, Gillianis Perez, Esteban Ramirez) | Cumple | Los 4 integrantes declarados aparecen en el historial. |
| Estructura mínima | README.md, docs/arc42/01-12, docs/adr/0001-0002, docs/c4/, docs/aspectos.md, docs/ia.md presentes | Cumple | Se cumple la estructura mínima del contrato. |
| Estado del repositorio que se califica (versionado) | hash_calificado 10d50eb anterior al cierre; sin salida de git tag --list | No verificado | No se pudo confirmar la existencia de la etiqueta corte-1. |
| Convenciones de ADR | docs/adr/0001-seleccion-monolito-modular.md y 0002-seleccion-tecnologia-backend-frontend.md siguen NNNN-titulo-kebab-case.md y tienen contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | No se detectaron ADRs reescritos. |
| Tabla de aspectos | docs/aspectos.md existe; referenciado desde ADRs y arc42 | No verificado | No se pudo verificar el contenido ni la navegabilidad de las celdas. |
| Registro de uso de IA | docs/ia.md existe con historial de commits | No verificado | No se pudo comprobar si incluye salidas aceptadas/corregidas/rechazadas con motivo técnico. |
| README | README.md documenta qué es el sistema, start.bat como comando único de arranque, y comandos de prueba (pytest, flutter test) | Cumple | Cumple con la sección 7 del contrato. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe | No verificado | No hay runs_ci en la evidencia; se necesita URL de un run para verificar ejecución en verde. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `10d50eb1409c29f5936e08102990a74513a98d09 2026-09-01T01:23:25-05:00 Update ia.md`
- **Veredicto**: al dia
- Resumen: La línea base del proyecto (estructura, identidad, README, ADRs) está sólida y no hay commits posteriores al cierre. Sin embargo, la respuesta al reto del corte 1 no se puede evaluar sin la restricción asignada y sin evidencia adicional (etiqueta, PDF, runs_ci, contenido de ia.md y aspectos.md).

Pendientes que siguen abiertos:
- Confirmar existencia de etiqueta corte-1
- Aportar PDF de dos páginas en Moodle
- Conocer la restricción asignada para evaluar el diagnóstico
- Aportar runs_ci del pipeline en verde
- Completar docs/ia.md con salida aceptada/corregida/rechazada
- Verificar navegabilidad de docs/aspectos.md

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1
- PDF de dos páginas
- Impacto de la restricción localizado
- Línea base medida
- ADR del reto
- Cambio implementado
- Límites conservados
- Prueba en pipeline
- Medición contra umbral
- Cadena de trazabilidad
- Registro de IA
- Sustentación
- Versionado (matriz transversal)
- Tabla de aspectos (matriz transversal)
- Registro de IA (matriz transversal)
- Pipeline y análisis estático (matriz transversal)

## Hallazgos para la planilla

- No se pudo confirmar la existencia de la etiqueta corte-1.
- Falta la restricción asignada al equipo para evaluar el diagnóstico del reto.
- No hay runs_ci en la evidencia; no se puede verificar el pipeline en verde.
- docs/ia.md y docs/aspectos.md existen pero su contenido no está disponible en la evidencia.
- El ADR-0002 podría ser la respuesta al reto si la restricción fue tecnológica, pero no se puede confirmar.
- No se encontró medición reproducible con herramienta, carga y procedimiento.
