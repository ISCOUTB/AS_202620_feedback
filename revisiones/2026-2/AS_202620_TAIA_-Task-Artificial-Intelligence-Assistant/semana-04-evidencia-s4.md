# semana-04-evidencia-s4 · TAIA

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `9df9d2a` (2026-08-29T18:51:30-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md contiene secciones 1 y 2 redactadas; no se muestran secciones 3-6 en la evidencia | No verificado | Falta evidencia de secciones 3-6 y filtro de plantilla |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se observa sección 9 en docs/arc42/arc42-template-EN.md | No verificado | Sin contenido de sección 9 en la evidencia |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se observa sección 10 en docs/arc42/arc42-template-EN.md | No verificado | Sin contenido de sección 10 en la evidencia |
| Glosario iniciado con términos del dominio | No se observa sección 12 en docs/arc42/arc42-template-EN.md | No verificado | Sin contenido de sección 12 en la evidencia |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/C4-C1.md y docs/c4/C4-C2.md con código Mermaid; actores externos coinciden | Cumple | Diagramas como código, coherencia entre niveles verificada |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Contenedor API corresponde a backend/app/main.py; no existe directorio para App Móvil (Flutter) | No cumple | App Móvil dibujada sin código en el repositorio |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md declara 'no se implementa lógica de negocio'; backend/app/main.py solo endpoint /health | No cumple | No hay lógica ni persistencia implementadas |
| Arranque documentado con un solo comando | README.md sección Ejecución: '.\run.bat' | Cumple | Comando declarado, no ejecutado |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_entrega3.py solo prueba /health; sin URL de run | No cumple | No existe prueba del corte vertical |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con celdas C4, Código, Pruebas, Evidencia en 'Pendiente' | No cumple | Celdas no navegables, fila incompleta |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant en ISCOUTB, visible true | Cumple | Nombre sigue patrón, público |
| Estructura mínima | Árbol incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | Estructura requerida presente |
| Versionado y estado calificado | Commit 9df9d2a 2026-08-29T18:51:30-05:00 antes del cierre, sin etiqueta corte-1 | No cumple | Falta etiqueta; se revisa último commit |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md sin secciones explícitas de Consecuencias y Trazabilidad | No cumple | ADR incompleto según contrato |
| Tabla de aspectos | docs/aspectos.md fila A-01 con celdas Pendiente | No cumple | Fila no defendible por huecos |
| Registro de uso de IA | docs/ia.md con entradas 001-003, incluye Rechazado o modificado con motivos | Cumple | Registro con rechazos técnicos |
| README | README.md con descripción, requisitos, comando .\run.bat y pytest | Cumple | Documento de arranque y prueba completo |
| Pipeline y análisis estático | Árbol sin .github/workflows/ ni evidencia de runs | No cumple | No hay CI configurada |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Secciones arc42 3-6,9,10,12
- Ejecución del comando de arranque
- Etiqueta de versionado
- Pruebas en CI

## Hallazgos para la planilla

- No hay corte vertical implementado
- Fila de aspectos incompleta con celdas Pendiente
- No hay pipeline de CI
- ADR sin trazabilidad completa
- Secciones arc42 3-6,9,10,12 no verificadas en evidencia
