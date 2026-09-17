# semana-07-evidencia-s7 · PideUtb

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `006edfe` en `origin/master` (2026-09-13T16:37:23-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Arbol de HEAD 006edfe (2026-09-13T16:37:23-05:00): no hay archivo openapi/swagger/asyncapi .yaml/.json ni .proto; solo backend/app/menu/contracts.py y backend/app/usuarios/contracts.py. | No cumple | Se esperaba especificacion OpenAPI/AsyncAPI o proto versionada; los contracts.py son lenguaje publicado entre modulos, no el contrato del API. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No existe archivo de especificacion en HEAD 006edfe del que citar rutas o esquemas; los unicos esquemas son modelos Pydantic en backend/app/{menu,pedidos,usuarios}/models.py. | No cumple | Sin contrato no hay version de especificacion, rutas ni esquemas de respuesta que revisar. |
| Correspondencia entre el contrato y la API implementada | El codigo expone POST /pedidos (backend/app/pedidos/router.py) pero no hay contrato donde contrastar rutas en ningun sentido. | No cumple | No se pudo tomar dos rutas del contrato hacia el codigo ni una del codigo hacia el contrato. |
| Version de la API declarada y con historial | Sin archivo de contrato no hay campo de version de API ni salida de git log sobre el contrato en HEAD 006edfe. | No cumple | Se esperaba la version declarada en el propio archivo o en su ruta y el historial de commits del contrato. |
| Prueba de contrato presente | backend/tests/ en HEAD 006edfe lista test_health, test_pedidos, test_propiedad_datos, test_modularidad y test_linea_base; ninguna prueba de contrato (dredd, schemathesis, pact, prism o spectral). | No cumple | test_modularidad.py audita imports por AST; no valida el contrato del API. |
| El pipeline ejecuta la prueba de contrato | Solo existe .github/workflows/ci.yml y ninguna prueba de contrato que invocar; la evidencia no aporta linea del workflow con contract/dredd/schemathesis/pact/spectral. | No cumple | Se esperaba la linea del workflow que invoca la prueba y la URL del run; ninguna de las dos aparece. |
| Evidencia de que la prueba falla ante un cambio incompatible | No hay run en rojo ni evidencia aportada por el equipo, y el listado de pruebas de HEAD 006edfe no incluye ninguna prueba de contrato. | No verificado | Hararia falta la prueba de contrato y un run fallido o el registro del cambio incompatible; queda como pregunta de sustentacion. |
| ADR de la estrategia de integracion ligado a un escenario | docs/adr/ en HEAD 006edfe contiene 0001-estilo-arquitectonico.md y 0002-propiedad-datos-establecimiento.md; ninguno decide sincrono frente a asincrono con alternativa descartada y consecuencias de acoplamiento. | No cumple | ADR-0002 menciona llamadas en proceso entre contextos como consecuencia, pero no es un ADR de estrategia de integracion. |
| arc42 seccion 6 con los flujos de interaccion | docs/arc42/arc42.md a 006edfe con vista de tiempo de ejecucion: README.md enlaza a arc42.md seccion 6 y docs/linea-base.md cita arc42 seccion 6.1 (#runtime-crear-pedido) y su diagrama de secuencia. | Cumple | Verificacion indirecta: la evidencia entrega el arc42 truncado, pero tres documentos citan la seccion 6 y el flujo de crear pedido. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/nivel2-contenedores.md a 006edfe: seis Rel(...) con etiqueta de tecnologia, entre ellas frontend hacia API como HTTPS/JSON y API hacia Supabase y Wompi como HTTPS/API. | Cumple | El formato de datos solo es explicito en frontend hacia API; las flechas a Supabase y Wompi indican protocolo sin formato declarado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_PideUtb, visible=true en HEAD 006edfe; autores consolidados con .mailmap dan 3 identidades de git (Santiago Cuesta y Santiago-C0; daniarriet; Ruddy y ruddy2000utb-droid) para 3 integrantes declarados. | Cumple | Ninguna cuenta se atribuyo por parecido de nombre; la consolidacion usa el mismo autor y el .mailmap versionado. |
| Estructura minima | HEAD 006edfe contiene docs/arc42/arc42.md, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Se cumple la ruta minima; arc42 se entrega como un unico Markdown dentro de docs/arc42/. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-propiedad-datos-establecimiento.md siguen el patron NNNN-kebab-case, enuncian la decision y traen alternativas descartadas y tabla de trazabilidad. | Cumple | No se observan reescrituras de ADR aceptados en la evidencia disponible. |
| Tabla de aspectos | docs/aspectos.md a 006edfe tiene 8 columnas (ID, aspecto, escenario, medida, C4, ADR, codigo, pruebas) y filas ESC-01 a ESC-05 enlazadas a C4, ADR, codigo y pruebas. | Cumple | ESC-01 y ESC-03 con cadena completa; ESC-04 y ESC-05 marcadas pendientes por el modulo pagos vacio. |
| Registro de uso de IA | docs/ia.md registra por entrega la herramienta, lo usado y una tabla de propuestas rechazadas con su motivo (S5), con 9 revisiones entre 2026-08-08 y 2026-09-13. | Cumple | El historial del archivo se cita con fecha y hash en la evidencia aportada. |
| README | README.md en HEAD 006edfe declara que es el sistema, el requisito Python 3.11+, un comando unico de arranque (venv, pip, uvicorn) y como correr pytest. | Cumple | Incluye la nota de que los repositorios usan datos en memoria en esta entrega. |
| Pipeline y analisis estatico | Existe .github/workflows/ci.yml y el README declara pytest en Python 3.11 y 3.12, pero en HEAD 006edfe no hay sonar-project.properties, ni URL del run del hash revisado, ni URL publica del analisis con Quality Gate. | No cumple | Se buscaron el archivo de configuracion del scanner y las URL de run y SonarCloud; solo docs/ia.md menciona correccion de hallazgos de SonarCloud, sin enlace publico. |
| Secretos | El barrido de patrones de credenciales sobre HEAD 006edfe no arrojo coincidencias y la lista de .env versionados esta vacia (secretos: sin coincidencias; envs_versionados: []). | Cumple | Sin incidentes en el commit calificado; el historial completo no se pudo barrer con la evidencia entregada. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `006edfe555ed809d027d7ed47657efc6a451f325 2026-09-13T16:37:23-05:00 Actualizar la evidencia de CI y reconvertir el documento de linea base`
- **Veredicto**: con pendientes
- Resumen: En la punta de master (006edfe, 2026-09-13) el proyecto conserva una base documental y de CI solida (identidad, estructura, ADRs, aspectos, IA, README y sin secretos) y cumple 2 de 10 criterios de la ficha S7; falta la pieza central de la semana: contrato del API ejecutable y versionado, su prueba en el pipeline, la evidencia de que esa prueba falla y el ADR de estrategia de integracion.

Pendientes que siguen abiertos:
- Contrato OpenAPI/AsyncAPI o proto versionado, con rutas, esquemas y version declarada
- Prueba de contrato invocada desde el workflow y evidencia de fallo ante cambio incompatible
- ADR de estrategia de integracion sincrona o asincrona con alternativa descartada
- Evidencia publica de SonarCloud: configuracion del scanner, run del hash y URL del analisis con Quality Gate
- Modulo pagos vacio: ESC-04 y ESC-05 sin codigo ni pruebas
- Deuda planificada V-07, V-08 y V-09 y prueba de carga de ESC-02

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba de contrato que falle ante un cambio incompatible: no hay prueba, ni run en rojo, ni evidencia del equipo (paso 6 de la ficha).
- Ejecucion del pipeline para el hash 006edfe: la evidencia no aporta runs_ci; correcciones.md cita un run verde de otro commit.
- Estado del Quality Gate de SonarCloud: sin URL publica del analisis y sin configuracion del scanner en el arbol.
- Contenido literal de arc42 seccion 6 y de los ADR: los documentos llegan truncados y su verificacion fue por referencias cruzadas.

## Hallazgos para la planilla

- La entrega S7 no incluye ninguna especificacion OpenAPI/AsyncAPI o proto versionada en el repositorio.
- En el proyecto, contracts.py designa el lenguaje publicado entre modulos, no el contrato del API principal.
- No existe prueba de contrato ni evidencia de que falle ante un cambio incompatible.
- No hay ADR que decida la estrategia de integracion sincrona o asincrona frente a un escenario.
- La matriz transversal del contrato se cumple en 7 de 8 filas; la pendiente es la evidencia publica de SonarCloud.
- La evidencia de SonarCloud no es auditable: falta configuracion del scanner, run del hash 006edfe y URL publica con Quality Gate.
- La evidencia reporta sin commits nuevos desde el cierre anterior, de modo que S7 no aporta commits propios en master.
- No hay commits posteriores al cierre en la rama master segun la evidencia entregada.
