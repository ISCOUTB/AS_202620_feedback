# Semana 10 · Segundo corte · TAIA

**Revisión preliminar abierta al cierre del 2026-10-12T05:00:00Z.** No reemplaza S9 definitiva ni aplica la fórmula semanal.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant |
| Rama principal remota | `main` |
| Estado revisado | `72a8b6a0b3680a59c235f9225f90bc260093d86b` en `origin/main` (2026-10-04T23:39:00-05:00) |
| Línea base S8 | `4b0724247c6a58f82bc6091f78ab8872d58456de` |
| Punta actual / S10 preliminar | `72a8b6a0b3680a59c235f9225f90bc260093d86b` · 2026-10-04T23:39:00-05:00 |
| Cierre S9 | 2026-10-05T05:00:00Z |
| Cierre eventual S10 | 2026-10-12T05:00:00Z |
| Revisión | 2026-10-06 (UTC) |

## Evolución desde S5 publicado

Base S5: `a3f4d826dd90bfc7e29ff9eb7d944b71ca99ecf7`. El delta hasta la punta contiene 96 commits y 287 rutas modificadas (PDF excluidos). Integra módulos, PostgreSQL, contrato, despliegue y observabilidad; suma normalización, auditoría de fronteras y evaluación del modelo. El pipeline actual falla y quedan conflictos documentales. Se contrastaron código, documentación, ADR y contratos; este recorrido aporta contexto de evolución, no recalifica S6–S9 ni acredita por sí mismo respuesta al escenario asignado.

## Alcance y método

Se consultó la rama principal remota mediante git y se eligió su último commit anterior o igual al cierre S9; no se consultaron etiquetas. S10 es preliminar y usa la punta actual. Se comparó S9 con la línea base S8; no se vuelven a puntuar entregas anteriores por existir. No se ejecutó código, pruebas ni despliegues del equipo. Los registros de ejecución del repositorio se distinguen de la comprobación externa. Por exclusión docente no se abrieron PDFs ni se evaluó su presencia, contenido, extensión o ubicación.

La consulta general de Actions se verificó mediante GET /actions/runs (100 registros como máximo); se distinguen el hash, la rama y la conclusión de cada run. Un intento inicial filtrado a pull requests no se usó para decidir. No se consultaron jobs ni logs adicionales.

## Escenario operativo oficialmente asignado

**No verificado.** No se encontró identificación de la asignación oficial del escenario operativo de S10 en README, ADRs y experimentos. Los escenarios S1/S3/S4 de calidad y las evidencias de generación S9 no prueban por sí mismos cuál fue el reto asignado. [docs/evaluacion_ia/contraste_umbrales.md:5–20](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/evaluacion_ia/contraste_umbrales.md#L5-L20); [docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md:22–28](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md#L22-L28) No se sustituye la asignación por un escenario genérico de calidad, una práctica S8/S9 o una hipótesis del revisor.

## Despliegue observado

GET http://taia-sistema-jkbo9i-ec2cd4-144-24-4-187.sslip.io/health respondió HTTP 200 en 6,930827 s, comprobación terminada el 2026-10-06T21:22:24Z, cuerpo status=ok. URL actual en [README.md:5–15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/README.md#L5-L15). La antigua URL IP de S8 respondió 502/connection refused durante la comprobación (2026-10-06T21:16:37Z); no se usa como URL vigente. Solo se consultó salud, sin autenticación ni prueba del flujo principal. HTTP 200 no demuestra que el hash revisado esté desplegado ni que Gemini o Telegram funcionen.

## Matriz de comprobación S10

Se omite expresamente la fila de PDF por exclusión docente. Quedan 12 filas; su recuento es diagnóstico y no es la fórmula de calificación.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | origin/main 72a8b6a0b3680a59c235f9225f90bc260093d86b, 2026-10-04T23:39:00-05:00, anterior al cierre eventual; revisión preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | GET http://taia-sistema-jkbo9i-ec2cd4-144-24-4-187.sslip.io/health respondió HTTP 200 en 6,930827 s, comprobación terminada el 2026-10-06T21:22:24Z, cuerpo status=ok. URL actual en [README.md:5–15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/README.md#L5-L15). La antigua URL IP de S8 respondió 502/connection refused durante la comprobación (2026-10-06T21:16:37Z); no se usa como URL vigente. Solo se consultó salud, sin autenticación ni prueba del flujo principal. HTTP 200 no demuestra que el hash revisado esté desplegado ni que Gemini o Telegram funcionen. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | No se encontró identificación de la asignación oficial del escenario operativo de S10 en README, ADRs y experimentos. Los escenarios S1/S3/S4 de calidad y las evidencias de generación S9 no prueban por sí mismos cuál fue el reto asignado. [docs/evaluacion_ia/contraste_umbrales.md:5–20](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/evaluacion_ia/contraste_umbrales.md#L5-L20); [docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md:22–28](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md#L22-L28) |
| Línea base medida y reproducible | No verificado | [docs/evaluacion_ia/contraste_umbrales.md:22–37](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/evaluacion_ia/contraste_umbrales.md#L22-L37). Dataset y medición del adaptador/confirmación de S9; no línea base del escenario oficialmente asignado S10. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0005-normalizacion-confirmacion-espanol.md:7–59](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/adr/0005-normalizacion-confirmacion-espanol.md#L7-L59) y [docs/adr/0006-fronteras-y-evaluacion-verificable.md:26–71](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/adr/0006-fronteras-y-evaluacion-verificable.md#L26-L71). Decisiones reales del periodo; falta relación acreditada con la asignación S10. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [backend/app/modules/ai/application/use_cases/handle_message.py:35–51](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/backend/app/modules/ai/application/use_cases/handle_message.py#L35-L51) y [docs/evaluacion_ia/diagnostico_conversations_null.md:41–52](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/evaluacion_ia/diagnostico_conversations_null.md#L41-L52). Cambios incorporados al repositorio, pero el CI de main falla y CD se omite; no está verificado qué corre en el despliegue ni la respuesta al reto asignado. |
| Resultado contrastado con el umbral | No verificado | [docs/evaluacion_ia/contraste_umbrales.md:22–37](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/evaluacion_ia/contraste_umbrales.md#L22-L37). Se contrastan resultados parciales y límites de S9; no hay resultado completo del reto S10 identificable. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | [.github/workflows/ci.yml:43–81](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/.github/workflows/ci.yml#L43-L81); [CI 37264440690](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/37264440690) failure y [CD 37264470652](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/37264470652) skipped. Health 200 y [backend/app/shared/adapters/inbound/observability.py:26–44](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/backend/app/shared/adapters/inbound/observability.py#L26-L44) configuran observabilidad básica, pero [docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md:82–85](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md#L82-L85) reconoce fallos del proveedor sin log y consumo repetido tras fallo. El conjunto operativo exigido no está acreditado. |
| Secretos protegidos | Cumple | [.env.example:25–41](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/.env.example#L25-L41); [run.bat:1–15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/run.bat#L1-L15). Barrido sobre código, docs y ejemplos de HEAD sin credenciales reales identificadas; coincidencias actuales son parámetros, variables y fixtures. El valor predeterminado JWT histórico se trata en la transversal; retirar el valor de HEAD no lo elimina del historial. El antecedente histórico exige cierre de rotación si se usó en algún entorno. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/arc42/07-vista-de-despliegue.md:67–96](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/arc42/07-vista-de-despliegue.md#L67-L96) contiene marcadores de merge sin resolver y mezcla operación histórica con Dokploy. [README.md:215–221](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/README.md#L215-L221) aún describe CD por SSH/GHCR, mientras [.github/workflows/cd.yml:39–63](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/.github/workflows/cd.yml#L39-L63) solicita despliegue por API Dokploy. Documentación parcialmente actualizada. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0006-fronteras-y-evaluacion-verificable.md:12–24](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/adr/0006-fronteras-y-evaluacion-verificable.md#L12-L24). La auditoría confirma/corrige fronteras pero no acredita una decisión previa confirmada o reemplazada por el experimento del escenario oficialmente asignado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Sustentación y ejecución del pipeline en vivo corresponden al docente; sin puntaje desde el repositorio. |

## Rúbrica propia del corte · propuesta al docente

Niveles admitidos: insuficiente 0,00; básico 0,60; competente 0,80; sobresaliente 1,00. No verificado no equivale a cero.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Asignación oficial S10 no identificada; los experimentos S9 no la sustituyen. |
| Decisión e implementación | No verificado | Pendiente | Cambios y ADR presentes; no está acreditado el vínculo con la asignación ni su despliegue actual. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Salud 200, pero CI falla y CD se omite. Sin asignación no se fija nivel completo; fallos operativos descritos en la matriz. |
| Evolución arquitectónica trazable | Básico | 0.60 | Actualización parcial con conflictos de merge y dos procedimientos de CD contradictorios. [docs/arc42/07-vista-de-despliegue.md:67–96](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/arc42/07-vista-de-despliegue.md#L67-L96) |
| Sustentación del reto | Lo fija el docente | Pendiente | Pendiente de sesión con entorno y pipeline en vivo. |

**Sin total final:** faltan la asignación verificada y la sustentación, que solo califica el docente con el entorno desplegado y el pipeline en vivo.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon anónimo público desde https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant; nombre y organización conformes. |
| Estructura mínima presente | Cumple | [README.md:99–107](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/README.md#L99-L107). Seis rutas mínimas presentes en el árbol: README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md. |
| Estado calificado identificable | Cumple | origin/main 72a8b6a0b3680a59c235f9225f90bc260093d86b, 2026-10-04T23:39:00-05:00; último ≤ cierre S9 y punta actual preliminar S10. |
| Nombres de ADR según la convención | Cumple | [README.md:84–90](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/README.md#L84-L90) y [docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md:1–5](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md#L1-L5). Siete ADR Markdown en NNNN-kebab-case; PDFs excluidos. |
| ADR aceptados no reescritos | No cumple | Historial leído de ADR-0001: aceptado, editado en 4dd3925 y 42c5b03; vuelve a corregir enlace en 8282044 sin sucesor. [docs/adr/0001-estilo-arquitectonico.md:85–107](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/adr/0001-estilo-arquitectonico.md#L85-L107) y [docs/ia.md:555–558](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/ia.md#L555-L558). Las nuevas aceptaciones de 0006/0007 no reemplazan 0001. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:709–787](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/ia.md#L709-L787). Entradas 011–017 incorporadas en el periodo S9 con decisiones y rechazos; no hay commits posteriores de S10 aún. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/ci.yml:43–81](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/.github/workflows/ci.yml#L43-L81). [CI 37264440690](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/37264440690) failure para el hash revisado; [CD 37264470652](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/37264470652) skipped. No hay scanner SonarCloud ni configuración/Quality Gate públicos verificados; workflow actual ejecuta pruebas/auditorías, no scanner. No confundir corridas verdes históricas de otras ramas con main actual. |
| Sin credenciales en el repositorio ni en el historial | No cumple | HEAD sin credenciales reales identificadas. El historial conserva un valor predeterminado de firma JWT en run.bat:5 del estado S8 4b07242, retirado en 8282044; [run.bat:4–11](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/run.bat#L4-L11) y [docs/ia.md:538–546](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/ia.md#L538-L546) reconocen el hecho. No se publica su valor ni se afirma uso productivo. Confirmar reemplazo/rotación en cualquier entorno que lo haya usado; borrar del árbol no borra exposición histórica. |
| Contribución de todos los integrantes | No verificado | 127 commits y seis grupos por identidad de correo; dos firmas comparten exactamente identidad y pueden consolidarse, pero otras no. Sin correspondencia explícita suficiente no se asignan cuentas por parecido ni se afirma que falte un integrante. Validación docente de autoría y contribución sustantiva pendiente. |

## Estado global del proyecto (overall)

La punta actual de `main` es `72a8b6a0b3680a59c235f9225f90bc260093d86b` (2026-10-04T23:39:00-05:00) y coincide con S9 congelada: no hay commits tardíos hasta esta revisión. La porción de confirmación y su ciclo rojo/verde están acreditados. El componente generativo ya tiene evaluación real, con límites declarados. Falta verificar S1 persistencia y S3 extremo a extremo; el pipeline de main termina en fallo, el CD se omite y hay conflictos documentales sin resolver. Salud accesible no equivale a flujo conversacional probado.

### Hallazgos abiertos

- Identificar el escenario oficialmente asignado de S10 y separar hipótesis, línea base, cambio y experimento.
- CI actual failure y CD skipped: no afirmar que la corrección del NULL o el hash actual estén desplegados. [CI 37264440690](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/37264440690); [CD 37264470652](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/37264470652)
- S1 de campos persistidos y S3 del backend al canal continúan sin medición completa; el 91,8 % corresponde solo a extracción. [docs/evaluacion_ia/contraste_umbrales.md:22–37](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/evaluacion_ia/contraste_umbrales.md#L22-L37)
- Resolver marcadores de merge y rutas de operación contradictorias. [docs/arc42/07-vista-de-despliegue.md:67–96](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/arc42/07-vista-de-despliegue.md#L67-L96)
- Degradación del proveedor: timeout 20 s frente a presupuesto 7 s; falta evento de error y last_usage puede repetir tokens tras fallo. [docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md:82–85](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/adr/0007-comportamiento-ante-fallo-del-proveedor-llm.md#L82-L85)
- Valor predeterminado histórico de firma JWT retirado: confirmar sustitución/rotación e invalidación de sesiones en los entornos que lo usaron, sin divulgar el valor. [run.bat:4–11](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/run.bat#L4-L11)
- SonarCloud/Quality Gate públicos pendientes y ADR-0001 editado sin sucesor.
- La URL publicada usa HTTP: validar un acceso HTTPS antes de transmitir credenciales o tokens. [README.md:5–12](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/README.md#L5-L12)

### Hallazgos cerrados o corregidos en esta revisión

- Se cierra la falta de actividad/porción S9 de la preliminar: 23 commits y normalización real con prueba roja/verde. [backend/app/modules/ai/application/use_cases/handle_message.py:35–51](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/backend/app/modules/ai/application/use_cases/handle_message.py#L35-L51)
- Registro de IA actualizado con aceptado/corregido/rechazado y razones. [docs/ia.md:709–787](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/ia.md#L709-L787)
- Hay evaluación real del componente generativo con dataset, resultado, costo, latencia y ADR de fallo; no confundir este cierre con cumplimiento de S1/S3 completos. [docs/evaluacion_ia/resultado_s1_100.json:13–27](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/evaluacion_ia/resultado_s1_100.json#L13-L27)
- Plantilla .env.example versionada sin claves reales y retirada de valores predeterminados en el arranque actual. [.env.example:25–41](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/.env.example#L25-L41)
- E-02/E-05 corregidos en el código: composición centralizada y contrato público de Academic; la evidencia histórica se conserva claramente como anterior. [docs/auditoria_erosion.md:3–13](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/72a8b6a0b3680a59c235f9225f90bc260093d86b/docs/auditoria_erosion.md#L3-L13)
- Health externo vigente HTTP 200; no cambia retroactivamente la evaluación S8 ni verifica el flujo conversacional.

## Preparación concreta para S10

Documenten el escenario operativo oficialmente asignado, con un antes y un después reproducibles en el despliegue. El health responde, pero el CI actual falla y CD queda omitido: verifiquen la versión desplegada y repitan el flujo conversacional después de corregirlo. Instrumenten fallos del proveedor y consumo por petición, revisen el timeout y sincronicen la documentación de Dokploy antes de la sustentación.

## Tres preguntas de sustentación

1. Si Gemini agota el timeout mientras existe una confirmación pendiente, ¿qué puede seguir funcionando y cómo distinguirán en logs la degradación de una respuesta exitosa HTTP 200?
2. ¿Cómo calculan el costo por operación con una llamada fallida sin tokens y con last_usage conservando el consumo anterior, además del costo fijo de infraestructura?
3. A la luz del 91,8 % de extracción, los fallos de estado y el máximo de 20,2 s, ¿qué cambiarían y qué prueba extremo a extremo confirmaría la mejora sin alterar las etiquetas después de ver el resultado?
