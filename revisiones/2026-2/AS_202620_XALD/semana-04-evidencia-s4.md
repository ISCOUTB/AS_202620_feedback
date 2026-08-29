# semana-04-evidencia-s4 · XALD

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `7d18220` (2026-08-29T00:06:12-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md contiene secciones 1 y 2 redactadas, pero no se observan secciones 3 a 6 en la evidencia proporcionada. | No verificado | Falta ver el contenido completo del archivo para confirmar las secciones 3, 4, 5 y 6. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se observa la sección 9 en el extracto de docs/arc42/arc42-template-EN.md. | No verificado | Se requiere el contenido completo del archivo para verificar enlaces a docs/adr/NNNN-*.md. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se observa la sección 10 en el extracto proporcionado. | No verificado | Falta ver la sección 10 y su correspondencia con la tabla de escenarios. |
| Glosario iniciado con términos del dominio | No se observa la sección 12 en el extracto de docs/arc42/arc42-template-EN.md. | No verificado | Se necesita el contenido completo para confirmar términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/c4.md solo contiene el diagrama C1; no hay diagrama C2. | No cumple | El archivo menciona 'C2 - Container' pero no lo desarrolla. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No existe C4 nivel 2, por lo que no hay contenedores que contrastar con la estructura de directorios. | No cumple | Sin C2 no se puede verificar correspondencia. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Existen archivos MainActivity.kt, corefinanciero/cf.kt y syncqueue/sync.kt, pero no se inspeccionó su contenido. | No verificado | Se requiere revisar el código para confirmar el recorrido completo. |
| Arranque documentado con un solo comando | README.md solo muestra comandos para ejecutar pruebas (gradlew test), no un comando de arranque de la aplicación. | No cumple | No se documenta cómo ejecutar la app Android. |
| Prueba automatizada del recorrido completo, en verde | Existen archivos de prueba (Entornotest.kt, ExampleUnitTest.kt) pero no hay pipeline de CI configurado. | No verificado | Sin run de CI no se puede verificar ejecución en verde. Comando declarado: ./XALDAPP/gradlew -p XALDAPP test |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tiene 5 filas, pero las columnas CÓDIGO y PRUEBAS están marcadas como 'Pendiente' en todas. | No cumple | Ninguna fila llega completa hasta Pruebas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_XALD visible, autores: dilanbejarano011, colmenares2007-crypto, xaviergarciadiaz20-commits, axeljruiz717-hash. | Cumple | Los 4 autores corresponden a los integrantes declarados. |
| Estructura mínima | Árbol incluye docs/arc42/arc42-template-EN.md, docs/adr/ (6 archivos), docs/c4/c4.md, docs/aspectos.md, docs/ia.md, README.md. | Cumple | Todas las rutas requeridas están presentes. |
| Estado del repositorio que se califica | Commit calificado 7d18220, fecha 2026-08-29T00:06:12-05:00, anterior al cierre 2026-08-31T05:00:00Z. | Cumple | Sin etiqueta requerida para evidencia semanal. |
| Convenciones de ADR | ADR 0001, 0002, 0003, 0004, 0005 carecen de secciones 'Opciones evaluadas' y 'Trazabilidad'. | No cumple | El contrato exige contexto, opciones, decisión, consecuencias y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md tiene 9 columnas (incluye ESCENARIO) en lugar de las 8 exigidas; celdas CÓDIGO, PRUEBAS y EVIDENCIA están 'Pendiente'. | No cumple | Estructura desviada y filas incompletas. |
| Registro de uso de IA | docs/ia.md existe pero no especifica herramienta concreta ni separa claramente qué se aceptó y qué se rechazó por uso. | No cumple | Falta estructura exigida por el contrato. |
| README | README.md documenta solo comandos de prueba, no cómo arrancar la aplicación. | No cumple | No cumple 'cómo se arranca con un solo comando'. |
| Pipeline y análisis estático | No existe .github/workflows/ en el árbol; no hay evidencia de CI ni SonarCloud. | No cumple | Sin pipeline configurado. |

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 3 a 6: falta contenido completo del archivo.
- arc42 sección 9: no visible en extracto.
- arc42 sección 10: no visible en extracto.
- Glosario (sección 12): no visible en extracto.
- Corte vertical: no se inspeccionó el código de MainActivity, cf.kt y sync.kt.
- Prueba en verde: no hay run de CI que lo demuestre.

## Hallazgos para la planilla

- Falta C4 nivel 2 en docs/c4/c4.md.
- README no incluye comando de arranque, solo de pruebas.
- Tabla de aspectos tiene 9 columnas y celdas pendientes.
- ADRs no cumplen estructura completa (sin opciones evaluadas ni trazabilidad).
- No hay pipeline de CI configurado.
- Arc42 solo muestra secciones 1 y 2 en la evidencia; secciones 3-6, 9, 10 y 12 no verificables.
