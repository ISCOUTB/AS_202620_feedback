# Evidencia S1 · CampusMarket

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `81ef5f10326ab27622a9b1e507fee2e7752f494e` · `2026-08-08T20:17:21-05:00` (último commit ≤ cierre 2026-08-10T05:00:00Z) |
| Comandos principales | `git clone --filter=blob:none --no-checkout` (sin auth); `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:<ruta>`; `git shortlog -sne HEAD`; `git grep -nI -E '<regex secretos>' <hash>` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:12` (OK sin autenticación); clon sin credenciales | Cumple | `AS_202620_PROYECTO_CAMPUSMARKET` en ISCOUTB, público |
| Integrantes del equipo con acceso | historial al cierre S1: 7 commits de una sola identidad (`camilixo92`) | No verificado | Sin API no se pueden listar colaboradores; ninguna otra cuenta aparece en el historial. Haría falta la lista de colaboradores |
| Equipo de 3 o 4 personas | `EQUIPOS.md:28` (3 integrantes) | Cumple | Nilver Garcia Pimentel · Camilo Jose Martinez Berrio · Joshua Jose Tenorio Alvarez. Ojo: el README al cierre S1 listaba solo 2 integrantes; Nilver se añadió el 11 de agosto (commit `9a9dc3d`, posterior al cierre) |
| Ficha del problema con usuarios y alcance | `README.md` en `81ef5f1` (Problema, Objetivo general, Beneficiarios) | Cumple | Usuarios: estudiantes y administrador; alcance: publicación, búsqueda y gestión de productos para venta/alquiler |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `README.md` y `docs/aspectos.md` en `81ef5f1` | No cumple | Solo se declara un aspecto (Mantenibilidad); no hay tensiones entre atributos |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `81ef5f1` (texto narrativo sobre Mantenibilidad) | No cumple | Sin la tabla de ocho columnas ni fila con ID + aspecto |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `81ef5f1` (tabla Registro con entrada 08/08/2026, ChatGPT) | Cumple | Una entrada real con fecha, herramienta y uso |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | árbol de `81ef5f1` → `README.md`, `docs/aspectos.md`, `docs/ia.md` | No cumple | No existe `docs/arc42/` ni plantilla en el commit calificado |
| `docs/adr/` y `docs/c4/` creados | árbol de `81ef5f1` (sin esas rutas); los commits `708a785` y `5b6f572` del 11-08 crean `docs/adr` y `docs/c4` como archivos, ya después del cierre | No verificado | Git no versiona directorios vacíos; la evidencia posterior muestra que ni siquiera como directorios existían al cierre. Observación de montaje |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:12`; clon sin autenticación | Cumple | Responde por protocolo git sin credenciales |
| Estructura mínima presente | árbol de `81ef5f1` | No cumple | Faltan `docs/arc42/`, `docs/adr/`, `docs/c4/`; la ficha vive en el README |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | `81ef5f10326ab27622a9b1e507fee2e7752f494e` · `2026-08-08T20:17:21-05:00`; sin etiquetas |
| Nombres de ADR según la convención | sin `docs/adr/` → filtro vacío | Cumple | Vacuo: sin ADR (no exigidos en S1) |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `docs/ia.md` en `81ef5f1` (entrada real, pero sin lo rechazado) | No cumple | Falta registrar qué se rechazó y por qué (CONTRATO §6) |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' 81ef5f1` (sin salida); sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | historial al cierre S1: una sola identidad (`camilixo92`, 7 commits) | No cumple | 1 de 3 integrantes con commits al cierre S1 |

## Recuento de criterios

4 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Acceso de los integrantes: sin API no se pueden listar colaboradores; haría falta la lista de colaboradores o commits de cada integrante.
- Creación de `docs/adr/` y `docs/c4/`: git no versiona directorios vacíos; la evidencia posterior (11-08) muestra que se crearon como archivos y después del cierre.

## Hallazgos para la planilla

- Integrantes sin aparición en el historial: Nilver Garcia Pimentel y Joshua Jose Tenorio Alvarez sin commits (todo firmado por `camilixo92`).
- README al cierre S1 con solo 2 integrantes; el tercero (Nilver Garcia Pimentel) se añadió el 11-08 (`9a9dc3d`), después del cierre.
- Entregas tardías de S1: `708a785` («Add architecture decision record file», 2026-08-11T11:23:15-05:00) y `5b6f572` («Create c4», 2026-08-11T11:23:29-05:00) — montaje de estructura posterior al cierre.
- Ficha del problema sin las dos tensiones de calidad; `docs/aspectos.md` sin la tabla de ocho columnas.
- `docs/ia.md` sin registro de lo rechazado.
