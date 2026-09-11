# semana-05-corte1 · Calificación automática

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `8b0d00b` en `origin/master` (2026-09-07T14:29:28-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | git log -1 --until=2026-09-10T17:00:00Z origin/master → 8b0d00b 2026-09-07T14:29:28-05:00 | Cumple | Hash 8b0d00b en master, anterior al cierre. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree --name-only 8b0d00b incluye correcciones.md; commit 8b0d00b 'Rename correcciones_feedback.md to correcciones.md' | Cumple | Archivo presente en la raíz del hash calificado. |
| Correcciones trazables y contrastadas | No se incluyó el contenido de correcciones.md en la evidencia | No verificado | Se requiere git show 8b0d00b:correcciones.md para contrastar cada hallazgo S1-S4. |
| S1 al día: equipo, problema y repositorio | docs/ficha-problema.md, README.md, shortlog con 4 cuentas | Cumple | Equipo, problema y repositorio presentes y coherentes. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42-template-ES.md secciones 1.2, 2 y 10 con EC-01 a EC-07 y RNF-01 a RNF-15 | Cumple | Escenarios y restricciones documentados y referenciados desde aspectos.md. |
| S3 al día: estrategia de solución y decisiones | docs/adr/ con 6 ADR (0001-0006), arc42 secciones 4-6 | Cumple | Decisiones registradas con contexto, alternativas y consecuencias. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-ES.md, docs/c4/doc-c4.md (niveles 1 y 2), backend/ingesta, frontend/lib | Cumple | Arc42, C4 y corte vertical A-01 construido. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta docker compose up y recorrido A-01; backend/tests (47 pruebas) y frontend/test (6 pruebas) | Cumple | Recorrido documentado y código coherente con C4. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml existe pero no se citó run de CI | No verificado | Falta URL de run asociado al hash 8b0d00b; comando: curl a actions/runs. |
| Trazabilidad consolidada navegable | docs/aspectos.md tabla con enlaces a requisitos, C4, ADR, código, pruebas y evidencia | Cumple | Fila A-01 navegable de punta a punta. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; adjunto de Moodle | No verificado | Depende del aula; no verificable desde el repo. |
| Sustentación del corte | Sesión de sustentación | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_Sistema-de-calificacion-automatica, público, 4 cuentas en shortlog | Cumple | Nombre, organización y visibilidad correctos. |
| Estructura mínima | Árbol incluye docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura conforme al contrato. |
| Convenciones de ADR | 6 ADR con nombres NNNN-kebab-case; 0001 marcado reemplazado por 0002 | Cumple | Nombres y ciclo de vida correctos. |
| Tabla de aspectos | docs/aspectos.md con 5 filas y columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia | Cumple | A-01 trazable; demás declarados. |
| Registro de uso de IA | docs/ia.md existe con 7 commits de historial, pero no se incluyó su contenido | No verificado | Falta contrastar columnas de aceptado/rechazado con motivo. |
| Pipeline y análisis estático | .github/workflows/ci.yml presente; sin run de CI citado | No verificado | Se requiere URL de run para verificar ejecución. |
| Secretos | git grep sin coincidencias; sin .env versionado | Cumple | Sin credenciales en el repositorio. |
| Autoría y colaboración | shortlog: scp1109 (36), josueacademico17-source (16), SusanaRosales (7), Mariadelmar-restrepo (3) | Cumple | Cuatro cuentas contribuyen, coincidiendo con los cuatro integrantes declarados; distribución desigual. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8b0d00b62d2a03dfe509edae578261748a842294 2026-09-07T14:29:28-05:00 Rename correcciones_feedback.md to correcciones.md`
- **Veredicto**: al dia
- Resumen: Proyecto completo al cierre del corte 1: arc42, C4, 6 ADR, corte vertical A-01 construido y medido, 4 cuentas contribuyendo. Sin commits posteriores al cierre. Pendientes de verificación: contenido de correcciones.md, run de CI y detalle de docs/ia.md.

Pendientes que siguen abiertos:
- Verificar contenido de correcciones.md
- Adjuntar run de CI del hash calificado
- Confirmar docs/ia.md con rechazos documentados

## Recuento y nota sugerida

8 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (8/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de correcciones.md (fila 3 de la ficha).
- Run de CI asociado al hash calificado (fila 9 de la ficha).
- PDF adjunto en Moodle (fila 11 de la ficha).
- Sustentación del corte (fila 12 de la ficha).
- Contenido de docs/ia.md (fila 5 de la transversal).

## Hallazgos para la planilla

- correcciones.md presente pero su contenido no fue contrastable en la evidencia.
- No hay run de CI citado para el hash calificado 8b0d00b.
- docs/ia.md existe pero no se verificaron las columnas de aceptado/rechazado.
- Distribución de commits desigual: una cuenta con 3 commits frente a 36 de la mayor.
- Sin commits posteriores al cierre; entrega a tiempo.
