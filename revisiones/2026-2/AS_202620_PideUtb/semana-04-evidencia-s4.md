# semana-04-evidencia-s4 · PideUtb

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `1636f20` (2026-08-30T22:17:18-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | No se listan archivos docs/arc42 en el árbol proporcionado | No verificado | Árbol truncado; falta listado de docs/arc42 |
| arc42 sección 9 al día y enlazada con los ADR existentes | Sin docs/adr en árbol | No verificado | No se puede comprobar enlace |
| arc42 sección 10 coherente con los escenarios de la semana 2 | Sin docs/arc42 | No verificado | No se puede comparar |
| Glosario iniciado con términos del dominio | Sin sección 12 visible | No verificado | Falta listado |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Sin docs/c4 en árbol | No verificado | No se puede verificar coherencia |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin docs/c4 ni estructura de código clara | No verificado | Árbol solo muestra .venv-1 |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Sin rutas de código en árbol | No verificado | No se identifican archivos de aplicación |
| Arranque documentado con un solo comando | Sin README en árbol | No verificado | No se puede leer comando |
| Prueba automatizada del recorrido completo, en verde | Sin ruta de prueba ni URL de run | No verificado | No hay CI visible |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | Sin docs/aspectos.md en árbol | No verificado | No se puede verificar fila |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_PideUtb visible true, pero organización no confirmada | No verificado | Falta confirmar ISCOUTB |
| Estructura mínima | Árbol no muestra docs/arc42, adr, c4, aspectos.md, ia.md, README.md | No verificado | Árbol truncado; no se puede confirmar estructura |
| Versionado | hash 1636f20 fecha 2026-08-30T22:17:18-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit vigente correcto para evidencia semanal |
| Convenciones de ADR | Sin docs/adr en árbol | No verificado | No se puede comprobar convenciones |
| Tabla de aspectos | Sin docs/aspectos.md | No verificado | No se puede comprobar tabla |
| Registro de uso de IA | Sin docs/ia.md | No verificado | No se puede comprobar registro |
| README | Sin README.md en árbol | No verificado | No se puede comprobar arranque |
| Pipeline y análisis estático | Sin .github/workflows ni runs | No verificado | No se puede comprobar CI |

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 1-6, 9, 10 y glosario: falta listado de docs/arc42
- C4 niveles 1 y 2 y correspondencia con código: falta docs/c4 y estructura de código
- Corte vertical y prueba automatizada: falta código fuente y CI
- Arranque con un solo comando: falta README
- Fila de aspectos: falta docs/aspectos.md
- Identidad: falta confirmar organización ISCOUTB
- Estructura mínima: falta listado completo de docs/
- ADR, IA, Pipeline: falta evidencia

## Hallazgos para la planilla

- .venv-1 versionado en el repositorio (miles de archivos de dependencias)
- Árbol de archivos proporcionado está truncado y no muestra docs/ ni código de aplicación
- No se observa evidencia de CI ni de pruebas automatizadas
- Secretos: las coincidencias de grep son falsos positivos en .venv-1/site-packages, no credenciales reales
