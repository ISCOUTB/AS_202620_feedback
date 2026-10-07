# Semana 9 · Generación verificada y trazable · mapsutb

Revisión definitiva actualizada tras el cierre. Propuesta al docente; la nota final se fija en Moodle.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_mapsutb |
| Rama remota principal | `origin/master` |
| Observación | 2026-10-06T21:31:50.415821+00:00 |
| Cierre S9 | 2026-10-05T05:00:00Z (medianoche de Colombia) |
| Estado revisado | `1b296a37c575a751e99df1a1b288d70efba03d56` en `origin/master` (2026-10-02T12:58:33-05:00) |
| Línea base S8 | `8cfe458141159c9663f543d7cf31faf240432214` |
| Commits del delta S8 → S9 | 18 |

## Alcance y método

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

S9 incorpora ruteo real, grafo, pantalla de mapa, pruebas y decisiones 0011–0015. Frente a la preliminar, se acepta 0014, se mide pantalla y se actualiza el inventario de dependencias. La fila de cadena se contrasta ahora estrictamente con la navegabilidad exigida por el contrato.

## Matriz de la ficha (10 criterios)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [docs/ia.md:21-25](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/ia.md#L21-L25) registra construcción asistida de grafo, Dijkstra y pantalla; [lib/routing/servicio_ruteo.dart:28-101](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/servicio_ruteo.dart#L28-L101) y [lib/routing/mapa_repository.dart:8-29](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/mapa_repository.dart#L8-L29) materializan la porción dentro del delta. El grafo se construye a partir del levantamiento del equipo, no es ejercicio aislado. |
| Cadena completa navegable para esa porción | No cumple | [docs/aspectos.md:5-9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/aspectos.md#L5-L9) lista los eslabones de A-01, pero C4/ADR/código/pruebas quedan como rutas en texto, sin enlaces; también conserva «Adapter sobre Google Maps SDK» frente al flutter_map vigente. [docs/evidencia-s9.md:18-23](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L18-L23) vuelve a enumerar rutas, no repara navegabilidad. La existencia de artefactos se reconoce; falta la cadena navegable del contrato. |
| ADR con la decisión argumentada por el equipo | Cumple | [docs/adr/0013-ruteo-dijkstra-grafo-propio.md:10-69](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0013-ruteo-dijkstra-grafo-propio.md#L10-L69) decide Dijkstra/heap propio frente a A*, precálculo y servicio externo según offline, tamaño y propiedad de datos. |
| Prueba que falla ante el defecto que cubre | Cumple | [test/ruteo_test.dart:99-112](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/test/ruteo_test.dart#L99-L112) compara algoritmo correcto y mutante de menos tramos; [docs/evidencia-s9.md:33-48](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L33-L48) documenta el cambio exacto d+t.metros→d+1 y pruebas que fallan. Se acepta mutación/procedimiento documentado permitido por ficha; no se ejecutó código. |
| Medición del escenario asociado | Cumple | [docs/evidencia-s9.md:50-62](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L50-L62) reporta 100 rutas, p95 0.68 ms, máximo 1.85 ms y pantalla 19 ms frente a 5 s. [test/ruteo_test.dart:184-197](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/test/ruteo_test.dart#L184-L197) y [test/mapa_test.dart:198-218](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/test/mapa_test.dart#L198-L218) contienen instrumentación y umbral. Evidencia documentada de CI, no ejecución independiente ni certificación de GPS real; el sensor sigue simulado y margen de 10 m no queda demostrado por estos tiempos. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | [docs/ia.md:21-25](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/ia.md#L21-L25) diferencia aceptado, corrección por complejidad y precisión, rechazo de A*/dependencia/GPS falso; incluye decisión de equipo y no solo aceptación de propuesta. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/evidencia-s9.md:78-87](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L78-L87) contrasta reglas S6 y admite escritura de datos de catálogo desde herramienta de construcción con control; [lib/routing/mapa_repository.dart:8-29](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/mapa_repository.dart#L8-L29) es dueño del grafo y [scripts/campo/analizar_campo.py:675-702](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/scripts/campo/analizar_campo.py#L675-L702) condiciona escritura a opción explícita. Imports de ruteo no dependen de Zona. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [pubspec.yaml:11-17](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/pubspec.yaml#L11-L17) incorpora flutter_map/latlong2; [docs/evidencia-s9.md:89-102](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L89-L102) registra inventario. Consultados registros oficiales de [flutter_map 8.3.2](https://pub.dev/packages/flutter_map/versions/8.3.2), [latlong2 0.10.1](https://pub.dev/packages/latlong2/versions/0.10.1) y [defusedxml 0.7.1](https://pypi.org/pypi/defusedxml/0.7.1/json): nombres/versiones y proyectos legítimos. Se lee metadato, sin instalar ni ejecutar. |
| Sin credenciales en código, ejemplos ni documentación generada | No verificado | El equipo declara su barrido en [docs/evidencia-s9.md:104-109](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L104-L109). El barrido independiente agregado fue cancelado por la herramienta y no se completó en el único reintento; no hay base para certificar limpieza integral ni para atribuir exposición al equipo. La comprobación permanece pendiente del revisor. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | [docs/adr/0014-sin-componente-generativo.md:3-48](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0014-sin-componente-generativo.md#L3-L48) ya está aceptado el 02/10 por el equipo, con motivos offline/costo/tamaño/fiabilidad y condición para reevaluación. Supera la propuesta pendiente de la preliminar. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_mapsutb; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes en árbol; arc42 mezcla adoc y md como desviación de formato, sin tratar artefactos existentes como ausentes; [docs/aspectos.md:5-9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/aspectos.md#L5-L9). |
| Estado calificado identificable | Cumple | origin/master 1b296a37c575a751e99df1a1b288d70efba03d56; fecha/corte en cabecera. |
| Nombres de ADR según la convención | Cumple | Listado docs/adr 0001–0015 conforme; [docs/adr/0015-cache-del-sitio-revalidar.md:1-9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L1-L9). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0001-patrones-de-diseno.md:5-14](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0001-patrones-de-diseno.md#L5-L14) reconoce ediciones aceptadas; el historial confirma cambios antes del reemplazo. ADR-0015 sí complementa decisiones sin reescribirlas; es una mejora de práctica, no eliminación del historial. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:21-25](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/ia.md#L21-L25) contiene S9 y rechazos motivados. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [.github/workflows/ci.yml:44-64](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/.github/workflows/ci.yml#L44-L64) contiene suite, scanner y gate. El conector consultó una vez el hash con filtro PR y devolvió cero registros; no demuestra falta de runs push. Los runs enlazados en [docs/evidencia-s9.md:52](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L52) son evidencia documental; falta trío de comprobación pública vigente para este hash. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El equipo declara su barrido en [docs/evidencia-s9.md:104-109](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L104-L109). El barrido independiente agregado fue cancelado por la herramienta y no se completó en el único reintento; no hay base para certificar limpieza integral ni para atribuir exposición al equipo. La comprobación permanece pendiente del revisor. |
| Contribución de todos los integrantes | No verificado | La planilla anterior mantiene correspondencias cuenta–persona por confirmar. No se atribuyen identidades por nombres parecidos ni se reutilizan conteos anteriores como comprobación vigente. |

## Estado global del proyecto (overall)

Punta observada de `origin/master`: `1b296a37c575a751e99df1a1b288d70efba03d56` (2026-10-02T12:58:33-05:00). Hay 0 commits posteriores al estado congelado S9. Punta igual al cierre S9; health declara ese mismo commit. Se cerraron varios pendientes preliminares. Persiste GPS real y entradas de zona provisionales. El nuevo ADR de caché es una respuesta fundada en medición; la política HTTP efectiva de la raíz merece revisión porque se observó max-age=3600.

- Convertir rutas en enlaces navegables de A-01 y corregir C4 que todavía dice MapaRepository pendiente.
- Separar medición de cálculo/pantalla de GPS real y precisión geográfica; no afirmar un flujo físico completo desde un test sintético.
- Verificar política de caché efectiva por URL y qué ve un usuario previo a un rollback.
- Aportar run/Quality Gate del hash, confirmar atribución y completar barrido independiente pendiente.
- Identificar el reto S10 antes de puntuar su respuesta.

### Hallazgos anteriores cerrados o delimitados

- ADR-0014 ahora aceptado por el equipo; no sigue pendiente de decisión.
- Evidencia S9 incluye medición de pantalla además del algoritmo.
- La sección de dependencias coincide con las incorporaciones flutter_map/latlong2.
- A-01 ya reconoce la pantalla implementada; queda otro texto anterior en C4.
- URL y health hoy accesibles, con commit desplegado igual al revisado.

## Recuento y nota sugerida

**8 de 10 criterios Cumple**,  1 No cumple y 1 No verificado. La transversal no entra en el cálculo.

**Nota propuesta pendiente de completar la comprobación bloqueada del revisor.** El recuento documental es 8/10; si las 1 comprobaciones bloqueadas resultan conformes, el intervalo resultante es 4.2–4.6. No es una nota cerrada ni se atribuye el bloqueo al equipo. La nota final la fija el docente en Moodle.

## Próximos pasos

El ruteo ya tiene decisión, pruebas de defecto y mediciones de cálculo y pantalla; la decisión de no incorporar generación quedó aceptada. Completen los enlaces de A-01 y actualicen el C4 que todavía declara el repositorio de mapas pendiente. Distingan el resultado con GPS simulado de la precisión en campo. La comprobación independiente de credenciales sigue pendiente por una limitación del revisor.
