# Tarjetas CRC — Sistema de Turnos Médicos

> **Base:** `anexos/introduccion.md` + `diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw`
> **Revisión crítica incorporada** en cada tarjeta con notas marcadas como ⚠️.

---

## Clases identificadas

| # | Clase | Origen |
|---|-------|--------|
| 1 | `Persona` | Implícita en la introducción (clase base para Paciente, Médico y Secretaria) |
| 2 | `Paciente` | Diagrama + RF1, RNF4 |
| 3 | `Medico` | Diagrama + RF2, RF3 |
| 4 | `Secretaria` | Diagrama + CU1, CU2, CU3 |
| 5 | `Turno` | Diagrama + RF1, RF4 |
| 6 | `Agenda` | Diagrama + RF2, RF3 |
| 7 | `Disponibilidad` | Diagrama + RF3 |
| 8 | `HistorialCambio` | Implícita — requerida por RF5 / RNF3 (ausente en el boceto) |

---

## Tarjetas CRC

---

### 1. `Persona` *(abstracta)*

| Campo | Contenido |
|-------|-----------|
| **Nombre** | `Persona` |
| **Superclase** | — |
| **Subclases** | `Paciente`, `Medico`, `Secretaria` |
| **Pensamiento del objeto** | *"Soy la representación abstracta de cualquier persona en el sistema. Conozco el nombre completo, el teléfono de contacto y el correo electrónico que me identifican. No existo por mí mismo: mis subclases me dan sentido."* |
| **Responsabilidades** | — Conocer `nombre`, `apellido`, `telefono`, `mail` |
| **Colaboraciones** | — (las subclases delegan en mí para los atributos comunes) |
| **Propiedad** | Clase base abstracta; no se instancia directamente |

> **⚠️ Corrección de diseño:** El boceto define `nombre`/`apellido`/`telefono`/`mail` por separado en `Paciente`, `Medico` y `Secretaria`. Esto viola el principio DRY. La introducción ya propone `Persona` como clase base. Se unifica aquí.

---

### 2. `Paciente`

| Campo | Contenido |
|-------|-----------|
| **Nombre** | `Paciente` |
| **Superclase** | `Persona` |
| **Subclases** | — |
| **Pensamiento del objeto** | *"Soy quien solicita atención médica. Conozco mi DNI, mi fecha de nacimiento y mi obra social. Soy identificado de forma inequívoca por mi DNI, lo que evita confusiones con homónimos. Sé qué turnos tengo, pero delego en la Agenda la lógica de verificar si un horario está libre."* |
| **Responsabilidades** | — Conocer `dni`, `fechaNacimiento`, `obraSocial` (heredados: `nombre`, `apellido`, `telefono`, `mail`) |
| **Colaboraciones** | `Turno`, `Agenda` |
| **Propiedad** | Creado y gestionado por `Secretaria` |

> **⚠️ Corrección de diseño:** El boceto asigna a `Paciente` los métodos `pedirTurno()`, `cancelarTurno()` y `verHorariosDisponibles()`. Esto es incorrecto: un paciente **es un dato del dominio**, no un agente que ejecuta lógica de negocio. Esas operaciones pertenecen a `Agenda` (validar, agregar, eliminar) y son *iniciadas por los actores* (Secretaria/Paciente vía interfaz). `Paciente` no necesita métodos de comportamiento en el modelo de dominio.

---

### 3. `Medico`

| Campo | Contenido |
|-------|-----------|
| **Nombre** | `Medico` |
| **Superclase** | `Persona` |
| **Subclases** | — |
| **Pensamiento del objeto** | *"Soy el profesional que brinda atención. Conozco mi especialidad y matrícula. Tengo una agenda que define mis horarios y soy el único autorizado a habilitar sobreturnos excepcionales."* |
| **Responsabilidades** | — Conocer `especialidad`, `matricula` (heredados: `nombre`, `apellido`, `telefono`, `mail`) — Autorizar la carga de un sobreturno (`autorizarSobreturno()`) |
| **Colaboraciones** | `Agenda`, `Disponibilidad` |
| **Propiedad** | Creado y gestionado por `Secretaria` / administrador del sistema |

> **⚠️ Ajuste de responsabilidades:** `consultarAgenda()` y `definirDisponibilidad()` son *acciones de actor* que invocan a `Agenda`/`Disponibilidad`, no responsabilidades del objeto `Medico` en sí. Se conserva solo `autorizarSobreturno()` como comportamiento propio porque implica una *regla de negocio* que depende del médico (RF2). Las otras operaciones son delegadas a sus colaboradores.

---

### 4. `Secretaria`

| Campo | Contenido |
|-------|-----------|
| **Nombre** | `Secretaria` |
| **Superclase** | `Persona` |
| **Subclases** | — |
| **Pensamiento del objeto** | *"Soy el operador administrativo del sistema. Me identifico como usuario con acceso de gestión. Registro pacientes, trabajo sobre la agenda del médico y registro los cambios que realizo."* |
| **Responsabilidades** | — Conocer sus datos de acceso (heredados: `nombre`, `apellido`, `telefono`, `mail`) — Ser identificada como la responsable de cada operación registrada en `HistorialCambio` |
| **Colaboraciones** | `Agenda`, `Paciente`, `Medico`, `HistorialCambio` |
| **Propiedad** | Creada y gestionada por administrador del sistema |

> **⚠️ Corrección de diseño crítica:** El boceto pone `agendarTurno()`, `reprogramarTurno()`, `cancelarTurno()` y `notificarPaciente()` como métodos de `Secretaria`. Esto es un error de modelado: mezcla al **actor** (quien inicia la acción) con el **objeto de dominio** (donde vive la lógica). La lógica de negocio de crear/modificar/cancelar un turno pertenece a `Agenda` y `Turno`. `Secretaria` *usa* esas clases, no las reemplaza. Eliminar esos métodos de `Secretaria`.

---

### 5. `Turno`

| Campo | Contenido |
|-------|-----------|
| **Nombre** | `Turno` |
| **Superclase** | — |
| **Subclases** | *(potencial futuro: `ConsultaControl`, `ConsultaPrimeraVez` — mencionadas en la introducción para polimorfismo de duración)* |
| **Pensamiento del objeto** | *"Soy una cita médica concreta. Conozco mi fecha, mi hora programada, a qué paciente y médico involucro, qué tipo de consulta represento y cuál es mi estado actual. Si soy un sobreturno, lo sé. Cuando el paciente llega, registro su hora real de arribo. Puedo transicionar de estado, pero no decido si el horario está disponible: eso lo sabe la Agenda."* |
| **Responsabilidades** | — Conocer `fecha`, `hora`, `estado` (Programado / Presente / Atendido / Cancelado / Ausente), `tipoConsulta`, `esSobreturno`, `horaLlegada` — Transicionar su propio estado (`cambiarEstado()`) — Registrar el check-in del paciente (`registrarLlegada(horaReal)`) — Notificar a `HistorialCambio` ante cada cambio de estado |
| **Colaboraciones** | `Paciente`, `Medico`, `Agenda`, `HistorialCambio` |
| **Propiedad** | Creado y gestionado por `Agenda` |

> **⚠️ Ajuste de responsabilidades:** Los métodos `reservar()`, `reprogramar()` y `cancelar()` del boceto implican que `Turno` se auto-gestiona en la agenda, lo que viola la separación de responsabilidades. `Turno` solo conoce *su propio estado*; la orquestación (verificar disponibilidad, insertar en la colección) es responsabilidad de `Agenda`. Se reemplaza por `cambiarEstado()` y `registrarLlegada()`.

---

### 6. `Agenda`

| Campo | Contenido |
|-------|-----------|
| **Nombre** | `Agenda` |
| **Superclase** | — |
| **Subclases** | — |
| **Pensamiento del objeto** | *"Soy el corazón operativo del sistema. Mantengo la colección completa de turnos de un médico y sus bloques de disponibilidad. Soy la única que puede confirmar si un horario está libre o no, y la única que puede insertar o quitar un turno de la lista. Garantizo que nunca haya dos turnos superpuestos para el mismo médico, y controlo que los sobreturnos no superen el límite de dos."* |
| **Responsabilidades** | — Mantener la colección privada de `Turno` — Validar disponibilidad antes de cualquier alta (`validarDisponibilidad()`) — Detectar y prevenir superposiciones horarias (`verificarConflicto()`) — Agregar y eliminar turnos (`agregarTurno()`, `eliminarTurno()`) — Consultar la vista diaria y semanal (`mostrarAgendaDiaria()`, `mostrarAgendaSemanal()`) — Controlar el límite de 2 sobreturnos autorizados |
| **Colaboraciones** | `Turno`, `Disponibilidad`, `Medico`, `HistorialCambio` |
| **Propiedad** | Pertenece a `Medico` (un médico tiene una única agenda en el MVP) |

> **⚠️ Corrección de diseño:** El atributo `vistaActual` del boceto es **estado de presentación (UI)**, no estado del dominio. Una agenda médica no "sabe" si se está viendo en modo diario o semanal: eso lo decide la capa de presentación. Eliminado del modelo de dominio.

---

### 7. `Disponibilidad`

| Campo | Contenido |
|-------|-----------|
| **Nombre** | `Disponibilidad` |
| **Superclase** | — |
| **Subclases** | — |
| **Pensamiento del objeto** | *"Soy un bloque horario del médico. Sé en qué día de la semana aplico, desde qué hora hasta qué hora, si estoy habilitado para turnos o bloqueado, y de qué tipo soy (atención regular, licencia, compromiso fijo). Puedo ser consultado para saber si un slot puntual cae dentro de mí."* |
| **Responsabilidades** | — Conocer `dia`, `horaInicio`, `horaFin`, `estado` (Habilitado / Bloqueado), `tipoBloque` — Responder si un intervalo de tiempo cae dentro de su rango (`estaDisponible(horaInicio, horaFin)`) — Ser bloqueado o habilitado (`bloquearHorario()`, `habilitarHorario()`) |
| **Colaboraciones** | `Agenda`, `Medico` |
| **Propiedad** | Creado y gestionado por `Agenda` a pedido de `Medico` |

---

### 8. `HistorialCambio` *(nuevo — ausente en el boceto)*

| Campo | Contenido |
|-------|-----------|
| **Nombre** | `HistorialCambio` |
| **Superclase** | — |
| **Subclases** | — |
| **Pensamiento del objeto** | *"Soy un registro inmutable de una modificación ocurrida en el sistema. Sé qué entidad fue modificada, cuál era el valor anterior, cuál es el nuevo, quién realizó el cambio y en qué momento exacto. Una vez creado, no puedo ser alterado."* |
| **Responsabilidades** | — Conocer `entidad`, `campoModificado`, `valorAnterior`, `valorNuevo`, `usuarioResponsable`, `timestamp` — Ser inalterable después de su creación (inmutabilidad garantiza trazabilidad) |
| **Colaboraciones** | `Turno`, `Agenda`, `Secretaria` |
| **Propiedad** | Creado automáticamente por `Turno` y `Agenda` ante cualquier cambio de estado o reprogramación |

> **⚠️ Clase faltante crítica:** Requerida explícitamente por RF5 (*"registrar de forma automática e inalterable el historial de modificaciones"*) y RNF3. Su ausencia en el boceto inicial representa un riesgo de incumplimiento de requisito. Debe incorporarse al diagrama de clases.

---

## Resumen de correcciones de diseño

| # | Problema en el boceto | Corrección aplicada |
|---|-----------------------|---------------------|
| 1 | `nombre`/`telefono`/`mail` duplicados en 3 clases | Extraídos a `Persona` (clase base abstracta) |
| 2 | `Paciente` con `pedirTurno()`, `cancelarTurno()` | Eliminados: la lógica de negocio pertenece a `Agenda` |
| 3 | `Secretaria` con `agendarTurno()`, `reprogramarTurno()`, `cancelarTurno()` | Eliminados: `Secretaria` es actor, no repositorio de lógica |
| 4 | `Turno` con `reservar()`, `reprogramar()`, `cancelar()` | Reemplazados por `cambiarEstado()` y `registrarLlegada()` |
| 5 | `Agenda.vistaActual` | Eliminado: es estado de UI, no de dominio |
| 6 | `HistorialCambio` ausente | Agregada como clase nueva, requerida por RF5/RNF3 |

---

## Jerarquía de herencia resultante

```
Persona (abstracta)
├── Paciente
├── Medico
└── Secretaria
```

## Relaciones de colaboración principales

```
Medico ─────────────────── posee ──────────────────→ Agenda
Agenda ─── contiene ──────────────────────────────→ Turno (colección)
Agenda ─── consulta ──────────────────────────────→ Disponibilidad (colección)
Turno ────── vincula ──────────────────────────────→ Paciente
Turno ────── vincula ──────────────────────────────→ Medico
Turno ────── notifica ─────────────────────────────→ HistorialCambio
Agenda ────── notifica ────────────────────────────→ HistorialCambio
Secretaria ── opera sobre ────────────────────────→ Agenda
```
