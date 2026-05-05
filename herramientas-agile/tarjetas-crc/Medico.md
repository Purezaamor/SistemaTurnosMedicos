# Medico

- **Superclase:** Persona
- **Subclases:** —
- **Pensamiento del objeto:**  
  "Soy el profesional que brinda atención. Conozco mi especialidad y matrícula. Tengo una agenda que define mis horarios y soy el único autorizado a habilitar sobreturnos excepcionales."
- **Responsabilidades:**  
  — Conocer especialidad, matricula (heredados: nombre, apellido, telefono, mail)  
  — Autorizar la carga de un sobreturno (autorizarSobreturno())
- **Colaboraciones:**  
  Agenda, Disponibilidad
- **Propiedad:**  
  Creado y gestionado por Secretaria o administrador del sistema

> ⚠️ Ajuste de responsabilidades: consultarAgenda() y definirDisponibilidad() son acciones de actor que invocan a Agenda/Disponibilidad, no responsabilidades del objeto Medico. Solo se conserva autorizarSobreturno() como comportamiento propio.
