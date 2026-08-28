# semana-04-evidencia-s4 · ROUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `1ed002b` (2026-08-23T20:31:54-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md contiene texto de plantilla 'About arc42' y solo se observan secciones 1 y 2 | No cumple | Faltan secciones 3-6 redactadas; hay rastros de plantilla |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se encuentra encabezado de sección 9 en docs/arc42/arc42-template-EN.md | No cumple | Sección 9 ausente |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se encuentra encabezado de sección 10 en docs/arc42/arc42-template-EN.md | No cumple | Sección 10 ausente |
| Glosario iniciado con términos del dominio | No se encuentra sección 12 ni glosario en docs/arc42/arc42-template-EN.md | No cumple | Glosario ausente |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/context.md contiene solo diagrama de contexto (nivel 1); no hay archivo de nivel 2 | No cumple | Falta diagrama de contenedores |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No existe C4 nivel 2 para contrastar con backend/app/modules/* | No cumple | Sin nivel 2 no se puede verificar correspondencia |
| Corte vertical que atraviesa interfaz, lógica y persistencia | backend/app/main.py y módulos solo contienen __init__.py; no hay archivos de lógica ni persistencia | No cumple | No se evidencia recorrido completo |
| Arranque documentado con un solo comando | README.md incluye 'uvicorn app.main:app --reload' como comando de arranque tras requisitos previos | Cumple | Documentación presente; no ejecutado |
| Prueba automatizada del recorrido completo, en verde | Solo existe backend/tests/test_health.py; no hay prueba de recorrido completo ni run de CI | No cumple | Falta prueba end-to-end y evidencia de ejecución |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tiene celdas vacías en ADR, Código y Pruebas en todas las filas | No cumple | Ninguna fila llega completa hasta Pruebas |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_ROUTB en ISCOUTB, público; autores consolidados: 4 integrantes | Cumple | Coincide con equipo declarado |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura correcta |
| Estado del repositorio (versionado) | Commit calificado 1ed002b (2026-08-23T20:31:54-05:00) anterior al cierre 2026-08-31 | Cumple | Sin etiqueta requerida para evidencia semanal |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md sigue numeración y contiene contexto, decisión, consecuencias, trazabilidad | Cumple | ADR aceptado sin evidencia de edición |
| Tabla de aspectos | docs/aspectos.md tiene celdas vacías en columnas ADR, Código, Pruebas | No cumple | Filas con huecos no defendibles |
| Registro de uso de IA | docs/ia.md registra semanas 1-3 con aceptado/rechazado y justificación | Cumple | Cumple requisito de rechazo con motivo |
| README | README.md describe sistema, instalación, arranque con uvicorn y pruebas con pytest | Cumple | Requisitos previos declarados |
| Pipeline y análisis estático | No existe .github/workflows/ en el árbol; sin datos de Actions | No cumple | Falta CI y SonarCloud |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes


## Hallazgos para la planilla

- arc42 incompleto: solo secciones 1 y 2 redactadas
- C4 nivel 2 ausente
- Corte vertical no implementado
- Tabla de aspectos con huecos
- Sin pipeline CI
