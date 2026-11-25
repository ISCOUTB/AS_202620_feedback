# ShareU · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`b17bf46daccad539020f521ccdb1ecb9765c28a3`](https://github.com/ISCOUTB/AS_202620_ShareU/commit/b17bf46daccad539020f521ccdb1ecb9765c28a3) · 2026-11-25T21:52:36.477 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_ShareU/compare/869a47c05be71adbc77af4cce9c57e1cc6de4fa4...b17bf46daccad539020f521ccdb1ecb9765c28a3). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide la topología; falta traza verificable.** C4 y arc42 representan Next.js/API y Firestore externo, como el ADR-0012 y el Compose. Las pruebas leídas usan Firestore simulado, y el README distingue salud de una búsqueda fallida histórica; no convertir esa observación en diagnóstico actual. La evaluación S16 detectó enlaces C4 no navegables: volver a enlazar cada aspecto con diagrama, implementación y prueba, y repetir búsqueda en el SHA servido.

Evidencia al SHA: [nivel-2.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/b17bf46daccad539020f521ccdb1ecb9765c28a3/docs/c4/nivel-2.md) · [07-vista-de-despliegue.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/b17bf46daccad539020f521ccdb1ecb9765c28a3/docs/arc42/07-vista-de-despliegue.md) · [0012-persistencia-en-firestore.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/b17bf46daccad539020f521ccdb1ecb9765c28a3/docs/adr/0012-persistencia-en-firestore.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_ShareU/blob/b17bf46daccad539020f521ccdb1ecb9765c28a3/Dockploy/compose.lab.yaml) · [test_repositorio_firestore.py](https://github.com/ISCOUTB/AS_202620_ShareU/blob/b17bf46daccad539020f521ccdb1ecb9765c28a3/tests/test_repositorio_firestore.py).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Tests](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/45120218890): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_ShareU` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_ShareU/runs/137512221552) completado el 2026-11-23T05:50:31 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_ShareU&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `app`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_ShareU/blob/b17bf46daccad539020f521ccdb1ecb9765c28a3/sonar-project.properties). El resumen del proveedor registra 0 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Web institucional](https://shareu.iscoutb.dev) y [API institucional](https://api-shareu.iscoutb.dev/health). [README del SHA](https://github.com/ISCOUTB/AS_202620_ShareU/blob/b17bf46daccad539020f521ccdb1ecb9765c28a3/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
