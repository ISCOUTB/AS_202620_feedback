# Evidencia S8 · uniTeam

> Revisión local preliminar. Puede cambiar hasta el cierre de la actividad.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `73d714c` en `origin/master` (2026-09-21T11:46:49-05:00) |
| Cierre previsto | 2026-09-28T05:00:00Z |
| Comprobación | 2026-09-24 (revisión local) |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `docs/calidad/analisis-estatico.md:122` declara expresamente que no existe despliegue; README y OpenAPI solo usan `localhost`. | No cumple | No hay URL pública que comprobar. |
| Health check consultable | `app/main.py:72-74` implementa `/activo` y `docs/api/openapi.yaml:26-41` lo documenta, pero solo para `localhost`. | No cumple | La ruta existe, pero no es consultable en un entorno público. |
| Infraestructura como código versionada en el repositorio | `Dockerfile`, `web/Dockerfile` y `compose.yaml` describen API, web, MySQL y emisor OIDC local. | Cumple | Infraestructura reproducible para el entorno local. |
| El entorno se puede recrear siguiendo el README | README documenta `docker compose up`; `compose.yaml:1-73` levanta cuatro piezas y espera el health de MySQL. | Cumple | El proveedor OIDC es solo de desarrollo y no debe usarse en producción. |
| Pipeline en verde sobre la rama principal | Run de CI de `73d714c` en `master`, conclusión `failure`: https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/35627786409 | No cumple | — |
| Logs estructurados | `app/application/bus.py:8-35` usa `logging` con una cadena parametrizada, sin formatter JSON ni campos estructurados. | No cumple | — |
| Métrica consultable asociada a un escenario de calidad | Existe `scripts/medir_esc01.py` y una línea base local, pero no endpoint/exportador/tablero de métricas consultable en el entorno. | No cumple | La ficha de medición reconoce que falta repetirla sobre el despliegue real. |
| Secretos fuera del código y tomados del entorno o del almacén | `compose.yaml:13-17` y `:43-50` contienen credenciales y configuración de desarrollo; no existe `.env.example` ni integración con almacén de secretos de un proveedor. | No cumple | La justificación de que sean locales no demuestra protección en despliegue. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | Los ADR mencionan infraestructura gratuita, pero no hay cálculo mensual por volumen, costo por pieza ni punto de ruptura. | No cumple | — |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42-uniteam.md:467-470` dice únicamente “Pendiente”. | No cumple | — |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42-uniteam.md:84-92` exige infraestructura gratuita o cuentas de estudiante y declara que no hay presupuesto. | Cumple | No se declara una restricción adicional de tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | Los ADR deciden stack, MySQL y OIDC, pero no existe decisión de plataforma/proveedor de despliegue; el proveedor OIDC también sigue pendiente. | No cumple | — |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon público sin autenticación. | Cumple | — |
| Estructura mínima presente | Las seis rutas mínimas existen. | Cumple | arc42 §7 y §8 están pendientes. |
| Estado calificado identificable | `origin/master`, `73d714c`, 2026-09-21T11:46:49-05:00. | Cumple | Estado preliminar elegible. |
| Nombres de ADR según la convención | Seis ADR con nombres válidos. | Cumple | — |
| ADR aceptados no reescritos | Cada ADR conserva un único commit de creación; 0001 declara reemplazo por 0002. | Cumple | — |
| `docs/ia.md` al día para la semana | Último cambio del 2026-09-18, anterior al periodo S8. | No cumple | — |
| Pipeline, SonarCloud y Quality Gate públicos | La punta está roja y el workflow no aporta scanner ni URL pública de SonarCloud. | No cumple | — |
| Sin credenciales en el repositorio ni en el historial | No se hallaron secretos de producción; las credenciales versionadas son las declaradas para contenedores locales efímeros. | Cumple | Deben separarse para un despliegue real. |
| Contribución de todos los integrantes | Hay seis grupos de identidades observadas; solo `JuanB`/`JuanBustamante` se consolidan por compartir la misma cuenta. `EQUIPOS.md` no aporta correspondencias individuales y `iansx` no aparece. | No verificado | No se atribuyen ni consolidan cuentas por parecido de nombre; hace falta confirmación docente. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `73d714ce49ee2085275755091d00f7688f4dee26`.
- Hay una base local reproducible con contenedores y health interno, pero el propio repositorio declara que no existe despliegue.
- La punta tiene CI fallido y faltan observabilidad, costos, arc42 §7 y decisiones de proveedor.

## Recuento y nota sugerida

**3 de 12 criterios Cumple.**

**Nota sugerida preliminar (propuesta al docente): 2.0 = 1 + 4 × (3/12).** La nota final la fija el profesor en Moodle.

## No conformidades y pendientes

- Publicar un entorno real con URL y health verificable.
- Corregir el CI de `master`.
- Añadir logs estructurados y una métrica consultable ligada a un escenario.
- Separar secretos de la configuración y conectarlos con el proveedor.
- Estimar costos, completar arc42 §7 y documentar cada decisión de plataforma en un ADR.

## Hallazgos para la planilla

- Cumplen la infraestructura local versionada, el procedimiento reproducible y la restricción de costo.
- El repositorio declara que todavía no hay despliegue y el CI de la punta está rojo.
