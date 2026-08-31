# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | TRACTAR |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Integrantes y su usuario de GitHub | Joriel Samir Barros Pena (sin cuentas en el historial) · Geronimo Alberto Cadena Garcia (sin cuentas) · Sebastian Garcia Devoz (firma con dos identidades de git, mismo correo, más el correo institucional) · Mateo Alfonso Millan Barraza (sin cuentas) |
| URL del sistema desplegado | sin URL (sin despliegue todavía) |
| Ultima revision | 2026-08-28 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | sin commits antes del cierre | — | no evaluable | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `0a23855` · 2026-08-16T20:05:46-05:00 | 6/9 | 3.7 (propuesta) | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `5f923cd` · 2026-08-23T22:40:51-05:00 | 7/9 | no se publica | sí |
| 4 | S4 | `2b16439` (2026-08-30T15:02:33-05:00) | 1/10 | 1.4 | si |
| 5 | Primer corte · reto de línea base | `corte-1` | | | |
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
| Solo una persona con commits (dos identidades de git del mismo integrante); 3 de 4 integrantes sin aparición en el historial | S1 (y S2) | sí | urgente para el proyecto final: la contribución individual se califica sobre el historial |
| Documentos con restos de edición e incoherencias (ficha obsoleta «sin poder incluirlo a ISCOUTB», tabla de interesados con nombres de otro equipo, enlaces rotos en `aspectos.md`) | S2 | sí | revisar y consolidar antes del corte 1 |
| Enlaces rotos en la documentación S3 (ADR → `10_requisitos_calidad.md` inexistente; `aspectos.md` → `arc42.md#qs-…` con ruta incorrecta) | S3 | sí | corregir las rutas al reorganizar los documentos |
| Basura versionada (`__pycache__/*.pyc`, `db.sqlite3`); `.gitignore` solo ignora `venv/` | S3 | sí | ampliar `.gitignore` y purgar los binarios del repo |
| `docs/ia.md` sin entradas del trabajo S3 ni rechazos con motivo | S3 | sí | registrar el uso de IA de cada entrega, incluyendo lo rechazado |
| Test de salud sin CI ni evidencia de verde | S3 | sí | montar `.github/workflows/` o aportar el run |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_TRACTAR`, público (antes privado: EQUIPOS.md) |
| Estructura mínima | No cumple | sin `docs/c4/` (C4 en `docs/arc42/images/`); `ficha_problema.md` en raíz |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` |
| ADR aceptados sin reescribir | Cumple | único commit sobre el ADR, el de creación |
| `docs/ia.md` al día | No cumple | sin entradas del trabajo S3 ni rechazos con motivo técnico |
| Sin credenciales en el repositorio ni en el historial | Cumple | greps limpios |
| Contribución de todos los integrantes | No cumple | 1 persona con 16 commits; 3 sin commits |
| Pipeline en verde | No verificado | sin pipeline todavía (no exigido aún) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Sebastian Garcia Devoz | dos identidades de git (mismo correo) + correo institucional | 16 | — | — | único autor del periodo |
| Joriel Samir Barros Pena | — | 0 | — | — | sin commits |
| Geronimo Alberto Cadena Garcia | — | 0 | — | — | sin commits |
| Mateo Alfonso Millan Barraza | — | 0 | — | — | sin commits |

## Preguntas abiertas para la sustentación

- ¿Tienen los cuatro integrantes acceso al repositorio? ¿Por qué solo uno ha empujado commits?
- El diagrama C4: ¿se puede entregar como código (workspace.dsl) para poder revisar leyenda y flechas?
- ¿La prueba `manage.py test` pasa en verde en el entorno del equipo? (sin pipeline ni evidencia; se comprobará con CI)
