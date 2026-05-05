Changelog
[Release Primer Parcial] - 2026-05-04
Added
[feature/esp-isp-add-anexo-isp] Análisis de Principio ISP y diseño de diagrama UML para Segregación de Interfaces. PR: #92 - @keviineze (Especialista en Segregación de Interfaces).
[Release Actividad Obligatoria N°2] - 2026-04-17
Added
[feature/modelador-diag-casos-uso] Modelado de 5 diagramas de casos de uso en PlantUML y exportación a PNG. PR: #20 — @keviineze (Modelador de Casos de Uso)

[feature/a2-tarjetas-crc] Creación de tarjetas CRC en archivos individuales, incluyendo responsabilidades, colaboradores y pensamiento del objeto. PR: #51 — @Purezaamor (Diseñador de Tarjetas CRC)

[feature/doc-coord-repo-update-readme-md-a2] Actualización de README.md con estructura final del proyecto, índices de navegación y documentación del equipo. PR: #52 — @nachonervi-design (Documentador y Coordinador)

Changed
[feature/escenarios-cu] Reestructuración completa de escenarios de casos de uso en carpeta dedicada, con archivos individuales e índice central. PR: #50 — @Purezaamor (Especialista en Escenarios)
Fixed
[fix/ia-y-herramientas-agile] Corrección de formato en prompts de IA (triple backtick) y limpieza del archivo herramientas_agile.md. PR: #73 — @nachonervi-design (Documentador y Coordinador)

[fix/diagramas-links-subindices] Corrección de enlaces en diagramas UML: actualización de rutas para apuntar a sub-índices (.md) en lugar de carpetas. PR: #74 — @nachonervi-design (Documentador y Coordinador)

[fix/escenarios-links-formato] Corrección de formato en enlaces de escenarios de casos de uso: actualización al formato completo CU-N - Nombre - Escenario. PR: #75 — @nachonervi-design (Documentador y Coordinador)

[fix/changelog-readme] Corrección final de changelog.md y README.md según observaciones de revisión. PR: #59 — @nachonervi-design (Documentador y Coordinador)

[fix/especialista-escenarios-casos-uso-a2] Corrección de escenarios: naming, flujo de cancelación y actualización del índice. PR: #61 — @Purezaamor (Especialista en Escenarios)

[fix/correcciones-modelador-diagramas-a2] Corrección de diagramas de casos de uso: ajuste de sintaxis UML, relaciones <> y actualización de PNG e índice. PR: #62 — @keviineze (Modelador de Casos de Uso)

[fix/diseniador-tarjetas-crc-a2] Corrección de tarjetas CRC: incorporación de clases Secretaria y LlegadaPaciente, ajuste de la tarjeta Turno (tipoConsulta y estados) y mejora de Agenda e índices de herramientas agile. PR: #60 — @Purezaamor (Diseñador de Tarjetas CRC)

[fix/backport-modelador-a2] Corrección de diagrama cancelar-turno (<>), actualización de índice diagramasUML.md y documentación IA modelador. PR: #66 — @keviineze (Modelador de Casos de Uso)

[fix/changelog-a1-formato-final] Corrección del formato en la sección de la Actividad Obligatoria N°1: normalización de entradas en ### Changed y ### Fixed según Keep a Changelog (PR links, autores y estructura). PR: #68 — @nachonervi-design (Documentador y Coordinador)

[fix/herramientas-agile-formato] Aplicación de correcciones finales de revisión: normalización de herramientas_agile.md, corrección del índice en tarjetas_crc.md y mejora de la documentación de IA (CRC y escenarios: prompts, contexto, iteraciones y outputs). PR: #67 — @nachonervi-design (Documentador y Coordinador)

[fix/ia-documentador-prompts] Corrección de formato en documentación de IA: se envuelven los prompts en bloques de código triple backtick en ia/a2/documentador-coordinador.md. PR: #71 — @nachonervi-design (Documentador y Coordinador)

[fix/limpieza-changelog-a2] Corrección de changelog.md según observaciones de revisión. PR: #70 — @keviineze (Modelador de Casos de Uso)

[fix/prompts-ia-y-changelog-final] Corrección final de formato en documentación de IA: prompts envueltos en bloques de código triple backtick en archivos de CRC, escenarios y documentador; ajuste de entradas faltantes e incorrectas en changelog.md. PR: #72 — @nachonervi-design (Documentador y Coordinador)

[fix/correcciones-finales-rc] Aplicación de correcciones finales de revisión (RC): ajustes en herramientas_agile, tarjetas CRC (Turno y herencia), escenarios de casos de uso, enlaces de diagramas UML y documentación de IA. PR: #69 — @nachonervi-design (Documentador y Coordinador)

[fix/modelador-casos-uso-crc] Corrección y refactorización del modelo de tarjetas CRC: unificación de atributos en Persona, redistribución de responsabilidades, incorporación de HistorialCambios y alineación con requisitos funcionales. PR: #80 — @keviineze (Modelador de Casos de Uso)

[fix/changelog-duplicados] Eliminación de líneas duplicadas en changelog.md para mantener consistencia y cumplimiento de formato en la entrega final de la Actividad Obligatoria N°2. PR: #78 — @nachonervi-design (Documentador y Coordinador)

[fix/herramientas agile formato nueva] Corrección de formato en herramientas agile. PR: #85

[fix/modelador casos usoA2] Ajustes en tarjetas CRC y documentación. PR: #84

[fix/changelog final ajustes] Ajustes finales en changelog. PR: #82

[fix/herramientas agile formato] Corrección previa de herramientas agile. PR: #76

[feature/escenarios cu] Implementación de escenarios de casos de uso. PR: #57

[fix/correcciones finales (UML, CRC, changelog y limpieza)] Resolución de conflictos, limpieza de duplicados, corrección de índices y actualización final del changelog. PR: #86

[fix/correcciones finales adicionales] Ajustes finales sobre UML, conflictos y consistencia general del repositorio. PR: #87

## [Release Primer Parcial] - 2026-05-04

### ISP (ya existente)
... tu contenido ISP ...

---

### OCP + LSP (NUEVO)

#### Added

[feature/esp-extension-ocp-lsp] Aplicación de principios OCP y LSP en el sistema de turnos médicos. PR: #91 — @Purezaamor

- Refactor de la clase Turno aplicando OCP
  - TurnoPresencial
  - TurnoVirtual
  - TurnoDomicilio

- Aplicación de LSP en la jerarquía Persona:
  - Paciente
  - Medico
  - Secretaria

- Diagramas UML en PlantUML y PNG

- Documentación:
  - ia/primer-parcial/especialista-ocp.md
  - ia/primer-parcial/especialista-lsp.md
  - anexos/principios-solid/02-ocp.md
  - anexos/principios-solid/03-lsp.md

#### Changed

- Ajustes de diseño del modelo de turnos
- Integración con Agenda y dominio existente

#### Result

Sistema extensible y consistente bajo principios SOLID.

[Release Actividad Obligatoria N°1] - 2026-03-25
Added
[feature/analista-requerimientos] Normalización de 5 RF y 5 RNF; definición de alcance MVP; enlace a NotebookLM. PR: #8 — @nachonervi-design (Analista de Requerimientos)

[feature/disenio-clases] Creación del diagrama de clases inicial en Excalidraw y exportación a PNG. PR: #7 — @lucastol-dev (Diseñador de Clases)

[fix/diseñador-de-clases-iniciales] Corrección de relaciones y atributos en el boceto de clases. PR: #18 — @lucastol-dev (Diseñador de Clases)

[feature/doc-coord-repo] Creación de estructura de carpetas, README institucional y anexos. PR: #10 — @Purezaamor (Documentador y Coordinador)

Changed
[feature/doc-coord-repo] Actualización de la carátula con datos completos de los integrantes en README.md. PR: #36 — @Purezaamor (Documentador y Coordinador)

[feature/modelador-casos-uso] Integración de la vista previa de diagramas en introduccion.md. PR: #37 — @keviineze (Modelador de Casos de Uso)

Fixed
[fix/workflow-git] Corrección del flujo de trabajo utilizando git en lugar del editor web de GitHub. PR: #35 — @Purezaamor (Documentador y Coordinador)

[fix/diagrama-clases] Corrección del diagrama de clases para ajustarlo al dominio del consultorio. PR: #41 — @keviineze (Modelador de Casos de Uso)

[fix/notebooklm-link] Corrección de sintaxis del enlace de NotebookLM en introduccion.md. PR: #30 — @keviineze (Modelador de Casos de Uso)

[fix/diagrama-tag] Corrección de error de renderizado (tag duplicado) en el diagrama de clases. PR: #40 — @keviineze (Modelador de Casos de Uso)  