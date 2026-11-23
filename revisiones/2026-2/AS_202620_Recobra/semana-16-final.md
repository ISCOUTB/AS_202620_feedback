# Semana 16 · Proyecto final · Recobra

**Borrador técnico para revisión docente · 23 de noviembre de 2026. Sin calificación final, sin C1/C5 numéricos.**

## Estado y alcance de verificación

- Rama: `master`. Candidato: [703d44471795910de17d8b2b8d57df5ae5df7d50](https://github.com/ISCOUTB/AS_202620_Recobra/commit/703d44471795910de17d8b2b8d57df5ae5df7d50).
- Commit observado: 703d44471795910de17d8b2b8d57df5ae5df7d50 2026-11-21T16:55:43-05:00 aspectos.md A3: la evidencia es la app Flutter (ADR-0031), no la vitrina.
- Referencia de cierre: 23 de noviembre, 05:00 UTC. La elegibilidad y correspondencia con SAVIO se consolidan por separado; no se certifican solo con la fecha interna del commit.
- Base S10: [eae8471c932f430d56b757dfb3e79e57a647f4b8](https://github.com/ISCOUTB/AS_202620_Recobra/commit/eae8471c932f430d56b757dfb3e79e57a647f4b8); [informe S10](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/revisiones/2026-2/AS_202620_Recobra/semana-10-corte2.md).
- Comparación exacta local: 257 files changed, 25272 insertions(+), 1384 deletions(-); 52 commits en el delta. Es tamaño de cambio, no medida de calidad o contribución individual.
- Se inspeccionaron archivos del SHA y evidencia de GitHub; no se ejecutó código estudiantil, no se modificó el repositorio y no se realizaron escrituras en los servicios desplegados. Las mediciones del equipo se distinguen de esta lectura independiente.
- El texto oficialmente asignado del desafío final no quedó verificado. No se sustituye por el escenario S10/S14, por una autoevaluación ni por preguntas propuestas.

## Síntesis

La integración conserva búsqueda y persistencia hexagonal e incorpora reclamaciones, avisos recuperables, privacidad, moderación y una única interfaz Flutter. Destacan pruebas contra PostgreSQL real y validación documental. Quedan límites de medición con pocos datos, vínculos de trazabilidad no navegables y un scanner fallido tolerado que debe distinguirse del Quality Gate externo aprobado.

## Alcance S10 → S16

S10 evaluó búsqueda S1 con p95 ≤400 ms hasta 200 conexiones y transición a Dokploy, sin deriva material observada en los recorridos históricos. Desde entonces se amplía el ciclo completo de publicación/reclamación y la política de datos. ADR0031 retira la vitrina duplicada y adopta Flutter adaptable: una decisión nueva que debe evaluarse por su integración, sin recalificar por separado S11–S14.

## Decisiones y evolución

31 ADR. ADR0031 sustituye parcialmente ADR0029 y ADR0022: raíz 302 a /app/, retirada de public/index.html, moderación en Flutter y 404 real fuera de las rutas reconocidas. Describe tres alternativas, costo de primera carga y condición de reconsideración. ADR0026 acota reintentos/DLQ al proceso y ADR0024 aporta conciliación por estado; no promete que un bus en memoria sea durable. ADR0011 conserva el registro de enmiendas, útil para reconstruir cambios sin ocultar los documentos aceptados.

Fuentes: [docs/adr/](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/adr/) · [README.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/README.md).

## Calidad, resiliencia y seguridad

S14 conserva el umbral de p95 ≤400 ms y reporta p97,5=203 ms a 200 conexiones, margen de 197 ms. La propia evidencia declara solo dos publicaciones y respuesta filtrada vacía; no valida un catálogo representativo ni permite atribuir toda diferencia respecto a S10 a la arquitectura. CI ejecuta adaptadores PostgreSQL, respaldo/restauración, contrato, E2E y seguridad. Persisten verificación de propiedad del correo y procedimientos productivos de respaldo, que no se sustituyen con pruebas.

## CI exacto, análisis estático y despliegue

Run exacto con backend, Flutter, seguridad, PostgreSQL/restauración y Quality Gate exitosos. Atención: el job SonarCloud Scan figura success porque usa continue-on-error: true; sus logs muestran Not authorized or project not found, EXECUTION FAILURE y exit 3. No es un scanner exitoso ([log del job](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/44954053647/job/136998119554)); la tolerancia está en [.github/workflows/ci.yml:118–121](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/.github/workflows/ci.yml#L118-L121). Existe además check externo SonarCloud Code Analysis exitoso del mismo SHA y job bloqueante Quality Gate que consulta el análisis exacto; reconocer ambos hechos. El resumen externo muestra 113 nuevas incidencias y cobertura nueva 0 %, no cero problemas.

[Run exacto](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/44954053647) · [Checks del SHA](https://api.github.com/repos/ISCOUTB/AS_202620_Recobra/commits/703d44471795910de17d8b2b8d57df5ae5df7d50/check-runs) · [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_Recobra&branch=master).

**README y despliegue son evidencias diferentes.** README diferencia raíz https://recobra.iscoutb.dev/ (302 esperado), /app/ y API del mismo host, /health frente a /health/ready. Están instrucciones separadas de backend y Flutter y build Docker. La existencia de estas direcciones y de CI no certifica la revisión desplegada ni la demostración actual.

## Coherencia arquitectónica y aspectos

arc42.md contiene doce secciones y glosario. C4-C1, C4-C2 y C4-C3 representan cliente, API y persistencia. Tabla de 15 aspectos revisada estructuralmente: 96 enlaces Markdown sin destino local ausente. Pero múltiples celdas Código/Pruebas son texto entre backticks, no enlaces; A8/A9 aún citan public/index.html, retirado por ADR0031. Es una no conformidad de navegabilidad/actualización, no ausencia de reclamaciones o notificaciones. Recorridos semánticos detallados: A3, A6 y A14.

Fuentes: [docs/arc42/](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/arc42/) · [docs/c4/](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/c4/) · [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/aspectos.md).

### Tres recorridos de trazabilidad contrastados

- **A3 · Reclamación autorizada:** [docs/adr/0014-reclamacion-con-prueba-y-aprobacion.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/adr/0014-reclamacion-con-prueba-y-aprobacion.md) → [src/application/use-cases/reclamaciones.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/src/application/use-cases/reclamaciones.ts) → [src/application/use-cases/reclamaciones.spec.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/src/application/use-cases/reclamaciones.spec.ts) → [docs/contracts/openapi.yaml](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/contracts/openapi.yaml). Compara propietario, estado y aprobación; tests de no autorización, dos aprobaciones y rechazo. La falta de verificación de propiedad del correo está declarada.
- **A6 · Búsqueda:** [docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md) → [src/application/use-cases/buscar-publicaciones.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/src/application/use-cases/buscar-publicaciones.ts) → [test/publicaciones.e2e-spec.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/test/publicaciones.e2e-spec.ts) → [docs/medicion-s14.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/medicion-s14.md). La cadena termina en medición real histórica, con carga de dos publicaciones/lista vacía claramente delimitada.
- **A14 · Entrega de eventos:** [docs/adr/0026-entrega-de-avisos-con-eventos-reintentos-y-cola-de-fallidos.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/adr/0026-entrega-de-avisos-con-eventos-reintentos-y-cola-de-fallidos.md) → [src/application/use-cases/entrega-de-eventos.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/src/application/use-cases/entrega-de-eventos.ts) → [src/application/use-cases/entrega-de-eventos.spec.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/src/application/use-cases/entrega-de-eventos.spec.ts) → [docs/taller-mensajes.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/taller-mensajes.md). Código limita a tres intentos; tests 78–120 cubren duplicados, recuperación y DLQ. La muerte del proceso requiere conciliación, no la sola espera creciente.

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
| Validación automática documental/arquitectónica | Cumple: documentación y reglas/pruebas de contrato | No se confunde el alcance del validador con corrección completa |
| Contribución de todos los integrantes | No verificado por persona | Se registra actividad agregada; no se equiparan identidades Git con personas |
| Revisión cruzada de fondo | No verificado con evidencia suficiente | Colección de comentarios revisada; límites abajo |
| Demostración y sustentación | No verificado | Corresponde al docente y jurado; no se puntúa desde el repositorio |

## Matriz transversal

| Criterio | Estado | Evidencia |
|---|---|---|
| Organización/nombre | Cumple en URL observada | Repositorio ISCOUTB/AS_202620; acceso anónimo no comprobado por separado |
| Estructura mínima | Cumple | README, arc42, ADR, C4, aspectos e IA presentes; ubicación combinada válida |
| Hash evaluable | Pendiente de consolidación del corte | Candidato fijado, no sustituido por revisiones posteriores |
| Convención de nombres ADR | Cumple | Catálogo numerado en docs/adr |
| Inmutabilidad histórica de ADR | No verificado exhaustivamente | Sucesión declarada no equivale a barrido de todos los cambios históricos |
| Uso de IA | Registro presente; cobertura temporal completa no verificada | [docs/ia.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/703d44471795910de17d8b2b8d57df5ae5df7d50/docs/ia.md); no inferir autoría o comprensión desde el registro |
| Pipeline/Sonar/gate | Ver lectura diferenciada | Run, check externo, scanner y bloqueo no son sinónimos |
| Ausencia de credenciales en árbol/historia | No verificado exhaustivamente | No se declara ausencia universal por una lectura documental; no se reproduce ningún secreto |
| Contribución de todos | No verificado por persona | Solo agregados, sin consolidación de identidades ni nota C5 |

## Niveles técnicos orientativos C2–C4, sin puntajes

- **C2 · Decisiones y evolución: Competente.** Se sostiene en las alternativas, sucesión y enlaces de implementación/prueba indicados. No se propone sobresaliente por cantidad de ADR.
- **C3 · Calidad, resiliencia y seguridad: Competente.** Se sostiene en pruebas exactas y mediciones con límites; no equivale a aceptación productiva.
- **C4 · Coherencia y trazabilidad: Básico para cumplimiento completo: validación automatizada presente, pero tabla no totalmente navegable y referencias retiradas.** Los huecos descritos impiden afirmar que todos los artefactos coincidan y sean navegables.

No se calcula total, no se propone nota C1 y no se asigna C5.

## Colaboración: evidencia agregada

Actividad por mes de fecha de commit (incluye merges): 2026-08: 34, 2026-09: 71, 2026-10: 82, 2026-11: 13. Hay 6 identidades Git nominales, **no 6 personas verificadas**. No se publican nombres ni correos ni se concluye quién trabajó o faltó. La colección consultada devuelve 0 comentarios de revisión en línea. No basta para negar conversaciones generales o revisiones sin comentario; colaboración sustantiva entre personas no se atribuye automáticamente.

[Comentarios de revisión consultados](https://api.github.com/repos/ISCOUTB/AS_202620_Recobra/pulls/comments?per_page=100).

## Acciones concretas para cierre/defensa

1. Corregir A8/A9 y convertir Código/Pruebas de todos los aspectos en enlaces directos a la revisión.
2. Separar el scanner tolerado con error de autorización del análisis externo y del Quality Gate; corregir el permiso del scanner sin ocultar el estado actual.
3. Repetir búsqueda con catálogo representativo y verificar respaldo/restauración de producción, no solo CI.

## Preguntas de sustentación

1. Si se pierde el proceso después de persistir una reclamación y antes del aviso, ¿cómo reconstruye la conciliación el mensaje sin duplicar ni entregar dos veces el objeto?
2. Si el catálogo crece a 100.000 publicaciones, ¿qué permite concluir el p97,5 de 203 ms obtenido con dos publicaciones y respuesta vacía?
3. Si Flutter Web tarda demasiado en una red de campus, ¿qué umbral reabre ADR0031 y cómo conservarían 404 y moderación sin volver a duplicar toda la interfaz?

## Pendiente de consolidación central

Agregar comprobaciones públicas con hora, códigos y versión servida; procedencia del desafío final; elegibilidad del corte. Conservar explícita la separación entre producción, resultados declarados, CI y demostración docente.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.
[Diferencias frente a la revisión S10](https://github.com/ISCOUTB/AS_202620_Recobra/compare/eae8471c932f430d56b757dfb3e79e57a647f4b8...703d44471795910de17d8b2b8d57df5ae5df7d50); es evidencia de cambio, no medida de mérito ni certificación de alcance acordado.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://recobra.iscoutb.dev/app/](https://recobra.iscoutb.dev/app/) → HTTP 200 (13:28:12 UTC).
- salud: [https://recobra.iscoutb.dev/health](https://recobra.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:12 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
