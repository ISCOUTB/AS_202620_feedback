# semana-07-evidencia-s7 · CampusMarket

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `baeca7e` en `origin/master` (2026-09-16T10:28:32-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | contracts/openapi-v1.json en árbol de baeca7e; README declara OpenAPI 3.1 versión 1.0.0. | Cumple | El archivo existe y está versionado; no se aporta su contenido completo. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | README y docs/arc42/06 listan GET /health, GET /publicaciones y POST /publicaciones, pero no se aporta fragmento de components.schemas del contrato. | No verificado | Haría falta citar el fragmento del contrato con los esquemas de datos. |
| Correspondencia entre el contrato y la API implementada | docs/arc42/06 y ADR-0003 describen router/service/repository, pero no se aporta el código de router.py ni el contrato para cotejar rutas. | No verificado | Falta el cotejo bidireccional exigido por la ficha. |
| Versión de la API declarada y con historial | README y ADR-0003 declaran versión 1.0.0, pero no se aporta git log de contracts/openapi-v1.json. | No verificado | Falta el historial del archivo del contrato. |
| Prueba de contrato presente | backend/tests/test_contrato_openapi.py aparece en el árbol de baeca7e. | Cumple | Archivo presente y referenciado en ADR-0003 y README. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/backend-tests.yml, pero no se aporta su contenido ni runs_ci con el comando de contrato. | No verificado | Haría falta la línea del workflow que invoca la prueba y la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/evidencias/fallo-contrato-s7-2026-09-15.md en baeca7e, referenciado por README como demostración controlada de ruptura. | Cumple | No se aporta run de CI en rojo; la evidencia es un documento del equipo. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003-usar-integracion-sincrona-http-json.md cita EC-06, alternativas síncrona/asíncrona y consecuencias. | Cumple | El ADR justifica la alternativa descartada. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06-vista-ejecucion.md contiene flujos 6.1 a 6.6 con diagramas de secuencia. | Cumple | Describe creación, consulta y persistencia no disponible. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/02-contenedores.md y .puml en el árbol; docs/arc42/06 sección 6.7 etiqueta HTTP/JSON y PyMySQL / SQL. | Cumple | La vista de ejecución respalda el etiquetado del nivel 2. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_PROYECTO_CAMPUSMARKET en organización ISCOUTB, visible; autores registrados en historial. | Cumple | No se verifica membresía a la organización, pero nombre y visibilidad son correctos. |
| Estructura mínima | Árbol de baeca7e incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | La estructura mínima está presente. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md a 0004-migrar-persistencia-a-mysql.md siguen el patrón NNNN-kebab-case.md. | Cumple | Los ADR revisados incluyen contexto, alternativas y consecuencias. |
| La tabla de aspectos | docs/aspectos.md existe en el árbol, pero no se aporta su contenido con las ocho columnas. | No verificado | No se pudo comprobar la trazabilidad navegable exigida. |
| Registro de uso de IA | docs/ia.md existe y ia_log muestra commits, pero no se aporta su contenido con uso, herramienta, aceptado y rechazado. | No verificado | Falta verificar la columna de lo rechazado y su motivo. |
| README | README.md describe el sistema, requisitos, arranque con scripts/run_s4.* y pruebas con python -m pytest backend/tests -q. | Cumple | El arranque depende de una instancia MySQL previa, documentada como requisito. |
| Pipeline y análisis estático | Existen .github/workflows/backend-tests.yml y .sonarcloud.properties, pero no se aportan URL de run exitoso ni URL pública de SonarCloud con Quality Gate. | No cumple | Falta la evidencia auditable completa exigida por el contrato. |
| Secretos | Grep de secretos en baeca7e solo muestra referencias a variables de entorno; envs_versionados vacío y .env no versionado. | Cumple | No se encontró credencial expuesta en el último commit. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `baeca7ea3cebe33818a68c1edc38e9aaf045424c 2026-09-16T10:28:32-05:00 Revise evidence document for API contract S7`
- **Veredicto**: al dia
- Resumen: A HEAD baeca7e (2026-09-16) el proyecto tiene contrato OpenAPI, prueba de contrato, ADR de integración y arc42/C4; faltan evidencias auditables de CI/SonarCloud y contenido de contrato, aspectos e IA.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Migración de SQLite a MySQL (ADR-0004, 2026-09-16) como corrección posterior al primer corte por observación docente; evidencia docs/adr/0004-migrar-persistencia-a-mysql.md y README.

Pendientes que siguen abiertos:
- Evidencia de run de CI que ejecute la prueba de contrato.
- URL pública de SonarCloud con Quality Gate y run del scanner.
- Fragmento del contrato con schemas y cotejo con router.py.
- Contenido de docs/aspectos.md y docs/ia.md.

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contrato con rutas y esquemas de datos, no solo listado de endpoints
- Correspondencia entre el contrato y la API implementada
- Versión de la API declarada y con historial
- El pipeline ejecuta la prueba de contrato
- La tabla de aspectos
- Registro de uso de IA

## Hallazgos para la planilla

- El contrato OpenAPI está versionado, pero no se aportó su contenido para verificar esquemas y correspondencia.
- No se aportan runs_ci ni la línea del workflow que ejecute la prueba de contrato.
- Existe evidencia documental de fallo por cambio incompatible, sin run en rojo de CI.
- La migración a MySQL (ADR-0004) corrige una observación docente posterior al primer corte.
- Pipeline y SonarCloud no tienen URL de ejecución ni Quality Gate público en la evidencia.
- docs/aspectos.md y docs/ia.md existen, pero su contenido no se aporta.
