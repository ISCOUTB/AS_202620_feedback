# Planilla de equipo · mapsutb

## Identificación

| | |
|---|---|
| Equipo | mapsutb |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Integrantes y su usuario de GitHub | Carlos Alberto Galvis Zuluaga · Carlos David Manrique Fals · Nerlis Nikol Otero Perez · Isabel Sofia Paez Matallana — cuentas observadas en el historial: `charlygz21`, `nerlis-otero`, `CarlosManrique-1397`, `i-matallana` (correspondencias por confirmar con el docente) |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-24 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `7e56ad3` · 2026-08-09T23:27:46-05:00 | 5/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `1cf1576` · 2026-08-16T21:26:05-05:00 | 4/9 | 2.8 | sí (revisión manual confirmatoria) |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `ed55eda` · 2026-08-23T21:44:05-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `f0d036a` (2026-08-30T22:53:06-05:00) | 5/10 | 3.0 | si |
| 5 | CORTE1 | `e8bad4c` histórico; excepción: `8aee879` (2026-09-13T18:14:14-05:00) | 8/12 | 3.7 | sí (actualizada con correcciones tardías aceptadas) |
| 6 | Evidencia S6 · Contextos delimitados y propiedad de datos | `8aee879` (2026-09-13T18:14:14-05:00) | 5/8 | 3.5 (prelim.) | sí |
| 7 | S7 | `5e2fdd5` (2026-09-20T21:15:28-05:00) | 10/10 | 5.0 | sí (auditoría definitiva corregida) |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `7048021` (2026-09-22T10:10:19-05:00) | 2/12 | 1.7 (propuesta preliminar) | sí (preliminar) |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 9 | Evidencia S9 · Generación verificada y trazable | | | no aplica | |
| 10 | Segundo corte · reto aplicado sobre el MVP | `corte-2` | | | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Estructura fuera de convención: `docs/arc42.md` único y `docs/c4_contexto.md` fuera de `docs/c4/` | S1 | sí | Mover a la estructura mínima del contrato |
| Sin tensiones de calidad en la ficha (S1) → árbol de utilidad sin impacto/riesgo (S2) | S1 | sí | Priorizar atributos por impacto y riesgo y vincularlos a los escenarios |
| Isabel Sofia Paez Matallana sin aparición en el historial | S1 | no (en HEAD aparece `i-matallana`, 39 commits en dos correos) | Confirmar acceso y contribución de la integrante |
| Etiqueta `corte-1` sobre el commit de S1 | S2 | sí (confirmado post-cierre: sigue sin moverse) | Moverla al commit real del corte 1 |
| `docs/aspectos.md` desactualizado («Sin ADR aún») y sin enlace al ADR 0001; `escenarios_calidad.md` con enlace roto al árbol | S3 | sí (confirmado también en HEAD `f40775d`, pese a que el ADR y el código ya existen) | Actualizar la tabla y enlazar el ADR desde el escenario que lo motiva |
| Sin matriz comparativa de los tres estilos contra el árbol de utilidad (el ADR la declina; el «corte anterior» no existe en el repo) | S3 | sí | escribir la matriz de estilos que pide la ficha |
| Estructura de paquetes del ADR no materializada (`lib/` solo tiene `main.dart`; faltan carpetas y `.gitkeep`) | S3 | no (resuelto en S4/S5: código de ubicación en `lib/services/`) | crear las carpetas del ADR antes de la S4 |
| `docs/ia.md` sin entradas del trabajo S3 | S3 | sí (última entrada 30/08, sin entrada de S5) | registrar el uso de IA de la semana con rechazados y motivo |
| Prueba de humo sin CI ni evidencia de verde | S3 | sí | pipeline o run aportado |
| Actualizar ficha-problema.md, escenarios_calidad.md y aspectos.md al alcance sin RA | S4 | sí | Alinear con el ADR 0002 que ya descarta RA |
| Limpiar plantilla arc42 en sección 5 | S4 | si | |
| Implementar o declarar contenedores C2 sin código (panorámicas, plano) | S4 | si | |
| Añadir CI con runs públicos que ejecuten las pruebas | S4 | sí (sigue sin `.github/workflows/` en HEAD) | Crear el workflow y publicar el run |
| Corregir mayúsculas en docs/Arc42 y docs/C4 | S4 | sí (persisten en HEAD) | Renombrar a minúsculas |
| Crear etiqueta corte-1 | S4 | sí (creada, pero sobre el commit equivocado) | Mover la etiqueta al commit real del corte |
| Registrar cambios de decisión en ADR nuevos, no editando aceptados | S4 | sí (ADR 0001 reescrito entre 23/08 y 31/08) | Crear ADR de reemplazo y conservar el aceptado |
| `correcciones.md` trazable en la raíz | S5 | cerrado | Se contrastó junto con las correcciones aplicadas hasta `8aee879`. |
| Ficha, escenarios, C4 y aspecto A-01 alineados al alcance sin RA | S5 | cerrado con revisión flexible | Se aceptan las correcciones de esta semana aunque sean posteriores al cierre original. |
| Comparación de estilos y ADR de monolito | S5 | cerrado con revisión flexible | ADR 0004 compara tres estilos y formaliza la elección; el historial de ADR 0001 sigue como observación. |
| Contenedores C2 sin activos | S5 | declarado pendiente | C2 reconoce explícitamente plano y panorámicas como diferidos. |
| CI de pruebas y evidencia de run | S5 | No verificado | `ci.yml` existe y ejecuta pruebas, pero falta un run público verificable. |
| PDF exigido por el aula y sustentación | S5 | No verificado | Se comprueban en Moodle y en la sesión docente. |
| Contrato de API en OpenAPI, AsyncAPI o proto, versionado y con esquemas de datos. | S7 | si | |
| Correspondencia entre contrato y API implementada. | S7 | si | |
| Prueba de contrato y su invocación en ci.yml, con run exitoso citado. | S7 | si | |
| Evidencia de que la prueba falla ante un cambio incompatible. | S7 | si | |
| ADR de estrategia de integración (síncrona o asíncrona) con alternativa descartada y consecuencias. | S7 | si | |
| C4 nivel 2 con protocolo y formato en cada flecha; revisar también docs/c4/C2.md. | S7 | si | |
| Evidencia auditable de SonarCloud: línea del scanner, run del hash revisado y URL pública con Quality Gate. | S7 | si | |
| Trasladar el mapa y lenguaje ubicuo a arc42 §8 y registrar el reajuste en un ADR. | S6 | sí | `dominio_y_modularidad.md` existe, pero §8 sigue siendo plantilla. |
| Mapear aspectos a contextos y aportar scanner/run/Quality Gate de SonarCloud. | S6 | sí | La fila A-01 no cubre los cuatro contextos. |
| Contenido verificable de docs/aspectos.md con las ocho columnas y celdas navegables. | S7 | si | |
| Evidencia de que la prueba de contrato falla ante un cambio incompatible (run en rojo o evidencia aportada). | S7 | no | Resuelto: el run fallido del cambio incompatible quedó citado en la auditoría definitiva. |
| Linea del workflow y URL del run que ejecuta la prueba de contrato sobre el hash revisado. | S7 | no | Resuelto: el workflow descubre la prueba y el run exitoso del estado calificado quedó citado. |
| Evidencia auditable de SonarCloud: invocacion del scanner, run exitoso y URL publica del analisis con Quality Gate (exigida desde S6). | S7 | si | |
| Publicar una URL real del sistema y un endpoint mínimo de salud verificable. | S8 | sí | No se encontró despliegue público ni endpoint de salud en el estado preliminar. |
| Versionar infraestructura como código y documentar un despliegue reproducible, no solo el arranque local. | S8 | sí | El README reproduce el entorno local, pero no existe infraestructura de despliegue. |
| Dejar el pipeline actual en verde y publicar la evidencia de análisis estático con Quality Gate. | S8 | sí | El run del estado revisado falla y no se encontró URL pública del análisis. |
| Añadir logs estructurados, una métrica operativa consultable y manejo seguro de secretos en la plataforma. | S8 | sí | No hay evidencia verificable de observabilidad ni de inyección segura de la clave de Google. |
| Completar costo mensual, arc42 §7 y ADR de plataforma de despliegue. | S8 | sí | Solo está documentada la restricción de costo cero; faltan cálculo y decisión de plataforma. |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `github.com/ISCOUTB/AS_202620_mapsutb`, público (clon sin auth el 2026-09-07) |
| Estructura mínima | Cumple | La punta aceptada usa `docs/arc42/`, `docs/c4/` y `docs/adr/`. |
| Convención de nombres de ADR | Cumple | Los ADR actuales están numerados y titulados en kebab-case. |
| ADR aceptados sin reescribir | No cumple | `0001-patrones-de-diseno.md` tiene múltiples reescrituras posteriores a su creación |
| `docs/ia.md` al día | No cumple | La última actualización verificable es del 2026-08-30, anterior a S8. |
| Sin credenciales en el repositorio ni en el historial | Cumple | greps limpios en HEAD `f40775d` |
| Contribución de todos los integrantes | Cumple | 4 personas consolidadas en HEAD: CarlosManrique-1397 (41), i-matallana (39, dos correos), charlygz21 (13), nerlis-otero (6) |
| Pipeline en verde | No cumple | El run del estado S8 revisado falla; además no se encontró análisis público de SonarCloud con Quality Gate. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Carlos Alberto Galvis Zuluaga | ¿`charlygz21`? (confirmar) | 13 | — | — | Autor de los commits `FeedbackS1..S4` (06/09, archivos vacíos) |
| Carlos David Manrique Fals | ¿`CarlosManrique-1397`? (confirmar) | 41 | — | — | Mayor volumen del historial |
| Nerlis Nikol Otero Perez | ¿`nerlis-otero`? (confirmar) | 6 | — | — | Merge del corte vertical de ubicación (PR #1) |
| Isabel Sofia Paez Matallana | ¿`i-matallana`? (confirmar, dos correos) | 39 | — | — | ADR 0002 y conversión adoc→md |

## Preguntas abiertas para la sustentación

- ¿`i-matallana` corresponde a Isabel Sofia Paez Matallana? Confirmar con el docente.
- ¿Cómo demuestran que el recorrido de zonas funciona de extremo a extremo, con una prueba y run de CI asociados a la entrega?
- ¿Cómo se conserva la historia de ADR 0001 al cambiar una decisión aceptada y cómo se conecta la fila A-01 con C4, ADR, código y pruebas?
