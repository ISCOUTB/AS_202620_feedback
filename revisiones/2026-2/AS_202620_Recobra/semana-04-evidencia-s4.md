# semana-04-evidencia-s4 · Recobra

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `50d601c` (2026-08-25T09:14:56-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42.md contiene secciones 1-4 y 10; no hay secciones 5 ni 6 | No cumple | Faltan las secciones 5 (bloques de construcción) y 6 (vista de ejecución) |
| arc42 sección 9 al día y enlazada con los ADR existentes | No existe sección 9 en docs/arc42.md ni archivo separado | No cumple | No se encontró referencia a docs/adr/0001-estilo-arquitectonico.md |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42.md sección 10 lista S1-S7 y los relaciona con decisiones | Cumple | Coherente con docs/escenarios_calidad.md y docs/arbol_utilidad.md |
| Glosario iniciado con términos del dominio | No hay sección 12 en docs/arc42.md ni archivo de glosario | No cumple | Sin términos propios del sistema |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/README.md incluye ambos niveles, pero el nivel 2 omite al actor admin y al sistema externo auth del nivel 1 | No cumple | Incoherencia: actores externos del nivel 1 no reaparecen en nivel 2 |
| Límites del C4 nivel 2 correspondientes a la estructura del código | El árbol proporcionado está truncado y no muestra src/ ni estructura de código | No verificado | Haría falta listar src/ para contrastar contenedores app, api, db |
| Corte vertical que atraviesa interfaz, lógica y persistencia | No se pudieron citar las tres rutas porque el árbol no incluye archivos de código | No verificado | Haría falta ver src/server.js, src/application, src/infrastructure |
| Arranque documentado con un solo comando | README.md declara requisitos (Node.js 18+) y comando 'npm install && npm start' | Cumple | Comando único con &&, aceptable |
| Prueba automatizada del recorrido completo, en verde | No se encontró ruta de prueba ni URL de run en la evidencia | No verificado | Haría falta tests/ y enlace a CI en verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md contiene solo texto narrativo, sin tabla con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia | No cumple | No hay fila defendible |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Nombre AS_202620_Recobra y visible true | Cumple | Sin confirmación explícita de organización ISCOUTB, pero patrón correcto |
| Estructura mínima | Árbol muestra docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Rutas mínimas presentes |
| Versionado/estado calificado | Hash 50d601c sin etiqueta corte-1 | No cumple | Etiqueta ausente; se revisó último commit antes del cierre |
| Convenciones ADR | docs/adr/0001-estilo-arquitectonico.md sigue patrón de nombre y contiene estado, contexto, decisión, consecuencias | Cumple | No se pudo verificar historial de edición |
| Tabla de aspectos | docs/aspectos.md no tiene tabla con las ocho columnas | No cumple | Solo texto narrativo |
| Registro IA | docs/ia.md existe y tiene commit 2026-08-23T23:44:12-05:00 cb5c579 | Cumple | Registro presente |
| README | README.md incluye descripción, arranque y pruebas | Cumple | Cumple requisitos |
| Pipeline y análisis estático | No hay .github/workflows en el árbol | No cumple | Sin CI configurada |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Corte vertical: no se pudieron citar rutas de interfaz/lógica/persistencia
- Prueba automatizada: falta URL de run en verde
- Correspondencia C4-código: árbol truncado no muestra estructura src/

## Hallazgos para la planilla

- Secciones arc42 5, 6, 9 y 12 ausentes
- C4 nivel 2 omite actor admin y sistema auth del nivel 1
- docs/aspectos.md no es tabla, solo narrativa
- node_modules versionado en el repositorio
- Secreto repo_token en node_modules/debug/.coveralls.yml
- Sin pipeline de CI
- Sin evidencia de corte vertical ni prueba automatizada
