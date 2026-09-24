# semana-07-evidencia-s7 · Calificación automática

> Revisión definitiva corregida después del cierre. El informe preliminar había omitido 19 commits elegibles; esta versión evalúa el último commit de `origin/master` anterior al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `2269ca5` en `origin/master` (2026-09-20T21:48:00-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | revisión académica local sobre evidencia Git y GitHub Actions |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | `docs/contrato/openapi.json:199` declara OpenAPI 3.1.0; el archivo aparece en el historial en `661b3a1` (2026-09-20T17:29:30-05:00). | Cumple | Es un contrato ejecutable versionado, no una descripción en prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | `docs/contrato/openapi.json:3-195` define `components.schemas`; las rutas `/examenes/{examen_id}/hojas` y `/health` están en las líneas 201 y 251. | Cumple | Las operaciones enlazan esquemas tipados de petición y respuesta. |
| Correspondencia entre el contrato y la API implementada | `backend/api/main.py:69-74` implementa `/health` y `/examenes/{examen_id}/hojas`; ambas rutas están en `docs/contrato/openapi.json:201,251`. `backend/tests/test_contrato.py:129-145` compara el documento generado con el versionado. | Cumple | La igualdad automatizada comprueba la correspondencia en ambos sentidos. |
| Versión de la API declarada y con historial | `docs/contrato/openapi.json:197` declara `1.0.0`, alineada con `backend/api/esquemas.py:24` y `backend/api/main.py:30-35`; `git log -- docs/contrato/openapi.json` registra `661b3a1`. | Cumple | Versión e introducción del contrato quedan trazables en Git. |
| Prueba de contrato presente | `backend/tests/test_contrato.py:122-195` compara esquemas y rutas, verifica la versión y valida respuestas reales contra el contrato. | Cumple | La prueba cubre sincronización documental y cuerpos de respuesta. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/ci.yml:37-38` ejecuta `pytest -v tests/test_contrato.py`; el run del hash calificado terminó exitoso: https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/35555368047 | Cumple | La prueba tiene un paso propio antes de la suite completa. |
| Evidencia de que la prueba falla ante un cambio incompatible | `docs/evidencia/prueba-de-contrato-falla.md:17,88-89` documenta el cambio deliberado de `nombre_archivo` a `archivo`, el run rojo 35548751589 y el run verde 35549237474 tras revertir. | Cumple | La evidencia distingue el fallo contractual de un error de sintaxis y conserva los runs reproducibles. |
| ADR de la estrategia de integración ligado a un escenario | `docs/adr/0002-procesar-calificacion-de-forma-asincrona.md:6,100-201,250-282` liga la asincronía a EC-03 y EC-04, compara alternativas y registra consecuencias. | Cumple | La elección y el acoplamiento se justifican contra escenarios concretos. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/arc42-template-ES.md:356-440` describe el arranque, la sonda de salud y la carga de hojas con el recorrido por API, almacenamiento, bitácora y cola. | Cumple | Los flujos corresponden al incremento implementado. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/doc-c4.md:273-280` enumera las ocho relaciones del nivel 2 con HTTPS/JSON/multipart, SQL/PostgreSQL, llamadas en proceso con bytes, Redis/JSON y lectura de imagen. | Cumple | Todas las relaciones indican el protocolo o mecanismo y el formato intercambiado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica`, accesible por clonación sin autenticación. | Cumple | Nombre y organización coinciden con `EQUIPOS.md`. |
| Estructura mínima presente | El árbol de `2269ca5` contiene `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas exigidas están versionadas. |
| Estado calificado identificable | `origin/master`, `2269ca5`, 2026-09-20T21:48:00-05:00; es el último commit anterior al cierre. | Cumple | La punta actual coincide con el estado calificado. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md` a `0007-declarar-los-contextos-delimitados-y-la-regla-de-dueno-unico.md`. | Cumple | Numeración y nombres siguen `NNNN-kebab-case.md`. |
| ADR aceptados no reescritos | El historial conserva los ADR por decisión; el 0001 solo añade el estado de reemplazo por el 0002 en `9ca9257`. | Cumple | El reemplazo está declarado y el contenido de la decisión anterior permanece trazable. |
| `docs/ia.md` al día para la semana | `docs/ia.md:126-138` registra la actividad de S7, propuestas rechazadas y motivos técnicos; el último commit del archivo es `2269ca5`. | Cumple | Se documentan incluso evidencias descartadas por no probar la propiedad correcta. |
| Pipeline, SonarCloud y Quality Gate públicos | `.github/workflows/ci.yml` y el run exitoso 35555368047 verifican CI, pero el árbol no contiene configuración ni invocación de SonarCloud y no se publica una URL de análisis con Quality Gate. | No cumple | Faltan las tres evidencias de SonarCloud exigidas desde S6. |
| Sin credenciales en el repositorio ni en el historial | El árbol solo contiene `.env.example`; el barrido estático del hash no encontró credenciales en código propio. | Cumple | No hay `.env` versionado. |
| Contribución de todos los integrantes | `git shortlog -sne 2269ca5` produce cuatro grupos de identidad, pero `EQUIPOS.md` solo confirma dos cuentas para este repositorio. | No verificado | No se atribuyen las otras identidades por parecido de nombre; hace falta confirmar las cuentas. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `2269ca5a1fa1b64787745a55f4d714070192a8f0 2026-09-20T21:48:00-05:00 docs(ia): registrar el uso de IA de la semana 7`.
- **Veredicto**: entrega S7 completa; persiste una no conformidad transversal de SonarCloud.
- El contrato OpenAPI, su correspondencia con FastAPI, la prueba de contrato en CI, la demostración en rojo, el ADR, arc42 §6 y el C4 nivel 2 están presentes y trazables en la punta actual.

Pendientes que siguen abiertos:
- Configurar e invocar SonarCloud desde el workflow, publicar un run exitoso que ejecute el scanner y enlazar el análisis público con Quality Gate.
- Confirmar las cuentas de GitHub de las dos identidades no mapeadas en `EQUIPOS.md`.

## Recuento y nota sugerida

10 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decisión del profesor): 5.0 = 1 + 4 × (10/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contribución: cuatro identidades aparecen en el historial, pero solo dos cuentas están confirmadas en `EQUIPOS.md`; se requiere asociación explícita para las otras dos.
- SonarCloud: no existe configuración o invocación del scanner ni URL pública del análisis con Quality Gate; es una no conformidad transversal, no una fila de la ficha S7.

## Hallazgos para la planilla

- El informe preliminar evaluó `a47d5bd`; el estado correcto al cierre es `2269ca5`, que incorpora 19 commits elegibles.
- La entrega S7 cumple las diez filas de la ficha, incluida una demostración reproducible de la prueba en rojo y su posterior recuperación.
- CI está verde para el hash calificado en el run 35555368047.
- SonarCloud continúa sin evidencia pública auditable.
