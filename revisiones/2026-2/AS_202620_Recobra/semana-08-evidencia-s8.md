# Semana 8 · Despliegue reproducible, CI y observabilidad · Recobra

> Revisión preliminar. El estado definitivo se fijará con el último commit de `master` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `8f25313` en `origin/master` (2026-09-19T13:37:58-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación | 2026-09-24T13:15:17Z, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `docs/arc42/arc42.md:174-178` declara que aún no existe despliegue en nube. | No cumple | No hay URL para consultar. |
| Health check consultable | Sin despliegue público no existe health check externo verificable. | No cumple | Falta endpoint y respuesta HTTP pública. |
| Infraestructura como código versionada en el repositorio | No se encontró IaC para un entorno público. | No cumple | El workflow de CI no sustituye infraestructura. |
| El entorno se puede recrear siguiendo el README | El README no permite recrear un despliegue público. | No cumple | Faltan proveedor, variables y pasos. |
| Pipeline en verde sobre la rama principal | Run exitoso de `8f25313`: https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/35461821663 | Cumple | CI público del estado revisado. |
| Logs estructurados | No se encontró configuración ni ejemplo de logs estructurados. | No cumple | Falta formato con campos. |
| Métrica consultable asociada a un escenario de calidad | No existe métrica consultable vinculada a un escenario. | No cumple | Falta fuente y consulta. |
| Secretos fuera del código y tomados del entorno o del almacén | No hay evidencia positiva del mecanismo de secretos del despliegue. | No cumple | No basta la ausencia de credenciales reales. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No se encontró estimación de costos S8. | No cumple | Faltan supuestos y umbral. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | La propia sección indica que el despliegue en nube está pendiente. | No cumple | No representa piezas ejecutándose en una plataforma. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | No se encontraron ambas restricciones explícitas. | No cumple | Deben documentarse conjuntamente. |
| Un ADR por decisión de plataforma, con alternativa descartada | No existe ADR de plataforma de despliegue. | No cumple | Falta decisión verificable. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación. |
| Estructura mínima presente | Cumple | Rutas contractuales presentes. |
| Estado calificado identificable | Cumple | Rama, hash, fecha y cierre consignados. |
| Nombres de ADR según la convención | Cumple | ADR numerados y en kebab-case. |
| ADR aceptados no reescritos | Cumple | Historial conservado. |
| `docs/ia.md` al día para la semana | No cumple | No registra actividad S8. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | CI verde, pero sin scanner y Quality Gate público. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin credenciales reales detectadas. |
| Contribución de todos los integrantes | Cumple | Historial con aportes del equipo. |

## Estado global del proyecto (overall · punta actual de la misma rama)

La punta actual coincide con el estado revisado. Conserva CI verde, pero la documentación confirma que el despliegue en nube y el resto de la evidencia S8 están pendientes.

## Recuento y nota sugerida

**1 de 12 criterios Cumple.**

**Nota sugerida preliminar (propuesta al docente): 1.3 = 1 + 4 × (1/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Publicar el sistema y un health check verificable.
- Versionar IaC y documentar la reproducción del despliegue.
- Completar observabilidad, secretos, costos, arc42 §7 y ADR de plataforma.

