# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ElMapita |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Integrantes y su usuario de GitHub | Angel Fabian Gutierrez Gomez (sin cuenta identificada en el historial) · Diego Rosales Garza (sin cuenta identificada) · Rodrigo Vazquez Rico (firma con su nombre). Historial: `RobotDRMX` (sin atribuir) y, en EQUIPOS.md, `YOOUYII` (nunca vista). |
| URL del sistema desplegado | sin desplegar todavía |
| Ultima revision | 2026-09-23 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 8 | S8 | `afae3be` (2026-09-20T19:09:25-06:00) | 2/12 | 1.7 (prelim.) | si |
| 6 | S6 | `a22f0a4` (2026-09-13T22:21:07-05:00) | 0/8 | 1.0 (prelim.) | si |
| 7 | S7 | `afae3be` (2026-09-20T19:09:25-06:00) | 4/10 | 2.6 | si |
| 5 | CORTE1 | `b28e068` (2026-09-07T14:57:28-06:00) | 7/12 | 3.3 | si |
| 4 | S4 | `07b36f4` (2026-08-30T23:31:03-05:00) | 4/10 | 2.6 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `938d0206` · 2026-08-07T21:36:01-06:00 | 5/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `c5d9964c` · 2026-08-16T14:21:20-05:00 | 8/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `8e30f616` · 2026-08-22T16:12:55-06:00 | 4/9 | no se publica | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/ia.md` vacío (0 bytes) | S1 | sí | Ver feedback S1/S2 y S3 |
| Sin ficha del problema | S1 | sí | Ver feedback S1/S2 |
| Sin tensiones de calidad | S1 | sí | Ver feedback S1/S2 |
| Historial con cuentas sin atribuir (2 identidades para 3 integrantes; en S3 solo una cuenta firma) | S1 | sí | Ver feedback S1/S2 y S3 |
| Sección 4 de arc42 vacía (la estrategia está en ADR y matriz, no en arc42) | S3 | sí | Ver feedback S3 |
| ADR no enlazado desde `aspectos.md` ni desde los escenarios | S3 | sí | Ver feedback S3 |
| Sin pipeline (pruebas sin evidencia de verde) | S3 | sí | Ver feedback S3 |
| Run de CI en failure (33357590091) | S4 | si | |
| Pruebas del recorrido completo pendientes y rutas inexistentes en aspectos.md | S4 | si | |
| Sin SonarCloud configurado | S4 | si | |
| Autoría concentrada en una cuenta (9/11 commits) | S4 | si | |
| ADR del reto | S5 | sí | Único ADR sigue siendo el de estilo arquitectónico de la línea base; sin actividad en el repositorio desde el 2026-09-01. |
| Línea base medida y verificable | S5 | sí | Las 4 filas de `docs/aspectos.md` siguen con Evidencia = "Pendiente". |
| Cadena de trazabilidad completa en docs/aspectos.md | S5 | sí | Se rompe sistemáticamente en Pruebas y Evidencia. |
| Prueba en verde en pipeline | S5 | sí (empeoró: confirmado en rojo) | Los 3 runs de CI disponibles, incluido el del commit calificado, están en `failure`. |
| Medición reproducible contra umbral | S5 | sí | Sin ejecutar. |
| Registro de IA con motivo técnico verificable | S5 | sí | `docs/ia.md` no tiene entradas posteriores al 2026-08-30. |
| Confirmar etiqueta corte-1 | S5 | sí (se usó un commit con ese mensaje, no una etiqueta) | Se les explicó la diferencia entre `git commit -m "corte-1"` y `git tag corte-1`; deben crear la etiqueta real. |
| Angel Fabian Gutierrez Gomez sin commits identificables | S5 | sí | Confirmado en el commit calificado: `git shortlog` solo muestra RobotDRMX, Rodrigo Vazquez Rico y dgarza2705 (Diego Rosales Garza, ahora identificado por su correo institucional). |
| correcciones.md se añadió en el commit b28e068 (2026-09-07T14:57:28-06:00), posterior al cierre; no se considera en la matriz S5. | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz del estado calificado. | S5 | si | |
| Evidencia de ejecución del pipeline CI para el hash calificado. | S5 | si | |
| Verificación de reproducibilidad del corte vertical. | S5 | si | |
| Pruebas de EC-01 a EC-04 pendientes | S5 | si | |
| Implementación de LOD y degradación progresiva (ADR-0002) | S5 | si | |
| Verificación de pipeline y CI | S5 | si | |
| Correcciones.md sin contrastar | S5 | si | |
| Contrato OpenAPI/AsyncAPI/proto versionado, con rutas, esquemas y versión | S7 | si | |
| Prueba de contrato presente y ejecutada desde el workflow | S7 | si | |
| Evidencia de que la prueba falla ante un cambio incompatible | S7 | si | |
| ADR de estrategia de integración síncrona o asíncrona con alternativa descartada | S7 | si | |
| arc42 sección 6 con los flujos de interacción | S7 | si | |
| C4 nivel 2 con protocolo y formato en cada flecha | S7 | si | |
| Contenido defendible de docs/aspectos.md y docs/ia.md | S7 | si | |
| Runs de CI y análisis público de SonarCloud con estado del Quality Gate | S7 | si | |
| Mapa de contextos con relaciones tipificadas en formato revisable. | S6 | si | |
| Tabla módulo a datos con dueño único y su contraste con las entidades del código. | S6 | si | |
| Lista de no conformidades de propiedad de datos con ubicación y plan de corrección. | S6 | si | |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos. | S6 | si | |
| ADR de reajuste y diff de C4 Nivel 3 si los límites cambiaron desde el primer corte. | S6 | si | |
| Evidencia de SonarCloud: configuración, run de CI y URL pública con Quality Gate. | S6 | si | |
| Sin envíos posteriores al cierre: commits_post_cierre vacío y el commit calificado afae3be es anterior al cierre. | S7 | no (resuelto tarde) | — |
| Brecha de `npm run test:contracts` prometida en ADR-0001 y nunca implementada: se cierra en afae3be con el ADR-0003, dentro del plazo de S7 pero aún sin evidencia de ejecución en CI. | S7 | no (resuelto tarde) | — |
| Deriva de rutas contrato-backend por prefijo duplicado (`/api/api/v1/...`), reconocida en ADR-0003 y no corregida. | S7 | si | |
| Evidencia de que la prueba de contrato se ejecuta en el pipeline y de que falla ante un cambio incompatible. | S7 | si | |
| Evidencia de SonarCloud (configuración del scanner, run exitoso y URL pública con Quality Gate), pendiente desde S6. | S7 | si | |
| Contenido verificable de la tabla de aspectos, de arc42 §6 y del C4 nivel 2 con protocolo y formato. | S7 | si | |
| Implementación pendiente declarada en ADR-0002 (LOD y degradación progresiva). | S7 | si | |
| URL desplegada con hora de comprobación | S8 | si | |
| Health check con código de respuesta | S8 | si | |
| Infraestructura como código versionada | S8 | si | |
| Run de CI en verde con URL | S8 | si | |
| Logs estructurados | S8 | si | |
| Métrica ligada a escenario | S8 | si | |
| Estimación de costo mensual y punto de ruptura | S8 | si | |
| arc42 secciones 7 y 2 | S8 | si | |
| ADR por decisión de plataforma | S8 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_ElMapita`, público. |
| Estructura mínima | Cumple | Las seis rutas; arc42 en plantilla única y C4 solo PNG (anotado desde S2). |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico-propuesto.md` conforme. |
| ADR aceptados sin reescribir | Cumple | Un solo commit de creación (`aa16382`). |
| `docs/ia.md` al día | No cumple | Vacío (0 bytes); último commit 2026-08-07. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Coincidencias solo en tipos (`password: string`) y badge placeholder del boilerplate. |
| Contribución de todos los integrantes | No cumple | Confirmado hasta el corte 1: `RobotDRMX` 12 commits (86%), `dgarza2705`/Diego Rosales Garza 1, Rodrigo Vazquez Rico 1; Angel Fabian Gutierrez Gomez sigue sin ningún commit identificable en todo el historial. |
| Pipeline en verde | No cumple | `.github/workflows/ci.yml` existe y corrió; los 3 runs disponibles vía API están en `failure`, incluido el commit calificado del corte 1. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Angel Fabian Gutierrez Gomez | sin cuenta identificada | 0 (S3) | — | — | `RobotDRMX` sin atribuir (¿es él o Diego Rosales Garza?) |
| Diego Rosales Garza | `dgarza2705` (correo institucional, confirmado en el corte 1) | 1 (corte 1) | — | — | Único commit del periodo: actualización de C4/arc42/pipeline. |
| Rodrigo Vazquez Rico | firma con su nombre | 0 (S3) | — | — | último commit en S2 |

## Preguntas abiertas para la sustentación

- ¿A quién pertenece `RobotDRMX` y por qué `YOOUYII` nunca aparece?
- ¿Quién escribió el ADR y el esqueleto si solo una cuenta firma en S3?
- ¿Cuándo se llenará `docs/ia.md` (usos reales y rechazos)?
- ¿Cuándo se escribirá la sección 4 de arc42 en su sitio (hoy está vacía y la estrategia vive en el ADR)?
- ¿Publicarán el C4 como código para reparar el enlace roto a `docs/c4/contexto.md`?
