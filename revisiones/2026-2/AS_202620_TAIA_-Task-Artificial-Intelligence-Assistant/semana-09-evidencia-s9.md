> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · TAIA

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `4b0724247c6a58f82bc6091f78ab8872d58456de` en `origin/main` (2026-09-27T23:03:53-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual de `origin/main` **es idéntica al hash calificado de S8** (`4b07242`, 2026-09-27):
el periodo S9 (`4b07242..origin/main`) está **vacío**, el equipo no empujó ninguna porción nueva.
Esta pasada **no tiene corte**: se califica la punta actual del 2026-10-01, no un commit anterior a
un cierre. Bajo CONTRATO §12 la evidencia previa es línea base y **no se recalifica por existir**:
las filas que describen la entrega S9 quedan en No cumple (o No verificado) por ausencia de artefacto
del periodo, y los artefactos anteriores se citan solo como contexto. La fila de credenciales y la
matriz transversal se deciden sobre el estado en la punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Contexto (semanas anteriores): `docs/ia.md` (última entrada 2026-09-15) documenta la construcción asistida del contrato de API; código en `backend/app/modules/ai/adapters/outbound/gemini_llm.py`, `docs/api/openapi.json` y `backend/tests/test_api_contract.py`. | No cumple | El periodo S9 (`4b07242..origin/main`) no tiene commits: no hay porción nueva construida en esta evidencia. El artefacto citado es de S7/S8: línea base (CONTRATO §12). |
| Cadena completa navegable para esa porción | `docs/aspectos.md` filas `A-01`…`A-07` (todas con C4, ADR, código y pruebas enlazados) y `docs/c4/C4-C2.md`. | No cumple | La tabla de aspectos no se tocó en el periodo; la cadena citada es de entregas anteriores y no satisface la fila S9. |
| ADR con la decisión argumentada por el equipo | Contexto (semanas anteriores): `docs/adr/0001-estilo-arquitectonico.md`, `0002-estrategia-integracion-api-sincrona.md`, `0003-plataforma-despliegue-api.md` y `0004-plataforma-base-de-datos.md`, con alternativas y restricciones. | No cumple | No hay ADR del periodo S9; los citados son de S3/S7/S8 (CONTRATO §12). |
| Prueba que falla ante el defecto que cubre | Contexto (semana anterior): `backend/tests/test_api_contract.py` y `docs/evidencia_s7_contract_failure.txt` documentan el fallo de contrato en S7. | No verificado | No hay run en rojo, prueba de mutación ni procedimiento documentado del periodo S9. Queda como pregunta para la sustentación (CONTRATO §13). |
| Medición del escenario asociado | Contexto (semana anterior): `GET /metrics` en `backend/app/shared/adapters/inbound/observability.py:135` y `docs/calidad/escenarios_calidad.md:101` (p95 de `POST /ai/message`). | No cumple | No hay medición nueva del periodo contrastada con su umbral. La métrica del despliegue es línea base de S8. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | El último commit sobre `docs/ia.md` es `7b32b3f` (2026-09-16), dentro de la ventana S7. No hay entrada del periodo S9. | No cumple | El registro histórico documenta rechazos con motivo (p. ej. no incorporar Schemathesis), pero no tiene extracto de la semana S9; la evidencia previa no satisface la fila (CONTRATO §12). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | El barrido `erosión\|límite de contexto` no devuelve coincidencias; `docs/auditoria_violaciones_s6.md` y `docs/propiedad_datos_s6.md` son de la semana 6. | No cumple | No hay auditoría de erosión del periodo S9 que registre hallazgos de contexto o propiedad de datos con su corrección. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 está vacío en `backend/requirements.txt`, `backend/requirements-dev.txt` y los ficheros de dependencias. | No cumple | Sin dependencias nuevas respecto de S8; no hay lista ni comprobación en npm/PyPI que citar. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta: coincidencias solo en nombres de parámetros y campos (`backend/app/modules/usuario/adapters/inbound/api.py:49` `password: str`), lecturas de entorno (`gemini_llm.py:95` `GEMINI_API_KEY`, `jwt_token_service.py:23` `TAIA_JWT_SECRET`) y datos de prueba (`backend/tests/test_usuario_register.py:63` `password = "segura123"`). Sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | Sin credenciales reales; los secretos se leen del entorno. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | El sistema sí incorpora un proveedor LLM: `docs/adr/0001-estilo-arquitectonico.md:7`, `docs/c4/C4-C2.md` (`System_Ext(gemini, ...)` con `BiRel(api, gemini, "HTTPS / JSON")`) y `docs/costo_mensual.md`. | No cumple | El componente generativo existe, pero no hay conjunto de evaluación con resultados, costo por operación ni latencia del periodo S9; los artefactos de costo y métrica son de S8 (línea base). |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant`, clonado sin autenticación; rama principal `origin/main`. | Cumple | Nombre `AS_202620_<PROYECTO>` conforme y visibilidad pública. |
| Estructura mínima presente | En `4b07242`: `README.md`, `docs/arc42/` (01-12 y arc42.md), `docs/adr/` (0001-0004), `docs/c4/` (C1-C3), `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas del contrato §2 están versionadas. |
| Estado calificado identificable | `4b0724247c6a58f82bc6091f78ab8872d58456de` en `origin/main`, commit del 2026-09-27T23:03:53-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. Coincide con el hash de S8; no hay commits posteriores. |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md` … `0004-plataforma-base-de-datos.md`. | Cumple | Los cuatro cumplen `NNNN-titulo-en-kebab-case.md`; el filtro de §4 no devuelve residuos. |
| ADR aceptados no reescritos | `git log --follow` de `docs/adr/0001-estilo-arquitectonico.md`: `decaa36` (creación, 2026-08-22), `4dd3925` (2026-08-29) y `42c5b03` (2026-09-06, «add traceability section»), sin ADR sucesor ni reemplazo declarado. | No cumple | Un ADR aceptado se editó tras su aceptación; viene registrado desde S5/S8. |
| `docs/ia.md` al día para la semana | Último commit sobre `docs/ia.md` = `7b32b3f` (2026-09-16); sin entradas del periodo S9. | No cumple | El registro no creció en la ventana de esta evidencia. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Runs del hash revisado: CI `36376147005` y CD `36376186792`, ambos `success`. No existe `sonar-project.properties` ni paso del scanner en `.github/workflows/`, ni URL pública de análisis con Quality Gate. | No cumple | El CI/CD está en verde, pero falta la evidencia de SonarCloud que exige CONTRATO §8. |
| Sin credenciales en el repositorio ni en el historial | `git grep` §9 sobre `4b07242`: coincidencias solo en parámetros, campos y datos de prueba; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | Barrido limpio. |
| Contribución de todos los integrantes | `git shortlog -sne 4b07242` consolidado por correo idéntico: val/valeria-estefania (42), dei0811 (31), Luis Mendoza/luis20072002 (28) y mark (3). | Cumple | Los cuatro integrantes declarados en EQUIPOS.md tienen commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `4b0724247c6a58f82bc6091f78ab8872d58456de` 2026-09-27T23:03:53-05:00 `docs: complete deployment workshop data` (`origin/main`)
- **Veredicto**: sin trabajo nuevo de S9; base de S8 sin mover
- Resumen: la rama `main` no se movió desde S8. El repositorio conserva su base: backend modular
  (hexagonal selectiva), contrato OpenAPI 3.1 con prueba de contrato en CI, ADRs de estilo, API,
  integración y plataformas, logs JSON y `/metrics` ligados a S3/RNF-08, estimación de costo con
  supuestos, Dockerfile y Terraform. Esa base es **línea base** bajo CONTRATO §12 y no satisface las
  filas de S9. Para esta evidencia faltan la porción nueva con IA y su cadena (aspectos, ADR, prueba
  y medición del periodo), el extracto de `docs/ia.md` del periodo, la auditoría de erosión, la
  verificación de dependencias del periodo y la evaluación del componente generativo (Gemini) con
  costo y latencia. Se mantienen las no conformidades transversales: ADR-0001 aceptado editado sin
  reemplazo, `docs/ia.md` sin entrada del periodo y ausencia de SonarCloud con Quality Gate público.

Pendientes que siguen abiertos:
- Sin commits de S9: la punta es la de S8.
- Sin porción S9, sin prueba del periodo y sin extracto de `docs/ia.md` del periodo: por CONTRATO §12
  las filas 1, 3 y 6 pasan a No cumple y la fila 4 a No verificado.
- Sin medición nueva contra umbral de ningún escenario.
- Sin auditoría de erosión del periodo ni verificación de propiedad de datos.
- Sin dependencias nuevas que verificar en el periodo.
- El componente generativo (Gemini) existe, pero sin conjunto de evaluación, costo por operación ni
  latencia del periodo.
- Sin SonarCloud (configuración, run y URL pública con Quality Gate), pendiente desde S6.
- ADR-0001 aceptado editado en `4dd3925` y `42c5b03` sin declarar reemplazo.

## Recuento y nota sugerida

**1 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, el único criterio que se resuelve sobre el estado en la punta es el barrido de
credenciales; las demás filas describen la entrega S9, cuyo periodo (`4b07242..origin/main`) está
vacío: la evidencia previa es línea base y no se recalifica por existir.

## No verificado / pendientes

- Prueba que falla ante el defecto: **No verificado**. No hay run en rojo, prueba de mutación ni
  procedimiento documentado del periodo S9. Queda como pregunta de sustentación.
- Medición de escenarios: no hay medición nueva del periodo contrastada con su umbral.
- Auditoría de erosión: no existe artefacto del periodo que la documente.
- Dependencias del periodo: el diff contra S8 está vacío, no hay nada que comprobar en los registros.
- Componente generativo: existe (Gemini) pero sin evaluación del periodo; sin ADR nuevo.

## Hallazgos para la planilla

- La punta de `origin/main` (`4b07242`, 2026-09-27) es idéntica al hash calificado de S8: el periodo S9 está vacío.
- Aplicado CONTRATO §12: sin artefacto del periodo, las filas 1, 3 y 6 pasan a No cumple y la fila 4 a No verificado; solo el barrido de credenciales queda en Cumple.
- `docs/ia.md` no creció en el periodo (último `7b32b3f`, 2026-09-16).
- El sistema incorpora Gemini como componente generativo sin conjunto de evaluación ni medición de costo/latencia del periodo.
- ADR-0001 aceptado editado en `4dd3925` (2026-08-29) y `42c5b03` (2026-09-06) sin ADR sucesor.
- Sin SonarCloud: ni configuración, ni run del scanner, ni URL pública con Quality Gate.
