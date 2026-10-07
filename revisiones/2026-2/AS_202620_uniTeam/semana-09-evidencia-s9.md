# Evidencia S9 definitiva · uniTeam

Revisión actualizada tras el cierre. Estado congelado al **2026-10-05T05:00:00Z** (domingo a medianoche en Colombia).

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_uniTeam |
| Rama principal remota | `master` |
| Base S5 publicada | `dc14298c32a4fde0956266b0300063c24d7a9486` |
| Base S8 | `0f3da0f36f8cd7b829106667de88a56a1bc81f54` |
| Estado revisado | `6e04b35317a0a68d239ae85c71cd60e21982b195` en `origin/master` (2026-10-04T16:37:55-05:00) |
| Punta actual / S10 preliminar | `6e04b35317a0a68d239ae85c71cd60e21982b195` · 2026-10-04T16:37:55-05:00 |
| Observado | 2026-10-06T21:29:11.332360Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

El delta se contrasta contra S8; los artefactos previos sirven de línea base y no vuelven a premiarse por existir. Los cambios tardíos se separan en overall.

## Matriz de la ficha S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [docs/ia.md:86](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L86) identifica el refactor real de Mis tareas; [app/application/servicio_tareas.py:219–232](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/app/application/servicio_tareas.py#L219-L232) y [app/infrastructure/repositorios.py:170–191](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/app/infrastructure/repositorios.py#L170-L191) están cambiados en el delta S8→S9. |
| Cadena completa navegable para esa porción | Cumple | [docs/aspectos.md:29](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/aspectos.md#L29) A-12 enlaza requisito, C4, ADR 0013, servicio/repositorio, pruebas y medición; se recorrieron los destinos. |
| ADR con la decisión argumentada por el equipo | Cumple | [docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md:3–6](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md#L3-L6) y [docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md:19–49](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md#L19-L49): decisión aceptada, alternativas JOIN/puerto/proyección por eventos, efectos de autorización, costo y reversión; [docs/ia.md:38–39](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L38-L39) registra decisión del equipo. |
| Prueba que falla ante el defecto que cubre | Cumple | [docs/calidad/mediciones/mis-tareas-limite-contexto.md:19–23](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/mediciones/mis-tareas-limite-contexto.md#L19-L23) registra cuatro fallos antes del cambio y cuatro pases después; [test/test_limites_contexto.py:21–33](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/test/test_limites_contexto.py#L21-L33) detecta tablas ajenas mediante AST. Procedimiento documentado admitido por la ficha; no ejecutado por el revisor. |
| Medición del escenario asociado | Cumple | [docs/calidad/mediciones/mis-tareas-limite-contexto.md:7–39](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/mediciones/mis-tareas-limite-contexto.md#L7-L39): 3×300 peticiones con 200 tareas/20 proyectos, p95 posterior 11,5–11,8 ms contra 2000 ms, tablas cruzadas de 2 a 0. Medición local SQLite, secuencial y en proceso; no acredita ESC-01 completo con 30 usuarios ni MySQL/despliegue. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | [docs/ia.md:86](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L86): identifica aceptado, dos alternativas rechazadas con razón y correcciones de percentil/importación; decisiones propias en D-025/D-026. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/ia.md:90–100](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L90-L100) y [docs/calidad/propiedad-datos.md:28–46](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/propiedad-datos.md#L28-L46) describen causa, ubicación y corrección; el servicio consulta Proyectos por puerto y el repositorio filtra solo TareaTabla. Persiste una dependencia bidireccional por puertos señalada en la auditoría. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [docs/ia.md:102–108](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L102-L108): no añade dependencias, confirmado por diff de requirements.txt/web/package.json. Registra 18/18 existentes y comprobación de procedencia PyPI/npm; [scripts/verificar_dependencias.py:28–62](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/scripts/verificar_dependencias.py#L28-L62) es inspeccionado, no ejecutado. El método npm consulta paquete y origen, sin prueba exhaustiva de resolución de todo rango/transitivas. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido estático del árbol y revisión de coincidencias: sin credenciales productivas reales detectadas. [.env.example:1–21](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/.env.example#L1-L21) contiene marcadores; [compose.yaml:9–27](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/compose.yaml#L9-L27) acota valores de desarrollo a contenedor local; [.github/workflows/ci.yml:23–40](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/.github/workflows/ci.yml#L23-L40) genera contraseña efímera. No se reproducen valores en este informe. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | [docs/adr/0014-no-incorporar-un-componente-generativo.md:3–32](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0014-no-incorporar-un-componente-generativo.md#L3-L32): ADR aceptado de no incorporar generación; justifica requisito, presupuesto, privacidad y latencia, compara alternativas y fija condiciones para reabrir. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público ISCOUTB/AS_202620_uniTeam correcto; [README.md:14–23](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/README.md#L14-L23). |
| Estructura mínima presente | Cumple | README y docs/arc42, adr, c4, aspectos.md, ia.md presentes; [docs/aspectos.md:44–51](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/aspectos.md#L44-L51). |
| Estado calificado identificable | Cumple | master y hash/fecha del encabezado; último commit ≤ cierre, sin etiquetas. |
| Nombres de ADR según la convención | Cumple | ADR 0001–0014 con nombres NNNN-titulo-en-kebab-case.md; [docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md:1–6](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md#L1-L6). |
| ADR aceptados no reescritos | No cumple | Historial leído: ADR 0011 creado en 369b0d9 y editado en 0f3da0f tras figurar Aceptada; [docs/adr/0011-mantener-la-api-despierta-con-un-sondeo-externo.md:3–7](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0011-mantener-la-api-despierta-con-un-sondeo-externo.md#L3-L7). El reemplazo parcial de 0008 por 0011 está declarado, pero no reemplaza la edición posterior de 0011. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:86–121](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L86-L121) aporta entrada y auditoría del periodo S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [CI del hash actual](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/37236877375) concluye failure. [.github/workflows/ci.yml:161–179](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/.github/workflows/ci.yml#L161-L179) exige scanner y espera Quality Gate, pero configuración no equivale a resultado; falta gate público satisfactorio de este estado. [Comprobación de despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/37512258356) también falla. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido de árbol e historial con patrones de alta especificidad sin credenciales reales confirmadas; valores locales/marcadores revisados en [compose.yaml:9–27](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/compose.yaml#L9-L27). Alcance de patrones declarado; no prueba sobre secretos externos. |
| Contribución de todos los integrantes | No verificado | 75 commits con siete firmas de autor y variantes; no se atribuyen las firmas a las cuatro personas de matrícula sin correspondencia confirmada. |

## Recuento y nota sugerida

**10 de 10 criterios Cumple. Nota sugerida: 5.0 = 1 + 4 × (10/10). Propuesta al docente; la nota final se fija en Moodle.** No verificado no se convierte en Cumple ni en una ejecución fallida.

## Estado global del proyecto (overall)

Punta de la misma rama: `6e04b35317a0a68d239ae85c71cd60e21982b195` (2026-10-04T16:37:55-05:00). Hay **6 commits en el delta S8→S9** y **0 commits posteriores al cierre S9**. La punta incorpora seis commits S9 que corrigen la lectura cruzada de tablas y añaden ADR aceptados, pruebas, medición y auditoría. No hay tardíos. Persisten CI y chequeos de despliegue en failure; se distinguen esos runs de los resultados locales documentados.

La aplicación pública devolvió HTTP 200 en 6,029311 s en la consulta iniciada 2026-10-06T21:21:59Z. La consulta de /health iniciada 2026-10-06T21:22:05Z agotó 25,001788 s sin bytes recibidos (curl 28, HTTP 000); es timeout de esta comprobación, no prueba concluyente de caída del servidor. Un segundo intento de /health iniciado 2026-10-06T21:27:21Z también agotó 90,000219 s sin bytes (HTTP 000). No se probó el flujo autenticado.

### Hallazgos abiertos

- Recuperar CI del hash actual y comprobación periódica de despliegue; publicar resultado verificable del scanner y Quality Gate.
- Medir el costo de consulta adicional en MySQL y carga real: la evidencia S9 es SQLite secuencial en proceso.
- Precisar la asignación operativa S10; no equipararla automáticamente con ESC-01/ESC-03.
- Completar arc42 §8 y reconciliar auditoría/mapa/ADRs con el MVP actual.
- No reescribir ADR aceptados; el antecedente de ADR 0011 sigue abierto.
- Confirmar correspondencia de firmas del historial con integrantes, sin atribuciones por parecido.

### Hallazgos cerrados o sustituidos con evidencia actual

- Ya hay incremento S9 y cadena A-12 completa: [docs/aspectos.md:29](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/aspectos.md#L29).
- Auditoría de erosión, corrección y prueba negativa ahora documentadas: [docs/calidad/mediciones/mis-tareas-limite-contexto.md:19–23](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/mediciones/mis-tareas-limite-contexto.md#L19-L23) y [docs/calidad/propiedad-datos.md:28–46](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/propiedad-datos.md#L28-L46).
- La no incorporación generativa ya es una decisión aceptada en ADR 0014: [docs/adr/0014-no-incorporar-un-componente-generativo.md:3–32](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0014-no-incorporar-un-componente-generativo.md#L3-L32).
- El registro de IA sí creció en S9 con aceptado/corregido/rechazado y verificación de dependencias: [docs/ia.md:86–121](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L86-L121).
- La planilla antigua dice sin URL, pero el README publica sitio/API y la portada respondió HTTP 200. [README.md:18–22](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/README.md#L18-L22). No se da por probado el flujo.

## Próximos pasos

La nueva porción de Mis tareas completa la cadena exigida: decisión aceptada, código, prueba que detecta el defecto, medición y auditoría de erosión. Mantengan explícito que la medición es SQLite en proceso; todavía falta comprobar el costo de la consulta extra en MySQL. El cumplimiento de S9 no cierra los fallos actuales del pipeline ni el Quality Gate.
