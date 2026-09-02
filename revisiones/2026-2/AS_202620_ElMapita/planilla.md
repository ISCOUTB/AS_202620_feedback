# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ElMapita |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Integrantes y su usuario de GitHub | Angel Fabian Gutierrez Gomez (sin cuenta identificada en el historial) · Diego Rosales Garza (sin cuenta identificada) · Rodrigo Vazquez Rico (firma con su nombre). Historial: `RobotDRMX` (sin atribuir) y, en EQUIPOS.md, `YOOUYII` (nunca vista). |
| URL del sistema desplegado | sin desplegar todavía |
| Ultima revision | 2026-09-02 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 5 | CORTE1 | `4806374` (2026-09-01T08:39:54-06:00) | 0/12 | no aplica | si |
| 4 | S4 | `07b36f4` (2026-08-30T23:31:03-05:00) | 4/10 | 2.6 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `938d0206` · 2026-08-07T21:36:01-06:00 | 5/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `c5d9964c` · 2026-08-16T14:21:20-05:00 | 8/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `8e30f616` · 2026-08-22T16:12:55-06:00 | 4/9 | no se publica | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/ia.md` vacío (0 bytes) | S1 | sí | Ver feedback S1/S2 y S3 |
| Sin ficha del problema | S1 | sí | Ver feedback S1/S2 |
| Sin tensiones de calidad | S1 | sí | Ver feedback S1/S2 |
| Historial con cuentas sin atribuir (2 identidades para 3 integrantes; en S3 solo una cuenta firma) | S1 | sí | Ver feedback S1/S2 y S3 |
| Sección 4 de arc42 vacía (la estrategia está en ADR y matriz, no en arc42) | S3 | sí | Ver feedback S3 |
| ADR no enlazado desde `aspectos.md` ni desde los escenarios | S3 | sí | Ver feedback S3 |
| Sin pipeline (pruebas sin evidencia de verde) | S3 | sí | Ver feedback S3 |
| Run de CI en failure (33357590091) | S4 | si | |
| Pruebas del recorrido completo pendientes y rutas inexistentes en aspectos.md | S4 | si | |
| Sin SonarCloud configurado | S4 | si | |
| Autoría concentrada en una cuenta (9/11 commits) | S4 | si | |
| ADR del reto | S5 | si | |
| Línea base medida y verificable | S5 | si | |
| Cadena de trazabilidad completa en docs/aspectos.md | S5 | si | |
| Prueba en verde en pipeline | S5 | si | |
| Medición reproducible contra umbral | S5 | si | |
| Registro de IA con motivo técnico verificable | S5 | si | |
| Confirmar etiqueta corte-1 | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_ElMapita`, público. |
| Estructura mínima | Cumple | Las seis rutas; arc42 en plantilla única y C4 solo PNG (anotado desde S2). |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico-propuesto.md` conforme. |
| ADR aceptados sin reescribir | Cumple | Un solo commit de creación (`aa16382`). |
| `docs/ia.md` al día | No cumple | Vacío (0 bytes); último commit 2026-08-07. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Coincidencias solo en tipos (`password: string`) y badge placeholder del boilerplate. |
| Contribución de todos los integrantes | No cumple | 2 identidades para 3 integrantes; en S3 solo `RobotDRMX` (2 commits). |
| Pipeline en verde | No verificado | Sin pipeline; pruebas locales sin evidencia de ejecución. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Angel Fabian Gutierrez Gomez | sin cuenta identificada | 0 (S3) | — | — | `RobotDRMX` sin atribuir (¿es él o Diego Rosales Garza?) |
| Diego Rosales Garza | sin cuenta identificada | 0 (S3) | — | — | ídem |
| Rodrigo Vazquez Rico | firma con su nombre | 0 (S3) | — | — | último commit en S2 |

## Preguntas abiertas para la sustentación

- ¿A quién pertenece `RobotDRMX` y por qué `YOOUYII` nunca aparece?
- ¿Quién escribió el ADR y el esqueleto si solo una cuenta firma en S3?
- ¿Cuándo se llenará `docs/ia.md` (usos reales y rechazos)?
- ¿Cuándo se escribirá la sección 4 de arc42 en su sitio (hoy está vacía y la estrategia vive en el ADR)?
- ¿Publicarán el C4 como código para reparar el enlace roto a `docs/c4/contexto.md`?
