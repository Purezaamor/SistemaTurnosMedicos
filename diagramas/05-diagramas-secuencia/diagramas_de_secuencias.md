# Diagramas de Secuencia - Sistema de Turnos Médicos

## Descripción General

Este directorio contiene los diagramas de secuencia del Sistema de Turnos Médicos, desarrollados como parte de la Actividad Obligatoria N°3. Los diagramas de secuencia muestran las interacciones entre objetos en el sistema a lo largo del tiempo, especificando el orden en que ocurren los eventos.

## Diagramas Incluidos

### 1. Secuencia: Agendar Turno (Flujo Principal)
**Archivo:** `05-secuencia-agendar-turno-flujo-principal-01.puml`

Representa el flujo de interacción principal para el caso de uso "Registrar Turno Médico". Muestra cómo el Paciente, a través de la Secretaria, solicita un turno y las operaciones internas del sistema.

**Objetos involucrados:**
- Paciente
- Secretaria
- Turno
- Agenda
- Disponibilidad

---

### 2. Secuencia: Reprogramar Turno (Flujo Principal)
**Archivo:** `05-secuencia-reprogramar-turno-flujo-principal-02.puml`

Detalla la secuencia de eventos cuando se reprograma un turno existente. Incluye validaciones, búsqueda de disponibilidad alternativa y actualización del sistema.

**Objetos involucrados:**
- Paciente
- Secretaria
- Turno (actual y nuevo)
- Agenda
- Disponibilidad

---

### 3. Secuencia: Cancelar Turno (Flujo Principal)
**Archivo:** `05-secuencia-cancelar-turno-flujo-principal-03.puml`

Ilustra el proceso de cancelación de un turno, incluyendo notificaciones y actualización de la agenda médica.

**Objetos involucrados:**
- Paciente
- Secretaria
- Turno
- Agenda
- Historial

---

### 4. Secuencia: Autorizar Sobreturno (Flujo Principal)
**Archivo:** `05-secuencia-autorizar-sobreturno-flujo-principal-04.puml`

Muestra el flujo de autorización y asignación de un sobreturno cuando la agenda está completa pero existe solicitud del Médico o el Paciente.

**Objetos involucrados:**
- Paciente
- Médico
- Secretaria
- Turno
- Agenda
- Autorización

---

### 5. Secuencia: Consultar Agenda Médica (Flujo Principal)
**Archivo:** `05-secuencia-consultar-agenda-medica-flujo-principal-05.puml`

Presenta la interacción para visualizar la agenda de un médico, mostrando turnos confirmados y disponibilidad.

**Objetos involucrados:**
- Secretaria
- Médico
- Agenda
- Turno
- Disponibilidad

---

## Notación y Convenciones

Los diagramas utilizan la notación UML 2.5 para diagramas de secuencia:

- **Actores/Objetos:** Representados en la parte superior
- **Línea de vida:** Línea vertical continua bajo cada actor/objeto
- **Mensajes:** Flechas sólidas para llamadas síncronas, punteadas para retornos
- **Fragmentos combinados:** Utilizados para condicionales, alternativas y bucles
- **Notas:** Aclaraciones sobre decisiones de diseño o casos especiales

## Relación con otros Diagramas

- **Casos de Uso** (`diagramas/02-casos-de-uso/`): Define los escenarios principales que estos diagramas detallan
- **Actividades** (`diagramas/04-diagramas-actividades/`): Proporciona perspectiva del flujo de control
- **Clases** (`diagramas/01-diagrama-clases/`): Define la estructura estática de los objetos que interactúan

## Archivos Generados

Además de los archivos `.puml` en PlantUML, se generan versiones en PNG para facilitar la visualización.

---

**Especialista Responsable:** Especialista en Diagramas de Secuencia
**Actividad:** Obligatoria N°3
**Última actualización:** 2026-05-16
