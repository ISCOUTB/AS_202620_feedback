# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo GimnasioUTB. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | GimnasioUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Sebastian Felipe Caicedo Acosta · Rodrigo Andres Facio Lince Beltran · Pedro Luis Pallares De La Hoz — cuentas abajo; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://gimnasio-utb.iscoutb.dev · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `main` · `af4796d6320766611d9fc01d7112a1c0e4112b40` · 2026-10-04T16:52:10-05:00 | 8/10 | 4.2 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `main` · `c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec` · 2026-10-05T18:16:08-05:00 | 3/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 6 | S6 | `106869b` (2026-09-13T22:19:08-05:00) | 6/8 | 4.0 (prelim.) | si |
| 8 | S8 | `a71bc75` (2026-09-27T21:55:06-05:00) | 3/10 | 2.2 | sí, definitiva |
| 7 | S7 | `0e3aeb5` (2026-09-20T23:29:29-05:00) | 8/10 | 4.2 | sí, auditada |
| 5 | Primer corte · reto de línea base | HEAD `9b9f7c8` (sin etiqueta `corte-1`) | 2/12 | subtotal técnico 0,60/4,00; sustentación pendiente | revisión definitiva post-cierre 2026-09-07 |
| 4 | S4 | `56db96b` (2026-08-30T22:33:47-05:00) | 2/10 | 1.8 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `a45615e9` · 2026-08-08T21:41:21-05:00 | 4/9 | 2,8 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `1b30b7a4` · 2026-08-16T21:04:17-05:00 | 5/9 | 3,2 * | sí |
| 3 | S3 | `73c1f24` (2026-08-23T19:38:29-05:00) | 6/9 | 3.7 | si |

S8 se califica sobre 10 de las 12 filas de la ficha: quedan pendientes de calificar las dos filas de despliegue (URL del sistema accesible desde fuera de la red de la universidad y health check consultable), porque la URL se entrega por Moodle. La nota publicada es provisional.

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Convertir aspectos en cadena de ocho columnas con enlaces reales a C4, código, prueba y medición. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Formalizar mediante ADR la decisión de no incorporar generación y la plataforma Dokploy. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Incluir PostgreSQL real en CI y aportar scanner, run y Quality Gate público. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Conservar ADR aceptados y resolver duplicación del 0001. Confirmar cuentas sin inferir personas. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Identificar el escenario asignado de S10 y levantar una línea base del despliegue. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Ya existe registro IA S9 con rechazo técnico y auditoría de erosión; V1 y V2 están corregidas en código. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La prueba de fallo por pérdida de bloqueo está documentada; no sigue simplemente «sin evidencia». | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| En la punta posterior al cierre ya existen Dockerfile, Compose, URL pública y arc42 de despliegue; no modificar notas S8/S9 por ello. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Sin `docs/arc42/` ni `docs/c4/` (arc42 en un solo archivo `docs/arc42_gimnasio_utb.md`, C4 en `docs/C4.jpg`) | S1 | Sí (parcial: `docs/adr/` ya existe) | Repartir el arc42 en `docs/arc42/` y el C4 en `docs/c4/` |
| Sebastián Caicedo Acosta sin commits ni cuenta atribuible | S1 | Cerrado en S3 (9 commits, identidad consolidada `[correo omitido]`) | Se resolvió; vigilar que la contribución siga repartida |
| `docs/aspectos.md` en prosa, sin la tabla de 8 columnas ni enlaces a escenarios | S1 | Sí | Convertir a tabla ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia y enlazar ADR y escenarios |
| `docs/ia.md` sin lo rechazado y su motivo por uso | S1 | Sí (mejora: entradas S3 con prompt y verificación) | Añadir por cada uso qué se rechazó y por qué |
| Inconsistencia «Equipo de 4 personas» (OC5) | S2 | Sí | Son 3 según matrícula; corregir en arc42 y en el ADR |
| ADR no alcanzable desde `aspectos.md` ni desde los escenarios ES1/ES7/ES8 | S3 | Sí | Enlazar el ADR desde la fila del aspecto y desde cada escenario que lo motiva |
| Implementar corte vertical (interfaz HTTP, lógica de aplicación, persistencia PostgreSQL) | S4 | si | |
| Añadir prueba automatizada del recorrido completo (registro de acceso y consulta de aforo) | S4 | si | |
| Corregir README: un solo comando de arranque y scripts existentes en package.json | S4 | si | |
| Completar trazabilidad de docs/aspectos.md y ADR 0001 con rutas y commits reales | S4 | si | |
| Verificar y completar secciones 4-6, 9, 10 y 12 del arc42 | S4 | si | |
| Configurar análisis estático con SonarCloud | S4 | si | |
| Etiqueta `corte-1` ausente | S5 | Sí | Sigue sin existir a la fecha del cierre; se calificó el último commit ≤ cierre (`9b9f7c8`). Etiquetar el estado entregable en cortes futuros. |
| Respuesta al reto sin diagnóstico, ADR ni incremento identificado | S5 | Sí | El trabajo previo al cierre (`7094a6c`..`9b9f7c8`) fue documental (README, aspectos, glosario, `correcciones.md`); sigue faltando diagnóstico, ADR, cambio de código y medición del reto. |
| Prueba concurrente con PostgreSQL y medición contra umbral pendientes | S4 | Sí | Aportar herramienta, carga, procedimiento, resultado y run de CI del cambio. |
| `docs/aspectos.md` no usa las ocho columnas del contrato ni contiene una fila del reto | S5 | Parcial (S1 sí es navegable) | La fila de S1 ya es navegable de escenario a pruebas; falta una fila para el reto de Corte 1. |
| Registro de IA sin entrada del Corte 1 | S5 | No (resuelto) | `docs/ia.md` ya tiene una entrada "Semana 5" (2026-09-06) con lo aceptado y lo rechazado con motivo técnico. |
| ADR aceptado reescrito en commits posteriores | S5 | Sí | Confirmado: `92f4a53` (aceptado) fue editado en contenido por `c271073`,`b556737`,`59b6d3e`,`47a18d0` (2026-08-30). Mantener el ADR histórico y registrar cambios mediante otro ADR. |
| Commit 38f0031 del 2026-09-01 y siguientes actualizan README después del cierre. | S3 | no (resuelto tarde) | — |
| Commit ba45154 del 2026-09-07 añade ADR0001.md y reorganiza docs/arc42/ y docs/c4/. | S3 | no (resuelto tarde) | — |
| Commits 9b9f7c8 y 56db96b actualizan docs/ia.md después del cierre. | S3 | no (resuelto tarde) | — |
| Sección 4 completa de arc42 y matriz comparativa verificable. | S3 | si | |
| docs/aspectos.md con enlaces al ADR y a los escenarios. | S3 | si | |
| Integración de SonarCloud en el pipeline. | S3 | si | |
| Consolidar la estructura mínima en HEAD y mantener la trazabilidad en las próximas semanas. | S3 | si | |
| Integrar el scanner de SonarCloud en .github/workflows/ci.yml y publicar la URL del análisis con el estado del Quality Gate. | S6 | si | |
| Eliminar o renombrar docs/adr/ADR0001.md para cumplir la convención NNNN-titulo-kebab-case.md. | S6 | si | |
| Completar docs/aspectos.md con las ocho columnas del contrato (C4 y Evidencia). | S6 | si | |
| Confirmar o escribir la sección 8 del arc42 con lenguaje ubicuo y mapa de contextos. | S6 | si | |
| Añadir C4 nivel 3 y ADR de reajuste si los límites de los contextos cambiaron desde el primer corte. | S6 | si | |
| Implementar el adaptador PostgreSQL y el historial de eventos, hoy declarados pendientes. | S6 | si | |
| SonarCloud sin evidencia auditable (configuración, scanner en el workflow y URL del análisis con Quality Gate). | S7 | si | |
| docs/adr/0003-comunicacion-sincrona-asincrona.md sin alternativa descartada ni escenario de calidad citado. | S7 | si | |
| docs/adr/ADR0001.md duplicado y fuera de la convención de nombres. | S7 | si | |
| docs/aspectos.md sin las ocho columnas del curso (faltan C4 y Evidencia). | S7 | si | |
| Evidencia de fallo de la prueba contractual ante un cambio incompatible | S7 | Sí | Aportar el log contractual o una reproducción verificable. |
| Despliegue público, health check e infraestructura como código ausentes | S8 | Sí | Publicar Render y versionar su definición. |
| Sin logs estructurados, métrica consultable ni estimación de costo completa | S8 | Sí | Instrumentar observabilidad y calcular el punto de ruptura. |
| arc42 §7 y ADR independiente de plataforma ausentes | S8 | Sí | Documentar cada pieza y su decisión de alojamiento. |
| Prueba que demuestre fallar ante el defecto de la porción S9 (run en rojo, mutación o procedimiento) | S9 | Sí | La prueba PostgreSQL existe en el periodo, pero falta la evidencia del fallo controlado. |
| Auditoría de erosión del periodo de generación S9 | S9 | Sí | Documentar si cruzó límites de contexto o reglas de propiedad de datos de S6, y su corrección. |
| ADR de decisión sobre el componente generativo | S9 | Sí | La ausencia de decisión no es la decisión de no incorporarlo. |
| `docs/ia.md` sin entrada de S9 (sigue en la semana 6) | S9 | Sí | Registrar lo aceptado, lo corregido y lo rechazado con motivo de la porción S9. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_GimnasioUTB; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Árbol Git con README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md; índice en [README.md:108-121](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L108-L121). |
| Estado calificado identificable | Cumple | Punta preliminar origin/main c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec; fecha anterior al cierre futuro S10. No modifica S9. |
| Nombres de ADR según la convención | No cumple | [docs/adr/ADR0001.md:1-8](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/adr/ADR0001.md#L1-L8) no sigue NNNN-titulo-en-kebab-case y duplica el número de [docs/adr/0001-arquitectura-hexagonal.md:1-5](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/adr/0001-arquitectura-hexagonal.md#L1-L5). |
| ADR aceptados no reescritos | No cumple | El ADR-0001 ya aceptado sigue reescrito sin reemplazo: historial verificado en [3fae092f](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/3fae092fe6d33872772f106dc2737f88339ba82c) y estado canónico [docs/adr/0001-arquitectura-hexagonal.md:1-15](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/adr/0001-arquitectura-hexagonal.md#L1-L15). La punta añade otra edición tardía. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:100-112](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/docs/ia.md#L100-L112) incorpora S9 con correcciones/rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [README.md:86-88](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L86-L88) declara ausencia de PostgreSQL en CI y de SonarCloud/Quality Gate; no se verificó run de esta punta. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Barrido estático del árbol textual, incluidos ejemplos y documentación: sin candidatos de credenciales reales; no hay .env versionado. [.github/workflows/ci.yml:11-23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/.github/workflows/ci.yml#L11-L23) y variables de entorno en [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js:14-27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js#L14-L27). Los PDF se excluyeron. No equivale a una certificación exhaustiva de secretos. El recorrido histórico ampliado está pendiente de completar; no se afirma ausencia histórica por el resultado del árbol actual. |
| Contribución de todos los integrantes | No verificado | Historial agregado a la punta: 5 grupos por correo idéntico frente a 3 integrantes; firmas distintas no se atribuyen por semejanza. Se requiere confirmar correspondencia cuenta–persona, sin publicar correos. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Historial de la punta: 108 commits y 7 firmas de autor distintas (firmas, no personas). Historial agregado a la punta: 5 grupos por correo idéntico frente a 3 integrantes; firmas distintas no se atribuyen por semejanza. Se requiere confirmar correspondencia cuenta–persona, sin publicar correos.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Sebastian Felipe Caicedo Acosta | `sebastian-caicedo` + «Sebastian Felipe Caicedo Acosta» (mismo correo `[correo omitido]`, consolidado) | 9 | 0 | — | Se incorporó en S3 (esqueleto, §4, ADR y CI); cerró el hallazgo de S1 |
| Rodrigo Andres Facio Lince Beltran | RodrigoFacioLince (correo omitido) | 3 | 0 | — | Sin commits en S3 |
| Pedro Luis Pallares De La Hoz | PedroPambi (correo omitido) | 9 | 0 | — | Documentó arranque y CI en README (último commit S3) |

Correspondencia cuenta↔persona inferida del correo institucional de los commits; la confirma el docente.

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Fallo: si PostgreSQL deja de responder o el pool se agota, ¿qué timeout y señal operativa impedirán que las solicitudes queden esperando indefinidamente?
- Costo: ¿qué recursos consume el Compose completo y cuál es el límite que obliga a abandonar el alojamiento sin costo?
- Medición: ¿qué cambiarían al pasar de 20 llamadas directas al adaptador a carga HTTP y qué resultado justificaría esa decisión?
