# semana-04-evidencia-s4 · TRACTAR

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `5f923cd` (2026-08-23T22:40:51-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42.md presente; contenido visible solo hasta sección 3 | No verificado | No se pudo comprobar secciones 4-6 por truncamiento de evidencia; haría falta ver encabezados completos |
| arc42 sección 9 al día y enlazada con los ADR existentes | ADR 0001 existe, pero sección 9 no visible en evidencia | No verificado | Falta confirmar que la sección 9 cite docs/adr/0001-*.md |
| arc42 sección 10 coherente con los escenarios de la semana 2 | Se observan QS-01..QS-05 en aspects.md y Quality Goals en arc42.md | No verificado | No se pudo ver la sección 10 completa para confirmar coherencia |
| Glosario iniciado con términos del dominio | No se observa sección 12 en el contenido visible | No verificado | Falta evidencia de glosario con términos propios |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | No existe docs/c4/; solo imagen c4_nivel1_contexto.png en docs/arc42/images/ | No cumple | Falta nivel 2 y coherencia entre niveles |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin C4 nivel 2 no hay contenedores que contrastar | No cumple | Imposible verificar correspondencia |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README indica que no hay modelos ni lógica de negocio (S3 solo fontanería) | No cumple | No existe recorrido vertical; apps vacías |
| Arranque documentado con un solo comando | README declara ./run.sh como comando único | No verificado | No se ejecutó; comando declarado: ./run.sh |
| Prueba automatizada del recorrido completo, en verde | Solo hay 1 prueba de health check según README | No cumple | No hay prueba del corte vertical ni CI en verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | Filas A-01..A-05 con celdas '—' o genéricas (health check) | No cumple | Ninguna fila tiene todas las celdas navegables hasta Pruebas |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Solo un autor en historial: Sebastian Garcia Devoz (13+2+1 commits) | No cumple | Faltan 3 integrantes declarados en el historial |
| Estructura mínima | Falta docs/c4/; existen docs/arc42/, docs/adr/, docs/aspectos.md, docs/ia.md, README.md | No cumple | Directorio docs/c4/ ausente |
| Estado del repositorio que se califica (versionado) | No hay etiqueta corte-1; commit calificado 5f923cd sin tag | No cumple | Se revisó último commit anterior al cierre, pero falta etiqueta |
| Convenciones de ADR | ADR 0001 sin trazabilidad completa (falta commit/PR y pruebas) | No cumple | El ADR no enlaza commit ni pruebas que lo cubran |
| Tabla de aspectos | docs/aspectos.md con filas incompletas (celdas '—' o genéricas) | No cumple | No cumple cadena completa aspecto→evidencia |
| Registro de uso de IA | docs/ia.md sin columna de rechazos explícitos | No cumple | Falta qué se rechazó y por qué |
| README | README tiene descripción y comando, pero no declara requisitos previos explícitos | No cumple | Falta sección de prerequisitos |
| Pipeline y análisis estático | No hay .github/workflows/ ni evidencia de CI/SonarCloud | No cumple | Sin pipeline ni análisis estático |

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 4-6: evidencia truncada, no se pudo confirmar redacción
- arc42 sección 9: no visible en evidencia
- arc42 sección 10: no visible en evidencia
- arc42 sección 12 (glosario): no visible en evidencia
- Arranque con ./run.sh: no se ejecutó

## Hallazgos para la planilla

- No existe directorio docs/c4/ ni diagramas C4 nivel 2
- No hay corte vertical: apps sin modelos ni lógica de negocio
- Solo una prueba de health check, no del recorrido completo
- Sin pipeline de CI ni análisis estático
- Solo un autor en el historial, faltan 3 integrantes
- ADR 0001 sin trazabilidad completa (commit/PR y pruebas)
- Tabla de aspectos con celdas vacías o genéricas
- Registro de IA sin rechazos explícitos
- README sin requisitos previos declarados
- No hay etiqueta corte-1
