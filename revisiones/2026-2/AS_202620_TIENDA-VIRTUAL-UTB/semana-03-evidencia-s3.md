# Evidencia S3 · Tienda virtual UTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `f4602a33a1030f42f90e0344fd0686f59bc4c0dd` · 2026-08-21T13:22:16-05:00 (último commit ≤ cierre 2026-08-24T05:00Z) |
| Fecha/hora de revisión | 2026-08-23T21:40-05:00 (ANTES del cierre) |
| Comandos | clon efímero con `--filter=blob:none --no-checkout`; lecturas con `git -C "$DIR" show "$HASH:…"`; sin ejecutar código del estudiante. API de GitHub usada 1 vez para el run. Si el equipo empuja antes de medianoche, el hash calificado puede cambiar. |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42-template-EN.md:111-155` | Cumple | «Solution Strategy» con tabla de decisiones fundamentales y «Relationship to quality goals» ligada a seguridad, usabilidad, rendimiento y disponibilidad. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/matriz-comparativa-arquitectura.md` | No cumple | Compara criterios genéricos (complejidad inicial, acoplamiento, curva de aprendizaje…), no los escenarios del árbol (`docs/arbol-utilidad.md`): no dice qué escenario mejora o empeora con cada estilo. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-monolito-modular.md` | Cumple | kebab-case correcto. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-monolito-modular.md` | Cumple | Título H1 enuncia la decisión; secciones Contexto, Alternativas consideradas, Decisión, Consecuencias. |
| Alternativas descartadas con su motivo | `docs/adr/0001-monolito-modular.md` («Alternativas consideradas») | Cumple | Capas y hexagonal evaluadas con ventaja/desventaja y motivo del descarte. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md`; `docs/escenarios-calidad.md` | No cumple | Ningún archivo menciona ni enlaza el ADR (`git grep -i adr` sin coincidencias). Sí se enlaza desde arc42 §4 y desde la matriz. |
| Arranque con un solo comando documentado en el README | `README.md` («docker compose up --build» desde la raíz); `compose.yaml` presente | Cumple | Ejecución real: **No verificado** (regla del kit); comando anotado. |
| Prueba automatizada en verde | `backend/tests/test_health.py`, `backend/tests/test_architecture.py`; `.github/workflows/tests.yml` | Cumple | Run en verde: https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/32514183233 («Pruebas», success, 2026-08-21T18:36Z, posterior al commit calificado). |
| Estructura de paquetes correspondiente al estilo del ADR | `backend/app/modules/{identity,catalog,inventory,orders}/__init__.py` + `backend/app/shared/__init__.py` | Cumple | Módulos por capacidad, coherentes con el monolito modular del ADR; `tests/test_architecture.py` comprueba la existencia de los paquetes. |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clonado sin autenticación. |
| Estructura mínima presente | Cumple | Seis rutas presentes en el hash calificado. |
| Estado calificado identificable | Cumple | `f4602a3` · 2026-08-21T13:22:16-05:00 ≤ cierre; sin etiqueta (evidencia semanal). |
| Nombres de ADR según la convención | Cumple | `0001-monolito-modular.md` pasa el filtro. |
| ADR aceptados no reescritos | Cumple | `git log --follow` → un solo commit (`f4602a3`), sin reescrituras. |
| `docs/ia.md` al día para la semana | No cumple | El commit del periodo (`f4602a3`) tocó el archivo, pero el contenido sigue con una sola entrada (08-09) sin columna de rechazados con motivo. |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias; sin `.env` versionado. Nota: `compose.yaml:7` lleva una contraseña de desarrollo para el Postgres local (solo entorno de demo). |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas: Jasen (2 firmas, mismo correo), RAZOR7150, pxtroniwnl, shalom-A26 = los 4 integrantes. |

## Recuento

**6 de 9** criterios de la ficha cumplidos. La nota la fija el profesor.

## No verificado / pendientes

- Ejecución real del arranque (`docker compose up --build`): no ejecutado por regla del kit.
- El «verde» de la prueba se comprobó con el run de la API; la ejecución local del equipo no se verificó.

## Hallazgos para la planilla

- Rehacer la matriz comparativa contra los escenarios del árbol de utilidad (qué escenario mejora/empeora por estilo); hoy es una tabla genérica.
- Enlazar el ADR desde `docs/aspectos.md` (que además sigue sin las 8 columnas del curso) y desde el escenario de calidad que lo motiva.
- `docs/ia.md`: registrar los usos de IA de S3 con lo aceptado y lo rechazado con motivo.
