# Semana 10 · Segundo corte · Calificación automática (QuantIA)

> **Revisión preliminar**, realizada el 6 de octubre de 2026. El cierre de S10 todavía no ha ocurrido. No constituye nota aplicada ni evaluación de sustentación.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica |
| Estado revisado | `72011933ff2238eaec697f565572fec6872a3cbc` en `origin/master` (2026-10-04T22:36:29-05:00) |
| Rama remota principal | `origin/master` |
| Base S8 | `1f8f76dc169da96e4f668ff6894e7d51ce5be252` |
| Estado preliminar S10 / HEAD | `72011933ff2238eaec697f565572fec6872a3cbc` · 2026-10-04T22:36:29-05:00 |
| Cierre previsto S10 | 2026-10-12T05:00:00Z |
| Observación | 2026-10-06T21:19:18Z |

## Escenario operativo asignado y alcance

**No verificado.** EC-08 es un escenario creado para RF-11/A-06 en S9. No se encontró una referencia oficial que lo identifique como escenario operativo asignado para S10; tampoco EC-07 previo demuestra esa asignación. [README.md:15–34](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/README.md#L15-L34), [docs/evidencia/evaluacion-distractores.md:1–20](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/evidencia/evaluacion-distractores.md#L1-L20) y ADR-0013 [docs/adr/0013-consumir-groq-detras-de-un-puerto-y-degradar-sin-bloquear-la-autoria.md:148–168](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/adr/0013-consumir-groq-detras-de-un-puerto-y-degradar-sin-bloquear-la-autoria.md#L148-L168).

Se revisaron README, ADR, arc42 y evidencias/experimentos. Un escenario de calidad elegido por el equipo no demuestra cuál le asignó el docente. Antes de valorar la respuesta del reto hay que disponer del enunciado o una referencia oficial equipo–escenario. Las evidencias S6–S9 se describen como línea base, sin recalificarlas por existir.

**PDF excluido por instrucción docente:** se omite su fila; no se leyó ningún PDF ni se cuenta como incumplimiento. La matriz conserva 12 comprobaciones. Se realizaron únicamente consultas HTTP de lectura indicadas abajo. No se ejecutó código del equipo ni se probó el flujo principal.

## Matriz de comprobación S10

| Criterio | Evidencia técnica esperada | Estado preliminar | Observaciones y evidencia |
|---|---|---|---|
| Estado de S10 identificable y anterior al cierre | Rama principal, hash y fecha; estado preliminar | Cumple | HEAD 72011933ff2238eaec697f565572fec6872a3cbc, 2026-10-04T22:36:29-05:00. Es preliminar anterior al cierre futuro S10. |
| Despliegue accesible en el momento de la revisión | Respuesta HTTP, tiempo y hora | Cumple | Consulta de lectura a https://quantia-utb.onrender.com iniciada 2026-10-06T21:19:18Z: HTTP 200 en 4,564212 s; https://quantia-utb-api.onrender.com/health iniciada 21:19:22Z: HTTP 200 en 8,116839 s. URLs en [README.md:78–79](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/README.md#L78-L79). Sin probar carga, generación ni otras acciones; no se deduce versión desplegada del 200. |
| Hipótesis, montaje, variables y umbral declarados | Caracterización del escenario operativo asignado | No verificado | EC-08 está caracterizado como porción S9; falta consigna oficial S10 y su correspondencia: [docs/evidencia/evaluacion-distractores.md:11–28](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/evidencia/evaluacion-distractores.md#L11-L28). |
| Línea base medida y reproducible | Herramienta, carga y procedimiento del escenario asignado | No verificado | Conjunto reproducible y resultados EC-08 existen, pero una evaluación final no demuestra por sí sola línea base del reto S10 desconocido: [docs/evidencia/evaluacion-distractores.md:11–20](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/evidencia/evaluacion-distractores.md#L11-L20). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | ADR y respuesta al escenario asignado | No verificado | ADR-0013 fundamenta integración generativa, contingencia y costo, como entrega S9. Falta identificar respuesta a la asignación S10. |
| Respuesta implementada o configurada sobre el MVP | Cambio trazable correspondiente al reto | No verificado | RF-11 implementado en API; no se probó el flujo desplegado ni su correspondencia con reto S10. [docs/aspectos.md:81–84](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/aspectos.md#L81-L84) reconoce pantalla pendiente. |
| Resultado contrastado con el umbral | Medición final comparable con línea base | No verificado | Resultado EC-08 contrastado y verificable documentalmente; no se transforma la medición S9 en calificación de reto S10 sin asignación. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | Run y observabilidad del escenario asignado | No verificado | CI success y salud 200; eventos/tiempos de EC-08 documentados en [docs/adr/0013-consumir-groq-detras-de-un-puerto-y-degradar-sin-bloquear-la-autoria.md:119–122](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/adr/0013-consumir-groq-detras-de-un-puerto-y-degradar-sin-bloquear-la-autoria.md#L119-L122). Pendiente métrica del escenario asignado, scanner y demostración del bloqueo de integración. |
| Secretos protegidos | Barrido del contrato | No verificado | Barrido de seguridad independiente bloqueado por herramienta; no se infiere secreto ni limpieza total. |
| C4, arc42, ADR y contratos correspondientes al MVP | Consistencia documental y trazabilidad | Cumple | C4 distingue relaciones construidas/previstas y Groq externo, protocolo/costo: [docs/c4/doc-c4.md:231–262](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/c4/doc-c4.md#L231-L262); A-06 enlaza ADR, contrato y evidencia: [docs/aspectos.md:28–40](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/aspectos.md#L28-L40). Se comprueba coherencia de la porción disponible, sin asignar una segunda nota por S9. |
| Decisión anterior confirmada o reemplazada con evidencia | Relación explícita entre medición y decisión | No verificado | ADR-0013 confirma aislamiento de autoría e introduce criterio medido para futura equivalencia: [docs/adr/0013-consumir-groq-detras-de-un-puerto-y-degradar-sin-bloquear-la-autoria.md:64–90](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/adr/0013-consumir-groq-detras-de-un-puerto-y-degradar-sin-bloquear-la-autoria.md#L64-L90). Falta confirmar que responde al reto S10. |
| Sustentación del reto sobre el entorno desplegado | Sesión y pipeline en vivo; lo resuelve el docente | No verificado | Sustentación en despliegue y pipeline en vivo pendiente del docente. |

## Rúbrica del segundo corte · cinco criterios

Escala de la ficha: **0,00 · 0,60 · 0,80 · 1,00 por criterio**. No se aplica la fórmula semanal. Una comprobación pendiente conserva puntaje pendiente; no se convierte automáticamente en cero.

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Sin escenario operativo oficialmente asignado, EC-08 de S9 no permite determinar nivel de S10. |
| Decisión e implementación | No verificado | Pendiente | Código/ADR/evaluación de S9 verificados; pendiente vinculación con consigna y flujo principal desplegado. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Salud y CI verificados; seguridad pendiente por bloqueo revisor, y riesgo documentado de consumir cuota sin autenticación. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Documentación técnica actualizada y evidencia completa para RF-11; falta cambio/confirmación específico del reto S10. |
| Sustentación del reto | Pendiente del docente | Pendiente | Pendiente de sustentación sobre el despliegue y ejecución del pipeline en vivo; no se infiere desde el repositorio. |

**Total: pendiente, no calculado.** La correspondencia con la asignación y la sustentación impiden proponer un total responsable.

## Matriz transversal · CONTRATO §11

| Criterio transversal | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon git público ISCOUTB/AS_202620_Sistema-de-calificacion-automatica; rama master y nombre conforme. |
| Estructura mínima presente | Cumple | README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md presentes; la fila [docs/aspectos.md:40](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/aspectos.md#L40) enlaza la porción. |
| Estado calificado identificable | Cumple | 72011933ff2238eaec697f565572fec6872a3cbc, 2026-10-04T22:36:29-05:00, último master anterior al cierre; HEAD coincide. |
| Nombres de ADR según la convención | Cumple | Inventario docs/adr: 0001–0014, nombres conformes NNNN-kebab-case.md. [docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md:1–6](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md#L1-L6). |
| ADR aceptados no reescritos | No cumple | Historial de ADR-0007 confirma creación c0f976d y edición 1c8bcfb el 26-sep tras aceptación. ADR-0014 explica cuatro cambios de enlace y conserva la decisión, pero no reemplaza el ADR ni borra la edición: [docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md:14–26](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md#L14-L26), [docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md:64–68](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/adr/0014-dejar-constancia-del-ajuste-de-enlaces-en-adr-0007.md#L64-L68). Su regla local más flexible no modifica el contrato del curso; queda aclarada la naturaleza del cambio, no cumplimiento retroactivo. |
| docs/ia.md al día para la semana | Cumple | Entrada S9 actualizada hasta el commit final; acepta, corrige y rechaza con motivo técnico: [docs/ia.md:215–232](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/ia.md#L215-L232). S10 requiere registro de su trabajo cuando se identifique el reto. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [CI del hash final success](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/37260121474). [.github/workflows/ci.yml:20–60](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/.github/workflows/ci.yml#L20-L60) instala y prueba backend/frontend sin invocación Sonar; enlace genérico en [README.md:67–68](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/README.md#L67-L68) no acredita scanner ni Quality Gate del hash. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El barrido independiente de snapshot e historial no concluyó por interrupción de herramienta. La revisión documental [docs/evidencia/auditoria-s9.md:130–146](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/docs/evidencia/auditoria-s9.md#L130-L146) explica las coincidencias de patrones citados, pero no sustituye la verificación pendiente. |
| Contribución de todos los integrantes | Cumple | README mapea explícitamente las cuatro cuentas a integrantes: [README.md:9–13](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/72011933ff2238eaec697f565572fec6872a3cbc/README.md#L9-L13). Shortlog del hash observado: cuatro firmas con 91, 44, 27 y 23 commits (185 total); sin correos publicados. Esta evidencia acredita presencia, no igualdad de esfuerzo ni comprensión individual. |

## Estado global (overall)

HEAD: `72011933ff2238eaec697f565572fec6872a3cbc` · 2026-10-04T22:36:29-05:00. La punta coincide con S9 y conserva CI success. RF-11 ya dejó de ser una capacidad solo prevista y tiene evaluación real del proveedor. La documentación reconoce ruta pública sin autenticación, riesgo de consumo de cuota, límite de equivalencias matemáticas y frontend de RF-11 pendiente; no deben presentarse como resueltos por tener pruebas verdes. Sonar y reglas históricas ADR siguen abiertos. Salud y frontend respondieron 200; no se ejecutó el flujo principal.

Recuento descriptivo: **3 Cumple, 0 No cumple, 9 No verificado, sobre 12.** No es una nota ni sustituye la rúbrica.

## Próximos pasos

Antes de evaluar el segundo corte identifiquen la asignación operativa oficial. La evaluación de distractores es una buena base de S9, pero no prueba por sí sola una línea base y respuesta al reto S10. Frontend y salud responden; falta demostrar el flujo principal, seguridad de acceso/cuota, métrica del reto y pipeline en vivo. La sustentación queda pendiente.

## Tres preguntas para la sustentación

1. Fallo: si el proveedor devuelve 429, JSON inválido o tarda más del límite, ¿cómo mantienen disponible la calificación y comprueban esa independencia en el despliegue?
2. Costo: con los tokens medidos por solicitud, ¿cuántos exámenes agotan primero la cuota y cómo impedirán que una ruta pública la consuma sin control?
3. Medición: al observar 44 de 60 propuestas válidas y errores de etiquetado, ¿qué cambiarían en el conjunto, la revisión o la implementación antes de ampliar el uso?

## Delta arquitectónico desde el primer corte

Base publicada de S5: `8b0d00b62d2a03dfe509edae578261748a842294`; comparación git contra HEAD `72011933ff2238eaec697f565572fec6872a3cbc`: 65 rutas cambiadas, de ellas 10 en ADR/arc42/C4 (sin leer PDF). Se inspeccionaron las decisiones, contratos, código y evidencia citados en las filas. El delta sirve para examinar evolución y consistencia del MVP, no para recalificar las entregas S6–S9. La correspondencia con el escenario asignado S10 sigue pendiente.
