# semana-04-evidencia-s4 · Recobra

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `df4689b` (2026-08-28T23:39:47-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42.md contiene 'Sección 5 — Requisitos de calidad' y 'Sección 6 — Construcción y despliegue' en lugar de bloques de construcción y vista de ejecución | No cumple | Las secciones 5 y 6 no corresponden al contenido exigido por arc42 |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se encuentra 'Sección 9' en docs/arc42.md | No cumple | Falta la sección 9 |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42.md sección 10 lista S1-S7 coincidiendo con docs/arbol_utilidad.md | Cumple | Coherente con los escenarios priorizados |
| Glosario iniciado con términos del dominio | Existe docs/glosarios.md pero no se pudo inspeccionar su contenido | No verificado | Haría falta ver el archivo para confirmar términos propios del sistema |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/README.md solo contiene diagrama de nivel 1 en mermaid | No cumple | No se encontró diagrama de nivel 2 |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay C4 nivel 2 para contrastar con el código | No cumple | Sin nivel 2 no se puede verificar correspondencia |
| Corte vertical que atraviesa interfaz, lógica y persistencia | El árbol no muestra archivos src/ ni tests/, solo node_modules y docs | No verificado | Haría falta listar src/ y tests/ para citar las tres rutas |
| Arranque documentado con un solo comando | README.md declara requisitos y comando 'npm install && npm start' | Cumple | Comando declarado, aunque incluye instalación |
| Prueba automatizada del recorrido completo, en verde | No se encontró URL de run de CI ni archivo de prueba en el árbol | No verificado | Haría falta ruta de la prueba y URL del run que la ejecutó |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tiene solo columnas Aspecto, Decisión, Justificación, Pruebas | No cumple | Faltan ID, Requisito, C4, ADR, Código y Evidencia |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_Recobra visible y público | Cumple | Cumple con organización y nombre |
| Estructura mínima | Existen docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | arc42 en docs/arc42.md y docs/arc42/04, desviación aceptable; node_modules versionado es hallazgo |
| Estado calificado/versionado | No se observa etiqueta corte-1; commit df4689b sin etiqueta | No cumple | Falta etiqueta de corte |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md con nombre válido y contenido completo | Cumple | ADR aceptado con contexto, alternativas, decisión y consecuencias |
| Tabla de aspectos | docs/aspectos.md tabla con solo 4 columnas | No cumple | Faltan columnas ID, Requisito, C4, ADR, Código, Evidencia |
| Registro de uso de IA | docs/ia.md existe con commit 2026-08-23, pero no se pudo inspeccionar contenido | No verificado | Haría falta ver el archivo para confirmar campos requeridos |
| README | README.md con qué es, requisitos, arranque y pruebas | Cumple | Documenta arranque con un comando |
| Pipeline y análisis estático | No se encontró .github/workflows en el árbol ni runs de CI | No cumple | Sin pipeline configurado |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de docs/glosarios.md no inspeccionado
- Rutas del corte vertical no visibles en árbol
- Prueba automatizada sin evidencia de ejecución en verde
- Contenido de docs/ia.md no inspeccionado

## Hallazgos para la planilla

- node_modules versionado en el repositorio
- Secreto repo_token en node_modules/debug/.coveralls.yml
- Falta autor Fernando Isacc Conde Herrera en historial de commits
- arc42 secciones 5 y 6 mal etiquetadas
- Falta C4 nivel 2
- Tabla de aspectos incompleta
- Sin pipeline de CI
- Sin etiqueta corte-1
