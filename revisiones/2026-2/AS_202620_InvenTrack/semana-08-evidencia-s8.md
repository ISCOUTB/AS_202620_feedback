# Semana 8 · Despliegue reproducible, CI y observabilidad · InvenTrack

> Revisión preliminar. El estado definitivo se fijará con el último commit de `main` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `f62ad34` en `origin/main` (2026-09-23T02:02:36-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación de URL | 2026-09-24T08:10:25-05:00 |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md` declara hosting «Por definir» y solo publica `http://127.0.0.1:8000`. | No cumple | No se declaró una URL pública. |
| Health check consultable | `app/main.py` implementa GET `/health`, pero solo es consultable en el servidor local documentado. | No cumple | Falta evidencia HTTP desde un entorno público. |
| Infraestructura como código versionada en el repositorio | No hay `Dockerfile`, Compose, Terraform, manifiestos ni archivo de proveedor. | No cumple | El workflow de CI no describe el entorno de ejecución productivo. |
| El entorno se puede recrear siguiendo el README | `README.md` documenta Python 3.11, instalación con `requirements.txt`, Uvicorn y pytest. | Cumple | El procedimiento reproduce el entorno local, no un despliegue público. |
| Pipeline en verde sobre la rama principal | Run `Run Tests` para `f62ad34`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/35829673280. | Cumple | Ejecuta pytest con cobertura, SonarCloud y la prueba contractual. |
| Logs estructurados | No se encontró configuración de logging JSON ni campos estructurados en `app/`. | No cumple | Falta archivo de configuración y ejemplo de línea. |
| Métrica consultable asociada a un escenario de calidad | La documentación menciona p95 y concurrencia, pero no existe instrumentación o endpoint consultable. | No cumple | Las mediciones de prueba no sustituyen una métrica del entorno desplegado. |
| Secretos fuera del código y tomados del entorno o del almacén | `.github/workflows/test.yml` consume `GITHUB_TOKEN` y `SONAR_TOKEN` desde `secrets.*`; no hay `.env` versionado ni patrones de credenciales. | Cumple | La evidencia cubre los secretos del pipeline; no hay aún configuración de despliegue. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | La restricción C5 indica que no hay presupuesto, sin cálculo de consumo ni punto de ruptura. | No cumple | Falta estimación por pieza y volumen. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `Deployment View` dibuja una aplicación FastAPI/Uvicorn en máquina local y declara pendiente el hosting productivo. | No cumple | No representa el entorno público pedido para S8. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `Architecture Constraints`, C5: no hay presupuesto para servicios de pago. | Cumple | El límite de costo está explícito; no se documenta una condición separada de tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | Los ADR 0001–0004 cubren estilo, concurrencia, integración y contrato; no hay ADR de plataforma de despliegue. | No cumple | El hosting sigue «Por definir». |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación desde `ISCOUTB/AS_202620_InvenTrack`. |
| Estructura mínima presente | Cumple | Las seis rutas documentales mínimas están presentes. |
| Estado calificado identificable | Cumple | `origin/main`, `f62ad34`, 2026-09-23T02:02:36-05:00. |
| Nombres de ADR según la convención | Cumple | ADR 0001–0004 siguen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | No verificado | Varios ADR aceptados tienen múltiples revisiones; hace falta establecer en qué commit fueron aceptados para juzgar cambios posteriores. |
| `docs/ia.md` al día para la semana | No cumple | Último cambio en `1ecdcc8` del 2026-09-20; los cambios del 22–23 de septiembre no aparecen registrados. |
| Pipeline, SonarCloud y Quality Gate públicos | Cumple | El workflow ejecuta scanner; README enlaza el proyecto público y el Quality Gate, y el run de `f62ad34` terminó en verde. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin `.env` ni coincidencias de patrones de claves en el estado revisado. |
| Contribución de todos los integrantes | Cumple | El historial permite consolidar las cuatro identidades declaradas; los alias se agruparon por evidencia del historial. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `f62ad34` en `origin/main`.
- **Veredicto:** con no conformidades.
- El pipeline y SonarCloud están en verde, y las correcciones de S7 quedaron documentadas; S8 sigue sin hosting, IaC, logs estructurados, métricas ni costo mensual.

## Recuento y nota sugerida

4 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente): 2.3 = 1 + 4 × (4/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Elegir y desplegar una plataforma con URL y health check públicos.
- Versionar la infraestructura y completar la vista de despliegue productiva.
- Instrumentar logs y una métrica ligada a escenario.
- Estimar costo por volumen y registrar la decisión en un ADR.
