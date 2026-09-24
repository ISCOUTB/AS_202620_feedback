# Evidencia S7 · XALD

> Auditoría local definitiva del informe automático. Se corrigieron discrepancias materiales al contrastar directamente el repositorio y la única consulta permitida de `actions/runs`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `62a0d15` en `origin/master` (2026-09-20T23:25:16-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | `docs/api/openapi.yaml:1-23` declara OpenAPI 3.1.0 y `POST /transacciones`. | Cumple | El archivo está versionado y no es prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | `docs/api/openapi.yaml:23-104` define `requestBody`, respuestas 202/400 y los esquemas `TransaccionDTO`, `RespuestaSincronizacion` y `OrigenDatosEnum`. | Cumple | Los campos obligatorios tienen tipos, formatos y restricciones. |
| Correspondencia entre el contrato y la API implementada | El servidor base del contrato termina en `/api/v1` y la ruta es `/transacciones`; `backend/app/main.py:9-15` implementa `POST /api/v1/transacciones`, y `backend/app/dtos.py:10-23` implementa los dos esquemas de entrada y salida. | Cumple | Se contrastó el contrato con el código, no solo con la matriz redactada por el equipo. |
| Versión de la API declarada y con historial | `info.version` es `1.0.0`; el historial del archivo muestra `b00b319`, `364ac5b`, `b7ca7f7` y `73de849` entre el 17 y el 20 de septiembre. | Cumple | Hay versión explícita e historial verificable. |
| Prueba de contrato presente | `.github/workflows/ci.yml:33-37` instala Redocly 1.25.0 y ejecuta `redocly lint docs/api/openapi.yaml`. | Cumple | La validación contractual está versionada como paso explícito del workflow. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/ci.yml:33-37`; run de `Android CI` para `62a0d15`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/35560909205 | Cumple | El run corresponde exactamente al estado revisado. |
| Evidencia de que la prueba falla ante un cambio incompatible | `b7ca7f7` cambió `/transacciones` por `/sync` y `TransaccionDTO` por `PayloadSincronizacionDTO`; su run falló: https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/35559611135. `73de849` revirtió el cambio y el run volvió a verde: https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/35560496404 | Cumple | La secuencia rojo→corrección→verde es auditable. |
| ADR de la estrategia de integración ligado a un escenario | `docs/adr/0007-contratos-por-modulo.md:19-64` compara comunicación directa, interfaces y orquestación centralizada. | No cumple | El ADR resuelve límites entre módulos, pero no liga la elección síncrona/asíncrona de la API a un escenario de calidad concreto, como exige la ficha. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/06-Runtime view.md` documenta flujos de captura, degradación de Gemini y sincronización con diagramas de secuencia. | Cumple | Distingue lo implementado de la reclasificación aún pendiente. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/c2.md:23-32` etiqueta llamadas Kotlin/DTO, HTTPS/REST/JSON, `BroadcastReceiver`/`SmsMessage` y UI nativa; `docs/c4/c2.md:66-76` explica los conectores. | Cumple | Cada relación muestra protocolo o mecanismo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | El clon sin autenticación de `ISCOUTB/AS_202620_XALD` respondió correctamente. | Cumple | Nombre y visibilidad verificables. |
| Estructura mínima presente | En `62a0d15` existen `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | `docs/arc42/07-Deployment View.md` está vacío, pero la ruta existe. |
| Estado calificado identificable | `origin/master`, `62a0d1540c9f4ae9d4df611b3a20286e8d7c1a76`, 2026-09-20T23:25:16-05:00. | Cumple | Es el último commit anterior o igual al cierre. |
| Nombres de ADR según la convención | Siete archivos `0001-...md` a `0007-...md`, todos en kebab-case. | Cumple | Sin nombres fuera de convención. |
| ADR aceptados no reescritos | Los ADR 0001–0006 tienen múltiples cambios posteriores a su creación; por ejemplo, el ADR 0005 fue actualizado el 6 y el 20 de septiembre. | No cumple | Los cambios no se registraron mediante ADR de reemplazo. |
| `docs/ia.md` al día para la semana | Último cambio `c450b4f` del 2026-09-20; `docs/ia.md:23-32` registra el trabajo de S6/S7 y decisiones aceptadas. | Cumple | Incluye aceptaciones y descartes con motivo. |
| Pipeline, SonarCloud y Quality Gate públicos | El CI del hash revisado está verde, pero `.github/workflows/ci.yml` no invoca un scanner ni existe URL pública de análisis con Quality Gate. | No cumple | El enlace presentado como Sonar en `docs/api/contrato.md` apunta a GitHub, no a `sonarcloud.io`. |
| Sin credenciales en el repositorio ni en el historial | Barrido de patrones, `.env` versionados y claves privadas sin coincidencias materiales. | Cumple | Los `.pyc` versionados son un problema de higiene, no una credencial. |
| Contribución de todos los integrantes | `git shortlog -sne 62a0d15` muestra cuatro identidades consolidadas, coincidentes en cantidad con los cuatro integrantes declarados. | Cumple | No se infiere correspondencia por parecido de nombre. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `62a0d1540c9f4ae9d4df611b3a20286e8d7c1a76` (2026-09-20T23:25:16-05:00).
- **Veredicto:** con no conformidades.
- No hay commits posteriores al cierre en `origin/master`.
- Siguen abiertos el ADR de estrategia de integración ligado explícitamente a un escenario, SonarCloud público con Quality Gate, la vista de despliegue vacía, la reescritura de ADR aceptados y los enlaces de `docs/aspectos.md` que apuntan a `experimental`.
- El contrato, la correspondencia con FastAPI, la validación en CI y la prueba rojo→verde sí quedaron verificadas en esta auditoría.

## Recuento y nota sugerida

**9 de 10 criterios Cumple.**

**Nota sugerida (propuesta al docente, publicada por decisión del profesor): 4.6 = 1 + 4 × (9/10).** La nota final la fija el profesor en Moodle.

## No conformidades y pendientes

- Vincular en un ADR la elección síncrona/asíncrona de la integración con un escenario de calidad concreto y su alternativa descartada.
- Incorporar scanner, run exitoso y URL pública de SonarCloud con Quality Gate.
- Registrar cambios de decisiones aceptadas mediante ADR de reemplazo, sin reescribir el registro histórico.
- Completar `docs/arc42/07-Deployment View.md` y corregir los enlaces de `docs/aspectos.md` hacia la rama principal.

## Hallazgos para la planilla

- La auditoría corrige el S7 automático: el workflow sí valida el contrato, el run del hash está verde y existe una secuencia roja verificable ante un cambio incompatible.
- El único criterio de la ficha que no cumple es el ADR de estrategia de integración ligado a un escenario.
- SonarCloud continúa sin evidencia pública completa.
