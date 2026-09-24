# Semana 8 · Despliegue reproducible, CI y observabilidad · PideUtb

> Revisión preliminar. El estado definitivo se fijará con el último commit de `master` anterior o igual al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `9db30b9` en `origin/master` (2026-09-21T10:25:39-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación de URL | 2026-09-24T13:14:11Z |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | El contrato declara `https://pideutb.vercel.app`; la raíz respondió HTTP 404. | No cumple | La dirección es pública, pero no sirve el sistema. |
| Health check consultable | `https://pideutb.vercel.app/health` respondió HTTP 404. | No cumple | Comprobación externa, sin ejecutar el repositorio. |
| Infraestructura como código versionada en el repositorio | No se encontró IaC o descriptor de Vercel que reproduzca el despliegue. | No cumple | El workflow no describe la infraestructura. |
| El entorno se puede recrear siguiendo el README | El README no permite recrear el entorno público declarado. | No cumple | Faltan plataforma, variables y pasos verificables. |
| Pipeline en verde sobre la rama principal | Run exitoso de `9db30b9`: https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/35619185088 | Cumple | CI público del estado revisado. |
| Logs estructurados | No se halló configuración de logs estructurados ni ejemplo consultable. | No cumple | Falta formato con campos. |
| Métrica consultable asociada a un escenario de calidad | No existe métrica desplegada y enlazada a un escenario. | No cumple | Falta fuente, consulta y umbral. |
| Secretos fuera del código y tomados del entorno o del almacén | `backend/app/pagos/service.py:30` incluye el fallback `secreto-de-desarrollo`. | No cumple | La configuración sensible debe fallar de forma segura. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | No se encontró estimación verificable. | No cumple | Faltan supuestos y punto de ruptura. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | La sección 7 no representa el despliegue público real. | No cumple | Faltan piezas y ubicaciones concretas. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | No se documentan conjuntamente ambas restricciones. | No cumple | Debe fijarse un límite verificable. |
| Un ADR por decisión de plataforma, con alternativa descartada | No existe ADR específico para cada plataforma del despliegue. | No cumple | Falta alternativa descartada y consecuencias. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio público y con nombre de convención | Cumple | Clonado sin autenticación. |
| Estructura mínima presente | Cumple | Rutas contractuales presentes. |
| Estado calificado identificable | Cumple | Rama, hash, fecha y cierre consignados. |
| Nombres de ADR según la convención | Cumple | ADR numerados y en kebab-case. |
| ADR aceptados no reescritos | Cumple | Historial conservado. |
| `docs/ia.md` al día para la semana | No cumple | No registra actividad S8. |
| Pipeline, SonarCloud y Quality Gate públicos | Cumple | Workflow con scanner y run público de análisis: https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/35556118369 |
| Sin credenciales en el repositorio ni en el historial | No cumple | Existe un valor sensible por defecto en el servicio de pagos. |
| Contribución de todos los integrantes | Cumple | El historial permite consolidar aportes de todo el equipo. |

## Estado global del proyecto (overall · punta actual de la misma rama)

La punta actual coincide con el estado revisado. El CI y el análisis estático son públicos, pero la URL declarada no sirve la aplicación ni el health check; los demás artefactos S8 no están completos.

## Recuento y nota sugerida

**1 de 12 criterios Cumple.**

**Nota sugerida preliminar (propuesta al docente): 1.3 = 1 + 4 × (1/12).** La nota final la fija el profesor en Moodle.

## No conformidades prioritarias

- Corregir el despliegue y acreditar raíz y health check con respuesta válida.
- Versionar IaC, pasos de reproducción y configuración de secretos sin fallback inseguro.
- Completar observabilidad, costos, arc42 §7 y ADR de plataforma.

