# Especialista en Diagramas de Actividades - Casos de Uso 1 y 2

## Prompt utilizado con Copilot (Caso de Uso 1: Registrar Turno Médico)

Diseñar un diagrama de actividades en PlantUML para el caso de uso "Registrar Turno Médico" del Sistema de Turnos Médicos.

Contexto:

- Archivo de caso de uso: diagramas/02-casos-de-uso/02-caso-uso-registrar-turno-medico-01.puml

- Escenario: diagramas/03-escenarios-casos-de-uso/03-registrar-turno-medico-flujo-principal-01.md

Requisitos:

- Mínimo 10 actividades

- Mínimo 3 swimlanes (carriles): Paciente, Secretaria, Sistema

- Incluir inicio, fin, decisiones (if/else) y caminos alternativos

- Representar el flujo normal (turno disponible) y alternativo (sin disponibilidad)


## Output obtenido (Caso de Uso 1)

Copilot generó el siguiente diagrama base:

```plantuml
@startuml
|Paciente|
start
:Solicita turno médico;

|Secretaria|
:Recibe solicitud;
:Verifica disponibilidad en el sistema;

|Sistema|
if (¿Hay turno disponible?) then (sí)
  |Secretaria|
  :Registra el turno;
  |Sistema|
  :Asigna médico y horario;
  |Paciente|
  :Recibe confirmación del turno;
  stop
else (no)
  |Secretaria|
  :Ofrece fechas alternativas;
  :Espera confirmación del paciente;
  if (¿Acepta nueva fecha?) then (sí)
    |Sistema|
    :Registra nuevo turno;
    |Paciente|
    :Recibe confirmación;
    stop
  else (no)
    stop
  endif
endif
@enduml

## Ajustes realizados (Caso de Uso 1)

- Verifiqué que las actividades sean claras y descriptivas

- Ajusté los nombres de los carriles para que coincidan con los actores reales del sistema

- Agregué el nodo de decisión "¿Hay turno disponible?" con el camino "sí/no"

- Completé el flujo alternativo para cuando no hay disponibilidad (ofrecer fechas alternativas)

- Me aseguré de que el diagrama tenga exactamente 10 actividades principales

## Prompt utilizado con Copilot (Caso de Uso 2: Reprogramar Turno Existente)

Diseñar un diagrama de actividades en PlantUML para el caso de uso "Reprogramar Turno Existente" del Sistema de Turnos Médicos.

Contexto:
- Archivo de caso de uso: diagramas/02-casos-de-uso/02-caso-uso-reprogramar-turno-existente-02.puml
- Escenario: diagramas/03-escenarios-casos-de-uso/03-reprogramar-turno-existente-flujo-principal-01.md

Requisitos:
- Mínimo 10 actividades
- Mínimo 3 swimlanes (carriles): Paciente, Secretaria, Sistema
- Incluir inicio, fin, decisiones (if/else) y caminos alternativos
- Representar el flujo normal (reprogramación exitosa) y alternativo (sin disponibilidad)

## Output obtenido (Caso de Uso 2)
Copilot generó el siguiente diagrama base:

@startuml
|Paciente|
start
:Solicita reprogramación de turno;

|Secretaria|
:Recibe solicitud;
:Busca turno existente en el sistema;

|Sistema|
:Muestra el turno actual;
|Secretaria|
:Consulta nueva fecha/hora;
|Sistema|
:Verifica disponibilidad;

if (¿Hay disponibilidad?) then (sí)
  |Secretaria|
  :Registra nueva fecha;
  |Sistema|
  :Actualiza turno;
  |Paciente|
  :Recibe confirmación de reprogramación;
  stop
else (no)
  |Secretaria|
  :Informa que no hay disponibilidad;
  :Ofrece cancelar o mantener turno;
  if (¿El paciente cancela?) then (sí)
    |Sistema|
    :Cancela turno;
    |Paciente|
    :Recibe notificación de cancelación;
    stop
  else (no)
    stop
  endif
endif
@enduml

## Ajustes realizados (Caso de Uso 2)

- Verifiqué que todas las actividades tengan nombres claros

- Ajusté la cantidad de actividades para llegar al mínimo de 10

- Agregué la opción de cancelar turno si no hay disponibilidad (camino alternativo)

- Corregí nombres de carriles para que coincidan con la realidad del sistema

- Verifiqué que los mensajes sean consistentes con las tarjetas CRC

## Archivos de contexto referenciados

- diagramas/02-casos-de-uso/02-caso-uso-registrar-turno-medico-01.puml

- diagramas/02-casos-de-uso/02-caso-uso-reprogramar-turno-existente-02.puml

- diagramas/03-escenarios-casos-de-uso/03-registrar-turno-medico-flujo-principal-01.md

- diagramas/03-escenarios-casos-de-uso/03-reprogramar-turno-existente-flujo-principal-01.md

- herramientas-agile/tarjetas-crc/ (consultado para verificar responsabilidades de Paciente, Secretaria y Sistema)

## Iteraciones

- Primer intento: Copilot generó diagramas con menos de 10 actividades. Se completaron manualmente.

- Segundo intento: Se ajustaron los carriles para que sean exactamente 3 (Paciente, Secretaria, Sistema).

- Tercer intento: Se agregaron caminos alternativos completos para los flujos "no disponibilidad".

- Versión final: Diagramas validados con los requisitos de la consigna (10+ actividades, 3+ swimlanes, decisiones y bifurcaciones).