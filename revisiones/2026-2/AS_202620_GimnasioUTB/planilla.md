# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo GimnasioUTB. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | GimnasioUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Integrantes y su usuario de GitHub | Sebastian Felipe Caicedo Acosta · Rodrigo Andres Facio Lince Beltran · Pedro Luis Pallares De La Hoz — cuentas abajo |
| URL del sistema desplegado | sin desplegar aún |
| Ultima revision | 2026-09-03 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 5 | Primer corte · reto de línea base | HEAD `38f0031` (sin etiqueta) | 0/12 | subtotal técnico preliminar 0,00/4,00; sustentación pendiente | revisión manual preliminar 2026-09-03 |
| 4 | S4 | `56db96b` (2026-08-30T22:33:47-05:00) | 2/10 | 1.8 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `a45615e9` · 2026-08-08T21:41:21-05:00 | 4/9 | 2,8 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `1b30b7a4` · 2026-08-16T21:04:17-05:00 | 5/9 | 3,2 * | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `73c1f240` · 2026-08-23T19:38:29-05:00 | 8/9 | no se publica | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Sin `docs/arc42/` ni `docs/c4/` (arc42 en un solo archivo `docs/arc42_gimnasio_utb.md`, C4 en `docs/C4.jpg`) | S1 | Sí (parcial: `docs/adr/` ya existe) | Repartir el arc42 en `docs/arc42/` y el C4 en `docs/c4/` |
| Sebastián Caicedo Acosta sin commits ni cuenta atribuible | S1 | Cerrado en S3 (9 commits, identidad consolidada `[correo omitido]`) | Se resolvió; vigilar que la contribución siga repartida |
| `docs/aspectos.md` en prosa, sin la tabla de 8 columnas ni enlaces a escenarios | S1 | Sí | Convertir a tabla ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia y enlazar ADR y escenarios |
| `docs/ia.md` sin lo rechazado y su motivo por uso | S1 | Sí (mejora: entradas S3 con prompt y verificación) | Añadir por cada uso qué se rechazó y por qué |
| Inconsistencia «Equipo de 4 personas» (OC5) | S2 | Sí | Son 3 según matrícula; corregir en arc42 y en el ADR |
| ADR no alcanzable desde `aspectos.md` ni desde los escenarios ES1/ES7/ES8 | S3 | Sí | Enlazar el ADR desde la fila del aspecto y desde cada escenario que lo motiva |
| Implementar corte vertical (interfaz HTTP, lógica de aplicación, persistencia PostgreSQL) | S4 | si | |
| Añadir prueba automatizada del recorrido completo (registro de acceso y consulta de aforo) | S4 | si | |
| Corregir README: un solo comando de arranque y scripts existentes en package.json | S4 | si | |
| Completar trazabilidad de docs/aspectos.md y ADR 0001 con rutas y commits reales | S4 | si | |
| Verificar y completar secciones 4-6, 9, 10 y 12 del arc42 | S4 | si | |
| Configurar análisis estático con SonarCloud | S4 | si | |
| Etiqueta `corte-1` ausente | S5 | Sí | Etiquetar el estado entregable antes del cierre. |
| Respuesta al reto sin diagnóstico, ADR ni incremento identificado | S5 | Sí | Declarar la restricción, medir la línea base y registrar e implementar la decisión. |
| Prueba concurrente con PostgreSQL y medición contra umbral pendientes | S4 | Sí | Aportar herramienta, carga, procedimiento, resultado y run de CI del cambio. |
| `docs/aspectos.md` no usa las ocho columnas del contrato ni contiene una fila del reto | S5 | Sí | Hacer navegable la cadena completa del reto. |
| Registro de IA sin entrada del Corte 1 | S5 | Sí | Registrar una salida aceptada, corregida o rechazada con motivo técnico. |
| ADR aceptado reescrito en commits posteriores | S5 | Sí | Mantener el ADR histórico y registrar cambios mediante otro ADR. |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_GimnasioUTB`, público |
| Estructura mínima | Cumple | Las seis rutas del contrato están presentes en HEAD. |
| Convención de nombres de ADR | Cumple | `0001-arquitectura-hexagonal.md` |
| ADR aceptados sin reescribir | No cumple | Aceptado en `92f4a53` y modificado en cuatro commits posteriores. |
| `docs/ia.md` al día | No cumple | Última entrada de Semana 4; falta Corte 1. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Escaneos limpios; solo `.env.example`. |
| Contribución de todos los integrantes | Cumple | Tres personas consolidadas para tres integrantes en HEAD. |
| Pipeline en verde | Cumple | Run de HEAD `33535934343` en verde; no demuestra el reto. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Sebastian Felipe Caicedo Acosta | `sebastian-caicedo` + «Sebastian Felipe Caicedo Acosta» (mismo correo `[correo omitido]`, consolidado) | 9 | 0 | — | Se incorporó en S3 (esqueleto, §4, ADR y CI); cerró el hallazgo de S1 |
| Rodrigo Andres Facio Lince Beltran | RodrigoFacioLince (correo omitido) | 3 | 0 | — | Sin commits en S3 |
| Pedro Luis Pallares De La Hoz | PedroPambi (correo omitido) | 9 | 0 | — | Documentó arranque y CI en README (último commit S3) |

Correspondencia cuenta↔persona inferida del correo institucional de los commits; la confirma el docente.

## Preguntas abiertas para la sustentación

- ¿El diagrama C4 (imagen) tiene leyenda y flechas etiquetadas? (no se pudo inspeccionar desde el repositorio).
- ¿Por qué 8 escenarios si la ficha pedía entre 3 y 5?
- ¿Cuándo van a repartir el arc42 en `docs/arc42/` y el C4 en `docs/c4/`? (arrastrado desde S1).
- ¿Por qué la restricción OC5 dice «equipo de 4 personas» si la matrícula registra 3?
