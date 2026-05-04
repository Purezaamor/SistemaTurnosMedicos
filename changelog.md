# Changelog

## [Unreleased]

---

## [Release Actividad Obligatoria N°2] - 2026-04-17

### Added

- [feature/modelador-diag-casos-uso] Modelado de 5 diagramas de casos de uso en PlantUML y exportación a PNG. PR: [#20](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/20) — @keviineze (Modelador de Casos de Uso)

- [feature/a2-tarjetas-crc] Creación de tarjetas CRC en archivos individuales, incluyendo responsabilidades, colaboradores y pensamiento del objeto. PR: [#51](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/51) — @Purezaamor (Diseñador de Tarjetas CRC)

- [feature/escenarios-cu] Desarrollo de escenarios de casos de uso en archivos individuales con estructura completa y campos obligatorios. PR: [#50](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/50) — @Purezaamor (Especialista en Escenarios)

- [feature/doc-coord-repo-update-readme-md-a2] Actualización de README.md con estructura final del proyecto, índices de navegación y documentación del equipo. PR: [#52](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/52) — @nachonervi-design (Documentador y Coordinador)

---

### Changed

- [feature/a2-tarjetas-crc] Ajuste de tarjetas CRC para reflejar correctamente relaciones del dominio e incorporación de la tarjeta HistorialCambios para auditoría. PR: [#51](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/51) — @Purezaamor (Diseñador de Tarjetas CRC)

- [feature/escenarios-cu] Reestructuración completa de escenarios de casos de uso en carpeta dedicada, con archivos individuales e índice central. PR: [#50](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/50) — @Purezaamor (Especialista en Escenarios)

---

### Fixed


- [fix/review-pr-20] Solicitud de corrección en documentación de IA y modelado de actores en UC02.
  PR: [#20] | Review realizado por @nachonervi-design (Documentador y Coordinador)
- [fix/review/pr-50] Solicitud de cambios en PR de escenarios de casos de uso por falta de estructura requerida, campos obligatorios incompletos, ausencia de documentación de IA.
  PR: [#50] | Review realizado por @nachonervi-design (Documentador y Coordinador)
  - [fix/review/pr-51] Solicitud de cambios en PR de tarjetas CRC por incumplimiento de estructura requerida, falta de documentación de IA, ausencia de actualización de changelog y descripción de PR incompleta.
  PR: [#51] | Review realizado por @nachonervi-design (Documentador y Coordinador)
- [review/pr-20] Request Changes en PR de diagramas de casos de uso por error de sintaxis UML en Caso 2.
  PR: [#20] | Review realizado por @nachonervi-design (Documentador y Coordinador)
- [fix/correcciones-modelador-diagramas-a2] Corregidas relaciones UML `<<extend>>` a `<<include>>` en procesos obligatorios (Cancelar y Registrar turno), corregida estructura de enlaces en `diagramasUML.md` y mejorado el formato de evidencia de IA con sección de iteraciones y bloques de código.
  PR: [#62](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/62) - @keviineze (Modelador Diagramas de Casos de Uso).
- [fix/ia-y-herramientas-agile] Corrección de formato en prompts de IA (triple backtick) y limpieza del archivo herramientas_agile.md. PR: [#73](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/73) — @nachonervi-design (Documentador y Coordinador)

- [fix/diagramas-links-subindices] Corrección de enlaces en diagramas UML: actualización de rutas para apuntar a sub-índices (.md) en lugar de carpetas. PR: [#74](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/74) — @nachonervi-design (Documentador y Coordinador)

- [fix/escenarios-links-formato] Corrección de formato en enlaces de escenarios de casos de uso: actualización al formato completo CU-N - Nombre - Escenario. PR: [#75](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/75) — @nachonervi-design (Documentador y Coordinador)

- [fix/changelog-readme] Corrección final de `changelog.md` y `README.md` según observaciones de revisión. PR: [#59](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/59) — @nachonervi-design (Documentador y Coordinador)

- [fix/especialista-escenarios-casos-uso-a2] Corrección de escenarios: naming, flujo de cancelación y actualización del índice. PR: [#61](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/61) — @Purezaamor (Especialista en Escenarios)

- [fix/correcciones-modelador-diagramas-a2] Corrección de diagramas de casos de uso: ajuste de sintaxis UML, relaciones <<include>> y actualización de PNG e índice. PR: [#62](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/62) — @keviineze (Modelador de Casos de Uso)

- [fix/diseniador-tarjetas-crc-a2] Corrección de tarjetas CRC: incorporación de clases Secretaria y LlegadaPaciente, ajuste de la tarjeta Turno (tipoConsulta y estados) y mejora de Agenda e índices de herramientas agile. PR: [#60](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/60) — @Purezaamor (Diseñador de Tarjetas CRC)

- [fix/backport-modelador-a2] Corrección de diagrama cancelar-turno (<<include>>), actualización de índice diagramasUML.md y documentación IA modelador. PR: [#66](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/66) — @keviineze (Modelador de Diagramas de CU)

- [fix/changelog-a1-formato-final] Corrección del formato en la sección de la Actividad Obligatoria N°1: normalización de entradas en `### Changed` y `### Fixed` según Keep a Changelog (PR links, autores y estructura). PR: [#68](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/68) — @nachonervi-design (Documentador y Coordinador)

- [fix/herramientas-agile-formato] Aplicación de correcciones finales de revisión: normalización de `herramientas_agile.md`, corrección del índice en `tarjetas_crc.md` y mejora de la documentación de IA (CRC y escenarios: prompts, contexto, iteraciones y outputs). PR: [#67](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/67) — @nachonervi-design (Documentador y Coordinador)

- [fix/ia-documentador-prompts] Corrección de formato en documentación de IA: se envuelven los prompts en bloques de código triple backtick en `ia/a2/documentador-coordinador.md`. PR: [#71](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/71) — @nachonervi-design (Documentador y Coordinador)

- [fix/limpieza-changelog-a2] Corrección de `changelog.md` según observaciones de revisión. PR: [#70](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/70) - @keviineze (Modelador de Diagramas de Casos de Uso).

- [fix/prompts-ia-y-changelog-final] Corrección final de formato en documentación de IA: prompts envueltos en bloques de código triple backtick en archivos de CRC, escenarios y documentador; ajuste de entradas faltantes e incorrectas en `changelog.md`. PR: [#72](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/72) — @nachonervi-design (Documentador y Coordinador)

- [fix/correcciones-finales-rc] Aplicación de correcciones finales de revisión (RC): ajustes en herramientas_agile, tarjetas CRC (Turno y herencia), escenarios de casos de uso, enlaces de diagramas UML y documentación de IA. PR: [#69](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/69) — @nachonervi-design (Documentador y Coordinador)

- [fix/registro-correcciones-finales] Registro final de correcciones aplicadas en documentación de IA, enlaces de diagramas UML y escenarios de casos de uso. PR: [#77](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/77) — @nachonervi-design (Documentador y Coordinador)- [fix/registro-correcciones-finales] Registro final de correcciones aplicadas en documentación de IA, enlaces de diagramas UML y escenarios de casos de uso. PR: [#77](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/77) — @nachonervi-design (Documentador y Coordinador)


---

## [Release Actividad Obligatoria N°1] - 2026-03-25

### Added


- [feature/analista-requerimientos] Normalización de 5 RF y 5 RNF; definición de alcance MVP; enlace a NotebookLM. PR: [#8](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/8) — @nachonervi-design (Analista de Requerimientos)

- [feature/disenio-clases] Creación del diagrama de clases inicial en Excalidraw y exportación a PNG. PR: [#7](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/7) — @lucastol-dev (Diseñador de Clases)

- [feature/diseñador-de-clases-iniciales-correccion] Corrección de relaciones y atributos en el boceto de clases. PR: [#18](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/18) — @lucastol-dev (Diseñador de Clases)

- [feature/doc-coord-repo] Creación de estructura de carpetas, README institucional y anexos. PR: [#10](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/10) — @Purezaamor (Documentador y Coordinador)

---

### Changed


- [feature/doc-coord-repo] Actualización de la carátula con datos completos de los integrantes en `README.md`. PR: [#36](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/36) — @Purezaamor (Documentador y Coordinador)

- [feature/modelador-casos-uso] Integración de la vista previa de diagramas en `introduccion.md`. PR: [#37](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/37) — @keviineze (Modelador de Casos de Uso)

---

### Fixed
- Corrección del workflow Git
- Corrección de PR templates
- Ajustes en diagramas y relaciones
- Limpieza de merge conflicts
- [fix/corrige RC finales (prompts IA + herramientas_agile limpio)] Corrección de prompts IA y limpieza de herramientas_agile.md. PR: [#73](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/73)

- [fix/corrige links de diagramas UML a sub-indices] Corrección de navegación en diagramas UML. PR: [#74](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/74)

- [fix/corrige texto de links en escenarios (formato CU completo)] Corrección del índice de escenarios. PR: [#75](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/75)

- [fix/workflow-git] Corrección del flujo de trabajo utilizando git en lugar del editor web de GitHub. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) — @Purezaamor (Documentador y Coordinador)

- [fix/pr-templates] Incorporación de templates de Pull Request para ramas feature y release. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) — @Purezaamor (Documentador y Coordinador)

- [fix/release-body] Actualización del body de la PR de release con estructura requerida. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) — @Purezaamor (Documentador y Coordinador)

- [fix/issues-cierre] Cierre de issues pendientes (#12, #15, #17). PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) — @Purezaamor (Documentador y Coordinador)

- [fix/reviews-ia] Mejora en las revisiones con asistencia de IA, agregando observaciones más específicas. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) — @Purezaamor (Documentador y Coordinador)

- [fix/excalidraw-recrear] Recreación del archivo excalidraw y subida correcta de formato en PNG. PR: [#41](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/41) — @keviineze (Modelador de Casos de Uso)

- [fix/changelog] Coordinación y consolidación del changelog final. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) — @Purezaamor (Documentador y Coordinador)

- [fix/notebooklm-link] Corrección de sintaxis del enlace de NotebookLM en `introduccion.md`. PR: [#30](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/30) — @keviineze (Modelador de Casos de Uso)

- [fix/actores-cu] Corrección de nombres de actores en casos de uso en `introduccion.md`. PR: [#37](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/37) — @keviineze (Modelador de Casos de Uso)

- [fix/diagrama-render] Corrección de la ruta de visualización del diagrama de clases (.excalidraw → .png). PR: [#36](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/36) — @Purezaamor (Documentador y Coordinador)

- [fix/merge-artifacts] Limpieza de artefactos de merge en `changelog.md`. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) — @Purezaamor (Documentador y Coordinador)

- [fix/diagrama-tag] Corrección de error de renderizado (tag duplicado) en el diagrama de clases. PR: [#40](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/40) — @keviineze (Modelador de Casos de Uso)
