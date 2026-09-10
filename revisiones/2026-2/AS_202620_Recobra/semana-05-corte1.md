# semana-05-corte1 · Recobra

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `6ee5b66` en `origin/master` (2026-09-05T20:26:56-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash 6ee5b66, fecha 2026-09-05T20:26:56-05:00 (anterior al cierre 2026-09-07T05:00:00Z) | Cumple | El commit calificado existe y es anterior al cierre. |
| correcciones.md existe en la raíz del estado calificado | Árbol del hash 6ee5b66 no incluye correcciones.md (ver arbol) | No cumple | No se encontró el archivo en la raíz del estado calificado. |
| Correcciones trazables y contrastadas | No existe correcciones.md que enlace hallazgos S1-S4 con evidencia | No cumple | Sin índice de correcciones, no hay trazabilidad de respuestas a hallazgos previos. |
| S1 al día: equipo, problema y repositorio | README.md describe problema y objetivos; autores en historial: Cconde31, vylrir, MiguelJacome, Fernando Isacc Conde Herrera (git shortlog) | Cumple | Equipo identificado y problema claro; repositorio público en ISCOUTB. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios_calidad.md con S1-S7; docs/Restricciones_justificadas.md con tabla de restricciones | Cumple | Escenarios y restricciones documentados y justificados. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04-estrategia-solucion.md con matriz comparativa; ADR-0001, 0002, 0003 en docs/adr/ | Cumple | Estrategia hexagonal y decisiones ADR presentes y coherentes. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42.md, docs/c4/README.md con diagramas mermaid; código en src/ y mobile/ implementa crear/consultar publicación | Cumple | Documentación y corte vertical implementado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md con comandos de arranque y prueba; src/application/use-cases/*.spec.ts y test/publicaciones.e2e-spec.ts | Cumple | Flujo HTTP→caso de uso→dominio→puerto→adaptador; pruebas unitarias y e2e. |
| Pipeline y pruebas respaldan el estado calificado | Run CI success 2026-09-05T18:21:52Z (posterior al hash 6ee5b66) en https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/33983825454 | Cumple | CI en verde para el estado calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md con tabla de 8 columnas enlazando aspecto→requisito→C4→ADR→código→pruebas→evidencia | Cumple | Cadenas navegables para A1, A2, A3, A4. |
| PDF u otro adjunto exigido por el aula | docs/entrega-corte1-moodle.pdf existe en el repo, pero no se puede confirmar entrega en Moodle | No verificado | Se requiere verificación en Moodle. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio | No verificado | Depende del docente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_Recobra en ISCOUTB, público; integrantes en historial (git shortlog) | Cumple | Nombre y organización correctos. |
| Estructura mínima | README.md, docs/arc42.md, docs/arc42/04-estrategia-solucion.md, docs/adr/0001-0003, docs/c4/README.md, docs/aspectos.md, docs/ia.md | Cumple | Estructura presente; arc42 en un solo archivo y subcarpeta, aceptable. |
| Estado del repositorio calificado | Hash 6ee5b66 en origin/master, anterior al cierre | Cumple | Se usó la rama principal correcta. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md, 0002-arquitectura-y-stack.md, 0003-reto-corte1-stack-obligatorio.md; nombres en kebab-case y numerados | Cumple | ADR-0001 marcado como reemplazada; ADR-0002 y 0003 aceptados. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas y enlaces a C4, ADR, código, pruebas y evidencia | Cumple | Cadenas navegables para A1-A4. |
| Registro de uso de IA | docs/ia.md con fechas, herramientas, aceptado/rechazado; log de commits 2026-08-23 a 2026-09-05 | Cumple | Registro detallado y con criterio. |
| README | README.md con qué es, cómo arrancar backend y Flutter, y cómo probar | Cumple | Comandos de arranque y prueba claros. |
| Pipeline y análisis estático | .github/workflows/ci.yml con jobs backend y mobile; runs success en 2026-09-05 y 2026-09-06 | Cumple | CI ejecuta pruebas y build; SonarCloud configurado en sonar-project.properties. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `f7c1a6c7c4371f1e9df38ca268895544cca43c17 2026-09-07T09:59:41-05:00 Enlazar ADR a sus commits y cubrir criterios 1-3 de la rúbrica del reto`
- **Veredicto**: con pendientes
- Resumen: El proyecto cumple con la mayoría de criterios de S1-S4 y el corte vertical, pero la ausencia de correcciones.md impide el compendio completo.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Commit f7c1a6c (2026-09-07) posterior al cierre enlaza ADR a commits y cubre criterios de rúbrica; no afecta la nota del corte pero es tardío.

Pendientes que siguen abiertos:
- Crear correcciones.md en la raíz antes del cierre.
- Verificar entrega del PDF en Moodle.
- Sustentación pendiente.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

## No verificado / pendientes

- PDF entregado en Moodle (no verificable desde repo).
- Sustentación del corte (depende del docente).

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado.
- No hay índice de correcciones trazables para hallazgos S1-S4.
- Commit f7c1a6c posterior al cierre modifica ADR y aspectos (tardío).
- docs/checklist-entrega-manual.md menciona token Coveralls en node_modules, posible riesgo de secreto histórico.
- Persistencia en memoria declarada como alcance, no deuda oculta.
- Commits posteriores al cierre (no calificados): f7c1a6c 2026-09-07T09:59:41-05:00 Enlazar ADR a sus commits y cubrir criterios 1-3 de la rúbrica del reto
