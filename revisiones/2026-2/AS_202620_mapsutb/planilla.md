# Planilla de equipo · mapsutb

## Identificación

| | |
|---|---|
| Equipo | mapsutb |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Carlos Alberto Galvis Zuluaga · Carlos David Manrique Fals · Nerlis Nikol Otero Perez · Isabel Sofia Paez Matallana — cuentas observadas en el historial: `charlygz21`, `nerlis-otero`, `CarlosManrique-1397`, `i-matallana` (correspondencias por confirmar con el docente); ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://mapsutb.web.app/ · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `1b296a37c575a751e99df1a1b288d70efba03d56` · 2026-10-02T12:58:33-05:00 | 8/10 | Pendiente por limitación de verificación; intervalo documental 4.2–4.6, sin descontar la comprobación bloqueada | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `1b296a37c575a751e99df1a1b288d70efba03d56` · 2026-10-02T12:58:33-05:00 | 2/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `7e56ad3` · 2026-08-09T23:27:46-05:00 | 5/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `1cf1576` · 2026-08-16T21:26:05-05:00 | 4/9 | 2.8 | sí (revisión manual confirmatoria) |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `ed55eda` · 2026-08-23T21:44:05-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `f0d036a` (2026-08-30T22:53:06-05:00) | 5/10 | 3.0 | si |
| 5 | CORTE1 | `e8bad4c` histórico; excepción: `8aee879` (2026-09-13T18:14:14-05:00) | 8/12 | 3.7 | sí (actualizada con correcciones tardías aceptadas) |
| 6 | Evidencia S6 · Contextos delimitados y propiedad de datos | `8aee879` (2026-09-13T18:14:14-05:00) | 5/8 | 3.5 (prelim.) | sí |
| 7 | S7 | `5e2fdd5` (2026-09-20T21:15:28-05:00) | 10/10 | 5.0 | sí (auditoría definitiva corregida) |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `8cfe4581` (2026-09-27T16:35:57-05:00) | 10/10 | 5.0 (propuesta; 2 filas de despliegue pendientes) | sí (definitiva) |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Convertir rutas en enlaces navegables de A-01 y corregir C4 que todavía dice MapaRepository pendiente. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Separar medición de cálculo/pantalla de GPS real y precisión geográfica; no afirmar un flujo físico completo desde un test sintético. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Verificar política de caché efectiva por URL y qué ve un usuario previo a un rollback. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Aportar run/Quality Gate del hash, confirmar atribución y completar barrido independiente pendiente. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Identificar el reto S10 antes de puntuar su respuesta. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| ADR-0014 ahora aceptado por el equipo; no sigue pendiente de decisión. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Evidencia S9 incluye medición de pantalla además del algoritmo. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La sección de dependencias coincide con las incorporaciones flutter_map/latlong2. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| A-01 ya reconoce la pantalla implementada; queda otro texto anterior en C4. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| URL y health hoy accesibles, con commit desplegado igual al revisado. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

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
| Dejar el pipeline actual en verde y publicar la evidencia de análisis estático con Quality Gate. | S8 | sí (parcial: el pipeline del hash revisado quedó citado en verde —`CI` #31 y `Despliegue web` #6—; falta el Quality Gate público de SonarCloud) | Publicar el Quality Gate del análisis sobre el hash revisado |
| Añadir logs estructurados, una métrica operativa consultable y manejo seguro de secretos en la plataforma. | S8 | sí | No hay evidencia verificable de observabilidad ni de inyección segura de la clave de Google. |
| Completar costo mensual, arc42 §7 y ADR de plataforma de despliegue. | S8 | sí | Solo está documentada la restricción de costo cero; faltan cálculo y decisión de plataforma. |
| ADR 0014 (no incorporar componente generativo) queda en estado *Propuesto*: falta la decisión del equipo. | S9 | sí | Marcar el ADR como *Aceptado* o tomar la decisión del componente generativo antes del cierre. |
| `docs/aspectos.md` (A-01) declara pendiente la pantalla de mapa que ya existe en la punta (`b679886`). | S9 | sí | Actualizar la celda Código de A-01. |
| `docs/evidencia-s9.md` §8 afirma «ninguna dependencia nueva» mientras `pubspec.yaml` añade `flutter_map` y `latlong2`. | S9 | sí | Alinear la sección de dependencias con el manifiesto. |
| GPS real y coordenadas definitivas de las 11 zonas, declarados pendientes por el equipo. | S9 | sí | Registrar los datos en campo y regenerar el grafo. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_mapsutb; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes en árbol; arc42 mezcla adoc y md como desviación de formato, sin tratar artefactos existentes como ausentes; [docs/aspectos.md:5-9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/aspectos.md#L5-L9). |
| Estado calificado identificable | Cumple | origin/master 1b296a37c575a751e99df1a1b288d70efba03d56; fecha/corte en cabecera. |
| Nombres de ADR según la convención | Cumple | Listado docs/adr 0001–0015 conforme; [docs/adr/0015-cache-del-sitio-revalidar.md:1-9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L1-L9). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0001-patrones-de-diseno.md:5-14](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0001-patrones-de-diseno.md#L5-L14) reconoce ediciones aceptadas; el historial confirma cambios antes del reemplazo. ADR-0015 sí complementa decisiones sin reescribirlas; es una mejora de práctica, no eliminación del historial. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:21-25](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/ia.md#L21-L25) contiene S9 y rechazos motivados. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [.github/workflows/ci.yml:44-64](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/.github/workflows/ci.yml#L44-L64) contiene suite, scanner y gate. El conector consultó una vez el hash con filtro PR y devolvió cero registros; no demuestra falta de runs push. Los runs enlazados en [docs/evidencia-s9.md:52](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L52) son evidencia documental; falta trío de comprobación pública vigente para este hash. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El equipo declara su barrido en [docs/evidencia-s9.md:104-109](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L104-L109). El barrido independiente agregado fue cancelado por la herramienta y no se completó en el único reintento; no hay base para certificar limpieza integral ni para atribuir exposición al equipo. La comprobación permanece pendiente del revisor. |
| Contribución de todos los integrantes | No verificado | La planilla anterior mantiene correspondencias cuenta–persona por confirmar. No se atribuyen identidades por nombres parecidos ni se reutilizan conteos anteriores como comprobación vigente. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Historial de la punta: 211 commits y 5 firmas de autor distintas (firmas, no personas). La planilla anterior mantiene correspondencias cuenta–persona por confirmar. No se atribuyen identidades por nombres parecidos ni se reutilizan conteos anteriores como comprobación vigente.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Carlos Alberto Galvis Zuluaga | ¿`charlygz21`? (confirmar) | 13 | — | — | Autor de los commits `FeedbackS1..S4` (06/09, archivos vacíos) |
| Carlos David Manrique Fals | ¿`CarlosManrique-1397`? (confirmar) | 41 | — | — | Mayor volumen del historial |
| Nerlis Nikol Otero Perez | ¿`nerlis-otero`? (confirmar) | 6 | — | — | Merge del corte vertical de ubicación (PR #1) |
| Isabel Sofia Paez Matallana | ¿`i-matallana`? (confirmar, dos correos) | 39 | — | — | ADR 0002 y conversión adoc→md |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Fallo: si el GPS entrega una posición errónea o el usuario conserva una versión cacheada, ¿qué señal evita una ruta engañosa y cómo verificarán el rollback desde su navegador?
- Costo: ¿cuál de las cuotas de Hosting/teselas/transferencia rompe primero el presupuesto cero y cómo cambia al revalidar recursos?
- Medición: ¿qué cambiarían si el tiempo de cálculo sigue siendo bajo pero el usuario tarda o se localiza a más de 10 metros del camino real?
