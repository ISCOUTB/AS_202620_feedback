# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | DinamikUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Luis Daniel Padilla Leottau (`Daniel-dev02`) · Gillianis Del Carmen Perez Revolledo (`gillianisperez-prog`) · Esteban Ramirez Rios (`Eramirezr`) · Juan Jose Vargas Perez (`JuanchisV`, firma también como «Juan José Vargas Pérez» con el mismo correo); ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://dinamikutb-api.onrender.com · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `2326dd7f9d4dda08ba557ea6602b0a7085c97bee` · 2026-10-04T21:47:16-05:00 | 5/10 | 3.0 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `5dc9acf9335fec70e274a2e5c494b3805b0e9646` · 2026-10-05T22:06:45-05:00 | 3/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 8 | S8 | `287c65d` (2026-09-27T23:57:31-05:00) | 10/10 | 5.0 (prop. prov.; 2 filas de despliegue diferidas) | sí |
| 7 | S7 | `5e6fa73` (2026-09-20T23:57:27-05:00) | 10/10 | 5.0 | si |
| 6 | S6 | `265e652` (2026-09-13T23:29:49-05:00) | 0/8 | 1.0 | si |
| 5 | CORTE1 | `72bfc7e` (2026-09-07T22:28:37-05:00) | 8/12 | 3.7 | sí (actualizada) |
| 4 | S4 | `8558156` (2026-08-30T23:52:24-05:00) | 7/10 | 3.8 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `769f970` · 2026-08-09T21:24:49-05:00 | 7/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `58734e1c` · 2026-08-16T23:33:53-05:00 | 9/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `fe52ab594` · 2026-08-23T23:20:33-05:00 | 5/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Aportar escenario S10 asignado, línea base y experimento reproducible sobre el MVP. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Corregir CI HEAD y adjuntar resultados de las pruebas ampliadas; no declarar 20/20 solo por contarlas. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Convertir rutas de código/pruebas de A-01 en enlaces y verificar cadena completa con medición. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Terminar controles de identidad y autorización antes de cargar información real; mantener datos ficticios mientras tanto. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Comprobar Quality Gate público y fijar fecha real de vencimiento/renovación de la base Render. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Se añade auditoría S9 de propiedad de datos con comando y localización; [docs/evidencia-s9.md:40–51](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/evidencia-s9.md#L40-L51). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Se incorporan ADR de verificación de artefactos y no incorporación generativa; [docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md:51–69](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md#L51-L69), [docs/adr/0009-no-incorporacion-componente-generativo.md:52–68](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0009-no-incorporacion-componente-generativo.md#L52-L68). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Después del cierre se incorpora rechazo explícito de hash inventado al registro de IA; [docs/ia.md:14–16](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/ia.md#L14-L16). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Ficha del problema entregada en PDF, no en Markdown | S1 | sí | Ver feedback S1/S2 |
| Solo una tensión de calidad declarada (se pedían dos) | S1 | sí | Ver feedback S1/S2 |
| Trabajo del periodo concentrado en un integrante | S2 | sí (en S3, JuanchisV firma 21 de 46 commits) | Ver feedback S1/S2 y S3 |
| Esteban sin commits en el periodo (S1; reaparece en S3) | S1 | cerrado en S3 (2 commits: `2c78be9`, `fe52ab5`) | Ver feedback S3 |
| Matriz de estilos sin referencia a los escenarios del árbol de utilidad | S3 | sí | Ver feedback S3 |
| `docs/aspectos.md` con la columna ADR en «Pendiente» aun existiendo el ADR 0001 (la tabla de 8 columnas y los enlaces a escenarios ya llegaron) | S3 | sí (parcialmente cerrado: tabla y enlaces a escenarios OK; columna ADR sigue pendiente) | Ver feedback S3 |
| 4258407 Update start.bat (2026-08-31T00:07:55-05:00) | S4 | no (resuelto tarde) | — |
| d87a771 Merge pull request #8 (2026-08-31T00:11:21-05:00) | S4 | no (resuelto tarde) | — |
| 1308052 Update start.bat (2026-08-31T00:12:04-05:00) | S4 | no (resuelto tarde) | — |
| 3c16fba Update start.bat (2026-08-31T00:13:28-05:00) | S4 | no (resuelto tarde) | — |
| Enlazar ADR-0002 en sección 9 | S4 | si | |
| Añadir trazabilidad commit/PR y pruebas en ADR | S4 | si | |
| Evidencia de run de CI en verde | S4 | si | |
| Verificar fila de aspectos.md | S4 | si | |
| Verificar contenido de docs/ia.md | S4 | si | |
| Correcciones S1–S4 trazables y contrastadas | S5 | cerrado | `correcciones.md` relaciona cada hallazgo con rutas verificadas en el hash calificado. |
| Pipeline de CI en el estado calificado | S5 | cerrado | El run asociado a `72bfc7e` terminó en verde. |
| Trazabilidad consolidada de aspectos | S5 | sí | A-02 a A-08 tienen eslabones o columnas pendientes en `docs/aspectos.md`. |
| ADR 0001 reescrito después de su aceptación | S5 | sí | Documentar cambios posteriores como ADR nuevo, sin editar una decisión aceptada. |
| PDF exigido por el aula y sustentación | S5 | No verificado | Se comprueban en Moodle y en la sesión docente, no en el repositorio. |
| Confirmar mapa de contextos y tabla módulo-datos en 08-cross-cutting-concepts.md | S6 | si | |
| Verificar violaciones de propiedad de datos y plan de corrección | S6 | si | |
| Comparar C4 nivel 3 con el hash de S5 y posible ADR de reajuste | S6 | si | |
| Revisar docs/aspectos.md | S6 | si | |
| Evidenciar ejecución del pipeline con runs_ci | S6 | si | |
| Contrato OpenAPI versionado con rutas y esquemas | S7 | no (releído y conforme) | — |
| Prueba de contrato integrada al pipeline | S7 | no (releído y conforme) | — |
| Demostración de que la prueba de contrato falla ante cambio incompatible | S7 | no (releído y conforme) | — |
| ADR de estrategia de integración (síncrono vs asíncrono) | S7 | no (releído y conforme) | — |
| Etiquetado de protocolo y formato en el C4 nivel 2 | S7 | no (releído y conforme) | — |
| Contenido verificable de docs/aspectos.md y docs/ia.md | S7 | si (aspectos con celdas «Pendiente»; ia conforme) | — |
| Evidencia pública del análisis estático con Quality Gate | S7 | si | |
| YAML de ci.yml corregido en 31350f1 el mismo día del cierre, tras el experimento del contrato. | S7 | no (resuelto tarde) | — |
| Bloqueo de permisos de SonarCloud documentado como hallazgo en 1ffe3e2 y 5e6fa73 en vez de resolverse. | S7 | no (resuelto tarde) | — |
| Commit 8a5ae13 'Update ci.yml' posterior al cierre (2026-09-21T00:01:43-05:00). | S7 | no (resuelto tarde) | — |
| SonarCloud: run que invoque el scanner y URL pública del análisis con Quality Gate. | S7 | si | |
| Contenido de arc42 sección 6 y del C4 nivel 2 con protocolo y formato por flecha. | S7 | no (releído y conforme) | — |
| Historial git del contrato y confirmación de la versión de la API. | S7 | no (releído y conforme) | — |
| Contenido de docs/aspectos.md con sus ocho columnas navegables. | S7 | si | |
| Publicar URL del sistema accesible desde fuera de la red universitaria, con hora de comprobación. | S8 | sí (diferido: URL por Moodle) | |
| Health check consultable y su código de respuesta. | S8 | sí (diferido: URL por Moodle) | |
| Infraestructura como código versionada (Dockerfile/compose o IaC del proveedor). | S8 | no (resuelto: `render.yaml` y `deploy-pages.yml`) | |
| Logs estructurados y métrica consultable ligada a un escenario de calidad. | S8 | no (resuelto: JSON logging y `/metrics` ligado a Q-05) | |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita. | S8 | no (resuelto: `docs/costos.md`) | |
| arc42 §7 con una caja por pieza y §2 con límite de costo y restricción de tarjeta. | S8 | no (resuelto en el hash calificado) | |
| Un ADR por decisión de plataforma con alternativa descartada. | S8 | no (resuelto: ADR-0005/0006/0007) | |
| Pendiente desde S6: URL pública del análisis en SonarCloud con estado del Quality Gate. | S8 | no (resuelto: scanner en CI y Quality Gate `OK`) | |
| ADR-0005 y ADR-0006 editados tras su aceptación el 2026-09-27 | S8 | sí | Ver feedback S8 |
| Sin entrega S9: la punta (`d72a10a`) es el estado de S8 más un commit de README | S9 | sí | Ver feedback S9 |
| Sin artefactos de S9 (porción, cadena, ADR, prueba, medición, erosión, dependencias, componente generativo) | S9 | sí | Ver feedback S9 |
| `docs/ia.md` sin actualización en el periodo de S9 | S9 | sí | Ver feedback S9 |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público ISCOUTB/AS_202620_DinamikUTB, rama master; [README.md:1–5](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Las seis rutas mínimas están presentes; arc42 01–12 y C4 en fuentes PlantUML, [docs/aspectos.md:9–18](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/aspectos.md#L9-L18). |
| Estado calificado identificable | Cumple | Punta master 5dc9acf9335fec70e274a2e5c494b3805b0e9646 de 2026-10-05T22:06:45-05:00; preliminar anterior a cierre S10. |
| Nombres de ADR según la convención | Cumple | Los nueve ADR cumplen NNNN-kebab-case; [docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md:1–9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md#L1-L9), [docs/adr/0009-no-incorporacion-componente-generativo.md:1–9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0009-no-incorporacion-componente-generativo.md#L1-L9). |
| ADR aceptados no reescritos | No verificado | Hay ediciones históricas de ADR-0001/0002/0005/0006; falta terminar contraste independiente de las versiones aceptadas. No se presume cerrado el arrastre de inmutabilidad. |
| docs/ia.md al día para la semana | Cumple | La punta añade entrada específica de hash inventado, verificado y rechazado, junto al registro de trabajo S9; [docs/ia.md:14–16](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/ia.md#L14-L16), [docs/ia.md:39–39](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/ia.md#L39-L39). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI de HEAD concluye failure aunque Deploy frontend success. Configuración y scanner existen; no se acredita pipeline integral en verde ni Quality Gate de esta revisión; [.github/workflows/ci.yml:55–78](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/.github/workflows/ci.yml#L55-L78). |
| Sin credenciales en el repositorio ni en el historial | No verificado | Barrido del snapshot sin valores de credencial: solo secretos de Actions y permisos id-token. Sin .env versionado. Historial completo no certificado. |
| Contribución de todos los integrantes | No verificado | Siete firmas, 294 commits agregados en S9. Variantes de identidad no equivalen a siete personas; falta correspondencia verificable completa con los cuatro integrantes. Punta actual: 7 firmas y 299 commits agregados; no equivalen automáticamente a personas. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Siete firmas de autor, 294 commits en el estado S9. Identidades variantes requieren consolidación acreditada; no se deducen personas por parecido. En HEAD: 7 firmas y 299 commits agregados.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Juan Jose Vargas Perez | `JuanchisV` (+ firma «Juan José Vargas Pérez») | 21 (S3) | — | — | Autor del ADR y del esqueleto |
| Gillianis Del Carmen Perez Revolledo | `gillianisperez-prog` | 11 (S3) | — | — | Enlaces de escenarios en aspectos.md |
| Luis Daniel Padilla Leottau | `Daniel-dev02` (+ firma «LUIS DANIEL») | 12 (S3) | — | — | README y merges de ramas |
| Esteban Ramirez Rios | `Eramirezr` | 2 (S3) | — | — | Estructura del proyecto e ia.md; reapareció tras S1/S2 sin commits |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Qué sucede con Q-01 y /health si Render pierde PostgreSQL o expira la instancia, y cómo demostrarían recuperación sin datos reales?
- ¿Cuál es la fecha concreta de expiración de la base gratuita y qué opción conserva datos dentro del presupuesto?
- ¿Qué cambiarían en la estrategia de pruebas al descubrir que contar 20 casos no garantiza un run verde ni cubre autorización?
