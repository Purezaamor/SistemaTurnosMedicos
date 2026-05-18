# Sistema de Turnos Médicos - Diseño Orientado a Objetos

---

## 📌 Datos Institucionales

- **Universidad:** UCES (Universidad de Ciencias Empresariales y Sociales)  
- **Carrera:** Tecnicatura en Programación de Sistemas  
- **Materia:** Diseño Orientado a Objetos  
- **Profesor:** Lic. Matías Velásquez  
- **Grupo:** Grupo N°3  

---

## 🧠 Introducción

El **Sistema de Gestión de Turnos Médicos** es una aplicación orientada a objetos diseñada para optimizar la administración de citas en un consultorio médico.

El sistema permite:
- A los **pacientes**, solicitar, reprogramar y cancelar turnos.  
- A los **profesionales**, organizar su agenda y visualizar citas programadas.  
- Al **personal administrativo**, gestionar la disponibilidad de consultorios y supervisar la atención.  

Incluye funcionalidades de:
- registro y asignación de turnos,
- gestión de estados de turnos (confirmado, reprogramado, cancelado),
- búsqueda de horarios disponibles y
- seguimiento de la agenda médica.  

Esto contribuye a mejorar la eficiencia del servicio y reducir tiempos de espera.

---

## 👥 Integrantes del Equipo


| Nombre y Apellido        | Matrícula | Usuario de GitHub|   
|------------------------|----------|---------------------|
| Ignacio Nervi          | 155475   | @nachonervi-design  |
| Kevin Ezequiel Sosa    | 154080   | @keviineze          |
| Alejo Guerricabeitia   | 156954   | @Purezaamor         |
| Santiago Joaquín Ferreyra   | 161304   | @ferreyrasantiagojoaquin-lab|

---


## Entregas del Proyecto

### Actividad Obligatoria N°1
- Requisitos funcionales y no funcionales.
- Casos de uso iniciales.
- Boceto inicial del diagrama de clases.

### Actividad Obligatoria N°2
- Tarjetas CRC.
- Diagramas de casos de uso.
- Escenarios de casos de uso.
- Documentación de IA por rol.

### Primer Parcial
- Aplicación de principios SOLID:
  - SRP
  - OCP
  - LSP
  - ISP
  - DIP
- Diagramas UML en PlantUML.
- Documentación del uso de Copilot Agent Mode.
- Code Reviews y coordinación del repositorio.

---

## Índices de Navegación

### Anexos
- [Anexos](./anexos/anexos.md)
- [Introducción](./anexos/introduccion.md)
- [Principios SOLID](./anexos/principios-solid/principios_solid.md)

### Diagramas
- [Índice de Diagramas UML](./diagramas/diagramasUML.md)

### Herramientas Agile
- [Herramientas Agile](./herramientas-agile/herramientas_agile.md)
- [Tarjetas CRC](./herramientas-agile/tarjetas-crc/tarjetas_crc.md)

### Inteligencia Artificial
- [IA - Diseñador de Tarjetas CRC](./ia/a2/disenador-tarjetas-crc.md)
- [IA - Modelador de Diagramas](./ia/a2/modelador-diagramas-casos-uso.md)
- [IA - Especialista en Escenarios](./ia/a2/especialista-escenarios.md)
- [IA - Documentador y Coordinador A2](./ia/a2/documentador-coordinador.md)
- [IA - Documentador y Coordinador Primer Parcial](./ia/primer-parcial/documentador-coordinador.md)
- [IA - SRP](./ia/primer-parcial/especialista-srp.md)
- [IA - OCP](./ia/primer-parcial/especialista-ocp.md)
- [IA - LSP](./ia/primer-parcial/especialista-lsp.md)
- [IA - ISP](./ia/primer-parcial/especialista-isp.md)
- [IA - DIP](./ia/primer-parcial/especialista-dip.md)
- [IA - Documentador y Coordinador A3](./ia/a3/documentador-coordinador.md)

---

## Principios SOLID Aplicados

- [Responsabilidad Única - SRP](./anexos/principios-solid/01-srp.md)
- [Abierto/Cerrado - OCP](./anexos/principios-solid/02-ocp.md)
- [Sustitución de Liskov - LSP](./anexos/principios-solid/03-lsp.md)
- [Segregación de Interfaces - ISP](./anexos/principios-solid/04-isp.md)
- [Inversión de Dependencias - DIP](./anexos/principios-solid/05-dip.md)

---

## Flujo de Trabajo

- `feature/*`: desarrollo de tareas específicas por integrante o por requisito.
- `fix/*`: correcciones rápidas y ajustes sobre ramas de entrega.
- `develop`: integración de funcionalidades aprobadas antes de preparar la entrega.
- `release/actividad-obligatoria-1`: rama de entrega de la Actividad Obligatoria N°1 donde se consolidan los cambios finales.
- `release/actividad-obligatoria-2`: rama de entrega de la Actividad Obligatoria N°2 donde se consolidan los cambios finales.
- `release/actividad-obligatoria-3`: rama de entrega de la Actividad Obligatoria N°3 donde se consolidan los cambios finales.

El trabajo se realiza mediante Pull Requests con revisión entre pares y control de versiones en GitHub, manteniendo el histórico en `changelog.md`.

---

## Diagramas de Actividades

- [Diagrama de actividad - Registrar Turno Médico](./diagramas/04-diagramas-actividades/04-actividad-registrar-turno-medico-01.png)
- [Diagrama de actividad - Reprogramar Turno Existente](./diagramas/04-diagramas-actividades/04-actividad-reprogramar-turno-existente-02.png)
- [Diagrama de Actividad - Cancelar Turno](./diagramas/04-diagramas-actividades/04-actividad-cancelar-turno-03.png)
- [Diagrama de Actividad - Visualizar Agenda Médica](./diagramas/04-diagramas-actividades/04-actividad-visualizar-agenda-medica-04.png)
- [Diagrama de Actividad - Administrar Disponibilidad del Profesional](./diagramas/04-diagramas-actividades/04-actividad-administrar-disponibilidad-05.png)

---

## Diagramas de Secuencia

- [Diagrama de Secuencia - Agendar Turno](./diagramas/05-diagramas-secuencia/05-secuencia-agendar-turno-flujo-principal-01.png)
- [Diagrama de Secuencia - Reprogramar Turno](./diagramas/05-diagramas-secuencia/05-secuencia-reprogramar-turno-flujo-principal-02.png)
- [Diagrama de Secuencia - Cancelar Turno](./diagramas/05-diagramas-secuencia/05-secuencia-cancelar-turno-flujo-principal-03.png)
- [Diagrama de Secuencia - Autorizar Sobreturno](./diagramas/05-diagramas-secuencia/05-secuencia-autorizar-sobreturno-flujo-principal-04.png)
- [Diagrama de Secuencia - Consultar Agenda Médica](./diagramas/05-diagramas-secuencia/05-secuencia-consultar-agenda-medica-flujo-principal-05.png)

---

## Uso de Inteligencia Artificial

Cada integrante documenta el uso de Copilot Agent Mode en `ia/primer-parcial/` y `ia/a3/`, indicando:

- Prompt utilizado.
- Archivos de contexto referenciados.
- Output obtenido.
- Ajustes realizados manualmente.

---

## Participación Adicional

Debido a la falta de integrantes en el equipo, el integrante **Ignacio Nervi (@nachonervi-design)** también asumió tareas correspondientes al rol de Especialista en Diagramas de Secuencia para la Actividad Obligatoria N°3.

Se realizó:
- modelado completo de diagramas de secuencia UML,
- generación de archivos `.puml` y `.png`,
- documentación del proceso utilizando IA,
- validación de participantes, mensajes y operaciones UML,
- actualización de índices y navegación,
- y revisión técnica final de consistencia y cumplimiento de requisitos.

---

## Observaciones Finales

El proyecto se desarrolló utilizando GitHub como herramienta principal de trabajo colaborativo, aplicando control de versiones, Pull Requests, Code Reviews, ramas de trabajo y registro de cambios en `changelog.md`.
