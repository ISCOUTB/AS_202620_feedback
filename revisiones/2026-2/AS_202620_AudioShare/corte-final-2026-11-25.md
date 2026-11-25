# AudioShare · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`b528cc26579d2b0c933ac6de119401f9adb05d6c`](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/b528cc26579d2b0c933ac6de119401f9adb05d6c) · 2026-11-25T21:52:35.996 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_AudioShare/compare/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa...b528cc26579d2b0c933ac6de119401f9adb05d6c). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Discrepancia.** C4 mantiene la API REST, sincronización NDJSON y MP3 con Range, y la vista de bloques arc42 no documenta el canal; el C4 tampoco representa el transporte de audio en vivo. Es un flujo distinto en el ADR-0015 y en el WebSocket implementado. Añadirlo al diagrama y distinguir archivo de audio en vivo; medir sincronía física, no solo el banco sintético.

Evidencia al SHA: [C4 Nivel 2 - Contenedores.mmd · L43-L51](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b528cc26579d2b0c933ac6de119401f9adb05d6c/docs/c4/C4%20Nivel%202%20-%20Contenedores.mmd#L43-L51) · [05_building_block_view.adoc](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b528cc26579d2b0c933ac6de119401f9adb05d6c/docs/arc42/src/05_building_block_view.adoc) · [0015-transmision-de-audio-en-vivo.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b528cc26579d2b0c933ac6de119401f9adb05d6c/docs/adr/0015-transmision-de-audio-en-vivo.md) · [index.ts · L3-L17](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b528cc26579d2b0c933ac6de119401f9adb05d6c/src/modules/live/index.ts#L3-L17) · [docker-compose.yml](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b528cc26579d2b0c933ac6de119401f9adb05d6c/docker-compose.yml).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [APK de Android](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/45299635833): pasó · [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/45299635849): pasó · [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/45299635820): pasó · [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/45299635798): pasó. El éxito de la publicación de imagen no prueba que el servidor la esté ejecutando.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_AudioShare` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_AudioShare/runs/138128893511) completado el 2026-11-24T00:45:17 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_AudioShare&branch=master). **Quality Gate: No aprobado.** Fuentes declaradas: `src`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b528cc26579d2b0c933ac6de119401f9adb05d6c/sonar-project.properties). El proveedor marcó incumplimiento en código nuevo; revisar en el tablero sin publicar el detalle de los hallazgos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Servicio web/API institucional](https://audioshare.iscoutb.dev); no se probó transmisión de audio. [README del SHA](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/b528cc26579d2b0c933ac6de119401f9adb05d6c/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
