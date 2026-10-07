# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | PideUtb |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Daniela Sofia Arrieta Guardo · Santiago Jose Cuesta Maza · Ruddy Rodriguez Romero — cuentas observadas: `daniarriet`, `Santiago Cuesta`/`Santiago-C0` (mismo correo, misma persona), `ruddy2000utb-droid`; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://pideutb-api.onrender.com · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `7e973faf7047e40137762befbc019f4736a813e6` · 2026-10-04T12:47:55-05:00 | 8/10 | 4.2 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `7e973faf7047e40137762befbc019f4736a813e6` · 2026-10-04T12:47:55-05:00 | 1/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `48cfbe3` · 2026-08-08T15:12:35-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `9b5f214` · 2026-08-16T12:47:26-05:00 | 9/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `b5f0310` · 2026-08-23T19:42:42-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `1636f20` (2026-08-30T22:17:18-05:00) | 1/10 | 1.4 | si |
| 5 | CORTE1 | `bbefae8` (2026-09-08T10:37:21-05:00) | 9/12 | 4.0 | si |
| 6 | S6 | `006edfe` (2026-09-13T16:37:23-05:00) | 7/8 | 4.5 (prelim.) | si |
| 7 | S7 | `3d78106` (2026-09-20T22:24:21-05:00) | 10/10 | 5.0 | si |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `a94bf4e` en `master` (2026-09-27T20:30:08-05:00) | 9/10 | 4.6 (2 filas de despliegue pendientes) | sí |
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
| Rotar/configurar de forma segura el secreto de la pasarela y acreditar que el despliegue usa el fail-closed; retirar el valor histórico de ejemplos/comentarios sin reproducirlo. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Resolver autenticación/roles del panel y verificación del canje; la máquina de estados no autoriza al establecimiento. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar fila ESC-03 con ADR-0005, código, prueba y medición navegables; reconciliar C4 con autenticación futura. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Integrar cobertura/Quality Gate en Sonar y aportar run del hash actual. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Confirmar escenario operativo S10, disponibilidad actual y atribución de contribuciones. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| El fallback ejecutable del secreto se retiró y falta de configuración rechaza firma; solo cierre de código, no de rotación/producción. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La auditoría de modularidad ya cubre archivos transversales; salud consume servicio, no repositorio ajeno. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Ya existe ADR del panel y de no incorporación generativa. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La cobertura se mide con umbral 85 % en el job de pruebas; se retiró la insignia que anunciaba una medida inexistente. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La migración PostgreSQL y el panel antes tardíos están dentro de este delta; no se altera retrospectivamente S8. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Estructura fuera de convención: `arc42.md` en raíz, C4 dentro de arc42, sin `docs/c4/`, ficha en PDF | S1 | sí (post-cierre movieron `arc42.md` a `docs/` y crearon `docs/C4/`, pero en mayúsculas y sin fusionar en `docs/arc42/`) | Mover arc42 y C4 a `docs/arc42/` y `docs/c4/` en minúsculas |
| `docs/ia.md` sin registro de lo rechazado | S1 | sí | Incluir la columna de rechazos con motivo en cada uso |
| Ruddy Rodriguez Romero sin aparición en el historial | S1 | no (resuelto en S4) | En HEAD aparece `ruddy2000utb-droid`; mantener contribución distribuida |
| Sección 4 sin tácticas por escenario; matriz comparativa sin filas por escenario | S3 | sí | Ligar estrategia y matriz a ESC-01/02/03 del árbol de utilidad |
| `docs/aspectos.md` sin enlace al ADR ni tabla de 8 columnas | S3 | sí (confirmado en HEAD post-cierre: sigue siendo narrativo por atributo, no tabla de 8 columnas) | Completar la tabla de trazabilidad y enlazar el ADR desde el aspecto y el escenario |
| Sin workflow ni evidencia de prueba en verde | S3 | sí (confirmado post-cierre: sigue sin `.github/workflows/`) | Añadir `.github/workflows/` con `pytest` y aportar el run |
| C4 niveles 1 y 2 en docs/c4/ | S4 | sí (creado post-cierre pero como `docs/C4/`, mayúsculas) | Renombrar a minúsculas |
| Glosario (sección 12) y secciones 1-6, 9, 10 de arc42 verificables | S4 | si | |
| Tabla de aspectos con columnas ID, C4, ADR, Código | S4 | si | |
| Trazabilidad del ADR a commit y pruebas | S4 | si | |
| docs/ia.md con lo rechazado | S4 | si | |
| CI con pruebas en verde | S4 | si | |
| Eliminar .venv-1 del repositorio | S4 | sí (sigue versionado en HEAD) | Añadir `.gitignore` y sacarlo del historial |
| Etiqueta `corte-1` ausente; HEAD sigue en S4 | S5 | sí (confirmado post-cierre: nunca se creó, tampoco tras seguir trabajando el 07/09 después del cierre) | Crear la etiqueta sobre el commit real del corte antes del cierre — no se hizo |
| Documentar restricción y diagnóstico | S5 | si | |
| Crear ADR del reto | S5 | si | |
| Completar docs/arc42/ y docs/c4/ | S5 | si | |
| Reestructurar docs/aspectos.md a 8 columnas | S5 | si | |
| Evidencia de CI y medición | S5 | si | |
| Entrada de IA del corte en docs/ia.md | S5 | si | |
| correcciones.md añadido en commit f9a3304 (2026-09-07T16:12:06-05:00), posterior al cierre | S5 | no (resuelto tarde) | — |
| docs/ia.md añadido en commit f9a3304 (2026-09-07T16:12:06-05:00), posterior al cierre | S5 | no (resuelto tarde) | — |
| CI configurado en commits c665562 y a5fe113 (2026-09-07), posterior al cierre | S5 | no (resuelto tarde) | — |
| correcciones.md no estaba en el estado calificado | S5 | si | |
| docs/ia.md no estaba en el estado calificado | S5 | si | |
| Tabla de aspectos incompleta en el estado calificado | S5 | si | |
| Sin evidencia de CI en el estado calificado | S5 | si | |
| Transcribir la restricción asignada en docs/restriccion-s5.md | S5 | si | |
| Crear ADR 0002 del reto | S5 | si | |
| Implementar el cambio que responde a la restricción y contrastarlo con el umbral | S5 | si | |
| Renombrar/mover el archivo de correcciones a correcciones.md en la raíz | S5 | si | |
| Equilibrar la contribución entre integrantes | S5 | si | |
| Contrato OpenAPI/AsyncAPI o proto versionado, con rutas, esquemas y version declarada | S7 | si | |
| Prueba de contrato invocada desde el workflow y evidencia de fallo ante cambio incompatible | S7 | si | |
| ADR de estrategia de integracion sincrona o asincrona con alternativa descartada | S7 | si | |
| Evidencia publica de SonarCloud: configuracion del scanner, run del hash y URL del analisis con Quality Gate | S7 | si | |
| Modulo pagos vacio: ESC-04 y ESC-05 sin codigo ni pruebas | S7 | si | |
| Deuda planificada V-07, V-08 y V-09 y prueba de carga de ESC-02 | S7 | si | |
| Evidencia pública de SonarCloud con Quality Gate para el hash revisado | S6 | si | |
| Títulos de ADR que enuncien la decisión | S6 | si | |
| Contenido verificable de arc42 §8 | S6 | si | |
| Diff contra hash de S5 para confirmar el reajuste de límites | S6 | si | |
| Correspondencia contrato–código (routers) | S7 | si | |
| Ejecución y run en rojo de la prueba de contrato | S7 | si | |
| arc42 §6 y C4 nivel 2 etiquetado | S7 | si | |
| URL pública de SonarCloud con Quality Gate | S7 | si | |
| Contenido de docs/aspectos.md | S7 | si | |
| Recuperar el despliegue público y completar IaC, observabilidad y costos. | S8 | no (resuelto en el estado calificado: despliegue en Render, `infra/` con Terraform, logs JSON y `/metricas` ligada a ESC-02) | — |
| Recoger el límite de costo y la restricción de tarjeta en arc42 §2. | S8 | sí (la sección 2 declara presupuesto cero y plan gratuito, pero la condición de tarjeta solo está en `docs/comparacion-despliegue.md` y ADR-0004) | Añadir ambas al apartado de restricciones |
| Registro de IA de la semana dentro del periodo. | S8 | sí (la entrada de S8 se subió el 28/09, después del cierre) | Registrar el uso de IA antes del cierre |
| No editar ADR aceptados sin declarar reemplazo. | S8 | sí (títulos de ADR-0001 y ADR-0002 reescritos el 20/09) | Escribir un ADR nuevo o declarar el reemplazo |
| Acreditar el run de CI del hash calificado y el Quality Gate público. | S6 | sí (parcial: el run de CI de `a94bf4e` ya quedó citado en S8; sigue pendiente el Quality Gate público) | Aportar la URL pública de análisis con su Quality Gate |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_PideUtb; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes; [docs/aspectos.md:8-13](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/aspectos.md#L8-L13) enlaza arc42, ADR, C4 e IA existente en el árbol. |
| Estado calificado identificable | Cumple | origin/master 7e973faf7047e40137762befbc019f4736a813e6; último commit anterior al cierre, fecha en cabecera. |
| Nombres de ADR según la convención | Cumple | Lista docs/adr 0001–0006 conforme a NNNN-titulo-en-kebab-case; [docs/adr/0005-maquina-de-estados-del-mostrador.md:1-5](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L1-L5) y [docs/adr/0006-componente-generativo.md:1-5](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0006-componente-generativo.md#L1-L5). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0001-estilo-arquitectonico.md:5-19](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0001-estilo-arquitectonico.md#L5-L19) y [docs/adr/0002-propiedad-datos-establecimiento.md:5-23](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0002-propiedad-datos-establecimiento.md#L5-L23) ahora explican reescrituras de título; el historial también conserva edición [1b4f0f64](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/1b4f0f64bdb9e51f7e3ded11b7ec336e9a30240d). Reconocimiento histórico útil, pero no reemplazo formal ni ausencia de reescritura. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:259-319](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/ia.md#L259-L319) incorpora S9 con criterio técnico. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/ci.yml:226-277](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/.github/workflows/ci.yml#L226-L277) omite scanner/gate sin token; [docs/evidencia-s9.md:255-290](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L255-L290) declara que cobertura no ingresa al Quality Gate. Cobertura mínima 85 % sí se agregó al job de pruebas, [.github/workflows/ci.yml:109-128](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/.github/workflows/ci.yml#L109-L128). Única consulta PR del hash vacía; no se confunde éxito global con scanner ejecutado. |
| Sin credenciales en el repositorio ni en el historial | No cumple | Incidente documentado por el equipo en [docs/evidencia-s9.md:196-215](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L196-L215): un valor por defecto publicado se utilizaba para firmas de pago por falta de variable en el despliegue. El valor histórico sigue escrito en documentación/comentario del archivo backend/app/pagos/service.py (sin reproducirlo aquí). [backend/app/pagos/service.py:69-114](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/pagos/service.py#L69-L114) ya falla cerrado al faltar secreto. No se verificó rotación/configuración productiva ni que el despliegue ejecute la corrección. Retirar referencias al valor, rotarlo en los destinos donde se usó y acreditar configuración/despliegue seguro. Esto no afirma que sea explotable actualmente ni se probó pago alguno. El incidente histórico se conserva como no conformidad aunque se haya retirado el fallback ejecutable; barrido general pendiente no lo invalida. |
| Contribución de todos los integrantes | No verificado | Historial con firmas múltiples y archivo .mailmap; solo se consolidan identidades cuando la correspondencia está acreditada. La contribución por los tres integrantes debe confirmarse sin inferir personas de nombres/cuentas ni publicar correos. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Historial de la punta: 103 commits y 5 firmas de autor distintas (firmas, no personas). Historial con firmas múltiples y archivo .mailmap; solo se consolidan identidades cuando la correspondencia está acreditada. La contribución por los tres integrantes debe confirmarse sin inferir personas de nombres/cuentas ni publicar correos.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits (HEAD) | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Daniela Sofia Arrieta Guardo | ¿`daniarriet`? (confirmar) | 21 | — | — | Autora de casi toda la actividad post-cierre del 07/09 |
| Santiago Jose Cuesta Maza | `Santiago Cuesta` / `Santiago-C0` (mismo correo) | 10 | — | — | Entrega S3 completa (ADR, esqueleto, README) |
| Ruddy Rodriguez Romero | `ruddy2000utb-droid` | 2 | — | — | Apareció desde S3/S4 |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Fallo: si falta la variable de la pasarela, ¿cómo se detecta que pagos legítimos se rechazan y cómo prueban el cierre seguro sin usar ni mostrar el valor expuesto?
- Costo: ¿cómo cambian costo y tiempo de arranque al mantener pool PostgreSQL, agregar roles y sostener el pico de pedidos?
- Medición: al incluir red y una persona real en ESC-03, ¿qué resultado los haría cambiar la interfaz o las transiciones y cómo aislarían ese efecto?
