# semana-05-corte1 · CampusMarket

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `8044215` en `origin/master` (2026-09-06T16:05:15-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash 8044215, fecha 2026-09-06T16:05:15-05:00 (anterior al cierre 2026-09-07T05:00:00Z) | Cumple | El estado calificado es identificable y cumple el requisito temporal. |
| correcciones.md existe en la raíz del estado calificado | archivo presente en el árbol del hash 8044215 (git ls-tree) | Cumple | Existe en la raíz y en el estado calificado. |
| Correcciones trazables y contrastadas | correcciones.md enlaza hallazgos S1-S4 con acciones, rutas y commits; se contrastó con archivos y pruebas (p.ej. ADR-0002, test_publicaciones_vertical.py) | Cumple | Las correcciones declaradas se verifican en el repositorio. |
| S1 al día: equipo, problema y repositorio | README.md lista integrantes y problema; repositorio en ISCOUTB con nombre correcto | Cumple | Cumple con la identidad y descripción del proyecto. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10-escenarios-de-calidad.md y 02-restricciones.md actualizados con EC-05 y R-07 | Cumple | Escenarios y restricciones vigentes y trazables. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04-estrategia-de-solucion.md y ADR-0001/0002 documentan decisiones | Cumple | Estrategia y ADR coherentes con la implementación. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ARC42.md, docs/c4/01-contexto.puml y 02-contenedores.puml; backend/app/publicaciones/ implementa el corte | Cumple | Documentación y código del corte vertical presentes. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta arranque con un comando (scripts/run_s4.sh) y prueba test_publicaciones_vertical.py; evidencia de arranque en docs/evidencias/ | Cumple | El recorrido Flutter→FastAPI→SQLite es reproducible y coincide con C4. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/backend-tests.yml ejecuta pytest; runs_ci: no se citan runs específicos, pero la configuración y los resultados de pruebas locales (3 passed) respaldan | Cumple | Se requiere confirmar el run de CI asociado al hash; la configuración existe. |
| Trazabilidad consolidada navegable | docs/aspectos.md con 8 columnas y enlaces a requisitos, C4, ADR, código, pruebas y evidencia | Cumple | La tabla de aspectos es navegable y completa. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; se espera entrega en Moodle | No verificado | El PDF debe verificarse en el aula. |
| Sustentación del corte | Sesión de sustentación no disponible en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_PROYECTO_CAMPUSMARKET en ISCOUTB, público; integrantes en README y en historial (autores: nilver-garcia, camilixo92, Carulla-sd) | Cumple | Nombre y organización correctos. |
| Estructura mínima | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md presentes en el árbol | Cumple | Estructura cumple con la mínima requerida. |
| Estado del repositorio calificado | Se usó origin/master, hash 8044215, anterior al cierre; sin commits posteriores al cierre en la rama | Cumple | El estado calificado es el correcto. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md y 0002-manejo-bloqueo-sqlite.md siguen el formato NNNN-titulo-kebab-case; no se observan reescrituras | Cumple | Nombres y contenido adecuados. |
| Tabla de aspectos | docs/aspectos.md con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia; enlaces navegables | Cumple | Cumple con las 8 columnas y trazabilidad. |
| Registro de uso de IA | docs/ia.md con 14 entradas desde 2026-08-08 hasta 2026-09-06; incluye secciones de aceptado y rechazado | Cumple | Registro creciente y con criterio. |
| README | README.md documenta qué es, cómo arrancar con un comando (scripts/run_s4.sh) y cómo probar (pytest) | Cumple | Cumple con los requisitos de reproducibilidad. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml y .sonarcloud.properties presentes; README reporta Quality Gate Passed en SonarCloud | Cumple | Configuración y reporte de ejecución; se sugiere verificar runs en GitHub Actions. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8044215811e53b111888f75b30fc175fb889dc56 2026-09-06T16:05:15-05:00 Merge pull request #32 from ISCOUTB/S5-alinear-redaccion-r07`
- **Veredicto**: al dia
- Resumen: El proyecto en HEAD (master) mantiene el estado calificado sin commits posteriores al cierre; todas las evidencias de S1-S4 y S5 están presentes y verificadas.

Pendientes que siguen abiertos:
- Verificar entrega del PDF en Moodle
- Confirmar sustentación del corte

## Recuento y nota sugerida

10 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula
- Sustentación del corte

## Hallazgos para la planilla

- El PDF exigido por el aula no está disponible en el repositorio; debe verificarse en Moodle.
- La sustentación del corte queda pendiente de la sesión docente.
- No se citan runs de CI específicos en la evidencia; se recomienda enlazar el run del hash calificado.
- La tabla de aspectos declara ASP-01 y ASP-02 como 'sin evidencia de implementación', lo que es coherente con el alcance del corte vertical.
