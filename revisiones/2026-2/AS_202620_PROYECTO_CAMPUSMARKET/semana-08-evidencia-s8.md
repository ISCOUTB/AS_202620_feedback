# Semana 8 · Despliegue reproducible, CI y observabilidad · CampusMarket

> Revisión preliminar. El estado definitivo se fijará con el último commit de `master` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `c53ee32` en `origin/master` (2026-09-18T21:11:48-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación | 2026-09-24T13:15:17Z, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | README y documentación no declaran una URL pública. | No cumple | No fue posible realizar una solicitud externa sin inventar una dirección. |
| Health check consultable | El backend implementa `/health`, pero no hay URL pública declarada. | No verificado | Falta endpoint público y código HTTP observable. |
| Infraestructura como código versionada en el repositorio | No se encontró descriptor de infraestructura o plataforma de despliegue. | No cumple | El workflow de pruebas no sustituye IaC. |
| El entorno se puede recrear siguiendo el README | El README cubre arranque local, no la recreación de un entorno público. | No cumple | Faltan proveedor, variables y pasos de despliegue. |
| Pipeline en verde sobre la rama principal | Run exitoso de `c53ee32`: https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/35414943658 | Cumple | CI público sobre el estado revisado. |
| Logs estructurados | No se encontró configuración ni ejemplo de logs estructurados. | No cumple | Falta formato y campos consultables. |
| Métrica consultable asociada a un escenario de calidad | No se encontró métrica desplegada ni consulta asociada a un escenario. | No cumple | Falta nombre, fuente y consulta. |
| Secretos fuera del código y tomados del entorno o del almacén | No hay evidencia positiva del manejo de secretos del despliegue. | No cumple | No basta con que el barrido no encuentre credenciales. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No existe estimación verificable. | No cumple | Faltan piezas, volumen y punto de ruptura. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | La sección 7 no representa un despliegue público actual. | No cumple | Faltan piezas y ubicaciones reales. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | La sección 2 no contiene ambas restricciones de S8. | No cumple | Debe declarar tope y prohibición/restricción de tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | No existe ADR de plataforma de despliegue. | No cumple | Falta decisión, alternativa y consecuencias. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación. |
| Estructura mínima presente | Cumple | Rutas contractuales presentes. |
| Estado calificado identificable | Cumple | Rama, hash, fecha y cierre consignados. |
| Nombres de ADR según la convención | Cumple | ADR numerados y en kebab-case. |
| ADR aceptados no reescritos | Cumple | Historial conservado. |
| `docs/ia.md` al día para la semana | No cumple | No registra actividad S8. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | CI verde, pero sin scanner y Quality Gate público asociado. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin credenciales reales detectadas. |
| Contribución de todos los integrantes | Cumple | Historial con aportes de los tres integrantes. |

## Estado global del proyecto (overall · punta actual de la misma rama)

La punta actual coincide con el estado revisado. El CI permanece verde, pero no hay entrega S8 verificable de despliegue u observabilidad.

## Recuento y nota sugerida

**1 de 12 criterios Cumple.**

**Nota sugerida preliminar (propuesta al docente): 1.3 = 1 + 4 × (1/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Declarar y publicar una URL con health check externo.
- Versionar IaC y documentar la reproducción del despliegue.
- Incorporar logs, métrica, costos, arc42 §7 y ADR de plataforma.
