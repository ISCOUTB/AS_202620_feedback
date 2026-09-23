# semana-08-evidencia-s8 · TRACTAR

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `9cf1ac9` en `origin/main` (2026-09-21T00:14:08-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | README.md en 9cf1ac9 solo documenta http://127.0.0.1:8000; ni el árbol ni la entrega incluyen URL pública. | No cumple | Sin URL no hay hora de comprobación posible ni curl ejecutable. |
| Health check consultable | Ruta /salud declarada en docs/contracts/openapi.json y app/routers/health.py (árbol a HEAD). | No verificado | Sin despliegue no se obtuvo código de respuesta; falta curl -sS -o /dev/null -w 'health=%{http_code}' $URL/salud. |
| Infraestructura como código versionada en el repositorio | ls-tree a HEAD sin Dockerfile, docker-compose, *.tf, *.tfvars, k8s/, helm/, fly.toml, render.yaml ni Procfile. | No cumple | Lo único de infraestructura es .github/workflows/ci.yml. |
| El entorno se puede recrear siguiendo el README | README.md sección 'Cómo arrancar (un solo comando)' describe ./run.sh y el servidor local en 127.0.0.1:8000. | No cumple | Documenta el entorno local de desarrollo, no el entorno desplegado de S8. |
| Pipeline en verde sobre la rama principal | Run UTB Tracker CI, 2026-09-21T05:14:21Z, conclusion success: https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/35563858214 | Cumple | Coincide en el tiempo con el HEAD 9cf1ac9 (2026-09-21T05:14:08Z); la evidencia no expone head_branch. |
| Logs estructurados | Sin coincidencias de structlog/winston/pino/logging.config en HEAD y requirements.txt sin librería de logging. | No cumple | No hay archivo de configuración ni línea de ejemplo que citar. |
| Métrica consultable asociada a un escenario de calidad | El árbol no contiene configuración de métricas, endpoint /metrics ni documento que asocie métrica a QS-01..QS-06. | No cumple | No existe ni la métrica ni el escenario asociado. |
| Secretos fuera del código y tomados del entorno o del almacén | Barrido a HEAD sin coincidencias y envs_versionados vacío, pero no hay .env.example ni referencias 'secrets.' en ci.yml. | No cumple | La higiene se cumple, pero no hay despliegue del que tomar variables de un almacén; DATABASE_URL solo se menciona en el README. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No hay documento de costos en el árbol ni mención de costo mensual en README.md. | No cumple | Falta volumen supuesto, cálculo por pieza y punto de ruptura. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | El árbol a HEAD solo tiene docs/arc42/arc42.md y la parte visible llega hasta 'Estrategia de solución', sin cajas de piezas desplegadas. | No cumple | La evidencia del archivo llega truncada; no hay vista de despliegue que diga dónde se ejecuta cada pieza. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | En docs/arc42/arc42.md la sección 'Restricciones arquitectónicas' lista restricciones técnicas, organizacionales y legales, sin límite de costo ni 'sin tarjeta'. | No cumple | La sección 2 existe y es legible, pero no recoge estas restricciones. |
| Un ADR por decisión de plataforma, con alternativa descartada | docs/adr/ solo tiene 0001-estilo-arquitectonico, 0002-cambio-stack-fastapi-flutter y 0003-integracion-sincrona; ninguno decide plataforma de despliegue. | No cumple | Los ADR existentes sí traen alternativas descartadas, pero son de semanas anteriores, no de plataforma ni de capa gratuita. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio público ('visible': true) y bajo ISCOUTB según los runs de CI; el historial registra una sola identidad de autor (Sebastian Garcia Devoz, 22 commits) frente a 4 integrantes declarados. | No cumple | El nombre reportado (AS_202620_TRACTAR) difiere del de los runs (ISCOUTB/AS_202620_UTB_TRACKER). |
| Estructura mínima | Árbol a HEAD con README.md, docs/arc42/, docs/adr/ (3), docs/c4/ (2), docs/aspectos.md y docs/ia.md. | Cumple | Estructura completa; arc42 en un solo archivo en lugar de secciones numeradas. |
| Convenciones de ADR | 0001-estilo-arquitectonico.md, 0002-cambio-stack-fastapi-flutter.md y 0003-integracion-sincrona.md cumplen el patrón NNNN-kebab-case y traen contexto, alternativas, decisión y consecuencias. | Cumple | La trazabilidad a C4/commit/pruebas es explícita solo en el 0001; en los otros queda como referencia a QS. |
| La tabla de aspectos | docs/aspectos.md con las ocho columnas y 6 filas (A-01 a A-06). | Cumple | Solo A-06 recorre la cadena completa; A-01 a A-05 tienen '—' en ADR/Código/Pruebas/Evidencia. |
| Registro de uso de IA | docs/ia.md con 2 registros, ambos del 2026-08-16 (últimos commits a ese archivo), y la columna 'Qué se usó/descartó' sin ningún rechazo. | No cumple | El registro no crece desde agosto y no documenta nada descartado con motivo. |
| README | README.md declara qué es el sistema, 'Cómo arrancar (un solo comando)' con ./run.sh y la sección 'Pruebas' con pytest. | Cumple | No enumera requisitos previos ni cubre el despliegue. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo instala dependencias y corre pytest; no hay sonar-project.properties ni paso del scanner; último run success (runs/35563858214). | No cumple | Falta la URL pública del análisis en SonarCloud con el estado del Quality Gate. |
| Secretos | Barrido a HEAD sin coincidencias y sin .env versionado ('envs_versionados': []). | Cumple | Sin despliegue no hay almacén de secretos del que tomar variables. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `9cf1ac95f4f75ae9af515dbf68ead79768d7f2ac 2026-09-21T00:14:08-05:00 S7`
- **Veredicto**: con pendientes
- Resumen: A HEAD (9cf1ac9, 2026-09-21, origin/main) el CI está en verde y la estructura documental se mantiene, pero la entrega S8 no existe: sin sistema desplegado, sin IaC, sin logs, métricas, costos, secciones 7/2 de arc42 ni ADR de plataforma; el commit es el mismo de la semana anterior.

Pendientes que siguen abiertos:
- URL pública del sistema accesible desde fuera de la red de la universidad
- Infraestructura como código versionada y recreación del entorno
- Health check verificable en el entorno desplegado
- Logs estructurados y métrica consultable asociada a un escenario de calidad
- Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita
- arc42 sección 7 con una caja por pieza y sección 2 con límite de costo
- Un ADR por decisión de plataforma con alternativa descartada
- Análisis estático en SonarCloud con URL pública y Quality Gate
- Registro de uso de IA actualizado con rechazos justificados
- Evidencia de commits de los cuatro integrantes declarados

## Recuento y nota sugerida

1 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.3 = 1 + 4 × (1/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Health check: la ruta /salud está declarada en docs/contracts/openapi.json y app/routers/health.py, pero sin URL desplegada no se pudo obtener código de respuesta; hace falta curl -sS -o /dev/null -w 'health=%{http_code}' $URL/salud.
- Rama del run de CI: la evidencia no expone head_branch; se infiere main por el trigger del workflow y por la coincidencia temporal con el HEAD.
- Contenido completo de docs/arc42/arc42.md: la evidencia llega truncada y no se pudo revisar más allá de la estrategia de solución.

## Hallazgos para la planilla

- El HEAD calificado (9cf1ac9, 2026-09-21) es un commit rotulado S7, sin commits nuevos desde el cierre anterior.
- No existe URL de sistema desplegado: el README solo expone http://127.0.0.1:8000.
- No hay infraestructura como código: sin Dockerfile, compose, Terraform, manifiestos ni Procfile.
- Sin logs estructurados, sin métricas y sin endpoint de métricas en el árbol.
- Sin estimación de costo mensual ni límite de costo en la sección 2 de arc42.
- Ningún ADR trata la plataforma de despliegue ni verifica la capa gratuita.
- El workflow de CI no invoca el scanner de SonarCloud ni existe archivo de configuración del análisis.
- Solo una identidad de autor aparece en el historial frente a cuatro integrantes declarados.
- El nombre del repositorio difiere entre la evidencia (TRACTAR) y las URL de los runs (UTB_TRACKER).
- docs/ia.md no crece desde el 2026-08-16 y no registra rechazos con motivo.
