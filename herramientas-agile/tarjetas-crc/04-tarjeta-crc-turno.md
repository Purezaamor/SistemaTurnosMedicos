|  |  |  |  |
|---|---|---|---|
| **Nombre de la Clase:** | Turno | | |
| **Superclase:** | | | |
| **Subclase:** | | | |
| **Responsabilidades** | **Colaboradores** | **Pensamiento del objeto** | **Propiedad** |
| Registrar turno | Paciente, Agenda | Represento una reserva en el sistema | fecha |
| Cambiar estado | Medico | Tengo un estado asociado al turno | hora |
| Permitir cancelación | Agenda | Puedo ser modificado o cancelado | estado |
| Asociar paciente y médico | Paciente, Medico | Sé a qué paciente y médico pertenezco | paciente, medico |
| Validar disponibilidad | Agenda | Verifico que no haya superposición | fecha, hora |