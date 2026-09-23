# semana-08-evidencia-s8 · ElMapita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `afae3be` en `origin/main` (2026-09-20T19:09:25-06:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | No hay URL ni salida de curl en la evidencia del commit afae3be. | No verificado | Falta la URL y la hora de comprobación; es el criterio central de S8 y no se puede cerrar. |
| Health check consultable | Existe backend/src/health.controller.ts (afae3be), pero no hay URL ni código de respuesta. | No verificado | ADR-0003 documenta la deriva /health vs /api/health; faltan rutas declaradas y respuesta. |
| Infraestructura como código versionada en el repositorio | El árbol de afae3be no contiene Dockerfile, docker-compose, .tf, k8s/, helm/, fly.toml ni Procfile. | No cumple | Solo hay .github/workflows/ci.yml; no existe IaC que describa el entorno. |
| El entorno se puede recrear siguiendo el README | README.md sección 'Inicio Rápido' con prerequisitos y scripts/dev.sh y scripts/dev.ps1 (afae3be). | Cumple | Documenta arranque local; sin despliegue no cubre el entorno de S8. |
| Pipeline en verde sobre la rama principal | Existe .github/workflows/ci.yml (afae3be) pero no se aporta ningún run. | No verificado | Falta nombre, conclusión y URL del último run (curl a actions/runs). |
| Logs estructurados | No hay archivo de configuración de logging en el árbol de afae3be. | No verificado | Falta el grep de structlog/winston/pino/logback y una línea de ejemplo. |
| Métrica consultable asociada a un escenario de calidad | No hay archivo de métricas en el árbol de afae3be. | No verificado | Falta el nombre de la métrica y el escenario (EC-01 a EC-04) al que se liga. |
| Secretos fuera del código y tomados del entorno o del almacén | backend/.env.example versionado, envs_versionados vacío y barrido con solo falsos positivos (afae3be). | Cumple | Sin credenciales reales; no se aporta grep de secrets.* en los workflows. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | El árbol de afae3be no incluye ningún documento de costos. | No cumple | Falta volumen supuesto, costo por pieza y punto de ruptura. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | Solo consta docs/arc42/arc42-template-EN.md (afae3be); no se aporta su contenido. | No verificado | Falta revisar la sección 7 (vista de despliegue). |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | ADR-0002 cita la sección 2 solo para RES-04 (rendimiento), sin costo ni tarjeta. | No verificado | Falta el contenido de la sección 2 y la restricción 'sin tarjeta'. |
| Un ADR por decisión de plataforma, con alternativa descartada | docs/adr/ solo tiene 0001 (estilo), 0002 (rendimiento) y 0003 (contrato OpenAPI) en afae3be. | No cumple | Ninguno decide plataforma de despliegue. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_ElMapita, visible público (afae3be). | Cumple | Solo una cuenta coincide por nombre visible; no se atribuyen las otras por parecido. |
| Estructura mínima | docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md y README.md presentes (afae3be). | Cumple | Documentación en Markdown dentro de las rutas mínimas. |
| Convenciones de ADR | docs/adr/0001-0003 con nombres NNNN-kebab-case (afae3be). | Cumple | No se aporta log de ediciones posteriores a su aceptación. |
| Tabla de aspectos | docs/aspectos.md existe (afae3be) pero no se aporta su contenido. | No verificado | Falta verificar las 8 columnas y que la cadena sea navegable. |
| Registro de uso de IA | docs/ia.md con 7 commits entre 2026-08-07 y 2026-09-20 (ia_log). | Cumple | Solo se ve la traza de commits; no se aporta la columna de lo rechazado. |
| README | README.md con qué es, prerequisitos, scripts/dev.sh y comandos de prueba (afae3be). | Cumple | El arranque en un comando exige Node/Flutter y credenciales Supabase. |
| Pipeline y análisis estático | Solo .github/workflows/ci.yml (afae3be); sin sonar-project.properties, sin URL de run ni de SonarCloud. | No cumple | Faltan las tres evidencias exigidas en el contrato. |
| Secretos | Sin .env versionado y barrido con solo falsos positivos (password/token de tipos) en afae3be. | Cumple | Sin credenciales reales; no se evaluó el historial previo. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `afae3be7c7fa2e00e311d899425149e3b954ae4f 2026-09-20T19:09:25-06:00 Contrato de API y prueba de contrato`
- **Veredicto**: con pendientes
- Resumen: Proyecto con buen código y documentación base en afae3be, pero la entrega S8 (despliegue accesible, IaC, CI verificable y observabilidad) no está cubierta a HEAD.

Pendientes que siguen abiertos:
- URL desplegada con hora de comprobación
- Health check con código de respuesta
- Infraestructura como código versionada
- Run de CI en verde con URL
- Logs estructurados
- Métrica ligada a escenario
- Estimación de costo mensual y punto de ruptura
- arc42 secciones 7 y 2
- ADR por decisión de plataforma

## Recuento y nota sugerida

2 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.7 = 1 + 4 × (2/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL desplegada: falta URL y hora; haría falta curl -w 'http=%{http_code} tiempo=%{time_total}s'.
- Health check: falta ruta y código; haría falta curl a la ruta declarada por el equipo.
- Pipeline en verde: falta runs_ci (nombre, conclusión y URL del último run).
- Logs estructurados: falta archivo de configuración y línea de ejemplo.
- Métrica consultable: falta nombre y escenario de calidad asociado.
- arc42 secciones 7 y 2: falta contenido; solo consta el archivo de plantilla.
- Tabla de aspectos: falta contenido y verificación de columnas.

## Hallazgos para la planilla

- Sin URL del sistema desplegado ni resultado de curl: el criterio central de S8 no es verificable.
- No hay infraestructura como código en HEAD, solo .github/workflows/ci.yml.
- Sin runs de CI aportados ni configuración de SonarCloud.
- Sin logs estructurados ni métrica asociada a un escenario de calidad.
- Sin estimación de costo mensual ni documento de costos.
- Los ADR 0001-0003 cubren estilo, rendimiento y contrato OpenAPI; ninguno decide plataforma de despliegue.
- El README describe /health mientras ADR-0003 documenta el prefijo duplicado /api/api/v1.
- Entrega en modo early: sin commits posteriores al cierre.
