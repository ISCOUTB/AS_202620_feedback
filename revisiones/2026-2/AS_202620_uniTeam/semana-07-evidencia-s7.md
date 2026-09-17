# semana-07-evidencia-s7 · uniTeam

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `6cc8e6f` en `origin/master` (2026-09-13T20:20:18-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | 6cc8e6f: árbol completo (docs/, app/, web/, test/, .github/) sin ningún archivo openapi/swagger/asyncapi .yaml/.json ni .proto | No cumple | La API expone OpenAPI autogenerado por FastAPI en /docs (README), pero no hay contrato versionado en el repositorio. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No existe archivo de contrato del cual citar rutas o esquemas de respuesta en 6cc8e6f | No cumple | El listado de 10 rutas del README es prosa, no un esquema ejecutable. |
| Correspondencia entre el contrato y la API implementada | 6cc8e6f:app/api/rutas_proyectos.py, rutas_tareas.py y rutas_progreso.py implementan rutas, pero no hay contrato con el que contrastarlas | No cumple | No se pudo tomar ninguna ruta del contrato ni comprobar el sentido inverso código→contrato. |
| Versión de la API declarada y con historial | Sin archivo de contrato en 6cc8e6f; no hay objeto para `git log -- <ruta del contrato>` | No cumple | No hay campo de versión de API ni historial del contrato. |
| Prueba de contrato presente | 6cc8e6f:test/ contiene __init__.py, conftest.py, prueba_test.py, test_autenticacion.py, test_corte_vertical.py, test_proyectos.py y test_tablero.py; ninguna prueba de contrato | No cumple | No aparece uso de dredd, schemathesis, pact ni prism en el árbol. |
| El pipeline ejecuta la prueba de contrato | 6cc8e6f:.github/workflows/ci.yml es el único workflow; no existe prueba de contrato que invocar y no se aportó el contenido del workflow ni runs_ci | No cumple | Se esperaba la línea del workflow con el comando de contrato y la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | Sin runs_ci ni evidencia aportada por el equipo en 6cc8e6f | No verificado | No hay prueba de contrato ni ejecución en rojo; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | 6cc8e6f:docs/adr/0003-usar-eventos-de-dominio-en-proceso.md — decide eventos de dominio con despacho en proceso y autorización síncrona antes de publicar, con alternativas descartadas (capas, hexagonal, monolito modular) y consecuencias | Cumple | Liga la decisión a ESC-03, ESC-01 y ESC-05; la comparación está en docs/c4/matriz-decision-adr-003.md. |
| arc42 sección 6 con los flujos de interacción | 6cc8e6f:docs/arc42/arc42-uniteam.md — la cabecera declara «Secciones 1, 2, 3, 4, 5, 6, 9, 10, 11 y 12 redactadas» | No verificado | El contenido aportado se corta en §3.1; no se pudo leer la §6 ni comprobar que describa los flujos de interacción. |
| C4 nivel 2 con protocolo y formato en cada flecha | 6cc8e6f:docs/c4/nivel2-contenedores.md — «Usa (HTTPS)», «Inicia sesión (OIDC)», «Valida el token (OIDC)» y «SQL» sin formato; «API → Servicio de correo» marcada «(previsto)» sin protocolo ni formato; solo «Aplicación Web → API (REST/JSON)» lleva ambos | No cumple | Falta el formato en cinco de las seis relaciones del diagrama. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | 6cc8e6f: repo AS_202620_uniTeam bajo la organización ISCOUTB, visible=true, rama principal origin/master | Cumple | El historial muestra 5 cuentas para 4 integrantes declarados: una misma cuenta aparece como JuanB y JuanBustamante (mismo identificador) y «super-gremlin» no corresponde a ningún integrante declarado; la pertenencia a la organización no es auditable con esta evidencia. |
| Estructura mínima | 6cc8e6f: docs/arc42/arc42-uniteam.md, docs/adr/0001..0005-*.md, docs/c4/nivel1-contexto.md y nivel2-contenedores.md, docs/aspectos.md, docs/ia.md y README.md | Cumple | El C4 vive en docs/c4/ como diagramas en Mermaid (código) y los ADR siguen NNNN-kebab-case. |
| Estado del repositorio que se califica | Rama principal origin/master; commit 6cc8e6f del 2026-09-13T20:20:18-05:00, anterior al cierre 2026-09-21T05:00:00Z | Cumple | No constan commits posteriores al cierre; no se aportó `show-ref` de origin/main. |
| Convenciones de ADR | 6cc8e6f:docs/adr/ — 0001 a 0005 con nombre NNNN-kebab-case; 0001 marcado «Reemplazado por 0002» con enlace, y 0004 y 0005 con sección de Trazabilidad | Cumple | Los títulos enuncian la decisión («Usar MySQL como base de datos», «Delegar la autenticación en un proveedor OIDC»). |
| Tabla de aspectos | 6cc8e6f:docs/aspectos.md — encabezado ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia con 9 filas (A-01 a A-09) y celdas enlazadas a archivos y pruebas | Cumple | Cada fila cierra contra la medida de un escenario; el propio documento marca ESC-02, ESC-04 y ESC-05 sin medir. |
| Registro de uso de IA | 6cc8e6f:docs/ia.md existe y `git log` muestra 11 entradas entre 2026-08-09 y 2026-09-13 (última 83ab788) | No verificado | No se aportó el contenido; no se pudo comprobar la columna de lo rechazado y su motivo, que es la que el contrato mira primero. |
| README | 6cc8e6f:README.md — qué es el sistema, arranque con un solo comando (`docker compose up`) y sección de pruebas (`pytest -v`, `scripts/verificar_enlaces.py`, `npm run build`) con requisitos previos declarados | Cumple | Declara requisito previo único (Docker con Compose) y variables obligatorias OIDC_EMISOR y OIDC_AUDIENCIA. |
| Pipeline y análisis estático | 6cc8e6f:.github/workflows/ci.yml es el único workflow; no hay `sonar-project.properties` ni opción equivalente en el árbol, y la evidencia no incluye contenido del workflow, ningún run de CI ni URL pública de SonarCloud | No cumple | El contrato §8 exige configuración más línea del scanner, URL del run y URL del análisis con Quality Gate; la búsqueda de secretos no encontró credenciales reales (las coincidencias son parámetros llamados token). |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `6cc8e6fda038b43ec221e5d796dbfaafa195c15e 2026-09-13T20:20:18-05:00 Merge pull request #2 from ISCOUTB/fix/correcciones`
- **Veredicto**: con pendientes
- Resumen: A HEAD de master (6cc8e6f, 2026-09-13, anterior al cierre) la documentación de arquitectura está madura —ADR 0001-0005, aspectos, arc42, C4 y README—, pero la entrega de la semana 7 no está: no hay contrato de API versionado, no hay prueba de contrato, no hay evidencia de que falle ante un cambio incompatible y el análisis estático no es auditable. No hay commits posteriores al cierre en la rama principal.

Pendientes que siguen abiertos:
- Contrato OpenAPI/AsyncAPI/proto versionado, con rutas, esquemas y versión de API (filas 1-4 de la ficha).
- Prueba de contrato e invocación desde el workflow (filas 5-6).
- Evidencia de que la prueba falla ante un cambio incompatible (fila 7).
- Sección 6 de arc42 con flujos de interacción y formato en cada flecha del C4 nivel 2 (filas 9-10, parcialmente resuelto).
- Evidencia auditable de SonarCloud: línea del scanner, URL del run y URL del análisis con Quality Gate (contrato §8).
- Secciones 7 y 8 de arc42, declaradas pendientes por el propio documento.

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de .github/workflows/ci.yml y existencia de runs de CI: no aportados; haría falta el archivo y la URL del run.
- Contenido de docs/ia.md, en especial la columna de lo rechazado y su motivo: haría falta el fragmento.
- Sección 6 de arc42 (flujos de interacción): el documento aportado se corta en §3.1.
- Fallo de la prueba de contrato ante un cambio incompatible: sin run en rojo ni evidencia del equipo en la entrega.
- Quality Gate de SonarCloud: sin URL pública del análisis ni rama o revisión asociada.
- Pertenencia de los integrantes a la organización ISCOUTB: la evidencia no incluye la lista de miembros.

## Hallazgos para la planilla

- No existe ningún archivo de contrato (OpenAPI, AsyncAPI o proto) en el árbol de 6cc8e6f: la semana 7 no dejó su artefacto central.
- No hay prueba de contrato en test/ y el pipeline solo consta como ci.yml, sin contenido citado ni runs.
- La evidencia no aporta ningún run de CI (runs_ci vacío), así que arranque, pruebas y pipeline no son verificables por ejecución.
- SonarCloud carece de las tres evidencias exigidas: configuración del scanner, run exitoso y URL pública con Quality Gate.
- El historial tiene 5 cuentas para 4 integrantes declarados: dos nombres son la misma cuenta y una cuenta no corresponde a ningún integrante declarado.
- Sin secretos reales: las coincidencias de la búsqueda son parámetros y funciones llamados token, y no hay .env versionado.
- arc42 declara pendientes las secciones 7 (despliegue) y 8 (conceptos transversales).
- El C4 nivel 2 solo etiqueta el formato en una flecha (REST/JSON); las demás llevan protocolo sin formato.
