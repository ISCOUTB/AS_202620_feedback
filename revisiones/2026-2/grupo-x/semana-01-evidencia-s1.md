# Evidencia S1 · Grupo X

## Datos

| Campo | Valor |
|---|---|
| Equipo | Grupo X (integrantes en [EQUIPOS.md](../../../EQUIPOS.md)) |
| Repositorio | sin repositorio declarado |
| Estado revisado | no aplica: no hay repositorio que revisar |
| Comandos | `git ls-remote` no ejecutable sin nombre de repositorio |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | respuesta de la API para `ISCOUTB/$REPO`, pública | No cumple | EQUIPOS.md lo registra «sin repositorio declarado»; no hay nombre que comprobar |
| Integrantes del equipo con acceso | contribuidores frente a integrantes de EQUIPOS.md | No verificado | sin repositorio no hay historial ni colaboradores que contrastar |
| Equipo de 3 o 4 personas | integrantes declarados en EQUIPOS.md | Cumple | EQUIPOS.md declara 3 integrantes |
| Ficha del problema con usuarios y alcance | documento citado, ruta o adjunto | No verificado | sin repositorio ni adjunto visible |
| Dos tensiones de calidad declaradas y enfrentadas | párrafo o tabla de la ficha | No verificado | ídem |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | fila citada del archivo | No verificado | ídem |
| `docs/ia.md` iniciado con contenido real | primeras entradas del archivo | No verificado | ídem |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | listado del directorio | No verificado | ídem |
| `docs/adr/` y `docs/c4/` creados | listado de directorios de `docs/` | No verificado | ídem |

## Matriz transversal (CONTRATO)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | URL y respuesta de la API | No cumple | sin repositorio declarado (EQUIPOS.md) |
| Estructura mínima presente | `git ls-tree` con las seis rutas | No verificado | sin repositorio |
| Estado calificado identificable | etiqueta o hash con `%cI` | No verificado | sin repositorio |
| Nombres de ADR según la convención | `ls docs/adr` | No verificado | sin repositorio |
| ADR aceptados no reescritos | historial de cada ADR | No verificado | sin repositorio |
| `docs/ia.md` al día para la semana | commits sobre el archivo | No verificado | sin repositorio |
| Sin credenciales en el repositorio ni en el historial | `git grep` y `git log -S` | No verificado | sin repositorio |
| Contribución de todos los integrantes | `git shortlog -sne` | No verificado | sin repositorio |

## Recuento de criterios

1 de 9 criterios Cumple. **No evaluable**: sin repositorio no se propone nota.

## Prioridad

Sin repositorio no hay historial, y la contribución individual del proyecto final se califica
sobre el historial. Resolver antes que ninguna otra cosa.
