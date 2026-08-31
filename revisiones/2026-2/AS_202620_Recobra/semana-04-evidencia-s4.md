# semana-04-evidencia-s4 · Recobra

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `2268b33` (2026-08-30T22:34:56-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42.md contiene secciones 1-6 pero la 5 es 'Requisitos de calidad' y la 6 'Construcción y despliegue', no bloques de construcción ni vista de ejecución | No cumple | Las secciones 5 y 6 no corresponden a lo exigido en la ficha |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se encuentra sección 9 en docs/arc42.md | No cumple | Falta la sección 9 de decisiones de arquitectura |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42.md incluye '## Sección 10 — Relación entre escenarios y decisiones de arquitectura' con lista S1-S7 | Cumple | Coherente con escenarios_calidad.md |
| Glosario iniciado con términos del dominio | Existe docs/glosarios.md pero no se pudo comprobar su contenido | No verificado | Haría falta ver el archivo para confirmar términos propios del sistema |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo se ve docs/c4/README.md en el árbol, sin contenido | No verificado | No se pudo comprobar presencia ni coherencia de diagramas |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin contenido de C4 no se puede contrastar con estructura de código | No verificado | Haría falta ver los diagramas y comparar con src/ |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md describe corte vertical con rutas: domain/entities/publicacion.js, application/use-cases/crear-publicacion.js, infrastructure/adapters/persistence/memoria-publicacion-repository.js, infrastructure/adapters/http/server.js | Cumple | Las tres capas están citadas |
| Arranque documentado con un solo comando | README.md sección 'Cómo levantar el esqueleto' con requisitos Node.js 18 y comando 'npm install && npm start' | Cumple | Comando único en una línea |
| Prueba automatizada del recorrido completo, en verde | README.md menciona 'npm test' con pass 7 fail 0, pero no hay URL de run de CI | No verificado | Haría falta evidencia de ejecución en pipeline |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | Existe docs/aspectos.md pero no se pudo comprobar contenido de filas | No verificado | Haría falta ver la tabla y verificar cada celda |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Recobra visible, autores: Cconde31, vylrir, MiguelJacome, Fernando Isacc Conde Herrera, Steamlinker; consolidando identidades aparecen los 4 integrantes | Cumple | Camilo Conde aparece con dos cuentas (Cconde31 y Steamlinker) |
| Estructura mínima | Árbol muestra docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura presente, aunque arc42 está en archivo único y directorio |
| Estado calificado | Commit 2268b33 con fecha 2026-08-30T22:34:56-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta requerida para evidencia semanal |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md no incluye trazabilidad con commit/PR/pruebas | No cumple | Falta sección de trazabilidad explícita |
| Tabla de aspectos | Existe docs/aspectos.md pero sin contenido visible | No verificado | No se pudo comprobar columnas ni filas |
| Registro de uso de IA | docs/ia.md existe con commits, pero sin contenido | No verificado | No se pudo verificar qué se aceptó/rechazó |
| README | README.md incluye qué es, arranque con un comando y pruebas | Cumple | Cumple requisitos |
| Pipeline y análisis estático | No se encontró .github/workflows/ en el árbol | No cumple | Sin CI configurada |

## Recuento y nota sugerida

3 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.2 = 1 + 4 × (3/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de docs/glosarios.md
- Diagramas C4 en docs/c4/README.md
- Correspondencia C4-código
- Ejecución de pruebas en CI
- Fila de aspectos completa
- Contenido de docs/ia.md
- Contenido de docs/aspectos.md

## Hallazgos para la planilla

- Secciones 5 y 6 de arc42 no corresponden a bloques de construcción y vista de ejecución
- No hay sección 9 en arc42
- No se encontró pipeline de CI
- ADR-0001 sin trazabilidad completa
- node_modules versionado en el repositorio
- Secreto en node_modules/debug/.coveralls.yml (repo_token)
