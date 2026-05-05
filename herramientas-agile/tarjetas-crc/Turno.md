# Turno

- **Superclase:** —
- **Subclases:** (potencial futuro: ConsultaControl, ConsultaPrimeraVez)
- **Pensamiento del objeto:**  
  "Soy una cita medica concreta. Conozco mi fecha, hora programada, paciente, medico, tipo de consulta y estado actual. Si soy sobreturno, lo conozco. Cuando el paciente llega, registro su hora real. Puedo cambiar mi estado, pero no defino disponibilidad horaria: eso pertenece a Agenda y a las politicas de disponibilidad."
- **Responsabilidades:**  
  - Conocer fecha, hora, estado (Programado/Presente/Atendido/Cancelado/Ausente), tipoConsulta, esSobreturno, horaLlegada  
  - Transicionar su propio estado (cambiarEstado())  
  - Registrar el check-in del paciente (registrarLlegada(horaReal))
- **Colaboraciones de dominio:**  
  Paciente, Medico, Agenda
- **Abstracciones para inversion de dependencias:**  
  - RegistroAuditoria: recibe eventos de cambios del turno.  
  - RelojSistema: provee marca temporal para cambios y check-in.
- **Inyeccion de dependencias (capa aplicacion):**  
  - ServicioGestionTurnos inyecta RepositorioTurnos, RegistroAuditoria y RelojSistema para operar sobre Turno.
- **Propiedad:**  
  Creado y gestionado por Agenda
