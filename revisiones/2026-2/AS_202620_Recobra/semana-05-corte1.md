# semana-05-corte1 · Recobra

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `905f546` (2026-09-01T08:43:20-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | hash_calificado 905f546 2026-09-01T08:43:20-05:00; sin salida de git tag --list ni git log -1 corte-1 | No verificado | El commit calificado es anterior al cierre, pero no se evidencia la existencia de la etiqueta. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | sin acceso al adjunto de Moodle en la evidencia del repositorio | No verificado | Se requiere el PDF de la entrega para verificar su contenido. |
| Impacto de la restricción localizado en requisitos, C4 y código | no consta la restricción asignada al equipo; docs/Restricciones_justificadas.md lista restricciones propias, no el reto | No verificado | Sin la restricción asignada no se puede juzgar el diagnóstico. |
| Línea base medida y verificable antes del cambio | docs/escenarios_calidad.md define umbrales (p.ej. S1 ≤400 ms p95) pero no hay cifra medida con herramienta y procedimiento en 905f546 | No cumple | No hay línea base verificable. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | solo docs/adr/0001-estilo-arquitectonico.md en 905f546; sin ADR nuevo del reto | No cumple | El ADR existente es de estilo arquitectónico, no del reto de corte 1. |
| Cambio implementado y ejecutable de extremo a extremo | README.md documenta npm install && npm start; sin runs_ci ni evidencia de ejecución | No verificado | No se puede verificar el arranque sin un run que lo demuestre. |
| Límites declarados conservados tras el cambio | docs/c4/README.md declara contenedores; sin verificación post-cambio | No verificado | Sin cambio identificado, no se puede comprobar la conservación de límites. |
| Prueba que cubre el cambio, en verde en el pipeline | runs_ci vacío; sin URL de run anterior a la etiqueta | No cumple | No hay pipeline configurado ni ejecución en verde. |
| Resultado contrastado con el umbral del escenario y reproducible | sin medición con herramienta, carga y procedimiento en 905f546 | No cumple | No hay resultado reproducible. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md en 905f546 tiene 4 columnas (Aspecto, Decisión, Justificación, Pruebas), no las 8 del contrato | No cumple | Faltan ID, Requisito, C4, ADR, Código y Evidencia; sin enlaces navegables. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md en 905f546 registra descarte de microservicios (2026-08-23) y declaraciones genéricas; sin entrada del reto de corte 1 | No cumple | No hay salida de IA de este corte con motivo técnico. |
| Sustentación del reto | sesión de sustentación, no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible:true, repo AS_202620_Recobra en ISCOUTB; autores consolidados en 905f546: Cconde31+Steamlinker (Camilo), vylrir (Veronica), MiguelJacome (Miguel), fconde (Fernando) | Cumple | Los 4 integrantes declarados tienen commits. |
| Estructura mínima | README.md, docs/arc42/04-estrategia-solucion.md, docs/adr/0001-*.md, docs/c4/README.md, docs/aspectos.md, docs/ia.md en 905f546 | Cumple | node_modules versionado y docs/arc42.md suelto; desviación menor. |
| Estado del repositorio que se califica | sin etiqueta corte-1 evidenciada; hash calificado 905f546 anterior al cierre | No cumple | Según contrato, etiqueta ausente deja la fila en No cumple. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md con contexto, alternativas, decisión, consecuencias y referencias en 905f546 | Cumple | Cumple formato y contenido; no hay ADR del reto. |
| Tabla de aspectos | docs/aspectos.md en 905f546 con 4 columnas y una fila | No cumple | Faltan 4 columnas y enlaces navegables. |
| Registro de uso de IA | docs/ia.md en 905f546 con tabla de usos y descarte de microservicios con motivo; log con commits 2026-08-23 y 2026-08-30 | Cumple | El registro existe y crece. |
| README | README.md en 905f546 documenta npm install && npm start y npm test | Cumple | Arranque reproducible documentado. |
| Pipeline y análisis estático | runs_ci vacío; sin .github/workflows en el árbol de 905f546 | No cumple | No hay CI ni SonarCloud. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `905f546b4530502951f37714572e83b141042428 2026-09-01T08:43:20-05:00 Corte 1 informe`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene avances de semanas anteriores (ADR-0001, README, corte vertical), pero la entrega de corte 1 no responde al reto: sin ADR del reto, sin medición, sin pipeline, y con pendientes de estructura y trazabilidad.

Pendientes que siguen abiertos:
- Confirmar etiqueta corte-1
- PDF de dos páginas
- ADR del reto con alternativas y consecuencias
- Línea base medida y reproducible
- Pipeline con pruebas en verde
- docs/aspectos.md con 8 columnas
- Registro de IA del corte
- Rotar token de Coveralls
- Eliminar node_modules del repositorio

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1
- PDF de dos páginas
- Impacto de la restricción
- Cambio implementado
- Límites conservados
- Sustentación

## Hallazgos para la planilla

- node_modules versionado en el repositorio (905f546).
- Token de Coveralls en node_modules/debug/.coveralls.yml:1 (905f546).
- Sin pipeline de CI: runs_ci vacío.
- docs/aspectos.md no cumple las 8 columnas del contrato.
- Sin ADR del reto de corte 1; solo ADR-0001 de estilo.
- Sin evidencia de la restricción asignada al equipo.
- Sin medición de línea base ni resultado contrastado.
- docs/ia.md sin entrada específica del reto de corte 1.
- Etiqueta corte-1 no evidenciada.
- Autoría muy desigual: Fernando con 1 commit.
