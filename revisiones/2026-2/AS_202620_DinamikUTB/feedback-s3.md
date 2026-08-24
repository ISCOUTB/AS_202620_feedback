# Feedback S3 · DinamikUTB

Qué está bien: esqueleto ejecutable completo y coherente (backend FastAPI + frontend Flutter con los módulos del monolito modular, `start.bat` como comando único documentado, pruebas en ambos lados), ADR 0001 bien redactado con título que enuncia la decisión y alternativas con motivo, `docs/ia.md` con rechazos y su motivo, y `aspectos.md` ya convertido en la tabla de 8 columnas con enlaces a los escenarios.

Qué falta (antes del corte 1, semana 5):

1. La matriz comparativa sigue con criterios genéricos y puntaje 1–5: compárenla contra su árbol de utilidad, fila por fila con Q-01, Q-02 y Q-03 (qué mejora y qué empeora cada estilo).
2. La sección 4 debe nombrar tácticas concretas contra los escenarios priorizados.
3. Enlacen el ADR 0001 en los dos sitios que faltan: la columna ADR de `aspectos.md` (hoy «Pendiente», y la nota dice que los elementos no existen — el ADR sí existe) y el escenario Q-01.
4. Sin pipeline: agreguen un workflow que ejecute las pruebas o guarden evidencia del verde antes del corte.
5. Bienvenido el regreso de todos al historial: mantengan la contribución repartida en la semana 4 (el periodo sigue concentrado en un integrante).
