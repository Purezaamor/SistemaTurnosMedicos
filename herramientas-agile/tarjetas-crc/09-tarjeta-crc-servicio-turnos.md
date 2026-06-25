# Tarjeta CRC — ServicioTurnos

| Campo | Contenido |
|-------|-----------|
| **Nombre** | ServicioTurnos |
| **Superclase** | — |
| **Subclases** | — |
| **Pensamiento del objeto** | *"Orquesto la lógica de negocio para gestionar reprogramaciones: valido disponibilidad, coordino entre `Agenda` y `Turno`, registro cambios en `HistorialCambio` y emito eventos/notificaciones hacia la capa de presentación."* |
| **Responsabilidades** | - `validarDisponibilidadParaReprogramar(turno, nuevoSlot)`  
- `reprogramarTurno(turno, nuevoSlot, usuarioResponsable)`  
- `autorizarSobreturnoSiCorresponde(turno, medico)`  
- `registrarHistorialCambio(turno, cambios, usuario)`  
- `emitirEventoReprogramacion(turno)` |
| **Colaboraciones** | `Agenda`, `Turno`, `HistorialCambio`, `Medico`, `Paciente`, sistema de notificaciones / eventos |
| **Propiedad** | Servicio de dominio / controlador de caso de uso (inyectado por el contenedor de la aplicación) |

**Notas:** Implementar como servicio de aplicación que orquesta entidades del dominio; debe ser transaccional y registrar en `HistorialCambio` toda reprogramación.

**Fuente:** [anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md](../../anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md#L107-L107)
