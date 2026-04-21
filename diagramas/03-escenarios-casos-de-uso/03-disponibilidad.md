| **Nombre del escenario:** | Flujo principal - Configuración de disponibilidad | | | |
|---|---|---|---|---|
| **Nombre del caso de uso:** | Administrar Disponibilidad | | **ID Única:** | 5 |
| **Área** | Gestión de Agenda | | | |
| **Actor(es):** | Médico, Secretaria | | | |
| **Descripción:** | Permite definir horarios disponibles del profesional | | | |

| **Activar Evento:** | El médico desea configurar horarios | **Identificadores e iniciadores de caso de uso** |
|---|---|---|
| **Tipo de señal:** | ☑️ Externa | ☐ Temporal | |

| **Pasos desempeñados (ruta principal)** | **Información para los pasos** |
|---|---|
| 1. Accede a configuración | Sistema |
| 2. Define horarios | Usuario |
| 3. Define bloqueos | Usuario |
| 4. Sistema valida conflictos | Sistema |
| 5. Se guarda configuración | Base de datos |

| **Condiciones, suposiciones y preguntas** | |
|---|---|
| **Precondiciones:** | Médico registrado |
| **Poscondiciones:** | Disponibilidad actualizada |
| **Suposiciones:** | Sistema activo |
| **Reunir requerimentos:** | RF3 |
| **Aspectos sobresalientes:** | Control de agenda |
| **Prioridad:** | Alta |
| **Riesgo:** | Medio |