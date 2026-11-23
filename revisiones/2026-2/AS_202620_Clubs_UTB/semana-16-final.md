# Clubs UTB · Semana 16 · proyecto final

> Revisión técnica documental. Los niveles son propuestas parciales, no calificación final. La demostración y el criterio 5 corresponden al docente.

**Hallazgo principal:** LinkClub integra autenticación local, PostgreSQL, clubes, publicaciones y eventos; la trazabilidad de salud, carga y notificaciones no justifica afirmar que todas las operaciones y niveles de calidad fueron comprobados.

- Rama principal: `master`. [Candidato de cierre `d49859834981d421b2ac995dfe5aec5bbef1f798`](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/d49859834981d421b2ac995dfe5aec5bbef1f798) observado tras el corte de referencia del 23-11-2026 a las 05:00 UTC (cierre del domingo 22 en Colombia). SAVIO, envío y transición en segundos inmediatos no comprobados.
- [Línea base S10 `cd0ad9c64925863ed5067ed53da7f3c6dcf09895`](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/cd0ad9c64925863ed5067ed53da7f3c6dcf09895); [comparación S10→S16](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/compare/cd0ad9c64925863ed5067ed53da7f3c6dcf09895...d49859834981d421b2ac995dfe5aec5bbef1f798): 111 commits por delante según GitHub. No se usaron tags ni ramas de trabajo.
- [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) y [contrato del curso](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

## Matriz técnica de la ficha

### C1 · Sistema funcional, desafío y alcance (1,25)

S10 usó U3 con JWT/JWKS de Supabase; S16 declara migración a autenticación local y PostgreSQL, y muestra [estado/limitaciones](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/README.md#L112-L193) y [componentes](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/c4/contexto.md#L172-L180) de perfil, publicaciones y eventos. La [API y salud declaradas](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/README.md#L197-L208) apuntan a Dokploy; ni el SHA servido ni funcionamiento de app, salud y errores fueron comprobados en vivo. No se identificó la guía final o desafío asignado.

### C2 · Decisiones y evolución (1,00)

[ADR-0007](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/adr/0007-migracion-dokploy-postgresql.md#L7-L46) contrasta mantener Supabase, usar un servicio administrado y despliegue autónomo. Explica sustitución y costos. [arc42 §5](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/arc42/05_vista_de_bloques.md#L28-L48) delimita qué conserva núcleo hexagonal y qué routers van directo al ORM. [Mensajería](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/adr/0010-mensajeria-asincrona-notificaciones.md#L87-L109) permanece prototipo volátil, no entrega garantizada; falta una comparación operativa cuantificada del cambio de proveedor para nivel máximo.

### C3 · Calidad, resiliencia y seguridad (1,00)

[Mediciones](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/mediciones_calidad.md#L8-L39) publican U1 p95 131 ms frente a 800 ms, dentro de la red privada según el informe, sin precisar tamaño/corridas ni aportar datos crudos en ese apartado. U2 afirma simulación de caída, pero [test_health.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/backend/tests/test_health.py#L12-L15) solo comprueba 200 con base online; el adaptador y código 503 no prueban el resultado bajo caída. [Pruebas U3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/backend/tests/test_auth.py#L19-L78) protegen escrituras y credenciales inválidas, no extrapolar roles a toda operación sin inventario. [Backend](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/45114446592) y [contrato](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/45114446581) verdes; el trabajo de cambios incompatibles se omitió.

### C4 · Coherencia y trazabilidad (0,75)

Las **12 secciones arc42** y los **tres diagramas C4** están presentes; los diagramas se concentran en [un archivo](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/c4/contexto.md#L1-L78). Se contrastaron U2 (prueba de fallo incompleta), U3 (contrato/código/pruebas trazables) y C3 (ADR, falta comparación operativa reproducible); [tabla](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/aspectos.md#L11-L43) admite automatización incompleta U1/C2. El ADR de archivo 0010 encabeza como 0009, duplicando numeración, y un nombre ADR incluye espacio. No consta validación integral de C4/enlaces.

### C5 · Aportes verificables y sustentación (1,00)

En los primeros 100 de 111 commits desde S10 se ven tres cuentas; no validar el cuarto integrante por recuento parcial. [PR #2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2) presenta comentarios técnicos de SonarCloud, [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3) un check; no equivalen a revisión cruzada humana con argumentos ni cubren el trabajo de noviembre. Demostración y defensa: **no verificadas; las resuelve el docente**.

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
| Registro IA | [Presente](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/ia.md); no se certifica exhaustividad de la declaración. |
| README arranque y pruebas | Documentado en [README](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/README.md); sin recrear entorno. |
| Pipeline y análisis estático | Resultados exactos y pasos omitidos diferenciados en C3. |
| Credenciales e historial | No verificado exhaustivamente; no se usaron credenciales ni se reportan identificadores personales. |
| Contribución y revisión cruzada | Evidencia parcial en C5; autoría no confirmada sólo mediante conteos. |

## Preguntas para sustentación

1. Si PostgreSQL deja de responder, ¿cómo distinguen 503 de salud de las rutas que podrían fallar sin manejo?
2. ¿Qué falla si se reinicia el proceso justo tras crear una publicación y cómo preservarían la notificación sin duplicarla?
3. ¿Cómo demostrarían en el entorno desplegado que cambiar el rol bloquea una escritura y que la versión desplegada es esta?

**Límites:** lectura de repositorio y metadatos/pasos de CI. No ejecutamos código estudiantil, no escribimos en aplicaciones, no verificamos despliegue ni usamos credenciales. La asignación oficial del desafío, documento entregado en SAVIO y defensa quedan pendientes.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- API salud: [https://api-linkclub.iscoutb.dev/health](https://api-linkclub.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:09 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
