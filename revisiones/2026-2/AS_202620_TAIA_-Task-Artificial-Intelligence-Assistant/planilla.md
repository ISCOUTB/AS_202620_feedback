# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | TAIA |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-03 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `76d4a91` · 2026-08-07T03:34:26-05:00 | 6/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `59590c9` · 2026-08-16T19:15:15-05:00 | 3/9 | no aplica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `46257a03` · 2026-08-23T16:47:00-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `c087303` (2026-08-30T18:54:10-05:00) | 5/10 | 3.0 | si |
| 5 | Primer corte · reto de línea base | HEAD `c087303` (sin etiqueta) | 0/12 | subtotal técnico preliminar 0,00/4,00; sustentación pendiente | revisión manual preliminar 2026-09-03 |
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
| `docs/adr/` inexistente | S1 (08-07) | No (cerrado en S3: `docs/adr/0001.md` desde 22-ago) | Crear el directorio (hecho) |
| Tensiones de calidad sin declarar en la ficha | S1 (08-07) | Sí | Enfrentar dos atributos de calidad en la ficha del problema |
| `docs/aspectos.md` con la trazabilidad en «Pendiente» y sin enlaces a los escenarios | S1 (08-07) | Sí | Ahora enlaza, pero a rutas rotas (`adr/0001-estilo-arquitectonico.md`, `ruta/al/escenario.md`): corregir en S4 |
| Documentación de calidad fuera del arc42 (`docs/calidad/`) con la sección 10 vacía | S2 (16-ago) | Sí | Mover o enlazar los escenarios y el árbol desde la sección 10 |
| Escenario 5 sin medida numérica; árbol de utilidad sin impacto/riesgo | S2 (16-08) | Sí | Completar la medida del escenario 5 y anotar impacto/riesgo en el árbol |
| C4 solo como imagen (PNG), sin verificar leyenda ni flechas | S2 (16-08) | No (cerrado en S3: `docs/c4/C4-ContextoTAIA.md` en Mermaid) | Preferir diagrama como código (hecho) |
| ADR sin nombre de convención, sin título H1 ni contexto | S3 (23-ago) | Sí | Renombrar a `0001-<kebab-case>.md`, añadir título y contexto, y corregir los enlaces rotos |
| Sin CI: no hay `.github/workflows/` y el verde de la prueba no es verificable | S3 (23-ago) | Sí | Montar workflow que corra `pytest` en cada push |
| `docs/ia.md` Entrada 03 incompleta (sin aceptado/rechazado) | S3 (23-ago) | Sí | Completar la entrada con su motivo |
| Ejecutar pytest y evidenciar run en verde | S4 | si | |
| Completar trazabilidad del ADR-0001 | S4 | si | |
| Verificar contenido de secciones arc42 3, 4, 9, 10 y 12 | S4 | si | |
| Configurar CI/SonarCloud o evidenciar plataforma alternativa | S4 | si | |
| Alinear C4 nivel 2 con el código actual | S4 | si | |
| Etiqueta corte-1 | S5 | si | |
| PDF de dos páginas | S5 | si | |
| Diagnóstico de la restricción con línea base medida | S5 | si | |
| ADR del reto | S5 | si | |
| Implementación del cambio | S5 | si | |
| Prueba en CI | S5 | si | |
| Medición contra umbral | S5 | si | |
| Trazabilidad del reto en aspectos.md | S5 | si | |
| Registro de IA del reto | S5 | si | |
| Pipeline de CI | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Clon anónimo OK en S3 (`46257a03`) |
| Estructura mínima | Cumple | Las seis rutas presentes en `46257a03` |
| Convención de nombres de ADR | No cumple | `docs/adr/0001.md` no sigue el kebab-case |
| ADR aceptados sin reescribir | Cumple | Un solo commit sobre el ADR (`decaa36`) |
| `docs/ia.md` al día | No cumple | Entrada 03 (08-23) sin aceptado/rechazado |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 y `.env` sin coincidencias |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas = 4 integrantes |
| Pipeline en verde | No cumple | Sin `.github/workflows/` y sin evidencia de ejecución |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Valeria Estefania Berrio Payares | val (2 identidades: `@email.com` y `@gmail.com`) | 8 (6+2, consolidadas) | | | Skeleton, arc42 §4 y ADR (22-ago) |
| Deiner De Jesus Gonzalez Paredes | dei0811 | 4 | | | C4 (16-ago), ia.md y README (23-ago) |
| Luis Eduardo Mendoza Angulo | luis20072002 | 1 | | | arc42 (15-ago) |
| Mark Steven Pastrana Koreia | mark | 1 | | | Escenarios (16-ago); «EtienneGW» del listado no aparece en el historial — correspondencia por confirmar |

## Preguntas abiertas para la sustentación

- ¿La cuenta «mark» es la misma persona que «EtienneGW» del listado de EQUIPOS.md?
- ¿El arranque real (`.\run.bat`) y la prueba (`pytest backend/tests`) pasan en el entorno del equipo? (no ejecutado por regla del kit)
