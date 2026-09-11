# semana-06-evidencia-s6 · Drift

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `6d0a1b8` en `origin/master` (2026-09-10T22:21:13-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | No hay archivo de mapa de contextos en el árbol de HEAD 6d0a1b8; docs/c4/contexto.md y docs/c4/contenedores.md son C4 técnico, no contextos delimitados. | No cumple | Falta el artefacto con vocabulario núcleo compartido/cliente-proveedor/capa anticorrupción. |
| Tabla módulo a datos con dueño único por entidad | No se encuentra tabla módulo-datos en el árbol de HEAD 6d0a1b8. | No cumple | Falta el artefacto solicitado. |
| La tabla cubre las entidades que existen en el código | No hay tabla; las entidades reales son backend/app/domain/model/game.py y frontend/domain/model/Game.js. | No cumple | Sin tabla no hay cobertura contrastable con el esquema real. |
| Violaciones de propiedad de datos detectadas sobre el código actual | No hay lista de violaciones en los documentos; el código solo muestra escrituras en backend/app/infrastructure/persistence/in_memory_game_repository.py. | No cumple | Falta el recorrido documentado sobre el código actual. |
| Plan de corrección por violación | No hay lista de violaciones ni plan asociado en HEAD 6d0a1b8. | No cumple | Falta el artefacto. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/ no contiene archivo 08*; las secciones presentes son 1,2,3,4,5,6,9,10,12. | No cumple | Falta la sección 8 con lenguaje ubicuo y mapa de contextos. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | No hay docs/c4/nivel3 ni ADR de reajuste en HEAD; falta el hash de S5 para comparar límites. | No verificado | Se requiere el hash de la revisión S5 y confirmar si los límites cambiaron. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md define E1-E5 sin referencias a contextos delimitados; no hay mapa de contextos. | No cumple | Los aspectos quedan sin contexto. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Drift en ISCOUTB, visible; historial con JerryDBM, lmpdiaz12, JoshuaR01, maufern4ndez y variantes consolidadas. | Cumple | Los 4 integrantes declarados aparecen tras consolidar identidades. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes en HEAD 6d0a1b8. | Cumple | Estructura completa; correciones.md en la raíz es desviación menor. |
| Qué estado del repositorio se califica | Hash calificado 6d0a1b8 (2026-09-10T22:21:13-05:00) anterior al cierre 2026-09-14T05:00:00Z en origin/master. | Cumple | Commit vigente al cierre, modo early. |
| Convenciones de ADR | docs/adr/0001-arquitectura-base.md y 0002-arquitectura-base.md; 0001 marcado como superado por 0002. | No cumple | Títulos temáticos no enuncian la decisión; ADR-0001 deja 'Commit de la decisión: pendiente'. |
| La tabla de aspectos | docs/aspectos.md con tabla de trazabilidad E1-E5. | No cumple | Celdas 'Pendiente' en E3, E4 y E5 son huecos no navegables. |
| Registro de uso de IA | docs/ia.md con log de 23 commits (2026-08-09 a 2026-09-07). | No cumple | No se evidencia columna de lo rechazado con motivo técnico. |
| README | README.md describe el proyecto y su estructura. | No cumple | No incluye arranque con un solo comando ni cómo probar; scripts/start.py no está referenciado. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe; ADR-0002 lo menciona. | No verificado | Sin runs de CI citados ni evidencia de SonarCloud; no se pudo verificar ejecución. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `6d0a1b88b48ae1da248f77a09bcd5c52d4e95ff1 2026-09-10T22:21:13-05:00 Fix links in correciones.md to GitHub URLs`
- **Veredicto**: con pendientes
- Resumen: La entrega S6 carece de los artefactos de contextos delimitados y propiedad de datos; la documentación base del proyecto está presente pero con huecos de trazabilidad y sin evidencia de ejecución de CI.

Pendientes que siguen abiertos:
- Mapa de contextos con relaciones tipificadas
- Tabla módulo-datos con dueño único
- Lista de violaciones con plan de corrección
- Sección 8 de arc42
- C4 nivel 3 y ADR si aplica
- Trazabilidad completa en aspectos.md
- Registro de rechazos en ia.md
- Instrucciones de arranque y prueba en README
- Evidencia de ejecución de CI

## Recuento y nota sugerida

0 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- C4 nivel 3 y ADR si los límites cambiaron desde el primer corte (falta hash de S5 para comparar).
- Pipeline y análisis estático (sin runs de CI citados).

## Hallazgos para la planilla

- No hay mapa de contextos delimitados en la entrega S6.
- No hay tabla módulo-datos con dueño único por entidad.
- No hay lista de violaciones de propiedad de datos ni plan de corrección.
- Falta la sección 8 de arc42 (lenguaje ubicuo y mapa de contextos).
- No hay C4 nivel 3 ni ADR de reajuste de límites.
- docs/aspectos.md tiene celdas 'Pendiente' que rompen la trazabilidad.
- docs/ia.md no documenta lo rechazado con motivo técnico.
- README.md no explica cómo arrancar ni probar el sistema.
- Los títulos de los ADR son temáticos y no enuncian la decisión.
- Sin evidencia de ejecución de CI ni análisis estático.
