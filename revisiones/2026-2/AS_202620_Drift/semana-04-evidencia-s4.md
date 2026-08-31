# semana-04-evidencia-s4 · Drift

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `4254f4a` (2026-08-30T19:13:01-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42_1_introduccion_objetivos.md a arc42_6_Vista_Ejecucion.md en 4254f4a; secciones redactadas con contenido propio, sin marcadores de plantilla | Cumple | Sección 5 descompone en bloques con responsabilidades; sección 6 describe 3 escenarios con diagramas e interpretación. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/arc42_9_Decisiones_Arquitectonicas.md enlaza a docs/adr/0001-arquitectura-base.md y 0002-arquitectura-base.md | Cumple | Índice y resumen sin duplicar el contenido de los ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42_10_Requisitos_Calidad.md tabla QS-01..QS-05; docs/escenarios.md E1-E5 | Cumple | QS-01..QS-05 corresponden a E1-E5 con mismas medidas. |
| Glosario iniciado con términos del dominio | docs/arc42/arc42_12_Glosario.md con términos DRIFT, Tienda digital, Sub-adaptador, Núcleo de dominio | Cumple | Excluye términos genéricos; incluye dominio propio. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.md y docs/c4/contenedores.md (Mermaid) en 4254f4a | Cumple | Actores del nivel 1 (Jugador, Administrador, Tiendas, Proveedor) reaparecen en nivel 2; flechas etiquetadas y leyenda. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Contenedor Persistencia ↔ backend/app/infrastructure/persistence/in_memory_game_repository.py; Dominio ↔ backend/app/domain/; Aplicación ↔ backend/app/application/usecases/search_games.py | Cumple | Adaptadores de fuentes externas solo tienen directorios con .md, sin implementación. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | backend/app/main.py (interfaz), backend/app/application/usecases/search_games.py (lógica), backend/app/infrastructure/persistence/in_memory_game_repository.py (persistencia) | Cumple | Commit ff339e9 implementa el corte vertical de búsqueda. |
| Arranque documentado con un solo comando | README.md en 4254f4a no muestra en el fragmento revisado una sección de requisitos previos ni comando de arranque | No verificado | El fragmento del README está truncado; se necesita inspeccionar el archivo completo para localizar el comando. |
| Prueba automatizada del recorrido completo, en verde | Solo existe backend/tests/test_health.py; no hay prueba que ejercite search_games + in_memory_game_repository; sin URL de run | No cumple | El health check no cubre el recorrido completo; falta evidencia de pipeline en verde. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tiene tabla de escenarios (ID, Aspecto, Fuente, Estímulo, Artefacto, Entorno, Respuesta, Medida) sin columnas Requisito, C4, ADR, Código, Pruebas | No cumple | No hay fila de trazabilidad con las 8 columnas del contrato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad y estructura | Repo AS_202620_Drift en ISCOUTB visible; estructura docs/arc42, adr, c4, aspectos.md, ia.md, README.md presente | Cumple | 4 integrantes consolidados en el historial. |
| Versionado | Commit 4254f4a 2026-08-30T19:13:01-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Evidencia semanal calificada en el último commit antes del cierre. |
| Convenciones de ADR | docs/adr/0001-arquitectura-base.md y 0002-arquitectura-base.md; 0001 no marca reemplazo por 0002; sin trazabilidad a commits/pruebas | No cumple | Nombres correctos, pero falta marcado de reemplazado y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md sin tabla ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia | No cumple | La tabla existente es de escenarios, no de trazabilidad. |
| Registro de uso de IA | docs/ia.md con registros de herramienta, prompt y uso; sin columna de lo rechazado y por qué | No cumple | Falta documentar lo rechazado con motivo técnico. |
| README y reproducibilidad | README.md en 4254f4a; fragmento no incluye sección de arranque | No verificado | Se requiere inspección completa del README. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe; sin URL de run en la evidencia | No verificado | Falta run de GitHub Actions que muestre el verde. |
| Secretos y autoría | Sin coincidencias de secretos; sin .env versionado; shortlog muestra 4 autores consolidados | Cumple | Identidades consolidadas: JerryDBM/Sherry, JoshuaR01/JoshXX. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `4254f4aa4f0d24dcaaaa3497af02b09bca830ee5 2026-08-30T19:13:01-05:00 Fix formatting in README.md`
- **Veredicto**: con pendientes
- Resumen: La semana 4 entrega arc42 1-6, 9, 10 y 12 redactados, C4 niveles 1 y 2 coherentes, y un corte vertical que atraviesa interfaz, lógica y persistencia. Quedan pendientes: prueba del recorrido completo, tabla de trazabilidad en aspectos, ADR con trazabilidad y marcado de reemplazo, README con arranque y evidencia de pipeline.

Pendientes que siguen abiertos:
- Prueba automatizada del recorrido completo
- Tabla de trazabilidad en docs/aspectos.md
- ADR con trazabilidad y marcado de reemplazo
- README con requisitos previos y comando de arranque
- Evidencia de run de CI en verde

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Arranque documentado en README (fragmento truncado).
- Pipeline en verde (sin URL de run).

## Hallazgos para la planilla

- La prueba test_health.py no ejercita el recorrido completo del corte vertical.
- docs/aspectos.md no tiene la tabla de trazabilidad con columnas Requisito, C4, ADR, Código, Pruebas.
- ADR-0001 no está marcado como reemplazado por ADR-0002 dentro del archivo.
- Los ADR carecen de trazabilidad a commits y pruebas.
- docs/ia.md no documenta lo rechazado y por qué.
- README no muestra sección de arranque con un solo comando en el fragmento revisado.
- No hay evidencia de run de CI con URL.
- Los adaptadores de fuentes externas (steam, xbox, playstation) solo tienen archivos .md, sin implementación.
