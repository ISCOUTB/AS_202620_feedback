# semana-05-corte1 · ElMapita

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `4806374` en `origin/main` (2026-09-01T08:39:54-06:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/main, hash 4806374, fecha 2026-09-01T08:39:54-06:00 (anterior al cierre 2026-09-07T05:00:00Z) | Cumple | El estado calificado es identificable y cumple la fecha límite. |
| correcciones.md existe en la raíz del estado calificado | Árbol del hash 4806374 no incluye correcciones.md; el commit b28e068 que lo agrega es posterior al cierre (2026-09-07T14:57:28-06:00) | No cumple | El archivo no existe en el estado calificado; se añadió después del cierre. |
| Correcciones trazables y contrastadas | No hay correcciones.md en el hash calificado; no se puede contrastar ningún hallazgo S1-S4 | No cumple | Sin el archivo en el estado calificado, no hay trazabilidad de correcciones. |
| S1 al día: equipo, problema y repositorio | README.md (hash 4806374) lista equipo (Diego Rosales Garza, Rodrigo Vazquez Rico, Angel Fabian Gutierrez Gomez), problema y stack; repo AS_202620_ElMapita en ISCOUTB | Cumple | El repositorio es visible y la documentación básica está presente. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42-template-EN.md (hash 4806374) secciones 1.2 y 2 incluyen objetivos de calidad y restricciones RES-01 a RES-03 | Cumple | Los escenarios de calidad y restricciones están documentados. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-estilo-arquitectonico-propuesto.md (hash 4806374) con decisión Monolito Modular, alternativas y consecuencias | Cumple | La estrategia y decisiones están documentadas en el ADR. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-EN.md, docs/c4/C4_L1_Context.md, C4_L2_Container.md y PNGs en hash 4806374; docs/CorteVertical_ElMapitaUTB.docx presente | Cumple | La documentación arc42, C4 y el corte vertical están presentes. |
| Corte vertical reproducible y coherente con la arquitectura | README.md (hash 4806374) describe comandos de arranque y pruebas, pero no hay evidencia de ejecución en el repositorio | No verificado | Se requiere ejecutar los comandos del README para verificar reproducibilidad; no hay runs de CI citados. |
| Pipeline y pruebas respaldan el estado calificado | Existe .github/workflows/ci.yml en el árbol, pero no se proporcionaron runs de CI asociados al hash 4806374 | No verificado | Falta evidencia de ejecución del pipeline para el estado calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md (hash 4806374) enlaza aspectos EC-01 a EC-04 con requisitos, C4, ADR, código y pruebas | Cumple | La tabla de aspectos es navegable y completa. |
| PDF u otro adjunto exigido por el aula | docs/cortes/corte-1.pdf existe en el árbol, pero no se puede confirmar la entrega en Moodle | No verificado | El PDF está en el repositorio; la entrega en Moodle no es verificable desde aquí. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_ElMapita en ISCOUTB, visible; integrantes declarados en README.md (hash 4806374) | Cumple | Cumple con organización, nombre y visibilidad. |
| Estructura mínima | Árbol del hash 4806374 incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | Estructura mínima presente. |
| Estado del repositorio calificado | Hash 4806374 en origin/main, fecha 2026-09-01T08:39:54-06:00, anterior al cierre | Cumple | Estado calificado correcto. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico-propuesto.md (hash 4806374) con nombre válido y contenido con contexto, decisión, consecuencias | Cumple | Un ADR con formato correcto. |
| Tabla de aspectos | docs/aspectos.md (hash 4806374) con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia | Cumple | Tabla completa con enlaces navegables. |
| Registro de uso de IA | docs/ia.md presente en el árbol del hash 4806374; log de commits muestra actualizaciones (07b36f4, df1e2f7) | Cumple | El archivo existe y tiene historial. |
| README | README.md (hash 4806374) describe qué es, cómo arrancar (scripts/dev.sh, dev.ps1) y cómo probar | Cumple | Cumple con los requisitos de README. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe, pero no hay runs de CI citados para el hash calificado | No verificado | Falta evidencia de ejecución del pipeline. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `b28e0684d4b38267c0a7d48152b0f5558a789b8c 2026-09-07T14:57:28-06:00 Se agrego correcciones.md`
- **Veredicto**: con pendientes
- Resumen: El proyecto está bien documentado en arquitectura y trazabilidad, pero no cumple con el requisito de correcciones.md en el estado calificado y carece de evidencia de CI.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- correcciones.md se añadió en el commit b28e068 (2026-09-07T14:57:28-06:00), posterior al cierre; no se considera en la matriz S5.

Pendientes que siguen abiertos:
- correcciones.md en la raíz del estado calificado.
- Evidencia de ejecución del pipeline CI para el hash calificado.
- Verificación de reproducibilidad del corte vertical.

## Recuento y nota sugerida

6 de 12 criterios Cumple.

## No verificado / pendientes

- Corte vertical reproducible y coherente con la arquitectura
- Pipeline y pruebas respaldan el estado calificado
- PDF u otro adjunto exigido por el aula
- Sustentación del corte
- Pipeline y análisis estático (transversal)

## Hallazgos para la planilla

- correcciones.md no existe en el estado calificado (hash 4806374); se añadió después del cierre en b28e068.
- No hay evidencia de ejecución del pipeline CI para el estado calificado.
- La reproducibilidad del corte vertical no está verificada sin runs de CI.
- El PDF del corte está en el repositorio, pero la entrega en Moodle no es verificable.
- La sustentación del corte queda pendiente de la sesión docente.
- Commits posteriores al cierre (no calificados): b28e068 2026-09-07T14:57:28-06:00 Se agrego correcciones.md
