# semana-07-evidencia-s7 · ShareU

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `0bae184` en `origin/master` (2026-09-14T15:26:52-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol del commit 0bae184 revisado con `git ls-tree -r --name-only HEAD` (openapi\|swagger\|asyncapi\|.proto) sin coincidencias; solo hay código FastAPI. | No cumple | Se esperaba un archivo OpenAPI/AsyncAPI/proto en el repositorio; la única documentación de API es la generada en tiempo de ejecución por FastAPI (`/docs`, citada en README.md). |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No existe archivo de contrato del cual citar versión, `paths` o `schemas` en el árbol de 0bae184. | No cumple | Se esperaba un fragmento con la versión de la especificación, al menos una ruta y su esquema de respuesta; no se encontró ninguno. |
| Correspondencia entre el contrato y la API implementada | Se esperaban dos rutas del contrato localizadas en el código (p. ej. `GET /busqueda/documentos` en app/busqueda/router.py y `/health` en app/main.py) y una ruta del código en el contrato; no hay contrato que contrastar. | No cumple | Sin contrato versionado el ejercicio de doble sentido no puede satisfacerse en ninguna dirección. |
| Versión de la API declarada y con historial | No hay archivo de contrato con campo de versión y `git log` sobre él no es aplicable; los ADR llevan fecha de documento, no versión de API. | No cumple | Se esperaba el campo de versión (en el archivo o en la ruta) y su historial de commits; ninguno aparece. |
| Prueba de contrato presente | tests/ contiene solo test_busqueda.py y test_esqueleto.py en el árbol de 0bae184; no hay archivo de prueba de contrato. | No cumple | No aparecen rastros de dredd, schemathesis, pact, prism ni spectral en el repositorio. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/tests.yml solo instala dependencias y ejecuta `PYTHONPATH=. pytest -q`; ningún comando de contrato. | No cumple | El run más reciente del workflow Tests terminó en success (2026-09-14, https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/34892971998), pero no ejecuta prueba de contrato. |
| Evidencia de que la prueba falla ante un cambio incompatible | No existe prueba de contrato; hay runs en failure (p. ej. 34801362933 y 34798284268) del workflow Tests, sin evidencia de que correspondan a un cambio incompatible de contrato. | No verificado | Haría falta un run en rojo provocado por contrato o la evidencia aportada por el equipo del cambio incompatible; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001-estilo-arquitectonico.md, 0002-usabilidad-busqueda-en-una-solicitud.md y 0003-separacion-contexto-calificaciones.md deciden estilo arquitectónico, flujo de búsqueda y propiedad del dato, no integración síncrona o asíncrona. | No cumple | Se esperaba un ADR que justifique síncrono o asíncrono contra el escenario de usabilidad, con la alternativa descartada y sus consecuencias de acoplamiento. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42.md, sección «6. Vista de ejecución»: escenario «buscar material» en pasos y escenario «sin resultados». | Cumple | Describe el flujo solicitud→router→servicio→repositorio→respuesta y el caso de lista vacía con total 0. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/nivel2.mmd etiqueta protocolo/formato solo en algunas relaciones («Consume», «JSON/HTTPS»; «Lee y escribe», «SQL») y deja otras sin etiquetar («Rel(estudiante, web, "Utiliza")», «Rel(api, usuarios, "Enruta solicitudes")», «Rel(api, storage, "Guarda/recupera archivos")»). | No cumple | docs/c4/nivel-2.md describe contenedores en tabla, pero no aporta cada flecha con protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_ShareU, público y visible (visible: true), con historial de 4 cuentas contribuyentes: Dayana, luiscorredor, Nicolas-HH y steven. | Cumple | Dos entradas de autora comparten la misma dirección institucional y se consolidan en una cuenta; no se atribuyen cuentas a personas por parecido de nombre, por lo que la correspondencia con los integrantes declarados no se afirma. |
| Estructura mínima | Presencia de docs/arc42/arc42.md, docs/adr/0001..0003, docs/c4/ (nivel-2.md, nivel1.mmd, nivel2.mmd, NIVEL2.png), docs/aspectos/aspectos.md, docs/ia/ia.md y README.md en 0bae184. | Cumple | aspectos.md e ia.md viven en subcarpeta propia: desviación de estructura, no ausencia del artefacto. |
| Convenciones de ADR | Los tres archivos de docs/adr/ cumplen el patrón NNNN-titulo-en-kebab-case.md y llevan contexto, alternativas, decisión, consecuencias y trazabilidad; ninguno está reescrito tras aceptarse. | Cumple | El título del ADR 0001 enuncia el tema (estilo arquitectónico) más que la decisión adoptada. |
| La tabla de aspectos | docs/aspectos/aspectos.md tiene encabezado Requisito · Aspecto · ADR · Código · Prueba · Evidencia, sin las columnas ID y C4. | No cumple | La cadena del contrato exige ID · Aspecto · Requisito · C4 · ADR · Código · Pruebas · Evidencia; faltan dos eslabones navegables. |
| Registro de uso de IA | docs/ia/ia.md registra seis usos con columna «Qué se rechazó y por qué» y motivo técnico (p. ej. no presentar la métrica HTTP como prueba con usuarios reales). | Cumple | El historial de commits del archivo no muestra crecimiento por entradas (carga única), aunque el contenido del registro sí está desarrollado. |
| README | README.md declara qué es el sistema, requisitos previos, instalación y arranque con un comando (`uvicorn app.main:app --reload`) y pruebas (`pytest -q`). | Cumple | Añade endpoint de salud y módulos con /ping como verificación rápida. |
| Pipeline y análisis estático | .github/workflows/tests.yml ejecuta pytest en push y pull_request, pero no invoca el scanner de SonarCloud ni existe archivo de configuración de análisis en el árbol, ni URL pública de análisis con Quality Gate en la evidencia. | No cumple | El badge del README no cuenta como evidencia de ejecución; faltan las tres piezas que el contrato exige para marcar esta fila como Cumple. |
| Secretos | Búsqueda de credenciales con `git grep -nIE` sobre HEAD sin coincidencias y sin archivos .env versionados. | Cumple | Sin hallazgos de llaves, tokens ni contraseñas en el último commit. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `0bae18410091824e51739f1bfc6fe0eabf954013 2026-09-14T15:26:52-05:00 Delete docs/adr/ShareU_Trazabilidad.pdf`
- **Veredicto**: con pendientes
- Resumen: A HEAD (0bae184, 2026-09-14) el proyecto conserva el corte vertical de búsqueda, los ADR y la documentación arc42/C4, pero la entrega de la semana 7 no está: no hay contrato de API versionado, ni prueba de contrato en el pipeline, ni evidencia de que falle ante un cambio incompatible, y el análisis estático no es auditable desde el repositorio.

Pendientes que siguen abiertos:
- Contrato de API en OpenAPI o AsyncAPI versionado en el repositorio
- Routes y esquemas de datos dentro del contrato
- Prueba de contrato presente y ejecutada por el workflow
- Evidencia de que la prueba falla ante un cambio incompatible
- ADR de estrategia de integración (síncrona o asíncrona) con alternativa descartada
- Etiquetado de protocolo y formato en cada flecha del C4 nivel 2
- Columnas ID y C4 en la tabla de aspectos
- Paso del scanner de SonarCloud en CI y URL pública del Quality Gate
- Puntos de la revisión del corte 1 aún sin resolver, según correcciones.md (reto/restricción asignada y etiqueta)

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba de contrato que falle ante un cambio incompatible: no existe la prueba; haría falta un run en rojo originado por contrato o la evidencia aportada por el equipo (se revisaron los runs 34892971998 y los failure 34801362933 y 34798284268).
- SonarCloud: sin archivo de configuración, sin línea del scanner en tests.yml y sin URL pública del análisis; haría falta el run que ejecuta el scanner para el hash 0bae184 y la URL del Quality Gate en la rama revisada.

## Hallazgos para la planilla

- No existe ningún archivo de contrato OpenAPI, AsyncAPI o proto versionado en el commit 0bae184.
- El workflow tests.yml solo ejecuta pytest: no hay paso de prueba de contrato ni del scanner de SonarCloud.
- No hay prueba de contrato en tests/ ni evidencia de que falle ante un cambio incompatible.
- La sección 6 de arc42 sí describe los flujos de interacción del corte vertical.
- El C4 nivel 2 deja varias flechas sin protocolo ni formato.
- La tabla de aspectos carece de las columnas ID y C4 exigidas por el contrato.
- Sin commits posteriores al cierre ni diferencias respecto al estado calificado.
- Ningún ADR decide la estrategia de integración síncrona frente a la asíncrona.
