# semana-04-evidencia-s4 · Recobra

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `2268b33` (2026-08-30T22:34:56-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42.md:1-120, docs/arc42/04-estrategia-solucion.md:1-86 | Cumple | Secciones 1-3, 5 y 6 en arc42.md; sección 4 desarrollada en arc42/04; sin rastros de plantilla. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42.md no contiene encabezado 'Sección 9'; no existe docs/arc42/09-*.md; docs/adr/0001-estilo-arquitectonico.md no está citado desde una sección 9 | No cumple | No se encuentra la sección de decisiones y su enlace a ADR en el commit calificado. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42.md:103-119 | Cumple | Sección 10 relaciona S1..S7 de docs/escenarios_calidad.md con decisiones de arquitectura. |
| Glosario iniciado con términos del dominio | docs/glosarios.md:1-20 | Cumple | Contiene términos propios del sistema (objeto perdido, reclamación, matching, trazabilidad). |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/README.md:4-62 | Cumple | Diagramas Mermaid nivel 1 y 2 con leyenda y flechas etiquetadas; actores y contenedores son coherentes entre niveles. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/README.md:28-37 vs estructura real del commit: solo src/domain, src/application, src/infrastructure y tests | No cumple | El C4 dibuja Flutter, PostgreSQL y proveedores externos que no existen en el código del commit calificado; no hay correspondencia con directorios. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md:44-49 y estructura del commit: src/domain/entities/publicacion.js, src/application/use-cases/crear-publicacion.js, src/infrastructure/adapters/persistence/memoria-publicacion-repository.js | Cumple | El README cita explícitamente las tres capas del recorrido HTTP → caso de uso → puerto de persistencia. |
| Arranque documentado con un solo comando | README.md:27-30 | Cumple | Declara requisito Node.js 18 y el comando único `npm install && npm start`. |
| Prueba automatizada del recorrido completo, en verde | tests/publicaciones-http.test.js declarado en README.md:31-33; sin runs_ci con run en verde del commit calificado | No verificado | No hay evidencia de ejecución del pipeline (URL de run) para el commit 2268b33; comando anotado: `npm test`. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md:1-10 | No cumple | La tabla tiene 4 columnas (Aspecto, Decisión, Justificación, Pruebas) en vez de las 8 requeridas; falta ID, Requisito, C4, ADR, Código, Evidencia; las celdas no enlazan a artefactos. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| 1. Identidad del repositorio | repo AS_202620_Recobra en ISCOUTB, visible=true; integrantes con commits en historial | Cumple | Nombre, organización y visibilidad coinciden con el contrato. |
| 2. Estructura mínima | Árbol del commit 2268b33: docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | No cumple | Estructura base presente, pero arc42 se concentra en un único arc42.md sin las 12 secciones separadas; también hay node_modules versionado en el repositorio (desviación de higiene). |
| 3. Estado del repositorio calificado | hash_calificado=2268b33, fecha 2026-08-30T22:34:56-05:00; commits_post_cierre listados | Cumple | Se calificó el último commit anterior al cierre (2026-08-31T05:00:00Z); hay commits posteriores que se registran en overall. |
| 4. Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md | Cumple | Un ADR por archivo, numerado 0001, nombre en kebab-case, con contexto, alternativas, decisión y consecuencias. |
| 5. Tabla de aspectos | docs/aspectos.md:1-10 | No cumple | La tabla solo tiene 4 columnas; la cadena aspecto→requisito→C4→ADR→código→pruebas no es navegable. |
| 6. Registro de uso de IA | docs/ia.md con tabla de usos, herramienta, aceptado/rechazado; log del archivo con commits en agosto-septiembre | Cumple | El registro incluye criterio del equipo y secciones por integrante; cumple la forma pedida. |
| 7. README | README.md:9-49 | Cumple | Explica qué es el sistema, requisitos, comando de arranque, pruebas y estructura del corte vertical. |
| 8. Pipeline y análisis estático | No hay .github/workflows en el árbol del commit 2268b33; sin runs_ci citados | No verificado | En HEAD existe .github/workflows/ci.yml, pero no se evidencia ejecución en el commit calificado; hace falta run o configuración en el estado revisado. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `f7c1a6c7c4371f1e9df38ca268895544cca43c17 2026-09-07T09:59:41-05:00 Enlazar ADR a sus commits y cubrir criterios 1-3 de la rúbrica del reto`
- **Veredicto**: con pendientes
- Resumen: El proyecto en HEAD ha evolucionado bastante después del cierre de la semana 4 (backend NestJS, frontend Flutter, CI, ADR nuevos, informe de corte), pero esas correcciones llegaron tarde y la entrega evaluada (2268b33) no cumple todos los criterios de la ficha: falta la sección 9, la tabla de aspectos está incompleta y no hay evidencia de pruebas en CI. Además, la documentación del HEAD (arc42.md) sigue sin sección 9 explícita y los C4 aún dibujan contenedores que el código no refleja del todo.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Corte vertical y documentación de publicación: commits 87ada13, 10c239b, 905f546 del 31 ago/1 sep (posteriores al cierre).
- Migración a NestJS/Flutter, CI y ADR 0002/0003: commits 3a82ca6, 316a994, dc91a8b, e68eb8e, 25525ae, 6ee5b66, f7c1a6c del 5 al 7 de septiembre.
- Corrección de identidad de autor con .mailmap: 6ee5b66 (posterior al cierre).

Pendientes que siguen abiertos:
- Redactar sección 9 de arc42 enlazada a los ADR (sigue ausente en HEAD).
- Completar docs/aspectos.md con las 8 columnas y enlaces verificables.
- Dejar evidencia de CI en verde para el commit de la entrega (no solo en HEAD).
- Corregir correspondencia entre C4 nivel 2 y el código real.
- Eliminar node_modules del repositorio y aplicar .gitignore.

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba automatizada del recorrido completo en verde: falta URL de run de CI o registro de ejecución del commit 2268b33.
- Pipeline y análisis estático (matriz transversal): no hay .github/workflows en el commit calificado ni run citado.

## Hallazgos para la planilla

- No está redactada la sección 9 de arc42 ni enlazada con ADR.
- El C4 nivel 2 dibuja contenedores (Flutter, PostgreSQL) sin código correspondiente en el commit calificado.
- docs/aspectos.md tiene 4 columnas en lugar de las 8 del contrato.
- No hay evidencia de ejecución del pipeline ni de la prueba del corte vertical en verde.
- node_modules está versionado en el commit calificado y persiste en HEAD.
- La sección 12 (glosario) vive en docs/glosarios.md y no dentro de la estructura arc42, aunque contiene términos propios.
- docs/ia.md incluye marcadores genéricos '[Fernando Isacc Conde Herrera]' y '[Camilo Conde]' como títulos, no nombres de cuenta.
- Commits posteriores al cierre reestructuran el backend a NestJS y agregan Flutter: son cambios tardíos sobre la entrega de la semana 4.
- Commits posteriores al cierre (no calificados): f7c1a6c 2026-09-07T09:59:41-05:00 Enlazar ADR a sus commits y cubrir criterios 1-3 de la rúbrica del reto; 6ee5b66 2026-09-05T20:26:56-05:00 Agregar .mailmap para consolidar la identidad de Camilo (Steamlinker); 25525ae 2026-09-05T19:44:03-05:00 Reemplazar estimación aproximada de línea base por medición reproducible; e68eb8e 2026-09-05T13:21:41-05:00 Ocultar los scaffolds y scripts de la plataforma de las estadísticas de lenguaje de GitHub; dc91a8b 2026-09-05T13:08:27-05:00 Fix CI Flutter y hallazgos Sonar en Android debug
