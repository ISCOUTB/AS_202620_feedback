> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · ShareU

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `39508608eae4c1a56a5e4fc11a055bf6afb2c003` en `origin/master` (2026-09-28T19:56:57-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

Esta pasada **no tiene corte**: se califica la punta actual del 2026-09-28, no un commit anterior a un
cierre. El periodo S9 (`332f67f..origin/master`, con `332f67f` el hash de S8) contiene cuatro commits
(`21256e5`, `0e14454`, `c552056`, `3950860`): la evidencia S9 (`docs/evidencia/evidencia-s9.md`), los
ADR-0008 y ADR-0009, la fachada `app/administracion/service.py`, tres pruebas nuevas y la corrección
del cruce de frontera detectado por la auditoría de erosión. La porción de la cadena incluye código del
propio periodo (la fachada y su consumo), aunque la métrica de origen sea de S8. La fila de credenciales
y la matriz transversal se deciden sobre el estado en la punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | `app/administracion/service.py` (nuevo en `3950860`, interfaz pública de administración), `app/busqueda/service.py` (modificado en `3950860` para consumir la fachada), `tests/test_fronteras.py`, `tests/test_metricas.py`, `tests/test_escenario_usabilidad.py`. `docs/ia/ia.md` fila 9 atribuye a IA la redacción de la fachada y las pruebas. | Cumple | La corrección de frontera es una porción real del sistema construida en el periodo con apoyo de IA. La métrica de origen es de S8 (`332f67f`); lo que el periodo aporta es la fachada, su consumo y las pruebas. |
| Cadena completa navegable para esa porción | `docs/evidencia/evidencia-s9.md` §1: aspecto (fila nueva en `docs/aspectos/aspectos.md`) → ADR-0008 → `app/administracion/service.py`, `app/busqueda/service.py` → `tests/test_metricas.py`, `test_fronteras.py`, `test_escenario_usabilidad.py` → medición (§3). Todas las rutas existen en la punta. | Cumple | La fila nueva de la tabla de aspectos llega al código, las pruebas y la evidencia; la cadena no se rompe. |
| ADR con la decisión argumentada por el equipo | `docs/adr/0008-metrica-tras-interfaz-de-administracion.md` compara cuatro alternativas (dejar el import, middleware, SQLite, fachada) contra las restricciones del proyecto: costo USD 0, sin disco persistente, ADR-0001 y equipo pequeño; incluye criterio de reapertura y trazabilidad. | Cumple | La decisión la argumenta el equipo con las restricciones del proyecto, no la herramienta. El ADR está en estado «Propuesto» (pendiente de aprobación formal del equipo). |
| Prueba que falla ante el defecto que cubre | `docs/evidencia/evidencia-s9.md` §2 documenta tres defectos introducidos a propósito y la prueba que falla en cada caso: `test_fronteras.py` (`AssertionError: ['busqueda/se…ion.metricas'] == []`), `test_metricas.py` (2 fallos al invertir la condición) y `test_escenario_usabilidad.py` (`assert 6 <= 3`); estado final `pytest -q` 12 passed. | Cumple | Procedimiento documentado con el defecto, la prueba y el mensaje de fallo; cada defecto se revirtió. El CI del hash revisado está en rojo (ver matriz transversal), lo que no permite confirmar desde el pipeline el «12 passed» local. |
| Medición del escenario asociado | `docs/evidencia/evidencia-s9.md` §3: interacciones mínimas (campos llenados + clic) para encontrar cada documento; máximo 2 frente al umbral ≤ 3, sobre cinco documentos de ejemplo. | Cumple | Resultado contrastado con el umbral; se declara como indicador técnico sobre datos de ejemplo, no como prueba con estudiantes. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | `docs/ia/ia.md` fila 9 (agregada en `3950860`) registra lo rechazado con motivo (dejar el import cruzado, middleware, SQLite, componente generativo), lo corregido (el marcador sin resolver de la fila 8) y lo aceptado (la fachada y la guardia de fronteras). | Cumple | Extracto del periodo con aceptado, corregido y rechazo motivado; el archivo vive en `docs/ia/ia.md` y se evalúa donde está. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | `docs/evidencia/evidencia-s9.md` §5: barrido de escrituras y de imports; hallazgos E1–E4 con ubicación y corrección. E1 (cruce `busqueda` → `administracion.metricas`) se corrigió con la fachada y la guardia `test_fronteras.py`; E2 (propiedad de datos) se actualizó. E3 y E4 quedan declarados como pendientes. | Cumple | Auditoría real con hallazgo, ubicación y corrección sobre el código; los pendientes E3/E4 se registran como hallazgo. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 (`332f67f`) sobre `requirements.txt`, `app/frontend/package.json` y su lock está vacío: no hay dependencias añadidas en el periodo. La verificación de `pyyaml`, `jsonschema` y los paquetes de Next.js que cita la evidencia corresponde a commits anteriores (`0c2b53a`, ancestro de S8). | No cumple | No hay dependencias añadidas en el periodo S9 que verificar; la verificación citada es de línea base (CONTRATO §12). Se registra además el hallazgo del equipo: `next@14.2.15` está marcado como vulnerable y la corrección propuesta es subir a 14.2.35. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta sin coincidencias; sin `.env` versionado; `app/frontend/.env.example` contiene solo una URL local; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. Las únicas menciones son `secrets.GITHUB_TOKEN` y `secrets.SONAR_TOKEN` en el workflow. | Cumple | Sin credenciales reales del equipo en la punta ni en el historial. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | `docs/adr/0009-no-incorporar-componente-generativo.md` decide no incorporarlo y argumenta con costo USD 0/sin tarjeta, latencia y disponibilidad del flujo de búsqueda, y simplicidad; incluye criterio de reapertura. | Cumple | Existe el ADR de no incorporarlo, exigido por la ficha. El ADR está en estado «Propuesto» (pendiente de aprobación formal del equipo). |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_ShareU`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre `AS_202620_ShareU` conforme y visibilidad pública. |
| Estructura mínima presente | En `3950860`: `README.md`, `docs/arc42/arc42.md`, `docs/adr/`, `docs/c4/`; `docs/aspectos/aspectos.md` y `docs/ia/ia.md` viven en subcarpetas propias, no en las rutas contractuales. | No cumple | Los artefactos existen (desviación, no ausencia), pero `docs/aspectos.md` y `docs/ia.md` no están en la ruta mínima del contrato §2. |
| Estado calificado identificable | `39508608eae4c1a56a5e4fc11a055bf6afb2c003` en `origin/master`, commit del 2026-09-28T19:56:57-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. |
| Nombres de ADR según la convención | `docs/adr/` contiene `0001`–`0004`, `0008` y `0009` con `NNNN-kebab-case.md`, más `ShareU_Trazabilida.pdf`, que no cumple la convención. | No cumple | El PDF ajeno a la convención sigue presente en el estado calificado. |
| ADR aceptados no reescritos | `git log --follow`: ADR-0008 y ADR-0009 tienen un único commit cada uno (`3950860`); los ADR 0001–0004 no registran ediciones en el periodo. | Cumple | Ninguna decisión aceptada se reescribe en el periodo; ADR-0001 conserva su contenido de línea base. |
| `docs/ia.md` al día para la semana | `docs/ia/ia.md` suma la fila 9 en `3950860`, dentro del periodo revisado, con lo aceptado, lo corregido y lo rechazado con motivo. | Cumple | El archivo está en la ruta desviada `docs/ia/ia.md`; se evalúa donde está. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Único run del hash revisado: [Tests 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458), conclusión `failure`. Existe `sonar-project.properties` y el workflow invoca `SonarSource/sonarcloud-github-action`, pero el run está en rojo. | No cumple | El pipeline de la rama principal en el hash revisado falla; sin run exitoso no se puede acreditar el Quality Gate público exigido por el contrato §8. |
| Sin credenciales en el repositorio ni en el historial | `git grep` del contrato y `git log -S'BEGIN PRIVATE KEY'` sin coincidencias; sin `.env` versionado. | Cumple | El repositorio no expone credenciales. |
| Contribución de todos los integrantes | `git shortlog -sne 3950860`: `Nicolas-HH` 14; `Dayana` 13 más `daynarvaez` 7 (mismo correo, consolidado); `luiscorredor` 11; `steven` 5. | Cumple | Cuatro personas para cuatro integrantes; la contribución está repartida. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `39508608eae4c1a56a5e4fc11a055bf6afb2c003 2026-09-28T19:56:57-05:00 semana 9` (`origin/master`)
- **Veredicto**: evidencia S9 sólida y bien trazada; el pipeline en rojo impide cerrar la semana
- Resumen: el equipo respondió a la auditoría de erosión con una corrección real: detectó que un módulo
  importaba un archivo interno de otro, lo reemplazó por una fachada de servicio y añadió una prueba que
  falla si vuelve a ocurrir. La cadena del aspecto nuevo es navegable hasta el código, las pruebas y la
  medición, y los ADR-0008 y ADR-0009 argumentan la decisión con las restricciones del proyecto. La
  prueba de mutación está documentada con el defecto, la prueba y el mensaje de fallo. El punto que
  impide cerrar la semana es el pipeline: el run del hash revisado está en rojo, aunque la evidencia
  afirme 12 pruebas en verde en local. Quedan además las desviaciones de estructura (aspectos e IA fuera
  de la ruta contractual), el PDF fuera de convención en `docs/adr/`, y los pendientes E3/E4 de la propia
  auditoría (referencias a archivos inexistentes y marcadores sin resolver). El periodo no añadió
  dependencias, así que la fila de verificación de dependencias no se satisface.

Pendientes que siguen abiertos:
- Pipeline de `master` en rojo en el hash revisado (`36505758458`, failure); sin run exitoso no hay Quality Gate acreditable.
- `docs/aspectos.md` y `docs/ia.md` fuera de la ruta mínima.
- `docs/adr/ShareU_Trazabilida.pdf` fuera de la convención de nombres.
- E3/E4 de la auditoría: README y arc42 citan `Dockerfile`, `render.yaml`, ADR 0005–0007 y `tests/test_contrato.py` que no están en el árbol; marcadores `<URL Render>`, `<URL Vercel>`, `<integrante>` y `<URL del run>` sin resolver.
- Sin dependencias añadidas en el periodo que verificar.
- ADR-0008 y ADR-0009 en estado «Propuesto», pendientes de aprobación formal del equipo.

## Recuento y nota sugerida

**9 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.6 = 1 + 4 × (9/10).** La nota final la fija el profesor en Moodle.

La fila 8 no se satisface porque el periodo S9 no añadió dependencias que verificar contra los registros
oficiales (CONTRATO §12).

## No verificado / pendientes

- Nada quedó en **No verificado** en la ficha: todas las comprobaciones se resolvieron sobre archivos
  legibles del repositorio.
- El CI del hash revisado está en rojo; no se pudo confirmar desde el pipeline el «12 passed» que
  reporta la evidencia. No se ejecutó el código (fuera del alcance de la revisión).
- Dependencias del periodo: el diff contra S8 está vacío; no hay nada que comprobar en los registros.

## Hallazgos para la planilla

- El periodo S9 corrige un cruce de frontera real: `app/busqueda/service.py` importaba `administracion.metricas`; se reemplazó por la fachada `app/administracion/service.py` con la guardia `tests/test_fronteras.py`.
- La cadena de `docs/aspectos/aspectos.md` (fila nueva) llega a código, pruebas y medición; no se rompe.
- ADR-0008 (métrica tras interfaz de servicio) y ADR-0009 (no incorporar componente generativo) argumentan la decisión con las restricciones del proyecto; ambos en estado «Propuesto».
- Prueba de mutación documentada con tres defectos y sus mensajes de fallo; estado final declarado 12 passed.
- Medición del escenario de usabilidad: máximo 2 interacciones frente al umbral ≤ 3.
- Sin credenciales en la punta ni en el historial; cuatro integrantes contribuyen.
- CI del hash revisado en rojo (run 36505758458): fila transversal de pipeline/SonarCloud en No cumple.
- Desviaciones de estructura (aspectos e IA fuera de ruta) y PDF fuera de convención en `docs/adr/`.
- Sin dependencias añadidas en el periodo; la verificación de `pyyaml`/`jsonschema`/Next.js es de línea base.
- Hallazgo de seguridad del equipo: `next@14.2.15` marcado como vulnerable; corrección propuesta a 14.2.35.
