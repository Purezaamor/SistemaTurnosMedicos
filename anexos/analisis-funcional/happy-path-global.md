# Pseudocódigo - Happy Path Global del Sistema

## 1. Descripción del escenario

El siguiente pseudocódigo muestra el flujo completo del sistema desde que un paciente llega al consultorio hasta que se registra un turno, se reprograma (si es necesario) y se notifica el resultado. Involucra a todos los actores y clases principales del sistema.

## 2. Pseudocódigo

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
// 7. FIN DEL FLUJO
// ============================================

mostrar("Proceso completado con éxito")

## 3. Tabla de trazabilidad (OBLIGATORIA)

| Paso | Artefacto de origen |
|------|---------------------|
| Registrar turno | CU1 - Diagrama de secuencia y actividades |
| Reprogramar turno | CU2 - Diagrama de secuencia y actividades |
| Cancelar turno | CU3 - Diagrama de secuencia y actividades |
| Administrar disponibilidad | CU5 - Diagrama de secuencia y actividades |
| Visualizar agenda | CU4 - Diagrama de secuencia y actividades |
| Clases principales | Diagrama de clases final unificado |
| Colaboraciones | Tarjetas CRC de A2 |