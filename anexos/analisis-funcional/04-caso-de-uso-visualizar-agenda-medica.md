# Análisis Funcional - Caso de Uso 4: Visualizar Agenda Médica

## Descripción del caso de uso y trazabilidad con requisitos funcionales

**Actor:** Médico

**Flujo principal:**
1. El médico solicita ver su agenda para una fecha específica.
2. El sistema consulta los turnos asignados para esa fecha.
3. El sistema muestra los horarios ocupados y libres.

**Flujos alternativos:**
- Si no hay turnos, se muestra mensaje informativo.

**Trazabilidad con RFs (A1):**
- **RF4 (Visualización de agenda):** El caso de uso permite al médico consultar su agenda.

## Diagrama de casos de uso (A2)

![Diagrama de casos de uso - Visualizar Agenda Médica](../../diagramas/02-casos-de-uso/02-caso-uso-visualizar-agenda-medica-04.png)

## Diagrama de actividades (A3)

![Diagrama de actividades - Visualizar Agenda Médica](../../diagramas/04-diagramas-actividades/04-actividad-visualizar-agenda-medica-04.png)

## Diagrama de secuencia (A3)

![Diagrama de secuencia - Visualizar Agenda Médica](../../diagramas/05-diagramas-secuencia/05-secuencia-consultar-agenda-medica-flujo-principal-05.png)

## Diagrama de clases (CU4)

![Diagrama de clases - Visualizar Agenda Médica](../../diagramas/01-diagrama-clases/04-clases-visualizar-agenda-medica-04.png)

## Pseudocódigo del caso de uso

ControladorAgenda controlador = new ControladorAgenda()
Date fecha = new Date("2026-06-15")
List<Turno> listaTurnos = controlador.obtenerTurnos(fecha)
if (listaTurnos.size() > 0) {
PantallaAgenda.mostrarAgenda(listaTurnos)
} else {
mostrar("No hay turnos para la fecha seleccionada")
}

text
