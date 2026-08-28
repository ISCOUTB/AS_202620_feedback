# semana-04-evidencia-s4 · Calificación automática

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `e976c92` (2026-08-24T01:58:18-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-ES.md indica 'secciones 5 a 8 se completan en las semanas 4 y 6' | No cumple | Las secciones 5 y 6 no están redactadas. |
| arc42 sección 9 al día y enlazada con los ADR existentes | El documento declara sección 9 escrita, pero el extracto no muestra su contenido | No verificado | Haría falta ver el archivo completo para confirmar enlaces a docs/adr/NNNN-*.md. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42-template-ES.md sección 1.2 referencia EC-01 a EC-06 y README menciona 5 priorizados y 2 complementarios | Cumple | La sección 10 está escrita y vinculada a los escenarios. |
| Glosario iniciado con términos del dominio | El documento declara sección 12 escrita, pero el extracto no muestra su contenido | No verificado | No se puede comprobar si contiene términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/doc-c4.md indica 'Niveles completos: Nivel 1 (Contexto)' y README lista 'C4 Niveles 2 y 3' como pendientes | No cumple | Falta el nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No existe C4 nivel 2 | No cumple | Sin diagrama de nivel 2 no hay correspondencia que verificar. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README dice 'Todavía no hay código para instalar ni ejecutar' y el árbol solo muestra módulos esqueleto | No cumple | No hay implementación del recorrido completo. |
| Arranque documentado con un solo comando | README sección 'Cómo se arranca' indica que no hay código para ejecutar | No cumple | No se documenta ningún comando de arranque. |
| Prueba automatizada del recorrido completo, en verde | README dice 'tampoco hay pruebas que correr' y los tests existentes son de arranque/importación, no del corte vertical | No cumple | No hay prueba del recorrido completo. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 tiene Código y Pruebas como 'Pendiente (S4)' | No cumple | La fila no está completa hasta Pruebas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Sistema-de-calificacion-automatica en ISCOUTB, público; autores: scp1109, josueacademico17-source, SusanaRosales, Mariadelmar-restrepo | Cumple | Los 4 integrantes declarados aparecen en el historial. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/0001-0003, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Rutas requeridas presentes. |
| Qué estado del repositorio se califica | Commit e976c92 del 2026-08-24, anterior al cierre 2026-08-31; sin commits posteriores | Cumple | Se califica el commit vigente al cierre. |
| Convenciones de ADR | Nombres 0001-usar-monolito-modular.md, 0002-procesar-calificacion-de-forma-asincrona.md, 0003-usar-fastapi-y-flutter.md siguen patrón; 0001 marcado reemplazado | Cumple | Sin ADR editados después de aceptados. |
| Tabla de aspectos | docs/aspectos.md fila A-01 tiene celdas Código y Pruebas con 'Pendiente (S4)' | No cumple | La fila exigida para esta semana tiene huecos. |
| Registro de uso de IA | docs/ia.md existe y tiene commits en 2026-08-07, 08-08, 08-16, 08-23 | Cumple | El registro crece a lo largo del semestre. |
| README | README sección 'Cómo se arranca' dice que no hay código para ejecutar | No cumple | No documenta arranque con un solo comando. |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml, pero no hay datos de ejecución ni configuración de SonarCloud | No verificado | Haría falta consultar runs de GitHub Actions y SonarCloud. |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 9 (contenido no visible)
- arc42 sección 12 glosario (contenido no visible)
- Pipeline y análisis estático (sin evidencia de ejecución)

## Hallazgos para la planilla

- arc42 secciones 5 y 6 pendientes
- C4 nivel 2 ausente
- Corte vertical no implementado
- README sin comando de arranque
- Fila A-01 de aspectos incompleta
- Sin prueba del recorrido completo
