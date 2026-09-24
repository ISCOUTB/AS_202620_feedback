# Evidencia S8 · mapsutb

> Revisión local preliminar. Puede cambiar hasta el cierre de la actividad.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `7048021` en `origin/master` (2026-09-22T10:10:19-05:00) |
| Cierre previsto | 2026-09-28T05:00:00Z |
| Comprobación | 2026-09-24 (revisión local) |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | El README y arc42 §7 no declaran una URL pública del sistema. | No cumple | No hubo URL que comprobar con hora y código HTTP. |
| Health check consultable | No se encontró ruta de health ni endpoint equivalente en el árbol revisado. | No cumple | — |
| Infraestructura como código versionada en el repositorio | No hay Dockerfile, Compose, Terraform, Kubernetes, Helm ni archivo de proveedor de despliegue. | No cumple | El workflow existente es de CI, no infraestructura del entorno. |
| El entorno se puede recrear siguiendo el README | `README.md:58-78` declara requisitos y `./scripts/start.sh`, que instala dependencias, ejecuta pruebas y arranca la app. | Cumple | Reproduce el entorno local; aún no documenta un despliegue público. |
| Pipeline en verde sobre la rama principal | El run de CI de `7048021` concluyó `failure`: https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/35745455578 | No cumple | Los runs exitosos del sincronizador de issues no sustituyen el CI. |
| Logs estructurados | No se encontró `structlog`, Winston, Pino, Serilog, JSON formatter ni configuración equivalente. | No cumple | — |
| Métrica consultable asociada a un escenario de calidad | No se encontró endpoint o tablero de métricas del entorno ligado a un escenario. | No cumple | La analítica funcional no es una métrica operativa consultable del despliegue. |
| Secretos fuera del código y tomados del entorno o del almacén | El CI usa `${{ secrets.SONAR_TOKEN }}`, pero la API key de Google se recibe por constructor y el README no documenta su origen seguro en despliegue; no existe `.env.example`. | No cumple | Falta la configuración reproducible del secreto de la aplicación. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No se encontró cálculo mensual por volumen ni punto de ruptura de APIs o plataforma. | No cumple | — |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07_deployment_view.adoc:43-97` conserva marcadores de plantilla sin piezas reales. | No cumple | — |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02_architecture_constraints.adoc:20-27` declara equipo sin presupuesto y uso de capas gratuitas. | Cumple | No se declara restricción adicional de tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | No hay ADR de plataforma de despliegue; el ADR 0006 trata límites de contexto. | No cumple | — |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon público sin autenticación. | Cumple | — |
| Estructura mínima presente | Las seis rutas mínimas existen en `7048021`. | Cumple | — |
| Estado calificado identificable | `origin/master`, `7048021`, 2026-09-22T10:10:19-05:00. | Cumple | Estado preliminar elegible. |
| Nombres de ADR según la convención | Seis ADR con nombres válidos. | Cumple | — |
| ADR aceptados no reescritos | El ADR 0001 conserva múltiples reescrituras sin reemplazo. | No cumple | — |
| `docs/ia.md` al día para la semana | Última actualización del 2026-08-30. | No cumple | — |
| Pipeline, SonarCloud y Quality Gate públicos | El workflow invoca scanner y Quality Gate, pero el run del hash revisado falló y no se aportó URL pública del análisis. | No cumple | — |
| Sin credenciales en el repositorio ni en el historial | Barrido sin coincidencias materiales. | Cumple | — |
| Contribución de todos los integrantes | Cuatro personas consolidadas en el historial. | Cumple | — |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `7048021965cf483d29ef199c57d50a914953ac55`.
- El trabajo posterior a S7 reforzó CI y SonarCloud, pero la punta está roja.
- No existe evidencia S8 de despliegue público, health, observabilidad, costo ni decisiones de plataforma.

## Recuento y nota sugerida

**2 de 12 criterios Cumple.**

**Nota sugerida preliminar (propuesta al docente): 1.7 = 1 + 4 × (2/12).** La nota final la fija el profesor en Moodle.

## No conformidades y pendientes

- Publicar la URL y health check, con evidencia HTTP fechada.
- Versionar la infraestructura y completar arc42 §7.
- Corregir el CI de la punta y publicar el análisis SonarCloud con Quality Gate.
- Incorporar logs estructurados, métrica consultable, manejo de la API key y estimación mensual de costo.
- Registrar ADR separados por cada decisión de plataforma.

## Hallazgos para la planilla

- Solo cumplen el procedimiento local del README y la restricción de costo gratuito.
- El CI más reciente está rojo y no hay entorno desplegado verificable.
