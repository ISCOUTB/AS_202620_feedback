# semana-05-corte1 · LaPlacita

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `50b92f8` en `origin/master` (2026-09-06T17:45:05-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master 50b92f8 2026-09-06T17:45:05-05:00 | Cumple | Anterior al cierre 2026-09-07T05:00:00Z. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree 50b92f8 muestra 'correciones.md' | No cumple | Nombre mal escrito; debe ser exactamente correcciones.md. |
| Correcciones trazables y contrastadas | No existe correcciones.md en 50b92f8 | No verificado | No se pudo contrastar; falta el archivo índice requerido. |
| S1 al día: equipo, problema y repositorio | README.md, docs/ficha_del_problema.md, shortlog 4 identidades | Cumple | Equipo y problema documentados; repositorio público en ISCOUTB. |
| S2 al día: escenarios de calidad y restricciones | docs/aspectos.md, arc42 §2 | Cumple | ESC-01..05 y RES-01..04 presentes. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001..0004, arc42 §4 | Cumple | Decisiones registradas con contexto y trazabilidad. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-EN.md, docs/c4/contexto.md, contenedores.md, src/corte-vertical.js | Cumple | Artefactos presentes en el estado calificado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md 'Cómo ejecutar', package.json test, tests/corte-vertical.test.js, run 34064927441 | Cumple | Flujo completo con tiendaId y pruebas en verde. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml, run CI LaPlacita 34064927441 success | Cumple | CI en verde para el hash calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md columna Evidencia | No cumple | Celdas de Evidencia son texto sin enlace (p.ej. 'npm test 13/13 en verde'). |
| PDF u otro adjunto exigido por el aula | Sin adjunto en el repositorio | No verificado | Se entrega en Moodle; no verificable desde el repo. |
| Sustentación del corte | Sin sesión registrada | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | Árbol 50b92f8: docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura requerida presente. |
| Convenciones de ADR | docs/adr/0001..0004 en kebab-case | Cumple | ADR-0001 no reescrito; cada uno con contexto, decisión, consecuencias y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md columna Evidencia | No cumple | La columna Evidencia no es navegable; rompe la cadena aspecto→evidencia. |
| Registro de uso de IA | docs/ia.md | No cumple | No documenta 'qué se rechazó y por qué'; solo Validación genérica. |
| README | README.md | Cumple | Describe qué es, arranque y pruebas. |
| Pipeline y análisis estático | .github/workflows/ci.yml, README 'Configuración SonarCloud pendiente' | No cumple | SonarCloud no activo por falta de SONAR_TOKEN/projectKey. |
| Secretos | git grep sin coincidencias; sin .env versionado | Cumple | Sin secretos en el estado calificado. |
| Autoría y colaboración | shortlog: Jorge M. Castillo, samulssl, Isaza927, matbuendia | Cumple | 4 contribuyentes consolidados; actividad repartida. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `50b92f8558f2f57d01aeee14dfe202c9e076e74f 2026-09-06T17:45:05-05:00 fix(ci): gata el análisis SonarCloud con env en vez de secrets`
- **Veredicto**: con pendientes
- Resumen: Base arquitectónica sólida con RES-05 implementado y CI en verde; persisten pendientes formales: correcciones.md mal nombrado, trazabilidad incompleta, IA sin rechazos y SonarCloud inactivo.

Pendientes que siguen abiertos:
- correcciones.md con nombre incorrecto
- docs/ia.md sin sección de rechazos
- docs/aspectos.md con Evidencia no navegable
- SonarCloud sin token/projectKey
- PDF adjunto no verificado

## Recuento y nota sugerida

7 de 12 criterios Cumple.

## No verificado / pendientes

- Correcciones trazables y contrastadas (sin contenido de correcciones.md)
- PDF u otro adjunto exigido por el aula (se entrega en Moodle)
- Sustentación del corte (sesión del docente)

## Hallazgos para la planilla

- correcciones.md está mal escrito como correciones.md en 50b92f8
- docs/ia.md no documenta rechazos de IA con motivo
- docs/aspectos.md tiene columna Evidencia sin enlaces navegables
- SonarCloud no está activo: falta SONAR_TOKEN y projectKey
- No hay PDF adjunto verificable en el repositorio
