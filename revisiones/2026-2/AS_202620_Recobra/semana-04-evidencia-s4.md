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
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42.md:1-120; docs/arc42/04-estrategia-solucion.md:1-80 | No cumple | Secciones 1-4 redactadas; la 5 es 'Requisitos de calidad' y la 6 'Construcción y despliegue', no bloques de construcción ni vista de ejecución. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42.md (sin sección 9); docs/arc42/ solo contiene 04-estrategia-solucion.md | No cumple | No hay sección 9 de decisiones en ningún archivo de docs/arc42/. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42.md:88-105; docs/escenarios_calidad.md:1-80 | Cumple | Relaciona S1-S7 con decisiones de arquitectura; coherente con los escenarios de la semana 2. |
| Glosario iniciado con términos del dominio | docs/glosarios.md:1-12 | Cumple | Términos propios del dominio: objeto perdido, reclamación, matching, trazabilidad. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/README.md:1-60 | No cumple | Diagramas en Mermaid con leyenda y flechas etiquetadas; el proveedor de autenticación del nivel 1 no aparece en el nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/README.md:35-55 vs árbol del commit (solo node_modules, docs, README, package.json) | No cumple | No hay código para app Flutter, API backend ni PostgreSQL; solo node_modules y documentación. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md:55-75 (rutas citadas) vs árbol del commit sin src/ | No cumple | Las tres rutas están documentadas pero los archivos no existen en el commit calificado. |
| Arranque documentado con un solo comando | README.md:38-42; package.json:8-10 | No cumple | README declara 'npm install && npm start', pero package.json apunta a src/server.js que no está en el árbol. |
| Prueba automatizada del recorrido completo, en verde | README.md:44-48; runs_ci vacío; sin tests/ en el árbol | No cumple | No hay archivos de prueba ni runs de CI en la semana. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md:5-8 | No cumple | La tabla solo tiene Aspecto, Decisión, Justificación y Pruebas; faltan ID, Requisito, C4, ADR, Código y Evidencia. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_Recobra en ISCOUTB, visible; shortlog: Cconde31, vylrir, MiguelJacome, Fernando Isacc Conde Herrera, Steamlinker | Cumple | 4 integrantes identificados tras consolidar Cconde31 y Steamlinker como una misma persona. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md en el árbol | Cumple | node_modules versionado es una desviación relevante. |
| Versionado (estado calificado) | 2268b33 2026-08-30T22:34:56-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin tags; para evidencia semanal el commit vigente al cierre es válido. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md | Cumple | Nombre válido, contexto, alternativas, decisión, consecuencias y referencias. |
| Tabla de aspectos | docs/aspectos.md:5-8 | No cumple | Faltan columnas ID, Requisito, C4, ADR, Código y Evidencia. |
| Registro de uso de IA | docs/ia.md:1-60; log: cb5c579, 632dca4, 2a01e68, 3309ce1 | Cumple | Registra usos, herramientas, aceptado/rechazado y declaraciones de autonomía; persisten entradas 'Ej:'. |
| README y reproducibilidad | README.md:38-48; package.json:8-10; árbol sin src/ | No cumple | El comando documentado no puede ejecutarse porque src/server.js no existe. |
| Pipeline y análisis estático | runs_ci vacío; sin .github/workflows/ en el árbol | No cumple | No hay CI configurado ni runs de la semana. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `2268b33f8acb8e76f0e151808321e21a84a3cde9 2026-08-30T22:34:56-05:00 Update arc42.md`
- **Veredicto**: con pendientes
- Resumen: A HEAD (2268b33) el repositorio contiene documentación (arc42, C4, glosario, aspectos, IA) pero no el código del corte vertical que el README describe: no hay src/ ni tests/. Las secciones 5 y 6 de arc42 están mal numeradas y falta la 9. El C4 dibuja contenedores sin implementación. No hay CI ni pruebas ejecutadas.

Pendientes que siguen abiertos:
- Implementar el corte vertical real (src/domain, src/application, src/infrastructure, tests/).
- Corregir secciones 5 y 6 de arc42 y añadir la sección 9.
- Completar tabla de aspectos con las 8 columnas.
- Alinear C4 con el código real o reducir alcance.
- Configurar CI y ejecutar pruebas en verde.
- Eliminar node_modules del repositorio y rotar el token expuesto.

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución de npm start y npm test: no ejecutadas; el estado se determinó por lectura del árbol (ausencia de src/ y tests/).
- Runs de CI: no disponibles (runs_ci vacío).

## Hallazgos para la planilla

- node_modules versionado en el repositorio.
- Secreto expuesto: repo_token de Coveralls en node_modules/debug/.coveralls.yml:1.
- README documenta src/ y tests/ que no existen en el commit calificado.
- Secciones 5 y 6 de arc42 no corresponden a bloques de construcción ni vista de ejecución.
- Falta la sección 9 de arc42 (decisiones).
- C4 nivel 2 omite el proveedor de autenticación del nivel 1.
- Contenedores C4 (Flutter, PostgreSQL) sin código en el repositorio.
- Sin pipeline de CI ni runs de GitHub Actions.
- docs/ia.md conserva entradas 'Ej:' sin sustituir.
- docs/glosarios.md define corte vertical como /health, incoherente con el README.
