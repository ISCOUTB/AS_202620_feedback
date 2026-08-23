# Evidencia S2 · TRACTAR

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `0a238559d612a83d0f1dcfe87fbdb813e13acbca` · `2026-08-16T20:05:46-05:00` («Docs: I added a adr doc») |
| Cierre de la actividad | `2026-08-17T05:00:00Z` (domingo 16 de agosto, medianoche Colombia) |
| Visibilidad | pública, comprobada con clone y `git ls-remote` sin autenticación (revisiones/2026-2/_meta/lsremote.txt) |

Comandos principales ejecutados: `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only 0a23855`; `git show 0a23855:docs/…`; `git grep -niE '<[a-z /]+>|\bTODO\b|lorem ipsum' 0a23855 -- docs/arc42/`; `git shortlog -sne HEAD`; `git log --format='%cI %h' -- docs/ia.md`; `git log --after='2026-08-17T05:00:00Z'`.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-template-EN.md:18-57`: visión del problema, 5 *quality goals* con motivación y tabla de *stakeholders* con expectativas | No cumple | No hay objetivos de negocio (los *quality goals* son atributos de calidad) ni se dice a quién le importa cada objetivo. Además, la tabla de interesados nombra un equipo que no corresponde al de `EQUIPOS.md` («Elías Ramos», «Dilan Gonzales»; faltan Sebastian Garcia y Joriel Barros). |
| arc42 sección 2 con restricciones clasificadas y justificadas | `arc42-template-EN.md:59-85`: tablas de restricciones técnicas, organizacionales y legales/normativas (Ley 1581) con origen e implicación | Cumple | Clasificación completa (incluye legales) y cada restricción dice de dónde viene. |
| Restricciones separadas de los requisitos | §2 con solo restricciones justificadas; los requisitos funcionales se describen en §1 | Cumple | Anotado: «Debe funcionar sin conexión y sincronizar…» se presenta como restricción técnica pero es más bien un requisito funcional derivado del alcance (el propio equipo lo anota «RNF derivado del alcance del producto»). |
| arc42 sección 3 con actores y sistemas externos | `arc42-template-EN.md:87-117`: comunicación Propietario/Conductor/Tractar/Excel y contexto técnico, coherente con el C4 | Cumple | Incoherencia menor: el texto dice «no hay integración con sistemas externos de terceros» mientras el pie del diagrama declara «dos sistemas externos» (Excel exportado y almacenamiento local). |
| Entre 3 y 5 escenarios de calidad redactados | `arc42-template-EN.md:286-344`: 5 escenarios numerados QS-01…QS-05 dentro de la sección 10 | Cumple | — |
| Cada escenario con sus seis partes y medida numérica | QS-01…QS-05 con Fuente/Estímulo/Ambiente/Artefacto/Respuesta/Medida: ≥99% (7am-10pm), ≤3 s (2GB RAM), ≥300 usuarios simultáneos, 0% accesos no autorizados + contraseñas con hash, ≤3 intentos y <2 minutos | Cumple | Cifra + unidad + condición de carga en los cinco. |
| Árbol de utilidad que prioriza por impacto y riesgo | `arc42-template-EN.md:259-284`: árbol por ramas de calidad con [Importancia / Dificultad] Alta/Media/Baja y los 5 escenarios ligados a las ramas | Cumple | Prioriza por importancia y dificultad; las ramas coinciden con QS-01…QS-05. |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/c4_nivel1_contexto.png` (PNG, 84 KB; duplicado en `docs/arc42/images/`) | No verificado | El diagrama está solo como imagen y el agente no pudo inspeccionarlo visualmente (sin soporte de imágenes). El pie en §3 describe actores, sistema y dos sistemas externos, pero no sirve de evidencia de leyenda ni de flechas etiquetadas. Qué haría falta: abrir la imagen o entregar el diagrama como código (`workspace.dsl` citado en §3 no está en el repo). |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md`: filas A-01 y A-04 seguidas al azar: sus enlaces apuntan a `arc42/10_requisitos_calidad.md#qs-…`, archivo que no existe (el árbol solo tiene `arc42-template-EN.md`) | No cumple | Los enlaces están rotos; los escenarios están embebidos en `aspectos.md` pero las filas de la tabla no llevan a ellos. Celda con enlace roto = hueco (CONTRATO §5). |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clone y ls-remote sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 0a23855`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Las seis rutas presentes. Desviaciones: `ficha_problema.md` en la raíz y ADR con nombre «doc». |
| Estado calificado identificable | sin etiquetas; hash `0a238559…` + `%cI 2026-08-16T20:05:46-05:00` | Cumple | Commit vigente al cierre identificado y citado. |
| Nombres de ADR según la convención | `docs/adr/doc` | No cumple | El archivo no sigue `NNNN-titulo-en-kebab-case.md`: sin número, sin extensión, sin título. Además es una plantilla sin rellenar. |
| ADR aceptados no reescritos | el único ADR es la plantilla de `docs/adr/doc` | Cumple | No hay ADR aceptado que reescribir. |
| `docs/ia.md` al día para la semana | commits sobre el archivo el 2026-08-16 (`74fdb96`, `e84871f`) | No cumple | El formato incluye «Qué se usó / descartó», pero las entradas no registran ningún rechazo concreto con su motivo técnico (CONTRATO §6). |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'` sin salida | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: una sola persona (Sebastian Garcia Devoz) con dos identidades (15 commits en total) | No cumple | Joriel Samir Barros Pena, Geronimo Alberto Cadena Garcia y Mateo Alfonso Millan Barraza no aparecen en el historial. |

## Recuento de criterios

6 de 9 criterios de la ficha cumplidos (1 No verificado, 2 No cumplen).

## No verificado / pendientes

- Leyenda y flechas del C4: pendiente de abrir la imagen o de que el equipo entregue el diagrama como código (`workspace.dsl` no está en el repo).
- Correspondencia cuenta↔estudiante: los correos de los commits (`correo omitido`, `correo omitido`) son ambos de Sebastian Garcia Devoz; lo confirma el propio `EQUIPOS.md`.

## Hallazgos para la planilla

- Sin entregas tardías posteriores al cierre S2 (`git log --after='2026-08-17T05:00:00Z'` vacío).
- Todo el trabajo del periodo lo firma una sola persona con dos identidades de git; 3 de 4 integrantes sin commits.
- `docs/adr/doc` fuera de convención (sin `NNNN-titulo.md`) y sin contenido.
- Enlaces rotos en `docs/aspectos.md` hacia `arc42/10_requisitos_calidad.md` (inexistente), y restos de edición en el propio archivo (fragmento suelto «C2/C3: pendiente (S4, S6)…» y una sección final que dice que A-01 no tiene escenario cuando QS-05 sí lo define).
- Tabla de interesados de §1 con nombres que no coinciden con los integrantes de `EQUIPOS.md`.
- Para el corte 1: las medidas de los escenarios no declaran cómo se medirán (herramienta, carga, umbral).
