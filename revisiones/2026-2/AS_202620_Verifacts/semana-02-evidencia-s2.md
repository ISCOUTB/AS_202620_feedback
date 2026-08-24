# Evidencia S2 · Verifacts (Grupo X)

> **Excepción docente**: por decisión del profesor, esta evidencia se evalúa sobre el estado
> actual del repositorio (HEAD `8ded7cf`, 2026-08-23), no sobre el commit al cierre
> (2026-08-17T05:00:00Z), que no existe: el primer commit es del 18-ago. Solo por esta vez.

## Datos

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | HEAD `8ded7cf3f975553a88dd833fd58051ead7965b4d` · 2026-08-23T19:23:38-05:00 (excepción docente) |
| Comandos | `git ls-tree -r HEAD`; `git show HEAD:docs/…`; `git grep -niE 'escenario' HEAD -- docs/`; `git shortlog -sne HEAD`; lectura de `resumen-entrega.pdf` (pdftotext) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42.md` §1.3-1.4-1.6 | No cumple | los objetivos específicos (§1.4) son funcionalidades; los usuarios (§1.6) no se ligan a cada objetivo |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42.md` §2 y `docs/restricciones.md` | No cumple | justificadas con impacto arquitectónico, pero sin clasificación técnica/organizativa/legal |
| Restricciones separadas de los requisitos | requisitos en §1.4/§1.5; restricciones en §2 y `docs/restricciones.md` | Cumple | ninguna restricción es un requisito funcional |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42.md` §3.2 y `docs/c4-contexto.md` | Cumple | mismos actores (Usuario, Sitio web externo, GitHub, SonarCloud) en §3 y en el diagrama; desviación de ruta (C4 fuera de `docs/c4/`) |
| Entre 3 y 5 escenarios de calidad redactados | `git grep -iE 'escenario' HEAD -- docs/`: no hay archivo de escenarios | No cumple | `resumen-entrega.pdf` dice entregar 5 escenarios en `docs/escenarios-de-calidad.md`, que NO existe en el repositorio; el ADR solo tiene 4 resúmenes de una línea |
| Cada escenario con sus seis partes y medida numérica | no existen escenarios con las seis partes | No cumple | sin escenarios, no hay medida que comprobar |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arbol_utilidad.md` | No cumple | lista plana de atributos (Utilidad/Calidad), sin priorización por impacto/riesgo |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4-contexto.md` (mermaid) | No cumple | flechas etiquetadas («Introduce texto o URL…», «Solicita contenido»), pero sin leyenda |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` | No cumple | narrativo, sin tabla de 8 columnas ni enlaces |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ls-remote` y clon sin autenticación OK | Cumple | — |
| Estructura mínima presente | `git ls-tree -r HEAD` | No cumple | `docs/arc42.md` único, `docs/IA.md`, sin `docs/c4/` |
| Estado calificado identificable | HEAD `8ded7cf` · 2026-08-23T19:23:38-05:00 (excepción docente) | Cumple | hash y fecha registrados |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | — |
| ADR aceptados no reescritos | un solo ADR, sin reescrituras | Cumple | estado «Propuesto» |
| `docs/ia.md` al día para la semana | `docs/IA.md`, commit `d42dd18` (2026-08-18) | No cumple | nombre desviado y sin registro de uso con rechazos |
| Sin credenciales en el repositorio ni en el historial | `git grep` §9 sin coincidencias, sin `.env` | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: 1 identidad para 3 integrantes | No cumple | solo `PedroC1213` (25 commits) |

## Recuento y nota sugerida

2 de 9 criterios Cumple. Propuesta al docente (regla local no publicada): `1 + 4 × (2/9) = 1,9`.

## Hallazgos para la planilla

- **Discrepancia con la entrega**: `resumen-entrega.pdf` declara entregar `docs/escenarios-de-calidad.md` (5 escenarios con medida), `docs/arc42/01,02,03.md` y `docs/diagrams/c4-contexto.md` — ninguno de esos archivos está en el repositorio. El repositorio es la entrega (CONTRATO §12).
- Núcleo de S2 pendiente: escenarios con seis partes y medida numérica, priorización del árbol.
- ADR-0001 bien formado (contexto, opciones, decisión, consecuencias) con 4 resúmenes de escenario por atributo: buen punto de partida para completar S2.
- 2 de 3 integrantes sin aparición en el historial.
