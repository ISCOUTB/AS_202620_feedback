# semana-07-evidencia-s7 · InvenTrack

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `d71c5b7` en `origin/main` (2026-09-15T11:15:51-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de d71c5b7 sin archivos openapi/swagger/asyncapi (.yaml/.json) ni .proto; solo routers en app/productos/infrastructure/router.py y app/inventario/infrastructure/router.py. | No cumple | Se esperaba el contrato versionado; no existe en HEAD. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No hay archivo de contrato en d71c5b7 del cual citar rutas o esquemas. | No cumple | No es posible citar fragmento de paths ni schemas. |
| Correspondencia entre el contrato y la API implementada | Existen rutas en app/productos/infrastructure/router.py y app/inventario/infrastructure/router.py, pero ningún contrato para cruzarlas. | No cumple | No verificable en ninguno de los dos sentidos. |
| Versión de la API declarada y con historial | Sin archivo de contrato, el git log del contrato no aplica (árbol d71c5b7). | No cumple | No hay campo de versión ni historial del contrato. |
| Prueba de contrato presente | tests/ de d71c5b7 solo contiene test_health.py, tests/productos/* y tests/inventario/*; ninguna prueba de contrato (schemathesis/pact/dredd). | No cumple | Se esperaba la ruta de la prueba de contrato. |
| El pipeline ejecuta la prueba de contrato | Único workflow en el árbol: .github/workflows/test.yml; no hay prueba de contrato que invocar y no se aportan runs_ci. | No cumple | Faltan la línea del workflow y la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | No hay runs_ci ni evidencia del cambio incompatible aportada por el equipo. | No verificado | Queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003-integracion-productos-inventario-via-puertos-de-aplicacion.md adopta la llamada síncrona (alternativa 4) frente a eventos de dominio (alternativa 3) descartada, ligada a ESC-01/ESC-02 y a consecuencias de acoplamiento. | Cumple | Fecha 2026-09-13; alternativa descartada y consecuencias explícitas. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42-template-EN.md existe y el README declara la sección 6 Runtime View con diagramas de secuencia, pero el fragmento aportado se corta antes de esa sección. | No verificado | Haría falta citar la sección 6 o el archivo completo. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/containers.md: las flechas de actores usan 'HTTPS' y la de notificaciones 'SMTP' sin formato; solo 'Web -- HTTPS/REST --> Api' nombra protocolo y formato. | No cumple | Falta el formato en varias flechas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_InvenTrack en la organización ISCOUTB, visible:true, con historial de commits. | Cumple | 8 firmas de commit que consolidan 5 identidades de correo; no se atribuyen cuentas a personas por parecido de nombre. |
| Estructura mínima | d71c5b7 incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | arc42 en un único Markdown; desviación de ruta, no ausencia. |
| Convenciones de ADR | docs/adr/0001-*.md, 0002-*.md y 0003-*.md en kebab-case, con contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | No se aportó el historial por archivo para detectar ADR reescritos. |
| La tabla de aspectos | docs/aspectos.md con las ocho columnas (ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia) y filas ASP-01 y ASP-02 con enlaces. | Cumple | Dos aspectos declarados; todos sus eslabones apuntan a artefactos existentes. |
| Registro de uso de IA | docs/ia.md con columna 'Rechazado / motivo' y 12 revisiones entre 2026-08-09 y 2026-09-13. | Cumple | El crecimiento del archivo es sostenido a lo largo del semestre. |
| README | README.md con descripción, índice que incluye 'Cómo ejecutar el esqueleto'; docs/adr/0001 cita el arranque en un solo comando (uvicorn app.main:app). | Cumple | El fragmento aportado está truncado; la sección de pruebas no se pudo citar textualmente. |
| Pipeline y análisis estático | sonar-project.properties existe en la raíz, pero docs/ia.md (2026-09-13) registra que el paso de SonarCloud se retiró del workflow por falta del secreto; solo hay .github/workflows/test.yml. | No cumple | Faltan la línea que invoca el scanner, la URL del run exitoso y la URL pública del análisis con Quality Gate. |
| Secretos | Evidencia sobre d71c5b7: 'secretos': '(sin coincidencias)' y 'envs_versionados': []. | Cumple | Sin credenciales ni .env versionados. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `d71c5b716e0e5bc92820264d558891e73a5a8e6b 2026-09-15T11:15:51-05:00 fix: corregir error tipográfico`
- **Veredicto**: con pendientes
- Resumen: En la punta d71c5b7 (main, 2026-09-15, subida previa al cierre) el proyecto mantiene arquitectura documentada, ADR-0003 de integración y CI de pruebas, pero no existe contrato de API ni prueba de contrato, y el análisis estático sigue fuera del pipeline.

Pendientes que siguen abiertos:
- Paso de SonarCloud retirado del CI (docs/ia.md, 2026-09-13) sin restituir a HEAD.
- Contrato de API y prueba de contrato de la semana 7 ausentes.
- Formato ausente en varias flechas del C4 nivel 2.

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Que la prueba de contrato falle ante un cambio incompatible: sin runs_ci ni evidencia aportada.
- Contenido de la sección 6 del arc42: el fragmento aportado se corta antes de esa sección.
- Ejecución del pipeline: no se aportaron runs_ci con nombre, conclusión y URL.

## Hallazgos para la planilla

- No existe contrato OpenAPI/AsyncAPI/proto en el árbol de d71c5b7.
- No hay prueba de contrato ni invocación de una en el pipeline.
- El paso de SonarCloud fue retirado del CI (docs/ia.md, 2026-09-13) y sigue sin restituirse a HEAD.
- El C4 nivel 2 no etiqueta el formato en todas las flechas.
- ADR-0003 sí justifica la integración síncrona frente a la alternativa de eventos.
- Sin commits posteriores al cierre; entrega registrada el 2026-09-15, antes del cierre del 2026-09-21.
