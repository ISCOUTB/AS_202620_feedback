# Evidencia S3 · DinamikUTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `fe52ab594` · 2026-08-23T23:20:33-05:00 (último commit ≤ cierre 2026-08-24T05:00:00Z) |
| Fecha/hora de revisión | 2026-08-24, DESPUÉS del cierre. Revisión actualizada tras el cierre: el equipo empujó después de la primera revisión; hash calificado definitivo |
| Primera revisión | `275560bb` · 2026-08-23T21:35:58-05:00 (quedó sin efecto; todo se recalifica sobre el hash definitivo) |
| Commits tardíos | ninguno: `git log --after='2026-08-24T05:00:00Z'` no devuelve commits |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until='2026-08-24T05:00:00Z'`; `git ls-tree`; `git show`; `git grep` de secretos (exit 1). Sin API de actions: no hay `.github/workflows/` |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/04-solution-strategy.md` | No cumple | La estrategia elegida (monolito modular, §4.5) está justificada para el proyecto, pero la sección no nombra tácticas concretas contra Q-01/Q-02/Q-03: §4.8 relaciona atributos a nivel declarativo, sin tácticas (p. ej. validación de consistencia, control de acceso). Sin cambios respecto de la primera revisión (último commit al archivo: `0b066e1` 2026-08-23T03:57). |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/arc42/04-solution-strategy.md` §4.4 | No cumple | La matriz compara los tres estilos con puntaje 1–5 sobre criterios genéricos (simplicidad, organización, evolución, testabilidad…), no contra el árbol de utilidad: ningún escenario Q-xx aparece como fila, así que no se lee qué escenario mejora/empeora cada estilo. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-seleccion-monolito-modular.md` | Cumple | Nombre conforme a `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$`. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-seleccion-monolito-modular.md` | Cumple | Título enuncia la decisión; secciones 1 (contexto), 3 (alternativas), 4 (decisión), 5 (consecuencias) completas. |
| Alternativas descartadas con su motivo | ADR §3.1 y §3.2 | Cumple | Capas descartada por acoplamiento y dificultad de evolución; hexagonal por complejidad/boilerplate innecesaria para el alcance inicial. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` (tabla de 8 columnas, columna ADR) y `docs/arc42/10-quality-requirements.md` | No cumple | Mejoró: `aspectos.md` ahora usa la tabla de 8 columnas y enlaza los escenarios Q-01/Q-02/Q-03, pero la columna ADR sigue en «Pendiente» en las 6 filas, y la nota final dice que los campos están pendientes «porque todavía no existen los elementos correspondientes» — el ADR 0001 sí existe. El escenario Q-01 tampoco enlaza al ADR. |
| Arranque con un solo comando documentado en el README | `README.md:188` (§Ejecución del Proyecto) + `start.bat` (raíz) | Cumple | El README documenta el comando único `start.bat` con requisitos previos y qué hace (backend FastAPI + frontend Flutter en Chrome); `start.bat` existe en la raíz. Ejecución real: No verificado (regla del kit: no se ejecuta código del estudiante). |
| Prueba automatizada en verde | `backend/tests/test_main.py` y `frontend/test/widget_test.dart` | No verificado | Las pruebas existen y el README documenta `pytest`/`flutter test`, pero no hay `.github/workflows/` ni run de CI; sin evidencia de ejecución aportada no se puede comprobar el «verde». |
| Estructura de paquetes correspondiente al estilo del ADR | `backend/app/{core,usuarios,estudiantes,requisitos,programas,ayuda}/__init__.py`; `frontend/lib/` con los mismos módulos | Cumple | Los módulos con paquetes vacíos coinciden con la estructura del ADR §6 (monolito modular con fronteras declaradas). |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clon anónimo OK de `ISCOUTB/AS_202620_DinamikUTB` | Cumple | Público y con el nombre de la convención. |
| Estructura mínima presente | `git ls-tree -r --name-only fe52ab594` | Cumple | Las seis rutas existen (arc42 con 12 secciones, c4 con contexto.puml/png, adr, aspectos.md, ia.md, README). |
| Estado calificado identificable | `fe52ab594` · 2026-08-23T23:20:33-05:00 | Cumple | Sin etiqueta; se registra hash+fecha del último commit anterior al cierre. |
| Nombres de ADR según la convención | `ls docs/adr` | Cumple | `0001-seleccion-monolito-modular.md` conforme. |
| ADR aceptados no reescritos | `git log --follow -- docs/adr/...`: creado `3d5aad8` 2026-08-23T04:00, iterado hasta `9fbed1f` 04:48 del mismo día | Cumple | Iterado el mismo día de creación, antes de la entrega; sin reescrituras posteriores. |
| `docs/ia.md` al día para la semana | commits `cc87ba7`/`0fbdbf7`/`2c78be9`/`fe52ab5` del 23-ago; entradas del 23/08 con «Rechazado parcialmente» y motivo | Cumple | Registro del periodo S3 con qué se rechazó y por qué (sobrecarga visual), aceptaciones validadas y herramienta por uso. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de secretos (exit 1), sin `.env` versionado | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | commits en S3: JuanchisV (20) + «Juan José Vargas Pérez» (1, mismo correo) = 21; gillianisperez-prog (11); Daniel-dev02 (11) + «LUIS DANIEL» (1, mismo correo) = 12; Eramirezr (2) | Cumple | Los 4 integrantes firman commits en S3. Esteban reapareció (`2c78be9` estructura del proyecto, `fe52ab5` ia.md): cerrado el hallazgo de S1/S2. Sigue el desbalance (JuanchisV concentra 21 de 46). |

## Recuento

**5 de 9** criterios de la ficha cumplidos (1 No verificado). La nota la fija el profesor (sin rúbrica publicada).

## No verificado / pendientes

- Prueba en verde: no verificable sin pipeline ni evidencia de ejecución (ver fila de la matriz).
- Ejecución real del arranque: No verificado por regla del kit (comando declarado: `start.bat`).

## Hallazgos para la planilla

- La matriz de estilos usa criterios genéricos con puntaje 1–5 y no compara contra el árbol de utilidad (ningún escenario Q-xx).
- La sección 4 no nombra tácticas contra los escenarios priorizados.
- `docs/aspectos.md` ya tiene la tabla de 8 columnas y enlaza los escenarios, pero la columna ADR sigue en «Pendiente» y su nota afirma que los elementos «todavía no existen»: el ADR 0001 sí existe y no es alcanzable desde allí ni desde Q-01.
- Contribución resuelta: los 4 integrantes firman commits en S3 (Esteban con 2). Queda el desbalance de concentración (JuanchisV 21 de 46).
- `docs/ia.md` con rechazos y motivo: cerrado el hallazgo arrastrado.
- Sin commits tardíos: todo lo empujado entró antes del cierre.
