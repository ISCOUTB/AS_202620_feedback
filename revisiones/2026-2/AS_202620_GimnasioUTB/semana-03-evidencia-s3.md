# semana-03-evidencia-s3 · GimnasioUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `73c1f24` (2026-08-23T19:38:29-05:00) |
| Cierre | 2026-08-24T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | docs/arc42_gimnasio_utb.md: sección 4 inicia pero se corta en 4.1; no se citan tácticas ni escenarios en la evidencia. | No cumple | La sección 4 está incompleta; falta contenido que ligue la estrategia a los escenarios ES1, ES7 y ES8. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | No aparece tabla comparativa en el fragmento de docs/arc42_gimnasio_utb.md; el ADR menciona 'matriz en sección 4.2' sin mostrarla. | No verificado | Se requiere leer el documento completo o la fila de arc42 para comprobar que exista la matriz con escenarios del equipo. |
| docs/adr/0001-*.md con el nombre de la convención | docs/adr/0001-arquitectura-hexagonal.md listado en docs/adr/0001-arquitectura-hexagonal.md. | Cumple | Nombre según convención NNNN-titulo-en-kebab-case. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | docs/adr/0001-arquitectura-hexagonal.md: contiene Contexto, Decisión, Alternativas consideradas y Consecuencias. | Cumple | Documenta correctamente los elementos exigidos. |
| Alternativas descartadas con su motivo | docs/adr/0001-arquitectura-hexagonal.md: apartado 'Alternativas consideradas' incluye A. Capas y B. Monolito Modular con motivos a favor/en contra. | Cumple | Las alternativas descartadas tienen su motivo explícito. |
| ADR alcanzable desde docs/aspectos.md y desde el escenario que lo motiva | docs/aspectos.md describe 'Consistencia de datos' sin enlaces ni referencias al ADR ni a escenarios ES1/ES7/ES8. | No cumple | No hay enlace navegable desde aspectos.md al ADR ni desde escenario de calidad. |
| Arranque con un solo comando documentado en el README | README.md: sección 'Cómo ejecutar el backend' documenta 'npm install && npm start' y package.json define 'start': 'node src/server.js'. | Cumple | Arranque documentado y soportado por package.json. |
| Prueba automatizada en verde | tests/health.test.js presente en el árbol; run CI con conclusion success en https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/33460309694 (2026-09-01T01:51:00Z). | Cumple | La prueba existe y hay evidencia de un run en verde, aunque el run es posterior al cierre. |
| Estructura de paquetes correspondiente al estilo del ADR | src/modules/aforo/{domain,application/ports,infrastructure/http,infrastructure/persistence} presente en el hash 73c1f24. | Cumple | Corresponde a la separación hexagonal descrita en el ADR. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio y visibilidad | repo visible en ISCOUTB/AS_202620_GimnasioUTB; visible=true en la evidencia. | Cumple | Nombre, organización y visibilidad coinciden con el contrato. |
| Estructura mínima del repositorio | El árbol en el hash calificado 73c1f24 tiene docs/arc42_gimnasio_utb.md, no docs/arc42/; falta docs/c4/. | No cumple | Desviación de estructura: arc42 fuera de su carpeta y C4 ausente como directorio. |
| Estado calificado y rama principal | hash_calificado 73c1f24 2026-08-23T19:38:29-05:00 anterior al cierre 2026-08-24T05:00:00Z. | Cumple | El commit evaluado es el vigente al cierre. |
| Convenciones de ADR (formato y no alteración) | docs/adr/0001-arquitectura-hexagonal.md está en la ruta y formato convencional; no se evidencia reescritura en el hash calificado. | Cumple | ADR 0001 cumple la convención; commit posterior ba45154 añade ADR0001.md sin borrar el original. |
| Tabla de aspectos trazable | docs/aspectos.md no contiene la tabla ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia; solo describe Consistencia de datos. | No cumple | No hay una fila navegable por aspecto; celdas sin enlaces son huecos. |
| Registro de uso de IA | docs/ia.md incluye entradas por semana con herramienta, prompt, salida y verificación; log de ia con commits desde a45615e hasta el cierre. | Cumple | El registro existe y crece; la columna de rechazo es menos detallada que la de aceptación. |
| README con arranque monolítico y prueba documentada | README.md: documenta 'npm install && npm start' para arrancar y 'npm test' para probar. | Cumple | Cumple con el arranque y la prueba documentados. |
| Pipeline y análisis estático | .github/workflows/ci.yml corre npm test, pero no hay archivo de configuración ni run de SonarCloud en el hash calificado. | No cumple | Falta análisis estático obligatorio por contrato. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `ba451547c00cdeea4adc7cd981c9f1fdd81ccfe8 2026-09-07T16:21:18-05:00 Add ADR0001 for Hexagonal Architecture adoption`
- **Veredicto**: con pendientes
- Resumen: A HEAD hay correcciones posteriores al cierre de la semana 3 que añaden ADR0001.md, reorganizan docs/arc42/ y docs/c4/, y agregan pruebas, pero todavía persisten problemas de trazabilidad y falta de análisis estático en el commit calificado.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Commit 38f0031 del 2026-09-01 y siguientes actualizan README después del cierre.
- Commit ba45154 del 2026-09-07 añade ADR0001.md y reorganiza docs/arc42/ y docs/c4/.
- Commits 9b9f7c8 y 56db96b actualizan docs/ia.md después del cierre.

Pendientes que siguen abiertos:
- Sección 4 completa de arc42 y matriz comparativa verificable.
- docs/aspectos.md con enlaces al ADR y a los escenarios.
- Integración de SonarCloud en el pipeline.
- Consolidar la estructura mínima en HEAD y mantener la trazabilidad en las próximas semanas.

## Recuento y nota sugerida

6 de 9 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (6/9).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Matriz comparativa de los tres estilos contra el árbol de utilidad: requiere contenido completo de la sección 4.2 de arc42 para confirmar que compara contra escenarios del equipo.

## Hallazgos para la planilla

- Sección 4 de arc42 incompleta en el commit calificado.
- docs/aspectos.md sin tabla trazable ni enlaces al ADR.
- Estructura mínima no respetada: arc42 fuera de docs/arc42/ y sin docs/c4/.
- No se evidencia integración de SonarCloud en el commit calificado.
- Commits posteriores al cierre (no calificados): ba45154 2026-09-07T16:21:18-05:00 Add ADR0001 for Hexagonal Architecture adoption; 9b9f7c8 2026-09-06T21:26:32-05:00 Update IA documentation with new project details; a71aece 2026-09-06T21:24:09-05:00 Actualizar registro de correcciones por entrega; 7094a6c 2026-09-06T21:16:32-05:00 Add corrections log for week 4; 38f0031 2026-09-01T12:07:42-05:00 Actualización del README
