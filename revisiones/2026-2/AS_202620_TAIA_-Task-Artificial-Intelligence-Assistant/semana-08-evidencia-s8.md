# semana-08-evidencia-s8 · TAIA

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `f818f75` en `origin/main` (2026-09-22T09:20:59-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | HEAD f818f75 (2026-09-22); README.md solo declara http://127.0.0.1:8000 y docs/arc42/07-vista-de-despliegue.md describe el arranque local con Uvicorn. | No cumple | No se aportó URL pública ni código de respuesta; no fue posible ejecutar el curl de comprobación. |
| Health check consultable | README.md declara GET /health con respuesta esperada {"status": "ok"}. | No verificado | Sin URL desplegada no se obtuvo código de respuesta; falta curl a $URL/health y la hora de la comprobación. |
| Infraestructura como código versionada en el repositorio | Árbol de f818f75: no hay Dockerfile, docker-compose, .tf, .tfvars, k8s/, helm/, fly.toml, render.yaml ni Procfile; solo .github/workflows/ci.yml. | No cumple | El despliegue documentado es un procedimiento manual (uvicorn backend.app.main:app --reload), no IaC. |
| El entorno se puede recrear siguiendo el README | README.md: secciones Requisitos (Python 3.14 y backend/requirements.txt), Ejecución (.\\run.bat) y Pruebas (pytest backend/tests); existe backend/requirements.lock.txt. | Cumple | Reproduce el entorno local del backend, no un entorno desplegado. |
| Pipeline en verde sobre la rama principal | Existe .github/workflows/ci.yml en f818f75; no se aportó ningún run. | No verificado | Falta URL del run, rama y conclusión; comprobar con curl a api.github.com/repos/ISCOUTB/$REPO/actions/runs. |
| Logs estructurados | El árbol completo de f818f75 no contiene configuración de registro (structlog, winston, pino, dictConfig ni equivalente) y ninguna línea de log con campos fue citada. | No cumple | Falta el archivo de configuración y un ejemplo de línea estructurada. |
| Métrica consultable asociada a un escenario de calidad | El árbol de f818f75 no contiene código de métricas (ni /metrics ni cliente de Prometheus u otro) y docs/ no asocia ninguna métrica a un escenario de calidad. | No cumple | Sin métrica no hay escenario asociado que validar. |
| Secretos fuera del código y tomados del entorno o del almacén | backend/app/modules/ai/adapters/outbound/gemini_llm.py:95 lee GEMINI_API_KEY del entorno, telegram_bot_client.py:12 lee TAIA_TELEGRAM_BOT_TOKEN y jwt_token_service.py:23 toma el secreto del entorno; envs_versionados vacío. | Cumple | No hay .env versionado ni credenciales embebidas; falta .env.example y, al no existir despliegue, no se puede comprobar el almacén del proveedor. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No existe documento de costos en el árbol de f818f75; docs/arc42/02-restricciones-de-arquitectura.md solo declara la restricción «costo cero». | No cumple | Falta el volumen supuesto, el costo por pieza y el punto donde se rompe la capa gratuita. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | docs/arc42/07-vista-de-despliegue.md: diagramas con cajas por pieza (7.1 y 7.2.1) y tabla 7.2.2 que indica dónde se ejecuta cada módulo (proceso FastAPI/Uvicorn). | Cumple | Documenta el corte local, no un entorno desplegado. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | docs/arc42/02-restricciones-de-arquitectura.md recoge la restricción «Costo cero: toda la infraestructura opera dentro de capas gratuitas» con sus implicaciones. | Cumple | No se recoge explícitamente la restricción de «sin tarjeta», que solo aplica si el proveedor la exige. |
| Un ADR por decisión de plataforma, con alternativa descartada | docs/adr/ solo contiene 0001-estilo-arquitectonico.md y 0002-estrategia-integracion-api-sincrona.md; docs/arc42/07-vista-de-despliegue.md afirma que la decisión de proveedor «queda pendiente de documentarse mediante un ADR específico». | No cumple | No hay ningún ADR de plataforma ni verificación de capa gratuita por pieza. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant en la organización ISCOUTB, público; historial con las cuentas val, dei0811, luis20072002, Luis Mendoza, mark y valeria-estefania. | Cumple | Los cuatro integrantes declarados tienen commits; hay cuentas repetidas de una misma identidad que se consolidan sin atribuir por parecido de nombre. |
| Estructura mínima | Árbol de f818f75: README.md, docs/arc42/ (secciones 01 a 12 más arc42.md), docs/adr/, docs/c4/ (C4-C1, C4-C2, C4-C3), docs/aspectos.md y docs/ia.md. | Cumple | Todo en Markdown y en las rutas del contrato. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-estrategia-integracion-api-sincrona.md siguen NNNN-titulo-en-kebab-case e incluyen contexto, opciones, decisión, consecuencias y trazabilidad. | Cumple | Solo dos ADR y ninguno reemplazado ni de plataforma. |
| La tabla de aspectos | docs/aspectos.md existe en f818f75. | No verificado | No se incluyó su contenido: no se pudieron comprobar las ocho columnas ni que cada celda sea navegable. |
| Registro de uso de IA | docs/ia.md con 10 commits entre 2026-08-07 y 2026-09-16. | No verificado | El archivo crece a lo largo del semestre, pero no se incluyó su contenido: falta comprobar qué se rechazó y por qué. |
| README | README.md describe qué es el sistema, requisitos previos, arranque con .\\run.bat, health check en /health y pruebas con pytest backend/tests. | Cumple | Declara 74 pruebas pasando, pero eso no es evidencia de ejecución en CI. |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml, pero no hay sonar-project.properties, ni URL de run, ni URL pública del análisis en SonarCloud. | No cumple | Faltan las tres evidencias que el contrato exige para marcar esta fila como Cumple. |
| Secretos | El barrido sobre f818f75 no encuentra credenciales: solo lecturas de variables de entorno (gemini_llm.py:95, telegram_bot_client.py:12, jwt_token_service.py:23) y lista de .env versionados vacía. | Cumple | Las coincidencias son nombres de parámetros y campos, no secretos. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `f818f750b51e82acfac73099e3f980cb983db78c 2026-09-22T09:20:59-05:00 Fix spelling of 'Gonzales' to 'Gonzalez'`
- **Veredicto**: al dia
- Resumen: Repositorio público, estructura, README, ADR y manejo de secretos correctos, con el backend modular funcionando en local; el objetivo de la semana no se cumple: no hay URL pública, ni infraestructura como código, ni pipeline verificable, ni observabilidad, ni estimación de costo. La entrega es anticipada (f818f75, 2026-09-22) y no hay commits posteriores al cierre en origin/main.

Pendientes que siguen abiertos:
- Publicar el sistema en una URL accesible desde fuera de la red de la universidad y registrar hora y código de respuesta.
- Versionar infraestructura como código para recrear el entorno con un solo comando.
- Dejar el pipeline en verde y aportar la URL del run con su conclusión.
- Añadir logs estructurados y una métrica consultable asociada a un escenario de calidad.
- Documentar la estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita.
- Escribir un ADR por decisión de plataforma con alternativa descartada y capa gratuita verificada.
- Declarar variables de entorno en .env.example y tomar sus valores del almacén del proveedor.
- Aportar el contenido de docs/aspectos.md y docs/ia.md para verificar su trazabilidad.

## Recuento y nota sugerida

4 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.3 = 1 + 4 × (4/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Health check: sin URL no se obtuvo código de respuesta; hace falta curl a $URL/health con hora.
- Pipeline: faltan URL, rama y conclusión del último run de GitHub Actions sobre main.
- SonarCloud: falta la URL pública del análisis y el estado del Quality Gate.
- docs/aspectos.md: falta el contenido para comprobar las ocho columnas y su trazabilidad.
- docs/ia.md: falta la columna de lo rechazado con su motivo técnico.
- Secretos en despliegue: sin entorno desplegado no se puede comprobar el almacén del proveedor.

## Hallazgos para la planilla

- El sistema no está desplegado: no hay URL pública y todo apunta a http://127.0.0.1:8000.
- No existe infraestructura como código; el arranque documentado es un procedimiento local manual.
- No hay evidencia ejecutable del pipeline: sin run, sin conclusión y sin análisis estático auditable.
- No hay logs estructurados ni métricas consultables asociadas a un escenario.
- Falta la estimación de costo mensual con volumen supuesto y punto de ruptura de la capa gratuita.
- Falta un ADR de plataforma; solo hay ADR de estilo arquitectónico e integración de API.
- Los documentos de aspectos y de uso de IA existen, pero su contenido no se pudo verificar.
- Entrega anticipada el 2026-09-22 y sin commits posteriores al cierre en origin/main.
