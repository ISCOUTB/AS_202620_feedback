# Semana 10 · Segundo corte · Recobra

**Revisión preliminar abierta al cierre del 2026-10-12T05:00:00Z.** No reemplaza S9 definitiva ni aplica la fórmula semanal.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_Recobra |
| Rama principal remota | `master` |
| Estado revisado | `ebe6cca7a903bb333678bd20ba5327d8fcb127f7` en `origin/master` (2026-10-04T23:40:37-05:00) |
| Línea base S8 | `5c7f77b3da94ed019ade4b959c723444a2ee7c02` |
| Punta actual / S10 preliminar | `ebe6cca7a903bb333678bd20ba5327d8fcb127f7` · 2026-10-04T23:40:37-05:00 |
| Cierre S9 | 2026-10-05T05:00:00Z |
| Cierre eventual S10 | 2026-10-12T05:00:00Z |
| Revisión | 2026-10-06 (UTC) |

## Evolución desde S5 publicado

Base S5: `f7c1a6c7c4371f1e9df38ca268895544cca43c17`. El delta hasta la punta contiene 85 commits y 82 rutas modificadas (PDF excluidos). Añade integración/eventos, PostgreSQL, despliegue, observabilidad, contrato y búsqueda con filtros; C4 aún conserva partes del corte inicial. Se contrastaron código, documentación, ADR y contratos; este recorrido aporta contexto de evolución, no recalifica S6–S9 ni acredita por sí mismo respuesta al escenario asignado.

## Alcance y método

Se consultó la rama principal remota mediante git y se eligió su último commit anterior o igual al cierre S9; no se consultaron etiquetas. S10 es preliminar y usa la punta actual. Se comparó S9 con la línea base S8; no se vuelven a puntuar entregas anteriores por existir. No se ejecutó código, pruebas ni despliegues del equipo. Los registros de ejecución del repositorio se distinguen de la comprobación externa. Por exclusión docente no se abrieron PDFs ni se evaluó su presencia, contenido, extensión o ubicación.

La consulta general de Actions se verificó mediante GET /actions/runs (100 registros como máximo); se distinguen el hash, la rama y la conclusión de cada run. Un intento inicial filtrado a pull requests no se usó para decidir. No se consultaron jobs ni logs adicionales.

## Escenario operativo oficialmente asignado

**No verificado.** No se encontró la asignación oficial de un escenario operativo para este equipo en README, ADRs o experimentos. S1 (búsqueda: p95 ≤400 ms con 200 usuarios) es un escenario de calidad usado en S9; no acredita por sí mismo la asignación S10. [docs/medicion-busqueda.md:27–80](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/medicion-busqueda.md#L27-L80) No se sustituye la asignación por un escenario genérico de calidad, una práctica S8/S9 o una hipótesis del revisor.

## Despliegue observado

GET https://recobra-backend.onrender.com/health respondió HTTP 200 en 27,367536 s; comprobación terminada el 2026-10-06T21:16:24Z, cuerpo de salud con status=ok. Solo se consultó salud; no se probó flujo principal, carga ni persistencia. URL publicada en [README.md:88–96](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/README.md#L88-L96).

## Matriz de comprobación S10

Se omite expresamente la fila de PDF por exclusión docente. Quedan 12 filas; su recuento es diagnóstico y no es la fórmula de calificación.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta de origin/master ebe6cca7a903bb333678bd20ba5327d8fcb127f7 (2026-10-04T23:40:37-05:00), anterior al cierre futuro; provisional. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://recobra-backend.onrender.com/health respondió HTTP 200 en 27,367536 s; comprobación terminada el 2026-10-06T21:16:24Z, cuerpo de salud con status=ok. Solo se consultó salud; no se probó flujo principal, carga ni persistencia. URL publicada en [README.md:88–96](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/README.md#L88-L96). |
| Hipótesis, montaje, variables y umbral declarados | No verificado | No se encontró la asignación oficial de un escenario operativo para este equipo en README, ADRs o experimentos. S1 (búsqueda: p95 ≤400 ms con 200 usuarios) es un escenario de calidad usado en S9; no acredita por sí mismo la asignación S10. [docs/medicion-busqueda.md:27–80](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/medicion-busqueda.md#L27-L80) |
| Línea base medida y reproducible | No verificado | [docs/medicion-busqueda.md:27–80](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/medicion-busqueda.md#L27-L80). Son corridas de S9, no línea base identificada del reto oficialmente asignado. Se necesita asignación, hipótesis y un antes medido comparable. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md:11–94](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md#L11-L94). Decisión verificable de S9; relación con la asignación S10 pendiente. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [src/publicaciones/publicaciones.controller.ts:37–44](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/src/publicaciones/publicaciones.controller.ts#L37-L44). Búsqueda implementada; falta identificar qué cambio responde al reto S10 y su despliegue. |
| Resultado contrastado con el umbral | No verificado | [docs/medicion-busqueda.md:27–80](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/medicion-busqueda.md#L27-L80). Comparación S9 disponible y brecha de producción declarada; no permite validar resultado del reto S10 sin asignación. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | [.github/workflows/ci.yml:31–49](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/.github/workflows/ci.yml#L31-L49); [src/observabilidad/metricas.service.ts:5–42](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/src/observabilidad/metricas.service.ts#L5-L42). Health 200 y logs configurados; métrica expuesta mide POST/S5, no búsqueda S1. Run actual CI success: [37264560596](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/37264560596). Observabilidad del escenario asignado pendiente. |
| Secretos protegidos | Cumple | Barrido del contrato en HEAD, ejemplos y docs sin secretos del equipo identificados; búsqueda histórica de claves privadas/tokens de alta confianza sin coincidencias fuera de dependencias. [docs/no-conformidades.md:8–40](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/no-conformidades.md#L8-L40) identifica el artefacto histórico Coveralls de un paquete tercero; no se publica su valor ni se atribuye al equipo. Alcance de barrido, no garantía universal. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/c4/C4-C2.md:9–34](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/c4/C4-C2.md#L9-L34) aún sitúa PostgreSQL como planeado y la persistencia en memoria, mientras [docs/arc42/arc42.md:190–194](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/arc42/arc42.md#L190-L194) describe Neon activo y el adaptador PostgreSQL existe. C4-C3 omite búsqueda/emparejamiento; no representa todo el MVP. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0009-versionado-del-contrato-y-error-unico.md:3–31](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/adr/0009-versionado-del-contrato-y-error-unico.md#L3-L31) es sucesor parcial de 0004, pero no vincula una decisión anterior al experimento del escenario oficialmente asignado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Solo el docente puede evaluar la sesión sobre despliegue y pipeline en vivo. No se puntúa desde el repositorio. |

## Rúbrica propia del corte · propuesta al docente

Niveles admitidos: insuficiente 0,00; básico 0,60; competente 0,80; sobresaliente 1,00. No verificado no equivale a cero.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | No hay asignación oficial identificada; el experimento S1 es de S9. |
| Decisión e implementación | No verificado | Pendiente | Hay decisión e implementación verificadas de búsqueda, sin vínculo acreditado al reto asignado. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Salud accesible; CI general en verde; falta métrica del escenario asignado y Quality Gate bloqueante acreditado. |
| Evolución arquitectónica trazable | Básico | 0.60 | Actualización parcial: C4 presenta PostgreSQL como planeado mientras arc42 y código lo implementan. [docs/c4/C4-C2.md:9–34](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/c4/C4-C2.md#L9-L34) |
| Sustentación del reto | Lo fija el docente | Pendiente | Sustentación pendiente sobre despliegue y pipeline en vivo. |

**Sin total final:** faltan la asignación verificada y la sustentación, que solo califica el docente con el entorno desplegado y el pipeline en vivo.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon anónimo de https://github.com/ISCOUTB/AS_202620_Recobra; nombre y organización conformes. |
| Estructura mínima presente | Cumple | [README.md:163–180](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/README.md#L163-L180). Árbol con README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md. |
| Estado calificado identificable | Cumple | origin/master, ebe6cca7a903bb333678bd20ba5327d8fcb127f7, 2026-10-04T23:40:37-05:00, último commit ≤ cierre S9. Para S10 es la punta preliminar actual. |
| Nombres de ADR según la convención | Cumple | [docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md:1–9](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md#L1-L9); nueve archivos Markdown con NNNN-kebab-case. |
| ADR aceptados no reescritos | No cumple | [docs/no-conformidades.md:167–194](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/no-conformidades.md#L167-L194). Historial leído: ADR-0002/0003 editados en f7c1a6c tras aceptación; ADR-0004 modificado en 34ab8f2. [docs/adr/0009-versionado-del-contrato-y-error-unico.md:3–31](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/adr/0009-versionado-del-contrato-y-error-unico.md#L3-L31) registra sucesión parcial de 0004; falta enlace de reemplazo en el antecedente y no regulariza todos los ADR. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:63](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/ia.md#L63). Registro actualizado en S9 con aceptado, corregido, rechazado y motivo; no hay actividad posterior en S10 aún. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/ci.yml:31–49](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/.github/workflows/ci.yml#L31-L49). Scanner explícito pero continue-on-error; [docs/no-conformidades.md:98–110](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/no-conformidades.md#L98-L110) declara token pendiente. Configuración en [sonar-project.properties:1–8](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/sonar-project.properties#L1-L8). No hay run exitoso del scanner y Quality Gate de esta revisión acreditados; CI general verificado success para el hash en [run 37264560596](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/37264560596), creado 2026-10-05T04:40:41Z; no acredita el scanner, que admite fallo. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del contrato en HEAD, ejemplos y docs sin secretos del equipo identificados; búsqueda histórica de claves privadas/tokens de alta confianza sin coincidencias fuera de dependencias. [docs/no-conformidades.md:8–40](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/no-conformidades.md#L8-L40) identifica el artefacto histórico Coveralls de un paquete tercero; no se publica su valor ni se atribuye al equipo. Alcance de barrido, no garantía universal. |
| Contribución de todos los integrantes | No verificado | Historial agregado: 128 commits; cinco grupos por identidad de correo, con .mailmap que vincula dos firmas. Se observan aportes de cuatro grupos consolidados. La correspondencia completa grupo→integrante y la sustantividad individual requieren validación docente; no se infieren identidades por parecido. |

## Estado global del proyecto (overall)

La punta actual de `master` es `ebe6cca7a903bb333678bd20ba5327d8fcb127f7` (2026-10-04T23:40:37-05:00) y coincide con S9 congelada: no hay commits tardíos hasta esta revisión. La entrega S9 aporta evidencia documental consistente y una porción nueva. La medición distingue local de producción y reconoce su brecha. Para el corte permanecen diferencias entre C4 y MVP, trazabilidad de la asignación y observabilidad del reto.

### Hallazgos abiertos

- Identificar y documentar la asignación oficial de S10 antes de juzgar su hipótesis, línea base y resultado.
- SonarCloud: falta evidencia del scanner exitoso y Quality Gate de la revisión; continue-on-error no impone bloqueo de integración. [.github/workflows/ci.yml:31–49](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/.github/workflows/ci.yml#L31-L49)
- C4-C2/C3 no representan PostgreSQL en producción ni todos los componentes actuales. [docs/c4/C4-C2.md:9–34](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/c4/C4-C2.md#L9-L34)
- S1 no está demostrado en producción: a 20 conexiones el documento informa p97,5=1113 ms; no se midieron 200. [docs/medicion-busqueda.md:27–80](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/medicion-busqueda.md#L27-L80)
- Regularizar sucesión de ADR-0002/0003 y el enlace del antecedente 0004 sin reescribir el historial.
- README mantiene descripción sin variables pese a DATABASE_URL y un ejemplo de error antiguo. [README.md:82–86](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/README.md#L82-L86); [README.md:135](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/README.md#L135)

### Hallazgos cerrados o corregidos en esta revisión

- La porción nueva S9 queda acreditada por búsqueda A6; el hallazgo preliminar de porción únicamente anterior a S8 se cierra. [docs/aspectos.md:15](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/aspectos.md#L15)
- La dependencia nueva autocannon está identificada y verificada en npm; no se exige añadir dependencias para aprobar una auditoría.
- Health público comprobado HTTP 200. Esto cierra la falta de comprobación puntual, sin cambiar retroactivamente las filas S8 diferidas.
- ADR-0009 documenta sucesión parcial y reconoce la edición de ADR-0004; cierre parcial de ese hallazgo, sin ocultar incumplimientos históricos.

## Preparación concreta para S10

Documenten cuál es el escenario operativo asignado y preparen una línea base y un resultado comparables en el despliegue. La salud responde, pero eso no prueba el flujo principal. Añadan la métrica del escenario al entorno, resuelvan la brecha de capacidad que midieron y expliquen la decisión frente al presupuesto antes de la sustentación.

## Tres preguntas de sustentación

1. Si Neon deja de responder durante una búsqueda, ¿cómo se detecta el fallo y qué respuesta observa el usuario sin confundir salud del proceso con disponibilidad de datos?
2. Con el presupuesto de cero y la saturación observada, ¿qué costo mensual tendría la alternativa elegida y a qué carga deja de ser suficiente la opción gratuita?
3. ¿Qué cambiarían primero después de medir la brecha entre memoria local y Render/Neon, y qué experimento permitiría distinguir CPU, red y consulta SQL?
