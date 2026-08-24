# Retroalimentación publicable · ShareU (S3)

Qué está bien: la sección Solution Strategy liga la decisión al escenario de usabilidad con una matriz comparativa contextualizada, el ADR 0001 tiene contexto, alternativas descartadas con criterio de reapertura y consecuencias, y el esqueleto monta los cinco módulos del ADR con su router.

Qué corregir antes del corte 1 (semana 5):
1. El README termina en el encabezado «Esqueleto ejecutable — arranque» sin ningún comando debajo y no hay manifest de dependencias: documenten el comando único y añadan `requirements.txt`.
2. Estructura mínima incompleta: muevan la plantilla suelta a `docs/arc42/` y creen `docs/c4/`.
3. Enlacen el ADR desde `docs/aspectos.md` y desde el escenario que lo motiva; `aspectos.md` sigue sin la tabla de 8 columnas.
4. Completen `docs/ia.md`: falta la columna de qué se rechazó y por qué, y las entradas de S3 quedaron «pendientes de revisión».
5. Sin pipeline ni evidencia del verde para `tests/test_esqueleto.py`: añadan un workflow con el run.
6. Asegúrense de que todos los integrantes contribuyan al historial con su cuenta antes del corte.
