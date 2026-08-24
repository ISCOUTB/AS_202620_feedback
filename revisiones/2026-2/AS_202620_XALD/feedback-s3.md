# Feedback S3 · XALD (para publicar en el foro)

Gran avance: el esqueleto ya existe (proyecto Android/Kotlin con los paquetes del ADR-006: `parser`, `corefinanciero`, `syncqueue`, `aigemini`) y el README documenta el comando único de verificación (`gradlew.bat -p XALDAPP test`). La §4 de arc42 sigue siendo sólida (Sync Queue con LWW, AES-256/KeyStore, regex+IA híbrido) y el ADR-006 tiene contexto, opciones, decisión y consecuencias con riesgos mitigados.

Antes del corte 1:
1. Evidenciar las pruebas en verde (pipeline o enlace a un run real, no la «salida esperada» del README).
2. Renombrar los 6 ADR a `NNNN-titulo-en-kebab-case.md`.
3. Subir los escenarios y el árbol de utilidad (pendientes desde S2) y anclar a ellos la matriz comparativa.
4. En `aspectos.md`, enlazar los ADR de verdad e incluir el ADR-006; quitar el resto `[cite: 1]`.
5. Sacar del repositorio `.gradle/`, `build/`, `.idea/` y `local.properties`.
6. Registrar en `docs/ia.md` el uso de IA de esta semana con lo rechazado y por qué.
