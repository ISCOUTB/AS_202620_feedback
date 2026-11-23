# Evaluación técnica S16 · UTB Tracker

Fecha de lectura: 23 de noviembre de 2026. Revisión técnica previa a la sustentación. No se ejecutó código estudiantil ni se modificaron calificaciones. No se califican demostración ni C5. La asignación oficial del desafío final no se encontró acreditada en las fuentes leídas: no se sustituye por el escenario S10.

## Estado y corte

- Repositorio: https://github.com/ISCOUTB/AS_202620_UTB_TRACKER
- Rama de referencia: main.
- Candidato observado: [2510dfc50292a4d85cd651403146120a495688e3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/2510dfc50292a4d85cd651403146120a495688e3); fecha de commit 2026-11-23T04:32:30Z.
- Cierre de referencia: 23 de noviembre, 05:00 UTC, equivalente al final del domingo 22 en Colombia. La captura contemporánea de rama es referencia; no certifica entrega SAVIO ni cierre efectivo de sección.

## Alcance S10 → S16

S10 se centró en QS-06 de recursos y préstamos. El README S16 redefine el producto como administración de salones, ocupación, habilitación y equipos fijos que no se prestan. ADR-0023 declara la retirada: conserva /prestamos/* como legado de experimentos, deprecated y fuera de pantallas, sin borrar préstamos vivos. Es una evolución explícita de alcance. No debe demostrarse el producto vigente únicamente con pruebas de préstamos individuales del legado.

Base S10 publicada: `d17c9eb241e56755d48b022dc00ddb865e40c391`. [Comparación de GitHub](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/compare/d17c9eb241e56755d48b022dc00ddb865e40c391...2510dfc50292a4d85cd651403146120a495688e3) informa 129 commits; la respuesta de archivos llega a 300 y no se trata como inventario completo. No se recalifican entregas previas por existir.

## Decisiones y evolución

El árbol contiene 23 ADR. ADR-0023 completa 0010 y 0001: elimina nuevas escrituras del estado prestado, migra solo equipos sin préstamo activo y añade tests de erosión backend/Flutter. Sus consecuencias y compatibilidad están explícitas. La prueba test_erosion_capas.py inspecciona capas Python y Dart; no ejecuta el cliente Flutter. La guía final sigue apoyando parte de la confiabilidad en test_loans y legado, por lo que se exige correspondencia adicional con solicitudes de salón vigentes.

## Calidad, resiliencia y seguridad

medicion-qs03.md declara API local real contra PostgreSQL, 50/150/300 concurrencias y dos corridas; p95 citado de 2523 ms. El escenario QS-03 exige 300 usuarios sin errores, mientras los 3 s vienen de QS-02 de vista móvil interactiva: latencia de API no acredita por sí sola ese escenario de interfaz. Se leyeron resiliencia, contrato y matriz de permisos: esta última parametriza endpoint×rol, y la de contrato comprueba paths y campos requeridos. La existencia de CircuitBreaker no demuestra su conexión a cada dependencia ni que el envío SMTP/FCM esté recuperándose en producción.

## Coherencia y trazabilidad

Se inspeccionaron arc42, C1–C3 y las 15 filas A-01–A-15. A-01, A-02 y A-03 se contrastaron en detalle: los C4 figuran como texto C1/C2 sin enlace; A-02 apunta a app/tests/test_main.py, que no existe en el árbol revisado. La referencia ../calidad/medicion-qs03.md desde docs/aspectos.md también sale de docs/ hacia una ruta distinta de docs/calidad. Hay prueba de salud real en app/routers/health.py delegada al servicio, pero eso no repara el enlace. Por tanto no cumple la exigencia de todas las cadenas navegables; 0/15 se certifican completas en este corte, sin negar el contenido de código/pruebas existente. La tabla final de términos existe, aunque no tenga encabezado «Glosario»: no se cuenta como ausente. Sin embargo define todavía Recurso/Préstamo/Auxiliar según préstamo individual, frente al alcance vigente de salones del README y ADR-0023. La regla de erosión en CI es una fortaleza, pero no compensa esos huecos ni esa desactualización.

## CI del SHA exacto

Run 45112477445 exacto exitoso, un job test con pytest y pip-audit; check externo SonarCloud Code Analysis exitoso. No ejecuta build ni pruebas Flutter, no acredita APK reciente ni versión desplegada. No trasladar al candidato la falla de CI de una referencia anterior.

- [UTB Tracker CI: 45112477445](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/45112477445): success, head_sha 2510dfc50292a4d85cd651403146120a495688e3.
- [SonarCloud Code Analysis](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/runs/137487871355): success.
- [test](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/45112477445/job/137487720312): success.

La configuración se leyó en [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/.github/workflows/ci.yml). El check Sonar exitoso no equivale a nueva prueba funcional ni a demostrar cobertura de todos los atributos.

## README y despliegue: evidencia separada

El README documenta https://api.iscoutb.dev. Esta pasada es documental: **sin sonda HTTP actual, sin credenciales, sin flujo productivo ni correspondencia imagen→SHA comprobados por este revisor**. Las comprobaciones históricas declaradas por el equipo no se presentan como observaciones nuevas. Incorporar aquí por separado las sondas centrales con hora, respuesta y límites; un health 200 no acredita la demostración.

## Colaboración verificable, sin atribución individual

La consulta de historial alcanzable desde el SHA devolvió 100 commits en esta página y cuatro identificadores de autor distintos (cuentas/firmas, no cuatro personas demostradas); es una muestra limitada a 100, no censo semestral. Meses visibles: 2026-11, 2026-10. La consulta de comentarios inline devolvió 13; todos son automáticos. Esto no demuestra revisión cruzada humana ni ausencia de otras modalidades de revisión. No se asignan cuentas por parecido de nombre, no se atribuye trabajo individual y no se fija C5.

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
| Aspectos completos y navegables | No cumple íntegramente | 15/15 filas inspeccionadas; muestra semántica y huecos detallados arriba. |
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

1. Si una APK antigua sigue invocando /prestamos después de retirar el préstamo individual, ¿qué contrato conservan, cómo identifican su uso y qué condición permite retirarlo?
2. Si 300 peticiones API cumplen p95 pero Flutter tarda más de 3 s en dejar la vista interactiva, ¿qué parte de QS-02 falta medir y cómo separarían red, servidor y render?
3. Si el worker envía un correo y cae antes de marcar el outbox, ¿cómo evitan efectos duplicados y qué evidencia corresponde al flujo actual de salones, no al legado?

## Fuentes del SHA revisado

- [docs/guia_evaluacion_final.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/docs/guia_evaluacion_final.md)
- [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/docs/aspectos.md)
- [docs/adr/0023-retiro-del-prestamo-de-equipos-y-control-de-erosion.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/docs/adr/0023-retiro-del-prestamo-de-equipos-y-control-de-erosion.md)
- [docs/calidad/medicion-qs03.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/docs/calidad/medicion-qs03.md)
- [app/core/resilience.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/app/core/resilience.py)
- [app/routers/health.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/app/routers/health.py)
- [tests/test_contract.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/tests/test_contract.py)
- [tests/test_matriz_permisos.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/tests/test_matriz_permisos.py)
- [tests/test_erosion_capas.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/tests/test_erosion_capas.py)
- [docs/c4/c4_nivel3.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/docs/c4/c4_nivel3.md)
- [docs/arc42/arc42.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/2510dfc50292a4d85cd651403146120a495688e3/docs/arc42/arc42.md)

## Verificación independiente del corte y del despliegue

El historial de `origin/main` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- API salud: [https://api.iscoutb.dev/salud](https://api.iscoutb.dev/salud) → HTTP 404 (13:28:15 UTC).
- web declarada en guía, no README: [https://tractar.iscoutb.dev/](https://tractar.iscoutb.dev/) → HTTP 200 (13:30:06 UTC).
- salud API declarada en guía, no README: [https://api-tractar.iscoutb.dev/salud](https://api-tractar.iscoutb.dev/salud) → HTTP 200, versión declarada `1.0.0` (sin SHA) (13:30:11 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
