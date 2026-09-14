# Evidencia S3 · ShareU

> **Revisión excepcional solicitada por el docente:** se revisan únicamente los entregables
> actualmente disponibles. No se aplican cierres, fechas, etiquetas, actividad de commits,
> autoría ni criterios de la matriz transversal.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado inspeccionado | punta actual de `master`: [`0bae184`](https://github.com/ISCOUTB/AS_202620_ShareU/tree/0bae18410091824e51739f1bfc6fe0eabf954013) |
| Alcance | Entregables de la ficha S3 solamente |
| Revisor | revisión excepcional del docente |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | [`docs/arc42/arc42.md:77-99`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/arc42/arc42.md#L77-L99), [`ADR 0001:87-95`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/adr/0001-estilo-arquitectonico.md#L87-L95) | Cumple | El monolito modular se vincula al escenario de usabilidad y las tácticas declaran atributo, costo y efecto. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | [`docs/aspectos/aspectos.md:15-62`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/aspectos/aspectos.md#L15-L62), [`ADR 0001:42-69`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/adr/0001-estilo-arquitectonico.md#L42-L69) | No cumple | Hay escenario y alternativas narradas, pero no una matriz que compare capas, hexagonal y monolito modular contra un árbol de utilidad con escenarios. |
| `docs/adr/0001-*.md` con el nombre de la convención | [`docs/adr/0001-estilo-arquitectonico.md`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/adr/0001-estilo-arquitectonico.md) | Cumple | El archivo usa prefijo numérico y nombre en kebab-case. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | [`ADR 0001:6-85`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/adr/0001-estilo-arquitectonico.md#L6-L85) | Cumple | Están presentes contexto, decisión, alternativas y consecuencias positivas y negativas. |
| Alternativas descartadas con su motivo | [`ADR 0001:42-69`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/adr/0001-estilo-arquitectonico.md#L42-L69) | Cumple | Capas y hexagonal se descartan con motivo, consecuencia y criterio de reapertura. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | [`docs/aspectos/aspectos.md:52-62`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/aspectos/aspectos.md#L52-L62), escenario en [`:15-24`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/aspectos/aspectos.md#L15-L24) | No cumple | La tabla enlaza ADR 0001, pero el escenario de usabilidad no contiene un enlace directo hacia ese ADR; la relación queda solo declarada en prosa. |
| Arranque con un solo comando documentado en el README | [`README.md:29-69`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/README.md#L29-L69), [`requirements.txt`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/requirements.txt) | Cumple | Declara requisitos e instalación; el comando de arranque es `uvicorn app.main:app --reload`. No se ejecutó localmente. |
| Prueba automatizada en verde | [`tests/test_esqueleto.py`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/tests/test_esqueleto.py), [`workflow`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/.github/workflows/tests.yml), [run verde](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/34892971998) | Cumple | El workflow ejecuta `PYTHONPATH=. pytest -q` y el run asociado al estado inspeccionado finalizó correctamente. |
| Estructura de paquetes correspondiente al estilo del ADR | [`app/main.py:10-32`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/app/main.py#L10-L32), [`ADR 0001:27-40`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/adr/0001-estilo-arquitectonico.md#L27-L40) | Cumple | Los módulos `usuarios`, `documentos`, `busqueda`, `calificaciones` y `administracion` se montan por separado, coherentes con el monolito modular decidido. |

## Recuento y nota sugerida

**7 de 9 criterios Cumple.**

**Nota sugerida: 4.1 = 1 + 4 × (7/9).** Es una propuesta al docente; la nota oficial la fija el docente en Moodle.

## Pendientes de los entregables

- Construir la matriz explícita de los tres estilos contra el árbol de utilidad y sus escenarios.
- Enlazar ADR 0001 directamente desde el escenario de calidad que lo motiva.
