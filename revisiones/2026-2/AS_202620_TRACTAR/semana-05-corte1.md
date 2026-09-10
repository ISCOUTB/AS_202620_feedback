# semana-05-corte1 · TRACTAR

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `7cfb872` en `origin/main` (2026-08-31T12:27:23-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/main, hash 7cfb872, fecha 2026-08-31T12:27:23-05:00 (anterior al cierre 2026-09-07T05:00:00Z) | Cumple | El estado calificado es el último commit de main antes del cierre. |
| correcciones.md existe en la raíz del estado calificado | Árbol del hash 7cfb872 no incluye correcciones.md (ver lista de archivos) | No cumple | No existe el archivo en la raíz del estado calificado. |
| Correcciones trazables y contrastadas | No hay correcciones.md que responda a hallazgos S1-S4 | No cumple | Sin índice de correcciones no se puede contrastar ninguna. |
| S1 al día: equipo, problema y repositorio | docs/ficha_problema.md con problema, afectados y propuesta; README.md describe el sistema; integrantes en historial (13+7+1 commits) | Cumple | El repositorio es público en ISCOUTB, nombre correcto AS_202620_TRACTAR. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42.md secciones de restricciones y objetivos de calidad; docs/aspectos.md con QS-01 a QS-06 | Cumple | Escenarios y restricciones documentados con justificación. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-estilo-arquitectonico.md y 0002-cambio-stack-fastapi-flutter.md; docs/matriz_estilos.md | Cumple | ADR con contexto, alternativas y consecuencias; decisión de monolito modular. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42.md completo; docs/c4/C2.md y c4_nivel1.md; código en app/routers/loans.py y resources.py; pruebas en tests/test_loans.py y test_resources.py | Cumple | Corte vertical de préstamo con regla de disponibilidad implementado y probado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md con comando ./run.sh y pasos de prueba; código en app/routers/loans.py y models.py; C4 en docs/c4/C2.md | Cumple | La regla de negocio central está implementada y documentada. |
| Pipeline y pruebas respaldan el estado calificado | Run CI success 2026-08-31T17:27:34Z (https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/33419672964) asociado al hash 7cfb872 | Cumple | El run success es posterior al commit calificado, pero el pipeline corre en cada push y el estado calificado tiene pruebas en verde. |
| Trazabilidad consolidada navegable | docs/aspectos.md tabla con enlaces a requisitos, ADR, código y pruebas; pero faltan enlaces a C4 y evidencia en varias filas | No cumple | La tabla de aspectos tiene huecos en columnas C4, código, pruebas y evidencia para A-01 a A-05. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; depende de Moodle | No verificado | No se puede verificar desde el repositorio. |
| Sustentación del corte | No hay evidencia de sesión de sustentación | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_TRACTAR en ISCOUTB, público, integrantes en historial (Sebastian Garcia Devoz, Sebas, Sebastian Garcia Devoz) | Cumple | Nombre y organización correctos; visibilidad pública. |
| Estructura mínima | README.md, docs/arc42/arc42.md, docs/adr/0001-*.md y 0002-*.md, docs/c4/C2.md y c4_nivel1.md, docs/aspectos.md, docs/ia.md | Cumple | Estructura cumple con la mínima; hay archivos adicionales permitidos. |
| Estado del repositorio calificado | Último commit de main 7cfb872 anterior al cierre; sin commits posteriores | Cumple | Se usó la rama principal main. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y 0002-cambio-stack-fastapi-flutter.md con nombres en kebab-case y contenido completo | Cumple | Dos ADR aceptados, no editados después de creación. |
| Tabla de aspectos | docs/aspectos.md tabla con filas A-01 a A-06; varias celdas con '—' en C4, ADR, código, pruebas y evidencia | No cumple | Huecos en la cadena de trazabilidad para la mayoría de aspectos. |
| Registro de uso de IA | docs/ia.md con dos entradas (2026-08-16) indicando herramienta, uso y descarte | Cumple | Registro presente y con columna de descarte. |
| README | README.md con comando ./run.sh, instrucciones de prueba y estructura | Cumple | Arranque con un solo comando y pruebas documentadas. |
| Pipeline y análisis estático | .github/workflows/ci.yml con pytest; run success 2026-08-31T17:27:34Z | Cumple | CI en GitHub Actions; no se evidencia SonarCloud en el repositorio. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849 2026-08-31T12:27:23-05:00 Fix: solved the text problem`
- **Veredicto**: con pendientes
- Resumen: El proyecto está al día en S1-S4 con corte vertical funcional, pero falta correcciones.md y la trazabilidad de aspectos está incompleta.

Pendientes que siguen abiertos:
- Crear correcciones.md en la raíz
- Completar tabla de aspectos con enlaces
- Subir PDF al aula
- Sustentar el corte

## Recuento y nota sugerida

7 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula
- Sustentación del corte

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado.
- La tabla de aspectos tiene huecos en la trazabilidad para A-01 a A-05.
- No hay evidencia de PDF adjunto en el repositorio.
- No hay evidencia de sustentación en el repositorio.
- El pipeline no incluye análisis estático (SonarCloud).
