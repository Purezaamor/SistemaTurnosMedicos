# Agenda

- **Superclase:** —
- **Subclases:** —
- **Pensamiento del objeto:**  
  "Soy el corazón operativo del sistema. Mantengo la colección completa de turnos de un médico y sus bloques de disponibilidad. Soy la única que puede confirmar si un horario está libre o no, y la única que puede insertar o quitar un turno de la lista. Garantizo que nunca haya dos turnos superpuestos para el mismo médico, y controlo que los sobreturnos no superen el límite de dos."
- **Responsabilidades:**  
  — Mantener la colección privada de Turno  
  — Validar disponibilidad antes de cualquier alta (validarDisponibilidad())  
  — Detectar y prevenir superposiciones horarias (verificarConflicto())  
  — Agregar y eliminar turnos (agregarTurno(), eliminarTurno())  
  — Consultar la vista diaria y semanal (mostrarAgendaDiaria(), mostrarAgendaSemanal())  
  — Controlar el límite de 2 sobreturnos autorizados
- **Colaboraciones:**  
  Turno, Disponibilidad, Medico, HistorialCambio
- **Propiedad:**  
  Pertenece a Medico (un médico tiene una única agenda en el MVP)

> ⚠️ Corrección de diseño: El atributo vistaActual del boceto es estado de presentación, no de dominio. Eliminado del modelo de dominio.
