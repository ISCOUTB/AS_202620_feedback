# Semana 9 · Generación verificada y trazable · GimnasioUTB

Revisión definitiva actualizada tras el cierre. Propuesta al docente; la nota final se fija en Moodle.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_GimnasioUTB |
| Rama remota principal | `origin/main` |
| Observación | 2026-10-06T21:31:50.150883+00:00 |
| Cierre S9 | 2026-10-05T05:00:00Z (medianoche de Colombia) |
| Estado revisado | `af4796d6320766611d9fc01d7112a1c0e4112b40` en `origin/main` (2026-10-04T16:52:10-05:00) |
| Línea base S8 | `a71bc7583b67cd4f5eca11dd6d356f7d08d1cdc7` |
| Commits del delta S8 → S9 | 12 |

## Alcance y método

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

El delta S8→S9 contiene 12 commits, desde la integración PostgreSQL hasta la UI Flutter. La verificación explícita de S9 entra en [25bd0918](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/25bd091809025d772b89a8730f35cf9f316b2166); no se confunde la UI con integración móvil ya probada.

## Matriz de la ficha (10 criterios)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [docs/ia.md:100-112](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/ia.md#L100-L112) registra la generación y revisión de correcciones V1/V2, verificadas en [src/modules/aforo/infrastructure/persistence/aforo-memoria.adapter.js:13-27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/src/modules/aforo/infrastructure/persistence/aforo-memoria.adapter.js#L13-L27) y [src/modules/aforo/application/consultar-aforo.usecase.js:1-17](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/src/modules/aforo/application/consultar-aforo.usecase.js#L1-L17). El delta añade también PostgreSQL y una UI Flutter, pero la porción de IA acreditada es la cadena del contador y sus correcciones. |
| Cadena completa navegable para esa porción | No cumple | [docs/aspectos.md:29-35](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/aspectos.md#L29-L35) conserva una tabla de cinco columnas: faltan enlaces navegables de código, pruebas, evidencia y C4. [docs/s9-cadena-verificada.md:11-20](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/s9-cadena-verificada.md#L11-L20) enumera rutas como texto; no repara la fila de ocho columnas del contrato. Los artefactos sí existen y se evalúan por separado. |
| ADR con la decisión argumentada por el equipo | Cumple | [docs/adr/0004-concurrencia-postgresql.md:7-33](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/adr/0004-concurrencia-postgresql.md#L7-L33) y [docs/adr/0004-concurrencia-postgresql.md:43-81](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/adr/0004-concurrencia-postgresql.md#L43-L81): bloqueo de fila, alternativas optimista/Redis y límites del contador; decisión fundada en infraestructura y dominio. |
| Prueba que falla ante el defecto que cubre | Cumple | [docs/s9-cadena-verificada.md:22-34](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/s9-cadena-verificada.md#L22-L34) documenta quitar FOR UPDATE, repetir tres veces y obtener 5/6/5 en vez de 20; la aserción existe en [tests/postgres/aforo-postgres.integration.test.js:86-98](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/tests/postgres/aforo-postgres.integration.test.js#L86-L98). Cumplimiento por procedimiento documentado permitido por la ficha, no por ejecución de esta revisión; [docs/ia.md:108](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/ia.md#L108) aún deja pendiente reproducción por el equipo. El dossier rotula estos datos como ejecutados/reales y el registro indica herramienta con entorno de ejecución; la casilla es una repetición humana pendiente, no una declaración de simulación. Se conserva Cumple por la vía documental de la ficha, con esa limitación explícita. |
| Medición del escenario asociado | Cumple | [docs/s9-cadena-verificada.md:7-34](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/s9-cadena-verificada.md#L7-L34) aporta entorno, 20 operaciones, 8/8 y resultado 20; [docs/adr/0004-concurrencia-postgresql.md:55-55](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/adr/0004-concurrencia-postgresql.md#L55-L55) limita correctamente el alcance al adaptador. No acredita carga HTTP ni identidad de estudiantes. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | [docs/ia.md:100-112](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/ia.md#L100-L112): aceptado, corrección de includeOnly y rechazos técnicos explícitos (evaluación de generación inexistente, migraciones mayores sin defecto que las justifique). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/auditoria-erosion.md:7-67](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/auditoria-erosion.md#L7-L67) enlaza reglas S6, V1/V2 corregidas y E1–E6; contrastado con el campo privado y caso de uso citados en la fila 1 y escrituras confinadas al adaptador [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js:44-88](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js#L44-L88). |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [docs/auditoria-dependencias.md:7-28](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/auditoria-dependencias.md#L7-L28) audita npm; delta [package.json:21-28](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/package.json#L21-L28) y [docs/Flutter/pubspec.yaml:7-55](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/Flutter/pubspec.yaml#L7-L55). Se comprobó el nombre exacto de pg y dependency-cruiser en [npm pg](https://registry.npmjs.org/pg) / [dependency-cruiser](https://registry.npmjs.org/dependency-cruiser), y las 42 dependencias con versión del pubspec en pub.dev (incluidas versiones publicadas; SDK Flutter queda aparte). Ejemplos: [google_fonts](https://pub.dev/api/packages/google_fonts), [go_router](https://pub.dev/api/packages/go_router). La auditoría del equipo precede a Flutter y debería ampliar su inventario; la verificación de registro de esta revisión cubre ese delta, sin ejecutar paquetes. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido estático del árbol textual, incluidos ejemplos y documentación: sin candidatos de credenciales reales; no hay .env versionado. [.github/workflows/ci.yml:11-23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/.github/workflows/ci.yml#L11-L23) y variables de entorno en [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js:14-27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js#L14-L27). Los PDF se excluyeron. No equivale a una certificación exhaustiva de secretos. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No cumple | [docs/s9-cadena-verificada.md:54-61](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/s9-cadena-verificada.md#L54-L61) explica que no hay modelo generativo, pero no existe un ADR de no incorporarlo en docs/adr. «No aplica» en un informe no sustituye la decisión formal exigida. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_GimnasioUTB; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Árbol Git con README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md; índice en [README.md:108-121](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/README.md#L108-L121). |
| Estado calificado identificable | Cumple | origin/main, af4796d6320766611d9fc01d7112a1c0e4112b40; último commit al cierre y baseline S8 declarados en cabecera. |
| Nombres de ADR según la convención | No cumple | [docs/adr/ADR0001.md:1-8](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/adr/ADR0001.md#L1-L8) no sigue NNNN-titulo-en-kebab-case y duplica el número de [docs/adr/0001-arquitectura-hexagonal.md:1-5](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/adr/0001-arquitectura-hexagonal.md#L1-L5). |
| ADR aceptados no reescritos | No cumple | El ADR-0001 ya aceptado sigue reescrito sin reemplazo: historial verificado en [3fae092f](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/3fae092fe6d33872772f106dc2737f88339ba82c) y estado canónico [docs/adr/0001-arquitectura-hexagonal.md:1-15](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/adr/0001-arquitectura-hexagonal.md#L1-L15). La punta añade otra edición tardía. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:100-112](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/docs/ia.md#L100-L112) incorpora S9 con correcciones/rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/ci.yml:11-23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/.github/workflows/ci.yml#L11-L23) carece de scanner y Quality Gate; [README.md:77-79](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/README.md#L77-L79) lo declara pendiente. Única consulta de runs PR del hash devolvió cero registros; no prueba que no haya runs push y no se reutilizan resultados antiguos. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Barrido estático del árbol textual, incluidos ejemplos y documentación: sin candidatos de credenciales reales; no hay .env versionado. [.github/workflows/ci.yml:11-23](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/.github/workflows/ci.yml#L11-L23) y variables de entorno en [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js:14-27](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/af4796d6320766611d9fc01d7112a1c0e4112b40/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js#L14-L27). Los PDF se excluyeron. No equivale a una certificación exhaustiva de secretos. El recorrido histórico ampliado está pendiente de completar; no se afirma ausencia histórica por el resultado del árbol actual. |
| Contribución de todos los integrantes | No verificado | Historial agregado a la punta: 5 grupos por correo idéntico frente a 3 integrantes; firmas distintas no se atribuyen por semejanza. Se requiere confirmar correspondencia cuenta–persona, sin publicar correos. |

## Estado global del proyecto (overall)

Punta observada de `origin/main`: `c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec` (2026-10-05T18:16:08-05:00). Hay 3 commits posteriores al estado congelado S9. Después del cierre se añadieron Dockerfile/Compose y documentación de Dokploy; las sondas públicas responden. Esto cierra deuda operativa en la punta, pero no altera S9. [README.md:40-46](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/c0a6a78f0ce87ea59040662b5abbbb4d2ab99aec/README.md#L40-L46) distingue PostgreSQL de Compose, UI sin integración y ausencia de prueba de retención tras redeploy.

- Convertir aspectos en cadena de ocho columnas con enlaces reales a C4, código, prueba y medición.
- Formalizar mediante ADR la decisión de no incorporar generación y la plataforma Dokploy.
- Incluir PostgreSQL real en CI y aportar scanner, run y Quality Gate público.
- Conservar ADR aceptados y resolver duplicación del 0001. Confirmar cuentas sin inferir personas.
- Identificar el escenario asignado de S10 y levantar una línea base del despliegue.

### Hallazgos anteriores cerrados o delimitados

- Ya existe registro IA S9 con rechazo técnico y auditoría de erosión; V1 y V2 están corregidas en código.
- La prueba de fallo por pérdida de bloqueo está documentada; no sigue simplemente «sin evidencia».
- En la punta posterior al cierre ya existen Dockerfile, Compose, URL pública y arc42 de despliegue; no modificar notas S8/S9 por ello.

## Recuento y nota sugerida

**8 de 10 criterios Cumple**,  2 No cumple y 0 No verificado. La transversal no entra en el cálculo.

**Nota sugerida definitiva: 4.2 = 1 + 4 × (8/10). Propuesta al docente; la nota final se fija en Moodle.**

## Próximos pasos

La verificación del contador ya incluye un defecto controlado, resultados y correcciones de erosión. Completen los enlaces de la tabla de aspectos y un ADR que justifique no incorporar un modelo generativo. La auditoría de dependencias debe incluir también la nueva UI Flutter; lleven la prueba PostgreSQL a CI y mantengan inmutables los ADR aceptados.
