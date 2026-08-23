# Evidencia S1 · uniTeam

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `4b4c5c0e09bc91b9dd930d65cf5ab9a2e4cac1ec` · `2026-08-09T11:22:38-05:00` («Add arc42 files») |
| Cierre de la actividad | `2026-08-10T05:00:00Z` (domingo 9 de agosto, medianoche Colombia) |
| Visibilidad | pública, comprobada con clone y `git ls-remote` sin autenticación (revisiones/2026-2/_meta/lsremote.txt) |

Comandos principales ejecutados: `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only 4b4c5c0`; `git show 4b4c5c0:docs/…`; `git shortlog -sne HEAD`; `git tag --list`.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | clone sin autenticación OK; `lsremote.txt` línea `AS_202620_uniTeam OK` | Cumple | — |
| Integrantes del equipo con acceso | `git shortlog -sne HEAD` al cierre: `super-gremlin <…users.noreply.github.com>` e `Ian Novoa` | No verificado | Sin API (403, sin token) no se listan colaboradores. Qué haría falta: la lista de colaboradores o confirmación del docente. |
| Equipo de 3 o 4 personas | `EQUIPOS.md`: 4 integrantes | Cumple | Julio Cesar Emiliani Ramos · Ian Novoa Carrillo · Juan Jose Bustamante More · Daniel Isaac Manjarres Herrera. |
| Ficha del problema con usuarios y alcance | `docs/ficha.md`: «Usuarios y beneficiarios» y «Alcance del prototipo» | Cumple | Usuarios explícitos y alcance mínimo declarado. |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | ausentes en `docs/ficha.md`, `README.md` y `docs/aspectos.md` | No cumple | No hay sección de tensiones: no se enfrentan dos atributos de calidad en ningún documento del cierre. |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md`: prosa con el aspecto «Gestión colaborativa de tareas», sin tabla de 8 columnas ni ID | No cumple | Un aspecto declarado sí, pero la ficha pide la tabla de ocho columnas con ID y aspecto rellenos. |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md`: herramientas utilizadas (ChatGPT, Claude) y descripción del uso inicial | Cumple | Contenido real, aunque genérico (sin entradas por uso). |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42/arc42-template-EN (1).md` con los 12 encabezados | Cumple | 12 secciones sin rellenar, como se espera. Nombre con « (1)» típico de descarga duplicada; anotado como detalle menor. |
| `docs/adr/` y `docs/c4/` creados | `docs/adr/.gitkeep` y `docs/c4/.gitkeep` | Cumple | — |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clone y ls-remote sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 4b4c5c0`: `README.md`, `docs/arc42/`, `docs/adr/.gitkeep`, `docs/c4/.gitkeep`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Las seis rutas presentes. |
| Estado calificado identificable | sin etiquetas; hash `4b4c5c0e…` + `%cI 2026-08-09T11:22:38-05:00` | Cumple | — |
| Nombres de ADR según la convención | sin ADR en el cierre | Cumple | — |
| ADR aceptados no reescritos | sin ADR en el cierre | Cumple | — |
| `docs/ia.md` al día para la semana | commits el 2026-08-09 (`efa8d03`, `ef63f09`) | No cumple | Hay commits en el periodo, pero el registro no incluye qué se rechazó y por qué (CONTRATO §6): solo herramientas y descripción general. |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'` sin salida | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: 2 identidades (super-gremlin, Ian Novoa) | No verificado | La comprobación de acceso exige la lista de colaboradores (API no disponible). En el historial al cierre solo hay 2 autores; la ficha S1 no lo penaliza si los demás tienen acceso. |

## Recuento de criterios

6 de 9 criterios de la ficha cumplidos (2 No cumplen, 1 No verificado).

## No verificado / pendientes

- Acceso de los 4 integrantes: sin API no se listan colaboradores.
- Atribución de cuentas: `Ian Novoa` se atribuye por el nombre y correo del commit; `super-gremlin` (noreply de GitHub) no se atribuye a ninguna persona. La cuenta `iansx` del listado no firma commits en este periodo; por confirmar.

## Hallazgos para la planilla

- El repositorio se reutilizó de un proyecto anterior: los commits del 09/08 borran artefactos de «InnovaActivos» / «Active Asset Management» (`Delete backend directory`, `Delete innova-activos.v2.sql`, etc.). Quedan en el historial público.
- Integrantes sin aparición en el historial al cierre S1: Julio Cesar Emiliani Ramos (primer commit el 16/08) y, según a quién corresponda `super-gremlin`, Juan Jose Bustamante More o Daniel Isaac Manjarres Herrera.
- Sin entregas tardías relativas a S1 (el siguiente commit tras el cierre es de la entrega S2, 16/08).
