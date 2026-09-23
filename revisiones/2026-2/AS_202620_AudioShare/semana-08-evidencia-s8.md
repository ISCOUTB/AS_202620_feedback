# semana-08-evidencia-s8 · AudioShare

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `d094a51` en `origin/master` (2026-09-21T00:21:38-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | La evidencia del commit d094a51 (2026-09-21T00:21:38-05:00) no incluye URL del sistema ni registro de comprobación con hora. | No verificado | Falta la URL y el resultado de `curl -sS -o /dev/null -w 'http=%{http_code} tiempo=%{time_total}s\n' "$URL"` con la hora exacta. |
| Health check consultable | El árbol de d094a51 contiene `tests/health.test.ts`, pero no se declara ruta de health ni hay URL desplegada que consultar. | No verificado | El equipo no declara ninguna ruta; sin despliegue no hay código de respuesta para `/health`. |
| Infraestructura como código versionada en el repositorio | En d094a51 solo aparecen `.devcontainer/Dockerfile`, `.devcontainer/devcontainer.json` y `.github/workflows/`; no hay compose, terraform, k8s, helm, fly.toml, render.yaml, railway ni Procfile. | No cumple | El devcontainer describe el entorno de desarrollo en Codespaces, no el entorno desplegado. |
| El entorno se puede recrear siguiendo el README | README.md, secciones Requisitos, Instalación (`flutter pub get`, `npm ci`), Ejecución (`npm run dev`) y Tests (`flutter analyze`, `flutter test`, `npm test`). | Cumple | El procedimiento recrea el entorno local con un comando; no cubre el entorno desplegado. |
| Pipeline en verde sobre la rama principal | Existen `.github/workflows/ci.yml` y `.github/workflows/flutter.yml` en d094a51, pero no se aporta ningún run con conclusión ni URL. | No verificado | Falta el último run de origin/master; comando anotado: `curl -s "https://api.github.com/repos/ISCOUTB/AS_202620_AudioShare/actions/runs?per_page=10"`. |
| Logs estructurados | Ni el árbol de d094a51 ni la documentación aportada contienen configuración de logging (pino, winston, structlog, logback, serilog) ni una línea de ejemplo. | No cumple | No hay archivo de configuración de registro ni ejemplo de campos estructurados. |
| Métrica consultable asociada a un escenario de calidad | `docs/escenarios_calidad.md` define EC-01 a EC-04 con umbrales (100 ms, 200 ms, 3 s), pero no hay métrica emitida ni consultable en el repositorio. | No cumple | Sin métrica ni instrumentación no hay escenario asociado que verificar. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example` en la raíz, `envs_versionados: []` y barrido de secretos sin coincidencias sobre d094a51. | Cumple | Se verifica que no hay credenciales en el repositorio; no hay despliegue configurado del que se tomen del almacén y no se aporta el contenido del workflow. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No existe documento de costos en el árbol; solo R-01 de `docs/Restricciones_justificadas.md` pide herramientas gratuitas. | No cumple | Falta volumen supuesto, costo por pieza y punto de ruptura de la capa gratuita. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/src/` en d094a51 no contiene `07_deployment_view.adoc` (sí 01-06, 08-10 y 12). | No cumple | La plantilla `arc42-template.adoc` incluye el `include` de la sección 7, pero el archivo no existe. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/src/02_architecture_constraints.adoc` lista solo restricciones técnicas (Flutter/Dart, Node/Express, SQLite, Wi-Fi local, audio físico fuera de alcance). | No cumple | El límite de costo no aparece en la sección 2; R-01 lo menciona en `docs/Restricciones_justificadas.md`, fuera de arc42. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/` en d094a51 contiene 0001-monolito-modular, 0002-estrategia-integracion y 0003-transicion-a-flutter; ninguno decide plataforma de despliegue. | No cumple | No hay alternativa de plataforma descartada ni capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio: organización ISCOUTB, nombre AS_202620_<PROYECTO>, público e integrantes en el historial | `repo: AS_202620_AudioShare`, `visible: true`, rama `origin/master`; historial con cuatro identidades de autor (Elian Daniel Perea Vanegas, Yeiver Andrés Vergel Pérez, Santiago Adolfo Camacho Hernández y la cuenta cardonavincent26-design). | Cumple | No se verifica membresía de las cuentas en la organización y la cuenta cardonavincent26-design no se atribuye a una persona por parecido de nombre. |
| Estructura mínima del repositorio (docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md) | El árbol de d094a51 contiene `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Faltan las secciones 07 y 11 de arc42 y la documentación está en asciidoc, no en Markdown revisable como pide la convención. |
| Estado calificado: último commit de master o main anterior o igual al cierre | `hash_calificado: d094a51`, fecha 2026-09-21T00:21:38-05:00, sobre `origin/master`, anterior al cierre 2026-09-28T05:00:00Z. | Cumple | Entrega en modo early; no hay commits posteriores al cierre en `commits_tardios_post_cierre`. |
| Convenciones de ADR: un archivo por decisión, numerado, con contexto, opciones, decisión, consecuencias y trazabilidad | 0001 y 0002 cumplen la convención, pero `docs/adr/0003-transicion-a-flutter.md` no incluye alternativas evaluadas ni bloque de trazabilidad (requisito/aspecto, C4, implementación, pruebas). | No cumple | Además, `docs/aspectos.md` enlaza a `0002-cliente-flutter-backend-modular.md`, que no existe en `docs/adr/`. |
| Tabla de aspectos con las ocho columnas navegables | `docs/aspectos.md` usa columnas propias (Escenario, Objetivo/métrica, Decisión arquitectónica) en vez de las ocho del curso y su columna ADR apunta a un archivo inexistente. | No cumple | Un enlace que no lleva a ninguna parte cuenta como hueco en la fila de trazabilidad. |
| Registro de uso de IA con lo aceptado y lo rechazado y por qué | `docs/ia.md` existe y crece (13 commits entre 2026-08-09 y 2026-09-20, último 5a6d73b), pero no se aporta su contenido. | No verificado | Haría falta el archivo para comprobar la columna de lo rechazado con su motivo técnico. |
| README: qué es, cómo se arranca con un solo comando y cómo se prueba | README.md describe el sistema, el arranque con `npm run dev`, las pruebas (`flutter analyze`, `flutter test`, `npm test`) y declara requisitos previos. | Cumple | El arranque documentado es local; no incluye la URL desplegada. |
| Pipeline en cada push y análisis estático en SonarCloud con evidencia auditable | Consta `sonar-project.properties` y `.github/workflows/ci.yml` en d094a51, pero no se aportan runs ni la URL pública del análisis con su Quality Gate. | No verificado | Faltan dos de las tres evidencias exigidas; comando anotado: `curl -s "https://api.github.com/repos/ISCOUTB/AS_202620_AudioShare/actions/runs?per_page=5"`. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `d094a5166d0af4067bfc717e4170e660aacacab1 2026-09-21T00:21:38-05:00 Update architectural decision references in documentation`
- **Veredicto**: con pendientes
- Resumen: En la punta de origin/master (d094a51, 2026-09-21) el proyecto mantiene código, documentación y secretos bajo control, pero la entrega de despliegue está prácticamente ausente: sin URL ni health check comprobables, sin IaC del entorno desplegado, sin logs estructurados, sin métrica con escenario, sin estimación de costo, sin sección 7 de arc42 y sin ADR de plataforma.

Pendientes que siguen abiertos:
- URL pública con hora y código de respuesta, y ruta de health check consultable.
- Infraestructura como código del entorno desplegado, versionada y reproducible desde el README.
- Run de CI sobre la rama principal y evidencia pública de SonarCloud con Quality Gate.
- Configuración de logs estructurados con línea de ejemplo.
- Métrica consultable asociada a un escenario de calidad.
- Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita.
- arc42 sección 7 con una caja por pieza y sección 2 con el límite de costo.
- Un ADR por decisión de plataforma, con alternativa descartada.
- Corrección del enlace a un ADR inexistente en `docs/aspectos.md` y de las columnas de la tabla de aspectos.

## Recuento y nota sugerida

2 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.7 = 1 + 4 × (2/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema desde fuera de la red: sin URL ni hora; comando `curl -sS -o /dev/null -w 'http=%{http_code} tiempo=%{time_total}s\n' "$URL"`.
- Health check: el equipo no declara ruta; falta `curl -sS -o /dev/null -w 'health=%{http_code}\n' "$URL/health"` sobre un despliegue accesible.
- Pipeline en verde: sin runs aportados; comando de la API de acciones de GitHub anotado sobre AS_202620_AudioShare.
- Análisis estático en SonarCloud: falta la URL pública del análisis y el estado del Quality Gate para el hash revisado.
- Contenido de `docs/ia.md`: solo consta su historial de commits, no lo aceptado ni lo rechazado con motivo.

## Hallazgos para la planilla

- No se aporta URL del sistema desplegado ni hora de comprobación, por lo que la fila principal de la ficha queda sin verificar.
- No existe `docs/arc42/src/07_deployment_view.adoc`, aunque la plantilla incluye su `include`.
- Ninguno de los tres ADR del repositorio decide plataforma de despliegue ni verifica capa gratuita.
- No hay documento de estimación de costo mensual con volumen supuesto y punto de ruptura.
- `docs/aspectos.md` enlaza a un ADR de cliente Flutter que no existe en `docs/adr/`.
- La sección 2 de arc42 no recoge límite de costo ni restricción de tarjeta.
- La única pieza de infraestructura versionada es el devcontainer de Codespaces, no el entorno desplegado.
- No hay configuración de logs estructurados ni métrica consultable con escenario asociado.
- El barrido de secretos no encontró coincidencias, hay `.env.example` y ningún `.env` versionado.
- ADR-0003 carece de alternativas evaluadas y de trazabilidad.
