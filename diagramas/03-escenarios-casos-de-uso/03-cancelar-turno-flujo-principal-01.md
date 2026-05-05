| **Nombre del escenario:** | Flujo principal - Cancelación de turno | | | |
|---|---|---|---|---|
| **Nombre del caso de uso:** | Cancelar Turno | | **ID Única:** | 3 |
| **Área** | Gestión de Turnos | | | |
| **Actor(es):** | Paciente, Secretaria | | | |
| **Descripción:** | Permite cancelar un turno existente | | | |

| **Activar Evento:** | El paciente solicita cancelar el turno | **Identificadores e iniciadores de caso de uso** |
|---|---|---|
| **Tipo de señal:** | ☑️ Externa | ☐ Temporal | |

| **Pasos desempeñados (ruta principal)** | **Información para los pasos** |
|---|---|
| 1. Se busca el turno | Sistema |
| 2. Se selecciona cancelar | Sistema |
| 3. Se confirma acción | Usuario |
| 4. Sistema cambia estado | Base de datos |
| 5. Se libera horario | Agenda |

| 6. El sistema notifica al paciente la cancelación | Canal de notificación (WhatsApp / mail) |

| **Condiciones, suposiciones y preguntas** | |
|---|---|
| **Precondiciones:** | Turno existente |
| **Poscondiciones:** | Turno cancelado |
| **Suposiciones:** | Sistema disponible |
| **Reunir requerimentos:** | RF1 |
| **Aspectos sobresalientes:** | Liberación de horario |
| **Prioridad:** | Media |
| **Riesgo:** | Bajo |