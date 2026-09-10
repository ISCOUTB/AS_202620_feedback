# semana-05-corte1 · ROUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `493efdb` en `origin/master` (2026-09-06T20:11:13-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master en 493efdb (2026-09-06T20:11:13-05:00), anterior al cierre 2026-09-07T05:00:00Z | Cumple | Rama principal declarada por el remoto: origin/master. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree 493efdb no lista correcciones.md en la raíz | No cumple | El archivo exigido por la ficha no existe en el estado calificado. |
| Correcciones trazables y contrastadas | No hay correcciones.md en 493efdb que enlace hallazgos S1-S4 con evidencia | No cumple | Sin índice de correcciones no es posible contrastar respuestas a hallazgos previos. |
| S1 al día: equipo, problema y repositorio | README.md lista a Diego Baron, Junior Orozco, Keiner Mendivil y Julian Manjarrez; docs/problema.md presente; repo ISCOUTB/AS_202620_ROUTB público | Cumple | Equipo declarado coincide con integrantes; problema documentado en docs/problema.md. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10_requisitos_de_calidad.md incluye árbol de utilidad y escenarios; docs/arc42/02_restricciones_de_arquitectura.md documenta restricciones | Cumple | Atributos priorizados y escenarios con medidas verificables presentes. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04_estrategia_de_solucion.md y ADR 0001, 0002 y 0003 en docs/adr/ | Cumple | Estrategia y decisiones documentadas con alternativas y consecuencias. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ secciones 01-12 presentes; docs/c4/context.md con niveles 1 y 2; backend y frontend con flujo de autenticación y reserva de cupos | Cumple | Documentación arc42 completa y C4 como código; corte vertical implementado en backend/tests y frontend/lib. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta arranque con uvicorn y flutter run; backend/tests/test_registro.py y test_cupos.py cubren registro y reserva; módulos backend/app/modules/trips y auth coherentes con C4 | Cumple | El flujo de registro y reserva de cupos corresponde con la arquitectura documentada. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml presente; README cita run de GitHub Actions #33992259222 con conclusión Success | Cumple | El run citado respalda el estado calificado; no se verificó ejecución local de pytest. |
| Trazabilidad consolidada navegable | docs/aspectos.md con 3 filas que enlazan aspecto, requisito, C4, ADR, código, pruebas y evidencia | Cumple | Cada fila tiene enlaces navegables a los artefactos citados. |
| PDF u otro adjunto exigido por el aula | No hay adjunto en el repositorio; la entrega se hace en Moodle | No verificado | Se requiere revisar el aula para confirmar el PDF; el repositorio no lo contiene. |
| Sustentación del corte | No hay sesión de sustentación registrada en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_ROUTB visible; integrantes en historial: MKeinerrr, diegobrr999-commits, juliandmanjarrez-tech, junior14700 | Cumple | Nombre y organización cumplen; identidades consolidadas por nombre visible. |
| Estructura mínima | README.md, docs/arc42/ (01-12), docs/adr/ (0001-0003), docs/c4/context.md, docs/aspectos.md y docs/ia.md presentes en 493efdb | Cumple | Estructura mínima completa en la raíz y docs/. |
| Estado del repositorio que se califica | Hash 493efdb (2026-09-06T20:11:13-05:00) anterior al cierre; commits posteriores 6f6e40c, 5c89522 y 343bb9d registrados en overall | Cumple | Se usó origin/master; no se mezclaron ramas. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md, 0002-usar-arquitectura-interna-por-capas.md y 0003-control-atomico-de-cupos.md con nombres en kebab-case y trazabilidad | Cumple | Nombres cumplen el patrón NNNN-titulo-en-kebab-case.md; no se detectaron ADR reescritos. |
| Tabla de aspectos | docs/aspectos.md con 3 filas y columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia | Cumple | Cada celda enlaza a un artefacto real del repositorio. |
| Registro de uso de IA | docs/ia.md con registro por semana, herramienta, contexto, aceptado y rechazado; historial con 6 commits entre 2026-08-07 y 2026-09-06 | Cumple | El registro crece a lo largo del semestre y documenta lo rechazado con justificación. |
| README | README.md describe el sistema, instalación, arranque con uvicorn y flutter run, y pruebas con pytest | Cumple | Arranque y pruebas documentados con comandos únicos por componente. |
| Pipeline y análisis estático | .github/workflows/ci.yml presente; run #33992259222 con conclusión Success citado en README | Cumple | CI ejecuta pruebas en cada push; no se verificó SonarCloud en el repositorio. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `343bb9d6565c1a81bdad542efde3fbb56b07e2ca 2026-09-09T21:10:40-05:00 Delete`
- **Veredicto**: con pendientes
- Resumen: El proyecto completo a HEAD mantiene la documentación arc42, ADR, C4, aspectos e IA, y el pipeline CI con éxito. Sin embargo, la ausencia de correcciones.md en el estado calificado impide declarar el compendio S5 como cumplido.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 6f6e40c (2026-09-07T13:23:46-05:00) 'Evaluación de retroalimentación de IA' actualiza docs/ia.md después del cierre.
- 5c89522 (2026-09-09T21:10:11-05:00) 'S6' y 343bb9d (2026-09-09T21:10:40-05:00) 'Delete' son posteriores al cierre y no forman parte del estado calificado.

Pendientes que siguen abiertos:
- correcciones.md no existe en la raíz del estado calificado ni en HEAD.
- No hay evidencia de que hallazgos S1-S4 hayan sido respondidos formalmente.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula: requiere revisar Moodle.
- Sustentación del corte: requiere sesión con el docente.
- Ejecución local de pytest: no se ejecutó código; se apoya en run de CI #33992259222.

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado 493efdb.
- No hay índice de correcciones que responda a hallazgos S1-S4.
- Commits posteriores al cierre (6f6e40c, 5c89522, 343bb9d) no afectan la matriz pero se registran en overall.
- docs/ia.md no documenta usos de IA posteriores al 2026-09-06 en el estado calificado.
- No se encontraron secretos reales; las coincidencias de 'password' son campos de esquema y variables de código.
- Commits posteriores al cierre (no calificados): 343bb9d 2026-09-09T21:10:40-05:00 Delete; 5c89522 2026-09-09T21:10:11-05:00 S6; 6f6e40c 2026-09-07T13:23:46-05:00 Evaluación de retroalimentación de IA
