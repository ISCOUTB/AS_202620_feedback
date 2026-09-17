# semana-07-evidencia-s7 · AudioShare

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `4a0eba9` en `origin/master` (2026-09-13T22:01:57-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de 4a0eba9 no incluye ningún archivo openapi/asyncapi/proto; solo src/, tests/, public/ y docs/ | No cumple | Se esperaba un archivo de contrato versionado y no existe en la punta calificada. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | Sin archivo de contrato en 4a0eba9 no hay rutas ni esquemas de respuesta que citar | No cumple | La ausencia se confirma sobre el mismo árbol revisado. |
| Correspondencia entre el contrato y la API implementada | La API real (src/app.ts, tests/a01.test.ts) maneja /rooms, /rooms/:roomId y /play, pero no existe contrato contra el que cotejar | No cumple | No es posible el doble cotejo por falta del artefacto. |
| Versión de la API declarada y con historial | No hay archivo de contrato ni campo de versión; git log del contrato no aplica | No cumple | Se esperaba versión en el archivo o en la ruta más su historial. |
| Prueba de contrato presente | tests/ solo contiene a01.test.ts y health.test.ts en 4a0eba9 | No cumple | No existe archivo de prueba de contrato (dredd, schemathesis, pact, prism, spectral u otro). |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml es el único workflow y no hay prueba de contrato que invocar; no se aportaron runs_ci | No cumple | Sin prueba de contrato el pipeline no puede ejecutarla; falta la línea del workflow y la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | No se aportó run en rojo ni evidencia de cambio incompatible; sin runs_ci en la evidencia | No verificado | Pregunta de sustentación: si no se demostró el fallo, la prueba no acredita valor; verificar con el listado de runs de Actions. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001-usar-monolito-modular.md decide el estilo arquitectónico, no la integración síncrona o asíncrona | No cumple | Se esperaba un ADR que justifique el mecanismo de comunicación frente a un escenario y su alternativa descartada. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/src/06_runtime_view.adoc describe creación de sala, incorporación de receptor, transmisión y pausa/reanudación con diagramas | Cumple | Los flujos están descritos como interacción entre bloques. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4 Nivel 2 - Contenedores.mmd etiqueta las flechas con [HTTPS], [JSON / HTTPS REST], [NDJSON / HTTP streaming] y [SQL / better-sqlite3] | Cumple | Cada relación indica propósito, protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_AudioShare en la organización ISCOUTB (visible=true) en 4a0eba9; 4 identidades de autor en el historial (50/41/36/31 commits) | Cumple | Tres cuentas con dominio institucional y una cuenta tipo handle; no se atribuye por parecido de nombre. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes en 4a0eba9 | Cumple | arc42 en .adoc bajo docs/arc42/src/: desviación de extensión/ubicación, pero el artefacto existe. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md sigue el patrón NNNN-kebab-case | Cumple | Un solo ADR; su decisión es el estilo arquitectónico, no la estrategia de integración. |
| Tabla de aspectos | docs/aspectos.md trae la matriz de A-01 con enlaces a requisito, ADR-0001, C4 nivel 2, código y pruebas | Cumple | No hay columna rotulada 'Evidencia' explícita, aunque los enlaces sí son navegables. |
| Registro de uso de IA | docs/ia.md incluye tabla con la propuesta de IA rechazada y su motivo, y su historial git se extiende a lo largo del semestre | Cumple | La columna de lo rechazado está diligenciada por uso. |
| README | README.md declara qué es, requisitos (Node.js 22+), arranque con `npm run dev` y prueba con `npm test`/`npm run verify` | Cumple | El arranque queda en un único comando documentado. |
| Pipeline y análisis estático | .github/workflows/ci.yml es el único workflow; no hay sonar-project.properties en el árbol ni URL de run o de SonarCloud aportada | No cumple | Faltan las tres evidencias exigidas: configuración, run exitoso y URL pública con Quality Gate. |
| Secretos | git grep de patrones de credenciales sin coincidencias y .env no versionado (solo .env.example) en 4a0eba9 | Cumple | Sin incidentes de secreto en el estado calificado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `4a0eba994357cba432178075dd872e0b52643595 2026-09-13T22:01:57-05:00 Revise documentation for week 6 updates`
- **Veredicto**: con pendientes
- Resumen: En la punta de origin/master (4a0eba9, 2026-09-13, entrega temprana) el proyecto no tiene contrato ejecutable, ni prueba de contrato, ni ADR de estrategia de integración, y no hay evidencia de SonarCloud; solo cumplen arc42 §6 y C4 nivel 2.

Pendientes que siguen abiertos:
- Contrato OpenAPI/AsyncAPI/proto versionado con rutas y esquemas
- Prueba de contrato presente y ejecutada por el pipeline
- Evidencia de fallo de la prueba ante cambio incompatible
- ADR de estrategia de integración con alternativa descartada
- Evidencia de SonarCloud: configuración, run exitoso y URL pública con Quality Gate

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución y fallo de la prueba de contrato: no se aportaron runs_ci; haría falta el listado de runs de Actions (curl a api.github.com/repos/ISCOUTB/AS_202620_AudioShare/actions/runs) o la evidencia del cambio incompatible.
- Contenido de .github/workflows/ci.yml: no se aportó el archivo; haría falta `ls .github/workflows/` y `grep -niE 'contract|spectral|schemathesis|prism|pact' .github/workflows/`.

## Hallazgos para la planilla

- No existe archivo OpenAPI/AsyncAPI/proto en la punta 4a0eba9: falta el contrato de la API principal.
- No hay prueba de contrato ni invocación de contrato en el pipeline.
- No se aportó run en rojo ni evidencia del cambio incompatible que hiciera fallar la prueba.
- El único ADR decide el estilo arquitectónico, no la estrategia de integración síncrona o asíncrona.
- Sin sonar-project.properties, sin URL de run y sin URL pública de SonarCloud con Quality Gate.
- arc42 §6 y C4 nivel 2 sí están presentes y etiquetan protocolo y formato por flecha.
- Sin secretos expuestos ni .env versionado; identidad y estructura mínima conformes.
