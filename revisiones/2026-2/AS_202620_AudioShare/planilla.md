# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | AudioShare |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Integrantes y su usuario de GitHub | Santiago Adolfo Camacho Hernandez (commits como «Santiago Adolfo Camacho Hernández») · Vincent Cardona Castro (presumiblemente `cardonavincent26-design`, sin confirmar) · Elian Daniel Perea Vanegas («Elian Daniel Perea Vanegas») · Yeiver Andres Verjel Perez («Yeiver Andrés Vergel Pérez») |
| URL del sistema desplegado | sin desplegar todavía |
| Ultima revision | 2026-09-23 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 8 | S8 | `d094a51` (2026-09-21T00:21:38-05:00) | 2/12 | 1.7 (prelim.) | si |
| 6 | S6 | `4a0eba9` (2026-09-13T22:01:57-05:00) | 4/8 | 3.0 (prelim.) | si |
| 7 | S7 | `0ada095` (2026-09-20T23:57:20-05:00) | 5/10 | 3.0 | si |
| 5 | CORTE1 | `cb65d13` (2026-09-06T22:00:48-05:00) | 8/12 | 3.7 | si |
| 4 | S4 | `24a5023` (2026-08-30T23:48:29-05:00) | 4/10 | 2.6 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `1c9ebb0a` · 2026-08-09T20:31:49-05:00 | 2/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `d0760fdf` · 2026-08-16T23:31:32-05:00 | 4/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `024ae3435` · 2026-08-23T23:47:38-05:00 | 5/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Nombre del repositorio con «PROYECTO_» de más (`AS_202620_PROYECTO_AudioShare`) | S1 (cierre 2026-08-10) | cerrado el 2026-08-18 (`31bcc18`), después del cierre S2 | Ver feedback S1/S2 (convención de nombre) |
| `docs/aspectos.md` sin la tabla de 8 columnas del curso y sin enlace al ADR | S1 | sí (en S3 rompe el enlace hacia el ADR) | Ver feedback S1/S2 y S3 |
| `docs/arc42/` en AsciiDoc; árbol de utilidad y matriz fuera de `docs/arc42/src/` | S1 (ausencia), S2 (formato/ubicación) | sí | Ver feedback S1/S2 |
| `docs/ia.md` sin entradas de «qué se rechazó y por qué» (sí creció en S3) | S2 | sí | Ver feedback S1/S2 y S3 |
| Sin `docs/adr/` ni ADR 0001 (S3 lo exigía) | S3 | cerrado el 2026-08-23 (`84e2e03`→`f5641c8`) | ADR 0001 creado y completo |
| Sin esqueleto ejecutable: cero código, README sin comando de arranque, sin prueba ni workflow | S3 | cerrado el 2026-08-23 (`be1bf24`) | Esqueleto monolito modular con README, prueba y paquetes |
| Yeiver sin commits en el periodo S3 (contribución 3 de 4) | S2 (Vincent sin commits en S1); Yeiver: S3 | cerrado (7 commits de Yeiver en S3) | Ver feedback S3 |
| Sección 4 de arc42 desincronizada: declara «pendiente» la selección del estilo ya decidida en el ADR; sin tácticas | S3 | sí | Ver feedback S3 |
| Matriz comparativa sin referencia a los escenarios del árbol de utilidad | S3 | sí | Ver feedback S3 |
| ADR no enlazado desde `aspectos.md` ni desde el escenario; «EC-nn» placeholder; estado «propuesto» | S3 | sí | Ver feedback S3 |
| Persistencia del corte vertical | S4 | si | |
| Sección 9 enlazada a ADR reales | S4 | si | |
| C4 nivel 2 coherente con el código | S4 | si | |
| Fila de aspectos con columnas Requisito y C4 y prueba citada | S4 | si | |
| README con un solo comando de arranque | S4 | si | |
| Pipeline con run en verde | S4 | si | |
| Confirmar etiqueta corte-1 | S5 | si | |
| Obtener restricción asignada | S5 | si | |
| Completar trazabilidad en docs/aspectos.md | S5 | si | |
| Actualizar ADR 0001 a aceptado con implementación y pruebas | S5 | si | |
| Agregar entrada de IA del corte 1 | S5 | si | |
| Configurar pipeline y aportar runs | S5 | si | |
| Conciliar C4 Nivel 2 con la implementación | S5 | si | |
| Aportar medición de línea base y resultado contra umbral | S5 | si | |
| Diagnosticar y responder la restricción nueva asignada en el corte 1 (S5) | S5 | si | Se revisó el repositorio completo hasta la etiqueta `corte-1` y no hay ADR, medición ni prueba de una restricción nueva; solo se integró el corte vertical de S4 y se ajustaron diagramas C4, README y CI. |
| `docs/ia.md` sin entrada específica del corte 1 | S5 | si | Se les dijo que la línea "actualizado durante la semana 5" no sustituye una entrada de uso de IA de este corte. |
| Crear correcciones.md en la raíz del repositorio con respuesta trazable a los hallazgos S1-S4. | S5 | si | |
| Verificar PDF adjunto en Moodle y sustentación oral. | S5 | si | |
| secciones arc42 07/08/11 | S5 | si | |
| análisis estático SonarCloud | S5 | si | |
| PDF en Moodle (no verificado) | S5 | si | |
| Sustentación (no verificada) | S5 | si | |
| Contrato OpenAPI/AsyncAPI/proto versionado con rutas y esquemas | S7 | si | |
| Prueba de contrato presente y ejecutada por el pipeline | S7 | si | |
| Evidencia de fallo de la prueba ante cambio incompatible | S7 | si | |
| ADR de estrategia de integración con alternativa descartada | S7 | si | |
| Evidencia de SonarCloud: configuración, run exitoso y URL pública con Quality Gate | S7 | si | |
| C4 nivel 3 y ADR del reajuste de límites | S6 | si | |
| docs/arc42/src/08_concepts.adoc (y secciones 07 y 11 ausentes) | S6 | si | |
| Auditoría de propiedad de datos con recorrido citado | S6 | si | |
| Tipificación de relaciones del mapa de contextos | S6 | si | |
| Evidencia pública de SonarCloud (configuración, run y Quality Gate) | S6 | si | |
| Pruebas de EC-02 y EC-03 | S6 | si | |
| Ocho commits posteriores al cierre 2026-09-21T05:00:00Z (=00:00-05:00): 900b3e8 (00:04:54), 628c8be (00:07:23), d01e743 (00:09:48), 354f1f5 (00:15:12), eab5775 (00:18:45), 5c72af6 (00:19:45), b83471f (00:20:25) y d094a51 (00:21:38), todos en origin/master. | S7 | no (resuelto tarde) | — |
| Evidencia de que la prueba de contrato falla ante un cambio incompatible (run en rojo o registro del cambio). | S7 | si | |
| Línea del workflow que ejecuta la prueba de contrato y URL del run de CI. | S7 | si | |
| Evidencia pública de SonarCloud: invocación del scanner, run exitoso y Quality Gate. | S7 | si | |
| Correspondencia verificable entre rutas del contrato y rutas implementadas en el código. | S7 | si | |
| Columna Evidencia en docs/aspectos.md y limpieza de la matriz duplicada. | S7 | si | |
| Marcadores de conflicto de fusión en README y ADR-0001 y enlaces a ADR inexistentes. | S7 | si | |
| Secciones 07 y 11 de arc42 ausentes y documentación arc42 en formato .adoc. | S7 | si | |
| Verificación del contenido de docs/ia.md (qué se rechazó y por qué). | S7 | si | |
| URL pública con hora y código de respuesta, y ruta de health check consultable. | S8 | si | |
| Infraestructura como código del entorno desplegado, versionada y reproducible desde el README. | S8 | si | |
| Run de CI sobre la rama principal y evidencia pública de SonarCloud con Quality Gate. | S8 | si | |
| Configuración de logs estructurados con línea de ejemplo. | S8 | si | |
| Métrica consultable asociada a un escenario de calidad. | S8 | si | |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita. | S8 | si | |
| arc42 sección 7 con una caja por pieza y sección 2 con el límite de costo. | S8 | si | |
| Un ADR por decisión de plataforma, con alternativa descartada. | S8 | si | |
| Corrección del enlace a un ADR inexistente en `docs/aspectos.md` y de las columnas de la tabla de aspectos. | S8 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_AudioShare`, público, clon anónimo OK. |
| Estructura mínima | Cumple | Las seis rutas existen; arc42 en AsciiDoc (desviación de formato anotada). |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular.md` conforme. |
| ADR aceptados sin reescribir | Cumple | Iterado el mismo día de creación, pre-aceptación (estado «propuesto»). |
| `docs/ia.md` al día | Cumple | Commit en S3 (`024ae34`) pero sin entradas de qué se rechazó y por qué. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin coincidencias; solo `.env.example`. |
| Contribución de todos los integrantes | Cumple | 4 de 4 en S3: Santiago 11, Elian 11, Yeiver 7, Vincent 6. |
| Pipeline en verde | No verificado | Prueba `tests/health.test.ts` y script `test`; sin workflow ni evidencia de ejecución. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Santiago Adolfo Camacho Hernandez | firma como «Santiago Adolfo Camacho Hernández» | 11 (S3) | — | — | Cierre de documentación S3 |
| Vincent Cardona Castro | presumiblemente `cardonavincent26-design` (sin confirmar) | 6 (S3) | — | — | Esqueleto ejecutable (`be1bf24`) |
| Elian Daniel Perea Vanegas | firma como «Elian Daniel Perea Vanegas» | 11 (S3) | — | — | Correcciones por feedback, estructura arc42 |
| Yeiver Andres Verjel Perez | firma como «Yeiver Andrés Vergel Pérez» | 7 (S3) | — | — | Autor del ADR 0001 |

## Preguntas abiertas para la sustentación

- Confirmar la cuenta de GitHub de Vincent Cardona Castro (¿`cardonavincent26-design`?) contra la matrícula.
- ¿Por qué el C4 de contexto omite la red Wi-Fi y el moderador que declara la sección 3?
- ¿Cómo medirán los escenarios (herramienta, carga, umbral)? Ninguno lo declara todavía.
- ¿Por qué la sección 4 sigue declarando «pendiente» la selección del estilo si el ADR 0001 ya la decidió y el esqueleto ya está montado?
- ¿Ratificarán el ADR como aceptado (hoy está «propuesto») y qué escenario lo motiva (el campo dice «EC-nn»)?
