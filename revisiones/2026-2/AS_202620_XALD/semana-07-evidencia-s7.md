# semana-07-evidencia-s7 · XALD

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `b00b319` en `origin/master` (2026-09-17T00:01:02-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.yaml en b00b319: 'openapi: 3.1.0', info.version 1.0.0, servidor /api/v1, archivo presente en el árbol del commit calificado. | Cumple | Formato ejecutable (YAML OpenAPI), no prosa; una sola ruta documentada. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.yaml: paths./transacciones.post con requestBody $ref TransaccionDTO y respuestas 202/400/422 con $ref a RespuestaSincronizacion, ErrorRespuesta y ErrorValidacion; components.schemas define TransaccionDTO con 7 campos tipados (monto number/double, moneda minLength 3, fecha_transaccion date-time). | Cumple | Esquemas de datos presentes y con restricciones; cobertura de una sola ruta. |
| Correspondencia entre el contrato y la API implementada | El contrato declara 'Servidor de Desarrollo Local (FastAPI)' en http://localhost:8000/api/v1, mientras el backend versionado es backend_xald/index.js + package.json (Node); no se aportó el contenido de index.js ni de PayloadSincronizacionDTO.kt/TransaccionEntidad.kt. | No verificado | Haría falta cotejar POST /transacciones en backend_xald/index.js y localizar una ruta del código en el OpenAPI; se esperaba además ver si el path /transacciones coincide con el handler. |
| Versión de la API declarada y con historial | Declarada: info.version 1.0.0 y servidor /api/v1 en docs/api/openapi.yaml (b00b319); sin salida de 'git log -- docs/api/openapi.yaml' en la evidencia. | No verificado | Versión citada, pero historial de versionado no comprobado; falta el log del archivo. |
| Prueba de contrato presente | Se esperaba archivo de prueba de contrato (dredd/schemathesis/pact/prism/spectral o test que consuma openapi.yaml); el árbol completo de b00b319 solo lista pruebas unitarias: XALDAPP/app/src/test/java/com/proyecto/xald/Cortevertical.kt, Entornotest.kt, ValidacionModulosTest.kt, ExampleUnitTest.kt y un ExampleUnitTest por módulo. | No cumple | Ningún nombre de prueba apunta al contrato; ValidacionModulosTest verifica imports cruzados, no el contrato. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml en el árbol, pero no se aportó su contenido ni runs de Actions (no hay runs_ci en la evidencia). | No verificado | Comando pendiente: grep -rniE 'contract\|dredd\|schemathesis\|pact\|prism\|spectral\|openapi' .github/workflows/ y curl a /repos/ISCOUTB/AS_202620_XALD/actions/runs; haría falta la línea del workflow que invoca la prueba y la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | No se aportó run en rojo ni evidencia de un cambio incompatible; no hay runs de Actions en la evidencia ni prueba de contrato en el árbol. | No verificado | Comando anotado: curl -s 'https://api.github.com/repos/ISCOUTB/AS_202620_XALD/actions/runs?per_page=50' filtrando conclusion != success; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001-patron-offline-first.md: opciones descartadas (cliente-servidor tradicional, sincronización periódica) y decisión de persistencia local con envío asíncrono por cola, ligada a ESC-01, ESC-05, RT-02 y RT-05; docs/adr/0007-contratos-por-modulo.md añade alternativa descartada y riesgos de acoplamiento del orquestador. | Cumple | Justifica lo asíncrono contra escenarios de calidad y declara consecuencias de acoplamiento; trazabilidad a aspectos y módulos incluida. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06-Runtime view.md: escenarios 6.1 a 6.4 con diagramas de secuencia Mermaid y pasos numerados por módulo (:parser, :aigemini, :corefinanciero, :syncqueue, :app). | Cumple | Describe flujos y reconoce explícitamente la reclasificación pendiente de implementar. |
| C4 nivel 2 con protocolo y formato en cada flecha | El árbol de b00b319 incluye docs/c4/c2.md, pero su contenido no fue aportado; docs/arc42/03-Context and Scope.md sí tabula protocolo y formato (HTTPS/REST, JSON, AES-256), lo que no verifica el diagrama C2. | No verificado | Haría falta el contenido de docs/c4/c2.md para comprobar que cada flecha lleva protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_XALD, organizacion ISCOUTB, visible: true y público; 4 cuentas con commits en el historial (171/78/53/38 commits). | Cumple | No se atribuyen las cuentas a personas por parecido de nombre: no se comprueba que las 4 cuentas correspondan a los 4 integrantes declarados. |
| Estructura mínima | b00b319 incluye docs/arc42/ (01-12), docs/adr/0001-0007, docs/c4/c1-c4.md, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Desviación menor: el código vive en XALDAPP/ y backend_xald/, no en la raíz. |
| Qué estado del repositorio se califica | Rama principal origin/master con hash b00b319 y fecha 2026-09-17T00:01:02-05:00, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | Entrega temprana; no hay commits posteriores al cierre en la evidencia. |
| Convenciones de ADR | docs/adr/0001-0007 con nombres NNNN-kebab-case y títulos que enuncian la decisión; cada archivo trae contexto, opciones evaluadas, decisión, consecuencias y trazabilidad. | Cumple | Indicios de edición posterior no verificables sin 'git log --follow': adenda en 0002 (Aprobado) y 0006 marcado 'Actualizado'; 0005 sigue 'En revisión'. |
| La tabla de aspectos | docs/aspectos.md existe en el árbol y los ADR citan aspectos A-01 a A-04, pero no se aportó el contenido del archivo. | No verificado | Haría falta ver las 8 columnas (ID · Aspecto · Requisito · C4 · ADR · Código · Pruebas · Evidencia) y que cada celda sea navegable. |
| Registro de uso de IA | docs/ia.md con historial de 12 commits entre 2026-08-07 y 2026-09-13 (ia_log: 09bdb18 ... e90d589), crecimiento sostenido a lo largo del semestre. | Cumple | El contenido (qué se rechazó y por qué) no se aportó; solo se verifica existencia y evolución. |
| README | README.md describe el sistema, requisitos previos (JDK 17, Android SDK) y comandos de arranque y prueba (gradlew.bat test, comando único tras fijar JAVA_HOME y ANDROID_HOME). | Cumple | El arranque exige configurar variables de entorno antes del comando, paso manual que sí está documentado. |
| Pipeline, análisis estático y secretos | Existe .github/workflows/ci.yml pero no se aportó su contenido ni runs_ci; no hay sonar-project.properties en el árbol ni URL pública de SonarCloud con Quality Gate. Sin secretos detectados ('sin coincidencias') y sin .env versionados. | No verificado | Comando pendiente: ls .github/workflows/ y curl a /repos/ISCOUTB/AS_202620_XALD/actions/runs; desde S6 se exigen configuración + run exitoso + URL pública de SonarCloud. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `b00b31921ff05a18cdb81bf809c86f828680be71 2026-09-17T00:01:02-05:00 Add OpenAPI specification for Financial Synchronization API`
- **Veredicto**: al dia
- Resumen: Se evalua la punta de origin/master en b00b319 (2026-09-17T00:01:02-05:00), anterior al cierre 2026-09-21T05:00:00Z, es decir entrega temprana. El proyecto esta al dia en la rama principal: no hay commits posteriores al cierre ni correcciones tardias registradas, y la documentacion arquitectonica (arc42, ADR, C4, aspectos, ia, README) esta presente en el arbol. La entrega de la semana queda a medias: contrato y ADR cumplen, pero no hay prueba de contrato ni evidencia de ejecucion del pipeline, y quedan sin verificar la correspondencia contrato-codigo, el C2 y SonarCloud.

Pendientes que siguen abiertos:
- Prueba de contrato inexistente en el arbol de b00b319.
- Sin evidencia de ejecucion de CI (runs) ni analisis SonarCloud publico con Quality Gate.
- Correspondencia contrato-codigo sin verificar; el contrato declara FastAPI y el backend versionado es Node.
- Sin historial git del contrato y sin contenido aportado de docs/c4/c2.md ni docs/aspectos.md.

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correspondencia contrato-código: falta el contenido de backend_xald/index.js y de las clases de dominio para localizar POST /transacciones y una ruta del código en el OpenAPI.
- Historial del contrato: falta 'git log --format=%h %cI %s -- docs/api/openapi.yaml'.
- Ejecución del pipeline: falta el contenido de .github/workflows/ci.yml y los runs de Actions (curl a /repos/ISCOUTB/AS_202620_XALD/actions/runs).
- Fallo de la prueba de contrato ante cambio incompatible: sin run en rojo ni evidencia aportada del cambio que la rompe.
- Contenido de docs/c4/c2.md (protocolo y formato en cada flecha) y de docs/aspectos.md (8 columnas navegables).
- SonarCloud: falta configuración del scanner, run exitoso y URL pública del análisis con estado del Quality Gate.

## Hallazgos para la planilla

- El contrato OpenAPI 3.1.0 existe y es ejecutable, con esquemas de datos y versión 1.0.0, pero documenta una sola ruta.
- No existe ninguna prueba de contrato en el árbol completo de b00b319; solo pruebas unitarias de módulos.
- No se aportaron runs de CI ni URL pública de SonarCloud con Quality Gate.
- El contrato declara servidor FastAPI en localhost:8000 y el backend versionado es Node (backend_xald/index.js), sin cotejo de rutas.
- La versión de la API está declarada pero no se aportó el historial git del archivo del contrato.
- Sin secretos detectados en HEAD ni .env versionados.
- No hay commits posteriores al cierre en la evidencia: la entrega quedó registrada antes del cierre.
