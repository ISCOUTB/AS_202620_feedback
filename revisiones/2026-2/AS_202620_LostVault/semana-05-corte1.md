# semana-05-corte1 · LostVault

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `952af8f` (2026-08-30T22:13:14-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Sin salida de `git tag --list` ni `git log -1 corte-1`; commit calificado 952af8f (2026-08-30T22:13:14-05:00) anterior al cierre 2026-09-07T05:00:00Z. | No verificado | Falta confirmar que la etiqueta corte-1 existe y apunta a 952af8f. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Documento adjunto en Moodle, no accesible desde el repositorio. | No verificado | Requiere revisar la entrega en Moodle; no hay ruta en el repo. |
| Impacto de la restricción localizado en requisitos, C4 y código | No se recibió la restricción asignada; README.md y docs/aspectos.md solo documentan AS-03 de la línea base, sin diagnóstico de una restricción nueva. | No cumple | Sin la restricción no se puede juzgar; no hay sección de diagnóstico del reto. |
| Línea base medida y verificable antes del cambio | docs/arc42/10_requisitos_calidad.md define umbrales (99 %, p95 ≤2 s) pero sin medición; README.md declara que las métricas no están demostradas. | No cumple | Falta cifra con herramienta y procedimiento. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/ solo contiene 0001-estilo-arquitectonico.md; no hay ADR nuevo para el reto. | No cumple | Falta ADR ligado al escenario de calidad del reto. |
| Cambio implementado y ejecutable de extremo a extremo | Commit 952af8f 'Se realiza el corte vertical y la fila de aspectos' implementa AS-03 de la línea base; README.md documenta `flutter run -d chrome`. | No cumple | No hay commit que implemente un ADR del reto de la semana 5. |
| Límites declarados conservados tras el cambio | Sin cambio del reto no hay contra qué verificar; test/architecture_structure_test.dart protege la regla de dependencias en la línea base. | No verificado | Se podría verificar si existiera el cambio del reto. |
| Prueba que cubre el cambio, en verde en el pipeline | Run 'Flutter checks' 33560607903 success (2026-09-01) en https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/33560607903; cubre test/claim_object_use_case_test.dart, test/widget_test.dart y test/architecture_structure_test.dart. | No cumple | Pipeline en verde, pero sin prueba de un cambio del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición con herramienta, carga y procedimiento en el repositorio; solo umbrales declarados en docs/arc42/10_requisitos_calidad.md. | No cumple | Falta evidencia reproducible de la medición. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md tiene fila AS-03 navegable hasta pruebas, pero no hay fila para el reto de la semana 5. | No cumple | La cadena del reto no existe; solo la de la línea base. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md tiene registros hasta S3 (2026-08-24, commit edd78d7); sin entrada para el corte 1. | No cumple | Falta registro de IA del trabajo de esta semana. |
| Sustentación del reto | Criterio de sesión de sustentación, no verificable desde el repositorio. | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_LostVault público; autores en historial: Roy Gonzalez, Fausto-4, shamarallorente-blip, Jose Faustino España, weller-rar y Shamara Llorente Tapias, consolidados en 4 personas. | Cumple | Los 4 integrantes declarados aparecen en el historial. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes en HEAD. | Cumple | Hay además REVISION_CORREGIDA.md y carpetas ejecutable/front_end. |
| Qué estado del repositorio se califica | Sin salida de `git tag --list`; commit calificado 952af8f anterior al cierre. | No verificado | Falta confirmar la etiqueta corte-1; si está ausente, la fila quedaría en No cumple. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md sigue el formato NNNN-titulo-en-kebab-case; sin reescrituras posteriores. | Cumple | Solo existe un ADR; ninguno del reto de la semana 5. |
| La tabla de aspectos | docs/aspectos.md no tiene las 8 columnas del contrato (faltan Requisito y C4 como columnas); la fila AS-03 es navegable. | No cumple | Desviación de estructura: usa columnas como 'Escenario relacionado' y 'Decisión/compromiso'. |
| Registro de uso de IA | docs/ia.md registra S1-S3 con aceptado y rechazado con motivo técnico. | Cumple | Sin entradas nuevas para el corte 1. |
| README | README.md documenta arranque con `flutter run -d chrome` y pruebas con `flutter test`. | Cumple | Reproducible según el comando declarado. |
| Pipeline y análisis estático | .github/workflows/flutter.yml ejecuta flutter analyze y flutter test en verde (run 33560607903), pero no hay configuración ni evidencia de SonarCloud. | No cumple | Falta el análisis estático en SonarCloud exigido por el contrato. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `952af8f4f2230a4cd2258d361629579da8a6ade6 2026-08-30T22:13:14-05:00 Se realiza el corte vertical y la fila de aspectos`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene una línea base arquitectónica completa (arc42, C4, ADR 0001, corte vertical AS-03 ejecutable y probado), pero la respuesta al reto del corte 1 no está en el repositorio a HEAD: falta diagnóstico, ADR, cambio, medición y trazabilidad del reto.

Pendientes que siguen abiertos:
- Confirmar etiqueta corte-1
- Diagnóstico de la restricción asignada con línea base medida
- ADR del reto con alternativas, fuerzas, decisión y consecuencias
- Cambio implementado y ejecutable de extremo a extremo
- Medición contrastada con umbral y reproducible
- Trazabilidad del reto en docs/aspectos.md
- Registro de IA del corte 1 en docs/ia.md
- PDF de dos páginas en Moodle
- SonarCloud en el pipeline

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1 sobre un commit anterior al cierre
- PDF de dos páginas en Moodle
- Límites declarados conservados tras el cambio
- Sustentación del reto
- Qué estado del repositorio se califica (matriz transversal)

## Hallazgos para la planilla

- No se confirma la existencia de la etiqueta corte-1 en la evidencia proporcionada.
- No hay ADR nuevo para el reto de la semana 5; solo existe 0001-estilo-arquitectonico.md.
- No hay diagnóstico de la restricción asignada ni línea base medida.
- No hay medición contrastada con umbral ni procedimiento reproducible.
- docs/ia.md no registra usos de IA del corte 1.
- La fila AS-03 de docs/aspectos.md es navegable, pero no cubre el reto.
- Pipeline en verde, pero sin SonarCloud.
- docs/aspectos.md no usa las 8 columnas del contrato.
- El apartado 11 del contrato no fue incluido en la entrada; la matriz transversal se infiere de las secciones 1-8.
