# PideUtb · Proyecto final S16

**Revisión técnica previa a la sustentación.** [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) · [Contrato](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

**Estado candidato:** `master` en [`e5f40775dc255ed5db8b1b32eb3c2e56610316db`](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/e5f40775dc255ed5db8b1b32eb3c2e56610316db) · commit 2026-11-22T21:29:25Z; observado en la captura de referencia del 23/11/2026 hacia las 05:00 UTC. Hora efectiva de SAVIO, entrega, URL oficial del equipo y documento guía de tres páginas no contrastados; no se sustituye esta evidencia con un tag. **Desafío S16 asignado: no verificado**; el reto técnico S10 no se presume S16.

## 1. Sistema, despliegue y alcance

Sitio público y API, compra de mostrador, canje, comprobante y avisos sujetos a alcance. Un formulario o HTML accesible no es demostración de pago o entrega. [README, destinos y health](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/README.md#L8-L35) · [OpenAPI menú](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/api/openapi.yaml#L172-L205).

**Comprobaciones externas de solo lectura (GET):** 23 nov 13:27:16–13:28:31 UTC: sitio 200 HTML (3,92 s), panel 200 HTML (2,49 s), health 200 JSON (2,20 s), menú contractual `/v1/menu/establecimientos/1/items` 200 JSON (2,30 s) y ruta inexistente 404 JSON (1,60 s). Primer health agotó 5 s. No ejecuté mutaciones, pagos, consultas de pedidos, panel autenticado ni comprobante. No consta revisión servida del SHA del corte. Sin código estudiantil ejecutado, cambios ni mutaciones. Funcionamiento completo con datos realistas y respuesta/desempeño frente al desafío quedan no verificados hasta cotejar SAVIO y demostración. El 404 acredita manejo del recurso inexistente únicamente, no todos los errores funcionales.

**[S10 `2497bfe`](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956) → [S16 `e5f4077`](https://github.com/ISCOUTB/AS_202620_PideUtb/compare/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956...e5f40775dc255ed5db8b1b32eb3c2e56610316db):** 115 commits y 200 archivos en la respuesta de comparación, versus S10 autenticación/canje y contrato 2.0. Estado nuevo: token de consulta por pedido, límites y demora prevista, correo para comprobante, avisos prescindibles y portabilidad a laboratorio. El GET de consulta antes reportado sin protección ahora exige `X-Token-Pedido`; sin token, inválido o inexistente comparten 404 ([router](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/backend/app/pedidos/router.py#L68-L101)). Corrección estática demostrada, no confirmación de la protección en producción.

## 2. Decisiones y evolución

14 ADR. [ADR-0008](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/adr/0008-despliegue-en-el-servidor-del-laboratorio.md#L5-L40) reemplaza plataforma ADR-0004, con arranque en frío medido 42,4 s frente a 10 s; ADR-0010 sondeo, ADR-0012 avisos/comprobante no críticos, [ADR-0014](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/adr/0014-topes-del-pedido-y-demora-estimada.md) explicita límites y demora. Distinguir topes del producto de requisitos del desafío docente.

## 3. Calidad, resiliencia y seguridad

[S14](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/evidencia-s14.md#L14-L76): ESC-03 antes 8,32 s dejaba 1,68 s humano; sondeo 5 s deja 4,68 s, con script/prueba de presupuesto y criterio explicados. [ESC-04](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/evidencia-s14.md#L139-L150) ~161 ms vs <2 s; anti-reutilización tiene pruebas y código de canje protegido por sesión/rol, pero prueba simultánea y alcance productivo no verificados. Validaciones de pedido, pago rechazado e idempotencia están en código y pytest; no se ejecutaron en producción.

**CI en el SHA exacto, no despliegue:** [45072376512](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/45072376512) push exacto: ambos Python, contrato Spectral/oasdiff, dependencias, imagen y recorrido navegador pasaron. El job llamado Sonar está verde pero **scanner y espera de Quality Gate omitidos**; sí hubo [check externo exacto](https://github.com/ISCOUTB/AS_202620_PideUtb/runs/137362174759) verde y [panel Sonar master](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_PideUtb&branch=master). No acreditar la cadena de Gate bloqueante de ese push. Sin job identificado de enlaces o C4 automático.

## 4. Coherencia y trazabilidad

[arc42 monolítico](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/arc42/arc42.md) y [C4 niveles 1–3](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/c4); contratos [OpenAPI/AsyncAPI y versiones](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/api). [Aspectos](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/aspectos.md#L17-L24): 3/6 recorridos (ESC-03 sondeo→ADR-0005/10→servicio/UI→pruebas/medición; ESC-04 canje→ADR-0007→service→tests; CON-01 contratos→ADR-0003→esquemas/CI). La matriz usa C4 y umbral pero no columna dedicada de evidencia de calidad; ESC-03 la incorpora en texto, ESC-04 y CON-01 requieren juntar otras evidencias. No afirmar cobertura completa 6/6.

**Transversal:** Repositorio conforme, estructura mínima presente; ADR numerados, historial de no edición post-aceptación no confirmado. Registro IA con entradas 22/11 [medición y correcciones](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/e5f40775dc255ed5db8b1b32eb3c2e56610316db/docs/ia.md#L800-L853). Job dependencias no prueba historial de secretos completo; análisis Sonar de push se trata como arriba.

**Colaboración, observación agregada:** Últimos 100 commits: octubre 60, noviembre 40; 3 firmas/cuentas sin reconciliar. 51 PR consultadas, 51 merges al corte y 18 comentarios inline antes de corte, todos de cuentas bot; no acreditan revisión humana cruzada y de fondo. No se emite juicio de demostración o sustentación.

## Lectura cualitativa de la rúbrica (sin puntos)

- **C2 · Decisiones y evolución:** **Sobresaliente, provisional.** El reemplazo de plataforma está vinculado a un arranque en frío medido y el ajuste de sondeo se justifica con contrastes de tiempos y presupuesto; confirmar la condición operativa en la defensa.
- **C3 · Calidad, resiliencia y seguridad:** **Competente.** Umbrales medidos, scripts y pruebas de mitigación; faltan comprobación concurrente de canje, verificación del SHA en vivo y cadena bloqueante del Gate en el propio push.
- **C4 · Coherencia y trazabilidad:** **Competente provisional.** arc42/glosario, C4 y contratos navegables; 3/6 filas recorridas. No se confirmó automatización documental ni cobertura total de evidencia por fila.

## Preguntas para el jurado

1. Si dos cajas confirman el mismo código a la vez, ¿dónde está el límite transaccional que evita doble entrega y cómo demostrarían el caso concurrente?
2. Si el panel tiene 100 mostradores abiertos o se congestionan, ¿cómo mantienen presupuesto de 10 s sin aumentar carga, y qué señal justificaría reemplazar el sondeo?
3. Si falla el proveedor de correo después de cobrar, ¿qué estado ve el usuario, cómo se reintenta sin doble comprobante y qué prueba separa éxito del pago de fallo de notificación?

**Antes de cerrar:** confirmar escenario, guía y URL en SAVIO; solicitar evidencia del SHA realmente desplegado, flujo principal con datos sintéticos y error controlado pertinente, y cobertura de aspectos no recorridos.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://pideutb.iscoutb.dev/](https://pideutb.iscoutb.dev/) → HTTP 200 (13:28:12 UTC).
- API salud: [https://api-pideutb.iscoutb.dev/health](https://api-pideutb.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:10 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
