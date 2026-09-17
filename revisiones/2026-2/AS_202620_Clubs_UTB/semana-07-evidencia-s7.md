# semana-07-evidencia-s7 · Clubs UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `d2d1450` en `origin/master` (2026-09-15T10:14:52-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de d2d1450 (2026-09-15) sin ningún archivo openapi/swagger/asyncapi .yaml/.json ni .proto; se buscó con ls-tree -r --name-only HEAD \| grep -iE '(openapi\|swagger\|asyncapi).*\.(ya?ml\|json)$\|\.proto$' y no hubo coincidencias. | No cumple | La API solo está descrita en prosa (README.md §7, arc42 03 y 06). |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No hay archivo de contrato que citar; la única ruta documentada es GET /health en docs/arc42/06_vista_de_ejecucion.md @ d2d1450, sin esquemas de datos. | No cumple | Sin contrato no hay rutas ni esquemas que revisar. |
| Correspondencia entre el contrato y la API implementada | No existe contrato contra el que cotejar; los routers backend/src/linkclub/adapters/inbound/api/health_router.py y publicacion_router.py no tienen especificación asociada en el árbol de d2d1450. | No cumple | No se puede tomar ninguna ruta del contrato ni una del código en el contrato. |
| Versión de la API declarada y con historial | No hay campo de versión (info.version/openapi) ni es posible ejecutar git log -- <ruta del contrato> porque el archivo no existe; README.md y arc42 no declaran versión de API @ d2d1450. | No cumple | Sin archivo versionado no hay historial del contrato. |
| Prueba de contrato presente | backend/tests/ solo contiene test_health.py y test_publicaciones.py; búsqueda de contract\|dredd\|schemathesis\|pact\|prism\|spectral\|openapi en el árbol de d2d1450 sin coincidencias. | No cumple | Las pruebas existentes son unitarias/integración de endpoints, no de contrato. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/backend-tests.yml es el único workflow y su paso 'Correr pruebas' ejecuta `pytest tests/ -v`; los runs listados ('Backend tests', success, p. ej. https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/34987143230 del 2026-09-15) no invocan herramienta de contrato. | No cumple | El workflow no contiene ningún comando de contrato. |
| Evidencia de que la prueba falla ante un cambio incompatible | Los runs listados concluyen success (p. ej. run 34987143230) y no hay evidencia aportada por el equipo en el repositorio de d2d1450; además no existe prueba de contrato que pueda fallar. | No verificado | Queda como pregunta de sustentación: haría falta un run en rojo o la evidencia del cambio incompatible. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001-hexagonal.md (estilo arquitectónico) y docs/adr/0002-hexagonal.md (fusión de contextos Actividades/Notificaciones) @ d2d1450; ninguno decide síncrono vs. asíncrono ni descarta una alternativa por acoplamiento. | No cumple | La estrategia de integración no está registrada como decisión. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06_vista_de_ejecucion.md @ d2d1450: diagrama Mermaid de secuencia GET /health (cliente → health_router → CheckHealthUseCase → StatusPort → InMemoryStatusAdapter), descripción paso a paso y vínculo a backend/tests/test_health.py. | Cumple | Documenta un solo flujo (health); el de publicaciones todavía no aparece. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/contexto.md @ d2d1450, diagrama de contenedores: solo APP → API indica 'Solicitudes JSON/HTTPS'; persona → APP ('Usa') y API → Supabase ('Valida tokens de sesión', 'Lee y escribe datos') no declaran protocolo ni formato. | No cumple | Flechas del nivel 2 sin etiquetar con protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio público ISCOUTB/AS_202620_Clubs_UTB; en los metadatos de autor de d2d1450 (2026-09-15) aparecen al menos cuatro identidades distintas (Zavod Dev, Josh Ortega y Josh4OP, Luis-Salas-Reyes, deortahollman-star), y README.md §5 declara 4 integrantes. | Cumple | La pertenencia de cada cuenta a la organización no se puede comprobar en este snapshot; las cuentas que comparten la misma dirección institucional en los metadatos se consolidan como un solo contribuyente. |
| Estructura mínima | Árbol de d2d1450 con docs/arc42/, docs/adr/0001-hexagonal.md y 0002-hexagonal.md, docs/c4/contexto.md, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Faltan las secciones 07 y 11 de arc42 y docs/c4/ concentra los niveles 1 a 3 en un solo archivo. |
| Estado del repositorio que se califica | Rama principal origin/master; commit vigente d2d14508c71639a2adb9acc53be97f50039ed0d8 del 2026-09-15T10:14:52-05:00, anterior al cierre 2026-09-21T05:00:00Z; commits_post_cierre y diff_desde_cierre vacíos. | Cumple | No hay commits posteriores al cierre. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md titula por tema y no por decisión; el archivo 0002-hexagonal.md no nombra la decisión que contiene (fusión en Publicaciones) y docs/arc42/tabla_modulo.md enlaza ../adr/0002-ajuste-contextos-publicaciones.md, ruta inexistente en el árbol de d2d1450. | No cumple | Ambos ADR sí incluyen contexto, opciones, decisión, consecuencias y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md @ d2d1450 usa las columnas ID \| Aspecto de calidad \| Escenario \| Requisito \| C4 \| ADR \| Código \| Pruebas, sin columna Evidencia, y las filas U1, U3, C1, C2 y C3 llevan 'Pendiente' en Código y Pruebas. | No cumple | Solo la fila U2 tiene código y pruebas navegables; el resto son huecos. |
| Registro de uso de IA | docs/ia.md @ d2d1450 con tabla Semana/Integrante/Para qué/Herramienta/Cómo se usó/Motivo y nueve entradas en su historial de commits (última d2d1450). | Cumple | La columna 'Cómo se usó' registra lo no incorporado y su motivo. |
| README | README.md @ d2d1450 describe el sistema, el stack, los requisitos previos (Python 3.10+), el arranque (uvicorn linkclub.main:app --app-dir src) y las pruebas (PYTHONPATH=src pytest tests/ -v). | Cumple | El arranque son varios pasos manuales documentados (venv, pip install, uvicorn), no un único comando. |
| Pipeline y análisis estático | Único workflow .github/workflows/backend-tests.yml (pytest en push/PR a master) con runs exitosos (p. ej. run 34987143230); no hay paso de scanner SonarCloud, ni sonar-project.properties, ni URL pública de análisis con Quality Gate en d2d1450. | No cumple | Sin run en rojo tampoco se comprueba que el pipeline bloquee la integración ante fallos. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `d2d14508c71639a2adb9acc53be97f50039ed0d8 2026-09-15T10:14:52-05:00 Update IA usage log for week 6`
- **Veredicto**: con pendientes
- Resumen: En la punta de origin/master (d2d1450, 2026-09-15, previa al cierre de S7) no existe contrato OpenAPI/AsyncAPI/proto, ni prueba de contrato, ni ADR de estrategia de integración: 1 de 10 criterios de la ficha (arc42 §6) y 5 de 8 del contrato transversal.

Pendientes que siguen abiertos:
- NC-01: datos de clubes hardcodeados en frontend/linkclub/lib/clubs_page.dart (docs/arc42/lista_errores.md).
- NC-02: sin manejo de errores de conexión en backend (docs/arc42/lista_errores.md).
- docs/arc42/tabla_modulo.md desalineada con los tres contextos vigentes, según ADR 0002 y arc42 §8.3.
- Secciones 07 y 11 de arc42 ausentes.
- Contrato de API, prueba de contrato en el pipeline y ADR de estrategia de integración sin entregar (S7).

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Pertenencia de las cuentas del historial a la organización ISCOUTB: se revisaron los metadatos de autor de d2d1450 y haría falta la lista de miembros de la organización.
- Evidencia de que la prueba de contrato falla ante un cambio incompatible: se revisaron los runs de Actions (todos success) y el árbol de d2d1450, sin run en rojo ni evidencia del equipo; haría falta un run fallido o el registro del cambio incompatible.
- Bloqueo de la integración por el pipeline: los runs listados concluyen success; haría falta un run en rojo o la configuración de protección de rama.
- Quality Gate de SonarCloud: se buscó scanner en .github/workflows/, sonar-project.properties y URL pública de análisis, y no existe ninguno; sin análisis no hay estado que verificar.

## Hallazgos para la planilla

- No existe archivo de contrato OpenAPI, AsyncAPI o proto en el árbol de d2d1450.
- No hay prueba de contrato ni herramienta asociada (dredd, schemathesis, pact, prism, spectral) en el repositorio.
- El único workflow ejecuta solo pytest y todos los runs listados concluyen success.
- Los ADR existentes cubren estilo arquitectónico y límites de contextos, no la estrategia de integración síncrona o asíncrona.
- Varias flechas del C4 nivel 2 no declaran protocolo ni formato.
- Sin scanner de SonarCloud en el workflow ni URL pública de análisis con Quality Gate.
- Enlace roto: docs/arc42/tabla_modulo.md apunta a ../adr/0002-ajuste-contextos-publicaciones.md, que no existe.
- Pendientes abiertos a HEAD: NC-01 y NC-02 de docs/arc42/lista_errores.md y la desalineación de tabla_modulo.md.
- Faltan las secciones 07 y 11 de arc42 y la columna Evidencia en docs/aspectos.md.
- Sin coincidencias de secretos y sin archivos .env versionados; el repositorio es público.
