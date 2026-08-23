# Evidencia S1 · Recobra

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `da5c15d428f49d6026a6e4b50881108ea1807cef` · `2026-08-07T17:54:04-05:00` (último commit ≤ cierre 2026-08-10T05:00:00Z) |
| Comandos principales | `git clone --filter=blob:none --no-checkout` (sin auth); `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:<ruta>`; `git shortlog -sne HEAD`; `git grep -nI -E '<regex secretos>' <hash>` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:15` (OK sin autenticación); clon sin credenciales | Cumple | `AS_202620_Recobra` en ISCOUTB, público |
| Integrantes del equipo con acceso | historial al cierre S1: 2 identidades (`Cconde31`, `MiguelJacome`, correos @utb.edu.co) | No verificado | Sin API no se pueden listar colaboradores; haría falta la lista de colaboradores o commits de los otros dos integrantes |
| Equipo de 3 o 4 personas | `EQUIPOS.md:29` (4 integrantes) | Cumple | Camilo Andres Conde Corrales · Fernando Isacc Conde Herrera · Miguel Alejandro Iii Jacome Yanez · Veronica Ubarne Reyes |
| Ficha del problema con usuarios y alcance | `README.md` en `da5c15d` (Problema y Objetivos; alcance: espacio delimitado, publicar/matching/notificar/trazabilidad) | Cumple | Los usuarios no tienen sección propia: están implícitos («quien pierde algo», «quien lo encuentra») |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `README.md` y `docs/aspectos.md` en `da5c15d` | No cumple | Solo se declara un aspecto (seguridad en la entrega); no hay tensiones entre atributos |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `da5c15d` (texto narrativo) | No cumple | Sin la tabla de ocho columnas ni fila con ID + aspecto |
| `docs/ia.md` iniciado con contenido real | `docs/ia` en `da5c15d` (archivo de 1 byte, vacío) | No cumple | El archivo existe (sin extensión `.md`) pero está vacío: no hay contenido real |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | árbol de `da5c15d` → `README.md`, `docs/aspectos.md`, `docs/ia` | No cumple | No existe `docs/arc42/` ni plantilla |
| `docs/adr/` y `docs/c4/` creados | árbol de `da5c15d` (sin esas rutas) | No verificado | Git no versiona directorios vacíos; haría falta `.gitkeep` o confirmación del equipo |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:15`; clon sin autenticación | Cumple | Responde por protocolo git sin credenciales |
| Estructura mínima presente | árbol de `da5c15d` | No cumple | Faltan `docs/arc42/`, `docs/adr/`, `docs/c4/`; la ficha vive en el README |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | `da5c15d428f49d6026a6e4b50881108ea1807cef` · `2026-08-07T17:54:04-05:00`; sin etiquetas |
| Nombres de ADR según la convención | sin `docs/adr/` → filtro vacío | Cumple | Vacuo: sin ADR (no exigidos en S1) |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `docs/ia` en `da5c15d` (vacío) | No cumple | Archivo de 1 byte, sin registro de uso ni de rechazos (CONTRATO §6) |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' da5c15d` (sin salida); sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | historial al cierre S1: 2 identidades (`Cconde31`, `MiguelJacome`) | No cumple | 2 de 4 integrantes con commits al cierre S1 |

## Recuento de criterios

3 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Acceso de los integrantes: sin API no se pueden listar colaboradores; haría falta la lista de colaboradores o commits de cada integrante.
- Creación de `docs/adr/` y `docs/c4/`: git no versiona directorios vacíos.

## Hallazgos para la planilla

- Integrantes sin aparición en el historial: Fernando Isacc Conde Herrera y Veronica Ubarne Reyes sin cuentas observadas (solo `Cconde31` y `MiguelJacome`).
- `docs/ia` vacío y sin extensión `.md`.
- Ficha del problema sin las dos tensiones de calidad; `docs/aspectos.md` sin la tabla de ocho columnas.
- Entregas tardías: nada posterior al cierre S1 con contenido de S1.
