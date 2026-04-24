| **Nombre del escenario:** | Flujo principal - Reprogramación de turno | | | |
|---|---|---|---|---|
| **Nombre del caso de uso:** | Reprogramar Turno | | **ID Única:** | 2 |
| **Área** | Gestión de Turnos | | | |
| **Actor(es):** | Secretaria | | | |
| **Descripción:** | Permite modificar la fecha y hora de un turno existente | | | |

| **Activar Evento:** | El paciente solicita cambio de turno | **Identificadores e iniciadores de caso de uso** |
|---|---|---|
| **Tipo de señal:** | ☑️ Externa | ☐ Temporal | |

| **Pasos desempeñados (ruta principal)** | **Información para los pasos** |
|---|---|
| 1. Se busca el turno | Sistema |
| 2. Se selecciona reprogramar | Sistema |
| 3. Se elige nueva fecha | Agenda |
| 4. Sistema valida disponibilidad | Agenda |
| 5. Se actualiza el turno | Base de datos |

| **Condiciones, suposiciones y preguntas** | |
|---|---|
| **Precondiciones:** | Turno existente |
| **Poscondiciones:** | Turno actualizado |
| **Suposiciones:** | Hay disponibilidad |
| **Reunir requerimentos:** | RF1 |
| **Aspectos sobresalientes:** | Control de conflictos |
| **Prioridad:** | Alta |
| **Riesgo:** | Medio |