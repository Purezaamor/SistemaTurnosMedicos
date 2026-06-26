# Tarjeta CRC — PantallaTurnos

|  |  |  |  |
|---|---|---|---|
| **Nombre de la Clase:** | PantallaTurnos | | |
| **Superclase:** | — | | |
| **Subclase:** | — | | |
| **Responsabilidades** | **Colaboradores** | **Pensamiento del objeto** | **Propiedad** |
| Mostrar opciones disponibles de horarios | ServicioTurnos, Agenda, Turno, Secretaria, Paciente, sistema de notificaciones / correo | Conozco la interfaz de presentación para capturar la intención del usuario, mostrar alternativas de horarios y presentar confirmaciones o errores. Delego la ejecución de la lógica al ServicioTurnos. | Componente de la capa de presentación (UI), gestionado por el framework de interfaz |
| Capturar la selección del usuario para reprogramación | ServicioTurnos, Turno, Secretaria, Paciente | | |
| Enviar solicitud de reprogramación | ServicioTurnos, Turno | | |
| Mostrar confirmaciones y errores | ServicioTurnos, Secretaria, Paciente | | |

**Notas:** Componente de UI; no contiene lógica de negocio, solo llamada a servicios y validaciones de entrada mínimas.

**Fuente:** [anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md](../../anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md#L108-L108)
