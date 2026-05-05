|  |  |  |  |
|---|---|---|---|
| **Nombre de la Clase:** | Turno | | |
| **Superclase:** | | | |
| **Subclase:** | | | |
| **Responsabilidades** | **Colaboradores** | **Pensamiento del objeto** | **Propiedad** |
| Cambiar estado del turno | Agenda, HistorialCambios | Tengo un ciclo de vida asociado | estado |
| Permitir cancelacion y reprogramacion | Agenda | Puedo ser cancelado o modificado bajo reglas de negocio | |
| Asociar paciente y medico | Paciente, Medico | Se a que paciente y medico pertenezco | paciente, medico |
| Registrar llegada del paciente | HistorialCambios | Distingo asistencia real respecto al horario planificado | hora |
| Gestionar tipo de consulta | TipoConsulta | Distingo duracion segun tipo de consulta | tipoConsulta |