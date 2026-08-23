# Evidencia S2 · XALD

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `8c37887ab83954a3d97f12e9782f93b49a460ced` · `2026-08-16T13:45:27-05:00` («Merge pull request #1 from ISCOUTB/experimental») |
| Cierre de la actividad | `2026-08-17T05:00:00Z` (domingo 16 de agosto, medianoche Colombia) |
| Visibilidad | pública, comprobada con clone y `git ls-remote` sin autenticación (revisiones/2026-2/_meta/lsremote.txt) |

Comandos principales ejecutados: `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only 8c37887`; `git show 8c37887:docs/…`; `git grep -niE 'fuente|estímulo|artefacto|entorno|respuesta|medida' 8c37887 -- docs/arc42/`; `git shortlog -sne 8c37887`; `git log -- docs/adr/`; `git log --after='2026-08-17T05:00:00Z'`.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-template-EN.md:6-56`: visión del problema, 4 *quality goals* con descripción y tabla de *stakeholders* con expectativas | No cumple | No hay objetivos de negocio (los *quality goals* son atributos) ni se dice a quién le importa cada uno; las expectativas de la tabla de interesados no se ligan a objetivos. |
| arc42 sección 2 con restricciones clasificadas y justificadas | `arc42-template-EN.md:58-78`: RT-01…RT-05 (técnicas) y RO-01/RO-02 (organizacionales) | No cumple | Falta la clase legal (la Ley 1581 se cita en §1 y en §4, no en §2), y varias restricciones no dicen de dónde vienen: RT-02, RT-03 y RT-05 describen decisiones sin justificación de origen. |
| Restricciones separadas de los requisitos | §2 con restricciones; los requisitos funcionales están en la narrativa de §1 | Cumple | Anotado: RT-02 (offline-first), RT-03 (cifrado) y RT-05 (LWW) son más decisiones de diseño que condiciones impuestas. |
| arc42 sección 3 con actores y sistemas externos | `arc42-template-EN.md:80-133`: tabla de negocio con Usuario, Banco/SMS, Backend XALD y Gemini; el C4 (`docs/c4/c4.md`) no incluye el Backend | No cumple | §3 y el C4 no coinciden: el «Backend XALD / Servidor» está en §3 pero no en el diagrama. Además §3 dice que «este diagrama de texto es la base para armar después el C4 de contexto formal», cuando `docs/c4/c4.md` ya existe. |
| Entre 3 y 5 escenarios de calidad redactados | §10 («Quality Requirements») vacía (`arc42-template-EN.md:305-309`); en §1 hay una tabla de 3 resúmenes («Registro offline», «Fallo de IA», «Ingesta CSV») sin formato de escenario | No cumple | No hay escenarios numerados en §10; los 3 de §1 son resúmenes de 3 columnas, no escenarios de seis partes. |
| Cada escenario con sus seis partes y medida numérica | no existe ningún escenario con las seis partes (fuente/estímulo/artefacto/entorno/respuesta/medida) | No cumple | El grep de la ficha sobre `docs/arc42/` solo encuentra la tabla «Escenario | Estímulo | Respuesta medible». |
| Árbol de utilidad que prioriza por impacto y riesgo | ausente en el repositorio | No cumple | No hay árbol de utilidad en `docs/arc42/` ni en otra ruta. |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/c4.md`: mermaid con flechas etiquetadas («1. Notificación SMS», «2. Inferencia / JSON», «3. UI / Reportes») y classDef de colores | No cumple | Como código (mermaid) y con flechas etiquetadas, pero sin leyenda que explique los colores/tipos de elemento; además falta el Backend que §3 sí declara. |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md`: 4 filas (A-01…A-04) con la columna ADR rellena con números sin enlace («002», «001»…); no hay escenarios que alcanzar | No cumple | No hay escenarios redactados y las celdas ADR no son navegables (texto plano); celda sin destino = hueco (CONTRATO §5). |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clone y ls-remote sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 8c37887`: `README.md`, `docs/arc42/`, `docs/adr/` (ADR-001…005), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Las seis rutas presentes desde S2. |
| Estado calificado identificable | sin etiquetas; hash `8c37887a…` + `%cI 2026-08-16T13:45:27-05:00` | Cumple | — |
| Nombres de ADR según la convención | `docs/adr/ADR-001.md` … `ADR-005.md` | No cumple | El nombre no sigue `NNNN-titulo-en-kebab-case.md`: prefijo «ADR-» y sin título descriptivo. |
| ADR aceptados no reescritos | cada ADR tiene un único commit de creación (15/08 y 16/08) y ninguno se editó después; ADR-001 en estado «Aprobado» | Cumple | No hay reescrituras de ADR aceptados. |
| `docs/ia.md` al día para la semana | commit `06b7696` (2026-08-16); el registro incluye rechazos con motivo (p. ej. «Se rechazó la complejidad propuesta…») | Cumple | — |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'` sin salida | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne 8c37887`: 4 identidades — dilanbejarano011 (28), colmenares2007-crypto (17), xaviergarciadiaz20-commits (9), axeljruiz717-hash (4) | Cumple | Los 4 integrantes contribuyen; hay un PR (merge #1) en el historial. |

## Recuento de criterios

1 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Nada que requiera ejecución o credenciales; lo pendiente es contenido, no comprobación.

## Hallazgos para la planilla

- Actividad posterior al cierre S2: `c05d607` («Create PROYECTO_XALD») y `d123c65` («Delete PROYECTO_XALD»), ambos del 2026-08-23 (hoy). No son entrega de S2; parecen prueba o accidente y quedan registrados.
- §10 de arc42 vacía; sin escenarios de seis partes ni árbol de utilidad: el núcleo de la entrega S2 falta.
- C4 sin leyenda y sin el Backend que §3 declara; §3 afirma que el C4 se hará «después» pese a que `docs/c4/c4.md` ya existe.
- `docs/aspectos.md`: restos de edición («```[cite: 1]») y celdas ADR con números sin enlace; la tabla ya tiene las 8 columnas del curso.
- ADR-001…005 con nombre fuera de convención.
- Para el corte 1: ninguna medida declara cómo se medirá (herramienta, carga, umbral).
