# Changelog

<<<<<<< HEAD
## [Unreleased]

---
=======
<<<<<<< HEAD
## [Unreleased]

## [Actividad Obligatoria N°2]

### Notes

- [contingencia-equipo] Debido a la baja cantidad de integrantes disponibles en el equipo, Alejo Guerricabeitia asumió dos roles en la Actividad Obligatoria N°2: Diseñador de Tarjetas CRC y Especialista en Escenarios.

### Added

- [feature/modelador-diag-casos-uso] Creación de diagramas de casos de uso en PlantUML (.puml y .png).
  PR: [#20] https://github.com/Purezaamor/SistemaTurnosMedicos/pull/20 | Issue: [#19] https://github.com/Purezaamor/SistemaTurnosMedicos/issues/19

- [feature/diseniador-tarjetas-crc] Creación de tarjetas CRC para las clases del sistema.
  PR: [#51] https://github.com/Purezaamor/SistemaTurnosMedicos/pull/51 | Issue: [#53] https://github.com/Purezaamor/SistemaTurnosMedicos/issues/54

- [feature/especialista-escenarios] Definición de escenarios de casos de uso.
  PR: [#50] https://github.com/Purezaamor/SistemaTurnosMedicos/pull/50 | Issue: [#54] https://github.com/Purezaamor/SistemaTurnosMedicos/issues/53

- [feature/doc-coord-repo-readme-md-a2] Documentación del uso de IA en ia/a2/ y preparación del flujo de integración.
  PR: [#49] https://github.com/Purezaamor/SistemaTurnosMedicos/pull/49 | Issue: [#48] https://github.com/Purezaamor/SistemaTurnosMedicos/issues/48

### Changed

- [feature/doc-coord-repo-readme-md-a2] Actualización del README.md integrando Actividad Obligatoria N°2.   PR: [#49] https://github.com/Purezaamor/SistemaTurnosMedicos/pull/49 | Issue: [#48] https://github.com/Purezaamor/SistemaTurnosMedicos/issues/48

- [review/pr-20] Aprobación de PR de diagramas de casos de uso tras validación de estructura, coherencia y documentación.
  PR: [#20] | Review realizado por @nachonervi-design (Documentador y Coordinador)
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
>>>>>>> origin/develop

## [Release Actividad Obligatoria N°2] - 2026-04-17

### Added

<<<<<<< HEAD
- [feature/modelador-diag-casos-uso] Modelado de 5 diagramas de casos de uso en PlantUML y exportación a PNG. PR: [#20](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/20) — @keviineze (Modelador de Casos de Uso)

- [feature/a2-tarjetas-crc] Creación de tarjetas CRC en archivos individuales, incluyendo responsabilidades, colaboradores y pensamiento del objeto. PR: [#51](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/51) — @Purezaamor (Diseñador de Tarjetas CRC)

- [feature/escenarios-cu] Desarrollo de escenarios de casos de uso en archivos individuales con estructura completa y campos obligatorios. PR: [#50](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/50) — @Purezaamor (Especialista en Escenarios)

- [feature/doc-coord-repo-update-readme-md-a2] Actualización de README.md con estructura final del proyecto, índices de navegación y documentación del equipo. PR: [#52](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/52) — @nachonervi-design (Documentador y Coordinador)

---

### Changed

- [feature/modelador-diag-casos-uso] Corrección de sintaxis UML y consistencia de render en diagramas de casos de uso. PR: [#20](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/20) — @keviineze (Modelador de Casos de Uso)

- [feature/a2-tarjetas-crc] Ajuste de tarjetas CRC para reflejar correctamente relaciones del dominio e incorporación de la tarjeta HistorialCambios para auditoría. PR: [#51](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/51) — @Purezaamor (Diseñador de Tarjetas CRC)

- [feature/escenarios-cu] Reestructuración completa de escenarios de casos de uso en carpeta dedicada, con archivos individuales e índice central. PR: [#50](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/50) — @Purezaamor (Especialista en Escenarios)

---

### Fixed

- [fix/changelog-readme] Corrección final de `changelog.md` y `README.md` según observaciones de revisión. PR: [#59](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/59) — @nachonervi-design (Documentador y Coordinador)

- [fix/especialista-escenarios-casos-uso-a2] Corrección de escenarios: naming, flujo de cancelación y actualización del índice. PR: [#61](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/61) — @Purezaamor (Especialista en Escenarios)

- [fix/correcciones-modelador-diagramas-a2] Corrección de diagramas de casos de uso: ajuste de sintaxis UML, relaciones <<include>> y actualización de PNG e índice. PR: [#62](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/62) — @keviineze (Modelador de Casos de Uso)

- [fix/diseniador-tarjetas-crc-a2] Corrección de tarjetas CRC: incorporación de Secretaria y LlegadaPaciente, mejora de Turno (tipoConsulta y estados) y ajuste de Agenda e índices. PR: [#60](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/60) — @Purezaamor (Diseñador de Tarjetas CRC)

---
=======
- [feature/modelador-diag-casos-uso-update-use-case-1] Modelado de Diagramas de Casos de Uso y Documentación de IA, junto con las carpetas requeridas, Actividad 2. PR: [#20](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/20) - @keviineze (Modelador de Diagramas de Casos de Uso)


### Changed

- [feature/modelador-diag-casos-uso-update-use-case-1] Corrección del Diagrama de Casos de Uso 2 "Reprogramar Turno Existente" y breve agregado de explicacion sobre "Ajustes Realizados" en ia\a2\modelador-diagramas-casos-uso.md 

>>>>>>> origin/develop

## [Release Actividad Obligatoria N°1] - 2026-03-25

### Added

<<<<<<< HEAD
- [feature/analista-requerimientos] Normalización de 5 RF y 5 RNF; definición de alcance MVP. PR: [#8](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/8)

- [feature/disenio-clases] Creación del diagrama de clases inicial. PR: [#7](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/7)

- [feature/diseñador-de-clases-iniciales-correccion] Corrección de relaciones y atributos. PR: [#18](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/18)

- [feature/doc-coord-repo] Creación de estructura del repositorio. PR: [#10](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/10)

---

### Changed

- Actualización de README.md con datos del equipo
- Integración de diagramas en introduccion.md

---

### Fixed

- Corrección del workflow Git
- Corrección de PR templates
- Ajustes en diagramas y relaciones
- Limpieza de merge conflicts
- [fix/corrige RC finales (prompts IA + herramientas_agile limpio)] Corrección de prompts IA y limpieza de herramientas_agile.md. PR: [#73](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/73)

- [fix/corrige links de diagramas UML a sub-indices] Corrección de navegación en diagramas UML. PR: [#74](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/74)

- [fix/corrige texto de links en escenarios (formato CU completo)] Corrección del índice de escenarios. PR: [#75](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/75)
=======
- [feature/analista-requerimientos] Normalización de 5 RF y 5 RNF; definición de alcance MVP; enlace a NotebookLM.
  PR: [#8](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/8) | Issue: [#6](https://github.com/Purezaamor/SistemaTurnosMedicos/issues/6)

- [feature/disenio-clases] Creación del diagrama de clases inicial en Excalidraw y exportación a PNG.
  PR: [#7](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/7) | Issue: [#8](https://github.com/Purezaamor/SistemaTurnosMedicos/issues/8)

- [feature/diseñador-de-clases-iniciales-correccion] Corrección de relaciones y atributos en el boceto de clases (@lucastol-dev).
  PR: [#18](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/18) | Issue: [#9](https://github.com/Purezaamor/SistemaTurnosMedicos/issues/9)

- [feature/doc-coord-repo] Creación de estructura de carpetas, README institucional y anexos.
  PR: [#10](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/10) | Issue: [#11](https://github.com/Purezaamor/SistemaTurnosMedicos/issues/11)

### Changed
- [feature/doc-coord-repo] Actualización de la carátula con datos completos de los integrantes en `README.md`.
- [feature/modelador-casos-uso] Integración de la vista previa de diagramas en `introduccion.md`.

### Fixed

- [fix/workflow-git] Corrección del flujo de trabajo utilizando git en lugar del editor web de GitHub. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) @Purezaamor (Coordinador)


### Added

- [feature/analista-requerimientos] Normalización de 5 RF y 5 RNF; definición de alcance MVP; enlace a NotebookLM.
  PR: [#8](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/8) | Issue: [#6](https://github.com/Purezaamor/SistemaTurnosMedicos/issues/6)

- [feature/disenio-clases] Creación del diagrama de clases inicial en Excalidraw y exportación a PNG.
  PR: [#7](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/7) | Issue: [#8](https://github.com/Purezaamor/SistemaTurnosMedicos/issues/8)

- [feature/diseñador-de-clases-iniciales-correccion] Corrección de relaciones y atributos en el boceto de clases (@lucastol-dev).
  PR: [#18](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/18) | Issue: [#9](https://github.com/Purezaamor/SistemaTurnosMedicos/issues/9)

- [feature/doc-coord-repo] Creación de estructura de carpetas, README institucional y anexos.
  PR: [#10](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/10) | Issue: [#11](https://github.com/Purezaamor/SistemaTurnosMedicos/issues/11)

### Changed
- [feature/doc-coord-repo] Actualización de la carátula con datos completos de los integrantes en `README.md`.
- [feature/modelador-casos-uso] Integración de la vista previa de diagramas en `introduccion.md`.

### Fixed

- [fix/workflow-git] Corrección del flujo de trabajo utilizando git en lugar del editor web de GitHub. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) @Purezaamor (Coordinador)

- [fix/pr-templates] Incorporación de templates de Pull Request para ramas feature y release. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) @Purezaamor (Coordinador)

- [fix/release-body] Actualización del body de la PR de release con estructura requerida. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) @Purezaamor (Coordinador)

- [fix/issues-cierre] Cierre de issues pendientes (#12, #15, #17). PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) @Purezaamor (Coordinador)

- [fix/reviews-ia] Mejora en las revisiones con asistencia de IA, agregando observaciones más específicas. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) @Purezaamor (Coordinador)

- [fix/diagrama-clases] Corrección del diagrama de clases para ajustarlo al dominio del consultorio. PR: [#41](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/41) @keviineze (Modelador)

- [fix/relaciones-clases] Ajuste de relaciones entre clases del modelo de dominio. PR: [#41](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/41) @keviineze (Modelador)

- [fix/changelog] Coordinación y consolidación del changelog final. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) @Purezaamor (Coordinador)

- [fix/notebooklm-link] Corrección de sintaxis del enlace de NotebookLM en introduccion.md. PR: [#30](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/30) @keviineze (Modelador)

- [fix/actores-cu] Corrección de nombres de actores en casos de uso en introduccion.md. PR: [#37](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/37) @keviineze (Modelador)

- [fix/diagrama-render] Corrección de la ruta de visualización del diagrama de clases (.excalidraw → .png). PR: [#36](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/36) @Purezaamor (Coordinador)

- [fix/merge-artifacts] Limpieza de artefactos de merge en changelog.md. PR: [#35](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35) @Purezaamor (Coordinador)

- [fix/diagrama-tag] Corrección de error de renderizado (tag duplicado) en el diagrama de clases. PR: [#40](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/40) @keviineze (Modelador)

- [excepción retroactiva — commit directo sobre release/entrega-final-correcta] Corrección del número de grupo en template de release. No siguió el flujo fix/ → PR. No repetir.  
  Commit: [7e4ac42](https://github.com/Purezaamor/SistemaTurnosMedicos/commit/7e4ac42ca776f1e9a98d7c224b7703fc1cc3bba1) — @nachonervi-design (Analista de Requerimientos)
feature/doc-coord-repo-update-readme-md-a2

- [excepción retroactiva — commit directo sobre release/entrega-final-correcta] Revisión del template de PR para entrega final. No siguió el flujo fix/ → PR. No repetir.  
  Commit: [98b5859](https://github.com/Purezaamor/SistemaTurnosMedicos/commit/98b58590dbcce30e71e0a2d53bee66ff694d16a9) — @nachonervi-design (Analista de Requerimientos)


- [excepción retroactiva — commit directo sobre release/entrega-final-correcta] Revisión del template de PR para entrega final. No siguió el flujo fix/ → PR. No repetir.  
  Commit: [98b5859](https://github.com/Purezaamor/SistemaTurnosMedicos/commit/98b58590dbcce30e71e0a2d53bee66ff694d16a9) — @nachonervi-design (Analista de Requerimientos)
=======

>>>>>>> origin/develop
