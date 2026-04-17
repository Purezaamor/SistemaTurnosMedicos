# Changelog

## [Unreleased]

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
* **Analista de Requerimientos (Ignacio Nervi):**
    * Finalización de la normalización de 5 RF y 5 RNF. [[#15](https://github.com/Purezaamor/SistemaTurnosMedicos/issues/15)]
    * Definición del alcance del MVP en `introduccion.md`. [[#28](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/28)]
    * Investigación técnica y creación de cuaderno compartido en **NotebookLM**. [4, 5]
    * Corrección técnica de los requisitos no funcionales RNF 2, 3 y 5 en `introduccion.md`. [[#28](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/28)]
*   **Modelador:** 
    *   Documentación de 5 casos de uso completos en `introduccion.md`. [Issue #4] [PR #11]
*   **Diseñador:** 
    *   Creación del diagrama de clases inicial. [Issue #17] [PR #18]
    *   **Recursos:** [Fuente .excalidraw](diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw) y [Exportación .png](diagramas/01-diagrama-clases/01-boceto-inicial.png).
*   **Coordinador:** 
    *   Estructura de repositorio y revisiones con IA. [Issue #12] [PR #23]

### Changed
- [feature/doc-coord-repo] Actualización de la carátula con datos completos de los integrantes en `README.md`.
- [feature/modelador-casos-uso] Integración de la vista previa de diagramas en `introduccion.md`.

### Fixed
- Corrección del flujo de trabajo utilizando git en lugar del editor web de GitHub (@Purezaamor)
- Incorporación de templates de Pull Request para ramas feature y release (@Purezaamor)
- Actualización del body de la PR de release con estructura requerida (@Purezaamor)
- Cierre de issues pendientes (#12, #15, #17) (@Purezaamor)
- Mejora en las revisiones con asistencia de IA, agregando observaciones más específicas (@Purezaamor)
- Corrección del diagrama de clases para ajustarlo al dominio del consultorio (@Purezaamor)
- Ajuste de relaciones entre clases del modelo de dominio (@Purezaamor)
- Coordinación y consolidación del changelog final (@Purezaamor)
- Corregida sintaxis de enlace de NotebookLM grupal en introduccion.md (@keviineze - Modelador de Casos de Uso). 
  PR: https://github.com/Purezaamor/SistemaTurnosMedicos/pull/30
- Corregida los nombres de los actores en los Casos de Uso en introduccion.md (@keviineze - Modelador de Casos de Uso)
  PR: https://github.com/Purezaamor/SistemaTurnosMedicos/pull/37
- [fix/workflow-cleanup] Corrección del flujo de trabajo y revert de merges accidentales a master (@Purezaamor).
  PR: [#35] [https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35]
- [fix/templates-init] Incorporación de plantillas obligatorias para Issues y Pull Requests (@Purezaamor).
  PR: [#35] [https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35]
- [fix/changelog-cleanup] Resolución de conflictos de merge y limpieza de metadatos en el historial.
   PR: [#35] [https://github.com/Purezaamor/SistemaTurnosMedicos/pull/35]
- Corrección de la ruta de visualización del diagrama de clases en `introduccion.md`, cambiando el puntero de `.excalidraw` a `.png` para permitir el renderizado en GitHub. [[PR #36](https://github.com/Purezaamor/SistemaTurnosMedicos/pull/36)]
- Corregidos artefactos de merge y limpieza de estructura en changelog.md.
- Corregido error de renderizado (tag duplicado) en el Diagrama de Clases de introduccion.md. (@keviineze)
  PR: https://github.com/Purezaamor/SistemaTurnosMedicos/pull/40
- Corrección de templates de Pull Request según la consigna y adaptación al proyecto (@Purezaamor)
- Recreado diagrama de clases en formato Excalidraw nativo y exportado PNG (@keviineze).
  PR: https://github.com/Purezaamor/SistemaTurnosMedicos/pull/41