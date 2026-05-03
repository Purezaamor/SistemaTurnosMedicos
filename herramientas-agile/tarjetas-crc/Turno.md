# Turno

- **Superclase:** —
- **Subclases:** (potencial futuro: ConsultaControl, ConsultaPrimeraVez)
- **Pensamiento del objeto:**  
  "Soy una cita médica concreta. Conozco mi fecha, mi hora programada, a qué paciente y médico involucro, qué tipo de consulta represento y cuál es mi estado actual. Si soy un sobreturno, lo sé. Cuando el paciente llega, registro su hora real de arribo. Puedo transicionar de estado, pero no decido si el horario está disponible: eso lo sabe la Agenda."
- **Responsabilidades:**  
  — Conocer fecha, hora, estado (Programado/Presente/Atendido/Cancelado/Ausente), tipoConsulta, esSobreturno, horaLlegada  
  — Transicionar su propio estado (cambiarEstado())  
  — Registrar el check-in del paciente (registrarLlegada(horaReal))  
  — Notificar a HistorialCambio ante cada cambio de estado
- **Colaboraciones:**  
  Paciente, Medico, Agenda, HistorialCambio
- **Propiedad:**  
  Creado y gestionado por Agenda
