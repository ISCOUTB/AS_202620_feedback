# LostVault · Proyecto final S16

**Revisión técnica previa a la sustentación.** [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) · [Contrato](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

**Estado candidato:** `main` en [`c54471bfb164c3825010d51b9ad9a246fad99ff7`](https://github.com/ISCOUTB/AS_202620_LostVault/commit/c54471bfb164c3825010d51b9ad9a246fad99ff7) · commit 2026-11-23T04:56:30Z; observado en la captura de referencia del 23/11/2026 hacia las 05:00 UTC. Hora efectiva de SAVIO, entrega, URL oficial del equipo y documento guía de tres páginas no contrastados; no se sustituye esta evidencia con un tag. **Desafío S16 asignado: no verificado**; el reto técnico S10 no se presume S16.

## 1. Sistema, despliegue y alcance

La entrega documenta API pública en Vercel; Flutter se ejecuta localmente. No presentar API pública como sistema Flutter desplegado. [README: API remota, Flutter local](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/README.md#L3-L7) · [arc42 despliegue](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/arc42/07_vista_despliegue.md#L9-L36) · [contrato versionado](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/contracts/lostvault-api.yaml#L42).

**Comprobaciones externas de solo lectura (GET):** 13:28:04 UTC (23 nov): `/health` 200 (2,75 s), `/objects` 200 JSON (2,71 s) y ruta inexistente 404 JSON (2,72 s); con límite inicial 5 s hubo timeouts. A las 13:28:31 UTC la ruta `/v1/objects` dio 404, mientras la pública documentada `/objects` sí respondía. No se probó reclamación/autenticación en producción ni hay huella del candidato. No se inspeccionaron registros de usuarios. Sin código estudiantil ejecutado, cambios ni mutaciones. Funcionamiento completo con datos realistas y respuesta/desempeño frente al desafío quedan no verificados hasta cotejar SAVIO y demostración. El 404 acredita manejo del recurso inexistente únicamente, no todos los errores funcionales.

**[S10 `99fb413`](https://github.com/ISCOUTB/AS_202620_LostVault/commit/99fb413bda00c208ec42104dcfe6a4c189fbad77) → [S16 `c54471b`](https://github.com/ISCOUTB/AS_202620_LostVault/compare/99fb413bda00c208ec42104dcfe6a4c189fbad77...c54471bfb164c3825010d51b9ad9a246fad99ff7):** 31 commits y 65 archivos frente a S10. Se pasó de una comparación Vercel/proxy no equivalente y dudas del p95 en memoria a medición extremo a extremo documentada, reforzando API/pruebas; aparece diseño de reclamaciones con outbox y contratos de eventos. No dar por desplegado el worker o el recorrido Flutter. Validación de identidad verifica que el identificador tiene contenido; verificación documental queda fuera.

## 2. Decisiones y evolución

8 archivos ADR; [ADR-0003 Vercel](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/adr/0003-plataforma-despliegue-vercel.md) frente a la medición pública del propio equipo; [ADR-0007](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/adr/0007-notificacion-asincrona-outbox.md#L22-L75) compara síncrono vs outbox con costo/entrega y residual; [ADR-0006](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/adr/0006-postgresql-fuente-de-verdad.md) fija fuente de verdad. Confirmación parcial de Vercel: escala pero falla primera ráfaga al objetivo, no afirmar ratificación global.

## 3. Calidad, resiliencia y seguridad

[S14 método/datos](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/medicion/s14-medicion-atributos.md#L4-L48): a ~200 usuarios contra umbral p95 ≤2.000 ms, precalentado 1.867 ms salva por ~7 %, primera ráfaga 2.279 ms incumple, 0 errores en 3.000 búsquedas reportadas. La métrica por instancia no reemplaza extremo a extremo. [AS-03](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/aspectos.md#L7) prueba JWT ausente/inválido/vencido y reclamación; no acredita verificación documental. [Amenazas](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/seguridad/amenazas-dependencias-privacidad.md#L7-L52) documentan control de tasa y actualización/auditoría de dependencias pendientes en esa evidencia; no inferir que la versión actual está vulnerada.

**CI en el SHA exacto, no despliegue:** Push exacto [Flutter](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/45114779269), [Backend/contrato](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/45114779292) y [Build/Sonar](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/45114779328) pasaron, incluido paso Quality Gate del último; [check externo](https://github.com/ISCOUTB/AS_202620_LostVault/runs/137495603185) · [panel Sonar main](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_LostVault&branch=main). No verifican despliegue Flutter ni ejecución de worker.

## 4. Coherencia y trazabilidad

[arc42](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/arc42) tiene 01–11 y `glosario.md`; [C4 N1–N3](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/c4). [Aspectos](https://github.com/ISCOUTB/AS_202620_LostVault/blob/c54471bfb164c3825010d51b9ad9a246fad99ff7/docs/aspectos.md#L5-L8): 2/2 declarados muestreados (no hay tercera fila): AS-03 seguridad→ADR-0002→FastAPI y Flutter→tests con alcance limitado; AS-04 rendimiento→Vercel→búsqueda/métricas→prueba p95→series reproducibles. 0/2 formalmente completos en la matriz exigida, porque falta enlace C4 por fila; diferencia documentada `/objects` vs `/v1/objects`. No se encontró un paso específico de validación automática de diagramas/enlaces en los tres jobs exactos; pruebas del contrato sí.

**Transversal:** Repositorio conforme y documentación mínima presente. `000.3-despliegue-busqueda-lostvault.md` no cumple numeración; historial completo de ADR aceptados no verificado. `docs/ia.md` líneas 383–393 explicita no confundir p95 estable y global y qué afirmación se rechazó; actualización en semana de cierre y validación de todo el registro no acreditadas. No se acreditó barrido histórico de credenciales.

**Colaboración, observación agregada:** Últimos 100 commits: septiembre 61, octubre 20, noviembre 19; 5 firmas/cuentas sin reconciliar. 26 PR consultadas hasta corte, 23 merges, 0 comentarios inline devueltos. Sin equivalencia oficial cuenta/persona o evidencia suficiente para atribuir contribución sustantiva a todo el grupo. No se emite juicio de demostración o sustentación.

## Lectura cualitativa de la rúbrica (sin puntos)

- **C2 · Decisiones y evolución:** **Competente.** Hay decisiones alternativas, consecuencias y contraste parcial de Vercel. Outbox no se ratifica como flujo desplegado completo.
- **C3 · Calidad, resiliencia y seguridad:** **Básico.** El escenario cumple estabilizado pero falla en la primera ráfaga. Hay pruebas de autenticación; no se acredita verificación documental ni operación del worker en producción.
- **C4 · Coherencia y trazabilidad:** **Básico.** C4 y arc42 presentes, pero las dos filas no enlazan C4, existe diferencia entre rutas públicas y contrato versionado y no se identificó validación automática de documentación.

## Preguntas para el jurado

1. ¿Qué cambia para cumplir p95 en la primera ráfaga de 200 y cómo repetirían el ensayo con idéntico estímulo y control de caché?
2. Si el proveedor de correo falla una hora, ¿qué persiste, quién reintenta, cómo demuestra deduplicación y cómo se detecta una cola estancada?
3. Si contrato del cliente solicita `/v1/objects` y la ruta pública es `/objects`, ¿cómo aseguran compatibilidad al cambiar proveedor y qué prueba desplegada debería fallar?

**Antes de cerrar:** confirmar escenario, guía y URL en SAVIO; solicitar evidencia del SHA realmente desplegado, flujo principal con datos sintéticos y error controlado pertinente, y cobertura de aspectos no recorridos.

## Verificación independiente del corte y del despliegue

El historial de `origin/main` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- host API externo: [https://backend-nu-self-91.vercel.app/](https://backend-nu-self-91.vercel.app/) → HTTP 200, estado declarado `online` (13:28:10 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
