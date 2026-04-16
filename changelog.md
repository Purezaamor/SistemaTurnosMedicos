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

### Fixed
- Corrección del flujo de trabajo utilizando git en lugar del editor web de GitHub (@Purezaamor)
- Incorporación de templates de Pull Request para ramas feature y release (@Purezaamor)
- Actualización del body de la PR de release con estructura requerida (@Purezaamor)
- Cierre de issues pendientes (#12, #15, #17) (@Purezaamor)
- Mejora en las revisiones con asistencia de IA, agregando observaciones más específicas (@Purezaamor)
- Corrección del diagrama de clases para ajustarlo al dominio del consultorio (@Purezaamor)
- Ajuste de relaciones entre clases del modelo de dominio (@Purezaamor)
- Coordinación y consolidación del changelog final (@Purezaamor)

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

