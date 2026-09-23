# semana-08-evidencia-s8 · DinamikUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `65202f2` en `origin/master` (2026-09-21T22:51:09-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | README.md (65202f2) solo declara http://127.0.0.1:8000 y el árbol de 65202f2 no incluye fly.toml, render.yaml, Procfile ni Dockerfile. | No cumple | No se declaró URL alguna, así que el curl de la ficha no se pudo ejecutar ni dejar hora de comprobación; no se aporta captura como sustituto. |
| Health check consultable | docs/api/openapi.json (65202f2) expone solo /, /estudiantes/{codigo_estudiantil}, /requisitos/{estudiante_id} y PUT /requisitos/{requisito_id}/estado. | No cumple | No hay ruta de health declarada ni código de respuesta que citar. |
| Infraestructura como código versionada en el repositorio | El listado de 65202f2 no contiene Dockerfile, docker-compose, .tf/.tfvars, k8s/, helm/, fly.toml, render.yaml ni Procfile; solo .github/workflows/ci.yml. | No cumple | No hay descripción del entorno como código. |
| El entorno se puede recrear siguiendo el README | README.md sección «Inicio Rápido» con el comando único start.bat, requisitos previos declarados y secciones de pruebas (pytest, flutter test, flutter analyze). | Cumple | Documenta arranque y prueba locales; no describe entorno desplegado porque no existe. |
| Pipeline en verde sobre la rama principal | La evidencia entregada no incluye runs_ci; docs/api/evidencia-prueba-contrato.md cita el run 35553215099 como «Verde», sin hash ni rama atados a 65202f2. | No verificado | Falta el listado de runs: curl -s "https://api.github.com/repos/ISCOUTB/AS_202620_DinamikUTB/actions/runs?per_page=10" para citar nombre, conclusión y URL del último run sobre master. |
| Logs estructurados | Ningún archivo del árbol de 65202f2 corresponde a configuración de logging (structlog, pino, winston, logback, serilog) ni hay línea de ejemplo citada. | No cumple | No se aportó la salida del git grep de logging; hoy no hay configuración citable. |
| Métrica consultable asociada a un escenario de calidad | docs/api/openapi.json (65202f2) no expone /metrics y el árbol no contiene archivos de métricas (Prometheus/OpenTelemetry) ni documento que ligue una métrica a un escenario. | No cumple | No se nombra métrica ni escenario asociado. |
| Secretos fuera del código y tomados del entorno o del almacén | Barrido de secretos sobre 65202f2 sin coincidencias y ningún .env versionado, pero no existe .env.example en el árbol ni referencias a secrets en .github/workflows/ci.yml. | No cumple | Se cumple la parte de «sin credenciales versionadas»; falta la declaración de variables y su toma del almacén del proveedor. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | Ningún documento del árbol de 65202f2 (README.md, docs/, correcciones.md) contiene volumen supuesto, cálculo por pieza ni punto de ruptura de la capa gratuita. | No cumple | No hay documento de costos. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | docs/arc42/07-deployment-view.md existe en el árbol de 65202f2, pero su contenido no se aportó en la evidencia. | No verificado | Hace falta el texto de la sección 7 para comprobar una caja por pieza y el sitio de ejecución. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | docs/arc42/02-architecture-constraints.md (2.1 a 2.4) enumera restricciones técnicas, organizativas y legales sin límite de costo ni restricción de «sin tarjeta». | No cumple | La tabla 2.4 no incluye ninguna fila de costo. |
| Un ADR por decisión de plataforma, con alternativa descartada | docs/adr/0001 a 0004 deciden estilo arquitectónico, stack backend/frontend, motor de base de datos y comunicación síncrona; ninguno decide plataforma de despliegue. | No cumple | No hay ADR de plataforma ni verificación de capa gratuita. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo público ISCOUTB/AS_202620_DinamikUTB; en 65202f2 se consolidan cuatro identidades de autor (las cuentas 404Vargas, JuanchisV y «Juan José Vargas Pérez» comparten identidad; Daniel-dev02 y «LUIS DANIEL» comparten identidad) que coinciden con los cuatro integrantes declarados. | Cumple | Nombre conforme a AS_202620_<PROYECTO> y visibilidad pública. |
| Estructura mínima | El árbol de 65202f2 contiene docs/arc42/01 a 12, docs/adr/, docs/c4/*.puml y *.png, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Se añade docs/api/ como material extra, sin desviación de la ruta mínima. |
| Convenciones de ADR | docs/adr/ solo tiene 0001-seleccion-monolito-modular.md, 0002-seleccion-tecnologia-backend-frontend.md, 0003-seleccion-motor-de-base-de-datos.md y 0004-comunicacion-sincrona-frontend-backend.md, todos con contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | No se aportó log --follow por ADR para verificar que un ADR aceptado no se reescribió. |
| Tabla de aspectos | docs/aspectos.md existe en 65202f2 y varios ADR enlazan anclas A-01 y A-02, pero no se aportó su contenido. | No verificado | Hace falta el archivo para ver las ocho columnas y que cada celda sea navegable. |
| Registro de uso de IA | docs/ia.md existe y crece a lo largo del semestre (última entrada 2026-09-20, commit aa35148), pero no se aportó su contenido. | No verificado | Falta el texto para verificar qué se rechazó y por qué. |
| README | README.md describe el sistema, el arranque con un solo comando (start.bat), los requisitos previos y cómo se prueba (pytest, flutter test). | Cumple | Sin pasos manuales ocultos declarados. |
| Pipeline y análisis estático | Existen .github/workflows/ci.yml y sonar-project.properties en 65202f2, pero no hay URL pública del análisis en SonarCloud con estado del Quality Gate ni runs_ci que aten un run verde a 65202f2. | No cumple | No conformidad del apartado 8: falta la tercera evidencia obligatoria y faltan las otras dos en la entrega. |
| Secretos | Barrido de secretos sobre 65202f2 sin coincidencias y sin .env versionado (envs_versionados vacío). | Cumple | No se hallaron credenciales en el historial revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `65202f28aec8bf65b192ba57cce5240b99b173d2 2026-09-21T22:51:09-05:00 Merge pull request #32 from ISCOUTB/workArea-Luis`
- **Veredicto**: con pendientes
- Resumen: A HEAD de master (65202f2, 2026-09-21T22:51:09-05:00) el proyecto mantiene lo construido hasta S7 (monolito modular, ADR, pruebas, contrato OpenAPI versionado y workflow de CI) pero la entrega de S8 está prácticamente ausente: sin despliegue, sin IaC, sin health check, sin observabilidad, sin secretos gestionados por proveedor y sin costos.

Pendientes que siguen abiertos:
- Publicar URL del sistema accesible desde fuera de la red universitaria, con hora de comprobación.
- Health check consultable y su código de respuesta.
- Infraestructura como código versionada (Dockerfile/compose o IaC del proveedor).
- Logs estructurados y métrica consultable ligada a un escenario de calidad.
- Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita.
- arc42 §7 con una caja por pieza y §2 con límite de costo y restricción de tarjeta.
- Un ADR por decisión de plataforma con alternativa descartada.
- Pendiente desde S6: URL pública del análisis en SonarCloud con estado del Quality Gate.

## Recuento y nota sugerida

1 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.3 = 1 + 4 × (1/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Pipeline en verde sobre la rama principal: la evidencia no incluye runs_ci; verificar con curl -s "https://api.github.com/repos/ISCOUTB/AS_202620_DinamikUTB/actions/runs?per_page=10".
- arc42 sección 7 (deployment view): el archivo existe en 65202f2 pero no se aportó su contenido para comprobar una caja por pieza y dónde se ejecuta.
- Tabla de aspectos: docs/aspectos.md existe pero no se aportó su contenido para verificar columnas y navegabilidad.
- Registro de IA: docs/ia.md existe y crece, pero falta su contenido para verificar la columna de lo rechazado y su motivo.
- Comprobación de la URL desde fuera de la red: no se declaró URL, por lo que los curl de la ficha no se pudieron ejecutar ni datar.

## Hallazgos para la planilla

- El commit calificado 65202f2 (2026-09-21T22:51:09-05:00, origin/master) no contiene ninguna pieza de despliegue ni infraestructura como código.
- No se declaró URL del sistema: el README solo publica direcciones locales 127.0.0.1, por lo que no hubo comprobación externa ni hora que registrar.
- No existe endpoint de health check en docs/api/openapi.json.
- No hay logs estructurados, ni métrica ligada a un escenario, ni estimación de costo mensual en el árbol.
- La sección 2 de arc42 no recoge límite de costo ni restricción de «sin tarjeta».
- No hay ADR de plataforma: los cuatro ADR deciden estilo, stack, motor de datos y comunicación.
- SonarCloud sigue sin URL pública con Quality Gate pese a existir sonar-project.properties.
- Sin commits posteriores al cierre y sin commits nuevos desde el cierre anterior.
