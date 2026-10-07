# Semana 10 · Segundo corte · PideUtb

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_PideUtb |
| Estado revisado | `7e973faf7047e40137762befbc019f4736a813e6` en `origin/master` (2026-10-04T12:47:55-05:00) |
| Rama remota principal | `origin/master` |
| Observación | 2026-10-06T21:31:50.478484+00:00 |
| Punta revisada para S10 | `7e973faf7047e40137762befbc019f4736a813e6` (2026-10-04T12:47:55-05:00) |
| S9 congelado, solo como línea base | `7e973faf7047e40137762befbc019f4736a813e6` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** Se encontró ESC-03 del panel y otros escenarios de calidad, pero no una fuente que identifique el reto operativo asignado al equipo para S10. Se documenta lo verificable sin presumir esa equivalencia. Fuente o búsqueda: [docs/evidencia-s9.md:11-26](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L11-L26) y [docs/adr/0005-maquina-de-estados-del-mostrador.md:21-30](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L21-L30); búsqueda en README, ADR, arc42 y evidencias. La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `bbefae828185e9baa4df757ea073cbe84539cd3f`: el delta hasta esta punta modifica 109 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master 7e973faf7047e40137762befbc019f4736a813e6; revisión preliminar anterior al cierre futuro. |
| Despliegue accesible en el momento de la revisión | No verificado | URL declarada: https://pideutb-api.onrender.com/health, [README.md:13-15](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/README.md#L13-L15). Intento iniciado 2026-10-06T21:27:56Z: la herramienta canceló la sesión antes de devolver un resultado HTTP; no es evidencia de caída del servicio. No se probó flujo ni pago. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Se encontró ESC-03 del panel y otros escenarios de calidad, pero no una fuente que identifique el reto operativo asignado al equipo para S10. Se documenta lo verificable sin presumir esa equivalencia. [docs/evidencia-s9.md:11-26](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L11-L26) y [docs/adr/0005-maquina-de-estados-del-mostrador.md:21-30](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L21-L30); búsqueda en README, ADR, arc42 y evidencias |
| Línea base medida y reproducible | No verificado | [docs/evidencia-s9.md:57-78](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L57-L78) mide porción local programática sin usuario/red; no es línea base del reto S10 confirmado sobre despliegue. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0005-maquina-de-estados-del-mostrador.md:32-72](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L32-L72) acredita alternativas y decisión del panel; falta correspondencia con asignación S10 y su montaje operativo. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [backend/app/pedidos/service.py:200-226](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/pedidos/service.py#L200-L226) prueba implementación estática; el delta desde S5 incluye PostgreSQL, contratos y panel, pero no se presume respuesta a reto no identificado. |
| Resultado contrastado con el umbral | No verificado | [docs/evidencia-s9.md:68-78](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L68-L78) contrasta tres interacciones/tiempo de sistema; falta resultado del reto asignado en entorno desplegado. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Pipeline y cobertura exigida en [.github/workflows/ci.yml:109-128](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/.github/workflows/ci.yml#L109-L128); health implementado en [backend/app/salud.py:35-55](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/salud.py#L35-L55). La operación actual no se comprobó por cancelación y falta confirmar corrección/configuración de secreto en despliegue. Métrica del reto asignado pendiente. |
| Secretos protegidos | No cumple | Incidente documentado por el equipo en [docs/evidencia-s9.md:196-215](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L196-L215): un valor por defecto publicado se utilizaba para firmas de pago por falta de variable en el despliegue. El valor histórico sigue escrito en documentación/comentario del archivo backend/app/pagos/service.py (sin reproducirlo aquí). [backend/app/pagos/service.py:69-114](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/pagos/service.py#L69-L114) ya falla cerrado al faltar secreto. No se verificó rotación/configuración productiva ni que el despliegue ejecute la corrección. Retirar referencias al valor, rotarlo en los destinos donde se usó y acreditar configuración/despliegue seguro. Esto no afirma que sea explotable actualmente ni se probó pago alguno. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/c4/nivel2-contenedores.md:24-34](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/c4/nivel2-contenedores.md#L24-L34) representa validación de identidad por Supabase, mientras [docs/adr/0005-maquina-de-estados-del-mostrador.md:114-120](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L114-L120) reconoce panel sin autenticar. [docs/aspectos.md:21-30](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/aspectos.md#L21-L30) no enlaza ADR-0005/medición y conserva estado S7. Alinear lo implementado y lo futuro. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | Las notas históricas de títulos [docs/adr/0001-estilo-arquitectonico.md:7-19](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0001-estilo-arquitectonico.md#L7-L19) explican ediciones, pero no confirman/reemplazan una decisión por experimento del reto S10 identificado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Pendiente de docente sobre despliegue y pipeline en vivo; no se puntúa desde el repositorio. |

Recuento descriptivo: 1 Cumple, 2 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Asignación S10 no confirmada; ESC-03 se conserva como antecedente. |
| Decisión e implementación | No verificado | Pendiente | Decisión/código del panel presentes, pertinencia y experimento del reto pendientes. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Incidente de secreto y corrección estática documentados; operación/configuración/rotación actuales no verificadas. No se presume vulnerabilidad activa ni ausencia de riesgo. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Desalineaciones C4/aspectos persisten; falta evolución ligada al reto confirmado. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | La fija el docente en sesión. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
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

## Estado global del proyecto (overall)

Punta observada de `origin/master`: `7e973faf7047e40137762befbc019f4736a813e6` (2026-10-04T12:47:55-05:00). Hay 0 commits posteriores al estado congelado S9. Punta igual al cierre S9. La auditoría encontró un incidente de secreto real y el código ahora falla en cerrado; falta evidencia de rotación y despliegue seguro, sin afirmar explotación vigente. La cobertura tiene umbral en CI, pero sigue fuera de SonarCloud. El panel continúa sin autenticar, declarado y no oculto.

- Rotar/configurar de forma segura el secreto de la pasarela y acreditar que el despliegue usa el fail-closed; retirar el valor histórico de ejemplos/comentarios sin reproducirlo.
- Resolver autenticación/roles del panel y verificación del canje; la máquina de estados no autoriza al establecimiento.
- Completar fila ESC-03 con ADR-0005, código, prueba y medición navegables; reconciliar C4 con autenticación futura.
- Integrar cobertura/Quality Gate en Sonar y aportar run del hash actual.
- Confirmar escenario operativo S10, disponibilidad actual y atribución de contribuciones.

### Hallazgos anteriores cerrados o delimitados

- El fallback ejecutable del secreto se retiró y falta de configuración rechaza firma; solo cierre de código, no de rotación/producción.
- La auditoría de modularidad ya cubre archivos transversales; salud consume servicio, no repositorio ajeno.
- Ya existe ADR del panel y de no incorporación generativa.
- La cobertura se mide con umbral 85 % en el job de pruebas; se retiró la insignia que anunciaba una medida inexistente.
- La migración PostgreSQL y el panel antes tardíos están dentro de este delta; no se altera retrospectivamente S8.

## Preparación de la sustentación

1. Fallo: si falta la variable de la pasarela, ¿cómo se detecta que pagos legítimos se rechazan y cómo prueban el cierre seguro sin usar ni mostrar el valor expuesto?
2. Costo: ¿cómo cambian costo y tiempo de arranque al mantener pool PostgreSQL, agregar roles y sostener el pico de pedidos?
3. Medición: al incluir red y una persona real en ESC-03, ¿qué resultado los haría cambiar la interfaz o las transiciones y cómo aislarían ese efecto?

## Próximos pasos

Antes de la defensa, acrediten la corrección y configuración segura del secreto en el despliegue, y resuelvan o delimiten el panel sin autenticación. Confirmen el escenario operativo asignado y midan su línea base y respuesta en el entorno real. La disponibilidad actual no pudo comprobarse por una cancelación de la herramienta; eso no demuestra que el servicio esté caído.
