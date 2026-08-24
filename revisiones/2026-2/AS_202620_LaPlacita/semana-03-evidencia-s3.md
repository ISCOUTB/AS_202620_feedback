# Evidencia S3 · LaPlacita

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `014751df8563676c208a7a13dbe2373efa8425a1` · 2026-08-23T19:30:17-05:00 (`Cambios de redacción a la documentación aspectos.md, ia.md, README y arc42`) |
| Fecha/hora de revisión | 2026-08-23 22:00 -05:00 (antes del cierre 2026-08-24T00:00-05:00) |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until=2026-08-24T05:00:00Z`; `git ls-tree`; `git show`; `git grep`. Sin API de CI (no hay `.github/workflows/`). |

**Aviso:** la revisión se hizo antes del cierre. Si el equipo empuja antes de medianoche, el hash calificado puede cambiar.

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42-template-EN.md:86-118` (§4.1-4.4) | Cumple | Estrategia (monolito modular con capas internas) ligada a ESC-01…ESC-05; descomposición por módulo con su escenario; no describe el estilo en abstracto. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/arc42/arc42-template-EN.md:96-102` (§4.2) | Cumple | Fila por escenario del equipo (ESC-02, ESC-01, ESC-03, ESC-04, ESC-05) y por costo con equipo de 3-4 personas; qué aporta/pierde cada estilo por escenario. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-adopcion-monolito-modular.md` | Cumple | Pasa el filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$`. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-adopcion-monolito-modular.md` (Contexto:10-12, Alternativas:14-20, Decisión:22-24, Consecuencias:26-31, Trazabilidad:33-47) | Cumple | Título enuncia la decisión; incluye trazabilidad completa. Observación: estado «propuesto», no «aceptado». |
| Alternativas descartadas con su motivo | `docs/adr/0001-adopcion-monolito-modular.md:14-20` | Cumple | Capas global descartada (riesgo de violar aislamiento ESC-02) y hexagonal descartada (tiempo de desarrollo supera la ventana del semestre), ambas con motivo. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md:11-16` (columna ADR) + `docs/arc42/arc42-template-EN.md:177,198,220,241,262` («Decisión relacionada» en cada ESC) | Cumple | Los dos enlaces existen y se siguieron: la fila de cada aspecto enlaza al ADR y cada escenario ESC-01…ESC-05 enlaza al ADR. |
| Arranque con un solo comando documentado en el README | `README.md:172` (`node src/index.js`) + `package.json:9` (script `start`) | Cumple | Comando único documentado con requisitos previos. Ejecución real: No verificado por regla del kit; el equipo declara haberlo ejecutado en `docs/ia.md`. |
| Prueba automatizada en verde | `tests/health.test.js` + `package.json:10` (`npm test`) | Cumple | Sin pipeline (no hay `.github/workflows/`). Verde según evidencia de ejecución aportada por el equipo en `docs/ia.md` (23/08: «npm test corridos localmente, prueba en verde confirmada (pass 1 / fail 0)»); no comprobado de forma independiente. |
| Estructura de paquetes correspondiente al estilo del ADR | `src/modules/{catalogo,entrega,notificaciones,pagos,pedidos}/index.js` + `src/index.js` | Cumple | Módulos por dominio con frontera declarada, coherente con el monolito modular del ADR. Observación: las capas internas de cada módulo todavía no aparecen (solo `index.js` por módulo); es aceptable para el esqueleto. |

Recuento: **9 de 9 criterios cumplidos** (sin nota numérica: la fija el profesor).

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | `ISCOUTB/AS_202620_LaPlacita`, clonado sin autenticación. |
| Estructura mínima presente | Cumple | Las seis rutas existen; C4 movido a `docs/c4/contexto.md` con leyenda (`340c22a`). |
| Estado calificado identificable | Cumple | Sin etiqueta (no exigible en evidencia semanal); hash y `%cI` registrados arriba. |
| Nombres de ADR según la convención | Cumple | `ls docs/adr` sin salida en el filtro. |
| ADR aceptados no reescritos | Cumple | Único commit `bf94244` (2026-08-23); estado «propuesto» anotado. |
| `docs/ia.md` al día para la semana | Cumple | Entradas del 23/08 con qué se rechazó y por qué (C4 más detallado rechazado; restauración de secciones en aspectos rechazada con motivo); cierra el hallazgo de S1. |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` de secretos sin coincidencias; sin `.env` versionado. |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas / 4 integrantes: Jorge M. Castillo 53; Isaza927+`isaza927` (mismo correo) 21; samulssl 18; matbuendia (dos correos) 3. |

## No verificado / pendientes

- Ejecución real del arranque y de la prueba: No verificado de forma independiente por regla del kit; el verde descansa en la evidencia declarada en `docs/ia.md` (pass 1 / fail 0) hasta que exista pipeline.
- Si el equipo empuja antes del cierre, repetir sobre el nuevo hash.

## Hallazgos para la planilla

- Cierran casi todo lo arrastrado: `ia.md` con rechazos y motivos, C4 en `docs/c4/` con leyenda, escenarios con «artefacto», aspectos con tabla de 8 columnas y enlaces al ADR.
- ADR en estado «propuesto»: conviene marcarlo «aceptado» una vez ratificado.
- Sin pipeline todavía: la evidencia del verde es declaración del equipo.
- `aspectos.md` enlaza ADR y código, pero la columna Requisito (RF-xx) no enlaza a los escenarios; C4 y Evidencia siguen «Pendiente» (esperable en S3).
