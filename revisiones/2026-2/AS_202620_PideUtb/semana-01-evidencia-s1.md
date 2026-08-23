# Evidencia S1 · PideUtb

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `48cfbe3b36f2cda51b8f6786a8424a9ec727fc1a` · `2026-08-08T15:12:35-05:00` (último commit ≤ cierre 2026-08-10T05:00:00Z) |
| Comandos principales | `git clone --filter=blob:none --no-checkout` (sin auth); `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:<ruta>`; extracción de `ficha_problema.pdf` y `pdftotext`; `git shortlog -sne HEAD`; `git grep -nI -E '<regex secretos>' <hash>` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:13` (OK sin autenticación); clon sin credenciales | Cumple | Estuvo privado en la primera comprobación (EQUIPOS.md:49-52) y hoy es público |
| Integrantes del equipo con acceso | historial al cierre S1: 4 commits de una sola persona (Santiago, dos identidades: `Santiago Cuesta` y `Santiago-C0`) | No verificado | Sin API no se pueden listar colaboradores; `daniarriet` aparece desde S2. Haría falta la lista de colaboradores |
| Equipo de 3 o 4 personas | `EQUIPOS.md:27` (3 integrantes) | Cumple | Daniela Sofia Arrieta Guardo · Santiago Jose Cuesta Maza · Ruddy Rodriguez Romero |
| Ficha del problema con usuarios y alcance | `ficha_problema.pdf` (1 página; texto extraído con pdftotext): usuarios (estudiantes, establecimientos) y alcance (módulo estudiante, módulo establecimiento, pago en Sandbox, código de recogida) | Cumple | La ficha está en PDF y no en Markdown: el curso pide documentación revisable en el repositorio (CONTRATO §2) |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | texto extraído de `ficha_problema.pdf` (sin tensiones de calidad) | No cumple | La ficha describe el problema y la propuesta funcional, sin tensiones entre atributos |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `48cfbe3` (solo texto narrativo sobre Usabilidad) | No cumple | Sin la tabla de ocho columnas ni fila con ID + aspecto |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `48cfbe3` | Cumple | Texto de política real, pero sin registro de usos concretos ni declaración de no haber usado IA todavía |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | árbol de `48cfbe3` → `README.md`, `docs/aspectos.md`, `docs/ia.md`, `ficha_problema.pdf` | No cumple | No existe `docs/arc42/` ni plantilla en el commit calificado |
| `docs/adr/` y `docs/c4/` creados | árbol de `48cfbe3` (sin esas rutas) | No verificado | Git no versiona directorios vacíos; haría falta `.gitkeep` o confirmación del equipo |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:13`; clon sin autenticación | Cumple | Antes privado (EQUIPOS.md:49-52); hoy público |
| Estructura mínima presente | árbol de `48cfbe3` | No cumple | Faltan `docs/arc42/`, `docs/adr/`, `docs/c4/`; ficha en PDF en la raíz |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | `48cfbe3b36f2cda51b8f6786a8424a9ec727fc1a` · `2026-08-08T15:12:35-05:00`; sin etiquetas (no exigidas en evidencia semanal) |
| Nombres de ADR según la convención | sin `docs/adr/` → filtro vacío | Cumple | Vacuo: sin ADR (no exigidos en S1) |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `docs/ia.md` en `48cfbe3` (solo política, sin registro de uso ni de rechazos) | No cumple | Falta el registro con lo aceptado y lo rechazado con motivo (CONTRATO §6) |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' 48cfbe3` (sin salida); sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | historial al cierre S1: una sola persona (identidades consolidadas `Santiago Cuesta`/`Santiago-C0`) | No cumple | 1 de 3 integrantes con commits al cierre S1 |

## Recuento de criterios

4 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Acceso de los integrantes: sin API no se pueden listar colaboradores; haría falta la lista de colaboradores o commits de cada integrante.
- Creación de `docs/adr/` y `docs/c4/`: git no versiona directorios vacíos.

## Hallazgos para la planilla

- Integrantes sin aparición en el historial: Ruddy Rodriguez Romero sin cuenta observada en todo el historial; Daniela Sofia Arrieta Guardo (cuenta `daniarriet` en EQUIPOS.md) empuja por primera vez en S2.
- Ficha del problema entregada solo como PDF (menos revisable; el curso pide Markdown).
- Ficha sin las dos tensiones de calidad.
- `docs/aspectos.md` narrativo, sin tabla de ocho columnas.
- `docs/ia.md` sin registro de usos (solo política).
- Entregas tardías: ninguna después del cierre S1.
- Nombre en el README con guion delante («-AS_202620_PideUtb») y URL de un merge con el mismo guion: inconsistencia menor de nomenclatura, el repo real cumple la convención.
