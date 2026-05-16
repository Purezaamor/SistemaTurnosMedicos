# Especialista en Diagramas de Secuencia - Actividad Obligatoria N°3

## Rol y Responsabilidades

Como Especialista en Diagramas de Secuencia, la responsabilidad es modelar las interacciones dinámicas entre objetos del Sistema de Turnos Médicos a lo largo del tiempo, utilizando la notación UML 2.5 para diagramas de secuencia.

## Objetivos

1. **Modelar interacciones**: Representar el intercambio de mensajes entre componentes del sistema
2. **Detallar flujos**: Especificar el orden temporal de eventos en cada caso de uso
3. **Validar diseño**: Confirmar que la arquitectura de clases soporta los flujos esperados
4. **Documentar comportamiento**: Proporcionar claridad sobre cómo los objetos colaboran

## Casos de Uso Asignados

Este rol cubre los cinco casos de uso principales del Sistema de Turnos Médicos:

### 1. Agendar Turno (Registrar Turno Médico)
- **Archivo**: `05-secuencia-agendar-turno-flujo-principal-01.puml`
- **Actores**: Paciente, Secretaria, Médico
- **Objetos de dominio**: Turno, Agenda, Disponibilidad
- **Propósito**: Detallar cómo se crea un nuevo turno en el sistema, verificando disponibilidad y actualizando la agenda

**Secuencia simplificada**:
1. Paciente solicita turno a Secretaria
2. Secretaria consulta disponibilidad del médico
3. Se selecciona fecha/hora disponible
4. Se crea Turno y se registra en Agenda
5. Se libera slot de Disponibilidad

---

### 2. Reprogramar Turno
- **Archivo**: `05-secuencia-reprogramar-turno-flujo-principal-02.puml`
- **Actores**: Paciente, Secretaria, Médico
- **Objetos de dominio**: Turno, Agenda, Disponibilidad
- **Propósito**: Especificar cómo se modifica un turno existente a una nueva fecha

**Secuencia simplificada**:
1. Paciente solicita cambio de turno existente
2. Se busca el turno actual
3. Se consulta disponibilidad para nueva fecha
4. Se actualiza Turno con nueva información
5. Se liberan slots anteriores en Disponibilidad
6. Se ocupan slots nuevos en Disponibilidad

---

### 3. Cancelar Turno
- **Archivo**: `05-secuencia-cancelar-turno-flujo-principal-03.puml`
- **Actores**: Paciente, Secretaria, Médico
- **Objetos de dominio**: Turno, Agenda, Disponibilidad, Historial
- **Propósito**: Modelar la eliminación de un turno con registro en historial

**Secuencia simplificada**:
1. Paciente solicita cancelación
2. Se busca y valida el turno
3. Se marca Turno como CANCELADO
4. Se registra en Historial
5. Se libera slot en Disponibilidad
6. Se elimina de Agenda

---

### 4. Autorizar Sobreturno
- **Archivo**: `05-secuencia-autorizar-sobreturno-flujo-principal-04.puml`
- **Actores**: Paciente, Secretaria, Médico
- **Objetos de dominio**: Turno, Agenda, Autorización
- **Propósito**: Detalle del flujo cuando se debe asignar un sobreturno con aprobación del médico

**Secuencia simplificada**:
1. Agenda completa, se ofrece sobreturno
2. Paciente acepta
3. Se solicita autorización a Médico
4. Médico autoriza
5. Se crea Turno especial como SOBRETURNO
6. Se registra en Agenda

---

### 5. Consultar Agenda Médica
- **Archivo**: `05-secuencia-consultar-agenda-medica-flujo-principal-05.puml`
- **Actores**: Secretaria, Médico
- **Objetos de dominio**: Agenda, Turno, Disponibilidad
- **Propósito**: Mostrar cómo se visualiza la agenda completa de un médico

**Secuencia simplificada**:
1. Secretaria o Médico solicita ver agenda
2. Sistema recupera turnos confirmados
3. Sistema obtiene disponibilidad
4. Se presenta información completa

---

## Consideraciones de Diseño

### Patrones Utilizados

- **Separation of Concerns**: Cada objeto tiene responsabilidades claras en la secuencia
- **Information Expert**: Los objetos responden a mensajes relacionados con su responsabilidad
- **Dependency Injection**: El SistemaAgendamiento coordina sin depender directamente de detalles internos

### Validaciones y Precondiciones

- La disponibilidad debe existir antes de agendar
- Un turno debe existir para ser reprogramado o cancelado
- Los sobreturno requieren validación especial
- Se debe mantener integridad de la agenda

### Flujos Alternativos y Excepciones

Los diagramas se enfocan en flujos principales (happy path). Flujos alternativos incluyen:
- Cancellación de turno cuando no existe
- Solicitud de sobreturno cuando hay disponibilidad
- Reprogramación a misma fecha (no permitida)

---

## Relación con otros Componentes

### Diagrama de Clases
Los diagramas de secuencia validan que las clases definidas en `diagramas/01-diagrama-clases/` pueden sostener estas interacciones. Las colaboraciones implican:
- Métodos en Turno, Agenda, Disponibilidad, etc.
- Visibilidad y accesibilidad entre objetos
- Responsabilidades distribuidas

### Diagramas de Casos de Uso
Los diagramas de secuencia detallan el "cómo" de cada caso de uso definido en `diagramas/02-casos-de-uso/`.

### Diagramas de Actividades
Proporcionan perspectiva de flujo de control paralelo a esta perspectiva de colaboración temporal.

---

## Notación UML 2.5 para Diagramas de Secuencia

### Elementos Principales

| Elemento | Símbolo | Significado |
|----------|---------|------------|
| Actor/Objeto | Rectángulo en la parte superior | Participante en la interacción |
| Línea de vida | Línea vertical punteada | Existencia del objeto en el tiempo |
| Mensaje síncrono | Flecha sólida → | Llamada de método |
| Retorno | Flecha punteada ← | Valor de retorno |
| Mensaje asíncrono | Flecha abierta | Mensaje no bloqueante |
| Fragmento alt | Marco con etiqueta | Condicional (if-else) |
| Fragmento loop | Marco con etiqueta | Repetición |
| Nota | Rectángulo con esquina doblada | Comentario adicional |

### Convenciones del Proyecto

- Numeración automática con `autonumber`
- Nombres descriptivos en formato: `05-secuencia-[descripcion]-flujo-principal-[numero].puml`
- Uso de notas para aclaraciones importantes
- Indentación clara de fragmentos combinados

---

## Próximos Pasos y Mejoras

1. **Generación de PNG**: Compilar diagramas PlantUML a PNG para visualización en documentación
2. **Validación cruzada**: Verificar consistencia entre secuencias, casos de uso y diagrama de clases
3. **Flujos alternativos**: Desarrollar diagramas para escenarios excepcionales (cuando sea requerido)
4. **Actualización de índices**: Vincular desde `diagramas/diagramasUML.md`

---

**Especialista Responsable**: Especialista en Diagramas de Secuencia  
**Actividad**: Obligatoria N°3  
**Última actualización**: 2026-05-16  
**Estado**: En desarrollo
