# semana-07-evidencia-s7 · GimnasioUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `106869b` en `origin/main` (2026-09-13T22:19:08-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Arbol de 106869b no contiene ningun archivo openapi/swagger/asyncapi (.yaml/.json) ni .proto; docs/ solo tiene arc42, adr, c4, aspectos.md, ia.md, problema.md y contextos-delimitados.md | No cumple | Se esperaba un contrato ejecutable versionado (p. ej. docs/openapi.yaml o *.proto) y no se encontro ninguno |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No existe archivo de contrato del cual citar rutas ni esquemas de respuesta en 106869b | No cumple | Sin archivo de contrato no hay secciones paths/components que revisar |
| Correspondencia entre el contrato y la API implementada | El codigo expone POST y GET sobre /api/v1/aforo (README.md, seccion Corte Vertical; src/modules/aforo/infrastructure/http/aforo.router.js) y ninguna de esas rutas existe en un contrato porque no hay contrato | No cumple | No se puede contrastar en ninguno de los dos sentidos; desincronizacion total por ausencia del artefacto |
| Version de la API declarada y con historial | No hay archivo de contrato cuyo git log revisar; package.json declara version 0.1.0 del paquete, que no es version de API en un contrato | No cumple | Se esperaba campo de version del contrato (info.version o similar) e historial git del archivo |
| Prueba de contrato presente | tests/ contiene solo health.test.js, domain/aforo.test.js y aforo.integration.test.js, y package.json ejecuta node --test sobre esos tres archivos | No cumple | No hay archivo de prueba de contrato (dredd, schemathesis, pact, prism, spectral) en el arbol |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml solo define pasos npm install y npm test; runs de CI en success (ultimo 2026-09-14T03:19:11Z, https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/34802198344) sin ningun comando de contrato | No cumple | Se esperaba una linea del workflow invocando la prueba de contrato; no aparece |
| Evidencia de que la prueba falla ante un cambio incompatible | Los 10 runs listados concluyen success (2026-09-01 a 2026-09-14) y no existe prueba de contrato que pueda fallar | No cumple | Sin run en rojo ni evidencia aportada de cambio incompatible; queda como pregunta de sustentacion |
| ADR de la estrategia de integracion ligado a un escenario | docs/adr/0001-arquitectura-hexagonal.md justifica el estilo (hexagonal vs capas vs monolito modular) contra ES1-ES4, no una estrategia de integracion sincrona/asincrona; docs/adr/ solo tiene 0001 y ADR0001.md | No cumple | Se esperaba un ADR que decidiera sincrono o asincrono con alternativa descartada y consecuencias de acoplamiento |
| arc42 seccion 6 con los flujos de interaccion | docs/arc42/arc42_gimnasio_utb.md existe en 106869b, pero el extracto disponible se corta en la seccion 3.2 y no permite confirmar la seccion 6 | No verificado | Falta el contenido completo o la linea de encabezado de la seccion 6 para poder citarla |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/c4_level2.md define relaciones etiquetadas: JSON / HTTPS (app-api), SQL / Port 5432 (api-db), HTTPS / REST API (api-FCM) | Cumple | Dos flechas no declaran formato explicito: estudiante-app aparece como HTTPS / Flutter y FCM-app como Push Protocol |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_GimnasioUTB publico (visible true) en 106869b; autores consolidados por identidad: PedroPambi, RodrigoFacioLince y sebastian-caicedo (las dos entradas de Sebastian Caicedo comparten la misma cuenta de correo, se cuentan como uno) coinciden con los 3 integrantes declarados | Cumple | Los 3 integrantes declarados aparecen en el historial de la rama main |
| Estructura minima | Arbol de 106869b incluye README.md, docs/arc42/arc42_gimnasio_utb.md, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | Desviaciones menores: docs/adr/ADR0001.md duplicado y correcciones.md en la raiz en vez de docs/; los artefactos se evaluan donde estan |
| Convenciones de ADR | docs/adr/ADR0001.md no cumple el patron NNNN-titulo-en-kebab-case y ademas duplica el contenido de docs/adr/0001-arquitectura-hexagonal.md | No cumple | Ademas de la no conformidad de nombre, hay dos versiones divergentes del mismo ADR aceptado |
| La tabla de aspectos | docs/aspectos.md tiene la fila S1 con aspecto, estimulo, respuesta, tension y ADR, y una tabla de trazabilidad con escenario, ADR, implementacion (codigo) y pruebas | No cumple | La cadena se rompe: no hay columna ni enlace a elementos C4 ni celda de Evidencia de calidad, asi que esos eslabones no son navegables |
| Registro de uso de IA | docs/ia.md con entradas por semana (commits a59410d, 9b9f7c8, 56db96b, b49eeda, a45615e) y campo de rechazo con motivo, p. ej. el diagrama C4 de contexto rechazado y rehecho por el equipo | Cumple | El documento crece a lo largo del semestre y registra lo rechazado con su razon |
| README | README.md declara requisitos (Node.js >= 18), arranque con un comando (npm install && npm start) y prueba (npm test), con verificacion via curl /health | Cumple | El estado real de la persistencia en memoria esta declarado explicitamente en el README |
| Pipeline y analisis estatico | .github/workflows/ci.yml solo ejecuta npm install y npm test (runs en success, https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/34802198344); no hay paso del scanner, ni sonar-project.properties en el arbol, ni URL publica de analisis con Quality Gate | No cumple | Faltan las tres evidencias exigidas (workflow que invoca scanner, run del hash y URL publica del analisis); esperado desde S6 |
| Secretos | Busqueda de patrones de credenciales sobre HEAD sin coincidencias, sin .env versionado (solo .env.example) y sin claves privadas en el historial | Cumple | Ninguna credencial expuesta en el repositorio publico |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `106869bd63ac89ce19eae93a464b341be6bf75f8 2026-09-13T22:19:08-05:00 Add context map diagram to documentation`
- **Veredicto**: con pendientes
- Resumen: A HEAD (106869b, origin/main) el proyecto mantiene un corte vertical funcional, arquitectura hexagonal documentada, ADR, C4 nivel 2 y CI en verde, pero la entrega S7 esta ausente: no hay contrato ejecutable, ni prueba de contrato, ni ADR de integracion. Ademas siguen pendientes el analisis SonarCloud exigido desde S6, la convencion de ADR y la trazabilidad con C4 en aspectos.

Pendientes que siguen abiertos:
- Contrato de API en OpenAPI/AsyncAPI/proto ausente y sin historial de version (S7)
- Prueba de contrato ausente y no invocada por .github/workflows/ci.yml (S7)
- ADR de estrategia de integracion sincrona/asincrona ausente (S7)
- SonarCloud sin scanner en el workflow ni URL publica de analisis con Quality Gate (pendiente desde S6)
- docs/adr/ADR0001.md duplicado y fuera de la convencion NNNN-kebab-case
- docs/aspectos.md sin columnas/enlaces a C4 y a evidencia de calidad
- arc42 seccion 6 no verificable con la evidencia disponible

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 seccion 6 (flujos de interaccion): el extracto de docs/arc42/arc42_gimnasio_utb.md se corta en la seccion 3.2; haria falta el archivo completo o verificar la linea de encabezado de la seccion 6 en 106869b

## Hallazgos para la planilla

- El repositorio no contiene ningun contrato OpenAPI, AsyncAPI ni proto en 106869b.
- No existe prueba de contrato ni comando de contrato en el workflow de CI.
- Todos los runs de CI estan en success: no hay evidencia de que una prueba pueda fallar.
- No hay ADR de estrategia de integracion sincrona o asincrona.
- SonarCloud no esta invocado por el workflow ni hay analisis publico verificable.
- docs/adr/ADR0001.md duplica el ADR 0001 aceptado y rompe la convencion de nombres.
- docs/aspectos.md no enlaza elementos C4 ni evidencia de calidad en la cadena de trazabilidad.
- La seccion 6 del arc42 no pudo confirmarse con el extracto disponible.
