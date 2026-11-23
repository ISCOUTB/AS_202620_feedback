# LaPlacita · Proyecto final S16

**Revisión técnica previa a la sustentación.** [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) · [Contrato](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

**Estado candidato:** `master` en [`69c2b5b84c95e7b96f993dc616b9d6b00b530022`](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/69c2b5b84c95e7b96f993dc616b9d6b00b530022) · commit 2026-11-22T23:03:37Z; observado en la captura de referencia del 23/11/2026 hacia las 05:00 UTC. Hora efectiva de SAVIO, entrega, URL oficial del equipo y documento guía de tres páginas no contrastados; no se sustituye esta evidencia con un tag. **Desafío S16 asignado: no verificado**; el reto técnico S10 no se presume S16.

## 1. Sistema, despliegue y alcance

Sistema de compra y recogida con PWA, tienda y administración. El README aún identifica entrega/sustentación final como pendiente (líneas 8–10 y 360); no convierte evidencias S15 en una entrega S16. [README, URLs y despliegue](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/README.md#L26-L35) · [publicación y huella](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/README.md#L263-L286).

**Comprobaciones externas de solo lectura (GET):** GET de la PWA 200 (13:27:16 UTC; 4,83 s), API `/api/v1/health` 200 y ruta inexistente 404 HTML (13:28:04 UTC; 3,88/3,87 s). El catálogo público contractual `/api/v1/catalogo/tiendas` confirmó HTTP 200 JSON (sondeo iniciado 13:31:41 UTC; 6,33 s). El primer intento de health agotó 5 s; no se obtuvo huella del SHA evaluado ni se ensayaron compra, PIN, tienda o administración con datos de prueba. Prueba puntual de disponibilidad, no de estabilidad sostenida. Sin código estudiantil ejecutado, cambios ni mutaciones. Funcionamiento completo con datos realistas y respuesta/desempeño frente al desafío quedan no verificados hasta cotejar SAVIO y demostración. El 404 acredita manejo del recurso inexistente únicamente, no todos los errores funcionales.

**[S10 `2c711d4`](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/2c711d44b31a41a09306f7840da480a21e8c749a) → [S16 `69c2b5b`](https://github.com/ISCOUTB/AS_202620_LaPlacita/compare/2c711d44b31a41a09306f7840da480a21e8c749a...69c2b5b84c95e7b96f993dc616b9d6b00b530022):** GitHub compara 110 commits y 293 archivos. S10 ESC-01 acreditó staging y señaló que el HTTP no esperaba durabilidad; ahora hay creación confirmada/reintentos, seguimiento por token, panel, administración y almacenamiento de imágenes (ADR-0025/26/28/36/37 y rutas nuevas `/api/v1/admin`). No equiparar confirmación de pedidos con éxito en concurrencia/falla. No hay notificación push/correo ni automatización de todas las transiciones (A-03); no se acredita cierre de los pendientes S15.

## 2. Decisiones y evolución

36 archivos ADR numerados observados (hay salto de 0027): ADR-0014 PostgreSQL, ADR-0016 Quality Gate, ADR-0018 retiro de Azure a Dokploy, ADR-0026 confirmación y ADR-0036 ratificación de funcionalidades de pedidos. Cotejar [ADR-0018](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/adr/0018-retiro-de-azure-despliegue-en-dokploy.md) con [ADR-0036](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/adr/0036-ratificacion-funcionalidades-de-pedidos.md) y los ensayos; una ratificación escrita no reemplaza la evidencia bajo fallo.

## 3. Calidad, resiliencia y seguridad

[S14, líneas 429–459](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/evidencias/evidencias-s14.md#L429-L459): normal 1.500/1.500, cero duplicados/pérdidas; estrés, primera de tres repeticiones: 98,4 % procesado y 1,6 % duplicado (no cumple ≥99 % y <1 %); caída de PostgreSQL: 486/600 (81 %, no cumple disponibilidad). Tres muestras públicas de lectura 1.800/1.800, no escritura ni SLO de p95. [S15](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/evidencias/evidencias-s15.md#L20-L45) no repite carga ni interrupción. Pruebas de aislamiento, persistencia y contrato; confirmar mitigaciones de pago/PII y reintentos en vivo solo con fixtures. No traslado de resultados históricos al SHA sin reejecución.

**CI en el SHA exacto, no despliegue:** [45081133410](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/45081133410) push exacto: docs (enlaces/anclas), frontend, backend, contrato, audit y scanner pasaron; [check externo exacto](https://github.com/ISCOUTB/AS_202620_LaPlacita/runs/137390243983) y [panel Sonar master](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_LaPlacita&branch=master). Workflow deploy separado no corrió para este SHA en consulta exacta: no confundir CI con publicación.

## 4. Coherencia y trazabilidad

[arc42 monolítico](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/arc42/arc42-template-EN.md), con glosario separado en la línea 1037; la sección numerada 12 está dedicada al PIN. [C4 N1/N2/N3](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/c4) presentes; revisar correspondencia de persistencia, PWA y administración con el runtime. [Aspectos 7 declarados](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/aspectos.md#L11-L19); revisé 3: A-01 requisitos→ADR→pedidos/persistencia→pruebas→series; A-02 aislamiento→ADR-0004→servicio/tests→ensayo histórico; A-03 parcial, sin escenario/umbral ni automatización de eventos. 0/3 con las ocho columnas del contrato: la tabla omite columna C4, aunque hay una segunda tabla de mapeo; 2/3 con cadena funcional documentada y 1/3 parcial.

**Transversal:** Repositorio conforme; arc42 consolidado (no exigir partición por archivo); ADR-0015 explicita historial de ediciones post-aceptación, no certificar regla global sin diffs; [registro IA](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/ia.md#L6-L14) 85 entradas reportadas, 39 validadas según equipo, actualización 22/11 pendiente de aprobación. Job audit verde no acredita por sí mismo barrido histórico de secretos completo.

**Colaboración, observación agregada:** Últimos 100 commits hasta SHA octubre 43 y noviembre 57, 3 firmas/cuentas sin reconciliar; 35 PR consultadas, 15 merges a la fecha de referencia, 0 comentarios inline devueltos. El plan S12–S15 divide frontend/backend; no valida identidad, aportes por persona o revisión sustantiva. No se emite juicio de demostración o sustentación.

## Lectura cualitativa de la rúbrica (sin puntos)

- **C2 · Decisiones y evolución:** **Competente.** Los ADR trazan evolución y decisiones explícitas; los ensayos cuantifican el trade-off, pero no acreditan mejora comparable para todos los escenarios ni recuperación bajo fallo.
- **C3 · Calidad, resiliencia y seguridad:** **Competente, con incumplimientos explícitos.** Método y artefactos reproducibles; el estrés y el fallo de BD no satisfacen el umbral de disponibilidad, y las lecturas públicas no prueban escrituras.
- **C4 · Coherencia y trazabilidad:** **Básico.** Hay validación automática de enlaces y anclas, pero no resuelve la evidencia parcial ni el vínculo C4 por fila; no se verificó la matriz completa.

## Preguntas para el jurado

1. Si se confirma el INSERT pero se pierde HTTP 201, ¿qué evita el duplicado en dos reintentos simultáneos y cómo concilian la repetición B fallida?
2. Si PostgreSQL cae cinco segundos en pico, ¿qué puede afirmar al cliente, y cómo mide tiempo de recuperación sin perder pedidos?
3. Si una tienda concentra 50 % del tráfico y el almacén de imágenes cae, ¿cómo separaría aislamiento, degradación de catálogo y confirmación de pedidos?

**Antes de cerrar:** confirmar escenario, guía y URL en SAVIO; solicitar evidencia del SHA realmente desplegado, flujo principal con datos sintéticos y error controlado pertinente, y cobertura de aspectos no recorridos.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://laplacita-app.iscoutb.dev/](https://laplacita-app.iscoutb.dev/) → HTTP 200 (13:28:11 UTC).
- API prueba salud: [https://laplacita-test.iscoutb.dev/api/v1/health](https://laplacita-test.iscoutb.dev/api/v1/health) → HTTP 200, estado declarado `ok` (13:28:10 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
