# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | CampusMarket |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Nilver Garcia Pimentel · Camilo Jose Martinez Berrio · Joshua Jose Tenorio Alvarez — cuentas consolidadas: `nilver-garcia`/`Nnigarp` (mismo id de cuenta, es una sola persona), `camilixo92`, `Carulla-sd`; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://nnigarp.github.io/AS_202620_PROYECTO_CAMPUSMARKET/ · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00` · 2026-10-04T02:14:34-05:00 | 10/10 | 5.0 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00` · 2026-10-04T02:14:34-05:00 | 4/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `81ef5f1` · 2026-08-08T20:17:21-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `4f72799` · 2026-08-16T22:01:41-05:00 | 7/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `4dd857a` · 2026-08-23T23:54:16-05:00 | 9/9 | no se publica | sí |
| 4 | S4 | `f3f4367` (2026-08-30T22:55:30-05:00) | 9/10 | 4.6 | si |
| 5 | CORTE1 | `8044215` (2026-09-06T16:05:15-05:00) | 10/12 | 4.3 | si |
| 6 | S6 | `dc548c0` (2026-09-13T01:19:54-05:00) | 7/8 | 4.5 | si |
| 7 | S7 | `c53ee32` (2026-09-18T21:11:48-05:00) | 10/10 | 5.0 | si |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `784d788` en `master` (2026-09-27T23:50:19-05:00) | 10/10 | 5.0 (2 filas de despliegue pendientes) | sí |
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
| Acreditar el escenario operativo asignado de S10 y preparar baseline/resultado comparables sobre el MVP desplegado. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Incorporar scanner Sonar y enlazar run del hash, análisis público y Quality Gate; demostrar bloqueo de integración. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar EC-01 público con 1000 filas, sin equiparar los tiempos loopback de CI al navegador. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Mantener constancia del historial de ADR aceptados reescritos; no repetir la práctica. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar barrido independiente del historial y confirmar mapa de identidades de autoría. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Revisar avisos vigentes que PyPI lista para python-multipart 0.0.20 y su aplicabilidad a la configuración; legitimidad del paquete no demuestra seguridad de la versión. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| La ausencia de entrega S9 de la preliminar queda superada: existen porción, trazabilidad, mutaciones, medición, IA, auditoría y ADR de no componente generativo. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La URL pública y el health check de S8 diferidos pudieron comprobarse por lectura en la revisión actual; esto no modifica retroactivamente S8. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La declaración inicial de ausencia de dependencias fue corregida por auditoría ampliada del periodo completo. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Historial con una sola identidad de commits (23/23) | S1 | no (S3: 3 personas; confirmado en S5 que `nilver-garcia`/`Nnigarp` son la misma cuenta) | Consolidar la identidad duplicada en git |
| Estructura fuera de convención: archivos sueltos en `docs/` | S1 | no (S3 resuelto, confirmado en `corte-1`) | `docs/arc42/`, `docs/adr/` y `docs/c4/` ya existen |
| `docs/aspectos.md` sin tabla ni enlaces | S1 | no (S3 resuelto; en S5 llegó a 6 filas con ASP-06 completo) | Tabla de 8 columnas con enlaces funcionales |
| `docs/ia.md` sin registro de lo rechazado | S1 | no (resuelto en S3/S4, confirmado en S5) | Mantener una entrada por semana con rechazo o corrección y motivo técnico |
| ADR 0001 ausente aunque arc42 y aspectos.md lo enlazaban | S3 | no (resuelto en PR #5) | ADR completo y enlazado desde EC-03 y ASP-03 |
| README sin comando único de arranque | S3 | no (resuelto) | `python -m uvicorn backend.app.main:app --reload` documentado |
| Sin prueba automatizada ni pipeline | S3 | no (resuelto) | `backend/tests/test_health.py` + workflow con runs en verde |
| Esqueleto Flutter por defecto, sin módulos del ADR | S3 | no (resuelto en S4: módulos `usuarios/publicaciones/catalogo/administracion`) | Backend y frontend con los 4 módulos |
| Integrar SonarCloud al pipeline | S4 | no (resuelto en S5: `.sonarcloud.properties` con proyecto oficial `ISCOUTB_AS_202620_PROYECTO_CAMPUSMARKET`; Quality Gate no verificado de forma independiente) | Confirmar en vivo el Quality Gate en la sustentación |
| Verificar arranque con un solo comando mediante ejecución | S4 | no (resuelto: evidencia en `docs/evidencias/arranque-un-comando-2026-09-04.md`) | — |
| Enlazar ADR-0001 con commit que lo implementa | S4 | no (resuelto: PR #5, commit `4dd857a`) | — |
| Definir medición de línea base | S4 | no (resuelto en S5 junto con el reto) | — |
| Diagnóstico de la restricción asignada (R-07) | S5 | no (resuelto: ADR-0002 y `docs/evidencias/linea-base-bloqueo-sqlite-2026-09-05.md`) | — |
| ADR del reto con alternativas y decisión | S5 | no (resuelto: ADR-0002) | — |
| Implementación del cambio sobre el corte vertical | S5 | no (resuelto: PR #28, commit `ff68cf2`) | — |
| Pruebas y medición contra umbral | S5 | no (resuelto: `test_bloqueo_sqlite_degrada_controladamente_y_se_recupera`, `medir_bloqueo_sqlite.py`) | — |
| Trazabilidad del reto en docs/aspectos.md | S5 | no (resuelto: fila ASP-06) | — |
| Registro de IA del corte en docs/ia.md | S5 | no (resuelto: sección "Evidencia S5") | — |
| PDF de dos páginas en Moodle | S5 | sin verificar | No disponible en el kit; confirmar en Moodle antes de cerrar la nota |
| ASP-01 y ASP-02 sin materializar en el corte vertical | S5 | sí (declarado explícitamente por el equipo, no oculto) | Materializar en cortes siguientes o mantener la declaración explícita si se posponen |
| Verificar entrega del PDF en Moodle | S5 | si | |
| Confirmar sustentación del corte | S5 | si | |
| Mapa de contextos con relaciones tipificadas | S6 | si | |
| Tabla módulo a datos con dueño único | S6 | si | |
| Lista de violaciones de propiedad de datos con plan de corrección | S6 | si | |
| Sección 8 de arc42 con lenguaje ubicuo y mapa de contextos | S6 | si | |
| C4 nivel 3 y ADR si los límites cambian | S6 | si | |
| Verificar contenido de docs/aspectos.md | S6 | si | |
| Verificar contenido de docs/ia.md | S6 | si | |
| Aportar runs_ci del pipeline | S6 | si | |
| Migración de SQLite a MySQL (ADR-0004, 2026-09-16) como corrección posterior al primer corte por observación docente; evidencia docs/adr/0004-migrar-persistencia-a-mysql.md y README. | S7 | no (resuelto tarde) | — |
| Evidencia de run de CI que ejecute la prueba de contrato. | S7 | si | |
| URL pública de SonarCloud con Quality Gate y run del scanner. | S7 | si | |
| Fragmento del contrato con schemas y cotejo con router.py. | S7 | si | |
| Contenido de docs/aspectos.md y docs/ia.md. | S7 | si | |
| Migración de persistencia SQLite→MySQL documentada en `docs/adr/0004-migrar-persistencia-a-mysql.md` (fechado 2026-09-16) como corrección posterior al cierre de S5, fuera del plazo de esa entrega. | S7 | no (resuelto tarde) | — |
| Saneamiento de S7 mediante el merge 5bedc83 (2026-09-17, PR #42 desde una rama de revisor) y los commits de documentación 3ca4535 y c53ee32 (2026-09-18). | S7 | no (resuelto tarde) | — |
| commits_post_cierre está vacío y no se aportó diff_desde_cierre: no se observan cambios posteriores al cierre de esta actividad. | S7 | no (resuelto tarde) | — |
| Acreditar SonarCloud: línea del scanner en el workflow y URL pública del análisis con estado del Quality Gate. | S7 | si | |
| Aportar la URL del run de CI sobre el hash revisado y del run en rojo del repositorio de la organización. | S7 | si | |
| Dejar revisable el contenido de `docs/aspectos.md` y `docs/ia.md`. | S7 | si | |
| Aportar `docs/c4/02-contenedores.puml` con protocolo y formato en cada flecha. | S7 | si | |
| Publicar una URL verificable, health check, IaC y observabilidad S8. | S8 | no (resuelto en el estado calificado: despliegue en GitHub Pages + Azure, `infra/main.bicep`, logs y métrica EC-01) | — |
| Acreditar SonarCloud: línea del scanner en el workflow y URL pública del análisis con Quality Gate. | S7 | sí (reiterado en S8: `.sonarcloud.properties` sin invocación del scanner ni URL pública) | Añadir el paso `sonar` al workflow y publicar el análisis con su Quality Gate |
| No editar ADR aceptados sin declarar reemplazo. | S8 | sí (ADR-0002, ADR-0003 y ADR-0005) | Los ajustes debieron ir en un ADR nuevo o declarar el reemplazo |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon git público de ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET y rama master; URL oficial y nombre conforme. |
| Estructura mínima presente | Cumple | Árbol con README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md; entrada navegable [README.md:13–28](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L13-L28). |
| Estado calificado identificable | Cumple | Último commit de origin/master anterior o igual al cierre: de6ed67c05ccdb7eabd9b1951f146ab8958b1d00, 2026-10-04T02:14:34-05:00; coincide con HEAD observado. |
| Nombres de ADR según la convención | Cumple | Inventario git de docs/adr: 0001–0019 siguen NNNN-titulo-en-kebab-case.md. Ejemplo [docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md:1–6](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md#L1-L6). |
| ADR aceptados no reescritos | No cumple | Historial revalidado de ADR-0002 (77e1323 → d72d6ac/3bb84a9/04fe631), 0003 (485249a → df72b1c), 0005 (39f0952 → 0e2b85b): ediciones después de aceptación sin reemplazo. El cierre reconoce que el hallazgo persiste: [docs/evidencias/evidencia-s9-2026-10-01.md:414–425](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L414-L425). No se penaliza por añadir ADR sucesores nuevos. |
| docs/ia.md al día para la semana | Cumple | Registro S9 actualizado y rechazo razonado: [docs/ia.md:482–506](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/ia.md#L482-L506). Para S10 aún no se acredita un registro específico del reto asignado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI backend y otros tres workflows del hash están success, pero backend-tests solo ejecuta Ruff/Gitleaks/pruebas: [.github/workflows/backend-tests.yml:61–78](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/.github/workflows/backend-tests.yml#L61-L78), [.github/workflows/backend-tests.yml:105–130](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/.github/workflows/backend-tests.yml#L105-L130). Falta scanner Sonar en CI; la documentación lo reconoce: [README.md:67–69](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L67-L69). Gate automático o badge no satisface los tres eslabones del contrato. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Checkout y CI sin hallazgos productivos observados. El barrido independiente amplio del historial no concluyó por interrupción de la herramienta; CI solo cubre el intervalo fijado en [.github/workflows/backend-tests.yml:70–78](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/.github/workflows/backend-tests.yml#L70-L78). El barrido histórico documentado distingue cinco falsos positivos: [docs/evidencias/evidencia-s9-2026-10-01.md:529–555](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L529-L555). Falta completar comprobación independiente del historial completo. |
| Contribución de todos los integrantes | No verificado | Historial agregado: 365 commits y cinco nombres de autor; dos firmas comparten dirección y se consolidan, sin publicar correos. [README.md:5–9](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L5-L9) enumera integrantes sin mapear todas las cuentas. La correspondencia previa no se da por probada por parecido de nombres; confirmar mapa explícito persona–cuenta. |

## Contribución por integrante

Actualización agregada del 2026-10-06: 365 commits; cinco nombres de autor, dos firmas consolidables por dirección idéntica. Correspondencia completa persona–cuenta pendiente; sin inferencias por semejanza de nombres.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits (HEAD) | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Nilver Garcia Pimentel | `nilver-garcia` / `Nnigarp` (misma cuenta, id 115980006) | 124+10+2 | — | — | Mayor volumen; ADR-0002 y reto S5 |
| Camilo Jose Martinez Berrio | `camilixo92` | 26 | — | — | Autor principal S1–S2; merges de PR #2, #3, #5 |
| Joshua Jose Tenorio Alvarez | `Carulla-sd` | 19 | — | — | Módulos de frontend |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Fallo: ¿qué ocurre con catálogo, health y datos si MySQL falla, y qué evidencia distingue recuperación de API de recreación de ambos contenedores?
- Costo: ¿qué límite de memoria, CPU o volumen haría inviable la solución actual y por qué la lectura en lote fue preferible a aumentar recursos?
- Medición: si el navegador público sigue sobre dos segundos mientras loopback cumple, ¿qué medirían y cambiarían primero?
