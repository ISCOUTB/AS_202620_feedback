> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · AudioShare


| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `e4789d887fe59b2ace65bd1d2680f79758db5b54` en `origin/master` (2026-09-27T23:49:01-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

Esta pasada **no tiene cierre**: se califica la punta actual de `origin/master`. La punta actual es idéntica al estado calificado de S8 (`e4789d887fe59b2ace65bd1d2680f79758db5b54`) y `git log e4789d88..origin/master` está vacío: no hay ningún commit nuevo desde el cierre de S8. Por eso no hay porción S9 entregada y todas las filas se deciden contra el estado existente.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | rutas del código y commits | No cumple | No hay porción S9: `git log e4789d88..origin/master` vacío. El código asistido por IA del repositorio es línea base (corte vertical A-01, `docs/ia.md` usos de semana 4 y migración Flutter de semana 7), no una porción nueva del periodo. |
| Cadena completa navegable para esa porción | fila de `docs/aspectos.md` recorrida hasta la evidencia | No cumple | `docs/aspectos.md` (último cambio `ddaf474`, 2026-09-25) trae la fila A-01 con ADR, C4, `lib/` y `test/`, pero es de S7/S8 y no corresponde a una porción del periodo. La propia fila declara la medición pendiente (`docs/aspectos.md:158`, «mediciones ... no deben presentarse como verificadas»). |
| ADR con la decisión argumentada por el equipo | `docs/adr/NNNN-*.md` con restricciones del proyecto | No cumple | No se añadió ningún ADR en el periodo: `docs/adr/` llega hasta `0004-despliegue-api-azure-vs-laboratorio.md` (fecha interna 2026-09-28, de S8). No hay ADR de la porción S9. |
| Prueba que falla ante el defecto que cubre | run en rojo, prueba de mutación o procedimiento documentado | No cumple | No hay prueba ni procedimiento nuevo del periodo. Existen `test/models_test.dart`, `test/view_model_test.dart`, `test/widget_test.dart`, `tests/a01.test.ts`, `tests/contract.test.ts` y `tests/health.test.ts`, todos anteriores a la punta de S8; ninguno documenta un fallo ante un defecto. |
| Medición del escenario asociado | resultado contrastado con el umbral | No cumple | No hay medición en el periodo. `docs/aspectos.md:158` afirma que las métricas de EC-01..EC-04 «se mantienen como objetivos arquitectónicos» sin resultado experimental. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | extracto citado del archivo | No cumple | Último commit sobre `docs/ia.md`: `5a6d73b` (2026-09-20T23:24:35-05:00). El documento cierra con «Documento actualizado durante la semana 7» (`docs/ia.md`, sección Estado); no hay entrada de S9. Tiene rechazos motivados de semanas anteriores, pero no del periodo evaluado. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | hallazgos con su ubicación y su corrección | No cumple | No hay auditoría del periodo. La única es `docs/auditoria-propiedad-datos.md` (`963dba7`, 2026-09-20), de S6: detecta que `SQLiteRoomRepository` escribe `start_at`/`playback_state`/`status` y lo declara NC-10, sin corrección documentada. Contra el código, `src/modules/session/infrastructure/persistence/sqlite-room-repository.ts:73,139,157` sigue siendo la única fuente de escrituras. |
| Dependencias propuestas verificadas en su registro oficial | lista de dependencias añadidas y su comprobación | No cumple | `git diff e4789d88..origin/master -- package.json requirements.txt pyproject.toml pom.xml go.mod Gemfile pubspec.yaml` está vacío: no se añadió ninguna dependencia en el periodo, así que no hay propuesta que verificar. |
| Sin credenciales en código, ejemplos ni documentación generada | barrido del contrato, incluido `docs/` | Cumple | `git grep` de patrones sobre la punta solo coincide con `origin/master:.github/workflows/publish-image.yml:19` (`password: ${{ secrets.DOCKERHUB_TOKEN }}`), referencia a secreto, no credencial. Ningún `.env` versionado; `git log -S"BEGIN PRIVATE KEY"` sin coincidencias. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | conjunto de evaluación con resultados, o el ADR | No cumple | El sistema no incorpora componente generativo (grep de `openai\|anthropic\|gemini\|llm\|gpt` sobre código sin coincidencias). No existe el ADR que justifique no incorporarlo: `docs/adr/` no tiene ninguna decisión al respecto. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_AudioShare`, clon anónimo con `--filter=blob:none` exitoso; rama `origin/master`. | Cumple | Responde sin autenticación y el nombre sigue `AS_202620_<PROYECTO>`. |
| Estructura mínima presente | Árbol con `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas existen; arc42 en AsciiDoc (desviación de formato ya anotada en S8). |
| Estado calificado identificable | `e4789d887fe59b2ace65bd1d2680f79758db5b54` en `origin/master`, `2026-09-27T23:49:01-05:00`. | Cumple | En esta pasada sin cierre se califica la punta actual; coincide con el hash de S8 y no hay commits posteriores. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md`, `0002-estrategia-integracion.md`, `0003-transicion-a-flutter.md`, `0004-despliegue-api-azure-vs-laboratorio.md`. | Cumple | Los cuatro siguen `NNNN-titulo-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0001 aceptado en `924d133` (2026-09-04) y editado después en `354f1f5`/`453710f` (2026-09-21); ADR-0003 aceptado (`e27fe2f`) y editado en `d11f39a` (2026-09-25). | No cumple | Las ediciones son posteriores a la aceptación y no declaran ADR de reemplazo (CONTRATO §4). |
| `docs/ia.md` al día para la semana | Último commit `5a6d73b` (2026-09-20); el documento cierra en «actualizado durante la semana 7». | No cumple | No hay entrada de la semana 9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Runs del hash revisado: `Flutter` `failure` (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/36379253148); `CI` `success` (runs/36379253187) y `Publicar imagen` `success` (runs/36379253129). | No cumple | Hay un run en rojo en la rama y no se aporta la URL pública del análisis con Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | Barrido sin credenciales reales (solo `secrets.DOCKERHUB_TOKEN`); ningún `.env` versionado; `git log -S"BEGIN PRIVATE KEY"` vacío. | Cumple | Sin hallazgos de secretos. |
| Contribución de todos los integrantes | `shortlog -sne`: Elian Daniel Perea Vanegas 60, cardonavincent26-design 59, Yeiver Andrés Vergel Pérez 41, Santiago Adolfo Camacho Hernández 37. | Cumple | Cuatro identidades para cuatro integrantes declarados; la atribución de `cardonavincent26-design` a Vincent Cardona es presunta (no se consolida por parecido de nombre). |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `e4789d887fe59b2ace65bd1d2680f79758db5b54 2026-09-27T23:49:01-05:00 S8: URL desplegada en Azure, evidencia de health y restricciones de la suscripción`
- **Veredicto**: sin entrega S9
- **Commits posteriores al cierre de S8**: ninguno; la punta actual es idéntica al hash calificado de S8.
- Resumen: no hay trabajo nuevo desde S8. El repositorio conserva la entrega de despliegue de la semana anterior (Dockerfile, compose, publish-image, `docs/despliegue.md`, ADR-0004, logs JSON, métrica de A-01) y arrastra sus pendientes: el workflow `Flutter` sigue en rojo en `origin/master`, no hay URL pública de SonarCloud con Quality Gate, ADR-0001 y ADR-0003 fueron editados tras su aceptación, y `docs/ia.md` no pasa de la semana 7. Para S9 no hay porción construida con IA, ni cadena, ni ADR, ni prueba, ni medición, ni entrada de IA, ni verificación de dependencias.

Pendientes que siguen abiertos:
- Entregar la porción S9 con su cadena completa (aspectos → ADR → código → prueba que falle ante el defecto → medición).
- Añadir a `docs/ia.md` lo aceptado, lo corregido y lo rechazado con motivo de la generación del periodo.
- Documentar la auditoría de erosión si la generación cruzó límites de contexto o las reglas de propiedad de datos de la semana 6.
- Poner en verde el workflow `Flutter` sobre `origin/master`.
- Publicar la URL pública del análisis de SonarCloud con Quality Gate (y alinear la organización, hoy `cardonavincent26`).
- Dejar de editar ADR aceptados sin declarar reemplazo.

## Recuento y nota sugerida

**1 de 10 criterios cumplidos.**

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Este informe no contiene filas No verificado: todas las comprobaciones se resolvieron leyendo el árbol de la punta. La ausencia de la entrega S9 es evidencia de ausencia, no una imposibilidad de comprobar.

## Hallazgos para la planilla

- La punta actual de `origin/master` es idéntica al hash calificado de S8: no hay ningún commit desde el cierre de S8, por lo que S9 no está entregada a la fecha de esta pasada temprana.
- No hay porción S9 ni su cadena; se arrastran los pendientes de S8 (workflow `Flutter` en rojo, SonarCloud sin URL pública con Quality Gate, ADR aceptados editados, `docs/ia.md` sin entrada posterior a la semana 7).
- El barrido de credenciales sigue limpio y la contribución sigue repartida entre los cuatro integrantes.
