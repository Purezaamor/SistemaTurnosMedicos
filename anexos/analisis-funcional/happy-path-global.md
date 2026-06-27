# Pseudocódigo - Happy Path Global del Sistema

## 1. Escenario Elegido

**Escenario:** El escenario describe el ciclo de vida operativo e institucional completo dentro de la clínica. Comienza con el registro de un nuevo paciente en el sistema y la configuración de la agenda del profesional. Luego, se simula la solicitud de un turno, su posterior reprogramación y cancelación. Finalmente, el médico visualiza su agenda diaria y registra formalmente la atención médica del paciente con su respectivo diagnóstico. Se eligió como happy path global porque recorre de punta a punta todas las funciones e involucra a todos los actores sobre las mismas entidades del dominio.

**Casos de uso involucrados:** CU01: Registrar Paciente, CU02: Registrar Agenda Médica, CU03: Solicitar Turno Médico, CU04: Cancelar Turno Médico, CU05: Registrar Atención Médica.

**Clases participantes:**

- Paciente
- Medico
- Agenda
- Turno
- EstadoTurno (Enum)
- Secretaria
- ControladorTurnos
- RepositorioTurnos
- Notificador
- PantallaTurnos
- PantallaAgenda
- HistorialClinico (o DetalleAtencion)

---

## 2. Pseudocódigo

```text
// ============================================
// 1. INSTANCIAR OBJETOS PRINCIPALES
// ============================================

// Crear pacientes y médicos
Paciente paciente1 = new Paciente("Juan Pérez", "12345678", "011-1234567", "OSDE")
Paciente paciente2 = new Paciente("María Gómez", "87654321", "011-7654321", "Swiss Medical")

Medico medico1 = new Medico("Dr. Rodríguez", "87654321", "011-998877", "Cardiología", "M-001")
Medico medico2 = new Medico("Dra. Martínez", "12349876", "011-887766", "Pediatría", "M-002")

// Crear agendas
Agenda agendaCardio = new Agenda()
Agenda agendaPedi = new Agenda()

// Asignar agendas a médicos
medico1.setAgenda(agendaCardio)
medico2.setAgenda(agendaPedi)

// Crear controladores y pantallas
PantallaTurnos pantalla = new PantallaTurnos()
ControladorTurnos controladorTurnos = new ControladorTurnos()

// Crear notificador
Notificador notificador = new Notificador()

// Crear repositorio de turnos
RepositorioTurnos repo = new RepositorioTurnos()

// ============================================
// 2. REGISTRAR TURNO
// ============================================

// [CU01] El sistema registra formalmente al paciente primero
controladorTurnos.registrarPaciente(paciente1)

// Secretaria inicia el proceso
Secretaria secretaria = new Secretaria("Ana García", "S-001")

// Secretaria solicita un turno para paciente1 con medico1
Turno turnoCreado = secretaria.registrarTurno(paciente1, "2026-06-20", "Cardiología")

// El sistema verifica disponibilidad en la agenda
if (medico1.getAgenda().verificarDisponibilidad("2026-06-20", "10:00") == true) {
// Registrar el turno
turnoCreado = medico1.getAgenda().registrarTurno(paciente1, "2026-06-20", "10:00")
repo.guardar(turnoCreado)

// Notificar al paciente
notificador.enviarConfirmacion(paciente1, "Turno registrado para Cardiología el 20/06 a las 10:00")
} else {
// Si no hay disponibilidad, ofrecer alternativas
List<Time> horariosDisponibles = medico1.getAgenda().consultarDisponibilidad("2026-06-20")
pantalla.mostrarHorarios(horariosDisponibles)
}

// ============================================
// 3. REPROGRAMAR TURNO
// ============================================

// Paciente solicita reprogramar su turno
Turno turnoExistente = repo.buscar(turnoCreado.getId())
if (turnoExistente != null) {
// Verificar nueva disponibilidad
if (medico1.getAgenda().verificarDisponibilidad("2026-06-22", "09:00") == true) {
turnoExistente.reprogramar("2026-06-22", "09:00")
repo.guardar(turnoExistente)

// Notificar al paciente
notificador.enviarReprogramacion(paciente1, "Turno reprogramado para el 22/06 a las 09:00")
} else {
pantalla.mostrarError("No hay disponibilidad para reprogramar")
}
}

// ============================================
// 4. CANCELAR TURNO
// ============================================

// Si el paciente necesita cancelar
turnoExistente.cancelar()
repo.cancelar(turnoExistente.getId())

// Notificar al paciente
notificador.enviarCancelacion(paciente1, "Su turno ha sido cancelado")

// ============================================
// 5. ADMINISTRAR DISPONIBILIDAD
// ============================================

// La secretaria agrega disponibilidad para un médico
secretaria.registrarDisponibilidad(medico1, "2026-06-25", "15:00")

// ============================================
// 6. VISUALIZAR AGENDA
// ============================================

// El médico consulta su agenda
List<Turno> turnosMedico = medico1.getAgenda().consultarTurnos("2026-06-20")
PantallaAgenda.mostrarAgenda(turnosMedico)

// ============================================
// 6.5 REGISTRAR ATENCIÓN MÉDICA [CU05]
// ============================================

// El médico recibe al paciente en el consultorio y registra la consulta
HistorialClinico registroAtencion = medico1.registrarAtencion(turnoExistente, "Paciente presenta mejoría clínica. Se receta descanso por 48hs.")
repo.guardarHistorial(registroAtencion)

// Cambiar el estado del turno a FINALIZADO
turnoExistente.setEstado(EstadoTurno.FINALIZADO)

// ============================================
// 7. FIN DEL FLUJO
// ============================================

mostrar("Proceso completado con éxito")
```

---

## 3. Trazabilidad del Pseudocódigo

| Bloque | Caso de uso | Clases involucradas | Diagrama de secuencia de referencia |
|--------|-------------|---------------------|-------------------------------------|
| Agendar turno | CU1 | SistemaTurnos, Paciente | [05-secuencia-agendar-turno-flujo-principal-01.png](../../diagramas/05-diagramas-secuencia/05-secuencia-agendar-turno-flujo-principal-01.png) |
| Reprogramar turno | CU2 | SistemaTurnos, Médico, Agenda | [05-secuencia-reprogramar-turno-flujo-principal-02.png](../../diagramas/05-diagramas-secuencia/05-secuencia-reprogramar-turno-flujo-principal-02.png) |
| Cancelar turno | CU3 | SistemaTurnos, Paciente, Médico, Agenda, Turno, EstadoTurno | [05-secuencia-cancelar-turno-flujo-principal-03.png](../../diagramas/05-diagramas-secuencia/05-secuencia-cancelar-turno-flujo-principal-03.png) |
| Autorizar Sobreturno | CU4 | SistemaTurnos, Turno, EstadoTurno, Notificacion (o ServicioNotificaciones), Paciente, Médico | [05-secuencia-autorizar-sobreturno-flujo-principal-04.png](../../diagramas/05-diagramas-secuencia/05-secuencia-autorizar-sobreturno-flujo-principal-04.png) |
| Consultar Agenda Medica | CU5 | SistemaTurnos, Médico, Turno, EstadoTurno, HistorialClinico (o DetalleAtencion) | [05-secuencia-consultar-agenda-medica-flujo-principal-05.png](../../diagramas/05-diagramas-secuencia/05-secuencia-consultar-agenda-medica-flujo-principal-05.png) |