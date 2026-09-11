# semana-05-corte1 · Recobra

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `f7c1a6c` en `origin/master` (2026-09-07T09:59:41-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash f7c1a6c, fecha 2026-09-07T09:59:41-05:00 (anterior al cierre 2026-09-10T17:00:00Z) | Cumple | El estado calificado es el último commit de master antes del cierre. |
| correcciones.md existe en la raíz del estado calificado | El árbol del hash f7c1a6c no incluye correcciones.md (ver arbol_head) | No cumple | No existe el archivo en la raíz del estado calificado. |
| Correcciones trazables y contrastadas | No hay correcciones.md que enlace hallazgos S1-S4 con evidencia | No cumple | Sin el archivo no se puede contrastar ninguna corrección. |
| S1 al día: equipo, problema y repositorio | README.md describe problema y objetivos; docs/escenarios_calidad.md y docs/arbol_utilidad.md cubren atributos; autores: Cconde31, vylrir, MiguelJacome, Fernando Isacc Conde Herrera (git shortlog) | Cumple | Equipo e identidad consolidados con .mailmap; problema y repositorio visibles. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios_calidad.md con S1-S7 y docs/Restricciones_justificadas.md con escenarios verificables | Cumple | Escenarios y restricciones documentados y trazables. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04-estrategia-solucion.md con matriz comparativa y ADR-0001/0002/0003 en docs/adr/ | Cumple | Estrategia hexagonal y decisiones ADR documentadas. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42.md, docs/c4/README.md (niveles 1 y 2), src/domain, src/application, src/infrastructure, mobile/ con código del corte vertical | Cumple | Documentación y código del corte vertical presentes. |
| Corte vertical reproducible y coherente con la arquitectura | README.md con comandos npm install/start/test y flutter; src/domain/entities/publicacion.ts, src/application/use-cases/crear-publicacion.ts, src/infrastructure/persistence/memoria-publicacion.repository.ts | Cumple | Flujo HTTP->caso de uso->dominio->puerto->adaptador coherente con C4. |
| Pipeline y pruebas respaldan el estado calificado | runs_ci: run 34135994956 success 2026-09-07T15:00:17Z (posterior al hash pero mismo commit); .github/workflows/ci.yml ejecuta npm test, test:e2e, flutter test | Cumple | CI en verde para el commit calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md con tabla de 8 columnas enlazando aspecto, requisito, C4, ADR, código, pruebas y evidencia | Cumple | Filas A1-A4 navegables con enlaces. |
| PDF u otro adjunto exigido por el aula | docs/entrega-corte1-moodle.pdf existe en el repo, pero no se puede confirmar el adjunto en Moodle | No verificado | Se requiere acceso al aula para verificar la entrega. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Recobra en org ISCOUTB, público, integrantes en historial (Cconde31, vylrir, MiguelJacome, Fernando Isacc Conde Herrera) | Cumple | Nombre y organización correctos. |
| Estructura mínima | docs/arc42.md, docs/adr/0001-0003, docs/c4/README.md, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Estructura cumple con la mínima exigida. |
| Estado del repositorio calificado | Rama master, hash f7c1a6c anterior al cierre; sin commits posteriores | Cumple | Se usó la rama principal declarada. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md, 0002-arquitectura-y-stack.md, 0003-reto-corte1-stack-obligatorio.md; nombres en kebab-case y numerados | Cumple | ADR-0001 marcado como reemplazada por ADR-0002. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas y filas A1-A4 con enlaces | Cumple | Cada fila tiene enlaces navegables. |
| Registro de uso de IA | docs/ia.md con fechas, herramientas, aceptado/rechazado y criterio del equipo | Cumple | Registro crece con commits (6 entradas). |
| README | README.md con qué es, cómo arrancar (npm install/start, flutter pub get/run) y cómo probar | Cumple | Comandos de arranque y prueba documentados. |
| Pipeline y análisis estático | .github/workflows/ci.yml con jobs backend y mobile; runs_ci con éxito en 34135994956; sonar-project.properties presente | Cumple | CI ejecuta pruebas y build; SonarCloud configurado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `f7c1a6c7c4371f1e9df38ca268895544cca43c17 2026-09-07T09:59:41-05:00 Enlazar ADR a sus commits y cubrir criterios 1-3 de la rúbrica del reto`
- **Veredicto**: con pendientes
- Resumen: El proyecto está al día en S1-S4 y CI, pero falta correcciones.md en la raíz del estado calificado, requisito explícito de S5.

Pendientes que siguen abiertos:
- Crear correcciones.md en la raíz del repositorio con trazabilidad de hallazgos S1-S4.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (8/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula
- Sustentación del corte

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado.
- No hay índice de correcciones trazables para S1-S4.
- PDF de Moodle no verificado desde el repositorio.
- Sustentación pendiente de sesión docente.
