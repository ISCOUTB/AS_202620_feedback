# Evidencia S12 · Estrategia de datos y eventos

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s12` |
| Semana | 12 |
| Corte | Tercer corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

**Tabla operación a garantía de consistencia**, **diseño de caché con su política de
invalidación**, y **ADR de la decisión de datos más costosa de revertir**.

El recordatorio de la semana pide reflejar los almacenes de datos y los brokers en el **C4 nivel
2** como contenedores propios, y recoger en la sección 8 de arc42 la estrategia de consistencia y
la de caché.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Tabla operación a garantía.** Comprueba que las operaciones son las del sistema real y que
   cada una declara su garantía: fuerte, eventual o un punto intermedio nombrado. Una tabla con
   tres operaciones de ejemplo que no existen en el código es hallazgo.
3. **Contrasta dos operaciones con el código.** Si la tabla promete consistencia fuerte, busca la
   transacción; si promete eventual, busca dónde se acepta el desfase y qué lo reconcilia.
   ```bash
   git -C "$DIR" grep -nIE '(BEGIN|COMMIT|transaction|@Transactional|session\.commit|atomic)' HEAD -- . ':!docs' | head -20
   ```
4. **Diseño de caché con política de invalidación.** Qué se cachea, dónde, cuánto tiempo y **qué
   lo invalida**. Un tiempo de vida sin política de invalidación tras escritura es exactamente lo
   que la semana pide resolver.
   ```bash
   git -C "$DIR" grep -nIE '(redis|memcach|cache|ttl|expire)' HEAD -- . ':!docs' | head -20
   ```
5. **Si hay flujo por eventos**, comprueba las garantías declaradas: al menos una vez, como máximo
   una vez, o exactamente una vez, y qué se asume en cada caso.
6. **ADR de la decisión más costosa de revertir.** Comprueba que el equipo argumenta **por qué esa
   es la más costosa**, con su costo de reversión. Elegir cualquier decisión y llamarla la más
   costosa no cumple.
7. **C4 nivel 2.** Almacenes de datos y brokers como contenedores propios, con su tecnología
   anotada.
8. **arc42 sección 8.** Estrategia de consistencia y de caché recogidas.

**Qué no hacer aquí:** no evaluar el taller de mensajes, que se califica aparte esta misma semana;
no exigir que exista caché si el equipo argumenta que no la necesita, siempre que lo argumente.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Tabla operación a garantía de consistencia, con operaciones reales | tabla citada, contrastada con el código | | |
| Dos operaciones verificadas contra la implementación | rutas donde se cumple la garantía declarada | | |
| Diseño de caché con qué, dónde y cuánto | apartado de caché | | |
| Política de invalidación tras escritura | regla declarada y su implementación o su plan | | |
| Garantías del flujo por eventos, si existe | apartado con la garantía elegida y lo que asume | | |
| ADR de la decisión de datos más costosa de revertir | `docs/adr/NNNN-*.md` | | |
| Argumento de por qué esa decisión es la más costosa de revertir | apartado de consecuencias del ADR, con el costo de reversión | | |
| Almacenes y brokers como contenedores propios en el C4 nivel 2 | diagrama del nivel 2 | | |
| arc42 sección 8 con consistencia y caché | `docs/arc42/08*` | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente.

Si la política de invalidación no existe, anótalo con la operación concreta que se rompe: es la
observación que más sirve al equipo antes del proyecto final, y la que la revisión entre pares de
la semana 14 suele señalar.
