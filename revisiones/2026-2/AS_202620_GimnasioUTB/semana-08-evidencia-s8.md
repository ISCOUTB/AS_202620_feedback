# Semana 8 · Despliegue reproducible, CI y observabilidad · GimnasioUTB

> Revisión definitiva: hash `a71bc7583b67cd4f5eca11dd6d356f7d08d1cdc7`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `main`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `a71bc75` en `origin/main` (2026-09-27T21:55:06-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md:29` solo nombra Render como intención y `README.md:39` publica `http://localhost:3000`; no hay URL pública. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. |
| Health check consultable | `src/server.js:11` implementa `GET /health`, pero no hay URL pública bajo la cual consultarlo. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. |
| Infraestructura como código versionada en el repositorio | El árbol solo contiene `.github/workflows/ci.yml`; no hay `Dockerfile`, Compose, Terraform, manifiestos, `render.yaml` ni `Procfile`. | No cumple | El workflow de pruebas no describe el entorno de despliegue. |
| El entorno se puede recrear siguiendo el README | `README.md:36` (`npm install && npm start`) y `README.md:49` (`npm test`), con Node.js ≥ 18 declarado. | Cumple | Reproduce el backend local con persistencia en memoria. |
| Pipeline en verde sobre la rama principal | Run `CI` en `main` para `a71bc75`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/36371651931. | Cumple | Ejecuta pruebas unitarias, de integración y de contrato. |
| Logs estructurados | `src/server.js:29` solo emite un `console.log` de arranque; no hay logger JSON ni campos. | No cumple | Falta archivo de configuración y ejemplo de línea. |
| Métrica consultable asociada a un escenario de calidad | El arc42 define una medida de rendimiento (p95 ≤ 200 ms) como texto, pero no hay instrumentación ni endpoint de métricas. | No cumple | Un umbral documental no es una métrica consultable. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example:1` solo declara `PORT`; `ci.yml` no referencia `secrets.*` y no hay almacén de secretos ni despliegue que los consuma. | No cumple | No se encontraron credenciales, pero tampoco hay gestión de secretos del proveedor. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/arc42/arc42_gimnasio_utb.md:82` fija Render free tier y presupuesto 0 USD, pero no presenta el costo del entorno desplegado. `docs/taller.md` §7 sí trae volumen (120.000 invocaciones/mes), costo por pieza y punto de ruptura, aunque pertenece al taller de despliegue, que es un entregable separado de esta evidencia S8. | No cumple | Falta la estimación exigida en la evidencia S8; el cálculo de `docs/taller.md` §7 se califica aparte, con el taller. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42_gimnasio_utb.md` salta de `## 6. Runtime View` (`:195`) a `## 8. Cross-cutting Concepts` (`:251`); no existe sección 7. | No cumple | No hay vista de despliegue. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42_gimnasio_utb.md:82` (TC4): Render free tier y presupuesto del equipo de 0 USD. | Cumple | El límite de costo es explícito; el equipo no documenta una exigencia adicional de tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | El arc42 resume un `ADR-0002` dentro de `## 9` (`docs/arc42/arc42_gimnasio_utb.md:294`), sin archivo propio en `docs/adr/` ni alternativas descartadas. | No cumple | La decisión de plataforma no cumple el formato pedido. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | `ISCOUTB/AS_202620_GimnasioUTB`, clonado sin autenticación. |
| Estructura mínima presente | Cumple | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` presentes. |
| Estado calificado identificable | Cumple | `origin/main`, `a71bc75`, 2026-09-27T21:55:06-05:00. |
| Nombres de ADR según la convención | No cumple | `docs/adr/ADR0001.md` no sigue `NNNN-titulo-en-kebab-case.md` y duplica el número 0001 de `docs/adr/0001-arquitectura-hexagonal.md`. |
| ADR aceptados no reescritos | No cumple | El ADR 0001, aceptado en `92f4a53`, fue editado después en `c271073`, `b556737`, `59b6d3e` y `47a18d0` (2026-08-30), sin ADR de reemplazo declarado. |
| `docs/ia.md` al día para la semana | No cumple | Último cambio en `a59410d` (2026-09-13); no registra S7 ni S8. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI en verde, pero no hay `sonar-project.properties`, scanner en el workflow ni URL pública del Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin `.env` versionado ni patrones de credenciales; solo `.env.example`. |
| Contribución de todos los integrantes | Cumple | `shortlog -sne` consolida las tres personas declaradas (una con dos identidades y un correo institucional compartido). |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `e6a7f58` en `origin/main` (2026-09-28T01:32:10-05:00).
- **Commits posteriores al cierre:** `201a8cf` (persistencia PostgreSQL y concurrencia), `b5a4fce` (manejo de errores), `ddb27d4` (composición del servidor y observabilidad), `3fae092` (documentación), `5213f49` (pruebas de integración y health) y `e6a7f58` (merge).
- **Veredicto:** con no conformidades. El backend local, el health check y el CI siguen en verde; el despliegue público, la infraestructura como código, los logs estructurados, la métrica y la estimación de costo no están versionados en el estado calificado. Lo posterior al cierre apunta a cerrar parte de esa deuda y no altera la matriz.

## Recuento y nota sugerida

3 de 10 criterios graduables Cumple.

**propuesta provisional al docente — `nota = 1 + 4 × (3/10) = 2.2`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- URL del sistema accesible desde fuera de la red de la universidad.
- Health check consultable.

Ambas quedan pendientes de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El README no declara una URL pública para probarlas.

## Hallazgos para la planilla

- Sin infraestructura como código versionada (ni `Dockerfile`, ni Compose, ni definición de Render): el entorno de despliegue no es recreable desde el repositorio.
- Sin logs estructurados ni métrica consultable asociada a un escenario de calidad.
- Sin estimación de costo mensual con supuestos ni punto de ruptura de la capa gratuita.
- Falta la sección 7 de arc42 (vista de despliegue) y un ADR independiente por decisión de plataforma con alternativa descartada.
- Transversal: `docs/adr/ADR0001.md` fuera de convención y duplicando el número 0001; ADR 0001 reescrito tras su aceptación; `docs/ia.md` sin la semana; SonarCloud ausente.
