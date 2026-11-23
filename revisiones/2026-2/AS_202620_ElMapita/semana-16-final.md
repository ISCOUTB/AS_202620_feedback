# ElMapita · Revisión técnica S16
**Rama:** `main` · [`834a79c2db765f93c38fc41840e09ead5001c6df`](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/834a79c2db765f93c38fc41840e09ead5001c6df) · fecha Git 22/nov 16:19:04 UTC−06. Candidato observado inmediatamente después del corte de referencia del 22 de noviembre, 23:59:59 COT; no certifica la entrega ni la hora efectiva de SAVIO. Comparación contra [S10 `f3bcfa83e80f5c8d0e30a01b656d89160c907d64`](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/f3bcfa83e80f5c8d0e30a01b656d89160c907d64): 139 archivos, +9770/−488. La presentación y el funcionamiento previos confirmados por el docente se conservan; no equivalen a verificación funcional de esta revisión.

**Alcance:** inspección estática de objetos Git fijados, CI público y, donde hubo URL, sondas HTTPS de lectura del 23/nov a las 13:27 UTC. No se ejecutó código del equipo ni se modificaron datos. No se verificó documento guía de SAVIO, asignación docente del desafío ni revisión servida; no se califica ni se infiere la sustentación. [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) · [Contrato](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

**Publicación frente a CI:** [`README.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/README.md) no publica el enlace institucional aunque [`deploy/compose.lab.yaml`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/deploy/compose.lab.yaml) y [`docs/evidencia/final-mediciones-dokploy-2026-11-22.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/evidencia/final-mediciones-dokploy-2026-11-22.md) registran https://elmapita.iscoutb.dev como host del backend. Cliente Flutter; no se verificó publicación separada del frontend.

## Matriz S16
| Criterio | Estado y evidencia |
|---|---|
| Estado al cierre identificable | Cumple para candidato documental: rama, hash y captura indicados; entrega SAVIO por contrastar. |
| Despliegue estable | No verificado para estabilidad: /health respondió 404 (2,970 s) en la sonda; el equipo reporta 200 el 22/nov. No inferir caída general a partir de esa ruta. |
| Flujos con datos realistas | No verificado de extremo a extremo: mapa 3D, selección y ubicación se leen en frontend/mapas y en las mediciones de descarga, pero transferencia exitosa no equivale a render/uso de la UI. |
| Caminos de error | Parcial: ruta inexistente devolvió 404 (2,959 s); evidencia del equipo registra 30/30 respuestas 404 para detalle/modelo. [`backend/src/health.controller.ts`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/backend/src/health.controller.ts) contempla 503; no se forzó fallo en producción. |
| Desafío final | No verificado como asignación. EC-01 es el escenario documentado, no se afirma que sea el desafío docente. |
| Alcance entregado frente a S10 | Parcial: frente al S10 centrado en ubicación/degradación y mapa, incluye visor 3D, selección de puntos y localización, backend Dokploy y OpenAPI; login desactivado en cliente declarado en [`docs/adr/0014-login-implementado-desactivado-en-cliente.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/adr/0014-login-implementado-desactivado-en-cliente.md). No están demostrados mapa offline completo ni umbrales de FPS sobre render real; sin documento guía no se valida todo el alcance comprometido. |
| ADR y evolución | Cumple: 15 ADR numerados; 0005 sustituye el estilo inicial, 0006 el contrato inicial, 0010 fija PostgreSQL/PostGIS y 0015 consolida Dokploy. Véase [`docs/arc42/arc42-template-EN.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/arc42/arc42-template-EN.md) §9. |
| Decisión confirmada o reemplazada con evidencia | Cumple documentalmente: [`docs/adr/0015-reemplazo-adr-0012-despliegue-dokploy.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/adr/0015-reemplazo-adr-0012-despliegue-dokploy.md) enlaza cadena 0004→0012→0015, Compose y mediciones. Motivo original queda por confirmar, no prueba paridad operacional. |
| Umbrales y atributos medidos | Parcial: [`docs/evidencia/final-mediciones-dokploy-2026-11-22.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/evidencia/final-mediciones-dokploy-2026-11-22.md) reporta capas+.glb p95 1026 ms con 30 HTTP 200 frente a 5 s, red rápida sin condiciones de 10 Mbps/gama media y sin medir render. La ruta API de detalle tuvo 30 HTTP 404; Render 500. No comparar esas latencias como mejora en corridas exitosas. |
| Modos de fallo y mitigaciones probados | Parcial: backend, Flutter, contrato, Docker y docs pasaron; gitleaks, SonarCloud y gate agregado fallaron. Véanse [`docs/seguridad/escaneo-secretos-historial.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/seguridad/escaneo-secretos-historial.md) y [`docs/adr/0011-modelado-de-amenazas-y-mitigaciones.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/adr/0011-modelado-de-amenazas-y-mitigaciones.md); sin afirmar exposición en producción, login activo ni cierre de todos los modos de fallo. |
| arc42 1–12 y glosario | Cumple en estructura: [`docs/arc42/arc42-template-EN.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/arc42/arc42-template-EN.md) tiene 1–12 y glosario L716; contrastar deuda de offline y alcance del login con vistas de ejecución. |
| C4 1–3 frente a código | Parcial: [`docs/c4/C4_L1_Context.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/c4/C4_L1_Context.md), [`docs/c4/C4_L2_Container.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/c4/C4_L2_Container.md), [`docs/c4/C4_L3_Component_Backend.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/c4/C4_L3_Component_Backend.md) permiten seguir Flutter, NestJS y persistencia; L3 es backend, no demuestra en sí la correspondencia completa del cliente. |
| Trazabilidad de aspectos | Parcial: recorridas 4/4 filas EC-01…04, [`docs/aspectos.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/aspectos.md) L3–8. EC-01 tiene medición nueva en otro archivo pero fila histórica apunta a decisión sustituida; EC-02 mide placeholder, EC-03 cubre fallback backend y falta tiempo UI, EC-04 registra 0/20 offline. Se revisó además A-01 narrativo, sin equipararlo a una quinta fila EC. |
| Validación automatizada | Cumple en alcance verificado: [`.github/workflows/ci.yml`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/.github/workflows/ci.yml) valida OpenAPI/drift y el job Docs pasó; el gate global sigue fallido. |
| Contribución sustantiva de todos | No verificado para el pleno del equipo: cinco firmas Git brutas, 65 commits ago–nov (11/20/22/12 por mes); se ven aportes en app, backend, diseño y ensayos. Identidades consolidadas y reparto individual pendientes; sin datos personales. |
| Revisión cruzada técnica | No verificado: [PR #2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2) integra validación de ubicación, sin revisión humana de fondo acreditada en la consulta. |
| Demo y sustentación | No verificado. Corresponde al docente y jurado ante la instancia desplegada; sin valoración C5. |

## Matriz transversal
| Criterio | Estado y evidencia |
|---|---|
| Convención y visibilidad | Cumple: [repositorio público](https://github.com/ISCOUTB/AS_202620_ElMapita) de la organización. |
| Estructura mínima | Cumple: README, arc42, ADR, C4, aspectos y registro IA presentes. |
| Estado revisado identificable | Cumple para la referencia Git descrita; SAVIO pendiente. |
| Nombres ADR | Cumple para 15 ADR numerados, aparte de .gitkeep. |
| Inmutabilidad ADR aceptados | No verificado exhaustivamente: 0015 documenta sustitución de 0012; falta auditoría histórica completa. |
| Registro IA de cierre | No verificado para S16: el último commit observado en [`docs/ia.md`](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/ia.md) es del 9/nov; falta trazabilidad específica del cierre. |
| Pipeline, SonarCloud y Quality Gate | No cumple: [run exacto 45077520811](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/45077520811), gitleaks y Sonar en rojo, gate agregado en rojo. |
| Credenciales en archivos e historial | No verificado: gitleaks falló en run exacto; revisar resultado y rotación si corresponde, sin reproducir valores ni inferir exposición. |
| Contribución de todos | No verificado para el pleno del equipo: cinco firmas Git brutas, 65 commits ago–nov (11/20/22/12 por mes); se ven aportes en app, backend, diseño y ensayos. Identidades consolidadas y reparto individual pendientes; sin datos personales. |

## Preguntas para jurado
1. Si no existe el objeto de un piso y el .glb del campus sí responde, ¿qué ve la persona y cómo distinguen un error de datos de uno de contrato?
2. Con un equipo de gama media, red de 10 Mbps y caché vacía, ¿cómo miden tiempo a primera vista interactiva y no solo transferencias?
3. Si cae Supabase tras precargar el edificio, ¿qué información seguiría navegable y qué test falsaría esa afirmación?

## Lectura cualitativa de rúbrica

C1 y C5 quedan pendientes de la verificación del aula y la defensa. No se asignan puntajes.

- **C2:** Competente: sucesión ADR formal y ensayos de Dokploy/Render; falta comparación equivalente con rutas exitosas en ambos y se debe confirmar la motivación original.
- **C3:** Básico: controles y medición de transferencia útiles; no acredita objetivo hasta render ni offline, y fallan gitleaks/Sonar/gate.
- **C4:** Básico: arc42 completo, C4 y CI documental útiles; tabla histórica no reconciliada con las mediciones, el login y los ADR vigentes.

## Verificación independiente del corte y del despliegue

El historial de `origin/main` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.
[Diferencias frente a la revisión S10](https://github.com/ISCOUTB/AS_202620_ElMapita/compare/f3bcfa83e80f5c8d0e30a01b656d89160c907d64...834a79c2db765f93c38fc41840e09ead5001c6df); es evidencia de cambio, no medida de mérito ni certificación de alcance acordado.

**Sondas de solo lectura del 23 de noviembre:**

- salud API declarada en docs, no README: [https://elmapita.iscoutb.dev/health](https://elmapita.iscoutb.dev/health) → HTTP 404 (13:30:06 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
