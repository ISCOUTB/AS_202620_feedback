# semana-06-evidencia-s6 · uniTeam

> Revisión directa manual, sin ejecutar código del equipo.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `6cc8e6f` en `origin/master` (2026-09-13T20:20:18-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | revisión directa estática |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | `docs/calidad/mapa-contextos.md` define Identidad, Proyectos, Tareas, Notificaciones y Auditoría; su diagrama y tabla distinguen Customer/Supplier y Published Language. | Cumple | Las relaciones citan mecanismo y justificación, incluido que no hay shared kernel ni ACL por ahora. |
| Tabla módulo a datos con dueño único por entidad | `docs/calidad/propiedad-datos.md` enumera Usuario, Proyecto, Tarea, Auditoría y Notificación con un único escritor. | Cumple | La tabla declara dueño y mecanismo de lectura para cada consumidor. |
| La tabla cubre las entidades que existen en el código | La misma tabla dice explícitamente que es una primera pasada y que debe completarse contra el esquema real de MySQL y los modelos FastAPI. | No cumple | Se esperaba la verificación entidad por entidad contra `app/domain/modelos.py` y persistencia; el documento declara que no la realizó. |
| No conformidades de propiedad de datos detectadas sobre el código actual | La sección “Violaciones detectadas” conserva tres filas con `*(revisar)*`, rutas `app/...` y preguntas de auditoría. | No cumple | Se esperaba entidad, módulo dueño y ubicación real; se revisó `docs/calidad/propiedad-datos.md` en `6cc8e6f` y solo hay plantilla de investigación. |
| Plan de corrección por no conformidad | Cada fila provisional propone una acción genérica, pero no queda asociada a una no conformidad comprobada. | No cumple | Sin hallazgo concreto no es posible verificar que el plan corrija el cruce de propiedad correspondiente. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | `docs/arc42/arc42-uniteam.md` marca la sección 8 como “Pendiente”, aunque el mapa vive en `docs/calidad/`. | No cumple | Se esperaba incorporar el lenguaje ubicuo y mapa a arc42 §8; la ausencia está declarada por el propio documento. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | Hay C4 niveles 1 y 2 y ADR-0003 sobre eventos, pero no se encontró C4 nivel 3 ni ADR que contraste el reajuste S6 con S5. | No cumple | Se revisaron `docs/c4/` y `docs/adr/` del hash calificado; falta la evidencia solicitada si los límites se reajustaron. |
| Aspectos relacionables con los contextos del mapa | `docs/aspectos.md` tiene la cadena de ocho columnas, pero sus filas enlazan C4, ADR, código y pruebas sin identificar los contextos de `mapa-contextos.md`. | No cumple | Se esperaba poder relacionar cada contexto con las filas de aspectos; esa relación no está declarada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | `AS_202620_uniTeam` es público en la organización ISCOUTB. | Cumple | Repositorio visible. |
| Estructura mínima | Árbol de `6cc8e6f`: `README.md`, `docs/adr/`, `docs/arc42/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Estructura presente. |
| Qué estado del repositorio se califica | `origin/master`, hash `6cc8e6f`, anterior al cierre. | Cumple | No se usaron etiquetas. |
| Convenciones de ADR | `docs/adr/0001-...` a `0005-...` siguen NNNN-kebab-case. | Cumple | La nomenclatura es verificable en el árbol. |
| La tabla de aspectos | `docs/aspectos.md` contiene ID, aspecto, requisito, C4, ADR, código, pruebas y evidencia. | Cumple | Falta aún enlazar explícitamente los contextos de S6. |
| Registro de uso de IA | No se encontró `docs/ia.md` en el árbol calificado. | No cumple | Se esperaba registro con aceptado, rechazado y motivo; no está disponible en la ruta exigida. |
| README | El arranque no se verificó en esta revisión estática. | No verificado | Habría que aportar el comando de arranque y un run citable; no se ejecuta código de estudiantes. |
| Pipeline y análisis estático | `.github/workflows/ci.yml` ejecuta pruebas y compilación, pero no invoca scanner ni enlaza análisis público SonarCloud con Quality Gate. | No cumple | Se esperaba scanner, run exitoso y URL pública de Quality Gate; en el workflow solo aparecen pruebas, frontend y cierre de dependencias. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `6cc8e6fda038b43ec221e5d796dbfaafa195c15e`.
- **Veredicto**: con pendientes.
- Resumen: el mapa y la declaración inicial de dueño único son útiles, pero la auditoría aún no contrasta el código y arc42 §8 permanece pendiente.

Pendientes que siguen abiertos:

- Completar la cobertura de entidad contra el esquema y los modelos reales.
- Sustituir la plantilla de violaciones por no conformidades reproducibles con ruta, línea y corrección asociada.
- Integrar mapa y lenguaje ubicuo en arc42 §8, y enlazar contextos desde aspectos.
- Publicar evidencia auditable de SonarCloud con su Quality Gate.

## Recuento y nota sugerida

2 de 8 criterios Cumple.

**Nota sugerida (propuesta al docente): 2.0 = 1 + 4 × (2/8).** La nota final la fija el profesor en Moodle.

## Hallazgos para la planilla

- La tabla de propiedad de datos declara que aún no fue contrastada contra el esquema y los modelos reales.
- Las tres no conformidades S6 son marcadores de investigación, no hallazgos de código citables.
- arc42 §8 está pendiente y el workflow no contiene SonarCloud ni Quality Gate públicos.
