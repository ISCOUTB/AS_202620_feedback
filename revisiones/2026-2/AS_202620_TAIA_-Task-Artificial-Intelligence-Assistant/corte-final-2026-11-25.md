# TAIA · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `main` · [`b221d26112ef256ddc2ae0548f1d333c2d680bcd`](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/b221d26112ef256ddc2ae0548f1d333c2d680bcd) · 2026-11-25T21:52:36.923 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/compare/bd3db97fd53469d8e1f9e397b69fc63acb21ccfa...b221d26112ef256ddc2ae0548f1d333c2d680bcd). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** C4 y arc42 sitúan PostgreSQL fuera del Compose. ADR-0012 decide recordatorios dentro de la API; Compose define un servicio backend y FastAPI instala el bucle en su `lifespan`. La prueba estática no verifica envío externo ni disponibilidad durante una caída. Confirmar el recorrido y el estado de la cola al reiniciar.

Evidencia al SHA: [C4-C2.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/b221d26112ef256ddc2ae0548f1d333c2d680bcd/docs/c4/C4-C2.md) · [07-vista-de-despliegue.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/b221d26112ef256ddc2ae0548f1d333c2d680bcd/docs/arc42/07-vista-de-despliegue.md) · [0012-enviar-recordatorios-con-un-proceso-dentro-de-la-api.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/b221d26112ef256ddc2ae0548f1d333c2d680bcd/docs/adr/0012-enviar-recordatorios-con-un-proceso-dentro-de-la-api.md) · [docker-compose.yml](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/b221d26112ef256ddc2ae0548f1d333c2d680bcd/docker-compose.yml) · [main.py · L183-L213](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/b221d26112ef256ddc2ae0548f1d333c2d680bcd/backend/app/main.py#L183-L213).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** No se localizó una ejecución por push asociada al SHA en la consulta. No se trasladó el resultado de otro SHA..
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` · rama `main` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/runs/138232210092) completado el 2026-11-24T05:07:40 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant&branch=main). **Quality Gate: Aprobado.** El alcance completo del análisis no quedó confirmado. El resumen del proveedor registra 54 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [API institucional](https://taia-sistema.iscoutb.dev/health); no equivale a cliente Flutter publicado. [README del SHA](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/b221d26112ef256ddc2ae0548f1d333c2d680bcd/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
