# Evidencia S3 · uniTeam

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `ca44917aad3aec690295ebf799631f804df1247e` · 2026-08-23T13:38:40-05:00 (último commit ≤ cierre 2026-08-24T05:00Z) |
| Fecha/hora de revisión | 2026-08-23T22:05-05:00 (ANTES del cierre) |
| Comandos | clon efímero con `--filter=blob:none --no-checkout`; lecturas con `git -C "$DIR" show "$HASH:…"`; sin ejecutar código del estudiante. Sin llamadas a la API (no hay `.github/workflows/`). Si el equipo empuja antes de medianoche, el hash calificado puede cambiar. |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42-uniteam.md:145-191` | Cumple | §4 con estilo, organización y tabla de tácticas por escenario (ESC-01…ESC-05). |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/c4/matriz-decision-adr-003.md` | Cumple | Compara capas/hexagonal/monolito modular contra ESC-01…ESC-05 del árbol con puntaje y justificación por escenario. Ubicada en `docs/c4/` (desviación de ubicación, no de contenido). |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/ADR-003-seleccion-estilo-arquitectonico (1).md` (y ADR-001, ADR-002) | No cumple | Prefijo «ADR-», y el del estilo lleva espacio y «(1)»: los tres fallan el filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$`. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/ADR-003-seleccion-estilo-arquitectonico (1).md` | Cumple | Contexto, alternativas (3 estilos), decisión (EDA, justificada por escenarios), tácticas y consecuencias positivas/negativas. |
| Alternativas descartadas con su motivo | `docs/adr/ADR-003-… (1).md` («Alternativas descartadas») | Cumple | Capas, hexagonal y monolito modular descartados como estilo principal, cada uno con su motivo. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md`; `docs/calidad/escenarios-calidad.md` | No cumple | `aspectos.md` enlaza escenarios y arc42 pero no el ADR; `escenarios-calidad.md` no enlaza el ADR-003 (solo interesados y árbol). |
| Arranque con un solo comando documentado en el README | `README.md` (118 líneas) | No cumple | El README documenta cómo correr la prueba (`pytest -v`) pero no el comando de arranque de la app; `app/main.py` existe sin referencia de arranque. Nota: `requirements.txt` trae `httpx2==2.12.0`, nombre que no corresponde a un paquete publicado (rompería el `pip install`). |
| Prueba automatizada en verde | `test/prueba_test.py` (test_health contra `/activo`) | No verificado | La prueba existe y el README declara «1 passed», pero no hay `.github/workflows/` ni evidencia de ejecución aportada: haría falta el run del pipeline o captura del `pytest`. |
| Estructura de paquetes correspondiente al estilo del ADR | `app/{api,application,domain,events,infrastructure}/` | Cumple | Coherente con la decisión EDA del ADR (paquete `events/` presente; capas de dominio/aplicación/infraestructura). |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clonado sin autenticación; `AS_202620_uniTeam`. |
| Estructura mínima presente | Cumple | Seis rutas presentes en el hash calificado. |
| Estado calificado identificable | Cumple | `ca44917` · 2026-08-23T13:38:40-05:00 ≤ cierre; sin etiqueta (evidencia semanal). |
| Nombres de ADR según la convención | No cumple | `ADR-00N-…` no pasan el filtro; el 003 lleva « (1)». |
| ADR aceptados no reescritos | Cumple | Un commit por ADR, sin reescrituras posteriores. Observación: ADR-001 (propuesta) y ADR-002 (aceptada) documentan la misma decisión y el 001 no queda marcado como reemplazado. |
| `docs/ia.md` al día para la semana | No cumple | Sin commits sobre el archivo en el periodo S3 (último: `da6055f`, 16-ago). |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias; sin `.env` versionado. |
| Contribución de todos los integrantes | No cumple | 3 identidades: super-gremlin (15), Ian Novoa (9), Julio Cesar Emiliani (2). Sin cuenta atribuible a Juan Jose Bustamante More ni a Daniel Isaac Manjarres Herrera. |

## Recuento

**5 de 9** criterios de la ficha cumplidos. La nota la fija el profesor.

## No verificado / pendientes

- Test en verde: sin CI y sin evidencia de ejecución (no se llama a la API: no hay workflows).
- Ejecución real del arranque: el README ni siquiera documenta el comando.

## Hallazgos para la planilla

- Renombrar los ADR (`NNNN-titulo-en-kebab-case.md`); quitar el « (1)» del ADR-003; marcar ADR-001 como reemplazado por ADR-002.
- Enlazar el ADR-003 desde `docs/aspectos.md` y desde ESC-03 (o el escenario que lo motiva) en `escenarios-calidad.md`.
- Documentar el comando único de arranque en el README (p. ej. `python -m uvicorn app.main:app --reload`) y corregir `httpx2` en `requirements.txt`.
- `docs/ia.md`: registrar el uso de IA de esta semana (ADR-003, matriz, esqueleto) con lo rechazado y su motivo.
- Contribución: solo Ian Novoa firmó los commits de S3; Bustamante y Manjarres siguen sin aparición.
