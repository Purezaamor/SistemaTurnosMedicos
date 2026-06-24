# Tarjeta CRC — Notificacion

| Campo | Contenido |
|-------|-----------|
| **Nombre** | Notificacion |
| **Superclase** | — |
| **Subclases** | — |
| **Pensamiento del objeto** | *"Encargado de generar y enviar mensajes de dominio (confirmaciones, cancelaciones, reprogramaciones) hacia los actores afectados (Paciente, Médico, Secretaria) usando los canales disponibles (email, SMS, en-app)."* |
| **Responsabilidades** | - `generarMensajeEvento(turno, tipoEvento)`  
- `enviarNotificacion(receptor, mensaje, canal)`  
- `registrarEnvio(turno, receptor, canal, resultado)` |
| **Colaboraciones** | `ServicioTurnos`, `Turno`, `Paciente`, `Medico`, sistema de mensajería / mailer |
| **Propiedad** | Servicio de infraestructura para la capa de aplicación; debe ser idempotente y registrar intentos de reenvío en caso de fallo |

**Notas:** Debe separarse la lógica de formato del mensaje (plantillas) de la entrega física (canales). Las notificaciones deben ser auditables y respetar la política de reintentos.

**Fuente:** [anexos/analisis-funcional/03-caso-de-uso-cancelar-turno.md](../../anexos/analisis-funcional/03-caso-de-uso-cancelar-turno.md#L108-L108)
