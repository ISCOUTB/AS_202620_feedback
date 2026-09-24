# Semana 07 · Evidencia S7 · PideUtb

> Revisión definitiva auditada localmente. Se corrigieron el hash y el resultado automático con la evidencia disponible al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `3d78106` en `origin/master` (2026-09-20T22:24:21-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato ejecutable versionado | `docs/api/openapi.yaml:13-17` y `docs/api/asyncapi.yaml`. | Cumple | OpenAPI 3.1.0 y AsyncAPI 3.0.0. |
| Rutas y esquemas de datos | `docs/api/openapi.yaml:77-361` contiene seis rutas y `components.schemas`. | Cumple | Peticiones y respuestas referencian esquemas. |
| Correspondencia contrato–API | `menu/router.py:18-34`, `pedidos/router.py:12-35` y `pagos/router.py:18-39` corresponden con las rutas del contrato; `test_contrato_api.py` compara también la API generada. | Cumple | Cotejo bidireccional automatizado. |
| Versión e historial | `info.version: 1.0.0`; historial en `docs/api/historial/`; alta en `3d69442`. | Cumple | Versión congelada y política de evolución. |
| Prueba de contrato presente | `backend/tests/test_contrato_api.py`, `test_compatibilidad_contrato.py` y `test_expectativas_consumidor.py`. | Cumple | Comprueban proveedor, compatibilidad y consumidor. |
| Pipeline ejecuta la prueba | `.github/workflows/ci.yml:47-48,72-120`; run verde del estado base de entrega: https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/35557330685 | Cumple | Los commits posteriores al run modifican solo evidencia documental. |
| Falla ante cambio incompatible | Run #22 en rojo: https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/35557297196; detalle en `docs/api/README.md:81-190`. | Cumple | Oasdiff y las pruebas detectaron la rotura deliberada. |
| ADR de integración ligado a escenario | `docs/adr/0003-estrategia-integracion.md:24-207` vincula ESC-05/ESC-04, descarta extremos síncrono y asíncrono y expone consecuencias. | Cumple | Acoplamiento temporal tratado explícitamente. |
| arc42 sección 6 | `docs/arc42/arc42.md:391-631` documenta flujos, protocolos, formatos y modos de fallo. | Cumple | Incluye pedido, pago y consulta de estado. |
| C4 nivel 2 etiquetado | `docs/c4/nivel2-contenedores.md:27-51` etiqueta todas las relaciones con protocolo, formato y modo. | Cumple | HTTPS/JSON, PostgREST y webhook firmado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia u observación |
|---|---|---|
| Repositorio público con nombre de convención | Cumple | Clon público `ISCOUTB/AS_202620_PideUtb`. |
| Estructura mínima | Cumple | Las seis rutas mínimas están presentes. |
| Estado calificado identificable | Cumple | `origin/master`, `3d78106`, fecha y cierre consignados. |
| Nombres de ADR | Cumple | ADR 0001–0003 cumplen la convención. |
| ADR aceptados sin reescribir | Cumple | Las decisiones permanecen en historial. |
| `docs/ia.md` al día | Cumple | Registro S7 con aceptaciones, correcciones y rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos | Cumple | Scanner en `ci.yml:182-196`, run https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/35556118369 y panel público https://sonarcloud.io/summary/overall?id=ISCOUTB_AS_202620_PideUtb |
| Sin credenciales expuestas | Cumple | Variables sensibles tomadas del entorno y `SONAR_TOKEN` desde GitHub Secrets. |
| Contribución de todo el equipo | Cumple | Tres identidades consolidadas para tres integrantes. |

## Estado global del proyecto

La punta actual `9db30b9` añade evidencia documental después del cierre; no cambia la matriz definitiva. S7 queda completamente demostrada en el estado calificado.

## Recuento y nota sugerida

**10 de 10 criterios Cumple.**

**Nota sugerida (propuesta al docente; la nota final se fija en Moodle): 5.0 = 1 + 4 × (10/10).**
