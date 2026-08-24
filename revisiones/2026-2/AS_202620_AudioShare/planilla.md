# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | AudioShare |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Integrantes y su usuario de GitHub | Santiago Adolfo Camacho Hernandez (commits como «Santiago Adolfo Camacho Hernández») · Vincent Cardona Castro (presumiblemente `cardonavincent26-design`, sin confirmar) · Elian Daniel Perea Vanegas («Elian Daniel Perea Vanegas») · Yeiver Andres Verjel Perez («Yeiver Andrés Vergel Pérez») |
| URL del sistema desplegado | sin desplegar todavía |
| Última revisión | 2026-08-24 (Evidencia S3, actualizada tras el cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
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

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_AudioShare`, público, clon anónimo OK. |
| Estructura mínima | Cumple | Las seis rutas existen; arc42 en AsciiDoc (desviación de formato anotada). |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular.md` conforme. |
| ADR aceptados sin reescribir | Cumple | Iterado el mismo día de creación, pre-aceptación (estado «propuesto»). |
| `docs/ia.md` al día | No cumple | Commit en S3 (`024ae34`) pero sin entradas de qué se rechazó y por qué. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin coincidencias; solo `.env.example`. |
| Contribución de todos los integrantes | Cumple | 4 de 4 en S3: Santiago 11, Elian 11, Yeiver 7, Vincent 6. |
| Pipeline en verde | No verificado | Prueba `tests/health.test.ts` y script `test`; sin workflow ni evidencia de ejecución. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---|---:|---:|---:|---|
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
