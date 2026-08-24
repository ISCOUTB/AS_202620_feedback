# Evidencia S3 · Clubs UTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `5bf86ead1` · 2026-08-23T23:05:10-05:00 (último commit ≤ cierre 2026-08-24T05:00:00Z) |
| Fecha/hora de revisión | 2026-08-24, DESPUÉS del cierre. Revisión actualizada tras el cierre: el equipo empujó después de la primera revisión; hash calificado definitivo |
| Primera revisión | `2c316f44` · 2026-08-23T21:15:42-05:00 (quedó sin efecto; todo se recalifica sobre el hash definitivo) |
| Commits tardíos | 1: `8d69f62` · 2026-08-24T00:21:05-05:00 «Esqueleto ejecutable: arranque con uvicorn, test de health en verde» (21 min después del cierre) |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until='2026-08-24T05:00:00Z'`; `git log --after` para tardíos; `git ls-tree`; `git show`; `git grep` de secretos (exit 1). Sin API de actions: no hay `.github/workflows/` |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/04_estrategia_de_solucion.md` | Cumple | Estrategia elegida (hexagonal, §4.2) justificada contra la meta de disponibilidad y la restricción T4; §4.3 nombra tácticas por meta (timeout/reintento en adaptadores, caché e índices en persistencia) y enlaza matriz y ADR. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/arc42/matriz_comparativa_estilos.md` | Cumple | Fila por escenario del equipo (U1–U3, C1–C3 de la sección 10, IDs coinciden), con qué estilo mejora/empeora por escenario y conclusión. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-hexagonal.md` | Cumple | Nombre conforme al filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$`. Sigue el residuo `docs/adr/.temp` (no es ADR, conviene borrarlo). |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-hexagonal.md` | Cumple | Contexto, Alternativas, Decision y Consecuencias presentes, estado «Aceptado» (desde `2c316f4`). Observación: el título «Arquitectura hexagonal» nombra el tema y no la decisión; el CONTRATO pide «Usar arquitectura hexagonal». |
| Alternativas descartadas con su motivo | ADR §Alternativas | Cumple | Capas descartada por mezclar lógica de negocio e infraestructura; monolito modular por no aislar la lógica de las tecnologías externas. Motivos breves pero presentes. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `git grep -i adr` en `docs/aspectos.md` y `docs/arc42/10_requisitos_de_calidad.md`: sin coincidencias | No cumple | El ADR solo es alcanzable desde la sección 4 (`04_estrategia_de_solucion.md:16`) y la matriz. `aspectos.md` sigue en prosa sin enlace, y el escenario U2 (disponibilidad, que motiva la decisión) no lo enlaza. |
| Arranque con un solo comando documentado en el README | `README.md` §6 («En fase de planeación… No hay desarrollo de código activo») | No cumple | En el hash calificado el README no documenta ningún comando de arranque, `backend/src/main.py` está vacío y no existe `requirements.txt` (todo eso llegó en el commit tardío `8d69f62`, 21 min después del cierre). |
| Prueba automatizada en verde | `backend/tests/test_health.py` en el hash calificado | No cumple | El archivo existe pero está **vacío** en `5bf86ead1`: la prueba con `assert` llegó solo en el commit tardío. Sin `.github/workflows/` ni evidencia de ejecución. |
| Estructura de paquetes correspondiente al estilo del ADR | `backend/src/linkclub/{domain,application/{ports,use_cases},adapters/{inbound/api,outbound/persistence}}` | Cumple | Estructura hexagonal (dominio, aplicación con puertos y casos de uso, adaptadores de entrada/salida) creada en `5bf86ea` y coherente con la decisión del ADR; paquetes vacíos como pide el esqueleto. |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clon anónimo OK de `ISCOUTB/AS_202620_Clubs_UTB` | Cumple | Público y con el nombre de la convención. |
| Estructura mínima presente | `git ls-tree -r --name-only 5bf86ead1` | Cumple | Las seis rutas existen; `docs/C4/` en mayúscula es desviación de ruta (anotada desde S2), no ausencia. |
| Estado calificado identificable | `5bf86ead1` · 2026-08-23T23:05:10-05:00 | Cumple | Sin etiqueta; se registra hash+fecha del último commit anterior al cierre. |
| Nombres de ADR según la convención | `ls docs/adr` | Cumple | `0001-hexagonal.md` conforme; residual `docs/adr/.temp` fuera de convención pero no es un ADR. |
| ADR aceptados no reescritos | `git log --follow -- docs/adr/0001-hexagonal.md`: `75aff08` (en revisión) → `2c316f4` (Aceptado) | Cumple | Aceptado en `2c316f4`; sin commits de reescritura posteriores a la aceptación. |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md`: último commit `c92595e` 2026-08-09 | No cumple | Sin commits en S2 ni S3; sin registro de usos reales ni de rechazos. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de secretos (exit 1), sin `.env` versionado | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | commits en S3: Luis-Salas-Reyes (2), Zavod Dev (2), deortahollman-star (1), Josh Ortega (1, mismo correo `joshortega@utb.edu.co` que `Josh4OP`) | Cumple | Los 4 integrantes firman commits dentro del periodo S3, consolidando las dos identidades de Josh. |

## Recuento

**6 de 9** criterios de la ficha cumplidos. La nota la fija el profesor (sin rúbrica publicada).

## No verificado / pendientes

- Nada quedó No verificado: toda la evidencia se pudo leer desde el commit calificado.
- Ejecución real del arranque: no aplica al hash calificado (no hay comando ni archivo que lo soporte; ambos llegaron tardíos).
- Sin llamada a la API de actions: el repositorio no tiene `.github/workflows/`.

## Hallazgos para la planilla

- La documentación S3 está completa y en verde: sección 4 con tácticas, matriz por escenarios, ADR aceptado con alternativas y paquetes hexagonales coherentes.
- **Commit tardío** (`8d69f62`, 00:21 del 24-ago, 21 min después del cierre): ahí llegó el esqueleto ejecutable real — `main.py` con uvicorn, `test_health.py` con asserts, `requirements.txt`. En el hash calificado `main.py` y `test_health.py` están vacíos y el README no documenta comando de arranque: las filas de arranque y prueba quedaron No cumple por 21 minutos.
- El ADR sigue sin ser alcanzable desde `docs/aspectos.md` ni desde el escenario U2.
- `docs/aspectos.md` sigue en prosa sin la tabla de 8 columnas (arrastrado de S1).
- `docs/ia.md` sin commits desde el 2026-08-09 (arrastrado de S2).
- Residuo `docs/adr/.temp` pendiente de borrar.
