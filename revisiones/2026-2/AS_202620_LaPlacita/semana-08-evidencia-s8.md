# Semana 8 · Despliegue reproducible, CI y observabilidad · LaPlacita

> Revisión preliminar. El estado definitivo se fijará con el último commit de `master` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `03b4e73` en `origin/master` (2026-09-21T20:20:16-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación de URL | 2026-09-24T08:10:25-05:00 |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md` declara expresamente que Railway está documentado, pero no desplegado; solo publica `http://localhost:3000`. | No cumple | No existe URL pública para comprobar. |
| Health check consultable | `app/api/v1/health/route.js` implementa GET `/api/v1/health`, pero solo se documenta en localhost. | No cumple | La ruta no pudo consultarse desde fuera por ausencia de despliegue. |
| Infraestructura como código versionada en el repositorio | `Dockerfile` multietapa construye Next.js con Node 22 y expone el puerto 3000. | Cumple | Describe la imagen de producción; falta archivo declarativo específico del proveedor. |
| El entorno se puede recrear siguiendo el README | `README.md` documenta Node 22, `npm ci`, `npm run dev`, build/start de producción y health check. | Cumple | El procedimiento y el Dockerfile permiten recrear el proceso local. |
| Pipeline en verde sobre la rama principal | El run de `03b4e73` terminó en `failure`: https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/35675386084. | No cumple | La API pública de Actions confirma que todos los runs recientes listados fallan. |
| Logs estructurados | El código usa `console.log` en `src/corte-vertical.js`; no hay logger JSON ni esquema de campos. | No cumple | Se esperaba configuración y ejemplo de línea estructurada. |
| Métrica consultable asociada a un escenario de calidad | No existe endpoint o exportador de métricas vinculado a ESC-01…ESC-05. | No cumple | Las pruebas de aislamiento no son una métrica consultable del entorno. |
| Secretos fuera del código y tomados del entorno o del almacén | `.github/workflows/ci.yml` usa `secrets.SONAR_TOKEN` y `secrets.GITHUB_TOKEN`; ADR-0003 define variables de Railway fuera del repositorio. | Cumple | No hay `.env` versionado ni patrones de credenciales detectados. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | ADR-0003 menciona tier académico/gratuito, sin volumen, cálculo por pieza ni punto de ruptura. | No cumple | Falta la estimación pedida por la ficha. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42-template-EN.md` salta de §6 a §8; no contiene vista de despliegue. | No cumple | El C4 de contenedores no sustituye la vista del entorno. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | §2 incluye RES-01 sobre no almacenar tarjeta, pero no fija límite monetario ni condición de cuenta sin tarjeta para el hosting. | No cumple | Falta la restricción económica de la plataforma. |
| Un ADR por decisión de plataforma, con alternativa descartada | ADR-0003 combina Railway y SonarCloud en un solo registro, aunque sí compara VPS, Render, Fly.io y Heroku. | No cumple | La ficha pide un ADR por cada decisión de plataforma, no una decisión combinada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación desde `ISCOUTB/AS_202620_LaPlacita`. |
| Estructura mínima presente | Cumple | Las seis rutas documentales mínimas están presentes. |
| Estado calificado identificable | Cumple | `origin/master`, `03b4e73`, 2026-09-21T20:20:16-05:00. |
| Nombres de ADR según la convención | Cumple | ADR 0001–0008 siguen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | No verificado | Varios ADR aceptados tienen más de una revisión; falta ubicar el commit de aceptación para decidir si hubo reescritura. |
| `docs/ia.md` al día para la semana | Cumple | Actualizado en `e578b20` del 2026-09-21 con decisiones y rechazos técnicos. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | Scanner configurado, pero el run de `03b4e73` falla y no hay URL pública de Quality Gate aportada. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin `.env` versionado ni coincidencias de patrones de claves. |
| Contribución de todos los integrantes | Cumple | Cuatro identidades consolidadas para los cuatro integrantes declarados. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `03b4e73` en `origin/master`.
- **Veredicto:** con no conformidades.
- El Dockerfile, el README y la gestión de secretos dan una base reproducible, pero Railway sigue sin desplegar, el pipeline falla y no hay observabilidad ni estimación de costos.

## Recuento y nota sugerida

3 de 12 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente): 2.0 = 1 + 4 × (3/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Completar el despliegue y publicar URL más health check.
- Corregir el pipeline hasta dejar el hash elegible en verde.
- Implementar logs estructurados y métrica consultable.
- Añadir arc42 §7, estimación de costo y separar los ADR de plataforma.
