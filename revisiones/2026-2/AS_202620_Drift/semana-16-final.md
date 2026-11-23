# Drift · Semana 16 · proyecto final

> Revisión técnica documental. Los niveles son propuestas parciales, no calificación final. La demostración y el criterio 5 corresponden al docente.

**Hallazgo principal:** traza sólida de evolución y comprobación automática de documentación, con una brecha operativa reconocida: E1 de búsquedas distintas obtuvo 9,05 s p95 en despliegue frente al objetivo de 3 s.

- Rama principal: `master`. [Candidato de cierre `b841450ce273f440d12d8fe6b5dd75c78e7b9bfb`](https://github.com/ISCOUTB/AS_202620_Drift/commit/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb) observado tras el corte de referencia del 23-11-2026 a las 05:00 UTC (cierre del domingo 22 en Colombia). SAVIO, envío y transición en segundos inmediatos no comprobados.
- [Línea base S10 `04874b8744dfa345a7fa7e12775e629c410fc870`](https://github.com/ISCOUTB/AS_202620_Drift/commit/04874b8744dfa345a7fa7e12775e629c410fc870); [comparación S10→S16](https://github.com/ISCOUTB/AS_202620_Drift/compare/04874b8744dfa345a7fa7e12775e629c410fc870...b841450ce273f440d12d8fe6b5dd75c78e7b9bfb): 63 commits por delante según GitHub. No se usaron tags ni ramas de trabajo.
- [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) y [contrato del curso](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

## Matriz técnica de la ficha

### C1 · Sistema funcional, desafío y alcance (1,25)

S10 abordó E6 con fuentes simuladas. Desde esa base se integraron catálogo multifuente, PostgreSQL, cuenta/dispositivos/favoritos, alertas y recomendaciones. [Contexto vigente](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/arc42/arc42_3_contexto_alcance.md#L78-L105) y [alcance/README](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/README.md#L374-L393) separan compromisos y exclusiones. [Laboratorio Dokploy](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/README.md#L301-L315) declarado; no confirmado SHA vivo, health/flujo/error actuales ni desafío oficial. No se identificó guía final separada.

### C2 · Decisiones y evolución (1,00)

[ADR-0023](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/adr/0023-ratificar-decisiones-de-noviembre.md#L15-L57) confirma ADR 13–22 y deja sin reescribir reemplazos, incluidas persistencia PostgreSQL, respaldo de fuentes y retiro de Azure/Vercel. [E5 en aspectos](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/aspectos.md#L57-L64) vincula plazo total a caída del p95 6,24→4,01 s en un escenario controlado, no a producción. [ADR-0024](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/adr/0024-precios-de-colombia-y-de-referencia.md) separa precios comparables y de referencia.

### C3 · Calidad, resiliencia y seguridad (1,00)

[Medición E1](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/README.md#L254-L272) muestra 9,05 s p95 en consultas distintas en el despliegue; 2,40 s para la misma consulta (2/3 corridas) y 0,63 s local simulado. [Remedición simulada](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/evidencias/s14-remedicion-e1-e6.md#L39-L73) obtuvo E1 955 ms y E6 3,41 s p95; hardware distinto, no inferir mejora real. [CI exacta](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/45112833917) pasó unitarias/vertical, auditorías, documentación, conexión frontend/API y análisis. [Privacidad actualizada](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/seguridad/privacidad.md#L17-L45) ya reconoce cuentas y PostgreSQL; Google real, borrado, respaldo/restauración siguen [pendientes](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/evidencias/verificaciones-pendientes-google-y-laboratorio.md).

### C4 · Coherencia y trazabilidad (0,75)

Las **12 secciones arc42** y C4 1–3 están presentes; [L3 vigente](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/c4/componentes.md#L5-L172) y diagramas históricos separados. [Tabla completa en estructura](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/aspectos.md#L49-L67) con E1–E6 y F1–F5, contrastados E1/E5/E6/F1/F2; F1/F2 necesitan cuenta real y restauración, y F1–F5 carecen de umbral propio. [Validador](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/scripts/validar_docs.py) ejecutado en [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/45112833917) comprueba enlaces, C4/ADR y reglas; corregir trazabilidad de rutas/cifras históricas para no confundir esquema y alcance.

### C5 · Aportes verificables y sustentación (1,00)

Cuatro cuentas de autor en 63 commits desde S10; [PR #61](https://github.com/ISCOUTB/AS_202620_Drift/pull/61), [#66](https://github.com/ISCOUTB/AS_202620_Drift/pull/66) y [#67](https://github.com/ISCOUTB/AS_202620_Drift/pull/67) trazan medición, correcciones y documentación. Sólo se observaron checks de SonarCloud en los hilos revisados; no contar como revisión humana ni certificar la distribución de contribución por persona. Demostración y defensa: **no verificadas; las resuelve el docente**.

| Criterio | Propuesta técnica |
|---|---|
| C1 | Pendiente demo/desafío |
| C2 | Sobresaliente documental (1,00) |
| C3 | Competente (0,80), con incumplimiento E1 explícito |
| C4 | Competente (0,60); automatización fuerte, cobertura operativa pendiente |
| C5 | **Reservado al docente** |
| Total | **Pendiente** |

## Matriz transversal del contrato

| Comprobación | Resultado |
|---|---|
| Repositorio público, nombre, estructura y estado | Repositorio accesible y rama/hash verificables; las salvedades de estructura/trazabilidad están en C4. |
| ADR, convenciones y vigencia | Véanse ADR y desalineaciones en C2/C4; integridad de todo el historial de ADR aceptados no certificada. |
| Registro IA | [Presente](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/docs/ia.md); no se certifica exhaustividad de la declaración. |
| README arranque y pruebas | Documentado en [README](https://github.com/ISCOUTB/AS_202620_Drift/blob/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb/README.md); sin recrear entorno. |
| Pipeline y análisis estático | Resultados exactos y pasos omitidos diferenciados en C3. |
| Credenciales e historial | No verificado exhaustivamente; no se usaron credenciales ni se reportan identificadores personales. |
| Contribución y revisión cruzada | Evidencia parcial en C5; autoría no confirmada sólo mediante conteos. |

## Preguntas para sustentación

1. Con búsquedas diversas y no calientes, ¿qué hace que E1 llegue a 9,05 s y qué medición comparable probaría una mejora?
2. Si una tienda agota el plazo y PostgreSQL cae al mismo tiempo, ¿qué se conserva, qué se marca degradado y qué no debería inventarse?
3. ¿Cómo demuestran en el entorno real Google, borrado y restauración sin recuperar indebidamente una cuenta eliminada?

**Límites:** lectura de repositorio y metadatos/pasos de CI. No ejecutamos código estudiantil, no escribimos en aplicaciones, no verificamos despliegue ni usamos credenciales. La asignación oficial del desafío, documento entregado en SAVIO y defensa quedan pendientes.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://drift.iscoutb.dev/](https://drift.iscoutb.dev/) → HTTP 200 (13:28:10 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
