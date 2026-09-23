# semana-08-evidencia-s8 · Drift

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `9334a03` en `origin/master` (2026-09-20T20:19:47-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | README.md solo documenta http://localhost:3000 y http://localhost:8000 y el arbol de HEAD 9334a03 no contiene URL publica ni archivos de despliegue. | No cumple | No hay URL declarada ni hora de comprobacion posible. |
| Health check consultable | docs/api/drift/openapi.yaml define GET / con HealthResponse y existe backend/tests/test_health.py, pero no hay entorno desplegado donde consultarlo. | No cumple | No se cumple el codigo de respuesta en vivo; el equipo no declara una ruta /health. |
| Infraestructura como codigo versionada en el repositorio | El arbol de HEAD 9334a03 no incluye Dockerfile, docker-compose, *.tf, *.tfvars, k8s/, helm/, Procfile ni fly.toml; solo .github/workflows/ci.yml y scripts/start.py. | No cumple | El arranque depende de pasos manuales documentados en el README. |
| El entorno se puede recrear siguiendo el README | README.md contiene Requisitos previos, Instalacion y 'Comando Unico de Ejecuccion' con python scripts/start.py, y scripts/start.py esta versionado en HEAD. | Cumple | Reproducible en local; no describe un entorno desplegado. |
| Pipeline en verde sobre la rama principal | Existen .github/workflows/ci.yml y sonar-project.properties, pero la evidencia no incluye runs_ci con conclusion ni URL. | No verificado | Comprobar con curl a api.github.com/repos/ISCOUTB/AS_202620_Drift/actions/runs sobre master. |
| Logs estructurados | El arbol de HEAD 9334a03 no contiene configuracion de registro (structlog, winston, pino, logback, serilog ni formatter JSON). | No cumple | No hay archivo de configuracion ni linea de ejemplo que citar. |
| Metrica consultable asociada a un escenario de calidad | scripts/k6_baseline.js y docs/evidencias/e1-linea-base.md reportan p95 1.24 s para E1, pero no hay metrica expuesta ni entorno desplegado donde consultarla. | No cumple | El escenario esta asociado (E1); falta la metrica consultable en ejecucion. |
| Secretos fuera del codigo y tomados del entorno o del almacen | El barrido no encontro coincidencias y envs_versionados esta vacio, pero el arbol no incluye .env.example ni configuracion de despliegue. | No cumple | No se puede citar la declaracion de variables ni su toma desde un almacen. |
| Estimacion de costo mensual con supuestos y punto de ruptura de la capa gratuita | El arbol de HEAD 9334a03 no contiene documento de costos y ni README.md ni docs/ mencionan volumen supuesto ni capa gratuita. | No cumple | No hay calculo ni punto de ruptura que revisar. |
| arc42 seccion 7 con una caja por pieza y donde se ejecuta | docs/arc42/ contiene las secciones 1, 2, 3, 4, 5, 6, 8, 9, 10 y 12; no existe archivo de la seccion 7. | No cumple | Falta la vista de despliegue con una caja por pieza y su ubicacion. |
| Limite de costo y restriccion de tarjeta recogidos en la seccion 2 | docs/arc42/arc42_2_restricciones.md cubre restricciones organizacionales, academicas, tecnologicas y de fuentes externas; no menciona limite de costo ni 'sin tarjeta'. | No cumple | El archivo existe, pero no recoge las restricciones pedidas. |
| Un ADR por decision de plataforma, con alternativa descartada | docs/adr/ solo contiene 0001 a 0004 (arquitectura hexagonal, stack Next.js/FastAPI, contextos del dominio y estrategia de integracion); ninguno decide la plataforma de despliegue. | No cumple | No hay ADR de plataforma ni capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_Drift en la organizacion ISCOUTB, visible: true, y el historial de HEAD 9334a03 lista 8 nombres de autor que consolidan en los 4 integrantes declarados. | Cumple | Nombre y visibilidad correctos; integrantes presentes en el historial. |
| Estructura minima | HEAD 9334a03 contiene docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | La documentacion es revisable en Markdown; arc42 aun sin secciones 7 y 11. |
| Convenciones de ADR | docs/adr/0001-0004 siguen el patron NNNN-titulo-en-kebab-case y 0001 esta marcado como Reemplazado por ADR-0002. | Cumple | La trazabilidad de 0001 queda pendiente y los enlaces de 0003 apuntan a rutas inexistentes. |
| Tabla de aspectos | docs/aspectos.md existe en HEAD 9334a03, pero su contenido no se incluyo en la evidencia entregada. | No verificado | Hace falta el contenido para verificar las ocho columnas y que cada celda sea navegable. |
| Registro de uso de IA | docs/ia.md existe y su historial crece entre 2026-08-09 y 2026-09-20 (ia_log), pero no se incluyo su contenido. | No verificado | Falta comprobar lo rechazado y su motivo tecnico. |
| README | README.md describe que es el sistema, requisitos previos, instalacion, 'Comando Unico de Ejecuccion' con python scripts/start.py y como se prueba (pytest, npm run build, k6). | Cumple | Cubre el arranque con un solo comando en local. |
| Pipeline y analisis estatico | Existen .github/workflows/ci.yml y sonar-project.properties, pero la evidencia no aporta runs_ci ni la URL publica del analisis con Quality Gate. | No verificado | Comprobar con curl a api.github.com/repos/ISCOUTB/AS_202620_Drift/actions/runs y con la URL publica de SonarCloud del hash revisado. |
| Secretos | El barrido de secretos sobre HEAD 9334a03 no arroja coincidencias y envs_versionados esta vacio (ningun .env versionado). | Cumple | Repositorio publico sin credenciales; conviene anadir .env.example. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `9334a03f97fc2ddb67846b8e6d229ff85898f3f1 2026-09-20T20:19:47-05:00 Update cambio_incompatible_evidencia.md`
- **Veredicto**: con pendientes
- Resumen: En HEAD 9334a03 (2026-09-20, anterior al cierre) el sistema sigue siendo local: sin URL publica, sin infraestructura como codigo, sin pipeline verificable y sin observabilidad, costo ni ADR de plataforma.

Pendientes que siguen abiertos:
- Despliegue accesible desde fuera con URL y health check.
- Infraestructura como codigo versionada y README de recreacion del entorno.
- Pipeline en verde sobre master y analisis SonarCloud auditable.
- Logs estructurados y metrica consultable ligada al escenario E1.
- Estimacion de costo mensual con supuestos; limite de costo y 'sin tarjeta' en arc42 seccion 2.
- arc42 seccion 7 y un ADR por decision de plataforma con alternativa descartada.

## Recuento y nota sugerida

1 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.3 = 1 + 4 × (1/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Pipeline en verde sobre master: falta el ultimo run de GitHub Actions con su conclusion y URL.
- Analisis de SonarCloud con estado del Quality Gate para el hash revisado: falta la URL publica.
- Contenido de docs/aspectos.md: no se incluyo, no se pudieron verificar las ocho columnas.
- Contenido de docs/ia.md: no se incluyo, no se pudo verificar lo rechazado y su motivo.
- Comprobacion en vivo de despliegue y health check: no hay URL declarada que abrir desde fuera de la red.

## Hallazgos para la planilla

- La entrega S8 no tiene despliegue: sin URL publica ni infraestructura como codigo en HEAD 9334a03.
- No hay runs de CI en la evidencia: no se puede confirmar pipeline en verde ni Quality Gate de SonarCloud.
- Faltan la seccion 7 de arc42, el limite de costo en la seccion 2, la estimacion mensual y los ADR de plataforma.
- No existe logging estructurado ni metrica consultable en un entorno desplegado.
- El repositorio esta limpio de secretos y sin .env versionado.
- El commit calificado (9334a03, 2026-09-20) es anterior al cierre y no hay commits posteriores ni tardios.
