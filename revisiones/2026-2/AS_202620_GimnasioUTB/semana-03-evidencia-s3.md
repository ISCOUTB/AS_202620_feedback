# Evidencia S3 · GimnasioUTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `73c1f2406400cd82c0d30f7c24d710db30e328a9` · 2026-08-23T19:38:29-05:00 (`Documentar esqueleto ejecutable y CI en README`) |
| Fecha/hora de revisión | 2026-08-23 21:45 -05:00 (antes del cierre 2026-08-24T00:00-05:00) |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until=2026-08-24T05:00:00Z`; `git ls-tree`; `git show`; `git grep`; API de GitHub solo para los runs de CI |

**Aviso:** la revisión se hizo antes del cierre. Si el equipo empuja antes de medianoche, el hash calificado puede cambiar.

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42_gimnasio_utb.md:116-147` (§4.1-4.3) | Cumple | Estrategia ligada a los escenarios ES1/ES7/ES8 (testabilidad, aislamiento de seguridad, cambio de reglas) y restricciones OC1/OC5; no describe el estilo en abstracto. No usa vocabulario explícito de «tácticas»: las tácticas quedan implícitas por escenario. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/arc42_gimnasio_utb.md:126-135` (§4.2) | Cumple | Filas ligadas a escenarios del equipo (ES1, ES7, ES6, ES8, OC1, OC5) con qué mejora/empeora por estilo; no es tabla genérica. Observación: no cubre ES2-ES5. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-arquitectura-hexagonal.md` | Cumple | Pasa el filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$`. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-arquitectura-hexagonal.md` (Contexto:5-13, Decisión:15-31, Alternativas:33-52, Consecuencias:54-67) | Cumple | Título enuncia la decisión («Adoptar Arquitectura Hexagonal…»); estado «Aceptada»; todas las secciones presentes. |
| Alternativas descartadas con su motivo | `docs/adr/0001-arquitectura-hexagonal.md:35-50` | Cumple | Capas descartada (dominio acoplado a Express/ORM) y Monolito Modular descartado (aislamiento no garantizado por la estructura), ambos con motivo. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` (sin menciones de ADR); escenarios ES1/ES7/ES8 en `docs/arc42_gimnasio_utb.md:211-300` sin enlace al ADR | No cumple | Solo alcanzable desde §4.2/§4.3 (`docs/arc42_gimnasio_utb.md:137,147`). `aspectos.md` sigue en prosa (hallazgo S2) y los escenarios no enlazan al ADR. |
| Arranque con un solo comando documentado en el README | `README.md` («Cómo ejecutar el backend»: `npm install && npm start`) + `package.json:10` (script `start`) | Cumple | Ejecución real: No verificado (regla del kit: no se ejecuta código del estudiante). Comando declarado: `npm install && npm start` (puerto 3000). |
| Prueba automatizada en verde | `tests/health.test.js` + `.github/workflows/ci.yml` (`npm test`); run de CI `success` | Cumple | Últimos 5 runs con conclusión `success`; el del hash calificado: `https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/32677307908` (2026-08-24T00:38:31Z, CI success). |
| Estructura de paquetes correspondiente al estilo del ADR | `src/modules/aforo/{domain,application/ports,infrastructure/{http,persistence}}`, `src/shared`, `src/server.js` | Cumple | Separación hexagonal dominio/puertos/adaptadores por módulo, coherente con el ADR (paquetes vacíos con `.gitkeep`, como pide el esqueleto). |

Recuento: **8 de 9 criterios cumplidos** (sin nota numérica: la fija el profesor).

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | `ISCOUTB/AS_202620_GimnasioUTB`, clonado sin autenticación. |
| Estructura mínima presente | No cumple | `docs/adr/` ya existe; siguen faltando `docs/arc42/` (arc42 en un solo archivo `docs/arc42_gimnasio_utb.md`) y `docs/c4/` (`docs/C4.jpg`). Desviación de ruta, no ausencia del artefacto. |
| Estado calificado identificable | Cumple | Sin etiqueta (no exigible en evidencia semanal); hash y `%cI` registrados arriba. |
| Nombres de ADR según la convención | Cumple | `ls docs/adr` sin salida en el filtro. |
| ADR aceptados no reescritos | Cumple | Único commit `92f4a53` (2026-08-23), creación; sin ediciones posteriores. |
| `docs/ia.md` al día para la semana | No cumple | Entrada S3 (23-ago) con prompt, salida y verificación del equipo, y commits dentro del periodo (`a835f55`, `b49eeda`); pero sigue sin registrar qué se rechazó y por qué (la columna que mira primero el contrato). |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` de secretos sin coincidencias; sin `.env` versionado (solo `.env.example`). |
| Contribución de todos los integrantes | Cumple | 3 personas consolidadas / 3 integrantes: PedroPambi 9; `sebastian-caicedo` 8 + «Sebastian Felipe Caicedo Acosta» 1 (mismo correo `[correo omitido]`, identidad consolidada = 9); RodrigoFacioLince 3. |

## No verificado / pendientes

- Ejecución real del arranque (`npm install && npm start`) y de la prueba local: No verificado por regla del kit (no se ejecuta código del estudiante); la prueba en verde se comprobó con el run de CI (success).
- Si el equipo empuja antes del cierre, repetir sobre el nuevo hash.

## Hallazgos para la planilla

- Gran avance frente a S2: ADR de estilo, §4 con matriz comparativa, esqueleto hexagonal y CI en verde.
- `aspectos.md` sigue en prosa sin enlaces (S2): el ADR no es alcanzable desde ahí ni desde los escenarios ES1/ES7/ES8.
- Estructura mínima: falta montar `docs/arc42/` y `docs/c4/` con el contenido repartido (desviación arrastrada desde S1).
- OC5 sigue diciendo «Equipo de 4 personas» (son 3 según matrícula), también repetido en el ADR.
- `ia.md` sigue sin registrar lo rechazado y su motivo.
- Matriz comparativa no cubre ES2-ES5.
