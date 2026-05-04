|  |  |  |  |
|---|---|---|---|
| **Nombre de la Clase:** | Turno | | |
| **Superclase:** | | | |
| **Subclase:** | | | |
| **Responsabilidades** | **Colaboradores** | **Pensamiento del objeto** | **Propiedad** |
| Registrar turno | Secretaria, Agenda | Represento una reserva en el sistema | fecha |
| Cambiar estado del turno (creado, confirmado, atendido, cancelado, ausente) | Medico | Tengo un ciclo de vida asociado | estado |
| Permitir cancelación | Secretaria | Puedo ser cancelado o modificado | |
| Asociar paciente y médico | Paciente, Medico | Sé a qué paciente y médico pertenezco | paciente, medico |
| Validar disponibilidad | Agenda | Verifico que no haya superposición | hora |
| Gestionar tipo de consulta | Secretaria | Distingo duración según tipo | tipoConsulta |
| | | | estados: creado, confirmado, atendido, cancelado, ausente |