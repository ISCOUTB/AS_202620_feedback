# Evidencia S8 · Despliegue reproducible, CI y observabilidad

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s8` |
| Semana | 8 |
| Corte | Segundo corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, la URL del sistema, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad, y el despliegue en ese momento |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

**URL del sistema desplegado y accesible desde fuera de la red de la universidad** (el evaluador
la abre desde su casa), **infraestructura como código versionada**, **pipeline en verde**,
**health check**, **logs estructurados**, **una métrica consultable ligada a un escenario**,
**evidencia de protección de secretos** y **estimación de costo mensual con sus supuestos**,
siguiendo el apartado «Cómo estimar el costo mensual» de la guía de despliegue.

El recordatorio de documentación pide la sección 7 de arc42 con **una caja por pieza** y dónde se
ejecuta, la sección 2 recogiendo el límite de costo y, si aplica, el de «sin tarjeta», y **un ADR
por decisión de plataforma**, no uno para todo el conjunto.

Esta es la evidencia con más piezas del semestre y la que sostiene el segundo corte, porque la
sustentación se hace sobre el entorno desplegado.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Abre la URL desde fuera de la red de la universidad** y registra código de respuesta y
   tiempo. Si responde solo desde la red interna, es No cumple con el motivo, porque el criterio
   es explícito.
   ```bash
   curl -sS -o /dev/null -w 'http=%{http_code} tiempo=%{time_total}s\n' "$URL"
   curl -sS -o /dev/null -w 'health=%{http_code}\n' "$URL/health"
   ```
   Prueba las rutas de health check que declare el equipo; si no declara ninguna, dilo.
3. **Infraestructura como código.** Debe estar versionada y describir el entorno, no ser un
   apunte de pasos manuales.
   ```bash
   git -C "$DIR" ls-tree -r --name-only HEAD | grep -iE 'dockerfile|docker-compose|\.tf$|\.tfvars$|k8s/|helm/|fly\.toml|render\.yaml|railway|Procfile|\.github/workflows/' | head -20
   ```
4. **Pipeline en verde.** Último run sobre la rama principal, con su conclusión y su URL.
   ```bash
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=10" \
     | python -c "import json,sys;[print(r['created_at'],r['name'],r['head_branch'],r['conclusion'],r['html_url']) for r in json.load(sys.stdin)['workflow_runs']]"
   ```
5. **Logs estructurados.** Busca la configuración del registro y comprueba que emite campos, no
   cadenas sueltas. Cita el archivo y una línea de ejemplo.
   ```bash
   git -C "$DIR" grep -nIE '(structlog|winston|pino|logback|serilog|logging\.config|json.*formatter)' HEAD -- . ':!docs' | head
   ```
6. **Métrica consultable ligada a un escenario.** Comprueba que existe la métrica y que el equipo
   dice **a qué escenario de calidad corresponde**. Una métrica de sistema sin escenario asociado
   se anota como incompleta.
7. **Protección de secretos.** Además del barrido del contrato, comprueba que las variables de
   entorno están declaradas y separadas del código, y que el despliegue las toma de un almacén de
   secretos o de la configuración del proveedor.
   ```bash
   ls .env.example 2>/dev/null; git -C "$DIR" ls-files | grep -E '(^|/)\.env$'
   grep -rniE 'secrets\.[A-Z_]+' .github/workflows/ | head
   ```
8. **Estimación de costo mensual con supuestos.** Tiene que salir del volumen del escenario del
   equipo, no del catálogo del proveedor: qué volumen supone, qué cuesta cada pieza y en qué punto
   se rompe la capa gratuita.
9. **arc42 sección 7 y sección 2.** Una caja por pieza con dónde se ejecuta; el límite de costo y,
   si aplica, la restricción de «sin tarjeta», recogidos como restricciones.
10. **Un ADR por decisión de plataforma.** Comprueba que hay uno por pieza decidida, cada uno con
    su alternativa descartada y la capa gratuita verificada.

**Qué no hacer aquí:** no comparar alternativas de despliegue, que es el taller de esta misma
semana y se califica aparte; no exigir alertas ni trazas distribuidas, que son nivel sobresaliente
del segundo corte; no dar por válida una captura del panel del proveedor como sustituto de la URL.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | código de respuesta y tiempo, con la hora de la comprobación | | |
| Health check consultable | ruta y código de respuesta | | |
| Infraestructura como código versionada en el repositorio | rutas de los archivos de infraestructura | | |
| El entorno se puede recrear siguiendo el README | sección del README con el procedimiento | | |
| Pipeline en verde sobre la rama principal | URL del último run y su conclusión | | |
| Logs estructurados | archivo de configuración y ejemplo de línea | | |
| Métrica consultable asociada a un escenario de calidad | nombre de la métrica y escenario al que corresponde | | |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example`, referencias a secretos en el workflow | | |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | documento con volumen supuesto y cálculo | | |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07*` | | |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02*` | | |
| Un ADR por decisión de plataforma, con alternativa descartada | archivos de `docs/adr/` de esta semana | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente.

Deja constancia de la hora exacta a la que comprobaste la URL. El criterio de MVP desplegado del
segundo corte se juzga sobre un entorno que puede estar caído en el momento de la revisión y en
pie una hora después, y sin hora la discusión no se puede cerrar.
