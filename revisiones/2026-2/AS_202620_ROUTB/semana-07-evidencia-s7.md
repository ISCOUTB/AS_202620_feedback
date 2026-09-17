# semana-07-evidencia-s7 · ROUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `dcd3317` en `origin/master` (2026-09-16T21:46:43-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | dcd3317: el árbol completo no contiene archivos openapi/swagger/asyncapi (.yaml/.json) ni .proto. | No cumple | Solo se menciona Swagger autogenerado en docs/adr/0002; no hay archivo de contrato versionado. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No existe archivo de contrato del que citar rutas ni esquemas de respuesta. | No cumple | Sin contrato no hay fragmento que citar. |
| Correspondencia entre el contrato y la API implementada | dcd3317: docs/adr/0003 cita POST /trips/, GET /trips/{trip_id} y POST /trips/{trip_id}/reservations, sin contraparte en un contrato inexistente. | No cumple | La desincronización se da por ausencia total del contrato. |
| Versión de la API declarada y con historial | No hay archivo de contrato, por lo que no hay campo de versión ni git log del contrato. | No cumple | Se esperaba version en el propio archivo o en la ruta. |
| Prueba de contrato presente | dcd3317: backend/tests/ solo tiene conftest.py, test_cupos.py, test_registro.py y test_trips_flow.py. | No cumple | No hay archivo de prueba de contrato (dredd, schemathesis, pact, prism). |
| El pipeline ejecuta la prueba de contrato | dcd3317: .github/workflows/ci.yml existe, pero no se aportó su contenido ni runs_ci. | No verificado | Comando anotado: grep -rniE 'contract\|dredd\|schemathesis\|pact\|prism\|spectral\|openapi' .github/workflows/. |
| Evidencia de que la prueba falla ante un cambio incompatible | Sin run en rojo en runs_ci y sin evidencia aportada por el equipo; además no existe prueba de contrato. | No verificado | Queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | dcd3317: docs/adr/ solo contiene 0001-monolito-modular, 0002-arquitectura-por-capas y 0003-control-atomico-de-cupos. | No cumple | Ningún ADR decide integración síncrona o asíncrona con alternativa descartada. |
| arc42 sección 6 con los flujos de interacción | dcd3317: docs/arc42/06_vista_de_ejecucion.md describe los escenarios 6.1 registro y 6.2 inicio de sesión con diagramas de secuencia. | Cumple | Flujos narrados por capas con aspectos relevantes. |
| C4 nivel 2 con protocolo y formato en cada flecha | dcd3317: docs/c4/context.md nivel 2 etiqueta APP->API [REST/JSON · HTTPS], API->DB [SQL · asyncpg] y API->PUSH [REST/JSON · HTTPS]. | Cumple | Las flechas persona->app solo dicen 'Usa', sin protocolo ni formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible:true; AS_202620_ROUTB en ISCOUTB; historial con 4 cuentas de git distintas (MKeinerrr, diegobrr999-commits, juliandmanjarrez-tech, junior14700). | Cumple | No se atribuyen cuentas a personas y no se pudo comprobar la pertenencia a la organización. |
| Estructura mínima | dcd3317: docs/arc42/01..12, docs/adr/0001-0003, docs/c4/context.md, docs/aspectos.md, docs/ia.md y README.md presentes. | Cumple | El C4 vive en docs/c4/; sin desviación relevante. |
| Convenciones de ADR | dcd3317: docs/adr/0001-usar-monolito-modular.md, 0002-usar-arquitectura-interna-por-capas.md y 0003-control-atomico-de-cupos.md siguen NNNN-kebab-case. | Cumple | Cada uno incluye contexto, opciones, decisión, consecuencias y trazabilidad. |
| Tabla de aspectos | dcd3317: docs/aspectos.md con 4 filas y columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas y Evidencia enlazadas. | Cumple | Añade columna Contextos relacionados; ningún eslabón queda en texto suelto. |
| Registro de uso de IA | docs/ia.md existe y acumula 7 commits entre 2026-08-07 y 2026-09-13, pero no se aportó su contenido. | No verificado | Falta citar la columna de lo rechazado y su motivo técnico. |
| README | dcd3317: README.md describe el sistema, tecnologías, 'Inicio rápido' con start.bat/start.sh y pruebas con pytest. | Cumple | Los requisitos previos se declaran solo de forma parcial (listado de tecnologías). |
| Pipeline y análisis estático | sonar-project.properties presente en dcd3317, pero sin runs_ci, sin la línea del workflow que invoca el scanner y sin URL pública del Quality Gate. | No verificado | El README enlaza un dashboard y un run, que no son evidencia de ejecución; comando anotado: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_ROUTB/actions/runs?per_page=5. |
| Secretos | dcd3317: el grep solo devuelve nombres de variables y valores de prueba (p. ej. hashed_password="hash"), y envs_versionados está vacío. | Cumple | No hay claves, .env versionado ni material privado en el historial reportado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `dcd33171ef4ef022278626ea0c0a2c418997afe3 2026-09-16T21:46:43-05:00 s7 - early`
- **Veredicto**: al dia
- Resumen: En dcd3317 (2026-09-16, entregado antes del cierre y sin commits posteriores) el proyecto tiene estructura documental completa, ADR 0001-0003, arc42 1-12 y C4 de niveles 1 a 3, pero no existe contrato de API, ni prueba de contrato, ni ADR de estrategia de integración: 2 de 10 criterios de la ficha cumplen. No se observan pendientes de semanas anteriores sin resolver ni correcciones posteriores al cierre en la rama principal.

Pendientes que siguen abiertos:
- Contrato de API en formato ejecutable, versionado y con esquemas de datos.
- Correspondencia contrato-API y versión de la API con historial en git.
- Prueba de contrato ejecutada por el pipeline y evidencia de que falla ante un cambio incompatible.
- ADR de la estrategia de integración (síncrona o asíncrona) ligado a un escenario de calidad.
- Evidencia pública de SonarCloud (scanner en el workflow, run del hash revisado y Quality Gate).

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución de la prueba de contrato en el pipeline: falta el contenido de .github/workflows/ci.yml y runs_ci; comprobar con grep -rniE 'contract|dredd|schemathesis|pact' .github/workflows/ y la API de runs.
- Prueba en rojo ante cambio incompatible: no hay run con conclusion distinta de success ni evidencia aportada por el equipo.
- SonarCloud: faltan la línea del workflow que invoca el scanner, la URL del run exitoso del hash revisado y la URL pública del análisis con estado del Quality Gate.
- Contenido de docs/ia.md: no se aporta la columna de lo rechazado y su motivo técnico.

## Hallazgos para la planilla

- No existe contrato de API en formato ejecutable (OpenAPI, AsyncAPI o proto) en el commit calificado.
- No hay prueba de contrato ni evidencia de que falle ante un cambio incompatible.
- Los ADR 0001-0003 cubren estilo arquitectónico y concurrencia, no la estrategia de integración síncrona/async.
- arc42 sección 6 y el C4 nivel 2 sí están y etiquetan protocolo y formato en las flechas entre contenedores.
- La entrega es temprana (dcd3317, 2026-09-16) y sin commits posteriores al cierre.
- La evidencia reporta 'sin commits nuevos' desde el cierre anterior en la rama principal.
- La verificación de SonarCloud y del contenido de docs/ia.md no puede auditarse con lo aportado.
