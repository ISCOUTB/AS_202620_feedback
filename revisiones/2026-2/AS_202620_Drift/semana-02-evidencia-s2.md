# Evidencia S2 · Drift

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `23fb8c2953ce2e628bdf05375257b72eb6cba121` · 2026-08-16T22:39:37-05:00 · «Rename c4_contexto to c4_contexto.md» |
| Cierre | 2026-08-17T05:00:00Z (domingo 16 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only 23fb8c29`; `git show 23fb8c29:docs/...`; `git grep -nIE '<[a-z ]+>|TODO|lorem ipsum'`; `git grep` de secretos; `git shortlog -sne 23fb8c29`; `git log --after='2026-08-17T05:00:00Z'` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42_1_introduccion_objetivos.md` | Cumple | Objetivos de calidad priorizados (§1.2) y tabla de interesados con sus objetivos (§1.3). Nota: el archivo vive en `docs/`, no en `docs/arc42/` (desviación de ruta). |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42_2_restricciones.md` | Cumple | Clasificadas por origen (organizacionales, académicas/plazo, tecnológicas, fuentes externas, proceso IA, rendimiento) y justificadas. Observaciones: no hay categoría legal; §2.3 es condicional; §2.6 son metas de calidad (p95) ubicadas entre restricciones. |
| Restricciones separadas de los requisitos | 02 frente a funcionalidades en 01 y escenarios en `docs/Escenarios.md` | Cumple | Los requisitos funcionales están en §1.1. El propio `docs/ia.md` narra que retiraron de la sección 2 lo que era requisito funcional. Anotar: §2.6 duplica medidas que pertenecen a los escenarios. |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42_3_contexto_alcance.md` frente a `docs/c4_contexto.md` | Cumple | Actores y sistemas externos idénticos en ambos: jugador, administrador, tiendas digitales, proveedor de información de videojuegos. |
| Entre 3 y 5 escenarios de calidad redactados | `docs/Escenarios.md` | Cumple | 5 escenarios numerados (1–5). Fuera de `docs/arc42/` (desviación de ruta). |
| Cada escenario con sus seis partes y medida numérica | Escenario 1 (cita completa) en `docs/Escenarios.md` | Cumple | Los 5 tienen Fuente, Estímulo, Artefacto, Entorno, Respuesta y Medida verificable. Medidas numéricas con unidad y carga: E1/E2 «≤3 s en p95 con hasta 50 usuarios concurrentes», E3 «máximo 3 interacciones», E4 «≤5 s en p95», E5 «≤5 s». |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arbol_utilidad.md` (diagrama Mermaid) | No cumple | Es una descomposición jerárquica de atributos con objetivos, pero sin priorización visible por impacto/riesgo (sin pares de valor ni niveles). La prioridad 1–5 está en la sección 1, no en el árbol. Las hojas sí coinciden con las medidas de los escenarios redactados. |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4_contexto.md` (código Mermaid) | No cumple | Flechas etiquetadas («Busca videojuegos», «Consulta precios»…) y los 4 elementos externos correctos. Sin leyenda ni estilos C4 de persona/sistema (es un `flowchart` plano). Ruta desviada: `docs/c4_contexto.md` en vez de `docs/c4/`. |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` en `23fb8c29` | No cumple | `docs/aspectos.md` sigue en prosa (mantenibilidad), sin tabla de filas por aspecto y sin enlaces a los escenarios. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree -r --name-only 23fb8c29` | No cumple | 3 de 6 rutas literales: `README.md` ✓, `docs/aspectos.md` ✓, `docs/ia.md` ✓. Los archivos arc42 (`docs/arc42_*.md`) y el C4 (`docs/c4_contexto.md`) existen pero fuera de `docs/arc42/` y `docs/c4/`; `docs/adr/` no existe. Desviación de estructura, no ausencia de artefactos. |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | Hash `23fb8c29…` con `%cI` 2026-08-16T22:39:37-05:00. |
| Nombres de ADR según la convención | sin `docs/adr/` | Cumple (vacuo) | Sin ADR todavía. |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md` | Cumple | `8df39f3` (2026-08-16T00:13:02-05:00, JoshuaR01) dentro del periodo S2; el archivo narra el uso de IA para arc42 y la revisión de restricciones. Sin entradas de rechazos con motivo (pendiente). |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex §9), `.env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne 23fb8c29` | Cumple | 5 identidades, consolidadas en 4 personas: `maufern4ndez` (20), `JoshuaR01` (2) + `JoshXX` (5, mismo correo `correo omitido`), `JerryDBM` (6), `lmpdiaz12` (4). Los 4 integrantes cubiertos; desbalance (20 de 37 commits de una persona). |

## Recuento de criterios

- Ficha: **6 de 9** criterios Cumple.

## No verificado / pendientes

- Consolidación oficial de `JoshuaR01`/`JoshXX` (mismo correo) con Joshua David Reyes Leones contra la matrícula.

## Hallazgos para la planilla

- Entregas tardías (posteriores al cierre S2): serie del 2026-08-22 — `d5b915a` «Create arc42» y renombrados `755c481`…`dbb4283` (reorganización de arc42), `083dffd`/`b6a4952` (ia.md), `3692d6d` (matriz.md), `f0d1018`…`398f186` (README). No cuentan para S2.
- Documentación arc42 fuera de `docs/arc42/` y C4 fuera de `docs/c4/` en el cierre S2 (reorganizada el 08-22, tras el cierre).
- `docs/aspectos.md` sigue sin la tabla de 8 columnas ni enlaces a escenarios (arrastre desde S1).
- Árbol de utilidad sin priorización por impacto/riesgo.
- C4 sin leyenda y sin estilos C4.
- Desbalance de contribución en el periodo (20/37 commits de una persona).
- De los 5 escenarios, todos tienen medida comprobable; E1/E2 declaran carga (50 usuarios) y E1–E5 umbral en p95 o interacciones, pero ninguno declara herramienta de medición: pendiente para el corte 1.
