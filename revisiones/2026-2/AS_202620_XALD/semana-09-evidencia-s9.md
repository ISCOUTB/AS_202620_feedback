# Evidencia S9 definitiva · XALD

Revisión actualizada tras el cierre. Estado congelado al **2026-10-05T05:00:00Z** (domingo a medianoche en Colombia).

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_XALD |
| Rama principal remota | `master` |
| Base S5 publicada | `9bf16cf989667977ff8afe95311a595a66517318` |
| Base S8 | `f90f28d3e3b0fe3da81d71b8cc9d9d10bdf07491` |
| Estado revisado | `9236ff97218b632eeb9a1910f6083968e2c22909` en `origin/master` (2026-10-04T23:53:02-05:00) |
| Punta actual / S10 preliminar | `9236ff97218b632eeb9a1910f6083968e2c22909` · 2026-10-04T23:53:02-05:00 |
| Observado | 2026-10-06T21:29:11.260956Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

El delta se contrasta contra S8; los artefactos previos sirven de línea base y no vuelven a premiarse por existir. Los cambios tardíos se separan en overall.

## Matriz de la ficha S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | No cumple | [docs/ia.md:39](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/ia.md#L39) atribuye a S9 implementación de LWW, pero [backend/app/main.py:110–132](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L110-L132) ya existe idéntico en S8 (diff de ese archivo vacío). El delta S8→S9 contiene siete archivos: dos herramientas de verificación (test/script), dos ADR, aspectos, IA y auditoría. backend/app/main.py es idéntico a S8; no se vuelve a puntuar su existencia como implementación nueva. Se reconoce la verificación nueva en las demás filas. |
| Cadena completa navegable para esa porción | Cumple | [docs/aspectos.md:9](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/aspectos.md#L9) A-03 enlaza ADR 0011; [docs/adr/0011-resolucion-conflictos-lww.md:19–24](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L19-L24) permite seguir rutas relativas a código, prueba y medidor en el estado calificado. Los enlaces directos de la tabla todavía apuntan a experimental: deben cambiarse, sin usar esa rama para esta evaluación. |
| ADR con la decisión argumentada por el equipo | Cumple | [docs/adr/0011-resolucion-conflictos-lww.md:7–32](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L7-L32): decide LWW en memoria, compara persistencia y CRDT/vector clocks, y reconoce reinicios y relojes como riesgos del MVP. Es nueva justificación, aunque el handler ya era parte de S8. |
| Prueba que falla ante el defecto que cubre | Cumple | [backend/tests/test_lww.py:5–8](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/tests/test_lww.py#L5-L8) y [backend/tests/test_lww.py:56–62](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/tests/test_lww.py#L56-L62) definen el defecto y la aserción. [docs/adr/0011-resolucion-conflictos-lww.md:24](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L24) documenta invertir la comparación y comprobar fallo; el procedimiento es admisible por ficha. [CI del hash en success](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/37265397606) respalda suite normal, no prueba por sí solo la mutación. |
| Medición del escenario asociado | No cumple | [docs/arc42/10-Quality Requirements.md:60–69](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/arc42/10-Quality%20Requirements.md#L60-L69) exige simultaneidad y comparar estado final; [backend/tests/test_lww.py:71–97](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/tests/test_lww.py#L71-L97) y [backend/scripts/medir_esc05.py:61–79](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/scripts/medir_esc05.py#L61-L79) envían pares secuencialmente. El script remoto cuenta 202 y un contador, sin leer el estado ganador; 30/30 no acredita el umbral completo declarado ni pérdida persistente. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | No cumple | [docs/ia.md:39–41](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/ia.md#L39-L41) añade aceptados y rechazos técnicos (CRDT, persistencia y requests), pero no concreta qué salida del periodo se corrigió ni declara que no necesitó corrección. Completar ese eslabón del registro, sin inventarlo. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/EVIDENCIA-S9.md:1–40](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L1-L40): reglas, método, resultados y hallazgos localizados; se contrastó la lista en memoria de [XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/GestorCoreFinanciero.kt:9–27](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/GestorCoreFinanciero.kt#L9-L27). La auditoría declara cero dependencias activas prohibidas y cinco deudas latentes abiertas, no las presenta como corregidas. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [docs/EVIDENCIA-S9.md:44–67](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L44-L67): seis paquetes backend verificados en PyPI con uso concreto. El delta no cambia requirements ni Gradle; el script nuevo usa biblioteca estándar. Alcance documental de dependencias directas, sin auditoría de todas las transitivas ni reproducibilidad por rangos abiertos. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido estático del árbol sin credenciales reales detectadas; [backend/app/main.py:59–65](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L59-L65) obtiene llave del entorno; [backend/scripts/medir_esc05.py:8–12](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/scripts/medir_esc05.py#L8-L12) es un marcador. La auditoría diferencia ejemplos/pruebas de secretos reales en [docs/EVIDENCIA-S9.md:71–105](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L71-L105). |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | [docs/adr/0012-aplazamiento-integracion-gemini.md:9–31](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0012-aplazamiento-integracion-gemini.md#L9-L31) decide explícitamente no incorporar la API generativa en este corte y conservar el mock por costo/secretos/determinismo. [XALDAPP/aigemini/src/main/java/CategorizadorGemini.kt:7–16](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/XALDAPP/aigemini/src/main/java/CategorizadorGemini.kt#L7-L16) confirma que no llama al proveedor. Es decisión acotada al corte; antes de integrar a futuro faltan conjunto de evaluación, costo y latencia. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público ISCOUTB/AS_202620_XALD; [README.md:1–9](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/README.md#L1-L9). |
| Estructura mínima presente | Cumple | README y seis rutas mínimas presentes; [docs/aspectos.md:5–11](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/aspectos.md#L5-L11) enlaza arquitectura y ADR. Hay binarios __pycache__ que deben retirarse sin confundirlos con ausencia documental. |
| Estado calificado identificable | Cumple | Rama master y hash/fecha exactos del encabezado, anterior al cierre; no se usaron etiquetas ni experimental para calificar. |
| Nombres de ADR según la convención | Cumple | Doce ADR con nombres NNNN-titulo-en-kebab-case.md; [docs/adr/0011-resolucion-conflictos-lww.md:1–5](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L1-L5). |
| ADR aceptados no reescritos | No cumple | Historial confirma adición de fechas a ADR 0001–0005 ya aprobados el 27-sep; por ejemplo efcc3902311cc8fec393fccf4f1cc7a95badf976 sobre [docs/adr/0001-patron-offline-first.md:1–4](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0001-patron-offline-first.md#L1-L4). Son ediciones de metadatos, no se afirma cambio de decisión; registrar adendas sin reescribir aceptados conforme al contrato. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:39–41](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/ia.md#L39-L41) crece en S9 con aceptados y rechazos motivados. La falta de un apartado de corrección se recoge en la fila específica S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Android CI del hash](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/37265397606) en success; [.github/workflows/ci.yml:29–57](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/.github/workflows/ci.yml#L29-L57) ejecuta Gradle, Redocly y pytest, pero no scanner SonarCloud. No hay configuración ni Quality Gate público de la revisión: el verde de pruebas no lo sustituye. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del árbol y búsqueda histórica de patrones de alta especificidad sin credenciales reales confirmadas; [backend/app/main.py:59–65](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L59-L65). Ejemplos y valores de pruebas revisados, sin publicar valores. |
| Contribución de todos los integrantes | No verificado | 419 commits con cuatro firmas observadas (186, 98, 72 y 63); la cantidad de firmas no verifica por sí sola correspondencia con cuatro integrantes ni distribución sustantiva. |

## Recuento y nota sugerida

**7 de 10 criterios Cumple. Nota sugerida: 3.8 = 1 + 4 × (7/10). Propuesta al docente; la nota final se fija en Moodle.** No verificado no se convierte en Cumple ni en una ejecución fallida.

## Estado global del proyecto (overall)

Punta de la misma rama: `9236ff97218b632eeb9a1910f6083968e2c22909` (2026-10-04T23:53:02-05:00). Hay **17 commits en el delta S8→S9** y **0 commits posteriores al cierre S9**. S9 agrega diecisiete commits de verificación/documentación, sin cambios al handler LWW respecto de S8; se reconoce ese avance sin duplicar la implementación previa. CI actual en verde. Persisten deudas de persistencia, cifrado, cliente Android→backend y evaluación de Gemini futuro.

GET https://xald-backend.onrender.com/health: primer intento 2026-10-06T21:24:29Z agotó 25,002608 s; segundo intento iniciado 2026-10-06T21:27:21Z devolvió HTTP 200 en 6,211375 s, cuerpo status=ok. Se comprueba salud puntual, no flujo de negocio ni carga.

### Hallazgos abiertos

- Repetir ESC-05 con conflictos realmente simultáneos, verificar estado ganador completo y distinguir aceptación HTTP de persistencia sin pérdidas.
- Precisar cuál código fue generado en S9: el handler LWW no cambia desde S8; sí cambian pruebas, medidor y documentación.
- Completar en docs/ia.md qué se corrigió del periodo, o declarar honestamente que no se requirió corrección.
- Cambiar enlaces de aspectos desde experimental al estado revisable y reconciliar Room/AES/TLS con el MVP real.
- Resolver o priorizar H-1…H-5 de la auditoría; no presentar la auditoría como corrección ya implementada.
- Integrar SonarCloud con scanner, run y Quality Gate públicos; retirar __pycache__ versionado.
- Identificar la consigna operativa S10 y medir línea base en el despliegue; documentar estabilidad y recuperación tras el primer timeout.
- Antes de incorporar Gemini, aportar conjunto de evaluación con resultados, costo y latencia; el ADR actual solo aplaza la integración.

### Hallazgos cerrados o sustituidos con evidencia actual

- Hay nueva prueba dirigida al defecto y procedimiento de mutación: [backend/tests/test_lww.py:5–8](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/tests/test_lww.py#L5-L8) y [docs/adr/0011-resolucion-conflictos-lww.md:24](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L24).
- La auditoría y la verificación de dependencias S9 ya están presentes: [docs/EVIDENCIA-S9.md:1–67](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L1-L67).
- La decisión sobre Gemini ya está explicitada para este corte y coincide con el mock: [docs/adr/0012-aplazamiento-integracion-gemini.md:17–31](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0012-aplazamiento-integracion-gemini.md#L17-L31).
- El pipeline sí corre sobre master y el hash actual pasa: [run](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/37265397606); no cierra SonarCloud.
- La planilla antigua decía sin URL, pero el README declara el servicio y health públicos: [README.md:8–11](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/README.md#L8-L11). Salud actual confirmada por HTTP 200 en la segunda consulta; no se probó flujo.

## Próximos pasos

Hay avances verificables en pruebas, auditoría y decisiones, pero el handler LWW no cambió respecto a la semana anterior. La medición 30/30 procesa pares en secuencia y solo observa aceptaciones y un contador; no demuestra conflictos simultáneos ni el estado ganador completo. Repitan ese experimento, precisen lo corregido en el registro de IA y actualicen los enlaces y las discrepancias de la arquitectura.
