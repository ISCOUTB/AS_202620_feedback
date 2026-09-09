# semana-02-evidencia-s2 · Calificación automática

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `d4302f4` (2026-08-16T23:17:26-05:00) |
| Cierre | 2026-08-17T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | docs/arc42/arc42-template-ES.md incluye 'Requirements Overview' con funcionalidades principales y 'Stakeholders' con expectativas; no hay tabla de objetivos de negocio por interesado. docs/aspectos.md:34 declara RF-01. Sin cita de 'objetivo de negocio'. | No cumple | La sección 1 mezcla funcionalidades con objetivos y carece de un objetivo de negocio explícito por interesado. |
| arc42 sección 2 con restricciones clasificadas y justificadas | docs/arc42/arc42-template-ES.md lista 6 restricciones numeradas con justificación, pero no las clasifica como técnicas, organizativas o legales. | No cumple | Faltan las categorías exigidas (técnicas, organizativas, legales). |
| Restricciones separadas de los requisitos | docs/arc42/arc42-template-ES.md lista restricciones 1-6 como «fijan límites del diseño»; docs/aspectos.md:34 declara RF-01 por separado; sin entremezcla aparente. | Cumple | Las restricciones están en arc42 sección 2 y los requisitos funcionales en docs/aspectos.md. |
| arc42 sección 3 con actores y sistemas externos | docs/arc42/arc42-template-ES.md 'Context and Scope' describe Profesor/TA y Hoja de Respuestas; docs/c4/doc-c4.md 'Nivel 1' enumera Profesor/TA y Sistema de Calificación OMR. | Cumple | Coherente con el C4 de contexto: mismos actores y sistemas. |
| Entre 3 y 5 escenarios de calidad redactados | docs/arc42/arc42-template-ES.md solo presenta 4 Quality Goals; no hay sección 10 con escenarios numerados en docs/arc42/. docs/aspectos.md:36 contiene un único 'Escenario de calidad (borrador)'. | No cumple | No se encontraron 3 a 5 escenarios redactados como tales; solo objetivos de calidad y un borrador. |
| Cada escenario con sus seis partes y medida numérica | El único escenario en docs/aspectos.md tiene tabla de seis partes, pero su medida dice '*Por definir*' (sin cifra ni unidad). | No cumple | Sin medida numérica el escenario cuenta como enunciado. |
| Árbol de utilidad que prioriza por impacto y riesgo | No hay archivo ni tabla de árbol de utilidad en docs/ ni en docs/arc42/arc42-template-ES.md; solo 'Quality Goals' sin priorización impacto/riesgo. | No cumple | No existe el árbol de utilidad exigido. |
| C4 de contexto con leyenda y flechas etiquetadas | docs/c4/doc-c4.md incluye diagrama Mermaid con «Profesor / TA» y «Sistema de Calificación OMR», flecha etiquetada '[HTTPS / Web UI]' y leyenda en la tabla 'Elementos del contexto'. | Cumple | Diagrama como código en docs/c4/doc-c4.md. |
| Escenarios alcanzables desde la fila de su aspecto | docs/aspectos.md tabla A-01: todas las celdas dicen 'Pendiente'; la columna Evidencia está vacía y no hay enlaces desde la fila a ningún escenario. | No cumple | Ninguna fila de aspectos enlaza a un escenario. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima del repositorio | Arbol en HEAD incluye README.md, docs/arc42/arc42-template-ES.md, docs/c4/doc-c4.md, docs/aspectos.md, docs/ia.md y docs/adr/ con archivos. | Cumple | Existe docs/arc42/, docs/adr/, docs/c4/ y los docs raíz requeridos. |
| Todas las entregas se califican sobre el último commit de master/main anterior o igual al cierre | Hash calificado: d4302f4 2026-08-16T23:17:26-05:00 anterior al cierre 2026-08-17T05:00:00Z. | Cumple | Se calificó sobre la rama principal al cierre, con hash citado. |
| Convenciones de ADR | En el estado calificado no existía docs/adr/ (directorio vacío); en HEAD hay 6 ADR con nombres tipo 0001-usar-monolito-modular.md. | No verificado | Falta comprobar en HEAD si los ADR cumplen las convenciones, porque al cierre no había ADR; hacer falta revisar docs/adr/ en HEAD. |
| Tabla de aspectos navegable | docs/aspectos.md tabla A-01 tiene 'Pendiente' en C4, ADR, Código, Pruebas y Evidencia sin enlaces. | No cumple | Una fila con huecos no se puede defender. |
| Registro de uso de IA | docs/ia.md contiene dos entradas con fecha, herramienta, prompt, respuesta, qué se aceptó y qué se rechazó con justificación. | Cumple | El registro crece en el historial (8 commits de docs/ia.md). |
| README con arranque y prueba | README.md en el estado calificado solo describe el proyecto y enlaza docs; no indica cómo arrancar ni cómo probar. | No cumple | Faltan comandos de arranque y prueba; en HEAD hay docker-compose.yml pero el README evaluado no los declara. |
| Pipeline y análisis estático | No hay runs_ci en la evidencia; .github/workflows/ci.yml aparece solo en HEAD, no en el estado calificado. | No verificado | Hacen falta runs de GitHub Actions o equivalente con conclusión y URL. |
| Secretos | Búsqueda de secretos en HEAD sin coincidencias y sin .env versionado. | Cumple | Sin credenciales detectadas en el repositorio. |
| Autoría y colaboración | shortlog HEAD: 36 tcp1109, 16 josueacademico17-source, 7 SusanaRosales, 3 Mariadelmar-restrepo. | Cumple | Cuatro contribuyentes distintos; se consolida por nombre visible de git. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `8b0d00b62d2a03dfe509edae578261748a842294 2026-09-07T14:29:28-05:00 Rename correcciones_feedback.md to correcciones.md`
- **Veredicto**: con pendientes
- Resumen: A HEAD el proyecto creció con ADR, backend, frontend, CI y evidencia de A-01, pero quedan pendientes de la semana 2 sin resolver: escenarios de calidad con medida, árbol de utilidad y tabla de aspectos navegable.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- ADR y estructura docs/adr creados después del cierre (commits 9a80cf0 a 201acac, 2026-08-30 en adelante).
- Pipeline CI agregado tras el cierre (.github/workflows/ci.yml solo en HEAD).
- README actualizado con arranque y prueba tras el cierre (commit 02c39d8 2026-08-30T14:05:57-05:00).
- docs/aspectos.md actualizado con A-04 y retiro de tensión T-2 tras el cierre (commit 9469642 2026-08-30T14:11:19-05:00).
- Código y evidencia del aspecto A-01 agregados después del cierre (59e182e y db99e99, 2026-08-30).

Pendientes que siguen abiertos:
- Escenarios de calidad con medida numérica en arc42 sección 10.
- Árbol de utilidad priorizado por impacto y riesgo.
- Tabla de aspectos navegable hasta código, ADR, pruebas y evidencia.
- Clasificación de restricciones en técnicas, organizativas y legales.

## Recuento y nota sugerida

3 de 9 criterios Cumple.

## No verificado / pendientes

- Convenciones de ADR: al cierre docs/adr estaba vacío; en HEAD hay 6 ADR pero no se pudo verificar contenido por falta de evidencia de commits/árbol en HEAD.
- Pipeline y análisis estático: no hay runs_ci; hace falta un run de GitHub Actions con conclusión y URL.

## Hallazgos para la planilla

- Sección 1 sin objetivos de negocio explícitos por interesado; mezcla funcionalidades.
- Restricciones sin clasificar en técnicas, organizativas y legales.
- No hay 3-5 escenarios de calidad redactados con sus seis partes; solo un borrador con medida 'Por definir'.
- No se encontró árbol de utilidad que priorice por impacto y riesgo.
- Tabla de aspectos con celdas Pendiente sin enlaces navegables.
- README sin instrucciones de arranque ni prueba al cierre.
- Sin evidencia de ejecución de CI (runs_ci vacío).
- Directorio docs/adr vacío al cierre; los ADR aparecen después del cierre.
- Commits posteriores al cierre agregan código, ADR, CI y correcciones de semanas anteriores.
- Commits posteriores al cierre (no calificados): 8b0d00b 2026-09-07T14:29:28-05:00 Rename correcciones_feedback.md to correcciones.md; 201acac 2026-09-06T23:34:17-05:00 Reto del primer corte: registrar la recepcion en una bitacora antes de encolar; cede35e 2026-08-30T23:51:34-05:00 Las secciones 5 y 6 describen el estado real del código; e40ce90 2026-08-30T23:29:07-05:00 docs(arc42): actualizar secciones 5 y 6 con el aspecto A-01 construido; 5f7a2d4 2026-08-30T23:04:23-05:00 Update last updated date to 2026-08-30
