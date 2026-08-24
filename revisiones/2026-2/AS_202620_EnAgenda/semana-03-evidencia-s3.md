# Evidencia S3 · EnAgenda

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `c38adfb94` · 2026-08-23T23:49:01-05:00 (último commit ≤ cierre 2026-08-24T05:00:00Z) |
| Fecha/hora de revisión | 2026-08-24, DESPUÉS del cierre. Revisión actualizada tras el cierre: el equipo empujó después de la primera revisión; hash calificado definitivo |
| Primera revisión | `32b8a9078` · 2026-08-23T15:24:19-05:00 (quedó sin efecto; todo se recalifica sobre el hash definitivo) |
| Commits tardíos | ninguno: `git log --after='2026-08-24T05:00:00Z'` no devuelve commits |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until='2026-08-24T05:00:00Z'`; `git ls-tree`; `git show`; `git grep` de secretos (exit 1). Sin API de actions: no hay `.github/workflows/` |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/04-estrategia-de-solución .md` | Cumple | Recuperada del placeholder: elige monolito modular (§4.2), justifica contra privacidad y consistencia, define límites entre módulos (§4.3), organización inicial (§4.4) y consecuencias, y enlaza matriz y ADR. Observación: no nombra tácticas explícitas por escenario EC-xx (las reglas de vigencia/estados se concentran en el módulo de invitaciones, sin citar los escenarios). |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/arquitectura/matriz-comparativa-estilos .md` | No cumple | Compara los tres estilos con criterios propios del proyecto (privacidad de enlaces, consistencia, ajuste al dominio, equipo de 3…), pero ninguna fila es un escenario del árbol de utilidad: no hay EC-01…EC-05 ni se lee qué escenario mejora/empeora con cada estilo. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-app-movil-y-web-de-invitaciones .md` | No cumple | El nombre no pasa el filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$` (espacio antes de `.md`) y ya no corresponde al contenido: el ADR ahora decide «Usar monolito modular» y sus enlaces internos apuntan a `0001-usar-monolito-modular.md`, que no existe. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-app-movil-y-web-de-invitaciones .md` | Cumple | Reemplazado por la decisión de estilo: estado «Aceptado», título «Usar monolito modular», contexto, alternativas A/B/C, decisión, consecuencias y trazabilidad. Escenarios EC-01…EC-05 citados en la cabecera. |
| Alternativas descartadas con su motivo | ADR §A y §B | Cumple | Capas descartada porque no expresa los límites entre áreas del negocio; hexagonal porque puertos/adaptadores no se justifican para el alcance actual. Con motivos detallados. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos .md:3` (columna ADR) y `docs/arc42/10-requisitos-de-calidad .md` | No cumple | `aspectos.md` ya usa la tabla de 8 columnas, pero la columna ADR sigue «Pendiente»; `10-requisitos-de-calidad .md` no enlaza al ADR. Además, §4.5 enlaza `docs/arquitectura/matriz-comparativa-estilos.md` sin el espacio que el archivo sí tiene (enlace roto). |
| Arranque con un solo comando documentado en el README | `README.md` (sin sección de arranque); `docs/main.py`, `docs/Esqueleto.py` | No cumple | El README no documenta ningún comando de arranque ni de prueba. El esqueleto real es un script demo suelto en `docs/`: `main.py` importa `app.eventos.factory`, módulo que no existe en el árbol, y `Esqueleto.py` es una clase monolítica de demostración. |
| Prueba automatizada en verde | `git ls-tree -r --name-only c38adfb94` | No cumple | No existe ninguna prueba: el ADR promete «prueba automatizada de reglas de invitación en `tests/`» y el README «comandos de prueba», pero no hay carpeta `tests/` ni archivo de test (solo `docs/requirements.txt` con pytest). |
| Estructura de paquetes correspondiente al estilo del ADR | `git ls-tree -r --name-only c38adfb94` | No cumple | El ADR y §4.4 definen `src/{eventos,invitaciones,tareas,agenda,presupuesto,panel,compartido}` + `app/` de Next.js, y ninguna de esas rutas existe: el único código es `docs/Esqueleto.py` (monolito de un archivo) y `docs/main.py` con import roto. |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clon anónimo OK de `ISCOUTB/AS_202620_EnAgenda` | Cumple | Público y con el nombre de la convención. |
| Estructura mínima presente | `git ls-tree -r --name-only c38adfb94` | Cumple | Las seis rutas existen, con desviaciones de nombre (espacios antes de `.md`: `aspectos .md`, `ia .md`, arc42, adr, matriz). |
| Estado calificado identificable | `c38adfb94` · 2026-08-23T23:49:01-05:00 | Cumple | Sin etiqueta; se registra hash+fecha del último commit anterior al cierre. |
| Nombres de ADR según la convención | `ls docs/adr` | No cumple | `0001-app-movil-y-web-de-invitaciones .md` con espacio: el filtro da salida. |
| ADR aceptados no reescritos | `git log -- docs/adr/...`: contenido reemplazado en `c38adfb` | Cumple | El ADR anterior estaba «propuesto» (no aceptado), así que su reemplazo no viola la regla de aceptados; pero se hizo en el mismo archivo, dejando un nombre que ya no corresponde al contenido (anotado en la fila de nombres). |
| `docs/ia.md` al día para la semana | `git log -- docs/ia .md`: último commit `6ff7f9a` 2026-08-17 (dentro de S3) | Cumple | Entradas del 07, 08, 15 y 17 de agosto con rechazos y motivos; sin cambios nuevos en el tramo final de S3. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de secretos (exit 1), sin `.env` versionado | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | commits en S3: Daoisttl0FB3 (4), Jein-12 (5), eliabarnedocondef10-gif (0) | No cumple | Eliab Josue Arnedo Conde no firma commits en el periodo S3 (último: `45ab58e` 2026-08-16, S2). 2 de 3 integrantes. |

## Recuento

**3 de 9** criterios de la ficha cumplidos. La nota la fija el profesor (sin rúbrica publicada).

## No verificado / pendientes

- Nada quedó No verificado: toda la evidencia se pudo leer desde el commit calificado.
- Ejecución real del arranque: no aplica (no hay comando documentado; además `docs/main.py` importa un módulo inexistente).
- Sin llamada a la API de actions: el repositorio no tiene `.github/workflows/`.

## Hallazgos para la planilla

- Gran recuperación de la documentación: §4 completa con estrategia elegida, ADR de estilo aceptado con alternativas y consecuencias, matriz propia y `aspectos.md` ya con tabla de 8 columnas.
- El esqueleto ejecutable prometido no existe: el ADR promete `src/` con 6 módulos y pruebas en `tests/`, y en el repositorio solo hay `docs/Esqueleto.py` (script demo monolítico), `docs/main.py` con un import roto (`app.eventos.factory` no existe) y README sin comando de arranque ni de prueba.
- El ADR quedó con el nombre viejo (`0001-app-movil-y-web-de-invitaciones .md`, con espacio) y sus enlaces internos apuntan a `0001-usar-monolito-modular.md`, que no existe; §4.5 enlaza la matriz sin el espacio real del nombre.
- La matriz comparativa no referencia los escenarios EC-01…EC-05 del árbol de utilidad.
- La columna ADR de `aspectos.md` sigue «Pendiente» y `10-requisitos-de-calidad .md` no enlaza al ADR.
- Eliab sin commits en S3 (contribución del periodo: 2 de 3).
- Sin commits tardíos: todo lo empujado entró antes del cierre.
