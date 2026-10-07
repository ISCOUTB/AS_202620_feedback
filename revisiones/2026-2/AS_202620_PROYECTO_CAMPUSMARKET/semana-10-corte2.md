# Semana 10 · Segundo corte · CampusMarket

> **Revisión preliminar**, realizada el 6 de octubre de 2026. El cierre de S10 todavía no ha ocurrido. No constituye nota aplicada ni evaluación de sustentación.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET |
| Estado revisado | `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00` en `origin/master` (2026-10-04T02:14:34-05:00) |
| Rama remota principal | `origin/master` |
| Base S8 | `784d788c19418099decde77a2cfb5ba831ab993b` |
| Estado preliminar S10 / HEAD | `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00` · 2026-10-04T02:14:34-05:00 |
| Cierre previsto S10 | 2026-10-12T05:00:00Z |
| Observación | 2026-10-06T21:17:09Z |

## Escenario operativo asignado y alcance

**No verificado.** EC-01 está documentado como escenario propio de consulta de productos y utilizado en S9. No se encontró evidencia que lo identifique como el escenario operativo oficialmente asignado para el segundo corte. Fuentes consultadas: [README.md:17–28](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L17-L28), [docs/evidencias/evidencia-s9-2026-10-01.md:350–371](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L350-L371) y [docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md:8–51](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md#L8-L51).

Se revisaron README, ADR, arc42 y evidencias/experimentos. Un escenario de calidad elegido por el equipo no demuestra cuál le asignó el docente. Antes de valorar la respuesta del reto hay que disponer del enunciado o una referencia oficial equipo–escenario. Las evidencias S6–S9 se describen como línea base, sin recalificarlas por existir.

**PDF excluido por instrucción docente:** se omite su fila; no se leyó ningún PDF ni se cuenta como incumplimiento. La matriz conserva 12 comprobaciones. Se realizaron únicamente consultas HTTP de lectura indicadas abajo. No se ejecutó código del equipo ni se probó el flujo principal.

## Matriz de comprobación S10

| Criterio | Evidencia técnica esperada | Estado preliminar | Observaciones y evidencia |
|---|---|---|---|
| Estado de S10 identificable y anterior al cierre | Rama principal, hash y fecha; estado preliminar | Cumple | HEAD de6ed67c05ccdb7eabd9b1951f146ab8958b1d00, 2026-10-04T02:14:34-05:00, anterior al cierre previsto; es una foto preliminar, no el futuro estado final. |
| Despliegue accesible en el momento de la revisión | Respuesta HTTP, tiempo y hora | Cumple | Comprobación de lectura iniciada 2026-10-06T21:17:09Z: frontend https://nnigarp.github.io/AS_202620_PROYECTO_CAMPUSMARKET/ HTTP 200 en 3,046350 s; /health https://campusmarket.iscoutb.dev/health HTTP 200 en 6,379432 s. URLs declaradas en [README.md:50–69](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L50-L69). No se probó flujo principal ni se atribuye el despliegue al hash documental. |
| Hipótesis, montaje, variables y umbral declarados | Caracterización del escenario operativo asignado | No verificado | EC-01 tiene carga y umbral propios, pero falta fuente de asignación S10: [docs/evidencias/evidencia-s9-2026-10-01.md:350–371](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L350-L371). |
| Línea base medida y reproducible | Herramienta, carga y procedimiento del escenario asignado | No verificado | Hay baseline del defecto N+1 y resultados bajo cuota de S9: [docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md:8–15](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md#L8-L15). No demuestra línea base del reto oficialmente asignado. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | ADR y respuesta al escenario asignado | No verificado | ADR-0019 fundamenta respuesta N+1; coherencia observada como base. Pendiente contrastarla con la consigna de S10, sin otorgar otra nota por S9. |
| Respuesta implementada o configurada sobre el MVP | Cambio trazable correspondiente al reto | No verificado | Implementación real de lote en [backend/app/catalogo/service.py:57–62](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/backend/app/catalogo/service.py#L57-L62); no puede afirmarse que sea la respuesta al escenario S10 desconocido. |
| Resultado contrastado con el umbral | Medición final comparable con línea base | No verificado | Medición S9 de loopback documentada y CI success; medición pública completa y correspondencia con el reto pendientes: [docs/evidencias/evidencia-s9-2026-10-01.md:350–371](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L350-L371). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | Run y observabilidad del escenario asignado | No verificado | Cuatro runs finales success y /health 200; métrica EC-01 documentada en [README.md:60–69](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L60-L69). Falta demostrar observación de la respuesta a la asignación S10 y el bloqueo de integración; scanner Sonar continúa abierto. |
| Secretos protegidos | Barrido del contrato | Cumple | Sin credenciales productivas detectadas en código/documentos actuales; CI Gitleaks de checkout success: [.github/workflows/backend-tests.yml:70–78](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/.github/workflows/backend-tests.yml#L70-L78). No se presenta el historial completo como comprobado. |
| C4, arc42, ADR y contratos correspondientes al MVP | Consistencia documental y trazabilidad | Cumple | C4 describe cuatro contextos, MySQL/archivos, HTTPS y OpenAPI v2: [docs/c4/02-contenedores.md:4–48](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/c4/02-contenedores.md#L4-L48). arc42 registra topología vigente separada de historia Azure: [docs/arc42/07-vista-despliegue.md:3–46](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/arc42/07-vista-despliegue.md#L3-L46). Correspondencia de base verificable; evolución específica del reto aún pendiente. |
| Decisión anterior confirmada o reemplazada con evidencia | Relación explícita entre medición y decisión | No verificado | ADR-0019 extiende 0009/0016 con evidencia N+1: [docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md:3–51](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md#L3-L51). Es respuesta medida de S9, sin identificación como cambio requerido por S10. |
| Sustentación del reto sobre el entorno desplegado | Sesión y pipeline en vivo; lo resuelve el docente | No verificado | El docente debe evaluar explicación del reto en el entorno desplegado y pipeline en vivo; no se puntúa desde el repositorio. |

## Rúbrica del segundo corte · cinco criterios

Escala de la ficha: **0,00 · 0,60 · 0,80 · 1,00 por criterio**. No se aplica la fórmula semanal. Una comprobación pendiente conserva puntaje pendiente; no se convierte automáticamente en cero.

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Sin asignación oficial, EC-01 propio no permite fijar nivel de caracterización del reto. |
| Decisión e implementación | No verificado | Pendiente | Hay decisión e implementación fundamentadas de S9; pendiente su correspondencia con el reto S10. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | CI y health actuales verificados; observabilidad específica del reto, scanner y bloqueo de integración pendientes. |
| Evolución arquitectónica trazable | No verificado | Pendiente | C4/arc42/contrato actualizados como línea base; no se atribuye nivel de evolución S10 a la entrega S9 por existir. |
| Sustentación del reto | Pendiente del docente | Pendiente | Pendiente de sustentación sobre el despliegue y ejecución del pipeline en vivo; no se infiere desde el repositorio. |

**Total: pendiente, no calculado.** La correspondencia con la asignación y la sustentación impiden proponer un total responsable.

## Matriz transversal · CONTRATO §11

| Criterio transversal | Estado | Evidencia y observaciones |
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

## Estado global (overall)

HEAD: `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00` · 2026-10-04T02:14:34-05:00. La punta coincide con S9; no hay cambios tardíos que alteren la calificación. Cuatro runs del hash están success. El frontend público y /health respondieron 200 en esta revisión. S9 presenta evidencia completa dentro de su alcance; siguen abiertos Sonar en pipeline, medición pública extremo a extremo y las ediciones históricas de ADR. La asignación específica S10 no se localizó.

Recuento descriptivo: **4 Cumple, 0 No cumple, 8 No verificado, sobre 12.** No es una nota ni sustituye la rúbrica.

## Próximos pasos

Para el segundo corte falta identificar el escenario operativo asignado por el docente. El despliegue y el health check responden; preparen la línea base, la intervención y el resultado comparable del reto, con métrica y límites de validez. No presenten el experimento de S9 como respuesta a una asignación todavía no confirmada. La sustentación y el pipeline en vivo quedan pendientes.

## Tres preguntas para la sustentación

1. Fallo: ¿qué ocurre con catálogo, health y datos si MySQL falla, y qué evidencia distingue recuperación de API de recreación de ambos contenedores?
2. Costo: ¿qué límite de memoria, CPU o volumen haría inviable la solución actual y por qué la lectura en lote fue preferible a aumentar recursos?
3. Medición: si el navegador público sigue sobre dos segundos mientras loopback cumple, ¿qué medirían y cambiarían primero?

## Delta arquitectónico desde el primer corte

Base publicada de S5: `8044215811e53b111888f75b30fc175fb889dc56`; comparación git contra HEAD `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00`: 157 rutas cambiadas, de ellas 34 en ADR/arc42/C4 (sin leer PDF). Se inspeccionaron las decisiones, contratos, código y evidencia citados en las filas. El delta sirve para examinar evolución y consistencia del MVP, no para recalificar las entregas S6–S9. La correspondencia con el escenario asignado S10 sigue pendiente.
