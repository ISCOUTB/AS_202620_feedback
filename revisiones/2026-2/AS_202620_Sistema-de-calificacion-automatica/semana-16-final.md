# Semana 16 · Proyecto final · Sistema-de-calificacion-automatica

**Borrador técnico para revisión docente · 23 de noviembre de 2026. Sin calificación final, sin C1/C5 numéricos.**

## Estado y alcance de verificación

- Rama: `master`. Candidato: [9c4e27831bca32a896254daa4ab135e0186ed0ed](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/9c4e27831bca32a896254daa4ab135e0186ed0ed).
- Commit observado: 9c4e27831bca32a896254daa4ab135e0186ed0ed 2026-11-22T23:19:33-05:00 ci: la base de pruebas del CI sin contraseña escrita.
- Referencia de cierre: 23 de noviembre, 05:00 UTC. La elegibilidad y correspondencia con SAVIO se consolidan por separado; no se certifican solo con la fecha interna del commit.
- Base S10: [85da6d3ab6ef882582839362b56981fa7cb53949](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/85da6d3ab6ef882582839362b56981fa7cb53949); [informe S10](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/revisiones/2026-2/AS_202620_Sistema-de-calificacion-automatica/semana-10-corte2.md).
- Comparación exacta local: 285 files changed, 42037 insertions(+), 1476 deletions(-); 202 commits en el delta. Es tamaño de cambio, no medida de calidad o contribución individual.
- Se inspeccionaron archivos del SHA y evidencia de GitHub; no se ejecutó código estudiantil, no se modificó el repositorio y no se realizaron escrituras en los servicios desplegados. Las mediciones del equipo se distinguen de esta lectura independiente.
- El texto oficialmente asignado del desafío final no quedó verificado. No se sustituye por el escenario S10/S14, por una autoevaluación ni por preguntas propuestas.

## Síntesis

QuantIA integra lectura OMR, calificación, revisión humana, sesiones, habilitación de clave y nuevos adaptadores Postgres. Las mediciones distinguen sintéticos y fotos limitadas de datos reales. Destacan la evolución explícita de persistencia y pruebas de frontera/contrato; quedan aislamiento por curso, cobertura de evidencia productiva y una fila A-04 desactualizada.

## Alcance S10 → S16

S10 evaluó EC-09, presupuesto del proveedor de distractores ante ráfagas; no se confunde con la asignación final. Se conserva presupuesto/cache y se agrega OMR, calificación/revisión, sesión y Postgres. README Estado al cierre declara pendientes cursos y aislamiento, estadísticas del Panel, banco de preguntas, calibración real, medición en servidor, doble carga y retención. El recorte está declarado, no se presenta como sistema de calificaciones listo para datos reales.

## Decisiones y evolución

27 ADR. ADR0027 transforma los registros JSONL en adaptadores Postgres detrás de los mismos puertos y compara alternativas; la evidencia base-de-datos.md reporta dos ejecuciones locales con límites del servidor, 200 hojas en 4,9/5,0 min y confirmación 1,2/2,8 s. Es evidencia para la decisión, no equivalencia a producción. ADR0025/0026 formalizan sesión y clave habilitada; ADR0024 distingue sugerencia de aprobación humana. La evolución de persistencia está justificada sin borrar el riesgo de archivos restantes ni las mediciones previas.

Fuentes: [docs/adr/](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/adr/) · [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/README.md).

## Calidad, resiliencia y seguridad

EC-01/02 se midieron en tres lotes sintéticos: 28.127 marcas claras y 3.134 ambiguas correctamente tratadas, según evidencia S14; EC-03 p95 1,22 s frente a ≤5 s y EC-04 3,5–3,6 min frente a ≤10 min, en local. ADR0027 advierte que esas cifras se obtuvieron con archivos y el Postgres posterior tuvo dos corridas distintas. No transferirlas sin más al candidato productivo. La preselección de 25/28 casos en tres fotos y cero errores reportados es un ensayo limitado, no validación clínica/estadística ni permiso para usar calificaciones reales. Sesión no equivale a autorización por curso.

## CI exacto, análisis estático y despliegue

Run push exacto: pruebas backend/contrato/presupuesto/fallos/mensajería, Flutter, auditoría OSV y publicar-despliegue exitosos. Publicar la rama de despliegue es un resultado distinto de verificar qué sirve Dokploy. Check externo SonarCloud Code Analysis success para el SHA; resumen 41 nuevas incidencias y 0 % cobertura nueva. Se encontró además run exacto 45112359326 con publicar-despliegue omitido: no anula el push exitoso. No se acreditó aquí que el check Sonar sea bloqueo obligatorio de integración.

[Run exacto](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/45111187109) · [Checks del SHA](https://api.github.com/repos/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commits/9c4e27831bca32a896254daa4ab135e0186ed0ed/check-runs) · [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_Sistema-de-calificacion-automatica&branch=master).

**README y despliegue son evidencias diferentes.** README separa https://calificacion.iscoutb.dev, API https://api-calificacion.iscoutb.dev y /revision.txt para identificar el frontend servido. La API raíz 404 es esperada; /health no consulta Postgres según ADR0027. Un health verde no prueba disponibilidad del almacén ni flujo de calificación. Las comprobaciones productivas y el SHA servido se incorporan separadamente.

## Coherencia arquitectónica y aspectos

arc42-template-ES.md contiene doce secciones sustantivas y glosario: el nombre template no es por sí mismo una ausencia. C4 reúne niveles 1–3. Se revisó estructuralmente el conjunto de seis aspectos y los 460 enlaces Markdown del documento, sin destinos locales ausentes. Tres recorridos detallados: A-02, A-05 y A-06. A-04 (línea 65) conserva C4/Código/Pruebas/Evidencia como Pendiente y ADR anteriores, aunque el desarrollo inferior y ADR0026 implementan registro/habilitación de clave. La tabla no cumple trazabilidad completa de todos los aspectos; no se debe concluir que la clave no existe. Cursos y banco siguen pendientes declarados.

Fuentes: [docs/arc42/](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/arc42/) · [docs/c4/](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/c4/) · [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/aspectos.md).

### Tres recorridos de trazabilidad contrastados

- **A-02 · Lectura de marcas:** [docs/adr/0023-leer-las-hojas-en-posiciones-fijas-y-mandar-a-revision-lo-que-no-se-ve-bien.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/adr/0023-leer-las-hojas-en-posiciones-fijas-y-mandar-a-revision-lo-que-no-se-ve-bien.md) → [backend/omr/decision.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/backend/omr/decision.py) → [backend/tests/test_decision.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/backend/tests/test_decision.py) → [docs/evidencia/medicion-s14.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/evidencia/medicion-s14.md). La regla separa marca única, doble, vacía y dudosa; la sugerencia no altera la nota hasta aprobación. Umbral real todavía sin calibrar.
- **A-05 · Sesión:** [docs/adr/0025-identificar-al-docente-con-una-sesion-firmada-y-una-lista-de-cuentas.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/adr/0025-identificar-al-docente-con-una-sesion-firmada-y-una-lista-de-cuentas.md) → [backend/identidad/](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/backend/identidad/) → [backend/tests/test_sesion.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/backend/tests/test_sesion.py) → [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/aspectos.md). Tests recorren rutas protegidas y requieren 401 sin token. Se declara que todo docente autenticado ve los exámenes al faltar cursos; no se acredita aislamiento.
- **A-06 · Presupuesto/caché de distractores:** [docs/adr/0015-limitar-el-gasto-del-proveedor-de-llm-con-un-presupuesto-en-la-api.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/adr/0015-limitar-el-gasto-del-proveedor-de-llm-con-un-presupuesto-en-la-api.md) → [backend/autoria/presupuesto.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/backend/autoria/presupuesto.py) → [backend/tests/test_presupuesto.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/backend/tests/test_presupuesto.py) → [docs/evidencia/experimento-presupuesto.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/evidencia/experimento-presupuesto.md). Permanece como paso específico CI del segundo corte. La integración no transforma el LLM en decisor de calificaciones.

## Matriz S16

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Identificación de estado | Cumple en identificación; elegibilidad pendiente de consolidación | SHA y fecha arriba; no se usa HEAD posterior ni tags |
| Sistema desplegado estable | No verificado en esta pasada | README y registros históricos no sustituyen comprobación viva y revisión servida |
| Flujos principales con datos realistas | No verificado en producción | Suite exacta y recorridos citados prueban el entorno de CI, no la demostración |
| Caminos de error | Cumple en la suite inspeccionada | Pruebas y run exacto; se reserva comportamiento vivo |
| Respuesta al desafío asignado | No verificado | Falta procedencia verificable de la consigna específica; no es ausencia de código |
| Alcance frente a S10 | Cumple como contraste documental | Comparación de hashes, README y pendientes declarados; no implica alcance íntegro completado |
| Evolución de ADR | Cumple | Secuencia y decisiones citadas en el apartado correspondiente |
| Decisión confirmada/reemplazada con evidencia | Cumple en evidencia documental | Sustitución/ajuste descrito y recorrido de código/prueba, no reproducción del experimento |
| Atributos medidos frente a umbral | Cumple con alcance de las mediciones descritas | No extrapolar entorno, volumen, datos ni revisión |
| Modos de fallo y mitigaciones | Cumple en muestra técnica | Pruebas específicas y CI; quedan riesgos residuales declarados |
| arc42 1–12 y glosario | Cumple en estructura y contenido revisado | No basta contar archivos; ver desfases de coherencia señalados |
| C4 1–3 coincide íntegramente | No verificado en totalidad | Niveles presentes; contraste limitado a recorridos señalados, no certificación exhaustiva |
| Todos los aspectos navegables de extremo a extremo | No cumple | Cobertura y huecos específicos descritos arriba; existencia de enlace no prueba semántica |
| Validación automática documental/arquitectónica | Cumple en reglas/contrato; enlaces/diagramas no acreditados | No se confunde el alcance del validador con corrección completa |
| Contribución de todos los integrantes | No verificado por persona | Se registra actividad agregada; no se equiparan identidades Git con personas |
| Revisión cruzada de fondo | Cumple en muestra, sin atribución individual | Colección de comentarios revisada; límites abajo |
| Demostración y sustentación | No verificado | Corresponde al docente y jurado; no se puntúa desde el repositorio |

## Matriz transversal

| Criterio | Estado | Evidencia |
|---|---|---|
| Organización/nombre | Cumple en URL observada | Repositorio ISCOUTB/AS_202620; acceso anónimo no comprobado por separado |
| Estructura mínima | Cumple | README, arc42, ADR, C4, aspectos e IA presentes; ubicación combinada válida |
| Hash evaluable | Pendiente de consolidación del corte | Candidato fijado, no sustituido por revisiones posteriores |
| Convención de nombres ADR | Cumple | Catálogo numerado en docs/adr |
| Inmutabilidad histórica de ADR | No verificado exhaustivamente | Sucesión declarada no equivale a barrido de todos los cambios históricos |
| Uso de IA | Registro presente; cobertura temporal completa no verificada | [docs/ia.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9c4e27831bca32a896254daa4ab135e0186ed0ed/docs/ia.md); no inferir autoría o comprensión desde el registro |
| Pipeline/Sonar/gate | Ver lectura diferenciada | Run, check externo, scanner y bloqueo no son sinónimos |
| Ausencia de credenciales en árbol/historia | No verificado exhaustivamente | No se declara ausencia universal por una lectura documental; no se reproduce ningún secreto |
| Contribución de todos | No verificado por persona | Solo agregados, sin consolidación de identidades ni nota C5 |

## Niveles técnicos orientativos C2–C4, sin puntajes

- **C2 · Decisiones y evolución: Competente.** Se sostiene en las alternativas, sucesión y enlaces de implementación/prueba indicados. No se propone sobresaliente por cantidad de ADR.
- **C3 · Calidad, resiliencia y seguridad: Competente con límites explícitos de datos/entorno.** Se sostiene en pruebas exactas y mediciones con límites; no equivale a aceptación productiva.
- **C4 · Coherencia y trazabilidad: Básico para trazabilidad completa: contenido amplio, pero A-04 queda con huecos.** Los huecos descritos impiden afirmar que todos los artefactos coincidan y sean navegables.

No se calcula total, no se propone nota C1 y no se asigna C5.

## Colaboración: evidencia agregada

Actividad por mes de fecha de commit (incluye merges): 2026-08: 60, 2026-09: 101, 2026-10: 140, 2026-11: 108. Hay 5 identidades Git nominales, **no 5 personas verificadas**. No se publican nombres ni correos ni se concluye quién trabajó o faltó. 22 comentarios humanos de revisión en línea en la colección consultada, creados antes del cierre de referencia (último: 23 de noviembre, 01:15 UTC). Ejemplos de fondo: [PR2, revisión sobre riesgo de preselección](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/2#discussion_r4660053728) cuestiona señales tardías y riesgo de preselección; [revisión de la condición del umbral](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/2#discussion_r4660057697) generaliza la condición umbral ≤100−corte. Se reconoce discusión técnica sin atribuir identidades ni dar por probada participación de cada integrante.

[Comentarios de revisión consultados](https://api.github.com/repos/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pulls/comments?per_page=100).

## Acciones concretas para cierre/defensa

1. Actualizar A-04 con ADR0026, C4, código, pruebas y evidencia ya existentes; preservar que RF-06 banco no está entregado.
2. No usar datos reales hasta resolver autorización/aislamiento por curso y retención; sesión sola no cierra EC-06.
3. Medir con Postgres y entorno servido, separar las dos corridas nuevas de las tres con archivos y agregar readiness de base.

## Preguntas de sustentación

1. Si dos docentes de cursos distintos entran al sistema actual, ¿qué impide que uno consulte o revise el examen del otro y qué frontera cambiarían para resolverlo?
2. Si Postgres cae mientras /health sigue verde, ¿qué ocurre con carga, bitácora y reintentos del worker, y cómo lo observaría el operador?
3. Si baja el umbral de confianza o cambia la iluminación del escaneo, ¿cuándo una sugerencia puede ocultar un error y qué evidencia necesitan antes de usar hojas reales?

## Pendiente de consolidación central

Agregar comprobaciones públicas con hora, códigos y versión servida; procedencia del desafío final; elegibilidad del corte. Conservar explícita la separación entre producción, resultados declarados, CI y demostración docente.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.
[Diferencias frente a la revisión S10](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/compare/85da6d3ab6ef882582839362b56981fa7cb53949...9c4e27831bca32a896254daa4ab135e0186ed0ed); es evidencia de cambio, no medida de mérito ni certificación de alcance acordado.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://calificacion.iscoutb.dev/](https://calificacion.iscoutb.dev/) → HTTP 200 (13:28:12 UTC).
- API salud: [https://api-calificacion.iscoutb.dev/health](https://api-calificacion.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:12 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
