# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo EnAgenda. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | EnAgenda |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Eliab Josue Arnedo Conde · Jeimy Yulieth Mendez Altamiranda · Gabriela Morales Cancino — cuentas abajo; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | URL pública vigente no localizada; despliegue No verificado. Ver [S10](semana-10-corte2.md). |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar; corrección documental de S10: 2026-10-07 |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `5aa889370dcf342ba06666893b97f8065b513de9` · 2026-10-04T23:46:49-05:00 | 3/10 | 2.2 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `c2077ac55a29562adc728734ca4c283ccb40f310` · 2026-10-05T10:40:19-05:00 | 1/12 de comprobación (sin PDF): 1 Cumple, 6 No cumple y 5 No verificado | C3: Insuficiente (0,00); total pendiente, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06; corrección documental 2026-10-07 |
| 8 | S8 | `2c7d77a` (2026-09-27T23:42:39-05:00) | 5/10 (2 filas de despliegue diferidas) | 3.0 (provisional) | sí |
| 7 | S7 | `849ee8c` (2026-09-20T23:59:07-05:00) | 4/10 | 2.6 | sí, auditada |
| 6 | S6 | `0a58de8` (2026-09-13T23:38:41-05:00) | 7/8 | 4.5 | si |
| 5 | CORTE1 | `696882e` (2026-09-07T16:21:16-05:00) | 10/12 | 4.3 | si |
| 4 | S4 | `df724b8` (2026-08-30T23:57:42-05:00) | 8/10 | 4.2 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `13f61b10` · 2026-08-09T05:34:14-05:00 | 8/9 | 4,6 * | sí |
| 2 | S2 | `5b6f7a8` (2026-08-16T23:33:20-05:00) | 5/9 | no aplica | si |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `c38adfb94` · 2026-08-23T23:49:01-05:00 | 3/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Normalizar/redactar tokens en métricas y restringir /metrics: no publicar rutas crudas de invitaciones. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Crear prueba del flujo completo POST / → plantilla de invitados → creación → respuesta; un test directo a /crear-invitaciones omite la pantalla intermedia. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Configurar host/HTTPS, medir salud y flujo principal con umbral y línea base identificables. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Aportar ADR coherente de evolución del flujo y preservar decisiones aceptadas con un ADR sustituto para Dokploy. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Añadir auditoría de erosión del cambio, inventario verificado de propuestas/dependencias y decisión sobre componente generativo. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Integrar SonarCloud y publicar scanner, run y Quality Gate; aclarar asignación operativa S10. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Conflictos de merge de Docker/Compose/ejemplos/evidencia ya no están presentes en snapshot S9; [Dockerfile:1–15](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/Dockerfile#L1-L15), [docs/evidencia.md:58–125](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/evidencia.md#L58-L125). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Se restauró encabezado de aspectos en S9 y se amplió tabla después del cierre; [docs/aspectos.md:1–5](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/aspectos.md#L1-L5), [docs/aspectos.md:5–12](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/aspectos.md#L5-L12). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Plantilla invitados.html agregada después del cierre; fallo identificado y corregido según registro de IA actual, [docs/ia.md:47–47](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/ia.md#L47-L47). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| CI pasa para hash S9 y HEAD; ello no cierra SonarCloud ni garantiza el flujo UI completo. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Nombres de archivo con espacio antes de la extensión (`docs/aspectos .md`, `docs/ia .md`, `docs/ficha-problema .md`, ADR, arc42, matriz) | S1 | Sí (el ADR además ya no corresponde a su nombre: el archivo dice «monolito modular» y se llama «app-movil-y-web…») | Renombrar a la convención; el ADR no pasa el filtro de nombres |
| Integrante Eliab Josue Arnedo Conde sin commits en S1 (primer commit 2026-08-16) | S1 | Cerrado en S2 (2 commits); reabierto en S3 (0 commits en el periodo) | Se resolvió solo; vigilar que la contribución siga repartida |
| `aspectos.md` sin enlaces a escenarios (C4/ADR/Código/Pruebas/Evidencia en «Pendiente») | S2 | Parcialmente cerrado: ya tiene la tabla de 8 columnas y enlaza escenarios; sigue «Pendiente» la columna ADR | Enlazar el ADR 0001 desde su fila y desde los escenarios EC que lo motivan |
| C4 de contexto sin leyenda | S2 | Sí | Añadir leyenda al mermaid |
| Evidencia S3 sin estrategia ni esqueleto: §4 en placeholder, sin matriz de estilos, sin código, pruebas ni workflow; ADR 0001 es de producto, no la decisión de estilo | S3 | Cerrado en documentación (§4 completa, ADR de estilo aceptado, matriz propia); sigue abierto el esqueleto | El esqueleto prometido (`src/` con 6 módulos + pruebas) no existe: solo `docs/Esqueleto.py` demo y `docs/main.py` con import roto; README sin comando de arranque |
| Esqueleto ejecutable inexistente: sin comando de arranque en README, sin prueba, paquetes del monolito modular ausentes | S3 | Sí | Crear `src/` con los módulos del ADR, prueba en verde y comando único en README |
| Matriz comparativa sin filas de los escenarios EC-01…EC-05 | S3 | Sí | Fila por escenario contra el árbol de utilidad |
| Commit 1d01401 (2026-08-31T00:28:12-05:00) actualiza docs/ia.md después del cierre. | S4 | no (resuelto tarde) | — |
| Ajustar C4 nivel 2 para reflejar el monolito Flask y el repositorio en memoria. | S4 | si | |
| Agregar SonarCloud al pipeline. | S4 | si | |
| Hacer navegable la celda C4 de docs/aspectos.md. | S4 | si | |
| Verificar redacción de arc42 01, 04, 05 y 06. | S4 | si | |
| Etiqueta `corte-1` ausente | S5 | No (creada 2026-09-06, `31773ad`) | Se resolvió; vigilar que en cortes futuros se etiquete con más antelación al cierre. |
| Respuesta al reto sin diagnóstico, ADR, cambio ni medición reproducible | S5 | Sí | El equipo dedicó el cierre a corregir feedback de S4 (C4, aspectos) y así lo documenta en `docs/correcciones.md`; sigue faltando diagnóstico, ADR, cambio y medición del reto de Corte 1. |
| Cadena de `docs/aspectos.md` no navegable y evidencia pendiente | S5 | Parcial (mejoró, celda Evidencia rota) | La fila A-01 ya enlaza C4/ADR/código/pruebas, pero "Evidencia" apunta a `correcciones-feedback.md`, archivo inexistente (el real es `docs/correcciones.md`); corregir el enlace y crear la fila del reto de Corte 1. |
| C4 de contenedores desactualizado frente al monolito Flask y el repositorio en memoria | S4 | Sí | Alinear el diagrama con el estado ejecutable. |
| Registro de IA sin entrada del Corte 1 | S5 | Sí | `docs/ia.md` sigue sin entradas posteriores al 30/08/2026; registrar el uso de IA (si lo hubo) en las correcciones del cierre y en el reto de Corte 1. |
| 13fdc8e Cambios C4 | S2 | no (resuelto tarde) | — |
| 66fb6e4 Cambios C4 | S2 | no (resuelto tarde) | — |
| 1d01401 Update documentation with recent project changes | S2 | no (resuelto tarde) | — |
| 696882e Update aspectos.md | S2 | no (resuelto tarde) | — |
| Falta docs/arc42/01* | S2 | si | |
| Trazabilidad de aspectos pendiente | S2 | si | |
| Sin integración continua | S2 | si | |
| docs/aspectos.md actualizado en commits 03c855c y 696882e (post-cierre) para corregir trazabilidad | S5 | no (resuelto tarde) | — |
| docs/evidencia.md agregado en commit 5a8a5c5 (post-cierre) como evidencia de corte vertical | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz | S5 | si | |
| Completar arc42 secciones 07, 08 y 11 | S5 | si | |
| Completar C4 nivel 3 | S5 | si | |
| Corregir enlace roto en aspectos.md | S5 | si | |
| Configurar SonarCloud | S5 | si | |
| C4 nivel 3 sin contenido | S6 | si | |
| arc42 sección 8 vacía | S6 | si | |
| Mapa de contextos y tabla módulo-datos ausentes | S6 | si | |
| SonarCloud no configurado | S6 | si | |
| SonarCloud no configurado en el pipeline. | S6 | si | |
| Pendientes de la semana 5: reto nuevo, medición, incremento y umbral. | S6 | si | |
| Ampliar la tabla de aspectos a más contextos. | S6 | si | |
| Eliminar archivos __pycache__ del repositorio. | S6 | si | |
| Rutas web expuestas fuera del contrato OpenAPI | S7 | Sí | Declarar `/` y `/invitacion/<token>` o separar explícitamente la frontera contractual. |
| Prueba funcional que no valida el OpenAPI ni se ejecuta como prueba contractual explícita | S7 | Sí | Hacer que la prueba lea la especificación y que el workflow invoque el paso contractual. |
| Evidencia de fallo ante un cambio incompatible | S7 | Sí | Aportar un run o reproducción verificable de la rotura. |
| ADR de integración incorporado después del cierre | S7 | No (resuelto tarde) | Existe en la punta actual, pero no modifica la calificación definitiva. |
| C4 nivel 2 sin formato de datos en cada flecha | S7 | Sí | Etiquetar canal y formato en todas las relaciones. |
| SonarCloud sin scanner, análisis público ni Quality Gate | S7 | Sí | Integrar el análisis y publicar la evidencia del hash. |
| Despliegue público, health check e infraestructura como código ausentes | S8 | Sí (IaC inválida) | Publicar una URL verificable y limpiar los conflictos de merge del entorno. |
| Sin logs estructurados, métrica consultable ni estimación de costo | S8 | Sí | No hay configuración de logging; la métrica no se ata a un EC real; los volúmenes de costo están sin completar. |
| arc42 §7 y ADR de plataforma ausentes | S8 | No (resuelto en S8) | `docs/arc42/07-vista-de-despliegue.md` y ADR-0003 escritos. |
| Conflictos de merge sin resolver en `Dockerfile`, `docker-compose.yml`, `render.yaml`, `.dockerignore`, `.env.example` y `docs/evidencia.md` | S8 | Sí | Limpiar los marcadores; la infraestructura no compila y el CI del hash revisado queda en rojo. |
| ADR-0003 cita un escenario inexistente («EC-03 — Observabilidad de solicitudes») | S8 | Sí | Alinear la métrica con un EC real de arc42 §10. |
| SonarCloud sin configuración, run ni Quality Gate públicos | S5 | Sí | Integrar el análisis y publicar la evidencia del hash. |
| Sin commits de S9: la punta es la de S8 (`2c7d77a`, 2026-09-27). | S9 | sí | La pasada S9 no tiene cierre y califica la punta actual; el equipo no ha empujado trabajo nuevo. |
| Recalce S9 por CONTRATO §12: sin artefacto del periodo, las filas de porción con IA, cadena, ADR, extracto de `docs/ia.md` y auditoría de erosión pasan a No cumple; la de prueba que falla ante el defecto ya estaba en No verificado. | S9 | sí | Solo el barrido de credenciales queda en Cumple; la evidencia de S6/S8 se cita como contexto pero no se recalifica. |
| Sin prueba que falle ante el defecto que cubre (run en rojo, mutación o procedimiento documentado). | S9 | sí | No verificado en la matriz de la ficha; queda como pregunta de sustentación. |
| Sin medición de escenario contra umbral. | S5/S9 | sí | — |
| Sin verificación de dependencias del periodo (diff vacío contra S8). | S9 | sí | — |
| Sin ADR sobre el componente generativo (ni componente, ni decisión de no incorporarlo). | S9 | sí | La ausencia de decisión no es la decisión de no hacerlo. |
| `docs/aspectos.md` sin fila de encabezado; `docs/evidencia.md` corrupto por conflictos de merge. | S9 | sí | La cadena A-01 navega, pero la evidencia no es un artefacto coherente. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público en organización ISCOUTB y nombre conforme; master declarado remoto, [README.md:1–8](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/README.md#L1-L8). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes y tablas ampliadas; [docs/aspectos.md:1–12](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/aspectos.md#L1-L12). |
| Estado calificado identificable | Cumple | Punta master c2077ac55a29562adc728734ca4c283ccb40f310 de 2026-10-05T10:40:19-05:00, preliminar anterior a cierre S10. |
| Nombres de ADR según la convención | Cumple | ADR 0001–0003 usan convención de nombres; [docs/adr/0003-desplegar-api-flask-en-dokploy.md:1–4](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L1-L4). |
| ADR aceptados no reescritos | No cumple | El ADR-0003 aceptado de Render en S8 fue eliminado y sustituido por otro 0003 de Dokploy sin preservar la decisión ni declarar nuevo ADR supersedes. [docs/adr/0003-desplegar-api-flask-en-dokploy.md:1–18](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L1-L18). Se verificó el original aceptado en el hash S8. |
| docs/ia.md al día para la semana | Cumple | Registro condensado en tabla y nueva entrada de diagnóstico de plantilla faltante; [docs/ia.md:43–47](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/ia.md#L43-L47). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI exacto success, pero no hay scanner/configuración/Quality Gate SonarCloud en el árbol; [.github/workflows/ci.yml:13–45](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/.github/workflows/ci.yml#L13-L45) solo prueba y build. |
| Sin credenciales en el repositorio ni en el historial | No verificado | No hay credenciales reales hardcodeadas ni .env versionado en el snapshot; no se certifica todo el historial. Existe riesgo operativo distinto: métricas exponen request.path, que puede contener tokens de invitación. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas, 173 commits agregados en S9, para tres integrantes. Variantes deben consolidarse por evidencia de identidad; no se adivina la equivalencia. Punta actual: 4 firmas y 177 commits agregados; no equivalen automáticamente a personas. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Cuatro firmas y 173 commits agregados en S9; consolidación de variantes no acreditada de forma independiente para todas las personas. En HEAD: 4 firmas y 177 commits agregados.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Eliab Josue Arnedo Conde | eliabarnedocondef10-gif (correo omitido) | 0 (S3) | 0 | — | Último commit `45ab58e` (2026-08-16, S2); sin commits en S3 |
| Jeimy Yulieth Mendez Altamiranda | Jein-12 (correo omitido) | 5 (S3) | 0 | — | C4 nivel 2, ia.md y archivos por upload |
| Gabriela Morales Cancino | Daoisttl0FB3 (correo omitido) | 4 (S3) | 0 | — | §4, matriz comparativa y ADR de estilo |

Correspondencia cuenta↔persona inferida del correo de los commits, no de parecidos de nombre; la confirma el docente.

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Qué pasa con invitaciones, tokens y contadores si el contenedor reinicia, y cómo evitarían exponer tokens mediante /metrics?
- ¿Qué cuotas de CPU/RAM/tráfico ofrece Dokploy y cuándo deja de ser válida la estimación de costo cero?
- El test directo no detectó TemplateNotFound: ¿qué cambiarían en la prueba para cubrir el recorrido real del organizador?
