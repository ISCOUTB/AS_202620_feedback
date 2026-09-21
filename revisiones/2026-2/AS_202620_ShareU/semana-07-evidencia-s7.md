# semana-07-evidencia-s7 · ShareU

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `29184bc` en `origin/master` (2026-09-20T23:34:09-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.yaml en el commit 29184bc: 'openapi: 3.1.0' con bloque 'paths' de 7 rutas. | Cumple | El archivo se movió a docs/api/ en el propio commit calificado (Rename openapi.yaml to docs/api/openapi.yaml). |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.yaml, 'components.schemas': Estado, EstadoModulo, DocumentoResumen (8 propiedades requeridas), ResultadoBusqueda y ErrorValidacion, referenciados con $ref desde cada respuesta 200. | Cumple | Los 200 y el 422 de /busqueda/documentos llevan esquema y ejemplos, no solo descripción. |
| Correspondencia entre el contrato y la API implementada | La evidencia no incluye el contenido de app/main.py ni de app/*/router.py, solo el listado de rutas del árbol. | No verificado | El README nombra /health, los cinco /ping y /busqueda/documentos, pero es documentación; haría falta citar router.py:línea para dos rutas del contrato y una del código ausente del contrato. |
| Versión de la API declarada y con historial | docs/api/openapi.yaml declara 'info.version: 1.0.0' y un comentario final 'Historial de versiones del contrato · 1.0.0 (2026-09, Semana 7)'; el commit 29184bc renombra el contrato y 15f25b8 lo incorpora. | Cumple | Historial corto (alta y rename) pero trazable en git sobre la ruta del contrato. |
| Prueba de contrato presente | Se esperaba un archivo de prueba de contrato; el árbol de 29184bc solo tiene tests/test_busqueda.py y tests/test_esqueleto.py, sin test de contrato ni dependencia de schemathesis, dredd, pact o prism. | No cumple | No existe prueba que consuma docs/api/openapi.yaml contra la API implementada. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/tests.yml solo ejecuta 'pip install --require-hashes -r requirements.txt' y 'PYTHONPATH=. pytest -q'; no hay ningún comando de contrato, y los runs 'Tests' (p. ej. 35561494254) solo corren pytest. | No cumple | Se buscó contract/dredd/schemathesis/pact/prism/spectral/openapi en el workflow y no aparece ninguna invocación. |
| Evidencia de que la prueba falla ante un cambio incompatible | Los únicos runs en rojo son del 2026-09-14 (34801362933, 34798284268, 34794259086), anteriores a la existencia del contrato, y no hay evidencia aportada de un cambio incompatible. | No verificado | Queda como pregunta de sustentación: haría falta el run fallido de la prueba de contrato o el diff incompatible documentado. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0004-integracion-sincrona-y-asincrona.md decide síncrono hacia almacenamiento y asíncrono hacia correo, con acoplamiento temporal, modos de fallo y las alternativas descartadas de cada lado. | Cumple | La justificación se apoya en acoplamiento y modos de fallo, pero no enlaza explícitamente con una fila de docs/aspectos/aspectos.md. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42.md, '# 6. Vista de ejecución': 'Escenario: buscar material' (6 pasos router→servicio→repositorio→SQLite) y 'Escenario: sin resultados'. | Cumple | Los flujos están descritos paso a paso y no solo enumerados. |
| C4 nivel 2 con protocolo y formato en cada flecha | En docs/c4/nivel2.mmd solo algunas flechas etiquetan ('Rel(web, api, "Consume", "JSON/HTTPS")', 'Rel(documentos, db, "Lee y escribe", "SQL")'); otras como 'Rel(estudiante, web, "Utiliza")', 'Rel(api, usuarios, "Enruta solicitudes")', 'Rel(busqueda, documentos, ...)', 'Rel(api, storage, ...)' y 'Rel(api, mail, ...)' no indican protocolo ni formato. | No cumple | docs/c4/nivel-2.md repite el flujo en texto sin etiquetar las flechas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_ShareU bajo la organización ISCOUTB, público (visible: true), con runs y análisis referidos al mismo repo; identidades git consolidadas: Dayana y daynarvaez (mismo correo, una sola cuenta), Nicolas-HH, luiscorredor y steven. | Cumple | Cuatro identidades git frente a cuatro integrantes declarados; la pertenencia a la organización no se puede comprobar con la evidencia aportada. |
| Estructura mínima | HEAD 29184bc contiene docs/arc42/arc42.md, docs/adr/, docs/c4/, docs/aspectos/aspectos.md, docs/ia/ia.md y README.md. | Cumple | Desviación de ruta en dos artefactos (docs/aspectos/aspectos.md y docs/ia/ia.md en vez de docs/aspectos.md y docs/ia.md): desviación de estructura, no ausencia. |
| Convenciones de ADR | docs/adr/0001..0004 siguen el patrón NNNN-kebab-case con estado, contexto, alternativas y consecuencias, pero docs/adr/ShareU_Trazabilida.pdf incumple el patrón NNNN-titulo.md: el chequeo 'ls docs/adr \| grep -Ev ^[0-9]{4}-...' no queda vacío en 29184bc. | No cumple | Los ADR 0003 y 0004 están en estado Propuesto; el PDF no es un ADR pero contamina la carpeta que el contrato normaliza. |
| La tabla de aspectos | docs/aspectos/aspectos.md, sección 'Trazabilidad', tiene 6 columnas (Requisito/Aspecto/ADR/Código/Prueba/Evidencia) con 2 filas, sin las columnas ID ni C4 de las ocho exigidas. | No cumple | Los enlaces navegan y están fijados al hash b7737be, pero la cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia queda incompleta. |
| Registro de uso de IA | docs/ia/ia.md tiene tabla por semana con tarea, uso de IA, 'Qué se rechazó y por qué', resultado/evidencia y revisión humana (p. ej. rechazo del hash-locking y de presentar la métrica HTTP como prueba con usuarios). | Cumple | El comando transversal 'git log -- docs/ia.md' no devuelve commits porque el archivo vive en docs/ia/ia.md. |
| README | README.md describe qué es el sistema, requisitos previos (Python 3.10+, pip), instalación, arranque con 'uvicorn app.main:app --reload' y pruebas con 'pytest -q'. | Cumple | El arranque encadena venv, instalación y ejecución, pero todos los pasos están documentados en el propio README. |
| Pipeline y análisis estático | .github/workflows/tests.yml ejecuta pytest y tiene run exitoso en la rama revisada (35561494254, 2026-09-21T04:34:11Z), pero no hay paso que invoque el scanner de SonarCloud ni archivo sonar-project.properties; la única mención es el badge del README. | No cumple | Faltan dos de las tres evidencias exigidas: la línea del workflow con el scanner y la URL pública del análisis con Quality Gate para el hash revisado. |
| Secretos | El chequeo de secretos sobre HEAD 29184bc no devuelve coincidencias y la lista de .env versionados está vacía. | Cumple | Sin hallazgos de credenciales ni de archivos de entorno en el repositorio. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `29184bc3f3f917e0058f7f78bde6d52eb4798887 2026-09-20T23:34:09-05:00 Rename openapi.yaml to docs/api/openapi.yaml`
- **Veredicto**: con pendientes
- Resumen: A HEAD 29184bc (2026-09-20T23:34:09-05:00), sin commits posteriores al cierre ni diferencias con el estado calificado, el equipo tiene contrato OpenAPI versionado con esquemas, ADR de integración y arc42 sección 6, pero no presenta prueba de contrato ni su ejecución en el pipeline y mantiene pendientes transversales (tabla de aspectos incompleta, C4 sin etiquetar, SonarCloud no auditable, PDF fuera de convención en docs/adr/).

Resuelto tarde (corregido despues del cierre, ahora al dia):
- La triplicación del árbol (AS_202620_ShareU-master/, shareu_base/) señalada en la revisión de semana 5 ya no aparece en el árbol de 29184bc, según se documenta en correcciones.md.
- Los commits 0bae184 (2026-09-14, borrado de docs/adr/ShareU_Trazabilidad.pdf) y f189703 (2026-09-20, Update requirements.in) corrigen entregas anteriores sobre trazabilidad y versiones de dependencias.

Pendientes que siguen abiertos:
- Prueba de contrato en el pipeline y evidencia de que falla ante un cambio incompatible (criterios 5 a 7 de la ficha).
- Correspondencia contrato-código sin evidencia citable de los routers.
- C4 nivel 2 con protocolo y formato en cada flecha.
- Tabla de aspectos con las ocho columnas del contrato (faltan ID y C4).
- SonarCloud auditable: paso del scanner en el workflow y URL pública del análisis con Quality Gate para el hash revisado.
- Carpeta docs/adr/ con un PDF ajeno a la convención de nombres.

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correspondencia contrato-código: falta el contenido de app/main.py y app/*/router.py en la evidencia; haría falta citar dos rutas del contrato en el código y una del código en el contrato.
- Fallo de la prueba de contrato: no hay run en rojo posterior al contrato ni evidencia del cambio incompatible; haría falta el run fallido o el diff documentado.
- Ejecución del scanner de SonarCloud: no hay run ni URL pública de análisis para 29184bc; haría falta el paso del workflow y el enlace al Quality Gate.
- Pertenencia de las cuentas a la organización ISCOUTB: no verificable con la evidencia aportada.

## Hallazgos para la planilla

- El contrato OpenAPI 3.1 con esquemas y versión 1.0.0 está versionado en docs/api/openapi.yaml (29184bc).
- No existe prueba de contrato: el árbol solo tiene tests/test_busqueda.py y tests/test_esqueleto.py.
- El workflow tests.yml no invoca ninguna herramienta de contrato; solo ejecuta pytest.
- No hay evidencia de que la prueba de contrato falle ante un cambio incompatible (los runs en rojo son del 14-09, anteriores al contrato).
- docs/c4/nivel2.mmd deja varias flechas sin protocolo ni formato.
- docs/aspectos/aspectos.md no tiene las columnas ID ni C4 del contrato.
- SonarCloud no es auditable: no hay scanner en el workflow ni URL pública del análisis con Quality Gate para el hash revisado.
- docs/adr/ contiene ShareU_Trazabilida.pdf, que rompe la convención NNNN-titulo.md.
- La correspondencia contrato-código no se puede comprobar porque la evidencia no incluye el código de los routers.
