# semana-05-corte1 · CampusMarket

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `f3f4367` (2026-08-30T22:55:30-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | modo early; sin etiqueta corte-1; se revisa f3f4367 (2026-08-30T22:55:30-05:00) | No cumple | Etiqueta ausente; último commit anterior al cierre f3f4367. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Adjunto en Moodle, no accesible desde el repositorio | No verificado | Requiere acceso a la entrega de Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | Sin commits entre S4 y cierre; docs/aspectos.md y arc42 sin cambios desde S4 | No cumple | No hay diagnóstico de restricción nueva; se desconoce la restricción asignada. |
| Línea base medida y verificable antes del cambio | Sin medición con herramienta y procedimiento en el repositorio | No cumple | docs/arc42/10-escenarios-de-calidad.md define umbrales pero no hay medición ejecutada. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existe docs/adr/0001-usar-monolito-modular.md (S3) | No cumple | No hay ADR nuevo para el reto de la semana 5. |
| Cambio implementado y ejecutable de extremo a extremo | Sin commit que implemente ADR del reto; README.md documenta arranque S4 con scripts/run_s4.sh | No cumple | El corte vertical S4 existe pero no hay cambio del reto. |
| Límites declarados conservados tras el cambio | Sin cambio del reto que verificar; docs/c4/02-contenedores.puml corresponde al código S4 | No verificado | No aplica porque no hay cambio del reto. |
| Prueba que cubre el cambio, en verde en el pipeline | runs_ci verdes (p.ej. 33355385223 success) solo ejecutan test_publicaciones_vertical.py y test_health.py | No cumple | No hay prueba que cubra un cambio del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | Sin medición del reto ni contraste con umbral | No cumple | No hay evidencia reproducible de herramienta, carga y procedimiento. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md con ASP-01/02 incompletas (—) y sin fila del reto | No cumple | ASP-05 llega hasta Pruebas con Evidencia S4, pero no cubre el reto. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md última entrada 2026-08-30 (S4); sin entradas de la semana 5 | No cumple | No hay registro de IA para este corte. |
| Sustentación del reto | Sesión de sustentación, no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET público; autores consolidados: Nnigarp, camilixo92, Carulla-sd | Cumple | Los tres integrantes declarados aparecen en el historial. |
| Estructura mínima | docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md presentes en el árbol | Cumple | Estructura conforme al contrato. |
| Estado del repositorio que se califica | Sin etiqueta corte-1; se califica f3f4367 (2026-08-30T22:55:30-05:00) | No cumple | Etiqueta ausente; contrato sección 3. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md cumple formato NNNN-kebab-case y contiene contexto, alternativas, decisión, consecuencias | Cumple | Sin ADR reescritos; falta ADR del reto (ficha). |
| Tabla de aspectos | docs/aspectos.md con ASP-01/02 incompletas (—) y sin fila del reto | No cumple | Cadena con huecos; no defendible para el corte. |
| Registro de uso de IA | docs/ia.md con entradas S1-S4 (última 2026-08-30); sin entrada del corte 1 | No cumple | El registro existe pero no cubre la semana 5. |
| README | README.md con arranque scripts/run_s4.sh y pruebas pytest | Cumple | Comando de arranque documentado; no ejecutado en esta revisión. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml; runs success (p.ej. 33355385223) | Cumple | Sin SonarCloud aún; esperado desde segundo corte. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `f3f436713bc79a7da4d5792c4f0876cc85fcdd3c 2026-08-30T22:55:30-05:00 Merge pull request #13 from ISCOUTB/S4-registro-ia-cierre`
- **Veredicto**: con pendientes
- Resumen: El proyecto está en la línea base de S4; el reto del corte 1 no tiene evidencia en el repositorio a HEAD.

Pendientes que siguen abiertos:
- Etiqueta corte-1
- Diagnóstico de la restricción asignada
- ADR del reto con alternativas y decisión
- Implementación del cambio sobre el corte vertical
- Pruebas y medición contra umbral
- Trazabilidad del reto en docs/aspectos.md
- Registro de IA del corte en docs/ia.md
- PDF de dos páginas en Moodle

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- PDF de dos páginas (adjunto Moodle, no accesible).
- Límites conservados tras el cambio (no hay cambio del reto).
- Sustentación del reto (sesión docente).

## Hallazgos para la planilla

- No existe la etiqueta corte-1; se revisa el último commit f3f4367 anterior al cierre.
- No hay commits nuevos entre S4 y el cierre de la semana 5; el reto no tiene trabajo subido.
- No hay ADR nuevo para el reto; solo persiste ADR-0001 de S3.
- docs/aspectos.md no tiene fila para el reto y ASP-01/02 tienen huecos.
- docs/ia.md no registra usos de IA de la semana 5.
- Los runs de CI en verde solo cubren pruebas de S4, no el reto.
- Sin medición de línea base ni contraste con umbral para el reto.
