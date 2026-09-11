# semana-05-corte1 · LaPlacita

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `50b92f8` en `origin/master` (2026-09-06T17:45:05-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master 50b92f8 (2026-09-06T17:45:05-05:00) < cierre 2026-09-10T17:00:00Z | Cumple | Rama principal master, hash y fecha verificados. |
| correcciones.md existe en la raíz del estado calificado | Árbol de 50b92f8 contiene 'correciones.md', no 'correcciones.md' | No cumple | Nombre mal escrito; la ficha lo declara no conforme. |
| Correcciones trazables y contrastadas | No se dispone del contenido de 'correciones.md' en la evidencia | No verificado | Falta el archivo para contrastar cada hallazgo S1-S4. |
| S1 al día: equipo, problema y repositorio | README.md (50b92f8) lista equipo, problema y repo; docs/ficha_del_problema.md | Cumple | Integrantes coinciden con autores del historial. |
| S2 al día: escenarios de calidad y restricciones | docs/aspectos.md (aspectos/escenarios); arc42 §2 RES-01 a RES-04 | Cumple | Escenarios y restricciones documentados. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-0004; arc42 §4 estrategia | Cumple | Decisiones con contexto, alternativas y trazabilidad. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-EN.md; docs/c4/contexto.md y contenedores.md; src/corte-vertical.js | Cumple | Documentación y corte vertical presentes. |
| Corte vertical reproducible y coherente con la arquitectura | README (arranque/pruebas); src/corte-vertical.js; tests/corte-vertical.test.js; run CI 34064927441 success | Cumple | Flujo completo con tiendaId y pruebas en verde. |
| Pipeline y pruebas respaldan el estado calificado | Run CI 34064927441 (2026-09-06T22:45:12Z) success; .github/workflows/ci.yml ejecuta npm test | Cumple | El run corresponde al hash calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md enlaza aspecto→requisito→C4→ADR→código→pruebas→evidencia | Cumple | Cadena navegable en el estado calificado. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio | No verificado | Se entrega en Moodle; no verificable aquí. |
| Sustentación del corte | Depende de sesión de sustentación | No verificado | Lo resuelve el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_LaPlacita en ISCOUTB, público; autores: Jorge M. Castillo, samulssl, Isaza927, matbuendia | Cumple | Integrantes declarados presentes en historial. |
| Estructura mínima | Árbol 50b92f8 incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | Rutas mínimas presentes. |
| Estado del repositorio que se califica | origin/master 50b92f8 anterior al cierre | Cumple | Hash y fecha registrados. |
| Convenciones de ADR | docs/adr/0001-0004 con nombres kebab-case y secciones contexto/decisión/consecuencias/trazabilidad | Cumple | Cumplen la plantilla. |
| Tabla de aspectos | docs/aspectos.md con columnas ID, Aspecto, Requisito, Escenarios, C4, ADR, Código, Pruebas, Evidencia | Cumple | Incluye columna extra 'Escenarios'; enlaces navegables. |
| Registro de uso de IA | docs/ia.md existe pero sin columna de 'rechazado' con motivo técnico | No cumple | El contrato exige documentar lo rechazado y por qué. |
| README | README.md describe qué es, cómo ejecutar y cómo probar | Cumple | Incluye comandos y requisitos. |
| Pipeline y análisis estático | ci.yml ejecuta npm test (run success 34064927441); SonarCloud inactivo por falta de SONAR_TOKEN | No cumple | El análisis estático no está activo. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `50b92f8558f2f57d01aeee14dfe202c9e076e74f 2026-09-06T17:45:05-05:00 fix(ci): gata el análisis SonarCloud con env en vez de secrets`
- **Veredicto**: al dia
- Resumen: Proyecto al día en el corte; 8/12 criterios cumplidos, 1 no cumple (correcciones.md), 3 no verificados.

Pendientes que siguen abiertos:
- Renombrar correciones.md a correcciones.md.
- Completar docs/ia.md con columna de rechazado.
- Configurar SONAR_TOKEN para activar SonarCloud.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (8/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correcciones trazables y contrastadas: falta el contenido de correciones.md.
- PDF u otro adjunto: no disponible en el repositorio.
- Sustentación del corte: depende de sesión docente.

## Hallazgos para la planilla

- 'correciones.md' mal escrito; debe ser 'correcciones.md'.
- docs/ia.md no documenta lo rechazado con motivo técnico.
- SonarCloud no configurado (falta SONAR_TOKEN); análisis estático no activo.
- Contenido de correciones.md no disponible para contrastar trazabilidad.
- PDF y sustentación no verificables desde el repositorio.
- El apartado 11 del contrato no fue proporcionado; la matriz transversal se evaluó con el contrato visible.
