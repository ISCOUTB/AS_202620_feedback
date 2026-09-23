# semana-08-evidencia-s8 · Clubs UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `dc211b8` en `origin/master` (2026-09-20T23:56:51-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | README.md §7 solo cita http://localhost:8000/health y el árbol a dc211b8 no tiene artefacto de despliegue alguno. | No cumple | No se declara URL pública, así que no se pudo registrar código ni tiempo desde fuera; una captura no sustituye la URL. |
| Health check consultable | backend/src/linkclub/adapters/inbound/api/health_router.py y README.md §7 declaran /health, pero no hay instancia desplegada que responda. | No cumple | Sin URL no hay código de respuesta que citar; la ruta local no satisface el criterio del entorno desplegado. |
| Infraestructura como código versionada en el repositorio | El árbol a dc211b8 no incluye Dockerfile, docker-compose, .tf/.tfvars, k8s/, helm/, fly.toml, render.yaml, railway ni Procfile. | No cumple | Solo hay .github/workflows/backend-tests.yml y contrato.yml, que son de pruebas y contrato, no de infraestructura. |
| El entorno se puede recrear siguiendo el README | README.md §7 documenta requisitos (Python 3.10+), venv, pip install y uvicorn, pero la evidencia no aporta runs_ci ni despliegue. | No verificado | Comando anotado para comprobar: cd backend && python -m venv venv && pip install -r requirements.txt && uvicorn linkclub.main:app --app-dir src (y PYTHONPATH=src pytest tests/ -v). |
| Pipeline en verde sobre la rama principal | Existen .github/workflows/backend-tests.yml y .github/workflows/contrato.yml, pero no se incluyó ningún run con nombre, conclusión y URL. | No verificado | Comando anotado: curl -s 'https://api.github.com/repos/ISCOUTB/AS_202620_Clubs_UTB/actions/runs?per_page=10'. |
| Logs estructurados | No hay archivo de configuración de logging en el árbol a dc211b8 y la evidencia no incluye el contenido de main.py ni la salida del grep de logging. | No verificado | Falta un ejemplo de línea con campos; comando anotado: git grep -nIE '(structlog\|winston\|pino\|logback\|serilog\|logging\.config)'. |
| Métrica consultable asociada a un escenario de calidad | El árbol a dc211b8 solo expone health_router.py y publicacion_router.py y ningún documento menciona métricas ni su escenario (U1, U2, U3, C1, C2 o C3). | No cumple | No hay métrica que consultar; sin escenario asociado el criterio sería incompleto de todos modos. |
| Secretos fuera del código y tomados del entorno o del almacén | El barrido de secretos no tiene coincidencias y envs_versionados está vacío, pero no existe .env.example ni se aportó el contenido de los workflows con referencias secrets.X. | No verificado | Falta .env.example y la línea del workflow que toma los valores del proveedor; sin eso no se prueba la separación. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No hay documento de costos en el árbol a dc211b8 ni mención de costo en README.md ni en docs/arc42/. | No cumple | Falta volumen supuesto, costo por pieza y el punto en que se rompe la capa gratuita. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | docs/arc42/ contiene 01-06, 08-10 y 12; no existe ningún archivo 07*. | No cumple | Falta la vista de despliegue; tampoco existe la sección 11. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | docs/arc42/02_restricciones.md solo lista T1-T4, O1-O3, C1-C2 y CV1. | No cumple | No se menciona el límite de costo ni la restricción de 'sin tarjeta'. |
| Un ADR por decisión de plataforma, con alternativa descartada | docs/adr/ a dc211b8 tiene 0001-hexagonal.md, 0002-ajuste-contextos-publicaciones.md y dos archivos 0003 (contrato REST); ninguno decide plataforma de despliegue. | No cumple | '0003- integacion rest openapi.md' rompe la convención de nombre (espacio) y duplica el número; no hay ADR de infraestructura ni de capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_Clubs_UTB en la organización ISCOUTB, visible=true, rama origin/master, commit dc211b8 (2026-09-20T23:56:51-05:00), con historial de las cuentas del equipo. | Cumple | El historial muestra 5 cuentas de autor para 4 integrantes declarados: 'Josh Ortega' y 'Josh4OP' comparten la misma identidad de autor registrada, y 'Luis Daniel' y 'Luis-Salas-Reyes' figuran como cuentas distintas (no se consolidan por parecido de nombre). |
| Estructura mínima | A dc211b8 existen README.md, docs/arc42/, docs/adr/, docs/c4/contexto.md, docs/aspectos.md y docs/ia.md. | Cumple | Faltan arc42 07 y 11; el C4 de contexto y contenedores vive en un solo archivo de docs/c4/, lo que es desviación de estructura y no ausencia del artefacto. |
| Convenciones de ADR | docs/adr/0003- integacion rest openapi.md (espacio inicial) y docs/adr/0003-API.md duplican el número y no cumplen el patrón NNNN-titulo-kebab-case; docs/arc42/09_decisiones_de_diseno.md enlaza 0003-integracion-rest-openapi.md, que no existe en el árbol. | No cumple | El ADR 0001 carece de trazabilidad a commit/PR y a elementos C4 exigida por la convención. |
| La tabla de aspectos | docs/aspectos.md existe a dc211b8, pero la evidencia no incluye su contenido. | No verificado | No se pueden comprobar las ocho columnas ni que cada celda sea navegable; el README §4 la describe con columnas distintas a las del contrato (incluye Escenario y omite Evidencia). |
| Registro de uso de IA | docs/ia.md crece a lo largo del semestre: commits de 2026-08-09 a 2026-09-15 (último d2d1450). | No verificado | No se incluyó el contenido del archivo, así que no se puede comprobar la columna de qué se rechazó y por qué, que es la que se mira primero. |
| README | README.md describe el sistema (§1-2), el stack (§3), cómo arrancar (§7, con Python 3.10+ y uvicorn) y cómo probar (PYTHONPATH=src pytest tests/ -v). | Cumple | El arranque son varios pasos y no un único comando, y no hay run de CI que confirme que el procedimiento funciona. |
| Pipeline y análisis estático | Hay .github/workflows/backend-tests.yml y contrato.yml, pero no existe sonar-project.properties en el árbol, ni URL de run de CI, ni URL pública de SonarCloud con Quality Gate para dc211b8. | No cumple | No conformidad del §8: falta al menos dos de las tres evidencias exigidas (configuración del scanner, run exitoso, análisis público con estado del Quality Gate). |
| Secretos | Barrido de patrones de credenciales sin coincidencias a dc211b8 y envs_versionados vacío (ningún .env versionado). | Cumple | No hay secretos que rotar; conviene añadir .env.example para el criterio de despliegue de la ficha S8. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `dc211b8f38c4f8d0ba0ebd13021e3181b6d573bb 2026-09-20T23:56:51-05:00 Merge pull request #2 from ISCOUTB/contrato-openapi`
- **Veredicto**: con pendientes
- Resumen: A la punta revisada de origin/master (dc211b8, 2026-09-20T23:56:51-05:00) el proyecto es un backend FastAPI con contrato OpenAPI y documentación arc42 parcial, sin despliegue, sin IaC, sin métrica, sin logs estructurados y sin estimación de costo; la entrega S8 no cumple ninguno de sus doce criterios.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Ninguno: commits_tardios_post_cierre está vacío y no hay commits nuevos desde el cierre anterior.

Pendientes que siguen abiertos:
- URL pública del sistema y comprobación externa de /health
- Infraestructura como código versionada
- arc42 §7 (vista de despliegue) y §11
- ADR por decisión de plataforma con alternativa descartada
- Estimación de costo mensual y restricciones de costo y tarjeta en §2
- Métrica consultable ligada a un escenario de calidad
- Logs estructurados con campos
- Runs de CI y análisis público de SonarCloud
- Corregir nombres y duplicados de ADR y el enlace roto de la sección 9
- Resolver NC-01 y NC-02 de docs/arc42/lista_errores.md

## Recuento y nota sugerida

0 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Recreación del entorno según README: falta run de CI del arranque; comando anotado con venv, pip install y uvicorn.
- Pipeline en verde: sin runs citados; comando anotado contra la API de GitHub Actions del repositorio.
- Logs estructurados: falta el contenido de main.py y la salida del grep de configuración de logging.
- Secretos tomados del entorno: hay barrido limpio pero no hay .env.example ni contenido de workflows con secrets.X.
- Tabla de aspectos: docs/aspectos.md no se incluyó en la evidencia, no se pueden comprobar sus ocho columnas.
- Registro de IA: docs/ia.md no se incluyó; solo se ve que crece por commits.

## Hallazgos para la planilla

- La entrega S8 no aporta ninguna pieza de despliegue: no hay URL pública, ni IaC, ni health check externo.
- El README solo describe arranque local en localhost:8000, no un entorno desplegado.
- Faltan las secciones 7 y 11 de arc42 y no existe ningún ADR de plataforma de despliegue.
- No hay estimación de costo mensual ni restricciones de costo o de 'sin tarjeta' en la sección 2.
- docs/adr/ tiene dos archivos 0003 (uno con espacio en el nombre) y la sección 9 enlaza un 0003 inexistente.
- No se aportaron runs de CI ni evidencia auditable de SonarCloud, por lo que el pipeline no se puede verificar.
- El historial registra 5 cuentas de autor para 4 integrantes declarados; hay identidad duplicada y cuentas con nombre parecido no consolidadas.
- No existe métrica consultable ni configuración de logs estructurados en el árbol revisado.
