# semana-05-corte1 · PideUtb

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `bbefae8` en `origin/master` (2026-09-08T10:37:21-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash bbefae8, fecha 2026-09-08T10:37:21-05:00 (anterior al cierre 2026-09-10T17:00:00Z) | Cumple | El commit calificado es el último de master antes del cierre. |
| correcciones.md existe en la raíz del estado calificado | Árbol del hash bbefae8: no aparece 'correcciones.md'; aparece 'CORRECCIONES.md' y 'docs/correcciones.md' | No cumple | El nombre exacto exigido no está en la raíz; hay variantes con mayúsculas y en docs/. |
| Correcciones trazables y contrastadas | docs/correcciones.md responde a hallazgos S1-S4 con enlaces y evidencia; p.ej. run CI #10 y rutas de código | Cumple | Aunque el archivo no está en la raíz con el nombre exacto, su contenido es trazable y contrastable. |
| S1 al día: equipo, problema y repositorio | ficha_problema.md presente con tensiones T-1 y T-2; repo público en ISCOUTB/AS_202620_PideUtb | Cumple | Equipo declarado coincide con integrantes en historial. |
| S2 al día: escenarios de calidad y restricciones | docs/aspectos.md con tabla de 8 columnas y escenarios ESC-01 a ESC-05; arc42 sección 2 con restricciones | Cumple | Escenarios y restricciones documentados y enlazados. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-estilo-arquitectonico.md con contexto, alternativas, decisión y trazabilidad; docs/comparativa-arquitectura.md | Cumple | ADR 0001 aceptado y con trazabilidad completa. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42.md con secciones 1-12; docs/c4/ con niveles 1-3 en Mermaid; backend con corte vertical POST /pedidos y pruebas | Cumple | C4 y arc42 coherentes con el código. |
| Corte vertical reproducible y coherente con la arquitectura | README documenta arranque y pruebas; backend/tests/test_pedidos.py cubre flujo; código en backend/app/pedidos y menu | Cumple | Flujo cruza módulos vía service público, coherente con ADR-0001. |
| Pipeline y pruebas respaldan el estado calificado | runs_ci: run 34245943551 success 2026-09-08T15:37:27Z (posterior al hash pero mismo estado); workflow .github/workflows/ci.yml | Cumple | CI en verde para el estado calificado y posteriores. |
| Trazabilidad consolidada navegable | docs/aspectos.md enlaza escenario, C4, ADR, código y pruebas; README índice de documentación | Cumple | Cadena completa para ESC-01; otras filas pendientes marcadas. |
| PDF u otro adjunto exigido por el aula | No disponible en repositorio; se entrega en Moodle | No verificado | Requiere acceso al aula para verificar. |
| Sustentación del corte | Sesión de sustentación no registrada en repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo público ISCOUTB/AS_202620_PideUtb; integrantes en historial (daniarriet, Santiago Cuesta, ruddy2000utb-droid) | Cumple | Nombre y organización correctos. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura cumple; correcciones.md no en raíz (ver ficha). |
| Estado del repositorio calificado | Hash bbefae8 en origin/master anterior al cierre; sin commits posteriores | Cumple | Estado calificado correcto. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md con nombre válido y contenido completo; sin reescrituras | Cumple | Un ADR aceptado, no editado. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas y filas por escenario; enlaces navegables | Cumple | Cadena completa para ESC-01; pendientes marcados. |
| Registro de uso de IA | docs/ia.md con usos por entrega y tabla de rechazos con motivos | Cumple | Incluye S5 y rechazos justificados. |
| README | README.md con descripción, comando único de arranque y cómo probar | Cumple | Reproducible. |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta pytest en 3.11 y 3.12; runs_ci success; SonarCloud no configurado | Cumple | CI en verde; SonarCloud no evidenciado (pendiente para segundo corte). |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `bbefae828185e9baa4df757ea073cbe84539cd3f 2026-09-08T10:37:21-05:00 Actualizar las referencias restantes al run de CI`
- **Veredicto**: con pendientes
- Resumen: El proyecto en HEAD (bbefae8) está al día en S1-S4 y en la mayoría de S5, pero quedan pendientes de S5: restricción no transcrita, ADR 0002 no creado, cambio no implementado, y el archivo correcciones.md no está en la raíz con el nombre exacto.

Pendientes que siguen abiertos:
- Transcribir la restricción asignada en docs/restriccion-s5.md
- Crear ADR 0002 del reto
- Implementar el cambio que responde a la restricción y contrastarlo con el umbral
- Renombrar/mover el archivo de correcciones a correcciones.md en la raíz
- Equilibrar la contribución entre integrantes

## Recuento y nota sugerida

9 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.0 = 1 + 4 × (9/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula: requiere acceso a Moodle.
- Sustentación del corte: requiere sesión docente.

## Hallazgos para la planilla

- El archivo correcciones.md no existe en la raíz del estado calificado; hay CORRECCIONES.md y docs/correcciones.md.
- La restricción asignada de S5 no está transcrita en docs/restriccion-s5.md (sección 1 pendiente).
- El ADR del reto (0002) no está creado; depende de la restricción.
- La implementación del cambio para la restricción S5 no está hecha (secciones 5-6 pendientes).
- La contribución está desbalanceada: daniarriet 23, Santiago Cuesta 21+2, ruddy2000utb-droid 2 commits.
- No hay evidencia de SonarCloud en el pipeline.
- El PDF de la entrega no está en el repositorio (se entrega en Moodle).
