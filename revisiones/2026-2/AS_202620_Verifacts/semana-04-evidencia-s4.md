# semana-04-evidencia-s4 · Verifacts

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Evaluacion manual complementaria
> del pipeline (Verifacts no fue procesado por la pasada automatica).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `443e908` (2026-08-29T18:17:18-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | agente de revision (kit arqsw) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/01..06 con contenido propio de VeriFacts; 05 descompone API/Content/Analysis/Scoring con responsabilidades y trazabilidad al codigo; 06 describe el escenario GET /health con diagrama de secuencia | Cumple | Sin restos de plantilla en el barrido; 03/04 redactadas y referenciadas por el resto |
| arc42 seccion 9 al dia y enlazada con los ADR existentes | docs/arc42/09-decisiones-arquitectonicas.md con tabla que enlaza ADR-0001 (docs/adr/0001-estilo-arquitectonico.md) | Cumple | Tambien anticipa ADR pendientes (persistencia, contrato Analyzer, ML) |
| arc42 seccion 10 coherente con los escenarios de la semana 2 | docs/arc42/10-requisitos-de-calidad.md resume Q-01..Q-05 y enlaza arbol-utilidad.md, escenarios-de-calidad.md y la matriz de estilos | Cumple | Coherente con la seccion 4 y el ADR; Q-05 con evidencia de prueba, Q-01..Q-04 pendientes de logica |
| Glosario iniciado con terminos del dominio | docs/arc42/11-glosario.md con terminos propios (Analysis, Analyzer, Scoring, indicador, regla, corte vertical, P95) | Cumple | Desviacion menor: archivo numerado 11 en lugar de la seccion 12 |
| C4 nivel 1 y nivel 2 presentes y coherentes entre si | docs/c4/01-contexto.md y docs/c4/02-contenedores.md en Mermaid; actores (usuario, sitio web externo) consistentes entre niveles; flechas etiquetadas | Cumple | Sin leyenda formal en el diagrama; como codigo, favorable para trazabilidad del corte |
| Limites del C4 nivel 2 correspondientes a la estructura del codigo | Contenedor API (FastAPI) corresponde a app/ y app/modules/{content,analysis,scoring}; BD (SQLite) e interfaz web (React) dibujados como «previsto, no implementado» | Cumple | FE y DB no tienen codigo todavia, pero el diagrama lo declara explicitamente |
| Corte vertical que atraviesa interfaz, logica y persistencia | GET /health solo atraviesa el bloque API (app/api/routes.py); la propia seccion 6 declara que no pasa por Content/Analysis/Scoring y que no hay persistencia | No cumple | El recorrido completo llego tarde: «Implement test for analysis vertical slice» (7f14952) y «Agrega data, persistence» (c6d62a6) son posteriores al cierre |
| Arranque documentado con un solo comando | README seccion 9/13: `python run.py` con requisitos previos (Python 3.11+, venv, pip install -r requirements.txt) | Cumple | No ejecutado (regla del kit); CI sin runs verificables (ver fila de prueba) |
| Prueba automatizada del recorrido completo, en verde | tests/test_health.py cubre solo GET /health; .github/workflows/tests.yml existe, pero la API no reporta runs y la URL citada en docs/aspectos.md (run 33235835069) devuelve 404 | No cumple | Al cierre no existe recorrido completo que probar; el test del health carece de run verificable |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tiene 9 columnas propias (Atributo, Preocupacion, Medida, Impacto, Riesgo) en lugar de las 8 del curso; la fila A-00 no tiene celdas C4, ADR ni codigo | No cumple | La cadena aspecto→requisito→C4→ADR→codigo→pruebas no es navegable; la celda Pruebas apunta a una URL inexistente |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_Verifacts publico, accesible sin autenticacion | Cumple | — |
| Estructura minima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes | Cumple | Glosario como 11-glosario.md; __pycache__/ y .pyc versionados (hallazgo) |
| Estado calificado identificable | Commit 443e908 (2026-08-29T18:17:18-05:00) anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta; evidencia semanal |
| Nombres de ADR segun la convencion | docs/adr/0001-estilo-arquitectonico.md | Cumple | — |
| ADR aceptados no reescritos | Historial del ADR: creacion (bc2b318) y renombrado (d932855), sin reescrituras; estado ahora «Aceptado» | Cumple | Corregido respecto a S3 («Propuesto») |
| docs/ia.md al dia para la semana | Registro con herramienta, uso, aceptado/rechazado y motivo; commit 8ad4574 dentro del periodo S4 | Cumple | Incluye lo rechazado con justificacion tecnica |
| Sin credenciales en el repositorio ni en el historial | git grep sin coincidencias; sin .env versionado | Cumple | — |
| Contribucion de todos los integrantes | En 443e908: PedroC1213 (110 consolidados con dos identidades) y Cristian Cardeño (12); el tercer integrante declarado no aparece | No cumple | Mismo pendiente que S1-S3 |

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## Estado global del proyecto (overall · revisado en HEAD)

- HEAD revisado: `d4723aa` (2026-08-31T11:24:47-05:00) — posterior al cierre
- Veredicto: **con pendientes**
- Commits posteriores al cierre (no calificados): corte vertical completo con persistencia (`c6d62a6` «Agrega data, persistence», `7f14952` test del vertical slice, `4aa91b9` health check, `d395997` service.py) y limpieza de `.gitignore` (`aaacc3d`)

Resuelto tarde (corregido despues del cierre, ahora al dia en HEAD):

- El corte vertical completo (interfaz→logica→persistencia) con su prueba quedo implementado el lunes despues del cierre: no cuenta para S4, pero deja el proyecto avanzado para el corte 1.
- `.gitignore` corregido (`aaacc3d`), aunque los `.pyc`/`__pycache__` ya versionados siguen en el historial.

Pendientes que siguen abiertos:

- Tercer integrante sin commits en el historial (arrastrado desde S1).
- `__pycache__/`, `*.pyc` y archivos duplicados `« (1).py»` versionados en el estado calificado.
- PDFs en la raiz del repositorio (`resumen-entrega.pdf`, `VeriFacts-resumen-entrega-final c1.pdf`).
- Tabla de aspectos con columnas fuera de la convencion del curso (falta la cadena C4/ADR/codigo).
- CI sin runs verificables: la URL citada en aspectos.md da 404 y la API no reporta runs.
- README declara «sin __pycache__ ni archivos duplicados», que no era cierto en el estado calificado.

## No verificado / pendientes

- Prueba del health en verde: sin run de CI citable (URL 404; API sin runs); haria falta el enlace al run o ejecutarla en la sustentacion.
- Arranque `python run.py`: no ejecutado (regla del kit); confirmar en la sustentacion.

## Hallazgos para la planilla

- Entrega S4 valida y bien documentada al cierre, pero el corte vertical completo llego tarde (lunes 31-ago 10:00-11:24 COT, posterior al cierre).
- La prueba automatizada solo cubre GET /health al cierre y no hay run de CI verificable.
- Tabla de aspectos fuera del formato de 8 columnas del curso.
- Basura versionada (`__pycache__`, `.pyc`, duplicados «(1).py», PDFs).
- Tercer integrante sigue sin commits.
