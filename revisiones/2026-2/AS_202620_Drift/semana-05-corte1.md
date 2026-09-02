# semana-05-corte1 · Drift

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `d7a61cc` (2026-08-31T20:45:45-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | hash_calificado d7a61cc 2026-08-31T20:45:45-05:00, anterior al cierre | No verificado | Falta salida de git tag --list y git log -1 corte-1 para confirmar la etiqueta. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay PDF en el repositorio | No verificado | El PDF se adjunta en Moodle; no es accesible desde el repositorio. |
| Impacto de la restricción localizado en requisitos, C4 y código | No hay diagnóstico de restricción en docs/adr/ ni docs/arc42/ | No verificado | No se proporcionó la restricción asignada al equipo; sin ella no se puede juzgar. |
| Línea base medida y verificable antes del cambio | docs/escenarios.md define medidas (≤3 s p95) pero sin medición real | No cumple | No hay cifra con herramienta y procedimiento de medición. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/ solo contiene 0001 y 0002, ambos de arquitectura base | No cumple | No hay ADR que responda a la restricción del reto. |
| Cambio implementado y ejecutable de extremo a extremo | commits_nuevos_desde_cierre_anterior: sin commits nuevos | No cumple | No hay commit que implemente un ADR del reto. |
| Límites declarados conservados tras el cambio | docs/c4/contenedores.md describe Web/API, Aplicación, Dominio, Adaptadores, Persistencia | No verificado | Sin cambio del reto, no hay límites que contrastar. |
| Prueba que cubre el cambio, en verde en el pipeline | backend/tests/test_health.py y .github/workflows/ci.yml existen | No verificado | No hay runs_ci con URL; no se verifica ejecución en verde. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay herramienta, carga ni procedimiento de medición en el repositorio | No cumple | Falta resultado contrastado con umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md tiene columnas ID, Aspecto, Fuente, Estímulo, Artefacto, Entorno, Respuesta, Medida | No cumple | No tiene columnas Requisito, C4, ADR, Código, Pruebas, Evidencia; enlaces solo a escenarios.md. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md con 5 registros (fecha, herramienta, prompt, uso) | No cumple | No hay columna de aceptado/corregido/rechazado con motivo técnico. |
| Sustentación del reto | No verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible=true, repo=AS_202620_Drift; autores consolidados: JerryDBM/Sherry, JoshuaR01/JoshXX, lmpdiaz12, maufern4ndez | Cumple | 4 personas consolidadas, coincide con los integrantes declarados. |
| Estructura mínima | arbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Desviaciones menores: nombres de archivos arc42 con mayúsculas y 'vista_bloques' vs 'bloques_construccion'. |
| Versionado y estado calificado | hash_calificado d7a61cc anterior al cierre; sin salida de git tag --list | No verificado | No se confirma la etiqueta corte-1. |
| Convenciones de ADR | docs/adr/0001-arquitectura-base.md y 0002-arquitectura-base.md con título 'Selección de Arquitectura Base' | No cumple | El título enuncia el tema, no la decisión; ADR-0001 no está marcado como reemplazado. |
| Tabla de aspectos y trazabilidad | docs/aspectos.md sin columnas Requisito, C4, ADR, Código, Pruebas, Evidencia | No cumple | No cumple el formato de 8 columnas del contrato. |
| Registro de uso de IA | docs/ia.md con registros de uso pero sin sección de rechazado con motivo | No cumple | Falta la columna de lo rechazado y por qué. |
| README y reproducibilidad | README.md presente pero truncado en la evidencia | No verificado | No se ven comandos de arranque en el fragmento disponible. |
| Pipeline, secretos y autoría | .github/workflows/ci.yml existe; secretos sin coincidencias; 4 autores | No verificado | Sin runs_ci no se verifica el pipeline; secretos y autoría cumplen. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `d7a61cc222416b9101abd731bc909a2427c37c29 2026-08-31T20:45:45-05:00 ci: corregir ejecución de pruebas backend`
- **Veredicto**: con pendientes
- Resumen: El repositorio tiene documentación base y código inicial, pero la respuesta al reto del corte 1 (diagnóstico, ADR, cambio, medición, trazabilidad) no está presente en el commit calificado.

Pendientes que siguen abiertos:
- Verificar/crear etiqueta corte-1
- Registrar ADR del reto con alternativas y decisión
- Medir línea base con procedimiento
- Completar aspectos.md con 8 columnas
- Añadir rechazos con motivo en ia.md
- Evidenciar run de CI en verde

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1: falta salida de git tag --list y git log -1 corte-1.
- PDF de dos páginas: adjunto en Moodle, no accesible desde el repositorio.
- Restricción asignada al equipo: no proporcionada, sin ella no se juzga el diagnóstico.
- Prueba en pipeline: existe ci.yml y test_health.py, pero no hay runs_ci con URL.
- README: texto truncado en la evidencia, no se ven comandos de arranque.
- Límites C4 tras el cambio: no hay cambio del reto que contrastar.

## Hallazgos para la planilla

- No se verificó la existencia de la etiqueta corte-1.
- No hay ADR del reto; solo ADR-0001/0002 de la línea base.
- No hay diagnóstico de la restricción asignada ni línea base medida.
- docs/aspectos.md no tiene las 8 columnas de trazabilidad del contrato.
- docs/ia.md no registra salidas rechazadas con motivo técnico.
- No hay runs de CI verificables para la prueba del cambio.
- README truncado en la evidencia; no se confirma comando de arranque único.
- Los títulos de los ADR enuncian el tema, no la decisión.
