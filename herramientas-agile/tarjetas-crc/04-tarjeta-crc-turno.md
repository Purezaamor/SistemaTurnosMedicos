|  |  |  |  |
|---|---|---|---|
| **Nombre de la Clase:** | Turno | | |
| **Superclase:** | | | |
| **Subclase:** | | | |
| **Responsabilidades** | **Colaboradores** | **Pensamiento del objeto** | **Propiedad** |
| Registrar turno | Paciente, Agenda | Represento una reserva en el sistema | fecha, hora |
| Gestionar estado del turno | Medico | Tengo un estado asociado al ciclo de vida (Programado, Confirmado, Atendido, Cancelado, Reprogramado, NoAsistió) | estado |
| Permitir cancelación | Agenda | Puedo ser modificado o cancelado | |
| Asociar paciente y médico | Paciente, Medico | Sé a qué paciente y médico pertenezco | paciente, medico |
| Validar disponibilidad | Agenda | Verifico que no haya superposición | fecha, hora |
| Mantener tipo de consulta | Agenda | Diferencio entre control y primera vez | tipoConsulta |