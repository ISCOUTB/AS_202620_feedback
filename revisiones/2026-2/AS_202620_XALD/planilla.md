# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | XALD |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Integrantes y su usuario de GitHub | Xavier Yesid Garcia Diaz (xaviergarciadiaz20-commits) · Dilan Joan Gonzalez Bejarano (dilanbejarano011) · Luis Estheban Lozano Colmenares (colmenares2007-crypto) · Axel Jair Ruiz Bolano (axeljruiz717-hash) — correspondencias por los correos de los commits (nombres explícitos), por confirmar con el docente |
| URL del sistema desplegado | sin URL (sin despliegue todavía) |
| Ultima revision | 2026-09-02 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `bf81545` · 2026-08-08T13:39:21-05:00 | 5/9 | 3.2 (propuesta) | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `8c37887` · 2026-08-16T13:45:27-05:00 | 1/9 | 1.4 (propuesta) | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `dc38992` · 2026-08-23T22:07:19-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `0205e44` (2026-08-30T23:12:03-05:00) | 4/10 | 2.6 | si |
| 5 | CORTE1 | `9a75929` (2026-08-31T18:20:56-05:00) | 1/12 | no aplica | si |
| 6 | Evidencia S6 · Contextos delimitados y propiedad de datos | | | no aplica | |
| 7 | Evidencia S7 · Contrato de API y prueba de contrato | | | no aplica | |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | | | no aplica | |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 9 | Evidencia S9 · Generación verificada y trazable | | | no aplica | |
| 10 | Segundo corte · reto aplicado sobre el MVP | `corte-2` | | | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Ficha del problema sin usuarios, sin alcance y sin tensiones de calidad enfrentadas | S1 | sí | completar la ficha |
| Restos de edición de herramientas de IA («```[cite: 1]») en `docs/aspectos.md` | S1 | sí | limpiar el archivo |
| Restricciones sin clase legal y con decisiones presentadas como restricciones | S2 | sí | clasificar técnicas/organizativas/legales con origen |
| Escenarios de calidad de seis partes y árbol de utilidad ausentes del repositorio | S2 | sí | subirlos; sin árbol no se puede anclar la matriz comparativa |
| Nombres de ADR fuera de convención (`ADR-NNN.md`) | S2 | sí | renombrar a `NNNN-titulo-en-kebab-case.md` |
| `aspectos.md` con celdas ADR sin enlace y sin referencia al ADR-006 | S3 | sí | enlazar de verdad y añadir la fila del estilo |
| `docs/ia.md` sin entradas del periodo S3 | S3 | sí | registrar el uso de IA de esta semana con rechazados y motivo |
| Artefactos de build versionados (`.gradle/`, `build/`, `XALDAPP/.idea/`, `local.properties`) | S3 | sí | sacar del repo y completar `.gitignore` en la raíz |
| Pruebas del esqueleto sin evidencia de verde (sin CI ni run) | S3 | sí | montar pipeline o aportar el run de `gradlew test` |
| Verificar secciones 3-6, 9, 10 y glosario del arc42 | S4 | si | |
| Confirmar que Cortevertical.kt atraviesa persistencia | S4 | si | |
| Implementar o justificar Backend XALD | S4 | si | |
| Añadir SonarCloud al pipeline | S4 | si | |
| Completar ADR con opciones evaluadas y trazabilidad | S4 | si | |
| Confirmar o crear la etiqueta corte-1 sobre el commit evaluado. | S5 | si | |
| Completar las celdas Pendiente de docs/aspectos.md. | S5 | si | |
| Añadir trazabilidad (requisito, C4, commit, pruebas) a los ADR. | S5 | si | |
| Configurar análisis estático SonarCloud en el pipeline. | S5 | si | |
| Entregar el PDF con diagnóstico, decisión, cambio, medición y trazabilidad. | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_XALD`, público (antes privado: EQUIPOS.md) |
| Estructura mínima | Cumple | seis rutas presentes; `docs/c4/` ahora en su carpeta |
| Convención de nombres de ADR | No cumple | `ADR-001.md`…`ADR-006.md` (deben ser `NNNN-titulo-en-kebab-case.md`) |
| ADR aceptados sin reescribir | Cumple | 001-005 sin ediciones posteriores; 006 editado el mismo día de creación (redacción) |
| `docs/ia.md` al día | No cumple | sin commits en el periodo S3 (último 16-ago) |
| Sin credenciales en el repositorio ni en el historial | Cumple | greps limpios; `local.properties` solo trae ruta de SDK (fuera del versionado de todas formas) |
| Contribución de todos los integrantes | Cumple | 4 identidades = 4 integrantes |
| Pipeline en verde | No cumple | sin pipeline; pruebas presentes pero verde no certificado |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Dilan Joan Gonzalez Bejarano | dilanbejarano011 | 39 | — | — | autor principal; esqueleto y README (23/08) |
| Luis Estheban Lozano Colmenares | colmenares2007-crypto | 17 | — | — | — |
| Xavier Yesid Garcia Diaz | xaviergarciadiaz20-commits | 17 | — | — | ADR-006 y matriz (23/08) |
| Axel Jair Ruiz Bolano | axeljruiz717-hash | 7 | — | — | matriz comparativa (23/08) |

## Preguntas abiertas para la sustentación

- ¿Dónde quedaron los escenarios de calidad de seis partes y el árbol de utilidad de la entrega S2?
- ¿La suite `gradlew.bat -p XALDAPP test` pasa en verde en el entorno del equipo? (el README muestra una salida esperada, no un run verificado)
- ¿Los commits del 23/08 («Create/Delete PROYECTO_XALD») fueron accidentales? Conviene aclararlo.
