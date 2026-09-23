# semana-08-evidencia-s8 · Verifacts

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `7d52e8e` en `origin/master` (2026-09-22T22:42:51-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | docs/despliegue.md declara https://verifacts-api.onrender.com y https://verifacts-web.onrender.com, probadas desde datos móviles, sin hora ni código de respuesta. | No verificado | Falta la comprobación con hora: curl -sS -o /dev/null -w 'http=%{http_code} tiempo=%{time_total}s' $URL. |
| Health check consultable | docs/despliegue.md cita GET /health en app/api/routes.py y HEALTHCHECK en Dockerfile; sin código de respuesta registrado. | No verificado | Falta curl -sS -o /dev/null -w 'health=%{http_code}' $URL/health. |
| Infraestructura como código versionada en el repositorio | En 7d52e8e están Dockerfile, .dockerignore y render.yaml; docs/despliegue.md lo describe como blueprint aplicado en Render. | Cumple | Describe el entorno (Web Service + Static Site), no pasos manuales. |
| El entorno se puede recrear siguiendo el README | README.md §4 indica arranque con python run.py y npm run dev, comprobación de GET /health y pruebas con pytest. | Cumple | No hay comando único ni requisitos previos; el ancla README#corte-vertical-ejecutable citada en docs no aparece en el contenido entregado. |
| Pipeline en verde sobre la rama principal | Existen .github/workflows/tests.yml y sonarcloud.yml en 7d52e8e, pero no se aportó ningún run ni su conclusión. | No verificado | Comando anotado: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_Verifacts/actions/runs?per_page=10. |
| Logs estructurados | app/observability.py (JsonFormatter y middleware observe_requests) y tests/test_observability.py en 7d52e8e; docs/despliegue.md describe una línea JSON por petición. | Cumple | No se aportó la línea de ejemplo para citar. |
| Métrica consultable asociada a un escenario de calidad | docs/despliegue.md cita GET /metrics (formato Prometheus) en app/observability.py sin escenario asociado; docs/escenarios-de-calidad.md deja Q-01 como pendiente de medición de P95. | No cumple | Métrica de sistema sin escenario: incompleta según la ficha. |
| Secretos fuera del código y tomados del entorno o del almacén | .env.example y frontend/.env.example versionados en 7d52e8e, sin .env en el índice y barrido de secretos sin coincidencias; docs/despliegue.md indica variables configuradas en el panel de Render. | Cumple | No se aportó el grep de secrets.* en los workflows. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | docs/costos.md define supuestos (uso académico, sin disco persistente), total $0/mes, límite de 100 GB/mes y ruptura de la capa gratuita al requerir plan Starter para disco persistente. | Cumple | El costo del plan Starter queda por confirmar, sin cifra. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | docs/arc42/07-despliegue.md §7.1 afirma que se despliega localmente y que no existe entorno cloud; §7.3 deja el contenedor web fuera de alcance. | No cumple | Contradice Dockerfile y render.yaml; usa una sola caja local en vez de una por pieza. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | docs/arc42/02-restricciones.md §2.1–2.3 (R-ORG-01/03, R-TEC-01/04, R-ALC-01, R-DAT-01) no menciona límite de costo ni restricción de «sin tarjeta». | No cumple | Ambas restricciones se piden explícitamente en esta entrega. |
| Un ADR por decisión de plataforma, con alternativa descartada | docs/adr/ sólo contiene 0001-estilo-arquitectonico (2026-08-24), 0002-contextos-sin-cambios (2026-09-11) y 0003-integracion-sincrona (2026-09-15). | No cumple | Ningún ADR decide la plataforma (Render, Docker, plan gratuito). |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_Verifacts en la organización ISCOUTB y público (visible: true); autores en el historial: PedroC1213 y Cristian Cardeño. | No cumple | El tercer integrante declarado no aparece en el historial; sólo dos cuentas visibles. |
| Estructura mínima | En 7d52e8e existen docs/arc42/ (01 a 11), docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | No hay archivo 12-glosario separado: el glosario vive en docs/arc42/11-glosario.md. |
| Convenciones de ADR | docs/adr/0001 a 0003 siguen el patrón NNNN-titulo-en-kebab-case y 0001 y 0003 incluyen contexto, opciones, decisión y consecuencias. | Cumple | Falta el enlace al commit o PR que implementa cada decisión. |
| Tabla de aspectos | docs/aspectos.md deja la fila A-04 con verificación manual y el propio texto admite que la columna CI de A-00 aún tiene un marcador por reemplazar. | No cumple | Fila con huecos: no defendible según el contrato. |
| Registro de uso de IA | docs/ia.md existe y evoluciona (commits del 2026-08-18, 2026-08-24 en dos ocasiones y 2026-09-08). | No verificado | No se aportó el contenido, así que no se puede comprobar qué se rechazó y por qué. |
| README | README.md describe qué es el sistema, arranque con python run.py y npm run dev, y pruebas con pytest. | Cumple | Sin comando único ni requisitos previos, y el ancla corte-vertical-ejecutable no aparece en el contenido entregado. |
| Pipeline y análisis estático | Existen .github/workflows/tests.yml, .github/workflows/sonarcloud.yml y sonar-project.properties en 7d52e8e. | No verificado | Faltan la URL del run y la URL pública del análisis en SonarCloud con estado del Quality Gate. |
| Secretos | Sin .env versionado (envs_versionados vacío), barrido de secretos sin coincidencias y .env.example presente en raíz y en frontend/. | Cumple | Estado limpio en el commit revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `7d52e8ef5f39ecd76cf95b9f7ccacc42257c4f5c 2026-09-22T22:42:51-05:00 docs: estimacion de costo mensual del despliegue`
- **Veredicto**: con pendientes
- Resumen: En HEAD 7d52e8e (2026-09-22, antes del cierre) el repositorio ya tiene IaC, secretos fuera del código, logs JSON y estimación de costos, pero la entrega S8 no se puede cerrar: no hay comprobación con hora de la URL ni del health, faltan runs de CI y la URL de SonarCloud, no hay ADR de plataforma y arc42 §7 y §2 no reflejan el despliegue real; la métrica publicada no se ata a ningún escenario.

Pendientes que siguen abiertos:
- Comprobar URL y /health con hora y código de respuesta.
- Aportar run de CI en verde y URL pública de SonarCloud con Quality Gate.
- Actualizar arc42 §7 con una caja por pieza y su ubicación de ejecución.
- Añadir límite de costo y restricción de tarjeta en arc42 §2.
- Registrar un ADR por decisión de plataforma con alternativa descartada y capa gratuita verificada.
- Asociar la métrica /metrics a un escenario de calidad y completar la medición de P95.
- Cerrar los huecos de docs/aspectos.md y corregir las secciones 3 y 10 desactualizadas.
- Incluir un integrante declarado que aún no aparece en el historial.

## Recuento y nota sugerida

5 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.7 = 1 + 4 × (5/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL desplegada: falta código HTTP y hora; comando curl -sS -o /dev/null -w 'http=%{http_code} tiempo=%{time_total}s' $URL.
- Health check: falta código de respuesta; comando curl -sS -o /dev/null -w 'health=%{http_code}' $URL/health.
- Pipeline: sin runs; comando curl -s https://api.github.com/repos/ISCOUTB/AS_202620_Verifacts/actions/runs?per_page=10.
- SonarCloud: falta la URL pública del análisis y el estado del Quality Gate para el hash revisado.
- docs/ia.md: sin contenido entregado, no se puede verificar la columna de lo rechazado y su motivo.
- Logs estructurados: falta una línea de ejemplo de app/observability.py para citarla.

## Hallazgos para la planilla

- Sin comprobación con hora de la URL ni de /health: la accesibilidad externa no queda demostrada.
- No hay runs de CI en la evidencia: el pipeline en verde no es verificable aunque existan los workflows.
- docs/arc42/07-despliegue.md sigue describiendo un despliegue sólo local y contradice Dockerfile y render.yaml.
- La sección 2 no recoge el límite de costo ni la restricción de «sin tarjeta».
- No existe ningún ADR de plataforma o despliegue; los tres ADR son de arquitectura e integración.
- La métrica /metrics no se asocia a ningún escenario Q-01 a Q-05.
- El tercer integrante declarado no tiene commits en el historial de la rama principal.
- La tabla de aspectos tiene huecos: A-04 sin prueba automatizada y la celda CI de A-00 con marcador pendiente.
- Documentación desactualizada en arc42 §3 y §10, que aún niegan la extracción por URL y la interfaz web ya implementadas.
- No se aportó el grep de secretos en los workflows ni una línea de ejemplo de los logs.
