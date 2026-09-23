# semana-08-evidencia-s8 · Tienda virtual UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `69aa82d` en `origin/main` (2026-09-20T09:34:49-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | La entrega no aporta URL del sistema; no se pudo ejecutar curl -sS -o /dev/null -w 'http=%{http_code} tiempo=%{time_total}s'. | No verificado | Sin URL no hay comprobación externa ni hora exacta de verificación que registrar. |
| Health check consultable | El equipo no declara ninguna ruta de health check en la evidencia aportada. | No verificado | Hace falta la ruta declarada para probar su código de respuesta. |
| Infraestructura como código versionada en el repositorio | En el árbol de 69aa82d sólo se ven .dockerignore y .github/workflows/tests.yml, y el listado aparece truncado. | No verificado | No se puede afirmar ausencia de Dockerfile, compose, terraform o helm; falta el listado completo (comando de ls-tree\|grep). |
| El entorno se puede recrear siguiendo el README | README.md no aparece en la parte visible del árbol de 69aa82d (listado truncado). | No verificado | Sin README no se puede comprobar el arranque con un solo comando ni los requisitos previos. |
| Pipeline en verde sobre la rama principal | No hay runs_ci en la evidencia; lo único visible es el archivo .github/workflows/tests.yml. | No verificado | Haría falta la URL y conclusión del último run sobre main (api.github.com/repos/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs). |
| Logs estructurados | No se aporta archivo de configuración de logging ni línea de ejemplo en formato de campos. | No verificado | Falta el grep de structlog/winston/pino/logback/logging.config y una línea de salida real. |
| Métrica consultable asociada a un escenario de calidad | No se nombra ninguna métrica ni el escenario de calidad al que corresponde. | No verificado | Una métrica de sistema sin escenario asociado se anotaría como incompleta. |
| Secretos fuera del código y tomados del entorno o del almacén | El barrido del contrato en 69aa82d sólo devuelve coincidencias dentro de .security-tools (código de terceros) y no se observa .env.example. | No verificado | Falta comprobar variables de entorno declaradas y que el despliegue las tome de la configuración del proveedor. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No se aporta documento de estimación de costo mensual. | No verificado | Debe partir del volumen del escenario del equipo y señalar dónde se rompe la capa gratuita. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | No se observa ninguna ruta docs/arc42/07* en la parte visible del árbol de 69aa82d. | No verificado | Falta el despliegue con una caja por pieza y su ubicación de ejecución. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | No se observa ninguna ruta docs/arc42/02* en la parte visible del árbol de 69aa82d. | No verificado | Faltan el límite de costo y, si aplica, la restricción de «sin tarjeta» como restricciones. |
| Un ADR por decisión de plataforma, con alternativa descartada | No se observan archivos de docs/adr/ correspondientes a esta semana en el árbol visible. | No verificado | Se espera un ADR por pieza decidida, cada uno con su alternativa descartada y capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_TIENDA-VIRTUAL-UTB, público (visible: true) y rama principal origin/main, hash 69aa82d. | Cumple | 5 identidades de git que consolidan en 4 personas (dos comparten la misma cuenta de correo); no se atribuye por nombre ni se pudo verificar la membresía en la organización. |
| Estructura mínima | El árbol visible de 69aa82d está truncado y sólo muestra archivos de sistema y el entorno vendorizado .security-tools. | No verificado | No se observan README.md ni docs/(arc42\|adr\|c4\|aspectos\|ia), pero el truncamiento impide afirmar ausencia. |
| Convenciones de ADR | No hay archivos de docs/adr/ en la parte visible del árbol del hash calificado. | No verificado | Haría falta el listado de docs/adr/ y el log de cada ADR para comprobar numeración y no reescritura. |
| La tabla de aspectos | No se observa docs/aspectos.md en el árbol visible de 69aa82d. | No verificado | Falta la tabla con las ocho columnas y la cadena aspecto-requisito-C4-ADR-código-pruebas-evidencia. |
| Registro de uso de IA | No se observa docs/ia.md en el árbol visible de 69aa82d. | No verificado | Falta el registro con lo aceptado y lo rechazado con su motivo técnico. |
| README | README.md no aparece en la parte visible del árbol de 69aa82d. | No verificado | Falta el arranque con un solo comando y el procedimiento de prueba. |
| Pipeline y análisis estático | Existe .github/workflows/tests.yml, pero no hay runs_ci aportados ni URL pública de SonarCloud. | No verificado | Se requiere la URL del run en verde sobre main y el estado del Quality Gate en la organización isco-utb. |
| Secretos | El barrido sobre 69aa82d no muestra credenciales reales: todas las coincidencias están en .security-tools/python/Lib/site-packages (terceros). | No verificado | Falta confirmar que no hay .env versionado y que las variables llegan desde el entorno o el almacén del proveedor. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `69aa82d36bd9f8efac8fc0541d58c07204724e91 2026-09-20T09:34:49-05:00 Evidencia S7, termino de documentacion, actualizacion de diagramas, correccion de errores`
- **Veredicto**: con pendientes
- Resumen: Sobre 69aa82d (origin/main, 2026-09-20, anterior al cierre) no se pudo verificar ningún criterio de la ficha: no hay URL, no hay runs de CI y el árbol visible está truncado. Sólo se confirmó la identidad del repositorio, 1 de 20 criterios (0 de 12 en la ficha, 1 de 8 en la transversal).

Pendientes que siguen abiertos:
- URL pública del sistema y health check con hora de verificación.
- Infraestructura como código versionada y README reproducible.
- Pipeline en verde sobre main con URL del run y evidencia pública de SonarCloud.
- Logs estructurados, métrica con escenario y estimación de costo con supuestos.
- arc42 secciones 2 y 7, ADRs de plataforma, docs/aspectos.md, docs/ia.md y diagramas C4.
- Retirar del versionado el entorno de terceros .security-tools.

## Recuento y nota sugerida

0 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema y su health check: no se aportó URL ni ruta declarada; hace falta ejecutar curl y registrar la hora exacta.
- Infraestructura como código: el listado del árbol está truncado; hace falta el listado completo o las rutas de Dockerfile/compose/terraform/helm/Procfile.
- README y estructura docs/: no visibles por el truncamiento; hace falta el listado de rutas de la estructura mínima.
- Pipeline: sin runs_ci; hace falta la URL y la conclusión del último run sobre la rama principal.
- Logs estructurados: falta la configuración de logging citada y una línea de ejemplo con campos.
- Métrica consultable: falta el nombre de la métrica y el escenario de calidad asociado.
- Secretos: faltan .env.example y las referencias a secretos en el workflow o en la configuración del proveedor.
- Estimación de costo mensual: falta el documento con volumen supuesto, cálculo por pieza y punto de ruptura.
- arc42 secciones 2 y 7 y ADRs de plataforma: no visibles en el árbol; faltan las rutas docs/arc42/02*, docs/arc42/07* y docs/adr/.

## Hallazgos para la planilla

- La entrega no aporta URL del sistema desplegado, así que no hubo nada que abrir desde fuera de la red.
- No se aportaron runs de CI: lo único visible es el archivo .github/workflows/tests.yml.
- El árbol visible de 69aa82d está truncado y dominado por un entorno Python vendorizado en .security-tools.
- Ese entorno versionado incluye miles de archivos de terceros e incluso binarios .exe, lo que infla el repositorio y ensucia el barrido de secretos.
- No se observan artefactos de S8 (infraestructura como código, health, métrica, costo, ADR de plataforma) en lo visible del árbol.
- Contribuciones: 5 identidades de git que consolidan en 4 personas, coincidente con los 4 integrantes declarados.
- El hash calificado 69aa82d es del 2026-09-20, anterior al cierre del 2026-09-28, sin datos de commits posteriores.
- El barrido de secretos no encontró credenciales reales; todas las coincidencias pertenecen a librerías de terceros.
