# semana-07-evidencia-s7 · ROUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `5b48dd0` en `origin/master` (2026-09-13T23:43:22-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Arbol de HEAD 5b48dd0: no aparece ningun archivo openapi/swagger/asyncapi (.yaml/.json) ni .proto; solo routers FastAPI en backend/app/modules/*/router.py. | No cumple | Se esperaba el contrato ejecutable versionado y no existe en la punta revisada. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No hay archivo de contrato del cual citar paths ni componentes; los unicos esquemas son Pydantic (backend/app/modules/trips/schemas.py, auth/schemas.py). | No cumple | Sin contrato no hay rutas ni esquemas de respuesta verificables. |
| Correspondencia entre el contrato y la API implementada | Rutas implementadas localizables en backend/app/modules/trips/router.py y backend/app/modules/auth/router.py, pero no hay contrato donde buscarlas ni contraste posible. | No cumple | Ninguno de los dos sentidos de la correspondencia se pudo comprobar. |
| Version de la API declarada y con historial | No existe ruta de contrato, por lo que no hay campo de version ni git log del archivo en 5b48dd0. | No cumple | Se esperaba version declarada (info.version o ruta versionada) y su historial. |
| Prueba de contrato presente | backend/tests/ solo contiene conftest.py, test_cupos.py, test_registro.py y test_trips_flow.py; ningun archivo tipo pact, dredd, schemathesis o similar. | No cumple | Ausencia reproducible sobre el arbol de 5b48dd0. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml existe en el arbol, pero no se aporto su contenido ni runs_ci del repositorio. | No verificado | Haria falta el grep de contract/dredd/pact/schemathesis en ci.yml y la URL del run que lo invoca. |
| Evidencia de que la prueba falla ante un cambio incompatible | No hay prueba de contrato ni run en rojo aportado; el unico run citado (README.md, enlace externo) se declara como Success. | No verificado | Queda como pregunta de sustentacion para el criterio de sobresaliente. |
| ADR de la estrategia de integracion ligado a un escenario | docs/adr/0001-usar-monolito-modular.md, 0002-usar-arquitectura-interna-por-capas.md y 0003-control-atomico-de-cupos.md; ninguno decide integracion sincrona o asincrona con alternativa descartada y consecuencias de acoplamiento. | No cumple | 0001 compara estilos de arquitectura, no la estrategia de integracion de la API. |
| arc42 seccion 6 con los flujos de interaccion | docs/arc42/06_vista_de_ejecucion.md describe registro e inicio de sesion con diagramas mermaid y aspectos relevantes por capa. | Cumple | Cubre dos flujos de interaccion; no los liga a rutas del contrato. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/context.md, bloque Nivel 2: APP->API [REST/JSON - HTTPS], API->DB [SQL - asyncpg], API->MAP y API->PUSH [REST/JSON - HTTPS], PUSH->actores [Push/FCM]. | Cumple | Las flechas actor->app solo dicen Usa, sin protocolo ni formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_ROUTB en la organizacion ISCOUTB, visible, con historial de 4 cuentas distintas: MKeinerrr, diegobrr999-commits, juliandmanjarrez-tech y junior14700. | Cumple | Se consolida por cuenta y no se atribuye identidad a personas por parecido de nombre. |
| Estructura minima | Arbol 5b48dd0: docs/arc42/01..12, docs/adr/0001..0003, docs/c4/context.md, docs/aspectos.md, docs/ia.md y README.md. | Cumple | El C4 vive en docs/c4/context.md con niveles 1 a 3; es desviacion de forma, no ausencia del artefacto. |
| Estado del repositorio calificado | origin/master, hash calificado 5b48dd0 con fecha 2026-09-13T23:43:22-05:00, anterior al cierre 2026-09-21; commits_tardios_post_cierre vacio. | Cumple | Modo early: se califica el ultimo commit previo al cierre en la rama principal. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md, 0002-usar-arquitectura-interna-por-capas.md y 0003-control-atomico-de-cupos.md; nombres numerados en kebab-case, con contexto, opciones, decision, consecuencias y trazabilidad. | Cumple | 0001 incluye matriz de decision con alternativas descartadas. |
| Tabla de aspectos | docs/aspectos.md con filas de ID, aspecto, requisito, contextos, C4, ADR, codigo, pruebas y evidencia, con enlaces navegables a los artefactos. | Cumple | Cuatro filas con la cadena completa; enlaza a modulos y pruebas existentes. |
| Registro de uso de IA | docs/ia.md existe y acumula 7 commits (ultimo 39b9658 del 2026-09-13), pero no se aporto su contenido. | No verificado | No se puede comprobar la columna de lo rechazado y su motivo; haria falta citar el texto del archivo. |
| README | README.md documenta pasos manuales (git clone, python -m venv, pip install -r requirements.txt, flutter pub get, uvicorn en una terminal y flutter run en otra) sin un unico comando de arranque. | No cumple | El arranque y las pruebas quedan repartidos en pasos manuales no automatizados. |
| Pipeline y analisis estatico | Existe .github/workflows/ci.yml, pero no hay sonar-project.properties en el arbol, ni linea del scanner, ni URL publica de SonarCloud con Quality Gate. | No cumple | El unico run citado esta en README.md como enlace externo y no se pudo confirmar contra runs_ci. |
| Secretos | El grep sobre HEAD solo devuelve identificadores password y hashed_password en codigo y pruebas; ls-files no muestra ningun .env versionado. | Cumple | No se hallaron credenciales reales ni claves privadas; hallazgos son falsos positivos de la expresion regular. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `5b48dd03dcd0e47b54b5683ebc243f626cf9f500 2026-09-13T23:43:22-05:00 Semana 6`
- **Veredicto**: con pendientes
- Resumen: En la punta de origin/master (5b48dd0, 2026-09-13) el proyecto tiene documentacion arquitectonica solida, estructura completa y sin secretos, pero la entrega de S7 no esta: no hay contrato de API ejecutable, no hay prueba de contrato ni evidencia de su fallo, y falta el ADR de estrategia de integracion.

Pendientes que siguen abiertos:
- Contrato OpenAPI o AsyncAPI versionado con rutas y esquemas.
- Prueba de contrato invocada desde el pipeline y evidencia de fallo ante cambio incompatible.
- ADR de estrategia de integracion sincrona o asincrona ligado a un escenario de calidad.
- Evidencia auditable de SonarCloud: configuracion, run exitoso y URL del Quality Gate.
- Comando unico de arranque y prueba en el README.
- Contenido verificable del registro de uso de IA.

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecucion de la prueba de contrato en el pipeline: no se aporto contenido de .github/workflows/ci.yml ni runs_ci; haria falta el grep de contract/pact/schemathesis y la URL del run.
- Fallo de la prueba de contrato ante cambio incompatible: no hay run en rojo ni evidencia aportada por el equipo.
- Contenido de docs/ia.md, en especial la columna de lo rechazado y su motivo.
- Estado real del pipeline y del Quality Gate de SonarCloud en el hash 5b48dd0: sin runs_ci ni URL publica del analisis.

## Hallazgos para la planilla

- No existe contrato OpenAPI, AsyncAPI ni proto en la punta revisada.
- No hay prueba de contrato ni evidencia de que falle ante un cambio incompatible.
- Los ADR cubren estilo arquitectonico y concurrencia de cupos, no la estrategia de integracion sincrona o asincrona.
- La documentacion arc42 y el C4 nivel 2 estan completos y etiquetados por protocolo y formato.
- No hay evidencia auditable de SonarCloud: sin configuracion, sin linea del scanner y sin URL del analisis.
- El README no ofrece un comando unico de arranque y prueba.
- Transversal: 5 de 8 filas cumplen, con IA sin contenido verificable y pipeline/analisis estatico sin conformidad.
