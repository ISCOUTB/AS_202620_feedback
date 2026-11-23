# GimnasioUTB · Revisión técnica S16
**Rama:** `main` · [`5a1044133267d7018714741211e0f3c0354815ec`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/5a1044133267d7018714741211e0f3c0354815ec) · fecha Git 22/nov 23:58:03 COT. Candidato observado inmediatamente después del corte de referencia del 22 de noviembre, 23:59:59 COT; no certifica la entrega ni la hora efectiva de SAVIO. Comparación contra [S10 `46742e5feaa3c8a06b7aebeb7a31fb93628e40b6`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6): 191 archivos, +17733/−820. El CI exacto se inició a 04:58:11 UTC, un indicio adicional de que este push antecede al corte de referencia.

**Alcance:** inspección estática de objetos Git fijados, CI público y, donde hubo URL, sondas HTTPS de lectura del 23/nov a las 13:27 UTC. No se ejecutó código del equipo ni se modificaron datos. No se verificó documento guía de SAVIO, asignación docente del desafío ni revisión servida; no se califica ni se infiere la sustentación. [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) · [Contrato](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

**Publicación frente a CI:** [`README.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/README.md) L65–85 documenta API https://gimnasio-utb.iscoutb.dev, PostgreSQL propio y login local tras revertir el intento Supabase. Cliente Flutter en docs/Flutter, no publicación independiente acreditada.

## Matriz S16
| Criterio | Estado y evidencia |
|---|---|
| Estado al cierre identificable | Cumple para candidato documental: rama, hash y captura indicados; entrega SAVIO por contrastar. |
| Despliegue estable | No verificado como estabilidad general; observados /health 200 (3,757 s) y /ready 200 (3,759 s), sin verificar SHA servido ni disponibilidad prolongada. |
| Flujos con datos realistas | Parcial: /api/v1/aforo dio 200 (3,749 s); no se probó ingreso/salida, login, QR/cédula ni alertas en vivo. [`src/modules/aforo/infrastructure/http/aforo.router.js`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/src/modules/aforo/infrastructure/http/aforo.router.js) define flujos. |
| Caminos de error | Parcial: ruta inexistente devolvió 404 (3,750 s); pruebas estáticas de aforo/readiness y seguridad existen, no se indujo fallo de DB ni se escribió en producción. |
| Desafío final | No verificado como asignación del aula; escenario visible de consistencia y cambios ADR-0012 no se equiparan a reto asignado. |
| Alcance entregado frente a S10 | Parcial: S10 aforo y concurrencia PostgreSQL evolucionan a estado/capacidad, QR, identidad local y alertas. [`docs/adr/0012-estado-capacidad-y-registro-por-cedula.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/adr/0012-estado-capacidad-y-registro-por-cedula.md) delimita no histórico/estadísticas; no se da por entregado WebSocket/FCM ni historial append-only. Guía SAVIO pendiente. |
| ADR y evolución | Cumple sobre la evolución documentada: hexagonal, FOR UPDATE, identidad QR, Supabase y regreso al perfil PostgreSQL/identidad local. [`docs/arc42/arc42_gimnasio_utb.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/arc42/arc42_gimnasio_utb.md) §9. |
| Decisión confirmada o reemplazada con evidencia | Cumple documentalmente: [`docs/adr/0011-volver-a-postgresql-propio-y-login-local.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/adr/0011-volver-a-postgresql-propio-y-login-local.md) explica sustitución de 0009/0010; [`README.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/README.md) L85 registra intento Supabase sin deploy funcional, no benchmark comparativo. |
| Umbrales y atributos medidos | Parcial: [`docs/arc42/arc42_gimnasio_utb.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/arc42/arc42_gimnasio_utb.md) L367–405 documenta 20/20 sobre adapter PostgreSQL (histórico, sin salida original), no carga HTTP ni frescura Q3 de 2 s; latencia de la sonda no mide Q3. |
| Modos de fallo y mitigaciones probados | Parcial: [`tests/seguridad.test.js`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/tests/seguridad.test.js), [`tests/health.test.js`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/tests/health.test.js) y [`tests/postgres/aforo-postgres.integration.test.js`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/tests/postgres/aforo-postgres.integration.test.js) cubren controles, readiness, concurrencia/rollback en fuentes; exacto CI no acredita Postgres real ni Flutter. [`README.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/README.md) describe roles DB separados. |
| arc42 1–12 y glosario | Cumple estructura: [`docs/arc42/arc42_gimnasio_utb.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/arc42/arc42_gimnasio_utb.md) tiene 1–12, glosario L476; mantiene explícita evidencia histórica y deuda. |
| C4 1–3 frente a código | Parcial: [`docs/c4/c4_level1.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/c4/c4_level1.md), [`docs/c4/c4_level2.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/c4/c4_level2.md), [`docs/c4/C4_Level3.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/c4/C4_Level3.md) representan API/DB/hexagonal; contrastar cobertura de identidad, medios de registro y avisos en nivel 3. |
| Trazabilidad de aspectos | Verificada 1/1 fila principal de [`docs/aspectos.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/aspectos.md): S1 pasa de estímulo a ADR-0004, dominio, adapter y suite; no hay tres filas declaradas. Otros atributos en arc42 no reciben automáticamente esa misma cobertura. |
| Validación automatizada | Cumple en alcance: [`.github/workflows/ci.yml`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/.github/workflows/ci.yml) L21–29 ejecuta contrato, fitness functions arch:check y cadena de suministro; sin evidencia de generación automática de C4. |
| Contribución sustantiva de todos | No verificado para el pleno: ocho firmas Git brutas, 164 commits ago–nov (72/27/36/29); aportes diferenciados en Flutter, identidad, documentación y backend. Consolidación de aliases/reparto pendientes. |
| Revisión cruzada técnica | No verificado: historial de merges local no acredita comentarios técnicos cruzados; no inferir revisión humana. |
| Demo y sustentación | No verificado. Corresponde al docente y jurado ante la instancia desplegada; sin valoración C5. |

## Matriz transversal
| Criterio | Estado y evidencia |
|---|---|
| Convención y visibilidad | Cumple: [repositorio público](https://github.com/ISCOUTB/AS_202620_GimnasioUTB) de la organización. |
| Estructura mínima | Cumple presencia de README, ADR, arc42, C4, aspectos, IA. |
| Estado revisado identificable | Cumple para la referencia Git descrita; SAVIO pendiente. |
| Nombres ADR | No cumple uniformidad: [`docs/adr/ADR0001.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/adr/ADR0001.md) queda fuera del patrón NNNN-kebab-case; se distingue de la serie normalizada. |
| Inmutabilidad ADR aceptados | No verificado en todo historial; reversión 0011 a 0009/0010 está declarada. |
| Registro IA de cierre | Parcial: [`docs/ia.md`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/ia.md) actualizado el 22/nov; confirmar comprobaciones y descartes de todo el tramo final. |
| Pipeline, SonarCloud y Quality Gate | Parcial: [run exacto 45114911596](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/45114911596) verde para Node, contrato, arquitectura y dependencias. Flutter y Sonar/Quality Gate exacto no acreditados. |
| Credenciales en archivos e historial | No verificado en todo historial; .env.example y gestión por panel no sustituyen el escaneo. |
| Contribución de todos | No verificado para el pleno: ocho firmas Git brutas, 164 commits ago–nov (72/27/36/29); aportes diferenciados en Flutter, identidad, documentación y backend. Consolidación de aliases/reparto pendientes. |

## Preguntas para jurado
1. Con aforo a un cupo del máximo y dos lecturas simultáneas de QR, ¿cuál transición resulta válida y por qué no se consume el QR rechazado?
2. Si se pierde el volumen de PostgreSQL al volver a desplegar, ¿qué recuperan y cómo medirían RTO y RPO?
3. ¿Cómo distinguirían atraso >2 s en la lectura de una demora de red y qué cambiaría al implementar alertas con dos instancias?

## Lectura cualitativa de rúbrica

C1 y C5 quedan pendientes de la verificación del aula y la defensa. No se asignan puntajes.

- **C2:** Competente: ADR de reversión y cambios de dominio se vinculan con estructura y código; no demuestra con cifras comparables la elección de plataforma.
- **C3:** Básico: integración histórica de PostgreSQL y señales operativas; frescura y carga HTTP no medidas, y el CI exacto no valida cliente ni PostgreSQL vivo.
- **C4:** Competente en evidencia estática: arc42 y tres niveles, una traza S1 y fitness functions en verde; falta verificar cobertura documental de identidad/avisos y la generación automática de los diagramas.

## Verificación independiente del corte y del despliegue

El historial de `origin/main` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.
[Diferencias frente a la revisión S10](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/compare/46742e5feaa3c8a06b7aebeb7a31fb93628e40b6...5a1044133267d7018714741211e0f3c0354815ec); es evidencia de cambio, no medida de mérito ni certificación de alcance acordado.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://gimnasio-utb.iscoutb.dev/](https://gimnasio-utb.iscoutb.dev/) → HTTP 200, estado declarado `ok` (13:28:09 UTC).
- salud: [https://gimnasio-utb.iscoutb.dev/health](https://gimnasio-utb.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:09 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
