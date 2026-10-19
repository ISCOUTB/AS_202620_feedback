# Evidencia S6 · Calificación automática (QuantIA) · rectificación aprobada

Sincronización: 19 de octubre de 2026. La revisión aprobada reemplaza la pasada parcial que dejó cinco criterios sin verificar. No se atribuye a la fecha de cierre contenido posterior.

| Campo | Valor |
|---|---|
| Repositorio | [Calificación automática](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica) |
| Estado de cierre | `a47d5bd660abb2d220071430f869e8ee8ee17bd2` · origin/master · 2026-09-13T23:21:55-05:00 |
| Límite exclusivo | 2026-09-14T05:00:00Z |
| Base S5 | `8b0d00b62d2a03dfe509edae578261748a842294` |

## Matriz de la ficha

| Criterio | Estado | Evidencia y fundamento |
|---|---|---|
| Mapa de contextos tipificado | Cumple | Siete contextos y relaciones de núcleo compartido, cliente/proveedor y anticorrupción, con distinción entre implementado y previsto. [Fuente de cierre](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/docs/arc42/arc42-template-ES.md#L443-L600). |
| Tabla módulo a datos con dueño único | Cumple | Seis entidades implementadas, dueño por entidad y distinción entre propiedad, ubicación y traducción de adaptadores. [Fuente de cierre](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/docs/arc42/08-propiedad-de-datos.md). |
| Cobertura de entidades existentes | Cumple | ArchivoCargado, HojaAceptada, ArchivoRechazado, ResultadoRecepcion, EntradaDeBitacora y Trabajo; el registro no atribuye código inexistente a A-02–A-05. [Fuente de cierre](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/docs/arc42/08-propiedad-de-datos.md). |
| No conformidades sobre el código actual | Cumple | Recorrido del backend y tabla V-1–V-5 con rutas, límites de auditoría y explicación de patrones de búsqueda no aplicables. [Fuente de cierre](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/docs/arc42/08-propiedad-de-datos.md#L100-L146). |
| Plan por no conformidad | Cumple | Cada V-1–V-5 contiene acción y dependencia; luego se desarrolla la corrección. Cumplir esta fila no afirma que esas correcciones ya estén implementadas. [Fuente de cierre](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/docs/arc42/08-propiedad-de-datos.md#L140-L270). |
| arc42 sección 8 con lenguaje ubicuo y mapa | Cumple | Mapa completo y vocabulario relacionado con tipos de código, con desajustes documentados. [Fuente de cierre](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/docs/arc42/arc42-template-ES.md#L443-L659). |
| C4 nivel 3 y ADR si cambiaron límites desde S5 | Cumple | Comparación con S5 8b0d00b: cambios de Docker, dependencias y medición, sin mover fronteras ni responsabilidades. ADR-0007 lo explicita. No se exige reajuste por cambios inexistentes. [Fuente de cierre](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/docs/adr/0007-declarar-los-contextos-delimitados-y-la-regla-de-dueno-unico.md#L84-L98). |
| Aspectos relacionables con contextos | Cumple | Tablas en ambas direcciones; A-03 abarca Calificación y Dashboard, Infraestructura es soporte sin aspecto propio. [Fuente de cierre](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/docs/arc42/08-propiedad-de-datos.md#L274-L330). |

## Alcance y pendientes transversales

- C4 nivel 3 existe en [docs/c4/doc-c4.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/docs/c4/doc-c4.md#L325), pero conserva afirmaciones desactualizadas (incluida ausencia de implementación). La fila condicional se cumple por no haber cambiado límites, no porque todo el C4 esté correcto. Deben conciliar diagrama, enlaces y tecnología con el código.
- [CI del estado revisado](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/34805781748) figura como exitoso en la revisión aprobada. El [workflow](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/a47d5bd660abb2d220071430f869e8ee8ee17bd2/.github/workflows/ci.yml) no incorpora scanner Sonar: el requisito transversal de análisis/Quality Gate queda sin cumplir. No es un noveno criterio S6.
- El archivo de correcciones del 26 de septiembre sirve de guía para localizar la evidencia, no de prueba de entrega oportuna. Las fuentes citadas arriba pertenecen a la instantánea de cierre.
- No se ejecutó código estudiantil. Los controles restantes de seguridad, contribución e inmutabilidad no se certifican por esta apelación; su seguimiento actual está en [S11](semana-11-evidencia-s11.md) y [S12 preliminar](semana-12-evidencia-s12.md).

## Recuento y nota sugerida

**8 de 8 criterios Cumple. Nota sugerida aprobada: 5.0 = 1 + 4 × (8/8).** Sustituye 3/8 y 2.5 de la pasada parcial; la nota final del curso corresponde al docente.

La [versión histórica anterior](https://github.com/ISCOUTB/AS_202620_feedback/blob/1e097657880c87f72241c7f0fb20690e64b7625a/revisiones/2026-2/AS_202620_Sistema-de-calificacion-automatica/semana-06-evidencia-s6.md) permanece en Git. Sus afirmaciones de contenido ausente quedan superadas por la lectura completa de las fuentes anteriores.
