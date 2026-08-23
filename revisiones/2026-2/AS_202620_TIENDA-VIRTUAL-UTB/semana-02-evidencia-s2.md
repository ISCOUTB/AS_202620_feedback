# Evidencia S2 · Tienda virtual UTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `456365b647c0555ca3e098797a1e57afb2f93447` · `2026-08-15T14:07:47-05:00` («Evidencia S2.1») |
| Cierre de la actividad | `2026-08-17T05:00:00Z` (domingo 16 de agosto, medianoche Colombia) |
| Visibilidad | pública, comprobada con `git ls-remote` sin autenticación (revisiones/2026-2/_meta/lsremote.txt) |

Comandos principales ejecutados: `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only 456365b`; `git show 456365b:docs/…`; `git grep -niE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template' 456365b -- docs/arc42/`; `git shortlog -sne HEAD`; `git log --format='%cI %h' -- docs/ia.md`; `git log --after='2026-08-17T05:00:00Z'`.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-template-EN.md:18-69`: visión general del alcance, 4 *quality goals* con motivación y tabla de *stakeholders* con expectativas | No cumple | No hay objetivos de negocio (los *quality goals* son atributos de calidad) ni se dice a quién le importa cada objetivo; las expectativas de la tabla de interesados no se ligan a ningún objetivo. |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/arc42-template-EN.md:71-80`: tabla Constraint/Type/Justification (Technical, Scope, Organizational, Infrastructure) | Cumple | Clasifica y dice de dónde viene cada una. No hay restricciones legales declaradas, de modo que no falta esa clase. |
| Restricciones separadas de los requisitos | §2 con restricciones y §1 «Requirements Overview» con el alcance funcional por separado | Cumple | Ninguna restricción es en realidad un requisito funcional; todas son limitaciones con justificación. |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/arc42-template-EN.md:82-109`: actores (comprador, administrador, responsable de inventario), sin sistemas externos, coherente con `docs/c4/context.md` | Cumple | Mismos actores y mismos sistemas (ninguno externo) que el C4. |
| Entre 3 y 5 escenarios de calidad redactados | `docs/escenarios-calidad.md`: 4 escenarios numerados (1-4) | Cumple | La sección 10 del arc42 (`arc42-template-EN.md:256-260`) está vacía; los escenarios viven en `docs/escenarios-calidad.md`. Desviación de estructura anotada (el artefacto se evalúa donde está, CONTRATO §2). |
| Cada escenario con sus seis partes y medida numérica | `docs/escenarios-calidad.md`: cada escenario con Fuente/Estímulo/Ambiente/Artefacto/Respuesta/Medida. Medidas: «100% rechazadas», «máximo 4 pantallas/pasos», «menos de 2 segundos», «~5 usuarios simultáneos» | Cumple | Cifra + unidad + condición de carga en los cuatro escenarios. |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arbol-utilidad.md`: hojas con IN (impacto de negocio) y RA (riesgo arquitectónico) en escala H/M/L, hojas con (*) ligadas a los 4 escenarios | Cumple | No es lista plana: prioriza por impacto y riesgo y coincide con los escenarios redactados. |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/context.md`: mermaid `flowchart TD`, flechas etiquetadas («Consulta catálogo…», «Administra catálogo…», «Consulta y actualiza existencias») | No cumple | Está como código (mermaid), no imagen; flechas etiquetadas sí; falta la leyenda de tipos de elementos (persona/sistema). |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md`: una única fila («Seguridad»), sin enlaces; ningún escenario se alcanza desde la tabla | No cumple | La fila de Seguridad no enlaza al escenario 1; los escenarios de usabilidad, rendimiento y disponibilidad no tienen fila de aspecto desde la que llegar. Los enlaces existen desde `docs/arbol-utilidad.md`, que no es la tabla de aspectos. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clone y ls-remote sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 456365b`: `README.md`, `docs/arc42/`, `docs/adr/.gitkeep`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Las seis rutas presentes. |
| Estado calificado identificable | sin etiquetas; hash `456365b6…` + `%cI 2026-08-15T14:07:47-05:00` | Cumple | Commit vigente al cierre identificado y citado. |
| Nombres de ADR según la convención | `docs/adr/` sin ADR todavía | Cumple | Nada que viole la convención. |
| ADR aceptados no reescritos | sin ADR en el periodo | Cumple | Nada que reescribir. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md`: último commit 2026-08-09, fuera del periodo S2 | No cumple | Sin commits entre el 10 y el 16 de agosto; además el registro no incluye qué se rechazó y por qué (CONTRATO §6). |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin salida | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` al cierre: 3 identidades (Jasen, RAZOR7150, pxtroniwnl); `shalom-A26` firma por primera vez el 2026-08-21 (`f4602a3`, tras el cierre) | No cumple | Shalom Jhoanna Arrieta Marrugo no aparece en el historial al cierre S2. |

## Recuento de criterios

6 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Correspondencia cuenta↔estudiante dejada al docente (los correos de los commits hacen evidente la atribución: `correo omitido`, `correo omitido`, `correo omitido`, `correo omitido`).

## Hallazgos para la planilla

- Entrega tardía posterior al cierre S2: `f4602a3` (2026-08-21T13:22:16-05:00, «evidencia s3», autor shalom-A26). No es contenido de S2; queda registrado.
- `docs/arc42/arc42-template-EN.md` §10 (Quality Requirements) vacía: los escenarios están en `docs/escenarios-calidad.md` (desviación de estructura).
- C4 de contexto sin leyenda de tipos de elementos.
- `docs/aspectos.md` sigue sin la tabla de 8 columnas ni enlaces a escenarios (se arrastra de S1).
- Escenarios sin declaración de cómo se medirán (herramienta, carga, umbral): las medidas son manuales o con prueba simple; anotado para el corte 1.
- Contribución al cierre S2: Jasen 4 commits, Levis (RAZOR7150) 2, Alejandro (pxtroniwnl) 2, Shalom 0.
