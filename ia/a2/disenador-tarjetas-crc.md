### Prompt utilizado
Leer los archivos anexos/introduccion.md y diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw.
Identifica las clases principales del sistema y genera una tarjeta CRC para cada una, usando la plantilla: nombre, superclase/subclase, pensamiento del objeto, responsabilidades, colaboraciones, propiedad. Revisa el diseño y corrige errores si detectás.

### Archivos de contexto utilizados

- anexos/introduccion.md
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw

### Ajustes realizados

- Unifiqué los atributos "nombre", "apellido", "telefono" y "mail" en una clase base abstracta "Persona" (no repetir código).
- Trasladé la lógica de gestión de turnos desde "Paciente" a la clase "Agenda" para respetar el diseño por responsabilidad.
- Eliminé métodos de actores desde "Secretaria", dejando solo las colaboraciones y propiedades.
- Incorporé la clase "HistorialCambio" que no estaba en el boceto pero era requerida por los requisitos funcionales.

---
