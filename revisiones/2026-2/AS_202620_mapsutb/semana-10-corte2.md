# Semana 10 · Segundo corte · mapsutb

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_mapsutb |
| Estado revisado | `1b296a37c575a751e99df1a1b288d70efba03d56` en `origin/master` (2026-10-02T12:58:33-05:00) |
| Rama remota principal | `origin/master` |
| Observación | 2026-10-06T21:31:50.415821+00:00 |
| Punta revisada para S10 | `1b296a37c575a751e99df1a1b288d70efba03d56` (2026-10-02T12:58:33-05:00) |
| S9 congelado, solo como línea base | `1b296a37c575a751e99df1a1b288d70efba03d56` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** Se localizaron Escenario 2 de ruteo, Escenario 7 de reversión y el taller con necesidad de reversión. Ninguno acredita por sí mismo el escenario operativo asignado específicamente al corte S10. Fuente o búsqueda: [docs/evidencia-s9.md:50-62](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L50-L62) y [docs/adr/0015-cache-del-sitio-revalidar.md:13-24](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L13-L24); búsqueda en README, ADR y docs/taller-despliegue.md. La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `e8bad4c286e5b985b324234b644e3b1fe961b626`: el delta hasta esta punta modifica 117 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master 1b296a37c575a751e99df1a1b288d70efba03d56; preliminar anterior al cierre futuro. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://mapsutb.web.app/health.json: HTTP 200, 7.064 s; inicio 2026-10-06T21:25:41Z. JSON declara commit 1b296a37c575a751e99df1a1b288d70efba03d56 y despliegue 2026-10-02T17:59:58Z. HEAD / devuelve 200. Es health estático; no demuestra ejecución de ruteo/GPS en navegador. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Se localizaron Escenario 2 de ruteo, Escenario 7 de reversión y el taller con necesidad de reversión. Ninguno acredita por sí mismo el escenario operativo asignado específicamente al corte S10. [docs/evidencia-s9.md:50-62](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L50-L62) y [docs/adr/0015-cache-del-sitio-revalidar.md:13-24](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L13-L24); búsqueda en README, ADR y docs/taller-despliegue.md |
| Línea base medida y reproducible | No verificado | Existen mediciones de cálculo/pantalla y caché: [docs/evidencia-s9.md:50-62](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L50-L62) y [docs/adr/0015-cache-del-sitio-revalidar.md:13-24](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L13-L24). Falta fijar cuál es la línea base del reto asignado S10. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0013-ruteo-dijkstra-grafo-propio.md:17-59](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0013-ruteo-dijkstra-grafo-propio.md#L17-L59) y [docs/adr/0015-cache-del-sitio-revalidar.md:26-55](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L26-L55) contienen alternativas y costo; falta asignación para valorar pertinencia S10. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [lib/routing/servicio_ruteo.dart:56-101](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/servicio_ruteo.dart#L56-L101) y [firebase.json:8-16](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/firebase.json#L8-L16) implementan respuestas reales a necesidades detectadas; no se presume que sean el reto asignado. |
| Resultado contrastado con el umbral | No verificado | Cálculo/pantalla documentados; no hay contraste atribuible al reto S10 confirmado. HEAD / observado 2026-10-06T21:25:55Z devuelve Cache-Control: max-age=3600, aunque [docs/adr/0015-cache-del-sitio-revalidar.md:26-35](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L26-L35) declara revalidación HTML/JS/JSON: comprobar por ruta la política efectiva; no se verificó el JS en esta pasada. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Health declara mismo hash; [lib/routing/servicio_ruteo.dart:62-75](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/servicio_ruteo.dart#L62-L75) produce evento estructurado de cálculo y [.github/workflows/ci.yml:44-64](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/.github/workflows/ci.yml#L44-L64) pipeline/gate. Run actual, métrica del reto y barrido independiente pendientes. |
| Secretos protegidos | No verificado | El equipo declara su barrido en [docs/evidencia-s9.md:104-109](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/evidencia-s9.md#L104-L109). El barrido independiente agregado fue cancelado por la herramienta y no se completó en el único reintento; no hay base para certificar limpieza integral ni para atribuir exposición al equipo. La comprobación permanece pendiente del revisor. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/c4/C2.md:39-50](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/c4/C2.md#L39-L50) aún declara MapaRepository y plano pendientes, aunque existen en [lib/routing/mapa_repository.dart:8-29](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/lib/routing/mapa_repository.dart#L8-L29). [docs/aspectos.md:7-9](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/aspectos.md#L7-L9) conserva Google Maps/coordenadas 0,0 como descripción anterior. Alinear C4/aspectos con el incremento real. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0015-cache-del-sitio-revalidar.md:13-24](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/1b296a37c575a751e99df1a1b288d70efba03d56/docs/adr/0015-cache-del-sitio-revalidar.md#L13-L24) usa una observación para complementar 0007/0010; buen antecedente técnico, pero no se puntúa como evolución del reto S10 aún no identificado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | La sesión docente debe ejecutar el despliegue y pipeline en vivo; no se puntúa por documentación. |

Recuento descriptivo: 2 Cumple, 1 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Asignación S10 no confirmada; ruteo y reversión son antecedentes distintos. |
| Decisión e implementación | No verificado | Pendiente | Decisiones argumentadas y código reales, pertinencia al reto pendiente. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Health versionado y logging presentes; ejecución/gate y política de caché efectiva por ruta pendientes. |
| Evolución arquitectónica trazable | No verificado | Pendiente | C4/aspectos desactualizados; ADR-0015 vincula decisión a observación pero no se presume reto S10. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | Pendiente docente. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

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

## Preparación de la sustentación

1. Fallo: si el GPS entrega una posición errónea o el usuario conserva una versión cacheada, ¿qué señal evita una ruta engañosa y cómo verificarán el rollback desde su navegador?
2. Costo: ¿cuál de las cuotas de Hosting/teselas/transferencia rompe primero el presupuesto cero y cómo cambia al revalidar recursos?
3. Medición: ¿qué cambiarían si el tiempo de cálculo sigue siendo bajo pero el usuario tarda o se localiza a más de 10 metros del camino real?

## Próximos pasos

El health público identifica el mismo commit revisado. Para el segundo corte, confirmen el escenario asignado y midan su línea base/respuesta sobre el entorno real. Comprueben la caché efectiva de cada recurso y la experiencia tras una reversión, y alineen C4 y aspectos con el código ya entregado.
