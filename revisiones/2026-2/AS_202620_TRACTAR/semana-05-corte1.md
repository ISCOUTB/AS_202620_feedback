# semana-05-corte1 · TRACTAR

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `7cfb872` (2026-08-31T12:27:23-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | estado calificado 7cfb872 2026-08-31T12:27:23-05:00; sin salida de git tag --list en la evidencia | No verificado | No se pudo comprobar la existencia de la etiqueta; el commit es anterior al cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | adjunto en Moodle, no disponible en el repositorio | No verificado | Depende de la entrega en Moodle; no verificable desde el repo. |
| Impacto de la restricción localizado en requisitos, C4 y código | sin documento de diagnóstico en el árbol; arc42.md no muestra sección 11; no se conoce la restricción asignada | No cumple | No hay rastro del reto en el repositorio. |
| Línea base medida y verificable antes del cambio | no hay cifra con herramienta y procedimiento en el repo | No cumple | El README menciona 7 pruebas, pero no es línea base de calidad del reto. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | solo docs/adr/0001 y 0002, ambos anteriores; sin ADR nuevo | No cumple | No hay ADR que registre alternativas, fuerzas y decisión del reto. |
| Cambio implementado y ejecutable de extremo a extremo | sin commit que implemente un ADR del reto; el README documenta ./run.sh para el corte vertical S4 | No cumple | No hay cambio atribuible al reto. |
| Límites declarados conservados tras el cambio | C2.md y c4_nivel1.md existen y coinciden con app/, pero no hay cambio del reto que verificar | No cumple | Sin cambio, no hay 'tras el cambio'. |
| Prueba que cubre el cambio, en verde en el pipeline | tests/test_loans.py y test_resources.py cubren S4; run success 33419672964 posterior al commit, pero no cubre cambio del reto | No cumple | No hay prueba del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | sin medición en el repo | No cumple | No hay herramienta, carga ni procedimiento. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md fila A-06 con enlaces a ../arc42.md inexistente; C4 sin enlaces | No cumple | La cadena se rompe en requisito y C4. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md con 2 entradas del 2026-08-16, sin rechazos | No cumple | Ninguna entrada referida al reto de este corte. |
| Sustentación del reto | sesión de sustentación | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo declarado AS_202620_TRACTAR; runs_ci en ISCOUTB/AS_202620_UTB_TRACKER | No verificado | Apartado 11 no incluido en la entrada; se evalúan las secciones 1-8 del contrato. Discrepancia entre nombre declarado y runs; no se pudo confirmar correspondencia. |
| Estructura mínima | docs/arc42/arc42.md, docs/adr/0001, 0002, docs/c4/C2.md, c4_nivel1.md, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | arc42 en un solo archivo; desviación menor aceptable. |
| Versionado | commit 7cfb872 anterior al cierre; sin salida de git tag --list | No verificado | No se pudo comprobar la etiqueta corte-1. |
| Convenciones de ADR | ADR-0001 enlaza a ../arc42/10_requisitos_calidad.md inexistente; sin ADR del reto | No cumple | Formato correcto pero trazabilidad rota. |
| Tabla de aspectos | docs/aspectos.md con enlaces rotos a ../arc42.md y celdas C4 sin enlace | No cumple | Cadena no navegable. |
| Registro de IA | docs/ia.md sin entradas del corte actual ni rechazos con motivo | No cumple | No evidencia criterio técnico. |
| README y reproducibilidad | README.md documenta ./run.sh y pytest; run.sh existe | No verificado | No hay run de CI que ejecute run.sh; solo pytest. Enlace interno a docs/arc42.md roto. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo ejecuta pytest; sin SonarCloud | No cumple | Falta análisis estático exigido por el contrato. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849 2026-08-31T12:27:23-05:00 Fix: solved the text problem`
- **Veredicto**: con pendientes
- Resumen: El proyecto entero a HEAD conserva la línea base S1-S4, pero el reto del corte 1 no está resuelto en el repositorio y persisten incumplimientos del contrato (SonarCloud, autoría, enlaces rotos, IA sin rechazos).

Pendientes que siguen abiertos:
- Diagnóstico de la restricción asignada
- ADR del reto con alternativas, fuerzas y consecuencias
- Cambio implementado sobre el corte vertical
- Medición reproducible contra umbral
- Trazabilidad navegable en docs/aspectos.md
- Análisis estático SonarCloud en pipeline
- Registro de IA del corte con salidas rechazadas
- Participación de los 4 integrantes en el historial

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1: falta salida de git tag --list.
- PDF de dos páginas: adjunto en Moodle, no disponible.
- Sustentación: sesión, no verificable desde el repo.
- Identidad del repositorio: discrepancia entre nombre declarado y runs_ci.
- README y reproducibilidad: no hay run de CI que ejecute run.sh.

## Hallazgos para la planilla

- No hay evidencia de la etiqueta corte-1; se evaluó el commit 7cfb872.
- No se encuentra diagnóstico de la restricción asignada en el repositorio.
- No hay ADR nuevo del reto; solo existen 0001 y 0002 de semanas anteriores.
- No hay cambio implementado sobre el corte vertical atribuible al reto.
- No hay medición contra umbral con procedimiento reproducible.
- Enlaces rotos en docs/aspectos.md y ADR hacia rutas inexistentes de arc42.
- docs/ia.md no registra salidas rechazadas con motivo técnico ni usos del corte actual.
- El pipeline no incluye análisis estático SonarCloud.
- Solo un integrante aparece en el historial de commits; los otros tres declarados no tienen commits.
- Los runs de CI pertenecen a ISCOUTB/AS_202620_UTB_TRACKER mientras la evidencia declara el repo como AS_202620_TRACTAR.
