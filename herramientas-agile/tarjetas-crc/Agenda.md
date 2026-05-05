# Agenda

- **Superclase:** —
- **Subclases:** —
- **Pensamiento del objeto:**  
  "Soy el nucleo operativo del sistema. Mantengo la coleccion completa de turnos de un medico y sus bloques de disponibilidad. Confirmo si un horario esta libre, inserto o quito turnos y garantizo que no haya superposiciones para el mismo profesional, respetando el limite de dos sobreturnos autorizados."
- **Responsabilidades:**  
  - Mantener la coleccion privada de Turno  
  - Validar disponibilidad antes de cualquier alta (validarDisponibilidad())  
  - Detectar y prevenir superposiciones horarias (verificarConflicto())  
  - Agregar y eliminar turnos (agregarTurno(), eliminarTurno())  
  - Consultar la agenda diaria y semanal (mostrarAgendaDiaria(), mostrarAgendaSemanal())  
  - Controlar el limite de 2 sobreturnos autorizados
- **Colaboraciones de dominio:**  
  Turno, Medico, Disponibilidad
- **Abstracciones para inversion de dependencias:**  
  - PoliticaDisponibilidad: encapsula reglas de superposicion y disponibilidad.  
  - AutorizadorSobreturno: valida autorizaciones especiales del medico.  
  - RegistroAuditoria: registra cambios inalterables (usuario, fecha/hora, descripcion).  
  - RepositorioAgenda: persistencia de agenda sin acoplar a almacenamiento concreto.
- **Inyeccion de dependencias (capa aplicacion):**  
  - ServicioGestionTurnos inyecta RepositorioAgenda, PoliticaDisponibilidad, RegistroAuditoria y RelojSistema.  
  - Agenda no depende de infraestructura; solo aplica reglas de negocio.
- **Propiedad:**  
  Pertenece a Medico (un medico tiene una unica agenda en el MVP)

> Correccion de diseno: el atributo vistaActual del boceto es estado de presentacion, no de dominio.
