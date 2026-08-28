# semana-04-evidencia-s4 · AudioShare

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `024ae34` (2026-08-23T23:47:38-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/src/ solo contiene 01,02,03,04; faltan 05 y 06 | No cumple | Secciones 5 y 6 ausentes |
| arc42 sección 9 al día y enlazada con los ADR existentes | No existe docs/arc42/src/09_architecture_decisions.adoc | No cumple | Falta sección 9 |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No existe docs/arc42/src/10_quality_requirements.adoc | No cumple | Falta sección 10 |
| Glosario iniciado con términos del dominio | No existe docs/arc42/src/12_glossary.adoc | No cumple | Falta glosario |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo docs/c4/context.mmd y context.png (nivel 1) | No cumple | Falta diagrama de nivel 2 |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay C4 nivel 2 para contrastar | No cumple | Sin nivel 2 no se puede verificar correspondencia |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README indica 'aún sin lógica de negocio'; arbol sin archivos de persistencia | No cumple | Solo esqueleto, sin recorrido vertical |
| Arranque documentado con un solo comando | README.md: 'npm run dev' con requisitos Node.js 20+ | Cumple | Comando de arranque declarado; no ejecutado |
| Prueba automatizada del recorrido completo, en verde | Solo tests/health.test.ts; sin .github/workflows | No cumple | Prueba no cubre recorrido completo y no hay CI |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md no tiene tabla con columnas C4, ADR, Código, Pruebas | No cumple | Formato narrativo, no trazable |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_AudioShare público; autores: Elian, Santiago, Yeiver, cardonavincent26-design | No verificado | No se puede confirmar que cardonavincent26-design sea Vincent Cardona Castro; falta consolidar identidad |
| Estructura mínima | Arbol contiene docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura mínima presente |
| Estado del repositorio calificado | Commit 024ae34 fecha 2026-08-23T23:47:38-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin commits tardíos |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md con trazabilidad 'Implementación: Pendiente' y 'Pruebas: Pendiente' | No cumple | ADR incompleto: faltan commit/PR y pruebas |
| Tabla de aspectos | docs/aspectos.md sin tabla de 8 columnas | No cumple | No cumple formato de trazabilidad |
| Registro de uso de IA | docs/ia.md sin columna de rechazo ni motivos | No cumple | Falta registrar qué se rechazó y por qué |
| README | README.md con qué es, arranque, pruebas y requisitos | Cumple | Documentación de arranque completa |
| Pipeline y análisis estático | No existe .github/workflows/ ni evidencia de CI/SonarCloud | No cumple | Sin pipeline ni análisis estático |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Identidad de cardonavincent26-design no confirmada como Vincent Cardona Castro

## Hallazgos para la planilla

- Faltan secciones arc42 5,6,9,10,12
- Solo C4 nivel 1, sin nivel 2
- Corte vertical inexistente: esqueleto sin lógica ni persistencia
- Prueba solo health, sin recorrido completo ni CI
- aspectos.md sin tabla de trazabilidad
- ADR con trazabilidad incompleta
- ia.md sin rechazos
- Sin pipeline
