# Evidencia S1 · XALD

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `bf81545166e3468ab33530ec5b5f69be8a370fc8` · `2026-08-08T13:39:21-05:00` («Add AI usage log for Proyecto XALD») |
| Cierre de la actividad | `2026-08-10T05:00:00Z` (domingo 9 de agosto, medianoche Colombia) |
| Visibilidad | pública, comprobada con clone y `git ls-remote` sin autenticación (revisiones/2026-2/_meta/lsremote.txt). Antes figuraba como no visible (EQUIPOS.md, apartado «Estado de los repositorios»). |

Comandos principales ejecutados: `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only bf81545`; `git show bf81545:docs/…`; `git shortlog -sne bf81545`; `git grep` (secretos); `git tag --list`.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | clone sin autenticación OK; `lsremote.txt` línea `AS_202620_XALD OK` | Cumple | — |
| Integrantes del equipo con acceso | `git shortlog -sne bf81545`: 4 autores con correos atribuibles (correo omitido, correo omitido, correo omitido, correo omitido) | Cumple | Los 4 integrantes de `EQUIPOS.md` tienen commits al cierre: acceso demostrado por el historial. La lista de colaboradores no se pudo consultar (API no disponible), pero no hace falta aquí. |
| Equipo de 3 o 4 personas | `EQUIPOS.md`: 4 integrantes | Cumple | Xavier Yesid Garcia Diaz · Dilan Joan Gonzalez Bejarano · Luis Estheban Lozano Colmenares · Axel Jair Ruiz Bolano. |
| Ficha del problema con usuarios y alcance | `docs/ficha del problema.md` (18 líneas): solo planteamiento del problema y propuesta tecnológica | No cumple | No declara usuarios ni alcance (tampoco el README). |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | ficha: dos limitaciones («fricción en la entrada de datos» y «dependencia de conectividad») | No cumple | Son dos problemas por separado, no una tensión que enfrente dos atributos de calidad entre sí (no hay tradeoff declarado). |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md`: tabla de 2 columnas (ID, ASPECTO) con una fila A-01 | No cumple | La ficha pide la tabla de ocho columnas con ID y aspecto; aquí solo hay 2 columnas. Queda un resto de edición «```[cite: 1]» al final del archivo. |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md`: tabla por entregable con contribución de la IA, rol del estudiante y justificación técnica | Cumple | Contenido real, incluye un rechazo explícito («Se descartaron estructuras redundantes…»). |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42/arc42-template-EN.md` con los 12 encabezados | Cumple | Sin rellenar, como se espera. |
| `docs/adr/` y `docs/c4/` creados | ausentes del árbol al cierre (`git ls-tree` no los lista) | No cumple | Sin `.gitkeep` ni contenido: git no versiona directorios vacíos, pero al cierre no hay rastro de ellos (observación de montaje; se crearon después, en S2). |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clone y ls-remote sin autenticación | Cumple | — |
| Estructura mínima presente | árbol al cierre: `README.md`, `docs/arc42/`, `docs/aspectos.md`, `docs/ia.md`; faltan `docs/adr/` y `docs/c4/` | No cumple | 4 de las 6 rutas al cierre S1. |
| Estado calificado identificable | sin etiquetas; hash `bf815451…` + `%cI 2026-08-08T13:39:21-05:00` | Cumple | — |
| Nombres de ADR según la convención | sin ADR al cierre | Cumple | — |
| ADR aceptados no reescritos | sin ADR al cierre | Cumple | — |
| `docs/ia.md` al día para la semana | commits el 07 y 08 de agosto (`09bdb18`, `bf81545`) | Cumple | El registro incluye qué se rechazó y por qué (CONTRATO §6). |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'` sin salida | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne bf81545`: 4 identidades (dilanbejarano011 4, xaviergarciadiaz20-commits 3, axeljruiz717-hash 2, colmenares2007-crypto 2), una por integrante | Cumple | Los 4 integrantes contribuyeron al cierre S1. |

## Recuento de criterios

5 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Lista de colaboradores del repo: no consultable sin API; no bloquea nada porque los 4 integrantes tienen commits.

## Hallazgos para la planilla

- `docs/adr/` y `docs/c4/` no existían al cierre S1 (se crean en S2).
- Ficha del problema sin usuarios ni alcance y sin tensiones enfrentadas; se arrastra a S2.
- Resto de edición «```[cite: 1]» en `docs/aspectos.md` (marca de una herramienta de IA, no limpiada).
- Sin entregas tardías relativas a S1 (los commits siguientes al cierre corresponden a S2, a partir del 15/08).
