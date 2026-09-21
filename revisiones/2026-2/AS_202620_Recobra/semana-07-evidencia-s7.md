# semana-07-evidencia-s7 · Recobra

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `8f25313` en `origin/master` (2026-09-19T13:37:58-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/contracts/openapi.yaml:1 `openapi: 3.0.3`, presente en el árbol de 8f25313 (2026-09-19T13:37:58-05:00). | Cumple | Es especificación OpenAPI 3.0.3, no prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/contracts/openapi.yaml: paths /publicaciones y /publicaciones/{id} con requestBody y components.schemas (Publicacion, CrearPublicacionRequest, Salud, ErrorDominio, ErrorInterno con `required` y `properties`). | Cumple | Los esquemas de respuesta están definidos; no hay ejemplos de payload. |
| Correspondencia entre el contrato y la API implementada | docs/contracts/evidencia-fallo-2026-09-19.txt muestra ejecución real de POST /publicaciones (201/400) y GET /publicaciones/:id (200/404); README.md documenta esos mismos endpoints y arc42 §6 los mapea a PublicacionesController y ConsultarPublicacion. | Cumple | No se aportó el contenido de los controladores; la correspondencia se apoya en el log e2e y en la documentación. |
| Versión de la API declarada y con historial | docs/contracts/openapi.yaml declara `version: "1.0.0"`, pero no se aporta el `git log` del archivo. | No verificado | Falta `git log --format='%h %cI %s' -- docs/contracts/openapi.yaml` para ver la evolución de la versión. |
| Prueba de contrato presente | test/contract.e2e-spec.ts y test/jest-e2e.json en el árbol de 8f25313; el log aportado lista 5 casos (health, 201, 400, 404 y 200). | Cumple | La prueba valida respuestas contra la especificación con el matcher del contrato. |
| El pipeline ejecuta la prueba de contrato | No se aportó el contenido de .github/workflows/ci.yml ni runs_ci; ADR-0004 menciona un paso «Contract tests» y un run en rojo (35411238008) que no se pudo contrastar. | No verificado | Hace falta `grep -n contract .github/workflows/ci.yml` y la URL, nombre y conclusión del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/contracts/evidencia-fallo-2026-09-19.txt: FAIL 2 de 5 casos por faltar la propiedad requerida 'matchScore' del esquema Publicacion; ADR-0004 cita el run en rojo 35411238008 y su reversión posterior. | Cumple | La evidencia es un log versionado; sin runs_ci no se pudo verificar la conclusión del run citado. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0004-integracion-sincrona-vs-asincrona.md: alternativas A (todo síncrono) y B (todo asíncrono) descartadas, decisión híbrida y consecuencias frente a S3, S4/S4a y S5. | Cumple | Justifica la alternativa descartada y el acoplamiento temporal asumido. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42.md §6 «Vista de ejecución» con el flujo crear publicación (5 pasos) y el flujo consultar; commit c7bf54c 2026-09-19 agrega el flujo de interacción. | Cumple | Los flujos referencian el contrato y el cliente Flutter. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4-C2.md: cada flecha etiquetada («HTTP/JSON», «UI local, sin red», «in-process, mismo proceso, sin red», «API/HTTPS · JSON» para las planeadas); commit 667d66f 2026-09-19 limpia formato del diagrama. | Cumple | Las relaciones aún no cableadas están marcadas como planeadas, con protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio público AS_202620_Recobra en la organización ISCOUTB, rama origin/master, hash 8f25313; historial con 5 cuentas (Cconde31, vylrir, Fernando Isacc Conde Herrera, MiguelJacome, Steamlinker). | Cumple | Hay 5 cuentas frente a 4 integrantes declarados; no se consolida identidad ni se atribuye por parecido de nombre. |
| Estructura mínima | En el árbol de 8f25313 están docs/arc42/arc42.md, docs/adr/0001..0004, docs/c4/C4-C1..C3, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Rutas mínimas completas; docs/calidad y docs/contracts son adicionales. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md, 0002-arquitectura-y-stack.md, 0003-reto-corte1-stack-obligatorio.md y 0004-integracion-sincrona-vs-asincrona.md con numeración kebab-case, contexto, opciones, decisión y consecuencias; ADR-0001 marcada «Reemplazada por ADR-0002». | Cumple | El ADR reemplazado se conserva y enlaza al que lo sustituye. |
| La tabla de aspectos | docs/aspectos.md con las 8 columnas (ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia) y filas A1–A4 con enlaces navegables. | Cumple | La fila A3 declara celdas «pendiente/planeado» sin artefacto: hueco declarado, no oculto. |
| Registro de uso de IA | docs/ia.md existe y acumula 9 commits (2026-08-23 a 2026-09-19, último 8f25313), pero no se aportó su contenido. | No verificado | No se puede comprobar la columna de lo rechazado y su motivo; haría falta el archivo. |
| README | README.md describe el sistema, el arranque con un solo comando (`npm install && npm run start`), las pruebas (`npm test`, `npm run test:e2e`, `flutter test`) y los requisitos (Node 18+, Flutter). | Cumple | Incluye endpoints de ejemplo y estructura del repositorio. |
| Pipeline y análisis estático | Existen sonar-project.properties y .github/workflows/ci.yml en el árbol, pero no se aportó su contenido, ni runs_ci, ni URL pública del análisis con Quality Gate; el commit 3d9da06 (2026-09-19) solo declara «ya corre y está en verde». | No verificado | Sin run del scanner y sin URL de SonarCloud el análisis no es auditable. |
| Secretos | La búsqueda de patrones de credenciales sobre HEAD no arroja coincidencias y no hay .env versionado (sí .env.example). | Cumple | docs/checklist-entrega-manual.md §2 menciona un token de Coveralls que estuvo versionado dentro de node_modules; conviene confirmar su rotación. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8f25313349ed23aafb246ffa146a0c63d3d1baa3 2026-09-19T13:37:58-05:00 Registrar en ia.md el uso de IA de esta semana (S6/S7)`
- **Veredicto**: con pendientes
- Resumen: En HEAD de origin/master (8f25313, 2026-09-19T13:37:58-05:00, anterior al cierre 2026-09-21T05:00Z) el equipo cumple 8 de 10 criterios de la ficha y 6 de 8 transversales: contrato OpenAPI 3.0.3 con esquemas, prueba de contrato con evidencia de fallo, ADR-0004, arc42 §6, C4 nivel 2, estructura, ADR, aspectos, README y secretos sin hallazgos en HEAD. Quedan sin verificar la ejecución del pipeline y el análisis SonarCloud (no hay runs_ci, solo la mención en ADR-0004 y un mensaje de commit), el historial del contrato y el contenido del registro de IA, por lo que no se puede certificar el cumplimiento pleno ni marcar al_dia.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 8f25313 2026-09-19T13:37:58-05:00 «Registrar en ia.md el uso de IA de esta semana (S6/S7)»: cierra la falta de registro de IA (contenido no aportado para verificar).
- 3d9da06 2026-09-19T13:37:14-05:00 «Corregir hallazgo de SonarCloud: ya corre y esta en verde (GitHub App)»: corrige un hallazgo transversal anterior solo de forma declarativa, sin run ni URL pública.
- 573e512 2026-09-19T13:04:46-05:00 «Agregar secciones 8 y 11 de arc42»: completa documentación de semanas anteriores al final de la ventana.
- c7bf54c 2026-09-19T11:26:41-05:00 «Agregar flujo de interaccion a seccion 6 y nueva seccion 7 de arc42»: cubre el recordatorio de documentación de S7 sobre la marcha.
- 667d66f 2026-09-19T13:33:47-05:00 «Limpiar formato de las secciones 6-12 de arc42 y del diagrama C4-C2»: ajuste de entregables previos.
- No hay commits posteriores al cierre de S7 (commits_tardios_post_cierre vacío).

Pendientes que siguen abiertos:
- Añadir la evidencia verificable de CI: contenido de .github/workflows/ci.yml con el paso de contrato y enlaces de los runs (verde y rojo).
- Publicar la URL del análisis de SonarCloud con el estado del Quality Gate para el hash revisado.
- Aportar el historial git de docs/contracts/openapi.yaml para respaldar la versión declarada.
- Aportar el contenido de docs/ia.md con lo rechazado y su motivo por cada uso.
- Consolidar las cuentas del historial con los integrantes declarados y confirmar la rotación del token de Coveralls mencionado en el checklist.

## Recuento y nota sugerida

8 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución de la prueba de contrato en el pipeline: falta el contenido de .github/workflows/ci.yml y runs_ci; se buscó en el árbol de 8f25313 y en el ADR-0004 y solo aparece la mención textual al paso «Contract tests». Haría falta `grep -n contract .github/workflows/ci.yml` y la URL, nombre y conclusión del run.
- Análisis SonarCloud auditable: existen sonar-project.properties y ci.yml pero sin su contenido, sin run del scanner y sin URL pública del análisis con Quality Gate para el hash 8f25313. Haría falta la URL de SonarCloud y el run asociado.
- Historial del contrato: no se aportó `git log --format='%h %cI %s' -- docs/contracts/openapi.yaml`, necesario para ver la evolución de la versión.
- Contenido de docs/ia.md: solo se aportan fechas de commit, no la tabla de usos con lo rechazado y su motivo.
- Pertenencia de las cuentas a la organización y su correspondencia con los 4 integrantes declarados: no verificable con la evidencia aportada; se requiere el listado de miembros del repositorio.

## Hallazgos para la planilla

- El contrato es OpenAPI 3.0.3 ejecutable con rutas y esquemas, versionado en docs/contracts/openapi.yaml.
- La prueba de contrato existe (test/contract.e2e-spec.ts) y hay evidencia versionada de que falla ante un cambio incompatible.
- ADR-0004 justifica la estrategia híbrida con las alternativas descartadas y su escenario de calidad.
- arc42 §6 y C4 nivel 2 cumplen: flujos descritos y cada flecha con protocolo y formato.
- No se pudo verificar que el workflow ejecute la prueba de contrato: falta el contenido de ci.yml y los runs_ci.
- SonarCloud no es auditable: solo se declara en un mensaje de commit, sin run del scanner ni URL pública con Quality Gate.
- No se aportó el historial git del contrato, por lo que la versión 1.0.0 no se puede contrastar con su evolución.
- El registro de IA no se aportó en contenido, solo su historial de commits.
- Las correcciones de hallazgos anteriores (SonarCloud, arc42 §6-12, formato de C4-C2) aterrizaron el 2026-09-19, al final de la ventana.
- No hubo commits posteriores al cierre de S7 en origin/master.
- El historial muestra 5 cuentas frente a 4 integrantes declarados, sin consolidación de identidad.
- docs/aspectos.md fila A3 mantiene celdas pendientes/planeadas sin artefacto navegable.
