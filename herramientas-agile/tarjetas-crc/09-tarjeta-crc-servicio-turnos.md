# Tarjeta CRC — ServicioTurnos

|  |  |  |  |
|---|---|---|---|
| **Nombre de la Clase:** | ServicioTurnos | | |
| **Superclase:** | — | | |
| **Subclase:** | — | | |
| **Responsabilidades** | **Colaboradores** | **Pensamiento del objeto** | **Propiedad** |
| Validar disponibilidad para reprogramar un turno | Agenda, Turno, HistorialCambio, Medico, Paciente, sistema de notificaciones / eventos | Conozco la lógica de negocio para gestionar reprogramaciones: valido disponibilidad, coordino entre Agenda y Turno, registro cambios en HistorialCambio y emito eventos/notificaciones hacia la capa de presentación. | Servicio de dominio / controlador de caso de uso (inyectado por el contenedor de la aplicación) |
| Reprogramar turno y registrar cambio | Agenda, Turno, HistorialCambio, Medico, Paciente | | |
| Autorizar sobreturno cuando corresponde | Agenda, Turno, Medico | | |
| Emitir evento de reprogramación | HistorialCambio, sistema de notificaciones / eventos | | |

**Notas:** Implementar como servicio de aplicación que orquesta entidades del dominio; debe ser transaccional y registrar en `HistorialCambio` toda reprogramación.

**Fuente:** [anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md](../../anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md#L107-L107)
