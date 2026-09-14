# semana-06-evidencia-s6 · DinamikUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `265e652` en `origin/master` (2026-09-13T23:29:49-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/arc42/08-cross-cutting-concepts.md sección 8.1 menciona núcleo compartido, cliente/proveedor y capa anticorrupción | No verificado | El fragmento no muestra el diagrama o tabla de contextos completo |
| Tabla módulo a datos con dueño único por entidad | docs/arc42/08-cross-cutting-concepts.md define el concepto de dueño único de datos | No verificado | No se observa la tabla en el fragmento proporcionado |
| La tabla cubre las entidades que existen en el código | backend/app/estudiantes/models.py y backend/app/requisitos/models.py existen en el árbol | No verificado | Contenido de los modelos no proporcionado para contrastar |
| Violaciones de propiedad de datos detectadas sobre el código actual | No hay lista de violaciones visible en la evidencia proporcionada | No verificado | Se requiere la lista con ubicaciones concretas en el código |
| Plan de corrección por violación | No se encontró plan de corrección en los documentos proporcionados | No verificado | Depende de la lista de violaciones del criterio anterior |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/08-cross-cutting-concepts.md existe y 8.1 contiene lenguaje ubicuo | No verificado | El mapa de contextos no se pudo confirmar en el fragmento |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/ contiene contexto.puml y contenedores.puml; ADRs existentes son 0001-0003 | No verificado | Falta el hash de S5 para comparar y no se observa ADR de reajuste |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md existe en el árbol | No verificado | Contenido no proporcionado para relacionar con los contextos |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible=true, repo=AS_202620_DinamikUTB, rama origin/master; shortlog consolidado muestra 4 integrantes | Cumple | Nombres visibles: Juan José Vargas Pérez, Luis Daniel Padilla Leottau, Gillianis Del Carmen Perez Revolledo, Esteban Ramirez Rios |
| Estructura mínima | Árbol contiene docs/arc42/01-12, docs/adr/0001-0003, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Ruta estándar respetada |
| Estado del repositorio calificado | 265e652 2026-09-13T23:29:49-05:00 es anterior al cierre 2026-09-14T05:00:00Z | Cumple | Sin commits posteriores al cierre |
| Convenciones de ADR | docs/adr/0001-seleccion-monolito-modular.md, 0002-seleccion-tecnologia-backend-frontend.md, 0003-seleccion-motor-de-base-de-datos.md siguen el formato NNNN-titulo-kebab | Cumple | Cada ADR incluye contexto, alternativas, decisión, consecuencias y trazabilidad |
| Tabla de aspectos | docs/aspectos.md existe en el árbol | No verificado | Contenido no proporcionado; no se pudo verificar las 8 columnas ni la navegabilidad |
| Registro de uso de IA | docs/ia.md con 17 commits entre 2026-08-09 y 2026-09-13 | Cumple | El log muestra crecimiento a lo largo del semestre |
| README | README.md describe el sistema, arranque con start.bat y pruebas con pytest/flutter test | Cumple | Incluye requisitos previos y URLs de desarrollo |
| Pipeline y análisis estático | .github/workflows/ci.yml existe pero no hay runs_ci citados | No verificado | Se requiere un run de GitHub Actions o enlace de CI para confirmar ejecución |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `265e652bb3c34c6b90d6d8c1e70db4d75e20a18e 2026-09-13T23:29:49-05:00 Create proguard-rules.pro`
- **Veredicto**: con pendientes
- Resumen: La entrega S6 presenta documentación parcial: la sección 8 de arc42 incluye lenguaje ubicuo, pero el mapa de contextos, la tabla módulo-datos y la lista de violaciones no se pudieron confirmar con la evidencia proporcionada.

Pendientes que siguen abiertos:
- Confirmar mapa de contextos y tabla módulo-datos en 08-cross-cutting-concepts.md
- Verificar violaciones de propiedad de datos y plan de corrección
- Comparar C4 nivel 3 con el hash de S5 y posible ADR de reajuste
- Revisar docs/aspectos.md
- Evidenciar ejecución del pipeline con runs_ci

## Recuento y nota sugerida

0 de 8 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Mapa de contextos completo en 08-cross-cutting-concepts.md
- Tabla módulo a datos con dueño único
- Cobertura de entidades del código
- Lista de violaciones de propiedad de datos
- Plan de corrección por violación
- C4 nivel 3 y ADR de reajuste (falta hash S5)
- Contenido de docs/aspectos.md
- Ejecución del pipeline (runs_ci)

## Hallazgos para la planilla

- La sección 8 de arc42 contiene lenguaje ubicuo con los términos de la semana (núcleo compartido, cliente/proveedor, capa anticorrupción)
- No se pudo confirmar el mapa de contextos ni la tabla módulo-datos por evidencia parcial
- No hay commits posteriores al cierre de S6
- Los 4 integrantes aparecen en el historial con contribuciones repartidas
- No se encontraron secretos en el repositorio
- El pipeline existe pero no hay runs_ci que confirmen ejecución
