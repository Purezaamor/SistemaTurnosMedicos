# Uso de IA - Especialista en Escenarios

## Prompt utilizado

```text
Analizar los requisitos del sistema de turnos médicos a partir del archivo anexos/introduccion.md.
Generar escenarios de casos de uso completos incluyendo: ID, nombre del caso de uso, actor,
área, evento activador, tipo de señal, flujo principal, flujos alternativos, precondiciones,
postcondiciones, suposiciones, requerimientos, aspectos sobresalientes, prioridad y riesgo.
```

---

## Archivos de contexto utilizados

- anexos/introduccion.md

---

## Output generado por la IA (fragmento)

Escenario: Registrar Turno  
Actor: Paciente  
Evento activador: Solicitud de turno  

Flujo principal:
1. El paciente solicita un turno
2. El sistema muestra disponibilidad
3. El paciente selecciona fecha y hora
4. El sistema registra el turno  

---

## Ajustes manuales realizados

- Se completaron todos los campos obligatorios requeridos por la consigna
- Se corrigieron nombres de escenarios para mejorar claridad
- Se agregaron flujos alternativos (cancelación, modificación, falta de disponibilidad)
- Se alinearon los escenarios con el modelo de clases definido
- Se mejoraron eventos activadores y precondiciones
- Se incorporaron prioridades y niveles de riesgo en cada escenario

---

## Iteraciones realizadas

- Iteración 1: Generación inicial de escenarios con estructura incompleta
- Iteración 2: Ajuste para incluir todos los campos obligatorios
- Iteración 3: Incorporación de flujos alternativos y validaciones de negocio
- Iteración 4: Refinamiento final para cumplir con la consigna

---

## Resultado final

Se generaron escenarios de casos de uso completos, organizados en archivos individuales dentro de:

diagramas/03-escenarios-casos-de-uso/

Se creó además un índice general:

diagramas/03-escenarios-casos-de-uso/escenarios_de_casos_de_uso.md

Cumpliendo con la estructura, contenido y nivel de detalle requerido por la actividad.