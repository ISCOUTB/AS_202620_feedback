# PROYECTO_CAMPUSMARKET · Proyecto final S16

**Revisión técnica previa a la sustentación.** [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) · [Contrato](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

**Estado candidato:** `master` en [`c79c73d47936790b0f248bdea5c0a700ce8fe017`](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/c79c73d47936790b0f248bdea5c0a700ce8fe017) · commit 2026-11-09T06:27:11Z; observado en la captura de referencia del 23/11/2026 hacia las 05:00 UTC. Hora efectiva de SAVIO, entrega, URL oficial del equipo y documento guía de tres páginas no contrastados; no se sustituye esta evidencia con un tag. **Desafío S16 asignado: no verificado**; el reto técnico S10 no se presume S16.

## 1. Sistema, despliegue y alcance

Marketplace institucional, API FastAPI/MySQL más Flutter Web servido desde el mismo contenedor. El último candidato documental no es el origen de la imagen desplegada citada. [README, fotografía y topología](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/README.md#L1-L20) · [cierre productivo histórico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/evidencias/cierre-productivo-incremento2-2026-11-03.md#L5-L46) · [auditoría documental y separación de runtime](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/evidencias/auditoria-documental-s1-s14-2026-11-08.md#L13-L22).

**Comprobaciones externas de solo lectura (GET):** 23 nov 13:28:04 UTC: `/app/` 200 HTML (2,95 s), `/health` 200 JSON (3,00 s), `/universidades` 200 JSON (3,06 s); un recurso inexistente a 13:27:16 UTC retornó 404 JSON (4,85 s). Un sondeo adicional de `/catalogo` devolvió 200 JSON (serie iniciada 13:31:41 UTC; 4,32 s). La propia fotografía del README registró `/universidades` 500 el 8 nov; esta lectura posterior 200 no contradice que fallara antes ni demuestra reparación estable. No se probaron compra/registro, favoritos o mensajería; revisar huella/runtime y fixture sin datos personales. Sin código estudiantil ejecutado, cambios ni mutaciones. Funcionamiento completo con datos realistas y respuesta/desempeño frente al desafío quedan no verificados hasta cotejar SAVIO y demostración. El 404 acredita manejo del recurso inexistente únicamente, no todos los errores funcionales.

**[S10 `1582c1f`](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/1582c1ff609202fa2cc4a06fa14d18b9b61bed74) → [S16 `c79c73d`](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/compare/1582c1ff609202fa2cc4a06fa14d18b9b61bed74...c79c73d47936790b0f248bdea5c0a700ce8fe017):** 245 commits y 159 archivos frente al S10 evaluado. Línea base S10: contrato v2 conservado ante consumidor incompatible y recuperación 200→422→200. En S16 se añaden Favoritos, mensajería y afiliación visible; promoción por digest y pruebas Web/Android en CI. El equipo declaró sin acreditar captura de afiliación no nula al crear anuncio, restauración SQL/fotos y rollback productivo; no presentar esos faltantes como resueltos por el incremento.

## 2. Decisiones y evolución

26 ADR: monolito/SQLite/MySQL, Azure y luego Dokploy/volúmenes, decisión de no extraer catálogo y publicación reproducible. [ADR-0020](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/adr/0020-preservar-contrato-v2-y-adaptar-consumidor-incompatible.md#L5-L41) confirma 0003/0009 contra línea base con muestras; [ADR-0024](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/adr/0024-publicar-imagen-verificada-y-condicionar-promocion.md#L21-L48) detalla gates por imagen/digest, ejecuciones y límites, sin probar rollback de producción.

## 3. Calidad, resiliencia y seguridad

[EC-01](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/evidencias/evidencia-s14-ec01-2026-11-05.md#L93-L127): 4 series HTTP 10/10 ante umbral visible ≥9/10≤2 s en 1.000 publicaciones; un Chrome 6/10 y luego no concluyente por observador/preparación; no acredita latencia visible ni EC-01 público. Sesiones opacas revocables, fotos reencodificadas y CI Gitleaks/contrato son controles verificables, no ausencia de incidentes. El run público exacto falló (registró 6/9 y catálogo válido 503 en [IA, última auditoría](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/ia.md#L817-L825)); no se repitió el experimento ni es diagnóstico de caída actual.

**CI en el SHA exacto, no despliegue:** Exactos de push [backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110636), [Flutter](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110702), [Compose](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110841) y [flujos Web/Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110863) verdes; [contrato HTTPS público](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/42573110656) **falló**; job EC-01 omitido en Compose. [Sonar externo exacto](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/runs/129023374055) verde, [panel](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_PROYECTO_CAMPUSMARKET&branch=master), pero no se certificó mismo SHA, scanner y Gate público bloqueante como una sola cadena. No usar CI como publicación.

## 4. Coherencia y trazabilidad

[arc42 consolidado](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/arc42/ARC42.md) índice §§1–12/glosario y [C4](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/c4) Markdown/PlantUML/SVG N1–N3. [Matriz aspectos](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/c79c73d47936790b0f248bdea5c0a700ce8fe017/docs/aspectos.md#L27-L42): 3/14 recorridos (ASP-01 catálogo/EC-01→ADR-0009/19→servicios/tests y medición parcial; ASP-02 protección→ADR-0012→sesiones/publicaciones/pruebas; ASP-07 EC-06→ADR-0003→OpenAPI/tests/experimento). Las tres son navegables; no afirmar 14/14. Existe verificador documental versionado y auditoría reproducible, pero no se acreditó un job de documentación aislado en runs exactos.

**Transversal:** Repositorio y estructura conforme; ADR numerados, historia de inmutabilidad no verificada. Registro IA actualizado con criterio de rechazo. Backend CI ejecutó barrido de checkout e historial con Gitleaks y preservó informes redactados, acotado al procedimiento; no se imprimieron valores. Pendiente confirmar Gate bloqueante y grupo persona/cuenta.

**Colaboración, observación agregada:** Muestra de últimos 100 commits, todos noviembre, dos firmas/cuentas sin reconciliar (no representa el semestre completo); 92 PR localizadas, 89 merges al corte, 0 comentarios inline devueltos. PR #85–90 documentan la secuencia de integración, no bastan para asignar autoría nominal ni revisión cruzada sustantiva. No se emite juicio de demostración o sustentación.

## Lectura cualitativa de la rúbrica (sin puntos)

- **C2 · Decisiones y evolución:** **Sobresaliente en la decisión acotada del contrato; propuesta general competente.** ADR-0020 confirma su táctica con rechazo/recuperación medidos, pero el run público del cierre falla y no se acreditó recuperación productiva de la estrategia posterior.
- **C3 · Calidad, resiliencia y seguridad:** **Básico.** Respaldo de pruebas y controles; la métrica visible prioritaria y el contrato público del candidato no quedan acreditados. No confundir medición HTTP parcial con cumplimiento completo.
- **C4 · Coherencia y trazabilidad:** **Competente provisional.** Las tres cadenas muestreadas enlazan requisitos, C4, ADR, código, pruebas y evidencia; 11/14 no recorridas y no se acreditó automatización documental en CI exacta.

## Preguntas para el jurado

1. Si el contrato público vuelve a devolver 503 mientras `/health` sigue OK, ¿qué señal y qué umbral impedirían promover o activarían rollback?
2. Si hay que restaurar MySQL y el volumen de fotos en otros momentos, ¿qué orden de recuperación conserva consistencia? ¿Cómo demostrarlo sin tocar datos reales?
3. ¿Qué medirían en Chrome para distinguir demora visible de un observador defectuoso y qué cambia cuando catálogo, filtros, imágenes y navegación compiten por recursos?

**Antes de cerrar:** confirmar escenario, guía y URL en SAVIO; solicitar evidencia del SHA realmente desplegado, flujo principal con datos sintéticos y error controlado pertinente, y cobertura de aspectos no recorridos.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://campusmarket.iscoutb.dev/app/](https://campusmarket.iscoutb.dev/app/) → HTTP 200 (13:28:09 UTC).
- salud: [https://campusmarket.iscoutb.dev/health](https://campusmarket.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:09 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
