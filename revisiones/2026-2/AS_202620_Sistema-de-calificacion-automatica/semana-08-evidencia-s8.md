# semana-08-evidencia-s8 · Calificación automática

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `2269ca5` en `origin/master` (2026-09-20T21:48:00-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | No se aporta URL ni salida de curl; el arbol de HEAD 2269ca5 no incluye artefacto de despliegue en nube (fly.toml, render.yaml, .tf). | No verificado | Sin URL no hay codigo de respuesta ni hora de comprobacion que registrar. |
| Health check consultable | README.md declara 'salud en /health' en la seccion Cómo se arranca, pero no hay codigo HTTP de respuesta en la evidencia. | No verificado | Falta el codigo de respuesta de la ruta declarada y la hora de la comprobacion. |
| Infraestructura como codigo versionada en el repositorio | HEAD 2269ca5 incluye docker-compose.yml, backend/Dockerfile, frontend/Dockerfile y .github/workflows/ci.yml. | Cumple | Describe el entorno (API, worker, Redis, Postgres, frontend) y no una lista de pasos manuales. |
| El entorno se puede recrear siguiendo el README | README.md, seccion 'Cómo se arranca': 'docker compose up', con requisitos previos y copia de .env.example. | Cumple | Un solo comando; las alternativas se declaran como no oficiales. |
| Pipeline en verde sobre la rama principal | Existe .github/workflows/ci.yml en HEAD, pero no hay runs_ci con conclusion ni URL en la evidencia. | No verificado | Falta el ultimo run de master; comando de la ficha anotado (api.github.com actions/runs). |
| Logs estructurados | README.md muestra una linea del worker con campos (trabajo=, examen=, archivo=, referencia=), pero no se aporta archivo de configuracion de logging. | No verificado | Falta la configuracion (structlog/pino/logback/etc.) o la busqueda que la cite. |
| Métrica consultable asociada a un escenario de calidad | backend/herramientas/medir_ec07.py y docs/evidencia/medicion-ec07.md (mas antes/despues/cola-caida.json) ligados a EC-07. | Cumple | La metrica de perdida silenciosa y latencia del lote de 200 hojas esta atada al escenario EC-07. |
| Secretos fuera del código y tomados del entorno o del almacén | .env.example en HEAD, envs_versionados vacio y barrido de secretos '(sin coincidencias)'. | Cumple | No se observan referencias a secrets en el workflow ni almacen externo; las variables vienen del entorno del compose. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | El arbol completo de HEAD 2269ca5 no contiene ningun documento de estimacion de costo. | No cumple | Falta volumen supuesto, costo por pieza y punto de ruptura de la capa gratuita. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | docs/arc42/arc42-template-ES.md declara: 'La unica pendiente es la 7 (Deployment View)'. | No cumple | No hay vista de despliegue ni caja por pieza con su ubicacion de ejecucion. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | La evidencia no aporta el contenido de arc42 seccion 2; solo el arbol y los ADR. | No verificado | No se puede confirmar el limite de costo ni la restriccion de 'sin tarjeta'. |
| Un ADR por decisión de plataforma, con alternativa descartada | docs/adr/ contiene 0001-0007, todos de arquitectura (monolito, asincronia, stack, SymPy, LLM, bitacora, contextos); ninguno decide plataforma de despliegue. | No cumple | Falta al menos un ADR de plataforma con su alternativa descartada y capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Sistema-de-calificacion-automatica en ISCOUTB, visible:true; cuatro cuentas en el historial (scp1109, josueacademico17-source, SusanaRosales, Mariadelmar-restrepo). | Cumple | La pertenencia a la organizacion no se puede comprobar; no se emparejan cuentas con personas por parecido de nombre. |
| Estructura mínima | HEAD 2269ca5 contiene docs/arc42/, docs/adr/, docs/c4/doc-c4.md, docs/aspectos.md, docs/ia.md y README.md. | Cumple | arc42 en un solo archivo Markdown y C4 en docs/c4/, ambas rutas aceptadas. |
| Qué estado del repositorio se califica | origin/master en 2269ca5, 2026-09-20T21:48:00-05:00, anterior al cierre 2026-09-28T05:00Z y sin commits post-cierre. | Cumple | Rama principal unica (master); se califica ese hash. |
| Convenciones de ADR | docs/adr/0001..0007 en kebab-case; 0001 marcado 'reemplazado por 0002' sin editarlo. | Cumple | Todos con contexto, alternativas, decision y consecuencias; la trazabilidad a commit/PR es parcial. |
| La tabla de aspectos | docs/aspectos.md existe en HEAD y los ADR citan sus filas (A-01, A-04, T-2). | No verificado | No se aporta su contenido: no se pueden comprobar las ocho columnas ni que cada celda sea navegable. |
| Registro de uso de IA | docs/ia.md existe y su historial crece (10 commits, 2026-08-07 a 2026-09-20, ultimo 2269ca5). | No verificado | No se aporta el contenido; falta comprobar que se rechazo y por que. |
| README | README.md describe que es, el arranque con un solo comando ('docker compose up') y como se prueba (pytest, flutter test). | Cumple | Declara requisitos previos: Docker con el plugin Compose. |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml, pero no hay sonar-project.properties en el arbol ni URL de run ni de Quality Gate publico. | No cumple | El contrato exige las tres evidencias; falta la de SonarCloud y el run del hash revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `2269ca5a1fa1b64787745a55f4d714070192a8f0 2026-09-20T21:48:00-05:00 docs(ia): registrar el uso de IA de la semana 7`
- **Veredicto**: con pendientes
- Resumen: A HEAD (master 2269ca5, 2026-09-20) el proyecto tiene codigo, ADR, IaC local y metrica ligada a EC-07, pero no acredita lo que este corte exige: sin URL publica ni health check comprobado, sin run de CI, sin seccion 7 de arc42, sin ADR de plataforma y sin estimacion de costo.

Pendientes que siguen abiertos:
- arc42 seccion 7 (Deployment View) con una caja por pieza y donde se ejecuta
- ADR por decision de plataforma con alternativa descartada y capa gratuita verificada
- Estimacion de costo mensual con volumen supuesto y punto de ruptura de la capa gratuita
- URL publica desplegada y health check con hora y codigo de respuesta
- Evidencia de pipeline en verde y de SonarCloud (configuracion, run y analisis publico)
- Limite de costo y restriccion de tarjeta en arc42 seccion 2
- Tabla de aspectos sin huecos (no verificable con la evidencia aportada)
- R-06 (persistencia) y V-5 (verificacion automatica de propiedad de datos) siguen abiertos

## Recuento y nota sugerida

4 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.3 = 1 + 4 × (4/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema accesible desde fuera de la red universitaria y su hora de comprobacion.
- Health check: codigo de respuesta de la ruta declarada (/health).
- Pipeline en verde: run de la rama principal con conclusion y URL (comando anotado en la ficha).
- Logs estructurados: archivo de configuracion de logging.
- arc42 seccion 2: limite de costo y restriccion de 'sin tarjeta' (contenido no aportado).
- docs/aspectos.md: contenido y celdas navegables.
- docs/ia.md: contenido y columna de lo rechazado con su motivo.

## Hallazgos para la planilla

- Entrega dentro del plazo (modo early) y sin commits posteriores al cierre.
- El historial no registra commits nuevos desde el cierre anterior.
- No se aporta URL del sistema ni comprobacion de health check con hora y codigo.
- No hay runs de CI en la evidencia: el pipeline no se puede acreditar.
- No existe ADR de plataforma de despliegue entre 0001 y 0007.
- La seccion 7 de arc42 sigue declarada como pendiente por el propio documento.
- No hay estimacion de costo mensual ni punto de ruptura de la capa gratuita.
- Sin sonar-project.properties ni analisis publico: falta la evidencia de SonarCloud.
- No se detectaron secretos en HEAD ni .env versionado.
- El contrato recibido no incluye el apartado 11; la matriz transversal se armo con los apartados 1 a 8.
