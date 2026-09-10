# Planilla de equipo · mapsutb

## Identificación

| | |
|---|---|
| Equipo | mapsutb |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Integrantes y su usuario de GitHub | Carlos Alberto Galvis Zuluaga · Carlos David Manrique Fals · Nerlis Nikol Otero Perez · Isabel Sofia Paez Matallana — cuentas observadas en el historial: `charlygz21`, `nerlis-otero`, `CarlosManrique-1397`, `i-matallana` (correspondencias por confirmar con el docente) |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-10 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `7e56ad3` · 2026-08-09T23:27:46-05:00 | 5/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `1cf1576` · 2026-08-16T21:26:05-05:00 | 4/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `ed55eda` · 2026-08-23T21:44:05-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `f0d036a` (2026-08-30T22:53:06-05:00) | 5/10 | 3.0 | si |
| 5 | CORTE1 | `f40775d` (2026-09-06T22:35:28-05:00) | 5/12 | no aplica | si |
| 6 | Evidencia S6 · Contextos delimitados y propiedad de datos | | | no aplica | |
| 7 | Evidencia S7 · Contrato de API y prueba de contrato | | | no aplica | |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | | | no aplica | |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 9 | Evidencia S9 · Generación verificada y trazable | | | no aplica | |
| 10 | Segundo corte · reto aplicado sobre el MVP | `corte-2` | | | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Estructura fuera de convención: `docs/arc42.md` único y `docs/c4_contexto.md` fuera de `docs/c4/` | S1 | sí | Mover a la estructura mínima del contrato |
| Sin tensiones de calidad en la ficha (S1) → árbol de utilidad sin impacto/riesgo (S2) | S1 | sí | Priorizar atributos por impacto y riesgo y vincularlos a los escenarios |
| Isabel Sofia Paez Matallana sin aparición en el historial | S1 | no (en HEAD aparece `i-matallana`, 39 commits en dos correos) | Confirmar acceso y contribución de la integrante |
| Etiqueta `corte-1` sobre el commit de S1 | S2 | sí (confirmado post-cierre: sigue sin moverse) | Moverla al commit real del corte 1 |
| `docs/aspectos.md` desactualizado («Sin ADR aún») y sin enlace al ADR 0001; `escenarios_calidad.md` con enlace roto al árbol | S3 | sí (confirmado también en HEAD `f40775d`, pese a que el ADR y el código ya existen) | Actualizar la tabla y enlazar el ADR desde el escenario que lo motiva |
| Sin matriz comparativa de los tres estilos contra el árbol de utilidad (el ADR la declina; el «corte anterior» no existe en el repo) | S3 | sí | escribir la matriz de estilos que pide la ficha |
| Estructura de paquetes del ADR no materializada (`lib/` solo tiene `main.dart`; faltan carpetas y `.gitkeep`) | S3 | no (resuelto en S4/S5: código de ubicación en `lib/services/`) | crear las carpetas del ADR antes de la S4 |
| `docs/ia.md` sin entradas del trabajo S3 | S3 | sí (última entrada 30/08, sin entrada de S5) | registrar el uso de IA de la semana con rechazados y motivo |
| Prueba de humo sin CI ni evidencia de verde | S3 | sí | pipeline o run aportado |
| Actualizar ficha-problema.md, escenarios_calidad.md y aspectos.md al alcance sin RA | S4 | sí | Alinear con el ADR 0002 que ya descarta RA |
| Limpiar plantilla arc42 en sección 5 | S4 | si | |
| Implementar o declarar contenedores C2 sin código (panorámicas, plano) | S4 | si | |
| Añadir CI con runs públicos que ejecuten las pruebas | S4 | sí (sigue sin `.github/workflows/` en HEAD) | Crear el workflow y publicar el run |
| Corregir mayúsculas en docs/Arc42 y docs/C4 | S4 | sí (persisten en HEAD) | Renombrar a minúsculas |
| Crear etiqueta corte-1 | S4 | sí (creada, pero sobre el commit equivocado) | Mover la etiqueta al commit real del corte |
| Registrar cambios de decisión en ADR nuevos, no editando aceptados | S4 | sí (ADR 0001 reescrito entre 23/08 y 31/08) | Crear ADR de reemplazo y conservar el aceptado |
| Etiqueta `corte-1` fijada en el commit inicial de S1 | S5 | sí (confirmado post-cierre, 2026-09-07) | Mover la etiqueta al commit real del corte antes del cierre — no se hizo |
| Sin diagnóstico, línea base ni medición reproducible del reto | S5 | sí | Documentar procedimiento, carga, cifra inicial, umbral y resultado |
| `docs/aspectos.md` contradice el alcance actual y no enlaza ADR, código ni pruebas | S5 | sí (persiste en HEAD) | Actualizar la cadena completa y hacerla navegable |
| ADR 0001 reescrito y ADR 0002 con nombre fuera de convención | S5 | sí | Conservar ADR aceptados y usar `NNNN-titulo-en-kebab-case.md` |
| Sin prueba específica del cambio ni workflow de CI | S5 | sí | Añadir prueba del reto y evidencia de run verde |
| Commits posteriores al cierre: 3f5221b, 09f7aad, af22316, fd046a8, e8bad4c (2026-09-08/09) ajustan plugins y manual de identidad visual; no se evidencia que corrijan hallazgos S1-S4. | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz del estado calificado | S5 | si | |
| Trazabilidad navegable en docs/aspectos.md | S5 | si | |
| Convención de nombre del ADR 0002 | S5 | si | |
| Evidencia de CI y pruebas asociadas al hash calificado | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `github.com/ISCOUTB/AS_202620_mapsutb`, público (clon sin auth el 2026-09-07) |
| Estructura mínima | Cumple | En HEAD usa `docs/Arc42/` y `docs/C4/`; la etiqueta S5 solo contiene README, aspectos e IA |
| Convención de nombres de ADR | No cumple | `0002.md` no incluye título en kebab-case |
| ADR aceptados sin reescribir | No cumple | `0001-patrones-de-diseno.md` tiene múltiples reescrituras posteriores a su creación |
| `docs/ia.md` al día | No cumple | última entrada 30/08; sin registro del trabajo S5 en HEAD `f40775d` |
| Sin credenciales en el repositorio ni en el historial | Cumple | greps limpios en HEAD `f40775d` |
| Contribución de todos los integrantes | Cumple | 4 personas consolidadas en HEAD: CarlosManrique-1397 (41), i-matallana (39, dos correos), charlygz21 (13), nerlis-otero (6) |
| Pipeline en verde | No verificado | Sin `.github/workflows/` ni URL de run, también en HEAD |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Carlos Alberto Galvis Zuluaga | ¿`charlygz21`? (confirmar) | 13 | — | — | Autor de los commits `FeedbackS1..S4` (06/09, archivos vacíos) |
| Carlos David Manrique Fals | ¿`CarlosManrique-1397`? (confirmar) | 41 | — | — | Mayor volumen del historial |
| Nerlis Nikol Otero Perez | ¿`nerlis-otero`? (confirmar) | 6 | — | — | Merge del corte vertical de ubicación (PR #1) |
| Isabel Sofia Paez Matallana | ¿`i-matallana`? (confirmar, dos correos) | 39 | — | — | ADR 0002 y conversión adoc→md |

## Preguntas abiertas para la sustentación

- ¿Por qué la etiqueta `corte-1` sigue sin moverse pese a que la revisión preliminar del 03/09 ya lo señaló?
- ¿`i-matallana` corresponde a Isabel Sofia Paez Matallana? Confirmar con el docente.
- ¿Cuándo se actualizará `docs/aspectos.md` para reflejar el ADR 0002 y el código que ya existen en HEAD?
- ¿La app compila y la prueba de humo pasa en verde en el entorno del equipo? (sin CI ni evidencia)
