# Evidencia S1 · ShareU

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `8886d4efa1ebbf0f801a2449315b752e2948753a` · `2026-08-09T22:03:52-05:00` («Add files via upload») |
| Cierre S1 | `2026-08-10T05:00:00Z` (domingo 9 de agosto medianoche, Colombia) |
| Comandos principales ejecutados | `git clone --filter=blob:none --no-checkout`; `git log -1 --until`; `git ls-tree -r --name-only $HASH`; `git show $HASH:...` (incluida la ficha PDF extraída y leída con `pdftotext`); `git shortlog -sne`; `git grep` (secretos); `git log --after` (tardías) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:16` (`AS_202620_ShareU OK`); protocolo git sin autenticación | Cumple | Visible y público |
| Integrantes del equipo con acceso | `git shortlog -sne 8886d4e`: solo `Dayana` (7 commits) | No verificado | Sin API no se listan colaboradores. `Nicolas-HH` y `steven` empujan el 10-ago (tras el cierre); no hay ninguna cuenta atribuible a Luis Carlos Corredor ni en S1 ni en S2 |
| Equipo de 3 o 4 personas | `EQUIPOS.md:31` | Cumple | 4 integrantes declarados |
| Ficha del problema con usuarios y alcance | `Ficha_del_Problema_EncuentraUTB.pdf` (raíz del repo, 1 página, leída con `pdftotext`) | Cumple | Usuarios (estudiantes, docentes, administrativos, seguridad, visitantes) y funciones/alcance declarados. Observaciones: la ficha está como PDF en la raíz (no Markdown en `docs/`), y el problema que describe (EncuentraUTB, objetos perdidos) ya no es el del proyecto en S2 (ShareU) |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `git grep -niE 'tension|tensión' 8886d4e`: sin resultados | No cumple | La ficha no enfrenta dos atributos de calidad |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `8886d4e` | No cumple | El aspecto Usabilidad está declarado en prosa (con escenario detallado), pero no hay tabla de 8 columnas ni ID |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `8886d4e` | Cumple | Declara herramienta usada (Claude), propósito y lineamientos de revisión humana |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `git ls-tree -r 8886d4e`: no existe `docs/arc42/` | No cumple | La plantilla arc42 no estaba montada al cierre de S1 |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree -r 8886d4e`: no existen `docs/adr/` ni `docs/c4/` | No cumple | Ninguno de los dos directorios creado |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:16` | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 8886d4e`: solo `README.md`, `docs/aspectos.md`, `docs/ia.md` y el PDF; faltan `docs/arc42/`, `docs/adr/`, `docs/c4/` | No cumple | Estructura incompleta al cierre de S1 |
| Estado calificado identificable | `8886d4efa1ebbf0f801a2449315b752e2948753a` · `2026-08-09T22:03:52-05:00` | Cumple | Commit anterior al cierre, sin etiqueta |
| Nombres de ADR según la convención | No existe `docs/adr/` | Cumple | Sin ADR; filtro vacío |
| ADR aceptados no reescritos | Sin ADR | Cumple | No aplica por ausencia |
| `docs/ia.md` al día para la semana | commits `2942395` y `400f095` (09-ago) dentro del periodo; contenido real pero sin registro de usos ni de lo rechazado | No cumple | Existe y se creó en el periodo, pero la «tabla de registro» anunciada no tiene entradas ni rechazos |
| Sin credenciales en el repositorio ni en el historial | `git grep` regex §9 sobre `8886d4e`: sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'`: vacío | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne 8886d4e`: 1 persona de 4 | No cumple | Hasta el cierre solo consta Dayana; no aparecen cuentas atribuibles a Steven Contreras, Nicolas Hernandez ni Luis Carlos Corredor antes del cierre |

## Recuento de criterios

- **4 de 9** criterios cumplidos en la matriz de la ficha.

## No verificado / pendientes

- Acceso de los 4 integrantes en S1: sin API no se listan colaboradores (en el historial hasta el cierre solo consta 1 cuenta).

## Hallazgos para la planilla

- Entrega tardía parcial tras el cierre de S1: `371e997` (10-ago 16:18) y `4690611` (10-ago 16:25), ambos retoques del README.
- Estructura no montada al cierre de S1 (sin `docs/arc42/`, `docs/adr/`, `docs/c4/`).
- Ficha del problema en PDF en la raíz, y sobre «EncuentraUTB», que en S2 se abandona por «ShareU» (el PDF se borra el 16-ago, commit `cf57f6e`). Repositorio y proyecto deben quedar alineados para el corte 1.
- Luis Carlos Corredor Altamiranda no aparece en el historial en ninguna semana.
