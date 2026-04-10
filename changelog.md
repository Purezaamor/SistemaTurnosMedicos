# Changelog

Todos los cambios importantes que se realicen en este proyecto quedarán documentados en este archivo.

---

## [Unreleased]
### Added
- Se agregó `anexos/introduccion.md` con análisis de requisitos y casos de uso.
- Se agregó el diagrama de clases inicial en `diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw`.

### Changed
- Se actualizó `README.md` con descripción del proyecto, objetivos y equipo.
- Se actualizó `anexos/introduccion.md` con la documentación técnica del requisito.

---

## [Release Actividad Obligatoria N°1] - 2026-03-25

### Added
- Análisis de requisitos funcionales y no funcionales del sistema.
- Diseño inicial de clases con atributos, métodos y relaciones.
- Documentación completa del sistema en formato Markdown.
*   **Analista (Ignacio Nervi):** 
    *   Finalización de la normalización de 5 RF y 5 RNF. [Issue #15]
    *   Definición del alcance del MVP en `introduccion.md`. [PR #16]
    *   Investigación y cuaderno compartido en NotebookLM.
      *   **Colaboración Técnica:** Asistencia al Documentador en la revisión asistida por IA del archivo `README.md`, aplicando pensamiento crítico sobre los hallazgos de Copilot para mejorar la carátula institucional y la descripción del proyecto. [PR #23 del Coordinador]
         *   **Asunción de tareas de Diseño de Clases:** 
        *   Refactorización técnica del archivo `01-boceto-inicial.excalidraw` para dar cumplimiento al requisito RNF2, integrando la clase **Agenda** y los métodos de ciclo de vida del **Turno**. [Issue #17]
        *   Aplicación de relaciones de herencia entre `Persona`, `Paciente` y `Medico`, y exportación final a formato `01-boceto-inicial.png`. [PR #18]
*   **Modelador:** 
    *   Documentación de 5 casos de uso completos en `introduccion.md`. [Issue #4] [PR #11]
*   **Diseñador:** 
    *   Creación del diagrama de clases inicial. [Issue #17] [PR #18]
    *   **Recursos:** [Fuente .excalidraw](diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw) y [Exportación .png](diagramas/01-diagrama-clases/01-boceto-inicial.png).
*   **Coordinador:** 
    *   Estructura de repositorio y revisiones con IA. [Issue #12] [PR #]

---

## Revisión del revisor

**Hallazgos**
- El changelog está bien iniciado, pero mezcla detalles técnicos de branches y PR con el registro de cambios, lo que puede dificultar su mantenimiento.
- La entrada indica un `.png` de diagrama que no se verifica en el diff actual.

**Sugerencias**
- Mantener el changelog enfocado en hitos, no en ramas o PRs, salvo que el proyecto adopte un formato formal de releases.
- Corregir o validar la referencia a recursos gráficos (PNG/EXCALIDRAW) si efectivamente están presentes.
- Considerar agregar fechas y una breve descripción de la versión en `Unreleased`.

