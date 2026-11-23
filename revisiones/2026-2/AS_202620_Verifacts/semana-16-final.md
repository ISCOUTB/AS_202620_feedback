# Evaluación técnica S16 · VeriFacts

Fecha de lectura: 23 de noviembre de 2026. Revisión técnica previa a la sustentación. No se ejecutó código estudiantil ni se modificaron calificaciones. No se califican demostración ni C5. La asignación oficial del desafío final no se encontró acreditada en las fuentes leídas: no se sustituye por el escenario S10.

## Estado y corte

- Repositorio: https://github.com/ISCOUTB/AS_202620_Verifacts
- Rama de referencia: master.
- Candidato observado: [96538d855c16d4f8c7ed8bb161d59823c34cc442](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/96538d855c16d4f8c7ed8bb161d59823c34cc442); fecha de commit 2026-11-21T00:28:27Z.
- Cierre de referencia: 23 de noviembre, 05:00 UTC, equivalente al final del domingo 22 en Colombia. La captura contemporánea de rama es referencia; no certifica entrega SAVIO ni cierre efectivo de sección.

## Alcance S10 → S16

S10 estudió Q-01 y el arranque frío de Render, con mantener Render+keepalive. S16 documenta Dokploy como referencia, web y API en dominio único, volumen SQLite y análisis de texto/URL con historial. La guía declara límites y diferencia el prototipo de mensajería de la aplicación. Mantener el monolito y no incorporar broker es una decisión defendible, no ausencia automática de trabajo.

Base S10 publicada: `6c08cc536ac7bd294c749548bd70276044ee511e`. [Comparación de GitHub](https://github.com/ISCOUTB/AS_202620_Verifacts/compare/6c08cc536ac7bd294c749548bd70276044ee511e...96538d855c16d4f8c7ed8bb161d59823c34cc442) informa 67 commits; 57 archivos modificados. No se recalifican entregas previas por existir.

## Decisiones y evolución

Hay 13 ADR. ADR-0010 complementa 0004/0008 por cold start de unos 22,4 s y falta de persistencia en Render; formaliza Compose y volumen. Sin embargo mezcla URL HTTPS vigente con párrafos que aún dicen solo HTTP/sslip.io y no medido: la evolución no está completamente reconciliada. ADR-0013 conserva mensajería aislada y admite expresamente que URL no está medida; no demuestra que su latencia cumpla Q-01.

## Calidad, resiliencia y seguridad

El informe Q-01/Q-05 leído mide texto de 10.000 caracteres local, 200 corridas/100 repeticiones, p95 46,9 ms y 100 % repetibilidad, excluyendo URL. La guía final declara p95 Dokploy 195,4 ms, pero es evidencia del equipo, no una nueva observación del revisor. extract_from_url llama directamente trafilatura.fetch_url; no incorpora guardia anti-SSRF ni timeout explícito propio. Sus cinco pruebas simulan descarga/extracción y 400/422, no timeout real, SSRF ni carga URL. La guía presenta en un pasaje el timeout como mitigación al justificar sincronía, mientras arc42 y ADR lo mantienen pendiente. También quedan idempotencia productiva, límites de tamaño e historial global sin propietario declarados como deuda. No se afirma explotación ni exposición real de datos.

## Coherencia y trazabilidad

Se leyeron doce secciones arc42 y C1–C3; C3 relaciona rutas, análisis y repositorio SQLite. Se inspeccionaron 14/14 filas A-00–A-13, contrastando A-00, A-01 y A-02 con health, vertical slice y modificación de regla, y A-08 con código/tests de URL. Las primeras filas usan rutas y pruebas como texto sin enlace y enlaces generales a Actions, no run preciso; no se certifica la navegabilidad completa de todas las cadenas. Además A-11 es prototipo aislado y debe mantenerse fuera del C4 de producción. CI incluye pytest, smoke de Docker y métricas; no se observó un paso específico que valide diagramas/enlaces.

## CI del SHA exacto

Runs exactos 44844061979 Tests y 44844062023 SonarCloud exitosos; check externo SonarCloud Code Analysis exitoso. El primero incluye Tests y Build y smoke test de la imagen. Smoke es del contenedor de CI, no disponibilidad productiva ni validación de todos los caminos de URL.

- [Tests: 44844061979](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/44844061979): success, head_sha 96538d855c16d4f8c7ed8bb161d59823c34cc442.
- [SonarCloud: 44844062023](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/44844062023): success, head_sha 96538d855c16d4f8c7ed8bb161d59823c34cc442.
- [SonarCloud Code Analysis](https://github.com/ISCOUTB/AS_202620_Verifacts/runs/136659729655): success.
- [Build y smoke test de la imagen](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/44844061979/job/136659455606): success.
- [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/44844062023/job/136659332291): success.
- [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/44844061979/job/136659332279): success.

La configuración se leyó en [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/.github/workflows/tests.yml). El check Sonar exitoso no equivale a nueva prueba funcional ni a demostrar cobertura de todos los atributos.

## README y despliegue: evidencia separada

El README documenta https://verifacts.iscoutb.dev. Esta pasada es documental: **sin sonda HTTP actual, sin credenciales, sin flujo productivo ni correspondencia imagen→SHA comprobados por este revisor**. Las comprobaciones históricas declaradas por el equipo no se presentan como observaciones nuevas. Incorporar aquí por separado las sondas centrales con hora, respuesta y límites; un health 200 no acredita la demostración.

## Colaboración verificable, sin atribución individual

La consulta de historial alcanzable desde el SHA devolvió 100 commits en esta página y tres identificadores de autor distintos (cuentas/firmas, no tres personas demostradas); es una muestra limitada a 100, no censo semestral. Meses visibles: 2026-11, 2026-10, 2026-09. La consulta de comentarios inline devolvió 0; no hay comentarios inline en esa respuesta. Esto no demuestra revisión cruzada humana ni ausencia de otras modalidades de revisión. No se asignan cuentas por parecido de nombre, no se atribuye trabajo individual y no se fija C5.

## Matriz S16

| Comprobación | Estado | Evidencia / límite |
|---|---|---|
| Estado final identificable | Candidato documentado | SHA y fecha arriba; elegibilidad SAVIO pendiente. |
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
| Aspectos completos y navegables | No cumple íntegramente | 14/14 filas inspeccionadas; muestra semántica y huecos detallados arriba. |
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

1. Si una URL redirige hacia una dirección privada o tarda más de 4 s, ¿qué impide actualmente el acceso y dónde medirían el presupuesto de Q-01 sin extrapolar las pruebas de texto?
2. Si el usuario repite POST tras perder la respuesta, ¿qué evita dos registros en el historial y qué parte de la idempotencia del prototipo todavía no existe en producción?
3. Si Dokploy pierde el volumen SQLite, ¿qué RPO/RTO pueden demostrar y por qué un volumen persistente no sustituye una copia de seguridad probada?

## Fuentes del SHA revisado

- [docs/entregas/entrega-final-guia-sistema-integrado.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/entregas/entrega-final-guia-sistema-integrado.md)
- [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/aspectos.md)
- [docs/adr/0010-despliegue-laboratorio-dokploy.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/adr/0010-despliegue-laboratorio-dokploy.md)
- [docs/adr/0013-no-incorporar-mensajeria-asincrona.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/adr/0013-no-incorporar-mensajeria-asincrona.md)
- [docs/evidencia/medicion-q01-q05.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/evidencia/medicion-q01-q05.md)
- [docs/arc42/11-riesgos-y-deuda-tecnica.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/arc42/11-riesgos-y-deuda-tecnica.md)
- [app/modules/content/service.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/app/modules/content/service.py)
- [tests/test_url_ingestion.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/tests/test_url_ingestion.py)
- [tests/test_health.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/tests/test_health.py)
- [tests/test_analysis.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/tests/test_analysis.py)
- [tests/test_rule_modification.py](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/tests/test_rule_modification.py)
- [docs/c4/03-componentes.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/c4/03-componentes.md)

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- API salud: [https://verifacts.iscoutb.dev/health](https://verifacts.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:12 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
