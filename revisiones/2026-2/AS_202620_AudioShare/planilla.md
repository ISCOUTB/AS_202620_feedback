# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | AudioShare |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Santiago Adolfo Camacho Hernandez (commits como «Santiago Adolfo Camacho Hernández») · Vincent Cardona Castro (presumiblemente `cardonavincent26-design`, sin confirmar) · Elian Daniel Perea Vanegas («Elian Daniel Perea Vanegas») · Yeiver Andres Verjel Perez («Yeiver Andrés Vergel Pérez»); ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://audioshare.iscoutb.dev · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `6a03a9718776420d46ed40f7addc5667206908cd` · 2026-10-04T23:15:57-05:00 | 3/10 | 2.2 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `6a03a9718776420d46ed40f7addc5667206908cd` · 2026-10-04T23:15:57-05:00 | 3/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 8 | S8 | `e4789d88` (2026-09-27T23:49:01-05:00) | 9/10 | 4.6 (provisional; 2 filas de despliegue diferidas por decisión docente) | si |
| 6 | S6 | `4a0eba9` (2026-09-13T22:01:57-05:00) | 4/8 | 3.0 (prelim.) | si |
| 7 | S7 | `0ada095` (2026-09-20T23:57:20-05:00) | 9/10 | 4.6 | si |
| 5 | CORTE1 | `cb65d13` (2026-09-06T22:00:48-05:00) | 8/12 | 3.7 | si |
| 4 | S4 | `24a5023` (2026-08-30T23:48:29-05:00) | 4/10 | 2.6 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `1c9ebb0a` · 2026-08-09T20:31:49-05:00 | 2/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `d0760fdf` · 2026-08-16T23:31:32-05:00 | 4/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `024ae3435` · 2026-08-23T23:47:38-05:00 | 5/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Sustituir la prueba de constantes por una que invoque la lógica real y falle al introducir un defecto de sincronización; registrar procedimiento y resultado. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar la cadena A-01 hacia ADR-0005, código exacto, prueba y medición reproducible. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Aportar mediciones de receptores y comparación con umbral, sin presentar un ejemplo sintético como experimento. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Localizar la consigna oficial S10 y definir línea base, hipótesis, variables y montaje. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Corregir Flutter CI, evidenciar SonarCloud/Quality Gate del hash y alinear Dokploy con ADR/C4/arc42. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Hacer específica la auditoría de erosión y la verificación de dependencias; registrar rechazo técnico propio de la entrega. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Existe decisión explícita de no incorporar componente generativo: [docs/adr/0006-no-incorporar-componente-generativo.md:22–45](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0006-no-incorporar-componente-generativo.md#L22-L45). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| URL y health check accesibles en la comprobación actual; no cambia retrospectivamente S8. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

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
| Contrato OpenAPI/AsyncAPI/proto versionado con rutas y esquemas | S7 | no (verificado en la relectura) | |
| Prueba de contrato presente y ejecutada por el pipeline | S7 | no (verificado en la relectura) | |
| Evidencia de fallo de la prueba ante cambio incompatible | S7 | si | |
| ADR de estrategia de integración con alternativa descartada | S7 | no (verificado en la relectura) | |
| Evidencia de SonarCloud: configuración, run exitoso y URL pública con Quality Gate | S7 | si | |
| C4 nivel 3 y ADR del reajuste de límites | S6 | si | |
| docs/arc42/src/08_concepts.adoc (y secciones 07 y 11 ausentes) | S6 | si | |
| Auditoría de propiedad de datos con recorrido citado | S6 | si | |
| Tipificación de relaciones del mapa de contextos | S6 | si | |
| Evidencia pública de SonarCloud (configuración, run y Quality Gate) | S6 | si | |
| Pruebas de EC-02 y EC-03 | S6 | si | |
| Ocho commits posteriores al cierre 2026-09-21T05:00:00Z (=00:00-05:00): 900b3e8 (00:04:54), 628c8be (00:07:23), d01e743 (00:09:48), 354f1f5 (00:15:12), eab5775 (00:18:45), 5c72af6 (00:19:45), b83471f (00:20:25) y d094a51 (00:21:38), todos en origin/master. | S7 | no (resuelto tarde) | — |
| Evidencia de que la prueba de contrato falla ante un cambio incompatible (run en rojo o registro del cambio). | S7 | si | |
| Línea del workflow que ejecuta la prueba de contrato y URL del run de CI. | S7 | no (verificado en la relectura) | |
| Evidencia pública de SonarCloud: invocación del scanner, run exitoso y Quality Gate. | S7 | si | |
| Correspondencia verificable entre rutas del contrato y rutas implementadas en el código. | S7 | no (verificado en la relectura) | |
| Columna Evidencia en docs/aspectos.md y limpieza de la matriz duplicada. | S7 | si | |
| Marcadores de conflicto de fusión en README y ADR-0001 y enlaces a ADR inexistentes. | S7 | si | |
| Secciones 07 y 11 de arc42 ausentes y documentación arc42 en formato .adoc. | S7 | si | |
| Verificación del contenido de docs/ia.md (qué se rechazó y por qué). | S7 | no (verificado en la relectura) | |
| URL pública con hora y código de respuesta, y ruta de health check consultable. | S8 | si | |
| Infraestructura como código del entorno desplegado, versionada y reproducible desde el README. | S8 | si | |
| Run de CI sobre la rama principal y evidencia pública de SonarCloud con Quality Gate. | S8 | si | |
| Configuración de logs estructurados con línea de ejemplo. | S8 | si | |
| Métrica consultable asociada a un escenario de calidad. | S8 | si | |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita. | S8 | si | |
| arc42 sección 7 con una caja por pieza y sección 2 con el límite de costo. | S8 | si | |
| Un ADR por decisión de plataforma, con alternativa descartada. | S8 | si | |
| Corrección del enlace a un ADR inexistente en `docs/aspectos.md` y de las columnas de la tabla de aspectos. | S8 | si | |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público por HTTPS y rama remota master; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Presentes README, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md; [docs/aspectos.md:36–43](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/aspectos.md#L36-L43). arc42 usa AsciiDoc, desviación de formato frente a Markdown. |
| Estado calificado identificable | Cumple | Hash y fecha completos en el encabezado, elegidos por git log --until sobre origin/master. |
| Nombres de ADR según la convención | No cumple | El nombre [docs/adr/0005 Validación-sincronización-inicial.md:1–7](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0005%20Validaci%C3%B3n-sincronizaci%C3%B3n-inicial.md#L1-L7) contiene espacio y acentos; no pasa NNNN-kebab-case. |
| ADR aceptados no reescritos | No cumple | ADR-0001 ya estaba aceptado en 924d133 y fue modificado en 354f1f5: se verificaron ambas versiones y el diff. El texto actual solo dice complementado, sin preservar la versión aceptada mediante reemplazo; [docs/adr/0001-usar-monolito-modular.md:1–8](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0001-usar-monolito-modular.md#L1-L8). |
| docs/ia.md al día para la semana | No cumple | Hubo cambios de S9, pero el registro específico no separa una salida rechazada con motivo técnico y mantiene Estado «semana 7»; [docs/ia.md:112–112](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L112-L112), [docs/ia.md:363–389](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L363-L389). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Scanner configurado en [sonar-project.properties:1–5](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/sonar-project.properties#L1-L5) y [.github/workflows/ci.yml:18–23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/.github/workflows/ci.yml#L18-L23); la organización configurada no es isco-utb. CI success, Flutter failure en el hash. Falta análisis público y Quality Gate atribuibles a esta revisión. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Sin credenciales reales en el árbol: coincidencias solo con referencias a secrets de Actions. Barrido histórico completo no concluyó; no se certifica el historial. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas de autor visibles, distribuidas en el historial. No se inventa la correspondencia entre cuentas y los cuatro integrantes; falta mapa verificable para acreditar a todas las personas. Punta actual: 4 firmas y 206 commits agregados; no equivalen automáticamente a personas. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Cuatro firmas de autor en el historial del estado S9; 206 commits agregados. Correspondencia completa cuenta-persona no verificada. En HEAD: 4 firmas y 206 commits agregados.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Santiago Adolfo Camacho Hernandez | firma como «Santiago Adolfo Camacho Hernández» | 11 (S3) | — | — | Cierre de documentación S3 |
| Vincent Cardona Castro | presumiblemente `cardonavincent26-design` (sin confirmar) | 6 (S3) | — | — | Esqueleto ejecutable (`be1bf24`) |
| Elian Daniel Perea Vanegas | firma como «Elian Daniel Perea Vanegas» | 11 (S3) | — | — | Correcciones por feedback, estructura arc42 |
| Yeiver Andres Verjel Perez | firma como «Yeiver Andrés Vergel Pérez» | 7 (S3) | — | — | Autor del ADR 0001 |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Qué ocurriría si un receptor recibe startAt después del instante programado y qué prueba real detectaría el desfase?
- ¿Qué consumo y persistencia necesita Dokploy y quién asume el costo al salir del recurso académico gratuito?
- La prueba actual produce 40 ms por construcción: ¿qué cambiarían al medir relojes, red y reproducción física reales?
