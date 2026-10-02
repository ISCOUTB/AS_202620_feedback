# semana-05-corte1 · TRACTAR

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `7cfb872` en `origin/main` (2026-08-31T12:27:23-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/main, hash 7cfb872, fecha 2026-08-31T12:27:23-05:00, anterior al cierre 2026-09-10T17:00:00Z | Cumple | El estado calificado es identificable y cumple la condición temporal. |
| correcciones.md existe en la raíz del estado calificado | El árbol del hash 7cfb872 no incluye el archivo correcciones.md | No cumple | Falta el archivo obligatorio en la raíz del estado calificado. |
| Correcciones trazables y contrastadas | No existe correcciones.md, por lo que no hay trazabilidad de correcciones | No cumple | Sin el archivo índice, no se puede verificar la respuesta a hallazgos previos. |
| S1 al día: equipo, problema y repositorio | docs/ficha_problema.md (hash 7cfb872) define problema, afectados y propuesta; repo AS_202620_TRACTAR en ISCOUTB | Cumple | El problema y el equipo están documentados; el repositorio es visible y con nombre correcto. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42.md (hash 7cfb872) incluye objetivos de calidad y restricciones técnicas, organizacionales y legales | Cumple | Los escenarios de calidad y restricciones están documentados en arc42. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-estilo-arquitectonico.md y 0002-cambio-stack-fastapi-flutter.md (hash 7cfb872) documentan decisiones con contexto y alternativas | Cumple | Los ADR están presentes y siguen la convención de nomenclatura. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42.md, docs/c4/C2.md y c4_nivel1.md (hash 7cfb872); README documenta corte vertical con pruebas | Cumple | La documentación arc42 y C4 está presente; el corte vertical está implementado y probado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md (hash 7cfb872) describe arranque con ./run.sh y pruebas; tests/test_loans.py y test_resources.py cubren la regla de negocio | Cumple | El corte vertical es reproducible y coherente con la arquitectura documentada. |
| Pipeline y pruebas respaldan el estado calificado | Run CI 'UTB Tracker CI' success 2026-08-31T17:27:34Z (https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/33419672964) asociado al hash | Cumple | El run exitoso respalda el estado calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md (hash 7cfb872) tabla con columnas aspecto, requisito, C4, ADR, código, pruebas y evidencia; enlaces a archivos | Cumple | La tabla de aspectos es navegable y enlaza los artefactos. |
| PDF u otro adjunto exigido por el aula | No hay evidencia del PDF en el repositorio; se entrega en Moodle | No verificado | No se puede verificar desde el repositorio; requiere revisión en Moodle. |
| Sustentación del corte | No hay evidencia de sesión de sustentación | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_TRACTAR en ISCOUTB, público, visible; integrantes en historial (autores: Sebastian Garcia Devoz, Sebas) | Cumple | Nombre y organización correctos; visibilidad pública. |
| Estructura mínima | Árbol del hash 7cfb872 incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | Estructura mínima presente. |
| Estado del repositorio calificado | Hash 7cfb872 en origin/main, fecha 2026-08-31T12:27:23-05:00, anterior al cierre | Cumple | Estado calificado correcto. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y 0002-cambio-stack-fastapi-flutter.md (hash 7cfb872) con nombres válidos y contenido con contexto, decisión, alternativas y consecuencias | Cumple | Los ADR cumplen la convención de nomenclatura y estructura. |
| Tabla de aspectos | docs/aspectos.md (hash 7cfb872) tabla con 8 columnas y enlaces a requisitos, C4, ADR, código y pruebas | Cumple | La tabla es navegable y completa para A-06. |
| Registro de uso de IA | docs/ia.md (hash 7cfb872) con 2 usos registrados, incluyendo qué se usó y qué se descartó | Cumple | El registro existe y documenta usos con criterio. |
| README | README.md (hash 7cfb872) describe qué es, cómo arrancar con ./run.sh y cómo probar | Cumple | El README es claro y reproducible. |
| Pipeline y análisis estático | .github/workflows/ci.yml (hash 7cfb872) ejecuta pytest en push; run success 2026-08-31T17:27:34Z | Cumple | Pipeline configurado y ejecutado con éxito. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849 2026-08-31T12:27:23-05:00 Fix: solved the text problem`
- **Veredicto**: con pendientes
- Resumen: El proyecto está al día en contenido técnico (S1-S4), pero falta el archivo correcciones.md obligatorio para S5.

Pendientes que siguen abiertos:
- Crear correcciones.md en la raíz del repositorio.
- Verificar la entrega del PDF en Moodle.
- Preparar la sustentación del corte.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (8/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula
- Sustentación del corte

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado.
- No hay trazabilidad de correcciones a hallazgos previos.
- El PDF de Moodle no es verificable desde el repositorio.
- La sustentación no se puede verificar desde el repositorio.
