# Evaluación técnica S16 · TAIA

Fecha de lectura: 23 de noviembre de 2026. Revisión técnica previa a la sustentación. No se ejecutó código estudiantil ni se modificaron calificaciones. No se califican demostración ni C5. La asignación oficial del desafío final no se encontró acreditada en las fuentes leídas: no se sustituye por el escenario S10.

## Estado y corte

- Repositorio: https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant
- Rama de referencia: main.
- Candidato observado: [bd3db97fd53469d8e1f9e397b69fc63acb21ccfa](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa); fecha de commit 2026-11-23T03:33:40Z.
- Cierre de referencia: 23 de noviembre, 05:00 UTC, equivalente al final del domingo 22 en Colombia. La captura contemporánea de rama es referencia; no certifica entrega SAVIO ni cierre efectivo de sección.

Se conserva bd3db97 como candidato observado en main en la captura 05:00:31–05:01:06 UTC. La reconstrucción posterior aporta 9437b14b0c6e027933f7e99e1846d5d77267942b, descendiente con fechas de commit anteriores al cierre. Comparación leída: e9957c5 (04:03:33 UTC) añade filtros task_id/status, cuatro pruebas y contrato; 9437b14 (04:15:12 UTC) añade requisitos de voz y Telegram. No se encontraron PR asociados ni Actions exactos para 9437b14. Fecha de commit no prueba fecha de push: mantener recuperación posterior separada hasta verificar presencia de rama al cierre, sin penalizar ni acreditar automáticamente.

## Alcance S10 → S16

S10 evaluó la confirmación en español asociada a S1/S3. S16 añade rotación de sesión, integración de Groq y Gemini, notificaciones FCM y trazabilidad del sistema académico. El alcance distingue RAG/embeddings/búsqueda semántica fuera del MVP. En el candidato observado, RF-REC-03 permanece parcial; no se le acredita la mejora que solo existe en los commits recuperados después.

Base S10 publicada: `72a8b6a0b3680a59c235f9225f90bc260093d86b`. [Comparación de GitHub](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/compare/72a8b6a0b3680a59c235f9225f90bc260093d86b...bd3db97fd53469d8e1f9e397b69fc63acb21ccfa) informa 170 commits; la respuesta de archivos llega a 300 y no se trata como inventario completo. No se recalifican entregas previas por existir.

## Decisiones y evolución

ADR-0013 reemplaza explícitamente el orden de proveedores de ADR-0011: Groq primero, Gemini de respaldo. Contrasta 99 casos y p95 1198,7 frente a 1690,3 ms, con un caso menos de acierto de intención. La lectura de fallback_llm.py y test_ai_fallback_llm.py confirma el orden, el respaldo y la obligación residual de GEMINI_API_KEY. El cierre de ADR-0013 aún dice «Código y pruebas: Pendientes», contradicción documental frente al código existente. Esto impide tratar toda la trazabilidad como completamente conciliada.

## Calidad, resiliencia y seguridad

La tabla vigente de escenarios reconoce que Groq, proveedor principal, obtiene 89,1 % de extracción de campos frente al 90 % requerido; 91,92 % es acierto de intención y no sustituye esa medida. Tampoco se mide el registro final en PostgreSQL. S3 solo mide el tramo del modelo, no backend→canal. S5 reconoce cuatro archivos de adaptador modificados frente al máximo de dos. Las pruebas leídas cubren confirmación repetida/concurrente y negativa, rotación/reutilización de tokens y fallback: evidencia valiosa de mitigaciones, no medición productiva completa.

## Coherencia y trazabilidad

Se leyeron las doce secciones arc42 y los tres niveles C4. C3 muestra FCM, Groq/Gemini, Resend, Telegram y bucle de recordatorios coherentes con los puertos descritos. Se inspeccionaron 7/7 filas de aspectos y se contrastaron semánticamente A-01, A-02 y A-03 con sus pruebas, decisiones y mediciones. No se certifican 7/7 cadenas como cumplidas: A-01 termina en una medición parcial de S1 y A-03 en medición parcial de S3; el ADR mantiene un pendiente obsoleto. El CI configura auditoría de fronteras y sincronización del cliente, pero no consta una nueva ejecución de esas pruebas para el candidato documental.

## CI del SHA exacto

No se encontró run de Actions exacto para bd3db97; sí un check externo SonarCloud Code Analysis exitoso. El filtro paths del CI excluye el cambio documental, por lo que el CI verde del padre no es una ejecución del candidato. No se afirma fallo de pruebas ni CI completo aprobado.


- [SonarCloud Code Analysis](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/runs/137469809072): success.

La configuración se leyó en [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa/.github/workflows/ci.yml). El check Sonar exitoso no equivale a nueva prueba funcional ni a demostrar cobertura de todos los atributos.

## README y despliegue: evidencia separada

El README documenta https://taia-sistema.iscoutb.dev. Esta pasada es documental: **sin sonda HTTP actual, sin credenciales, sin flujo productivo ni correspondencia imagen→SHA comprobados por este revisor**. Las comprobaciones históricas declaradas por el equipo no se presentan como observaciones nuevas. Incorporar aquí por separado las sondas centrales con hora, respuesta y límites; un health 200 no acredita la demostración.

## Colaboración verificable, sin atribución individual

La consulta de historial alcanzable desde el SHA devolvió 100 commits en esta página y cuatro identificadores de autor distintos (cuentas/firmas, no cuatro personas demostradas); es una muestra limitada a 100, no censo semestral. Meses visibles: 2026-11, 2026-10. La consulta de comentarios inline devolvió 3; todos son automáticos. Esto no demuestra revisión cruzada humana ni ausencia de otras modalidades de revisión. No se asignan cuentas por parecido de nombre, no se atribuye trabajo individual y no se fija C5.

## Matriz S16

| Comprobación | Estado | Evidencia / límite |
|---|---|---|
| Estado final identificable | Candidato documentado | SHA y fecha arriba; elegibilidad SAVIO pendiente; caso de recuperación TAIA separado. |
| Despliegue estable durante revisión | No verificado | Incorporar sondas centrales; README no basta. |
| Flujos principales con datos realistas | No verificado en vivo | Código y pruebas documentados no sustituyen sesión funcional. |
| Caminos de error | Evidencia técnica parcial | Pruebas leídas en fuentes; sin ejecución por el revisor. |
| Respuesta al desafío final | No verificado | Falta acreditar asignación oficial. |
| Alcance frente a S10 | Comparado documentalmente | Base, diff y cambios explícitos arriba. |
| Evolución de ADR | Evidencia presente | Decisiones y límites descritos arriba. |
| Decisión confirmada/reemplazada | Evidencia presente con reservas | Revisar conciliación y fuentes de decisiones; no inferir ratificación personal. |
| Atributos contra umbral | Parcial | Mediciones y sus límites en sección de calidad. |
| Fallos y seguridad | Parcial | Controles/tests y deuda explícitos; no ensayo de producción. |
| arc42 1–12 y glosario | Estructura leída | No equivale a coherencia total; contradicciones señaladas. |
| C4 1–3 | Presente | Correspondencia y límites arriba. |
| Aspectos completos y navegables | No cumple íntegramente | 7/7 filas inspeccionadas; muestra semántica y huecos detallados arriba. |
| Validación automática arquitectónica/documental | Parcial | Workflow y pruebas; no inferir validador de diagramas/enlaces. |
| Contribución sustantiva semestral | No verificado individualmente | Agregados limitados; sin vinculación cuenta-persona. |
| Revisión cruzada de fondo | No verificado | Comentarios inline encontrados no acreditan discusión humana. |
| Demostración y defensa | Reservado al docente | Sin puntuación ni conclusión desde repositorio. |

## Matriz transversal del CONTRATO

| Criterio | Estado | Observación |
|---|---|---|
| Organización y convención de nombre | Cumple para ubicación/nombre | URL ISCOUTB; visibilidad anónima no probada en esta consulta autenticada. |
| Estructura mínima | Presente | README, arc42, ADR, C4, aspectos e IA en árbol exacto; rutas alternativas no cuentan como ausencia. |
| Estado identificado | Candidato explícito | No confundir fecha de commit con momento de push. |
| Convención de nombres ADR | Cumple en archivos de decisión observados | Numeración de cuatro dígitos; índices/.gitkeep no son decisiones. |
| Inmutabilidad de ADR aceptados | No verificado | No se realizó auditoría completa por archivo y fecha de aceptación. |
| Uso de IA actualizado y rechazo razonado | No verificado íntegramente | Archivo localizado; no se certifica cada entrada de todo el semestre. |
| CI/Sonar/Quality Gate | Evidencia exacta arriba, alcance limitado | Sin extrapolar pruebas del padre ni producción. |
| Sin secretos en todo el historial | No verificado | No se hizo barrido completo; no se afirma ausencia ni se reproducen valores. |
| Todos los integrantes contribuyen | No verificado | Agregados no resuelven identidad ni sustancia individual. |

## Niveles técnicos sugeridos para C2–C4

- **C2, decisiones y evolución: Competente, provisional.** Hay decisiones con alternativas y consecuencias, evolución concreta y contraste con implementación. Las reservas documentales indicadas impiden sugerir sobresaliente automático.
- **C3, calidad/resiliencia/seguridad: Básico, provisional.** Existen pruebas y mediciones, pero no se acreditan íntegramente todos los umbrales prioritarios ni la recuperación operativa; ver los límites específicos, no una penalización por no ejecutar durante esta lectura.
- **C4, coherencia/trazabilidad: Básico, provisional.** Hay documentación y reglas, pero persisten huecos o contradicciones concretas señaladas en la revisión de cadenas y decisiones.

No se propone C1 completo sin desafío acreditado y evidencia funcional vigente; no se asignan puntos, subtotal, nota total ni C5.

## Tres preguntas de defensa

1. Si Groq baja la exactitud de campos a 89,1 %, ¿qué evidencia justifica hacerlo principal y cómo medirían el resultado confirmado y persistido, no solo la intención?
2. Si cada clave de Groq agota su timeout antes del respaldo Gemini, ¿qué límite extremo a extremo protege los 7 s y qué funcionalidades permanecen disponibles?
3. Si se despliegan dos réplicas de la API con el bucle de recordatorios, ¿qué garantiza un único efecto y cómo demostrarían recuperación tras enviar FCM pero antes de confirmar el envío?

## Fuentes del SHA revisado

- [docs/calidad/escenarios_calidad.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa/docs/calidad/escenarios_calidad.md)
- [docs/adr/0013-usar-groq-como-proveedor-llm-principal.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa/docs/adr/0013-usar-groq-como-proveedor-llm-principal.md)
- [backend/app/modules/ai/adapters/outbound/fallback_llm.py](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa/backend/app/modules/ai/adapters/outbound/fallback_llm.py)
- [backend/tests/test_ai_fallback_llm.py](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa/backend/tests/test_ai_fallback_llm.py)
- [backend/tests/test_ai_create_task_confirmation.py](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa/backend/tests/test_ai_create_task_confirmation.py)
- [backend/tests/test_usuario_sessions.py](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa/backend/tests/test_usuario_sessions.py)
- [docs/c4/C4-C3.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa/docs/c4/C4-C3.md)
- [docs/arc42/05-vista-de-bloques-de-construccion.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa/docs/arc42/05-vista-de-bloques-de-construccion.md)

## Verificación independiente del corte y del despliegue

Git registra el commit 9437b14 a las 23:15 COT, pero las consultas contemporáneas de main hasta 05:01:06 UTC aún mostraban bd3db97 y no se halló push exacto de 9437b14 anterior al corte. No se acredita ese trabajo como integrado al cierre.

**Sondas de solo lectura del 23 de noviembre:**

- API salud: [https://taia-sistema.iscoutb.dev/health](https://taia-sistema.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:14 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
