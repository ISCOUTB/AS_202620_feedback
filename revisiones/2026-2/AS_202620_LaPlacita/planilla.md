# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo LaPlacita. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | LaPlacita |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Integrantes y su usuario de GitHub | Mateo Josue Buendia Barrios · Miguel Angel Isaza Montalvo · Samuel David Jimenez Alvarez · Jorge Alberto Martinez Castillo — cuentas abajo |
| URL del sistema desplegado | declarada en el repo: `https://laplacita-app.graymoss-fdd72159.canadacentral.azurecontainerapps.io` (no consultada; pendiente por Moodle) |
| Ultima revision | 2026-10-01 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | Evidencia S9 · Generación verificada y trazable | `b03a797` (2026-09-27T19:00:57-05:00) | 1/10 | 1.4 (provisional; sin entrega S9 en la punta al momento de la pasada) | sí, preliminar |
| 8 | S8 (definitiva) | `b03a797` (2026-09-27T19:00:57-05:00) | 10/10 | 5.0 (provisional; 2 filas de despliegue pendientes) | sí, definitiva |
| 7 | S7 | `8c2e1bc` (2026-09-20T22:47:32-05:00) | 10/10 | 5.0 | sí, auditada |
| 6 | S6 | `2c0eb01` (2026-09-13T21:28:00-05:00) | 7/8 | 4.5 | si |
| 5 | CORTE1 | `50b92f8` (2026-09-06T17:45:05-05:00) | 8/12 | 3.7 | si |
| 4 | S4 | `745e799` (2026-08-30T21:52:41-05:00) | 4/10 | 2.6 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `37f1deb8` · 2026-08-08T15:37:16-05:00 | 8/9 | 4,6 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `fa7e13bc` · 2026-08-15T18:13:29-05:00 | 5/9 | 3,2 * | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `014751df` · 2026-08-23T19:30:17-05:00 | 9/9 | no se publica | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `ia.md` sin registro de lo rechazado y su motivo | S1 | Cerrado en S3 (entradas del 23/08 con rechazos y motivos) | Resuelto |
| C4 de contexto sin leyenda y guardado dentro del arc42 (§3.3), no en `docs/c4/` | S2 | Cerrado en S3 (`docs/c4/contexto.md` con leyenda, `340c22a`) | Resuelto |
| Escenarios sin la parte «artefacto» | S2 | Cerrado en S3 (ESC-01…ESC-05 con artefacto) | Resuelto |
| `aspectos.md` sin enlaces a los escenarios | S2 | Sí (parcial: ya es tabla de 8 columnas con enlaces al ADR y al código; la columna Requisito sigue sin enlazar a los escenarios) | Enlazar RF-xx a los escenarios correspondientes |
| Ficha del problema sin dos tensiones de calidad (S1) | S1 | Cerrado en S2 parcialmente | Las tensiones aparecen implícitas en el arc42 (objetivos 1.2); declararlas explícitas si vuelven a pedirse |
| ADR 0001 en estado «propuesto» | S3 | No (resuelto en el corte 1, `95ec841`) | Resuelto: ahora dice "aceptado (ratificado por ADR-0002)". |
| Sin pipeline: el verde descansa en evidencia declarada en `ia.md` | S3 | No (resuelto en S4) | Pipeline añadido y en verde desde S4; confirmado en verde también en `corte-1`. |
| Contenedores C4 sin código | S4 | si | |
| docs/ia.md sin columna de rechazo | S4 | si | |
| Trazabilidad ADR-0001/0003 pendiente | S4 | si | |
| Verificación de secciones arc42 5-12 | S4 | si | |
| Etiqueta `corte-1` | S5 | No (resuelto, `50b92f8` antes del cierre) | Resuelto. |
| Declarar restricción asignada | S5 | No (resuelto: RES-05, aislamiento por establecimiento) | Resuelto, con ADR-0004 y línea base medida. |
| Completar trazabilidad en aspectos.md | S5 | No (resuelto, fila A-02 completa) | Resuelto. |
| Registrar motivos técnicos en ia.md | S5 | Parcial | Hay entrada del Corte 1, pero su columna Validación no cierra con el resultado final; completarla. |
| Configurar SonarCloud | S5 | Parcial | `sonar-project.properties` y el paso en CI existen; falta activar `SONAR_TOKEN` para el análisis en vivo. |
| Aportar mediciones reproducibles | S5 | No (resuelto, scripts/medir-aislamiento.js) | Resuelto: 2/2 línea base -> 0/300 post-cambio, reproducible. |
| correcciones.md con nombre incorrecto | S5 | si | |
| docs/ia.md sin sección de rechazos | S5 | si | |
| docs/aspectos.md con Evidencia no navegable | S5 | si | |
| SonarCloud sin token/projectKey | S5 | si | |
| PDF adjunto no verificado | S5 | si | |
| Configurar SONAR_TOKEN para activar SonarCloud | S6 | si | |
| Crear C4 nivel 3 (componentes) | S6 | si | |
| Documentar mapa de contextos con relaciones tipificadas | S6 | si | |
| Crear tabla módulo a datos con dueño único | S6 | si | |
| Completar sección 8 de arc42 con lenguaje ubicuo | S6 | si | |
| Renombrar correciones.md a correcciones.md. | S5 | si | |
| Completar docs/ia.md con columna de rechazado. | S5 | si | |
| Configurar SONAR_TOKEN para activar SonarCloud. | S5 | si | |
| Configurar SONAR_TOKEN y projectKey para activar SonarCloud (desde S4) | S6 | si | |
| Verificar que arc42 §8 contenga lenguaje ubicuo y mapa de contextos | S6 | si | |
| Evidenciar la ejecución del pipeline CI en el commit actual | S6 | si | |
| Deuda de propiedad V-02/V-04/V-05/V-06 planificada para Corte 2 | S6 | si | |
| SonarCloud sin URL de análisis ni Quality Gate (ADR-0003 lo declara pendiente del secreto) | S7 | si | |
| V-02 ACL Pedidos→Catálogo | S7 | si | |
| V-04 Shared Kernel tiendaId | S7 | si | |
| V-05 OHS evento notificaciones | S7 | si | |
| V-06 orquestador | S7 | si | |
| Enlaces tabla aspectos | S7 | si | |
| Despliegue público y health check ausentes; pipeline en rojo | S8 | No (resuelto en S8) | Desplegado en Azure Container Apps y workflow del hash calificado en verde; queda calificar la URL por Moodle. |
| Sin logs estructurados, métrica consultable ni estimación de costo | S8 | No (resuelto en S8) | `src/logger.js` + `GET /api/v1/metricas` ligado a ESC-01/03/04 + estimación con supuestos y ruptura ×36. |
| arc42 §7, restricción económica y ADR separados por plataforma ausentes | S8 | No (resuelto en S8) | §7 y RES-06 añadidos; ADR-0009/0010/0011 por decisión de plataforma. |
| ADR aceptados editados sin reemplazo declarado (0003, 0009, 0010) | S8 | Sí | No editar ADR aceptados: si cambia la decisión, escribir otro y marcar el anterior como reemplazado. |
| Quality Gate de SonarCloud sin URL pública (job `sonar` informativo) | S8 | Sí | Vincular org/proyecto y publicar la URL del Quality Gate. |
| Sin entrega S9 en la punta: 0 commits entre el hash de S8 (`b03a797`) y `origin/master` | S9 | Sí (preliminar) | Empujar la porción construida con IA, su ADR, la prueba que falla y la medición antes del cierre del 2026-10-05T05:00:00Z. |
| ADR aceptados editados sin reemplazo declarado (0001, 0003, 0009, 0010) | S8 | Sí | Persiste en S9; si la decisión cambia, escribir otro ADR y marcar el anterior como reemplazado. |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_LaPlacita`, público |
| Estructura mínima | Cumple | Seis rutas; C4 en `docs/c4/contexto.md` con leyenda |
| Convención de nombres de ADR | Cumple | `0001-adopcion-monolito-modular.md` |
| ADR aceptados sin reescribir | No cumple | ADR-0003 (`745e799`→`95ec841`), ADR-0009 (`9452e43`→`4f38051`) y ADR-0010 (`c46fd36`→`c99f542`) editados tras su aceptación sin reemplazo declarado. |
| `docs/ia.md` al día | Cumple | Actualizado el 27/09/2026 con decisiones y rechazos técnicos. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Greps limpios |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas / 4 integrantes (64+34+29+20) |
| Pipeline en verde | Cumple | Run `36360634637` sobre `b03a797` en `master`, en verde; `sonar` informativo. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Mateo Josue Buendia Barrios | matbuendia (dos correos consolidados) | 3 | 0 | — | Sin commits en S3 |
| Miguel Angel Isaza Montalvo | Isaza927 + `isaza927` (mismo correo, consolidado) | 21 | 0 | — | Motor de S3: esqueleto, §4, enlaces del ADR |
| Samuel David Jimenez Alvarez | samulssl (correo omitido) | 18 | 0 | — | Creó el ADR 0001 (`bf94244`) |
| Jorge Alberto Martinez Castillo | Jorge M. Castillo (correo omitido) | 53 | 0 | — | Mayor contribuidor; redacción final de S3 |

Correspondencia cuenta↔persona inferida del correo de los commits; la confirma el docente.

## Preguntas abiertas para la sustentación

- ¿Por qué se retiró de `aspectos.md` la sección de enlaces a los escenarios (commit `b1f8da2`) que existía en `a484f1a`? (parcialmente resuelto: la tabla ya enlaza ADR y código; los RF-xx siguen sin enlazar a los escenarios).
- ¿Cuál es el artefacto (módulo) que recibe el estímulo en cada uno de los cinco escenarios? (resuelto en S3: la sección 4.3 asigna módulo por escenario).
- ¿Cuándo piensan montar el pipeline para que la prueba en verde deje de descansar en la declaración de `ia.md`?
- ¿Ratifican el ADR 0001 como «aceptado» (hoy dice «propuesto»)?
