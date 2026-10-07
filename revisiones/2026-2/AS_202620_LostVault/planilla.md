# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | LostVault |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Jose Faustino Espana Noriega · Roy Andres Gonzalez Blanco · Shamara Llorente Tapias · Kiefer Monterroza Manjarres — identidades del historial: Roy Gonzalez (¿`RGBlanco18`?), `shamarallorente-blip`, `Fausto-4` (correo `ganonimo2504`), `weller-rar` (correo `pelu.kiefer`); correspondencias por confirmar con el docente; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://backend-nu-self-91.vercel.app · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `main` · `99fb413bda00c208ec42104dcfe6a4c189fbad77` · 2026-10-04T22:30:53-05:00 | 4/10 | Pendiente por limitación de verificación; intervalo documental 2.6–3.0, sin descontar la comprobación bloqueada | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `main` · `99fb413bda00c208ec42104dcfe6a4c189fbad77` · 2026-10-04T22:30:53-05:00 | 2/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `560ba89` · 2026-08-09T21:10:31-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `af94a30` · 2026-08-16T22:09:43-05:00 | 7/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `1ddb826` · 2026-08-23T23:57:37-05:00 | 4/9 | no se publica | sí |
| 4 | S4 | `952af8f` (2026-08-30T22:13:14-05:00) | 7/10 | 3.8 | si |
| 5 | CORTE1 | `c0c17c1` (2026-09-07T16:46:16-05:00) | 7/12 | 3.3 | si |
| 6 | S6 | `9d57572` (2026-09-13T22:11:29-05:00) | 6/8 | 4.0 (prelim.) | si |
| 7 | S7 | `7bf515f` (2026-09-20T23:55:34-05:00) | 7/10 | 3.8 | sí, auditada |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `4a9ecc94` (2026-09-27T23:52:06-05:00) | 10/10 | 5.0 (provisional; 2 filas de despliegue pendientes) | sí, definitiva |
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
| Completar cadena navegable de AS-04 con C4, código, prueba y medición. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Formalizar la decisión de la porción p95; demostrar la prueba ante defecto concreto y registrar rechazo técnico de IA. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Corregir NC6 o justificar una arquitectura actual que preserve dueño único, con prueba que la proteja. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Agregación de métricas/persistencia en despliegue serverless y tratamiento del fallo con 200 conexiones. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Eliminar referencias a IaC inexistente, ordenar ADR y aportar run/Quality Gate actual. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Asignación S10, autoría y barrido independiente de secretos pendientes. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Se cierra la ausencia preliminar de porción S9: métrica con objective_ms/met y test nuevos. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Registro IA S9 y auditoría NC6 existen, aunque no completan todos sus criterios. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| ADR-0004 formaliza no generación. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Existe medición del despliegue real con umbral y fallos declarados; health accesible hoy. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Historial con una sola identidad de commits | S1 | no (S3 cierre: 4 identidades) | `weller-rar` apareció vía PR #4 en la actualización; confirmar la atribución de `Fausto-4` y `weller-rar` |
| `docs/ia.md` sin registro de lo rechazado ni de uso de IA en S3 | S1 | Sí (última entrada 08-ago) | Actualizar con los usos de S3 y lo rechazado con motivo |
| Estructura incompleta: sin `docs/c4/`; C4 en `docs/arc42/c4_contexto.png` | S1 | Sí | Mover el C4 a `docs/c4/` |
| Sección 4 y matriz comparativa genéricas, sin comparar contra los escenarios 1-4 | S3 | Sí | Reescribir la matriz fila por escenario del árbol de utilidad y ligar la estrategia a los escenarios |
| Paquetes de módulos del ADR inexistentes (solo `lib/main.dart`) | S3 | Sí | Crear `lib/<modulo>/` con la frontera `public/` que declara el ADR; el checklist del README los da por creados |
| ADR no alcanzable desde `aspectos.md` ni desde los escenarios | S3 | Sí | Enlazar el ADR desde la fila del aspecto y desde el escenario que lo motiva |
| Archivos basura en la raíz (`front_end`, `ejecutable`, 1 byte) | S3 (cierre) | Sí (un documento propio, `REVISION_CORREGIDA.md`, afirma desde el 24 de agosto que ya se eliminaron, pero siguen presentes en `corte-1`) | Borrar de verdad los residuos de los zips subidos en `cd5ee95`…`1ddb826`. |
| Integración con SonarCloud pendiente según contrato | S4 | si | |
| C4 nivel 2 sin código fuente que permita verificar coherencia y límites | S4 | si | |
| Arranque documentado pero sin verificación ejecutada | S4 | si | |
| Cortes ejecutables para AS-01, AS-02 y AS-04 pendientes según docs/aspectos.md | S4 | si | |
| Confirmar etiqueta corte-1 | S5 | No (confirmada, `952af8f`, pero sin contenido de reto) | La etiqueta existe y es válida por fecha; su contenido sigue siendo el de S4. |
| Diagnóstico de la restricción asignada con línea base medida | S5 | Sí (sin cambios desde la revisión preliminar) | Cero commits nuevos desde el 30 de agosto (`git log 952af8f..HEAD` vacío); declarar la restricción y medir la línea base. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | S5 | Sí | Sin ADR nuevo. |
| Cambio implementado y ejecutable de extremo a extremo | S5 | Sí | Sin cambio de código desde S4. |
| Medición contrastada con umbral y reproducible | S5 | Sí | Sin medición nueva. |
| Trazabilidad del reto en docs/aspectos.md | S5 | Sí | Sin fila nueva del reto. |
| Registro de IA del corte 1 en docs/ia.md | S5 | Sí | Última entrada sigue siendo del 24 de agosto (S3). |
| PDF de dos páginas en Moodle | S5 | No verificado | No accesible desde el kit. |
| SonarCloud en el pipeline | S5 | Sí | El pipeline (`flutter.yml`) sigue sin paso de SonarCloud. |
| Se agregaron .github/workflows/build.yml y sonar-project.properties en commits posteriores al cierre (37eb409, 847adca, 6e48599, 5c3cf21, 5ed88e6, c0c17c1), sin resolver el pendiente de correcciones.md. | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz del estado calificado. | S5 | si | |
| Run de CI asociado al hash calificado o anterior al corte. | S5 | si | |
| Cortes ejecutables y mediciones de AS-01, AS-02 y AS-04. | S5 | si | |
| Crear correcciones.md en la raíz | S5 | si | |
| Completar trazabilidad con C4 en docs/aspectos.md | S5 | si | |
| Limpiar archivos residuales | S5 | si | |
| docs/arc42/08* con lenguaje ubicuo y mapa de contextos incorporado. | S6 | si | |
| C4 nivel 3 y ADR del reajuste si los límites cambiaron respecto al corte anterior. | S6 | si | |
| URL pública del análisis de SonarCloud con rama o revisión y estado del Quality Gate. | S6 | si | |
| Columnas Requisito y C4 en docs/aspectos.md y cierre de las celdas pendientes de AS-01, AS-02 y AS-04. | S6 | si | |
| Correspondencia entre el contrato y una API implementada (o aclaración explícita de que la frontera HTTP aún no existe). | S7 | si | |
| Evidencia de ejecución de la prueba de contrato en rojo ante un cambio incompatible. | S7 | si | |
| URL pública del análisis en SonarCloud con Quality Gate para el hash revisado. | S7 | si | |
| C4 nivel 2 revisable (como código) con protocolo y formato en cada flecha (el diagrama existe como .jpg; sus flechas de cruce tecnológico no llevan protocolo ni formato). | S7 | si | — |
| Columna C4 y celdas completas en docs/aspectos.md para todas las filas. | S7 | si | |
| Actualización de docs/arc42/09_decisiones.md con el ADR 0002. | S7 | si | |
| Despliegue público, health check e infraestructura como código ausentes | S8 | No (resuelto en S8) | API desplegada en Vercel; Dockerfile/Compose/Terraform versionados; URL y health documentados. |
| Sin logs estructurados, métrica consultable ni estimación de costo | S8 | No (resuelto en S8) | Logs JSON por request, `GET /metrics` (p95 ligado al escenario de rendimiento) y estimación con supuestos y ruptura. |
| arc42 §7 y ADR de plataforma ausentes | S8 | No (resuelto en S8) | `07_vista_despliegue.md` con una pieza por fila y ADR-0003 de plataforma con alternativa y capa gratuita. |
| ADR `000.3` incumple la convención de nombres | S8 | Sí | Renombrar a `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados editados sin reemplazo declarado (0001, 0002) | S8 | Sí | No editar ADR aceptados; si cambia la decisión, escribir otro y marcar el anterior como reemplazado. |
| URL pública del Quality Gate de SonarCloud | S8 | Sí | Publicar el enlace del análisis y el estado del Quality Gate. |
| `backend/vercel.json` citado por arc42 §7 y Terraform no existe en el repo | S8 | Sí | Versionarlo o corregir las referencias documentales. |
| Sin entrega S9 en la punta: el periodo `4a9ecc94..a5faf6a` solo modifica `backend/DEPLOY_VERCEL.md` (Swagger UI) | S9 | Sí (preliminar) | Empujar la porción construida con IA, su ADR, la prueba que falla y la medición antes del cierre del 2026-10-05T05:00:00Z. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_LostVault; [README.md:1-9](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/README.md#L1-L9). |
| Estructura mínima presente | Cumple | Árbol Git contiene las seis rutas mínimas; índice [README.md:207-224](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/README.md#L207-L224). |
| Estado calificado identificable | Cumple | origin/main 99fb413bda00c208ec42104dcfe6a4c189fbad77; último commit anterior al cierre en cabecera. |
| Nombres de ADR según la convención | No cumple | [docs/adr/000.3-despliegue-busqueda-lostvault.md:1-4](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L1-L4) usa 000.3, fuera de convención; [docs/adr/0003-plataforma-despliegue-vercel.md:23-30](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L23-L30) reconoce el typo y que es un taller distinto. |
| ADR aceptados no reescritos | No cumple | Historial verificado de ADR-0001/0002: [edd78d72](https://github.com/ISCOUTB/AS_202620_LostVault/commit/edd78d72afe70c55ca77e37b909f2ab8ab442834) y [b5615768](https://github.com/ISCOUTB/AS_202620_LostVault/commit/b5615768472c8c64dc3abff3dbf701faa40c2420) modifican decisiones aceptadas; no se localizó reemplazo declarado que resuelva el arrastre. |
| docs/ia.md al día para la semana | No cumple | [docs/ia.md:181-223](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ia.md#L181-L223) está al día temporalmente, pero falta rechazo con motivo técnico de S9; la razón de propiedad individual no satisface esa parte. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [.github/workflows/build.yml:62-76](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/.github/workflows/build.yml#L62-L76) tiene scanner y Quality Gate; configuración versionada sonar-project.properties. Única consulta PR del hash devolvió cero runs, sin demostrar inexistencia de runs push. No se verificó run/Quality Gate público de este hash y no se recicla el verde S8. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El equipo auditó main.py/Dockerfile en [docs/ddd/auditoria_backend.md:29-44](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L29-L44) y el código lee JWT_SECRET del entorno en [backend/main.py:50-55](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L50-L55). El barrido independiente completo fue cancelado por la herramienta, también en el reintento autorizado. No se atribuye exposición ni incumplimiento académico por esa limitación; falta cerrar la comprobación del revisor. El literal de CI en [.github/workflows/build.yml:55-60](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/.github/workflows/build.yml#L55-L60) está rotulado como prueba efímera y no se presenta como secreto de producción. |
| Contribución de todos los integrantes | No verificado | La planilla anterior deja asociaciones de varias cuentas por confirmar. No se asignan personas por semejanza ni se repiten conteos antiguos como estado vigente; pendiente validación docente de autoría. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Historial de la punta: 124 commits y 9 firmas de autor distintas (firmas, no personas). La planilla anterior deja asociaciones de varias cuentas por confirmar. No se asignan personas por semejanza ni se repiten conteos antiguos como estado vigente; pendiente validación docente de autoría.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Jose Faustino Espana Noriega | ¿`Fausto-4`? (correo `ganonimo2504`, sin confirmar) | 1 (via PR #3) | — | — | Apareció en S3 con «Add files via upload»; correspondencia por confirmar con el docente |
| Roy Andres Gonzalez Blanco | «Roy Gonzalez» en commits (¿`RGBlanco18`?) — confirmar | 24 (HEAD) | 2 PR mergeados (#1, #3) | — | Principal autor; hace los merges |
| Shamara Llorente Tapias | `shamarallorente-blip` (correo institucional `[correo omitido]`) | 1 (via PR #1) | 0 | — | Autora del ADR 0001 |
| Kiefer Monterroza Manjarres | ¿`weller-rar`? (correo `pelu.kiefer`, sin confirmar) | 1 (via PR #4) | 0 | — | Primera aparición en la actualización S3 (PR #4: «Create ejecutable») |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Fallo: ¿cómo evitarán dos reclamaciones inconsistentes o pérdida de datos cuando Vercel atienda solicitudes en instancias distintas?
- Costo: ¿cuánto cuestan persistencia y métricas compartidas para sostener 200 conexiones, frente al plan gratuito actual?
- Medición: con ~44 % de fallos bajo la carga prevista, ¿qué decisión de plataforma o control de carga cambiarían y qué resultado demostraría la mejora?
