# Semana 8 · Despliegue reproducible, CI y observabilidad · ShareU

> Revisión preliminar. El estado definitivo se fijará con el último commit de `master` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `532fcf6` en `origin/master` (2026-09-21T12:26:41-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación | 2026-09-24T13:15:17Z, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | No se declara una URL pública. | No cumple | No fue posible una solicitud externa. |
| Health check consultable | Existe `/health` en código, pero no un endpoint público declarado. | No verificado | Falta respuesta HTTP externa. |
| Infraestructura como código versionada en el repositorio | No se encontró IaC o descriptor de plataforma. | No cumple | El workflow no es infraestructura de despliegue. |
| El entorno se puede recrear siguiendo el README | El README cubre ejecución local, no el entorno público. | No cumple | Faltan proveedor, variables y pasos. |
| Pipeline en verde sobre la rama principal | Run exitoso de `532fcf6`: https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/35632045274 | Cumple | CI público del estado revisado. |
| Logs estructurados | No se encontró configuración ni ejemplo de logs estructurados. | No cumple | Falta formato con campos. |
| Métrica consultable asociada a un escenario de calidad | No existe métrica desplegada ligada a un escenario. | No cumple | Falta consulta y umbral. |
| Secretos fuera del código y tomados del entorno o del almacén | No hay evidencia positiva del manejo de secretos del despliegue. | No cumple | La ausencia de coincidencias no prueba carga segura. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No se encontró estimación verificable. | No cumple | Faltan piezas, supuestos y umbral. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | La sección 7 presenta Uvicorn/FastAPI/SQLite de forma genérica, no un entorno actual. | No cumple | Faltan plataformas y ubicaciones reales. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | No se documentan conjuntamente ambas restricciones. | No cumple | Falta límite operativo verificable. |
| Un ADR por decisión de plataforma, con alternativa descartada | No existe ADR de plataforma de despliegue. | No cumple | Falta decisión, alternativa y consecuencias. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación. |
| Estructura mínima presente | No cumple | Aspectos e IA están fuera de las rutas contractuales. |
| Estado calificado identificable | Cumple | Rama, hash, fecha y cierre consignados. |
| Nombres de ADR según la convención | No cumple | `docs/adr/` contiene un PDF fuera de la convención. |
| ADR aceptados no reescritos | Cumple | Historial conservado para los ADR Markdown. |
| `docs/ia.md` al día para la semana | No cumple | No registra actividad S8 en la ruta contractual. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | CI verde, pero sin scanner y Quality Gate público. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin credenciales reales detectadas. |
| Contribución de todos los integrantes | Cumple | Historial con aportes del equipo. |

## Estado global del proyecto (overall · punta actual de la misma rama)

La punta actual coincide con el estado revisado. El CI está en verde, pero no hay despliegue público ni evidencia operativa S8. La documentación además referencia una prueba contractual inexistente y debe reconciliarse con el árbol real.

## Recuento y nota sugerida

**1 de 12 criterios Cumple.**

**Nota sugerida preliminar (propuesta al docente): 1.3 = 1 + 4 × (1/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Declarar una URL pública y comprobar el health check.
- Versionar IaC y documentar la recreación del entorno.
- Completar logs, métrica, secretos, costos, arc42 §7 y ADR de plataforma.
