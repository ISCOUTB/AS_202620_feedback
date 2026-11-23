# EnAgenda · Revisión técnica S16
**Rama:** `master` · [`a6dde3025c6864eb8c2871c6e9732b205f68001b`](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/a6dde3025c6864eb8c2871c6e9732b205f68001b) · fecha Git 25/oct 22:57:38 COT. Candidato observado inmediatamente después del corte de referencia del 22 de noviembre, 23:59:59 COT; no certifica la entrega ni la hora efectiva de SAVIO. Comparación contra [S10 `4bec22f3821493014e8352ece8274bb2950e97db`](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/4bec22f3821493014e8352ece8274bb2950e97db): 60 archivos, +4069/−145. `25484af` lleva fecha 22/nov 23:57:14 COT en rama lateral, no es la punta principal contemporánea. En primer padre, `a6dde30 → 4a78873 → 9f972bc → 24cf01a → f728124`; los posteriores son del 23/nov desde las 00:14, y [PR #6](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/6) fusionó el rediseño a las 00:44 COT. No se incorpora ese material en la evaluación del candidato.

**Alcance:** inspección estática de objetos Git fijados, CI público y, donde hubo URL, sondas HTTPS de lectura del 23/nov a las 13:27 UTC. No se ejecutó código del equipo ni se modificaron datos. No se verificó documento guía de SAVIO, asignación docente del desafío ni revisión servida; no se califica ni se infiere la sustentación. [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) · [Contrato](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

**Publicación frente a CI:** [`README.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) L305–315 informa contenedor en Dokploy sin URL pública; [`docs/despliegue/medicion-dokploy.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/despliegue/medicion-dokploy.md) confirma que falta host. App web Flask/Jinja, no sitio y API independientes acreditados.

## Matriz S16
| Criterio | Estado y evidencia |
|---|---|
| Estado al cierre identificable | Cumple para candidato documental: rama, hash y captura indicados; entrega SAVIO por contrastar. |
| Despliegue estable | No verificado: sin host documentado no hay sonda; no es prueba de caída. |
| Flujos con datos realistas | No verificado en vivo. [`app/web.py`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/app/web.py) L128–362 implementa registro/acceso, eventos e invitaciones/RSVP; confirmar con usuarios y datos realistas sin inferir que el entorno público existe. |
| Caminos de error | No verificado en despliegue; [`tests/test_api_invitaciones.py`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/tests/test_api_invitaciones.py) y [`app/web.py`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/app/web.py) documentan controles de invitación/vigencia; el CI principal no pasó. |
| Desafío final | No verificado: ni desafío asignado ni línea base S16 acreditados; no usar el ejercicio de simulación como sustituto. |
| Alcance entregado frente a S10 | Parcial: S10 centrado en invitaciones y observabilidad; se añaden autenticación, eventos, invitación por evento, persistencia PostgreSQL y taller aislado. [`README.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/README.md) L38–67 todavía promete tareas, gastos, agenda y elementos y dice memoria; no acredita entrega/recorte explícito de todo. No trasladar rediseño del PR #6. |
| ADR y evolución | Cumple en trazabilidad parcial: monolito modular → API integrada → Dokploy → persistencia SQL/taller aislado: [`docs/adr/0001-usar-monolito-modular.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/adr/0001-usar-monolito-modular.md), [`docs/adr/0002-estrategia-integracion-api.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/adr/0002-estrategia-integracion-api.md) y [`docs/adr/0004-persistir-datos-en-postgresql.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/adr/0004-persistir-datos-en-postgresql.md). |
| Decisión confirmada o reemplazada con evidencia | Parcial: ADR PostgreSQL describe migración e integración, pero el README describe memoria y no se confirma una sustitución formal o evidencia comparada en producción. |
| Umbrales y atributos medidos | No verificado: [`docs/despliegue/medicion-dokploy.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/despliegue/medicion-dokploy.md) fija umbral y procedimiento de disponibilidad/latencia, pero documenta medición externa pendiente. |
| Modos de fallo y mitigaciones probados | Parcial: [`docs/arc42/08-conceptos-transversales.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/arc42/08-conceptos-transversales.md) describe consistencia/caché y fallos; pruebas y taller existen, pero el run de taller verde no sustituye el principal fallido ni valida seguridad operativa. |
| arc42 1–12 y glosario | Cumple en estructura: 12 ficheros numerados, incluido [`docs/arc42/12-glosario.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/arc42/12-glosario.md); contraste de la vista con PostgreSQL/README es parcial. |
| C4 1–3 frente a código | Parcial: [`docs/c4/nivel-1-contexto.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/c4/nivel-1-contexto.md), [`docs/c4/nivel-2-contenedores.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/c4/nivel-2-contenedores.md) y [`docs/c4/nivel-3-componentes.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/c4/nivel-3-componentes.md) describen invitaciones/Flask; no aseguran trazabilidad completa de autenticación/eventos y persistencia efectiva. |
| Trazabilidad de aspectos | Parcial: 6/6 filas A-01…06 leídas en [`docs/aspectos.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/aspectos.md) L5–12. A-01 token, A-04 RSVP y A-06 contrato enlazan código/pruebas; el mismo corte vertical para las seis y falta cobertura de módulos posteriores. |
| Validación automatizada | Parcial: [`.github/workflows/ci.yml`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/.github/workflows/ci.yml) declara contrato OpenAPI y Docker, pero el paso pytest falló; no se verificó un validador de C4/enlaces ejecutado en este candidato. |
| Contribución sustantiva de todos | No verificado para todo el equipo: cuatro firmas Git brutas, 187 commits ago–oct (119/43/25); cambios de código, persistencia y pruebas. Falta cruzar aliases y responsabilidades con EQUIPOS; junio/noviembre no se infieren de ramas posteriores. |
| Revisión cruzada técnica | No verificado: [PR #3](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/3) integra S12 sin revisiones en el registro consultado; PR #6 posterior se conserva fuera. |
| Demo y sustentación | No verificado. Corresponde al docente y jurado ante la instancia desplegada; sin valoración C5. |

## Matriz transversal
| Criterio | Estado y evidencia |
|---|---|
| Convención y visibilidad | Cumple: [repositorio público](https://github.com/ISCOUTB/AS_202620_EnAgenda) de la organización. |
| Estructura mínima | Cumple presencia: README, 12 arc42, ADR, C4, aspectos, IA. |
| Estado revisado identificable | Cumple para la referencia Git descrita; SAVIO pendiente. |
| Nombres ADR | Verificado el patrón de nombres de los cinco ficheros; comprobar si dos decisiones comparten 0004 antes de atribuir identidad inequívoca. |
| Inmutabilidad ADR aceptados | No verificado para todo historial; quedan tensiones de transición entre documentación de memoria y persistencia. |
| Registro IA de cierre | No verificado para S16: [`docs/ia.md`](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/a6dde3025c6864eb8c2871c6e9732b205f68001b/docs/ia.md) se actualizó por última vez el 25/oct en el candidato. |
| Pipeline, SonarCloud y Quality Gate | No cumple para CI integral: [taller 40266609284](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609284) verde y [CI 40266609410](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40266609410) falla en pruebas; sin gate público confirmado. |
| Credenciales en archivos e historial | No verificado; no se examinó todo el historial con scanner independiente. |
| Contribución de todos | No verificado para todo el equipo: cuatro firmas Git brutas, 187 commits ago–oct (119/43/25); cambios de código, persistencia y pruebas. Falta cruzar aliases y responsabilidades con EQUIPOS; junio/noviembre no se infieren de ramas posteriores. |

## Preguntas para jurado
1. Si dos respuestas concurrentes modifican una invitación al borde de su vencimiento, ¿qué persiste y cómo lo prueban?
2. ¿Qué puede hacer el invitado si falla PostgreSQL después de generar un enlace? ¿Cómo distinguen fallo de expiración?
3. Si migran de un prototipo aislado de mensajes a notificaciones reales, ¿qué parte del contrato preserva idempotencia y qué medirían primero?

## Lectura cualitativa de rúbrica

C1 y C5 quedan pendientes de la verificación del aula y la defensa. No se asignan puntajes.

- **C2:** Básico: reconstrucción de monolito/modularidad e introducción de PostgreSQL; README todavía describe memoria y no acredita ratificación con evidencia comparada.
- **C3:** Básico: controles y prueba del prototipo, pero falla CI principal y falta medición externa contra umbrales.
- **C4:** Básico: doce secciones arc42 y tres niveles C4, pero la tabla se limita a invitaciones y la transición a persistencia/organizador no es coherente en toda la evidencia.

## Verificación independiente del corte y del despliegue

El commit 25484af tiene fecha local 23:57, pero el primer padre y el [PR #6](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/6) lo sitúan en integración posterior al corte (00:44 COT). No se incorpora a esta entrega.
[Diferencias frente a la revisión S10](https://github.com/ISCOUTB/AS_202620_EnAgenda/compare/4bec22f3821493014e8352ece8274bb2950e97db...a6dde3025c6864eb8c2871c6e9732b205f68001b); es evidencia de cambio, no medida de mérito ni certificación de alcance acordado.

**Sondas de solo lectura del 23 de noviembre:**

- No se probó una URL pública: el README del candidato no identifica un destino apto para la sonda. Solicitar la URL entregada en SAVIO, sin inferir falta de implementación.

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
