# Semana 8 · Despliegue reproducible, CI y observabilidad · ROUTB

> Revisión preliminar. El estado definitivo se fijará con el último commit de `master` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `35d088c` en `origin/master` (2026-09-23T23:53:01-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación | 2026-09-24T13:15:17Z, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | No se declara una URL pública en README ni documentación. | No cumple | No se inventó una dirección a partir del nombre del servicio. |
| Health check consultable | `backend/app/main.py` y `render.yaml` configuran health check, pero no hay URL pública declarada. | No verificado | Falta solicitud externa y código HTTP observable. |
| Infraestructura como código versionada en el repositorio | `render.yaml:1-18`, `Dockerfile` y `docker-compose.yml`. | Cumple | La infraestructura está descrita como código. |
| El entorno se puede recrear siguiendo el README | El README no documenta el procedimiento de despliegue con los artefactos presentes. | No cumple | Faltan variables, proveedor y pasos. |
| Pipeline en verde sobre la rama principal | El run de `35d088c` concluyó `failure`: https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/35957534355 | No cumple | Un run posterior de otra rama no acredita `master`. |
| Logs estructurados | `backend/app/main.py:14-43` emite logs JSON con campos. | Cumple | Configuración versionada y verificable. |
| Métrica consultable asociada a un escenario de calidad | No se encontró una métrica consultable ligada a un escenario. | No cumple | Falta consulta, fuente y umbral. |
| Secretos fuera del código y tomados del entorno o del almacén | `render.yaml` usa variables del proveedor con `sync: false` y se documenta `.env.example`. | Cumple | El despliegue productivo no contiene valores reales; el Compose local conserva literales inseguros como no conformidad transversal. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/evidencia/costo_mensual.md:3-58` detalla piezas, supuestos y umbrales. | Cumple | Incluye punto de ruptura de la capa gratuita. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | La sección 7 usa cajas genéricas de servidor y datos, sin identificar Render/Supabase. | No cumple | No representa el despliegue real. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02-restricciones.md:65-69` fija costo y restricción de tarjeta. | Cumple | Ambas restricciones están explícitas. |
| Un ADR por decisión de plataforma, con alternativa descartada | El ADR 0005 agrupa Render y Supabase en una sola decisión. | No cumple | La ficha exige un ADR por plataforma. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación. |
| Estructura mínima presente | Cumple | Rutas contractuales presentes. |
| Estado calificado identificable | Cumple | Rama, hash, fecha y cierre consignados. |
| Nombres de ADR según la convención | Cumple | ADR numerados y en kebab-case. |
| ADR aceptados no reescritos | Cumple | Historial conservado. |
| `docs/ia.md` al día para la semana | No cumple | No registra actividad S8. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | El run de `master` falla y no acredita Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | No cumple | `docker-compose.yml:6-32` contiene contraseña y secreto JWT literales, aunque sean valores locales. |
| Contribución de todos los integrantes | Cumple | Historial con aportes de todo el equipo. |

## Estado global del proyecto (overall · punta actual de la misma rama)

La punta actual coincide con el estado revisado. Hay avance material en IaC, logs y costos, pero faltan URL verificable, CI verde de `master`, métrica, vista real y separación de ADR de plataforma.

## Recuento y nota sugerida

**5 de 12 criterios Cumple.**

**Nota sugerida preliminar (propuesta al docente): 2.7 = 1 + 4 × (5/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Declarar la URL y permitir comprobar externamente el health check.
- Recuperar el pipeline de `master` y añadir una métrica ligada a un escenario.
- Actualizar arc42 §7, separar las decisiones de plataforma y retirar secretos literales del Compose.

