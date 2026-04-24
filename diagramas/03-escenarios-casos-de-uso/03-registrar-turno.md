| **Nombre del escenario:** | Flujo principal - Registro de turno exitoso | | | |
|---|---|---|---|---|
| **Nombre del caso de uso:** | Registrar Turno Médico | | **ID Única:** | 1 |
| **Área** | Sistema de Turnos Médicos, Gestión de Turnos | | | |
| **Actor(es):** | Paciente, Secretaria | | | |
| **Descripción:** | Permite registrar un turno médico entre un paciente y un profesional | | | |

| **Activar Evento:** | El paciente solicita un turno y la secretaria lo registra en el sistema | **Identificadores e iniciadores de caso de uso** |
|---|---|---|
| **Tipo de señal:** | ☑️ Externa | ☐ Temporal | |

| **Pasos desempeñados (ruta principal)** | **Información para los pasos** |
|---|---|
| 1. El paciente solicita un turno | Datos del paciente |
| 2. La secretaria ingresa al sistema | Usuario y clave |
| 3. Se selecciona el paciente y profesional | Sistema |
| 4. Se selecciona fecha y hora | Agenda |
| 5. El sistema valida disponibilidad | Agenda |
| 6. Se registra el turno | Base de datos |
| 7. Se confirma el turno | Pantalla |

| **Condiciones, suposiciones y preguntas** | |
|---|---|
| **Precondiciones:** | Paciente y médico registrados |
| **Poscondiciones:** | Turno registrado correctamente |
| **Suposiciones:** | Sistema funcionando |
| **Reunir requerimentos:** | RF1, RF2 |
| **Aspectos sobresalientes:** | Validación de disponibilidad |
| **Prioridad:** | Alta |
| **Riesgo:** | Medio |