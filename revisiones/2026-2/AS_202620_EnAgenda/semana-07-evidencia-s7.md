# semana-07-evidencia-s7 · EnAgenda

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `0a58de8` en `origin/master` (2026-09-13T23:38:41-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | 0a58de8: el árbol completo no contiene ningún .yaml/.json de openapi\|swagger\|asyncapi ni ningún .proto; solo docs/*.md, app/web.py, src/** y tests/**. | No cumple | Se esperaba un archivo de contrato ejecutable; docs/adr/0001-usar-monolito-modular.md declara que el sistema 'no expondrá una API pública', por lo que el artefacto no existe. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No hay archivo de contrato en 0a58de8 del que citar rutas ni esquemas de respuesta. | No cumple | Al no existir contrato no hay fragmento citable de paths ni de schemas. |
| Correspondencia entre el contrato y la API implementada | La API implementada son rutas Flask en app/web.py (p. ej. endpoint ver_invitacion en app/web.py:38) y no existe contrato con el que contrastar en ninguno de los dos sentidos. | No cumple | No se puede tomar dos rutas del contrato ni una del código porque el contrato falta. |
| Versión de la API declarada y con historial | No existe ruta de contrato en 0a58de8, por lo que `git log -- <contrato>` no aplica; README.md describe la aplicación sin declarar versión de API. | No cumple | Se esperaba campo de versión en el contrato y su historial en git; ninguno es verificable. |
| Prueba de contrato presente | tests/ solo contiene tests/test_invitaciones.py (pruebas unitarias de dominio); no hay archivos ni dependencias tipo dredd, pact, schemathesis, prism o spectral. | No cumple | Las pruebas existentes validan reglas de invitaciones, no un contrato de API. |
| El pipeline ejecuta la prueba de contrato | 0a58de8:.github/workflows/ci.yml solo define checkout, setup-python 3.13, `pip install -r requerimiento.txt` y `pytest -q`; ningún paso invoca una prueba de contrato (run de ejemplo: run 34806818454 del 2026-09-14, success). | No cumple | El workflow sí se ejecuta en push/PR a master, pero no contiene nada relacionado con contrato. |
| Evidencia de que la prueba falla ante un cambio incompatible | Los 10 runs listados para 0a58de8 (CI y pages) tienen conclusion success; el equipo no aporta evidencia de un cambio incompatible que rompiera la prueba. | No verificado | No hay prueba de contrato que pueda fallar; queda como pregunta de sustentación: qué cambio incompatible se probó y con qué resultado. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001-usar-monolito-modular.md decide estilo (capas, hexagonal, monolito modular) y menciona EC-01..EC-05 y la alternativa descartada, pero no compara integración síncrona frente a asíncrona ni sus consecuencias de acoplamiento. | No cumple | El ADR existente es de estilo arquitectónico, no de estrategia de integración; no se localizó otro ADR en docs/adr/. |
| arc42 sección 6 con los flujos de interacción | 0a58de8:docs/arc42/06-vista-de-ejecución.md existe en el árbol, pero su contenido no viene incluido en la evidencia entregada. | No verificado | Haría falta leer el archivo para comprobar los flujos; docs/arc42/07-vista-de-despliegue.md sí aparece como plantilla vacía ('se completará durante el desarrollo'). |
| C4 nivel 2 con protocolo y formato en cada flecha | 0a58de8:docs/c4/nivel-2-contenedores.md: las flechas usan 'HTTP' (organizador→webApp, invitado→webApp) y 'Llamada interna' (webApp→módulo, módulo→repositorio); ninguna declara formato (JSON, HTML, etc.). | No cumple | Faltan los formatos en todas las flechas y dos flechas internas no declaran protocolo ni formato explícito. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio visible en la organización ISCOUTB con nombre AS_202620_EnAgenda (0a58de8); autoría en el historial: Daoisttl0FB3, Jein-12, eliabarnedocondef10-gif y GabrielaMorales Cancino. | Cumple | Daoisttl0FB3 y GabrielaMorales Cancino comparten la misma dirección de autor y se consolidan en una identidad; no se atribuyen cuentas a integrantes por parecido de nombre. |
| Estructura mínima | 0a58de8 contiene docs/arc42/ (01 a 12), docs/adr/0001-usar-monolito-modular.md, docs/c4/ (niveles 1, 2 y 3), docs/aspectos.md, docs/ia.md y README.md, con el código en src/ y app/. | Cumple | Desviaciones menores: nombres de arc42 con espacios y acentos, y archivos .pyc versionados en src/ y tests/. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md cumple el patrón NNNN-kebab-case, el título enuncia la decisión y el documento trae contexto, alternativas evaluadas, decisión, consecuencias y trazabilidad. | Cumple | Solo hay un ADR; su sección de trazabilidad cita rutas de arc42 que no coinciden con los nombres reales de los archivos. |
| La tabla de aspectos | docs/aspectos.md tiene las ocho columnas (ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia) y la fila A-01 enlaza C4 niveles 1-3, ADR-0001, src/invitaciones/, app/web.py, tests/test_invitaciones.py y docs/evidencia.md. | Cumple | Una sola fila, coherente con el único corte vertical implementado. |
| Registro de uso de IA | docs/ia.md registra fecha, herramienta, propósito, qué se aceptó, qué se rechazó y cómo se verificó, con cinco entradas entre 2026-08-25 y 2026-09-13. | Cumple | Incluye rechazos con motivo técnico (rol colaborador, envío obligatorio por correo, propuesta de Next.js). |
| README | README.md describe el sistema, declara requisitos previos (Python 3.13 y pip), la instalación, las pruebas con `pytest -q` y el arranque con `python app\web.py`. | Cumple | El comando de arranque usa ruta de Windows y no se comprobó ejecución real (no se ejecuta código). |
| Pipeline y análisis estático | 0a58de8:.github/workflows/ci.yml ejecuta `pip install -r requerimiento.txt` y `pytest -q` con runs exitosos (run 34806818454), pero no hay sonar-project.properties en el árbol, ni paso del scanner en el workflow, ni URL pública de análisis con Quality Gate. | No cumple | Se esperaban las tres evidencias de SonarCloud; faltan la invocación del scanner y la URL del análisis, aunque el CI sí corre y pasa. |
| Secretos | La búsqueda de secretos en 0a58de8 solo marca nombres de variable token= en src/invitaciones/dominio/invitaciones.py:26 (`secrets.token_urlsafe(32)`), app/web.py y tests; envs_versionados vacío, sin claves privadas. | Cumple | Los aciertos del patrón son identificadores de invitación, no credenciales; no hay nada que rotar. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `0a58de865e0ddcde35c2b6fb73433c8611752219 2026-09-13T23:38:41-05:00 Update ia.md`
- **Veredicto**: con pendientes
- Resumen: Estado calificado 0a58de8 (2026-09-13T23:38:41-05:00) sobre origin/master, sin diferencias frente al cierre anterior y sin commits nuevos: la entrega de S7 no está reflejada en la rama. El proyecto mantiene su corte vertical de Invitaciones con documentación arc42, C4, ADR y aspectos coherentes, y CI en verde, pero no hay contrato de API, ni prueba de contrato en el pipeline, ni ADR de estrategia de integración, y el C4 nivel 2 no declara formatos.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Ninguno: commits_post_cierre vacío y diff_desde_cierre 'sin diferencias con el estado calificado'; el HEAD de la rama sigue siendo 0a58de8.

Pendientes que siguen abiertos:
- Contrato OpenAPI/AsyncAPI/proto versionado y ejecutable
- Rutas con esquemas de datos y correspondencia con la API implementada
- Versión de API declarada con historial en git
- Prueba de contrato presente y ejecutada por el workflow
- Evidencia de que la prueba falla ante un cambio incompatible (run en rojo o evidencia aportada)
- ADR de estrategia de integración (síncrona o asíncrona) con alternativa descartada
- Verificación de arc42 sección 6 con los flujos de interacción
- Formato en cada flecha del C4 nivel 2
- Análisis estático auditable en SonarCloud (scanner en workflow, run y URL con Quality Gate)

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 6: docs/arc42/06-vista-de-ejecución.md existe en 0a58de8 pero su contenido no fue incluido en la evidencia; hace falta leerlo para comprobar los flujos de interacción.
- Fallo de la prueba de contrato: no hay prueba de contrato en la rama ni run en rojo entre los diez runs revisados; se requiere la prueba en el pipeline y el run que falle.
- SonarCloud: sin archivo de configuración, sin invocación del scanner en el workflow y sin URL pública del análisis, no se puede auditar el Quality Gate.
- Ejecución local de arranque y de pruebas: no se ejecuta código; solo se cuenta con la transcripción de docs/evidencia.md ('6 passed') y con los runs de CI.

## Hallazgos para la planilla

- No existe contrato OpenAPI, AsyncAPI ni proto en el árbol del commit calificado 0a58de8.
- El ADR-0001 descarta explícitamente una API pública, de modo que en esta entrega no hay artefacto de contrato que versionar.
- El workflow .github/workflows/ci.yml solo instala dependencias y ejecuta pytest; no hay paso de contrato ni de escáner estático.
- No hay sonar-project.properties ni URL pública de análisis con Quality Gate.
- Todos los runs revisados terminan en success; no hay ningún run en rojo en el historial consultado.
- El C4 nivel 2 etiqueta protocolos (HTTP, llamada interna) pero ningún formato de datos.
- docs/correcciones.md enlaza docs/correcciones-feedback.md, ruta que no existe en el árbol.
- Se versionan archivos compilados .pyc bajo src/ y tests/.
