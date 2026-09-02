# semana-05-corte1 · TAIA

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `c087303` (2026-08-30T18:54:10-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | git tag --list no muestra corte-1; hash calificado c087303 (2026-08-30T18:54:10-05:00) anterior al cierre 2026-09-07T05:00:00Z. | No cumple | Etiqueta ausente; se revisó el último commit anterior al cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No accesible desde el repositorio; requiere adjunto en Moodle. | No verificado | No verificable sin el documento. |
| Impacto de la restricción localizado en requisitos, C4 y código | docs/adr solo contiene 0001-estilo-arquitectonico.md; head c087303 es un commit de documentación sin cambios de código. | No cumple | No se proporcionó la restricción asignada; no hay diagnóstico del reto en el repositorio. |
| Línea base medida y verificable antes del cambio | No hay cifra con herramienta y procedimiento en el repositorio. | No cumple | escenarios_calidad.md define umbrales pero no mediciones. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | ls docs/adr/ → solo 0001-estilo-arquitectonico.md. | No cumple | No existe ADR del reto. |
| Cambio implementado y ejecutable de extremo a extremo | No hay commit que implemente un ADR del reto; head es 'docs: change prueba (readme) add ia entry (ia.md) change c2 text'. | No cumple | README documenta arranque con run.bat, pero no hay cambio del reto. |
| Límites declarados conservados tras el cambio | No hay cambio del reto que verificar; C4-C2 y estructura backend coinciden para el corte vertical anterior. | No cumple | No aplica porque no hay implementación del reto. |
| Prueba que cubre el cambio, en verde en el pipeline | runs_ci vacío; no hay evidencia de ejecución en pipeline. | No cumple | Existen pruebas locales (test_academic_register_task.py) pero sin run de CI. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición contra umbral en el repositorio. | No cumple | Falta herramienta, carga y procedimiento. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md tiene fila A-01 navegable, pero corresponde al corte vertical de la semana 4. | No cumple | No hay fila del aspecto del reto. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md entradas 004 y 005 (2026-08-29 y 2026-08-30) con aceptado/rechazado y motivos, pero referidas al corte vertical de la semana 4. | No cumple | Ninguna entrada menciona el reto de línea base. |
| Sustentación del reto | No verificable desde el repositorio. | No verificado | Lo resuelve el docente en la sesión de sustentación. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant en ISCOUTB, público; 4 autores visibles (val, dei0811, mark, luis20072002) coinciden con los integrantes. | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima | README.md, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md presentes en el árbol. | Cumple | Incluye además docs/calidad y docs/ficha_problema.md. |
| Versionado | No existe etiqueta corte-1; se revisó c087303 (2026-08-30T18:54:10-05:00), anterior al cierre. | No cumple | Etiqueta ausente; se aplicó la resolución del contrato. |
| Convenciones de ADR | 0001-estilo-arquitectonico.md cumple el formato NNNN-titulo-en-kebab-case. | Cumple | Sin reescrituras detectadas. |
| Tabla de aspectos | docs/aspectos.md con fila A-01 y 8 columnas navegables. | Cumple | Corresponde al corte vertical anterior; el reto no tiene fila. |
| Registro de uso de IA | docs/ia.md con 5 entradas, cada una con aceptado/rechazado y motivo. | Cumple | Ninguna entrada referida al reto de línea base. |
| README | README.md documenta qué es, arranque con run.bat y pruebas con pytest backend/tests. | Cumple | Requisitos previos declarados. |
| Pipeline y análisis estático | No hay .github/workflows en el árbol; runs_ci vacío. | No cumple | Sin evidencia de integración continua ni análisis estático. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `c0873031acbab61c644e1fac546915b7dde5d1cb 2026-08-30T18:54:10-05:00 docs: change prueba  (readme) add ia entry (ia.md) change c2 text`
- **Veredicto**: con pendientes
- Resumen: El repositorio conserva el corte vertical A-01 de la semana 4 con documentación y pruebas, pero la entrega del reto de línea base no se evidencia: falta la etiqueta corte-1, no hay ADR del reto, no hay medición de línea base ni resultado contra umbral, y no hay pipeline de CI.

Pendientes que siguen abiertos:
- Etiqueta corte-1
- PDF de dos páginas
- Diagnóstico de la restricción con línea base medida
- ADR del reto
- Implementación del cambio
- Prueba en CI
- Medición contra umbral
- Trazabilidad del reto en aspectos.md
- Registro de IA del reto
- Pipeline de CI

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- PDF de dos páginas (adjunto en Moodle, no accesible desde el repositorio).
- Sustentación del reto (se resuelve en sesión).
- Restricción asignada al equipo (no proporcionada; sin ella no se puede juzgar el diagnóstico).

## Hallazgos para la planilla

- No existe la etiqueta corte-1; se revisó el último commit c087303 anterior al cierre.
- docs/adr solo contiene 0001-estilo-arquitectonico.md; no hay ADR del reto.
- No hay evidencia de diagnóstico, línea base medida ni medición contra umbral.
- runs_ci vacío: no hay pipeline configurado ni ejecuciones.
- docs/ia.md registra 5 entradas, pero ninguna referida al reto de línea base.
- La fila A-01 de aspectos.md es navegable, pero corresponde al corte vertical de la semana 4.
- docs/ia.md entrada 005 deja pendiente ejecutar pytest.
