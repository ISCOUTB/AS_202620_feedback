# semana-04-evidencia-s4 · LaPlacita

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `745e799` (2026-08-30T21:52:41-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md existe, pero la evidencia solo muestra hasta la sección 4 | No verificado | No se incluyó el contenido de las secciones 5 y 6; haría falta ver el archivo completo |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se muestra la sección 9 en la evidencia | No verificado | Haría falta ver el contenido de la sección 9 y sus enlaces a docs/adr/ |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se muestra la sección 10 en la evidencia | No verificado | Haría falta ver la sección 10 y compararla con la tabla de escenarios |
| Glosario iniciado con términos del dominio | No se muestra la sección 12 en la evidencia | No verificado | Haría falta ver la sección 12 y sus términos propios del sistema |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.md y docs/c4/contenedores.md existen; actores Usuario y Establecimiento y sistemas externos Pago y Push reaparecen en ambos niveles | Cumple | Coherencia verificada entre actores y sistemas externos |
| Límites del C4 nivel 2 correspondientes a la estructura del código | El diagrama de contenedores incluye App/Web Cliente, Portal Establecimiento, Redis y PostgreSQL, pero el repositorio solo tiene código para API Backend Central (src/modules, app/health/route.js) | No cumple | Correspondencia parcial: API Backend Central sí corresponde; los demás contenedores no tienen código |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Existen src/corte-vertical.js y tests/corte-vertical.test.js, pero no se muestra su contenido | No verificado | Haría falta ver el código para citar las tres rutas (interfaz, lógica, persistencia) |
| Arranque documentado con un solo comando | README.md tiene sección 'Cómo ejecutar' pero no se muestra el comando único | No verificado | Haría falta ver el contenido de esa sección para confirmar requisitos previos y comando |
| Prueba automatizada del recorrido completo, en verde | tests/corte-vertical.test.js existe, pero no se proporciona URL de run de CI en verde | No verificado | Haría falta la URL del run de GitHub Actions que ejecutó la prueba |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | Fila A-01 tiene Código (src/modules/pedidos/index.js) y Pruebas (tests/modulos.test.js, tests/corte-vertical.test.js) con rutas existentes | Cumple | Las celdas hasta Pruebas están llenas y navegables |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_LaPlacita público; autores consolidados: Jorge M. Castillo, samulssl, Isaza927, matbuendia | Cumple | Los cuatro integrantes declarados aparecen en el historial |
| Estructura mínima | Existen docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura conforme, aunque arc42 está en un solo archivo |
| Estado del repositorio calificado | Commit 745e799 con fecha 2026-08-30T21:52:41-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta, pero para evidencia semanal no se exige |
| Convenciones de ADR | Archivos 0001, 0002, 0003 con nombres en kebab-case; cada uno tiene contexto, opciones, decisión, consecuencias y trazabilidad | Cumple | ADR 0001 propuesto, 0002 y 0003 aceptados; no se evidencia edición posterior |
| Tabla de aspectos | docs/aspectos.md tiene fila A-01 con columnas hasta Pruebas completas y enlaces válidos | Cumple | Cumple el requisito semanal de una fila completa hasta Pruebas |
| Registro de uso de IA | docs/ia.md existe con bitácora y múltiples commits en su historial | Cumple | Registro presente y en crecimiento |
| README | README.md tiene sección 'Cómo ejecutar' pero no se muestra el comando único ni requisitos previos | No verificado | Haría falta ver el contenido completo de esa sección |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml, pero no se evidencia ejecución de CI ni configuración de SonarCloud | No verificado | Haría falta URL de run en verde y evidencia de análisis estático |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 1-6: falta contenido de secciones 5 y 6.
- arc42 sección 9: falta contenido y enlaces a ADR.
- arc42 sección 10: falta contenido y comparación con escenarios.
- Glosario (sección 12): falta contenido.
- Corte vertical: falta código para citar interfaz, lógica y persistencia.
- Arranque: falta comando único en README.
- Prueba en verde: falta URL de run de CI.
- Pipeline y análisis estático: falta evidencia de ejecución y SonarCloud.

## Hallazgos para la planilla

- El C4 nivel 2 incluye contenedores sin código correspondiente (App/Web Cliente, Portal Establecimiento, Redis, PostgreSQL).
- No se pudo verificar el contenido de las secciones 5, 6, 9, 10 y 12 de arc42 porque la evidencia no incluye el archivo completo.
- No se evidencia ejecución de CI ni URL de run en verde para la prueba del corte vertical.
- El README declara secciones de ejecución pero no se muestra el comando único de arranque.
