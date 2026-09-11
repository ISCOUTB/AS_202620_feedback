# semana-06-evidencia-s6 · LaPlacita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `50b92f8` en `origin/master` (2026-09-06T17:45:05-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/arc42/arc42-template-EN.md (contenido truncado), docs/c4/contexto.md, docs/c4/contenedores.md | No verificado | No se pudo comprobar la sección 8 del arc42; el C4 disponible es técnico y no usa vocabulario DDD. |
| Tabla módulo a datos con dueño único por entidad | Árbol sin migraciones/modelos; src/modules/*/index.js | No verificado | No hay tabla visible en el árbol; podría estar en arc42, pero no se pudo verificar. |
| La tabla cubre las entidades que existen en el código | src/modules/{catalogo,pedidos,pagos,entrega,notificaciones}/index.js | No verificado | Depende de la tabla del criterio anterior; sin ella no se puede contrastar. |
| Violaciones de propiedad de datos detectadas sobre el código actual | docs/adr/0004-aislamiento-por-establecimiento.md | No cumple | El ADR-0004 documenta accesos cruzados entre tiendas, no violaciones de propiedad de datos entre módulos. |
| Plan de corrección por violación | docs/adr/0004-aislamiento-por-establecimiento.md | No cumple | El plan del ADR-0004 es para aislamiento por tienda, no para propiedad de datos. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/arc42-template-EN.md | No verificado | Contenido truncado en la evidencia; no se pudo acceder a la sección 8. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/ solo contexto.md y contenedores.md; docs/adr/0004 | No cumple | No existe docs/c4/componentes.md (nivel 3); el ADR-0004 existe pero sin C4 nivel 3. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md | No verificado | Sin mapa de contextos no se pueden relacionar los aspectos con contextos delimitados. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_LaPlacita en ISCOUTB, visible; autores: Jorge M. Castillo, samulssl, Isaza927, matbuendia | Cumple | Los 4 integrantes declarados aparecen en el historial. |
| Estructura mínima | docs/arc42/, docs/adr/0001-0004, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | La plantilla arc42 está en inglés, pero la estructura existe. |
| Estado del repositorio calificado | hash 50b92f8 (2026-09-06T17:45:05-05:00) anterior al cierre 2026-09-14T05:00:00Z | Cumple | Sin commits posteriores al cierre. |
| Convenciones de ADR | docs/adr/0001-0004 con numeración, títulos kebab-case, contexto, alternativas, decisión, consecuencias, trazabilidad | Cumple | ADR-0002 es ratificación, no reemplaza. |
| Tabla de aspectos | docs/aspectos.md con columnas ID, Aspecto, Requisito, Escenarios, C4, ADR, Código, Pruebas, Evidencia | Cumple | Enlaces navegables a código y pruebas. |
| Registro de uso de IA | docs/ia.md existe con 15 commits; fragmento no muestra columna de rechazo | No verificado | Se necesita revisar el archivo completo para verificar lo rechazado y por qué. |
| README | README.md con descripción, estructura, cómo ejecutar, pruebas | Cumple | Incluye guía paso a paso. |
| Pipeline y análisis estático | .github/workflows/ci.yml; runs_ci con éxito; ADR-0003 dice SONAR_TOKEN pendiente | No cumple | SonarCloud no está activo por falta de token. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `50b92f8558f2f57d01aeee14dfe202c9e076e74f 2026-09-06T17:45:05-05:00 fix(ci): gata el análisis SonarCloud con env en vez de secrets`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene una base sólida de CI, ADR y aspectos, pero la entrega de la semana 6 no incluye los artefactos clave de contextos delimitados y propiedad de datos.

Pendientes que siguen abiertos:
- Configurar SONAR_TOKEN para activar SonarCloud
- Crear C4 nivel 3 (componentes)
- Documentar mapa de contextos con relaciones tipificadas
- Crear tabla módulo a datos con dueño único
- Completar sección 8 de arc42 con lenguaje ubicuo

## Recuento y nota sugerida

0 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de docs/arc42/arc42-template-EN.md secciones 5-12 (incluida la 8).
- Columna de rechazo en docs/ia.md.
- Ejecución real del job de SonarCloud en los runs de CI.

## Hallazgos para la planilla

- No hay mapa de contextos con relaciones tipificadas (núcleo compartido, cliente-proveedor, capa anticorrupción).
- No hay tabla módulo a datos con dueño único por entidad.
- No hay C4 nivel 3 (docs/c4/componentes.md ausente).
- SonarCloud no está activo: falta configurar SONAR_TOKEN.
- El ADR-0004 documenta una violación de aislamiento corregida, pero no una auditoría de propiedad de datos.
- La sección 8 del arc42 no se pudo verificar por contenido truncado.
