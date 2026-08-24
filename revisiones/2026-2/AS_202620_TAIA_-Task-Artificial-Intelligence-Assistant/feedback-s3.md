# Retroalimentación publicable · TAIA (S3)

Qué está bien: la sección 4 liga la estrategia a los escenarios S1–S5 con mecanismos concretos, la matriz del ADR compara los tres estilos contra su árbol de utilidad con justificación por escenario, `run.bat` documenta el arranque en un solo comando y los paquetes `domain/application/adapters` por módulo coinciden con el ADR.

Qué corregir antes del corte 1 (semana 5):
1. Renombren `docs/adr/0001.md` a la convención `0001-<kebab-case>.md` y corrijan los enlaces rotos que apuntan a `0001-estilo-arquitectonico.md` (en `aspectos.md` y README) y el placeholder `ruta/al/escenario.md`.
2. El ADR no tiene título que enuncie la decisión ni sección de contexto: complétenlos.
3. Completen la entrada 03 de `docs/ia.md` anotando qué se aceptó y qué se rechazó con su motivo.
4. Monten un workflow para que `backend/tests/test_entrega3.py` corra en cada push y quede evidencia del verde.
