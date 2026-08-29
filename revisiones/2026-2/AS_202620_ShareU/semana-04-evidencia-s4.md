# semana-04-evidencia-s4 · ShareU

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `4fb8f3e` (2026-08-26T18:47:08-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md contiene sección 1 redactada (Introduction and Goals, Requirements Overview, Quality Goals) | No verificado | Solo se evidencia sección 1; secciones 2-6 no mostradas en el contenido proporcionado |
| arc42 sección 9 al día y enlazada con los ADR existentes | Existe docs/adr/0001-estilo-arquitectonico.md | No verificado | No se muestra la sección 9 del arc42 |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se muestra la sección 10 | No verificado | No se puede contrastar con escenarios |
| Glosario iniciado con términos del dominio | No se muestra la sección 12 | No verificado | Sin evidencia de glosario |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/C4/nivel1.mmd (código) y docs/C4/NIVEL2.png (imagen) | No verificado | NIVEL2.png no es inspeccionable; no se puede verificar coherencia |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Estructura de código: app/usuarios, app/documentos, app/busqueda, app/calificaciones, app/administracion | No verificado | No se puede contrastar con NIVEL2.png |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README: 'todavía sin lógica de negocio'; árbol sin archivos de persistencia | No cumple | No hay lógica ni persistencia; solo routers vacíos |
| Arranque documentado con un solo comando | README.md no incluye sección de arranque ni comando | No cumple | Falta comando único de arranque |
| Prueba automatizada del recorrido completo, en verde | tests/test_esqueleto.py existe, sin contenido ni run de CI | No verificado | No se evidencia prueba del recorrido completo ni ejecución en verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos/aspectos.md es narrativo, sin tabla de columnas | No cumple | No hay fila con ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_ShareU visible; autores: Dayana, Nicolas-HH, luiscorredor, steven | Cumple | Los 4 integrantes declarados aparecen en el historial |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos/aspectos.md, docs/ia.md, README.md presentes | Cumple | aspectos.md en subcarpeta docs/aspectos/ en lugar de docs/aspectos.md (desviación) |
| Estado calificado | Commit 4fb8f3e anterior al cierre, sin etiqueta | No cumple | Sin etiqueta de corte; se revisa último commit anterior al cierre |
| Convenciones de ADR | Existe 'docs/adr/ADR 0001 — Arquitectura del backend: Monolito Modular.md' | No cumple | Nombre no sigue convención kebab-case |
| Tabla de aspectos | docs/aspectos/aspectos.md sin tabla de 8 columnas | No cumple | Contenido narrativo, no navegable |
| Registro de uso de IA | docs/ia.md con tabla pero sin columna de rechazo técnico | No cumple | No registra qué se rechazó y por qué |
| README | README.md sin comando de arranque ni instrucciones de prueba | No cumple | No cumple reproducibilidad |
| Pipeline y análisis estático | Sin .github/workflows/ ni runs de CI | No cumple | No hay integración continua |

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Secciones 2-6,9,10,12 de arc42
- Coherencia C4 nivel1-nivel2
- Correspondencia C4-código
- Prueba automatizada en verde

## Hallazgos para la planilla

- Sin etiqueta de corte
- ADR con nombre no conforme
- README sin comando de arranque
- No hay pipeline CI
- aspectos.md no es tabla
- Corte vertical sin lógica ni persistencia
- arc42 solo sección 1 evidenciada
- C4 nivel2 solo imagen no verificable
