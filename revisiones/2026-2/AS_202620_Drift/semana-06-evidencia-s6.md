# semana-06-evidencia-s6 · Drift

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `5f7fa4c` en `origin/master` (2026-09-13T22:07:49-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/arc42/arc42_8_conceptos_transversales.md §8.2-8.3 (HEAD 5f7fa4c): nombra Búsqueda y comparación, Integración de fuentes externas, Compatibilidad de PC y Experiencia de usuario, pero el diagrama solo muestra flujos, sin tipo de relación. | No cumple | No usa núcleo compartido, cliente-proveedor ni capa anticorrupción; ADR-0003 solo califica a la interfaz como 'cliente'. |
| Tabla módulo a datos con dueño único por entidad | docs/arc42/arc42_8_conceptos_transversales.md §8.4 y docs/adr/0003-reajuste-contextos-dominio.md (sección Propiedad de los datos): tabla Dato→Contexto responsable con un solo dueño por fila. | Cumple | Asigna contextos lógicos, no módulos de código; cada dato tiene un único responsable declarado. |
| La tabla cubre las entidades que existen en el código | Modelos reales backend/app/domain/model/game.py y game_requirements.py; §8.4 cubre Game, GameRequirements, precios de Steam, caché y catálogo de respaldo, y §8.7 declara frontend/domain/model/Game.js como representación. | Cumple | No hay migraciones ni .sql: la persistencia actual es en memoria, coherente con la tabla. |
| No conformidades de propiedad de datos detectadas sobre el código actual | Los documentos aportados (arc42 §8.4, ADR-0003) no listan no conformidades ni rutas de escritura; docs/semana-06-contextos-y-propiedad-de-datos.md existe en el árbol pero su contenido no se incluyó. | No verificado | Haría falta el contenido del documento S6 y el barrido git grep -nIE '(INSERT INTO\|UPDATE \|\.save\(\|\.create\(\|\.update\()' HEAD. |
| Plan de corrección por no conformidad | No se aportó la lista de no conformidades ni las acciones asociadas; ADR-0003 solo describe el reajuste de contextos, no correcciones de escritura sobre entidades. | No verificado | Sin la auditoría visible no se puede comprobar que cada no conformidad tenga acción concreta. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/arc42_8_conceptos_transversales.md §8.1 lenguaje ubicuo, §8.2 contextos delimitados y §8.3 context map, enlazada desde README.md. | Cumple | La sección está completa y navegable; el detalle de tipificación de relaciones es el punto débil. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/adr/0003-reajuste-contextos-dominio.md (Aceptado) y docs/c4/componentes.md incluye ResilientGameRepository, EstimateCompatibility, GameRequirements y GameRequirementsRepository. | Cumple | No se aportó el hash revisado en S5 para el diff; el ADR-0003 deja el commit de implementación pendiente y enlaza a ../adr/0002-arquitectura-base.md, que no existe. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md filas E1-E5 frente al mapa §8.3: E1↔Búsqueda y comparación, E4↔Compatibilidad de PC, E5↔Integración de fuentes externas, E3↔Experiencia de usuario. | Cumple | La relación es inferible pero no explícita; E2 (mantenibilidad) es transversal y no cae en un único contexto. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio público AS_202620_Drift en la organización ISCOUTB; historial consolidado en 4 cuentas (JerryDBM/Sherry, lmpdiaz12, maufern4ndez, JoshuaR01/JoshXX) que cubren los 4 integrantes declarados. | Cumple | Cuentas consolidadas por identidad de correo repetido en los commits, sin atribuir por parecido de nombre. |
| Estructura mínima | Árbol en 5f7fa4c con docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Estructura mínima completa y documentación en Markdown revisable. |
| Convenciones de ADR | docs/adr/0001-adoptar-arquitectura-hexagonal.md, 0002-adoptar-nextjs-fastapi-arquitectura-hexagonal.md y 0003-reajuste-contextos-dominio.md siguen NNNN-kebab-case; ADR-0001 está marcado 'Reemplazado por' con enlace. | Cumple | ADR-0003 tiene enlace roto a un ADR-0002 inexistente y trazabilidad de commit pendiente. |
| La tabla de aspectos | docs/aspectos.md con las ocho columnas (ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia) y filas E1-E5 con enlaces. | Cumple | En E2 la prueba citada (backend/tests/test_health.py) no cubre la sustitución del adaptador; la celda existe pero es débil. |
| Registro de uso de IA | docs/ia.md existe en el árbol y acumula unos 27 commits entre 2026-08-09 y 2026-09-13 (ia_log). | No verificado | No se aportó su contenido, así que no se puede comprobar la columna de lo rechazado y su motivo técnico. |
| README | README.md describe el sistema, los requisitos previos, el comando único python scripts/start.py y cómo se prueba (python -m pytest tests -q, npm run build). | Cumple | Los resultados que declara son validaciones locales; no hay run de CI que los respalde. |
| Pipeline y análisis estático | Existen .github/workflows/ci.yml y sonar-project.properties, pero README.md afirma que el análisis 'se ejecutará en GitHub Actions cuando el equipo realice un push autorizado' y no hay URL de run ni de Quality Gate para 5f7fa4c. | No cumple | Faltan las tres evidencias exigidas (línea del scanner, run exitoso, análisis público con Quality Gate); se esperaba el run y el gate en SonarCloud. Comando: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_Drift/actions/runs?per_page=5. |
| Secretos | Barrido de secretos sobre HEAD 5f7fa4c: '(sin coincidencias)' y envs_versionados vacío. | Cumple | No se encontró .env versionado ni credenciales en el árbol revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `430b9a0cf7c2c9effde4b983e0ca256082f77f1d 2026-09-15T11:27:22-05:00 Revise performance testing details in README`
- **Veredicto**: con pendientes
- Resumen: En la punta de master el proyecto tiene identidad, estructura, ADR, aspectos, arc42 y secretos en orden, y la tabla de propiedad de datos es coherente con las entidades reales. Sin embargo no hay evidencia pública de CI/SonarCloud para el hash revisado y la auditoría de no conformidades del S6 no es verificable, además de correcciones posteriores al cierre.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 2026-09-15T11:04-11:27 -05:00: b2bf164, 56f979b, 66dccb3, 7483132, 579ff78 y 430b9a0 reescriben y renombran el documento S6 y ajustan los enlaces del README después del cierre 2026-09-14T05:00Z.
- 2026-09-15T10:40:25-05:00: 418196c elimina matrices de cumplimiento y secciones de conclusión del paquete S6 tras el cierre.

Pendientes que siguen abiertos:
- Evidencia pública de SonarCloud (run exitoso del scanner y URL del análisis con Quality Gate) para el hash revisado.
- Lista de no conformidades de propiedad con entidad, dueño esperado y ubicación observada, más su plan de corrección.
- Tipificación de las relaciones del mapa de contextos con el vocabulario de la semana.
- Trazabilidad de ADR-0003 (commit de implementación y enlace correcto al ADR de referencia) y de ADR-0001.
- Prueba específica de sustitución del adaptador externo para el escenario E2, hoy citada con una prueba que no la cubre.

## Recuento y nota sugerida

5 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.5 = 1 + 4 × (5/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de docs/semana-06-contextos-y-propiedad-de-datos.md (lista de no conformidades y plan): el archivo está en el árbol pero no se incluyó su contenido.
- Barrido de escrituras sobre el código (git grep -nIE 'INSERT INTO|UPDATE |\.save\(|\.create\(|\.update\(' HEAD -- . ':!docs'): no ejecutable con la evidencia entregada.
- Existencia real de dos módulos escribiendo la misma entidad: no confirmable ni descartable con lo visible.
- Ejecución de CI y Quality Gate de SonarCloud: sin URL de run ni de análisis público; comando anotado en la fila transversal de pipeline.
- Contenido de docs/ia.md y de su columna de uso rechazado.

## Hallazgos para la planilla

- El mapa de contextos (§8.3) nombra los contextos del dominio pero no tipifica las relaciones con el vocabulario de la semana.
- La propiedad de datos está declarada con un único responsable por dato en §8.4 y en ADR-0003.
- No se aportó el documento S6 con la auditoría de no conformidades, por lo que el recorrido no es repetible.
- No hay evidencia pública de CI ni de SonarCloud para el hash revisado; el README remite a un push futuro.
- El paquete de S6 se reorganizó después del cierre (7 commits del 2026-09-15, incluido el renombrado del documento).
- Las entidades del código se limitan a Game y GameRequirements, ambas cubiertas por la tabla de propiedad.
- ADR-0003 deja el commit de implementación pendiente y un enlace a un ADR-0002 que no existe con ese nombre.
- Commits posteriores al cierre (no calificados): 430b9a0 2026-09-15T11:27:22-05:00 Revise performance testing details in README; 579ff78 2026-09-15T11:12:24-05:00 Update link for context and data ownership section; 7483132 2026-09-15T11:10:43-05:00 Add C4 components diagram link to README; 66dccb3 2026-09-15T11:06:31-05:00 Update link text for arc42 section 8 in README; 56f979b 2026-09-15T11:05:25-05:00 Rename Contextos_delimitados_propiedad_datos.md to contextos_delimitados_propiedad_datos.md
