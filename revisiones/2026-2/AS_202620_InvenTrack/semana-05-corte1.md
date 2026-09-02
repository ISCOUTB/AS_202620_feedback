# semana-05-corte1 · InvenTrack

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `202e225` (2026-09-01T02:40:57-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta corte-1 sobre un commit anterior al cierre | hash_calificado 202e225, fecha 2026-09-01T02:40:57-05:00 (anterior al cierre 2026-09-07T05:00:00Z) | No verificado | No se proporcionó salida de git tag --list ni git log -1 corte-1; no se confirma la existencia de la etiqueta. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No presente en el repositorio; se adjunta en Moodle | No verificado | No verificable desde la evidencia del repositorio. |
| Impacto de la restricción localizado en requisitos, C4 y código | Sin diagnóstico de restricción nueva; docs existentes son de S1-S4 | No cumple | No se identificó la restricción asignada ni su impacto. |
| Línea base medida y verificable antes del cambio | No hay cifra con herramienta y procedimiento | No cumple | Falta línea base verificable. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo docs/adr/0001-...md; head menciona ADR-0002/0003 inexistentes | No cumple | No hay ADR del reto. |
| Cambio implementado y ejecutable de extremo a extremo | No hay commit que implemente un ADR del reto; README documenta arranque de S4 | No cumple | Sin cambio atribuible al reto. |
| Límites declarados conservados tras el cambio | C4 containers.md declara límites; sin cambio no hay comparación | No cumple | No aplica por ausencia de cambio. |
| Prueba que cubre el cambio, en verde en el pipeline | Runs CI en verde (p.ej. 33483307820) pero cubren tests de S4 | No cumple | No hay prueba nueva del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición con herramienta, carga y procedimiento | No cumple | Falta resultado contrastado con umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md tiene fila ASP-01 navegable a ADR-0001; head referencia ADR-0002/0003 inexistentes | No cumple | La cadena del reto no existe; referencias rotas. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md última entrada 2026-08-30 (S4) | No cumple | Sin salida de IA de la semana 5. |
| Sustentación del reto | Sesión en aula | No verificado | No verificable desde el repositorio. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_InvenTrack en ISCOUTB, visible; autores consolidados: Jose Vargas, Esteban Peluffo, Felix Taborda, Javier Carta | Cumple | Los 4 integrantes aparecen en el historial. |
| Estructura mínima | docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | docs/c4/containers.md (plural) es desviación menor de la ruta mínima. |
| Qué estado del repositorio se califica | hash calificado 202e225 anterior al cierre; sin salida de git tag | No verificado | No se pudo confirmar la etiqueta corte-1. |
| Convenciones de ADR | ADR-0001 sigue nomenclatura y tiene contexto, alternativas, decisión, consecuencias | Cumple | Head menciona ADR-0002/0003 que no existen; referencias rotas. |
| La tabla de aspectos | docs/aspectos.md con fila ASP-01 de 8 columnas navegable | Cumple | No hay fila para el reto de la semana 5. |
| Registro de uso de IA | docs/ia.md con entradas hasta 2026-08-30; sin entrada de la semana 5 | No cumple | Falta salida aceptada/corregida/rechazada de este corte. |
| README | README documenta arranque con python -m uvicorn app.main:app --reload y pruebas pytest | Cumple | Reproducible. |
| Pipeline y análisis estático | .github/workflows/test.yml ejecuta pytest; runs en verde; sin evidencia de SonarCloud | No cumple | Falta análisis estático SonarCloud exigido por el contrato. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `202e2253f0eadc4619008a6d40dff657128ab94a 2026-09-01T02:40:57-05:00 Fix references to ADR-0002 and ADR-0003 in documentation`
- **Veredicto**: con pendientes
- Resumen: El proyecto mantiene la línea base de S1-S4, pero el reto del corte 1 (diagnóstico, ADR, implementación, medición, trazabilidad e IA) no se evidencia en el commit calificado 202e225.

Pendientes que siguen abiertos:
- ADR del reto
- Diagnóstico con línea base
- Implementación del cambio
- Prueba y medición
- Registro de IA del corte
- Referencias a ADR-0002/0003 rotas
- SonarCloud

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1
- PDF de dos páginas
- Sustentación del reto
- Qué estado del repositorio se califica (matriz transversal)

## Hallazgos para la planilla

- No hay ADR nuevo para el reto de la semana 5; solo existe ADR-0001 de la semana 3.
- El mensaje del commit head referencia ADR-0002 y ADR-0003 que no existen en el árbol.
- No hay diagnóstico de la restricción asignada ni línea base medida.
- docs/ia.md no registra usos de IA de la semana 5.
- No hay evidencia de SonarCloud en el repositorio.
- La etiqueta corte-1 no se pudo verificar en la evidencia proporcionada.
- El PDF de dos páginas se entrega en Moodle, no verificable desde el repositorio.
- Las pruebas de CI están en verde pero cubren el corte vertical de semanas anteriores, no un cambio del reto.
- El apartado 11 del contrato no fue proporcionado; la matriz transversal se infiere de las secciones 1-10.
