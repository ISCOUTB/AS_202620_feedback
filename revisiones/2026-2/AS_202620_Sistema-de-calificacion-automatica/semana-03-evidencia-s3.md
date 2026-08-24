# Evidencia S3 · Calificación automática

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `dd422fb202214b3d00c569ce58387660ae2a405d` · 2026-08-23T23:52:23-05:00 (`docs: subir la ficha del problema actualizada al alcance OMR`) |
| Fecha/hora de revisión | 2026-08-24 (posterior al cierre 2026-08-24T05:00:00Z) |
| Revisión actualizada tras el cierre | el equipo empujó después de la primera revisión (que vio `b65626e`); hash calificado definitivo `dd422fb`, último commit ≤ cierre. **Hay 2 commits tardíos posteriores al cierre** (ver hallazgos). |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until=2026-08-24T05:00:00Z`; `git ls-tree`; `git show`; `git grep`. Sin API de CI (no hay `.github/workflows/` al cierre). |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42-template-ES.md` §4.1 (matriz por escenario) y §4.2 (tácticas frente a los escenarios priorizados con su registro) | Cumple | §4.2 lista tácticas concretas: cola y workers para EC-04 (aritmética 200×5 s > 10 min), umbral de confianza con revisión manual, validación SymPy obligatoria, separación autoría/calificación, auditoría; cada una con motivación y enlace a su ADR. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | §4.1 tabla capas / hexagonal / monolito modular (+asíncrono) × EC-01…EC-07 + mantenibilidad + coste de montaje, con «mejora/empeora/neutro» por celda | Cumple | Compara contra los escenarios del equipo, celda por celda, con lectura de la matriz. Matiz: la tercera columna es «monolito modular + asíncrono» (el estilo elegido con su táctica clave); la comparación sigue siendo por escenario y no genérica. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-usar-monolito-modular.md`, `0002-procesar-calificacion-de-forma-asincrona.md`, `0003-usar-fastapi-y-flutter.md` | Cumple | Los tres pasan el filtro; títulos que enuncian la decisión. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | 0001 (reemplazado), 0002 y 0003 con contexto, opciones, decisión motivada y consecuencias | Cumple | 0002 corrige premisas falsas de 0001 sin reescribirlo (lo marca reemplazado); 0003 justifica FastAPI (SymPy solo existe en Python) y Flutter (experiencia del equipo) contra RNF-08. |
| Alternativas descartadas con su motivo | 0001: capas, microservicios y hexagonal con «Por qué no se eligió»; 0003: NestJS/Next.js descartadas con motivo | Cumple | Motivos concretos ligados a restricciones y escenarios. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` (tabla de trazabilidad: A-01/A-03 → 0002, A-04 → 0003); EC-04 en `arc42-template-ES.md:437` con `[ADR-0002](../adr/0002-…)` como hipervínculo; EC-05 → 0003 | Cumple | Los dos lados resueltos en esta actualización: la fila del aspecto enlaza y el escenario motivador EC-04 ya tiene hipervínculo (antes era texto plano). |
| Arranque con un solo comando documentado en el README | sin código en `dd422fb`; el README al cierre aún lista «[ ] Código» y «[ ] Elección de stack» | No cumple | Al cierre no hay comando ni archivo que lo soporte. El esqueleto y el README actualizado entraron **después del cierre** (`88294cc` 01:00, `e976c92` 01:58 -05:00) y no cuentan para S3. |
| Prueba automatizada en verde | sin carpeta de pruebas ni `.github/workflows/` en `dd422fb` | No cumple | No existía al cierre; la prueba llegó con el esqueleto tardío. |
| Estructura de paquetes correspondiente al estilo del ADR | sin código en `dd422fb` (solo `README.md` y `docs/`) | No cumple | Los 7 módulos del ADR-0002 no existían al cierre; entraron en el commit tardío `e976c92`. |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, nombre de convención y público | Cumple | clon sin autenticación de `github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica`. |
| Estructura mínima presente | Cumple | Las seis rutas en `dd422fb`; además se sumó `docs/Ficha-problema.md` (arrastre de S1 resuelto). |
| Estado calificado identificable | Cumple | Sin etiquetas; hash `dd422fb` `2026-08-23T23:52:23-05:00`, último ≤ cierre. 2 commits posteriores al cierre registrados como tardíos. |
| Nombres de ADR según la convención | Cumple | Los tres pasan el filtro. |
| ADR aceptados no reescritos | Cumple | 0001 marcado como reemplazado por 0002; 0003 nuevo (mismo día, antes del cierre); sin reescrituras de contenido posteriores a la aceptación. |
| `docs/ia.md` al día para la semana | Cumple | Último commit `aa14dca` (2026-08-23) con entradas de S3 y lo aceptado/rechazado con justificación. |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias (exit 1); sin `.env` versionado. |
| Contribución de todos los integrantes | Cumple | 4 cuentas para 4 integrantes en HEAD: scp1109 27 · josueacademico17-source 9 · SusanaRosales 3 · Mariadelmar-restrepo 1. |

## Recuento

**6 de 9** criterios cumplidos.

## No verificado / pendientes

- Arranque y prueba: al cierre no existía código que ejecutar; el esqueleto y la prueba entraron después del cierre y se evaluarán en S4 (pendiente también el run en verde).

## Hallazgos para la planilla

- La actualización cierra los huecos de documentación que quedaban: matriz por escenario contra el árbol (§4.1), enlace del ADR desde EC-04 y EC-05, `aspectos.md` como tabla de trazabilidad ADD con enlaces, ADR-0003 (stack) y la ficha del problema subida al repo (`docs/Ficha-problema.md`).
- **2 commits tardíos posteriores al cierre**: `88294cc` (2026-08-24T01:00:51-05:00, README con el stack) y `e976c92` (2026-08-24T01:58:18-05:00, esqueleto ejecutable OMR). El esqueleto completo llegó ~2 h después del cierre y **no cuenta para S3**; queda como base para S4, donde debe venir con run en verde.
- El patrón se repite: la primera revisión ya advertía que el ADR-0001 prometía «paquetes vacíos y prueba en verde» para S3 y no se cumplió al cierre.
- Sin commits adicionales al cierre que afecten la matriz.
