# Evidencia S3 · Drift

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `0d006bba` · 2026-08-23T18:05:58-05:00 (último commit ≤ cierre 2026-08-24T05:00:00Z) |
| Fecha/hora de revisión | 2026-08-23 22:08 (UTC-5), ANTES del cierre: si el equipo empuja antes de medianoche, el hash calificado puede cambiar |
| Comandos | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-24T05:00:00Z'`; `git ls-tree -r --name-only 0d006bba`; `git show 0d006bba:<ruta>`; sin llamada a la API (no hay `.github/workflows/`) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42_4_soluciones_arquitectonica.md` §4.1 | Cumple | Estrategia elegida (hexagonal) y tabla objetivo→escenario→estrategia: aislamiento núcleo/adaptadores para mantenibilidad, aislamiento de dependencias externas para el fallo de una fuente (E5), dobles de prueba (mocks/stubs) para testabilidad. No describe el estilo en abstracto. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/matriz.md` | No cumple | La matriz está hecha a medida de DRIFT (incorporar plataformas, cambiar API externa, aislamiento) pero ninguna fila referencia los escenarios E1–E5 ni las hojas del árbol de utilidad; no se lee qué escenario mejora/empeora cada estilo. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-arquitectura-base.md` | Cumple | Nombre conforme a la convención (renombrado desde `001estrategia.md` el mismo día, `8606140`). |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-arquitectura-base.md` | Cumple | Título enuncia la decisión; secciones Contexto, Alternativas Consideradas (3 opciones con ventajas/desventajas), Decisión y Consecuencias completas. |
| Alternativas descartadas con su motivo | ADR §Opción 1 y §Opción 2 | Cumple | Capas descartada por acoplamiento y lógica dependiente de infraestructura; monolito modular por dependencias entre módulos y no separar lógica de infraestructura. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `git grep -i 'adr' docs/aspectos.md docs/escenarios.md docs/arbol_utilidad.md` → sin coincidencias | No cumple | Ninguno de los dos enlaces existe: `docs/aspectos.md` (que además sigue en prosa, sin tabla de 8 columnas) no enlaza el ADR, y los escenarios de `docs/escenarios.md` tampoco. El ADR solo se enlaza desde el README. |
| Arranque con un solo comando documentado en el README | `README.md` (dos secciones de ejecución contradictorias) | No cumple | El README documenta `mvn spring-boot:run` (sin `pom.xml` en el repositorio) y más abajo `cd backend && uvicorn app.main:app --reload` (solo backend, sin comando para el frontend Next). No hay un comando único que arranque el sistema completo. |
| Prueba automatizada en verde | `backend/tests/test_health.py` | No verificado | La prueba existe (health contra `backend/app/main.py`), pero no hay `.github/workflows/` ni run de CI, y no se aportó evidencia de ejecución: el «verde» no se puede comprobar. Haría falta un pipeline o evidencia de ejecución entregada. |
| Estructura de paquetes correspondiente al estilo del ADR | `backend/app/domain/{model,ports}` · `backend/app/application/usecases` · `backend/app/infrastructure/{api,steam,epic,gog,persistence}` | Cumple | Separación dominio/puertos/adaptadores coherente con hexagonal. Observación: el ADR dibuja `src/main/java/com/drift` con carpeta `config`; el código real es Python en `backend/app/` sin `config`. |

Recuento: **5 de 9** criterios cumplidos.

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clon anónimo OK de `ISCOUTB/AS_202620_Drift` | Cumple | Público y con el nombre de la convención. |
| Estructura mínima presente | `git ls-tree -r --name-only 0d006bba` | Cumple | Las seis rutas existen (arc42, adr, c4, aspectos.md, ia.md, README). |
| Estado calificado identificable | `0d006bba` 2026-08-23T18:05:58-05:00 | Cumple | Sin etiqueta; se registra hash+fecha del último commit anterior al cierre. |
| Nombres de ADR según la convención | `ls docs/adr` | Cumple | `0001-arquitectura-base.md` conforme. |
| ADR aceptados no reescritos | `git log --follow -- docs/adr/...`: creado `ad6db68`, renombrado/iterado hasta `752dde2`, todo el 2026-08-23 | Cumple | Creado e iterado el mismo día de la entrega; sin reescrituras posteriores. |
| `docs/ia.md` al día para la semana | commits `083dffd`/`b6a4952` (2026-08-22), `8cb8e55` (08-21) | Cumple | Actualizado en el periodo S3; rechazo narrado en §3.1 con motivo (elementos que no eran restricciones). |
| Sin credenciales en el repositorio ni en el historial | `git grep` (exit 1), sin `.env` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | commits en S3: lmpdiaz12 (51), maufern4ndez (19), JoshuaR01 (18), JerryDBM (9) | Cumple | Los 4 integrantes firman commits en S3 (desbalance marcado: 51 vs 9). |

## Recuento

**5 de 9** criterios de la ficha cumplidos. La nota la fija el profesor (sin rúbrica publicada).

## No verificado / pendientes

- Prueba en verde: no verificable sin pipeline ni evidencia de ejecución (ver fila de la matriz).
- Ejecución real del arranque: no aplica, no hay comando único documentado; ejecución no verificada por regla del kit.
- Si el equipo empuja antes del cierre (2026-08-24T05:00:00Z), el hash calificado cambia.

## Hallazgos para la planilla

- README con dos formas de arranque contradictorias (`mvn spring-boot:run` sin pom.xml; `uvicorn` solo backend) y sin comando para el frontend.
- El ADR no es alcanzable desde `docs/aspectos.md` ni desde los escenarios (solo desde el README).
- `docs/aspectos.md` sigue en prosa, sin la tabla de 8 columnas (arrastrado desde S1).
- La matriz comparativa no referencia los escenarios E1–E5 del árbol de utilidad.
- Sin pipeline: la prueba existe pero el verde no está evidenciado.
- Desbalance de contribución que se arrastra (51 vs 9 commits en S3).
- Lo positivo: ADR completo y paquetes hexagonales coherentes con el ADR.
