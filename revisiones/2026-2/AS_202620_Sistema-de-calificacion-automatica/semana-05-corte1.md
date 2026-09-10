# semana-05-corte1 · Calificación automática

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `201acac` en `origin/master` (2026-09-06T23:34:17-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | hash 201acac, 2026-09-06T23:34:17-05:00, rama origin/master | Cumple | Anterior al cierre 2026-09-07T05:00:00Z |
| correcciones.md existe en la raíz del estado calificado | Árbol de 201acac incluye correcciones_feedback.md; no incluye correcciones.md | No cumple | El nombre exigido es exactamente correcciones.md; el renombrado en 8b0d00b es posterior al cierre |
| Correcciones trazables y contrastadas | No se dispone del contenido de correcciones_feedback.md en la evidencia | No verificado | Haría falta git show 201acac:correcciones_feedback.md para contrastar cada hallazgo S1-S4 |
| S1 al día: equipo, problema y repositorio | README.md, docs/ficha-problema.md, shortlog con 4 cuentas | Cumple | La correspondencia de cuentas con integrantes no se pudo atribuir, pero hay 4 identidades git |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42-template-ES.md secciones 1.2, 2 y 10; docs/aspectos.md | Cumple | EC-01 a EC-07 y RNF-01 a RNF-15 documentados |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-usar-monolito-modular.md a 0006-registrar-la-recepcion-en-una-bitacora-antes-de-encolar.md | Cumple | Decisiones de monolito modular, asíncrono, stack, alcance LLM y bitácora |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-ES.md, docs/c4/doc-c4.md, backend/tests/test_recepcion.py, README.md sección corte vertical | Cumple | A-01 construido de punta a punta; C4 niveles 1 y 2 |
| Corte vertical reproducible y coherente con la arquitectura | README.md 'Cómo se arranca' y 'Cómo recorrerlo'; docker-compose.yml; backend/ingesta/recepcion.py; frontend/lib/pantalla_carga.dart | Cumple | El recorrido A-01 atraviesa API, almacén, cola y worker; 47 pruebas backend y 6 frontend |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml existe; sin runs_ci en la evidencia | No verificado | Haría falta consultar la API de actions runs para el hash 201acac |
| Trazabilidad consolidada navegable | docs/aspectos.md tabla con columnas ID, Aspecto, Requisito, Escenario, C4, ADR, Código, Pruebas, Evidencia | Cumple | Cada celda enlaza a archivos del repositorio |
| PDF u otro adjunto exigido por el aula | No disponible en la evidencia del repositorio | No verificado | Lo resuelve el aula en Moodle |
| Sustentación del corte | No hay sesión de sustentación en la evidencia | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible:true; repo AS_202620_Sistema-de-calificacion-automatica | No verificado | Falta confirmar la organización ISCOUTB; haría falta la URL completa del repositorio |
| Estructura mínima | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md en árbol de 201acac | Cumple | Estructura mínima completa |
| Convenciones de ADR | docs/adr/0001-0006 numerados y en kebab-case | Cumple | 0001 marcado reemplazado por 0002; cada ADR tiene contexto, alternativas, decisión, consecuencias y trazabilidad |
| Registro de uso de IA | docs/ia.md presente; ia_log con 7 commits entre 2026-08-07 y 2026-09-06 | Cumple | El registro crece a lo largo del semestre |
| README | README.md con descripción, arranque con docker compose up y pruebas | Cumple | Incluye cómo se arranca y cómo se prueba |
| Pipeline y análisis estático | .github/workflows/ci.yml presente; sin runs_ci | No verificado | Falta evidencia de ejecución en CI para el hash calificado |
| Secretos | secretos: sin coincidencias; envs_versionados: [] | Cumple | Sin credenciales ni .env versionados |
| Autoría y colaboración | shortlog: 4 cuentas, 61 commits (35+16+7+3) | Cumple | Actividad repartida; no se atribuyeron cuentas a personas por parecido de nombre |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8b0d00b62d2a03dfe509edae578261748a842294 2026-09-07T14:29:28-05:00 Rename correcciones_feedback.md to correcciones.md`
- **Veredicto**: con pendientes
- Resumen: Proyecto con corte vertical A-01 completo y arquitectura documentada; la entrega del corte incumplió el nombre exacto de correcciones.md, corregido después del cierre. Quedan pendientes de verificación: CI, PDF y sustentación.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Renombrado de correcciones_feedback.md a correcciones.md en 8b0d00b (2026-09-07T14:29:28-05:00), posterior al cierre

Pendientes que siguen abiertos:
- Verificar contenido de correcciones.md a HEAD
- Confirmar run de CI para el hash calificado
- PDF en Moodle
- Sustentación
- Confirmar organización ISCOUTB

## Recuento y nota sugerida

7 de 12 criterios Cumple.

## No verificado / pendientes

- Correcciones trazables y contrastadas
- Pipeline y pruebas respaldan el estado calificado
- PDF u otro adjunto exigido por el aula
- Sustentación del corte
- Identidad del repositorio
- Pipeline y análisis estático

## Hallazgos para la planilla

- correcciones.md ausente en 201acac; solo correcciones_feedback.md
- Renombrado a correcciones.md en 8b0d00b, posterior al cierre
- Sin run de CI en la evidencia para el hash calificado
- Contenido de correcciones_feedback.md no contrastable con la evidencia dada
- Organización ISCOUTB no confirmada explícitamente
- PDF y sustentación pendientes de verificación por el aula
- Commits posteriores al cierre (no calificados): 8b0d00b 2026-09-07T14:29:28-05:00 Rename correcciones_feedback.md to correcciones.md
