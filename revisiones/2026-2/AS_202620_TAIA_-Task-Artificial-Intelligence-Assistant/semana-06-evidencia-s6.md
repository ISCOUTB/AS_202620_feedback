# semana-06-evidencia-s6 · TAIA

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `3950aba` en `origin/main` (2026-09-11T00:51:26-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/arc42/arc42.md en 3950aba; contenido recibido truncado antes de la sección 8; commit head anuncia 'update to arc42 section 8' | No verificado | Se requiere leer la sección 8 o un archivo de contextos para verificar núcleo compartido, cliente-proveedor y capa anticorrupción |
| Tabla módulo a datos con dueño único por entidad | Sin archivo de tabla módulo-datos en el árbol de 3950aba; posiblemente dentro de la sección 8 no inspeccionable | No verificado | Falta la tabla citada y contrastada con el esquema real |
| La tabla cubre las entidades que existen en el código | Entidades visibles en el árbol: Task, Reminder, Notification, Usuario, Conversation; sin la tabla no se puede contrastar | No verificado | No hay migraciones ni .sql en el árbol; persistencia en memoria |
| Violaciones de propiedad de datos detectadas sobre el código actual | No hay lista de violaciones visible en los documentos de 3950aba | No verificado | Se requiere la lista con ubicaciones ruta:línea sobre el código actual |
| Plan de corrección por violación | Sin lista de violaciones visible no hay plan asociado que verificar | No verificado | Falta el plan con acción concreta por cada violación |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/arc42.md existe en 3950aba; commit head 'feat(docs): S6 - update to arc42 section 8'; contenido no inspeccionable | No verificado | Hace falta leer la sección 8 para verificar lenguaje ubicuo y mapa incorporado |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/C4-C3.md existe (diagrama C4Component); único ADR es 0001-estilo-arquitectonico; falta hash de S5 para comparar | No verificado | C4-C3 presente, pero sin el hash de S5 no se puede determinar si hacía falta ADR de reajuste |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md en 3950aba tiene filas A-01 a A-06; sin el mapa de contextos no se puede cruzar | No verificado | Falta el mapa para relacionar cada aspecto con su contexto |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | visible:true; repo AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant en ISCOUTB | Cumple |  |
| Estructura mínima presente | Árbol 3950aba: README.md, docs/arc42/arc42.md, docs/adr/0001-*.md, docs/c4/C4-C1/C2/C3.md, docs/aspectos.md, docs/ia.md | Cumple | arc42 en un solo archivo en lugar de secciones separadas; desviación de estructura, no ausencia |
| Estado calificado identificable | 3950aba624aa00d3185c60d7f44a1835c3680c21 2026-09-11T00:51:26-05:00, anterior al cierre 2026-09-14T05:00:00Z | Cumple |  |
| Nombres de ADR según la convención | docs/adr/0001-estilo-arquitectonico.md cumple el patrón NNNN-titulo-en-kebab-case.md | Cumple |  |
| ADR aceptados no reescritos | Sin git log --follow de docs/adr/0001-*.md en la evidencia recibida | No verificado | Hace falta el historial del ADR para comprobar que no fue reescrito tras aceptarse |
| docs/ia.md al día para la semana | ia_log: 8 commits entre 2026-08-07 (76d4a91) y 2026-09-10 (bf798ad), previos al head; entrada 006 visible | Cumple | El contenido de la última entrada no se inspeccionó; el log muestra crecimiento continuo |
| Sin credenciales en el repositorio ni en el historial | git grep en 3950aba: solo nombres de variables/parámetros (api_key, token, password); envs_versionados: [] | Cumple | Sin .env versionado ni claves privadas en el historial |
| Contribución de todos los integrantes | shortlog 3950aba consolidado: val/valeria-estefania (Valeria), dei0811 (Deiner), luis20072002/Luis Mendoza (Luis), mark (Mark); los 4 con commits | Cumple | Distribución desigual: Valeria 29, Deiner 9, Luis 4, Mark 3 |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `3950aba624aa00d3185c60d7f44a1835c3680c21 2026-09-11T00:51:26-05:00 feat(docs): S6 - update to arc42 section 8, adding C4-3 component diagram for the TAIA API architecture`
- **Veredicto**: con pendientes
- Resumen: Proyecto con backend modular ejecutable (usuario, academic, ai, reminders), pruebas automatizadas y documentación arc42/C4/ADR; la entrega S6 de contextos delimitados y propiedad de datos no pudo verificarse por falta de contenido inspeccionable de la sección 8 de arc42.

Pendientes que siguen abiertos:
- Verificar mapa de contextos con relaciones tipificadas
- Verificar tabla módulo-datos con dueño único
- Verificar lista de violaciones y plan de corrección
- Verificar arc42 sección 8 con lenguaje ubicuo
- Comparar límites contra hash de S5 y posible ADR de reajuste
- Cruzar aspectos con contextos del mapa

## Recuento y nota sugerida

0 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Mapa de contextos con relaciones tipificadas
- Tabla módulo a datos con dueño único por entidad
- La tabla cubre las entidades que existen en el código
- Violaciones de propiedad de datos detectadas sobre el código actual
- Plan de corrección por violación
- arc42 sección 8 con lenguaje ubicuo y mapa de contextos
- C4 nivel 3 y ADR si los límites cambiaron desde el primer corte
- Aspectos relacionables con los contextos del mapa
- ADR aceptados no reescritos (transversal)

## Hallazgos para la planilla

- La documentación de S6 no es inspeccionable: docs/arc42/arc42.md se recibió truncado antes de la sección 8
- El commit head 3950aba anuncia la sección 8 y el C4-C3, pero su contenido no pudo verificarse
- docs/c4/C4-C3.md es un diagrama de componentes, no un mapa de contextos delimitados
- No hay ADR de reajuste de límites; solo existe ADR-0001 de estilo arquitectónico
- No hay migraciones ni esquema SQL en el árbol; la persistencia es en memoria
- Autoría concentrada: Valeria 29 commits frente a 3-9 del resto
