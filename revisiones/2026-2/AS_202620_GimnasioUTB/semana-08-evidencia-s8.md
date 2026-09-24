# Semana 8 · Despliegue reproducible, CI y observabilidad · GimnasioUTB

> Revisión preliminar. El estado definitivo se fijará con el último commit de `main` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `0e3aeb5` en `origin/main` (2026-09-20T23:29:29-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación de URL | 2026-09-24T08:10:25-05:00 |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md` solo declara `http://localhost:3000`; la mención a Render no incluye URL. | No cumple | No hubo destino público para consultar. |
| Health check consultable | `src/server.js` implementa GET `/health`, pero únicamente se documenta su uso en localhost. | No cumple | La ruta existe, pero no es consultable desde fuera sin una URL desplegada. |
| Infraestructura como código versionada en el repositorio | No hay `Dockerfile`, Compose, Terraform, manifiestos ni configuración declarativa de Render. | No cumple | El workflow de pruebas no recrea el entorno de despliegue. |
| El entorno se puede recrear siguiendo el README | `README.md` documenta Node.js ≥18, `npm install && npm start`, health check y `npm test`. | Cumple | Reproduce el backend local con persistencia en memoria. |
| Pipeline en verde sobre la rama principal | Run `CI` para `0e3aeb5`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/35561182912. | Cumple | Ejecuta pruebas base y de contrato. |
| Logs estructurados | `src/server.js` solo emite un `console.log` de arranque; no hay logger JSON ni campos estructurados. | No cumple | Falta configuración y ejemplo de log consultable. |
| Métrica consultable asociada a un escenario de calidad | arc42 propone latencia menor a 200 ms, pero no existe instrumentación ni endpoint de métricas. | No cumple | Un umbral documental no es una métrica consultable. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example` declara `PORT` y comenta un `DATABASE_URL`; el código solo consume `PORT` y no hay integración con secretos del proveedor. | No cumple | No se encontraron credenciales, pero la protección operativa aún no está implementada. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | arc42 fija Render free tier y presupuesto 0 USD, sin volumen, cálculo por pieza ni punto de ruptura. | No cumple | Falta la estimación exigida. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42_gimnasio_utb.md` no contiene sección 7. | No cumple | No hay vista de despliegue. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | §2.2, TC4: Render free tier y presupuesto del equipo de 0 USD. | Cumple | La restricción de costo está explícita; no se documenta una exigencia adicional de tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | arc42 resume un ADR-0002 de Render, pero no existe archivo ADR independiente ni alternativas descartadas. | No cumple | La decisión no satisface el formato pedido para cada plataforma. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación desde `ISCOUTB/AS_202620_GimnasioUTB`. |
| Estructura mínima presente | Cumple | Las seis rutas documentales mínimas están presentes. |
| Estado calificado identificable | Cumple | `origin/main`, `0e3aeb5`, 2026-09-20T23:29:29-05:00. |
| Nombres de ADR según la convención | No cumple | `docs/adr/ADR0001.md` no cumple `NNNN-titulo-en-kebab-case.md` y duplica el número 0001. |
| ADR aceptados no reescritos | No verificado | La duplicidad de ADR 0001 impide establecer una única decisión aceptada e inmutable. |
| `docs/ia.md` al día para la semana | No cumple | Último cambio en `a59410d` del 2026-09-13; no registra S8. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | CI en verde, pero sin scanner ni URL pública del Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Solo `.env.example`; ningún `.env` ni patrón de clave detectado. |
| Contribución de todos los integrantes | Cumple | Las identidades del historial consolidan los tres integrantes declarados. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `0e3aeb5` en `origin/main`.
- **Veredicto:** con no conformidades.
- Existe backend local reproducible, health check y CI en verde; no hay despliegue público, infraestructura como código, observabilidad ni estimación de costos completa.

## Recuento y nota sugerida

3 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente): 2.0 = 1 + 4 × (3/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Publicar la URL de Render y comprobar `/health` desde fuera.
- Versionar la definición de infraestructura y documentar secretos del entorno.
- Implementar logs estructurados y una métrica asociada a un escenario.
- Completar arc42 §7, estimación de costo y ADR de plataforma con alternativas.
