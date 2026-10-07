# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | UTB Tracker |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_UTB_TRACKER` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Joriel Samir Barros Pena (sin cuentas en el historial) · Geronimo Alberto Cadena Garcia (sin cuentas) · Sebastian Garcia Devoz (firma con dos identidades de git, mismo correo, más el correo institucional) · Mateo Alfonso Millan Barraza (sin cuentas); ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | URL pública vigente no localizada; despliegue No verificado. Ver [S10](semana-10-corte2.md). |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `main` · `ae526db29b4f2d1f5981536e18438f9a62b1516d` · 2026-09-25T11:36:43-05:00 | 1/10 | 1.4 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `main` · `d17c9eb241e56755d48b022dc00ddb865e40c391` · 2026-10-06T01:08:05-05:00 | 2/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 1 | S1 | `(sin commits)` () | sin actividad | no aplica | si |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `0a23855` · 2026-08-16T20:05:46-05:00 | 6/9 | 3.7 (propuesta) | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `5f923cd` · 2026-08-23T22:40:51-05:00 | 7/9 | no se publica | sí |
| 4 | S4 | `2b16439` (2026-08-30T15:02:33-05:00) | 1/10 | 1.4 | si |
| 5 | CORTE1 | `7cfb872` (2026-08-31T12:27:23-05:00) | 8/12 | 3.7 | si |
| 6 | S6 | main `ae526db` — excepción docente | 0/8 | 1.0 | si |
| 7 | S7 | `7cfb872` (2026-08-31T12:27:23-05:00) | 2/10 | 1.8 (prelim.) | si |
| 8 | S8 | `ae526db` (2026-09-25T11:36:43-05:00) | 1/10 | 1.4 (provisional; 2 filas de despliegue pendientes) | sí (definitiva) |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

S8 se califica sobre 10 filas graduables. Quedan **pendientes de calificar** las dos filas de despliegue («URL del sistema accesible desde fuera de la red de la universidad» y «Health check consultable»): la URL se entrega por Moodle y no está disponible en esta pasada.

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| S9 no incorpora commits nuevos frente a S8; la autenticación de octubre es tardía y solo se valora en overall/S10. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Recuperar el CI y ejecutar también tests/ de contratos, préstamos y recursos; actualmente solo se invoca app/tests/. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Actualizar README, enlaces de aspectos y C4 para la nueva estructura; completar arc42 de despliegue. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Publicar URL de despliegue, procedimiento reproducible, logs estructurados, métricas y costo. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Registrar la asignación S10, la línea base, ADR y experimento con resultados. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Actualizar docs/ia.md, auditar propiedad de datos y decidir sobre componente generativo. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Corregir configuración de expiración JWT: [app/core/config.py:10](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/config.py#L10) devuelve texto y [app/core/security.py:10](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/security.py#L10) lo pasa a timedelta(minutes=...). Hallazgo estático; no se ejecutó. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Verificar correspondencia de las identidades del historial con los integrantes. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| El workflow actual coloca preparación de Python y pruebas antes del despliegue mediante needs: test: [.github/workflows/ci.yml:7–26](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L7-L26). Es una mejora tardía; el run aún falla y no cierra CI. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Aparecen firmas adicionales en el historial actual; se retira la afirmación categórica antigua de que solo una persona ha contribuido. No se atribuye por nombre una firma a una persona. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Solo una persona con commits (dos identidades de git del mismo integrante); 3 de 4 integrantes sin aparición en el historial | S1 (y S2) | sí | urgente para el proyecto final: la contribución individual se califica sobre el historial |
| Documentos con restos de edición e incoherencias (ficha obsoleta «sin poder incluirlo a ISCOUTB», tabla de interesados con nombres de otro equipo, enlaces rotos en `aspectos.md`) | S2 | sí | revisar y consolidar antes del corte 1 |
| Enlaces rotos en la documentación S3 (ADR → `10_requisitos_calidad.md` inexistente; `aspectos.md` → `arc42.md#qs-…` con ruta incorrecta) | S3 | sí | corregir las rutas al reorganizar los documentos |
| Basura versionada (`__pycache__/*.pyc`, `db.sqlite3`); `.gitignore` solo ignora `venv/` | S3 | sí | ampliar `.gitignore` y purgar los binarios del repo |
| `docs/ia.md` sin entradas del trabajo S3 ni rechazos con motivo | S3 | sí | registrar el uso de IA de cada entrega, incluyendo lo rechazado |
| Test de salud sin CI ni evidencia de verde | S3 | sí | montar `.github/workflows/` o aportar el run |
| e88a3d6 (2026-08-31T03:35:36-05:00) añade C4 nivel 2, ADR 0002, persistencia y pruebas de loans/resources después del cierre de S4 | S4 | no (resuelto tarde) | — |
| El run CI 33373654206 en HEAD concluye en failure, por lo que las pruebas nuevas no están en verde | S4 | no (resuelto tarde) | — |
| Pipeline en rojo a HEAD | S4 | si | |
| Autoría: 3 integrantes declarados sin commits en el historial | S4 | si | |
| Sin análisis estático SonarCloud | S4 | si | |
| Glosario y secciones 5/6/9/10 de arc42 no verificados en HEAD | S4 | si | |
| Diagnóstico de la restricción asignada | S5 | si | no se pudo ubicar el diagnóstico ni la restricción asignada; localizarla y registrar estado inicial medido antes de sustentar |
| ADR del reto con alternativas, fuerzas y consecuencias | S5 | si | falta un ADR nuevo del reto S5, ligado al escenario de calidad afectado |
| Cambio implementado sobre el corte vertical | S5 | si | los commits de S5 son documentales (texto, C4); falta el cambio que responda al reto |
| Medición reproducible contra umbral | S5 | si | no hay medición con herramienta/carga/procedimiento, ni antes ni después del cambio |
| Trazabilidad navegable en docs/aspectos.md | S5 | si | añadir la fila del reto S5; las filas actuales son de la línea base S4 |
| Análisis estático SonarCloud en pipeline | S5 | si | activar SonarCloud (org isco-utb) en el workflow de CI |
| Registro de IA del corte con salidas rechazadas | S5 | si | docs/ia.md sin cambios desde 2026-08-16; registrar el uso de IA de este corte |
| Participación de los 4 integrantes en el historial | S5 | si | tres integrantes siguen sin commits; es crítico antes del proyecto final |
| Crear correcciones.md en la raíz | S5 | si | |
| Completar tabla de aspectos con enlaces | S5 | si | |
| Subir PDF al aula | S5 | si | |
| Sustentar el corte | S5 | si | |
| Crear correcciones.md en la raíz del repositorio. | S5 | si | |
| Verificar la entrega del PDF en Moodle. | S5 | si | |
| Preparar la sustentación del corte. | S5 | si | |
| Contrato OpenAPI/AsyncAPI/proto versionado con rutas y esquemas de datos | S7 | si | |
| Prueba de contrato presente y ejecutada por el pipeline | S7 | si | |
| Evidencia de que la prueba de contrato falla ante un cambio incompatible | S7 | si | |
| Sección 6 de arc42 con los flujos de interacción | S7 | si | |
| SonarCloud: configuración, run del scanner y URL pública con Quality Gate | S7 | si | |
| Registro de IA con al menos un rechazo justificado | S7 | si | |
| Contribución al historial de los tres integrantes restantes | S7 | si | |
| Que el workflow ejecute la totalidad de las pruebas del repositorio | S7 | si | |
| URL pública del sistema accesible desde fuera de la red de la universidad | S8 | si | |
| Infraestructura como código versionada y recreación del entorno | S8 | si | |
| Health check verificable en el entorno desplegado | S8 | si | |
| Logs estructurados y métrica consultable asociada a un escenario de calidad | S8 | si | |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | S8 | si | |
| arc42 sección 7 con una caja por pieza y sección 2 con límite de costo | S8 | si | |
| Un ADR por decisión de plataforma con alternativa descartada | S8 | si | |
| Análisis estático en SonarCloud con URL pública y Quality Gate | S8 | si | |
| Registro de uso de IA actualizado con rechazos justificados | S8 | si | |
| Evidencia de commits de los cuatro integrantes declarados | S8 | si | |
| Periodo S9 vacío: la punta `ae526db` (2026-09-25) coincide con el hash calificado de S8; no hay porción nueva. | S9 (preliminar) | si | Empujar la porción con IA y su cadena antes del cierre del 2026-10-05. |
| Cadena de aspectos, prueba que falla, medición, auditoría de erosión y dependencias del periodo: sin artefacto S9. | S9 (preliminar) | si | CONTRATO §12: la evidencia previa es línea base y no se recalifica. |
| Componente generativo: sin ADR de no incorporarlo. | S9 (preliminar) | si | Registrar la decisión. |
| Pipeline aún en rojo (`36161882569`) sin corregir en el periodo. | S9 (preliminar) | si | Recuperar el verde y citar la URL del run. |
| Excepción docente en S6: la matriz se completó sobre la punta actual porque no hubo actividad en la ventana de S6. | S6 | no (excepción aplicada) | — |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público del repositorio vigente; [README.md:1–3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/README.md#L1-L3). |
| Estructura mínima presente | Cumple | Las seis rutas mínimas siguen presentes en la punta. La vigencia de enlaces/diagramas se evalúa por separado. [docs/aspectos.md:63–72](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L63-L72). |
| Estado calificado identificable | Cumple | main d17c9eb241e56755d48b022dc00ddb865e40c391 del 2026-10-06; punta preliminar distinta del estado S9 congelado. |
| Nombres de ADR según la convención | Cumple | Tres nombres conformes: 0001-estilo-arquitectonico.md, 0002-cambio-stack-fastapi-flutter.md y 0003-integracion-sincrona.md; [docs/adr/0003-integracion-sincrona.md:7–25](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L7-L25). |
| ADR aceptados no reescritos | Cumple | Historial de los tres ADR: solo sus commits de creación (5f923cd, e88a3d6, 9cf1ac9); sin ediciones posteriores. [docs/adr/0003-integracion-sincrona.md:3–5](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L3-L5). |
| docs/ia.md al día para la semana | No cumple | [docs/ia.md:11–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/ia.md#L11-L14): no documenta tampoco la nueva autenticación y reorganización de octubre. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Run de la punta](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/37422096531) en failure. [.github/workflows/ci.yml:19–23](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L19-L23) solo invoca app/tests/, omitiendo tests/ de contratos/préstamos/recursos; no incluye scanner SonarCloud. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido de la punta sin credenciales reales; [app/core/config.py:7–11](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/config.py#L7-L11) toma las claves del entorno. No se verificó rotación ni configuración del servidor externo. |
| Contribución de todos los integrantes | No verificado | Firmas del historial agregadas, con variantes de identidad; correspondencia con toda la matrícula no verificada. No se mantienen inferencias individuales de informes anteriores. |

## Contribución por integrante

Actualización agregada del 2026-10-06: S9 conserva 25 commits; la punta tiene 32. Variantes de firmas presentes y una firma adicional en octubre; correspondencia completa con la matrícula no verificada, sin inferencias por parecido.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Sebastian Garcia Devoz | dos identidades de git (mismo correo) + correo institucional | 22 | — | — | autor mayoritario del historial |
| Joriel Samir Barros Pena | identidad detectada en el historial | 3 | — | — | aportes menores |
| Geronimo Alberto Cadena Garcia | — | 0 | — | — | sin commits |
| Mateo Alfonso Millan Barraza | — | 0 | — | — | sin commits |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Cómo evitarían dos préstamos simultáneos del mismo recurso y qué prueba o métrica evidencia que el control funciona?
- ¿Qué servidor y base de datos sostienen el despliegue y cuál es su costo mensual y límite de capacidad?
- ¿Qué decisión cambiarían después de comparar la línea base con el experimento del escenario asignado?
