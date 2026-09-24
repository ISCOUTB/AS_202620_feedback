# Semana 8 · Despliegue reproducible, CI y observabilidad · LostVault

> Revisión preliminar. El estado definitivo se fijará con el último commit de `main` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `7bf515f` en `origin/main` (2026-09-20T23:55:34-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación de URL | 2026-09-24T08:10:25-05:00 |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | No hay URL de aplicación en `README.md`; `https://api.lostvault.example` del OpenAPI es un dominio de ejemplo. | No cumple | No se declaró una URL pública verificable. |
| Health check consultable | El árbol no contiene ruta de health check ni servidor desplegado. | No cumple | Se esperaba ruta y código HTTP observable. |
| Infraestructura como código versionada en el repositorio | No hay `Dockerfile`, Compose, Terraform, manifiestos ni archivo de proveedor. | No cumple | Los workflows compilan y prueban, pero no describen un entorno desplegado. |
| El entorno se puede recrear siguiendo el README | `README.md` documenta Flutter estable, `flutter pub get`, `flutter run -d chrome`, `flutter analyze` y `flutter test`. | Cumple | Reproduce la aplicación local y su corte vertical. |
| Pipeline en verde sobre la rama principal | Para `7bf515f`, `Flutter checks` y `Build` terminaron en `success`: https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/35562671798 y https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/35562671796. | Cumple | Los runs corresponden al hash elegible. |
| Logs estructurados | No hay configuración de logging JSON ni ejemplo de evento con campos. | No cumple | Falta observabilidad de logs. |
| Métrica consultable asociada a un escenario de calidad | `README.md` reconoce que las métricas de producción no están demostradas; no existe endpoint de métricas. | No cumple | Falta instrumento y vínculo a escenario. |
| Secretos fuera del código y tomados del entorno o del almacén | `.github/workflows/build.yml` consume `SONAR_TOKEN` desde `secrets.*`; no hay `.env` versionado ni patrones de credenciales. | Cumple | La evidencia cubre el secreto del pipeline; no existe aún configuración de aplicación desplegada. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | §2 solo exige servicios gratuitos; no hay cálculo por pieza ni punto de ruptura. | No cumple | Falta estimación mensual. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/` contiene secciones 1–6, 9, 10 y glosario; no existe sección 7. | No cumple | Falta vista de despliegue. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02_restricciones.md` exige servicios de nivel gratuito y declara ausencia de presupuesto. | Cumple | Fija costo cero; no se explicita una condición separada de tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | Los ADR 0001 y 0002 tratan estilo e integración; no hay ADR de plataforma. | No cumple | Falta decidir alojamiento y piezas operativas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación desde `ISCOUTB/AS_202620_LostVault`. |
| Estructura mínima presente | Cumple | Las seis rutas documentales mínimas están presentes. |
| Estado calificado identificable | Cumple | `origin/main`, `7bf515f`, 2026-09-20T23:55:34-05:00. |
| Nombres de ADR según la convención | Cumple | ADR 0001 y 0002 siguen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | Cumple | Cada ADR aceptado tiene una sola revisión en su ruta actual. |
| `docs/ia.md` al día para la semana | No cumple | Último cambio en `73abe8a` del 2026-09-20; no registra trabajo de S8. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | Scanner y run de Build en verde para `7bf515f`, pero no se aporta URL pública del Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin `.env` versionado ni patrones de claves detectados. |
| Contribución de todos los integrantes | Cumple | El historial contiene contribuciones atribuibles a los cuatro integrantes; los alias se consolidan cuando comparten evidencia. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `7bf515f` en `origin/main`.
- **Veredicto:** con no conformidades.
- El entorno local y ambos workflows son reproducibles, pero el proyecto no ofrece despliegue público, health check, IaC, observabilidad, estimación de costos ni vista de despliegue.

## Recuento y nota sugerida

4 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente): 2.3 = 1 + 4 × (4/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Definir plataforma, desplegar y publicar URL con health check.
- Versionar infraestructura y completar arc42 §7.
- Implementar logs estructurados y métrica consultable.
- Estimar costos y registrar las decisiones de plataforma en ADR.
