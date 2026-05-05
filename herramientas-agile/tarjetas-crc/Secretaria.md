# Secretaria

- **Superclase:** Persona
- **Subclases:** —
- **Pensamiento del objeto:**  
  "Soy el operador administrativo del sistema. Me identifico como usuario con acceso de gestión. Registro pacientes, trabajo sobre la agenda del médico y registro los cambios que realizo."
- **Responsabilidades:**  
  — Conocer sus datos de acceso (heredados: nombre, apellido, telefono, mail)  
  — Ser identificada como la responsable de cada operación registrada en HistorialCambio
- **Colaboraciones:**  
  Agenda, Paciente, Medico, HistorialCambio
- **Propiedad:**  
  Creada y gestionada por administrador del sistema

> ⚠️ Corrección de diseño crítica: El boceto pone agendarTurno(), reprogramarTurno(), cancelarTurno() y notificarPaciente() como métodos de Secretaria. Esto es un error: la lógica pertenece a Agenda y Turno. Secretaria usa esas clases, no las reemplaza.
