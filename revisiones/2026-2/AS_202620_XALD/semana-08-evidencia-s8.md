# Evidencia S8 · XALD

> Revisión local preliminar. Puede cambiar hasta el cierre de la actividad.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `62a0d15` en `origin/master` (2026-09-20T23:25:16-05:00) |
| Cierre previsto | 2026-09-28T05:00:00Z |
| Comprobación | 2026-09-24 (revisión local) |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `docs/api/openapi.yaml:16` contiene `https://api.xald-app.com/api/v1`, pero el README no la declara como entorno desplegado ni se autorizó sondear esa URL externa descubierta en el repositorio. | No verificado | Hace falta una URL entregada explícitamente y una comprobación HTTP con hora. |
| Health check consultable | No hay ruta de health en `backend/app/main.py`, en el OpenAPI ni en el README. | No cumple | Se esperaba una ruta declarada y su código HTTP. |
| Infraestructura como código versionada en el repositorio | El árbol de `62a0d15` no contiene Dockerfile, Compose, Terraform, Kubernetes, Helm ni configuración de proveedor. | No cumple | El workflow de CI no describe el entorno desplegado. |
| El entorno se puede recrear siguiendo el README | `README.md:30-45` documenta la suite Android local, pero no la creación de un entorno desplegado con backend, configuración y secretos. | No cumple | La guía local no reproduce un despliegue S8. |
| Pipeline en verde sobre la rama principal | Run `Android CI` de `master` para `62a0d15`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/35560909205 | Cumple | Es el último run del estado revisado. |
| Logs estructurados | No se encontró configuración de logs estructurados ni ejemplo con campos en el código del hash revisado. | No cumple | Cadenas de consola sin estructura no bastan. |
| Métrica consultable asociada a un escenario de calidad | No se encontró endpoint, exportador o tablero de métricas ligado a ESC-01…ESC-05. | No cumple | Las medidas documentales no son una métrica consultable del entorno. |
| Secretos fuera del código y tomados del entorno o del almacén | El OpenAPI declara `X-API-Key`, pero no existe configuración de despliegue, `.env.example` ni referencia a un almacén de secretos. | No cumple | No hay evidencia de cómo se inyectaría el secreto en producción. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/arc42/02-Architecture constraints.md:21` fija costo cero, pero no calcula volumen, costo por pieza ni punto de ruptura. | No cumple | Una restricción de presupuesto no sustituye la estimación. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07-Deployment View.md` está vacío. | No cumple | Falta la vista completa. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02-Architecture constraints.md:17-21` exige servicios gratuitos e infraestructura sin costo. | Cumple | No se declara una restricción adicional de tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | No existe ADR de plataforma de despliegue; el ADR 0007 trata contratos entre módulos. | No cumple | Faltan decisiones de proveedor/plataforma y sus alternativas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon público sin autenticación de `ISCOUTB/AS_202620_XALD`. | Cumple | — |
| Estructura mínima presente | Las seis rutas mínimas están presentes en `62a0d15`. | Cumple | La sección 7 existe pero está vacía. |
| Estado calificado identificable | `origin/master`, `62a0d15`, 2026-09-20T23:25:16-05:00. | Cumple | Estado preliminar elegible antes del cierre S8. |
| Nombres de ADR según la convención | Siete ADR con `NNNN-titulo-en-kebab-case.md`. | Cumple | — |
| ADR aceptados no reescritos | Los ADR 0001–0006 tienen reescrituras posteriores sin reemplazo declarado. | No cumple | — |
| `docs/ia.md` al día para la semana | El último cambio es del 2026-09-20, anterior al periodo S8. | No cumple | Falta registrar el trabajo de despliegue/observabilidad o declarar que no se realizó. |
| Pipeline, SonarCloud y Quality Gate públicos | CI verde, pero sin scanner ni URL pública de SonarCloud con Quality Gate. | No cumple | — |
| Sin credenciales en el repositorio ni en el historial | Barridos sin coincidencias materiales. | Cumple | — |
| Contribución de todos los integrantes | Cuatro identidades consolidadas en el historial. | Cumple | Coincide en cantidad con el equipo declarado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `62a0d1540c9f4ae9d4df611b3a20286e8d7c1a76`.
- No hay actividad nueva después de S7.
- El CI está verde y existe una restricción de costo cero, pero no hay evidencia de despliegue, health, infraestructura como código, observabilidad, gestión de secretos ni cálculo de costo.

## Recuento y nota sugerida

**2 de 12 criterios Cumple.**

**Nota sugerida preliminar (propuesta al docente): 1.7 = 1 + 4 × (2/12).** La nota final la fija el profesor en Moodle.

## No conformidades y pendientes

- Entregar una URL pública explícita y un health check verificable con hora.
- Versionar la infraestructura y documentar cómo recrear el entorno desplegado.
- Añadir logs estructurados, una métrica consultable ligada a un escenario y manejo de secretos del proveedor.
- Calcular el costo mensual y el punto de ruptura de la capa gratuita.
- Completar arc42 §7 y registrar las decisiones de plataforma en ADR separados.

## Hallazgos para la planilla

- El estado S8 coincide con S7; no hay commits nuevos en la rama principal.
- Solo cumplen el pipeline verde y la restricción de costo cero.
