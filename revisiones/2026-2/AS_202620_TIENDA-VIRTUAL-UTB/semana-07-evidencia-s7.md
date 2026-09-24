# semana-07-evidencia-s7 · Tienda virtual UTB

> Revisión definitiva corregida después del cierre. El informe preliminar evaluó un borrador; esta versión usa el último commit de `origin/main` anterior al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `69aa82d` en `origin/main` (2026-09-20T09:34:49-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | revisión académica local sobre evidencia Git y GitHub Actions |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | `docs/api/openapi.json:2` declara OpenAPI 3.1.0 y el archivo está versionado desde `0416e62`. | Cumple | Es el contrato generado de la API implementada; `docs/openapi/tienda-virtual.yaml` queda como contrato de diseño futuro. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | `docs/api/openapi.json:8,34,58-104` define `/catalog/products`, `/health` y los esquemas `HealthOut` y `ProductOut`. | Cumple | Las respuestas de ambas rutas enlazan modelos tipados. |
| Correspondencia entre el contrato y la API implementada | `backend/app/main.py:45-59` implementa `/health` y registra el router; `backend/app/modules/catalog/router.py:10-13` implementa `/catalog/products`. `backend/tests/contract/test_openapi.py:39` exige igualdad entre `app.openapi()` y el contrato. | Cumple | Se cotejan las dos rutas del contrato y la igualdad automatizada impide rutas extra no documentadas. |
| Versión de la API declarada y con historial | `docs/api/openapi.json:5` y `backend/app/main.py:45` declaran `0.2.0`; `git log -- docs/api/openapi.json` registra `0416e62` y su antecedente documental `f4602a3`. | Cumple | La versión coincide entre contrato y proveedor y la ruta tiene historial Git. |
| Prueba de contrato presente | `backend/tests/contract/test_openapi.py:34-67` valida la especificación, la igualdad con FastAPI, respuestas reales y mutaciones incompatibles. | Cumple | Usa OpenAPI Spec Validator y JSON Schema Draft 2020-12. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/tests.yml:24-33` ejecuta `python -m pytest tests/contract ...` y publica el JUnit; run exacto del hash: https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/35516931181 | Cumple | El run existe y concluye en fallo; esa condición se registra además como no conformidad transversal. |
| Evidencia de que la prueba falla ante un cambio incompatible | `backend/tests/contract/test_openapi.py:57-67` elimina `name` o cambia `price_cents` a texto y exige `ValidationError` al validar la respuesta contra el contrato. | Cumple | La mutación negativa demuestra de forma estática que el validador rechaza dos rupturas del proveedor; no se confunde con una prueba que pasa sin ejercer el cambio. |
| ADR de la estrategia de integración ligado a un escenario | `docs/adr/0002-contrato-integracion-http.md:7-24,76-88` compara HTTP síncrono, mensajería y HTTP sin contrato, y documenta consecuencias. No enlaza ningún escenario de calidad concreto. | No cumple | Se esperaba un identificador y vínculo a un escenario medible que justificara la elección y sus consecuencias de acoplamiento. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/arc42-template-EN.md:350-404` contiene secuencias para arranque/siembra y navegación del catálogo entre Compose, FastAPI, PostgreSQL y Next.js. | Cumple | Los dos flujos describen comportamiento existente y puntos de fallo. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/container.md:28-32` etiqueta web→API como REST/JSON sobre HTTP y API→base como SQL/SQLAlchemy, pero las tres relaciones persona→web solo indican HTTPS. | No cumple | HTTPS declara protocolo, no el formato; cada flecha debe explicitar ambos según la ficha. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB`, accesible por clonación sin autenticación. | Cumple | Nombre y organización coinciden con `EQUIPOS.md`. |
| Estructura mínima presente | El árbol de `69aa82d` contiene `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas exigidas están versionadas. |
| Estado calificado identificable | `origin/main`, `69aa82d`, 2026-09-20T09:34:49-05:00; es el último commit anterior al cierre. | Cumple | La punta actual coincide con el estado calificado. |
| Nombres de ADR según la convención | `docs/adr/0001-monolito-modular.md` y `docs/adr/0002-contrato-integracion-http.md`. | Cumple | Ambos siguen `NNNN-kebab-case.md`. |
| ADR aceptados no reescritos | El ADR 0001 tiene dos cambios: creación en `f4602a3` y reescritura de trazabilidad en `e8ae57d`. | No cumple | El contrato exige crear un ADR sucesor cuando cambia una decisión aceptada, no reescribir el anterior. |
| `docs/ia.md` al día para la semana | `docs/ia.md:7,19,31` registra la actividad de S7, propuestas descartadas, motivo y validación humana; el archivo fue actualizado en el periodo. | Cumple | Distingue pruebas locales de evidencia de despliegue o CI. |
| Pipeline, SonarCloud y Quality Gate públicos | El run 35516931181 del hash calificado concluye en fallo; el workflow no invoca SonarCloud y no existe URL pública del análisis con Quality Gate. | No cumple | CI no está verde y faltan las evidencias públicas de SonarCloud requeridas desde S6. |
| Sin credenciales en el repositorio ni en el historial | No hay `.env` versionado y el barrido estático del hash no encontró credenciales en código propio. | Cumple | El entorno de terceros versionado se excluyó del juicio sobre código propio, pero debe retirarse por higiene. |
| Contribución de todos los integrantes | `git shortlog -sne 69aa82d` consolida cuatro grupos de identidad; corresponden a las cuatro cuentas declaradas en `EQUIPOS.md`. | Cumple | Dos firmas pertenecen al mismo grupo y se contabilizan una sola vez. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `69aa82d36bd9f8efac8fc0541d58c07204724e91 2026-09-20T09:34:49-05:00 Evidencia S7, termino de documentacion, actualizacion de diagramas, correccion de errores`.
- **Veredicto**: entrega S7 mayormente completa, con dos no conformidades de ficha y el pipeline transversal en rojo.
- El contrato OpenAPI, la correspondencia con FastAPI, las pruebas de contrato, la mutación negativa y los flujos de arc42 están presentes en la punta actual.

Pendientes que siguen abiertos:
- Vincular el ADR de integración a un escenario de calidad concreto y medible.
- Completar protocolo y formato en las tres flechas de actores hacia el cliente web del C4 nivel 2.
- Corregir el pipeline, integrar SonarCloud y publicar el análisis con Quality Gate.
- Evitar reescribir ADR aceptados y retirar del repositorio el entorno Python de terceros.

## Recuento y nota sugerida

8 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decisión del profesor): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- No quedan filas de la ficha en estado No verificado: las dos no conformidades se comprobaron directamente en el ADR y el C4.
- El resultado preciso de cada job del run fallido no se consultó; la API pública sí confirma la conclusión `failure` para el hash calificado.

## Hallazgos para la planilla

- El informe preliminar evaluó `dea5bc9`; el estado correcto al cierre es `69aa82d`.
- Ocho filas de la ficha cumplen; el ADR carece de escenario de calidad concreto y tres flechas del C4 solo declaran protocolo.
- El workflow ejecuta las pruebas de contrato, pero el run exacto del hash calificado está en rojo.
- SonarCloud no tiene configuración, ejecución ni Quality Gate público verificables.
