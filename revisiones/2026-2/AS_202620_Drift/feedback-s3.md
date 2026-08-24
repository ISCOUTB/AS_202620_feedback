# Feedback S3 · Drift

Qué está bien: la sección 4 elige hexagonal y la liga a los escenarios (aislamiento de adaptadores para el fallo de una fuente, mocks/stubs para testabilidad); el ADR 0001 está completo (contexto, tres alternativas con motivos, decisión, consecuencias) y la estructura de paquetes del backend es coherente con puertos y adaptadores.

Qué corregir antes del corte 1 (semana 5):

1. README contradictorio: documenta `mvn spring-boot:run` (no hay pom.xml) y `uvicorn` solo para el backend. Definan UN solo comando de arranque para todo el sistema y borren el que no aplica.
2. El ADR no es alcanzable desde `docs/aspectos.md` ni desde los escenarios: enlácenlo en ambos sitios y conviertan `aspectos.md` en la tabla de 8 columnas (se arrastra desde S1).
3. La matriz comparativa debe nombrar los escenarios E1–E5 del árbol de utilidad (qué mejora/empeora cada estilo), no solo criterios de mantenibilidad.
4. Falta pipeline: la prueba existe (`backend/tests/test_health.py`) pero no hay evidencia de que esté en verde; agreguen un workflow antes del corte.
5. Equilibren la contribución: en S3 un integrante firma 51 commits y otro 9.
