# Primer corte S5 · mapsutb

> Revisión manual con **excepción docente**: se aceptan para S5 las correcciones
> incorporadas durante esta semana aunque sean posteriores al cierre original. S2
> conserva su evaluación histórica. S5 sigue siendo un compendio S1--S4: no evalúa
> un reto ni una restricción nueva.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Hash histórico de corte | `origin/master` [`e8bad4c`](https://github.com/ISCOUTB/AS_202620_mapsutb/tree/e8bad4c286e5b985b324234b644e3b1fe961b626) · 2026-09-09T18:34:48-05:00 |
| Estado aceptado excepcionalmente para S5 | `origin/master` [`8aee879`](https://github.com/ISCOUTB/AS_202620_mapsutb/tree/8aee87957c958b8602c5d964ac194d3d13752412) · 2026-09-13T18:14:14-05:00 |
| Regla aplicada | Correcciones posteriores aceptadas por indicación docente; no se usaron etiquetas. |
| Revisor | revisión manual de evidencias públicas |

## Matriz del corte

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | [`e8bad4c`](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/e8bad4c286e5b985b324234b644e3b1fe961b626) en `master` | Cumple | El hash histórico es identificable y anterior al cierre; las correcciones se aceptan por la excepción documentada arriba. |
| `correcciones.md` existe en la raíz del estado calificado | [`correcciones.md`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/correcciones.md) | Cumple | El archivo existe en la raíz desde el hash histórico y se conserva en la punta aceptada. |
| Correcciones trazables y contrastadas | [`correcciones.md:27-88`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/correcciones.md#L27-L88), contraste abajo | Cumple | El índice identifica origen, acción, rutas y estado. Se contrastaron además las correcciones de esta semana, aunque el índice aún conserve algunos estados previos. |
| S1 al día: equipo, problema y repositorio | [`ficha_problema.md:8-40`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/ficha_problema.md#L8-L40) | Cumple | Problema, alcance sin RA, dos tensiones y la relación con los ADR están alineados con la arquitectura actual. |
| S2 al día: escenarios de calidad y restricciones | [`escenarios_calidad.md`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/escenarios_calidad.md), [`02_architecture_constraints.adoc`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/arc42/02_architecture_constraints.adoc) | Cumple | Los cinco escenarios ya usan las seis partes y medidas; las restricciones se mantienen clasificadas. El árbol aún es una priorización básica, aceptada en esta revisión laxa. |
| S3 al día: estrategia de solución y decisiones | [`04_solution_strategy.adoc`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/arc42/04_solution_strategy.adoc), [`ADR 0004`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/adr/0004-adoptar-monolito-como-estilo-arquitectonico.md) | Cumple | La estrategia enlaza escenarios y tácticas; ADR 0004 añade una comparación explícita de tres estilos contra el árbol de utilidad y formaliza el monolito elegido. |
| S4 al día: arc42, C4 y corte vertical | [C4 nivel 1](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/c4/C1.md), [nivel 2](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/c4/C2.md), [`main.dart`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/lib/main.dart) | Cumple | C4 está como código, las rutas están normalizadas y C2 declara los contenedores aún diferidos. El flujo de zonas conecta interfaz, repositorio y JSON; se acepta como corte vertical documental. |
| Corte vertical reproducible y coherente con la arquitectura | [`main.dart`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/lib/main.dart), [`zonas_screen.dart`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/lib/features/zonas/presentation/screens/zonas_screen.dart), [`zona_repository.dart`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/lib/repositories/zona_repository.dart), [`start.sh`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/scripts/start.sh) | No verificado | El recorrido y el comando único se pueden leer, pero no se ejecutó código estudiantil y no se encontró un run que pruebe el flujo. |
| Pipeline y pruebas respaldan el estado aceptado | [`ci.yml`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/.github/workflows/ci.yml), [`app_smoke_test.dart`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/test/app_smoke_test.dart) | No verificado | El workflow actual ejecuta `flutter test`, pero no se encontró un run público verificable asociado. |
| Trazabilidad consolidada navegable | [`docs/aspectos.md`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/aspectos.md) | Cumple | A-01 ya identifica requisito, C4, ADR, código, prueba y evidencia; se acepta como trazabilidad suficiente para este compendio flexible, aunque parte de la implementación siga declarada como parcial. |
| PDF u otro adjunto exigido por el aula | Repositorio público | No verificado | El adjunto de Moodle no es accesible desde el repositorio. |
| Sustentación del corte | Sesión docente | No verificado | La resuelve el docente en la sustentación. |

## Correcciones contrastadas

| Origen | Corrección aceptada | Evidencia actual | Resultado |
|---|---|---|---|
| S1 | Problema y alcance sin RA | [`ficha_problema.md`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/ficha_problema.md) y [`ADR 0003`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/adr/0003-descartar-realidad-aumentada.md) | Verificada |
| S2 | Escenarios completos y enlace del árbol | [`escenarios_calidad.md`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/escenarios_calidad.md), [`arbol_utilidad.md`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/arbol_utilidad.md) | Verificada con observación: falta expresar impacto/riesgo de forma explícita. |
| S3 | Comparación de estilos y ADR con nombre convencional | [`ADR 0004`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/adr/0004-adoptar-monolito-como-estilo-arquitectonico.md) | Verificada bajo criterio flexible: compara monolito, cliente-servidor y microservicios. |
| S4 | Rutas normalizadas y contenedores diferidos declarados | [`docs/c4/C2.md`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/docs/c4/C2.md) | Verificada: plano y panorámicas se declaran pendientes, no se presentan como implementados. |
| S4/S5 | Workflow de pruebas | [`ci.yml`](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/8aee87957c958b8602c5d964ac194d3d13752412/.github/workflows/ci.yml) | Parcial: el workflow existe, pero falta evidencia pública de una ejecución. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio público y nombre convencional | Cumple | `ISCOUTB/AS_202620_mapsutb` es accesible públicamente. |
| Estructura mínima | Cumple | Las rutas actuales incluyen `docs/arc42/`, `docs/c4/`, `docs/adr/`, aspectos e IA. |
| Convención de ADR | Cumple | Los ADR actuales siguen el patrón numerado y con título kebab-case. |
| ADR aceptados sin reescribir | No cumple | ADR 0001 conserva reescrituras históricas; los cambios posteriores ya se registran en ADR separados. |
| Registro de IA y ausencia de secretos | Cumple | `docs/ia.md` registra decisiones; el escaneo estático no detectó patrones comunes de credenciales. |
| Colaboración | Cumple | El historial contiene cuatro cuentas; la correspondencia individual permanece a confirmar por el docente. |
| Pipeline en verde | No verificado | Existe `ci.yml`, pero falta un run público verificable. |

## Recuento y nota sugerida

**8 de 12 criterios Cumple.**

**Nota sugerida: 3.7 = 1 + 4 × (8/12).** Es una propuesta al docente; la nota oficial la fija el docente en Moodle.

## Pendientes

- Aportar un run público que ejecute las pruebas y demuestre el flujo completo.
- Convertir la priorización del árbol en impacto/riesgo explícito y completar los contenedores diferidos.
- Verificar el PDF en Moodle y resolver la sustentación.
