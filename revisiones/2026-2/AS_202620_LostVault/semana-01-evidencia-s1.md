# Evidencia S1 · LostVault

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `560ba895e65114ab67c5699515ed6e9856d36ee8` · `2026-08-09T21:10:31-05:00` (último commit ≤ cierre 2026-08-10T05:00:00Z; sin etiquetas en el repo) |
| Comandos principales | `git clone --filter=blob:none --no-checkout` (sin auth); `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:<ruta>`; `git shortlog -sne HEAD`; `git grep -nI -E '<regex secretos>' <hash>` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:11` (OK sin autenticación); clon por protocolo git sin credenciales | Cumple | Nombre según convención `AS_202620_LostVault`, visible públicamente |
| Integrantes del equipo con acceso | `git shortlog -sne HEAD`: 13 commits, una sola identidad (`Roy Gonzalez`) | No verificado | Sin API disponible no se pueden listar colaboradores; el historial solo muestra un autor. Haría falta la lista de colaboradores o commits de los demás integrantes |
| Equipo de 3 o 4 personas | `EQUIPOS.md:25` (4 integrantes) | Cumple | Jose Faustino Espana Noriega · Roy Andres Gonzalez Blanco · Shamara Llorente Tapias · Kiefer Monterroza Manjarres |
| Ficha del problema con usuarios y alcance | `docs/ficha_problema.md` — «Población afectada» (usuarios) y «Propuesta» (alcance) | Cumple | Ficha de una página con contexto, problema, población, propuesta y valor esperado |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `docs/ficha_problema.md` (sin sección de tensiones); `docs/aspectos.md` declara un único aspecto (Disponibilidad) | No cumple | Se declara un atributo prioritario, no dos tensiones enfrentadas (p. ej. tiempo de respuesta vs. costo) |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `560ba895` | No cumple | El archivo es narrativo (aspecto + justificación + cómo garantizarlo); no existe la tabla de ocho columnas ni fila con ID + aspecto |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `560ba895`; commit `560ba89` (2026-08-09) | Cumple | Registra uso de Claude el 2026-08-08 para redacción de la ficha, qué se aceptó y criterio del equipo. No registra nada rechazado (ver matriz transversal) |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `git ls-tree -r --name-only 560ba895` → `README.md`, `docs/aspectos.md`, `docs/ficha_problema.md`, `docs/ia.md` | No cumple | No existe `docs/arc42/` ni plantilla alguna en el árbol del commit calificado |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree -r --name-only 560ba895` (sin esas rutas) | No verificado | Ausentes del árbol. Git no versiona directorios vacíos: no se puede distinguir «creados vacíos sin .gitkeep» de «no creados». Observación de montaje; lo aclara el equipo (o con `.gitkeep`) |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:11`; clon sin autenticación | Cumple | `github.com/ISCOUTB/AS_202620_LostVault` responde |
| Estructura mínima presente | árbol de `560ba895` | No cumple | Faltan `docs/arc42/`, `docs/adr/` y `docs/c4/`; presentes `README.md`, `docs/aspectos.md`, `docs/ia.md` |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | `560ba895e65114ab67c5699515ed6e9856d36ee8` · `2026-08-09T21:10:31-05:00`; sin etiquetas (no exigidas en evidencia semanal) |
| Nombres de ADR según la convención | `docs/adr/` inexistente → filtro vacío | Cumple | Sin ADR todavía (no exigidos en S1); nada que incumpla la convención |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo: no hay ADR que reescribir |
| `docs/ia.md` al día para la semana | `docs/ia.md`; `git log -- docs/ia.md` → `2026-08-09 560ba89` | No cumple | Existe y tiene contenido real, pero no registra qué se rechazó ni por qué (§6 del contrato) |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' 560ba895` (sin salida); `git ls-tree` sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` → 13 commits de una sola identidad | No cumple | Solo «Roy Gonzalez»; 3 de 4 integrantes sin aparición (en S1 puede ser reparto, pero el acceso de los demás no se pudo comprobar — fila 2 de la ficha) |

## Recuento de criterios

4 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Acceso de los integrantes: sin API no se pueden listar colaboradores; haría falta la lista de colaboradores del repo o commits de cada integrante.
- Creación de `docs/adr/` y `docs/c4/`: git no versiona directorios vacíos; haría falta un `.gitkeep` o confirmación del equipo.

## Hallazgos para la planilla

- Integrantes sin aparición en el historial: Jose Faustino Espana Noriega, Shamara Llorente Tapias y Kiefer Monterroza Manjarres no tienen commits (identidad única «Roy Gonzalez»; EQUIPOS.md observa la cuenta `RGBlanco18`; la correspondencia entre «Roy Gonzalez» y Roy Andres Gonzalez Blanco es probable por el nombre del autor de commits, pero la confirma el docente).
- Ficha del problema sin las dos tensiones de calidad exigidas.
- `docs/aspectos.md` sin la tabla de ocho columnas (narrativo).
- Estructura no montada en S1: sin `docs/arc42/`, `docs/adr/`, `docs/c4/`.
- `docs/ia.md` sin registro de lo rechazado.
- Entregas tardías: nada después del cierre S1 que corresponda a S1.
