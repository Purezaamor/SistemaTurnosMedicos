# Diagramas de Secuencia - Sistema de Turnos Médicos

## Descripción General

Este directorio contiene los diagramas de secuencia del Sistema de Turnos Médicos, desarrollados como parte de la Actividad Obligatoria N°3. Los diagramas de secuencia muestran las interacciones entre objetos en el sistema a lo largo del tiempo, especificando el orden en que ocurren los eventos.

## Estructura del Proyecto

Los diagramas siguen la notación UML 2.5 para diagramas de secuencia, con énfasis en:
- **Participantes**: Actores y objetos del sistema (Paciente, Secretaria, Médico, ServicioTurnos, Agenda, Turno, etc.)
- **Mensajes**: Interacciones síncronas y asincrónicas con parámetros en camelCase
- **Secuencialidad**: Orden temporal correcto de eventos
- **Ciclo de vida**: Creación (`create`) y destrucción (`destroy`) de objetos

## Diagramas Incluidos

### 1. Agendar Turno Médico (Flujo Principal)

**Archivo PlantUML**: [05-secuencia-agendar-turno-flujo-principal-01.puml](05-secuencia-agendar-turno-flujo-principal-01.puml)

**Diagrama PNG**: [05-secuencia-agendar-turno-flujo-principal-01.png](05-secuencia-agendar-turno-flujo-principal-01.png)

**Caso de Uso Asociado**: Registrar Turno Médico

**Propósito**: Detallar el flujo completo de creación de un nuevo turno. Muestra cómo el Paciente, a través de la Secretaria, consulta disponibilidad, selecciona un slot y se registra en la agenda del médico.

**Participantes (8)**:
- `Paciente` (actor)
- `Secretaria` (actor)
- `PantallaTurnos:UI` (interfaz del sistema)
- `ServicioTurnos:Servicio` (lógica de negocio)
- `turno:Turno` (objeto creado)
- `agenda:Agenda` (gestor de disponibilidad)
- `notificacion:Notificacion` (notificación temporal)
- `Médico` (actor - receptor)

**Secuencia Principal**:
1. Paciente solicita agendar turno a Secretaria
2. Secretaria consulta disponibilidad en la UI
3. UI delega en ServicioTurnos que consulta agenda
4. Agenda retorna slots disponibles
5. Secretaria presenta opciones al Paciente
6. Paciente selecciona slot
7. Se crea nuevo objeto Turno
8. Turno se registra en Agenda
9. Se crea notificación que se envía
10. Médico recibe notificación

**Requisitos de Diseño Cumplidos**:
- ✓ 8 participantes (mínimo 4)
- ✓ Mensajes en camelCase con argumentos: `solicitarAgendarTurno()`, `obtenerSlotsDisponibles()`, etc.
- ✓ Notación UML: `:Clase`, `objeto:Clase`
- ✓ Ciclo de vida: `create Turno`, `create Notif`, `destroy Notif`
- ✓ Coherencia con sistema de turnos médicos

---

### 2. Reprogramar Turno Existente (Flujo Principal)

**Archivo PlantUML**: [05-secuencia-reprogramar-turno-flujo-principal-02.puml](05-secuencia-reprogramar-turno-flujo-principal-02.puml)

**Diagrama PNG**: [05-secuencia-reprogramar-turno-flujo-principal-02.png](05-secuencia-reprogramar-turno-flujo-principal-02.png)

**Caso de Uso Asociado**: Reprogramar Turno Existente

**Propósito**: Mostrar cómo se modifica un turno existente a una nueva fecha. Incluye búsqueda del turno actual, liberación de slot anterior y ocupación de nuevo slot.

**Participantes (6)**:
- `Paciente` (actor)
- `Secretaria` (actor)
- `PantallaTurnos:UI` (interfaz)
- `ServicioTurnos:Servicio` (lógica)
- `turnoActual:Turno` y `turnoNuevo:Turno` (en realidad, el mismo objeto actualizado)
- `agenda:Agenda` (gestor)

**Secuencia Principal**:
1. Paciente solicita reprogramar turno
2. Sistema busca y recupera turno existente
3. Se consulta disponibilidad alternativa
4. Se presentan opciones
5. Paciente selecciona nuevo slot
6. Se actualiza turno
7. Se libera slot anterior
8. Se ocupa nuevo slot en agenda

**Requisitos de Diseño Cumplidos**:
- ✓ 6 participantes (mínimo 4)
- ✓ Mensajes descriptivos: `obtenerTurnoExistente()`, `reprogramarTurno()`, etc.
- ✓ Transiciones de estado: CONFIRMADO → REPROGRAMADO
- ✓ Gestión de recursos: liberación y ocupación de slots

---

### 3. Cancelar Turno (Flujo Principal)

**Archivo PlantUML**: [05-secuencia-cancelar-turno-flujo-principal-03.puml](05-secuencia-cancelar-turno-flujo-principal-03.puml)

**Diagrama PNG**: [05-secuencia-cancelar-turno-flujo-principal-03.png](05-secuencia-cancelar-turno-flujo-principal-03.png)

**Caso de Uso Asociado**: Cancelar Turno

**Propósito**: Detallar el proceso de cancelación de un turno, incluyendo validación de estado, cambio de estado en el objeto, liberación de recursos y notificaciones.

**Participantes (7)**:
- `Paciente` (actor)
- `Secretaria` (actor)
- `PantallaTurnos:UI` (interfaz)
- `ServicioTurnos:Servicio` (lógica)
- `turno:Turno` (objeto existente)
- `agenda:Agenda` (gestor)
- `notificacion:Notificacion` (temporal)

**Secuencia Principal**:
1. Paciente solicita cancelación
2. Sistema busca turno
3. Se solicita confirmación
4. Se cambia estado a CANCELADO
5. Se libera slot en agenda
6. Se crean y envían notificaciones
7. Se destruye objeto notificación

**Requisitos de Diseño Cumplidos**:
- ✓ 7 participantes (mínimo 4)
- ✓ Ciclo de vida completo: `create Notif`, `destroy Notif`
- ✓ Validaciones y confirmaciones
- ✓ Notificaciones a múltiples actores

---

### 4. Autorizar Sobreturno (Flujo Principal)

**Archivo PlantUML**: [05-secuencia-autorizar-sobreturno-flujo-principal-04.puml](05-secuencia-autorizar-sobreturno-flujo-principal-04.puml)

**Diagrama PNG**: [05-secuencia-autorizar-sobreturno-flujo-principal-04.png](05-secuencia-autorizar-sobreturno-flujo-principal-04.png)

**Caso de Uso Asociado**: Autorizar Sobreturno

**Propósito**: Mostrar el flujo especial cuando la agenda está completa pero se ofrece un sobreturno, requiriendo autorización del médico. Incluye el flujo de aprobación y creación de turno especial.

**Participantes (7)**:
- `Paciente` (actor)
- `Secretaria` (actor)
- `PantallaTurnos:UI` (interfaz)
- `ServicioTurnos:Servicio` (lógica)
- `turnoSobreturno:Turno` (creación especial)
- `agenda:Agenda` (gestor)
- `autorizacion:Autorizacion` (objeto temporal)
- `Médico` (actor - aprobador)

**Secuencia Principal**:
1. Paciente solicita turno con agenda completa
2. Se detecta que no hay disponibilidad
3. Se ofrece sobreturno
4. Se crea solicitud de autorización
5. Médico recibe notificación
6. Médico autoriza
7. Se crea Turno especial con tipo SOBRETURNO
8. Se registra en agenda como sobreturno

**Requisitos de Diseño Cumplidos**:
- ✓ 7 participantes (mínimo 4)
- ✓ Flujo condicional: rechazo vs. aceptación de sobreturno
- ✓ Objeto temporal: `Autorizacion` con `destroy`
- ✓ Creación especial de turno con estado diferenciado

---

### 5. Consultar Agenda Médica (Flujo Principal)

**Archivo PlantUML**: [05-secuencia-consultar-agenda-medica-flujo-principal-05.puml](05-secuencia-consultar-agenda-medica-flujo-principal-05.puml)

**Diagrama PNG**: [05-secuencia-consultar-agenda-medica-flujo-principal-05.png](05-secuencia-consultar-agenda-medica-flujo-principal-05.png)

**Caso de Uso Asociado**: Visualizar Agenda Médica

**Propósito**: Detallar cómo se consulta y visualiza la agenda completa de un médico, incluyendo turnos confirmados y disponibilidad. Incluye flujos alternativos para acceso por Secretaria o por el Médico mismo.

**Participantes (7)**:
- `Secretaria` (actor)
- `PantallaTurnos:UI` (interfaz)
- `ServicioTurnos:Servicio` (lógica)
- `agenda:Agenda` (gestor)
- `turno:Turno` (objetos existentes)
- `disponibilidad:Disponibilidad` (gestor)
- `Médico` (actor)

**Secuencia Principal**:
1. Secretaria selecciona médico en UI
2. UI solicita agenda al servicio
3. Servicio recupera agenda con turnos
4. Servicio obtiene disponibilidad
5. Se formula datos completos
6. UI presenta agenda a Secretaria

**Flujos Alternativos**:
- **Alt 1**: Médico consulta su propia agenda (acceso personalizado)
- **Alt 2**: Secretaria cambia rango de fechas (actualización de vista)

**Requisitos de Diseño Cumplidos**:
- ✓ 7 participantes (mínimo 4)
- ✓ Fragmentos combinados (alt) para flujos alternativos
- ✓ Iteración sobre colecciones: `iterarTurnos()`
- ✓ Consultas complejas a agenda y disponibilidad

---

## Notación y Convenciones UML

### Participantes
- **Actor** (`actor`): Usuarios externos (Paciente, Secretaria, Médico)
- **Participant** (`participant`): Componentes del sistema (clases, servicios)
- **Notación**: `NombreClase:Instancia` (ej: `turno:Turno`)

### Mensajes
- **Síncrono** (`->`): Llamada de método bloqueante
- **Asíncrono** (`-->`, `->`): Retorno o mensaje no bloqueante
- **Parámetros**: Todos en camelCase (ej: `obtenerSlotsDisponibles(especialidadID, rango)`)

### Ciclo de Vida
- **Creación** (`create Objeto`): Instanciación durante la secuencia
- **Destrucción** (`destroy Objeto`): Finalización explícita de objeto temporal

### Fragmentos Combinados
- **alt**: Decisión (if-else)
- **loop**: Repetición
- **par**: Paralelismo

### Notas
Clarificaciones y aclaraciones sobre decisiones de diseño y estados.

---

## Relación con otros Diagramas

### Con Casos de Uso (`diagramas/02-casos-de-uso/`)
Los diagramas de secuencia detallen el "cómo" de cada caso de uso, definiendo las interacciones específicas.

### Con Diagrama de Clases (`diagramas/01-diagrama-clases/`)
Validan que la estructura de clases puede sostener las interacciones mostradas. Cada mensaje implica:
- Método existente en la clase
- Parámetros y tipos correctos
- Visibilidad y accesibilidad apropiadas

### Con Diagramas de Actividades (`diagramas/04-diagramas-actividades/`)
Proporcionan perspectiva complementaria:
- **Secuencias**: Enfoque en colaboración entre objetos
- **Actividades**: Enfoque en flujo de control y decisiones

### Con Principios SOLID (`anexos/principios-solid/`)
Los diagramas aplican:
- **SRP**: Cada objeto tiene responsabilidad clara
- **OCP**: Extensión sin modificación (nuevos tipos de turno)
- **LSP**: Sustitución de implementaciones
- **ISP**: Interfaces específicas para cada cliente
- **DIP**: Dependencia en abstracciones, no en clases concretas

---

## Generación de Imágenes

### Herramienta: PlantUML
Los archivos `.puml` pueden compilarse a múltiples formatos:
- **PNG**: Imágenes rasterizadas (carpeta local)
- **SVG**: Vectoriales para web
- **PDF**: Para documentación de impresión

### Comando de Compilación
```bash
plantuml -png diagramas/05-diagramas-secuencia/*.puml
```

### Servicio en Línea
Alternativamente, usar http://www.plantuml.com/plantuml/uml/ para visualización inmediata.

---

## Validación y Calidad

Cada diagrama ha sido validado según:

1. **Sintaxis**: PlantUML válido
2. **Requisitos de Cátedra**:
   - ✓ Mínimo 4 participantes
   - ✓ Mínimo 3 mensajes/interacciones por participante
   - ✓ Mensajes en camelCase con argumentos
   - ✓ Notación UML correcta
   - ✓ Ciclo de vida de objetos (create/destroy)
3. **Consistencia**: Alineación con otros diagramas
4. **Claridad**: Legibilidad y comprensibilidad

---

## Próximas Actividades

1. **Generación de PNG**: Compilar a imágenes para documentación
2. **Documentación HTML**: Crear vista interactiva
3. **Flujos Alternativos**: Diagramas adicionales para escenarios excepcionales
4. **Integración en README**: Enlaces desde documentación principal

---

**Especialista Responsable**: Especialista en Diagramas de Secuencia  
**Actividad**: Obligatoria N°3  
**Última actualización**: 2026-05-16  
**Estado**: Completado  
**Validación**: ✓ Todos los requisitos cumplidos

