# semana-04-evidencia-s4 · AudioShare

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `24a5023` (2026-08-30T23:48:29-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/src/01..06_*.adoc en 24a5023, redactados y sin marcadores de plantilla visibles | Cumple | Secciones 1-6 presentes con contenido propio del proyecto. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/src/09_section_desing_decisions.adoc (24a5023) redacta ADR-001..003 sin enlazar docs/adr/; solo existe docs/adr/0001-usar-monolito-modular.md | No cumple | La sección 9 repite decisiones y crea ADR-002/003 sin archivo en docs/adr/. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/src/10_quality_requirements.adoc (24a5023) incluye EC-01..EC-04 con métricas 100ms/200ms/3s, coherente con docs/escenarios_calidad.md | Cumple | Escenarios y métricas alineados con el árbol de utilidad. |
| Glosario iniciado con términos del dominio | docs/arc42/src/12_glossary.adoc (24a5023) define Sala, Emisor, Receptor, Sincronización, A-01, EC-01..04 | Cumple | Términos propios del sistema, no solo genéricos de arquitectura. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/Context - Nivel 1.mmd y docs/c4/Contenedor - Nivel 2.mmd (24a5023); actores Emisor/Receptor coherentes, flechas etiquetadas y leyenda | Cumple | Los actores del nivel 1 reaparecen en el nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/Contenedor - Nivel 2.mmd dibuja Frontend, Discovery, Signaling y Media Engine; src/ solo tiene modules/session, audio, sync y server.ts (24a5023) | No cumple | Contenedores dibujados sin código correspondiente; no hay frontend ni discovery. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Interfaz en src/app.ts, lógica en src/modules/sync/index.ts; sin ruta de persistencia en el árbol (24a5023) | No cumple | Falta el tramo de persistencia: no hay BD, archivo ni almacenamiento. |
| Arranque documentado con un solo comando | README.md (24a5023) declara Node.js 20+ y comandos npm install + npm run dev; no ejecutado | No verificado | Comando declarado: npm run dev tras npm install; no se ejecutó en contenedor. |
| Prueba automatizada del recorrido completo, en verde | tests/a01.test.ts existe (24a5023); runs_ci vacío, sin run en verde | No verificado | Falta evidencia de ejecución del pipeline; comando anotado: npm test. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md (24a5023) tabla A-01 sin columnas Requisito ni C4; celda Pruebas cita health.test.ts y 'pendientes', no tests/a01.test.ts | No cumple | Huecos en la fila: faltan Requisito/C4 y la prueba real del corte vertical. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_AudioShare en ISCOUTB, público; shortlog 24a5023 muestra 4 autores (Elian, Yeiver, Santiago, cardonavincent26) | Cumple | Integrantes declarados presentes en el historial. |
| Estructura mínima | docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md y README.md presentes en 24a5023 | Cumple | Estructura base del contrato cumplida. |
| Versionado (estado calificado) | Commit 24a5023 2026-08-30T23:48:29-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiquetas, pero para evidencia semanal el commit vigente es válido. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md existe y cumple el nombre; pero 09 crea ADR-002/003 sin archivo y ADR-0001 dice 'propuesto'/'pendiente' | No cumple | Decisiones sin archivo en docs/adr/ y ADR-0001 desactualizado frente al corte vertical. |
| Tabla de aspectos | docs/aspectos.md (24a5023) tabla A-01 sin columnas Requisito ni C4; celda Pruebas con pendientes | No cumple | La cadena aspecto->requisito->C4->ADR->código->pruebas no está completa. |
| Registro de uso de IA | docs/ia.md (24a5023) con tabla de usos, herramientas, verificación y propuestas rechazadas con motivo; log con 8 commits | Cumple | Registro creciente y con columna de rechazos. |
| README | README.md (24a5023) documenta npm install + npm run dev, no un único comando de arranque | No cumple | El contrato pide arranque con un solo comando. |
| Pipeline y análisis estático | Sin .github/workflows en el árbol (24a5023); runs_ci vacío | No cumple | No hay integración continua configurada ni runs que evidencien pruebas en verde. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `24a502338e4ebd33eb28e5650d2f5c2b445c2043 2026-08-30T23:48:29-05:00 Update traceability matrix and summary`
- **Veredicto**: con pendientes
- Resumen: Entrega con arc42 1-6, 10 y glosario redactados, y C4 niveles 1-2 presentes; pero el corte vertical carece de persistencia, la sección 9 no enlaza ADR reales, el C4 nivel 2 no corresponde al código y no hay evidencia de CI.

Pendientes que siguen abiertos:
- Persistencia del corte vertical
- Sección 9 enlazada a ADR reales
- C4 nivel 2 coherente con el código
- Fila de aspectos con columnas Requisito y C4 y prueba citada
- README con un solo comando de arranque
- Pipeline con run en verde

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Arranque: no ejecutado; comando declarado npm run dev tras npm install.
- Prueba en verde: sin runs_ci; comando anotado npm test.

## Hallazgos para la planilla

- La sección 9 de arc42 redacta ADR-002 y ADR-003 sin archivos en docs/adr/.
- El C4 nivel 2 dibuja frontend, discovery, signaling y media engine que no existen en src/.
- El corte vertical no incluye persistencia; solo estado en memoria.
- docs/aspectos.md no tiene columnas Requisito ni C4 y la celda Pruebas cita pendientes.
- README documenta arranque con npm install + npm run dev, no un solo comando.
- No hay runs_ci ni workflows; la prueba a01.test.ts no tiene evidencia de ejecución en CI.
- ADR-0001 sigue en estado 'propuesto' con implementación pendiente pese al corte vertical.
