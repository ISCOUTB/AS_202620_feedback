# semana-05-corte1 · Clubs UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `4ede977` en `origin/master` (2026-09-06T22:41:55-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash 4ede977, fecha 2026-09-06T22:41:55-05:00 (anterior al cierre 2026-09-10T17:00:00Z) | Cumple | El estado calificado es el último commit de master antes del cierre. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree del hash 4ede977 no incluye correcciones.md; árbol del estado calificado no lo lista | No cumple | No existe el archivo en la raíz del estado calificado. |
| Correcciones trazables y contrastadas | No hay correcciones.md que responda a hallazgos S1-S4; no se puede contrastar | No cumple | Sin índice de correcciones, no hay trazabilidad. |
| S1 al día: equipo, problema y repositorio | README.md sección 5 lista 4 integrantes; docs/ficha_problema.md describe problema; repo en ISCOUTB con nombre correcto | Cumple | Equipo y problema documentados; repositorio visible y correcto. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10_requisitos_de_calidad.md incluye árbol de utilidades y escenarios U1-U3, C1-C3; docs/arc42/02_restricciones.md lista T1-T4, O1-O3, C1-C2 | Cumple | Escenarios y restricciones completos y coherentes. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04_estrategia_de_solucion.md y docs/adr/0001-hexagonal.md documentan decisión hexagonal con alternativas y consecuencias | Cumple | Estrategia y ADR presentes y trazables. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ secciones 1-6,9,10,12; docs/c4/contexto.md con diagramas C4 nivel 1 y 2; backend con endpoints /health y /publicaciones y pruebas | Cumple | Documentación arc42 y C4 completas; corte vertical implementado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md sección 7 da comandos de arranque y pruebas; backend/src/linkclub/main.py y routers implementan puertos/adaptadores; tests en backend/tests/ | Cumple | El corte vertical es reproducible y sigue la arquitectura hexagonal. |
| Pipeline y pruebas respaldan el estado calificado | runs_ci: Backend tests success en 2026-09-06T23:58:26Z y 2026-09-07T03:42:14Z (posteriores al hash pero antes del cierre); workflow .github/workflows/backend-tests.yml | Cumple | CI ejecuta pruebas y pasa en runs asociados al estado. |
| Trazabilidad consolidada navegable | docs/aspectos.md tabla con enlaces a escenarios, ADR, código y pruebas; ADR 0001 enlaza a aspectos y secciones arc42 | Cumple | La tabla de aspectos es navegable y enlaza los elementos. |
| PDF u otro adjunto exigido por el aula | No hay evidencia del PDF en el repositorio; depende de Moodle | No verificado | No se puede verificar desde el repositorio; requiere acceso al aula. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_Clubs_UTB en organización ISCOUTB, público; integrantes en README y en historial (autores: Zavod Dev, Josh Ortega, Luis-Salas-Reyes, deortahollman-star) | Cumple | Nombre y organización correctos; visibilidad pública. |
| Estructura mínima | Árbol incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | Estructura cumple con la mínima requerida. |
| Estado del repositorio calificado | Rama master con hash 4ede977 anterior al cierre; sin commits posteriores al cierre | Cumple | Estado calificado correcto. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md sigue convención de nombre y formato; no se observan reescrituras (solo un commit de creación) | Cumple | ADR bien formado y no modificado. |
| Tabla de aspectos | docs/aspectos.md tiene 8 columnas (ID, Aspecto, Escenario, Requisito, C4, ADR, Código, Pruebas) y filas U1-U3, C1-C3 con enlaces | Cumple | Tabla completa y navegable. |
| Registro de uso de IA | docs/ia.md con tabla de usos, herramientas, qué se aceptó y motivo; historial muestra 7 commits de ia.md | Cumple | Registro presente y con evolución. |
| README | README.md incluye descripción, stack, estructura, equipo, cómo arrancar y cómo probar | Cumple | Cumple con requisitos de README. |
| Pipeline y análisis estático | Workflow .github/workflows/backend-tests.yml ejecuta pruebas en push/PR; runs_ci muestran success; no hay SonarCloud configurado | Cumple | CI presente y exitoso; análisis estático no configurado (no exigido en este corte). |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `4ede977c7cccc335d878019ce06cba2e23cf76d2 2026-09-06T22:41:55-05:00 quite el C2 y lo reemplaze con el C3`
- **Veredicto**: con pendientes
- Resumen: El proyecto está al día en S1-S4 y corte vertical, pero falta correcciones.md, requisito de S5.

Pendientes que siguen abiertos:
- Crear correcciones.md en la raíz del estado calificado

## Recuento y nota sugerida

8 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (8/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula
- Sustentación del corte

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado.
- No hay índice de correcciones que responda a hallazgos S1-S4.
- PDF de Moodle no verificado desde el repositorio.
- Sustentación pendiente de sesión docente.
