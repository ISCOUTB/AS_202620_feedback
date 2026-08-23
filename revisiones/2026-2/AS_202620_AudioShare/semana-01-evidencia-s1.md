# Evidencia S1 · AudioShare

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` (en el cierre S1 el nombre era `AS_202620_PROYECTO_AudioShare`; renombrado el 2026-08-18) |
| Estado revisado | `1c9ebb0a57a85fa8ac7d68289d46fd83faee0853` · 2026-08-09T20:31:49-05:00 · «Update IA usage documentation in ia.md» |
| Cierre | 2026-08-10T05:00:00Z (domingo 9 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:docs/...`; `git shortlog -sne <hash>`; `git grep -nIE '<secreto>' <hash>` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | Clon público sin autenticación OK; `revisiones/2026-2/_meta/lsremote.txt` | No cumple | En el cierre el nombre era `AS_202620_PROYECTO_AudioShare` (título del README en `1c9ebb0a` y commit de renombrado `31bcc18` «Rename project from AS_202620_PROYECTO_AudioShare to AS_202620_AudioShare», 2026-08-18, posterior al cierre). Visible y en la organización sí. |
| Integrantes del equipo con acceso | `git shortlog -sne 1c9ebb0a` | No verificado | Aparecen 3 de 4: Yeiver (6 commits), Santiago (3), Elian (2). Vincent Cardona Castro no aparece en el historial S1 (sí en S2 como `cardonavincent26-design`). Sin API de GitHub no se puede comprobar la lista de colaboradores en S1; haría falta esa lista o la matrícula. |
| Equipo de 3 o 4 personas | EQUIPOS.md, fila AudioShare | Cumple | 4 integrantes declarados: Santiago Adolfo Camacho Hernandez, Vincent Cardona Castro, Elian Daniel Perea Vanegas, Yeiver Andres Verjel Perez. |
| Ficha del problema con usuarios y alcance | `docs/ficha-problema.md` (en `1c9ebb0a`) | No cumple | El apartado «Prototipo» describe el alcance, pero la ficha no declara usuarios (solo roles de dispositivo emisor/receptor, y estos viven en `docs/aspectos.md`, no en la ficha). |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `docs/ficha-problema.md` completo | No cumple | La ficha no menciona ninguna tensión de calidad. Solo problema y prototipo. |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` (en `1c9ebb0a`) | No cumple | Hay un aspecto declarado («Sincronización de reproducción de audio»), pero el archivo es una lista campo:valor, no la tabla de 8 columnas del curso (ID · Aspecto · Requisito · C4 · ADR · Código · Pruebas · Evidencia), y no hay columna ID. |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` (creado en `d94cccc`, actualizado en `1c9ebb0a`, dentro del cierre) | Cumple | Propósito, herramientas, verificación de resultados y estado reales; declara que el registro detallado se completará después (entrada válida). |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `git ls-tree -r --name-only 1c9ebb0a` | No cumple | `docs/arc42/` no existe en el árbol S1 (solo `README.md`, `docs/aspectos.md`, `docs/ficha-problema.md`, `docs/ia.md`). |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree -r --name-only 1c9ebb0a` | No cumple | No existen en el árbol S1. Git no versiona directorios vacíos y no hay `.gitkeep`, así que se anota como observación de montaje, no como contenido ausente; aun así, en S1 no hay rastro de su creación. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | No cumple | Público y en la organización sí; el nombre en el cierre (`AS_202620_PROYECTO_AudioShare`) no sigue `AS_202620_<PROYECTO>`: le sobra `PROYECTO_`. Corregido por el equipo el 2026-08-18 (`31bcc18`), después del cierre. |
| Estructura mínima presente | `git ls-tree -r --name-only 1c9ebb0a` | No cumple | De las seis rutas solo hay 3: `README.md`, `docs/aspectos.md`, `docs/ia.md`. Faltan `docs/arc42/`, `docs/adr/` y `docs/c4/`. |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | Hash `1c9ebb0a…` con `%cI` 2026-08-09T20:31:49-05:00; último commit anterior al cierre. |
| Nombres de ADR según la convención | sin `docs/adr/` en S1 | Cumple (vacuo) | No hay ADR todavía (no exigidos en S1): nada que incumpla la convención. |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md` | Cumple | Creado `d94cccc` y actualizado `1c9ebb0a`, ambos dentro del periodo S1. Todavía no registra «qué se rechazó y por qué» (no exigido en S1; pendiente cuando haya usos reales). |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex CONTRATO §9), `git ls-files \| grep .env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias en las tres comprobaciones. |
| Contribución de todos los integrantes | `git shortlog -sne 1c9ebb0a` | No verificado | Historial S1 con 3 identidades de 4 (falta Vincent Cardona Castro). En semana 1 la ficha admite que solo empuje uno si el resto tiene acceso; sin API no se puede comprobar el acceso de Vincent en S1. |

## Recuento de criterios

- Ficha: **2 de 9** criterios Cumple.

## No verificado / pendientes

- Acceso de Vincent Cardona Castro a la organización en la semana 1 (requiere lista de colaboradores o matrícula; la API de GitHub estaba agotada).
- No se pudo inspeccionar visualmente ningún PNG con la herramienta de revisión (aplica a semanas con diagramas).

## Hallazgos para la planilla

- Nombre del repositorio desviado hasta el 2026-08-18: `AS_202620_PROYECTO_AudioShare` → renombrado a `AS_202620_AudioShare` en `31bcc18` (posterior al cierre S2).
- Ficha del problema sin usuarios declarados y sin tensiones de calidad.
- `docs/aspectos.md` no usa la tabla de 8 columnas del curso.
- Estructura no montada en S1: sin `docs/arc42/`, `docs/adr/`, `docs/c4/`.
- Vincent Cardona Castro sin commits en el historial S1.
- Entregas posteriores al cierre S1 (para contexto): todo el trabajo de arc42/C4 llegó entre el 2026-08-16 y el 2026-08-22.
