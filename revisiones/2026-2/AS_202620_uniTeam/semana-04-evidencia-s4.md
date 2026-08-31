# semana-04-evidencia-s4 · uniTeam

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `dc14298` (2026-08-29T11:49:10-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-uniteam.md declara 'Secciones 1, 2, 3, 4, 5, 6, 9, 10, 11 y 12 redactadas'; commit ca51944 'arc42 secciones 5 y 6' | Cumple | La plantilla original se conserva aparte en arc42-template-EN.md sin sustituir; el documento principal no muestra rastros de plantilla en las secciones visibles. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/arc42-uniteam.md declara la sección 9 redactada; existen docs/adr/0001-0005 | No verificado | No se pudo comprobar que la sección 9 cite los ADR; haría falta leer el contenido de la sección 9 en el repositorio. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/calidad/escenarios-calidad.md contiene ESC-01 a ESC-05; la sección 10 se declara redactada | No verificado | No se pudo comprobar la correspondencia entre la sección 10 y los escenarios; falta leer su contenido. |
| Glosario iniciado con términos del dominio | docs/arc42/arc42-uniteam.md declara la sección 12 redactada | No verificado | No se pudo comprobar que el glosario use términos propios del sistema; falta leer la sección 12. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/nivel1-contexto.md y docs/c4/nivel2-contenedores.md; sección 'Correspondencia con el nivel 1' en nivel2 | Cumple | Diagramas como código Mermaid con leyenda y flechas etiquetadas; los tres actores y dos externos del nivel 1 reaparecen en el nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/nivel2-contenedores.md tabla 'Correspondencia con el código': web/app/, app/main.py+app/api+app/application+app/domain+app/events, app/infrastructure/ | Cumple | Las rutas citadas existen en el árbol del repositorio; el servicio de correo está marcado como previsto sin código, lo cual es explícito. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md cita test/test_corte_vertical.py como recorrido completo; ADR-0004 cita app/api/rutas_tareas.py, app/application/servicio_tareas.py, app/infrastructure/repositorios.py | Cumple | Interfaz HTTP en app/api/, lógica en app/application/, persistencia en app/infrastructure/; la prueba test_corte_vertical.py existe. |
| Arranque documentado con un solo comando | README.md sección 'Arranque rápido': requisito previo Docker Compose y comando 'docker compose up' | Cumple | Un solo comando declarado; no se ejecutó, pero la lectura del README es suficiente para este criterio. |
| Prueba automatizada del recorrido completo, en verde | test/test_corte_vertical.py existe; .github/workflows/ci.yml existe | No verificado | No hay URL de run de GitHub Actions que demuestre la ejecución en verde; el badge del README no es evidencia de ejecución según el contrato. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md filas A-01 a A-09 con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia; rutas enlazadas existen en el árbol | Cumple | Cada celda enlaza a un destino existente; la fila A-06 incluye además la medición ESC-01. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_uniTeam en ISCOUTB, visible:true; shortlog consolidado: Ian Novoa (26), JuanB (10), Julio (10), Daniel (4) | Cumple | Cuatro identidades consolidadas coinciden con los cuatro integrantes declarados; super-gremlin se consolida con Ian Novoa. |
| Estructura mínima | Árbol con docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | La estructura coincide con la mínima del contrato; los .gitkeep son irrelevantes porque hay contenido real. |
| Estado calificado y versionado | hash dc14298, fecha 2026-08-29T11:49:10-05:00, anterior al cierre 2026-08-31T05:00:00Z; commits_tardios_post_cierre vacío | Cumple | No hay tags visibles, pero para evidencia semanal el commit vigente al cierre es el criterio; se anota el hash. |
| Convenciones de ADR | docs/adr/0001 a 0005 con nombres NNNN-kebab-case; ADR-0001 marcado como reemplazado por 0002; ADR-0004 y 0005 con tabla de trazabilidad | Cumple | Los nombres cumplen el patrón; un ADR aceptado no se editó, se marcó reemplazado. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas y filas A-01 a A-09; enlaces a requisitos, C4, ADR, código, pruebas y evidencia | Cumple | Las celdas apuntan a rutas existentes verificadas en el árbol. |
| Registro de uso de IA | docs/ia.md existe con 10 commits de historial entre 2026-08-09 y 2026-08-29 | No verificado | No se pudo comprobar el contenido (para qué, herramienta, aceptado/rechazado); falta leer docs/ia.md. |
| README y reproducibilidad | README.md con arranque rápido, requisitos previos, comando único 'docker compose up', sección de pruebas y API | Cumple | El README es completo y navegable; no se ejecutó el arranque. |
| Pipeline, secretos y autoría | .github/workflows/ci.yml existe; sin .env versionados; grep de secretos solo muestra nombres de parámetros; shortlog con 4 autores | No verificado | Secretos y autoría cumplen, pero no hay evidencia de un run de CI en verde (falta URL); el badge no es evidencia. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `dc14298c32a4fde0956266b0300063c24d7a9486 2026-08-29T11:49:10-05:00 Línea base de ESC-01 medida, y corrección de lo que la tabla prometía de más`
- **Veredicto**: al dia
- Resumen: El proyecto a HEAD (dc14298) cumple 6 de 10 criterios de la ficha y 6 de 8 transversales; los no verificados son por falta de evidencia en el contenido de secciones arc42 y en el run de CI, no por ausencia comprobada.

Pendientes que siguen abiertos:
- Confirmar contenido de secciones 9, 10 y 12 de arc42
- Aportar URL de run de CI en verde
- Verificar contenido de docs/ia.md

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 9: falta leer su contenido para confirmar que cita los ADR.
- arc42 sección 10: falta leer su contenido para confirmar coherencia con escenarios.
- Glosario sección 12: falta leer su contenido para confirmar términos del dominio.
- Prueba en verde: falta URL del run de GitHub Actions.
- docs/ia.md: falta leer su contenido para confirmar lo aceptado/rechazado.
- Pipeline: falta URL de run de CI.

## Hallazgos para la planilla

- La sección 9 de arc42 no muestra en la evidencia la cita a los ADR.
- La sección 10 y el glosario (12) se declaran redactados pero su contenido no se pudo verificar.
- No hay URL de run de CI que demuestre la prueba del corte vertical en verde.
- Los diagramas C4 están como código Mermaid, favorable para la trazabilidad del primer corte.
- Los ADR 0004 y 0005 incluyen trazabilidad con código y pruebas.
- Existe medición de línea base ESC-01 con p95 de 762 ms.
