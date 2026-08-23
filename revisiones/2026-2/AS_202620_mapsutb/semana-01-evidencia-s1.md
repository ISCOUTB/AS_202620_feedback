# Evidencia S1 · mapsutb

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `7e56ad372dbfebd8c7c38f74b19006e14f9e72e3` · `2026-08-09T23:27:46-05:00` (último commit ≤ cierre 2026-08-10T05:00:00Z) |
| Comandos principales | `git clone --filter=blob:none --no-checkout` (sin auth); `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:<ruta>`; `git shortlog -sne HEAD`; `git grep -nI -E '<regex secretos>' <hash>` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:22` (OK sin autenticación); clon sin credenciales | Cumple | `AS_202620_mapsutb` en ISCOUTB, público |
| Integrantes del equipo con acceso | `git shortlog` al cierre S1: `charlygz21` (3 commits) y `nerlis-otero` (1) | No verificado | Sin API no se pueden listar colaboradores. `CarlosManrique-1397` aparece desde S2; de «Isabel Paez Matallana» no hay cuenta observada. Haría falta la lista de colaboradores |
| Equipo de 3 o 4 personas | `EQUIPOS.md:26` (4 integrantes); `docs/ficha-problema.md` lista los 4 | Cumple | Carlos Alberto Galvis Zuluaga · Carlos David Manrique Fals · Nerlis Nikol Otero Perez · Isabel Sofia Paez Matallana |
| Ficha del problema con usuarios y alcance | `docs/ficha-problema.md` (usuarios en «Problema»: estudiantes nuevos, de intercambio y visitantes; «Alcance» con inclusión/exclusión) | Cumple | Ficha completa con problema, objetivo general/específicos, alcance y arquitectura propuesta |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `docs/ficha-problema.md` (sin sección de tensiones) | No cumple | No hay tensiones de calidad; el árbol de utilidad y los atributos llegan después, en S2 |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `7e56ad3` (tabla de 8 columnas; fila A-01 con ID y aspecto) | Cumple | Además de lo pedido, la fila A-01 trae requisito RF-01 y un escenario en formato de seis partes |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `7e56ad3`; commit `f829f2e` (2026-08-09) | Cumple | Dos entradas (07/08/2026) con herramienta, uso, resultado y columna Aceptado/Rechazado con motivo |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | árbol de `7e56ad3` → `README.md`, `docs/aspectos.md`, `docs/ficha-problema.md`, `docs/ia.md` | No cumple | No existe `docs/arc42/` ni la plantilla en el commit calificado |
| `docs/adr/` y `docs/c4/` creados | árbol de `7e56ad3` (sin esas rutas) | No verificado | Git no versiona directorios vacíos: no se puede distinguir «creados sin `.gitkeep`» de «no creados». Observación de montaje |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:22`; clon sin autenticación | Cumple | Responde por protocolo git sin credenciales |
| Estructura mínima presente | árbol de `7e56ad3` | No cumple | Faltan `docs/arc42/`, `docs/adr/`, `docs/c4/`; la ficha está como `docs/ficha-problema.md` (no exigida en ruta) |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | `7e56ad372dbfebd8c7c38f74b19006e14f9e72e3` · `2026-08-09T23:27:46-05:00`. Ojo: la etiqueta `corte-1` apunta exactamente a este commit de S1 (prematura para un corte posterior; verificar si se moverá) |
| Nombres de ADR según la convención | sin `docs/adr/` → filtro vacío | Cumple | Vacuo: sin ADR (no exigidos en S1) |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md` → `2026-08-09 f829f2e`; contenido con Aceptado/Rechazado y motivo | Cumple | Mejor que el mínimo: registra qué se aceptó, qué se rechazó y por qué |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' 7e56ad3` (sin salida); sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | `git shortlog` al cierre S1: 2 identidades (`charlygz21`, `nerlis-otero`) | No cumple | 2 de 4 integrantes sin aparición al cierre S1; sin cuenta atribuible a Isabel Sofia Paez Matallana (correspondencias de cuentas las confirma el docente) |

## Recuento de criterios

5 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Acceso de los integrantes: sin API no se pueden listar colaboradores; haría falta la lista de colaboradores o commits de cada integrante.
- Creación de `docs/adr/` y `docs/c4/`: git no versiona directorios vacíos; haría falta `.gitkeep` o confirmación del equipo.

## Hallazgos para la planilla

- Integrantes sin aparición en el historial: Isabel Sofia Paez Matallana sin ninguna cuenta observada; Carlos David Manrique Fals (cuenta `CarlosManrique-1397` observada en EQUIPOS.md) sin commits hasta después del cierre S1.
- Ficha del problema sin las dos tensiones de calidad.
- Estructura no montada en S1: sin `docs/arc42/`, `docs/adr/`, `docs/c4/`.
- Etiqueta `corte-1` colocada sobre el commit de S1 (`7e56ad3`): si el corte 1 es posterior, la etiqueta está mal puesta o se moverá; quedará vigilada.
- Entregas tardías: nada después del cierre S1 con contenido de S1.
