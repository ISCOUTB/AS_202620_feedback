# Semana 8 · Despliegue reproducible, CI y observabilidad · EnAgenda

> Revisión preliminar. El estado definitivo se fijará con el último commit de `master` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `6db7cd9` en `origin/master` (2026-09-21T02:53:08-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación de URL | 2026-09-24T08:10:25-05:00 |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md` solo publica `http://127.0.0.1:5000`; `docs/api/openapi.yaml` declara `http://localhost:5000`. | No cumple | No se declaró una URL pública que pudiera consultarse en la hora indicada. |
| Health check consultable | `app/web.py` expone `/`, `/invitacion/<token>` y `/api/v1/invitaciones/<token>`; no define `/health` ni otra ruta de salud. | No cumple | Se esperaba una ruta declarada y un código HTTP observable. |
| Infraestructura como código versionada en el repositorio | El árbol no contiene `Dockerfile`, Compose, Terraform, manifiestos, `render.yaml`, `fly.toml` ni `Procfile`. | No cumple | `.github/workflows/ci.yml` ejecuta pruebas, pero no describe el entorno de despliegue. |
| El entorno se puede recrear siguiendo el README | `README.md` documenta Python 3.13, `pip install -r requerimiento.txt`, `pytest -q` y `python app\\web.py`. | Cumple | El entorno local es reproducible; todavía no existe procedimiento para un entorno público. |
| Pipeline en verde sobre la rama principal | Run `CI` de `6db7cd9`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/35575083849. | Cumple | El workflow instala dependencias y ejecuta `pytest -q`. |
| Logs estructurados | No se encontró configuración de `structlog`, `logging` con JSON ni campos estructurados; Flask conserva su salida por defecto. | No cumple | Se esperaba archivo de configuración y ejemplo de línea con campos. |
| Métrica consultable asociada a un escenario de calidad | No hay endpoint, colector ni nombre de métrica en código o documentación. | No cumple | Falta vincular una métrica observable con un escenario de calidad. |
| Secretos fuera del código y tomados del entorno o del almacén | `docs/arc42/02- restricciones.md` promete variables de entorno, pero el árbol no contiene `.env.example`, lectura de configuración sensible ni referencia a un almacén de secretos. | No cumple | El barrido de patrones no encontró credenciales, pero falta la evidencia positiva de configuración segura. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | La restricción R-05 exige capa gratuita, sin volumen, cálculo por pieza ni punto de ruptura. | No cumple | Una preferencia por costo cero no sustituye la estimación pedida. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07-vista-de-despliegue.md` indica que la sección se completará durante el desarrollo. | No cumple | No hay vista de despliegue. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02- restricciones.md`, R-05: herramientas gratuitas o de capa gratuita y sin exigir cuentas personales de pago. | Cumple | La restricción fija costo cero y evita depender de una cuenta de pago. |
| Un ADR por decisión de plataforma, con alternativa descartada | Los ADR 0001 y 0002 tratan estilo e integración; no existe ADR de plataforma de despliegue. | No cumple | Se esperaba una decisión de alojamiento con alternativas y consecuencias. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación desde `ISCOUTB/AS_202620_EnAgenda`. |
| Estructura mínima presente | Cumple | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md` presentes. |
| Estado calificado identificable | Cumple | `origin/master`, `6db7cd9`, 2026-09-21T02:53:08-05:00. |
| Nombres de ADR según la convención | Cumple | `0001-usar-monolito-modular.md` y `0002-estrategia-integracion-api.md`. |
| ADR aceptados no reescritos | Cumple | Cada ADR aceptado tiene una sola revisión en su ruta actual. |
| `docs/ia.md` al día para la semana | No cumple | Último cambio en `0a58de8` del 2026-09-13; no registra S8. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | CI en verde, pero sin scanner, proyecto público ni Quality Gate de SonarCloud. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin `.env` versionado ni coincidencias de patrones de claves en el estado revisado. |
| Contribución de todos los integrantes | Cumple | El historial permite consolidar tres integrantes; una identidad adicional corresponde a una persona ya contabilizada. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `6db7cd9` en `origin/master`.
- **Veredicto:** con no conformidades.
- El proyecto conserva contrato, pruebas y CI local reproducible, pero no presenta despliegue público, health check, infraestructura como código, observabilidad ni estimación de costos.

## Recuento y nota sugerida

3 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente): 2.0 = 1 + 4 × (3/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Publicar y declarar una URL verificable con health check.
- Versionar la infraestructura y documentar la recreación del entorno público.
- Añadir logs estructurados, una métrica ligada a un escenario y protección operativa de secretos.
- Completar arc42 §7, costo mensual y ADR de plataforma.
