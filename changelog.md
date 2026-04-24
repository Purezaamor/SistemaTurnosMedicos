## [Release Actividad Obligatoria N°2] - 2026-04-17

### Added

- [feature/modelador-diag-casos-uso] Modelado de 5 diagramas de casos de uso en PlantUML y exportación a PNG. PR: [#20](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/20) — @keviineze (Modelador de Casos de Uso)

- [feature/a2-tarjetas-crc] Creación de tarjetas CRC en archivos individuales, incluyendo responsabilidades, colaboradores y pensamiento del objeto. PR: [#51](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/51) — @Purezaamor (Diseñador de Tarjetas CRC)

- [feature/escenarios-cu] Desarrollo de escenarios de casos de uso en archivos individuales con estructura completa y campos obligatorios. PR: [#50](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/50) — @Purezaamor (Especialista en Escenarios)

- [feature/doc-coord-repo-update-readme-md-a2] Actualización de README.md con estructura final del proyecto, índices de navegación y documentación del equipo. PR: [#52](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/52) — @nachonervi-design (Documentador y Coordinador)

### Changed

- [feature/modelador-diag-casos-uso] Corrección de sintaxis UML y consistencia de render en diagramas de casos de uso. PR: [#20](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/20) — @keviineze (Modelador de Casos de Uso)

- [feature/a2-tarjetas-crc] Ajuste de tarjetas CRC para reflejar correctamente relaciones del dominio e incorporación de la tarjeta HistorialCambios para auditoría. PR: [#51](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/51) — @Purezaamor (Diseñador de Tarjetas CRC)

- [feature/escenarios-cu] Reestructuración completa de escenarios de casos de uso en carpeta dedicada, con archivos individuales e índice central. PR: [#50](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/50) — @Purezaamor (Especialista en Escenarios)


### Fixed

- [fix/changelog-readme] Corrección final de `changelog.md` y `README.md` según observaciones de revisión: normalización del formato bajo Keep a Changelog, eliminación de duplicados y activación de enlaces de navegación. PR: [#59](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/59) — @nachonervi-design (Documentador y Coordinador)

- [fix/especialista-escenarios-casos-uso-a2] Corrección de escenarios de casos de uso: normalización de naming de archivos, incorporación de notificación obligatoria en "Cancelar Turno" y actualización del índice con enlaces válidos. PR: [#61](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/61) — @Purezaamor (Especialista en Escenarios)

- [fix/correcciones-modelador-diagramas-a2] Corrección de diagramas de casos de uso: ajuste de sintaxis UML, corrección de relaciones <<include>> y actualización de archivos .png e índice de diagramas. PR: [#62](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/62) — @keviineze (Modelador de Casos de Uso)

---

## [Release Actividad Obligatoria N°1] - 2026-03-25

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

