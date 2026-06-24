# Tarjeta CRC — PantallaTurnos

| Campo | Contenido |
|-------|-----------|
| **Nombre** | PantallaTurnos |
| **Superclase** | — |
| **Subclases** | — |
| **Pensamiento del objeto** | *"Interfaz de presentación encargada de capturar la intención del usuario (reprogramar), mostrar alternativas de horarios y presentar confirmaciones o errores. Delego la ejecución de la lógica al `ServicioTurnos`."* |
| **Responsabilidades** | - `mostrarOpcionesDisponibles(listaSlots)`  
- `capturarSeleccionUsuario()`  
- `enviarSolicitudReprogramacion(turno, nuevoSlot)`  
- `mostrarConfirmacion()`  
- `mostrarError(mensaje)` |
| **Colaboraciones** | `ServicioTurnos`, `Agenda` (lectura), `Turno`, actores `Secretaria`/`Paciente`, sistema de notificaciones / correo |
| **Propiedad** | Componente de la capa de presentación (UI), gestionado por el framework de interfaz |

**Notas:** Componente de UI; no contiene lógica de negocio, solo llamada a servicios y validaciones de entrada mínimas.

**Fuente:** [anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md](../../anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md#L108-L108)
