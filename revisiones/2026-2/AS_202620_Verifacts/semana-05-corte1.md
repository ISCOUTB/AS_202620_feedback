# semana-05-corte1 · Verifacts

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `3120e06` en `origin/master` (2026-09-06T18:36:46-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master 3120e06 2026-09-06T18:36:46-05:00, anterior al cierre 2026-09-07T05:00:00Z | Cumple | Rama principal master identificada; no se usaron etiquetas. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree 3120e06 incluye correcciones.md; git show 3120e06:correcciones.md contiene el registro | Cumple | Archivo presente en la raíz del hash calificado. |
| Correcciones trazables y contrastadas | correcciones.md marca Pendiente árbol de utilidad, leyenda C4 y tensiones, pero docs/arbol-utilidad.md y docs/c4/01-contexto.md ya los tienen; marca Pendiente corte vertical pero 3120e06 incluye POST /analysis y tests/test_analysis.py | No cumple | El índice no refleja el estado real; varios hallazgos siguen abiertos. |
| S1 al día: equipo, problema y repositorio | git shortlog -sne 3120e06: autores PedroC1213 y Cristian Cardeño; Julian Samuel Cabeza Pena sin commits; README lista solo dos integrantes | No cumple | El tercer integrante declarado no aparece en el historial. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios-de-calidad.md con Q-01 a Q-05 en 6 partes; docs/arc42/02-restricciones.md; docs/arbol-utilidad.md con impacto/riesgo | Cumple | Escenarios y restricciones presentes y numerados. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04-estrategia-de-solucion.md con tácticas por escenario; docs/adr/0001-estilo-arquitectonico.md; docs/matriz-estilos.md | Cumple | Estrategia, ADR y matriz comparativa disponibles. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/11-glosario.md es el glosario pero falta sección 11 (riesgos); docs/c4/03-componentes.md contiene plantilla sin completar ('Completa esta tabla', 'ej.') | No cumple | arc42 incompleto y C4 nivel 3 es un esqueleto, no documentación. |
| Corte vertical reproducible y coherente con la arquitectura | README documenta python run.py y POST /analysis; tests/test_health.py y tests/test_analysis.py existen en 3120e06; sin run de CI anterior al cierre | No verificado | No se ejecutó; comando anotado: python -m pytest -q y python run.py. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/tests.yml existe en 3120e06; runs_ci disponibles son posteriores y en failure (p.ej. Tests and SonarCloud 34407270858) | No verificado | No hay run asociado al hash calificado; no se puede confirmar que las pruebas pasaran al cierre. |
| Trazabilidad consolidada navegable | docs/aspectos.md fila A-02 'Pendiente'; README enlaza docs/decisiones-arquitectonicas.md inexistente en 3120e06; docs/c4/03-componentes.md sin completar | No cumple | La cadena aspecto→evidencia tiene huecos y enlaces rotos. |
| PDF u otro adjunto exigido por el aula | No hay acceso a Moodle; en el repo existe VeriFacts-resumen-entrega-final c1.pdf en la raíz de 3120e06 | No verificado | La entrega en aula no es verificable desde el repositorio. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | 3120e06 contiene README.md, docs/arc42/ (01-11), docs/adr/0001, docs/c4/01-03, docs/aspectos.md, docs/ia.md | Cumple | Rutas mínimas presentes; persisten artefactos no deseados (__pycache__, archivos con sufijos, PDF) que se registran en S4. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md con nombre válido, contexto, alternativas, decisión, consecuencias y trazabilidad a Q-01..Q-05 | Cumple | Un solo ADR; no se observó reescritura posterior. |
| Tabla de aspectos | docs/aspectos.md tiene 8 columnas pero A-02 'Pendiente' y A-00 cita URL de CI no respaldada por runs_ci | No cumple | Fila con hueco en evidencia; no toda la cadena es navegable. |
| Registro de uso de IA | docs/ia.md con 4 registros (aceptado/rechazado/pendiente) y motivos; log de commits 8ad4574, 5eed315, d42dd18 | Cumple | Incluye lo rechazado y por qué, como exige el contrato. |
| README | README.md describe el sistema, requisitos, python run.py como arranque único y cómo probar | Cumple | Contiene enlace roto a docs/decisiones-arquitectonicas.md, pero el núcleo de arranque/prueba está. |
| Pipeline y análisis estático | 3120e06 solo tiene .github/workflows/tests.yml sin SonarCloud; runs_ci posteriores fallan (34407270858) | No cumple | No hay análisis estático configurado en el estado calificado ni run en verde. |
| Secretos | git grep sin coincidencias de credenciales; sin .env versionados en 3120e06 | Cumple | No se hallaron secretos en el hash calificado. |
| Autoría y colaboración | git shortlog -sne 3120e06: PedroC1213 (150) y Cristian Cardeño (12); Julian Samuel Cabeza Pena sin commits | No cumple | No todos los integrantes declarados aparecen en el historial. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `67f8cea03e6a7b827aced6b60d3af8cf4307b237 2026-09-09T16:30:01-05:00 feat: integrate backend URL analysis contract and align frontend`
- **Veredicto**: con pendientes
- Resumen: El corte calificado 3120e06 tiene avances reales (corte vertical POST /analysis, escenarios, ADR, aspectos parciales) pero arrastra pendientes de S1-S4; la punta actual 67f8cea añade frontend, ingesta por URL y SonarCloud, pero la CI sigue en rojo y persisten huecos documentales.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Limpieza de __pycache__, archivos con sufijos '(3).py'/' (4).py' y data/verifacts.db realizada después del cierre (diff_desde_cierre 3120e06→67f8cea); el PDF en raíz persiste.
- SonarCloud y workflow 'Tests and SonarCloud' añadidos después del cierre (commits a1d23eb, 2a90b44, ab978d3, efbad6b), pero los runs 34407270858 y siguientes fallan.
- Frontend y soporte de URL incorporados después del cierre (commits 5fc30ce, 04d625d, 67f8cea), ampliando el corte vertical.

Pendientes que siguen abiertos:
- Julian Samuel Cabeza Pena sigue sin commits en HEAD.
- arc42 incompleto: falta sección 11 (riesgos) y docs/c4/03-componentes.md es plantilla sin completar.
- CI en rojo: runs_ci de 'Tests and SonarCloud' posteriores al cierre concluyen failure.
- docs/aspectos.md A-02 pendiente y enlaces rotos (docs/decisiones-arquitectonicas.md).
- PDF en la raíz del repositorio persiste en HEAD.

## Recuento y nota sugerida

4 de 12 criterios Cumple.

## No verificado / pendientes

- Corte vertical reproducible: requiere ejecutar python run.py y python -m pytest -q; no hay run que lo respalde.
- Pipeline y pruebas del estado calificado: no hay run anterior/igual al cierre; runs_ci posteriores fallan.
- PDF adjunto en Moodle: no disponible en la evidencia.
- Sustentación del corte: la resuelve el docente.

## Hallazgos para la planilla

- correcciones.md no refleja el estado real: marca pendientes ya resueltos (árbol de utilidad, leyenda C4, tensiones, POST /analysis).
- Tercer integrante declarado sin commits en el historial.
- arc42 incompleto y C4 nivel 3 sin completar.
- Persisten artefactos no deseados en el hash calificado: __pycache__, archivos con sufijos, PDF en raíz.
- Sin run de CI anterior al cierre; runs posteriores fallan.
- Trazabilidad con huecos: A-02 pendiente y enlace roto en README.
- Commits posteriores al cierre (no calificados): 67f8cea 2026-09-09T16:30:01-05:00 feat: integrate backend URL analysis contract and align frontend; 78126d4 2026-09-09T16:21:14-05:00 Update global.css with new styles and remove comments; 46fb432 2026-09-09T16:20:01-05:00 Destructure response from fetchAnalysisList; 2239a5f 2026-09-09T16:19:16-05:00 Add metadata section to ResultPanel component; f9324ee 2026-09-09T16:18:37-05:00 Update timestamp display format in HistoryLedger
