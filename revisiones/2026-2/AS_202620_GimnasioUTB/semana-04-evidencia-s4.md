# semana-04-evidencia-s4 · GimnasioUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `73c1f24` (2026-08-23T19:38:29-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42_gimnasio_utb.md existe pero contenido truncado tras sección 2.2 | No verificado | No se pudo comprobar secciones 3-6; haría falta contenido completo del archivo. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se muestra sección 9 en el contenido proporcionado | No verificado | Haría falta ver el encabezado y enlaces a docs/adr/. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se muestra sección 10 | No verificado | Haría falta ver la sección y comparar con escenarios. |
| Glosario iniciado con términos del dominio | No se muestra sección 12 | No verificado | Haría falta ver la sección 12 con términos propios. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo existe docs/C4.jpg, sin nivel 2 separado | No cumple | No hay evidencia de diagrama de nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay C4 nivel 2 para contrastar | No cumple | Sin nivel 2 no se puede verificar correspondencia. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README indica 'Esta entrega no incluye lógica de negocio'; solo esqueleto con .gitkeep | No cumple | No hay implementación de interfaz/lógica/persistencia. |
| Arranque documentado con un solo comando | README.md: 'npm install && npm start' y 'npm start' | Cumple | Requisitos previos declarados (Node.js ≥18). |
| Prueba automatizada del recorrido completo, en verde | Solo tests/health.test.js, prueba de health no de recorrido | No cumple | No existe prueba del corte vertical. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md es texto narrativo, sin tabla de 8 columnas | No cumple | No hay fila con ID, aspecto, requisito, C4, ADR, código, pruebas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_GimnasioUTB público, autores en historial | Cumple | Tres integrantes con commits. |
| Estructura mínima | Faltan directorios docs/arc42/ y docs/c4/; artefactos en docs/arc42_gimnasio_utb.md y docs/C4.jpg | No cumple | Desviación de estructura registrada. |
| Estado del repositorio calificado | hash 73c1f24 fecha 2026-08-23T19:38:29-05:00 anterior al cierre | Cumple | Sin commits tardíos. |
| Convenciones de ADR | docs/adr/0001-arquitectura-hexagonal.md con nombre correcto y contenido completo | Cumple | Sin reescrituras. |
| Tabla de aspectos | docs/aspectos.md sin tabla de 8 columnas | No cumple | Falta estructura de trazabilidad. |
| Registro de uso de IA | docs/ia.md tiene entradas pero no documenta rechazos con motivo técnico | No cumple | Falta columna de rechazado. |
| README | README.md con qué es, arranque y prueba | Cumple | Comando único documentado. |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta npm test, pero no hay SonarCloud | No cumple | Falta análisis estático. |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 1 a 6 redactadas
- arc42 sección 9
- arc42 sección 10
- Glosario iniciado

## Hallazgos para la planilla

- No hay corte vertical implementado
- C4 solo nivel 1 en imagen
- aspectos.md no es tabla
- estructura desviada
- falta SonarCloud
- IA sin rechazos
