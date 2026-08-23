# Evidencia S1 · ROUTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `68b0b05d764b3fd7d111235cde13fe8bb36fff01` · `2026-08-09T14:48:08-05:00` («AS - Semana #1») |
| Cierre S1 | `2026-08-10T05:00:00Z` (domingo 9 de agosto medianoche, Colombia) |
| Comandos principales ejecutados | `git clone --filter=blob:none --no-checkout`; `git log -1 --until`; `git ls-tree -r --name-only $HASH`; `git show $HASH:docs/...`; `git shortlog -sne`; `git grep` (secretos); `git log --after` (entregas tardías) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:14` (`AS_202620_ROUTB OK`); protocolo git sin autenticación | Cumple | Visible y público, nombre correcto |
| Integrantes del equipo con acceso | `git shortlog -sne 68b0b05`: solo `MKeinerrr` (2 identidades consolidadas: `correo omitido` + `correo omitido`) y `junior14700` | No verificado | Sin API no se pueden listar colaboradores. En el historial hasta el cierre solo constan 2 cuentas; las otras 2 (`diegobrr999-commits`, `juliandmanjarrez-tech`) empujan desde el 13-ago, lo que sugiere acceso. Haría falta el listado de colaboradores o confirmación en la sustentación |
| Equipo de 3 o 4 personas | `EQUIPOS.md:30` | Cumple | 4 integrantes declarados |
| Ficha del problema con usuarios y alcance | `docs/problema.md` (en `68b0b05`) | Cumple | Usuarios: pasajeros, conductores, administradores; alcance: consulta de rutas/cupos y reserva |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `git grep -niE 'tension|tensión|calidad' 68b0b05 -- docs README.md`: sin resultados | No cumple | La ficha declara usuarios y alcance pero ninguna tensión entre atributos de calidad |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `68b0b05` | No cumple | La tabla tiene solo 2 columnas (Aspecto/Descripción), no las 8 del curso, y la fila no lleva ID |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `68b0b05` | No cumple | Solo plantilla: tabla de herramientas vacía («—») y «Pendiente por documentar»; no hay entrada real ni declaración de no uso |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42/arc42-template-EN.md` en `68b0b05` | Cumple | Un archivo Markdown con los 12 encabezados de sección (líneas 18–207); sin rellenar, como se espera en S1 |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree -r 68b0b05`: `docs/adr/.gitkeep`, `docs/c4/.gitkeep` | Cumple | Ambos directorios versionados con `.gitkeep` |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:14` | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 68b0b05`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` | Cumple | arc42 como archivo único de plantilla |
| Estado calificado identificable | `68b0b05d764b3fd7d111235cde13fe8bb36fff01` · `2026-08-09T14:48:08-05:00` | Cumple | Commit anterior al cierre, sin etiqueta |
| Nombres de ADR según la convención | `docs/adr/` contiene solo `.gitkeep` | Cumple | Sin ADR todavía; filtro sin salida |
| ADR aceptados no reescritos | Sin ADR en el repositorio | Cumple | No aplica por ausencia |
| `docs/ia.md` al día para la semana | commits `b9b4ee8` (08-08) y `90f5542` (08-07); contenido: plantilla vacía, sin entradas ni rechazos | No cumple | Existe y se creó en el periodo, pero sin contenido real |
| Sin credenciales en el repositorio ni en el historial | `git grep` regex §9 sobre `68b0b05`: sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'`: vacío | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne 68b0b05`: 2 personas (MKeinerrr consolidado + junior14700) de 4 | No cumple | No aparece ninguna cuenta atribuible a Diego Baron ni a Julian Manjarrez antes del cierre S1; normal en semana de montaje según la ficha |

## Recuento de criterios

- **5 de 9** criterios cumplidos en la matriz de la ficha.

## No verificado / pendientes

- Acceso de los 4 integrantes en S1: sin API no se pueden listar colaboradores; resolver en la sustentación (los 4 aparecen en el historial desde la semana 2).

## Hallazgos para la planilla

- Sin entregas tardías en S1: commit calificado `68b0b05` dentro del plazo; siguiente commit el 13-ago (`89b6ff5`).
- `MKeinerrr` firma con dos identidades (correo personal e institucional): consolidado como una persona.
- Ficha del problema sin tensiones de calidad; `aspectos.md` sin las 8 columnas ni ID; `ia.md` solo plantilla.
