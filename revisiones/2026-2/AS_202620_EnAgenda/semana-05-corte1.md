# semana-05-corte1 · EnAgenda

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `696882e` en `origin/master` (2026-09-07T16:21:16-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | Rama origin/master, hash 696882e, fecha 2026-09-07T16:21:16-05:00, anterior al cierre 2026-09-10T17:00:00Z. | Cumple | El estado calificado es identificable y cumple la condición temporal. |
| correcciones.md existe en la raíz del estado calificado | docs/correcciones.md presente en el árbol del hash 696882e. | Cumple | El archivo está en la raíz y dentro del estado calificado. |
| Correcciones trazables y contrastadas | docs/correcciones.md responde a hallazgos de S4 (C4 y aspectos) con enlaces a rutas y commits; se contrastó con el árbol y el historial. | Cumple | Las correcciones declaradas se verifican en el estado calificado. |
| S1 al día: equipo, problema y repositorio | README.md y docs/ficha-problema.md describen problema, usuarios y alcance; integrantes en historial (Daoisttl0FB3, Jein-12, eliabarnedocondef10-gif). | Cumple | El repositorio es público y pertenece a la organización ISCOUTB. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10-requisitos-de-calidad.md incluye árbol de utilidad y EC-01 a EC-05; docs/arc42/02- restricciones.md define R-01 a R-06. | Cumple | Escenarios y restricciones están documentados y coherentes. |
| S3 al día: estrategia de solución y decisiones | docs/arquitectura/matriz-comparativa-estilos.md y ADR-0001 (docs/adr/0001-usar-monolito-modular.md) documentan la decisión de monolito modular. | Cumple | La estrategia está respaldada por ADR y matriz comparativa. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ contiene secciones 1-12; docs/c4/ tiene niveles 1-3; corte vertical implementado en src/invitaciones/ y app/web.py con pruebas en tests/test_invitaciones.py. | Cumple | La documentación y el código están alineados con la implementación. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta arranque con 'python app\web.py' y pruebas con 'pytest -q'; evidencia en docs/evidencia.md muestra 6 passed y ejecución local. | Cumple | El flujo descrito coincide con la arquitectura de monolito modular. |
| Pipeline y pruebas respaldan el estado calificado | Run CI success del 2026-09-07T21:21:18Z (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/34162828625) asociado al hash 696882e. | Cumple | El pipeline ejecuta pytest y pasa en el estado calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md enlaza A-01 con C4, ADR, código, pruebas y evidencia; todos los enlaces apuntan a rutas existentes en el árbol. | Cumple | La fila de aspectos está completa y navegable. |
| PDF u otro adjunto exigido por el aula | No se dispone del documento entregado en Moodle; solo se evalúa el repositorio. | No verificado | Requiere verificación en el aula. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio. | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_EnAgenda en ISCOUTB, público; integrantes en historial (Daoisttl0FB3, Jein-12, eliabarnedocondef10-gif). | Cumple | Cumple con organización, nombre y visibilidad. |
| Estructura mínima | Existen docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md en el árbol. | Cumple | Se observan archivos __pycache__ versionados, pero no afectan la estructura mínima. |
| Estado del repositorio calificado | Se usó origin/master, hash 696882e, anterior al cierre; sin commits posteriores. | Cumple | El estado calificado es el correcto. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md sigue la convención de nombre y contiene contexto, alternativas, decisión y trazabilidad. | Cumple | No se detectaron ADR reescritos. |
| Tabla de aspectos | docs/aspectos.md tiene una fila con las 8 columnas y enlaces navegables a C4, ADR, código, pruebas y evidencia. | Cumple | La fila está completa y navegable. |
| Registro de uso de IA | docs/ia.md registra usos con herramienta, propósito, aceptado, rechazado y verificación; creció en 3 commits. | Cumple | El registro es detallado y muestra criterio. |
| README | README.md incluye qué es, cómo arrancar con un comando y cómo probar. | Cumple | El comando de arranque es 'python app\web.py'. |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta pytest en cada push; runs CI success en GitHub Actions. | Cumple | No se evidencia análisis estático con SonarCloud, pero el contrato no lo exige explícitamente en este corte. |
| Secretos | No se encontraron secretos en el árbol ni .env versionado; el grep solo detectó la palabra 'token' en contexto de código. | Cumple | No hay incidentes de secretos. |
| Autoría y colaboración | Historial con 65 commits de Daoisttl0FB3, 55 de Jein-12 y 12 de eliabarnedocondef10-gif; actividad distribuida en el tiempo. | Cumple | Los tres integrantes contribuyen. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `696882ecb889c01bdc93170556c90044acf4fcff 2026-09-07T16:21:16-05:00 Update aspectos.md`
- **Veredicto**: al dia
- Resumen: El proyecto está al día con los requisitos de S1 a S4 y el corte vertical funciona. No hay pendientes de semanas anteriores sin resolver.

## Recuento y nota sugerida

10 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.3 = 1 + 4 × (10/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula
- Sustentación del corte

## Hallazgos para la planilla

- Se versionan archivos __pycache__ en el repositorio, lo que ensucia el árbol.
- El nombre de archivo 'docs/arc42/02- restricciones.md' tiene un espacio inusual, pero no afecta la estructura.
- El C4 nivel 3 está vacío, aunque no se exige contenido en este corte.
- No se evidencia análisis estático con SonarCloud en el pipeline.
- El PDF de Moodle no está disponible para verificación.
