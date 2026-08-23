# Evidencia S1 · TRACTAR

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | **sin commits anteriores al cierre** — hash vacío |
| Cierre de la actividad | `2026-08-10T05:00:00Z` (domingo 9 de agosto, medianoche Colombia) |
| Visibilidad | pública en la revisión (clone y `git ls-remote` sin autenticación; revisiones/2026-2/_meta/lsremote.txt). El historial muestra que el primer commit es `d96664f` del `2026-08-12T21:48:09-05:00`, posterior al cierre; antes, el repo figuraba como no visible (EQUIPOS.md, apartado «Estado de los repositorios»). |

Comandos principales ejecutados: `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'` (salida vacía); `git log --format='%h %cI %an | %s'` (primer commit `d96664f`, 2026-08-12).

## Matriz de la ficha

Semana **No evaluable**: no existe ningún commit con fecha menor o igual al cierre de S1, de modo que no hay estado S1 que calificar.

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | clone sin autenticación OK | No verificado | El repo responde hoy, pero no había contenido en el cierre de S1. |
| Integrantes del equipo con acceso | — | No verificado | Sin commits ni estado que comprobar en el cierre. |
| Equipo de 3 o 4 personas | `EQUIPOS.md`: 4 integrantes | No verificado | Dato del listado, no del repositorio en el cierre. |
| Ficha del problema con usuarios y alcance | — | No verificado | La ficha (`ficha_problema.md`) se subió el 2026-08-16, después del cierre. |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | — | No verificado | Mismo motivo: contenido posterior al cierre. |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | — | No verificado | `docs/aspectos.md` se subió el 2026-08-16. |
| `docs/ia.md` iniciado con contenido real | — | No verificado | `docs/ia.md` se subió el 2026-08-16. |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | — | No verificado | Subida el 2026-08-16. |
| `docs/adr/` y `docs/c4/` creados | — | No verificado | Creados el 2026-08-16. |

Motivo único de la matriz: repo sin commits antes del cierre de S1 (primer commit `d96664f`, 2026-08-12T21:48:09-05:00).

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clone sin autenticación OK | No verificado | No aplica a S1: sin contenido en el cierre. |
| Estructura mínima presente | — | No verificado | Sin árbol en el cierre. |
| Estado calificado identificable | — | No verificado | Sin commits en el cierre; no hay hash que citar. |
| Nombres de ADR según la convención | — | No verificado | Sin ADR en el cierre. |
| ADR aceptados no reescritos | — | No verificado | Sin ADR en el cierre. |
| `docs/ia.md` al día para la semana | — | No verificado | Sin `docs/ia.md` en el cierre. |
| Sin credenciales en el repositorio ni en el historial | — | No verificado | Sin historial en el cierre. |
| Contribución de todos los integrantes | — | No verificado | Sin historial en el cierre. |

## Recuento de criterios

No evaluable: `git log --until='2026-08-10T05:00:00Z'` devuelve vacío (repo sin commits antes del cierre de S1).

## No verificado / pendientes

- Qué pasó con la entrega S1: el contenido de S1 (ficha, aspectos, ia.md, arc42) se subió entre el 12 y el 16 de agosto, dentro de la ventana de S2. El docente decide si lo considera recuperación parcial.

## Hallazgos para la planilla

- Entrega S1 tardía/inexistente: todo el montaje de la semana 1 llegó el 2026-08-12 o después (posterior al cierre del 09/08).
- La ficha `ficha_problema.md` está fechada «09/08/2026» pero su commit es del 16/08 (`516d95a`), y dice que el repo «sin poder incluirlo todavia a la organización ISCOUTB»: texto obsoleto respecto a la fecha real de subida (el repo sí está en ISCOUTB hoy).
- Integrantes de `EQUIPOS.md` sin aparición en el historial en todo el periodo revisado: Joriel Samir Barros Pena, Geronimo Alberto Cadena Garcia y Mateo Alfonso Millan Barraza (todo el historial lo firma Sebastian Garcia Devoz con dos identidades de git).
