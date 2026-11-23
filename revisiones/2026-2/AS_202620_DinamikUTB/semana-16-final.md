# DinamikUTB · Semana 16 · proyecto final

> Revisión técnica documental. Los niveles son propuestas parciales, no calificación final. La demostración y el criterio 5 corresponden al docente.

**Hallazgo principal:** hay progreso curricular y ayuda aislada por programa con pruebas backend; CI del frontend falla y C4 no llega a nivel 3. No confundir Pages publicado con la validación integrada.

- Rama principal: `master`. [Candidato de cierre `2dd324ea6a9f53d5be48f20ababd21a541c83d52`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/2dd324ea6a9f53d5be48f20ababd21a541c83d52) observado tras el corte de referencia del 23-11-2026 a las 05:00 UTC (cierre del domingo 22 en Colombia). SAVIO, envío y transición en segundos inmediatos no comprobados.
- [Línea base S10 `5dc9acf9335fec70e274a2e5c494b3805b0e9646`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/5dc9acf9335fec70e274a2e5c494b3805b0e9646); [comparación S10→S16](https://github.com/ISCOUTB/AS_202620_DinamikUTB/compare/5dc9acf9335fec70e274a2e5c494b3805b0e9646...2dd324ea6a9f53d5be48f20ababd21a541c83d52): 277 commits por delante según GitHub. No se usaron tags ni ramas de trabajo.
- [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) y [contrato del curso](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

## Matriz técnica de la ficha

### C1 · Sistema funcional, desafío y alcance (1,25)

Sobre S10 (exactitud Q-01 y health/métricas, sin base operativa fiable), ahora se ven [pruebas de progreso, prerrequisitos, elegibilidad y auditoría](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/backend/tests/test_progreso.py#L41-L155), y [radicación/aislamiento de solicitudes](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/backend/tests/test_ayuda.py#L70-L178). [Guía README](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/README.md#L153-L211) declara inicio Windows de un comando y dependencias; [arc42 del despliegue](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/docs/arc42/07-deployment-view.md#L9-L46) enumera Pages, Render históricos y laboratorio. No comprobados los flujos, health/error en despliegue ni el SHA del backend; no se identificó guía de tres páginas ni desafío S16 asignado.

### C2 · Decisiones y evolución (1,00)

[ADR-0011](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/docs/adr/0011-historial-de-cambios-transaccional.md) conserva auditoría y cambio juntos, y los ADR-0014/0015 extienden datos de estudiante y avance. [ADR-0016](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/docs/adr/0016-modulo-ayuda-y-aislamiento-por-programa.md#L12-L75) contrasta alternativas, documenta autoridad del servidor y directorio demo, y confirma implementación mediante pruebas, no medición operativa cuantificada comparable.

### C3 · Calidad, resiliencia y seguridad (1,00)

[arc42 §10](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/docs/arc42/10-quality-requirements.md#L67-L209) fija umbrales de exactitud/aislamiento. Las [pruebas de ayuda](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/backend/tests/test_ayuda.py#L112-L178) ejercen visibilidad y cambios ajenos, y [progreso](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/backend/tests/test_progreso.py#L140-L219) roles y elegibilidad. En [CI exacta](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/45111037920) Pytest pasó; Flutter falló en dos búsquedas de texto del login y SonarCloud no corrió. [pip-audit](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/45111037781) y [build/publicación Pages](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/45111037826) pasaron por separado. No se verificó 100% en operación, carga, recuperación o respaldo.

### C4 · Coherencia y trazabilidad (0,75)

Hay **12 secciones arc42** pero el árbol [C4](https://github.com/ISCOUTB/AS_202620_DinamikUTB/tree/2dd324ea6a9f53d5be48f20ababd21a541c83d52/docs/c4) solo tiene contexto/contenedores, no nivel 3; [vista de bloques](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/docs/arc42/05-building-block-view.md#L35-L90) ayuda pero no cierra la ausencia del C4 L3. [Aspectos](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/docs/aspectos.md#L8-L21): 8 declarados; se contrastaron A-02 con pruebas progreso, A-07 con ADR/aislamiento y A-08 con historial parcial. A-03 sigue pendiente. La trazabilidad y los contratos existen, no son completos para todos ni se acreditó validación integral de documentación.

### C5 · Aportes verificables y sustentación (1,00)

Dos cuentas en la página de 100 de 277 commits S10→S16, muestra insuficiente para cubrir el historial. [PR #36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36) y [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37) evidencian integración, sin revisión humana de fondo demostrada en los hilos leídos. Demostración y defensa: **no verificadas; las resuelve el docente**.

| Criterio | Propuesta técnica |
|---|---|
| C1 | Pendiente demo/desafío |
| C2 | Competente (0,80) |
| C3 | Básico (0,60) |
| C4 | Básico (0,45) |
| C5 | **Reservado al docente** |
| Total | **Pendiente** |

## Matriz transversal del contrato

| Comprobación | Resultado |
|---|---|
| Repositorio público, nombre, estructura y estado | Repositorio accesible y rama/hash verificables; las salvedades de estructura/trazabilidad están en C4. |
| ADR, convenciones y vigencia | Véanse ADR y desalineaciones en C2/C4; integridad de todo el historial de ADR aceptados no certificada. |
| Registro IA | [Presente](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/docs/ia.md); no se certifica exhaustividad de la declaración. |
| README arranque y pruebas | Documentado en [README](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2dd324ea6a9f53d5be48f20ababd21a541c83d52/README.md); sin recrear entorno. |
| Pipeline y análisis estático | Resultados exactos y pasos omitidos diferenciados en C3. |
| Credenciales e historial | No verificado exhaustivamente; no se usaron credenciales ni se reportan identificadores personales. |
| Contribución y revisión cruzada | Evidencia parcial en C5; autoría no confirmada sólo mediante conteos. |

## Preguntas para sustentación

1. Si un coordinador recibe una solicitud de otro programa, ¿qué devuelve la API y dónde se aplica el aislamiento?
2. Si dos gestores cambian el mismo requisito, ¿qué registra la auditoría y qué evita que el historial atribuya un estado previo incorrecto?
3. ¿Qué flujo de acceso demostrarían desde Pages al backend del laboratorio y cómo explicarían las dos regresiones Flutter y la ausencia de Sonar de este hash?

**Límites:** lectura de repositorio y metadatos/pasos de CI. No ejecutamos código estudiantil, no escribimos en aplicaciones, no verificamos despliegue ni usamos credenciales. La asignación oficial del desafío, documento entregado en SAVIO y defensa quedan pendientes.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- API salud: [https://api-dinamikutb.iscoutb.dev/health](https://api-dinamikutb.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:09 UTC).
- web externa: [https://iscoutb.github.io/AS_202620_DinamikUTB/](https://iscoutb.github.io/AS_202620_DinamikUTB/) → HTTP 200 (13:28:08 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
