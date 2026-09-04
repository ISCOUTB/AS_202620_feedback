# Evidencia S3 · InvenTrack

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `dd4ea1cb8` · 2026-08-23T23:46:24-05:00 (último commit ≤ cierre 2026-08-24T05:00:00Z) |
| Fecha/hora de revisión | 2026-08-24, DESPUÉS del cierre. Revisión actualizada tras el cierre: el equipo empujó después de la primera revisión; hash calificado definitivo |
| Primera revisión | `6a5d0c4c` · 2026-08-23T19:03:12-05:00 (quedó sin efecto; todo se recalifica sobre el hash definitivo) |
| Commits tardíos | ninguno: `git log --after='2026-08-24T05:00:00Z'` no devuelve commits |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until='2026-08-24T05:00:00Z'`; `git ls-tree`; `git show`; `git grep` de secretos (exit 1); API de actions (1 llamada): `runs?per_page=5` |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42-template-EN.md:183-233` (Solution Strategy) | Cumple | Estrategia (monolito modular + hexagonal por módulo) con respuesta por objetivo de calidad (consistencia, mantenibilidad, seguridad, rendimiento, disponibilidad); no es descripción abstracta del estilo. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/matriz-comparativa-estilos.md` (tabla «Evaluación frente a InvenTrack») | Cumple | Fila por escenario del equipo (ESC-01…ESC-05) y restricciones (C1, C4, C5), con qué mejora/empeora por estilo; la tabla genérica de arriba está acompañada de la comparación propia. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md` | Cumple | Pasa el filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$`. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md` (Contexto:8-16, Alternativas:18-31, Decisión:33-51, Consecuencias:53-74) | Cumple | Nombre del archivo enuncia la decisión («usar…»); observaciones: estado «Propuesto, pendiente de ratificación del equipo» (no «aceptado») y el título H1 no lleva verbo de decisión. |
| Alternativas descartadas con su motivo | ADR:18-31 + `docs/matriz-comparativa-estilos.md` («Las alternativas se descartan por estas razones») | Cumple | Capas, hexagonal puro y microservicios descartados con motivo en el ADR y en la matriz. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md:28` (fila ASP-01, columna ADR) y `docs/arc42/arc42-template-EN.md:374` (ESC-01) | Cumple | Corregido desde la primera revisión: la fila ASP-01 enlaza `[ADR-0001](adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md)` y el escenario ESC-01 cierra con «Este escenario motivó la decisión de estructura en ADR-0001». Ambos enlaces navegables. |
| Arranque con un solo comando documentado en el README | `README.md:210-220` + `requirements.txt` | Cumple | Documenta `python -m pip install -r requirements.txt` y `python -m uvicorn app.main:app --reload` (con requisitos previos declarados y `GET /health` como comprobación). Ejecución real: No verificado (regla del kit: no se ejecuta código del estudiante). |
| Prueba automatizada en verde | `tests/test_health.py` + `.github/workflows/test.yml` (creado en `3e2a54b`) | Cumple | Run de CI en verde sobre el hash calificado: «Run Tests» success en `dd4ea1cb` — https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/32691253620 (2026-08-24T04:46Z). El primer intento falló (`3e2a54b`) y lo corrigieron con `93f4b00` (PYTHONPATH). |
| Estructura de paquetes correspondiente al estilo del ADR | `app/{productos,proveedores,inventario,usuarios,alertas}/{domain,application,infrastructure}` + `app/shared/` + `app/main.py` | Cumple | Módulos con frontera declarada y hexagonal interno por módulo, coherente con el ADR (paquetes vacíos, como pide el esqueleto). |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clon anónimo OK de `ISCOUTB/AS_202620_InvenTrack` | Cumple | Público y con el nombre de la convención. |
| Estructura mínima presente | `git ls-tree -r --name-only dd4ea1cb8` | Cumple | Las seis rutas existen (arc42 en `docs/arc42/arc42-template-EN.md`, con contenido propio). |
| Estado calificado identificable | `dd4ea1cb8` · 2026-08-23T23:46:24-05:00 | Cumple | Sin etiqueta; se registra hash+fecha del último commit anterior al cierre. |
| Nombres de ADR según la convención | `ls docs/adr` | Cumple | `0001-usar-monolito-modular-con-hexagonal-por-modulo.md` conforme; el placeholder `README.md` se eliminó en `2abab34`. |
| ADR aceptados no reescritos | `git log --follow -- docs/adr/...` | Cumple | El ADR está «propuesto» (no aceptado), así que el churn del 23-ago (borrado `1375411` y restauración por merge `6a5d0c4`, mismo contenido) no viola la regla de aceptados; queda anotado. |
| `docs/ia.md` al día para la semana | `docs/ia.md` (tabla con columna «Rechazado / motivo») | Cumple | Corregido desde la primera revisión: la entrada S3 (22-ago) ahora registra qué se rechazó y por qué (estructuras y ADR genéricos rechazados hasta evaluarlos contra ESC-01…ESC-05). |
| Sin credenciales en el repositorio ni en el historial | `git grep` de secretos (exit 1), sin `.env` versionado | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | commits en S3: Josephva24+«Jose Vargas» (mismo correo `[correo omitido]`) 6; Esteban Peluffo 3; FlexT21+«Felix Taborda» (mismo noreply) 1; jxviercarta-a11y 3 | Cumple | 4 identidades consolidadas de 4 integrantes. Apareció `jxviercarta-a11y` (3 commits en S3), cuenta atribuible a Javier Carta Lacharme — atribución por confirmar con el docente. |

## Recuento

**9 de 9** criterios de la ficha cumplidos. La nota la fija el profesor (sin rúbrica publicada).

## No verificado / pendientes

- Ejecución real del arranque: No verificado por regla del kit (comando declarado: `python -m uvicorn app.main:app --reload`).
- Atribución de `jxviercarta-a11y` a Javier Carta Lacharme: por confirmar con el docente.

## Hallazgos para la planilla

- Cerraron los huecos de la primera revisión: enlaces del ADR desde `aspectos.md` y desde ESC-01, `ia.md` con la columna de rechazos llena, workflow de CI añadido y **en verde sobre el hash calificado** (run `32691253620`, success en `dd4ea1cb`).
- Apareció en el historial `jxviercarta-a11y` (3 commits en S3), cuenta atribuible a Javier Carta: contribución 4 de 4.
- Sigue abierto: el ADR 0001 está «propuesto, pendiente de ratificación» (no aceptado) y su título H1 no enuncia la decisión.
- Sin commits tardíos: todo lo empujado entró antes del cierre.
