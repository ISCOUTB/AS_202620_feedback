# Evidencia S4 · ShareU

> **Revisión excepcional solicitada por el docente:** se revisan únicamente los entregables
> actualmente disponibles. No se aplican cierres, fechas, etiquetas, actividad de commits,
> autoría ni criterios de la matriz transversal.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado inspeccionado | punta actual de `master`: [`0bae184`](https://github.com/ISCOUTB/AS_202620_ShareU/tree/0bae18410091824e51739f1bfc6fe0eabf954013) |
| Alcance | Entregables de la ficha S4 solamente |
| Revisor | revisión excepcional del docente |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | [`docs/arc42/arc42.md:6-170`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/arc42/arc42.md#L6-L170) | Cumple | Las secciones 1 a 6 están redactadas para ShareU y describen objetivos, restricciones, contexto, estrategia, bloques y ejecución. |
| arc42 sección 9 al día y enlazada con los ADR existentes | [`docs/arc42/arc42.md:217-220`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/arc42/arc42.md#L217-L220), [`docs/adr/`](https://github.com/ISCOUTB/AS_202620_ShareU/tree/0bae18410091824e51739f1bfc6fe0eabf954013/docs/adr) | No cumple | La sección 9 enlaza ADR 0001, pero no los ADR 0002 y 0003 que también existen en el repositorio; por ello no está al día. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | [`docs/arc42/arc42.md:222-231`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/arc42/arc42.md#L222-L231), [`docs/aspectos/aspectos.md:15-24`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/aspectos/aspectos.md#L15-L24) | Cumple | Conserva el escenario de usabilidad de tres interacciones y lo relaciona con filtros combinables en una solicitud. |
| Glosario iniciado con términos del dominio | [`docs/arc42/arc42.md:243-254`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/arc42/arc42.md#L243-L254) | Cumple | Incluye términos propios como ShareU, documento y filtro, además de conceptos arquitectónicos necesarios. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | [`docs/c4/nivel1.mmd:5-28`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/c4/nivel1.mmd#L5-L28), [`docs/c4/nivel2.mmd:5-38`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/c4/nivel2.mmd#L5-L38) | No cumple | El archivo llamado nivel 1 usa `C4Container` y se titula «Diagrama de Contenedores»; no aporta el diagrama de contexto (nivel 1) requerido. El segundo también es de contenedores. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | [`docs/c4/nivel2.mmd:19-36`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/c4/nivel2.mmd#L19-L36), [`app/main.py:10-32`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/app/main.py#L10-L32) | Cumple | Los cinco módulos del diagrama se corresponden con los routers y directorios de la aplicación. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | [`app/busqueda/router.py:19-37`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/app/busqueda/router.py#L19-L37), [`service.py:56-87`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/app/busqueda/service.py#L56-L87), [`repository.py:25-84`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/app/documentos/repository.py#L25-L84) | Cumple | El endpoint invoca el servicio de búsqueda, que usa el servicio público de documentos y su repositorio SQLite. |
| Arranque documentado con un solo comando | [`README.md:29-69`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/README.md#L29-L69) | Cumple | Requisitos, instalación y un único comando de arranque están documentados. No se ejecutó localmente. |
| Prueba automatizada del recorrido completo, en verde | [`tests/test_busqueda.py:9-60`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/tests/test_busqueda.py#L9-L60), [`workflow`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/.github/workflows/tests.yml), [run verde](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/34892971998) | Cumple | La prueba ejercita el endpoint de búsqueda con filtros y el workflow la ejecuta con `pytest -q` en verde. |
| Fila de `docs/aspectos.md` completa hasta la columna Pruebas | [`docs/aspectos/aspectos.md:50-55`](https://github.com/ISCOUTB/AS_202620_ShareU/blob/0bae18410091824e51739f1bfc6fe0eabf954013/docs/aspectos/aspectos.md#L50-L55) | No cumple | El archivo está en una ruta desviada y la tabla tiene seis columnas; faltan al menos ID y C4 de la cadena de ocho columnas del curso. |

## Recuento y nota sugerida

**7 de 10 criterios Cumple.**

**Nota sugerida: 3.8 = 1 + 4 × (7/10).** Es una propuesta al docente; la nota oficial la fija el docente en Moodle.

## Pendientes de los entregables

- Crear un C4 de contexto real como nivel 1 y mantener el nivel 2 de contenedores coherente con él.
- Actualizar la sección 9 de arc42 con ADR 0002 y ADR 0003.
- Llevar la trazabilidad a `docs/aspectos.md` y completar las ocho columnas: ID, Aspecto, Requisito, C4, ADR, Código, Pruebas y Evidencia.
