# Semana 9 · Generación verificada y trazable · ShareU

Revisión definitiva; reemplaza la preliminar.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_ShareU |
| Rama principal remota | `master` |
| Estado revisado | `39508608eae4c1a56a5e4fc11a055bf6afb2c003` en `origin/master` (2026-09-28T19:56:57-05:00) |
| Línea base S8 | `332f67f726969e0c73b98dd4705aea6c37e5603b` |
| Punta actual / S10 preliminar | `39508608eae4c1a56a5e4fc11a055bf6afb2c003` · 2026-09-28T19:56:57-05:00 |
| Cierre S9 | 2026-10-05T05:00:00Z |
| Cierre eventual S10 | 2026-10-12T05:00:00Z |
| Revisión | 2026-10-06 (UTC) |

## Alcance y método

Se consultó la rama principal remota mediante git y se eligió su último commit anterior o igual al cierre S9; no se consultaron etiquetas. S10 es preliminar y usa la punta actual. Se comparó S9 con la línea base S8; no se vuelven a puntuar entregas anteriores por existir. No se ejecutó código, pruebas ni despliegues del equipo. Los registros de ejecución del repositorio se distinguen de la comprobación externa. Por exclusión docente no se abrieron PDFs ni se evaluó su presencia, contenido, extensión o ubicación.

La consulta general de Actions se verificó mediante GET /actions/runs (100 registros como máximo); se distinguen el hash, la rama y la conclusión de cada run. Un intento inicial filtrado a pull requests no se usó para decidir. No se consultaron jobs ni logs adicionales.

El delta S8→S9 contiene 4 commits. Cuatro commits: ajustes de CI/frontend y corrección de frontera con fachada, pruebas, ADR 0008/0009 y evidencia S9.

## Matriz de la ficha S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [app/administracion/service.py:1–8](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/administracion/service.py#L1-L8) y [app/busqueda/service.py:5–6](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/busqueda/service.py#L5-L6): fachada e import corregido nuevos en 3950860; [docs/ia/ia.md:33](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/ia/ia.md#L33) atribuye apoyo de IA. Se evalúa esta corrección del periodo, no la métrica previa de S8. |
| Cadena completa navegable para esa porción | No cumple | [docs/aspectos/aspectos.md:50–56](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/aspectos/aspectos.md#L50-L56). La fila nueva enlaza ADR, código, pruebas y evidencia, pero la tabla conserva seis columnas: faltan ID y, sobre todo, el eslabón C4 de la cadena exigida. La referencia indirecta en el ADR no completa una fila aspecto→requisito→C4→ADR→código→prueba→medición. |
| ADR con la decisión argumentada por el equipo | Cumple | [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:9–86](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L9-L86). Compara cuatro alternativas y decide fachada con restricciones de costo cero, propiedad y simplicidad; el estado Propuesto en líneas 1–4 deja pendiente ratificación del equipo, que debe aclararse. |
| Prueba que falla ante el defecto que cubre | Cumple | [docs/evidencia/evidencia-s9.md:18–43](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L18-L43). Procedimiento documentado introduce tres defectos y sus fallos y declara reversión; los archivos de prueba existen. La ficha permite este procedimiento. No se ejecutaron; CI rojo no confirma el 12 passed local. |
| Medición del escenario asociado | Cumple | [docs/evidencia/evidencia-s9.md:18–43](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L18-L43) y [tests/test_escenario_usabilidad.py:1–33](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/tests/test_escenario_usabilidad.py#L1-L33). Se reporta máximo 2 interacciones frente al umbral 3 para cinco documentos. Alcance técnico sintético, no prueba con usuarios ni despliegue. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | [docs/ia/ia.md:33](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/ia/ia.md#L33). Registra aceptación de fachada, corrección y cuatro rechazos técnicos. La fila 8 mantiene un marcador pese a declararlo resuelto; se señala sin negar la entrada S9. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/evidencia/evidencia-s9.md:50–61](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L50-L61) y [tests/test_fronteras.py:15–26](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/tests/test_fronteras.py#L15-L26). E1 corregido con fachada; E2 propiedad documentada; E3/E4 explícitamente pendientes. Lectura confirma que búsqueda consume administracion.service. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [docs/evidencia/evidencia-s9.md:63–73](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L63-L73). No cambia requirements ni package.json respecto a S8; la evidencia NUEVA de S9 audita 26 versiones PyPI y 7 npm. Consulta externa el 2026-10-06 confirma todas esas versiones, incluidos [PyYAML](https://pypi.org/pypi/pyyaml/6.0.2/json), [jsonschema](https://pypi.org/pypi/jsonschema/4.23.0/json) y [Next](https://registry.npmjs.org/next/14.2.15). Ausencia de altas no es incumplimiento. Next existe y es legítimo, pero el registro advierte vulnerabilidad: corrección de seguridad pendiente. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | [app/frontend/.env.example:1](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/frontend/.env.example#L1) y [.github/workflows/tests.yml:22–32](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/.github/workflows/tests.yml#L22-L32). Barrido actual y patrones históricos sin credenciales reales identificadas; variables de GitHub y URL local no son secretos. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | [docs/adr/0009-no-incorporar-componente-generativo.md:13–58](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0009-no-incorporar-componente-generativo.md#L13-L58). La decisión escrita de no incorporarlo está razonada por costo, disponibilidad y alcance; no hay LLM en ejecución. El encabezado aún Propuesto requiere ratificación expresa. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon anónimo público de https://github.com/ISCOUTB/AS_202620_ShareU; organización y nombre conformes. |
| Estructura mínima presente | No cumple | [README.md:191–200](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md#L191-L200). Aspectos e IA existen en subcarpetas, no docs/aspectos.md y docs/ia.md. Desviación de ruta, no ausencia. |
| Estado calificado identificable | Cumple | origin/master 39508608eae4c1a56a5e4fc11a055bf6afb2c003, 2026-09-28T19:56:57-05:00; último ≤ cierre S9 y punta preliminar S10. |
| Nombres de ADR según la convención | Cumple | Los seis ADR Markdown 0001–0004, 0008 y 0009 siguen NNNN-kebab-case; [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:1–4](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L1-L4). Archivos PDF excluidos expresamente del criterio por decisión docente. |
| ADR aceptados no reescritos | Cumple | Historial de ADR leído: 0002/0003/0004/0008/0009 creados una vez; ADR-0001 solo movimientos de ruta sin edición de contenido. [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:1–7](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L1-L7) nuevo en 3950860. |
| docs/ia.md al día para la semana | Cumple | [docs/ia/ia.md:33](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/ia/ia.md#L33). Nueva entrada del periodo S9; ruta desviada evaluada por contenido. Aún no hay actividad adicional S10. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/tests.yml:22–32](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/.github/workflows/tests.yml#L22-L32). Consulta general Actions confirma [run 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458) en el hash revisado, conclusión failure (2026-09-29T00:59:44Z). Sin run exitoso de scanner y Quality Gate de esta revisión acreditados. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del contrato sobre HEAD, docs y ejemplos sin credenciales identificadas; sin .env versionado; búsqueda histórica de patrones de claves privadas/tokens de alta confianza sin coincidencias. [docs/evidencia/evidencia-s9.md:75–80](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L75-L80). Resultado acotado al barrido, no garantía absoluta. |
| Contribución de todos los integrantes | No verificado | 50 commits en cuatro grupos por identidad de correo; dos firmas se consolidan por coincidencia exacta, sin publicar correos. No se deduce la correspondencia completa con los cuatro integrantes solo por nombres de cuenta; validación docente pendiente, sin afirmar ausencia individual. |

## Estado global del proyecto (overall)

La punta actual de `master` es `39508608eae4c1a56a5e4fc11a055bf6afb2c003` (2026-09-28T19:56:57-05:00) y coincide con S9 congelada: no hay commits tardíos hasta esta revisión. Hay una corrección de erosión comprobable y medición sintética explícita. La cadena conserva una omisión de C4. El pipeline sigue fallando y la URL de salud no entrega el health esperado; la infraestructura y decisiones de plataforma documentadas siguen ausentes.

### Hallazgos abiertos

- Identificar el escenario oficialmente asignado y su línea base medida para S10.
- Pipeline de la punta en rojo: [run 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458).
- Health de la URL declarada respondió 404; confirmar URL vigente y restablecer despliegue.
- Completar ID y C4 en la tabla de trazabilidad; normalizar rutas de aspectos e IA. [docs/aspectos/aspectos.md:50–56](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/aspectos/aspectos.md#L50-L56)
- Versionar los archivos declarados ausentes o corregir documentos: Dockerfile, render.yaml, ADR 0005–0007 y prueba de contrato. [docs/evidencia/evidencia-s9.md:56–61](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L56-L61)
- Actualizar Next a una versión corregida tras revisar el aviso oficial: el registro de next 14.2.15 confirma advertencia de seguridad. [app/frontend/package.json:11–14](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/frontend/package.json#L11-L14)
- Ratificar ADR-0008/0009 y resolver marcadores documentales sin atribuir al equipo decisiones pendientes.

### Hallazgos cerrados o corregidos en esta revisión

- El cruce búsqueda→interno de administración está corregido mediante fachada y prueba de fronteras. [app/busqueda/service.py:5–6](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/busqueda/service.py#L5-L6)
- Se corrige el hallazgo preliminar de dependencias: no añadir paquetes no obliga a fallar; hay auditoría nueva del periodo y existencia contrastada en registros oficiales.
- Se excluye el hallazgo de convención sobre PDF por decisión docente; los ADR Markdown sí siguen la convención.

## Recuento y nota sugerida

**9 de 10 criterios Cumple. Propuesta al docente: 4.6 = 1 + 4 × (9/10).** La nota final la fija el profesor en Moodle; la matriz transversal no entra en esta fórmula.

## Próximo paso

La corrección de frontera está implementada y respaldada por pruebas que documentan el fallo esperado. Completen el eslabón C4 en la fila de aspectos y ratifiquen los ADR propuestos. La auditoría de dependencias es válida aunque no hayan añadido paquetes; atiendan la vulnerabilidad registrada de Next y las referencias a archivos todavía ausentes.

## Comprobación independiente de registros (2026-10-06)

Se consultaron las 26 versiones de requirements.txt y los 7 paquetes directos de frontend; todas existen. Esto verifica identidad/versiones, no ausencia de vulnerabilidades. No se instalaron paquetes.

- [annotated-types==0.8.0](https://pypi.org/pypi/annotated-types/0.8.0/json): annotated-types 0.8.0
- [anyio==4.15.1](https://pypi.org/pypi/anyio/4.15.1/json): anyio 4.15.1
- [attrs==26.1.0](https://pypi.org/pypi/attrs/26.1.0/json): attrs 26.1.0
- [certifi==2026.7.22](https://pypi.org/pypi/certifi/2026.7.22/json): certifi 2026.7.22
- [click==8.5.0](https://pypi.org/pypi/click/8.5.0/json): click 8.5.0
- [fastapi==0.115.0](https://pypi.org/pypi/fastapi/0.115.0/json): fastapi 0.115.0
- [h11==0.16.0](https://pypi.org/pypi/h11/0.16.0/json): h11 0.16.0
- [httpcore==1.0.9](https://pypi.org/pypi/httpcore/1.0.9/json): httpcore 1.0.9
- [httpx==0.27.2](https://pypi.org/pypi/httpx/0.27.2/json): httpx 0.27.2
- [idna==3.20](https://pypi.org/pypi/idna/3.20/json): idna 3.20
- [iniconfig==2.3.0](https://pypi.org/pypi/iniconfig/2.3.0/json): iniconfig 2.3.0
- [jsonschema==4.23.0](https://pypi.org/pypi/jsonschema/4.23.0/json): jsonschema 4.23.0
- [jsonschema-specifications==2025.9.1](https://pypi.org/pypi/jsonschema-specifications/2025.9.1/json): jsonschema-specifications 2025.9.1
- [packaging==26.3](https://pypi.org/pypi/packaging/26.3/json): packaging 26.3
- [pluggy==1.6.0](https://pypi.org/pypi/pluggy/1.6.0/json): pluggy 1.6.0
- [pydantic==2.13.5](https://pypi.org/pypi/pydantic/2.13.5/json): pydantic 2.13.5
- [pydantic-core==2.46.5](https://pypi.org/pypi/pydantic-core/2.46.5/json): pydantic_core 2.46.5
- [pytest==8.3.3](https://pypi.org/pypi/pytest/8.3.3/json): pytest 8.3.3
- [pyyaml==6.0.2](https://pypi.org/pypi/pyyaml/6.0.2/json): PyYAML 6.0.2
- [referencing==0.37.0](https://pypi.org/pypi/referencing/0.37.0/json): referencing 0.37.0
- [rpds-py==2026.6.3](https://pypi.org/pypi/rpds-py/2026.6.3/json): rpds-py 2026.6.3
- [sniffio==1.3.1](https://pypi.org/pypi/sniffio/1.3.1/json): sniffio 1.3.1
- [starlette==0.38.6](https://pypi.org/pypi/starlette/0.38.6/json): starlette 0.38.6
- [typing-extensions==4.16.0](https://pypi.org/pypi/typing-extensions/4.16.0/json): typing-extensions 4.16.0
- [typing-inspection==0.4.4](https://pypi.org/pypi/typing-inspection/0.4.4/json): typing-inspection 0.4.4
- [uvicorn==0.32.0](https://pypi.org/pypi/uvicorn/0.32.0/json): uvicorn 0.32.0
- [next==14.2.15](https://registry.npmjs.org/next/14.2.15): next 14.2.15 · advertencia de seguridad del registro
- [react==18.3.1](https://registry.npmjs.org/react/18.3.1): react 18.3.1
- [react-dom==18.3.1](https://registry.npmjs.org/react-dom/18.3.1): react-dom 18.3.1
- [typescript==5.6.3](https://registry.npmjs.org/typescript/5.6.3): typescript 5.6.3
- [@types/node==20.16.11](https://registry.npmjs.org/@types%2Fnode/20.16.11): @types/node 20.16.11
- [@types/react==18.3.11](https://registry.npmjs.org/@types%2Freact/18.3.11): @types/react 18.3.11
- [@types/react-dom==18.3.0](https://registry.npmjs.org/@types%2Freact-dom/18.3.0): @types/react-dom 18.3.0
